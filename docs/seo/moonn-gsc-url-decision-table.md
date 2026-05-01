# Moonn GSC URL Decision Table

Created: 2026-05-01  
Project: `moon-psy-site`  
Workstream: `seo-aeo-retrofit`  
Scope: decision registry before production Tilda edits.

## Boundary

No production Tilda, Google Search Console, Yandex Webmaster or Yandex Metrica settings were changed while preparing this table.

Production changes require action-time confirmation because they can affect public indexing, redirects, robots behavior and live pages.

## Current GSC State

- Indexed pages: `29`.
- Not indexed pages: `116`.
- Reason groups: `5`.
- Last visible GSC update: `2026-04-27`.

## Priority Logic

- `P0`: concrete broken user/crawler path; fix first.
- `P1`: SEO-relevant page or redirect with direct indexation value.
- `P2`: needs classification before optimization.
- `P3`: mostly monitor or low-priority duplicate/parameter handling.

## Batch 1: 404 URLs

| URL | Live status | Decision | Target | Priority | Why |
| --- | ---: | --- | --- | --- | --- |
| `https://moonn.ru/http://wa.me/+79777770303` | 404 | fix link + possible 301 | `https://wa.me/79777770303` | P0 | External WhatsApp URL is wrapped as an internal site path. |
| `https://moonn.ru/static.tildacdn.com/` | 404 | fix asset link, keep out of index | none | P0 | Tilda CDN host appears as an internal page path. |
| `https://moonn.ru/emotionalnaya-vygoranie` | 404 | 301 + strengthen target | `/vigoranie_article` or `/emotional-intelligence/knowledge-base/burnout` | P1 | Burnout has real article/knowledge-base search intent. |
| `https://moonn.ru/zaprocy` | 404 | 301 or make clean canonical page | `/page120952796.html` or `/psiholog-konsultacii-moskva` | P1 | Search-intent page exists but canonical structure is unclear. |
| `https://moonn.ru/zaprocy.html` | 404 | 301 | same as `/zaprocy` | P1 | Legacy `.html` duplicate. |
| `https://moonn.ru/bystraya-psihologiya.html` | 404 | 301 + possible clean alias | `/page120899276.html` | P1 | Matching method page exists as technical Tilda URL. |
| `https://moonn.ru/leksii.html` | 404 | 301 | `/lectures1` or `/vystupleniya-lekcii-treningi-psiholog-tatiana-moonn` | P1 | Old lecture URL should consolidate to lecture hub. |
| `https://moonn.ru/kurs-duhovnoy-psihologii.html` | 404 | 301 or noindex/retire | `/page120915666.html` or `/platnye-treningi-seminary-programmy-tatiana-moonn` | P2 | Need business decision: active product or old/test page. |
| `https://moonn.ru/podrostki.html` | 404 | 301 + strengthen target | `/uslugi_podrostki` | P1 | Teen consultation has commercial search value. |

## Batch 2: Robots Decisions

| URL | Live status | Current blocker | Decision | Target | Why |
| --- | ---: | --- | --- | --- | --- |
| `https://moonn.ru/psiholog` | 200 | `Disallow: /psiholog` | redirect if duplicate, open if unique | `/psiholog-konsultacii-moskva` | Live page is blocked; must classify as duplicate or active landing. |
| `https://moonn.ru/psiholog-moskva-online` | 200 | prefix block from `Disallow: /psiholog` | redirect if duplicate, open if unique | `/psiholog-konsultacii-moskva` | Broad robots prefix may accidentally block a useful landing page. |

## Batch 3: Strengthen Public Pages

| URL | GSC reason | Decision | Priority | Required work |
| --- | --- | --- | --- | --- |
| `/article_gadget_addiction` | Discovered, not indexed | strengthen + open | P1 | Article schema, FAQ, teen-service internal links, image alt. |
| `/article_toxic_job` | Discovered, not indexed | strengthen + open | P1 | Article schema, workplace/service links, EI links. |
| `/baza-znaniy-emocionalnyy-intellekt-psihologiya` | Discovered, not indexed | strengthen hub | P1 | Hub metadata, ItemList, links to EI articles and knowledge base. |
| `/emotional-intelligence/articles` | Crawled, not indexed | strengthen hub | P1 | Unique hub intro, ItemList schema, links from EI hub. |
| `/semeyniy_psiholog` | Crawled, not indexed | strengthen or consolidate | P1 | Decide duplicate vs service page, then metadata/schema/links. |

## Batch 4: Keep Out Or Classify

| URL | GSC reason | Proposed decision | Why |
| --- | --- | --- | --- |
| `/cta` | Discovered, not indexed | noindex/remove unless real landing | Looks like a utility/test page. |
| `/aromatherapy` | Discovered, not indexed | classify as core vs non-core | May dilute psychology/EI topical authority if unrelated. |
| `/water` | Crawled, not indexed | classify as core vs non-core | Crawled but ignored; likely low topical fit unless rewritten. |
| `/tpost/...` and `amp=true` variants | Crawled, not indexed | canonical/redirect/monitor | Do not optimize duplicates directly. |

## Immediate Execution Plan

1. Build the Tilda redirect/link-fix map for the nine 404 rows.
2. In staging, inspect the candidate targets for content quality and duplication.
3. Before production, ask for confirmation to edit redirects/links in Tilda.
4. After publishing production fixes, run live checks.
5. Only then validate the 404 group in GSC.

