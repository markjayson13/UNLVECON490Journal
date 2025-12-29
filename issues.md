---
layout: single
title: Browse issues by semester
permalink: /issues/
---
{% assign issues = site.pages | where: "is_issue", true | sort: "issue_order" | reverse %}

<p class="eyebrow">Issues</p>
<p class="muted">Newest releases appear first.</p>

{% if issues and issues.size > 0 %}
  <div class="card-grid">
    {% for issue in issues %}
      <article class="card">
        <p class="eyebrow">{{ issue.issue_title | default: issue.title }}</p>
        <h3><a href="{{ issue.url | relative_url }}">{{ issue.title }}</a></h3>
        {% if issue.description %}
          <p class="muted">{{ issue.description }}</p>
        {% endif %}
        <div class="card-actions">
          <a class="btn btn-small btn-primary" href="{{ issue.url | relative_url }}">View Issue</a>
        </div>
      </article>
    {% endfor %}
  </div>
{% else %}
  <p class="muted">No issues have been published yet.</p>
{% endif %}

<!-- issues-list:start -->
<!-- Managed by tools/new_issue.py; newest first -->
- [Fall 2025]({{ '/issues/2025-fall/' | relative_url }})
- [Spring 2024]({{ '/issues/2024-spring/' | relative_url }})
<!-- issues-list:end -->
