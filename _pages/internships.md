---
layout: page
title: Internships
permalink: /internships/
description: Research internships at Google, NVIDIA, Adobe and MERL.
nav: true
nav_order: 1.5
navigation_group: internships
---

<link rel="stylesheet" href="{{ '/assets/css/research-projects.css' | relative_url }}">
<div class="research-projects">
  <p class="research-intro">Industry research in novel view synthesis, physical properties of 3D assets and diffusion models.</p>
  <div class="project-list">
    {% assign industry_projects = site.projects | where: 'project_group', 'industry' | sort: 'industry_order' %}
    {% for item in industry_projects %}
      {% assign project = site.data.research_projects[item.project_key] %}
      {% include research-project-summary.liquid item=item project=project industry=true %}
    {% endfor %}
  </div>
</div>
