# Camp page update checklist — 2026-05-31

Контур: Moonn Tilda camp page content/pricing update.
Ветка: `codex/moonn-camp-page-update`.
Страница: `https://moonn.ru/podrostkovyy-lager-psihologiya`.
Tilda page id: `140348786`.

## Scope

- Обновить публичный оффер страницы лагеря без изменения банковского кабинета, юридических текстов, персональных данных и чужих доменов.
- Обновить HTML-пакет, PDF и постер.
- Опубликовать через Tilda/Rublev Chrome только после локальной проверки.
- Проверить live HTML/rendered page и Tilda cart.

## Required changes

- [x] Название: оставить явный психологический смысл, но сделать его живее для подростков.
- [x] Цена: убрать `30 000`; заменить на раннюю оплату `40 000 ₽` и стандартную `50 000 ₽` с зачёркиванием старшей цены.
- [x] Проверить, что в HTML, постере, PDF и schema нет старых `30 000` / `30000`.
- [x] Группа: заменить `3-5` / `3 - 5` на `10-12`.
- [x] Фото блока “Татьяна Мунн ведёт программу лично”: заменить чёрно-белый портрет на цветное изображение.
- [x] ИИ: добавить раннюю заметную плашку и оставить полноценный блок нейросетей.
- [x] Добавить блок “первые шаги психолога” для подростков, которым интересна профессия психолога.
- [x] Добавить блок питания: один приём пищи в день программы, перерывы и вода.
- [x] Проверить/уточнить день 10:00-18:00, обед и перерывы.
- [x] Добавить календарь смен: июль, конец августа, сентябрьская предзапись/weekend, октябрьские каникулы, профориентационная смена.
- [x] Добавить лояльность: рекомендация знакомым и бонус `5 000 ₽` после фактической оплаты участника.
- [x] Добавить несколько CTA “Оплатить/забронировать” в разных частях страницы.
- [x] Проверить cart: продукт, цена `40 000 ₽`, путь к Tilda/T-Bank.
- [x] Опубликовать обновлённый HEAD-loader через Tilda/Rublev Chrome.
- [x] Проверить live HTML/rendered page после публикации.
- [x] Обновить `docs/codex-chat-history.md` и отчёт публикации.

## Local verification

- `2026-05-31`: rendered desktop check of `tilda-page-final.html` passed:
  - old price `30 000` / `30000`: not found;
  - old group `3-5` / `3 - 5`: not found;
  - past deadline `15 мая`: not found;
  - black-and-white author image runtime refs: `0`;
  - food, calendar, loyalty, AI teaser and profession track: present;
  - payment CTA/order links: `6`;
  - cart price marker: `40000`.
- `2026-05-31`: mobile rendered check `390x844` passed: no horizontal overflow, no old price, `6` order links.
- `2026-05-31`: Tilda/Rublev Chrome publication completed for page `140348786`.
- `2026-05-31`: after reopening Tilda HEAD editor, server-side editor value contained `20260531-camp-update`, `40000`, commit `1aab5c887ee`; old `20260523-offer-visual-ai` and `30000` were absent.
- `2026-05-31`: live raw HTML on `https://мунн.рф/podrostkovyy-lager-psihologiya` returned `200`, contained `20260531-camp-update`, `40000`, commit `1aab5c887ee`, and did not contain old `30000`.
- `2026-05-31`: live rendered check passed: H1 `Психология без скуки: уверенность, общение и ИИ`, no old `30 000`, `40 000` and `50 000` present, group `10-12`, food, calendar, loyalty and AI blocks present, no horizontal overflow.
- `2026-05-31`: live cart check passed without payment submission: Tilda cart opens with product `Психология без скуки — подростковый лагерь`, SKU `teen-camp-2026`, price `40000`, total `40000`; `30000` absent.

## Risk notes

- `15 мая` на дату работы уже прошло. Не использовать это как действующее условие ближайшей оплаты без контекста; безопаснее писать “ранняя оплата / предзапись следующей смены”.
- Даты школьных каникул у школ могут отличаться. На странице писать “предварительные даты” и “финальные даты уточняются после подтверждения календаря школы”.
- Бонус `5 000 ₽` может иметь налоговые/договорные нюансы; формулировать как программу лояльности по согласованию с организатором.
- `moonn.ru` с этой машины по-прежнему не резолвится; аварийный live-домен `мунн.рф` работает и проверен.
- Обычная UI-вставка в Tilda Ace editor может не сохраняться на сервере. Готовность для HEAD-правок считать только после повторного открытия редактора, проверки серверного значения и live HTML/rendered проверки.
