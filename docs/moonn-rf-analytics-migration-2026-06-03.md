# Moonn RF Analytics Migration — 2026-06-03

Контур: Moonn SEO / analytics-domain-migration.
Ветка: `codex/moonn-seo-audit`.

## Цель

Перевести ежедневные SEO/analytics supervisor-задачи с аварийного/исторического доменного контура `moonn.ru` на текущий live-домен `мунн.рф`, не смешивая старую аналитику и новую видимость.

## Проверенные факты

- Текущий live-домен: `https://мунн.рф/`.
- Punycode: `https://xn--l1acaw.xn--p1ai/`.
- `https://мунн.рф/` отвечает HTTP `200`.
- `moon.ru` с одной `n` не относится к проекту Moonn и не должен использоваться в проверках.
- Google Search Console на скрине и в предыдущем GUI-прогоне открыта для legacy property `https://moonn.ru/`.
- Последние legacy GSC numbers для `https://moonn.ru/`: `245` clicks, `14.6K` impressions, CTR `1.7%`, average position `7.4`, `40` indexed pages, `135` not indexed pages.
- Последний legacy Yandex.Metrika weekly slice для counter `96397286`: `105` pageviews, `78` visits, `69` visitors.

## Канонический доменный контракт

| Layer | New domain value | Legacy value | Rule |
| --- | --- | --- | --- |
| Human URL | `https://мунн.рф/` | `https://moonn.ru/` | Human-facing reports show `мунн.рф` as live domain. |
| Technical URL | `https://xn--l1acaw.xn--p1ai/` | `https://moonn.ru/` | Scripts may use punycode for DNS/HTTP stability. |
| Google Search Console | `https://мунн.рф/` or domain property for `мунн.рф` | `https://moonn.ru/` | Legacy GSC data must be labelled legacy until new property is verified. |
| Yandex.Webmaster | `https://мунн.рф/` | `https://moonn.ru` | Reindex should target `мунн.рф` scoped URLs only. |
| Yandex.Metrika | same counter only if host attribution includes `мунн.рф`; otherwise new/corrected counter setting is needed | counter `96397286` | Do not claim new-domain traffic from old-domain reports. |
| Google Analytics / Google tag | property/data stream must include `мунн.рф` | old host stream if present | Verify host/domain in Admin before using traffic as new-domain evidence. |

## Required external cabinet actions

These are settings actions in authenticated Alexander/Rublev browser profile. They are not complete until GUI/API evidence is recorded.

1. Google Search Console:
   - Add or verify property for `https://мунн.рф/` or domain-level `мунн.рф`.
   - Submit `https://мунн.рф/sitemap.xml`.
   - Request URL inspection/reindex only for the scoped URLs in `docs/moonn-rf-five-page-reindex-urls-2026-06-03.txt`; do not submit the old 83-URL batch.

2. Yandex.Webmaster:
   - Add/verify host `https://мунн.рф/`.
   - Submit the scoped URLs from `docs/moonn-rf-five-page-reindex-urls-2026-06-03.txt`.
   - Record statuses as `queued`, `processed`, `error`, or `not verified`.

3. Yandex.Metrika:
   - Verify that counter `96397286` receives visits for host `мунн.рф`.
   - If counter settings are locked to `moonn.ru`, update allowed domains/site URL to `мунн.рф` or create a documented follow-up for the owner.
   - Exclude supervisor/test querystrings from growth reads where possible.

4. Google Analytics / Google tag:
   - Verify GA property/data stream host is `мунн.рф` or add/update the web stream.
   - Do not create duplicate measurement unless the old stream cannot be safely repointed.

## Local changes made in this contour

- `scripts/moonn_five_page_seo_sprint_audit.py` now supports `--base-url`.
- `scripts/moonn_privacy_compliance_audit.py` now supports `--base-url`.
- `data/site.json` now stores `мунн.рф` as the current brand domain.
- `docs/moonn-rf-five-page-reindex-urls-2026-06-03.txt` defines the new scoped reindex set.
- Both Codex automations were updated outside Git so future runs treat `мунн.рф` as current live domain and `moonn.ru` as legacy analytics unless explicitly proven otherwise.

## 2026-06-03 Local Verification

Ran:

```powershell
python scripts\moonn_five_page_seo_sprint_audit.py --packet docs\moonn-five-page-seo-packets-2026-05-21.json --base-url https://мунн.рф --out-prefix moonn-rf-five-page-seo-sprint-audit-2026-06-03
python scripts\moonn_privacy_compliance_audit.py --base-url https://мунн.рф --preflight-timeout 8 --timeout 8 --max-urls 8
```

Verified:

- DNS for `мунн.рф` resolves.
- Five scoped pages return HTTP `200`.
- `robots.txt` does not block the five scoped pages.
- New-domain audit artifacts were written:
  - `docs/moonn-rf-five-page-seo-sprint-audit-2026-06-03.json`
  - `docs/moonn-rf-five-page-seo-sprint-audit-2026-06-03.md`
  - `docs/moonn-privacy-compliance-audit-2026-06-03.json`
  - `docs/moonn-privacy-compliance-audit-2026-06-03.md`

Detected blockers:

- The five scoped pages are not detected in `https://мунн.рф/sitemap.xml`.
- The five scoped pages still report `canonical_mismatch`, which likely means live Tilda metadata still points to `moonn.ru`.
- Privacy endpoints on `мунн.рф` return `404`: `/privacy`, `/personal-data-consent`, `/cookies`, `/data-subject-request`.
- Smoke privacy scan found forms without detected checkbox signals on the first 8 checked URLs.

## Ready Gate

The migration is not complete until all of these are true:

1. `python scripts\moonn_five_page_seo_sprint_audit.py --packet docs\moonn-five-page-seo-packets-2026-05-21.json --base-url https://мунн.рф --rendered` completes without DNS/live blockers.
2. GSC has verified property evidence for `мунн.рф`.
3. Yandex.Webmaster has verified host evidence for `мунн.рф`.
4. Yandex.Metrika or GA evidence explicitly shows traffic by host `мунн.рф`.
5. Reports keep legacy `moonn.ru` metrics separate from new-domain `мунн.рф` metrics.

## Blockers

- External Google/Yandex cabinet changes require authenticated GUI confirmation. Do not report property/counter creation as complete unless the cabinet page confirms it.
- Search Console currently visible in Chrome is still `https://moonn.ru/`, not `мунн.рф`.
- Public source/canonical metadata may still point to `moonn.ru`; changing public canonical URLs in Tilda is a separate live-publication action and should not be hidden inside analytics setup.
