#!/usr/bin/env python3
import json
from pathlib import Path

def main():
    root = Path(__file__).resolve().parents[2]
    manifest_path = root / 'figures' / 'peer_review' / 'figure_manifest.json'
    if not manifest_path.exists():
        print('Manifest not found:', manifest_path)
        return
    with open(manifest_path) as f:
        data = json.load(f)
    figures = data.get('figures', [])
    figures = sorted(figures, key=lambda m: m.get('filename','').lower())

    md_lines = []
    md_lines.append('# Figure Gallery (Canonical)\n')
    md_lines.append('Source: `figures/canonical_outputs/`\n')
    md_lines.append('')
    for m in figures:
        fn = m.get('filename','')
        canon = m.get('canonical_path','')
        w = m.get('width','')
        h = m.get('height','')
        rel = canon if canon else ('figures/canonical_outputs/' + fn)
        md_lines.append(f'- {fn} ({w}x{h}) — `{rel}`')
    md = '\n'.join(md_lines) + '\n'

    out1 = root / 'docs' / 'assets' / 'FIGURE_GALLERY.md'
    out1.parent.mkdir(parents=True, exist_ok=True)
    out1.write_text(md, encoding='utf-8')

    out2 = root / 'docs' / 'FIGURE_GALLERY.md'
    out2.write_text(md, encoding='utf-8')

    print('Wrote gallery to:', out1)
    print('Wrote gallery to:', out2)

if __name__ == '__main__':
    main()
