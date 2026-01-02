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
  },{id: "nav-publications",
          title: "Publications",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
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
          section: "News",},{id: "projects-project-1",
          title: 'project 1',
          description: "with background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/1_project/";
            },},{id: "projects-project-2",
          title: 'project 2',
          description: "a project with a background image and giscus comments",
          section: "Projects",handler: () => {
              window.location.href = "/projects/2_project/";
            },},{id: "projects-project-3-with-very-long-name",
          title: 'project 3 with very long name',
          description: "a project that redirects to another website",
          section: "Projects",handler: () => {
              window.location.href = "/projects/3_project/";
            },},{id: "projects-project-4",
          title: 'project 4',
          description: "another without an image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/4_project/";
            },},{id: "projects-project-5",
          title: 'project 5',
          description: "a project with a background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/5_project/";
            },},{id: "projects-project-6",
          title: 'project 6',
          description: "a project with no image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/6_project/";
            },},{id: "projects-project-7",
          title: 'project 7',
          description: "with background image",
          section: "Projects",handler: () => {
              window.location.href = "/projects/7_project/";
            },},{id: "projects-project-8",
          title: 'project 8',
          description: "an other project with a background image and giscus comments",
          section: "Projects",handler: () => {
              window.location.href = "/projects/8_project/";
            },},{id: "projects-project-9",
          title: 'project 9',
          description: "another project with an image 🎉",
          section: "Projects",handler: () => {
              window.location.href = "/projects/9_project/";
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
