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
  <p class="research-intro">I build generative models that learn from synthetic data and adapt to new conditions. Explore the projects below through visual summaries, presentation slides and the original papers.</p>
  <section class="research-overview research-overview-link" aria-labelledby="research-overview-title">
    <h2 id="research-overview-title">Research overview</h2>
    <p>A visual introduction to my work on large-scale training and multimodal vision.</p>
    <div class="project-links">
      <a href="{{ '/projects/research-overview/' | relative_url }}">Browse presentation</a>
      <a href="{{ '/assets/slides/research-overview.pdf' | relative_url }}" download>Download PDF</a>
      <a href="{{ '/assets/slides/research-overview.pptx' | relative_url }}" download>Download PowerPoint</a>
    </div>
  </section>
  <div class="project-list">
    {% assign projects = site.projects | where: 'research_project', true | sort: 'importance' %}
    {% for item in projects %}
      {% assign project = site.data.research_projects[item.project_key] %}
      <article class="project-entry{% unless project.image %} project-entry--text{% endunless %}">
        {% if project.image %}
        <a class="project-entry-image" href="{{ item.url | relative_url }}" aria-label="View {{ project.title | escape }}">
          <img src="{{ project.image | relative_url }}" alt="{{ project.image_alt | escape }}" width="800" height="500" loading="lazy" decoding="async">
        </a>
        {% endif %}
        <div>
          <p class="project-meta">{{ project.venue }} {{ project.year }}</p>
          <h3><a href="{{ item.url | relative_url }}">{{ project.title }}</a></h3>
          <p>{{ project.description }}</p>
          <div class="project-links">
            <a href="{{ item.url | relative_url }}">{{ project.gallery_label | default: 'View project and slides' }}</a>
            {% if project.links.size > 0 %}
            <a href="{{ project.links[0].url }}" target="_blank" rel="noopener noreferrer">{{ project.links[0].label }}</a>
            {% endif %}
          </div>
        </div>
      </article>
    {% endfor %}
  </div>
</div>
