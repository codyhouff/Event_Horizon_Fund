#!/usr/bin/env python3
"""Convert a markdown file to a styled PDF using markdown + weasyprint.

Usage:
    python3 md_to_pdf.py                          # converts default file
    python3 md_to_pdf.py "My Document.md"         # converts specified file
    python3 md_to_pdf.py input.md output.pdf      # custom output path

Requirements (install once):
    brew install pango glib python@3
    /opt/homebrew/bin/python3 -m pip install --break-system-packages --user markdown weasyprint

Note: Use homebrew's Python (/opt/homebrew/bin/python3) rather than the
system Python, as weasyprint needs homebrew's pango/glib libraries.
"""
import sys
import os
import markdown

INPUT = sys.argv[1] if len(sys.argv) > 1 else "Event Horizon Fund Deep Dive Analysis 3-31-26.md"
OUTPUT = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(INPUT)[0] + ".pdf"

with open(INPUT, "r", encoding="utf-8") as f:
    md_text = f.read()

html_body = markdown.markdown(
    md_text,
    extensions=["tables", "fenced_code", "toc", "sane_lists"],
)

CSS = """
@page {
    size: letter;
    margin: 0.7in 0.8in;
    @bottom-center {
        content: counter(page);
        font-size: 9pt;
        color: #888;
    }
}
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.52;
    color: #1a1a1a;
}
h1 {
    font-size: 21pt;
    margin-top: 0.25in;
    margin-bottom: 0.12in;
    color: #0d1117;
    border-bottom: 2.5px solid #1a1a2e;
    padding-bottom: 6px;
    page-break-after: avoid;
}
h2 {
    font-size: 15pt;
    margin-top: 0.3in;
    margin-bottom: 0.1in;
    color: #1a1a1a;
    border-bottom: 1px solid #d0d0d0;
    padding-bottom: 4px;
    page-break-after: avoid;
}
h3 {
    font-size: 12.5pt;
    margin-top: 0.18in;
    margin-bottom: 0.06in;
    color: #222;
    page-break-after: avoid;
}
h4 {
    font-size: 11pt;
    margin-top: 0.12in;
    margin-bottom: 0.05in;
    color: #333;
    page-break-after: avoid;
}
p { margin: 0.05in 0; }
strong { color: #000; }
table {
    border-collapse: collapse;
    width: 100%;
    margin: 0.1in 0;
    font-size: 8.8pt;
    line-height: 1.35;
    page-break-inside: auto;
}
thead { display: table-header-group; }
tr { page-break-inside: avoid; }
th {
    background-color: #1a1a2e;
    color: #ffffff;
    font-weight: 600;
    text-align: left;
    padding: 5px 6px;
    border: 1px solid #2a2a3e;
}
th, th * {
    color: #ffffff !important;
}
th a {
    color: #ffffff !important;
    text-decoration: none;
}
td {
    padding: 4px 6px;
    border: 1px solid #d0d0d0;
    vertical-align: top;
}
tr:nth-child(even) { background-color: #f6f6f8; }
code {
    font-family: 'SF Mono', 'Menlo', 'Monaco', 'Courier New', monospace;
    font-size: 8.5pt;
    background-color: #f0f0f0;
    padding: 1px 3px;
    border-radius: 3px;
}
pre {
    background-color: #1e1e2e;
    color: #cdd6f4;
    padding: 10px 14px;
    border-radius: 5px;
    overflow-x: auto;
    font-size: 7.5pt;
    line-height: 1.4;
    white-space: pre-wrap;
    word-wrap: break-word;
    page-break-inside: avoid;
}
pre code { background: none; padding: 0; color: inherit; font-size: inherit; }
hr {
    border: none;
    border-top: 1px solid #ddd;
    margin: 0.18in 0;
}
ul, ol { margin: 0.05in 0; padding-left: 0.28in; }
li { margin-bottom: 2px; }
blockquote {
    border-left: 3px solid #4a90d9;
    margin: 0.08in 0;
    padding: 0.04in 0.12in;
    background: #f0f4ff;
    color: #333;
}
"""

full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>{CSS}</style>
</head>
<body>
{html_body}
</body>
</html>"""

print(f"Converting {INPUT} to PDF...")
from weasyprint import HTML
HTML(string=full_html).write_pdf(OUTPUT)
file_size = os.path.getsize(OUTPUT)
print(f"PDF written to {OUTPUT} ({file_size / 1024:.0f} KB)")
