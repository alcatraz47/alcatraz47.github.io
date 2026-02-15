#!/usr/bin/env python3
from __future__ import annotations

import email.utils
import html
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import List

FEED_URL = "https://medium.com/feed/@arfanmahmud47"
POSTS_DIR = Path("_posts")
MAX_POSTS = 30

FALLBACK_POSTS = [
    {
        "title": "Build OpenCV 4 from Source with GStreamer (Ubuntu/Zorin/Peppermint)",
        "link": "https://medium.com/@arfanmahmud47/build-opencv-4-from-source-with-gstreamer-ubuntu-zorin-peppermint-c2cff5393ef",
        "date": datetime(2020, 8, 12, 12, 0, 0, tzinfo=timezone.utc),
        "summary": "A practical walkthrough for compiling OpenCV 4 from source with GStreamer support, including dependency setup and build troubleshooting on Linux distributions.",
        "tags": ["opencv", "gstreamer", "linux"],
    },
    {
        "title": "FSCK error code 4 and BusyBox boot block: how I fixed it",
        "link": "https://medium.com/@arfanmahmud47/fsck-error-code-4-and-your-pc-laptop-gets-blocked-in-busybox-while-booting-just-like-mine-7b3215cd38f1",
        "date": datetime(2020, 7, 28, 12, 0, 0, tzinfo=timezone.utc),
        "summary": "A concise recovery guide for BusyBox boot failures caused by fsck error code 4, with practical repair steps and safety notes.",
        "tags": ["linux", "fsck", "troubleshooting"],
    },
    {
        "title": "How to Repair Windows 10 Boot after partition resizing mistakes",
        "link": "https://medium.com/@arfanmahmud47/how-to-repair-windows-10-boot-after-making-annoying-mistake-like-me-while-shrinking-extending-3b9bb724f06",
        "date": datetime(2020, 7, 19, 12, 0, 0, tzinfo=timezone.utc),
        "summary": "A step-by-step account of restoring Windows 10 boot after partition changes, focused on reliable recovery actions and pitfalls to avoid.",
        "tags": ["windows", "boot-repair", "troubleshooting"],
    },
]



def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "medium-post"


def strip_html(raw: str) -> str:
    raw = re.sub(r"<br\s*/?>", "\n", raw, flags=re.I)
    raw = re.sub(r"</p>\s*<p[^>]*>", "\n\n", raw, flags=re.I)
    raw = re.sub(r"<[^>]+>", "", raw)
    raw = html.unescape(raw)
    raw = raw.replace("\xa0", " ")
    raw = re.sub(r"\n{3,}", "\n\n", raw)
    return raw.strip()


def first_paragraph(text: str) -> str:
    parts = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    return parts[0] if parts else text.strip()


def clean_link(link: str) -> str:
    link = link.strip()
    # remove tracking query params for stable canonical links
    link = re.sub(r"\?source=.*$", "", link)
    return link


def parse_feed(xml_bytes: bytes) -> List[dict]:
    root = ET.fromstring(xml_bytes)
    items = root.findall("./channel/item")
    posts = []
    for item in items[:MAX_POSTS]:
        title = (item.findtext("title") or "").strip()
        link = clean_link(item.findtext("link") or "")
        if not title or not link:
            continue

        pub_date_text = (item.findtext("pubDate") or "").strip()
        dt = email.utils.parsedate_to_datetime(pub_date_text)
        if dt is None:
            dt = datetime.now(timezone.utc)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        dt_utc = dt.astimezone(timezone.utc)

        description = item.findtext("description") or ""
        summary = first_paragraph(strip_html(description))

        tags = [
            (cat.text or "").strip()
            for cat in item.findall("category")
            if (cat.text or "").strip()
        ]

        link_slug = slugify(link.rsplit("/", 1)[-1])
        filename = f"{dt_utc:%Y-%m-%d}-{link_slug}.md"

        posts.append(
            {
                "title": title,
                "link": link,
                "date": dt_utc,
                "summary": summary,
                "tags": tags,
                "filename": filename,
            }
        )
    return posts


def yaml_quote(text: str) -> str:
    text = text.replace('"', '\\"')
    return f'"{text}"'


def render_post(post: dict) -> str:
    date_str = post["date"].strftime("%Y-%m-%d %H:%M:%S +0000")
    lines = [
        "---",
        f"title: {yaml_quote(post['title'])}",
        f"date: {date_str}",
        "categories: [medium]",
    ]
    if post["tags"]:
        quoted = ", ".join(yaml_quote(t) for t in post["tags"])
        lines.append(f"tags: [{quoted}]")
    lines.extend(
        [
            f"link: {post['link']}",
            "---",
            "",
            post["summary"],
            "",
            f"Read on Medium: {post['link']}",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    try:
        with urllib.request.urlopen(FEED_URL, timeout=30) as resp:
            xml_bytes = resp.read()
        posts = parse_feed(xml_bytes)
        source = "rss"
    except Exception as exc:
        posts = []
        for item in FALLBACK_POSTS:
            link_slug = slugify(item["link"].rsplit("/", 1)[-1])
            filename = f"{item['date']:%Y-%m-%d}-{link_slug}.md"
            p = dict(item)
            p["filename"] = filename
            posts.append(p)
        source = f"fallback ({exc})"
    written = 0
    for post in posts:
        target = POSTS_DIR / post["filename"]
        content = render_post(post)
        if target.exists() and target.read_text(encoding="utf-8") == content:
            continue
        target.write_text(content, encoding="utf-8")
        written += 1

    print(f"Parsed {len(posts)} Medium posts from {source}; wrote/updated {written} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
