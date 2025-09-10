---
layout: page
permalink: /publications/
title: Publications
description: 
years: [2025, 2024,2023,2022,2021]
nav: true
nav_order: 1
---

A selection of my recent publications, organized by year. For the full list, see my [Google Scholar](https://scholar.google.com/citations?user=AkEXTbIAAAAJ&hl=en).

<style>
h2.year {
  border-bottom: 2px solid #ccc;
  padding-bottom: 0.25rem;
  margin-bottom: 1rem; /* adds space so the line doesn’t overlap the first publication */
}
</style>

<div class="publications mt-4">
{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  <div class="mb-4">
    {% bibliography -f papers -q @*[year={{y}}]* %}
  </div>
{% endfor %}
</div>
