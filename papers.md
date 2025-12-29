---
layout: single
title: Papers
permalink: /papers/
---
{% assign papers = site.pages | where: "is_paper", true %}
{% assign issues = site.pages | where: "is_issue", true | sort: "issue_order" | reverse %}

<div class="page__content">
  <p class="eyebrow">All Papers</p>
  <h1>Papers by issue</h1>
  <p class="muted">Browse every paper organized by semester release.</p>

  {% if papers and papers.size > 0 %}
    {% for issue in issues %}
      {% assign issue_papers = papers | where: "issue_slug", issue.issue_slug | sort: "publication_date" | reverse %}
      {% if issue_papers and issue_papers.size > 0 %}
        <h2 id="{{ issue.issue_slug | slugify }}">{{ issue.title }}</h2>
        <div class="card-grid">
          {% for paper in issue_papers %}
            {% assign clean_title = paper.title %}
            {% if paper.title contains ":" %}
              {% assign title_parts = paper.title | split: ":" %}
              {% if title_parts.first contains "Paper" %}
                {% assign clean_title = title_parts.last | strip %}
              {% endif %}
            {% endif %}
            {% assign pdf_path = paper.pdf_path | default: paper.pdf %}
            <article class="card paper-card">
              <div class="paper-meta">
                {% if paper.publication_date %}
                  <span class="pill">{{ paper.publication_date }}</span>
                {% endif %}
                <span class="pill light">{{ issue.title }}</span>
              </div>
              <h3><a href="{{ paper.url | relative_url }}">{{ clean_title }}</a></h3>
              {% if paper.authors %}
                <p class="muted small">By {{ paper.authors | join: ", " }}</p>
              {% endif %}
              {% if paper.abstract %}
                <p class="muted">{{ paper.abstract | strip_html | truncatewords: 32 }}</p>
              {% endif %}
              <div class="card-actions">
                <a class="btn btn-small" href="{{ paper.url | relative_url }}">Read abstract</a>
                {% if pdf_path %}
                  <a class="btn btn-small btn-primary" href="{{ pdf_path | relative_url }}">Download PDF</a>
                {% endif %}
              </div>
            </article>
          {% endfor %}
        </div>
      {% endif %}
    {% endfor %}
  {% else %}
    <p class="muted">No papers available yet.</p>
  {% endif %}
</div>
