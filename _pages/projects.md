---
layout: project-showcase
title: Projects
permalink: /projects/
description: Generative vision, large-scale training and multimodal intelligence.
nav: true
nav_order: 2.5
navigation_group: projects
---

<header class="showcase-hero">
  <div class="showcase-container">
    <h1>Projects</h1>
    <p class="showcase-hero-lede">Selected work on large-scale training, generative models and multimodal learning.</p>
    <div class="showcase-hero-media" aria-label="Selected projects">
      <a href="{{ '/projects/novel-view-synthesis/' | relative_url }}"><div><img src="{{ site.data.project_showcase['novel-view-synthesis'].image | relative_url }}" alt="A Tok-D scene reconstruction from the Google project." fetchpriority="high"></div><span>Google: Novel view synthesis</span></a>
      <a href="{{ '/projects/control2control/' | relative_url }}"><div><img src="{{ site.data.project_showcase.control2control.hero_image | relative_url }}" alt="The edited corgi wearing sunglasses from the Control2Control research draft."></div><span>Adobe: Control2Control</span></a>
      <a href="{{ '/projects/nvidia-mesh-properties/' | relative_url }}"><div><img src="{{ site.data.project_showcase['nvidia-mesh-properties'].hero_image | relative_url }}" alt="Estimated materials for 3D furniture from the NVIDIA research draft."></div><span>NVIDIA: 3D asset understanding</span></a>
    </div>
    <div class="showcase-proof"><p><strong>18</strong> peer-reviewed publications</p><p>Research internships at <strong>Google · NVIDIA · Adobe · MERL</strong></p></div>
  </div>
</header>
<div class="showcase-container">
  <nav class="showcase-section-nav" aria-label="Project sections"><a href="#papers">Publications</a><a href="#internships">Internships</a></nav>
  <section class="showcase-section" id="papers" aria-labelledby="papers-heading">
    <div class="showcase-section-heading"><h2 id="papers-heading">Publications</h2></div>
    <div class="showcase-filters" role="group" aria-label="Filter research projects">
      <button type="button" data-project-filter="all" aria-pressed="true">All</button>
      <button type="button" data-project-filter="Training at scale" aria-pressed="false">Large-scale training</button>
      <button type="button" data-project-filter="Control and composition" aria-pressed="false">Control &amp; composition</button>
      <button type="button" data-project-filter="3D and visual understanding" aria-pressed="false">Visual understanding</button>
    </div>
    <p class="showcase-filter-status" role="status" data-filter-status>9 research projects</p>
    <div class="showcase-project-grid">
      {% include showcase-card.liquid key='novel-view-synthesis' featured=true %}
      {% include showcase-card.liquid key='gendeg' %}
      {% include showcase-card.liquid key='unite-and-conquer' %}
      {% include showcase-card.liquid key='steered-diffusion' %}
      {% include showcase-card.liquid key='maxfusion' %}
      {% include showcase-card.liquid key='scale-wise-var' %}
      {% include showcase-card.liquid key='briar' %}
      {% include showcase-card.liquid key='petalface' %}
      {% include showcase-card.liquid key='crowddiff' %}
    </div>
  </section>
  <section class="showcase-section showcase-industry" id="internships" aria-labelledby="internships-heading">
    <div class="showcase-section-heading"><h2 id="internships-heading">Internships</h2></div>
    <div class="showcase-project-grid">
      {% include showcase-card.liquid key='novel-view-synthesis' industry=true %}
      {% include showcase-card.liquid key='nvidia-mesh-properties' industry=true %}
      {% include showcase-card.liquid key='control2control' industry=true %}
      {% include showcase-card.liquid key='steered-diffusion' industry=true %}
    </div>
  </section>
  <section class="showcase-endnote"><div class="showcase-actions"><a class="showcase-button showcase-button-dark" href="{{ '/publications/' | relative_url }}">Publications</a><a class="showcase-button showcase-button-light" href="{{ '/cv/' | relative_url }}">CV</a></div>{% include showcase-credit.liquid %}</section>
</div>
