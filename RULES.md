# Mitothrum rules

The rules every page and change on mitothrum.com must follow, and why. The weekly
research loop (`.github/workflows/research.yml`) watches the sources below and
opens an issue, plus a pull request revising this file when an API key is set,
whenever one of them changes. Rules marked **[auto]** are enforced by the daily
site monitor (`.github/workflows/monitor.yml`).

**Last reviewed:** October 29, 2026
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

## 8. Social video and email (added 2026-10-21)
- 8.1 Every video carries the affiliate disclosure on screen for its whole length, and in the caption. Spoken disclosure too when a video has a voiceover; disclose in the language of the video. *Source: [FTC Disclosures 101 for social media influencers](https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers); [FTC Endorsement Guides FAQ](https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking).*
- 8.2 YouTube: tick "includes paid promotion" on every product video. TikTok: turn on the commercial content disclosure for any post with product recommendations or links (undisclosed posts can lose For You eligibility). Platform labels are in addition to our own disclosure, never instead of it. *Sources: [YouTube paid promotion](https://support.google.com/youtube/answer/154235?hl=en); [TikTok content disclosure](https://ads.tiktok.com/resources/help/article/about-the-content-disclosure-setting-for-creators).*
- 8.3 "Affiliate link", "commissionable link" or a bare "Buy now" don't count as a disclosure on their own; a plain sentence near the link does, and "(paid link)" beside a link is acceptable. *Source: FTC Endorsement Guides FAQ.*
- 8.4 Email list: accurate sender and subject, identified as an ad where it is one, a postal address (a PO box or registered private mailbox is allowed), and opt-outs honored within 10 business days. *Source: [FTC CAN-SPAM guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business).*
- 8.5 Never buy followers, views or reviews. *Source: FTC fake reviews rule (2024).*

## 9. Search in the AI era (added 2026-10-21)
- 9.1 Original, point-of-view pages (evidence tables, who should skip it, a verdict) are the long-term lever; mass-produced pages are scaled content abuse. *Source: [Google: optimizing for generative AI search](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).*
- 9.2 No special markup or "AI optimization" tricks are needed for AI Overviews or AI Mode: pages must be indexed, eligible for a snippet, findable through internal links, with structured data that matches visible text. *Source: [Google: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features).*
- 9.3 Build hub pages per ritual that link to every comparison in it; track AI visibility in Search Console's reports, not third-party tools claiming Google data.

## 10. Brand vocabulary: "routine" vs "ritual" (added 2026-10-28, owner decision)
- 10.1 Use "routine" wherever readers search, scan or navigate: page titles, H1s, meta and og descriptions, structured-data descriptions, nav labels, section labels, buttons, Pinterest pin titles, how-to headings, the concierge's category answers, and llms.txt. The six categories are "the six routines."
- 10.2 Keep "ritual" only as brand voice: the category name "Rest & Ritual", the tagline "We read the studies; you enjoy the ritual.", the homepage H2 "One ritual, six ways in", and occasional editorial lines in body copy (e.g. "contrast completes the ritual"). Never in a title, H1 or meta description lead.
- 10.3 Keep the `#rituals` anchor, CSS class names and code identifiers unchanged so existing links don't break.
- 10.4 Social profile board and playlist names follow "routine" too (owner decision 2026-10-29): Pinterest boards read "Bath & Body Routines" and "Rest & Routines". The on-site category name "Rest & Ritual" (10.2) is unchanged; the board name deliberately differs from it.

## 11. Promotion hygiene (added 2026-10-29, adapted from Marketcall's affiliate rules)
Mitothrum has no Marketcall offer; these are the network-agnostic practices from
its rules that tighten what sections 1–4 already require. *Sources: [Marketcall Creative Submission Rules](https://help.marketcall.com/en/article/creative-submission-rules-1rj093s/); [Marketcall Sanctions](https://help.marketcall.com/en/article/sanctions-i1y27p/).*
- 11.1 Promote only what each program pays for. Read every program's terms (allowed traffic, excluded products, prohibited keywords) before linking, and the program's own page wins over general guidance.
- 11.2 Never present the site as the brand or an official store: no brand logos as our branding, no "official site" wording, no bidding on brand names if ads ever start (rule 7.5).
- 11.3 No discounts, coupons, rebates, cash-back, financing or "free" offers unless the merchant's program provides them and they're current.
- 11.4 No fake urgency: no countdown timers, "only 3 left", "today only" or fabricated screenshots, and no made-up badges or certifications (extends 2.3).
- 11.5 Warranty or guarantee mentions add "Terms set by the brand" and link the brand's own policy.
- 11.6 Superlatives in moderation; a page stacked with "best / cheapest / #1" fails review even when each one is sourced (extends 3.3).
- 11.7 Proofread before publishing: no unfilled placeholders (`{product}`, `{city}`), broken characters or cut-off text in images or pins.
- 11.8 Run your own landing pages on mitothrum.com only, never a free builder subdomain.
- 11.9 One account per program; never use incentivized clicks, bought traffic or third-party resold traffic.
- 11.10 Keep traffic records (Search Console, GA4, UTM-tagged social) able to show where clicks come from; programs can ask, and failing to answer is grounds for removal.
## Changelog
- 2026-10-29: Added 10.4 (social board names follow "routine").
- 2026-10-29: Added section 11 (promotion hygiene adapted from Marketcall's rules).
- 2026-10-28: Added brand vocabulary rule (routine vs ritual).
- 2026-10-21: Added social video, email and AI-search rules from verified research.
- 2026-10-20: First version, distilled from the October 2026 audit and research.
