---
title: "Projects"
permalink: /projects/
layout: single
---

<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">

{% assign sorted_projects = site.projects | sort: 'date' | reverse %}

{% if sorted_projects.size > 0 %}
<div class="project-grid">
  {% for project in sorted_projects %}
  <article class="project-card">
    <h3 class="project-title">{{ project.title }}</h3>

    {% if project.excerpt %}
    <p class="project-excerpt">{{ project.excerpt | strip_html | strip }}</p>
    {% endif %}

    {% if project.tags %}
    <div class="project-tags">
      {% for tag in project.tags %}
      <span class="project-tag">{{ tag }}</span>
      {% endfor %}
    </div>
    {% endif %}

    <p class="project-link-wrap">
      <a class="project-link" href="{{ project.url | relative_url }}">View</a>
    </p>
  </article>
  {% endfor %}
</div>
{% else %}
<p>Projects coming soon.</p>
{% endif %}
