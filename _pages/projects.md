---
layout: page
title: Projects
permalink: /projects/
description: Research in generative modeling, synthetic data and 3D vision.
nav: true
nav_order: 2.5
---

<link rel="stylesheet" href="{{ '/assets/css/research-projects.css' | relative_url }}">
<div class="research-projects">
  <p class="research-intro">My work spans large-scale generative modeling, multimodal understanding and 3D vision, across industry research and academic projects.</p>
  <nav class="project-section-links" aria-label="Project sections">
    <a href="#internships">Industry &amp; internships</a>
    <a href="#research">Research projects</a>
  </nav>
  <section class="research-overview research-overview-link" aria-labelledby="research-overview-title">
    <h2 id="research-overview-title">Research overview</h2>
    <p>A visual introduction to my work on large-scale training and multimodal vision.</p>
    <div class="project-links">
      <a href="{{ '/projects/research-overview/' | relative_url }}">Browse presentation</a>
      <a href="{{ '/assets/slides/research-overview.pptx' | relative_url }}" download>Download PowerPoint</a>
    </div>
  </section>
  <section id="internships" class="project-section" aria-labelledby="industry-title">
    <h2 id="industry-title">Industry &amp; internship work</h2>
    <p class="project-section-intro">Research internships at Google, NVIDIA, Adobe and MERL.</p>
    <div class="project-list">
      {% assign industry_projects = site.projects | where: 'project_group', 'industry' | sort: 'industry_order' %}
      {% for item in industry_projects %}
        {% assign project = site.data.research_projects[item.project_key] %}
        {% include research-project-summary.liquid item=item project=project industry=true %}
      {% endfor %}
    </div>
  </section>
  <section id="research" class="project-section" aria-labelledby="research-title">
    <h2 id="research-title">Research projects</h2>
    <div class="project-list">
      {% assign projects = site.projects | where: 'research_project', true | sort: 'importance' %}
      {% for item in projects %}
        {% unless item.project_group == 'industry' %}
          {% assign project = site.data.research_projects[item.project_key] %}
          {% include research-project-summary.liquid item=item project=project %}
        {% endunless %}
      {% endfor %}
    </div>
  </section>
</div>
