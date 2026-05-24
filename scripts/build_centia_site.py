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
  @media(max-width:680px){{
    .section-head,.section-copy,.container,.hero-inner,.page-intro,.editorial-card p{{max-width:100%!important}}
    .section-title{{font-size:clamp(44px,16vw,82px)!important}}
    .hero h1{{font-size:clamp(58px,22vw,112px)!important}}
    .page-hero h1{{font-size:clamp(50px,16vw,96px)!important}}
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
