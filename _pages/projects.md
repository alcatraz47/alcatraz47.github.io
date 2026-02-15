---
title: "Projects"
permalink: /projects/
layout: single
---

{% assign sorted_projects = site.projects | sort: 'date' | reverse %}

{% if sorted_projects.size > 0 %}
  <div class="project-grid">
    {% for project in sorted_projects %}
      <article class="project-card">
        <h2><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h2>
        {% if project.excerpt %}
          <p>{{ project.excerpt | markdownify | strip_html }}</p>
        {% endif %}
        {% if project.tags %}
          <p><strong>Tags:</strong> {{ project.tags | join: ", " }}</p>
        {% endif %}
        <p><a href="{{ project.url | relative_url }}">View project →</a></p>
      </article>
    {% endfor %}
  </div>
{% else %}
  <p>Projects will be added soon.</p>
{% endif %}
