---
title: "Medium Writings"
permalink: /blog/medium/
layout: single
author_profile: true
---

Latest writings synced from Medium.

{% assign medium_posts = site.posts | where_exp: "post", "post.categories contains 'medium'" %}
{% for post in medium_posts %}
### [{{ post.title }}]({{ post.link | default: post.url }})

{{ post.excerpt | strip_html | truncate: 220 }}

*{{ post.date | date: "%B %-d, %Y" }}*  
[Read on Medium]({{ post.link | default: post.url }})

{% endfor %}
