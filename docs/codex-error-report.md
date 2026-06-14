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
