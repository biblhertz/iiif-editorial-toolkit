# IIIF Editorial Toolkit

A suite of self-contained, single-file HTML tools for creating, viewing, and managing IIIF (International Image Interoperability Framework) manifests in academic and scholarly contexts. Developed at the [Bibliotheca Hertziana – Max Planck Institute for Art History](https://www.biblhertz.it), Rome.

**[Try the tools live](https://biblhertz.github.io/iiif-editorial-toolkit/)** — no cloning required.

## The History Behind

This toolkit was created out of frustration in order to have a sensible way to generate multi-image IIIF manifests as a better solution than generating a composition in a photo editor for Art History academic digital publications. After testing what was available, I decided that what I needed was nowere to be found and started a complex jurney with the support of an artificial intelligence (Claude Sonnet 4 by Anthropic). Initially the idea was to use Openseadragon to view them and the solution provided by Claude 4 Sonnet worked, kind of. The viewer was added as a quick way to check the code, and it is a Openseadragon with multi-image enabled. The problems started with more complex layout with different vertical alignment, because the coordinates made absolutely no sense. The other problem was that those manifest were not properly displayed in Mirador, even if the manifest and the layers were correctly loaded.

For this reason I double checked the IIIF Multi-Image cookbook and found that the OSD manifest had a totally different approach. I asked to rebuilt everything in a new version. If you think this might be interesting or useful, you can read the full description below.

Please note that you need to know your IIIF image api link (the info.json), to be able to create a composition manifest. Also, for very complex layouts, it is faster to do a mockup in Illustrator and then insert the coordinates (xywh) of each element than hoping for a preset to fit your needs.

This toolkit was also funded as part of Publink, a platform developed at the Institute — hence some in-tool references to "Publink." It lives independently, though: nothing here requires the Publink platform to use.

## Quick Start

```bash
git clone https://github.com/biblhertz/iiif-editorial-toolkit.git
cd iiif-editorial-toolkit
# Open any HTML file in your browser - no build step required!
```

No installation, no server, no internet connection required to run any of the browser tools.

## Project Structure

```
iiif-editorial-toolkit/
├── docs/                          # Documentation
├── src/
│   ├── generator/
│   │   └── iiif_generator.html    # Main manifest generator (5 tabs, see below)
│   ├── size_updater/
│   │   └── IIIF_manifest_dimension_updater.html  # Fetch real image sizes into an existing manifest
│   ├── contentstate/
│   │   ├── iiif_contentstate_generator.html  # IIIF Content State (deep-link) generator, with pan/zoom preview
│   │   ├── iiif_viewer.html                  # Test viewer for generated content states
│   │   └── minimal_iiif_viewer.html          # Clean viewer for embedding content states in articles
│   ├── jats_alternatives/
│   │   └── jats-alternatives-generator.html  # Generates JATS <alternatives> graphic blocks for HSAH figures
│   └── xml2manifest/              # JATS XML → IIIF manifest pipeline (Python)
└── README.md
```

## Tools Overview

### 1. IIIF Manifest Generator (`src/generator/iiif_generator.html`)
**Best for:** the full manifest lifecycle, from a single image to a complex scholarly comparison.

A single HTML file with five tabs:

| Tab | Purpose |
|---|---|
| Individual Images | Generate a single-image manifest with full scholarly metadata |
| Comparison Layouts | Build a multi-image manifest from library items using preset layout algorithms |
| Layer Alignment | Position images of different sizes on a shared canvas and export as a layered manifest |
| Manifest Library | Manage, edit, duplicate, export, and import your manifest collection |
| Validation & Testing | Check any manifest for IIIF compliance and open it in viewers |

**No dependencies** — uses only standard browser APIs:

| API | Purpose |
|---|---|
| Web Crypto API (`crypto.subtle`) | SHA-256 manifest ID generation from title |
| Fetch API | Manifest import, `info.json` dimension fetch |
| `localStorage` | Library persistence; comparison and layer session restore |
| Clipboard API (`navigator.clipboard`) | Copy manifest JSON or URL to clipboard |
| Blob / `URL.createObjectURL` | JSON file download |

**Note on CORS:** IIIF images are online resources by definition. Some institutional image servers block browser-side `fetch` requests for `info.json` (cross-origin policy). If auto-fetch fails, image dimensions can be entered manually — the generated manifest is unaffected, since IIIF viewers fetch images directly from the server.

**Use Cases:** art history comparisons, manuscript analysis, multi-image scholarly publications, complex positioning requirements.

### 2. Manifest Dimension Updater (`src/size_updater/IIIF_manifest_dimension_updater.html`)
**Best for:** fixing placeholder or unknown image dimensions in an already-generated manifest.

Batch-fetches real dimensions from each image's `info.json` and updates both Canvas and Image body sizes. Drag-and-drop interface with progress tracking.

### 3. XML → Manifest Suite (`src/xml2manifest/`)
**Best for:** editorial teams converting JATS XML articles into manifests without touching the generator UI.

A Python pipeline (`xml-to-manifest.py` + `manifest_config.json` + `fig-extractor.py`) that converts a JATS XML article into a IIIF Presentation API 3.0 manifest in one automated pass, fetching real image dimensions from the IIIF server. See `src/xml2manifest/readme.md`.

### 4. IIIF Content State Generator (`src/contentstate/`)
**Best for:** generating a shareable deep-link (IIIF Content State) into a single region or view of an image, for citing a detail in an article.

`iiif_contentstate_generator.html` builds and encodes a IIIF Content State, with a pan/zoom canvas preview (drag to pan, +/−/reset controls) for framing the target region before sharing. It links out to two companion viewers included in the same folder: `iiif_viewer.html` (a test/debug viewer for the generated content state) and `minimal_iiif_viewer.html` (a stripped-down viewer meant for embedding in published articles). **Important:** Mirador 3 does not support Content State — only TheseusViewer and the two companion viewers here do. See the [Content State Guide](./docs/contentstate_guide.md).

### 5. JATS Alternatives Generator (`src/jats_alternatives/jats-alternatives-generator.html`)
**Best for:** editorial staff preparing HSAH article XML, pairing each figure's online (IIIF) and archival image references.

A standalone, no-network local tool that generates paired JATS `<graphic>` blocks wrapped in `<alternatives>` — one pointing to the Hertziana IIIF endpoint, one to the local archival file — ready to paste into article XML in place of a bare `<graphic>`. Supports sequential ranges and a custom list mode for reconciling author-numbered figures (e.g. `3a`/`3b`) against sequentially-exported filenames. See the [JATS Alternatives Generator doc](./docs/jats-alternatives-generator.md).

## Detailed Documentation

- [Generator Guide](./docs/generator_guide.md) — complete guide to manifest generation
- [Content State Guide](./docs/contentstate_guide.md) — deep links into a canvas region, viewer compatibility caveats
- [Manifest Dimension Updater](./docs/IIIF_manifest_dimension_updater_readme.md)
- [Publishing on GitHub Pages](./docs/github_pages_guide.md) — serve your manifests publicly for free
- [Layout Algorithms](./docs/layout_algorithms.md) — understanding positioning systems
- [IIIF Compliance](./docs/iiif_compliance.md) — standards and best practices
- [Examples](./docs/examples.md) — coded examples and use cases
- [Possible Integrations](./docs/possible_integrations.md) — prioritised list of future features
- [JATS Alternatives Generator](./docs/jats-alternatives-generator.md) — pairing online/archival graphic references for HSAH figures

## Technical Requirements

### Browser Support
- Chrome 70+ (recommended)
- Firefox 65+
- Safari 12+
- Edge 79+

### IIIF Compliance
- IIIF Presentation API 3.0
- IIIF Image API 2.1/3.0

### Dependencies
- `src/generator/`, `src/size_updater/`, `src/contentstate/`, and `src/jats_alternatives/` are pure HTML/CSS/JavaScript with no third-party libraries.
- `src/xml2manifest/*` requires Python 3.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [IIIF Community](https://iiif.io/) for standards and specifications
- [Mirador](https://projectmirador.org/) for viewer integration
- [TheseusViewer](https://theseusviewer.org/) for comparison viewing

---

**Made with ❤️ and Claude for the academic editorial community**
