# IIIF Manifest and Comparison Generator — User Guide

A self-contained, single-file HTML tool for generating IIIF Presentation 3 manifests and structured image comparison layouts. No installation, no server, no internet connection required to run — open the file in any modern browser.

---

## Overview

The tool has five tabs:

| Tab | Purpose |
| --- | --- |
| Individual Images | Generate a single-image manifest with full metadata |
| Comparison Layouts | Build a multi-image manifest from selected library items |
| Layer Alignment | Position images on a shared canvas and export as a layered manifest |
| Manifest Library | Manage, edit, export, and import your manifest collection |
| Validation & Testing | Check any manifest for IIIF compliance and open it in viewers |

All data is stored in your browser's `localStorage`. Use **Export library** regularly to back up your work as a JSON file. Working sessions in the Comparison Layouts and Layer Alignment tabs are also persisted automatically and survive page reloads.

---

## Individual Images

### 1. Provide the image URL

Paste a full IIIF Image API URL into the **IIIF Image URL** field, for example:

```text
https://fotothek.biblhertz.it/iiif/3/dpub%2Fhsah0410%2Fhsah_0410_09.jp2/full/max/0/default.jpg
```

The tool automatically derives the **Service ID** (the base URL before the four IIIF request parameters) and fetches the image dimensions and a thumbnail preview from the server's `info.json`. If the fetch fails due to CORS or network issues, enter the service ID and dimensions manually and click **Retry fetch**.

### 2. Language settings

Select the **primary language** from the dropdown. Optionally click **+ Second language** to add a second set of title and description fields. Language codes follow BCP47 and appear as the keys in the manifest's `label` and `summary` objects.

### 3. Metadata fields

| Field | Notes |
| --- | --- |
| Title | Required. Used as manifest label and canvas label. Also drives the auto-generated manifest ID. |
| Description | Becomes the manifest `summary`. |
| Artist, Date, Institution | Written into the manifest `metadata` array. |
| Rights / License | Dropdown of common Creative Commons URIs (CC0 through CC BY-NC-ND 4.0) plus InC and a Custom URL option. Written as the manifest `rights` property (a URI). |

### 4. Manifest ID and Base URL

The **Manifest ID** is auto-generated as a 12-character SHA-256 hash of the title. It is editable — type a custom value to override. Together with the **Base URL**, it forms the manifest's `id`:

```text
https://username.github.io/my-manifests/a3f5b2c9d1e8.json
```

Set the Base URL to wherever you will serve the JSON file (see the [GitHub Pages guide](./github_pages_guide.md)).

### 5. Generate and save

Click **Generate Manifest** to produce the JSON. The generated code appears in a panel below the button. Click the **▼/▶ toggle** on the panel header to collapse or expand the code block. The JSON is syntax-highlighted: keys, string values, numbers, and booleans are shown in distinct colours. Then:

- **Download JSON** to save the file locally.
- **Publish** to push the manifest directly to GitHub Pages or a manifest server (see [Publishing manifests](#publishing-manifests)).
- **Save to Library** to add it to the manifest library for use in comparisons.

---

## Manifest Library

The library stores all individually generated and imported image records. It persists in `localStorage` until you clear the browser or use **Export library** to save it externally.

### Structure

Items are grouped by the source they were imported from. Each group shows the source manifest label, a thumbnail of the first image, and the item count. Click the arrow to expand a group and see individual items. Locally generated items appear below all groups under a **Generated in this tool** heading.

### Per-item actions

- **Edit** — opens an inline form to update title, artist, date, institution, description, and rights. Changes are written back to localStorage immediately on save.
- **Download** — generates and downloads a manifest for this item. For single-image items (individually generated or imported), the manifest is always built fresh from the stored metadata using the Base URL currently set in the Individual Images tab — so the downloaded file reflects your current server, not the one used when the item was first saved. If no Base URL is set, `https://example.org/manifests` is used as a placeholder so the file is always valid JSON. For comparison and layer alignment items, the stored manifest is downloaded as-is.
- **Publish** — publishes the manifest directly to GitHub Pages or a manifest server and returns a public URL (see [Publishing manifests](#publishing-manifests)).
- **Duplicate** — creates a copy of the item with a "Copy of …" title and a new auto-generated manifest ID. Useful for creating variants (different rights, metadata, or cropped URL) without re-filling all the fields from scratch.
- **Copy URL** — copies the manifest URL (`baseUrl/id.json`) to the clipboard. Requires the Base URL to be set in the Individual Images tab.
- **Delete** — removes the item from the library.

### Group actions

- Expand/collapse — click the arrow on a group header.
- **Delete all** — removes all items in the group. Clicking the button shows an inline confirmation with three options: **Save JSON & delete** (downloads the group as a JSON file first), **Delete anyway**, or **Cancel**.

### Export and import

**Export library** downloads the entire library as a single JSON file. **Import library** merges a previously exported file into the current library, skipping duplicates. Use this to transfer your library between browsers or machines.

Exported libraries are server-independent — no Base URL is stored in the library file. When another user imports the library and clicks Download on an item, the manifest is generated using their own Base URL. This makes it safe to share libraries across institutions or team members working on different servers.

### Generate Collection Manifest

At the bottom of the Library tab, a dedicated section generates a IIIF Collection manifest listing all library items. Enter a title, choose a language, and set the Base URL to wherever you publish your manifests (for example your GitHub Pages URL). Click **Generate Collection**. The JSON appears in a collapsible panel with a **▼/▶ toggle** on the header; the code is syntax-highlighted (keys, strings, numbers, and booleans in distinct colours). Click **Download collection.json** to save it.

Upload this file alongside your individual manifests and share the single collection URL — any IIIF viewer that supports Collections (Mirador 3, Universal Viewer) will present the full set as a browseable library. Each entry includes a thumbnail drawn from the image server. A **Publish** button is available alongside **Download collection.json** to push the collection directly to your configured destination.

See the [GitHub Pages guide](./github_pages_guide.md) for the complete publishing workflow.

---

## Comparison Layouts

### Step 1 — Collect images

**From library:** Check individual items or use the group checkbox (selects all items in that group at once) in the top section, then click **Import selected**.

**From manifest:** Paste a manifest URL or JSON in the lower section and click **Import into library**. The manifest is parsed (IIIF v2 and v3 are both supported), images are extracted with their labels, descriptions, service IDs, dimensions, image-server profile, and per-canvas rights (if the source manifest sets one — otherwise it's left blank rather than assumed), and added to the library grouped under the source manifest. Select them for comparison from the library section above.

When extracting labels, the tool detects generic canvas labels (`Canvas 34`, `folio 12v`, `p. 3`) and promotes the canvas `summary` or `description` instead — useful for article figure manifests where the caption lives in the description field.

### Step 2 — Arrange images

After importing, images appear in the **Selected for comparison** list. Use the arrows to reorder them. Select a layout from the **Layout Type** dropdown:

| Layout | Best for |
| --- | --- |
| Horizontal Row | Side-by-side, natural aspect ratios |
| Horizontal Row (Balanced Heights) | All images scaled to the same height |
| Storyboard | Viewing presentation, landscape canvases |
| Main + Derivatives (1+N) | One primary image with detail crops below |
| 2×2 Grid | Four-image systematic comparison |
| Vertical Stack | Chronological sequences, portrait images |

For opacity/curtain comparison of images stacked on the same canvas, use the **Layer Alignment** tab, which provides full per-layer positioning and metadata.

The **Layout preview** renders immediately. Drag any image placeholder to reposition it freely. A click without movement (under 2 px) selects the image and opens the coordinate editor for precise numeric control. Activate **Advanced layout settings** to adjust padding and access the coordinate editor. The coordinate editor exposes X, Y, W, and H fields; tick **Lock W/H to original image proportions** to constrain width and height to the image's native aspect ratio when either field is changed.

### Step 3 — Manifest details

Set the title, optional description, language(s), and Base URL for the comparison manifest.

When the layout is not Layered Overlay, choose the **target viewer**:

| Option | Output | Use when |
| --- | --- | --- |
| Universal | Single canvas, images positioned with `#xywh` fragments | Mirador 3, TheseusViewer — supports zooming across the full composition |
| Simple Manifest | Multiple canvases, one per image | Any IIIF viewer, browseable sequence |
| Dual Output | Both of the above | Unknown target viewer, maximum compatibility |

For Layered Overlay the target viewer selector is hidden — the output is always a single canvas with all images listed as painting annotations targeting the full canvas area.

Click **Create comparison manifest** to generate. The JSON appears in a collapsible panel with a **▼/▶ toggle** on the header; the code is syntax-highlighted (keys, strings, numbers, and booleans in distinct colours). Download, **Publish**, or copy the JSON output. Click **Save to library** to store the generated manifest in the Manifest Library — it will appear under the group **Comparison layout** and can be included in a collection manifest.

**Session persistence:** The entire comparison workspace — selected images, their positions, layout type, title, description, language, and Base URL — is saved automatically to `localStorage` and restored when you return to the tab or reload the page. Click **Clear all** to reset the working set and discard the saved session.

---

## Layer Alignment

Use this tab to position images of different sizes on a shared canvas and export the result as a positioned IIIF manifest. The primary use case is reintegrating details — for example, placing a missing illumination back onto its host page from an incunabulum — where images do not share the same dimensions.

**Session persistence:** The layer workspace — all layers with their positions, sizes, opacity values, and metadata — is saved automatically to `localStorage` and restored when you return to the tab or reload the page. Click **Clear workspace** to remove all layers and discard the saved session.

### Step 1 — Add layers

**From library:** Check items in the grouped library list and click **Import selected**. The library groups and expand/collapse behaviour are the same as in the Comparison Layouts tab.

**By URL:** Paste a IIIF Image URL or bare service ID and click **Add layer**. If the image dimensions cannot be fetched automatically, a manual entry form appears — enter width and height and click **Add**.

Each added layer appears in the layer list in Step 2 with a colour-coded label. To quickly set every layer to fill the entire canvas (the typical starting point for an opacity comparison), click **Snap all to canvas** at the top of Step 2. Conversely, **Fit canvas to layers** resizes the canvas to exactly contain every current layer and shifts them so nothing sits outside it — useful after rotating a layer near the canvas edge, since rotation can grow a layer's footprint past the original bounds.

### Step 2 — Arrange in the canvas workspace

The workspace shows a scaled-down representation of the canvas. The canvas is sized automatically to the first layer's native image dimensions when you add it.

**Moving:** Drag a layer thumbnail on the canvas to reposition it. The layer's top-left corner coordinates are shown in the layer panel.

**Resizing:** Drag any of the four corner handles (shown on the selected layer) to resize the image area on the canvas. Hold **Shift** while dragging to lock the original aspect ratio.

**Selecting:** Click a layer on the canvas or in the layer panel to select it. The selected layer shows a dashed ring and resize handles.

**Keyboard:** With a layer selected, use the arrow keys to nudge it one pixel at a time (hold Shift for 10 px). Press Delete to remove the selected layer.

**Opacity:** Each layer has an opacity slider in the panel. Use it to check alignment by making the top layer semi-transparent.

**Reordering:** Use the ↑ / ↓ arrows in the layer panel to change the painting order. Lower items in the list are painted first (bottom of the stack).

**Per-layer metadata:** Each layer has collapsible fields for title, description, date, institution, and rights. These are embedded in the exported manifest so viewers can name and describe individual layers.

**Rotate:** The panel header contains ↺ (counter-clockwise 90°) and ↻ (clockwise 90°) buttons, plus a numeric input for arbitrary integer rotation from 0 to 359°. Rotating a layer resizes its on-canvas footprint to the true rotated bounding box (larger than the original at any angle other than 0°/180°) while keeping the layer centered on the same spot — the box grows around the image rather than shifting away from it. The **Natural size** button resets the layer to its true rotated-native size at the current angle.

**Flip/mirror:** The ↔ button in the panel header toggles horizontal mirroring. The button is highlighted in blue when mirroring is active. Mirror is applied before rotation, following the IIIF Image API `!` parameter convention.

**Canvas zoom:** Once at least one layer has been added, `−`, `+`, and `Fit` buttons appear in the canvas size row. The scroll wheel on the canvas also zooms. 100% corresponds to fit-to-window; zooming in enables scrolling within the workspace. The current zoom level is persisted in the session and restored on reload.

**Undo:** Press **Ctrl+Z** (or **Cmd+Z** on Mac) to undo the last operation. Up to 20 steps are stored. Undo covers moves, resizes, rotations, flips, deletes, stack reorders, snaps, and canvas resizes. The undo history is not persisted across page reloads — session state (layer positions, sizes, etc.) is restored, but the undo stack is not.

### Step 3 — Export manifest

Enter a title for the manifest, select the language, and set the Base URL. Click **Generate manifest** to produce the JSON. The output appears in a collapsible panel with a **▼/▶ toggle** on the header; the code is syntax-highlighted (keys, strings, numbers, and booleans in distinct colours). Click **Download** to save it, **Publish** to push it directly to your configured destination, or **Save to library** to store it in the Manifest Library — it will appear under the group **Layer alignment** and can be included in a collection manifest.

**How coordinates map to IIIF:** Each layer that exactly covers the full canvas (position 0,0, same dimensions) is written as a painting annotation targeting the bare canvas ID. Layers positioned or sized differently are written with a `#xywh=x,y,w,h` fragment target. This means a full base image and a smaller positioned detail can coexist correctly in any IIIF viewer.

Per-layer metadata (`label`, `summary`, `rights`, `metadata`) is embedded on each annotation body. Viewers such as Mirador 3 with the image-tools plugin use the annotation `label` to name each layer in the opacity panel.

---

## Validation and Testing

Paste a manifest URL or JSON and click **Validate manifest** for a line-by-line compliance check covering context, identity, type, label, canvas structure, and painting annotation targets. Click **Test viewer compatibility** to get direct links to open the manifest in Mirador 3, TheseusViewer, and Universal Viewer (requires network access to those services).

---

## Publishing manifests

Every output section — Individual Images, Comparison Layouts, Layer Alignment, Collection, and per-Library-item — has a teal **Publish** button next to the Download button. Clicking it sends the manifest JSON directly to your configured destination and shows a success notice with the public URL and a **Copy URL** button.

### Configure a publish destination

Click **⚙ Publish settings** in the top-right corner of the tool header. The modal offers two destinations; configure one or both.

#### GitHub Pages

A free, CORS-enabled static file host. Suitable for anyone without a manifest server.

| Field | Value |
| --- | --- |
| Personal Access Token | A GitHub PAT with `repo` scope — see [GitHub Pages guide](./github_pages_guide.md) for step-by-step creation instructions. |
| Repository | Your repository as `username/iiif-manifests`. |
| Branch | The branch GitHub Pages is deployed from (usually `main`). |

#### Manifest Server

A custom server with a `POST /api/manifests` endpoint.

| Field | Value |
| --- | --- |
| Server URL | Base URL of the server, e.g. `https://example.org`. |
| API Token | Optional bearer token sent as `Authorization: Bearer {token}`. |

Select **Default destination** to choose which one the Publish button uses. If you configure only one destination it is used automatically.

Saving settings auto-fills all Base URL fields (Individual Images, Comparison, Layer Alignment, Collection) with the appropriate public URL, so newly generated manifests will have correct `id` values without further configuration.

### What happens when you publish

1. The manifest JSON is taken from the current output panel (the same content as Download).
2. For GitHub Pages: the file is PUT to the GitHub Contents API. If the file already exists it is updated in place (the existing SHA is fetched first). The public URL is `https://username.github.io/repo/filename.json`.
3. For a manifest server: the JSON is POSTed to `{Server URL}/api/manifests`. The server is expected to return `{ "url": "…" }` with the public URL; if absent the tool constructs `{Server URL}/filename.json` as a fallback.
4. A dismissible notice appears with the URL and a **Copy URL** button. The notice stays for 15 seconds.

GitHub Pages has a propagation delay of up to 60 seconds after the first publish to a repository. Subsequent updates are usually faster.

---

## Manifest structure reference

### Individual manifest (IIIF Presentation 3)

```json
{
  "@context": ["http://iiif.io/api/presentation/3/context.json"],
  "id": "https://username.github.io/manifests/a3f5b2c9.json",
  "type": "Manifest",
  "label": { "it": ["Title in Italian"], "en": ["Title in English"] },
  "summary": { "it": ["Description"] },
  "rights": "https://creativecommons.org/licenses/by/4.0/",
  "metadata": [
    { "label": {"en": ["Artist"], "it": ["Artista"]}, "value": {"none": ["Name"]} }
  ],
  "items": [{
    "id": "…/canvas/1",
    "type": "Canvas",
    "width": 4200,
    "height": 5600,
    "items": [{
      "id": "…/page/1",
      "type": "AnnotationPage",
      "items": [{
        "id": "…/annotation/1",
        "type": "Annotation",
        "motivation": "painting",
        "target": "…/canvas/1",
        "body": {
          "id": "https://imageserver.org/iiif/3/identifier/full/max/0/default.jpg",
          "type": "Image",
          "format": "image/jpeg",
          "service": [{
            "id": "https://imageserver.org/iiif/3/identifier",
            "type": "ImageService3",
            "profile": "level2"
          }]
        }
      }]
    }]
  }]
}
```

### Comparison manifest — Universal (single canvas)

```json
{
  "@context": ["http://iiif.io/api/presentation/3/context.json"],
  "id": "https://username.github.io/manifests/comparison-universal-….json",
  "type": "Manifest",
  "label": { "en": ["Comparison title"] },
  "items": [{
    "id": "…/canvas/layout",
    "type": "Canvas",
    "width": 1600,
    "height": 700,
    "items": [{
      "type": "AnnotationPage",
      "items": [
        {
          "type": "Annotation",
          "motivation": "painting",
          "body": { "id": "…image1…", "type": "Image", "service": [{}] },
          "target": "…/canvas/layout#xywh=100,50,680,450"
        },
        {
          "type": "Annotation",
          "motivation": "painting",
          "body": { "id": "…image2…", "type": "Image", "service": [{}] },
          "target": "…/canvas/layout#xywh=820,50,680,450"
        }
      ]
    }]
  }]
}
```

### Comparison manifest — Simple (multi-canvas)

```json
{
  "@context": ["http://iiif.io/api/presentation/3/context.json"],
  "id": "…",
  "type": "Manifest",
  "behavior": ["individuals"],
  "viewingDirection": "left-to-right",
  "items": [
    {
      "type": "Canvas",
      "label": { "en": ["Image 1 title"] },
      "rights": "https://creativecommons.org/licenses/by/4.0/",
      "metadata": [
        { "label": {"en": ["Artist"]}, "value": {"none": ["Name"]} },
        { "label": {"en": ["Source"]}, "value": {"none": ["Manifest title (https://…)"]} }
      ],
      "items": [{ "type": "AnnotationPage", "items": [{ "motivation": "painting" }] }]
    }
  ]
}
```

---

## Common issues

### Auto-fetch returns nothing / CORS error

The image server does not allow cross-origin requests from a browser. Enter the service ID manually and set the dimensions. The generated manifest itself is not affected — viewers fetch images directly from the server, and many cultural heritage servers allow viewer requests even when they block browser-side fetch.

### Imported manifest shows no images

Check that the manifest is valid IIIF v2 or v3. The tool inspects `@context` to detect the version and reads `sequences[0].canvases` for v2 or `items[]` for v3. If canvas labels are all generic (`Canvas 1`, `Canvas 2`), look for a `summary` or `description` field on the canvas — the tool will promote those automatically.

### Viewer shows the manifest but images fail to load

The image server is likely blocking CORS. This is a server-side issue independent of the manifest, but contact the server administrator or route requests through a proxy to resolve it.

### Manifest ID clashes / duplicate filenames

Each manifest ID is a 12-character SHA-256 hex hash of the title, so different titles always produce different IDs. If you want a human-readable filename, edit the Manifest ID field before generating — the download filename follows that value.

---

## See also

- [Publishing manifests on GitHub Pages](./github_pages_guide.md)

---

Last updated: 2026-05-22
