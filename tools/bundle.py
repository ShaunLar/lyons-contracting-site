#!/usr/bin/env python3
"""Bundle the 16-page Lyons site into ONE self-contained artifact page.

Each page's <body> is stored as an inert template; a tiny hash router swaps them
on nav clicks so the whole demo works from a single shareable URL.
"""
import re, os, json, html

SRC = "/Users/shaunlaranjeira/Claude/Websites/lyons-contracting"
OUT = "/private/tmp/claude-501/-Users-shaunlaranjeira-Claude-Websites-lyons-contracting/b2cbae5c-14a9-4563-83ec-4829ff10884b/scratchpad/lyons-demo.html"

PAGES = ["index.html", "roof-replacement.html", "roof-repair.html", "storm-damage.html",
         "emergency.html", "roof-cost.html", "gallery.html", "about.html", "contact.html",
         "alexandria.html", "arlington.html", "falls-church.html", "mclean.html",
         "springfield.html", "fairfax.html", "404.html"]

css = open(os.path.join(SRC, "css/styles.css")).read()
js = open(os.path.join(SRC, "js/main.js")).read()

# Turn the IIFE into a re-runnable init so listeners rebind after each page swap.
assert "(function () {" in js, "unexpected js wrapper"
js = js.replace("(function () {", "window.__lyonsInit = function () {", 1)
js = js.rstrip()
assert js.endswith("})();"), "unexpected js tail"
js = js[:-len("})();")] + "};"

# Inline images as data URIs — the artifact must be one self-contained file.
import base64, glob
IMG = {}
for f in sorted(glob.glob(os.path.join(SRC, "images", "*.jpg"))):
    name = "images/" + os.path.basename(f)
    IMG[name] = "data:image/jpeg;base64," + base64.b64encode(open(f, "rb").read()).decode()
print("inlined %d images (%.1f MB)" % (len(IMG), sum(len(v) for v in IMG.values())/1048576))

bodies, titles = {}, {}
for p in PAGES:
    raw = open(os.path.join(SRC, p)).read()
    m = re.search(r"<body>(.*)</body>", raw, re.S)
    body = m.group(1) if m else re.split(r"<body>", raw, 1)[-1]
    # Drop the local script tag — the bundle supplies its own.
    body = re.sub(r'<script src="js/main\.js"[^>]*></script>', "", body)
    bodies[p] = body.strip()
    t = re.search(r"<title>(.*?)</title>", raw, re.S)
    titles[p] = html.unescape(t.group(1)).strip() if t else "Lyons Contracting"

# Store page bodies inside <template> so nothing in them runs or loads until routed to.
templates = "\n".join(
    '<template data-page="%s" data-title="%s">%s</template>' % (p, html.escape(titles[p], quote=True), bodies[p])
    for p in PAGES)

banner = """
<div id="demo-banner">
  <span><strong>Demo</strong> for Lyons Contracting &mdash; not a live site. Real reviews, real photos of your work.</span>
  <button type="button" id="demo-dismiss" aria-label="Dismiss notice">&times;</button>
</div>
"""

img_json = json.dumps(IMG)

page = f"""<title>Lyons Contracting Demo</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Public+Sans:wght@400;500;600;700&display=swap">

<style>
{css}

/* ---------- bundle-only chrome ---------- */
#demo-banner {{
  position: sticky; top: 0; z-index: 200;
  background: var(--gold-100); color: #6b4e07;
  border-bottom: 1px solid #e3cf9a;
  font-family: var(--font-display); font-weight: 600; font-size: .84rem;
  display: flex; align-items: center; justify-content: center; gap: 14px;
  padding: 9px 44px 9px 16px; text-align: center; line-height: 1.4;
}}
#demo-banner strong {{ color: #6b4e07; }}
#demo-banner button {{
  position: absolute; right: 10px; top: 50%; transform: translateY(-50%);
  background: none; border: 0; font-size: 1.4rem; line-height: 1;
  color: #6b4e07; cursor: pointer; padding: 2px 8px; border-radius: 6px;
}}
#demo-banner button:hover {{ background: rgba(107,78,7,.12); }}
#demo-banner.hidden {{ display: none; }}
/* The site header sticks below the banner rather than under it. */
#demo-banner:not(.hidden) ~ #app .site-header {{ top: 38px; }}
@media (max-width: 560px) {{
  #demo-banner {{ font-size: .78rem; padding: 8px 40px 8px 12px; }}
  #demo-banner:not(.hidden) ~ #app .site-header {{ top: 52px; }}
}}
</style>

{banner}
<div id="app"></div>
{templates}

<script id="img-map" type="application/json">{img_json}</script>

<script>
(function () {{
  "use strict";
  {js}

  var app = document.getElementById("app");
  // Images live once in a JSON map rather than once per page template.
  var IMGMAP = JSON.parse(document.getElementById("img-map").textContent);
  var TPL = {{}};
  document.querySelectorAll("template[data-page]").forEach(function (t) {{
    TPL[t.dataset.page] = t;
  }});

  function pageFromHash() {{
    var h = (location.hash || "").replace(/^#\\/?/, "");
    return TPL[h] ? h : "index.html";
  }}

  function render(name, keepScroll) {{
    var tpl = TPL[name] || TPL["404.html"];
    app.innerHTML = "";
    app.appendChild(tpl.content.cloneNode(true));
    app.querySelectorAll("img[src^='images/']").forEach(function (img) {{
      var uri = IMGMAP[img.getAttribute("src")];
      if (uri) img.src = uri;
    }});
    document.title = tpl.dataset.title || "Lyons Contracting";
    // Mark the current page in the nav.
    app.querySelectorAll(".nav-links a").forEach(function (a) {{
      a.classList.toggle("active", a.getAttribute("href") === name);
    }});
    if (window.__lyonsInit) window.__lyonsInit();
    // Reveal animations need a tick to catch up after a swap.
    app.querySelectorAll(".reveal").forEach(function (el) {{ el.classList.add("in"); }});
    if (!keepScroll) window.scrollTo(0, 0);
  }}

  // Route internal .html links; leave tel:, mailto: and real anchors alone.
  document.addEventListener("click", function (e) {{
    var a = e.target.closest && e.target.closest("a[href]");
    if (!a) return;
    var href = a.getAttribute("href");
    if (!href || /^(tel:|mailto:|https?:)/i.test(href)) return;

    if (href.charAt(0) === "#") {{           // same-page anchor
      var el = document.querySelector(href);
      if (el) {{ e.preventDefault(); el.scrollIntoView({{ behavior: "smooth", block: "start" }}); }}
      return;
    }}
    var m = href.match(/^([a-z0-9-]+\\.html)(#.*)?$/i);
    if (!m) return;
    e.preventDefault();
    var target = TPL[m[1]] ? m[1] : "404.html";
    if (pageFromHash() === target) {{
      render(target, true);
    }} else {{
      location.hash = "/" + target;          // triggers hashchange → render
      return;
    }}
    if (m[2]) {{
      var anchor = document.querySelector(m[2]);
      if (anchor) anchor.scrollIntoView({{ behavior: "smooth", block: "start" }});
    }}
  }});

  window.addEventListener("hashchange", function () {{ render(pageFromHash()); }});

  var dismiss = document.getElementById("demo-dismiss");
  if (dismiss) dismiss.addEventListener("click", function () {{
    document.getElementById("demo-banner").classList.add("hidden");
  }});

  render(pageFromHash(), true);
}})();
</script>
"""

# Emit pure ASCII with numeric character references: the artifact harness owns the
# <head>, so the page must not depend on a charset declaration it cannot set.
ascii_page = page.encode("ascii", "xmlcharrefreplace").decode("ascii")
open(OUT, "w", encoding="ascii").write(ascii_page)
print("wrote %s  (%.0f KB, %d pages, ascii-safe)" % (OUT, len(ascii_page) / 1024, len(PAGES)))
