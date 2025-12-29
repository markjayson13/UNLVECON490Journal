---
layout: single
title: Papers
permalink: /papers/
---

{% assign papers = site.pages | where: "is_paper", true %}
{% assign papers_with_pub = papers | where_exp: "paper", "paper.publication_date" | sort: "publication_date" | reverse %}
{% assign papers_without_pub = papers | where_exp: "paper", "paper.publication_date == nil" | sort: "date" | reverse %}
{% assign all_papers = papers_with_pub | concat: papers_without_pub %}

{% if all_papers and all_papers.size > 0 %}
<div class="card-grid featured-papers">
  {% for paper in all_papers %}
    {% assign clean_title = paper.title %}
    {% if paper.title contains ":" %}
      {% assign clean_title = paper.title | split: ":" | last | strip %}
    {% endif %}
    <article class="summary-card paper-card">
      <div class="paper-meta">
        {% if paper.publication_date %}
          <span class="pill">{{ paper.publication_date }}</span>
        {% endif %}
        {% if paper.issue_title %}
          <span class="pill">{{ paper.issue_title }}</span>
        {% endif %}
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
<p>No papers available yet.</p>
{% endif %}
