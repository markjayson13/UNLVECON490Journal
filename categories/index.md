---
layout: single
title: Categories
permalink: /categories/
---

<section class="container content-section page-header">
  <h1>Categories</h1>
  <p class="page-subtitle">Choose a category to view all working papers tagged for that topic.</p>
</section>

<section class="container content-section">
  <div class="grid-4">
    {% for category in site.data.categories %}
      <a class="box-card" href="{{ '/categories/' | append: category.slug | append: '/' | relative_url }}">
        <h3>{{ category.name }}</h3>
        <p class="muted small">Browse working papers in {{ category.name }}.</p>
      </a>
    {% endfor %}
  </div>
</section>
