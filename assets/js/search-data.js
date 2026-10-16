// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "About",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-internships",
          title: "Internships",
          description: "Research internships at Google, NVIDIA, Adobe and MERL.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/internships/";
          },
        },{id: "nav-publications",
          title: "Publications",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-projects",
          title: "Projects",
          description: "Generative modeling and computer vision.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-cv",
          title: "CV",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "post-google-gemini-updates-flash-1-5-gemma-2-and-project-astra",
        
          title: 'Google Gemini updates: Flash 1.5, Gemma 2 and Project Astra <svg width="1.2rem" height="1.2rem" top=".5rem" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><path d="M17 13.5v6H5v-12h6m3-3h6v6m0-6-9 9" class="icon_svg-stroke" stroke="#999" stroke-width="1.5" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"></path></svg>',
        
        description: "We’re sharing updates across our Gemini family of models and a glimpse of Project Astra, our vision for the future of AI assistants.",
        section: "Posts",
        handler: () => {
          
            window.open("https://blog.google/technology/ai/google-gemini-update-flash-ai-assistant-io-2024/", "_blank");
          
        },
      },{id: "post-displaying-external-posts-on-your-al-folio-blog",
        
          title: 'Displaying External Posts on Your al-folio Blog <svg width="1.2rem" height="1.2rem" top=".5rem" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><path d="M17 13.5v6H5v-12h6m3-3h6v6m0-6-9 9" class="icon_svg-stroke" stroke="#999" stroke-width="1.5" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"></path></svg>',
        
        description: "",
        section: "Posts",
        handler: () => {
          
            window.open("https://medium.com/@al-folio/displaying-external-posts-on-your-al-folio-blog-b60a1d241a0a?source=rss-17feae71c3c4------2", "_blank");
          
        },
      },{id: "books-the-godfather",
          title: 'The Godfather',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/the_godfather/";
            },},{id: "news-i-started-my-summer-internship-at-mitsubishi-electric-research-labs-focusing-on-diffusion-based-face-synthesis",
          title: 'I started my summer internship at Mitsubishi Electric Research Labs, focusing on diffusion-based...',
          description: "",
          section: "News",},{id: "news-two-of-our-papers-were-accepted-at-icip-2023",
          title: 'Two of our papers were accepted at ICIP 2023.',
          description: "",
          section: "News",},{id: "news-our-work-t2v-ddpm-was-accepted-at-ieee-fg-2023-t2v-ddpm-achieves-state-of-the-art-performance-in-thermal-to-visible-face-translation",
          title: 'Our work T2V-DDPM was accepted at IEEE FG 2023. T2V-DDPM achieves state-of-the-art performance...',
          description: "",
          section: "News",},{id: "news-our-work-at-ddpm-was-accepted-at-wacv-2023-at-ddpm-achieves-state-of-the-art-performance-in-mitigating-atmospheric-turbulence-effects",
          title: 'Our work AT-DDPM was accepted at WACV 2023. AT-DDPM achieves state-of-the-art performance in...',
          description: "",
          section: "News",},{id: "news-our-work-unite-and-conquer-was-accepted-at-cvpr-2023-this-work-enables-plug-and-play-multimodal-generation-using-diffusion-models",
          title: 'Our work Unite and Conquer was accepted at CVPR 2023. This work enables...',
          description: "",
          section: "News",},{id: "news-i-started-my-summer-internship-at-adobe-seattle-working-on-diffusion-based-image-editing",
          title: 'I started my summer internship at Adobe Seattle, working on diffusion-based image editing....',
          description: "",
          section: "News",},{id: "news-our-work-steered-diffusion-was-accepted-at-iccv-2023-steered-diffusion-enables-zero-shot-conditional-sampling-using-pre-trained-unconditional-diffusion-models",
          title: 'Our work Steered Diffusion was accepted at ICCV 2023. Steered Diffusion enables zero-shot...',
          description: "",
          section: "News",},{id: "news-i-started-my-summer-internship-at-nvidia-research",
          title: 'I started my summer internship at Nvidia Research.',
          description: "",
          section: "News",},{id: "news-our-work-maxfusion-was-accepted-at-eccv-2024-maxfusion-enables-training-free-multimodal-spatial-conditioning-in-text-to-image-diffusion-models",
          title: 'Our work MaxFusion was accepted at ECCV 2024. MaxFusion enables training-free multimodal spatial...',
          description: "",
          section: "News",},{id: "news-i-started-a-new-position-as-a-research-intern-at-google",
          title: 'I started a new position as a Research Intern at Google.',
          description: "",
          section: "News",},{id: "news-my-internship-work-at-google-scaling-transformer-based-novel-view-synthesis-models-with-token-disentanglement-and-synthetic-data-was-accepted-at-iccv-2025-our-work-scales-up-3d-reconstruction-using-synthetic-data-and-achieves-state-of-the-art-results",
          title: 'My internship work at Google, Scaling Transformer-Based Novel View Synthesis Models with Token...',
          description: "",
          section: "News",},{id: "projects-unconstrained-face-recognition",
          title: 'Unconstrained face recognition',
          description: "Large-scale pretraining and staged adaptation improve face recognition under long range, low resolution and other unconstrained conditions.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/briar/";
            },},{id: "projects-control2control",
          title: 'Control2Control',
          description: "Revitalized attention transfer for consistent diffusion image editing.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/control2control/";
            },},{id: "projects-crowddiff",
          title: 'CrowdDiff',
          description: "Conditional diffusion predicts detailed crowd density maps, with multiple hypotheses to improve counting.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/crowddiff/";
            },},{id: "projects-gendeg",
          title: 'GenDeg',
          description: "Diffusion-generated degradations improve restoration on patterns that the model has not seen during training.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/gendeg/";
            },},{id: "projects-maxfusion",
          title: 'MaxFusion',
          description: "Variance-guided feature fusion combines off-the-shelf controllers for generation with multiple spatial conditions.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/maxfusion/";
            },},{id: "projects-novel-view-synthesis-at-scale",
          title: 'Novel view synthesis at scale',
          description: "Token disentanglement lets transformer models learn from diffusion-generated views and generalize to unseen scenes.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/novel-view-synthesis/";
            },},{id: "projects-physical-property-assignment-to-3d-meshes",
          title: 'Physical-property assignment to 3D meshes',
          description: "Foundation models for part segmentation and material identification of 3D assets.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/nvidia-mesh-properties/";
            },},{id: "projects-petalface",
          title: 'PETALface',
          description: "Quality-weighted low-rank adapters improve low-resolution recognition while retaining a strong pretrained backbone.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/petalface/";
            },},{id: "projects-scale-wise-var",
          title: 'Scale-Wise VAR',
          description: "A theoretical connection between scale-wise autoregressive generation and discrete diffusion motivates iterative visual refinement.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/scale-wise-var/";
            },},{id: "projects-steered-diffusion",
          title: 'Steered Diffusion',
          description: "A general framework steers pretrained diffusion models during sampling for image-to-image and label-conditioned generation.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/steered-diffusion/";
            },},{id: "projects-unite-and-conquer",
          title: 'Unite and Conquer',
          description: "Independently trained diffusion models compose at inference time to satisfy multiple conditions without joint multimodal training.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/unite-and-conquer/";
            },},{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=_julgEYAAAAJ", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/Nithin-GK", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/nithin-gk-218174137", "_blank");
        },
      },{
        id: 'social-x',
        title: 'X',
        section: 'Socials',
        handler: () => {
          window.open("https://twitter.com/NithinGK10", "_blank");
        },
      },{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%69%61%6D%6E%69%74%68%69%6E%67%6B@%67%6D%61%69%6C.%63%6F%6D", "_blank");
        },
      },{
        id: 'social-rss',
        title: 'RSS Feed',
        section: 'Socials',
        handler: () => {
          window.open("/feed.xml", "_blank");
        },
      },];
