# Lyons Contracting — Demo Website

A fast, mobile-first, SEO-optimized static site for **Lyons Contracting**
(roofing contractor — 4930 A Eisenhower Ave, Alexandria, VA 22304 · 703-299-8888).

Built to fix the specific gaps in the current lyonscontracting.com that are costing
phone calls and estimate requests. No build tools, no frameworks — plain HTML/CSS/JS
that runs on any host.

> **This is a demo.** Several things on it are deliberately placeholders and must be
> replaced before it goes anywhere near a live domain. See §3.

> ## 🚫 NOINDEX IS ON — remove it before this goes live
>
> This repo is public and served from GitHub Pages, so every page carries
> `<meta name="robots" content="noindex, nofollow">` and `robots.txt` has
> `Disallow: /`. That stops Google indexing a public copy of Lyons' reviews and
> photos as a near-duplicate of lyonscontracting.com.
>
> **Leaving it on when the site goes live on their real domain would make the
> entire site invisible to Google.** To remove: set `DEMO_NOINDEX = False` in
> `tools/build_lyons.py` and re-run `python3 tools/pages_lyons.py`, or delete the
> meta tag from all 16 pages and restore `robots.txt` by hand.

---

## 1. Why this site exists — what the current site is losing

Findings from a teardown of the live lyonscontracting.com, in order of cost:

| # | Problem on the current site | Fixed here |
|---|---|---|
| 1 | **The phone number is not a link.** Zero `tel:` hrefs sitewide — on mobile, tapping it does nothing. The only fixed element on mobile is a scroll-to-top arrow. | Every number is a real `tel:` link (9 per page) plus a **sticky mobile call bar** on every screen |
| 2 | **Estimate form has 5 required fields + reCAPTCHA**, including a required "How did you hear about us?" dropdown asked before a stranger with a leaking roof gets any help | **Three fields**, no CAPTCHA (hidden honeypot instead), referral question dropped |
| 3 | **No photos of their own work.** All 13 homepage images are logos, favicons and award badges | Five of Lyons' own project photos throughout, plus a gallery and photo blocks on every city page |
| 4 | **No pricing or financing anywhere** | `roof-cost.html` with an instant estimate calculator and a financing section |
| 5 | **Emergency pages carry no urgency** — no response promise, no after-hours path, hours are M–F 7–7 | `emergency.html` with a what-to-do-now guide and a stated callback commitment |
| 6 | **Form only on 2 pages** | Lead form on every service and city page, with reviews above it |
| 7 | **Schema says `Organization`** — no `LocalBusiness`, no address, no hours, no `areaServed`, no rating, despite displaying 4.9 on Google | Full `RoofingContractor` JSON-LD sitewide + per-city `Service` schema + `FAQPage` |
| 8 | **Templated ~550-word city pages** with no neighborhoods, no local photos, no local proof | Six rewritten city pages with real neighborhoods and genuinely local content |
| 9 | **Duplicate indexed pages** (`/alexandria/` vs `/alexandria-roofing/`, six `/news-old/*`) | Clean flat structure, one page per intent |
| 10 | **No call tracking** — GA4 and Meta Pixel installed, but the phone (where the revenue is) is invisible | See §4 |

---

## 2. Pages

| File | Purpose |
|------|---------|
| `index.html` | Home — hero + quick form, services, why-us, process, gallery, reviews, FAQ |
| `roof-replacement.html` | Money page — what a full replacement includes |
| `roof-repair.html` | Money page — leaks, flashing, valleys, slate, repair-vs-replace |
| `storm-damage.html` | Money page — wind/hail damage and insurance claims |
| `emergency.html` | High-urgency page — active leak, what to do while you wait |
| `roof-cost.html` | Money page — instant cost calculator + financing |
| `gallery.html` | Project photo gallery |
| `about.html` | Company story, sheet metal shop, certifications |
| `contact.html` | Free-estimate form + full contact info |
| `alexandria.html` `arlington.html` `falls-church.html` `mclean.html` `springfield.html` `fairfax.html` | Six local landing pages |
| `404.html` | Not-found page |
| `sitemap.xml` · `robots.txt` · `site.webmanifest` | Crawl + PWA files |

Shared assets: `css/styles.css` (all colors are CSS variables at the top) and
`js/main.js` (nav, FAQ, scroll reveal, calculator, form handling).

---

## 3. What's real, and what still needs Lyons' input

### ✅ Real — sourced, not invented

**The reviews are genuine.** All ten testimonials are real Google reviews published
verbatim on lyonscontracting.com, with the reviewers' real names: Deborah Brautigam,
Catherine Steadman, Caryn Thiboheim, Lino Miani, Hassan Aden, Adam Szczypka,
Rebecca Gould, Kent Rogers, MHL and Tom P. Longer ones are trimmed with an ellipsis;
wording is otherwise untouched. Worth re-checking against the live Google profile
before launch, but nothing here is fabricated.

**The photos are Lyons' own work**, pulled from their Houzz portfolio
(`houzz.com/professionals/roofing-and-gutters/lyons-contracting-pfvwus-pf~504818024`)
— uploads they posted themselves, so ownership is clean:

| File | What it shows |
|---|---|
| `slate-mansard-copper-dormers-old-town.jpg` | Slate mansard with three hand-fabricated copper oval dormer vents — unmistakably Old Town |
| `copper-cupola-weathervane.jpg` | Hand-formed copper bell-curve cupola with horse weathervane — the sheet metal shop story in one image |
| `shingle-copper-bay-alexandria.jpg` | Architectural shingle plus custom copper standing-seam bay roof |
| `standing-seam-metal-mclean.jpg` | Dark standing seam metal roof with dormers |
| `flat-membrane-roof-studio.jpg` | White single-ply membrane flat roof on a modern studio |

**Tom Petrilli is named on the About page.** Customers name him repeatedly in their own
reviews, so the site is built around the thing that's actually working: people trust Tom.

### ⚠️ Still needs Lyons

- **Star-rating schema is commented out.** Each page carries an `aggregateRating` block inside an HTML comment with `REPLACE_WITH_REAL_COUNT`. The 4.9 is real (it's on their own site) but the review *count* needs confirming on the Google Business Profile before it's published — a rating that doesn't match visible reviews is a structured-data violation.
- **A photo of Tom.** `about.html` has a marked slot for `images/tom-petrilli.jpg`. This is the single easiest high-impact addition.
- **Four gallery slots** on `gallery.html` are still grey placeholders (Rosemont slate valley, Springfield tear-off, Fairfax storm rebuild, Vienna tile). Ask for job photos — they'll have hundreds.
- **Calculator prices are ballparks, not Lyons' pricing.** The per-square-foot figures in `js/main.js` (`PRICE`, `STORY_MULT`, `COMPLEX_MULT`, `TEAR_OFF`) are reasonable Northern Virginia numbers. Replace with real ones. The financing figure assumes 120 months at ~9.99% — swap in the lender's actual terms.
- **The form doesn't deliver anywhere yet.** Falls back to the visitor's mail client at `INFO@LYONSCONTRACTING.COM` (a guess — confirm the real lead address). See §4a.
- **No financing partner connected.** `roof-cost.html` says financing is available but has no application link. Connect a lender or soften the copy.
- **After-hours arrangement undecided.** `emergency.html` has a `NOTE TO OWNER` about this. Decide what happens on a 9pm Saturday call. **Don't promise 24/7 unless someone answers.**
- **"25+ years"** comes from their own copy. Confirm the real founding year — a specific year converts better than a rounded claim.

## 4. Three things to do before going live

### a) Make the form deliver leads (~5 min)
1. Go to [web3forms.com](https://web3forms.com) (or Formspree.io), enter the lead email, get an **Access Key / endpoint URL**.
2. Find `action="#FORM_ENDPOINT"` — it appears once per form, on every page — and replace it with the endpoint.
3. For Web3Forms, add inside each form: `<input type="hidden" name="access_key" value="YOUR-KEY">`

`js/main.js` automatically switches to AJAX submission with an inline thank-you once
a real endpoint is present.

### b) Turn on call tracking — day one
This is how the whole engagement gets proven. The current site tracks clicks (GA4 +
Meta Pixel are installed) but not calls, so most of Lyons' leads are invisible to
their own analytics.

- Add a call-tracking number with dynamic number insertion (CallRail or similar)
- Fire a GA4 conversion on `tel:` taps **and** form submits
- Baseline the current numbers **before** launch so the before/after is defensible

### c) Hook up Google
- **Google Business Profile** — name/address/phone must match this site *exactly*
- **Google Search Console** — add the site, submit `sitemap.xml`
- **301 redirects** from the old URLs, especially `/news-old/*` → the live service pages and `/alexandria-roofing/` → `/alexandria.html`
- Embed a Google Map on `contact.html` (see the `NOTE TO OWNER` there)

---

## 5. The single highest-value ask: photos

Lyons has 25+ years of completed roofs and not one of them is on their website.
Homeowners making a $15k–$40k decision want to see slate on an Old Town rowhouse
and standing seam on a Del Ray bungalow. A badge proves you're legitimate; a
photograph proves you're good.

**Ask for the job photos in the first meeting.** It's a small, free yes, and a demo
populated with real Lyons roofs is a completely different conversation.

To add them:
1. Drop images into `images/`
2. Replace `<span class="ph-label">…</span>` inside each `<figure class="tile">` with:
   ```html
   <img src="images/your-photo.jpg"
        alt="Slate roof restoration in Old Town Alexandria VA"
        loading="lazy">
   ```
3. **Always write alt text naming the work AND the city** — it helps accessibility and local search.

---

## 6. Editing & deploying

**Edit:** open any `.html` in a text editor. Colors live as CSS variables at the top
of `css/styles.css` — change `--gold-500` / `--navy-900` to re-theme the whole site.

The header and footer markup is repeated on each page. If you change one, change all
(or have a developer add server-side includes).

**Preview locally:**
```bash
python3 -m http.server 8000
```
then open `http://localhost:8000`.

**Deploy — pick one:**
- **Netlify / Cloudflare Pages / GitHub Pages** — drag-and-drop this folder. Free, fast, HTTPS. (Netlify also gives you free form handling as an alternative to §4a.)
- **Their current host (SiteGround)** — upload to the web root via FTP. Note this replaces a live WordPress install; back it up first and keep the redirects from §4c.

---

## 7. Verified against the build

- 9 `tel:` links per page, 0 on the current live site
- All JSON-LD blocks parse as valid JSON
- All internal links resolve — no 404s
- Every referenced image file exists — no broken images
- No horizontal overflow at 375px
- All tap targets ≥ 44px
- Single `<h1>` per page
- Every image has descriptive alt text naming the work and the city

---

*Business details encoded site-wide: Lyons Contracting · 4930 A Eisenhower Ave,
Alexandria, VA 22304 · 703-299-8888 · Mon–Fri 7:00 AM–7:00 PM · GAF, Firestone and
Revere certified. Update these in the footer of each page and in the JSON-LD blocks
if anything changes.*
