#!/usr/bin/env python3
"""
Validate paper metadata and PDF presence.
"""
import argparse
import sys
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FIELDS = [
    "title",
    "is_paper",
    "paper_id",
    "issue_slug",
    "issue_title",
    "publication_date",
    "authors",
    "keywords",
    "abstract",
    "pdf_path",
]


def parse_front_matter(path: Path) -> Dict[str, object]:
    data: Dict[str, object] = {}
    in_fm = False
    current_list_key = None
    current_block_key = None
    block_lines: List[str] = []

    with path.open(encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            if line.strip() == "---":
                if not in_fm:
                    in_fm = True
                    continue
                else:
                    break

            if not in_fm:
                continue

            if current_block_key:
                if line.startswith("  ") or line.strip() == "":
                    block_lines.append(line.strip())
                    continue
                else:
                    data[current_block_key] = "\n".join(block_lines).strip()
                    current_block_key = None
                    block_lines = []

            if line.startswith("  - ") and current_list_key:
                data.setdefault(current_list_key, []).append(line[4:].strip())
                continue

            if ":" in line:
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip()
                if value == "":
                    current_list_key = key
                    data[key] = []
                    continue
                if value == "|":
                    current_block_key = key
                    block_lines = []
                    continue
                current_list_key = None
                data[key] = value.strip('"')

    if current_block_key:
        data[current_block_key] = "\n".join(block_lines).strip()

    return data


def validate_paper(path: Path, ci: bool) -> Tuple[int, int]:
    errors = 0
    warnings = 0
    fm = parse_front_matter(path)

    missing = [field for field in REQUIRED_FIELDS if field not in fm or fm[field] in (None, "", [])]
    if missing:
        errors += 1
        print(f"[ERROR] {path.relative_to(ROOT)} missing fields: {', '.join(missing)}")

    if not fm.get("authors"):
        warnings += 1
        print(f"[WARN ] {path.relative_to(ROOT)} authors list is empty.")

    if not fm.get("keywords"):
        warnings += 1
        print(f"[WARN ] {path.relative_to(ROOT)} has no keywords.")

    abstract = fm.get("abstract", "")
    if isinstance(abstract, str) and len(abstract.strip().split()) < 20:
        warnings += 1
        print(f"[WARN ] {path.relative_to(ROOT)} abstract is very short.")

    pdf_path = fm.get("pdf_path")
    if pdf_path:
        pdf_file = ROOT / pdf_path.lstrip("/")
        if not pdf_file.exists():
            msg = f"[{'ERROR' if ci else 'WARN '}] {path.relative_to(ROOT)} PDF missing at {pdf_path}"
            print(msg)
            if ci:
                errors += 1
            else:
                warnings += 1

    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description="Validate paper front matter and PDFs.")
    parser.add_argument("--ci", action="store_true", help="Fail on missing PDFs and required fields.")
    args = parser.parse_args()

    paper_paths = sorted(ROOT.glob("issues/*/paper-*.md"))
    total_errors = 0
    total_warnings = 0

    if not paper_paths:
        print("No papers found.")

    for paper in paper_paths:
        errs, warns = validate_paper(paper, args.ci)
        total_errors += errs
        total_warnings += warns

    print(f"\nValidation complete. Errors: {total_errors}, Warnings: {total_warnings}")
    if total_errors > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
