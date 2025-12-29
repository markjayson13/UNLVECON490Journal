#!/usr/bin/env python3
import argparse
from pathlib import Path
from typing import List

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "paper-template.md"
ALLOWED_CATEGORIES = [
    "Applied Microeconomics",
    "Macroeconomics",
    "Economic Growth",
    "Public and Policy",
    "Labor and Demography",
    "Health",
    "Education",
    "International",
    "Finance",
    "IO and Strategy",
    "Environmental and Resource",
    "Economic History and Institutions",
    "Methods and Econometrics",
]


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


def to_yaml_block(items: List[str], placeholder: str) -> str:
    if not items:
        return f"  - {placeholder}"
    return "\n".join(f"  - {item.strip()}" for item in items if item.strip())


def render_template(
    issue_slug: str,
    issue_title: str,
    paper_number: str,
    paper_number_int: int,
    paper_title: str,
    authors_block: str,
    keywords_block: str,
    categories_block: str,
    abstract_text: str,
    publication_date: str,
) -> str:
    content = TEMPLATE.read_text(encoding="utf-8")
    return (
        content.replace("{{ISSUE_SLUG}}", issue_slug)
        .replace("{{ISSUE_TITLE}}", issue_title)
        .replace("{{PAPER_NUMBER}}", paper_number)
        .replace("{{PAPER_NUMBER_INT}}", str(paper_number_int))
        .replace("{{PAPER_TITLE}}", paper_title.strip())
        .replace("{{AUTHORS_BLOCK}}", authors_block)
        .replace("{{KEYWORDS_BLOCK}}", keywords_block)
        .replace("{{CATEGORIES_BLOCK}}", categories_block)
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
    parser.add_argument("--categories", help="Comma-separated categories from the allowed list")
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
    paper_title = prompt_if_missing(args.title, "Paper title").strip('"')
    authors_input = prompt_if_missing(args.authors or "", "Authors (comma separated)")
    keywords_input = prompt_if_missing(args.keywords or "", "Keywords (comma separated)")
    categories_input = prompt_if_missing(
        args.categories or "", "Categories (comma separated, choose from allowed list)"
    )
    abstract_text = prompt_if_missing(args.abstract or "", "Abstract")
    publication_date = prompt_if_missing(
        args.publication_date or "", "Publication date (YYYY-MM-DD)"
    )

    authors = [a.strip() for a in authors_input.split(",") if a.strip()]
    keywords = [k.strip() for k in keywords_input.split(",") if k.strip()]
    categories = [c.strip() for c in categories_input.split(",") if c.strip()]

    invalid = [c for c in categories if c not in ALLOWED_CATEGORIES]
    if invalid:
        print("The following categories are not allowed:")
        for item in invalid:
            print(f" - {item}")
        print("Allowed categories:")
        for item in ALLOWED_CATEGORIES:
            print(f" - {item}")
        return

    authors_block = to_yaml_block(authors, "Author Name")
    keywords_block = to_yaml_block(keywords, "keyword")
    categories_block = to_yaml_block(categories, "Education")

    try:
        paper_number_int = int(paper_number)
    except ValueError:
        print(f"Paper number must be numeric, got '{paper_number}'.")
        return

    rendered = render_template(
        issue_slug=issue_slug,
        issue_title=issue_title,
        paper_number=paper_number,
        paper_number_int=paper_number_int,
        paper_title=paper_title,
        authors_block=authors_block,
        keywords_block=keywords_block,
        categories_block=categories_block,
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
