# Mitothrum — working notes for Claude

Evidence-led affiliate site for at-home spa rituals (https://mitothrum.com).
Owner: Matthew Quinn. Static HTML/CSS/JS, no build step.

## Read first
- `RULES.md` — compliance and growth rules, each tied to a source. Follow it;
  when a revenue idea conflicts with a rule, the rule wins.
- `CHANGES.md` — history of the October 2026 revisions.
- `marketing/SOCIAL.md` — social playbook (YouTube, Instagram, TikTok,
  Facebook, Threads, Pinterest): disclosure stack, destinations, UTM tags,
  one-master workflow, cadence. Read before drafting any post or video.

## How changes go live
- Push to `main` → `.github/workflows/deploy.yml` uploads to GoDaddy over FTPS
  (secrets FTP_SERVER = cPanel shared IP, FTP_USERNAME, FTP_PASSWORD) into the
  site's own folder, `public_html/mitothrum.com`. The FTP account's Directory is
  that folder, so `server-dir` stays `./`. Commits touching only research/,
  RULES.md, CLAUDE.md or .github/ don't deploy.
- `public_html` itself belongs to waterdamagegwinnett.com (its own repo:
  mquinn52/Water-Damage-Gwinnett). Never deploy or rewrite anything outside
  `public_html/mitothrum.com`. The deploy's "Check the FTP target" step refuses
  to upload if the FTP root holds WDG site files or lacks `media/`.
- Never point `server-dir` at a subfolder to "fix" a wrong FTP root. An earlier
  account rooted at `public_html/mitothrum.com/deploy` silently published to
  `mitothrum.com/deploy/` for days. Fix the FTP account's Directory instead.
- Media (videos, large images) lives only in the server's `media/` folder,
  outside the repo and skipped by the deploy. To add one, the owner attaches
  the file to a GitHub release and runs the manual "Media upload" workflow
  (`.github/workflows/media-upload.yml`): one file, into media/ only, new
  name preferred (e.g. -v2), 644 permissions, public URL verified. Then link
  it from a page by pull request. Small text assets like captions go in
  `captions/`, which deploys normally.
- New pages: work on a branch and open a pull request; `pr-check.yml` runs the
  site rules (affiliate tag, rel=sponsored, disclosures, no
  SITESTRIPE-LINK-NEEDED placeholders). The owner merges.

## Automation already running
- `registry-check.yml` on every PR and push to main: `.github/scripts/registry_check.py`
  checks every page against `.github/registry.json` and the RULES.md rule cards,
  naming the rule ID, file, text and whether it's a violation or an approved
  exception. Strict and required on `main` since Nov 1, 2026: a violation blocks
  the merge. Planning baseline: Business Models v9 (Side Hustle Project).
- `monitor.yml` daily 7 a.m. ET and after each deploy: repo rules + every live
  sitemap URL loads and matches the repo; opens/closes `site-monitor` issues.
- `research.yml` Mondays: snapshots policy sources in `research/sources.json`
  (Google, Amazon Associates, Federal Register FTC feeds), saves snapshots on the
  `research-snapshots` branch (main requires the Registry check, which blocks
  the bot's direct pushes), opens a `research` issue on change; AI review needs an ANTHROPIC_API_KEY secret (on hold).

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
