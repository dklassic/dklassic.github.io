#!/usr/bin/env python3
"""Convert Hugo markdown faq.md and tech-fixes.md files to BBCode.

Usage:
    python md_to_bbcode.py <content_root> <output_dir>

Scans <content_root> for all first-level subdirectories (each represents a game),
and for each game converts faq.md and tech-fixes.md into BBCode files placed under:
    <output_dir>/<game>/faq.bbcode
    <output_dir>/<game>/tech-fixes.bbcode
"""

import re
import sys
import os
from pathlib import Path


# ---------------------------------------------------------------------------
# Markdown -> BBCode conversion helpers
# ---------------------------------------------------------------------------

def strip_frontmatter(text: str) -> str:
    """Remove Hugo YAML front matter delimited by ---."""
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            return text[end + 3:].lstrip("\n")
    return text


def strip_html_comments(text: str) -> str:
    """Remove HTML/Hugo comments <!-- ... -->."""
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def convert_headings(text: str) -> str:
    """Convert Markdown headings to BBCode [h1]-[h3] style (Steam uses [h1]-[h3])."""
    # Process from deepest heading first to avoid false matches
    text = re.sub(r"^### (.+)$", r"[h3]\1[/h3]", text, flags=re.MULTILINE)
    text = re.sub(r"^## (.+)$",  r"[h2]\1[/h2]", text, flags=re.MULTILINE)
    text = re.sub(r"^# (.+)$",   r"[h1]\1[/h1]", text, flags=re.MULTILINE)
    return text


def convert_bold_italic(text: str) -> str:
    """Convert ***text***, **text**, and *text* to BBCode."""
    # Bold + italic: ***...***
    text = re.sub(r"\*\*\*(.+?)\*\*\*", r"[b][i]\1[/i][/b]", text)
    # Bold: **...**
    text = re.sub(r"\*\*(.+?)\*\*", r"[b]\1[/b]", text)
    # Italic: *...*  (but not list bullets — those are handled separately)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"[i]\1[/i]", text)
    return text


def convert_inline_code(text: str) -> str:
    """Convert `code` to [code]...[/code] (single-line inline)."""
    return re.sub(r"`([^`\n]+)`", r"[code]\1[/code]", text)


def convert_links(text: str) -> str:
    """Convert [label](url) to [url=url]label[/url]."""
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"[url=\2]\1[/url]", text)


def convert_bare_urls(text: str) -> str:
    """Wrap bare http/https URLs in [url]...[/url], skipping those already
    inside a [url=...] attribute or already wrapped in [url]...[/url]."""
    # Split on existing BBCode url tags so we only touch the text segments
    # between them.  Pattern matches both [url=...]...[/url] and [url]...[/url].
    bbcode_url_pattern = re.compile(
        r'(\[url(?:=[^\]]+)?\].*?\[/url\])', re.DOTALL
    )
    parts = bbcode_url_pattern.split(text)
    result = []
    for part in parts:
        if bbcode_url_pattern.fullmatch(part):
            # Already a BBCode url tag — leave untouched
            result.append(part)
        else:
            # Plain text segment — wrap any bare URLs
            result.append(
                re.sub(r'(https?://[^\s\[\]"<>]+)', r'[url]\1[/url]', part)
            )
    return "".join(result)


def convert_lists(text: str) -> str:
    """Convert Markdown unordered and ordered lists to BBCode [list].

    Handles simple flat lists.  Indented continuation lines that belong to a
    list item (i.e. lines indented with 4+ spaces immediately after a list
    item) are appended to the preceding [*] entry so the list tag is not
    prematurely closed.
    """
    lines = text.split("\n")
    result = []
    in_list = False
    list_type = None  # "ul" or "ol"

    i = 0
    while i < len(lines):
        line = lines[i]

        # Detect unordered list item at column 0 (leading -, *, or +)
        ul_match = re.match(r"^[-*+] (.+)$", line)
        # Detect ordered list item at column 0
        ol_match = re.match(r"^\d+\. (.+)$", line)
        # Indented continuation line (4+ spaces) — treated as part of the
        # current list item when we are inside a list
        indent_match = re.match(r"^    (.*)$", line) if in_list else None

        if ul_match:
            if not in_list or list_type != "ul":
                if in_list:
                    result.append("[/list]")
                result.append("[list]")
                in_list = True
                list_type = "ul"
            result.append(f"[*]{ul_match.group(1)}")
        elif ol_match:
            if not in_list or list_type != "ol":
                if in_list:
                    result.append("[/list]")
                result.append("[list=1]")
                in_list = True
                list_type = "ol"
            result.append(f"[*]{ol_match.group(1)}")
        elif indent_match and in_list:
            # Continuation of the current list item — append inline
            content = indent_match.group(1)
            if content:
                # Attach to the last [*] line
                result[-1] = result[-1] + "\n" + content
            # Blank indented lines are silently dropped
        else:
            if in_list and line.strip() == "":
                # A blank line *might* separate items; peek ahead to see if
                # the next non-blank line is still a list item of the same type.
                j = i + 1
                while j < len(lines) and lines[j].strip() == "":
                    j += 1
                if j < len(lines):
                    next_line = lines[j]
                    next_ul = re.match(r"^[-*+] ", next_line)
                    next_ol = re.match(r"^\d+\. ", next_line)
                    next_indent = re.match(r"^    ", next_line)
                    if (list_type == "ul" and next_ul) or \
                       (list_type == "ol" and next_ol) or \
                       next_indent:
                        # Keep the list open; skip the blank line(s)
                        i = j
                        continue
                # No matching continuation — close the list
                result.append("[/list]")
                in_list = False
                list_type = None
                result.append(line)
            else:
                if in_list:
                    result.append("[/list]")
                    in_list = False
                    list_type = None
                result.append(line)

        i += 1

    if in_list:
        result.append("[/list]")

    return "\n".join(result)


def convert_blockquote(text: str) -> str:
    """Convert > blockquotes to [quote]...[/quote]."""
    lines = text.split("\n")
    result = []
    in_quote = False

    for line in lines:
        if line.startswith("> ") or line == ">":
            if not in_quote:
                result.append("[quote]")
                in_quote = True
            result.append(line[2:] if line.startswith("> ") else "")
        else:
            if in_quote:
                result.append("[/quote]")
                in_quote = False
            result.append(line)

    if in_quote:
        result.append("[/quote]")

    return "\n".join(result)


def clean_up(text: str) -> str:
    """Final cleanup: collapse excessive blank lines."""
    # Collapse 3+ consecutive blank lines into 2
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def markdown_to_bbcode(md_text: str) -> str:
    text = strip_frontmatter(md_text)
    text = strip_html_comments(text)
    text = convert_headings(text)
    text = convert_bold_italic(text)
    text = convert_inline_code(text)
    text = convert_links(text)
    text = convert_bare_urls(text)
    text = convert_lists(text)
    text = convert_blockquote(text)
    text = clean_up(text)
    return text


# ---------------------------------------------------------------------------
# File discovery and main
# ---------------------------------------------------------------------------

TARGET_FILES = {"faq.md", "tech-fixes.md"}


def process_content_root(content_root: Path, output_dir: Path):
    """Walk each game subfolder under content_root and convert target files."""
    changed_files = []

    for game_dir in sorted(content_root.iterdir()):
        if not game_dir.is_dir():
            continue
        # Skip Hugo posts/meta directories
        if game_dir.name.startswith(".") or game_dir.name == "posts":
            continue

        for filename in TARGET_FILES:
            src = game_dir / filename
            if not src.exists():
                continue

            md_text = src.read_text(encoding="utf-8")
            bbcode = markdown_to_bbcode(md_text)

            stem = filename.replace(".md", "")
            out_path = output_dir / game_dir.name / f"{stem}.bbcode"
            out_path.parent.mkdir(parents=True, exist_ok=True)

            # Only report as changed if content actually differs
            if out_path.exists() and out_path.read_text(encoding="utf-8") == bbcode:
                print(f"  [unchanged] {out_path.relative_to(output_dir.parent)}")
            else:
                out_path.write_text(bbcode, encoding="utf-8")
                print(f"  [written]   {out_path.relative_to(output_dir.parent)}")
                changed_files.append(str(out_path))

    return changed_files


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <content_root> <output_dir>")
        sys.exit(1)

    content_root = Path(sys.argv[1]).resolve()
    output_dir = Path(sys.argv[2]).resolve()

    if not content_root.exists():
        print(f"Error: content root '{content_root}' does not exist.")
        sys.exit(1)

    print(f"Scanning: {content_root}")
    print(f"Output:   {output_dir}\n")

    changed = process_content_root(content_root, output_dir)

    print(f"\nDone. {len(changed)} file(s) written/updated.")


if __name__ == "__main__":
    main()
