layout: single
title: Browse papers by category
permalink: /categories/
---

<p class="eyebrow">Categories</p>
<p class="muted">Choose a category to view all working papers tagged for that topic.</p>

<div class="card-grid">
  {% for category in site.data.categories %}
    <article class="card">
      <h3><a href="{{ '/categories/' | append: category.slug | append: '/' | relative_url }}">{{ category.name }}</a></h3>
      <p class="muted small">Browse working papers in {{ category.name }}.</p>
    </article>
  {% endfor %}
</div>
