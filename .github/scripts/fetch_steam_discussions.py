#!/usr/bin/env python3
"""
Crawls new Steam game discussion posts from the forum page and outputs them
as a JSON array for use in GitHub Actions matrix strategy.

Usage:
    python fetch_steam_discussions.py <DISCUSSIONS_URL> <STATE_FILE>

    DISCUSSIONS_URL  Full URL to the Steam discussions page, e.g.:
                     https://steamcommunity.com/app/3718870/discussions/
    STATE_FILE       Path to a file that persists seen topic IDs between runs.

Outputs (to stdout):
    JSON array of {"title": ..., "url": ...} objects for new topics.
    Writes updated seen IDs back to STATE_FILE.
"""

import sys
import json
import re
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

DISCUSSIONS_URL = sys.argv[1].rstrip("/") + "/"
STATE_FILE = Path(sys.argv[2])

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}


class ForumParser(HTMLParser):
    """Extracts forum topics from the Steam discussions page HTML."""

    def __init__(self):
        super().__init__()
        self.topics = []          # list of {"id", "title", "url"}
        self._in_topic = False
        self._in_name_div = False
        self._in_label_span = False
        self._current = {}
        self._name_depth = 0
        self._label_text = ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        # Detect a forum_topic div
        if tag == "div":
            classes = attrs.get("class", "")
            el_id = attrs.get("id", "")
            if "forum_topic" in classes and "data-gidforumtopic" in attrs:
                self._in_topic = True
                self._current = {
                    "id": attrs.get("data-gidforumtopic", ""),
                    "title": "",
                    "url": "",
                }
                return

        if not self._in_topic:
            return

        # Grab the overlay link URL
        if tag == "a" and "forum_topic_overlay" in attrs.get("class", ""):
            self._current["url"] = attrs.get("href", "")
            return

        # Detect the title div
        if tag == "div" and "forum_topic_name" in attrs.get("class", ""):
            self._in_name_div = True
            self._name_depth = 1
            return

        # Detect the "PINNED:" label span inside the title div
        if self._in_name_div and tag == "span" and "forum_topic_label" in attrs.get("class", ""):
            self._in_label_span = True
            self._label_text = ""
            return

        # Track nesting depth inside the name div
        if self._in_name_div:
            self._name_depth += 1

    def handle_endtag(self, tag):
        if not self._in_topic:
            return

        if self._in_label_span and tag == "span":
            self._in_label_span = False
            return

        if self._in_name_div:
            if tag == "div":
                self._name_depth -= 1
                if self._name_depth <= 0:
                    self._in_name_div = False
                    # Finalise topic
                    topic = self._current.copy()
                    topic["title"] = topic["title"].strip()
                    if topic["id"] and topic["title"] and topic["url"]:
                        self.topics.append(topic)
                    self._in_topic = False
                    self._current = {}

    def handle_data(self, data):
        if not self._in_topic:
            return

        if self._in_label_span:
            # Skip label text like "PINNED:"
            return

        if self._in_name_div:
            self._current["title"] += data


def fetch_html(url: str) -> str:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read().decode("utf-8", errors="replace")


def main():
    # Load seen topic IDs
    if STATE_FILE.exists():
        seen_ids = set(STATE_FILE.read_text().splitlines())
    else:
        seen_ids = set()

    html = fetch_html(DISCUSSIONS_URL)
    parser = ForumParser()
    parser.feed(html)

    new_topics = []
    all_ids = set()

    for topic in parser.topics:
        tid = topic["id"]
        all_ids.add(tid)
        if tid not in seen_ids:
            new_topics.append({"title": topic["title"], "url": topic["url"]})

    # Persist: union of previously seen + everything on page now
    updated_ids = seen_ids | all_ids
    STATE_FILE.write_text("\n".join(sorted(updated_ids)))

    print(json.dumps(new_topics))


if __name__ == "__main__":
    main()
