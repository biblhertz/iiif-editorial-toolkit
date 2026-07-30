# IIIF Compliance

What this toolkit actually generates and checks against the IIIF Presentation and Image APIs, and where its built-in validator falls short. For the full tab-by-tab workflow, see the [Generator Guide](./generator_guide.md).

---

## What the generator writes

Every manifest produced by `src/generator/iiif_generator.html` (Individual Images, Comparison Layouts, Layer Alignment, Collection) follows the same fixed structure:

- `@context`: always `["http://iiif.io/api/presentation/3/context.json"]` — the tool only ever emits Presentation API 3.0, never 2.0.
- `id`: always an absolute URL, `{Base URL}/{manifestId}.json`.
- `type`: always `"Manifest"`.
- `label`: always a language map keyed by the BCP47 code(s) chosen in the form — never a bare string.
- Canvas `width`/`height`: taken from the fetched or manually entered image dimensions; always present when a manifest is generated (the form requires them).
- Annotation `motivation`: always `"painting"`.
- Annotation `body`: always includes `id`, `type: "Image"`, `format: "image/jpeg"`, and a `service` array.

The `service.profile` value reflects the real server capability whenever the toolkit has it: `fetchImageInfo()` (Individual Images) and `laFetchInfo()` (Layer Alignment) both read the actual `profile` field from the fetched `info.json` and normalize it (`normalizeProfile()`, handling both the Image API 3.0 plain-string form and the 2.x array form); importing an existing manifest (`extractImagesV3`/`extractImagesV2`) reads the profile the source manifest already declares. That value then flows through library storage and into Comparison Layouts and library-regenerated manifests. `"level2"` is used only as a fallback when no real value was ever available — e.g. dimensions entered by hand instead of fetched.

**Target format:** every annotation `target` the tool writes is a plain string — either the bare canvas ID, or `{canvasId}#xywh=x,y,w,h`. The toolkit never emits IIIF's alternative object-form target (`{"type": "SpecificResource", "source": ..., "selector": ...}`). If you need that form, it has to be added by hand after export.

---

## Built-in validator (Validation & Testing tab)

Clicking **Validate manifest** passes the parsed JSON to `validateIIIFManifest(manifest)` (`iiif_generator.html:3007`), which returns an array of `{valid, message}` objects rendered by `displayValidationResults()` (`iiif_generator.html:3088`) as PASS/FAIL lines.

What it checks, in order:

1. **Version** — detected by substring match on `@context` (`presentation/3` vs `presentation/2`). No match is reported as a failure.
2. **Identity** — presence of `id` or `@id`.
3. **Type** — must be `"Manifest"` (v3) or `"sc:Manifest"` (v2).
4. **Label** — presence only, not language-map structure.
5. **Canvas structure**:
   - v2: reads `sequences[0].canvases`; for each canvas, checks `images[0].resource` has an `@id`/`id`.
   - v3: reads `items[]`; for each canvas, checks `width`/`height` are *present* (truthy check, not type- or value-validated), then flattens `items[].items` to get painting annotations, flags any whose `motivation` isn't `"painting"`, and checks each annotation body has an `id`.

When a manifest has exactly one canvas with more than one painting annotation, the validator treats it as a single-canvas composition and checks whether *any* annotation's target has a `#xywh=` fragment (`iiif_generator.html:3075-3078`). This correctly handles a Layer Alignment export where the full-canvas base layer (target = bare canvas ID, no fragment) sits alongside positioned detail layers with `#xywh` fragments, regardless of which order they appear in — previously this check only looked at `annotations[0]` and could false-FAIL a valid export depending on layer order.

The validator does not check `service`/`profile` values, and has no code path for the Authentication API or Search API — neither is referenced anywhere in the toolkit, so there's no support to look for.

---

## Image API: auto-detection

In the Individual Images tab, `fetchImageInfo()` (`iiif_generator.html:1444`) reads the **IIIF Service ID** field, requests `{serviceId}/info.json`, and on success populates width/height and a thumbnail preview. On failure — most commonly a CORS restriction on the image server — it reports the error through the on-screen message area (`showMessage`) rather than throwing, and the dimensions can then be entered manually.

The tool also reads the server's declared `profile` from the same `info.json` response and carries it into the generated manifest's `service` block (see above) — it isn't validated against what the server can actually do beyond that, so a server misreporting its own profile would still be trusted as-is.

---

## Viewer compatibility testing

**Test viewer compatibility** (`testViewerCompatibility()`, `iiif_generator.html:3098`) builds direct links to:

- Mirador 3 (`https://projectmirador.org/embed/?iiif-content=...`)
- TheseusViewer (`https://theseusviewer.org/?manifest=...`)
- Universal Viewer (`https://uv-v4.netlify.app/#?manifest=...`)

This requires network access to those services and does not validate anything locally beyond generating the links — actually loading the manifest in each viewer is the real test.

---

## External validators

For checks beyond what the toolkit itself performs, use:

- [IIIF Presentation Validator](https://presentation-validator.iiif.io/)
- [IIIF Validator (general)](https://iiif.io/api/presentation/validator/service/)
- [Manifest Editor](https://manifest-editor.digirati.services/)

---

Last updated: 2026-07-30
