---
layout: single
title: Fall 2025
is_issue: true
issue_slug: "2025-fall"
issue_title: "Fall 2025"
issue_order: 2025.2
permalink: /issues/2025-fall/
description: Student research from the Fall 2025 ECON 490 capstone cohort.
classes: wide
---

## Papers in this issue

{% assign papers = site.pages | where: "issue_slug", page.issue_slug | where: "is_paper", true | sort: "publication_date" | reverse %}
{% if papers and papers.size > 0 %}
<div class="card-grid featured-papers">
  {% for paper in papers %}
    {% assign clean_title = paper.title %}
    {% if paper.title contains ":" %}
      {% assign clean_title = paper.title | split: ":" | last | strip %}
    {% endif %}
    <article class="summary-card paper-card">
      <div class="paper-meta">
        {% if paper.publication_date %}
          <span class="pill">{{ paper.publication_date }}</span>
        {% endif %}
        <span class="pill">{{ page.issue_title }}</span>
      </div>
      <h3><a href="{{ paper.url | relative_url }}">{{ clean_title }}</a></h3>
      {% if paper.authors %}
        <p class="authors">By {{ paper.authors | join: ", " }}</p>
      {% endif %}
      {% if paper.abstract %}
        <p>{{ paper.abstract | strip_html | truncatewords: 36 }}</p>
      {% endif %}
      <div class="paper-actions">
        <a class="btn" href="{{ paper.url | relative_url }}">Read abstract</a>
        {% if paper.pdf_path %}
          <a class="btn btn--primary" href="{{ paper.pdf_path | relative_url }}">Download PDF</a>
        {% endif %}
      </div>
    </article>
  {% endfor %}
</div>
{% else %}
No papers have been added to this issue yet.
{% endif %}
