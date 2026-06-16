# Moonn SEO Growth Check — 2026-06-16

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
  - `python scripts\moonn_five_page_seo_sprint_audit.py --packet docs\moonn-five-page-seo-packets-2026-05-21.json --base-url https://xn--l1acaw.xn--p1ai --out-prefix moonn-five-page-seo-sprint-audit-2026-06-16`
- New dated artifacts:
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-16.json`
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-16.md`
- DNS for `xn--l1acaw.xn--p1ai` resolves on this host.
- All 5 scoped live URLs on `мунн.рф` returned HTTP `200`.
- `https://xn--l1acaw.xn--p1ai/sitemap.xml` includes all 5 scoped URLs in this run.
- `https://xn--l1acaw.xn--p1ai/robots.txt` does not block the 5 scoped URLs.
- Raw canonical now matches `мунн.рф` / `xn--l1acaw.xn--p1ai` on all 5 scoped URLs; the 4-page canonical mismatch seen on `2026-06-06` is no longer present in raw HTML.
- Source-level debt still remains:
  - gallery page raw HTML still contains placeholder strings `Your Name` and `Your Email`;
  - missing raw image `alt` persists across all 5 pages;
  - raw H1 remains non-canonical on camp (`0`), consultations (`2`) and reviews (`2`).

### Rendered audit durability

- Attempted twice today:
  - `python scripts\moonn_five_page_seo_sprint_audit.py --packet docs\moonn-five-page-seo-packets-2026-05-21.json --rendered --base-url https://xn--l1acaw.xn--p1ai --out-prefix moonn-five-page-seo-sprint-audit-2026-06-16`
- Result:
  - first attempt timed out after about `124s`;
  - second attempt timed out after about `364s`;
  - to keep append-only evidence clean, the final `2026-06-16` dated audit artifacts were regenerated as non-rendered only.
- Supporting context from the already-present local `2026-06-15` rendered artifact:
  - camp rendered answer block was `1`;
  - gallery and exam-prep pages hit Playwright navigation timeouts;
  - consultations and reviews were left `not_requested`.
- Therefore the rendered quality gate is currently not green and not closed; it is blocked by audit-runtime instability, not by a proven fresh content regression on all 5 pages.

### GUI evidence collected today

- In the real `Alexander` Chrome profile, Google Search Console for `sc-domain:xn--l1acaw.xn--p1ai` still opens `Oops, you don't have access to this property`.
- In the real `Alexander` Chrome profile, Yandex.Webmaster for `https://xn--l1acaw.xn--p1ai:443` shows the ownership blocker banner: `Сайт https://xn--l1acaw.xn--p1ai вам не принадлежит. Добавьте его в список ваших сайтов и подтвердите права на него, чтобы просматривать информацию.`
- Combined new-domain blocker for this run remains: `новая property не подтверждена, traffic migration не доказан`.

## Предположения / limits

- Today’s rendered quality signals are unproven end-to-end because the rendered audit path no longer completes within a bounded automation window.
- The `2026-06-15` rendered artifact is local workspace evidence, not yet a committed canonical report.
- Because the new-domain properties are not confirmed, legacy `moonn.ru` GSC/Metrika numbers still cannot be used as proof of `мунн.рф` migration.

## Blockers

- `P0` New-domain property blocker: `новая property не подтверждена, traffic migration не доказан`.
- `P0` Rendered audit durability blocker: `--rendered` timed out twice on `2026-06-16`, so the live rendered gate is not currently reliable enough for unattended daily proof.
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

1. Stabilize the rendered supervisor lane: inspect why Playwright stalls on gallery and exam-prep pages and make the rendered audit finish within a bounded timeout.
2. After rendered durability is restored, re-run a full rendered `мунн.рф` audit and confirm whether the camp AEO block is truly fixed or not.
3. In authenticated Chrome, verify/add access to the GSC property for `мунн.рф` and confirm the Yandex.Webmaster host before any scoped reindex submission.
4. After property confirmation and a green rendered pass, submit only the 5 scoped URLs plus sitemap; do not submit the 83-URL batch.

## Self-review

- Что проверено: raw live HTTP/sitemap/robots/canonical state for all 5 scoped `мунн.рф` URLs; GSC GUI access state for `sc-domain:xn--l1acaw.xn--p1ai`; Yandex.Webmaster GUI ownership state for `https://xn--l1acaw.xn--p1ai:443`; rendered audit runtime behavior.
- Какие артефакты изменены: `docs/moonn-five-page-seo-sprint-audit-2026-06-16.{json,md}`, `docs/moonn-seo-growth-check-2026-06-16.md`, `docs/moonn-five-page-seo-change-ledger-2026-05-21.json`, `docs/moonn-seo-growth-backlog.md`, `docs/codex-chat-history.md`.
- Где риск преждевременного отчёта: нельзя объявлять five-page lane fully green, потому что property blocker сохраняется, а rendered quality gate сейчас деградировал по времени выполнения.
