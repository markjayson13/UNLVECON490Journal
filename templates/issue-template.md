---
layout: default
title: {{ISSUE_TITLE}}
parent: Issues
nav_order: 1
has_children: true
is_issue: true
issue_slug: "{{ISSUE_SLUG}}"
issue_title: "{{ISSUE_TITLE}}"
issue_order: {{ISSUE_ORDER}}
permalink: /issues/{{ISSUE_SLUG}}/
description: Research from {{ISSUE_TITLE}}.
---

# {{ISSUE_TITLE}}

{% assign papers = site.pages | where: "issue_slug", page.issue_slug | where: "is_paper", true | sort: "nav_order" %}
{% if papers and papers.size > 0 %}
<ul>
  {% for paper in papers %}
  <li>
    <a href="{{ paper.url | relative_url }}">{{ paper.title }}</a><br />
    <small>Authors: {{ paper.authors | join: ", " }}</small><br />
    <small>{{ paper.abstract | strip_html | truncatewords: 32 }}</small>
  </li>
  {% endfor %}
</ul>
{% else %}
No papers have been added to this issue yet.
{% endif %}
