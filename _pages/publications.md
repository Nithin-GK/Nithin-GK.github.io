---
layout: page
permalink: /publications/
title: Publications
description: 
years: [2025,2024,2023,2022,2021]
nav: true
nav_order: 1
---

## Publications

A selection of my recent publications, organized by year. For the full list, see my [Google Scholar](https://scholar.google.com/citations?user=AkEXTbIAAAAJ&hl=en).

<div class="publications mt-4">
{%- for y in page.years %}
  <h2 class="year border-bottom pb-2 mt-4">{{y}}</h2>
  <div class="mb-4">
    {% bibliography -f papers -q @*[year={{y}}]* %}
  </div>
{% endfor %}
</div>
