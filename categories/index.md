layout: single
title: Browse papers by category
permalink: /categories/
---

<section class="container content-section page-header">
  <p class="eyebrow">Categories</p>
  <h1>Categories</h1>
  <p class="page-subtitle">Choose a category to view all working papers tagged for that topic.</p>
</section>

<section class="container content-section">
  <div class="card-grid">
    {% for category in site.data.categories %}
      <article class="card link-card">
        <p class="eyebrow">Category</p>
        <h3><a href="{{ '/categories/' | append: category.slug | append: '/' | relative_url }}">{{ category.name }}</a></h3>
        <p class="muted small">Browse working papers in {{ category.name }}.</p>
        <div class="card-actions">
          <a class="btn btn-small btn-primary" href="{{ '/categories/' | append: category.slug | append: '/' | relative_url }}">View category</a>
        </div>
      </article>
    {% endfor %}
  </div>
</section>
