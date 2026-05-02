# Moonn.ru production 83-page SEO/design status

Date: 2026-05-02
Workstream: Moonn production SEO/design rollout
Branch: `codex/tilda-api-sync`

## Scope Decision

The production scope is expanded from `73` to `83` pages as:

- the previously verified `73` original production pages;
- plus the next `10` published production pages that have real aliases and clear SEO value.

Blank-alias legacy pages were not added automatically because they often resolve through `pageNNN.html` filenames and can be test/technical duplicates rather than canonical SEO pages.

Canonical scope: `registry/tilda/moonn-production-83-rollout.json`.

## Added 10 Pages

1. `https://moonn.ru/novosti`
2. `https://moonn.ru/emotional-intelligence/knowledge-base/male-loneliness-russia`
3. `https://moonn.ru/articles/eq-dlya-rukovoditeley`
4. `https://moonn.ru/emotional-intelligence/diagnostoka-ei`
5. `https://moonn.ru/emotional-intelligence/ei-leader-12`
6. `https://moonn.ru/emotional-intelligence/knowledge-base/personal-boundaries`
7. `https://moonn.ru/emotional-intelligence/knowledge-base/active-listening`
8. `https://moonn.ru/emotional-intelligence/knowledge-base/emotional-contagion`
9. `https://moonn.ru/emotional-intelligence/knowledge-base/psychological-safety`
10. `https://moonn.ru/emotional-intelligence/knowledge-base/emotional-maturity`

## Verified Done

- Live availability: `83/83` production URLs return `200 OK`.
- Production design: `83/83` pages include the verified `Radiant Sanctuary` theme marker and pinned CSS.
- The `10` added pages were updated and published through Tilda UI automation.
- The trailing-slash canonical case for `/emotional-intelligence/` is preserved in the `83`-page scope.
- SEO/AEO schema manifest generated for all `83` pages:
  `registry/seo/moonn-production-83-schema-snippets.json`.
- Source-link issue queue generated:
  `registry/seo/moonn-production-83-link-issue-pages.json`.

## Current Live Audit

Source: `python scripts/seo_audit_production_73.py --scope registry/tilda/moonn-production-83-rollout.json --out registry/seo/moonn-production-83-seo-audit.json`

- Pages in scope: `83`.
- `200 OK`: `83`.
- Errors: `0`.
- Theme missing: `0`.
- Schema missing in live HTML: `83`.
- JSON-LD missing in live HTML: `82`.
- Pages with bad source links: `46`.
- Bad link totals:
  - `http://wa.me/79777770303`: `73`;
  - `http://twa.me/79777770303`: `4`;
  - `http://.moonn.ru`: `28`.
- Heading issue pages: `63`.
- Image alt issue pages: `83`.
- Duplicate title groups: `1`.
- Duplicate description groups: `4`.

## Not Complete Yet

The following SEO items are still not complete in live HTML and require source-level Tilda edits:

1. Fix bad links inside page blocks on `46` pages.
2. Normalize H1/H2 structure on `63` pages.
3. Add meaningful alt text to images on `83` pages.
4. Resolve duplicate title/description groups.
5. Publish JSON-LD/schema only after a reliable Tilda save path is proven by Tilda API/export and live HTML.

## Decision

Design is complete for the `83` production pages.

SEO/AEO is structurally prepared and audited, but not fully complete in live HTML. The next production-safe step is batch source-link cleanup because it is a real technical SEO defect visible to users and crawlers.
