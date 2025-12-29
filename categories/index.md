---
layout: single
title: Categories
permalink: /categories/
---

<section class="container-wide content-section page-header">
  <p class="page-subtitle">Choose a category to view all working papers tagged for that topic.</p>
</section>

<section class="container-wide content-section">
  <div class="grid-4 category-grid">
    {% for category in site.data.categories %}
      <a class="box" href="{{ '/categories/' | append: category.slug | append: '/' | relative_url }}">
        <h3>{{ category.name }}</h3>
        <p>View papers</p>
      </a>
    {% endfor %}
  </div>
</section>
