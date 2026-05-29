# Centia amoCRM Import Plan - 2026-05-29

## Scope

- Project: Centia studio, Maryina Roshcha.
- Branch: `codex/studia`.
- amoCRM account: `rublevalexandermsu.amocrm.ru`.
- Browser rule: amoCRM is opened only through Google Chrome profile Alexander / Rublev.
- Source sheet: `2605_Лагерь_ЛИДЫ`, sheet `Теплые контакты`.

## Verified Source Structure

- Contact rows found: 29.
- Sections found: hot camp leads, parents with teenagers from consultations, previous camp contacts.
- Source columns used:
  - `Имя родителя`
  - `телефон`
  - `Подросток`
  - `комментарий`
  - optional loyalty/source marks from adjacent rows

No raw contact names, phones, child details or notes are stored in this repository file.

## API Status

- Official amoCRM docs confirm API access is configured through an amoMarket integration.
- Integration path found in the live account: `amoМаркет` -> top-right menu near `WEB HOOKS` -> `Создать интеграцию`.
- External integration form was opened and filled with non-secret metadata.
- OAuth secrets were not copied into chat or repository.
- Current blocker: GUI save did not complete during this pass; likely validation remains in the integration form. Continue from the open amoCRM tab before attempting import.

## Recommended Pipeline

Pipeline name: `Касдев лагерь / Центия`.

Statuses:

1. `Новый тёплый контакт`
2. `Первичное касание`
3. `Ответил / есть контакт`
4. `Zoom назначен`
5. `Zoom проведён`
6. `Подарок видео отправлен`
7. `Обсуждаем участие`
8. `Бронь / предоплата`
9. System win: `Успешно реализовано`
10. System loss with reasons: `Не актуально`, `Не отвечает`, `Не подходит по возрасту`, `Отложить`, `Нужен другой продукт`

## Field Mapping

- Contact name: parent name.
- Phone: normalized Russian phone from the sheet.
- Lead name: `Касдев лагерь: {parent} / {child-or-teen-summary}`.
- Lead source: `Google Sheet 2605_Лагерь_ЛИДЫ`.
- Tags:
  - `centia`
  - `warm-leads-2605`
  - `camp-custdev`
  - `google-sheet-import`
  - segment tags: `hot-camp`, `parent-client`, `past-camp`, `loyal`, `referral-source`

## Custom Fields

- `Имя подростка / ребёнка` - text.
- `Возраст / класс` - text.
- `Источник лида` - select.
- `Сегмент` - select.
- `Лояльность / теплота` - select.
- `Custdev пройден` - checkbox.
- `Подарок видео отправлен` - checkbox.
- `Исходная строка Google Sheet` - text or number.

## Import Gate

Before creating or updating contacts in amoCRM:

1. Complete OAuth/private integration setup and store secrets only in a secure local credential store.
2. Export a local ignored dry-run file, not committed to Git.
3. Validate phone normalization, duplicate phones, missing names and sensitive notes.
4. Confirm whether raw sensitive comments about minors may be imported as internal amoCRM notes.
5. Create or verify the pipeline and custom fields.
6. Import a small test batch first.
7. Verify in amoCRM UI that contacts, deals, tasks and gift-video stage are correct.

## Data Protection Rule

The source sheet contains personal data and sensitive family/child context. Do not store raw contact rows, passwords, OAuth secrets, access tokens or refresh tokens in Git. Use ignored `.local.*` files only for transient dry runs and prefer Windows Credential Manager or Chrome Password Manager for secrets.
