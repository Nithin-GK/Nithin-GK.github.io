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
    <p class="showcase-eyebrow">Nithin Gopalakrishnan Nair · Selected research</p>
    <h1>Generative vision.<br><span>Built to scale.</span></h1>
    <p class="showcase-hero-lede">I build generative and multimodal models, with a focus on large-scale training, synthetic data and 3D understanding.</p>
    <div class="showcase-actions"><a class="showcase-button showcase-button-primary" href="#papers">Explore the research</a><a class="showcase-button showcase-button-outline" href="#internships">Internship work</a></div>
    <div class="showcase-hero-media" aria-label="Research in action">
      <a href="{{ '/projects/novel-view-synthesis/' | relative_url }}"><div><img src="{{ site.data.project_showcase['novel-view-synthesis'].image | relative_url }}" alt="Published reconstruction examples from the Google novel view synthesis project." fetchpriority="high"></div><span>Learning from generated views</span></a>
      <a href="{{ '/projects/control2control/' | relative_url }}"><div><img src="{{ site.data.project_showcase.control2control.image | relative_url }}" alt="A sketch-guided corgi image edit from the Control2Control research draft."></div><span>Controlling what changes</span></a>
      <a href="{{ '/projects/nvidia-mesh-properties/' | relative_url }}"><div><img src="{{ site.data.project_showcase['nvidia-mesh-properties'].image | relative_url }}" alt="Colored 3D part segments and estimated materials from the NVIDIA research draft."></div><span>Understanding 3D materials</span></a>
    </div>
    <div class="showcase-proof"><p><strong>18</strong> peer-reviewed publications</p><p>Research internships at <strong>Google · NVIDIA · Adobe · MERL</strong></p></div>
  </div>
</header>
<div class="showcase-container">
  <nav class="showcase-section-nav" aria-label="Project sections"><a href="#papers">Papers</a><a href="#internships">Internship work</a></nav>
  <section class="showcase-section" id="papers" aria-labelledby="papers-heading">
    <div class="showcase-section-heading"><div><p class="showcase-eyebrow">Ideas, methods and evidence</p><h2 id="papers-heading">Research in action.</h2></div><p>Explore the question, the approach and the result behind each project.</p></div>
    <div class="showcase-filters" role="group" aria-label="Filter research projects">
      <button type="button" data-project-filter="all" aria-pressed="true">All research</button>
      <button type="button" data-project-filter="Training at scale" aria-pressed="false">Training at scale</button>
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
    <div class="showcase-section-heading"><div><p class="showcase-eyebrow">Research in industry</p><h2 id="internships-heading">Ideas put to work.</h2></div><p>Projects from research internships at Google, NVIDIA, Adobe and MERL.</p></div>
    <div class="showcase-project-grid">
      {% include showcase-card.liquid key='novel-view-synthesis' industry=true %}
      {% include showcase-card.liquid key='nvidia-mesh-properties' industry=true %}
      {% include showcase-card.liquid key='control2control' industry=true %}
      {% include showcase-card.liquid key='steered-diffusion' industry=true %}
    </div>
  </section>
  <section class="showcase-endnote"><h2>Keep exploring.</h2><p>Find the complete publication list and my academic CV.</p><div class="showcase-actions"><a class="showcase-button showcase-button-dark" href="{{ '/publications/' | relative_url }}">Publications</a><a class="showcase-button showcase-button-light" href="{{ '/cv/' | relative_url }}">CV</a></div></section>
</div>
