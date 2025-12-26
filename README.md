# UNLV ECON 490 Journal

A GitHub Pages site for hosting UNLV ECON 490 academic papers using Jekyll with the Just-the-Docs theme.

## Features

- 📚 Organized paper collections by semester
- 🔍 Full-text search functionality
- 📱 Responsive design
- 🎨 Clean, academic layout using Just-the-Docs theme

## Site Structure

```
├── _config.yml                          # Jekyll configuration
├── index.md                             # Home page
├── issues.md                            # Issues listing page
├── issues/
│   └── 2025-fall/
│       ├── index.md                     # Fall 2025 issue page
│       ├── paper-001.md                 # Paper 001 details
│       └── paper-002.md                 # Paper 002 details
└── assets/
    └── papers/
        └── 2025-fall/
            ├── paper-001.pdf            # PDF file for paper 001
            └── paper-002.pdf            # PDF file for paper 002
```

## Deployment Steps

### 1. Configure GitHub Pages

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Pages**
3. Under **Source**, select the branch you want to deploy (e.g., `main` or `copilot/setup-jekyll-site-just-the-docs`)
4. Click **Save**

### 2. Update Configuration

Edit `_config.yml` and replace the placeholder values:

```yaml
url: https://USERNAME.github.io
baseurl: /REPOSITORY-NAME
```

Replace:
- `USERNAME` with your GitHub username (e.g., `markjayson13`)
- `REPOSITORY-NAME` with your repository name (e.g., `UNLVECON490Journal`)

Example:
```yaml
url: https://markjayson13.github.io
baseurl: /UNLVECON490Journal
```

Also update the GitHub link in the aux_links section:
```yaml
aux_links:
  "View on GitHub":
    - "https://github.com/USERNAME/REPOSITORY-NAME"
```

### 3. Wait for Deployment

After pushing changes:
1. Go to **Actions** tab in your repository
2. Wait for the "pages build and deployment" workflow to complete
3. Your site will be available at: `https://USERNAME.github.io/REPOSITORY-NAME/`

### 4. Add Papers

To add new papers:

1. Upload PDF files to `assets/papers/SEMESTER/`
2. Create a new markdown file in `issues/SEMESTER/` (e.g., `paper-003.md`)
3. Use the existing paper templates as a reference
4. Update the front matter with appropriate title, parent, and nav_order

## Local Development

To test the site locally:

```bash
# Install Jekyll and dependencies
gem install jekyll bundler

# Create Gemfile
cat > Gemfile << EOF
source 'https://rubygems.org'
gem "github-pages", group: :jekyll_plugins
gem "just-the-docs"
EOF

# Install dependencies
bundle install

# Serve the site locally
bundle exec jekyll serve

# Visit http://localhost:4000/REPOSITORY-NAME/
```

## Theme Documentation

This site uses the Just-the-Docs theme. For more information on customization options:
- [Just-the-Docs Documentation](https://just-the-docs.github.io/just-the-docs/)
- [Jekyll Documentation](https://jekyllrb.com/docs/)

## License

MIT License