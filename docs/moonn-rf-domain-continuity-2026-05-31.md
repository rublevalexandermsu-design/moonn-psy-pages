# Moonn domain continuity: `мунн.рф`

Дата проверки: 2026-05-31 09:10 MSK.
Контур: Moonn domain continuity / temporary domain.
Ветка: `codex/moonn-rf-domain-continuity`.

## Цель

Временно подключить новый домен `мунн.рф` к сайту Tilda проекта Moonn, чтобы сайт не исчезал из интернета, пока решается юридическая перерегистрация основного домена `moonn.ru`.

## Проверенные факты

- Новый домен: `мунн.рф`.
- Punycode:
  - `мунн.рф` -> `xn--l1acaw.xn--p1ai`;
  - `www.мунн.рф` -> `www.xn--l1acaw.xn--p1ai`.
- REG.RU открыт в Chrome профиля Alexander/Rublev, аккаунт: `tatiana201777@mail.ru`.
- Домен `мунн.рф` в REG.RU действует до `30.05.2027`.
- NS домена: `ns1.reg.ru`, `ns2.reg.ru`.
- Tilda project settings accepted `мунн.рф` as the custom domain for project `8326812`.
- Tilda requires A records for both root and `www` to point to `176.57.67.109`.

## Выполнено

1. In Tilda project settings, custom domain was changed from `moonn.ru` to `мунн.рф`.
2. REG.RU DNS zone UI was changed and reloaded; after reload the cabinet shows:
   - `A @ -> 176.57.67.109`;
   - `A www -> 176.57.67.109`.
3. No paid REG.RU services were purchased.
4. No legal text, payment settings, personal data, or unrelated domain (`miiiips.ru`) settings were changed.

## Текущий блокер

REG.RU cabinet shows the new DNS values, but direct DNS checks still return the old parking/REG.RU IP:

```text
xn--l1acaw.xn--p1ai      A 95.163.244.138
www.xn--l1acaw.xn--p1ai  A 95.163.244.138
```

Checked against:

- `ns1.reg.ru` / `194.58.117.17`;
- `ns2.reg.ru` / `194.58.117.14`;
- local resolver.

Live HTTP checks are also not green yet:

```text
curl -I http://xn--l1acaw.xn--p1ai/                         -> HTTP 400
curl -I https://xn--l1acaw.xn--p1ai/                        -> HTTP 400
curl -I --resolve xn--l1acaw.xn--p1ai:443:176.57.67.109 ... -> HTTP 400
```

This means the migration is not yet complete: cabinet state and authoritative/public DNS state are not aligned yet.

## Incident rule

Symptom: REG.RU UI displayed updated A records, but DNS still resolved to the previous IP.

Likely root cause: DNS zone publication/cache delay or a separate REG.RU save/publish layer after UI editing.

Follow-up rule: do not report domain migration complete from registrar UI alone. Completion requires all of:

1. REG.RU cabinet shows `A @` and `A www` pointing to Tilda IP.
2. DNS checks resolve root and `www` to `176.57.67.109`.
3. Tilda domain check accepts the domain.
4. Browser/curl live check returns the Moonn site, not REG.RU parking or HTTP 400.

## Next check

Recheck DNS in 30-60 minutes. If DNS still points to `95.163.244.138`, reopen REG.RU DNS zone and look for a separate publish/save action or contact REG.RU support with the exact mismatch.
