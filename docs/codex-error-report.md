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
