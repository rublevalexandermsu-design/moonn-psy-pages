import argparse
import json
import time
from pathlib import Path

import pyautogui
from pywinauto import Desktop

from tilda_production_theme_rollout_ui import hard_navigate, publish_page


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCOPE = ROOT / "registry" / "tilda" / "moonn-production-83-rollout.json"
DEFAULT_SNIPPET = ROOT / "output" / "moonn-radiant-production-snippet.html"


def chrome_window():
    candidates = []
    for window in Desktop(backend="uia").windows():
        title = window.window_text()
        if title.endswith(" - Google Chrome") and "0.0.0.5" not in title and "about:blank" not in title:
            candidates.append(window)
    if not candidates:
        raise RuntimeError("No authenticated regular Chrome window found")
    for window in candidates:
        try:
            address = window.descendants(control_type="Edit")[0].window_text()
        except Exception:
            address = ""
        if "tilda.ru" in address or "DT_OK" in title:
            return window
    return candidates[0]


def console_edit(window):
    edits = window.descendants(control_type="Edit")
    candidates = []
    for edit in edits:
        rect = edit.rectangle()
        if rect.left > 500 and rect.top > 280 and rect.width() > 300 and edit.window_text() != "Filter":
            candidates.append((rect.top, edit))
    if not candidates:
        raise RuntimeError("DevTools console input not found")
    return sorted(candidates, key=lambda item: item[0])[0][1]


def open_devtools_console(window) -> None:
    window.set_focus()
    try:
        console_edit(window)
        return
    except Exception:
        pass
    pyautogui.hotkey("ctrl", "shift", "j")
    time.sleep(3.5)
    pyautogui.click(760, 352)
    time.sleep(0.4)
    try:
        console_edit(window)
        return
    except Exception:
        pyautogui.press("f12")
        time.sleep(3.5)
        pyautogui.click(760, 352)
        time.sleep(0.4)


def close_devtools(window) -> None:
    window.set_focus()
    try:
        console_edit(window)
    except Exception:
        return
    pyautogui.press("f12")
    time.sleep(1.8)


def submit_headcode(window, project_id: str, page_id: str, snippet: str) -> str:
    command = (
        "td__submit('/projects/submit/',"
        + json.dumps(
            {
                "comm": "editpageheadcode",
                "projectid": int(project_id),
                "pageid": int(page_id),
                "headcode": snippet,
            },
            ensure_ascii=False,
        )
        + ",{ctext:'codex devtools'},"
        + "function(r){document.title='DT_OK_'+JSON.stringify(r)},"
        + "function(e){document.title='DT_ERR_'+JSON.stringify(e)});"
    )
    edit = console_edit(window)
    edit.set_focus()
    edit.set_edit_text(command)
    time.sleep(0.3)
    edit.type_keys("{ENTER}")
    time.sleep(5.0)
    title = window.window_text()
    if "DT_OK_" not in title:
        raise RuntimeError(f"Tilda submit did not return OK for page {page_id}: {title}")
    return title


def main() -> int:
    parser = argparse.ArgumentParser(description="Save Tilda page headcode through authenticated Chrome DevTools console.")
    parser.add_argument("--project-id", default="8326812")
    parser.add_argument("--scope", default=str(DEFAULT_SCOPE.relative_to(ROOT)))
    parser.add_argument("--snippet", default=str(DEFAULT_SNIPPET.relative_to(ROOT)))
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int, default=3)
    parser.add_argument("--out", default="output/tilda-headcode-submit-devtools-ui.json")
    args = parser.parse_args()

    pages = json.loads((ROOT / args.scope).read_text(encoding="utf-8"))
    snippet = (ROOT / args.snippet).read_text(encoding="utf-8-sig").strip()
    selected = pages[args.offset : args.offset + args.limit]
    window = chrome_window()
    results = []

    for page in selected:
        page_id = str(page["source_page_id"])
        item = {
            "alias": page.get("alias"),
            "page_id": page_id,
            "production_url": page.get("production_url"),
        }
        try:
            hard_navigate(
                window,
                f"https://tilda.ru/projects/editheadcode/?projectid={args.project_id}&pageid={page_id}",
                wait_seconds=5.5,
            )
            open_devtools_console(window)
            item["submit_title"] = submit_headcode(window, args.project_id, page_id, snippet)
            close_devtools(window)
            publish_page(window, page_id, args.project_id)
            item["status"] = "saved_and_published"
        except Exception as exc:
            item["status"] = "error"
            item["error"] = str(exc)
            try:
                close_devtools(window)
            except Exception:
                pass
        results.append(item)
        out = ROOT / args.out
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "out": args.out,
                "processed": len(results),
                "errors": sum(1 for item in results if item.get("status") == "error"),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
