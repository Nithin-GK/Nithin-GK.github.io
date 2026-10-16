---
layout: page
title: Research overview
permalink: /projects/research-overview/
description: Large-scale training and multimodal vision.
nav: false
---

<link rel="stylesheet" href="{{ '/assets/css/research-projects.css' | relative_url }}">
<article class="research-project-page">
  <a class="project-back" href="{{ '/projects/' | relative_url }}">Back to projects</a>
  {% assign overview_slides = "1,2,3,4,5,7,8,9,10,11,14,16" | split: ',' %}
  {% include research-slides.liquid slides=overview_slides label="Research overview presentation" %}
  <div class="project-links">
    <a href="{{ '/assets/slides/research-overview.pdf' | relative_url }}" download>Download PDF</a>
    <a href="{{ '/assets/slides/research-overview.pptx' | relative_url }}" download>Download PowerPoint</a>
  </div>
</article>
<script src="{{ '/assets/js/research-slides.js' | relative_url }}" defer></script>
