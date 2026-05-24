# Centia Operations Dashboard - 2026-05-24

## Scope

- Project: Centia studio under the Moonn ecosystem.
- Workstream branch: `codex/studia`.
- Deliverable: native Google Sheets dashboard for studio launch operations.
- Google Sheets title: `Центия — операционный дашборд студии Марьина Роща`.
- Google Sheets URL: `https://docs.google.com/spreadsheets/d/1HFoSMv6un1NpoQJGm6_fDgDA-kIBFithpti5tXM6_ms/edit`.

## Reference

- User supplied YouTube Short: `https://youtube.com/shorts/dgpCSYY6P6I`.
- YouTube oEmbed verified title: `Шаблоны в Гугл таблицах для устранения хаоса в твоей жизни`.
- YouTube oEmbed verified author/channel: `RITM` / `https://www.youtube.com/@ritm_tab`.

## Dashboard Structure

The spreadsheet contains 13 tabs:

- `00 Dashboard` - KPI summary and launch control panel.
- `01 Цели KPI` - business objectives, target metrics and status.
- `02 Воронка` - channel-to-booking funnel.
- `03 Программы` - product lineup and page links.
- `04 Расписание` - weekly schedule and weekend uses.
- `05 Выручка` - monthly revenue model with occupancy formulas and chart.
- `06 Задачи запуска` - task tracker with status and priority validation plus status chart.
- `07 Контент SEO` - 12 live Tilda pages with titles, descriptions, aliases and URLs.
- `08 Маркетинг` - channels, offers and KPI ownership.
- `09 CRM заявки` - lead intake template.
- `10 Пространство` - room, furniture, formats and procurement control.
- `11 Инциденты` - incidents, root causes, fixes and follow-up rules.
- `12 Источники` - provenance for YouTube, context JSON, Tilda manifest and live site.

## Verified

- Local workbook generated: `output/centia-studio-dashboard-2026-05-24.xlsx`.
- Imported to Google Drive as native Google Sheets:
  - `converted: true`;
  - MIME type: `application/vnd.google-apps.spreadsheet`;
  - spreadsheet id: `1HFoSMv6un1NpoQJGm6_fDgDA-kIBFithpti5tXM6_ms`.
- Google Sheets metadata confirmed all 13 expected tabs.
- `00 Dashboard!A1:C9` read back successfully:
  - live pages: `12`;
  - planned group occupancy: `70%`;
  - planned monthly revenue: `444,000 ₽`;
  - blockers: `0`.

## Follow-Up Rule

For Centia operations, treat the Google Sheet as the working dashboard, but keep canonical publication facts in the repo manifest/report first. If a page, price, program, schedule or booking flow changes, update the source artifact and then refresh the dashboard tab that depends on it.
