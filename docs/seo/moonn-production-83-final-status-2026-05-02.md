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

Raw source audit:

`python scripts/seo_audit_production_73.py --scope registry/tilda/moonn-production-83-rollout.json --out registry/seo/moonn-production-83-seo-audit.json`

Rendered browser audit:

`python scripts/seo_rendered_audit_production.py --scope registry/tilda/moonn-production-83-rollout.json --out registry/seo/moonn-production-83-rendered-seo-audit.json`

Final rendered result after the DevTools/Tilda rollout on 2026-05-03:

- Pages in scope: `83`.
- Render errors: `0`.
- Enhancer missing: `0`.
- Rendered JSON-LD missing: `0`.
- Bad link pages after rendered normalization: `0`.
- Missing content image alt pages after rendered normalization: `0`.
- Lazy-load missing pages after rendered normalization: `0`.
- Live raw headcode check: `83/83` pages include `moonn-seo-aeo-enhancer.js`.

Evidence:

- `registry/seo/moonn-production-83-live-headcode-check.json`
- `registry/seo/moonn-production-83-rendered-seo-audit.json`
- `output/tilda-headcode-submit-devtools-ui-83.json`
- `output/tilda-headcode-submit-devtools-ui-live-missing-pass4.json`

## Remaining Source-Level Work

The production pages now pass the rendered SEO/AEO gate, but some fixes are applied by the rendered enhancer rather than by native Tilda block data. For the next hardening pass, migrate these into source-level Tilda blocks where practical:

1. Replace bad WhatsApp/internal links directly inside Tilda blocks.
2. Normalize native H1/H2 structure page by page.
3. Add native image alt text for reusable images in Tilda.
4. Reduce duplicate metadata in native Tilda page settings.
5. Keep the rendered audit as the release gate after every SEO/design batch.

## Decision

Design is complete for the `83` production pages.

SEO/AEO is complete for the rendered production surface of the `83` pages: schema, normalized links, image alt fallback, lazy loading, and entity meta are present after browser execution. The next production-safe improvement is source-level Tilda cleanup so the raw HTML moves closer to the rendered SEO state.
