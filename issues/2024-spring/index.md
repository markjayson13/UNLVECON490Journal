---
layout: single
title: Spring 2024
is_issue: true
issue_slug: "2024-spring"
issue_title: "Spring 2024"
issue_order: 2024.1
parent: Issues
nav_order: 2
has_children: true
permalink: /issues/2024-spring/
issue_id: 2024-spring
description: Student research from the Spring 2024 ECON 490 cohort.
---

# Spring 2024 Issue

This issue features research papers from the Spring 2024 semester of UNLV ECON 490.

## Papers in this Issue

Browse the papers below or use the navigation menu to explore individual submissions.

{% assign papers = site.pages | where: "issue_id", page.issue_id | where_exp: "page", "page.paper_id" | sort: "paper_id" %}
{% if papers and papers.size > 0 %}
<ul>
  {% for paper in papers %}
    <li>
      <a href="{{ paper.url | relative_url }}">{{ paper.title }}</a><br />
      <small>Authors: {{ paper.authors | join: ", " }}</small><br />
      {% if paper.abstract %}
        <small>{{ paper.abstract | strip_html | truncatewords: 30 }}</small>
      {% endif %}
    </li>
  {% endfor %}
</ul>
{% else %}
No papers have been added to this issue yet. Use the submission instructions to contribute.
{% endif %}
