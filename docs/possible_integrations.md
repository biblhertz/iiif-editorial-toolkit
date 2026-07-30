# Possible Integrations and Future Features

Reference list for future development of the IIIF Generator tool. Grouped by scope: standalone improvements that need no server, Publink-side work, advanced IIIF features, and viewer/data integrations.

Last updated: 2026-05-22

---

## 1. Standalone tool improvements

These can be implemented directly in `iiif_generator.html` without any server-side work.

### 1.1 Canvas resize (Comparison Layouts)
Deferred / not needed. The Layer Alignment tab already achieves the same result: add layers to the workspace, resize the canvas to the dimensions you need, and reposition images accordingly. Adding canvas resize controls to the Comparison Layouts tab would duplicate that capability without adding new value.

### 1.2 Image layer annotations — recipe 0326
**Reference:** [IIIF Cookbook recipe 0326](https://iiif.io/api/cookbook/recipe/0326-annotating-image-layer/)

This recipe describes how to embed scholarly annotations (tagging, transcription, etc.) on a specific image layer rather than on the canvas as a whole. The annotation lives in the image body's own `annotations` array and uses a `SpecificResource` target with an `ImageApiSelector` (region in pixel coordinates + mandatory `size` attribute to ensure correct scaling).

**Relevance to this tool:** The Layer Alignment tab currently exports painting annotations only. Adding recipe 0326 support would allow users to mark up regions on individual layers (e.g. annotate a detail visible only in the X-ray version). This requires:
- Adding a `Choice` body option to the Layer Alignment manifest (to allow switching between named layers)
- An annotation editor panel per layer (region selector + label/type)
- Serialising annotations as `AnnotationPage` entries on the image body

This is a medium-complexity new feature. The manifest structure is well-defined by the cookbook recipe; the main work is building the annotation editor UI.

### 1.3 Duplicate library item
✓ Implemented 2026-05-22.

### 1.4 Inline manifest preview
✓ Implemented 2026-05-22.

### 1.5 Validation for reachable image URLs
The Validation tab currently checks manifest structure. Extend it with an option to probe whether each image body URL returns a valid response (HEAD request). Flag broken URLs before publishing. Useful when manifests are assembled from external sources.

### 1.6 Comparison session form-field save on second-language toggle
The second-language toggle state (visible/hidden) is saved to the session. The `padding` field in Advanced layout settings is not currently saved to the session. Add it.

### 1.7 Per-item "Copy manifest URL to clipboard" in library
✓ Implemented 2026-05-22.

### 1.8 Canvas zoom — Layer Alignment tab

✓ Implemented 2026-05-22. `−`/`+`/`Fit` buttons and scroll wheel zoom on the canvas workspace. `laZoom` multiplier on top of fit-to-container base scale. Zoom level persisted in `iiifLayerSession`.

### 1.9 Rotation and mirror per layer — Layer Alignment tab

✓ Implemented 2026-05-22. ↺/↻ buttons (90° steps) and numeric degree input (0–359, integer) per layer. ↔ button for horizontal mirror. IIIF Image API `!rotation` URL used in exported manifest. "Natural size" button respects current rotation.

### 1.10 Undo stack — Layer Alignment tab

✓ Implemented 2026-05-22. 20-step snapshot stack. Ctrl/Cmd+Z. Covers: add layer, delete, move (drag start), resize (drag start), rotate, flip, snap, canvas resize, stack reorder. Arrow-key nudge: one snapshot per key-press or hold. History not persisted across reloads.

### 1.11 Rotation and mirror per image — Comparison Layouts tab

✓ Implemented 2026-05-22. Same ↺/↻ and ↔ controls as Layer Alignment, applied per image in the comparison list. Written into exported manifest as IIIF Image API rotation/mirror URL.

### 1.12 Content State Generator as a generator tab

Currently a separate standalone tool (`src/contentstate/iiif_contentstate_generator.html` + two companion viewers, `iiif_viewer.html` and `minimal_iiif_viewer.html`). Candidate for folding into `iiif_generator.html` as a 6th tab, following the same path Layer Alignment took (started standalone, later absorbed into the main tool).

**Benefit:** region selection could pull the target manifest/canvas directly from the Manifest Library instead of requiring the manifest URL to be re-pasted from scratch.

**Tradeoff:** adds more surface area to an already large (242KB) single file, versus keeping Content State small and easy to reason about or hand off independently — e.g. for embedding in the JATS/OJS article pipeline. IIIF viewer injection into JATS→HTML output is a deferred feature (pending the self-hosted OJS migration); a Content State deep link would be a natural mechanism for highlighting one detail inline in an article body, once that migration lands.

Note: the Mirador 3 incompatibility (Content State isn't supported there at all) is orthogonal to this decision — that limitation exists regardless of where the tool lives.

---

## 2. Publink server integration

These require changes on the Publink PHP/MySQL backend. See `publink_integration.md` for the full technical specification.

### 2.1 Library CRUD via API
Replace all `localStorage` read/write calls with `fetch()` calls to a Publink REST API (`GET/POST/PUT/DELETE /api/library/items`). The `metadata.id` field (SHA-256 hash) serves as the stable item identifier.

### 2.2 Manifest publishing via API ✓ (standalone); remaining: Publink server-side

The standalone tool now has a **Publish** button on every output panel. It calls `POST /api/manifests` on the configured manifest server (or GitHub Pages via the GitHub Contents API) and displays the public URL. The Download button is retained as a local fallback. **Remaining for Publink:** implement `POST /api/manifests` returning `{ "url": "…" }`, and wire up the Publink server URL + token in the publish settings or via `postMessage`.

### 2.3 Base URL auto-population ✓ (standalone); remaining: Publink injection

Saving publish settings now auto-fills all four Base URL fields (`baseUrl`, `comparisonBaseUrl`, `collectionBaseUrl`, `laBaseUrl`) from the configured destination. **Remaining for Publink:** inject Publink's manifest server URL into those same fields via the iframe `postMessage` bridge or PHP template, so users never need to set it manually.

### 2.4 Session persistence via API
The tool now saves comparison and layer sessions to `localStorage` (`iiifComparisonSession`, `iiifLayerSession`). In Publink, replace these with `POST /api/sessions/:type` calls so sessions survive across devices and browser clears. The existing `saveComparisonSession()` / `loadComparisonSession()` and `saveLayerSession()` / `loadLayerSession()` functions are the seam to replace.

### 2.5 Data model unification
✓ Partially resolved in standalone tool (2026-05-22).

**Resolved:** Single-image items (individually generated or imported) no longer store a manifest object. `downloadLibraryItemManifest()` always regenerates the manifest on demand from metadata and the current Base URL, with `https://example.org/manifests` as fallback. Composite items (comparison layout, layer alignment) still store their manifest — unavoidable since the multi-image layout cannot be reconstructed from metadata alone.

**Remaining work for Publink:** At save/import time, persist the manifest JSON for composite items to the `iiif_manifests` table. For single-image items, generate and persist the manifest at publish time (when the user requests a public URL) via `POST /api/manifests`. The on-the-fly generation path in `downloadLibraryItemManifest()` is the correct model — replace it with the API call rather than eliminating it.

### 2.6 User identity and access control
Add `user_id` to the manifest table so each user owns their manifests. Expose an admin view listing all users' manifests for the PI. Role-based: PI can view/export all; researchers see their own.

---

## 3. Advanced IIIF features

### 3.1 IIIF Choice body (alternative image layers)
IIIF Presentation 3 supports a `Choice` body with multiple alternatives — for example Natural Light, UV, and X-ray versions of the same object. The viewer presents a layer switcher. This is complementary to recipe 0326 (§1.2 above) and to the Layer Alignment tab's layered output. Supporting `Choice` in the Layer Alignment tab would require:
- A toggle per layer: "alternative" vs. "overlay"
- Generating the `Choice` body structure in the manifest
- The image-tools viewer plugin to expose the switcher

### 3.2 IIIF Ranges (table of contents)
Add a **Structure** section to the Comparison Layouts manifest that defines named ranges grouping canvases (for Simple multi-canvas manifests). Useful when a comparison covers multiple sections of a work.

### 3.3 IIIF Auth API 2.0
Some institutional image servers require authentication. IIIF Auth 2.0 defines a standard probe/token flow. Adding basic support would allow the tool to fetch `info.json` from protected servers by triggering the auth flow in a popup. Medium complexity.

### 3.4 IIIF Search API
Generate a `service` entry linking to a full-text search endpoint on the manifest. Currently out of scope for standalone manifests but relevant once manifests are served from Publink (which could host a search index).

### 3.5 IIIF Change Discovery API
When manifests are served from Publink, publish a Change Discovery API stream (`ActivityStream`) listing created/updated/deleted manifests. Allows aggregators (Europeana, JSTOR Global Plants, etc.) to harvest and index the collection automatically.

### 3.6 Annotation store (Mirador ↔ Publink)
Publink already has a Mirador annotation interface. Ensure that annotations saved by Mirador reference the canonical canvas `id` from manifests generated by this tool. The `canvas/layout` ID pattern must remain stable across manifest updates (do not use timestamp-based IDs for re-published manifests).

---

## 4. Viewer integrations

### 4.1 Mirador 3 — image-tools plugin (opacity / curtain compare)
**Reference:** [mirador-image-tools on GitHub](https://github.com/ProjectMirador/mirador-image-tools)

Install alongside Publink's Mirador instance to expose per-layer opacity sliders for Layered Overlay manifests. Requires a Mirador build step in the Publink project.

### 4.2 Curtain / slider compare component
A split-screen reveal component driven by a drag handle — two images on the same viewport, revealing one as the handle moves. Not a standard Mirador feature; requires a custom OpenSeadragon component. The IIIF manifest structure is already correct (same canvas, two painting annotations). Viewer-side work only.

### 4.3 TheseusViewer deep links
TheseusViewer supports URL parameters for pre-selecting canvases and setting the initial view. Add a "Open at this canvas" link in the Comparison output section that constructs a deep link for the generated manifest.

### 4.4 IIIF drag-and-drop from other sources
Allow dragging a IIIF drag-and-drop payload (the standard `application/json` drag payload defined by the IIIF community) from another browser window directly onto the Comparison or Layer Alignment import area. Enables workflows where the user drags from a Mirador panel directly into the generator.

---

## 5. Data enrichment

### 5.1 Wikidata / Getty ULAN artist lookup
In the Individual Images form, add an autocomplete on the **Artist** field that queries Wikidata or the Getty ULAN API. Selecting a result fills the field with the authority-controlled name and optionally writes a `seeAlso` reference into the manifest metadata.

### 5.2 Bibliographic metadata from opac / Zotero
Allow importing item metadata (title, date, institution, rights) from a Zotero library or an OAI-PMH endpoint. Reduces re-keying for items already catalogued.

### 5.3 EXIF / XMP metadata extraction
If the user pastes a direct JPEG URL (not a IIIF service), attempt to read EXIF/XMP metadata from the image (requires a server-side proxy since JavaScript cannot read raw EXIF cross-origin). Could pre-fill Artist, Date, Institution.

---

## Priority summary

| Item | Effort | Value | Suggested order |
|------|--------|-------|----------------|
| 1.6 Padding field to session | Low | Low | When convenient |
| 1.12 Content State tab merge | Medium | Medium | When convenient — no urgent driver |
| 2.1–2.3 Publink API + manifest server | High | High | Publink integration sprint |
| 2.5 Data model unification (Publink remainder) | Low | High | Same sprint — standalone part done |
| 1.2 Recipe 0326 layer annotations | Medium | High | After Publink, Layer Alignment v2 |
| 3.1 Choice body | High | High | Layer Alignment v2 |
| 4.1 image-tools plugin | Low (viewer side) | High | Publink sprint |
| 4.2 Curtain compare | High | Medium | Post-launch |
| 3.5 Change Discovery API | Medium | Medium | When Publink is live |
