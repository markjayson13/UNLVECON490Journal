#!/usr/bin/env python3
import argparse
import re
from pathlib import Path
from typing import List, Dict

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "issue-template.md"
ISSUES_PAGE = ROOT / "issues.md"


def read_front_matter(path: Path) -> Dict[str, str]:
    """Lightweight front matter reader for issue files."""
    if not path.exists():
        return {}
    data = {}
    inside = False
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line == "---":
                inside = not inside
                if not inside:
                    break
                continue
            if inside and ":" in line:
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip().strip('"')
    return data


def format_issue_content(issue_slug: str, title: str, order: str) -> str:
    template = TEMPLATE.read_text(encoding="utf-8")
    return (
        template.replace("{{ISSUE_SLUG}}", issue_slug)
        .replace("{{ISSUE_TITLE}}", title)
        .replace("{{ISSUE_ORDER}}", order)
    )


def update_issues_page(entries: List[Dict[str, str]]):
    """Rewrite the managed list block in issues.md in newest-first order."""
    text = ISSUES_PAGE.read_text(encoding="utf-8")
    start = "<!-- issues-list:start -->"
    end = "<!-- issues-list:end -->"
    if start not in text or end not in text:
        return

    try:
        sorted_entries = sorted(
            entries, key=lambda e: float(e.get("issue_order", 0)), reverse=True
        )
    except ValueError:
        sorted_entries = entries

    lines = [start]
    for entry in sorted_entries:
        slug = entry["issue_slug"]
        title = entry.get("issue_title") or entry.get("title") or slug
        lines.append(f"- [{title}]({{{{ '/issues/{slug}/' | relative_url }}}})")
    lines.append(end)

    pattern = re.compile(
        r"<!-- issues-list:start -->.*<!-- issues-list:end -->", re.DOTALL
    )
    ISSUES_PAGE.write_text(
        pattern.sub("\n".join(lines), text), encoding="utf-8"
    )
    print("Updated issues.md list (newest first).")


def collect_issues() -> List[Dict[str, str]]:
    issues = []
    issues_dir = ROOT / "issues"
    for path in issues_dir.glob("*/index.md"):
        fm = read_front_matter(path)
        if not fm:
            continue
        issues.append(
            {
                "issue_slug": fm.get("issue_slug") or path.parent.name,
                "issue_title": fm.get("issue_title")
                or fm.get("title")
                or path.parent.name,
                "issue_order": fm.get("issue_order", "0"),
            }
        )
    return issues


def main():
    parser = argparse.ArgumentParser(
        description="Create a new issue directory with an index page."
    )
    parser.add_argument("issue_slug", help="Issue slug, e.g., 2025-fall")
    parser.add_argument(
        "--title", help="Issue title (defaults to slug converted to title case)"
    )
    parser.add_argument(
        "--order",
        help="Numeric order for sorting (newest first), e.g., 2025.2 for Fall 2025",
        default=None,
    )
    args = parser.parse_args()

    issue_slug = args.issue_slug.rstrip("/")
    title = args.title or issue_slug.replace("-", " ").title()
    order = args.order or "0"

    issue_dir = ROOT / "issues" / issue_slug
    issue_dir.mkdir(parents=True, exist_ok=True)
    index_path = issue_dir / "index.md"

    if index_path.exists():
        print(f"{index_path} already exists; no changes made.")
        return

    content = format_issue_content(issue_slug, title, order)
    index_path.write_text(content, encoding="utf-8")
    print(f"Created {index_path.relative_to(ROOT)}")

    assets_dir = ROOT / "assets" / "papers" / issue_slug
    assets_dir.mkdir(parents=True, exist_ok=True)
    print(f"Ensured PDF directory: {assets_dir.relative_to(ROOT)}")

    entries = collect_issues()
    update_issues_page(entries)


if __name__ == "__main__":
    main()
