from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from pywinauto import Desktop
from pywinauto.keyboard import send_keys


ROOT = Path(__file__).resolve().parents[1]


def chrome_window():
    candidates = []
    for window in Desktop(backend="uia").windows(title_re=".*Google Chrome.*"):
        try:
            address = next(
                edit.window_text()
                for edit in window.descendants(control_type="Edit")
                if edit.element_info.automation_id == "view_1012"
            )
        except Exception:
            address = ""
        candidates.append((window, address))
    for window, address in candidates:
        title = window.window_text() or ""
        if "tilda.ru" in address or "rublevalexandermsu@gmail.com" in title or title.strip():
            window.restore()
            window.set_focus()
            return window
    raise RuntimeError("No Google Chrome window found")


def address_bar(window):
    for edit in window.descendants(control_type="Edit"):
        if edit.element_info.automation_id == "view_1012":
            return edit
    raise RuntimeError("Chrome address bar edit control not found")


def navigate(window, url: str, wait_seconds: float = 4.0):
    window.restore()
    window.set_focus()
    bar = address_bar(window)
    bar.set_focus()
    bar.set_edit_text(url)
    send_keys("{ENTER}")
    time.sleep(wait_seconds)


def run_javascript_url(window, code: str, wait_seconds: float = 2.0):
    window.restore()
    window.set_focus()
    bar = address_bar(window)
    bar.set_focus()
    bar.set_edit_text("javascript:" + code)
    send_keys("{ENTER}")
    time.sleep(wait_seconds)


def publish_page(window, project_id: str, page_id: str):
    navigate(window, f"https://tilda.ru/page/?pageid={page_id}&projectid={project_id}", wait_seconds=7.0)
    buttons = [button for button in window.descendants(control_type="Button") if (button.window_text() or "").strip() == "Опубликовать"]
    if not buttons:
        raise RuntimeError(f"Publish button not found for page {page_id}")
    buttons[0].click_input()
    time.sleep(6.0)


def load_pages(packet_path: Path) -> list[dict]:
    return json.loads(packet_path.read_text(encoding="utf-8"))["pages"]


def apply_head_layer(window, project_id: str, page: dict, snippet: str) -> dict:
    page_id = str(page["sourcePageId"])
    navigate(window, f"https://tilda.ru/projects/editheadcode/?projectid={project_id}&pageid={page_id}", wait_seconds=5.0)
    payload = {
        "pageId": page_id,
        "start": "<!-- moonn-five-page-seo-sprint-layer:start -->",
        "end": "<!-- moonn-five-page-seo-sprint-layer:end -->",
        "snippet": snippet.strip(),
    }
    code = """
(async function(payload){
  function wait(ms){return new Promise(resolve=>setTimeout(resolve,ms));}
  var editor = window.ace && window.ace.edit ? window.ace.edit("aceeditor_head") : null;
  var textarea = document.querySelector("textarea");
  var current = editor ? editor.getValue() : (textarea ? textarea.value : "");
  if (typeof current !== "string") current = "";
  var start = current.indexOf(payload.start);
  while (start !== -1) {
    var end = current.indexOf(payload.end, start + payload.start.length);
    if (end === -1 || end < start) break;
    current = current.slice(0, start).trimEnd() + "\\n" + current.slice(end + payload.end.length).trimStart();
    start = current.indexOf(payload.start);
  }
  var next = (current.trimEnd() + "\\n\\n" + payload.snippet + "\\n").trimStart();
  if (editor) {
    editor.setValue(next, -1);
    editor.session && editor.session.setValue(next);
  }
  if (textarea) {
    textarea.value = next;
    textarea.dispatchEvent(new Event("input", {bubbles:true}));
    textarea.dispatchEvent(new Event("change", {bubbles:true}));
  }
  var save = document.querySelector(".js-btn-save") || Array.from(document.querySelectorAll("button,input[type=button],input[type=submit]")).find(function(el){
    return /Сохранить/i.test(el.textContent || el.value || "");
  });
  if (!save) throw new Error("save button not found");
  save.click();
  await wait(2600);
  document.title = "HEAD_UI_SAVED_" + payload.pageId;
})(__PAYLOAD__).catch(function(error){
  document.title = "HEAD_UI_ERROR_" + __PAGE_ID__ + "_" + String(error && error.message || error).slice(0,80);
});
""".replace("__PAYLOAD__", json.dumps(payload, ensure_ascii=False)).replace("__PAGE_ID__", json.dumps(page_id))
    run_javascript_url(window, code, wait_seconds=3.0)
    deadline = time.time() + 14
    title = window.window_text()
    while f"HEAD_UI_SAVED_{page_id}" not in title and time.time() < deadline:
        time.sleep(0.5)
        title = window.window_text()
    if f"HEAD_UI_SAVED_{page_id}" not in title:
        raise RuntimeError(f"HEAD save was not confirmed for page {page_id}: {title}")
    return {"pageId": page_id, "status": "saved", "method": "chrome_javascript_url_aceeditor_head"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply Moonn five-page SEO/AEO layer snippet to scoped Tilda page HEAD editors.")
    parser.add_argument("--project-id", default="8326812")
    parser.add_argument("--packet", default="docs/moonn-five-page-seo-packets-2026-05-21.json")
    parser.add_argument("--snippet", default="docs/moonn-five-page-seo-sprint-head-snippet-2026-05-21.html")
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--out", default="output/tilda-five-page-head-layer-ui-rollout-2026-05-21.json")
    args = parser.parse_args()

    pages = load_pages(ROOT / args.packet)
    selected = pages[args.offset : args.offset + args.limit]
    snippet = (ROOT / args.snippet).read_text(encoding="utf-8")
    out_path = ROOT / args.out
    results = json.loads(out_path.read_text(encoding="utf-8")) if out_path.exists() else []
    window = chrome_window()
    for page in selected:
        item = {
            "pageId": str(page["sourcePageId"]),
            "url": page["url"],
            "alias": page.get("alias"),
            "snippet": args.snippet,
            "publishRequested": args.publish,
        }
        try:
            item["headLayer"] = apply_head_layer(window, args.project_id, page, snippet)
            if args.publish:
                publish_page(window, args.project_id, str(page["sourcePageId"]))
                item["published"] = True
            item["status"] = "saved"
        except Exception as exc:  # noqa: BLE001
            item["status"] = "error"
            item["error"] = str(exc)
        results.append(item)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"out": str(out_path.relative_to(ROOT)), "processed": len(selected), "errors": sum(1 for item in results[-len(selected):] if item.get("status") == "error")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
