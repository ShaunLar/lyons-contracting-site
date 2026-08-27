#!/usr/bin/env python3
"""Page content for the Lyons Contracting site. Run this file to build."""
from build_lyons import (page, lead_form, cta_band, icon, AREAS_SECTION,
                         PHONE_D, PHONE_T, CITIES, SITE, STREET, CITY, REGION, ZIP, HOURS)
import os, datetime

OUT = "/Users/shaunlaranjeira/Claude/Websites/lyons-contracting"

# --------------------------------------------------------------------------
# Reusable blocks
# --------------------------------------------------------------------------

ROOF_TYPES = [
    ("layers", "Asphalt Shingle",
     "The workhorse of Northern Virginia. Architectural shingles from GAF, installed "
     "with a full ventilation and underlayment system rather than just a new top layer.",
     "25–30 years"),
    ("bolt", "Standing Seam Metal",
     "Fabricated in our own sheet metal shop, so panels are cut for your roof instead "
     "of ordered to the nearest stock size. Copper, aluminium and steel.",
     "50+ years"),
    ("drop", "Flat &amp; Rubber Membrane",
     "Firestone EPDM and modified bitumen for low-slope roofs, porch roofs and the flat "
     "sections that sit behind so many Alexandria parapets.",
     "20–30 years"),
    ("shield", "Slate",
     "Repair, selective replacement and full restoration. The right answer for historic "
     "Old Town and Rosemont homes where a tear-off would be the wrong call.",
     "75–100 years"),
    ("home", "Tile",
     "Concrete and clay tile replacement, plus underlayment renewal — usually the part "
     "that has actually failed when a tile roof starts leaking.",
     "50+ years"),
]


def roof_type_cards():
    out = []
    for ic, name, blurb, life in ROOF_TYPES:
        out.append(f"""
      <div class="card svc-card reveal">
        <span class="svc-icon">{icon(ic)}</span>
        <h3>{name}</h3>
        <p>{blurb}</p>
        <p class="more">Typical service life: {life}</p>
      </div>""")
    return "".join(out)


# Real Google reviews, published verbatim on lyonscontracting.com. Long ones are
# trimmed with an ellipsis; wording is otherwise untouched. Locations appear only
# where the reviewer states one.
# NOTE TO OWNER: verify each against your live Google profile before launch, and
# add more as they come in.
TESTIMONIALS = [
    ("Tom is my go-to roofing guy: responsive, professional, local, quick, reasonably "
     "priced and excellent quality. This time his team did a gorgeous copper seamed roof "
     "over a DR bump out. My bungalow has a little bling! My neighbor also uses Lyons "
     "Contracting and said Tom's proposal was the lowest price and best quality of all six. "
     "I didn't bother getting other proposals. I know Tom is going to be fair and stand by "
     "his work.",
     "Deborah Brautigam", "Google review &middot; Del Ray"),

    ("Tom is responsive, professional and honest. I have worked with Lyons at both of my "
     "homes, one of which was a 60 year old slate roof. Recently, we neglected to promptly "
     "clean our gutters and it caused water to sit on our roof line. Tom came out the next "
     "morning and quickly assessed the situation. He informed us that we did not have a "
     "larger roof issue and gave us practical advice instead of a bill. This is only my "
     "second google review, but when you are lucky enough to find good partner it is worth "
     "sharing. I highly recommend Tom and Lyons!",
     "Catherine Steadman", "Google review"),

    ("I had been dealing with another company but it took them three visits, a hole cut in "
     "my ceiling, and three weeks to give me a quote. When I reached out to Tom late on a "
     "Friday he responded right away and scheduled an appointment for the following Monday&hellip; "
     "Although his quote was twice as much as the first company's, Tom's quote was for a full "
     "replacement and not the band-aid the other company was proposing&hellip; And now I don't "
     "have to worry about my roof for another 20+ years!",
     "Caryn Thiboheim", "Google review &middot; Alexandria"),

    ("Lyons installed my roof in 2015, and it was a great experience! I've had no trouble "
     "since&hellip; they seemed especially experienced with the flat, rubber-membrane roofs "
     "that are so common in Alexandria. UPDATE: My neighbor replaced his upper roof and we "
     "went in on replacing our shared porch roof. Everything went seamlessly, from the "
     "estimate to the installation. I learned today that Tom has employed the same 10 people "
     "for 16 years &mdash; which says a lot if you're concerned about how the contractors you "
     "hire treat their employees.",
     "MHL", "Google review &middot; Alexandria"),

    ("Tom and the company were very professional throughout the entire process. He never "
     "tried to up sell any materials or unnecessary services&hellip; The crew showed up on time "
     "on the scheduled day and went straight to work. Throughout the workday, they answered "
     "any questions we had. They were very professional, courteous, and friendly. I can't "
     "commend him and the crew enough. I highly recommend them.",
     "Lino Miani", "Google review"),

    ("Lyons Contracting did an amazing job inspecting, and replacing our roof. There were "
     "many complex issues/problems with the roof that warranted a full replacement. Tom took "
     "the time to discuss the options and answered my questions in a way that made me very "
     "comfortable with our decision. Tom obtained the permits necessary to do the work and we "
     "navigated winter weather to get it scheduled. His crew was extremely professional, "
     "punctual and performed flawlessly.",
     "Hassan Aden", "Google review"),

    ("Tom Petrilli and his crew did a great job in replacing my flat/low-slopped roof in "
     "Alexandria at a very fair price&hellip; Tom was in constant communication with me during "
     "the entirety of the process and answered all my questions. He provided video and picture "
     "updates of anything him and his crew noticed or worked on which I really appreciated. "
     "They also made sure to clean up not only my, but my neighbors properties of any debris.",
     "Tom P.", "Google review &middot; Alexandria"),

    ("Very professional and the only quote we could obtain that would actually reengineer the "
     "poorly designed awning on the house we just bought. At least 2 layers of completely "
     "rotten code violation are no longer attached to our house. All the work done in one day "
     "and I'm fully confident we'll have no more water damage. Updates throughout the day with "
     "pictures so that I don't have to climb up there to inspect.",
     "Adam Szczypka", "Google review"),

    ("I was pleasantly surprised at the quote, I was expecting something over inflated given "
     "that this is NOVA and it's post-covid, but the final price was 100% fair given the size "
     "of my roof. The crew came out and worked 9+ hours a day to finish the project including "
     "replacing sections of the roof deck where there had been water damage. And they cleaned "
     "everything up, there was no trace that they had even been here.",
     "Rebecca Gould", "Google review"),

    ("Tom, the manager, was very responsive, explained everything in detail and patiently "
     "answered all my questions. I observed his installation team closely &mdash; they were "
     "extremely diligent in their work and went out of their way to clean up the old roof "
     "materials. I am highly satisfied with their work and I absolutely recommend Lyons "
     "Contracting for any type of roof replacement.",
     "Kent Rogers", "Google review"),
]


def testimonials(limit=3, start=0):
    out = []
    picks = (TESTIMONIALS * 2)[start:start + limit]
    for quote, who, where in picks:
        out.append(f"""
      <div class="testi reveal">
        <span class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
        <p>&ldquo;{quote}&rdquo;</p>
        <cite>{who}<small>{where}</small></cite>
      </div>""")
    return "".join(out)


# Real Lyons Contracting project photos, pulled from the company's own Houzz
# portfolio (houzz.com/professionals/.../lyons-contracting) — their uploads, their work.
# Entries with img=None are still grey placeholders awaiting more photos from Lyons.
GALLERY = [
    ("slate-mansard-copper-dormers-old-town.jpg",
     "Slate mansard &amp; copper dormer vents", "Old Town Alexandria",
     "Slate mansard roof with three hand-fabricated copper oval dormer vents on a historic Old Town Alexandria home"),
    ("copper-cupola-weathervane.jpg",
     "Hand-fabricated copper cupola", "Our sheet metal shop",
     "Hand-fabricated copper bell-curve cupola roof with a horse weathervane, made in the Lyons Contracting sheet metal shop"),
    ("shingle-copper-bay-alexandria.jpg",
     "Architectural shingle &amp; copper bay roof", "Northern Virginia",
     "New architectural shingle roof with a custom copper standing-seam bay window roof on a brick ranch in Northern Virginia"),
    ("standing-seam-metal-mclean.jpg",
     "Standing seam metal roof", "McLean",
     "Dark standing seam metal roof with dormers on a large Northern Virginia home, installed by Lyons Contracting"),
    ("flat-membrane-roof-studio.jpg",
     "Single-ply membrane flat roof", "Alexandria",
     "White single-ply membrane flat roof on a modern backyard studio in Alexandria VA"),
    (None, "Slate &amp; copper valley repair", "Rosemont, Alexandria", None),
    (None, "Full tear-off &amp; replacement", "West Springfield", None),
    (None, "Storm damage rebuild", "Fairfax", None),
    (None, "Tile underlayment renewal", "Vienna", None),
]


def gallery_tiles(limit=None, start=0, real_only=False):
    pool = [g for g in GALLERY if g[0]] if real_only else GALLERY
    items = (pool * 3)[start:start + limit] if limit else pool
    out = []
    for img, what, where, alt in items:
        if img:
            inner = ('<img src="images/%s" alt="%s" loading="lazy" decoding="async" width="1200" height="800">'
                     % (img, alt))
        else:
            inner = ('<!-- NOTE TO OWNER: replace with a real photo of this job -\n'
                     '             <img src="images/your-photo.jpg" alt="%s in %s" loading="lazy"> -->\n'
                     '        <span class="ph-label">%s<br><span class="muted">%s</span></span>'
                     % (what, where, what, where))
        out.append("""
      <figure class="tile reveal" style="margin:0">
        %s
        <figcaption class="tile-cap">%s &middot; %s</figcaption>
      </figure>""" % (inner, what, where))
    return "".join(out)


FAQS = [
    ("How much does a new roof cost in Northern Virginia?",
     "For a typical Alexandria or Arlington single-family home, an architectural shingle "
     "replacement usually lands between $12,000 and $26,000 depending on size, pitch, "
     "how many layers have to come off, and how complicated the roof is. Slate, metal and "
     "tile run higher. Our <a href='roof-cost.html'>roof cost page</a> has a calculator "
     "that gives you a real range in about twenty seconds, without talking to anyone."),
    ("Do you offer financing?",
     "Yes. Most homeowners replacing a roof do it as a monthly payment rather than a lump "
     "sum, and a roof rarely fails at a convenient moment. We can walk you through the "
     "options on the estimate visit — see <a href='roof-cost.html'>roof cost &amp; financing</a>."),
    ("My roof is leaking right now. What do I do?",
     "Move what you can out of the way, put a bucket under it, and if the ceiling is bulging, "
     f"poke a small hole at the lowest point to let the water out. Then call <a href='tel:{PHONE_T}'>{PHONE_D}</a>. "
     "See our <a href='emergency.html'>emergency roof leak page</a> for what we do when we arrive."),
    ("Will you deal with my insurance company?",
     "For storm and hail claims, yes — we document the damage properly, meet the adjuster on "
     "the roof, and make sure the scope reflects what actually needs replacing. Details on the "
     "<a href='storm-damage.html'>storm damage page</a>."),
    ("Do you subcontract the work out?",
     "No. The crew on your roof is a Lyons crew. We also fabricate our own metal in our own "
     "sheet metal shop, which is why we can do things a subcontracted crew can't — custom "
     "valleys, bay roofs and flashing cut for your house rather than ordered to the nearest size."),
    ("How long does a replacement take?",
     "Most single-family shingle roofs are a one- to two-day job. Slate, metal and complicated "
     "roofs take longer. You'll get a start date and a realistic finish date in writing before "
     "anything begins."),
    ("Are you licensed and insured?",
     "Licensed and insured in the Commonwealth of Virginia, and certified by GAF, Firestone and "
     "Revere — which is what makes the manufacturer warranties on your roof actually valid."),
]


def faq_block(items=None):
    items = items or FAQS
    out = []
    for q, a in items:
        out.append(f"""
      <div class="faq-item">
        <button class="faq-q" type="button" aria-expanded="false">{q}</button>
        <div class="faq-a"><p style="margin:0">{a}</p></div>
      </div>""")
    return "".join(out)


def faq_ld(items=None):
    import json
    items = items or FAQS
    import re
    def strip(t):
        return re.sub(r"<[^>]+>", "", t).replace("&amp;", "&").replace("&mdash;", "—").replace("&nbsp;", " ")
    data = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": strip(q),
             "acceptedAnswer": {"@type": "Answer", "text": strip(a)}}
            for q, a in items
        ],
    }
    return '\n  <script type="application/ld+json">\n' + json.dumps(data, indent=2) + '\n  </script>\n'


TRUST_STRIP = f"""
<div class="trust-strip">
  <div class="container">
    <span class="badge">{icon('star')} <span class="n">4.9</span> Google rating</span>
    <span class="badge">{icon('clock')} <span class="n">25+</span> years in Alexandria</span>
    <span class="badge">{icon('shield')} GAF &middot; Firestone &middot; Revere certified</span>
    <span class="badge">{icon('check')} Angi Super Service Award</span>
    <span class="badge">{icon('home')} Our own sheet metal shop</span>
  </div>
</div>
"""

PROCESS = """
<section class="section section--cloud">
  <div class="container">
    <div class="center" style="margin-bottom:44px">
      <p class="eyebrow">How it works</p>
      <h2>Four steps, no surprises</h2>
      <p class="lead center">The part most homeowners dread is the estimate. Ours is one visit,
      one page, and one number.</p>
    </div>
    <div class="steps">
      <div class="step reveal">
        <h3>You call or send three lines</h3>
        <p>Name, a way to reach you, and what's going on. That's the whole form.</p>
      </div>
      <div class="step reveal">
        <h3>We get on the roof</h3>
        <p>A real inspection with photographs — not a walk around the yard with binoculars.</p>
      </div>
      <div class="step reveal">
        <h3>You get an itemised estimate</h3>
        <p>Written, line by line, with the materials named. The number you sign is the number you pay.</p>
      </div>
      <div class="step reveal">
        <h3>Our crew does the work</h3>
        <p>Lyons employees, not subcontractors. Magnet-swept for nails before we leave.</p>
      </div>
    </div>
  </div>
</section>
"""


def why_us():
    return f"""
<section class="section">
  <div class="container">
    <div class="grid grid-2" style="gap:52px;align-items:center">
      <div>
        <p class="eyebrow">Why Lyons</p>
        <h2>Twenty-five years on Northern Virginia roofs</h2>
        <p class="lead">Most roofing companies in this area buy their metal and send out a
        subcontracted crew. We fabricate our own and send our own people. On an old
        Alexandria house with a bay window, a slate valley and three different roof
        planes meeting at one point, that difference is the whole job.</p>
        <ul class="checklist" style="margin-top:22px">
          <li><strong>Manufacturer-certified.</strong> GAF, Firestone and Revere — the certifications that keep your warranty valid.</li>
          <li><strong>In-house sheet metal fabrication.</strong> Custom valleys, flashing and bay roofs cut for your house.</li>
          <li><strong>Our own crews.</strong> No subcontractors, no rotating faces, no finger-pointing.</li>
          <li><strong>Historic-district experience.</strong> Old Town, Rosemont and Del Ray have rules. We've worked inside them for decades.</li>
          <li><strong>Written, itemised estimates.</strong> No asterisks, no "subject to conditions found".</li>
        </ul>
      </div>
      <div class="grid" style="gap:18px">
        {gallery_tiles(4, 0, real_only=True)}
      </div>
    </div>
  </div>
</section>
"""


# --------------------------------------------------------------------------
# Home
# --------------------------------------------------------------------------

home = f"""
<section class="hero">
  <div class="container">
    <div class="hero-grid">
      <div>
        <h1>Alexandria's roofer for more than 25 years.</h1>
        <p class="hero-sub">
          Roof replacement, repair and storm damage across Northern Virginia — with our own
          crews, our own sheet metal shop, and an estimate that fits on one page.
        </p>
        <div class="hero-actions">
          <a class="btn btn-primary btn-lg" href="#quote">Get My Free Estimate</a>
          <a class="btn btn-ghost-light btn-lg" href="tel:{PHONE_T}">{icon('phone')} {PHONE_D}</a>
        </div>
        <div class="hero-trust">
          <span class="trust-item">{icon('star')} 4.9 on Google</span>
          <span class="trust-item">{icon('shield')} Licensed &amp; insured in VA</span>
          <span class="trust-item">{icon('clock')} Callback within 1 business day</span>
        </div>
      </div>

      <div class="quote-card" id="quote">
        {lead_form("hero-form", "Free estimate, three questions",
                   "No CAPTCHA. No &ldquo;how did you hear about us?&rdquo; Just tell us about the roof.")}
      </div>
    </div>
  </div>
</section>

{TRUST_STRIP}

<section class="section">
  <div class="container">
    <div class="center" style="margin-bottom:46px">
      <p class="eyebrow">What we do</p>
      <h2>Every roof on a Northern Virginia street</h2>
      <p class="lead center">From a 1940s slate roof in Rosemont to a flat EPDM porch behind an
      Old Town parapet — we install and repair all of it.</p>
    </div>
    <div class="grid grid-3">{roof_type_cards()}</div>
  </div>
</section>

<section class="section section--cloud">
  <div class="container">
    <div class="grid grid-3">
      <a class="card card-link svc-card reveal" href="roof-replacement.html">
        <span class="svc-icon">{icon('home')}</span>
        <h3>Roof Replacement</h3>
        <p>A full system — decking, underlayment, ventilation, flashing and surface — not just
        a new layer on top of an old problem.</p>
        <span class="more">See what's included &rarr;</span>
      </a>
      <a class="card card-link svc-card reveal" href="roof-repair.html">
        <span class="svc-icon">{icon('wrench')}</span>
        <h3>Roof Repair</h3>
        <p>Leaks, flashing failures, missing shingles and cracked slate. We'll tell you honestly
        when a repair is the right call — and when it isn't.</p>
        <span class="more">Common repairs &rarr;</span>
      </a>
      <a class="card card-link svc-card reveal" href="storm-damage.html">
        <span class="svc-icon">{icon('bolt')}</span>
        <h3>Storm Damage &amp; Insurance</h3>
        <p>Documented properly, and we meet your adjuster on the roof so the claim reflects
        what actually needs replacing.</p>
        <span class="more">How claims work &rarr;</span>
      </a>
    </div>
  </div>
</section>

{why_us()}

<section class="section section--tight emg-band">
  <div class="container cta-flex">
    <div>
      <h2 style="margin-bottom:8px">Water coming in right now?</h2>
      <p style="margin:0">Don't wait for a form. Call and you'll reach a person, and we'll get
      a tarp on it before the damage spreads.</p>
    </div>
    <div class="hero-actions" style="margin:0">
      <a class="btn btn-lg" style="background:#fff;color:#a8351c" href="tel:{PHONE_T}">{icon('phone')} {PHONE_D}</a>
      <a class="btn btn-ghost-light btn-lg" href="emergency.html">Emergency info</a>
    </div>
  </div>
</section>

{PROCESS}

<section class="section">
  <div class="container">
    <div class="center" style="margin-bottom:40px">
      <p class="eyebrow">Our work</p>
      <h2>Roofs we've done, on streets you know</h2>
      <p class="lead center">A badge proves we're legitimate. A photograph proves we're good.</p>
    </div>
    <div class="gallery-grid">{gallery_tiles(5, 0, real_only=True)}</div>
    <p class="center" style="margin-top:32px">
      <a class="btn btn-ghost btn-lg" href="gallery.html">See the full gallery</a>
    </p>
  </div>
</section>

<section class="section section--cloud">
  <div class="container">
    <div class="center" style="margin-bottom:40px">
      <p class="eyebrow">Reviews</p>
      <h2>4.9 on Google, earned one roof at a time</h2>
    </div>
    <div class="grid grid-3">{testimonials()}</div>
  </div>
</section>

<section class="section">
  <div class="container" style="max-width:820px">
    <div class="center" style="margin-bottom:30px">
      <p class="eyebrow">Questions</p>
      <h2>The things homeowners actually ask</h2>
    </div>
    {faq_block()}
  </div>
</section>

{AREAS_SECTION}
{cta_band()}
"""

page("index.html",
     "Roofing Company in Alexandria, VA | Lyons Contracting",
     "Roof replacement, repair and storm damage across Alexandria, Arlington, Fairfax, "
     "Falls Church, McLean and Springfield. 4.9 on Google, 25+ years, free estimates. "
     "Call 703-299-8888.",
     home, active="index.html", extra_ld=faq_ld())


# --------------------------------------------------------------------------
# Service pages
# --------------------------------------------------------------------------

def service_page(slug, nav_active, h1, crumb, intro, body_html, title, desc,
                 sidebar_head="Free roof estimate", extra_ld=""):
    body = f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="index.html">Home</a><span>/</span>{crumb}</p>
    <h1>{h1}</h1>
    <p>{intro}</p>
  </div>
</section>

{TRUST_STRIP}

<section class="section">
  <div class="container svc-layout">
    <div class="prose">{body_html}</div>
    <aside class="sidebar-card">
      <h3>{sidebar_head}</h3>
      <p class="muted" style="font-size:.95rem;margin-bottom:16px">
        Three questions. We'll call you back within one business day.
      </p>
      {lead_form(slug.replace('.html','') + "-form", None, None)}
      <p style="margin:16px 0 0;text-align:center">
        <a class="nav-phone" href="tel:{PHONE_T}">{icon('phone')} {PHONE_D}</a>
      </p>
    </aside>
  </div>
</section>

{AREAS_SECTION}
{cta_band()}
"""
    page(slug, title, desc, body, active=nav_active, extra_ld=extra_ld)


service_page(
    "roof-replacement.html", "roof-replacement.html",
    "Roof Replacement in Alexandria &amp; Northern Virginia",
    "Roof Replacement",
    "A roof is a system, not a surface. When we replace one, every layer gets addressed — "
    "not just the part you can see from the street.",
    f"""
    <h2>What a Lyons replacement actually includes</h2>
    <p>Plenty of quotes in this area cover shingles and labour, then discover the rest once
    the old roof is off. Here's what's in ours before you sign anything.</p>
    <ul class="checklist">
      <li><strong>Full tear-off.</strong> Down to the deck, so we can see what's underneath. Layering over old shingles hides rot and voids most warranties.</li>
      <li><strong>Deck inspection and repair.</strong> Soft or rotted sheathing is replaced. You see photographs of anything we find.</li>
      <li><strong>Ice-and-water shield</strong> at eaves, valleys and penetrations — the places Northern Virginia roofs actually leak.</li>
      <li><strong>Synthetic underlayment</strong> across the field, not felt paper.</li>
      <li><strong>New flashing.</strong> Chimneys, walls, skylights and valleys, fabricated in our own shop. Re-using old flashing is the single most common corner cut in this trade.</li>
      <li><strong>A balanced ventilation system.</strong> Intake at the soffit, exhaust at the ridge. Get this wrong and the new roof cooks itself from underneath.</li>
      <li><strong>Manufacturer-certified installation</strong> so the GAF or Firestone warranty on your roof is valid rather than theoretical.</li>
      <li><strong>Magnet sweep and full cleanup</strong> before we leave. Twice.</li>
    </ul>

    <h2>Choosing the surface</h2>
    <p>The right material depends on the house, the pitch, the neighbourhood and how long you
    plan to stay. We'll give you a straight recommendation rather than steering you to whatever
    we have the most of.</p>
    <div class="grid grid-2" style="margin:22px 0">{roof_type_cards()}</div>

    <h2>Do you actually need a replacement?</h2>
    <p>Sometimes not. A roof with ten good years left and one failed valley needs a repair, and
    we'll say so — we'd rather have the repair job and the referral than sell you a roof you
    didn't need. Signs it really is time:</p>
    <ul>
      <li>Shingles curling, cupping or losing granules across whole slopes, not just one patch</li>
      <li>Daylight visible through the roof deck from inside the attic</li>
      <li>Repeat leaks in different places — a roof failing generally rather than at one point</li>
      <li>Sagging along the ridge or between rafters</li>
      <li>An asphalt roof past 20–25 years, especially if it was layered over</li>
    </ul>
    <p>Not sure which side of that line you're on? <a href="roof-repair.html">Start with a repair
    inspection</a> — it's free either way.</p>

    <h2>What it costs</h2>
    <p>Most single-family shingle replacements in Alexandria, Arlington and Fairfax land between
    <strong>$12,000 and $26,000</strong>. Slate, metal and tile run higher. Rather than making you
    call to find out, we put a calculator on the
    <a href="roof-cost.html">roof cost page</a> that gives you a range in twenty seconds — and
    financing details, because most people do this as a monthly payment.</p>
    """,
    "Roof Replacement Alexandria VA | Full Tear-Off &amp; Installation | Lyons Contracting",
    "Complete roof replacement in Alexandria and Northern Virginia — full tear-off, new "
    "flashing, ventilation and manufacturer-certified installation. Free estimate: 703-299-8888.")


service_page(
    "roof-repair.html", "roof-repair.html",
    "Roof Repair in Alexandria &amp; Northern Virginia",
    "Roof Repair",
    "Most leaks aren't the roof failing — they're one detail failing. We find which one, "
    "and we'll tell you honestly whether a repair will hold.",
    f"""
    <h2>What usually turns out to be the problem</h2>
    <p>After twenty-five years, the causes repeat. In this area it's almost always one of these:</p>
    <ul class="checklist">
      <li><strong>Flashing.</strong> Chimneys, sidewalls, skylights. The metal fails long before the shingles do, and it's the leading cause of leaks we're called out for.</li>
      <li><strong>Valleys.</strong> Where two slopes meet, water concentrates. Old open valleys and worn valley metal are a constant on Alexandria's older housing stock.</li>
      <li><strong>Cracked or slipped slate.</strong> Individual slates fail while the roof around them has decades left. Replacing them properly is a repair, not a re-roof.</li>
      <li><strong>Pipe boots.</strong> The rubber collar around a plumbing vent dries out and splits at about the 10-year mark. Cheap to fix, expensive to ignore.</li>
      <li><strong>Flat-roof seams.</strong> EPDM and modified bitumen fail at the seams and terminations, not in the middle of the field.</li>
      <li><strong>Ventilation and condensation.</strong> Sometimes the water isn't coming in at all — it's condensing in an under-ventilated attic. A new roof won't fix that; correcting the airflow will.</li>
    </ul>

    <h2>We'll tell you when a repair is the wrong answer</h2>
    <p>A repair on a roof that's genuinely finished is money spent twice. If yours is past
    saving we'll show you photographs of why, and if it isn't, we'll fix the thing that's
    actually broken and leave the rest alone. That's the whole basis of our
    <a href="index.html#quote">free inspection</a> — an honest read on which one you're facing.</p>

    <h2>Every repair inspection includes</h2>
    <ul>
      <li>Somebody physically on the roof — not a look from the driveway</li>
      <li>Photographs of what we find, sent to you whether or not you hire us</li>
      <li>An attic check where accessible, because that's where the evidence usually is</li>
      <li>A written estimate covering the repair, and the honest remaining life of the roof</li>
    </ul>

    <h2>How fast can you get here?</h2>
    <p>Routine repairs are usually scheduled within a few days. If water is coming into the
    house right now, that's not a repair call — that's an
    <a href="emergency.html">emergency</a>, and it's handled differently.
    Call <a href="tel:{PHONE_T}">{PHONE_D}</a>.</p>

    <h2>Repair or replace?</h2>
    <p>The rough rule: if the roof is under 15 years old and the problem is confined to one area,
    repair it. If it's over 20, failing in several places, or has been layered over, you're
    usually better off putting the money toward a
    <a href="roof-replacement.html">replacement</a>. Our
    <a href="roof-cost.html">cost calculator</a> will show you what that would run before you
    have to speak to anybody.</p>
    """,
    "Roof Repair Alexandria VA | Leaks, Flashing &amp; Slate | Lyons Contracting",
    "Roof leak and repair specialists in Alexandria, Arlington and Fairfax. Flashing, valleys, "
    "slate and flat roofs. Free inspection with photos. Call 703-299-8888.")


service_page(
    "storm-damage.html", "storm-damage.html",
    "Storm Damage Roof Repair &amp; Insurance Claims",
    "Storm Damage",
    "Wind and hail damage is often invisible from the ground and obvious from the roof. "
    "We document it properly — and we meet your adjuster up there.",
    f"""
    <h2>What storm damage actually looks like</h2>
    <p>Homeowners usually call after they see shingles in the yard. But the damage that costs
    you later is the damage you can't see:</p>
    <ul class="checklist">
      <li><strong>Creased shingles.</strong> Wind lifts a shingle, it folds, it lies back down. The seal is broken and it will leak — sometimes a year later.</li>
      <li><strong>Hail bruising.</strong> Granule loss and soft spots in the mat. Cosmetic versus functional hail damage is the single biggest argument in claims, and it turns on evidence.</li>
      <li><strong>Lifted or displaced flashing</strong> around chimneys and walls.</li>
      <li><strong>Damaged ridge caps and vents</strong> — the highest, most exposed components.</li>
      <li><strong>Gutter and fascia damage</strong> that lets water get behind the drip edge.</li>
    </ul>

    <h2>How we handle a claim</h2>
    <div class="steps" style="margin:26px 0">
      <div class="step">
        <h3>Free documented inspection</h3>
        <p>We photograph and mark every point of damage, with measurements and a written scope.</p>
      </div>
      <div class="step">
        <h3>You file the claim</h3>
        <p>It's your policy and your claim — we give you everything you need to file it properly.</p>
      </div>
      <div class="step">
        <h3>We meet the adjuster</h3>
        <p>On the roof, with our documentation, so the approved scope matches the real damage.</p>
      </div>
      <div class="step">
        <h3>We do the work</h3>
        <p>Our crews, to the approved scope, with any supplements documented as we go.</p>
      </div>
    </div>

    <div class="emg-note">
      <p style="margin:0"><strong>A word about storm chasers.</strong> After every major storm,
      out-of-state crews canvass Alexandria and Arlington offering free roofs and "we'll cover
      your deductible." Waiving a deductible is insurance fraud in Virginia, and those companies
      are gone before the warranty matters. We've been on Eisenhower Avenue for more than
      25 years — you'll be able to find us in ten.</p>
    </div>

    <h2>Deadlines matter</h2>
    <p>Most policies require you to report damage promptly, and an undocumented leak that spreads
    can be denied as a maintenance failure rather than storm damage. If a storm has just come
    through, get it looked at — the inspection is free and it starts the clock properly.</p>

    <h2>If water is already coming in</h2>
    <p>That's an <a href="emergency.html">emergency</a>, not a claim conversation.
    Call <a href="tel:{PHONE_T}">{PHONE_D}</a>, get a tarp on it, and we'll sort the
    paperwork afterwards.</p>
    """,
    "Storm Damage Roof Repair &amp; Insurance Claims | Alexandria VA | Lyons Contracting",
    "Wind and hail roof damage in Northern Virginia. Documented inspections, adjuster meetings "
    "and full storm repairs. Free inspection — call 703-299-8888.")


# --------------------------------------------------------------------------
# Emergency
# --------------------------------------------------------------------------

emergency = f"""
<section class="page-hero" style="background:linear-gradient(118deg,#7d2614,#a8351c)">
  <div class="container">
    <p class="breadcrumb"><a href="index.html">Home</a><span>/</span>Emergency Roof Leak</p>
    <h1>Roof leaking right now?</h1>
    <p>Call <a href="tel:{PHONE_T}" style="color:#fff;text-decoration:underline"><strong>{PHONE_D}</strong></a>
    and you'll reach a person. We'll get a tarp on it before the damage spreads into
    drywall, insulation and flooring.</p>
    <div class="hero-actions" style="margin-top:26px">
      <a class="btn btn-lg" style="background:#fff;color:#a8351c" href="tel:{PHONE_T}">{icon('phone')} Call {PHONE_D}</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container svc-layout">
    <div class="prose">
      <h2>Do these four things while you wait</h2>
      <ol>
        <li><strong>Move what matters.</strong> Furniture, electronics, anything on the floor beneath the leak.</li>
        <li><strong>Contain the water.</strong> Buckets, towels, a plastic sheet over what you can't move.</li>
        <li><strong>If the ceiling is bulging, pierce it.</strong> A small hole at the lowest point of the bulge lets the water drain in one place. A ceiling that collapses under trapped water does far more damage than the hole will.</li>
        <li><strong>Photograph everything.</strong> Before you clean up. If this becomes an insurance claim, those photos are the claim.</li>
      </ol>

      <div class="emg-note">
        <p style="margin:0"><strong>Please don't get on the roof.</strong> A wet roof, in
        weather, at night, is how people get seriously hurt. Whatever is up there will still
        be up there when we arrive with harnesses.</p>
      </div>

      <h2>What we do when we get there</h2>
      <ul class="checklist">
        <li><strong>Stop the water first.</strong> Emergency tarping or a temporary patch — stabilise before diagnose.</li>
        <li><strong>Find the actual entry point.</strong> Water travels along rafters and decking; the stain on your ceiling is rarely under the hole.</li>
        <li><strong>Document it.</strong> Photographs and notes you can hand straight to your insurer.</li>
        <li><strong>Give you the real options.</strong> What has to happen now, what can wait, and what each costs.</li>
      </ul>

      <h2>Our hours &mdash; honestly</h2>
      <p>Our office hours are {HOURS}. Storms don't keep office hours, so leave a message
      on the emergency line and it reaches someone. If you don't hear back quickly and water
      is actively coming in, keep calling — we'd far rather be woken up than have you spend
      a night watching a ceiling.</p>

      <!-- NOTE TO OWNER: this is the single biggest lead gap on your current site. A leak at
           9pm on a Saturday currently has nowhere to go and calls the next company on Google.
           Decide the real after-hours arrangement (answering service, forwarded mobile, or a
           stated callback window) and put it here. Don't promise 24/7 unless you'll answer. -->

      <h2>What it costs</h2>
      <p>Emergency tarping is a flat call-out plus materials, and if you go ahead with the
      permanent repair or a <a href="roof-replacement.html">replacement</a>, we credit the
      call-out against it. You'll hear the number before we do anything.</p>

      <h2>Not an emergency?</h2>
      <p>If it's a stain that's been there a while, or missing shingles with no water coming
      in, that's a <a href="roof-repair.html">roof repair</a> — same free inspection, normal
      scheduling, no call-out fee.</p>
    </div>

    <aside class="sidebar-card" style="border-top-color:#a8351c">
      <h3>Not urgent? Send three lines.</h3>
      <p class="muted" style="font-size:.95rem;margin-bottom:16px">
        We'll call you back within one business day.
      </p>
      {lead_form("emergency-form", None, None)}
      <p style="margin:16px 0 0;text-align:center">
        <a class="nav-phone" href="tel:{PHONE_T}">{icon('phone')} {PHONE_D}</a>
      </p>
    </aside>
  </div>
</section>

{AREAS_SECTION}
{cta_band("Water stopped? Let's fix the cause.",
          "A free inspection, photographs of what we find, and an honest read on repair versus replace.")}
"""

page("emergency.html",
     "Emergency Roof Leak Repair | Alexandria VA | Lyons Contracting",
     "Roof leaking right now? Call 703-299-8888. Emergency tarping and leak repair across "
     "Alexandria, Arlington and Northern Virginia — plus what to do while you wait.",
     emergency, active="roof-repair.html")


# --------------------------------------------------------------------------
# Roof cost + calculator + financing
# --------------------------------------------------------------------------

cost = f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="index.html">Home</a><span>/</span>Roof Cost &amp; Financing</p>
    <h1>What a new roof costs in Northern Virginia</h1>
    <p>Every other roofer makes you book an appointment to find out. Here's a real range
    in about twenty seconds, no email required.</p>
  </div>
</section>

<section class="section section--tight section--cloud">
  <div class="container" style="max-width:940px">
    <div class="calc" id="calc">
      <div class="calc-grid">
        <div class="calc-inputs">
          <p class="eyebrow" style="margin-bottom:18px">Estimate your roof</p>
          <label class="field">
            <span>Roughly how many square feet is your home's footprint?</span>
            <input type="number" id="calc-area" value="1800" min="400" max="12000" step="50" inputmode="numeric">
          </label>
          <div class="form-row">
            <label class="field">
              <span>Material</span>
              <select id="calc-material">
                <option value="shingle">Asphalt shingle</option>
                <option value="metal">Standing seam metal</option>
                <option value="flat">Flat / rubber membrane</option>
                <option value="slate">Slate</option>
                <option value="tile">Tile</option>
              </select>
            </label>
            <label class="field">
              <span>Stories</span>
              <select id="calc-stories">
                <option value="1">1 story</option>
                <option value="2" selected>2 stories</option>
                <option value="3">3+ stories</option>
              </select>
            </label>
          </div>
          <div class="form-row">
            <label class="field">
              <span>Roof shape</span>
              <select id="calc-complexity">
                <option value="simple">Simple — one or two slopes</option>
                <option value="average" selected>Average — a few valleys, a chimney</option>
                <option value="complex">Complex — dormers, bays, many planes</option>
              </select>
            </label>
            <label class="field">
              <span>Layers to remove</span>
              <select id="calc-tearoff">
                <option value="one" selected>One existing layer</option>
                <option value="two">Two or more layers</option>
                <option value="none">New construction — nothing to remove</option>
              </select>
            </label>
          </div>
        </div>

        <div class="calc-out">
          <span class="calc-label">Typical installed range</span>
          <div class="calc-range" id="calc-range">—</div>
          <div class="calc-mo" id="calc-mo"></div>
          <p class="calc-disclaimer">
            A genuine ballpark based on what roofs like yours cost in this area — not a quote.
            The real number depends on what's under the old roof, and nobody can tell you that
            without getting up there. Our inspection is free and the written estimate is the
            number you pay.
          </p>
          <a class="btn btn-primary btn-block btn-lg" href="contact.html">Get an exact estimate</a>
          <p style="margin:14px 0 0;text-align:center">
            <a class="nav-phone" href="tel:{PHONE_T}">{icon('phone')} {PHONE_D}</a>
          </p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container svc-layout">
    <div class="prose">
      <h2>What actually drives the price</h2>
      <p>Two houses on the same street with the same footprint can be $9,000 apart. Here's why:</p>
      <ul class="checklist">
        <li><strong>Roof area, not floor area.</strong> A steep roof has far more surface than the house's footprint. Pitch alone can swing the number 30%.</li>
        <li><strong>How many layers come off.</strong> Two layers of old shingles is double the tear-off labour and double the disposal.</li>
        <li><strong>What's under them.</strong> Rotted decking has to be replaced. This is the number one reason a cheap quote becomes an expensive job.</li>
        <li><strong>Complexity.</strong> Dormers, bay roofs, skylights, chimneys and multiple valleys are all hand-work and all flashing.</li>
        <li><strong>Access.</strong> Three stories, a steep lot, or no room for a dumpster all cost time.</li>
        <li><strong>Material.</strong> Asphalt to slate is roughly a 4× difference per square foot.</li>
      </ul>

      <h2>Why cheap quotes get expensive</h2>
      <p>If one bid comes in dramatically under the others, look for what's missing rather than
      assuming you found a bargain. The usual omissions: re-using old flashing, going over the
      existing layer instead of tearing off, felt instead of synthetic underlayment, no
      ventilation work, and "decking replacement billed as found" with no cap. Ask every bidder
      to put those five line items in writing and the bids start looking very different.</p>

      <h2>Financing</h2>
      <p>Roofs rarely fail at a convenient moment, and most people replace one as a monthly
      payment rather than a lump sum. We can walk you through the available options during the
      estimate visit — including terms that let you get the work done now and pay over several
      years.</p>
      <!-- NOTE TO OWNER: connect a real lender (GreenSky, Hearth, Service Finance, Acorn) and
           put the application link here. The monthly figure in the calculator is illustrative
           only — update js/main.js with your lender's actual APR and terms before launch. -->
      <div class="emg-note" style="background:#f7edd6;border-left-color:#c69214">
        <p style="margin:0"><strong>Ask about financing on the estimate visit.</strong>
        A $19,000 roof at a monthly payment is a different decision than a $19,000 cheque —
        and the estimate is free either way.</p>
      </div>

      <h2>Getting a comparable estimate</h2>
      <p>Ours is one page and itemised, so you can hold it next to anyone else's. If a competitor
      won't put the same line items in writing, that tells you something useful.</p>
    </div>

    <aside class="sidebar-card">
      <h3>Get the exact number</h3>
      <p class="muted" style="font-size:.95rem;margin-bottom:16px">
        Free inspection, written estimate, no obligation.
      </p>
      {lead_form("cost-form", None, None)}
    </aside>
  </div>
</section>

{AREAS_SECTION}
{cta_band()}
"""

page("roof-cost.html",
     "Roof Replacement Cost in Alexandria VA (2026 Calculator) | Lyons Contracting",
     "What does a new roof cost in Northern Virginia? Use our instant calculator for a real "
     "range by material and roof size, plus what drives the price and financing options.",
     cost, active="roof-cost.html")


# --------------------------------------------------------------------------
# Gallery, About, Contact
# --------------------------------------------------------------------------

gallery = f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="index.html">Home</a><span>/</span>Our Work</p>
    <h1>Roofs we've done across Northern Virginia</h1>
    <p>Slate in Old Town, copper in McLean, EPDM behind an Arlington parapet. Twenty-five
    years of it.</p>
  </div>
</section>

{TRUST_STRIP}

<section class="section">
  <div class="container">
    <!-- ======================================================================
         NOTE TO OWNER — this is the most important page to populate.
         Every tile below is a grey placeholder. Real before/after photos of
         your own work are the most persuasive thing you can put on this site;
         the current lyonscontracting.com has none at all. Drop images into
         /images and replace each <span class="ph-label">…</span> with:
           <img src="images/your-photo.jpg"
                alt="Slate roof restoration in Old Town Alexandria VA"
                loading="lazy">
         Always write alt text naming the work AND the city — it helps both
         accessibility and local search.
         ====================================================================== -->
    <div class="gallery-grid">{gallery_tiles()}</div>
  </div>
</section>

<section class="section section--cloud">
  <div class="container">
    <div class="center" style="margin-bottom:40px">
      <p class="eyebrow">Reviews</p>
      <h2>What homeowners said afterwards</h2>
    </div>
    <div class="grid grid-3">{testimonials(3, 3)}</div>
  </div>
</section>

{AREAS_SECTION}
{cta_band("See something like your roof?",
          "Tell us what you're dealing with and we'll come look at it — free, and with photographs.")}
"""

page("gallery.html",
     "Our Roofing Work | Project Gallery | Lyons Contracting Alexandria VA",
     "Photos of completed roofing projects across Alexandria, Arlington, McLean, Falls Church, "
     "Springfield and Fairfax — slate, standing seam metal, shingle and flat roofs.",
     gallery, active="gallery.html")


about = f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="index.html">Home</a><span>/</span>About</p>
    <h1>Twenty-five years on Eisenhower Avenue</h1>
    <p>A roofing company that still fabricates its own metal and still sends its own crews.</p>
  </div>
</section>

{TRUST_STRIP}

<section class="section">
  <div class="container svc-layout">
    <div class="prose">
      <h2>Who we are</h2>
      <p>Lyons Contracting has been roofing Northern Virginia homes for more than 25 years,
      from a shop on Eisenhower Avenue in Alexandria. In that time the area has filled up with
      roofing companies that appear after a storm and disappear before the warranty matters.
      We're still here, at the same address, with the same phone number.</p>

      <h2>You'll deal with Tom</h2>
      <p>Tom Petrilli runs Lyons Contracting, and he's the one who comes out to look at your
      roof. Not a commissioned salesman working from a script &mdash; the person whose name is on
      the company. Read our Google reviews and you'll notice how many of them are about him by
      name: responding on a Friday evening, showing up the next morning, sending photographs
      from the roof, and more than once telling a homeowner they didn't need the work.</p>
      <p>The crew is just as settled. As one customer put it in their review:
      <em>&ldquo;I learned today that Tom has employed the same 10 people for 16 years &mdash;
      which says a lot if you're concerned about how the contractors you hire treat their
      employees.&rdquo;</em></p>
      <!-- NOTE TO OWNER: a photo of Tom belongs right here. Drop it in as
           <img src="images/tom-petrilli.jpg" alt="Tom Petrilli, owner of Lyons Contracting"> -->

      <h2>The sheet metal shop</h2>
      <p>This is the part that makes us different, and it's genuinely unusual. We fabricate our
      own metal in-house — valleys, flashing, drip edge, bay window roofs, standing seam panels.
      Most companies order stock components and make the house fit them. On the older homes in
      Alexandria and Arlington, where nothing is square and no two dormers match, being able to
      cut a piece for the actual roof is the difference between a job that lasts and a job that
      leaks in four years.</p>

      <h2>Certified, and why that matters</h2>
      <p>We're certified by <strong>GAF</strong>, <strong>Firestone</strong> and
      <strong>Revere</strong>. This isn't decoration: manufacturer warranties on roofing
      materials are conditional on certified installation. An uncertified installer can hand you
      a warranty document that the manufacturer will not honour when you try to use it. Ask any
      roofer you're considering for their certification numbers.</p>

      <h2>Our own crews</h2>
      <p>We don't subcontract. The people on your roof are Lyons employees, which means one
      standard of work, one point of accountability, and nobody to point at if something goes
      wrong. It also means the crew that shows up has done this on houses like yours before.</p>

      <h2>Recognition</h2>
      <ul class="checklist">
        <li><strong>4.9 on Google</strong> across a quarter century of work</li>
        <li><strong>Angi Super Service Award</strong></li>
        <li><strong>Better Business Bureau</strong> accredited</li>
        <li><strong>Consumers' Checkbook</strong> listed</li>
        <li>Licensed and insured in the Commonwealth of Virginia</li>
      </ul>

      <h2>Where we work</h2>
      <p>Alexandria, Arlington, Falls Church, McLean, Springfield and Fairfax — plus the
      surrounding communities. If you're near the edge of that, call and ask.</p>
    </div>

    <aside class="sidebar-card">
      <h3>Free roof estimate</h3>
      <p class="muted" style="font-size:.95rem;margin-bottom:16px">
        Three questions. Callback within one business day.
      </p>
      {lead_form("about-form", None, None)}
    </aside>
  </div>
</section>

<section class="section section--cloud">
  <div class="container">
    <div class="center" style="margin-bottom:40px">
      <p class="eyebrow">Reviews</p>
      <h2>4.9 on Google</h2>
    </div>
    <div class="grid grid-3">{testimonials(3, 6)}</div>
  </div>
</section>

{AREAS_SECTION}
{cta_band()}
"""

page("about.html",
     "About Lyons Contracting | Alexandria VA Roofing for 25+ Years",
     "Lyons Contracting has roofed Northern Virginia homes for over 25 years from Alexandria — "
     "with in-house sheet metal fabrication, our own crews, and GAF, Firestone and Revere certification.",
     about, active="about.html")


contact = f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="index.html">Home</a><span>/</span>Contact</p>
    <h1>Get your free estimate</h1>
    <p>Three questions, no CAPTCHA, and no "how did you hear about us?" before we've even
    said hello.</p>
  </div>
</section>

<section class="section">
  <div class="container svc-layout">
    <div>
      <div class="card" style="border-top:4px solid var(--gold-500)">
        {lead_form("contact-form", "Tell us about the roof",
                   "We'll call you back within one business day. If it's urgent, call us instead &mdash; you'll reach a person.")}
      </div>

      <div class="grid grid-2" style="margin-top:26px">
        <div class="card">
          <h3>{icon('phone')} Call us</h3>
          <p style="font-size:1.2rem"><a class="nav-phone" href="tel:{PHONE_T}">{PHONE_D}</a></p>
          <p class="muted" style="margin:0">{HOURS}</p>
        </div>
        <div class="card">
          <h3>{icon('pin')} Visit the shop</h3>
          <p style="margin-bottom:4px">{STREET}<br>{CITY}, {REGION} {ZIP}</p>
          <p class="muted" style="margin:0">Our sheet metal fabrication shop</p>
        </div>
      </div>

      <!-- NOTE TO OWNER: embed your Google Map here.
           Google Maps → your business → Share → Embed a map → paste the iframe. -->
    </div>

    <aside class="sidebar-card">
      <h3>Leaking right now?</h3>
      <p style="margin-bottom:14px">Don't use the form. Call and you'll reach a person, and
      we'll get a tarp on it before the damage spreads.</p>
      <p><a class="btn btn-primary btn-block btn-lg" href="tel:{PHONE_T}">{icon('phone')} {PHONE_D}</a></p>
      <p style="margin:14px 0 0"><a href="emergency.html">What to do while you wait &rarr;</a></p>
      <hr style="border:0;border-top:1px solid var(--line);margin:22px 0">
      <h3 style="font-size:1.05rem">Not sure what it'll cost?</h3>
      <p style="margin-bottom:12px">Get a real range in twenty seconds, without talking to anyone.</p>
      <a class="btn btn-ghost btn-block" href="roof-cost.html">Roof cost calculator</a>
    </aside>
  </div>
</section>

{AREAS_SECTION}
"""

page("contact.html",
     "Contact Lyons Contracting | Free Roof Estimate | Alexandria VA",
     "Get a free roofing estimate in Alexandria and Northern Virginia. Three-question form, "
     "no CAPTCHA, callback within one business day. Or call 703-299-8888.",
     contact, active="contact.html")


# --------------------------------------------------------------------------
# City pages
# --------------------------------------------------------------------------

CITY_CONTENT = {
    "alexandria": dict(
        hoods=["Old Town", "Del Ray", "Rosemont", "Beverley Hills", "Seminary Hill",
               "Belle Haven", "Parkfairfax", "North Ridge"],
        angle="""
        <p>Alexandria is where we're based — our sheet metal shop is on Eisenhower Avenue — and
        it's also the hardest roofing city in Northern Virginia to do properly. The housing stock
        runs from 18th-century Old Town rowhouses to 1950s Parkfairfax garden apartments to new
        construction in Eisenhower East, and almost none of it takes a stock component off a truck.</p>

        <h3>Old Town and the historic districts</h3>
        <p>Work visible from the street in the Old and Historic Alexandria District generally
        needs Board of Architectural Review approval, and slate, standing seam and flat roofs
        behind parapets are the norm rather than the exception. We've been working inside those
        constraints for decades — including selective slate replacement where a tear-off would
        be both wrong and unapprovable.</p>

        <h3>Del Ray and Rosemont</h3>
        <p>1920s and 1930s bungalows and four-squares, most on their second or third roof, many
        with the original slate still on the main slopes and asphalt patched over the additions.
        The recurring problem here is the junction between the two — and old valley metal.</p>

        <h3>The flat-roof problem</h3>
        <p>A large share of Alexandria homes have a low-slope section behind a parapet, over a
        porch, or on a rear addition. These fail at the seams and terminations long before the
        main roof does, and they're the source of more Alexandria leaks than anything else.
        We install Firestone EPDM and modified bitumen on these.</p>"""),

    "arlington": dict(
        hoods=["Clarendon", "Ballston", "Lyon Village", "Cherrydale", "Westover",
               "Arlington Ridge", "Aurora Highlands", "Bluemont"],
        angle="""
        <p>Arlington's roofs are a study in two eras colliding: pre-war bungalows and colonials
        in Lyon Village, Cherrydale and Westover, and the pop-tops and whole-house rebuilds that
        have gone up beside them over the last twenty years.</p>

        <h3>Pop-tops and additions</h3>
        <p>When a 1930s colonial gets a second storey or a rear addition, you end up with new
        roof planes meeting old ones — and the tie-in is where it leaks. Getting that junction
        right is flashing work, not shingle work, and it's exactly what our own sheet metal shop
        exists for.</p>

        <h3>Mature tree cover</h3>
        <p>Arlington's canopy is one of its best features and one of the hardest things about its
        roofs. Constant leaf load in valleys and gutters, moss on north slopes, and limb strikes
        in every serious storm. Roofs under heavy canopy need their valleys checked far more
        often than the neighbourhood average.</p>

        <h3>Condo and townhouse associations</h3>
        <p>Much of Arlington is governed by an HOA or condo board with its own approval process
        and material requirements. We've submitted to enough of them to know what the packet
        needs to contain.</p>"""),

    "falls-church": dict(
        hoods=["Broadmont", "Lake Barcroft", "Seven Corners", "Falls Hill",
               "Winter Hill", "Sleepy Hollow", "Pimmit Hills"],
        angle="""
        <p>Falls Church covers both the City of Falls Church and the much larger area with a
        Falls Church mailing address — and the roofs differ sharply between them.</p>

        <h3>The City</h3>
        <p>Older, denser, and increasingly rebuilt: modest post-war houses on generous lots are
        steadily being replaced with large new construction. That means we're often working next
        door to a build site, and often tying a new roof into a house that's been added to twice.</p>

        <h3>Lake Barcroft and Sleepy Hollow</h3>
        <p>Mid-century contemporaries with low-slope and shed roofs, wide overhangs and a lot of
        skylights. Low-slope roofs on these homes are frequently mis-specified with shingles when
        the pitch genuinely calls for a membrane — which is why they leak. If yours has been
        re-shingled twice and still leaks, that's likely the reason.</p>

        <h3>Storm exposure</h3>
        <p>The Seven Corners and Route 7 corridor sees consistent wind damage in summer storms.
        Wind damage is the kind that's invisible from the ground — see our
        <a href="storm-damage.html">storm damage page</a> for what to look for.</p>"""),

    "mclean": dict(
        hoods=["Langley", "Chesterbrook", "Franklin Park", "Salona Village",
               "West McLean", "Evermay", "El Nido"],
        angle="""
        <p>McLean has the largest and most architecturally complicated roofs we work on. Big
        colonials, extensive slate and tile, copper details, and roofs with a dozen planes,
        multiple chimneys and dormers on every elevation.</p>

        <h3>Copper and standing seam</h3>
        <p>McLean is where our sheet metal shop earns its keep. Copper bay roofs, standing seam
        porch roofs, custom valleys and chimney crickets — all fabricated for the specific house
        rather than ordered to the nearest stock size. Very few contractors in the area can do
        this in-house.</p>

        <h3>Slate and tile</h3>
        <p>Many McLean homes carry genuine slate or clay tile. Both routinely outlive the
        underlayment beneath them, which means the correct repair is often removing, renewing
        and re-laying the original material — not replacing it. A contractor who only quotes a
        tear-off is telling you what they can do, not what your roof needs.</p>

        <h3>Complexity is the cost driver</h3>
        <p>On a roof this complicated, the square footage matters less than the number of
        transitions. Our <a href="roof-cost.html">cost calculator</a> accounts for that — set
        complexity to "complex" for a realistic McLean range.</p>"""),

    "springfield": dict(
        hoods=["West Springfield", "Kingstowne", "Newington", "Rolling Valley",
               "Orange Hunt", "Saratoga", "Daventry", "Cardinal Forest"],
        angle="""
        <p>Springfield is largely 1960s–1990s subdivision housing, which makes it the most
        predictable roofing market in our service area — and the one where timing matters most.</p>

        <h3>Whole streets aging at once</h3>
        <p>When a subdivision goes up in one phase, its roofs reach end of life in one phase too.
        If neighbours on either side have replaced theirs in the last two years, yours is on the
        same clock. That's usually why we're in Rolling Valley or Orange Hunt three times in a
        month.</p>

        <h3>Builder-grade originals</h3>
        <p>A lot of these homes still have builder-grade three-tab shingles, minimal ventilation,
        and felt underlayment. The upgrade to architectural shingles with a proper ridge-and-soffit
        ventilation system is genuinely noticeable — in attic temperature, in energy bills, and in
        how long the new roof lasts.</p>

        <h3>HOA approvals</h3>
        <p>Most Springfield communities have an HOA with an approved colour and material list.
        We'll tell you what's permitted in your community before you fall in love with a colour.</p>"""),

    "fairfax": dict(
        hoods=["City of Fairfax", "Fair Oaks", "Mantua", "Oakton", "Burke",
               "Chantilly", "Fairfax Station", "Kings Park West"],
        angle="""
        <p>Fairfax covers the widest range of anywhere we work — the compact older City of
        Fairfax, 1970s subdivisions in Kings Park West and Burke, and large newer homes on
        acreage in Fairfax Station and Oakton.</p>

        <h3>Large, steep, complicated</h3>
        <p>The newer Fairfax Station and Oakton homes have big roofs with steep pitches, multiple
        gables and a lot of surface area. Steep pitch adds cost — more surface per square foot of
        house, and staging and safety requirements that a walkable roof doesn't have.</p>

        <h3>Mantua and the older city</h3>
        <p>Mid-century split-levels and ramblers, many with low-slope sections over carports and
        additions. The same low-slope problem we see across Northern Virginia: shingles installed
        on a pitch that needed a membrane.</p>

        <h3>Storm corridor</h3>
        <p>The Fair Oaks and Route 50 corridor takes consistent summer storm damage. If a storm
        has come through recently, get the roof looked at before a small wind lift becomes a
        winter leak — the <a href="storm-damage.html">inspection is free</a>.</p>"""),
}


def city_page(slug, name, idx=0):
    c = CITY_CONTENT[slug]
    hoods = ", ".join(c["hoods"][:-1]) + " and " + c["hoods"][-1]
    others = "".join(
        f'<li><a href="{s}.html">{n}, VA</a></li>' for s, n in CITIES if s != slug)

    body = f"""
<section class="page-hero">
  <div class="container">
    <p class="breadcrumb"><a href="index.html">Home</a><span>/</span>{name}, VA</p>
    <h1>Roofing in {name}, Virginia</h1>
    <p>Replacement, repair and storm damage across {name} — from a company that's been
    doing it from Alexandria for more than 25 years.</p>
  </div>
</section>

{TRUST_STRIP}

<section class="section">
  <div class="container svc-layout">
    <div class="prose">
      <h2>Roofing {name} homes</h2>
      {c["angle"]}

      <h2>Neighbourhoods we work in</h2>
      <p>{hoods} — plus the surrounding streets. If you're nearby and not listed,
      call and ask: <a href="tel:{PHONE_T}">{PHONE_D}</a>.</p>

      <h2>What we do in {name}</h2>
      <div class="grid grid-2" style="margin:22px 0">
        <a class="card card-link svc-card" href="roof-replacement.html">
          <span class="svc-icon">{icon('home')}</span>
          <h3>Roof Replacement</h3>
          <p>Full tear-off, new flashing, proper ventilation, manufacturer-certified installation.</p>
          <span class="more">What's included &rarr;</span>
        </a>
        <a class="card card-link svc-card" href="roof-repair.html">
          <span class="svc-icon">{icon('wrench')}</span>
          <h3>Roof Repair</h3>
          <p>Leaks, flashing, valleys, slate and flat-roof seams — with an honest read on repair versus replace.</p>
          <span class="more">Common repairs &rarr;</span>
        </a>
        <a class="card card-link svc-card" href="storm-damage.html">
          <span class="svc-icon">{icon('bolt')}</span>
          <h3>Storm Damage</h3>
          <p>Documented inspections and adjuster meetings so your claim reflects the real damage.</p>
          <span class="more">How claims work &rarr;</span>
        </a>
        <a class="card card-link svc-card" href="emergency.html">
          <span class="svc-icon">{icon('drop')}</span>
          <h3>Emergency Leaks</h3>
          <p>Water coming in now? Call and we'll get it tarped before it spreads.</p>
          <span class="more">What to do first &rarr;</span>
        </a>
      </div>

      <h2>What a roof costs in {name}</h2>
      <p>Most single-family replacements in {name} fall between <strong>$12,000 and
      $26,000</strong> for architectural shingle, with slate, metal and tile running higher.
      Our <a href="roof-cost.html">cost calculator</a> gives you a range for your specific roof
      in about twenty seconds — no email, no phone call.</p>

      <h2>Recent work near {name}</h2>
      <div class="gallery-grid" style="grid-template-columns:repeat(3,1fr);margin-top:18px">
        {gallery_tiles(3, idx, real_only=True)}
      </div>
      <!-- NOTE TO OWNER: swap these for three real photos of jobs in {name}.
           Local photos on a local page are worth far more than stock ones. -->
    </div>

    <aside class="sidebar-card">
      <h3>Free {name} roof estimate</h3>
      <p class="muted" style="font-size:.95rem;margin-bottom:16px">
        Three questions. Callback within one business day.
      </p>
      {lead_form(slug + "-form", None, None)}
      <p style="margin:16px 0 0;text-align:center">
        <a class="nav-phone" href="tel:{PHONE_T}">{icon('phone')} {PHONE_D}</a>
      </p>
    </aside>
  </div>
</section>

<section class="section section--cloud">
  <div class="container">
    <div class="center" style="margin-bottom:40px">
      <p class="eyebrow">Reviews</p>
      <h2>What Northern Virginia homeowners said</h2>
    </div>
    <div class="grid grid-3">{testimonials(3, idx)}</div>
  </div>
</section>

<section class="section section--navy section--tight">
  <div class="container">
    <p class="eyebrow">Also serving</p>
    <h2 style="margin-bottom:20px">Nearby communities</h2>
    <ul class="area-links">{others}</ul>
  </div>
</section>

{cta_band(f"Need a roofer in {name}?",
          "Free inspection, photographs of what we find, and a written estimate you can compare.")}
"""

    # Per-city service schema so each page carries its own local signal.
    extra = f"""
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Service",
    "serviceType": "Roofing",
    "provider": {{ "@id": "{SITE}/#business" }},
    "areaServed": {{ "@type": "City", "name": "{name}", "addressRegion": "VA", "addressCountry": "US" }},
    "url": "{SITE}/{slug}.html"
  }}
  </script>
"""
    page(f"{slug}.html",
         f"Roofing Contractor in {name}, VA | Roof Repair &amp; Replacement | Lyons Contracting",
         f"Roof replacement, repair and storm damage in {name}, Virginia. 25+ years, 4.9 on "
         f"Google, free estimates. Serving {c['hoods'][0]}, {c['hoods'][1]} and nearby. "
         f"Call 703-299-8888.",
         body, active="index.html", extra_ld=extra)


for _i, (slug, name) in enumerate(CITIES):
    city_page(slug, name, _i)


# --------------------------------------------------------------------------
# 404
# --------------------------------------------------------------------------

notfound = f"""
<section class="page-hero">
  <div class="container center">
    <h1>That page isn't here</h1>
    <p style="margin:0 auto">The link may be old, or we may have moved it. Here's the way back.</p>
    <div class="hero-actions" style="justify-content:center;margin-top:28px">
      <a class="btn btn-primary btn-lg" href="index.html">Back to home</a>
      <a class="btn btn-ghost-light btn-lg" href="tel:{PHONE_T}">{icon('phone')} {PHONE_D}</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-3">
      <a class="card card-link svc-card" href="roof-replacement.html">
        <span class="svc-icon">{icon('home')}</span><h3>Roof Replacement</h3>
        <p>Full tear-off and installation.</p></a>
      <a class="card card-link svc-card" href="roof-repair.html">
        <span class="svc-icon">{icon('wrench')}</span><h3>Roof Repair</h3>
        <p>Leaks, flashing and slate.</p></a>
      <a class="card card-link svc-card" href="roof-cost.html">
        <span class="svc-icon">{icon('doc')}</span><h3>Roof Cost</h3>
        <p>Instant range calculator.</p></a>
    </div>
  </div>
</section>
{cta_band()}
"""
page("404.html", "Page Not Found | Lyons Contracting",
     "That page isn't here — but we can still help with your roof. Call 703-299-8888.",
     notfound, active="index.html")


# --------------------------------------------------------------------------
# sitemap.xml / robots.txt / manifest
# --------------------------------------------------------------------------

PAGES = ([("index.html", "1.0"), ("roof-replacement.html", "0.9"), ("roof-repair.html", "0.9"),
          ("storm-damage.html", "0.8"), ("emergency.html", "0.8"), ("roof-cost.html", "0.9"),
          ("gallery.html", "0.7"), ("about.html", "0.6"), ("contact.html", "0.8")]
         + [(f"{s}.html", "0.8") for s, _ in CITIES])

today = "2026-08-27"
urls = "\n".join(
    f"""  <url>
    <loc>{SITE}/{'' if p == 'index.html' else p}</loc>
    <lastmod>{today}</lastmod>
    <priority>{pr}</priority>
  </url>""" for p, pr in PAGES)

with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
    f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
""")

with open(os.path.join(OUT, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

with open(os.path.join(OUT, "site.webmanifest"), "w") as f:
    f.write("""{
  "name": "Lyons Contracting",
  "short_name": "Lyons",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#0d1733"
}
""")

print("Built %d pages + sitemap/robots/manifest" % (len(PAGES) + 1))
