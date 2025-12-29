# UNLV ECON 495 Capstone Proceedings

Static GitHub Pages site built with **Jekyll + Minimal Mistakes**. Papers are organized by issue (semester + year). Each paper page exposes its abstract, metadata, and PDF link plus Google Scholar–friendly citation tags.

## Local preview (macOS)

```bash
brew install ruby
gem install bundler
bundle install

# Serve locally with live reload
bundle exec jekyll serve --livereload

# Build only
bundle exec jekyll build
```

Site output is written to `_site/`.

## Adding an issue (semester/year)

```bash
python tools/new_issue.py 2026-spring --title "Spring 2026" --order 2026.1
```

What it does:
- Creates `issues/<issue_slug>/index.md` from `templates/issue-template.md`
- Ensures `assets/papers/<issue_slug>/` exists
- Inserts the new issue link into `issues.md` (newest first)

## Adding a paper

```bash
python tools/new_paper.py --issue 2026-spring --number 001 \
  --title "Paper Title" \
  --authors "Author One,Author Two" \
  --keywords "economics,policy" \
  --publication-date "2026-05-15"
```

The script prompts for any missing fields, writes `issues/<issue_slug>/paper-###.md` from `templates/paper-template.md`, and tells you where to place the PDF (`assets/papers/<issue_slug>/paper-###.pdf`).

## Validate the catalog

```bash
python tools/validate_catalog.py           # warnings only
python tools/validate_catalog.py --ci      # fail on errors (used in CI)
```

Checks required front matter, keywords/abstract length, and PDF existence.

## Deployment

GitHub Actions workflow: `.github/workflows/deploy-pages.yml`
- Triggers on pushes to `main` and manual dispatch
- Runs catalog validation, builds with Jekyll, and deploys to Pages
- Publishes to: `https://markjayson13.github.io/UNLVECON490Journal/`

Branch-based fallback (no Actions):
1) Settings → Pages → Source: select `main` branch and `/ (root)`  
2) Save. Pages will serve the built site in a few minutes.

## Baseurl troubleshooting

The site is a GitHub project page and **must** use:

```yaml
url: "https://markjayson13.github.io"
baseurl: "/UNLVECON490Journal"
```

If links 404 locally, include `--baseurl ''` when serving (`bundle exec jekyll serve --baseurl ''`).

## Placeholder PDFs

Example PDFs live in `assets/papers/2025-fall/`. Replace them with your actual exports but keep the same filenames to match paper pages.
