# Moonn SEO Growth Check — 2026-06-03

## Scope

- Project: Moonn / Tatyana Munn site.
- Workstream: `moonn-seo-privacy-supervisor`.
- Branch: `codex/moonn-seo-audit`.
- Requested analytics period: `2026-04-29..2026-06-03`.
- Requested reindex scope remains limited to `docs/moonn-five-page-reindex-urls-2026-05-21.txt` plus sitemap only.

## Verified Facts (this run)

### Infra / live fetch

- `python scripts\moonn_five_page_seo_sprint_audit.py --packet docs/moonn-five-page-seo-packets-2026-05-21.json --rendered` wrote:
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-03.json`
  - `docs/moonn-five-page-seo-sprint-audit-2026-06-03.md`
- This host still cannot resolve `moonn.ru`:
  - Python DNS probe returned `[Errno 11001] getaddrinfo failed`.
  - PowerShell HEAD checks for `/`, `/events_tp`, `/lectures1`, `/psiholog-konsultacii-moskva`, `sitemap.xml`, `robots.txt` failed with `Этот хост неизвестен. (moonn.ru:443)`.
  - The dated five-page audit marked all scoped URLs as `dns_blocked`.
- Local repo canon is still intact:
  - `assets/moonn-five-page-seo-sprint-layer.js` exists.
  - git object `49a093e` resolves as `commit`.
  - `docs/moonn-five-page-reindex-urls-2026-05-21.txt` remains the bounded reindex scope.

### GUI-verified: Google Search Console

- Real Chrome profile `Alexander` / `rublevalexandermsu@gmail.com` is still usable for GSC GUI fallback.
- GSC property `https://moonn.ru/` is accessible.
- GSC Performance report currently shows:
  - `245` total clicks;
  - `14.6K` total impressions;
  - `1.7%` average CTR;
  - `7.4` average position;
  - freshness: `Last update: 3.5 hours ago`.
- Top visible queries in the current GSC Performance table:
  - `татьяна мунн` — `26` clicks / `38` impressions;
  - `дневник эмоций как вести` — `6` / `177`;
  - `дневник эмоций` — `5` / `792`;
  - `как вести дневник эмоций` — `3` / `610`;
  - `как правильно вести дневник эмоций` — `1` / `100`.
- GSC Overview currently shows:
  - `135` not indexed pages;
  - `40` indexed pages;
  - `22` HTTPS pages and `0` non-HTTPS;
  - `25` valid Breadcrumb enhancements and `0` invalid.

### GUI-verified: Yandex.Metrika

- Real Chrome profile `Alexander` is also usable for Yandex.Metrika GUI fallback.
- Counter `96397286` is accessible.
- Visible default dashboard slice is still weekly, not the requested full custom period:
  - period in UI: `Неделя 28 мая - 3 июн`;
  - `Просмотры` — `105`;
  - `Визиты` — `78`;
  - `Посетители` — `69`;
  - `Время на сайте` — `1 м 4 c`;
  - `Глубина просмотра` — `1,35`;
  - `Отказы` — `58,97%`.
- Visible traffic-source totals in the same weekly slice:
  - `Прямые заходы` — `66`;
  - `Переходы из поисковых систем` — `10`;
  - `Переходы по ссылкам на сайтах` — `1`;
  - `Переходы из мессенджеров` — `1`.
- Visible page/landing evidence in the same weekly slice:
  - `мунн.рф/` — `41` pageviews;
  - `мунн.рф/podrostkovyy-lager-psihologiya` — `22`;
  - multiple supervisor/test querystring URLs are now present in the visible top-page tables, including `?payment-click-audit=20260602`, `?hero-live-check=20260602-2`, `?verify=20260603-audio-marketing-qa`, `?verify=20260603-sales-sprint`.

### GUI-verified: Yandex.Webmaster

- The canonical Moonn Yandex.Webmaster route is now verified:
  - `https://webmaster.yandex.ru/site/https:moonn.ru:443/indexing/reindex/`
- The previous guessed route with `/sites/` was wrong; the working route uses `/site/`.
- The reindex page currently shows:
  - `Дневной лимит - 470 адресов для сайта`;
  - status table `Отправленные страницы`.
- Priority URL statuses visible in the reindex table:
  - `https://moonn.ru/` — `Заявка обработана`, sent `08.05.2026 9:20`, `Уже отслеживается`;
  - `https://moonn.ru/events_tp` — `Заявка обработана`, sent `08.05.2026 9:20`;
  - `https://moonn.ru/lectures1` — `Заявка обработана`, sent `08.05.2026 9:20`;
  - `https://moonn.ru/psiholog-konsultacii-moskva` — `Заявка обработана`, sent `08.05.2026 9:20`.

## Assumptions / Limits

- GSC metrics above are GUI-verified, but still from the default visible report state (`3 months`), not a strict custom slice `2026-04-29..2026-06-03`.
- Metrika remained on the default weekly dashboard slice; the requested full-period cut, search phrases and click goals were not collected in this run.
- Yandex.Webmaster route and reindex-table statuses are verified, but a full 83-URL classification export was not collected in this run.
- DNS on this host is still broken, so GUI evidence must not be conflated with live HTTP/raw HTML/rendered DOM verification.

## Blockers

- `P0` Infra/DNS: `moonn.ru` still does not resolve on this host (`[Errno 11001] getaddrinfo failed`).
- `P0` Analytics contract remains incomplete for the requested period `2026-04-29..2026-06-03`.
- `P0` GSC URL Inspection statuses for the 4 priority URLs were not collected in this run.
- `P0` Metrika top-page tables are polluted by supervisor QA querystrings, so current page-level evidence mixes organic traffic with verification traffic.
- `P1` MIIIIPS PR #11 deploy/merge verification remains blocked because the canonical repo+PR URL is still missing in this repo context.

## Not Done

- No Tilda content edits.
- No privacy/legal edits.
- No GSC or Yandex.Webmaster submissions.
- No 83-URL batch actions.
- No screenshots were saved or committed.

## Next Actions

1. Restore DNS for `moonn.ru` on this host or move the supervisor live-check lane to a resolving host.
2. In GSC GUI, switch from the default `3 months` preset to the required custom period `2026-04-29..2026-06-03` and capture pages + queries + 4 priority URL Inspection statuses only.
3. In Metrika GUI, switch from the default weekly dashboard to the required custom period and capture visits/users/pageviews, sources, landing pages, search phrases and click goals.
4. Treat the new Metrika querystring-heavy landings as a measurement-quality incident and decide whether supervisor QA URLs should be normalized, excluded or moved off public querystrings.
5. Use the now-verified Yandex.Webmaster route `/site/https:moonn.ru:443/indexing/reindex/` for future bounded checks instead of the broken `/sites/` guess.
6. Keep reindex bounded to `docs/moonn-five-page-reindex-urls-2026-05-21.txt` plus sitemap only; do not widen to the 83-URL Google URL Inspection batch.
