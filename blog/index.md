---
layout: page
title: Blog
permalink: /blog/
author_profile: false
---

{% assign posts = site.posts | sort: "date" | reverse %}

<p class="muted">Announcements and updates from the journal.</p>

{% if posts and posts.size > 0 %}
  <div class="card-grid">
    {% for post in posts %}
      <article class="card">
        <p class="eyebrow">{{ post.date | date: "%B %d, %Y" }}</p>
        <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
        {% if post.excerpt %}
          <p class="muted">{{ post.excerpt | strip_html | truncatewords: 34 }}</p>
        {% endif %}
      </article>
    {% endfor %}
  </div>
{% else %}
  <p class="muted">No posts yet.</p>
{% endif %}
