# Moonn Five-Page SEO Change Ledger — 2026-05-21

Append-only ledger for measuring SEO/AEO changes against GSC, Yandex.Metrika and Yandex Webmaster.

## 2026-05-21 Live Publication

- SEO title/description/canonical saved in Tilda for all five scoped pages through authenticated Alexander/Rublev Chrome.
- AEO/FAQ/schema runtime layer saved in each page-specific Tilda HEAD editor through `aceeditor_head`.
- Only the five scoped pages were published.
- Live audit after publication:
  - all five URLs return `200`;
  - all five URLs are in sitemap;
  - none of the five URLs is robots-blocked;
  - rendered H1 count is `1` on all five pages;
  - rendered AEO answer block count is `1` on all five pages;
  - rendered placeholders are absent on all five pages.
- Remaining source-level cleanup:
  - raw HTML still reports missing image alt on all five pages;
  - raw HTML still reports old/multiple/missing H1 on camp, consultation and reviews, although rendered H1 is corrected;
  - raw HTML still contains placeholder strings on camp/gallery, although rendered placeholders are hidden.
- Reindex action remains pending: submit only the five URLs from `docs/moonn-five-page-reindex-urls-2026-05-21.txt` after final source-cleanup decision, not all 83 URLs.

## Review Windows

- T0: baseline before live edits.
- T+3: technical/live verification.
- T+14: early impressions/CTR movement.
- T+28: CTR/click assessment.
- T+56: scale or pivot decision.

## Entries

### https://moonn.ru/podrostkovyy-lager-psihologiya

- Tilda page id: `140348786`
- Baseline date: `2026-05-21`
- Hypothesis: Сужение страницы под родителя подростка и запросы про психологический лагерь даст больше релевантных показов и кликов, чем общий блок с программой.
- Target queries: `подростковый психологический лагерь Москва`, `лагерь для подростков психология`, `тревожность и общение подростков`, `психологический лагерь для подростков`
- Changes planned: `seo_title_description_canonical`, `single_h1`, `faq_aeo_block`, `page_specific_schema`, `metrika_click_goals`
- Changes applied: `seo_title_description_canonical_saved_in_tilda`, `five_page_aeo_faq_schema_layer_saved_in_page_head`, `scoped_tilda_page_publish_completed`, `rendered_browser_audit_completed`
- Reindex date: pending
- T+3: early live check passed, source-level cleanup remains
- T+14/T+28/T+56: pending

### https://moonn.ru/kartiny-tatiany-munn

- Tilda page id: `140864526`
- Baseline date: `2026-05-21`
- Hypothesis: Галерея лучше работает как доверительный и продуктовый слой, если отделить арт-интент от общей психологии и добавить понятный CTA.
- Target queries: `картины Татьяны Мунн`, `галерея Татьяны Мунн`, `авторские картины психолога`, `энергетические картины Татьяна Мунн`
- Changes planned: `seo_title_description_canonical`, `single_h1`, `faq_aeo_block`, `page_specific_schema`, `metrika_click_goals`
- Changes applied: `seo_title_description_canonical_saved_in_tilda`, `five_page_aeo_faq_schema_layer_saved_in_page_head`, `scoped_tilda_page_publish_completed`, `rendered_browser_audit_completed`
- Reindex date: pending
- T+3: early live check passed, source-level cleanup remains
- T+14/T+28/T+56: pending

### https://moonn.ru/psypodgotovka1

- Tilda page id: `62652841`
- Baseline date: `2026-05-21`
- Hypothesis: Уточнение под ОГЭ/ЕГЭ и тревогу перед экзаменами увеличит CTR по низко- и среднечастотным запросам.
- Target queries: `подготовка к ЕГЭ без паники`, `стресс перед экзаменом`, `психологическая подготовка к ОГЭ`, `как справиться с тревогой перед экзаменом`
- Changes planned: `seo_title_description_canonical`, `single_h1`, `faq_aeo_block`, `page_specific_schema`, `metrika_click_goals`
- Changes applied: `seo_title_description_canonical_saved_in_tilda`, `five_page_aeo_faq_schema_layer_saved_in_page_head`, `scoped_tilda_page_publish_completed`, `rendered_browser_audit_completed`
- Reindex date: pending
- T+3: early live check passed, source-level cleanup remains
- T+14/T+28/T+56: pending

### https://moonn.ru/psiholog-konsultacii-moskva

- Tilda page id: `135430346`
- Baseline date: `2026-05-21`
- Hypothesis: Разделение интентов взрослые/подростки/онлайн/Москва и один H1 должны улучшить релевантность коммерческих запросов.
- Target queries: `психолог подростку`, `психолог онлайн`, `психолог в Москве`, `психолог МГУ`, `консультация психолога Татьяна Мунн`
- Changes planned: `seo_title_description_canonical`, `single_h1`, `faq_aeo_block`, `page_specific_schema`, `metrika_click_goals`
- Changes applied: `seo_title_description_canonical_saved_in_tilda`, `five_page_aeo_faq_schema_layer_saved_in_page_head`, `scoped_tilda_page_publish_completed`, `rendered_browser_audit_completed`
- Reindex date: pending
- T+3: early live check passed, source-level cleanup remains
- T+14/T+28/T+56: pending

### https://moonn.ru/otzivi

- Tilda page id: `81167556`
- Baseline date: `2026-05-21`
- Hypothesis: Страница отзывов должна поднимать доверие и переходы к записи, а не пытаться конкурировать как общая SEO-статья.
- Target queries: `Татьяна Мунн отзывы`, `психолог Татьяна Мунн отзывы`, `Татьяна Мунн Яндекс Услуги`, `отзывы о психологе Татьяне Мунн`
- Changes planned: `seo_title_description_canonical`, `single_h1`, `faq_aeo_block`, `page_specific_schema`, `metrika_click_goals`
- Changes applied: `seo_title_description_canonical_saved_in_tilda`, `five_page_aeo_faq_schema_layer_saved_in_page_head`, `scoped_tilda_page_publish_completed`, `rendered_browser_audit_completed`
- Reindex date: pending
- T+3: early live check passed, source-level cleanup remains
- T+14/T+28/T+56: pending

## 2026-06-14 Live Recheck

- Current source report: `docs/moonn-seo-growth-check-2026-06-14.md`
- Live `мунн.рф` state is still technically healthy:
  - all 5 scoped URLs return `200`;
  - all 5 are present in sitemap;
  - none are blocked by `robots.txt`;
  - rendered H1 count is still `1` on all 5 URLs.
- Main blockers did not clear:
  - camp page `/podrostkovyy-lager-psihologiya` still renders answer block `0`;
  - gallery, exam prep, consultations and reviews still expose `canonical_mismatch` to legacy `https://moonn.ru/...`;
  - source cleanup debt remains: gallery placeholders, missing image `alt`, and raw H1 anomalies.
- Cabinet lane regressed:
  - GSC direct open now fails for both `sc-domain:xn--l1acaw.xn--p1ai` and legacy `https://moonn.ru/`;
  - Yandex.Webmaster direct route for `https://xn--l1acaw.xn--p1ai:443` opened `404`;
  - blocker wording stays canonical: `новая property не подтверждена, traffic migration не доказан`.
