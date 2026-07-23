---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am a Ph.D. student at **The University of Hong Kong (HKU)** and a member of **HKU MMLab**. Before that, I received my B.Eng. in Computer Science and Technology from **Zhejiang University** in 2025, where I conducted research at the State Key Laboratory of CAD&CG.

My research focuses on **generative models**, **multimodal intelligence**, and **interactive agents**. I am particularly interested in building controllable visual generation systems and generalist models that can perceive, reason, and act in complex environments.

I have worked with research teams at **Alibaba Tongyi Laboratory**, the **University of Illinois Urbana-Champaign**, and **Zhejiang University**. I am always happy to discuss research ideas and potential collaborations—please feel free to reach out by [email](mailto:zkchen66@outlook.com).

<div class="profile-actions">
  <a class="profile-action" href="resume/Zhekai_Chen_Resume.pdf"><i class="fas fa-file-alt"></i> Curriculum Vitae</a>
  <a class="profile-action" href="https://scholar.google.com/citations?user=_eZWcIMAAAAJ&hl=en"><i class="fas fa-graduation-cap"></i> Google Scholar</a>
  <a class="profile-action" href="https://github.com/Zhekai-Chen"><i class="fab fa-github"></i> GitHub</a>
</div>

# 🔥 News

- *Jul. 2026*. &nbsp;🤖 We release [**UniClawBench**](https://arxiv.org/abs/2607.17497), a unified benchmark for evaluating whether generalist agents can perceive, reason, and act in complex environments.
- *Mar. 2026*. &nbsp;🎉 We release [**MACRO**](https://arxiv.org/abs/2603.11438), a unified model for human-centered spatial reasoning and collaboration.
- *Sep. 2025*. &nbsp;🎉 [**TTS-VAR**](https://arxiv.org/abs/2507.18537) is accepted to **NeurIPS 2025**.
- *2025*. &nbsp;🎓 I started my Ph.D. study at **The University of Hong Kong**.
- *2025*. &nbsp;🎉 [**Framer**](https://arxiv.org/abs/2410.18978) is accepted to **ICLR 2025**.
- *Oct. 2024*. &nbsp;🎉 [**FreeCompose**](https://arxiv.org/abs/2407.04947) is presented at **ECCV 2024**.
- *2024*. &nbsp;💼 I joined **Alibaba Tongyi Laboratory** as a research intern.
- *Summer 2024*. &nbsp;💼 I worked as a research intern with Prof. Tong Zhang's group at **UIUC**.

# 📈 Citations

<div class="citation-card">
  <div class="citation-card__head">
    <div class="citation-card__stats">
      <div class="citation-card__total">
        <span id="total_cit">—</span>
        <span class="citation-card__total-label">total citations</span>
      </div>
      <div class="citation-card__metrics">
        <span><strong id="h_index">—</strong>&nbsp;h-index</span>
        <span class="citation-metric-sep">·</span>
        <span><strong id="i10_index">—</strong>&nbsp;i10-index</span>
      </div>
    </div>
    <div class="citation-card__controls">
      <div class="citation-toggle" id="citation-toggle">
        <button type="button" class="is-active" data-mode="total">Total</button>
        <button type="button" data-mode="avg">Avg / paper</button>
      </div>
      <a class="citation-card__link" href="https://scholar.google.com/citations?user=_eZWcIMAAAAJ&hl=en"><i class="fas fa-graduation-cap"></i> Google Scholar</a>
    </div>
  </div>
  <div class="citation-card__chart"><canvas id="citation-chart"></canvas></div>
  <p class="citation-card__empty" id="citation-chart-empty" hidden>Citation history will appear after the first scheduled update.</p>
</div>

# 📝 Selected Publications

My recent work spans generalist agents, human-centered spatial intelligence, visual generation, and multimodal understanding. Please see my [Google Scholar profile](https://scholar.google.com/citations?user=_eZWcIMAAAAJ&hl=en) for the full and most up-to-date list.

(\*: equal contribution)

<div class='paper-box'><div class='paper-box-image'><div class='paper-placeholder paper-placeholder--agent'><span>UniClawBench</span><small>Generalist Agents</small></div></div>
<div class='paper-box-text' markdown="1">

[**<font size=4>UniClawBench: A Unified Benchmark for Generalist Agents</font>**](https://arxiv.org/abs/2607.17497)  
**<font color="#dd0000">Preprint 2026</font>**  
Yanting Yang\*, Yujie Wei\*, **<u>Zhekai Chen</u>**, Xihui Liu

[arXiv](https://arxiv.org/abs/2607.17497)

- A unified evaluation platform for generalist agents across perception, reasoning, and embodied interaction.
- Studies whether a single agent can generalize across diverse tasks and environments.

</div></div>

<div class='paper-box'><div class='paper-box-image'><div class='paper-placeholder paper-placeholder--macro'><span>MACRO</span><small>Spatial Intelligence</small></div></div>
<div class='paper-box-text' markdown="1">

[**<font size=4>MACRO: A Unified Model for Human-Centered Spatial Reasoning and Collaboration</font>**](https://arxiv.org/abs/2603.11438)  
**<font color="#dd0000">Preprint 2026</font>**  
**<u>Zhekai Chen</u>**, Zhengqin Li, Zhao Yang, Yujie Wei, Yifan Zhou, Yanting Yang, Hongtao Wu, Xihui Liu

[arXiv](https://arxiv.org/abs/2603.11438)

- Unifies spatial perception, reasoning, and human-agent collaboration in one model.
- Targets interactive systems that understand people, objects, and their spatial relationships.

</div></div>

<div class='paper-box'><div class='paper-box-image'><div class='paper-placeholder paper-placeholder--video'><span>TTS-VAR</span><small>Visual Generation</small></div></div>
<div class='paper-box-text' markdown="1">

[**<font size=4>TTS-VAR: A Test-Time Scaling Framework for Visual Auto-Regressive Generation</font>**](https://arxiv.org/abs/2507.18537)  
**<font color="#dd0000">NeurIPS 2025</font>**  
Ling Yang\*, Zhaochen Yu\*, Chenlin Meng\*, Minkai Xu, **<u>Zhekai Chen</u>**, Kai-Wei Chang, Bin Cui, Yu-Gang Jiang, Chun-Yi Lee, Jianfeng Gao, Caiming Xiong

[arXiv](https://arxiv.org/abs/2507.18537) \| [project](https://ali-vilab.github.io/tt-scaling-visual-generation/)

- Introduces test-time scaling for visual autoregressive models through increasingly capable verification.
- Improves generation quality and prompt alignment without retraining the base generator.

</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025</div><img src='images/framer.png' alt="Framer teaser" width="100%" loading="lazy" decoding="async"></div></div>
<div class='paper-box-text' markdown="1">

[**<font size=4>Framer: Interactive Frame Interpolation</font>**](https://arxiv.org/abs/2410.18978)  
**<font color="#dd0000">ICLR 2025</font>**  
Wen Wang, Qiuyu Wang, Kecheng Zheng, Hao Ouyang, **<u>Zhekai Chen</u>**, Biao Gong, Hao Chen, Yujun Shen, Chunhua Shen

[arXiv](https://arxiv.org/abs/2410.18978) \| [project](https://aim-uofa.github.io/Framer/) \| [github](https://github.com/aim-uofa/Framer)

- Supports flexible frame interpolation conditioned on user-provided text, trajectories, and keyframes.

</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ECCV 2024</div><img src='images/free_compose.png' alt="FreeCompose teaser" width="100%" loading="lazy" decoding="async"></div></div>
<div class='paper-box-text' markdown="1">

[**<font size=4>FreeCompose: Generic Zero-Shot Image Composition with Diffusion Prior</font>**](https://arxiv.org/abs/2407.04947)  
**<font color="#dd0000">ECCV 2024</font>**  
**<u>Zhekai Chen</u>**\*, Wen Wang\*, Zhen Yang, Zeqing Yuan, Hao Chen, Chunhua Shen

[arXiv](https://arxiv.org/abs/2407.04947) \| [github](https://github.com/aim-uofa/FreeCompose)

- A generic zero-shot framework for composing images with multiple forms of user control.

</div></div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS</div><img src='images/image_textualization.png' alt="Image Textualization teaser" width="100%" loading="lazy" decoding="async"></div></div>
<div class='paper-box-text' markdown="1">

[**<font size=4>Image Textualization: An Automatic Framework for Creating Accurate and Detailed Image Descriptions</font>**](https://arxiv.org/abs/2406.07502)  
**<font color="#dd0000">NeurIPS Datasets & Benchmarks</font>**  
Renjie Pi\*, Jianshu Zhang\*, Jipeng Zhang, Rui Pan, **<u>Zhekai Chen</u>**, Tong Zhang

[arXiv](https://arxiv.org/abs/2406.07502) \| [github](https://github.com/sterzhang/image-textualization)

- Automatically creates accurate, detailed textual descriptions for large-scale image collections.

</div></div>

<div class='paper-box'><div class='paper-box-image'><div><img src='images/autostory.png' alt="AutoStory teaser" width="100%" loading="lazy" decoding="async"></div></div>
<div class='paper-box-text' markdown="1">

[**<font size=4>AutoStory: Generating Diverse Storytelling Images with Minimal Human Effort</font>**](https://arxiv.org/abs/2311.11243)  
**<font color="#dd0000">International Journal of Computer Vision</font>**  
Wen Wang\*, Canyu Zhao\*, Hao Chen, **<u>Zhekai Chen</u>**, Kecheng Zheng, Chunhua Shen

[arXiv](https://arxiv.org/abs/2311.11243) \| [project](https://aim-uofa.github.io/AutoStory/) \| [github](https://github.com/aim-uofa/AutoStory)

- Generates diverse, character-consistent storytelling images with minimal manual intervention.

</div></div>

# 🎓 Education

- *2025 - Present*. **The University of Hong Kong**, Ph.D. student.
- *2021 - 2025*. **Zhejiang University**, B.Eng. in Computer Science and Technology.
- *2018 - 2021*. **Suzhou Academy**, High School.

# 💼 Internships

<div class="experience-grid">
  <div class="experience-card">
    <span class="experience-date">Nov. 2024 – 2025</span>
    <h3>Alibaba Tongyi Laboratory</h3>
    <p><strong>Research Intern</strong></p>
    <p>Worked on visual generation and multimodal models, including test-time scaling for visual autoregressive generation.</p>
  </div>
  <div class="experience-card">
    <span class="experience-date">Summer 2024</span>
    <h3>University of Illinois Urbana-Champaign</h3>
    <p><strong>Research Intern · Prof. Tong Zhang's Group</strong></p>
    <p>Conducted research on multimodal learning and automatic image textualization.</p>
  </div>
</div>

# 🤝 Collaborations

- **HKU MMLab** — working with Prof. [Xihui Liu](https://xh-liu.github.io/) and collaborators on generalist agents, spatial intelligence, and human-agent collaboration.
- **Zhejiang University · State Key Laboratory of CAD&CG** — worked with Prof. [Chunhua Shen](https://cshen.github.io/), Prof. [Hao Chen](https://stan-haochen.github.io/), and the AIM research group on controllable image and video generation.
- **Alibaba Tongyi Laboratory** — collaborated with researchers in visual generation and multimodal intelligence on TTS-VAR and related projects.
- **UIUC** — worked with Prof. [Tong Zhang](https://tongzhang-ml.org/)'s group on multimodal data and image textualization.

<div class="collaboration-callout">
  <strong>Open to collaboration.</strong> I am interested in research on generative models, multimodal agents, visual reasoning, and human-AI interaction. If our interests overlap, please feel free to <a href="mailto:zkchen66@outlook.com">get in touch</a>.
</div>

# 🏆 Awards

- *2023 - 2024*. **Ho Chi Kwan Education Scholarship**, Zhejiang University CS Department (7 recipients each year).

# 🛎 Academic Service

- **Conference Reviewer**: ICLR 2025.

<script>
document.addEventListener('DOMContentLoaded', function () {
  var LIMIT = 5;
  var heading = document.getElementById('-news');
  if (!heading) return;
  var list = heading.nextElementSibling;
  while (list && list.tagName !== 'UL') list = list.nextElementSibling;
  if (!list) return;
  var items = Array.prototype.filter.call(list.children, function (el) { return el.tagName === 'LI'; });
  if (items.length <= LIMIT) return;
  items.forEach(function (li, i) { if (i >= LIMIT) li.classList.add('news-hidden'); });
  var button = document.createElement('button');
  button.className = 'news-toggle';
  button.type = 'button';
  button.innerHTML = 'Show all news <span class="news-toggle__chevron">⌄</span>';
  list.insertAdjacentElement('afterend', button);
  button.addEventListener('click', function () {
    var expanded = button.classList.toggle('is-expanded');
    items.forEach(function (li, i) { if (i >= LIMIT) li.classList.toggle('news-hidden', !expanded); });
    button.firstChild.nodeValue = expanded ? 'Show less ' : 'Show all news ';
  });
});
</script>
