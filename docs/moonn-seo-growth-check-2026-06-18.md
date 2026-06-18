# Moonn SEO Growth Check — 2026-06-18

## Scope

- Project: Moonn / Tatyana Munn site.
- Workstream: `moonn-five-page-seo-aeo-supervisor`.
- Branch: `codex/moonn-seo-audit`.
- Live domain under test: `https://мунн.рф/` (`https://xn--l1acaw.xn--p1ai/` for technical fetches).
- Legacy analytics lane: `https://moonn.ru/` only when explicitly labeled historical/legacy.
- Reindex scope remains limited to the approved five URLs plus sitemap; no 83-URL batch.

## Проверенные факты

### Raw live audit on `мунн.рф`

- Ran successfully:
  - `python scripts\moonn_five_page_seo_sprint_audit.py --packet docs\moonn-five-page-seo-packets-2026-05-21.json --base-url https://xn--l1acaw.xn--p1ai --out-prefix moonn-five-page-seo-sprint-audit-2026-06-18`
- New dated artifacts:
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-18.json`
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-18.md`
- DNS for `xn--l1acaw.xn--p1ai` resolves on this host.
- All 5 scoped live URLs on `мунн.рф` returned HTTP `200`.
- `https://xn--l1acaw.xn--p1ai/sitemap.xml` includes all 5 scoped URLs in this run.
- `https://xn--l1acaw.xn--p1ai/robots.txt` does not block the 5 scoped URLs.
- Raw canonical still matches `мунн.рф` / `xn--l1acaw.xn--p1ai` on all 5 scoped URLs.
- Source-level debt still remains:
  - gallery page raw HTML still contains placeholder strings `Your Name` and `Your Email`;
  - missing raw image `alt` persists across all 5 pages;
  - raw H1 remains non-canonical on camp (`0`), consultations (`2`) and reviews (`2`).

### Rendered audit durability

- Attempted today with an extended timeout:
  - `python scripts\moonn_five_page_seo_sprint_audit.py --packet docs\moonn-five-page-seo-packets-2026-05-21.json --rendered --base-url https://xn--l1acaw.xn--p1ai --out-prefix moonn-five-page-seo-sprint-audit-2026-06-18-rendered`
- Result:
  - the run timed out after about `904s`;
  - no dated rendered `2026-06-18` artifact was produced;
  - therefore today’s evidence remains raw-only.
- Supporting context from the already-present local `2026-06-15` rendered artifact:
  - camp rendered answer block was `1`;
  - gallery and exam-prep pages hit Playwright navigation timeouts;
  - consultations and reviews were left `not_requested`.
- Therefore the rendered quality gate is currently not green and not closed; it is blocked by audit-runtime instability, not by a proven fresh content regression on all 5 pages.

### GUI evidence status

- Fresh bounded GUI confirmation was attempted, but the active desktop state did not yield a reliable cabinet proof in this run.
- The last confirmed GUI evidence remains `2026-06-16`:
  - GSC for `sc-domain:xn--l1acaw.xn--p1ai` showed `Oops, you don't have access to this property`;
  - Yandex.Webmaster for `https://xn--l1acaw.xn--p1ai:443` showed that the site does not belong to the current operator.
- Therefore the canonical blocker text remains unchanged, but it was not freshly re-proven today: `новая property не подтверждена, traffic migration не доказан`.

### Local canon anchors

- `assets/moonn-five-page-seo-sprint-layer.js` exists in the canonical worktree.
- `git rev-parse --verify 49a093e` still resolves locally.

## Предположения / limits

- Today’s rendered quality signals are unproven end-to-end because the rendered audit path still does not complete within a bounded automation window.
- The `2026-06-15` rendered artifact is local workspace evidence, not yet a committed canonical report.
- Because the new-domain properties are not confirmed, legacy `moonn.ru` GSC/Metrika numbers still cannot be used as proof of `мунн.рф` migration.
- Because the fresh cabinet GUI proof did not complete today, property-access status is carried forward from the last confirmed `2026-06-16` evidence rather than newly asserted.

## Blockers

- `P0` New-domain property blocker: `новая property не подтверждена, traffic migration не доказан`.
- `P0` Rendered audit durability blocker: `--rendered` timed out again on `2026-06-18` after about `904s`, so the live rendered gate is not currently reliable enough for unattended daily proof.
- `P1` Source cleanup debt remains: gallery placeholders, missing image `alt`, and raw H1 anomalies.

## Не делалось

- No Tilda edits.
- No canonical rewrites in page settings.
- No privacy/legal edits.
- No GSC or Yandex.Webmaster submissions.
- No Yandex.Metrika edits.
- No 83-URL batch actions.
- No cabinet settings changes.

## Следующий action

1. Stabilize the rendered supervisor lane: inspect why Playwright still hangs long enough to exceed a `904s` window and make the rendered audit finish with a dated artifact again.
2. After rendered durability is restored, re-run a full rendered `мунн.рф` audit and confirm whether the camp AEO block is truly fixed or not.
3. In authenticated Chrome, re-check/add access to the GSC property for `мунн.рф` and confirm the Yandex.Webmaster host before any scoped reindex submission.
4. After property confirmation and a green rendered pass, submit only the 5 scoped URLs plus sitemap; do not submit the 83-URL batch.

## Self-review

- Что проверено: raw live HTTP/sitemap/robots/canonical state for all 5 scoped `мунн.рф` URLs; local canon anchors `assets/moonn-five-page-seo-sprint-layer.js` and commit `49a093e`; rendered audit runtime behavior.
- Что не получилось проверить свежо: полноценное GUI-подтверждение cabinet blocker для `мунн.рф` в этом run.
- Какие артефакты изменены: `docs/moonn-five-page-seo-sprint-audit-2026-06-18.{json,md}`, `docs/moonn-seo-growth-check-2026-06-18.md`, `docs/moonn-five-page-seo-change-ledger-2026-05-21.json`, `docs/moonn-seo-growth-backlog.md`, `docs/codex-chat-history.md`.
- Где риск преждевременного отчёта: нельзя объявлять five-page lane fully green, потому что property blocker не закрыт, а rendered quality gate по-прежнему не даёт датированный артефакт.
