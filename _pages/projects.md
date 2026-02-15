---
title: "Projects"
permalink: /projects/
layout: single
---

{% assign sorted_projects = site.projects | sort: 'date' | reverse %}

{% if sorted_projects.size > 0 %}
{% for project in sorted_projects %}
- [{{ project.title }}]({{ project.url | relative_url }})
{% endfor %}
{% else %}
Projects coming soon.
{% endif %}
