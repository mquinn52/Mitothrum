# Mitothrum revision — October 20, 2026

## Fixed in these files
1. privacy.html — The old policy said the site runs no Google Analytics, but every page loads it. Rewritten to disclose GA4 and affiliate-click logging, with an analytics opt-out button and a Global Privacy Control section. Email list now described as "coming soon". Removed `noindex` (it conflicted with the page being in the sitemap).
2. All pages — Analytics now loads only if the visitor hasn't opted out (GPC signal or the privacy-page button). Affiliate-click events log the product page path only, not the full tracking URL.
3. script.js — The email form said "You're on the list" while saving nothing; it now says so honestly. Concierge points to the live sauna comparison. Keyword matching fixed ("rest" no longer fires on "interest"; "five" → "six").
4. sauna-blanket-comparison.html — "3624$" fixed to "$$$" (a shell variable had replaced "$$"). Tiers defined. Removed contradictions and unverifiable superlatives ("hottest blanket" while both are listed at ~176°F, "uniquely", "most-cited", unnamed "independent testing", "$5,000 setup"). Tent copy corrected (head usually stays outside). The 120-day guarantee now notes it applies to direct purchases, not Amazon orders. Added byline/date, cold-plunge safety note, and the 2023 RCT citation.
5. index.html — "Ask the AI" → "Ask the concierge" (it's rule-based, not AI). Comparisons table reflects the live page. Study sources added under Episode 1. RoC description reworded to cosmetic language.
6. llms.txt — Was stale (said the site has no product links and the concierge never names products). Rewritten. Sitemap dates updated.

## Still yours to do
- Product thumbnails (media/products/media-generation-*) look AI-generated or downloaded. Replace with SiteStripe/API images, brand-approved assets, or your own photos.
- Check the 2-month (shortest) data retention setting in Google Analytics → Admin → Data retention.
- If you get EU/UK traffic, add a consent banner (Google Consent Mode) before GA loads.
- Wire the email form to a provider, then restore a success message and name the provider in privacy.html.
- Add a named editor and, for health-adjacent pages, a credentialed reviewer.
- Verify each spec on the comparison page (sizes, warranties, ETL, 77-gallon) against current listings, and FDA clearances in FDA's database.
- Regenerate Amazon links from SiteStripe to drop search-session parameters (optional).
- Submit the sitemap in Search Console.

# Revenue update — October 20, 2026 (second pass)

## Added
- led-mask-vs-microcurrent.html — New buyer-intent comparison of the site's two highest-priced beauty picks (SpectraLite FaceWare Pro vs NuFACE Trinity). Specs from brand pages and the NuFACE manual. Covers contraindications, the red-light evidence (Wunsch & Matuschka 2014) and what "FDA-cleared" does and doesn't mean. No prices, no testing claims, disclosure above every link.
- Internal links: the Beauty devices and Infrared & sauna cards link to their comparisons; the hero's second button now goes to the comparisons; each comparison page links to the other.
- Sitemap, llms.txt and the concierge include the new page.
- Header button no longer wraps on small phones.

## Before publishing
- Check the new page's specs against the current Amazon listings (kit contents vary).
- In Associates Central, create a separate tracking ID per page (for example one for each comparison page) and swap it into that page's links, so you can see which pages earn.

# Incident and fixes — October 23, 2026

- **Site-wide 403 (≈1:01–1:30 PM ET).** A zip (`mitothrum-pinterest-update-20261023-v2.zip`) was extracted on the server outside the GitHub deploy. Its pages landed with mode 0660, which Apache can't read, so every page and llms.txt returned 403. FTP deploys keep a file's existing mode, so deploying didn't repair it. Fix: the deploy now resets web files to 644 after every upload (`.github/scripts/ftp_inspect.py`); `FTP inspect` (manual workflow) lists the server folder with modes.
- **Pinterest:** domain-verification meta tag on the homepage; Pinterest profile added to every page's Organization `sameAs`, footer "Follow" links, and llms.txt (same content the zip carried, now in the repo so deploys don't undo it).
- **Public exposure closed:** the server folder holds ~1 GB of old upload zips, index backups, notes (.md) and an old `mitothrum/` copy of the site, all downloadable. `.htaccess` now denies *.zip, *.md, *-backup-*.html and the deploy state file, and 404s `/mitothrum/`. Nothing was deleted — the owner can remove them in cPanel File Manager.
- **Rule going forward:** change the site through the repo only. Files uploaded or extracted by hand are overwritten by the next deploy and can break permissions.
