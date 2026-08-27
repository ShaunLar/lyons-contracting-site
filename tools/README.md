# Page generator (optional)

The site in the parent folder is plain, editable HTML — you do **not** need these
scripts to work on it. Edit the `.html` files directly.

These are the generators used to produce the pages from one shared template, so the
header, footer and JSON-LD stay identical across all 16 pages. If you make a
sitewide change (a new nav item, a phone number change), it's faster to edit the
template here and re-run:

    python3 tools/pages_lyons.py

**Warning:** re-running overwrites every `.html` file in the parent folder. If you've
hand-edited pages, your changes will be lost. Once real photos and reviews are in,
stop using these and edit the HTML directly.
