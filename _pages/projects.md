---
layout: page
title: Projects
permalink: /projects/
description: Selected papers and internship research.
nav: true
nav_order: 2.5
navigation_group: projects
---

<link rel="stylesheet" href="{{ '/assets/css/research-projects.css' | relative_url }}">
<div class="research-projects">
  <p class="research-intro">Research in generative models, multimodal learning and 3D vision, with paper walkthroughs and work from my research internships.</p>
  <nav class="project-section-links" aria-label="Project sections">
    <a href="#papers">Papers</a>
    <a href="#internships">Internship work</a>
  </nav>
  <section class="project-section" id="papers" aria-labelledby="papers-heading">
    <h2 id="papers-heading">Papers</h2>
    <p class="project-section-intro">Selected papers and preprints with visual summaries, slides and technical details.</p>
    <div class="project-list">
      {% assign projects = site.projects | where: 'research_project', true | sort: 'importance' %}
      {% for item in projects %}
        {% assign project = site.data.research_projects[item.project_key] %}
        {% if project.navigation_group == 'papers' %}
          {% include research-project-summary.liquid item=item project=project sectioned=true %}
        {% endif %}
      {% endfor %}
    </div>
  </section>
  <section class="project-section" id="internships" aria-labelledby="internships-heading">
    <h2 id="internships-heading">Internship work</h2>
    <p class="project-section-intro">Research at Google, NVIDIA, Adobe and MERL.</p>
    <div class="project-list">
      {% assign industry_projects = site.projects | where: 'project_group', 'industry' | sort: 'industry_order' %}
      {% for item in industry_projects %}
        {% assign project = site.data.research_projects[item.project_key] %}
        {% include research-project-summary.liquid item=item project=project industry=true sectioned=true %}
      {% endfor %}
    </div>
  </section>
</div>
