# CLAUDE.md

Guidance for working in this repository.

## Structure

- `src/<tool>/` — each tool is a self-contained artifact (mostly single-file HTML, no build step). One folder per tool.
- `docs/` — one guide per tool, referenced from the README's Documentation list.
- `src/xml2manifest/` is the one Python-based tool; requires Python 3, no dependencies beyond the standard library.

## Conventions

- Browser tools are pure HTML/CSS/JS with no third-party dependencies.
- Target spec: IIIF Presentation API 3.0, Image API 2.1/3.0.
- When adding a new tool: create `src/<tool_name>/`, add a matching `docs/<tool>.md` guide, and update the README's Project Structure tree, Tools Overview table, and Documentation list.
- No build step, no package manager, no test suite — verify changes by opening the HTML file directly in a browser.
