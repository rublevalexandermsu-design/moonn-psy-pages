# Moonn H1/H2 Implementation Status — 2026-05-06

Scope: original published Moonn pages in the 83-page production SEO set.

## Verified Result

- Live production audit after the pilot checked `83` URLs.
- `83/83` returned HTTP `200`.
- `missing_h1` changed from `44` to `43`.
- `multiple_h1` remains `14`.
- Confirmed live fix: `https://moonn.ru/aromatherapy`.
  - Tilda page `62470081`, record `860030752`, block type `485`.
  - Applied through real Google Chrome / Tilda block settings.
  - Supported UI field used: `SEO: тег для заголовка -> H1`.
  - Live HTML now contains `<h1>` for `Ароматерапия и психология`.

## Implementation Gate Found

The original 52-action plan cannot be applied blindly.

- Block type `485` supports the SEO heading tag field. Pilot succeeded.
- Block type `18` was tested on `https://moonn.ru/emotional-intelligence/`, record `1500161991`.
  - Tilda block settings open correctly.
  - The field `SEO: тег для заголовка` is not present.
  - There are `23` planned `H1` actions of this type.
- Block type `578` was tested on `https://moonn.ru/otzivi`, record `1352757211`.
  - Tilda block settings open correctly.
  - The field `SEO: тег для заголовка` is not present.

Conclusion: many H1/H2 defects are not fixable by simply setting a block-level SEO tag. The safe route is to split the work by Tilda block capability instead of forcing unsupported UI changes.

## Current Artifacts

- Live audit: `docs/moonn-production-scope-seo-audit-2026-05-06.json`
- Human audit: `docs/moonn-production-scope-seo-audit-2026-05-06.md`
- H1/H2 source packet: `docs/moonn-h1-h2-source-cleanup-packet-2026-05-06.json`
- Tilda block map: `docs/moonn-h1-h2-block-map-2026-05-06.json`
- Initial UI apply plan: `docs/moonn-h1-h2-ui-apply-plan-2026-05-06.json`
- UI apply report: `docs/moonn-h1-h2-ui-apply-report-2026-05-06.json`

## Next Safe Plan

1. Keep `/aromatherapy` as the confirmed applied pilot.
2. Rebuild the H1/H2 plan into three buckets:
   - `supported_block_setting`: only block types proven to expose `SEO: тег для заголовка`.
   - `unsupported_needs_design_solution`: blocks like type `18`, where Tilda does not expose the field.
   - `manual_verify`: ambiguous blocks that require a visual field check before live changes.
3. For unsupported missing-H1 pages, choose one supported Tilda design solution before applying at scale:
   - add a dedicated lightweight H1 text block to the page;
   - replace the hero block with a Tilda block type that outputs a semantic H1;
   - keep visual design but add an approved semantic heading block, then verify live HTML.
4. For multiple-H1 pages, test each secondary heading block type once before batch work. If no SEO-tag field exists, fix by changing the block design/source structure, not by unsupported endpoints.
5. After each applied bucket, publish and rerun `python scripts/moonn_final_seo_audit.py --production-scope`.

## Open Decision

To complete H1/H2 fully, the remaining unsupported pages need a design-level decision: whether to add a visible/lightweight semantic H1 block or replace the current hero/title block type. I should not inject hidden headings or runtime JavaScript as the primary SEO fix without approval, because that is weaker and may be treated as manipulative or unreliable by search engines.
