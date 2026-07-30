# JATS `<alternatives>` Generator

**File:** `jats-alternatives-generator.html`
**Type:** Standalone local HTML tool (no server, no network calls — everything runs in the browser)
**Origin:** Rebuilt from two prior chats — "Converting author-numbered graphics to sequential numbering" (a manual pass for one article) and "Image alternatives for another article" (where the manual approach was generalized into this tool).

## What it does

Generates paired JATS `<graphic>` blocks wrapped in `<alternatives>` for HSAH figures — one pointing to the Hertziana IIIF endpoint, one to the local archival file — ready to paste into the article XML in place of a bare `<graphic>`.

Output structure:

```xml
<!-- Figura 1 — hsah_0000_01 -->
<alternatives>
  <graphic specific-use="online" xlink:href="https://fotothek.biblhertz.it/iiif/3/dpub%2Fhsah0000%2Fhsah_0000_01.jp2/full/max/0/default.jpg"><alt-text>Immagine descritta in didascalia</alt-text></graphic>
  <graphic specific-use="archival" xlink:href="hsah_0000_01.jpg"><alt-text>Immagine descritta in didascalia</alt-text></graphic>
</alternatives>
```

This matches the convention already live in HSAH article XML files: `specific-use="online"` for the IIIF graphic, `specific-use="archival"` for the local one, both carrying the same `<alt-text>`.

## Fields

| Field | Purpose |
|---|---|
| Article ID | e.g. `0000` — used to build filenames (`{article}_{suffix}`) |
| Journal folder | dpub path segment, e.g. `hsah0000` — usually `hsah` + article ID with no underscore |
| IIIF base URL pattern | Defaults to `https://fotothek.biblhertz.it/iiif/3`; editable if the endpoint ever changes |
| Default alt-text | Defaults to `Immagine descritta in didascalia`; editable per batch |

## Two input modes

**Range** — set a first and last figure number and a zero-padding style (`01`, `001`, or no padding). Figure label and filename number stay in sync (Figura *N* → `{article}_N`). Use this for straightforwardly sequential articles.

**Custom list** — one entry per line, either:
- a bare filename suffix (figure numbers auto-increment: 1, 2, 3…), or
- `fig_num, filename_suffix` pairs

This is the mode built specifically for the **author-numbering mismatch problem**: when the author's original figure list uses labels like `3a`/`3b` but the image export assigns them sequential numbers (`03`, `04`, …), or vice versa. Example:

```
1, 01
2, 02
3, 03a
4, 03b
```

## Output

Syntax-highlighted preview in the tool; **Copy XML** button copies the plain (unhighlighted) XML to the clipboard, ready to paste into the article file.

## Gotchas (carried over from the original workflow notes)

- SciFlow local filenames and IIIF server filenames can diverge — reconcile these manually before generating (this is exactly what Custom list mode is for).
- Multi-image figures (`3a`, `3b`) each get their own `<alternatives>` block in this tool's output; if the target JATS structure instead wants one `<alternatives>` with multiple `<graphic>` children for a single `<fig>`, the generated blocks will need manual regrouping.
- The tool doesn't read or write your JATS file directly — it only generates the `<alternatives>` snippets. Insertion into the article XML (replacing the old bare `<graphic>` elements) is still a manual paste step.

## Status

This is a rebuild, since the original chat's live artifact could not be located (search only reaches conversation transcripts, not artifact code itself, once a chat drops out of the index). Worth re-saving this file to the publishing-toolkit repo so it doesn't need reconstructing again.
