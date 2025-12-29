---
layout: single
title: Papers
permalink: /papers/
---

{% assign papers = site.pages | where_exp: "page", "page.paper_id" %}
{% assign issues = site.pages | where: "is_issue", true | sort: "issue_order" | reverse %}

{% if papers and papers.size > 0 %}
  {% for issue in issues %}
    {% assign issue_papers = papers | where: "issue_id", issue.issue_id | sort: "publication_date" | reverse %}
    {% if issue_papers and issue_papers.size > 0 %}
      <h2 id="{{ issue.issue_id | slugify }}">{{ issue.title }}</h2>
      <div class="card-grid featured-papers">
        {% for paper in issue_papers %}
          {% assign clean_title = paper.title %}
          {% if paper.title contains ":" %}
            {% assign clean_title = paper.title | split: ":" | last | strip %}
          {% endif %}
          {% assign pdf_path = paper.pdf_path | default: paper.pdf %}
          <article class="summary-card paper-card">
            <div class="paper-meta">
              {% if paper.publication_date %}
                <span class="pill">{{ paper.publication_date }}</span>
              {% endif %}
              <span class="pill">{{ issue.title }}</span>
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
              {% if pdf_path %}
                <a class="btn btn--primary" href="{{ pdf_path | relative_url }}">Download PDF</a>
              {% endif %}
            </div>
          </article>
        {% endfor %}
      </div>
    {% endif %}
  {% endfor %}
{% else %}
<p>No papers available yet.</p>
{% endif %}
