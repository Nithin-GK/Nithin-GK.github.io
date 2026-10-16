---
layout: page
title: Papers
permalink: /projects/
description: Generative modeling and computer vision.
nav: true
nav_order: 2
navigation_group: papers
---

<link rel="stylesheet" href="{{ '/assets/css/research-projects.css' | relative_url }}">
<div class="research-projects">
  <p class="research-intro">Selected papers and preprints on generative models, multimodal learning and 3D vision, with visual summaries, slides and technical details.</p>
  <div class="project-links paper-list-links">
    <a href="{{ '/publications/' | relative_url }}">Full publication list</a>
    <a href="{{ '/internships/' | relative_url }}">Internship work</a>
  </div>
  <section class="research-overview research-overview-link" aria-labelledby="research-overview-title">
    <h2 id="research-overview-title">Research overview</h2>
    <p>A visual introduction to my work on large-scale training and multimodal vision.</p>
    <div class="project-links">
      <a href="{{ '/projects/research-overview/' | relative_url }}">Browse presentation</a>
      <a href="{{ '/assets/slides/research-overview.pptx' | relative_url }}" download>Download PowerPoint</a>
    </div>
  </section>
  <div class="project-list">
    {% assign projects = site.projects | where: 'research_project', true | sort: 'importance' %}
    {% for item in projects %}
      {% assign project = site.data.research_projects[item.project_key] %}
      {% if project.navigation_group == 'papers' %}
        {% include research-project-summary.liquid item=item project=project %}
      {% endif %}
    {% endfor %}
  </div>
</div>
