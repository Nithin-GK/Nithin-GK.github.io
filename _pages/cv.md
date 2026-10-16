---
layout: page
permalink: /cv/
title: CV
nav: true
nav_order: 3
cv_pdf: Nithin_CV.pdf
cv_version: 28cc69cdced9
description: Research experience, selected publications and education.
_styles: |
  .cv-actions { display: flex; flex-wrap: wrap; gap: 1rem 1.8rem; margin: 0 0 2rem; }
  .cv-preview figure { margin: 0 0 2rem; }
  .cv-preview a { display: block; border: 1px solid var(--global-divider-color); background: #fff; }
  .cv-preview img { display: block; width: 100%; height: auto; }
  .cv-preview figcaption { margin-top: .5rem; color: var(--global-text-color-light); font-size: .85rem; }
---

{% assign cv_url = page.cv_pdf | prepend: '/assets/pdf/' | relative_url | append: '?v=' | append: page.cv_version %}
<div class="cv-actions">
  <a href="{{ cv_url }}" target="_blank" rel="noopener noreferrer">Open CV PDF</a>
  <a href="{{ cv_url }}" download="Nithin_Gopalakrishnan_Nair_CV.pdf">Download CV</a>
</div>
<div class="cv-preview" aria-label="CV preview">
  <figure>
    <a href="{{ cv_url }}#page=1" target="_blank" rel="noopener noreferrer" aria-label="Open CV PDF at page 1">
      <img src="{{ '/assets/img/cv/nithin-cv-page-1.webp' | relative_url }}" alt="CV page 1: Nithin Gopalakrishnan Nair, research focus, research experience and research highlights." width="1275" height="1650" fetchpriority="high">
    </a>
    <figcaption>Page 1 of 2</figcaption>
  </figure>
  <figure>
    <a href="{{ cv_url }}#page=2" target="_blank" rel="noopener noreferrer" aria-label="Open CV PDF at page 2">
      <img src="{{ '/assets/img/cv/nithin-cv-page-2.webp' | relative_url }}" alt="CV page 2: selected publications, education, technical skills, mentoring and academic service." width="1275" height="1650" loading="lazy" decoding="async">
    </a>
    <figcaption>Page 2 of 2</figcaption>
  </figure>
</div>
