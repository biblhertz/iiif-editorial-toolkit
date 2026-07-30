# Comparison Layout Algorithms

How the six layout presets in the Comparison Layouts tab compute image positions, based on `calculateLayoutPositions()` in `src/generator/iiif_generator.html`. This covers the **Comparison Layouts** tab only — the **Layer Alignment** tab uses fully manual positioning (drag, resize handles, keyboard nudge) with no preset algorithms; see the [Generator Guide](./generator_guide.md#layer-alignment).

---

## The layout canvas is fixed at 1600×700

Every preset positions images inside a canvas that is hardcoded at **1600×700 px**, regardless of how many images are selected or their native sizes. This is the same fixed size used for the final "Universal" comparison manifest's `Canvas.width`/`Canvas.height` — the preview you see while arranging images is pixel-for-pixel what ends up in the manifest.

This only applies to the **Universal** target-viewer output (single canvas, images positioned with `#xywh` fragments). The **Simple Manifest** output ignores layout positions entirely and instead creates one canvas per image at that image's own native dimensions.

Each computed position becomes a fragment-target annotation:

```json
{
  "type": "Annotation",
  "motivation": "painting",
  "body": {
    "id": "https://imageserver.org/iiif/3/id/full/max/0/default.jpg",
    "type": "Image",
    "service": [{ "id": "https://imageserver.org/iiif/3/id", "type": "ImageService3", "profile": "level2" }]  // real value if fetched/imported, "level2" only as fallback
  },
  "target": "https://.../canvas/layout#xywh=100,50,680,450"
}
```

**Manual overrides are not clamped consistently.** Dragging an image in the preview is clamped to the visible canvas area (`Math.max(0, Math.min(previewWidth - w, ...))` in `initDragHandlers`), so you can't drag a placeholder off-canvas. The numeric coordinate editor (X/Y/W/H fields, opened via **Advanced layout settings → Open coordinate editor**) has no such check — `updateSelectedPosition()` writes `parseInt()` of whatever you type directly into the position, so it's possible to enter coordinates that place an image partly or fully outside the 1600×700 canvas.

---

## Layout Type dropdown

These are the exact options in the `#layoutType` select, in order:

| Value | Label shown in the dropdown |
| --- | --- |
| `horizontal` | Horizontal Row |
| `horizontal-balanced` | Horizontal Row (Balanced Heights) |
| `storyboard` | Storyboard Layout (Optimized for Viewing) |
| `main-derivatives` | Main + Derivatives (1+N) |
| `grid-2x2` | 2x2 Grid |
| `vertical` | Vertical Stack |

Padding (default 100px, editable in **Advanced layout settings**) is shared by all six presets — it controls the gap between images and, in most layouts, the starting offset from the canvas edge.

### Horizontal Row

Images are placed left to right at their native size, provided they fit. Specifically:
- `maxHeight` is the tallest native height among the selected images. Because it's a maximum, every image's own height already satisfies `min(img.height, maxHeight)` — this step never actually shrinks anything; it's a no-op cap given how the code computes it.
- The natural total width (sum of native widths) plus padding gaps is compared against the 1600px canvas width. If it exceeds 1600, every image is scaled down by the same factor so the row fits; otherwise images are placed at native size (they can end up narrower than the canvas with empty space to the right — the canvas width doesn't adapt to content).
- Images are placed sequentially (`x += width + padding`), vertically positioned at `padding + (700 - height) / 2` — centered in the canvas height, with the padding value added on top of the centering offset rather than pure centering.

### Horizontal Row (Balanced Heights)

Each image is independently scaled so its height is exactly **400px** (hardcoded), width scaled proportionally to preserve aspect ratio. Images are placed left to right with `padding` gaps, all at a fixed `y = padding` (top-aligned, not centered). Unlike Horizontal Row, there is no check against the 1600px canvas width — if the combined scaled width of all images exceeds it, the row simply overflows past the canvas edge rather than shrinking to fit.

### Storyboard Layout

This is the same algorithm as Horizontal Row (Balanced Heights), with two constants changed: target height is **350px** instead of 400, and `y = padding + 50` instead of `padding`. There is no additional viewing-order or "optimization" logic beyond that — despite the "(Optimized for Viewing)" label, the position math is identical to Balanced Heights.

### Main + Derivatives (1+N)

The **first image in the Selected list** (order set by the reorder arrows in Comparison Layouts Step 2) becomes the main image:
- It is scaled to fit inside an 800×400 box while preserving aspect ratio (`Math.min(800/w, 400/h)`), placed at the top-left corner `(padding, padding)`.
- The remaining images (derivatives) are placed in a single row starting at `y = padding + mainHeight + 50`. Their combined width is divided evenly across the space equal to the main image's scaled width (`mainWidth`), accounting for the gaps between them.
- **Derivative height is derived from each image's own aspect ratio**: `derivativeWidth × (img.height / img.width)`, so a derivative with different proportions than the main image keeps its own shape rather than being forced into a fixed box.

### 2x2 Grid

Cell size is fixed and derived only from the canvas and padding — `cellWidth = (1600 - padding×3) / 2`, `cellHeight = (700 - padding×3) / 2` — not from any image's dimensions. Placement is `row = floor(index/2)`, `col = index % 2`. Each image is scaled to fit inside its cell without exceeding either dimension (`Math.min(cellWidth/img.width, cellHeight/img.height)`) and centered within it, so proportions are preserved rather than stretched to fill the cell. Only the first 4 selected images are placed this way — if more than 4 are selected, the tool shows an error ("2x2 Grid only shows the first 4 images; the rest are left unpositioned") rather than silently extending past the canvas.

### Vertical Stack

The mirror of Horizontal Row along the other axis: `maxVerticalWidth` is the widest native width among selected images (same no-op cap as Horizontal Row, for the same reason). If the total stacked height plus padding gaps exceeds the 700px canvas height, the whole stack is scaled down uniformly to fit; otherwise images keep native size. Each image is horizontally centered (`x = padding + (1600 - width) / 2`) and stacked top to bottom with `padding` gaps between them.

---

## What isn't real

An earlier version of this document included a "Performance Matrix" (canvas size / memory usage / loading time per layout) and a generic tile-pyramid / IIIF-tiling optimization section. Neither reflects anything this tool measures or does — the generator computes static `xywh` positions in JavaScript; it does not tile images, generate image pyramids, or measure loading time or memory. Those sections have been removed rather than presented as findings.

---

**See also:** [Generator Guide](./generator_guide.md) | [IIIF Compliance](./iiif_compliance.md)

---

Last updated: 2026-07-30
