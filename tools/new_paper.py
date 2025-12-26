#!/usr/bin/env python3
import argparse
from pathlib import Path
from typing import List

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "paper-template.md"


def read_front_matter_title(issue_slug: str) -> str:
    index_path = ROOT / "issues" / issue_slug / "index.md"
    if not index_path.exists():
        return issue_slug.replace("-", " ").title()
    inside = False
    with index_path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line == "---":
                inside = not inside
                continue
            if inside and line.lower().startswith("title:"):
                return line.split(":", 1)[1].strip()
    return issue_slug.replace("-", " ").title()


def to_yaml_block(items: List[str]) -> str:
    if not items:
        return "  - Author Name"
    return "\n".join(f"  - {item.strip()}" for item in items if item.strip())


def render_template(
    issue_slug: str,
    issue_title: str,
    paper_number: str,
    paper_title: str,
    authors_block: str,
    keywords_block: str,
    abstract_text: str,
    publication_date: str,
) -> str:
    content = TEMPLATE.read_text(encoding="utf-8")
    return (
        content.replace("{{ISSUE_SLUG}}", issue_slug)
        .replace("{{ISSUE_TITLE}}", issue_title)
        .replace("{{PAPER_NUMBER}}", paper_number)
        .replace("{{PAPER_NUMBER_INT}}", str(int(paper_number)))
        .replace("{{PAPER_TITLE}}", paper_title.strip())
        .replace("{{AUTHORS_BLOCK}}", authors_block)
        .replace("{{KEYWORDS_BLOCK}}", keywords_block)
        .replace("{{ABSTRACT_TEXT}}", abstract_text.strip())
        .replace("{{PUBLICATION_DATE}}", publication_date)
    )


def prompt_if_missing(current: str, prompt: str) -> str:
    if current:
        return current
    return input(f"{prompt}: ").strip()


def main():
    parser = argparse.ArgumentParser(
        description="Create a paper page for an existing issue."
    )
    parser.add_argument("--issue", required=True, help="Issue slug, e.g., 2025-fall")
    parser.add_argument("--number", required=True, help="Paper number (001, 002...)")
    parser.add_argument("--title", help="Paper title")
    parser.add_argument("--authors", help="Comma-separated authors")
    parser.add_argument("--keywords", help="Comma-separated keywords")
    parser.add_argument("--abstract", help="Abstract text (multi-line allowed)")
    parser.add_argument(
        "--publication-date",
        dest="publication_date",
        help="Publication date YYYY-MM-DD",
        default=None,
    )
    args = parser.parse_args()

    issue_slug = args.issue.rstrip("/")
    issue_title = read_front_matter_title(issue_slug)
    paper_number = args.number.zfill(3)
    paper_title = prompt_if_missing(args.title, "Paper title")
    authors_input = prompt_if_missing(args.authors or "", "Authors (comma separated)")
    keywords_input = prompt_if_missing(args.keywords or "", "Keywords (comma separated)")
    abstract_text = prompt_if_missing(args.abstract or "", "Abstract")
    publication_date = prompt_if_missing(
        args.publication_date or "", "Publication date (YYYY-MM-DD)"
    )

    authors = [a.strip() for a in authors_input.split(",") if a.strip()]
    keywords = [k.strip() for k in keywords_input.split(",") if k.strip()]

    authors_block = to_yaml_block(authors)
    keywords_block = to_yaml_block(keywords) if keywords else "  - keyword"

    rendered = render_template(
        issue_slug=issue_slug,
        issue_title=issue_title,
        paper_number=paper_number,
        paper_title=paper_title,
        authors_block=authors_block,
        keywords_block=keywords_block,
        abstract_text=abstract_text,
        publication_date=publication_date,
    )

    paper_path = ROOT / "issues" / issue_slug / f"paper-{paper_number}.md"
    if paper_path.exists():
        print(f"{paper_path} already exists; aborting.")
        return

    paper_path.parent.mkdir(parents=True, exist_ok=True)
    paper_path.write_text(rendered, encoding="utf-8")
    print(f"Created {paper_path.relative_to(ROOT)}")

    assets_dir = ROOT / "assets" / "papers" / issue_slug
    assets_dir.mkdir(parents=True, exist_ok=True)
    pdf_path = assets_dir / f"paper-{paper_number}.pdf"
    print(f"Place the PDF at: {pdf_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
