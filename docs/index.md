---
layout: page
title: Home Page
description: ""
---

<h2>Welcome</h2>
<p>This page is auto-generated, and is sorted alphabetically by "Title"</p>

{% assign cur_pages = site.pages | sort: 'title' %}

{%- for entry in cur_pages %}
{%- if entry.layout == "page" and entry.url != "/" %}
  <h3><a href="{{ site.url }}{{ entry.url }}">►&nbsp;{{ entry.title }}</a></h3>
  <p>{{ entry.description }}</p>
{%- endif %}
{%- endfor %}
