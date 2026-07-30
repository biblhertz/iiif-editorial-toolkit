# IIIF Content State Generator — User Guide

A self-contained, single-file HTML tool for creating IIIF Content States — compact, shareable deep links into a specific region of a specific canvas — following [IIIF Recipe 0485](https://iiif.io/api/cookbook/recipe/0485-region-of-interest/). No installation, no server required — open `src/contentstate/iiif_contentstate_generator.html` in any modern browser.

---

## Viewer compatibility (important)

Content States are not universally supported. As the tool's own banner states:

- ✅ **TheseusViewer** — full support, including region highlighting
- ❌ **Mirador 3** — Content State is **not** supported. The generator's Mirador link opens the plain manifest (no region highlight) rather than the encoded state.
- 🔧 **Other viewers** — check IIIF compatibility before relying on Content State support.

If your primary target is Mirador, this tool won't get you a working deep link there — use the main [Generator](./generator_guide.md)'s Layer Alignment or Comparison tabs instead, which produce standard manifests Mirador fully supports.

---

## Workflow

### 1. Load a manifest and select a canvas

Paste a IIIF manifest URL into **IIIF Manifest URL** and click **📥 Load Manifest**. If the manifest has multiple canvases, a **Select Canvas** dropdown appears — canvas labels are read from `canvas.label` (English or Italian preferred, falling back to the first available language). Once a canvas is selected, its title, pixel dimensions, and canvas ID are shown, and its image loads into the region-selection canvas below (fetched at `{service}/full/800,/0/default.jpg` when the canvas has an IIIF image service, or the plain image URL otherwise).

### 2. Define a region

On the canvas preview:

- **Click and drag** to draw a region freehand.
- Drag the region's corner handles to resize it, or drag the region itself to move it.
- Use a **preset**: Center (50% width/height, centered), or one of the four corners (30% width/height each).
- Or type exact **X / Y / W / H** values directly into the coordinate inputs below the canvas.
- **Clear** removes the current region.

The preview also has independent pan/zoom controls (`+`/`−`/`⌂` reset, shown as a percentage) for navigating large images while you work — this only affects the preview, not the region coordinates, which are always in canvas pixel space.

### 3. Add optional context

- **Annotation Label** — short label for the region (e.g. "Detail of hand").
- **Description/Note** — longer free-text note.

Both are optional. If either is filled in, the generated Content State includes a `W3C Annotation` (`motivation: "highlighting"`) targeting the region, with the note (or label, if no note) as the annotation body and the label as the annotation's `label`. If both are left empty, the Content State is just the bare canvas region — no annotation.

### 4. Generate and use the output

Click **🚀 Generate Content State**. The output section shows:

- **Minimal Content State JSON** — pretty-printed for reading (the minified version is what actually gets encoded), plus its size in bytes.
- **Base64 Encoded Parameter** — the standard `btoa()` encoding of the minified JSON, ready to drop into a `?iiif-content=` or `?content=` URL parameter.
- **Test in Viewers** — four links, generated from the same Content State:

  | Link | Destination | Notes |
  | --- | --- | --- |
  | 📚 TheseusViewer (Full Support) | `theseusviewer.org/?iiif-content=...` | Native Content State support — the region highlight will show |
  | 🎯 Clean Viewer (For Articles) | `minimal_iiif_viewer.html?content=...` (same folder) | Minimal chrome, meant for embedding — see below |
  | 🎭 Mirador 3 (Manifest Only) | `projectmirador.org/embed/?iiif-content=<manifest URL>` | Opens the full manifest, unencoded — no region highlight, since Mirador doesn't read Content State |
  | 🔧 Test Viewer (Debug) | `iiif_viewer.html?content=...` (same folder) | Validation and dual-viewer debug tool — see below |

- **Download JSON** saves the (non-minified) Content State as a file.
- **Share Link** builds a link to the Clean Viewer (`minimal_iiif_viewer.html?content=...`) and uses the Web Share API if the browser supports it, so it can go straight to a share sheet on mobile.

---

## Content State structure

```json
{
  "@context": "http://iiif.io/api/presentation/3/context.json",
  "id": "https://example.org/canvas/1#xywh=100,150,400,300",
  "type": "Canvas",
  "partOf": [
    { "id": "https://example.org/manifest.json", "type": "Manifest" }
  ],
  "annotations": [
    {
      "@context": "http://www.w3.org/ns/anno.jsonld",
      "id": "https://example.org/canvas/1#annotation-1234567890",
      "type": "Annotation",
      "motivation": "highlighting",
      "body": { "type": "TextualBody", "value": "Detail of hand", "format": "text/plain" },
      "target": "https://example.org/canvas/1#xywh=100,150,400,300",
      "label": { "en": ["Detail of hand"] }
    }
  ]
}
```

The `annotations` array is only present if a label or note was provided in step 3.

---

## Companion viewer: Clean Viewer (`minimal_iiif_viewer.html`)

A minimal iframe wrapper intended for embedding a Content State (or a plain manifest) in an article. It reads its target from the query string:

- Content State: `?content=`, `?contentState=`, `?iiif-content=`, or `?c=` (whichever is present, checked in that order) — base64-decoded first, falling back to plain URL-decoding if that fails.
- Plain manifest (no region): `?manifest=` or `?m=`.

Either way, it builds a `theseusviewer.org` embed URL and loads it in an iframe, showing a loading spinner and a friendly error message if nothing valid was supplied. Add `?minimal=true` or `&m=1` to hide the header and footer entirely for a tighter embed. The page title and heading update automatically from the Content State's annotation label, if one is present.

## Companion viewer: Test Viewer (`iiif_viewer.html`)

A debug tool for checking a Content State before using it elsewhere. It reads the same `?content=`-style parameters, extracts and validates the referenced manifest, and displays the decoded Content State info alongside a line-by-line IIIF compliance check. It has two viewer tabs — **Mirador 3** and **TheseusViewer** — so you can compare how the manifest looks in each; Mirador loads the plain manifest (no region highlight, per the compatibility note above) and TheseusViewer loads the actual encoded Content State.

Both companion files live alongside the generator in `src/contentstate/`.

---

## Common issues

**Manifest won't load** — check the URL is reachable and returns valid JSON; CORS restrictions on the image server will block the canvas thumbnail even if the manifest itself loads.

**Region looks right here but doesn't highlight in a viewer** — confirm you're testing in TheseusViewer or the Clean/Test viewers, not Mirador 3, which doesn't support Content State at all.

**Base64 string looks huge** — the encoded parameter length scales with the base URL and any annotation text; keep labels/notes short if you need a compact URL.
