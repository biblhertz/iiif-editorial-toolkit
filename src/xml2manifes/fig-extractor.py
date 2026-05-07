"""
Extract all <fig> elements from the article body of a JATS XML file.
Targets <alternatives> blocks and separates online (IIIF) from archival graphics.
Output: CSV ready for direct use as manifest generator input.

Expected structure:
  <alternatives>
    <graphic specific-use="online"   xlink:href="https://.../full/max/0/default.jpg"/>
    <graphic specific-use="archival" xlink:href="local-file.jpg"/>
  </alternatives>
"""

import xml.etree.ElementTree as ET
import csv, sys, re
from collections import defaultdict

XLINK = "{http://www.w3.org/1999/xlink}"

# Strips the IIIF request suffix to derive the service ID base URL
IIIF_SUFFIX = re.compile(r"/(?:full|square|region)/.*$")


def derive_service_id(full_url: str) -> str:
    """
    https://host/iiif/3/image-id/full/max/0/default.jpg
    → https://host/iiif/3/image-id
    """
    return IIIF_SUFFIX.sub("", full_url)


def flatten(el) -> str:
    return " ".join("".join(el.itertext()).split()) if el is not None else ""


def extract_figs(xml_path, out_csv="fig_manifest_input.csv"):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    body = root.find(".//body")
    if body is None:
        print("⚠️  No <body> element found — scanning entire document instead.")
        body = root

    rows = []
    seen_ids = defaultdict(int)

    for position, fig in enumerate(body.iter("fig"), start=1):
        fig_id   = fig.get("id", "").strip()
        fig_type = fig.get("fig-type", "").strip()
        label    = flatten(fig.find("label"))

        # Caption title + body text (kept separate for manifest label vs summary)
        caption_el = fig.find("caption")
        cap_title  = flatten(caption_el.find("title")) if caption_el is not None else ""
        cap_text   = flatten(caption_el) if caption_el is not None else ""

        # Extract all <ext-link> URLs from caption, split into licence vs credit
        handle  = ""
        licence = ""
        if caption_el is not None:
            for ext in caption_el.iter("ext-link"):
                if ext.get("ext-link-type") != "uri":
                    continue
                href = ext.get(f"{XLINK}href", "").strip()
                if not href:
                    continue
                if any(d in href for d in ("creativecommons.org", "rightsstatements.org")):
                    if not licence:
                        licence = href
                else:
                    if not handle:
                        handle = href

        # Graphics from <alternatives>
        online_url   = ""
        service_id   = ""
        archival_ref = ""

        alternatives = fig.find("alternatives")
        graphics_source = alternatives if alternatives is not None else fig

        for graphic in graphics_source.findall("graphic"):
            use  = graphic.get("specific-use", "")
            href = graphic.get(f"{XLINK}href", "").strip()

            if use == "online":
                online_url = href
                service_id = derive_service_id(href)
            elif use == "archival":
                archival_ref = href
            elif not use and not online_url:
                # Fallback: treat any https:// graphic as online
                if href.startswith("https://"):
                    online_url = href
                    service_id = derive_service_id(href)
                else:
                    archival_ref = archival_ref or href

        seen_ids[fig_id] += 1

        rows.append({
            "position":    position,
            "id":          fig_id,
            "fig_type":    fig_type,
            "label":       label,
            "cap_title":   cap_title,
            "cap_text":    cap_text,
            "handle":      handle,
            "licence":     licence,
            "online_url":  online_url,
            "service_id":  service_id,
            "archival":    archival_ref,
        })

    fieldnames = [
        "position", "id", "fig_type", "label",
        "cap_title", "cap_text", "handle", "licence",
        "online_url", "service_id", "archival",
    ]
    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Found {len(rows)} <fig> element(s) → {out_csv}")

    # Sanity checks
    dupes = {fid: n for fid, n in seen_ids.items() if n > 1}
    if dupes:
        print(f"\n⚠️  {len(dupes)} duplicate fig id(s):")
        for fid, n in sorted(dupes.items()):
            print(f"  {fid!r} appears {n}×")
    else:
        print("\n✓ All fig ids are unique.")

    no_online = [r for r in rows if not r["online_url"]]
    if no_online:
        no_online_ids = [r["id"] or "pos {}".format(r["position"]) for r in no_online]
        print(f"\n⚠️  {len(no_online)} fig(s) have no online/IIIF graphic "
              f"(ids: {no_online_ids})")
    else:
        print("✓ All figs have an online graphic URL.")

    no_service = [r for r in rows if r["online_url"] and not r["service_id"]]
    if no_service:
        no_service_ids = [r["id"] or "pos {}".format(r["position"]) for r in no_service]
        print(f"\n⚠️  {len(no_service)} fig(s) could not derive a service ID "
              f"(ids: {no_service_ids})")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "article.xml"
    out  = sys.argv[2] if len(sys.argv) > 2 else "fig_manifest_input.csv"
    extract_figs(path, out)
