---
layout: page
permalink: /cv/
title: CV
nav: true
nav_order: 3
cv_pdf: Nithin_CV.pdf
cv_version: 28cc69cdced9
description: Research experience, selected publications and education.
---

<link rel="stylesheet" href="{{ '/assets/css/cv-page.css' | relative_url }}">
{% assign cv_url = page.cv_pdf | prepend: '/assets/pdf/' | relative_url | append: '?v=' | append: page.cv_version %}
<div class="cv-document">
  <div class="cv-actions">
    <a href="{{ cv_url }}" target="_blank" rel="noopener noreferrer">Open CV PDF</a>
    <a href="{{ cv_url }}" download="Nithin_Gopalakrishnan_Nair_CV.pdf">Download CV</a>
  </div>
  <div class="cv-contact" aria-label="Contact and profiles">
    <a href="mailto:iamnithingk@gmail.com">iamnithingk@gmail.com</a>
    <a href="tel:+16672129785">+1-667-212-9785</a>
    <a href="https://scholar.google.com/citations?user=_julgEYAAAAJ&amp;hl=en">Google Scholar</a>
    <a href="https://www.linkedin.com/in/nithin-gk-218174137/">LinkedIn</a>
    <a href="https://github.com/Nithin-GK">GitHub</a>
  </div>
  <nav class="cv-sections" aria-label="CV sections">
    <a href="#research-experience">Experience</a>
    <a href="#research-highlights">Research highlights</a>
    <a href="#selected-publications">Publications</a>
    <a href="#education">Education</a>
  </nav>
  <section class="cv-section" id="research-focus">
    <h2>Research Focus</h2>
    <p>Large-scale training of generative and multimodal models, with a focus on synthetic data, compositional generation, and 3D understanding.</p>
  </section>
  <section class="cv-section" id="research-experience">
    <h2>Research Experience</h2>
  <div class="cv-entry">
    <div class="cv-entry-heading">
      <h3>Apple – Research Engineer, Multimodal Agents</h3>
      <p class="cv-date">Jun 2025 – Present</p>
    </div>
    <ul>
      <li>Improved multimodal model performance on <strong>human interaction understanding</strong> tasks.</li>
      <li>Own <strong>agent development infrastructure</strong>, integrating simulation and evaluation workflows.</li>
      <li>Define evaluation protocols and scoring rubrics to assess multimodal agent behavior and guide model improvements.</li>
    </ul>
  </div>
  <div class="cv-entry">
    <div class="cv-entry-heading">
      <h3>Google – Google Beam / Project Starline</h3>
      <p class="cv-date">Dec 2024 – Mar 2025</p>
    </div>
    <ul>
      <li>Demonstrated the first successful training of transformer-based novel view synthesis models with <strong>diffusion-generated synthetic data</strong>.</li>
      <li>Introduced source/target token disentanglement to suppress synthetic-data artifacts and improve generalization to unseen scenes (ICCV 2025; patent application filed).</li>
    </ul>
  </div>
  <div class="cv-entry">
    <div class="cv-entry-heading">
      <h3>NVIDIA Research</h3>
      <p class="cv-date">Apr 2024 – Dec 2024</p>
    </div>
    <ul>
      <li>Developed the first foundation-model framework for <strong>physical-property assignment to 3D meshes</strong> through part segmentation and multimodal material identification.</li>
      <li>Co-inventor on <a href="https://patents.google.com/patent/US20260038283A1/en">U.S. Patent Application 19/024,394</a>, filed January 2025.</li>
    </ul>
  </div>
  <div class="cv-entry">
    <div class="cv-entry-heading">
      <h3>Adobe Inc.</h3>
      <p class="cv-date">May 2023 – Aug 2023</p>
    </div>
    <ul>
      <li>Built a training-free diffusion pipeline for interactive image editing.</li>
    </ul>
  </div>
  <div class="cv-entry">
    <div class="cv-entry-heading">
      <h3>Mitsubishi Electric Research Labs (MERL)</h3>
      <p class="cv-date">May 2022 – Aug 2022</p>
    </div>
    <ul>
      <li>Developed energy-based guidance for zero-shot conditional generation with pretrained diffusion models (Steered Diffusion, ICCV 2023).</li>
    </ul>
  </div>
  </section>
  <section class="cv-section" id="research-highlights">
    <h2>Research Highlights</h2>
  <div class="cv-entry">
    <div class="cv-entry-heading">
      <h3>Inference-Time Steering and Compositional Generation</h3>
      <p class="cv-date">2022 – 2024</p>
    </div>
    <ul>
      <li>Introduced <strong>Steered Diffusion</strong>, the first plug-and-play framework to unify image-to-image and label-conditioned generation through <strong>inference-time steering</strong>, without task-specific training (ICCV 2023).</li>
      <li>Pioneered <strong>compositional multimodal generation</strong> with <strong>Unite and Conquer</strong>, combining independently trained diffusion models at inference time without joint multimodal training (CVPR 2023).</li>
      <li>Extended pretrained text-to-image models to multiple simultaneous conditions through <strong>variance-guided feature fusion</strong> (<strong>MaxFusion</strong>, ECCV 2024).</li>
    </ul>
  </div>
  <div class="cv-entry">
    <div class="cv-entry-heading">
      <h3>Efficient Diffusion Steering (D3SG)</h3>
      <p class="cv-date">2026</p>
    </div>
    <ul>
      <li>Developed <strong>D3SG</strong> for guidance without U-Net backpropagation, combining noise-space and image-space gradients with adaptive scaling for linear and nonlinear conditions. <em>Research manuscript.</em></li>
    </ul>
  </div>
  <div class="cv-entry">
    <div class="cv-entry-heading">
      <h3>Synthetic Data for Generalizable Image Restoration (GenDeg)</h3>
      <p class="cv-date">2025</p>
    </div>
    <ul>
      <li>Introduced <strong>GenDeg</strong> to synthesize realistic image degradations from clean inputs, improving <strong>all-in-one restoration on unseen degradation patterns</strong> (CVPR 2025).</li>
      <li>Built <strong>GenDS (750K+ samples)</strong>, including <strong>550K+ synthetic image pairs</strong> spanning six degradation types.</li>
    </ul>
  </div>
  <div class="cv-entry">
    <div class="cv-entry-heading">
      <h3>IARPA BRIAR – Unconstrained Face Recognition</h3>
      <p class="cv-date">2021 – 2025</p>
    </div>
    <ul>
      <li>Achieved <strong>state-of-the-art results on five face-recognition benchmarks</strong> through large-scale pretraining, staged fine-tuning, and context-aware face crops (FG 2025; co-first author).</li>
      <li>Surpassed AdaFace by <strong>31.4 percentage points in BRIAR TAR at FAR 10<sup>−3</sup></strong>, with both models pretrained on WebFace12M; achieved <strong>81.38% Rank-1</strong> with WebFace42M.</li>
    </ul>
  </div>
  </section>
  <section class="cv-section" id="selected-publications">
    <h2>Selected Publications</h2>
    <p>18 peer-reviewed publications; full list on <a href="https://scholar.google.com/citations?user=_julgEYAAAAJ&amp;hl=en">Google Scholar</a>.</p>
    <ol class="cv-publications">
      <li>
        <div class="cv-entry-heading">
          <h3><a href="https://scaling3dnvs.github.io/">Scaling Transformer-Based Novel View Synthesis with Token Disentanglement and Synthetic Data</a></h3>
          <p class="cv-date">2025</p>
        </div>
        <p class="cv-authors"><strong>Nithin Gopalakrishnan Nair*</strong>, Srinivas Kaza*, Xuan Luo, Vishal M. Patel, Stephen Lombardi, Jungyeon Park</p>
        <p class="cv-venue">IEEE/CVF International Conference on Computer Vision (ICCV)</p>
      </li>
      <li>
        <div class="cv-entry-heading">
          <h3><a href="https://sudraj2002.github.io/gendegpage/">GenDeg: Diffusion-Based Degradation Synthesis for Generalizable All-in-One Image Restoration</a></h3>
          <p class="cv-date">2025</p>
        </div>
        <p class="cv-authors">Sudarshan Rajagopalan, <strong>Nithin Gopalakrishnan Nair</strong>, Jay N. Paranjape, Vishal M. Patel</p>
        <p class="cv-venue">IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)</p>
      </li>
      <li>
        <div class="cv-entry-heading">
          <h3><a href="https://arxiv.org/abs/2404.09977">MaxFusion: Plug&amp;Play Multi-Modal Generation in Text-to-Image Diffusion Models</a></h3>
          <p class="cv-date">2024</p>
        </div>
        <p class="cv-authors"><strong>Nithin Gopalakrishnan Nair</strong>, Jeya Maria Jose Valanarasu, Vishal M. Patel</p>
        <p class="cv-venue">European Conference on Computer Vision (ECCV)</p>
      </li>
      <li>
        <div class="cv-entry-heading">
          <h3><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Ranasinghe_CrowdDiff_Multi-hypothesis_Crowd_Density_Estimation_using_Diffusion_Models_CVPR_2024_paper.html">CrowdDiff: Multi-hypothesis Crowd Density Estimation using Diffusion Models</a></h3>
          <p class="cv-date">2024</p>
        </div>
        <p class="cv-authors">Yasiru Ranasinghe, <strong>Nithin Gopalakrishnan Nair</strong>, Wele Gedara Chaminda Bandara, Vishal M. Patel</p>
        <p class="cv-venue">IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)</p>
      </li>
      <li>
        <div class="cv-entry-heading">
          <h3><a href="https://openaccess.thecvf.com/content/ICCV2023/html/Nair_Steered_Diffusion_A_Generalized_Framework_for_Plug-and-Play_Conditional_Image_Synthesis_ICCV_2023_paper.html">Steered Diffusion: A Generalized Framework for Plug-and-Play Conditional Image Synthesis</a></h3>
          <p class="cv-date">2023</p>
        </div>
        <p class="cv-authors"><strong>Nithin Gopalakrishnan Nair</strong>, Anoop Cherian, Suhas Lohit, Ye Wang, Toshiaki Koike-Akino, Vishal M. Patel, Tim K. Marks</p>
        <p class="cv-venue">IEEE/CVF International Conference on Computer Vision (ICCV)</p>
      </li>
      <li>
        <div class="cv-entry-heading">
          <h3><a href="https://openaccess.thecvf.com/content/CVPR2023/papers/Nair_Unite_and_Conquer_Plug__Play_Multi-Modal_Synthesis_Using_Diffusion_CVPR_2023_paper.pdf">Unite and Conquer: Plug&amp;Play Multi-Modal Synthesis Using Diffusion Models</a></h3>
          <p class="cv-date">2023</p>
        </div>
        <p class="cv-authors"><strong>Nithin Gopalakrishnan Nair</strong>, Wele Gedara Chaminda Bandara, Vishal M. Patel</p>
        <p class="cv-venue">IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)</p>
      </li>
      <li>
        <div class="cv-entry-heading">
          <h3><a href="https://arxiv.org/abs/2412.07771">PETALface: Parameter Efficient Transfer Learning for Low-Resolution Face Recognition</a></h3>
          <p class="cv-date">2025</p>
        </div>
        <p class="cv-authors">Kartik Narayan, <strong>Nithin Gopalakrishnan Nair</strong>, Jennifer Xu, Rama Chellappa, Vishal M. Patel</p>
        <p class="cv-venue">IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), <strong>Oral</strong></p>
      </li>
    </ol>
    <p class="cv-note">* Equal contribution.</p>
  </section>
  <section class="cv-section" id="education">
    <h2>Education</h2>
  <div class="cv-entry">
    <div class="cv-entry-heading">
      <h3>Johns Hopkins University, Baltimore, USA</h3>
      <p class="cv-date">2021 – 2025</p>
    </div>
    <ul>
      <li>Ph.D. in Electrical and Computer Engineering, advised by Prof. Vishal M. Patel; GPA: <em>3.96/4.0</em>.</li>
    </ul>
  </div>
  <div class="cv-entry">
    <div class="cv-entry-heading">
      <h3>Indian Institute of Technology Madras, Chennai, India</h3>
      <p class="cv-date">2015 – 2020</p>
    </div>
    <ul>
      <li>B.Tech. and M.Tech. Dual Degree in Electrical Engineering; CGPA: <em>9.0/10.0</em>.</li>
    </ul>
  </div>
  </section>
  <section class="cv-section" id="technical-skills">
    <h2>Technical Skills</h2>
    <dl class="cv-skills">
      <dt>Languages</dt><dd>Python, C, C++, MATLAB</dd>
      <dt>Frameworks</dt><dd>PyTorch, JAX</dd>
      <dt>Generative Models</dt><dd>Diffusion models, autoregressive models, VAEs, GANs</dd>
    </dl>
  </section>
  <section class="cv-section" id="mentoring">
    <h2>Mentoring</h2>
    <p>Mentored five student researchers at Johns Hopkins University (2022–2025).</p>
  </section>
  <section class="cv-section" id="academic-service">
    <h2>Academic Service</h2>
    <p><strong>Reviewer:</strong> ICLR, NeurIPS, CVPR, ICCV, ECCV; IEEE TPAMI, TIP, and TMI.</p>
  </section>
</div>
