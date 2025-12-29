---
layout: single
title: Browse issues by semester
permalink: /issues/
---
{% assign all_issues = site.pages | where: "is_issue", true %}
{% assign issues_with_dates = all_issues | where_exp: "issue", "issue.issue_date" | sort: "issue_date" | reverse %}
{% assign issues_without_dates = all_issues | where_exp: "issue", "issue.issue_date == nil" | sort: "issue_slug" | reverse %}
{% comment %}Newest issues prioritize explicit issue_date, then fall back to slug order.{% endcomment %}
{% assign issues = issues_with_dates | concat: issues_without_dates %}

<section class="container content-section page-header">
  <p class="eyebrow">Issues</p>
  <h1>Issues</h1>
  <p class="page-subtitle">Browse by semester</p>
  <p class="muted small">Newest releases appear first.</p>
</section>

<section class="container content-section">
  {% if issues and issues.size > 0 %}
    <div class="card-grid">
      {% for issue in issues %}
        {% assign issue_title = issue.issue_title | default: issue.title %}
        {% assign fallback_description = 'Capstone papers for ' | append: issue_title | append: '.' %}
        <article class="card issue-card">
          <p class="eyebrow">{{ issue_title | upcase }}</p>
          <h3><a href="{{ issue.url | relative_url }}">{{ issue_title }}</a></h3>
          <p class="muted">{{ issue.description | default: fallback_description }}</p>
          <div class="card-actions">
            <a class="btn btn-small btn-primary" href="{{ issue.url | relative_url }}">View Issue</a>
          </div>
        </article>
      {% endfor %}
    </div>
  {% else %}
    <div class="card">
      <p class="muted">No issues have been published yet.</p>
    </div>
  {% endif %}
</section>

<!-- issues-list:start -->
<!-- Managed by tools/new_issue.py; newest first -->
- [Fall 2025]({{ '/issues/2025-fall/' | relative_url }})
- [Spring 2024]({{ '/issues/2024-spring/' | relative_url }})
<!-- issues-list:end -->
