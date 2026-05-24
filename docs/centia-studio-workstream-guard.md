# Centia Studio Workstream Guard

Status: active
Created: 2026-05-24
Repository: `rublevalexandermsu-design/moonn-psy-pages`
Canonical branch: `codex/studia`

## Scope

This branch is reserved for the Centia studio website and directly related launch artifacts:

- Centia static site source under `centia/`
- Centia build and SEO tooling
- Centia image manifest, image sitemap, schema.org, canonical URLs, `llms.txt`
- Centia launch, domain, compliance and verification docs

## Out Of Scope

Do not use this branch for unrelated Moonn/Tilda SEO audits, Timepad payment work, teen camp edits, ANO institute pages, grant workflows, editorial workflows, runtime repairs or generic chat-history backups.

If another task appears while this branch is active, route it to its own existing branch or create a new `codex/` branch.

## Domain Rule

Current low-risk build path: `/centia/` under the existing Pages deployment domain.

Recommended production target after approval: `centia.moonn.ru`.

Do not change `CNAME`, DNS, Tilda production pages, payment settings, legal pages, personal-data flows or public publication state from this branch without explicit approval.

## Verification Gate

Before reporting the site as launch-ready:

- `python build_site.py --output dist` succeeds
- `dist/centia/index.html` and all 11 subpages exist
- sitemap includes all Centia pages
- `dist/centia/centia-image-sitemap.xml` exists
- no public page contains internal placeholders or local paths
- local browser/Playwright visual check passes on desktop and mobile
- legal/publication gate is updated for personal data, age-sensitive content and advertising claims
