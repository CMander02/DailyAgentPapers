---
title: "How do Visual Attributes Influence Web Agents? A Comprehensive Evaluation of User Interface Design Factors"
authors:
  - "Kuai Yu"
  - "Naicheng Yu"
  - "Han Wang"
  - "Rui Yang"
  - "Huan Zhang"
date: "2026-01-29"
arxiv_id: "2601.21961"
arxiv_url: "https://arxiv.org/abs/2601.21961"
pdf_url: "https://arxiv.org/pdf/2601.21961v2"
categories:
  - "cs.AI"
  - "cs.HC"
tags:
  - "Web & Browser Automation"
  - "Human-Agent Interaction"
relevance_score: 7.5
taxonomy:
  capability:
    - "Web & Browser Automation"
    - "Human-Agent Interaction"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "GPT-4V, LLaVA-NeXT, CogAgent, Qwen-VL-Chat"
  key_technique: "VAF (Visual Attribute Factors evaluation pipeline)"
  primary_benchmark: "VAF (自建评测框架)"
---

# How do Visual Attributes Influence Web Agents? A Comprehensive Evaluation of User Interface Design Factors

## 原始摘要

Web agents have demonstrated strong performance on a wide range of web-based tasks. However, existing research on the effect of environmental variation has mostly focused on robustness to adversarial attacks, with less attention to agents' preferences in benign scenarios. Although early studies have examined how textual attributes influence agent behavior, a systematic understanding of how visual attributes shape agent decision-making remains limited. To address this, we introduce VAF, a controlled evaluation pipeline for quantifying how webpage Visual Attribute Factors influence web-agent decision-making. Specifically, VAF consists of three stages: (i) variant generation, which ensures the variants share identical semantics as the original item while only differ in visual attributes; (ii) browsing interaction, where agents navigate the page via scrolling and clicking the interested item, mirroring how human users browse online; (iii) validating through both click action and reasoning from agents, which we use the Target Click Rate and Target Mention Rate to jointly evaluate the effect of visual attributes. By quantitatively measuring the decision-making difference between the original and variant, we identify which visual attributes influence agents' behavior most. Extensive experiments, across 8 variant families (48 variants total), 5 real-world websites (including shopping, travel, and news browsing), and 4 representative web agents, show that background color contrast, item size, position, and card clarity have a strong influence on agents' actions, whereas font styling, text color, and item image clarity exhibit minor effects.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在系统性地研究网页视觉属性如何影响基于视觉-语言模型（VLM）的网页智能体（Web Agent）的决策过程。研究背景是，尽管VLM网页智能体在网页浏览、在线购物等任务上展现出强大能力，但现有研究大多关注智能体在对抗性攻击下的鲁棒性，而对其在正常（良性）场景中的内在决策偏好探索不足。早期工作主要分析了文本属性（如价格、评分）的影响，但现实网页包含丰富的视觉元素（如布局、颜色、样式），这些因素如何塑造智能体的决策尚缺乏系统理解。

现有方法的不足在于：首先，缺乏一个受控的评估框架来量化单一视觉属性变化对智能体行为的影响；其次，以往评估往往忽略人类浏览网页时的自然交互模式（如滚动、点击）；最后，对于哪些视觉属性（如颜色对比度、位置、字体）对智能体决策具有显著影响，缺乏基于大规模实验的实证结论。

因此，本文的核心问题是：**不同的网页视觉属性如何影响智能体的决策？** 为解决这一问题，论文提出了VAF评估流程，通过生成语义相同但视觉属性可控变化的网页变体，模拟人类浏览交互，并综合点击率和推理提及率来量化视觉属性的影响，从而识别出对智能体行为最具影响力的视觉设计因素。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及三类：网络智能体、环境变异对智能体的影响，以及面向人类的网页设计。

在网络智能体方面，相关工作根据感知模态分为基于文本和基于多模态（视觉语言模型，VLM）的智能体。基于文本的智能体操作HTML代码等结构化表示，缺乏视觉感知；而VLM智能体能处理渲染后的截图，理解布局和颜色等视觉信息。本文聚焦于VLM智能体，系统研究视觉属性对其决策的影响。

在环境变异影响方面，先前研究多集中于对抗性攻击下的鲁棒性，例如提示注入攻击或视觉侧漏洞，旨在测试智能体的安全性。相比之下，对良性场景中智能体偏好的研究较少，尤其是视觉属性如何塑造决策尚未得到充分探索。本文则填补了这一空白，专注于非对抗性视觉属性的系统性评估。

在网页设计方面，大量人机交互和认知心理学研究表明，视觉属性（如颜色对比度、元素大小、位置）显著影响人类的注意力与决策。这些发现为本文提供了动机，以探究网络智能体是否与人类具有相似的视觉感知偏好。本文通过构建受控评估流程，首次对多种视觉属性进行了量化分析，揭示了智能体与人类反应的异同。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为VAF（Visual Attribute Factors）的受控评估流程来解决系统量化网页视觉属性如何影响智能体决策的问题。其核心方法是一个三阶段管道，旨在隔离视觉因素的影响并精确测量其效应。

整体框架与主要模块如下：
1.  **变体生成阶段**：首先从五个真实网站（涵盖购物、旅行、新闻浏览）获取HTML页面快照，并指定一个目标商品（如特定笔记本电脑）。关键创新在于，仅通过修改目标项的CSS样式（如背景色、字体、大小、位置）来生成视觉变体，同时严格保持HTML内容与功能语义不变。这确保了原始页面与变体页面之间仅有目标项的视觉属性存在差异，从而能将后续观察到的行为变化归因于视觉修改。该研究实例化了8个变体家族（背景色、文本颜色、字体族、字体大小、位置、卡片大小、清晰度、顺序），共计48个具体变体，实现了对常见网页设计因素的全面覆盖。

2.  **拟人化浏览交互阶段**：为了模拟更真实的人类浏览行为，该框架允许智能体执行滚动操作（上下滚动600像素），从而观察一系列视口图像序列，而非仅提供单一静态视图。这种设计使智能体能够像人类一样通过滚动建立对页面的全局认知，并在决策时参考当前的视口内容及交互历史，支持跨不同视口的项目比较。

3.  **双重验证与量化评估阶段**：这是方法的核心创新点。研究不仅通过智能体的最终点击行为（动作层面）进行验证，还通过分析其推理轨迹（思维层面）进行验证。具体使用两个量化指标：
    *   **目标点击率**：计算智能体点击落在目标项边界框内的试验比例，直接衡量视觉属性对最终选择行为的影响。
    *   **目标提及率**：利用基于大语言模型的评估器，分析智能体的思维链，判断其是否在推理中明确提及了目标项。该指标用于衡量视觉属性对智能体注意力分配和内部决策推理过程的影响。

通过系统比较智能体在原始页面与各视觉变体页面上的行为差异（综合使用TCR和TMR），该方法能够精确识别出哪些视觉属性对智能体决策产生强影响（如背景对比度、项目大小、位置、卡片清晰度），哪些影响较弱（如字体样式、文本颜色、图片清晰度），从而实现了对视觉属性影响的全面、定量评估。

### Q4: 论文做了哪些实验？

实验设置方面，研究提出了VAF评估流程，包含变体生成、浏览交互和验证三个阶段。在浏览交互中，智能体通过滚动和点击进行导航，模拟人类浏览行为。验证时使用目标点击率（TCR）和目标提及率（TMR）共同评估视觉属性的影响。实验在五个真实网站（Amazon、eBay、Booking、Expedia、NPR）上进行，覆盖电商、旅游和新闻浏览场景。研究针对每个目标项目生成了8个变体家族共48种视觉变体，仅修改CSS元素以保持语义不变。对比方法涉及四个代表性视觉语言模型：三个开源模型（UI-TARS 7B、GLM-4.1v-9B、Qwen3-VL-8B-Instruct）和一个商业闭源模型（OpenAI-CUA）。每个变体进行50次独立试验，推理温度设为1.0，top-p为0.8。

主要结果显示，背景颜色对比度、项目大小、位置和卡片清晰度对智能体行为有显著影响。具体数据指标包括：高对比度背景平均提升TCR达11.7%；将卡片缩放因子从0.8增至1.2和1.5分别使TCR提升12%和20%。位置变体中，将目标项目移至页面底部或侧边栏会导致点击率大幅下降，例如UI-TARS 7B在侧边栏位置的TCR仅为0.060。相比之下，字体样式和文本颜色变体影响较小，图像清晰度的影响也有限，但整个卡片模糊会显著降低TCR。各模型表现存在差异：例如Qwen3VL-8B对卡片缩放（scale_1.5）的TCR达0.680，而GLM4.1v-9B对背景颜色（#4caf50）的TCR高达0.770。TMR与TCR呈现正相关，高点击率变体通常伴随更高的目标提及率。

### Q5: 有什么可以进一步探索的点？

基于论文的局限性，未来研究可以从以下几个方向深入探索：首先，可扩展评估范围，将VAF框架应用于更大规模的模型（如GPT-4V、Gemini等多模态大模型）及更多样化的智能体架构（如基于强化学习的端到端代理），以验证视觉属性影响的普适性。其次，需进一步探究动态与复杂场景，例如交互式网页中的动画效果、响应式布局变化或用户行为模拟，这些因素可能更贴近真实环境中的决策干扰。此外，可结合因果分析厘清视觉属性与决策偏差的机制，例如通过注意力可视化技术解析智能体对特定视觉特征的依赖程度。最后，可探索自适应优化策略，如设计对抗性训练或视觉鲁棒性增强方法，以降低智能体对无关视觉因素的敏感性，提升其在多样化界面中的泛化能力。

### Q6: 总结一下论文的主要内容

该论文针对网页视觉属性如何影响智能体决策这一研究空白，提出了一个名为VAF的系统性评估框架。其核心贡献在于设计了一套包含变体生成、浏览交互和验证的三阶段流程，能够量化评估不同视觉属性对网页智能体行为的影响。研究发现，在购物、旅游和新闻浏览等真实网站场景下，背景颜色对比度、项目大小、位置以及卡片清晰度对智能体行为有显著影响，而字体样式、文字颜色和图片清晰度的影响则相对较小。这些结论表明，智能体的注意力模式与人类受视觉显著性和位置偏差驱动的模式相似，但其决策仍显脆弱，一旦视觉基础被破坏就容易失效。该研究为理解智能体在良性环境中的偏好提供了新视角，对改进网页智能体的鲁棒性和人机交互设计具有指导意义。
