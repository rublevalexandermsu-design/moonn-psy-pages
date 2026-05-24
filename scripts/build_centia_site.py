from __future__ import annotations

import base64
import hashlib
import html
import json
import re
import shutil
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "centia" / "source"
SEO_IMAGES = ROOT / "centia" / "seo-images"
CONTEXT_PATH = ROOT / "centia" / "centia_chat_context_for_codex.json"
OUTPUT_DIRNAME = "centia"

DATA_IMAGE_RE = re.compile(r'src="data:image/(?P<kind>png|jpeg|jpg|webp);base64,(?P<data>[^"]+)"')
LOCAL_IMAGE_RE = re.compile(r'<img[^>]+src="(?P<src>assets/[^"]+)"', re.IGNORECASE)
TITLE_RE = re.compile(r"<title>.*?</title>", re.IGNORECASE | re.DOTALL)
DESCRIPTION_RE = re.compile(r'<meta\s+name="description"\s+content="[^"]*"\s*/?>', re.IGNORECASE)


PAGE_ORDER = [
    "index.html",
    "deti-7-10.html",
    "podrostki-11-13.html",
    "podrostki-14-16.html",
    "podrostki-15-17.html",
    "roditelyam.html",
    "vzroslym.html",
    "prostranstvo.html",
    "raspisanie.html",
    "oplata.html",
    "o-tatyane.html",
    "contacts.html",
]

PAGE_META: dict[str, dict[str, str]] = {
    "index.html": {
        "title": "Центия — психологические группы для детей и взрослых в Марьиной Роще",
        "description": "Студия Центия в Москве рядом с Марьиной Рощей: психологические группы для детей, подростков, родителей и взрослых, расписание, бронь и контакты.",
        "image": "01_space_design/02-centia-studio-main-interior-green-seating.webp",
    },
    "deti-7-10.html": {
        "title": "Эмоции и общение для детей 7-10 лет | Центия",
        "description": "Мягкая психологическая группа для детей 7-10 лет: эмоции, дружба, общение, просьбы, договоренности и уверенность в группе.",
        "image": "02_program_scenes/05-scene-children-emotions-group.webp",
    },
    "podrostki-11-13.html": {
        "title": "Общение и уверенность для подростков 11-13 лет | Центия",
        "description": "Подростковая группа 11-13 лет в студии Центия: общение, уверенность, дружба, обиды, конфликты и страх оценки.",
        "image": "02_program_scenes/08-scene-teens-communication-lounge.webp",
    },
    "podrostki-14-16.html": {
        "title": "Самооценка, тревога и общение для подростков 14-16 лет | Центия",
        "description": "Главная подростковая группа Центии для 14-16 лет: самооценка, тревога, общение, конфликты, одиночество и мягкая практика контакта.",
        "image": "02_program_scenes/03-scene-teen-workshop-bright-space.webp",
    },
    "podrostki-15-17.html": {
        "title": "Стресс, экзамены и выбор будущего 15-17 лет | Центия",
        "description": "Группа для подростков 15-17 лет: стресс перед экзаменами, тревога, прокрастинация, сильные стороны и выбор будущего.",
        "image": "02_program_scenes/04-scene-stress-exams-workshop.webp",
    },
    "roditelyam.html": {
        "title": "Родительский клуб в Марьиной Роще | Центия",
        "description": "Родительский клуб Центии: встречи для родителей детей и подростков о контакте, границах, конфликтах и разговоре без давления.",
        "image": "02_program_scenes/02-scene-parent-club-workshop.webp",
    },
    "vzroslym.html": {
        "title": "Стресс, выгорание и саморегуляция для взрослых | Центия",
        "description": "Взрослая психологическая группа Центии: стресс, выгорание, тревога, усталость, раздражение и восстановление без давления.",
        "image": "02_program_scenes/07-scene-calm-adult-wellness-group.webp",
    },
    "prostranstvo.html": {
        "title": "Пространство студии Центия у Марьиной Рощи",
        "description": "Светлая трансформируемая студия 30 м² у Марьиной Рощи: круг на пуфах, лекции, тренинги, мягкие практики и группы.",
        "image": "01_space_design/03-centia-studio-workshop-space-natural-light.webp",
    },
    "raspisanie.html": {
        "title": "Расписание групп Центии на сентябрь и октябрь",
        "description": "Расписание психологических групп Центии: дети 7-10, подростки 11-13, 14-16, 15-17, родительский клуб и взрослая группа.",
        "image": "02_program_scenes/01-scene-group-discussion-circle-format.webp",
    },
    "oplata.html": {
        "title": "Бронь и стоимость занятий | Центия",
        "description": "Стоимость пробных встреч, разовых занятий, абонементов и брони места в психологических группах студии Центия.",
        "image": "01_space_design/05-centia-studio-flex-room-plants-seating.webp",
    },
    "o-tatyane.html": {
        "title": "Татьяна Мунн — психолог МГУ, основатель студии Центия",
        "description": "Татьяна Мунн: психолог МГУ, эксперт по психологии эмоций и состояний, автор метода «Быстрая психология» и основатель Центии.",
        "image": "02_program_scenes/12-scene-warm-conversation-modern-interior.webp",
    },
    "contacts.html": {
        "title": "Контакты студии Центия у Марьиной Рощи",
        "description": "Контакты студии Центия: Москва, рядом с парком Фестивальный и метро Марьина Роща, запись на группы и пробные встречи.",
        "image": "01_space_design/04-centia-studio-wellness-space-natural-light.webp",
    },
}

CARD_IMAGE_BY_LABEL: dict[str, str] = {
    "часто обижается или злится": "03_cards_children/01-children-card-emotion-cards.webp",
    "сложно говорить о чувствах": "03_cards_children/02-children-card-drawing-feelings.webp",
    "трудно договариваться в игре и классе": "03_cards_children/03-children-card-communication-games.webp",
    "боится ошибки и оценки": "04_cards_teens_adults/02-card-fear-of-judgment.webp",
    "хочется больше уверенности": "03_cards_children/08-children-card-soft-group-communication.webp",
    "карточки эмоций": "03_cards_children/01-children-card-emotion-cards.webp",
    "рисование состояний": "03_cards_children/02-children-card-drawing-feelings.webp",
    "игры на общение": "03_cards_children/03-children-card-communication-games.webp",
    "мини-сценки про дружбу": "03_cards_children/04-children-card-friendship-mini-scenes.webp",
    "больше слов вместо крика или молчания": "03_cards_children/05-children-card-more-words-instead-of-crying.webp",
    "понятнее, как просить и договариваться": "03_cards_children/06-children-card-asking-and-agreeing.webp",
    "опыт, что его слышат": "03_cards_children/07-children-card-feeling-heard.webp",
    "мягкая тренировка общения в группе": "03_cards_children/08-children-card-soft-group-communication.webp",
    "подросток стесняется": "04_cards_teens_adults/02-card-fear-of-judgment.webp",
    "трудно знакомиться": "04_cards_teens_adults/03-card-communication-difficulties.webp",
    "часто переживает из-за мнения других": "04_cards_teens_adults/02-card-fear-of-judgment.webp",
    "сложно отстаивать себя спокойно": "04_cards_teens_adults/03-card-communication-difficulties.webp",
    "есть конфликты или одиночество": "04_cards_teens_adults/06-card-feeling-lonely.webp",
    "разбор школьных ситуаций": "04_cards_teens_adults/03-card-communication-difficulties.webp",
    "игры на коммуникацию": "03_cards_children/03-children-card-communication-games.webp",
    "работа с границами": "04_cards_teens_adults/03-card-communication-difficulties.webp",
    "разговор о дружбе и конфликтах": "04_cards_teens_adults/05-card-conflicts.webp",
    "больше спокойствия в общении": "04_cards_teens_adults/03-card-communication-difficulties.webp",
    "меньше страха проявляться": "04_cards_teens_adults/02-card-fear-of-judgment.webp",
    "тревога и напряжение": "04_cards_teens_adults/01-card-anxiety-and-tension.webp",
    "страх оценки": "04_cards_teens_adults/02-card-fear-of-judgment.webp",
    "сложности в общении": "04_cards_teens_adults/03-card-communication-difficulties.webp",
    "низкая самооценка": "04_cards_teens_adults/04-card-low-self-esteem.webp",
    "конфликты": "04_cards_teens_adults/05-card-conflicts.webp",
    "ощущение одиночества": "04_cards_teens_adults/06-card-feeling-lonely.webp",
    "работаем с тревожными мыслями": "04_cards_teens_adults/01-card-anxiety-and-tension.webp",
    "тренируем спокойную коммуникацию": "04_cards_teens_adults/03-card-communication-difficulties.webp",
    "говорим о границах и образе себя": "04_cards_teens_adults/04-card-low-self-esteem.webp",
    "больше понимания себя": "04_cards_teens_adults/04-card-low-self-esteem.webp",
    "новые способы общения без агрессии и ухода": "04_cards_teens_adults/05-card-conflicts.webp",
    "впереди экзамены": "04_cards_teens_adults/07-card-exams-ahead.webp",
    "много тревоги": "04_cards_teens_adults/08-card-lots-of-anxiety.webp",
    "сложно выбрать направление": "04_cards_teens_adults/09-card-hard-to-choose-direction.webp",
    "есть прокрастинация": "04_cards_teens_adults/10-card-procrastination.webp",
    "давление родителей и школы": "04_cards_teens_adults/08-card-lots-of-anxiety.webp",
    "подросток говорит «я не знаю»": "04_cards_teens_adults/09-card-hard-to-choose-direction.webp",
    "стресс и саморегуляция": "04_cards_teens_adults/01-card-anxiety-and-tension.webp",
    "страх ошибки": "04_cards_teens_adults/02-card-fear-of-judgment.webp",
    "план подготовки": "04_cards_teens_adults/07-card-exams-ahead.webp",
    "спокойнее взгляд на экзамены": "04_cards_teens_adults/07-card-exams-ahead.webp",
    "первый реалистичный план": "04_cards_teens_adults/09-card-hard-to-choose-direction.webp",
    "подросток не слушает": "04_cards_teens_adults/03-card-communication-difficulties.webp",
    "много конфликтов": "04_cards_teens_adults/05-card-conflicts.webp",
    "гаджеты и границы": "04_cards_teens_adults/03-card-communication-difficulties.webp",
    "тревога за учёбу": "04_cards_teens_adults/08-card-lots-of-anxiety.webp",
    "ребёнок закрывается": "04_cards_teens_adults/06-card-feeling-lonely.webp",
    "родитель срывается": "04_cards_teens_adults/15-card-lots-of-irritation.webp",
    "разбор типичных ситуаций": "04_cards_teens_adults/05-card-conflicts.webp",
    "фразы, которые помогают говорить": "04_cards_teens_adults/03-card-communication-difficulties.webp",
    "больше спокойствия в разговоре": "04_cards_teens_adults/03-card-communication-difficulties.webp",
    "понятнее, где поддержка, а где давление": "04_cards_teens_adults/04-card-low-self-esteem.webp",
    "усталость стала фоном": "04_cards_teens_adults/11-card-fatigue-became-background.webp",
    "часто тревожно": "04_cards_teens_adults/12-card-often-anxious.webp",
    "сложно отдыхать без вины": "04_cards_teens_adults/13-card-hard-to-rest-without-guilt.webp",
    "тело в напряжении": "04_cards_teens_adults/14-card-body-in-tension.webp",
    "много раздражения": "04_cards_teens_adults/15-card-lots-of-irritation.webp",
    "хочется восстановиться, но непонятно как": "04_cards_teens_adults/16-card-want-to-recover-but-unclear-how.webp",
    "объяснения о стрессе": "04_cards_teens_adults/11-card-fatigue-became-background.webp",
    "упражнения на саморегуляцию": "04_cards_teens_adults/12-card-often-anxious.webp",
    "мягкие телесные практики": "04_cards_teens_adults/14-card-body-in-tension.webp",
    "практики на неделю": "04_cards_teens_adults/16-card-want-to-recover-but-unclear-how.webp",
    "замечать напряжение раньше": "04_cards_teens_adults/14-card-body-in-tension.webp",
    "получить инструменты восстановления": "04_cards_teens_adults/16-card-want-to-recover-but-unclear-how.webp",
}

CARD_IMAGE_BY_LABEL.update(
    {
        "спокойный круг обсуждения": "02_program_scenes/01-scene-group-discussion-circle-format.webp",
        "маленький вывод для дома": "03_cards_children/06-children-card-asking-and-agreeing.webp",
        "психолог мгу": "02_program_scenes/12-scene-warm-conversation-modern-interior.webp",
        "эмоции и состояния": "03_cards_children/01-children-card-emotion-cards.webp",
        "быстрая психология": "02_program_scenes/06-scene-bright-wellness-seminar.webp",
        "упражнения на знакомство": "04_cards_teens_adults/03-card-communication-difficulties.webp",
        "опыт быть услышанным": "03_cards_children/07-children-card-feeling-heard.webp",
        "понимание своих реакций": "04_cards_teens_adults/04-card-low-self-esteem.webp",
        "разбираем реальные ситуации": "04_cards_teens_adults/03-card-communication-difficulties.webp",
        "называем чувства": "03_cards_children/01-children-card-emotion-cards.webp",
        "опыт безопасного разговора": "02_program_scenes/12-scene-warm-conversation-modern-interior.webp",
        "меньше внутреннего давления": "04_cards_teens_adults/01-card-anxiety-and-tension.webp",
        "сильные стороны": "04_cards_teens_adults/04-card-low-self-esteem.webp",
        "интересы и ценности": "04_cards_teens_adults/09-card-hard-to-choose-direction.webp",
        "разговор о будущем без давления": "02_program_scenes/12-scene-warm-conversation-modern-interior.webp",
        "больше ясности": "04_cards_teens_adults/09-card-hard-to-choose-direction.webp",
        "понимание сильных сторон": "04_cards_teens_adults/04-card-low-self-esteem.webp",
        "12 зелёных пуфов": "01_space_design/02-centia-studio-main-interior-green-seating.webp",
        "15 мягких стульев": "01_space_design/05-centia-studio-flex-room-plants-seating.webp",
        "арочные окна": "01_space_design/03-centia-studio-workshop-space-natural-light.webp",
        "сакральная геометрия": "01_space_design/04-centia-studio-wellness-space-natural-light.webp",
        "тв и флипчарт": "01_space_design/03-centia-studio-workshop-space-natural-light.webp",
        "зелёный вход": "01_space_design/05-centia-studio-flex-room-plants-seating.webp",
        "короткая теория": "02_program_scenes/06-scene-bright-wellness-seminar.webp",
        "обсуждение без осуждения": "02_program_scenes/12-scene-warm-conversation-modern-interior.webp",
        "границы и договорённости": "04_cards_teens_adults/03-card-communication-difficulties.webp",
        "меньше чувства вины": "04_cards_teens_adults/13-card-hard-to-rest-without-guilt.webp",
        "новый язык контакта": "04_cards_teens_adults/03-card-communication-difficulties.webp",
        "обсуждение в группе": "02_program_scenes/01-scene-group-discussion-circle-format.webp",
        "лучше понимать свои состояния": "03_cards_children/01-children-card-emotion-cards.webp",
        "почувствовать больше внутренней опоры": "04_cards_teens_adults/16-card-want-to-recover-but-unclear-how.webp",
    }
)


def esc(value: Any) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def load_context() -> dict[str, Any]:
    if not CONTEXT_PATH.exists():
        return {}
    return json.loads(CONTEXT_PATH.read_text(encoding="utf-8"))


def site_base(root_site_url: str) -> str:
    return root_site_url.rstrip("/") + "/" + OUTPUT_DIRNAME


def page_url(root_site_url: str, filename: str) -> str:
    base = site_base(root_site_url)
    return base + "/" if filename == "index.html" else f"{base}/{filename}"


def seo_image_url(root_site_url: str, image_rel: str) -> str:
    return f"{site_base(root_site_url)}/assets/seo-images/{image_rel}"


def copy_tree(source: Path, destination: Path) -> None:
    if not source.exists():
        return
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(source, destination)


def externalize_data_images(page_html: str, page_stem: str, out_assets: Path) -> tuple[str, list[str]]:
    out_assets.mkdir(parents=True, exist_ok=True)
    created: list[str] = []
    index = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal index
        index += 1
        raw = base64.b64decode(match.group("data"))
        ext = "jpg" if match.group("kind") == "jpeg" else match.group("kind")
        digest = hashlib.sha256(raw).hexdigest()[:12]
        filename = f"{page_stem}-{index:02d}-{digest}.{ext}"
        target = out_assets / filename
        if not target.exists():
            target.write_bytes(raw)
        created.append(f"assets/generated/{filename}")
        if index == 1:
            return f'src="assets/generated/{filename}" fetchpriority="high" decoding="async"'
        return f'src="assets/generated/{filename}" loading="lazy" decoding="async"'

    return DATA_IMAGE_RE.sub(replace, page_html), created


def collect_local_images(page_html: str) -> list[str]:
    return sorted(set(LOCAL_IMAGE_RE.findall(page_html)))


def enrich_list_cards(page_html: str) -> str:
    def replace(match: re.Match[str]) -> str:
        label = re.sub(r"\s+", " ", match.group("label")).strip()
        image = CARD_IMAGE_BY_LABEL.get(label.lower())
        if not image:
            return match.group(0)
        image_src = f"assets/seo-images/{image}"
        image_alt = f"Мини-изображение для карточки: {label}"
        return (
            '<div class="list-card card-with-image">'
            f'<strong>{match.group("label")}</strong>'
            f'{match.group("rest")}'
            f'<img class="list-card-image" src="{esc(image_src)}" loading="lazy" decoding="async" alt="{esc(image_alt)}">'
            "</div>"
        )

    return re.sub(
        r'<div class="list-card"><strong>(?P<label>.*?)</strong>(?P<rest>(?:<p>.*?</p>)?)</div>',
        replace,
        page_html,
        flags=re.DOTALL,
    )


def build_jsonld(root_site_url: str, filename: str, meta: dict[str, str], context: dict[str, Any]) -> str:
    project = context.get("project", {})
    location = context.get("location_and_market_context", {})
    founder = project.get("founder", {})
    url = page_url(root_site_url, filename)
    graph: list[dict[str, Any]] = [
        {
            "@type": "WebSite",
            "@id": f"{site_base(root_site_url)}/#website",
            "url": f"{site_base(root_site_url)}/",
            "name": "Центия",
            "inLanguage": "ru-RU",
        },
        {
            "@type": "LocalBusiness",
            "@id": f"{site_base(root_site_url)}/#studio",
            "name": "Центия",
            "description": "Студия психологических групп для детей, подростков, родителей и взрослых.",
            "url": f"{site_base(root_site_url)}/",
            "founder": {
                "@type": "Person",
                "name": founder.get("name_ru", "Татьяна Мунн"),
                "url": "https://moonn.ru/",
            },
            "address": {
                "@type": "PostalAddress",
                "addressLocality": location.get("city", "Москва"),
                "addressCountry": "RU",
            },
            "areaServed": [
                "Марьина Роща",
                "Рижская",
                "Мещанский район",
                "Москва",
            ],
        },
        {
            "@type": "WebPage",
            "@id": url + "#webpage",
            "url": url,
            "name": meta["title"],
            "description": meta["description"],
            "isPartOf": {"@id": f"{site_base(root_site_url)}/#website"},
            "about": {"@id": f"{site_base(root_site_url)}/#studio"},
            "inLanguage": "ru-RU",
            "primaryImageOfPage": {
                "@type": "ImageObject",
                "url": seo_image_url(root_site_url, meta["image"]),
            },
        },
    ]
    if filename not in {"index.html", "prostranstvo.html", "raspisanie.html", "oplata.html", "o-tatyane.html", "contacts.html"}:
        graph.append(
            {
                "@type": "Service",
                "@id": url + "#service",
                "name": meta["title"].split("|")[0].strip(),
                "provider": {"@id": f"{site_base(root_site_url)}/#studio"},
                "areaServed": "Москва",
                "serviceType": "Психологическая группа",
                "url": url,
            }
        )
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)


def inject_head(page_html: str, root_site_url: str, filename: str, meta: dict[str, str], context: dict[str, Any]) -> str:
    canonical = page_url(root_site_url, filename)
    image = seo_image_url(root_site_url, meta["image"])
    page_html = TITLE_RE.sub(f"<title>{esc(meta['title'])}</title>", page_html, count=1)
    page_html = DESCRIPTION_RE.sub(
        f'<meta name="description" content="{esc(meta["description"])}">',
        page_html,
        count=1,
    )
    page_html = re.sub(r'<link\s+rel="canonical"[^>]*>\s*', "", page_html, flags=re.IGNORECASE)
    page_html = re.sub(r'<meta\s+name="robots"[^>]*>\s*', "", page_html, flags=re.IGNORECASE)
    page_html = re.sub(r'<meta\s+property="og:[^"]+"[^>]*>\s*', "", page_html, flags=re.IGNORECASE)
    page_html = re.sub(r'<meta\s+name="twitter:[^"]+"[^>]*>\s*', "", page_html, flags=re.IGNORECASE)
    jsonld = build_jsonld(root_site_url, filename, meta, context)
    injection = f"""
<link rel="canonical" href="{esc(canonical)}">
<meta name="robots" content="index,follow">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Центия">
<meta property="og:title" content="{esc(meta['title'])}">
<meta property="og:description" content="{esc(meta['description'])}">
<meta property="og:url" content="{esc(canonical)}">
<meta property="og:image" content="{esc(image)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(meta['title'])}">
<meta name="twitter:description" content="{esc(meta['description'])}">
<meta name="twitter:image" content="{esc(image)}">
<script type="application/ld+json">{jsonld}</script>
<style id="centia-codex-qa-gate">
  h1,h2,h3,.display-title,.section-title,.quote,.footer-logo,.final-cta h2,.program-content h3,.mode-text h3,.day-card h3,.price{{letter-spacing:0!important}}
  h1,h2,h3,p,a,button,summary,strong,span{{overflow-wrap:anywhere}}
  img{{background:#efe7d7}}
  .hero{{min-height:92svh!important}}
  .page-hero{{min-height:78svh!important}}
  .hero h1{{font-size:clamp(70px,12vw,178px)!important;line-height:.9!important;max-width:880px!important}}
  .page-hero h1{{font-size:clamp(62px,8.5vw,136px)!important;line-height:.92!important;max-width:980px!important}}
  .hero-lead{{font-size:clamp(20px,2.05vw,30px)!important;line-height:1.18!important;max-width:760px!important}}
  .section-title{{font-size:clamp(56px,7.1vw,112px)!important;line-height:.94!important;max-width:980px!important}}
  .section-copy{{font-size:clamp(19px,1.75vw,28px)!important;line-height:1.22!important}}
  .quote{{font-size:clamp(54px,7.5vw,124px)!important;line-height:.94!important}}
  .editorial-card h3{{font-size:clamp(34px,3.8vw,68px)!important;line-height:.98!important}}
  .program-content h3{{font-size:clamp(30px,2.4vw,38px)!important;line-height:1!important}}
  .mode-text h3{{font-size:clamp(42px,4.2vw,64px)!important;line-height:.96!important}}
  .day-card h3{{font-size:clamp(30px,2.5vw,40px)!important}}
  .footer-logo,.final-cta h2{{font-size:clamp(62px,8.2vw,136px)!important;line-height:.9!important}}
  .list-card.card-with-image{{position:relative;overflow:hidden;min-height:230px;padding:20px;background:linear-gradient(135deg,rgba(255,253,247,.94),rgba(239,231,215,.82))!important;isolation:isolate}}
  .list-card.card-with-image strong{{position:relative;z-index:2;max-width:72%;display:block}}
  .list-card.card-with-image p{{position:relative;z-index:2;max-width:70%}}
  .list-card-image{{position:absolute;right:0;bottom:0;width:64%;height:78%;object-fit:cover;object-position:center;border-radius:24px 0 8px 0;opacity:.92;z-index:1;filter:saturate(.92) contrast(1.02)}}
  .list-card.card-with-image:after{{content:"";position:absolute;inset:0;z-index:1;background:linear-gradient(115deg,rgba(255,253,247,.96) 0%,rgba(255,253,247,.86) 32%,rgba(255,253,247,.18) 70%)}}
  @media(max-width:680px){{
    .hero{{min-height:88svh!important}}
    .page-hero{{min-height:72svh!important}}
    .section-head,.section-copy,.container,.hero-inner,.page-intro,.editorial-card p{{max-width:100%!important}}
    .section-title{{font-size:clamp(38px,13vw,66px)!important}}
    .hero h1{{font-size:clamp(48px,17vw,86px)!important}}
    .page-hero h1{{font-size:clamp(42px,13vw,78px)!important}}
    .hero-lead{{font-size:19px!important}}
    .list-card.card-with-image{{min-height:190px}}
    .list-card.card-with-image strong{{max-width:78%}}
  }}
</style>
"""
    return page_html.replace("</head>", injection + "</head>", 1)


def build_image_sitemap(root_site_url: str, page_images: dict[str, list[str]]) -> str:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">',
    ]
    seo_manifest = SEO_IMAGES / "seo_manifest.optimized.json"
    seo_by_page: dict[str, list[dict[str, str]]] = {}
    if seo_manifest.exists():
        for item in json.loads(seo_manifest.read_text(encoding="utf-8")):
            suggested = item.get("suggested_page", "")
            seo_by_page.setdefault(suggested, []).append(item)
    suggested_map = {
        "index.html": ["homepage"],
        "deti-7-10.html": ["children-page"],
        "podrostki-11-13.html": ["teens-11-13-page", "teens-page"],
        "podrostki-14-16.html": ["teens-page"],
        "podrostki-15-17.html": ["teens-15-17-page"],
        "roditelyam.html": ["parents-page"],
        "vzroslym.html": ["adults-page"],
        "prostranstvo.html": ["space-page"],
    }
    for filename in PAGE_ORDER:
        lines.append(f"  <url><loc>{esc(page_url(root_site_url, filename))}</loc>")
        for image in page_images.get(filename, [])[:8]:
            lines.append(f"    <image:image><image:loc>{esc(site_base(root_site_url) + '/' + image)}</image:loc></image:image>")
        for key in suggested_map.get(filename, []):
            for item in seo_by_page.get(key, [])[:6]:
                image_url = seo_image_url(root_site_url, item["optimized_filename"])
                title = item.get("seo_title") or item.get("suggested_alt_text", "")
                caption = item.get("suggested_alt_text", "")
                lines.append(
                    "    <image:image>"
                    f"<image:loc>{esc(image_url)}</image:loc>"
                    f"<image:title>{esc(title)}</image:title>"
                    f"<image:caption>{esc(caption)}</image:caption>"
                    "</image:image>"
                )
        lines.append("  </url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def build_llms(root_site_url: str, context: dict[str, Any]) -> str:
    location = context.get("location_and_market_context", {})
    lines = [
        "# Центия",
        "",
        "Центия — студия психологических групп для детей, подростков, родителей и взрослых в Москве.",
        f"URL: {site_base(root_site_url)}/",
        "Founder: Татьяна Мунн",
        f"Location signal: {location.get('walking_message_for_site', 'Марьина Роща, Москва')}",
        "",
        "Canonical pages:",
    ]
    for filename in PAGE_ORDER:
        meta = PAGE_META[filename]
        lines.append(f"- {page_url(root_site_url, filename)} — {meta['title']}")
    lines.extend(
        [
            "",
            "Do not expose internal marketing tokens or developer notes on public pages.",
            "Use page titles, schema.org graph, image sitemap and canonical URLs as the machine-readable layer.",
        ]
    )
    return "\n".join(lines) + "\n"


def build_centia_site(out_dir: Path, root_site_url: str) -> list[str]:
    context = load_context()
    centia_out = out_dir / OUTPUT_DIRNAME
    if centia_out.exists():
        shutil.rmtree(centia_out)
    centia_out.mkdir(parents=True, exist_ok=True)
    generated_assets = centia_out / "assets" / "generated"

    copy_tree(SOURCE / "assets", centia_out / "assets")
    copy_tree(SEO_IMAGES, centia_out / "assets" / "seo-images")

    page_images: dict[str, list[str]] = {}
    for filename in PAGE_ORDER:
        source_file = SOURCE / filename
        if not source_file.exists():
            raise FileNotFoundError(f"Missing Centia source page: {source_file}")
        page_html = source_file.read_text(encoding="utf-8")
        page_html, images = externalize_data_images(page_html, Path(filename).stem, generated_assets)
        page_html = enrich_list_cards(page_html)
        page_html = inject_head(page_html, root_site_url, filename, PAGE_META[filename], context)
        (centia_out / filename).write_text(page_html, encoding="utf-8")
        page_images[filename] = sorted(set(images + collect_local_images(page_html)))

    copy_tree(SOURCE / "refero-style-reference", centia_out / "refero-style-reference")
    (centia_out / "centia-image-sitemap.xml").write_text(build_image_sitemap(root_site_url, page_images), encoding="utf-8")
    (centia_out / "llms.txt").write_text(build_llms(root_site_url, context), encoding="utf-8")
    (centia_out / "source-provenance.json").write_text(
        json.dumps(
            {
                "source": "centia/source from centia_sequel_light.zip",
                "context": "centia/centia_chat_context_for_codex.json",
                "seo_images": "centia/seo-images from centia_images_seo_clean_renamed.zip",
                "domain_note": "Current build path is /centia/ under the repository Pages domain. DNS/CNAME switch to a Moonn subdomain requires explicit approval.",
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    return [OUTPUT_DIRNAME + "/" if filename == "index.html" else f"{OUTPUT_DIRNAME}/{filename}" for filename in PAGE_ORDER] + [
        f"{OUTPUT_DIRNAME}/centia-image-sitemap.xml",
        f"{OUTPUT_DIRNAME}/llms.txt",
    ]
