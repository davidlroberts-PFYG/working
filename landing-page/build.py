#!/usr/bin/env python3
"""Inline the images in mockup/index.html so the mock-up opens as one self-contained file."""
import base64, mimetypes, pathlib, re

root = pathlib.Path(__file__).parent / "mockup"
html = (root / "index.html").read_text(encoding="utf-8")

def inline(match):
    path = root / match.group(2)
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return f'{match.group(1)}="data:{mime};base64,{data}"'

out = re.sub(r'(src|href)="(assets/[^"]+)"', inline, html)
target = root.parent / "planforyourgoals-landing-mockup.html"
target.write_text(out, encoding="utf-8")
print(f"wrote {target.name} ({len(out) // 1024} KB)")
