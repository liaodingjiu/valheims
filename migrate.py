#!/usr/bin/env python3
"""
Migrate existing HTML files to use include markers.
Uses regex to match blocks (handles formatting/text variations).
"""
import re
import os
from pathlib import Path

TEMPLATE_DIR = "_templates"
PAGES_DIR = "pages"

# Regex patterns for common blocks (ordered bottom-to-top)
BLOCKS = [
    # (name, pattern, template_file)
    # Must match from bottom of page upward to avoid position shifts
    ('scripts', r'<button class="back-top".*?(?=</body>)', None),  # dynamic template (lookahead preserves </body>)
    ('sidebar', r'<aside class="sidebar">.*?</aside>', None),   # dynamic template
    ('footer', r'<footer>.*?</footer>', None),                   # dynamic template
    ('nav', r'<nav aria-label="Main navigation">.*?</nav>', None),  # dynamic template
    ('clarity', r'<script type="text/javascript">\s*\(function\(c,l,a,r,i,t,y\).*?</script>', 'clarity.html'),
]

# Category → sidebar template mapping
SIDEBAR_MAP = {
    'bosses': ['boss-order', 'eikthyr', 'elder', 'bonemass', 'moder', 'yagluth', 'queen', 'fader'],
    'equipment': ['best-weapons', 'armor', 'food-recipes'],
    'world': ['biome', 'base-locations', 'ashlands', 'deep-north', 'sailing', 'traders', 'farming'],
    'survival': ['building', 'base-defense', 'taming', 'beginner'],
    'technical': ['server-setup', 'crossplay', 'known-issues', 'mods', 'console', 'multiplayer'],
}

HUB_MAP = {
    'guides-bosses': 'bosses', 'guides-equipment': 'equipment',
    'guides-world': 'world', 'guides-survival': 'survival', 'guides-technical': 'technical',
}

def get_sidebar_category(filename):
    base = filename.replace('.html', '')
    if base in HUB_MAP:
        return HUB_MAP[base]
    for cat, keywords in SIDEBAR_MAP.items():
        for kw in keywords:
            if kw in base:
                return cat
    return None

def get_footer_template(content):
    """Determine footer variant from content."""
    if 'Valheim and all related content are trademarks of Iron Gate Studio' in content:
        return 'footer-full.html'
    return 'footer-guide.html'

def get_scripts_template(content):
    """Determine scripts variant from content."""
    if 'handleFeedback' in content:
        return 'scripts-full.html'
    # Check indentation style
    m = re.search(r'<button class="back-top".*?\n', content)
    if m and '\n  ' in m.group(0):
        return 'scripts-contact.html'  # multiline style (about/contact/privacy/terms)
    return 'scripts-guide.html'

def get_nav_template(content):
    """Determine nav variant."""
    # Simple nav has 6 flat links without dropdown-menu
    if 'dropdown-menu' not in re.search(r'<nav aria-label="Main navigation">.*?</nav>', content, re.DOTALL).group(0):
        return 'nav-simple.html'
    return 'nav-full.html'

def load_template(name):
    path = os.path.join(TEMPLATE_DIR, name)
    if os.path.exists(path):
        with open(path, 'r') as f:
            return f.read().strip()
    return None

def migrate_file(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, 'r') as f:
        content = f.read()

    original = content
    results = []

    # Process blocks in reverse order (bottom of page first)
    for block_name, pattern, default_tmpl in BLOCKS:
        m = re.search(pattern, content, re.DOTALL)
        if not m:
            results.append((block_name, False, 'not found'))
            continue

        matched_text = m.group(0)

        # Determine which template to use
        if block_name == 'nav':
            tmpl_file = get_nav_template(content)
            # For Phase 2: preserve current nav text
            # Save the matched text as the actual template
            tmpl_path = os.path.join(TEMPLATE_DIR, tmpl_file)
            # Don't overwrite - keep what we extracted earlier
        elif block_name == 'footer':
            tmpl_file = get_footer_template(content)
        elif block_name == 'scripts':
            tmpl_file = get_scripts_template(content)
        elif block_name == 'sidebar':
            cat = get_sidebar_category(filename)
            if cat:
                tmpl_file = f'sidebar-{cat}.html'
            else:
                results.append((block_name, False, 'no category'))
                continue
        else:
            tmpl_file = default_tmpl

        # Replace with include marker
        content = content[:m.start()] + f'<!-- #include {tmpl_file} -->' + content[m.end():]
        results.append((block_name, True, tmpl_file))

    if content == original:
        return filename, False, "no changes"

    out_path = os.path.join(PAGES_DIR, filename)
    with open(out_path, 'w') as f:
        f.write(content)

    replaced = [r[0] for r in results if r[1]]
    failed = [r[0] for r in results if not r[1]]
    msg = f"replaced: {', '.join(replaced)}"
    if failed:
        msg += f" | MISSING: {', '.join(failed)}"
    return filename, True, msg


def main():
    os.makedirs(PAGES_DIR, exist_ok=True)
    html_files = sorted(Path('.').glob('*.html'))
    print(f"Migrating {len(html_files)} HTML files...\n")

    success, fail = 0, 0
    for fp in html_files:
        fname, ok, msg = migrate_file(str(fp))
        if ok:
            success += 1
        else:
            fail += 1
        print(f"  {'✓' if ok else '✗'} {fname} — {msg}")

    print(f"\nDone: {success} migrated, {fail} unchanged")
    print(f"Source files: {PAGES_DIR}/")
    print(f"Templates: {TEMPLATE_DIR}/")

if __name__ == '__main__':
    main()
