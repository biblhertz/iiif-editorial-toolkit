# IIIF Manifest Pipeline
## Documentation for Editorial Staff and Developers

---

## Overview

This pipeline converts a JATS XML article file into a IIIF Presentation API 3.0 manifest in a single automated pass. It is designed for use with articles published by the Bibliotheca Hertziana and compatible institutions whose images are served from a IIIF image server.

The pipeline consists of three files:

| File | Role |
|---|---|
| `xml-to-manifest.py` | Main script — do not edit |
| `manifest_config.json` | Configuration — editors set values here |
| `fig-extractor.py` | Optional audit tool — exports a CSV of all figures |

---

## Requirements

- Python 3.8 or later (no external libraries required)
- Network access to the IIIF image server during execution
- A JATS XML article file with `<fig>` elements in the `<body>`

---

## Quick Start

1. Place `xml-to-manifest.py` and `manifest_config.json` in the same folder as your XML file(s).
2. Edit `manifest_config.json` with the correct values for your volume/journal (see Configuration below).
3. Open a terminal in that folder and run:

```bash
# One article
python xml-to-manifest.py article.xml output.json

# A whole volume — every article XML in a folder, one manifest per article out
python xml-to-manifest.py volume_folder/ output_folder/
```

---

## Configuration (`manifest_config.json`)

Editors should only ever modify this file. Per-article values (manifest URL, canvas base, title) are auto-derived from each XML file — the config holds only what's shared across a whole volume/journal plus the base URL pattern.

```json
{
  "base_url":          "https://your-server.example/iiif_manifests",
  "primary_lang":      "it",
  "rights":            "http://creativecommons.org/licenses/by/4.0/",
  "required_stmt_it":  "Name of the institution (Italian)",
  "required_stmt_en":  "Name of the institution (English)",
  "fetch_delay":       0.3,
  "fallback_width":    1000,
  "fallback_height":   1000
}
```

### Required keys

| Key | Description | Example |
|---|---|---|
| `rights` | Rights statement URI. `creativecommons.org`/`rightsstatements.org` URIs are normalized to `http://` automatically (IIIF's recognized rights vocabularies are canonically `http://`, even though the sites redirect to https) — paste either scheme, the output is always correct. | `"http://creativecommons.org/licenses/by/4.0/"` |
| `required_stmt_it` | Attribution text in Italian | `"Nome dell'istituzione..."` |
| `required_stmt_en` | Attribution text in English | `"Institution name..."` |
| `base_url` | Base URL manifests are published under — used to derive each article's `manifest_id`/`base_canvas` from its filename. Not needed if you provide `manifest_id`/`base_canvas` explicitly (single-article mode only). | `"https://your-server.example/iiif_manifests"` |

### Optional keys

| Key | Default | Description |
|---|---|---|
| `primary_lang` | `"it"` | Language code the auto-derived `<article-title>` is filed under |
| `fetch_delay` | `0.3` | Seconds to wait between `info.json` requests. Increase if the server rate-limits. |
| `fallback_width` | `1000` | Canvas width used if `info.json` cannot be reached |
| `fallback_height` | `1000` | Canvas height used if `info.json` cannot be reached |

### Manual overrides (single-article mode only)

Set these to bypass auto-derivation for one article — e.g. a one-off manifest that doesn't follow the volume's usual URL/filename pattern:

| Key | Description |
|---|---|
| `manifest_id` | Explicit public URL of the manifest file (must be paired with `base_canvas`) |
| `base_canvas` | Explicit base URL for canvas/annotation IDs (must be paired with `manifest_id`) |
| `label_it` | Manifest title in Italian, used verbatim instead of the JATS title |
| `label_en` | Manifest title in English, used verbatim instead of the JATS title |

> **Note:** If any required key is missing the script will exit immediately with a clear error message before making any network requests.

---

## Auto-derivation

Per article, unless overridden above:

- **`manifest_id` / `base_canvas`** — built from `base_url` + the XML filename stem, e.g. `article-042.xml` → `{base_url}/article-042.json` and `{base_url}/article-042`. This means the XML filename *is* the manifest slug — rename the file if you need a different published URL.
- **`label`** — taken from `<title-group><article-title>`, filed under `primary_lang` — unless the article's own root declares `<article xml:lang="…">`, which wins over the config default (e.g. one French article in an otherwise English volume gets filed under `fr`, not `en`). A second language is added **only** if the JATS file itself carries a `<trans-title-group xml:lang="…"><trans-title>` — no title is ever duplicated into a language that isn't actually present in the source. So a genuinely bilingual article gets a bilingual label automatically; a monolingual one gets a single-language label, not a fabricated second one.

---

## Command Line Usage

```bash
# Single article — minimal
python xml-to-manifest.py article.xml

# Single article — explicit output filename
python xml-to-manifest.py article.xml my_output.json

# Single article — custom config file (e.g. for a different journal or institution)
python xml-to-manifest.py article.xml my_output.json my_config.json

# Whole volume — one XML per article in a folder, one manifest per article out
python xml-to-manifest.py volume_folder/ output_folder/
python xml-to-manifest.py volume_folder/ output_folder/ my_config.json
```

Batch mode processes every `.xml` file in the folder. Files with no `<body>` (e.g. a `volume-meta.xml`) are recognized as non-articles and skipped automatically; files with a `<body>` but no derivable title are reported and skipped rather than aborting the run. An article that produces zero canvases — no `<fig>` elements at all, or figures with no usable online image URL — is also reported and **no manifest file is written for it**, in either single-article or batch mode; an empty manifest isn't a useful output.

---

## What the Script Does

For each `<fig>` element found in the article `<body>`:

1. **Extracts** the figure ID, label, caption title, full caption text, and any external handle URL.
2. **Locates the IIIF image URL** using the following priority order:
   - A `<graphic specific-use="online">` inside `<alternatives>` ← Hertziana standard
   - Any `<graphic>` with an `https://` URL inside `<alternatives>`
   - Any `<graphic>` with an `https://` URL directly on `<fig>` ← simple JATS files
3. **Derives the IIIF service ID** by stripping the request suffix (`/full/max/0/default.jpg`) from the image URL.
4. **Fetches real image dimensions** from the service's `info.json` endpoint.
5. **Builds a IIIF Canvas** with the correct label, dimensions, painting annotation, thumbnail, summary, and `seeAlso` link (where a handle URL is present in the caption).

---

## JATS `<fig>` Structure

The script supports three `<graphic>` arrangements:

**1. Hertziana standard — `<alternatives>` with `specific-use`**
```xml
<fig id="fig-001" fig-type="content-image">
  <label>Figure 1.</label>
  <caption>
    <title>Artist Name, Work Title...</title>
    <p>Source: Institution Name
      <ext-link ext-link-type="uri"
        xlink:href="http://hdl.handle.net/example/handle-id">...</ext-link>
    </p>
  </caption>
  <alternatives>
    <graphic specific-use="online"
             xlink:href="https://iiif.example.org/image-id/full/max/0/default.jpg"/>
    <graphic specific-use="archival" xlink:href="article-id_01.jpg"/>
  </alternatives>
</fig>
```

**2. `<alternatives>` without `specific-use`**
```xml
<alternatives>
  <graphic xlink:href="https://iiif.example.org/image-id/full/max/0/default.jpg"/>
  <graphic xlink:href="local-file.tif"/>
</alternatives>
```
The first `https://` URL is used; local paths are ignored.

**3. Direct `<graphic>` on `<fig>` (simple JATS)**
```xml
<fig id="fig1">
  <label>Figure 1.</label>
  <caption>...</caption>
  <graphic xlink:href="https://iiif.example.org/image-id/full/max/0/default.jpg"/>
</fig>
```

---

## Output Manifest Structure

The output is a IIIF Presentation API 3.0 manifest with:

- One **Canvas** per figure, sized to the real pixel dimensions of the image
- **Canvas label** combining figure number and caption title: `Figure 1. — Artist Name, Work Title...`
- **Summary** containing the full flattened caption text
- **Thumbnail** at 300px width via the IIIF image API
- **`rights`** at canvas level, set from the licence URL in the caption (`creativecommons.org` or `rightsstatements.org`) when present — overrides the manifest-level default for that figure. Figures with no per-image licence inherit the manifest-level `rights` from the config.
- **`seeAlso`** link to the source or credit URL found in the caption (Wikimedia, HDL handle, Census, etc.), where present
- **`rights`** and **`requiredStatement`** set at manifest level from the config

---

## Console Output

During execution the script prints a progress line for each figure:

```
✓ article-id_01.jp2  3456×4800
✓ article-id_02.jp2  2800×3200
⚠ article-id_03.jp2: HTTP 503 — using 1000×1000
...
✓ Manifest written → article-id.json
  45 canvases, 0 skipped
```

Warnings are printed for:
- Figures with no online/IIIF graphic URL (skipped from manifest)
- `info.json` fetch failures (fallback dimensions used, canvas still included)
- Duplicate `fig` IDs in the source XML

---

## Optional: Figure Audit CSV (`fig-extractor.py`)

If you need to review or spot-check the figure data before generating the manifest, run the standalone extractor first:

```bash
python fig-extractor.py article.xml fig_audit.csv
```

This writes a CSV with one row per figure and the following columns:

| Column | Content |
|---|---|
| `position` | Order of appearance in the body |
| `id` | `fig` element ID attribute |
| `fig_type` | `fig-type` attribute if present |
| `label` | Flattened `<label>` text |
| `cap_title` | Flattened `<caption><title>` text |
| `cap_text` | Full flattened caption |
| `handle` | Source or credit URL from `<ext-link>` in caption (Wikimedia, HDL, Census, etc.) |
| `licence` | Licence URL from `<ext-link>` in caption (`creativecommons.org` or `rightsstatements.org`); empty if the figure inherits the manifest-level rights |
| `online_url` | Full IIIF image URL |
| `service_id` | Derived IIIF service base URL |
| `archival` | Local filename from `specific-use="archival"` |

The CSV can be opened in Excel or any spreadsheet application for editorial review before the manifest is generated.

---

## Fetching image dimensions from internal servers

By default the script fetches image dimensions by querying each image's
`info.json` endpoint over HTTPS. If your IIIF image server is only reachable
internally (e.g. via a `/etc/hosts` entry or an internal DNS name), HTTPS
certificate validation will fail and the request will time out or error.

To handle this, add the optional `force_http_hosts` key to your
`manifest_config.json`:

```json
"force_http_hosts": ["images.example.org"]
```

Any hostname listed there will be contacted over HTTP instead of HTTPS
**for the `info.json` dimension fetch only**. The URLs written into the
manifest itself are always taken verbatim from the XML source and are not
modified — so the published manifest will still reference the correct
public HTTPS addresses that viewers use.

Multiple internal hostnames can be listed:

```json
"force_http_hosts": ["internal-cantaloupe.example.org", "images-dev.example.org"]
```

If the key is absent from the config file entirely, the script behaves as
before and uses HTTPS for all requests. No changes to existing config files
are required.

---

## Troubleshooting

**`✗ Config file not found`**
The script cannot find `manifest_config.json`. Make sure the config file is in the same folder as the script, or pass its path explicitly as the third argument.

**`✗ Config is missing required keys`**
A required key has been deleted or misspelled in the config. Check the key names against the Required keys table above.

**Figures skipped with `no online URL`**
The `<graphic>` in those figures has a local path rather than an `https://` URL. The image needs to be uploaded to the IIIF server first and the XML updated before re-running.

**Dimensions showing as `1000×1000`**
The `info.json` fetch failed for that image — network issue, server downtime, or an incorrect service URL in the XML. Check the URL printed in the warning, then re-run once the server is reachable. The `fetch_delay` value in the config can be increased if the server is rate-limiting requests.

**Manifest loads in viewer but images are blank**
The IIIF service URL is correct but the image server requires authentication or is not publicly accessible. Verify the image is publicly reachable by opening the `online_url` value directly in a browser.
