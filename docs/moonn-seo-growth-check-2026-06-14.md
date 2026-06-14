# Moonn SEO Growth Check — 2026-06-14

## Scope

- Project: Moonn / Tatyana Munn site.
- Workstream: `moonn-five-page-seo-aeo-supervisor`.
- Branch: `codex/moonn-seo-supervisor-20260614` from `origin/codex/moonn-seo-audit`.
- Live domain under test: `https://мунн.рф/` (`https://xn--l1acaw.xn--p1ai/` for technical fetches).
- Legacy analytics lane: `https://moonn.ru/` only when explicitly labeled historical/legacy.
- Weekly privacy/RKN lane was not run in this pass because the weekly gate is Monday-only and today is `2026-06-14`.

## Проверенные факты

### 1. Live `мунн.рф` technical / rendered audit

- Ran:
  - `python scripts\moonn_five_page_seo_sprint_audit.py --packet docs\moonn-five-page-seo-packets-2026-05-21.json --rendered --base-url https://xn--l1acaw.xn--p1ai --out-prefix moonn-five-page-seo-sprint-audit-2026-06-14`
- New dated artifacts:
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-14.json`
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-14.md`
- DNS for `xn--l1acaw.xn--p1ai` resolves on this host.
- All 5 scoped live URLs on `мунн.рф` returned HTTP `200`.
- `https://xn--l1acaw.xn--p1ai/sitemap.xml` includes all 5 scoped URLs in this run.
- `https://xn--l1acaw.xn--p1ai/robots.txt` does not block the 5 scoped URLs.
- Rendered H1 count is `1` on all 5 URLs.
- Rendered answer block count:
  - camp `/podrostkovyy-lager-psihologiya` -> `0`;
  - other 4 pages -> `1`.
- Canonical status:
  - camp `/podrostkovyy-lager-psihologiya` stays on new-domain canonical;
  - gallery, exam prep, consultations and reviews still expose `canonical_mismatch` to legacy `https://moonn.ru/...`.
- Raw source debt still visible:
  - camp raw title/description are still not aligned with the 2026-05-21 packet;
  - gallery raw HTML still contains placeholder strings `Your Name` and `Your Email`;
  - missing raw image `alt` persists across all 5 pages;
  - raw H1 remains non-canonical on camp (`0`), consultations (`2`) and reviews (`2`).

### 2. Search-console / webmaster lane

- In the real `Alexander` Chrome profile, direct GSC open for `sc-domain:xn--l1acaw.xn--p1ai` still shows `Oops, you don't have access to this property`.
- In the same profile, direct GSC open for legacy property `https://moonn.ru/` now also lands on `Oops, you don't have access to this property`.
- Direct Yandex.Webmaster open for `https://xn--l1acaw.xn--p1ai:443` opened a Yandex `404` page in this run; today I did not reproduce the older orange ownership banner.
- New-domain blocker wording remains unchanged:
  - `новая property не подтверждена, traffic migration не доказан`.

### 3. Legacy analytics lane

- In the real `Alexander` Chrome profile, Yandex.Metrika counter `96397286` is accessible.
- Current visible default weekly slice is `8 июня - 14 июня` for `Сайт moonn.ru`.
- Visible legacy Metrika aggregates in this slice:
  - `32` pageviews;
  - `21` visits;
  - `20` visitors;
  - `44 c` average time on site;
  - `1,52` depth;
  - `28,57%` bounce rate.
- This is still legacy-domain evidence and not proof of `мунн.рф` host migration.

### 4. MIIIIPS / deploy side-lane

- `https://school.miiiips.ru/` returns HTTP `200`.
- `https://school.miiiips.ru/robots.txt` returns HTTP `200`.
- `https://school.miiiips.ru/sitemap.xml` returns HTTP `200`.
- MIIIIPS PR `#11` merge/deploy provenance is still not verifiable from this repo context because the canonical repo+PR URL is still missing.

## Предположения / limits

- Today’s GSC and Yandex.Webmaster results are GUI-only access checks; no cabinet settings were changed.
- The legacy Yandex.Metrika numbers were captured from the default weekly dashboard slice, not from the required custom period `2026-04-29..2026-06-14`.
- Because both new-domain and legacy GSC direct opens now fail in the Alexander profile, today’s run cannot confirm whether this is a property-removal event, a profile/session regression, or only a route-specific access issue.

## Blockers

- `P0` New-domain property blocker: `новая property не подтверждена, traffic migration не доказан`.
- `P0` Search-console access regression: today the Alexander profile could not open either `sc-domain:xn--l1acaw.xn--p1ai` or legacy `https://moonn.ru/` in GSC.
- `P0` Canonical migration is still incomplete on 4 of the 5 scoped live pages.
- `P0` Camp page remains the main live quality blocker: rendered answer block is `0`, and raw title/description still drift from the sprint packet.
- `P0` Yandex.Webmaster route for `мунн.рф` is not stable: the direct route used today returns `404`, so verified host evidence is still absent in this run.
- `P1` Analytics contract is still incomplete for `2026-04-29..today`: no custom-period GSC, no host-split Metrika evidence, no top queries/landing pages/goals in this run.
- `P1` MIIIIPS PR `#11` merge/deploy verification remains blocked by missing canonical PR URL.

## Не делалось

- No Tilda edits.
- No canonical rewrites in page settings.
- No GSC or Yandex.Webmaster submissions.
- No Yandex.Metrika settings changes.
- No privacy/legal edits.
- No screenshots were saved or committed.
- No 83-URL batch actions.

## Следующие действия

1. Recover the canonical GSC access path for both `sc-domain:xn--l1acaw.xn--p1ai` and legacy `https://moonn.ru/` in the Alexander profile, then record whether this is a real permissions loss or only a route/session regression.
2. Fix native canonical on the remaining 4 scoped `мунн.рф` pages at Tilda source before any new-domain reindex claims.
3. Inspect the camp page in Tilda source for the missing rendered answer block and the stale raw title/description.
4. Recover a stable Yandex.Webmaster route for `https://xn--l1acaw.xn--p1ai:443` and prove either verified-host access or explicit absence.
5. Capture the required custom analytics period `2026-04-29..2026-06-14` from Metrika/GSC once cabinet access is restored; keep it separated into legacy-domain vs new-domain evidence.
6. Prepare source-cleanup packet for gallery placeholders, missing image `alt`, and raw H1 anomalies across the 5 scoped pages.
7. Record the canonical MIIIIPS PR `#11` repo+PR URL in a stable registry/doc or remove this stale checklist item from future runs if the PR reference is no longer canonical.

## Self-review

- Что запрошено: ежедневный Moonn SEO/privacy supervisor с live-domain canon `мунн.рф`, analytics/growth separation and privacy gate discipline.
- Что реально сделано: checked git routing, isolated a clean supervisor worktree, reran the five-page rendered audit on `мунн.рф`, verified current GUI access state for GSC/Yandex.Metrika/Yandex.Webmaster, and rechecked `school.miiiips.ru` live HTTP.
- Что фактически проверено: live HTTP/sitemap/robots/rendered state for the 5 scoped `мунн.рф` URLs; current GSC access failure for both new and legacy properties in Alexander Chrome; current legacy Metrika weekly metrics for counter `96397286`; current `school.miiiips.ru` HTTP 200 for root/robots/sitemap.
- Где риск преждевременного отчёта: live `мунн.рф` availability must not be reported as completed migration while new-domain property access is still blocked and 4 pages still canonicalize to `moonn.ru`.
