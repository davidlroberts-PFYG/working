#!/usr/bin/env python3
"""Assemble the Secure On Every Front refresh mock-ups.

Reads mockup/src/ (shared styles, footer text, one body file per page) and writes:
  mockup/<page>.html         linked pages that share mockup/assets/
  soef-<page>-mockup.html    one self-contained file per page, images inlined
"""
import base64, mimetypes, pathlib, re

here = pathlib.Path(__file__).parent
src = here / "mockup" / "src"
out = here / "mockup"

LIVE = "https://www.secureoneveryfront.com"
PAGES = {
    "home":    {"file": "index.html",                "single": "soef-home-mockup.html",    "label": "Home",
                "title": "Secure On Every Front | Business Value First for veteran business owners"},
    "pilot":   {"file": "business-value-first.html", "single": "soef-pilot-mockup.html",   "label": "Pilot page",
                "title": "Business Value First pilot | Secure On Every Front"},
    "applied": {"file": "applied.html",              "single": "soef-applied-mockup.html", "label": "Application received",
                "title": "Application received | Secure On Every Front"},
}

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title} (DRAFT MOCK-UP)</title>
<link rel="icon" href="assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600&family=Roboto:ital,wght@0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
<style>
{css}
</style>
</head>
<body>

<!-- ============ DRAFT BAR: belongs to this mock-up file only. Do not build in Squarespace. ============ -->
<div class="draftbar" role="region" aria-label="Mock-up status">
  <div class="wrap">
    <span><strong>DRAFT MOCK-UP</strong> &nbsp;Draft for the firm&rsquo;s CCO. Not signed off for publication.</span>
    <span class="pages">{pagelinks}</span>
    <button type="button" id="notesToggle" aria-pressed="false">Show review notes</button>
  </div>
</div>

<!-- ============ HEADER ============ -->
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="{{{{HOME}}}}" aria-label="Secure On Every Front home"><img src="assets/soef-logo.png" alt="Secure On Every Front" width="600" height="210"></a>
    <nav aria-label="Primary">
      <a class="text" href="{{{{PILOT}}}}"{pilot_current}>Business Value First</a>
      <a class="text" href="#program-note">The Program</a>
      <a class="text" href="{live}/david-teresa">Meet David &amp; Teresa</a>
      <a class="text" href="{live}/guides">Guides</a>
      <a class="text" href="{live}/faq">FAQ</a>
      <a class="btn btn--small" href="{{{{PILOT}}}}#apply">Apply for the pilot</a>
    </nav>
  </div>
</header>
"""

FOOT = """
<!-- ============ FOOTER ============ -->
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <img src="assets/soef-logo-white.png" alt="Secure On Every Front" width="750" height="262">
        <address>
          <a href="mailto:david@secureoneveryfront.com">david@secureoneveryfront.com</a><br>
          <a href="tel:+18556968284">+1 (855) 696-8284</a><br>
          Gulf Breeze, Florida
        </address>
      </div>
      <div>
        <h4>Secure On Every Front</h4>
        <ul>
          <li><a href="{{{{PILOT}}}}">Business Value First pilot</a></li>
          <li><a href="#program-note">The Program</a></li>
          <li><a href="{live}/review">Readiness Review</a></li>
          <li><a href="{live}/david-teresa">Meet David &amp; Teresa</a></li>
          <li><a href="{live}/guides">Money &amp; Mission Guides</a></li>
          <li><a href="{live}/faq">FAQ</a></li>
          <li><a href="{live}/contact">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Elsewhere</h4>
        <ul>
          <li><a href="https://planforyourgoals.link/VBOlab">VBO Lab community</a></li>
          <li><span class="placeholder">[YouTube channel link, once the channel exists]</span></li>
          <li><a href="https://www.linkedin.com/in/david-roberts-planforyourgoals/">LinkedIn</a></li>
          <li><a href="https://www.facebook.com/VeteranBusinessOwnerLab/">Facebook</a></li>
        </ul>
        <h4 style="margin-top:22px">Firm documents</h4>
        <ul>
          <li><a href="https://planforyourgoals.link/ADV">Form ADV Part 2A</a></li>
          <li><span class="placeholder">[Privacy Policy link]</span></li>
          <li><span class="placeholder">[Terms link]</span></li>
        </ul>
      </div>
    </div>
    <p class="note"><b>Footer note.</b> New here: the VBO Lab link, the YouTube slot, the Privacy Policy and Terms links (none was found on the live pages), and the david@ address in place of support@. Instagram is on the live footer and can stay; it is left out here only to keep the list short.</p>

    <div class="disclosure">
      <p>Secure On Every Front is an education and planning program for veteran business owners, co-founded by David Roberts and Teresa Roberts, Col (Ret.) USAF. Content from Secure On Every Front, the VBO Lab, and its online community is general education only and is not individualized investment, tax, or legal advice.</p>
{website_block}
    </div>
    <p class="note"><b>Disclosure note.</b> First paragraph: your SOEF block, first paragraph, word for word. The rest: your WEBSITE block as amended on 2026-11-19 for planforyourgoals.com, which you decided on 2026-11-20 to use on this site too. The firm email inside it is left as a marked placeholder; paste the block from your own disclosure file when you build.</p>
  </div>
</footer>

<script>
  (function () {{
    var btn = document.getElementById('notesToggle');
    btn.addEventListener('click', function () {{
      var on = document.body.classList.toggle('notes-on');
      btn.setAttribute('aria-pressed', on ? 'true' : 'false');
      btn.textContent = on ? 'Hide review notes' : 'Show review notes';
    }});
    if (/[?&#]notes\\b/.test(location.search + location.hash)) btn.click();
  }})();
</script>
</body>
</html>
"""


def page(key, linkmap):
    meta = PAGES[key]
    css = (src / "styles.css").read_text(encoding="utf-8")
    body = (src / f"{key}.body.html").read_text(encoding="utf-8")
    block = (src / "website-block.html").read_text(encoding="utf-8")
    block = "\n".join("      " + line for line in block.splitlines())
    links = "".join(
        f'<a href="{{{{{k.upper()}}}}}"' + (' aria-current="page"' if k == key else "") + f'>{v["label"]}</a>'
        for k, v in PAGES.items()
    )
    html = HEAD.format(title=meta["title"], css=css, pagelinks=links, live=LIVE,
                       pilot_current=' aria-current="page"' if key == "pilot" else "")
    html += body.replace("{live}", LIVE)
    html += FOOT.format(live=LIVE, website_block=block)
    for k, target in linkmap.items():
        html = html.replace("{{" + k.upper() + "}}", target)
    return html


def inline(html):
    def repl(m):
        path = out / m.group(2)
        mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        return f'{m.group(1)}="data:{mime};base64,{base64.b64encode(path.read_bytes()).decode("ascii")}"'
    return re.sub(r'(src|href)="(assets/[^"]+)"', repl, html)


for key, meta in PAGES.items():
    multi = page(key, {k: v["file"] for k, v in PAGES.items()})
    (out / meta["file"]).write_text(multi, encoding="utf-8")
    single = inline(page(key, {k: v["single"] for k, v in PAGES.items()}))
    (here / meta["single"]).write_text(single, encoding="utf-8")
    print(f'{meta["file"]:28} {len(multi) // 1024:4} KB   {meta["single"]:26} {len(single) // 1024:5} KB')
