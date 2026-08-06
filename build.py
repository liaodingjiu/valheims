#!/usr/bin/env python3
"""
Build system for Valheim Guides.
Reads source pages from pages/ and template fragments from _templates/,
replaces <!-- #include filename --> markers, outputs final HTML to root.
Auto-submits changed URLs to Bing via IndexNow.
"""
import re
import os
import json
import datetime
import urllib.request
from pathlib import Path

TEMPLATE_DIR = "_templates"
PAGES_DIR = "pages"
OUTPUT_DIR = "."

INCLUDE_RE = re.compile(r'<!-- #include (.+?) -->')

THEME_HEAD_SCRIPT = ("<script>(function(){try{var t=localStorage.getItem('valheim-theme');"
                     "if(t)document.documentElement.setAttribute('data-theme',t);}catch(e){}})();</script>")

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

def inject_theme_script(content):
    """Apply the saved theme before first paint to avoid a flash of the wrong theme."""
    marker = '<link rel="stylesheet" href="shared.css">'
    if marker in content:
        return content.replace(marker, THEME_HEAD_SCRIPT + marker, 1)
    return content.replace("<head>", "<head>\n" + THEME_HEAD_SCRIPT, 1)

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

        output = inject_theme_script(resolve_includes(content, src.name))

        out_path = Path(OUTPUT_DIR) / src.name
        with open(out_path, 'w') as f:
            f.write(output)

        count += 1
        print(f"  ✓ {src.name}")

    print(f"\nBuilt {count} files → {OUTPUT_DIR}/")

    # Refresh sitemap lastmod so search engines re-crawl changed pages
    try:
        update_sitemap()
    except Exception as e:
        print(f"  ⚠ sitemap: {e}")

    # Notify Bing via IndexNow
    try:
        submit_indexnow(count)
    except Exception as e:
        print(f"  ⚠ IndexNow: {e}")

    return 0

def update_sitemap():
    path = Path(OUTPUT_DIR) / "sitemap.xml"
    s = path.read_text(encoding="utf-8")

    def clean_loc(m):
        loc = m.group(1).strip()
        if loc.startswith("/https://"):
            loc = loc[1:]  # repair a previously broken relative URL
        elif loc.startswith("/"):
            loc = "https://valheims.com" + loc
        return f"<loc>{loc}</loc>"

    today = datetime.date.today().isoformat()
    s = re.sub(r"<loc>(.*?)</loc>", clean_loc, s)
    s = re.sub(r"<lastmod>[^<]*</lastmod>", f"<lastmod>{today}</lastmod>", s)
    path.write_text(s, encoding="utf-8")
    print(f"  ✓ sitemap.xml updated ({today})")

def submit_indexnow(count):
    urls = [
        "https://valheims.com/sitemap.xml",
        "https://valheims.com/",
        "https://valheims.com/progression/",
        "https://valheims.com/biomes/",
        "https://valheims.com/multiplayer/",
        "https://valheims.com/boss-order",
        "https://valheims.com/best-weapons",
        "https://valheims.com/beginner-guide",
        "https://valheims.com/building-guide",
        "https://valheims.com/biome-guide",
        "https://valheims.com/server-setup",
        "https://valheims.com/crossplay-guide",
    ]
    data = json.dumps({
        "host": "valheims.com",
        "key": "a9d39cb1bcb44ac19886b900940fbb5a",
        "keyLocation": "https://valheims.com/a9d39cb1bcb44ac19886b900940fbb5a.txt",
        "urlList": urls
    }).encode('utf-8')

    req = urllib.request.Request(
        'https://www.bing.com/indexnow',
        data=data,
        headers={'Content-Type': 'application/json; charset=utf-8'}
    )
    resp = urllib.request.urlopen(req, timeout=10)
    if resp.status == 200 or resp.status == 202:
        print(f"  ✓ IndexNow: {len(urls)} URLs submitted to Bing")
    else:
        print(f"  ⚠ IndexNow: HTTP {resp.status}")

if __name__ == '__main__':
    exit(build())
