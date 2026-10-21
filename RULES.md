# Mitothrum rules

The rules every page and change on mitothrum.com must follow, and why. The weekly
research loop (`.github/workflows/research.yml`) watches the sources below and
opens an issue, plus a pull request revising this file when an API key is set,
whenever one of them changes. Rules marked **[auto]** are enforced by the daily
site monitor (`.github/workflows/monitor.yml`).

**Last reviewed:** October 20, 2026
**Goal:** earn affiliate revenue from honest, research-led content, without breaking
copyright law, privacy law, Google's guidelines, affiliate program terms or
generally accepted ethics. When a revenue idea conflicts with a rule, the rule wins.

## 1. Affiliate links and disclosure
- 1.1 **[auto]** Every Amazon link carries `tag=mitothrum-20` (or a page-specific tracking ID created in Associates Central) and `rel="sponsored"`. *Sources: Google outbound links; Google spam policies (link spam).*
- 1.2 **[auto]** Every page shows "As an Amazon Associate I earn from qualifying purchases." *Source: Amazon Associates Program Policies.*
- 1.3 A plain-language disclosure sits directly above each group of affiliate links, visible at the same time as the links, not only in the footer. *Source: FTC Endorsement Guides FAQ.*
- 1.4 Never put an Amazon tag on another network's link, and never earn twice on the same traffic. *Source: Amazon operating agreement (multiple programs).*
- 1.5 Generate links with SiteStripe or the API; never buy through our own links or ask friends to. *Source: Amazon operating agreement.*

## 2. Prices, ratings and reviews
- 2.1 Never print a product price. Use "See current price" links and relative tiers ($ / $$ / $$$). Amazon allows prices only from Amazon-served links or its API, with a timestamp if refreshed less than hourly. *Source: Amazon Program Policies.*
- 2.2 Never quote, count or summarize Amazon customer reviews or star ratings ("thousands of reviews"). *Source: Amazon Program Policies.*
- 2.3 Never write or imply "we tested it" unless we did. Never publish invented, AI-generated or paid reviews or testimonials. *Sources: FTC rule on fake reviews; methodology page.*

## 3. Content quality (Google)
- 3.1 Every product page adds original value: comparison, evidence, who should skip it, trade-offs. No pages that only restate merchant copy. *Source: Google spam policies (thin affiliation); Google reviews guidance.*
- 3.2 AI may help draft, but a person reviews every page before it publishes. No bulk-generated pages. *Sources: Google spam policies (scaled content abuse); Google gen-AI guidance.*
- 3.3 Specs come from brand pages, manuals or listings and are labeled as such; anything unverified says so. Superlatives ("hottest", "best", "most-cited") need a source or get cut.
- 3.4 Comparison pages carry a byline and a "Last reviewed" date, link to the methodology page, and link to other comparisons. *Source: Google helpful content (who, how, why).*
- 3.5 Offer more than one seller when practical (brand-direct affiliate links next to Amazon). *Source: Google reviews guidance.*

## 4. Health and safety claims
- 4.1 Cosmetic and wellness language only: no disease, treatment, cure, detox or guaranteed-outcome claims.
- 4.2 Cite the study behind every evidence claim, report null results, and never upgrade "associated with" to "proven".
- 4.3 Include who should skip a device (contraindications from the manual) and a safety note for heat and cold exposure.
- 4.4 "FDA-cleared" is stated only as the brand describes it, with the cleared use, and never as "FDA-approved".
- 4.5 **[auto]** Every page carries "Educational content — not medical advice."

## 5. Privacy
- 5.1 The privacy policy names every tracker the site loads (currently Google Analytics 4) and is updated before a new one is added.
- 5.2 Analytics loads only if the visitor hasn't opted out (Global Privacy Control signal or the privacy page button).
- 5.3 The concierge stays in the browser; any change that sends chat or email data to a server needs a privacy policy update first.
- 5.4 The email form must never claim to save an address until a provider is connected.

## 6. Copyright
- 6.1 Product images come from SiteStripe/API, brand-approved assets or our own photos, never copied or AI-generated depictions of real products.
- 6.2 Studies are paraphrased in our own words and linked; music and footage in videos are licensed or our own.

## 7. Growth priorities (revisit monthly)
1. One researched comparison page per week on a high-intent, higher-ticket query.
2. Short videos and pins for each comparison, with spoken and written disclosure, linking to the page.
3. Brand-direct affiliate programs beside Amazon, one route per product.
4. Email list once a provider is connected.
5. Ads only after about 25,000 monthly pageviews.

## Changelog
- 2026-10-20: First version, distilled from the October 2026 audit and research.
