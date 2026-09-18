"""
Link a JATS article to its already-generated IIIF manifest.

Run this right after xml-to-manifest.py has produced (and, ideally, after
you've uploaded) manifest.json for an article. It writes two things into the
article XML:

  1. A shared, article-level manifest reference:
       front/article-meta/custom-meta-group/custom-meta[meta-name='iiif-manifest']
  2. Per-figure canvas markers, one per <fig> that actually got a canvas:
       <object-id pub-id-type="iiif-canvas">N</object-id>
     as the first child of that <fig> — N is the figure's 1-based position
     among the article's *rendered* canvases (matching xml-to-manifest.py's
     own build order), not a raw fig count. Figures xml-to-manifest.py
     skipped (no online image URL) correctly get no marker at all and just
     render as plain, non-interactive thumbnails.

The canvas count/order is read directly from manifest.json's own "items"
list and cross-checked against each fig's own id (canvas ids are always
"{base_canvas}/canvas/{fig_id}") — if a fig and its expected canvas don't
line up, that's reported as an error rather than silently mislinking a
figure to the wrong image.

Already-linked figures (anything already carrying an iiif-canvas or
iiif-manifest object-id) are left untouched, so re-running this after a
manifest regeneration is safe — pass --force to strip and redo everything
instead, e.g. after a fig was added/removed and canvas numbers shifted.

Usage:
    # Single article
    python add-manifest-links.py article.xml manifest.json
    python add-manifest-links.py article.xml manifest.json --force
    python add-manifest-links.py article.xml manifest.json -o linked.xml

    # Whole volume — matches article.xml <-> manifests/article.json by filename stem
    python add-manifest-links.py volume_folder/ manifests_folder/
    python add-manifest-links.py volume_folder/ manifests_folder/ --force
"""

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

XLINK = "{http://www.w3.org/1999/xlink}"


class LinkError(Exception):
    """Raised for per-article problems so batch mode can skip just that
    article instead of aborting the whole run."""


def has_online_graphic(fig) -> bool:
    """Same detection xml-to-manifest.py uses to decide whether a fig gets
    a canvas at all — must stay in lockstep with that script."""
    alternatives = fig.find("alternatives")
    graphics = alternatives.findall("graphic") if alternatives is not None \
               else fig.findall("graphic")
    for g in graphics:
        use = g.get("specific-use", "")
        href = g.get(f"{XLINK}href", "").strip()
        if use == "online":
            return True
        if not use and href.startswith("https://"):
            return True
    return False


def find_or_create(parent, tag):
    el = parent.find(tag)
    if el is None:
        el = ET.SubElement(parent, tag)
    return el


def set_manifest_meta(root, manifest_url: str):
    """Ensure front/article-meta/custom-meta-group/custom-meta[iiif-manifest]
    exists with the given URL — updates it in place if already present with
    a different value."""
    article_meta = root.find(".//front/article-meta")
    if article_meta is None:
        raise LinkError("no <front><article-meta> found — not a JATS article?")

    cmg = article_meta.find("custom-meta-group")
    if cmg is None:
        cmg = ET.SubElement(article_meta, "custom-meta-group")
        cmg.text = "\n  "
        cmg.tail = "\n"

    for cm in cmg.findall("custom-meta"):
        name = cm.find("meta-name")
        if name is not None and (name.text or "").strip() == "iiif-manifest":
            value = find_or_create(cm, "meta-value")
            if value.text != manifest_url:
                print(f"  Updating existing iiif-manifest meta-value → {manifest_url}")
                value.text = manifest_url
            return

    cm = ET.SubElement(cmg, "custom-meta")
    cm.text = "\n    "
    cm.tail = "\n  "
    name = ET.SubElement(cm, "meta-name")
    name.text = "iiif-manifest"
    name.tail = "\n    "
    value = ET.SubElement(cm, "meta-value")
    value.text = manifest_url
    print(f"  Added iiif-manifest meta-value = {manifest_url}")


def already_linked(fig) -> bool:
    return any(
        oid.get("pub-id-type") in ("iiif-canvas", "iiif-manifest")
        for oid in fig.findall("object-id")
    )


def strip_canvas_links(root):
    for fig in root.iter("fig"):
        for oid in fig.findall("object-id"):
            if oid.get("pub-id-type") == "iiif-canvas":
                fig.remove(oid)


def add_canvas_links(root, canvas_ids: list, article_name: str) -> int:
    """Walk <fig> in document order (mirrors xml-to-manifest.py's own
    body.iter("fig")), consuming canvas_ids in order for every fig that has
    an online graphic. Returns the number of figs newly linked."""
    body = root.find(".//body")
    if body is None:
        raise LinkError("no <body> found")

    remaining = list(canvas_ids)
    linked = 0
    already_linked_count = 0

    for fig in body.iter("fig"):
        if already_linked(fig):
            if has_online_graphic(fig):
                already_linked_count += 1
            continue
        if not has_online_graphic(fig):
            continue

        if not remaining:
            raise LinkError(
                f"more figs with online images than canvases in the manifest "
                f"({len(canvas_ids)} canvases) — manifest may be stale, "
                f"regenerate it first"
            )

        position = len(canvas_ids) - len(remaining) + 1
        canvas_id = remaining.pop(0)
        fig_id = fig.get("id", "").strip()
        if fig_id and not canvas_id.endswith(f"/canvas/{fig_id}"):
            raise LinkError(
                f"canvas order mismatch on fig id='{fig_id}' in {article_name}: "
                f"expected canvas {position} to be '.../canvas/{fig_id}', "
                f"got '{canvas_id}' — figs and manifest are out of sync, "
                f"regenerate the manifest before linking"
            )

        oid = ET.Element("object-id", {"pub-id-type": "iiif-canvas"})
        oid.text = str(position)
        oid.tail = fig.text
        fig.text = "\n" + (fig.text or "").lstrip("\n") if fig.text else "\n"
        fig.insert(0, oid)
        linked += 1

    if remaining and linked + already_linked_count < len(canvas_ids):
        print(f"  ⚠  {len(remaining)} canvas(es) in the manifest have no matching fig "
              f"— manifest may be ahead of the article XML")

    return linked


def link_article(xml_path: Path, manifest_path: Path, out_path: Path, force: bool):
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest_url = manifest["id"]
    canvas_ids = [item["id"] for item in manifest["items"]]

    tree = ET.parse(xml_path)
    root = tree.getroot()

    if force:
        strip_canvas_links(root)

    set_manifest_meta(root, manifest_url)
    linked = add_canvas_links(root, canvas_ids, xml_path.name)

    tree.write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"✓ {xml_path.name}: linked {linked} new fig(s) to {manifest_path.name} "
          f"({len(canvas_ids)} canvases total) → {out_path}")


def process_folder(xml_dir: Path, manifest_dir: Path, force: bool):
    xml_files = sorted(xml_dir.glob("*.xml"))
    if not xml_files:
        sys.exit(f"✗ No .xml files found in {xml_dir}")

    linked, no_manifest, failed = [], [], []
    for xml_path in xml_files:
        manifest_path = manifest_dir / f"{xml_path.stem}.json"
        if not manifest_path.exists():
            no_manifest.append(xml_path.name)
            continue
        print(f"── {xml_path.name} ──")
        try:
            link_article(xml_path, manifest_path, xml_path, force)
        except LinkError as exc:
            print(f"  ✗ {exc}")
            failed.append(xml_path.name)
        print()

    print(f"── Batch complete: {len(linked) or len(xml_files) - len(no_manifest) - len(failed)} "
          f"article(s) processed, {len(no_manifest)} had no matching manifest, "
          f"{len(failed)} failed ──")
    if no_manifest:
        print(f"  No manifest: {no_manifest}")
    if failed:
        print(f"  Failed: {failed}")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("article_or_folder")
    ap.add_argument("manifest_or_folder")
    ap.add_argument("-o", "--output", help="Single-article mode only: write to this "
                                            "file instead of overwriting the article in place")
    ap.add_argument("--force", action="store_true",
                     help="Strip existing iiif-canvas links and relink from scratch")
    args = ap.parse_args()

    article_path = Path(args.article_or_folder)
    manifest_path = Path(args.manifest_or_folder)

    if article_path.is_dir():
        if args.output:
            sys.exit("✗ -o/--output isn't supported in batch (folder) mode")
        process_folder(article_path, manifest_path, args.force)
    else:
        out_path = Path(args.output) if args.output else article_path
        try:
            link_article(article_path, manifest_path, out_path, args.force)
        except LinkError as exc:
            sys.exit(f"✗ {exc}")


if __name__ == "__main__":
    main()
