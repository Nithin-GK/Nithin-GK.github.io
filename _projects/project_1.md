---
layout: page
title: Unite and Conquer- Plug & Play Multi-Modal Synthesis using Diffusion Models
permalink: projectpages/Multidiff
# description: a project with a background image
img: assets/img/publication_preview/multi.png
importance: 1
category: work
---
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XB3PR2Y1TQ"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-XB3PR2Y1TQ');
    </script>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <title>Unite and Conquer</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.0/css/bootstrap.min.css">
    <link href='https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,500,600' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="/assets/css/Highlight-Clean.css">
    <link rel="stylesheet" href="/assets/css/styles.css">

    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="manifest" href="/site.webmanifest">

    <meta property="og:site_name" content="Unite and Conquer: Cross Dataset Multimodal Synthesis using Diffusion Models" />
    <meta property="og:type" content="video.other" />
    <meta property="og:title" content="Unite and Conquer: Cross Dataset Multimodal Synthesis using Diffusion Models" />
    <meta property="og:description" content="Unite and Conquer: Cross Dataset Multimodal Synthesis using Diffusion Models, 2022." />
    <meta property="og:url" content="https://dreamfusion3d.github.io/" />
    <meta property="og:image" content="https://dreamfusion3d.github.io/assets/images/multi.png" />

    <meta property="article:publisher" content="https://dreamfusion3d.github.io/" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="Unite and Conquer: Cross Dataset Multimodal Synthesis using Diffusion Models" />
    <meta name="twitter:description" content="We combine neural rendering with a multi-modal text-to-2D image diffusion generative model to synthesize diverse 3D objects from text." />
    <meta name="twitter:url" content="https://dreamfusion3d.github.io/" />
    <meta name="twitter:image" content="https://dreamfusion3d.github.io/assets/images/multi.png" />
    <!-- <meta name="twitter:site" content="" /> -->

    <script src="assets/js/video_comparison.js"></script>
    <script type="module" src="https://unpkg.com/@google/model-viewer@2.0.1/dist/model-viewer.min.js"></script>
</head>

<body>

    <div class="highlight-clean" style="padding-bottom: 10px;">
        <!-- <div class="container" style="max-width: 1250px;">: 
            <h1 class="text-center"><b>Unite and Conquer</b>: Cross Dataset Multimodal Synthesis using Diffusion Models</h1>
        </div> -->
        <div class="container" style="max-width: 1100px;">
            <div class="row authors">
             <div class="col-sm-2">
                    <!-- <h5 class="text-center"><a class="text-center" href="https://nithin-gk.github.io/">Nithin Gopalakrishnan Nair</a></h5> -->
                </div>
                <div class="col-sm-3">
                    <h5 class="text-center"><a class="text-center" href="https://nithin-gk.github.io/">Nithin Gopalakrishnan Nair</a></h5>
                </div>
                <div class="col-sm-3">
                    <h5 class="text-center"><a class="text-center" href="https://www.wgcban.com/">Chaminda Bandara</a></h5>
                </div>
                <div class="col-sm-3">
                    <h5 class="text-center"><a class="text-center" href="https://engineering.jhu.edu/vpatel36/team/vishalpatel/">Vishal M Patel</a></h5>
                </div>
            </div>    
        </div>
        <div align= "center" class="buttons" style="margin-bottom: 8px;">
             
            <a class="btn btn-light" role="button" href="https://arxiv.org/abs/2212.00793">
                <svg style="width:24px;height:24px;margin-left:-12px;margin-right:12px" viewBox="0 0 24 24">
                    <path fill="currentColor" d="M16 0H8C6.9 0 6 .9 6 2V18C6 19.1 6.9 20 8 20H20C21.1 20 22 19.1 22 18V6L16 0M20 18H8V2H15V7H20V18M4 4V22H20V24H4C2.9 24 2 23.1 2 22V4H4M10 10V12H18V10H10M10 14V16H15V14H10Z"></path>
                </svg>Paper
            </a>
            <a class="btn btn-light border border-dark" role="button" href="https://github.com/Nithin-GK/UniteandConquer">
                <svg style="visibility:hidden;width:0px;height:24px;margin-left:-12px;margin-right:12px" width="0px" height="24px" viewBox="0 0 375 531">
                    <polygon stroke="#000000" points="0.5,0.866 459.5,265.87 0.5,530.874 "/>
                </svg>
                Github
            </a>
            <a class="btn btn-light" role="button" href="https://huggingface.co/spaces/gknithin/MultimodalDiffusion">
                <svg style="width:24px;height:24px;margin-left:-12px;margin-right:12px" width="24px" height="24px" viewBox="0 0 375 531">
                    <polygon stroke="#000000" points="0.5,0.866 459.5,265.87 0.5,530.874 "/>
                </svg>
                Demo
            </a>
        </div>
    </div>
    <hr class="divider" />
    <div align="justify" class="container" style="max-width: 768px;">
        <div class="row">
            <div class="col-md-12">
                <h2><center> Abstract </center></h2>
                <p>
                    <!-- <strong> -->
                        Generating photos satisfying multiple constraints finds broad utility in the content creation industry. A key hurdle to accomplishing this task is the need for paired data consisting of all modalities (i.e., constraints) and their corresponding output. Moreover, existing methods need retraining using paired data across all modalities to introduce a new condition. This paper proposes a solution to this problem based on denoising diffusion probabilistic models (DDPMs). Our motivation for choosing diffusion models over other generative models comes from the flexible internal structure of diffusion models. Since each sampling step in the DDPM follows a Gaussian distribution, we show that there exists a closed-form solution for generating an image given various constraints. Our method can unite multiple diffusion models trained on multiple sub-tasks and conquer the combined task through our proposed sampling strategy. We also introduce a novel reliability parameter that allows using different off-the-shelf diffusion models trained across various datasets during sampling time alone to guide it to the desired outcome satisfying multiple constraints. We perform experiments on various standard multimodal tasks to demonstrate the effectiveness of our approach. 
                    <!-- </strong> -->
                </p>
            </div>
        </div>
    </div>
    <div align="center" class="container" style="max-width: 768px;">
        <div class="row captioned_videos">
            <div class="col-md-12">
            <img src="assets/images/multi.png" alt="sym" width="700" height ="500" style="border-style: none" />
                <h6 class="caption">Our model can combine task spectific information learned by multiple models and perform composite generation during inference time without any explciit retraining.</h6>
            </div>
        </div>
    </div>
    <hr class="divider" />
    
    </div>   
    <hr class="divider" />
    <div class="container" style="max-width: 768px;">
        <div class="row">
            <div class="col-md-12">
                <h2>Method</h2>
            </div>
        </div>
    </div>
    <div align="center" class="container" style="max-width: 768px;">
        <div class="row captioned_videos">
            <div class="col-md-12">
            <img src="assets/img/paper_images/method_train.png" alt="sym" width="500" height ="300" style="border-style: none" />
                <!-- <h6 class="caption">Our model can combine task spectific information learned by multiple models and perform composite generation during inference time without any explciit retraining.</h6> -->
            </div>
        </div>
    </div>
    <div align="center" class="container" style="max-width: 768px;">
        <div class="row captioned_videos">
            <div class="col-md-12">
            <img src="assets/img/paper_images/method.png" alt="sym" width="700" height ="500" style="border-style: none" />
                <!-- <h6 class="caption">Our model can combine task spectific information learned by multiple models and perform composite generation during inference time without any explciit retraining.</h6> -->
            </div>
        </div>
    </div>
    <hr class="divider" />
   <div class="container" style="max-width: 768px;">
        <div class="row">
            <div class="col-md-12">
                <h2>Multimodal face generation</h2>
            </div>
        </div>
    </div>

    <div align="center" class="container" style="max-width: 768px;">
        <div class="row captioned_videos">
            <div class="col-md-12">
            <img src="assets/img/paper_images/multimodal4.png" alt="sym" width="700" height ="500" style="border-style: none" />
                <!-- <h6 class="caption">Our model can combine task spectific information learned by multiple models and perform composite generation during inference time without any explciit retraining.</h6> -->
            </div>
        </div>
    </div>

    <hr class="divider" />
   <div class="container" style="max-width: 768px;">
        <div class="row">
            <div class="col-md-12">
                <h2>Multimodal generic scenes generation</h2>
            </div>
        </div>
    </div>

    <div align="center" class="container" style="max-width: 768px;">
        <div class="row captioned_videos">
            <div class="col-md-12">
            <img src="assets/img/paper_images/comparison.png" alt="sym" width="700" height ="250" style="border-style: none" />
            </div>
        </div>
    </div>

   <hr class="divider" />
   <div class="container" style="max-width: 768px;">
        <div class="row">
            <div class="col-md-12">
                <h2>Multimodal Interpolation</h2>
            </div>
        </div>
    </div>

    <div align="center" class="container" style="max-width: 768px;">
        <div class="row captioned_videos">
            <div class="col-md-12">
            <img src="assets/img/paper_images/interpolation.png" alt="sym" width="700" height ="700" style="border-style: none" />
                <!-- <h6 class="caption">Our model can combine task spectific information learned by multiple models and perform composite generation during inference time without any explciit retraining.</h6> -->
            </div>
        </div>
    </div>
    <hr class="divider" />
    
   <div align="center" class="container" style="max-width: 768 px;">
        <div class="row">
            <div class="col-md-12">
                <h2>Demo Video</h2>
            </div>
        </div>
    </div>
<!--    <div align="center" class="container" style="max-width: 512 px;">
    <div class="row">
            <div class="col-md-12">
                <video class="video lazy" autoplay playsinline controls muted poster="assets/img/paper_images/demovideo.png">
                    <source data-src="https://github.com/Nithin-GK/nithin-gk.github.io/blob/main/projectpages/Multidiff/assets/img/paper_images/demo_video.mp4?raw=true" type="video/mp4"></source>
                </video>
            </div>
    </div>
    </div>
 -->
    <hr class="divider" />

    <div class="container" style="max-width: 768px;">
        <div class="row">
            <div class="col-md-12">
                <h2>Citation</h2>
                <code>
                 @article{nair2022unite,<br>
                &nbsp;  title={Unite and Conquer: Cross Dataset Multimodal Synthesis using Diffusion Models},<br>
                &nbsp; author={Nair, Nithin Gopalakrishnan and Bandara, Wele Gedara Chaminda and Patel, Vishal M},<br>
                &nbsp; journal={arXiv preprint arXiv:2212.00793},<br>
                &nbsp; year={2022}<br>
                &nbsp; }<br>
                </code>
            </div>
        </div>
    </div>
 <hr class="divider" />
    <div class="container" style="max-width: 768px;">
        <div class="row">
            <div class="col-md-12">
                <h2>Acknowledgement</h2>
                <p>
                    This template has been borrowed from https://dreamfusion3d.github.io/
                </p>
            </div>
        </div>
    </div>
    <script src="https://polyfill.io/v3/polyfill.js?features=IntersectionObserver"></script>
    <script src="/assets/js/yall.js"></script>
    <script>
        yall(
            {
                observeChanges: true
            }
        );
    </script>
    <script src="/assets/js/scripts.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.0/js/bootstrap.bundle.min.js"></script>
    <script src="https://uploads-ssl.webflow.com/51e0d73d83d06baa7a00000f/js/webflow.fd002feec.js"></script>
    <!-- Import the component -->
</body>

