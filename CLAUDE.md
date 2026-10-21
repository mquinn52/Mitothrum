# Mitothrum — working notes for Claude

Evidence-led affiliate site for at-home spa rituals (https://mitothrum.com).
Owner: Matthew Quinn. Static HTML/CSS/JS, no build step.

## Read first
- `RULES.md` — compliance and growth rules, each tied to a source. Follow it;
  when a revenue idea conflicts with a rule, the rule wins.
- `CHANGES.md` — history of the October 2026 revisions.

## How changes go live
- Push to `main` → `.github/workflows/deploy.yml` uploads to GoDaddy over FTPS
  (secrets FTP_SERVER = cPanel shared IP, FTP_USERNAME, FTP_PASSWORD) into
  `public_html`. Commits touching only research/, RULES.md, CLAUDE.md or
  .github/ don't deploy.
- `public_html` also contains the separate `waterdamagegwinnett.com` folder
  (its own repo: mquinn52/Water-Damage-Gwinnett). Never deploy or rewrite
  anything that would touch it.
- New pages: work on a branch and open a pull request; `pr-check.yml` runs the
  site rules (affiliate tag, rel=sponsored, disclosures, no
  SITESTRIPE-LINK-NEEDED placeholders). The owner merges.

## Automation already running
- `monitor.yml` daily 7 a.m. ET and after each deploy: repo rules + every live
  sitemap URL loads and matches the repo; opens/closes `site-monitor` issues.
- `research.yml` Mondays: snapshots policy sources in `research/sources.json`
  (Google, Amazon Associates, Federal Register FTC feeds), opens a `research`
  issue on change; AI review needs an ANTHROPIC_API_KEY secret (on hold).

## Hard rules (details in RULES.md)
- Amazon links: SiteStripe links with `tag=mitothrum-20` and `rel="noopener sponsored"`;
  disclosure line above every group of links. Claude can't create affiliate
  links — ask the owner for SiteStripe links.
- Never print prices (use $/$$/$$$ tiers) or quote Amazon reviews/ratings.
- No "we tested it", no invented reviews, cosmetic/wellness language only,
  cite studies, include who should skip a product.

## Open items (as of 2026-10-21)
- Branch `vitamin-c-comparison`: vitamin-c-serums.html needs four SiteStripe
  links (SkinCeuticals C E Ferulic 30 ml, Paula's Choice C15 20 ml, The
  Ordinary Vitamin C Suspension 23% 30 ml, Klairs Freshly Juiced 35 ml), sold
  by Amazon or the brand's official store, before the PR can merge.
- Product thumbnails in media/products look AI-generated or downloaded;
  replace with SiteStripe/brand-approved images or own photos.
- Next content: Sunday bath reset; diffusers/oils/steamers comparison;
  short-video scripts and pins for live comparisons.

## Environment notes
- The web-fetch tool may serve stale copies of pages; verify live changes with
  a cache-busting query (?v=…) or ask the owner to check in a private window.
