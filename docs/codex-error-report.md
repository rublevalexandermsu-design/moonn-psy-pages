# Codex Error Report

## 2026-06-14 12:50 +03:00 — Moonn SEO automations reused legacy domain from source files

### Symptom

- The user saw SEO automation opening or checking old `moonn.ru` / Google Search Console property while the live site is `мунн.рф`.
- A first rerun still produced `dns_blocked` results for `moonn.ru` even after automation prompt text was corrected.

### Root Cause

- The automation prompt was not the only source of truth.
- The five-page SEO packet and audit scripts still contained `moonn.ru` as executable defaults or generated packet URLs.
- Privacy audit also used legacy `moonn.ru` as its default base.

### Fix Implemented

- In branch `codex/moonn-seo-supervisor-20260614`, default audit base URLs now point to `https://xn--l1acaw.xn--p1ai`.
- The five-page SEO packet generator now emits new-domain URLs.
- SEO and privacy audits were rerun against the new domain and produced new reports.

### Verification

- SEO audit report base URL: `https://xn--l1acaw.xn--p1ai`.
- DNS check: true.
- Five-page SEO audit: 5/5 pages returned HTTP 200, in sitemap, not robots-blocked.
- Privacy audit: 83 scoped URLs returned HTTP 200; policy endpoints still returned 404.

### Follow-up Rule

- When changing a scheduled domain migration task, verify three layers: automation prompt, script defaults, and input packet/manifest. Do not treat prompt update alone as complete.

## 2026-06-14 13:10 +03:00 — SEO audit mixed raw Tilda debt with rendered-page status

### Symptom

- After live Tilda fixes, the audit still listed `raw_h1_count_not_one`, `placeholder_text`, and `images_missing_alt`.
- This could be misread as if the public pages were still visibly broken.

### Root Cause

- The audit already checked rendered H1 and answer block, but image alt status was measured only in raw Tilda HTML.
- Tilda source HTML can differ from the final browser DOM after the shared SEO head layer runs.

### Fix Implemented

- Added rendered image count and rendered missing-alt count to `scripts/moonn_five_page_seo_sprint_audit.py`.
- Published the shared head layer with `ensureImageAlts()` to the five scoped Tilda pages.
- Reran the audit against `https://xn--l1acaw.xn--p1ai`.

### Verification

- 5/5 scoped pages return HTTP `200`, are in sitemap, and are not robots-blocked.
- 5/5 pages have expected live-domain title, description, and canonical.
- 5/5 rendered pages have one H1 and one answer block.
- 5/5 rendered pages have `0` rendered images missing `alt`.
- Rendered placeholder hits are empty on all five pages.

### Follow-up Rule

- SEO reports must label raw-source debt separately from rendered browser defects. Raw Tilda debt is still worth cleaning, but it must not be reported as a live rendered-page failure after browser verification passes.

## 2026-06-14 13:35 +03:00 — Privacy audit overcounted raw Tilda form signals

### Symptom

- The privacy audit reported form signals on all `83` scoped URLs and `forms_without_detected_checkbox` on `78` pages.
- This made the site look like almost every page had a live form without a consent checkbox.

### Root Cause

- The audit counted raw Tilda HTML/script markers such as generated form infrastructure.
- It did not distinguish inactive/generated markup from actual rendered browser forms.
- The existing canonical policy page `/politic` was also not included in the policy endpoint list, while future aliases were checked and returned `404`.

### Fix Implemented

- Added rendered Playwright checks to `scripts/moonn_privacy_compliance_audit.py`.
- Added `/politic` as the current canonical live policy endpoint.
- Fixed `/politic` title, description and canonical through Tilda UI.
- Published a narrow `/politic` runtime patch that removes legacy `https://moonn.ru/politic` from rendered policy text without changing operator/legal terms.

### Verification

- `/politic` returns HTTP `200`.
- Rendered `/politic` has title `Политика обработки персональных данных | Татьяна Мунн`.
- Rendered `/politic` canonical is `https://xn--l1acaw.xn--p1ai/politic`.
- Rendered `/politic` has patch marker `2026-06-14`.
- Full rendered audit checked `83` scoped URLs.
- Rendered pages with forms: `15`.
- Rendered form pages without checkbox: `0`.

### Follow-up Rule

- Privacy/form compliance must separate raw-source findings from rendered-browser gate results. Do not report generated Tilda form infrastructure as live missing-consent failure unless a rendered form page lacks a checkbox.

## 2026-06-14 19:15 +03:00 — SEO automations ran from stale checkout and audited legacy `moonn.ru`

### Symptom

- The 2026-06-14 SEO and privacy automation reports showed DNS failures for `https://moonn.ru/...`.
- This looked like the site/search contour was broken, even though the current live domain is `https://мунн.рф/` (`https://xn--l1acaw.xn--p1ai/`).

### Root Cause

- The automation prompts had already been updated to use `мунн.рф` and to forbid `moon.ru` / legacy `moonn.ru`.
- The actual automation `cwds` still pointed to `C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site`.
- That checkout was on `codex/moonn-camp-page-update` and still had older audit scripts with hardcoded `moonn.ru`.
- Codex previously treated the prompt as sufficient and did not verify execution cwd/branch/script version before relying on the scheduled reports.

### Fix Implemented

- Updated both Codex automation TOML files:
  - `moonn-five-page-seo-aeo-supervisor`
  - `moonn-seo-privacy-supervisor`
- Both now run from `C:\пайто н тесты\Ано_институт_глаболизация\moon-psy-site-supervisor-20260614`, where the scripts default to `https://xn--l1acaw.xn--p1ai` and support explicit `--base-url`.

### Verification

- Both automations remain `ACTIVE`.
- Both automations remain scheduled for 09:00 Moscow time daily.
- Non-rendered five-page autocheck against `https://xn--l1acaw.xn--p1ai` returned:
  - DNS resolve: `True`.
  - 5/5 priority URLs HTTP `200`.
  - 5/5 priority URLs in sitemap.
  - 5/5 priority URLs not blocked by robots.
- Browser rendered audit timed out and is not counted as verified.

### Follow-up Rule

- For scheduled Codex automations, always verify three layers before trusting the result: prompt domain, execution cwd/branch, and script/config domain defaults. A correct prompt does not protect against a stale checkout.

## 2026-06-14 14:20 +03:00 — AEO answer block appeared above the teen camp hero

### Symptom

- The user saw a new visible block titled `Коротко по запросу` above the main teen camp hero.
- The block was useful for SEO/AEO, but visually damaged the landing page first screen.

### Root Cause

- The shared five-page SEO layer inserted `#moonn-five-page-answer-block` near the top of `main`.
- The teen camp page is a custom external-HTML Tilda page, and live head code contained multiple old loader URLs. Updating only one occurrence could leave old loaders able to remount stale content.

### Fix Implemented

- Moved the answer block into the native teen camp HTML body after the hero and upper facts section.
- Added a native-placement guard so the SEO layer does not move this block back up.
- Replaced all live teen camp loader URLs in Tilda head code with commit `b373c90`.
- Removed the separate problematic five-page SEO include from the teen camp page head.

### Verification

- Raw live HTML has `8` references to the current teen camp external HTML commit `b373c90`.
- Raw live HTML has `0` references to old teen camp commit `560518a98698cf6019cc07cb8a4b98b52d9daf6a`.
- Rendered mounted version is `20260614-answer-block-middle`.
- Rendered `#moonn-five-page-answer-block` exists at child index `2` inside `main`.
- The first visible text slice no longer contains `Коротко по запросу`.

### Follow-up Rule

- Before declaring Tilda runtime placement fixed, verify rendered DOM position and scan raw HTML for duplicate old loader URLs. A single updated loader is not enough when repeated snippets exist.

## 2026-06-16 14:05 +03:00 — Old camp-page AEO failure disappeared, but 4 rendered checks timed out

### Symptom

- The historical camp-page rendered failure `answer block = 0` was no longer reproduced on `https://xn--l1acaw.xn--p1ai/podrostkovyy-lager-psihologiya`.
- At the same time, 4 other scoped pages failed the rendered audit with `Page.goto timeout 45000ms exceeded`.
- A superficial comparison with the 2026-06-14 run could falsely suggest that the whole rendered lane improved or fully passed.

### Root Cause

- The supervisor had been tracking one stable symptom and risked overfitting to it.
- Today's rendered lane changed failure mode: one page recovered, but the rest no longer completed within the Playwright timeout budget.
- Without explicit incident logging, the automation could collapse these different outcomes into a misleading “camp fixed, rendered okay” summary.

### Fix Implemented

- Recorded a new dated rendered audit for 2026-06-16 instead of overwriting older evidence.
- Updated the daily growth report and backlog to separate:
  - resolved old camp-page symptom;
  - new four-page rendered timeout incident;
  - still-open new-domain property blocker.

### Verification

- Camp page rendered result is `ok` with `answerBlockCountRendered = 1`.
- Gallery, exam prep, consultations and reviews each return rendered status `error` with `Page.goto timeout 45000ms exceeded`.
- Raw HTTP/sitemap/robots/title/description/canonical checks still pass on all 5 scoped URLs.

### Follow-up Rule

- When a recurring SEO/AEO defect disappears, do not upgrade the whole rendered lane automatically. Compare page-by-page rendered statuses and record any change in failure class as a new incident.
