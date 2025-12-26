---
layout: default
title: Issues
nav_order: 2
has_children: true
permalink: /issues/
---

# Issues

Browse published semesters. Newest issues appear first.

{% assign issue_pages = site.pages | where: "is_issue", true | sort: "issue_order" | reverse %}
{% if issue_pages and issue_pages.size > 0 %}
<ul>
  {% for issue in issue_pages %}
  <li>
    <a href="{{ issue.url | relative_url }}">{{ issue.issue_title | default: issue.title }}</a>
    {% if issue.description %}
      — {{ issue.description }}
    {% endif %}
  </li>
  {% endfor %}
</ul>
{% else %}
No issues published yet.
{% endif %}

<!-- issues-list:start -->
- [Fall 2025]({{ "/issues/2025-fall/" | relative_url }})
<!-- issues-list:end -->
