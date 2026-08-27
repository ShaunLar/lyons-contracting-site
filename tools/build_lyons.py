#!/usr/bin/env python3
"""Generate the Lyons Contracting static site.

Emits plain, dependency-free HTML into the repo so the owner can edit any page
in a text editor. Run:  python3 build_lyons.py
"""
import os, html, datetime

OUT = "/Users/shaunlaranjeira/Claude/Websites/lyons-contracting"

SITE = "https://lyonscontracting.com"
NAME = "Lyons Contracting"
PHONE_D = "703-299-8888"
PHONE_T = "+17032998888"
STREET = "4930 A Eisenhower Ave"
CITY, REGION, ZIP = "Alexandria", "VA", "22304"
HOURS = "Mon–Fri, 7:00 AM – 7:00 PM"
TODAY = "2026-08-27"

# ===========================================================================
# DEMO GUARD - set to False before Lyons deploys this for real.
#
# This is a public demo repo hosted on GitHub Pages. It carries Lyons' own
# reviews and project photos, so it must not be indexed: Google would treat it
# as a near-duplicate of lyonscontracting.com and it could compete with their
# real site. True adds <meta name="robots" content="noindex, nofollow"> to every
# page and Disallow: / to robots.txt.
#
# LEAVING THIS ON when the site goes live on their real domain would make the
# whole site invisible to Google. Flip it to False and rebuild.
# ===========================================================================
DEMO_NOINDEX = True

CITIES = [
    ("alexandria",  "Alexandria"),
    ("arlington",   "Arlington"),
    ("falls-church","Falls Church"),
    ("mclean",      "McLean"),
    ("springfield", "Springfield"),
    ("fairfax",     "Fairfax"),
]

NAV = [
    ("roof-replacement.html", "Roof Replacement"),
    ("roof-repair.html",      "Roof Repair"),
    ("storm-damage.html",     "Storm Damage"),
    ("roof-cost.html",        "Roof Cost"),
    ("gallery.html",          "Our Work"),
    ("about.html",            "About"),
]

# --------------------------------------------------------------------------
# Shared chrome
# --------------------------------------------------------------------------

def icon(name):
    p = {
        "check": '<path d="M20 6 9 17l-5-5"/>',
        "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.4-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2Z"/>',
        "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/>',
        "star": '<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8-6.2-3.3-6.2 3.3L7 14.2l-5-4.9 6.9-1Z"/>',
        "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
        "home": '<path d="m3 10 9-7 9 7v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z"/>',
        "drop": '<path d="M12 2.7 6.3 9.5a7.5 7.5 0 1 0 11.4 0Z"/>',
        "layers": '<path d="m12 2 9 5-9 5-9-5Z"/><path d="m3 12 9 5 9-5"/><path d="m3 17 9 5 9-5"/>',
        "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7Z"/>',
        "wrench": '<path d="M14.7 6.3a4 4 0 0 0 5 5l-10 10a2.8 2.8 0 0 1-4-4Z"/>',
        "doc": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/><path d="M14 2v6h6"/>',
        "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    }[name]
    return ('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            + p + '</svg>')


def head(title, desc, slug, extra_ld=""):
    # Normalise first: callers write either "&" or "&amp;"; escaping a
    # pre-escaped string yields "&amp;amp;", which Google renders literally.
    title = html.unescape(title)
    desc = html.unescape(desc)
    canon = f"{SITE}/" if slug == "index.html" else f"{SITE}/{slug}"
    # See DEMO_NOINDEX above - remove before this goes live on the real domain.
    robots_meta = ('<meta name="robots" content="noindex, nofollow">\n  '
                   if DEMO_NOINDEX else "")
    ld = f""" <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "RoofingContractor",
  "@id": "{SITE}/#business",
  "name": "{NAME}",
  "description": "Roofing contractor in Alexandria, Virginia. Roof replacement, roof repair and storm damage work across Northern Virginia for more than 25 years.",
  "url": "{SITE}/",
  "telephone": "{PHONE_T}",
  "priceRange": "$$",
  "image": "{SITE}/images/lyons-og.jpg",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "{STREET}",
    "addressLocality": "{CITY}",
    "addressRegion": "{REGION}",
    "postalCode": "{ZIP}",
    "addressCountry": "US"
  }},
  "geo": {{ "@type": "GeoCoordinates", "latitude": 38.8009, "longitude": -77.1091 }},
  "openingHoursSpecification": [{{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "07:00", "closes": "19:00"
  }}],
  "areaServed": [
{chr(10).join('    { "@type": "City", "name": "' + n + '", "addressRegion": "VA" }' + ("," if i < len(CITIES) - 1 else "") for i, (_, n) in enumerate(CITIES))}
  ],
  "sameAs": [
    "https://www.facebook.com/lyonscontracting",
    "https://www.linkedin.com/company/lyons-contracting-inc-",
    "https://x.com/varoofer"
  ]
}}
  </script>

  <!-- ==========================================================================
       NOTE TO OWNER — star ratings in Google results
       The live site displays a 4.9 Google rating but publishes no rating markup,
       so Google can't show stars next to your listing. Confirm your current
       rating and review count on your Google Business Profile, then uncomment
       the block below. Only publish numbers that match real, visible reviews.
       ==========================================================================
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@id": "{SITE}/#business",
    "aggregateRating": {{
      "@type": "AggregateRating",
      "ratingValue": "4.9",
      "reviewCount": "REPLACE_WITH_REAL_COUNT",
      "bestRating": "5"
    }}
  }}
  </script>
  -->
{extra_ld}"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  {robots_meta}<title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc)}">
  <link rel="canonical" href="{canon}">

  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{NAME}">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(desc)}">
  <meta property="og:url" content="{canon}">
  <meta property="og:image" content="{SITE}/images/lyons-og.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="theme-color" content="#0d1733">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&family=Public+Sans:wght@400;500;600;700&display=swap">
  <link rel="stylesheet" href="css/styles.css">
  <link rel="manifest" href="site.webmanifest">
 {ld}
</head>
<body>
"""


def header(active):
    parts = []
    for h, t in NAV:
        cls = ' class="active"' if h == active else ''
        parts.append('<li><a href="%s"%s>%s</a></li>' % (h, cls, t))
    links = "".join(parts)
    return f"""
<div class="topbar">
  <div class="container">
    <span>Serving Alexandria &amp; Northern Virginia &middot; {HOURS}</span>
    <div class="topbar-badges">
      <span><span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span> 4.9 on Google</span>
      <span>Licensed &amp; insured in Virginia</span>
    </div>
  </div>
</div>

<header class="site-header">
  <div class="container nav">
    <a class="brand" href="index.html">
      <span class="brand-mark" aria-hidden="true">LC</span>
      <span class="brand-text">
        <span class="brand-name">Lyons Contracting</span>
        <span class="brand-sub">Roofing &middot; 25+ Years</span>
      </span>
    </a>

    <nav aria-label="Main">
      <ul class="nav-links">{links}</ul>
    </nav>

    <div class="nav-cta">
      <!-- Every phone number on this site is a real tel: link. On the current
           lyonscontracting.com the number is plain text, so tapping does nothing. -->
      <a class="nav-phone" href="tel:{PHONE_T}">{icon('phone')}<span class="num">{PHONE_D}</span></a>
      <a class="btn btn-primary" href="contact.html">Free Estimate</a>
      <button class="nav-toggle" type="button" aria-label="Menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>
"""


def lead_form(form_id, heading, sub, btn="Get My Free Estimate", compact=False):
    """Three fields. No CAPTCHA. No 'how did you hear about us'."""
    return f"""
<form id="{form_id}" data-lead-form action="#FORM_ENDPOINT" method="post" novalidate>
  <div class="form-success" role="status">
    <strong>Got it &mdash; thank you.</strong><br>
    We'll call you back within one business day. If it's urgent, call
    <a href="tel:{PHONE_T}">{PHONE_D}</a> and you'll reach a person.
  </div>

  <div class="form-fields">
    {f'<h2>{heading}</h2><p class="muted" style="margin-bottom:18px">{sub}</p>' if heading else ''}

    <label class="field">
      <span>Your name</span>
      <input type="text" name="name" autocomplete="name" required placeholder="Jane Doe">
    </label>

    <label class="field">
      <span>Phone or email &mdash; whichever you prefer</span>
      <input type="text" name="contact" autocomplete="tel" required placeholder="703-555-0142">
    </label>

    <label class="field">
      <span>What's going on with your roof?</span>
      <textarea name="details" required placeholder="Leak over the kitchen after last week's storm &mdash; 1940s slate roof in Del Ray."></textarea>
    </label>

    <!-- Honeypot: stops bots without asking a homeowner to solve a puzzle.
         Deliberately never mentioned in the copy - the absence of friction
         should be felt, not advertised. -->
    <div class="hp-field" aria-hidden="true">
      <label>Company website <input type="text" name="company_website" tabindex="-1" autocomplete="off"></label>
    </div>

    <button class="btn btn-primary btn-block btn-lg" type="submit">{btn}</button>
    <p class="form-note">
      We'll call you back within one business day &mdash; no obligation, no sales visit.
      Rather talk it through now? Call <a href="tel:{PHONE_T}">{PHONE_D}</a>.
    </p>
  </div>
</form>
"""


AREAS_SECTION = f"""
<section class="section section--navy section--tight">
  <div class="container">
    <p class="eyebrow">Areas we serve</p>
    <h2 style="margin-bottom:18px">Northern Virginia roofing, from one local crew</h2>
    <p class="lead" style="margin-bottom:24px">
      We're based on Eisenhower Avenue in Alexandria. Every crew that works on your
      roof is a Lyons crew &mdash; we don't subcontract the work out.
    </p>
    <ul class="area-links">
      {"".join(f'<li><a href="{s}.html">{n}, VA</a></li>' for s, n in CITIES)}
    </ul>
  </div>
</section>
"""


def cta_band(title="Ready for a straight answer about your roof?",
             text="A free, no-pressure inspection and a written estimate you can actually compare."):
    return f"""
<section class="section section--tight cta-band">
  <div class="container cta-flex">
    <div>
      <h2 style="margin-bottom:8px">{title}</h2>
      <p style="margin:0">{text}</p>
    </div>
    <div class="hero-actions" style="margin:0">
      <a class="btn btn-primary btn-lg" href="contact.html">Get My Free Estimate</a>
      <a class="btn btn-ghost-light btn-lg" href="tel:{PHONE_T}">{icon('phone')} {PHONE_D}</a>
    </div>
  </div>
</section>
"""


FOOTER = f"""
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="brand" href="index.html" style="margin-bottom:14px">
          <span class="brand-mark" aria-hidden="true">LC</span>
          <span class="brand-text">
            <span class="brand-name" style="color:#fff">Lyons Contracting</span>
            <span class="brand-sub">Roofing &middot; 25+ Years</span>
          </span>
        </a>
        <p>
          More than 25 years replacing, repairing and fabricating roofs across
          Northern Virginia &mdash; with our own sheet metal shop and our own crews.
        </p>
        <p style="margin-top:14px">
          <span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
          <strong style="color:#fff">4.9</strong> on Google &middot; Angi Super Service Award &middot; BBB
        </p>
      </div>

      <div>
        <h4>Services</h4>
        <ul class="footer-links">
          <li><a href="roof-replacement.html">Roof Replacement</a></li>
          <li><a href="roof-repair.html">Roof Repair</a></li>
          <li><a href="storm-damage.html">Storm Damage &amp; Insurance</a></li>
          <li><a href="emergency.html">Emergency Roof Leak</a></li>
          <li><a href="roof-cost.html">Roof Cost &amp; Financing</a></li>
          <li><a href="gallery.html">Our Work</a></li>
        </ul>
      </div>

      <div>
        <h4>Service Areas</h4>
        <ul class="footer-links">
          {"".join(f'<li><a href="{s}.html">{n}, VA</a></li>' for s, n in CITIES)}
        </ul>
      </div>

      <div>
        <h4>Contact</h4>
        <ul class="footer-contact">
          <li><a href="tel:{PHONE_T}"><strong>{PHONE_D}</strong></a></li>
          <li>{STREET}<br>{CITY}, {REGION} {ZIP}</li>
          <li>{HOURS}</li>
          <li style="margin-top:6px"><a class="btn btn-primary" href="contact.html">Free Estimate</a></li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom">
      <span>&copy; <span id="year">2026</span> Lyons Contracting. All rights reserved.</span>
      <span>Licensed &amp; insured in the Commonwealth of Virginia &middot; GAF, Firestone &amp; Revere certified</span>
    </div>
  </div>
</footer>

<!-- Sticky call bar: mobile only. The fix that matters most on this site. -->
<div class="mobile-callbar">
  <a class="cb-call" href="tel:{PHONE_T}">{icon('phone')} Call Now</a>
  <a class="cb-quote" href="contact.html">Free Estimate</a>
</div>

<script src="js/main.js" defer></script>
</body>
</html>
"""


def page(slug, title, desc, body, active=None, extra_ld=""):
    doc = head(title, desc, slug, extra_ld) + header(active or slug) + body + FOOTER
    with open(os.path.join(OUT, slug), "w") as f:
        f.write(doc)
    return slug
