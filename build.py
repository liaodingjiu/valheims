#!/usr/bin/env python3
"""
Build system for Valheim Guides.
Reads source pages from pages/ and template fragments from _templates/,
replaces <!-- #include filename --> markers, outputs final HTML to root.
"""
import re
import os
from pathlib import Path

TEMPLATE_DIR = "_templates"
PAGES_DIR = "pages"
OUTPUT_DIR = "."

INCLUDE_RE = re.compile(r'<!-- #include (.+?) -->')

def load_template(name):
    path = os.path.join(TEMPLATE_DIR, name)
    if os.path.exists(path):
        with open(path, 'r') as f:
            return f.read().strip()
    raise FileNotFoundError(f"Template not found: {path}")

def resolve_includes(content, page_name):
    def replacer(match):
        tmpl_name = match.group(1)
        return load_template(tmpl_name)
    return INCLUDE_RE.sub(replacer, content)

def build():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    pages = sorted(Path(PAGES_DIR).glob('*.html'))
    if not pages:
        print("ERROR: No source files found in pages/")
        return 1

    count = 0
    for src in pages:
        with open(src, 'r') as f:
            content = f.read()

        output = resolve_includes(content, src.name)

        out_path = Path(OUTPUT_DIR) / src.name
        with open(out_path, 'w') as f:
            f.write(output)

        count += 1
        print(f"  ✓ {src.name}")

    print(f"\nBuilt {count} files → {OUTPUT_DIR}/")
    return 0

if __name__ == '__main__':
    exit(build())
