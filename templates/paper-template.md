---
layout: default
title: "Paper {{PAPER_NUMBER}}: {{PAPER_TITLE}}"
parent: {{ISSUE_TITLE}}
grand_parent: Issues
nav_order: {{PAPER_NUMBER_INT}}
is_paper: true
paper_id: "{{ISSUE_SLUG}}-{{PAPER_NUMBER}}"
issue_slug: "{{ISSUE_SLUG}}"
issue_title: "{{ISSUE_TITLE}}"
publication_date: "{{PUBLICATION_DATE}}"
authors:
{{AUTHORS_BLOCK}}
keywords:
{{KEYWORDS_BLOCK}}
abstract: |
  {{ABSTRACT_TEXT}}
pdf_path: "/assets/papers/{{ISSUE_SLUG}}/paper-{{PAPER_NUMBER}}.pdf"
---

# {{ '{{' }} page.title {{ '}}' }}

**Authors:** {{ '{{' }} page.authors | join: ", " {{ '}}' }}  
**Publication date:** {{ '{{' }} page.publication_date {{ '}}' }}  
**Issue:** {{ '{{' }} page.issue_title {{ '}}' }}

## Abstract

{{ '{{' }} page.abstract {{ '}}' }}

## Download

[Download PDF]({{ '{{' }} page.pdf_path | relative_url {{ '}}' }}){: .btn .btn-primary }

## Keywords

{{ '{{' }} page.keywords | join: ", " {{ '}}' }}
