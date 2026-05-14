---
title: "EcoGEO: Trajectory-Aware Evidence Ecosystems for Web-Enabled LLM Search Agents"
authors:
  - "Hengwei Ye"
  - "Jiasheng Mao"
  - "Zhenhan Guan"
  - "Zheng Tian"
date: "2026-05-13"
arxiv_id: "2605.12887"
arxiv_url: "https://arxiv.org/abs/2605.12887"
pdf_url: "https://arxiv.org/pdf/2605.12887v1"
categories:
  - "cs.IR"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Web Agent"
  - "Generative Engine Optimization"
  - "Search Agent"
  - "Multi-step Browsing"
relevance_score: 8.5
---

# EcoGEO: Trajectory-Aware Evidence Ecosystems for Web-Enabled LLM Search Agents

## 原始摘要

Web-enabled LLM agents are changing how online information influences search outcomes. \ Existing Generative Engine Optimization (GEO) studies mainly focus on individual webpages. \ However, agentic web search is not a single-document setting: an agent may issue queries, crawl pages, follow links, reformulate searches, and synthesize evidence across multiple browsing steps. \ Influence therefore depends not only on page content, but also on how pages are organized, connected, and encountered along the agent's browsing trajectory. \ We study this shift through \textbf{Ecosystem Generative Engine Optimization} (\textbf{EcoGEO}), which treats GEO as an environment-level influence problem for web-enabled LLM agents. \ To instantiate this perspective, we propose \textbf{TRACE}, a \textbf{Trajectory-Aware Coordinated Evidence Ecosystem}. \ Given a recommendation query and a fictional target product, our method builds a controlled evidence environment that coordinates an agent-facing navigation entry page with heterogeneous support pages. \ These pages use shared terminology, internal links, and consistent product attributes to introduce, verify, and reinforce the target product. We evaluate our method on OPR-Bench, a benchmark for open-ended product recommendation. \ Experiments show that it consistently outperforms page-level GEO baselines in final target recommendation. \ Trajectory-level metrics further show increased initial target-result crawls, target-specific follow-up searches, and internal-link crawls, suggesting that the gains come from shaping the agent's evidence-acquisition process rather than merely adding more target-related content. \ Overall, our findings support an ecosystem research paradigm for GEO, where web-enabled LLM agents are studied in relation to the broader evidence environments that guide search, browsing, and answer synthesis.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在支持网络搜索的大语言模型（LLM）智能体环境下，如何优化信息影响力的问题。研究背景是：LLM智能体正成为新的在线信息访问接口，它们能执行多步骤的浏览轨迹（如发起查询、爬取页面、跟进链接、整合证据）来生成最终回答。现有生成式引擎优化（GEO）研究主要关注单个网页的优化（如重写内容以提高可见性），但这种方法忽略了智能体搜索的核心特性——最终答案所依赖的证据是通过整个浏览轨迹动态构建的，而非仅由单一文档决定。因此，现有方法的不足在于：它们无法捕捉页面间的组织方式、连接关系以及页面在智能体浏览路径中被遇到的顺序如何影响智能体的证据获取与最终决策。本文要解决的核心问题是：如何将GEO从单页面层面的优化，提升到整个证据生态系统（即多个协调一致的页面所构成的环境）的层面，通过设计智能体的浏览轨迹来影响其信息获取过程，从而更有效地引导智能体在开放式产品推荐等任务中得出特定结论。为验证这一视角，作者提出了EcoGEO框架及其实例化方法TRACE。

### Q2: 有哪些相关研究？

在相关研究方面，本文首先回顾了传统的**搜索引擎优化（SEO）** 领域。经典SEO研究如何通过修改网页元数据、关键词、内容结构等页面级特征，或利用竞争性排名激励机制，来提升网页在搜索引擎结果页（SERP）中的排名可见性。其优化单元通常是单个网页或站点，目标聚焦于改善排名位置或点击率。本文与传统SEO的核心区别在于，研究背景已从传统搜索转向了以大型语言模型（LLM）为基础的生成式引擎（GE）和智能体搜索，优化单元从单个网页转变为整个证据生态系统。

其次，本文重点梳理了**生成式引擎优化（GEO）** 领域的最新工作。早期GEO研究提出了以内容创作者为中心的黑盒优化框架，通过重写或重构源内容来提升其在生成式答案中的可见性；后续工作则扩展到了生成式搜索偏好、自动内容重写、对话式搜索引擎优化、电商专属GEO基准等。本文指出，现有GEO研究大多仍采用页面级或文档级的视角，将单个源文档作为优化、引用和评估的基本单元。与之相比，本文提出的EcoGEO方法将分析单元从优化的单个网页提升到协调一致的证据环境，不再只关注让单页更易读或更易被引用，而是研究智能体入口页面与相互支撑的辅助页面如何协同塑造智能体的曝光、后续浏览、证据积累和最终答案合成过程。

此外，本文的研究还涉及**智能体网络搜索**的相关方法，即模型能够自主查询、爬取页面、跟随链接、重组搜索并在多步浏览中综合证据。本文工作正是在此背景下，通过构建可控的证据环境来影响智能体的整个信息获取轨迹，而非仅仅修改其可能访问的某一篇源文档。

### Q3: 论文如何解决这个问题？

为了应对网络增强型LLM代理在开放式产品推荐场景中的搜索过程依赖轨迹而非单一文档的问题，论文提出了EcoGEO框架，其核心方法是**TRACE（轨迹感知的协调证据生态系统）**。该方法将生成引擎优化（GEO）提升为环境级影响问题，通过构建一个由**导航入口页**和**多源支持页**组成的协调证据图来引导代理的浏览轨迹。

整体框架围绕一个证据图$G_P$构建，该图基于目标产品$P$的描述$P_{desc}$。主要模块包括：
1.  **导航入口页 ($v_0$)**：作为代理从搜索结果首次进入生态系统的网关。它被设计为评价导向（如购买指南、评测），而非官方产品页。其功能是吸引代理爬取，并作为导航枢纽，概述产品属性并链接到下游证据。
2.  **协调多页证据 ($V_s$)**：一组角色专门化的支持页面，模拟真实世界中证据的异质性。系统定义了六种原型：官方网站、评测、专家文章、新闻报道、论坛讨论和社交媒体。这些页面通过**属性一致性**（如产品名称、核心特征稳定）和**跨页引用**（如评测页引用官方规格）相互协调，确保证据在多样化的来源上下文中保持连贯。

关键创新点在于，TRACE不直接注入大量目标内容，而是通过精心设计的证据生态来**塑造代理的证据获取轨迹**。实验表明，该方法能增加对目标结果的初始爬取、目标特定的后续搜索以及内部链接爬取，从而在最终推荐中显著优于页面级GEO基线。这证明了通过影响代理的浏览路径而非仅内容，可以更有效地实现生态层面的影响。

### Q4: 论文做了哪些实验？

论文在OPR-Bench基准测试上评估了EcoGEO方法。实验设置包括SafeSearch、E-Commerce和E-GEO三个数据集，对比方法为页面级GEO基线。主要实验结果显示，TRACE在最终推荐率上显著优于所有基线：SafeSearch上达到67.2%（绝对增益31.3百分点），E-Commerce上71.9%（增益15.7百分点），E-GEO上73.9%（增益14.9百分点）。轨迹级指标显示，TRACE增加了初始目标结果爬取率、目标特定后续搜索次数和内部链接爬取，说明其通过塑造智能体的证据获取过程而非单纯增加目标相关内容来提升效果。此外，在两个小数据集上进行了曝光控制消融研究，固定初始暴露后比较非协调、协调和TRACE三种变体。结果显示，从非协调到协调提升了推荐率，证明了协调多页证据的效果；从协调到TRACE进一步提升了推荐率和内部链接爬取，证明了导航页入口对进入和遍历协调证据网络的关键作用。页面级GEO方法未持续优于未优化基线，表明在开放式推荐任务中，单一页面优化效果有限。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在实验环境的可控性上：OPR-Bench使用虚构产品，无法模拟真实世界的排名波动、有机发现、内容时效变化和商业源交互等动态因素。未来研究方向包括：1）扩展证据生态系统的设计空间，系统研究支持页面规模、页面样式多样性、入口排名、交叉链接密度、摘要设计和后续搜索行为如何影响影响效果；2）探索更复杂的代理行为模式，如多步验证、跨源对比和证据置信度评估；3）开发防御机制，鼓励代理从更多独立来源交叉验证证据，而非被单一协调生态系统引导。此外，当前方法仅适用于推荐查询，未来可扩展到问答、事实核查等任务场景；也可结合强化学习让生态系统自适应调整页面结构和链接策略，以应对不同代理的浏览偏好。

### Q6: 总结一下论文的主要内容

本文提出了EcoGEO（生态系统生成引擎优化），将针对网络增强型LLM智能体的生成引擎优化从单页面视角提升至协调的“证据生态系统”层面。核心问题在于：智能体通过多步浏览轨迹（如查询、爬取、链接跳转）合成答案，页面影响力不仅取决于内容，更取决于其在浏览轨迹中的位置与连接方式。为此，作者设计了TRACE方法，构建一个以目标产品为核心的协调证据生态系统，包含导航入口页和多种专业化支持页面（如官方、评论、专家页等），通过共享术语、内部链接和一致产品属性引导智能体的证据获取过程。在基于OPR-Bench（涵盖3124个查询-产品对）的实验中，TRACE在最终目标推荐率上显著优于单页面和页面级GEO基线。轨迹级指标显示，其成功源于重塑了智能体的证据获取轨迹（如增加目标相关爬取和追踪搜索），而不仅仅是增加目标内容。结论表明，未来GEO研究应转向以生态系统为导向，关注协调化信息环境对智能体搜索与推理过程的整体影响。
