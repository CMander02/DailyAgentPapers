---
title: "NewsLens: A Multi-Agent Framework for Adversarial News Bias Navigation"
authors:
  - "Joy Bose"
date: "2026-05-17"
arxiv_id: "2605.17364"
arxiv_url: "https://arxiv.org/abs/2605.17364"
pdf_url: "https://arxiv.org/pdf/2605.17364v1"
categories:
  - "cs.CL"
  - "cs.IR"
tags:
  - "多智能体系统"
  - "媒体偏见检测"
  - "新闻框架分析"
  - "宣传检测"
  - "开源LLM"
relevance_score: 7.5
---

# NewsLens: A Multi-Agent Framework for Adversarial News Bias Navigation

## 原始摘要

Media bias detection has predominantly been framed as a classification task: assign a political label to an article or outlet. We argue this framing is too shallow: it identifies that bias exists but not where, how, or crucially, what is structurally omitted. We present NewsLens, a five-agent adversarial pipeline for structured news bias navigation. A Fact Verifier, Progressive Framing Analyst, Conservative Framing Analyst, Propaganda Detector, and Neutral Summarizer collaborate to deconstruct articles into interpretable framing maps, exposing ideological omissions, rhetorical manipulation, and framing boundaries. The system is evaluated on 15 articles across four geopolitical event clusters (India-Pakistan Kashmir, Gaza, Climate Policy, Ukraine) using Qwen2.5-3B-Instruct (4-bit quantised, Google Colab T4), with cross-model validation using Mistral 7B on the Kashmir cluster. Center outlets show the highest mean Perspective Divergence Score (PDS: Qwen 0.907, Mistral 0.729 on Kashmir subset); conservative-framing outlets show the highest mean Manipulation Index (MI: 0.600 across both models). Cross-model comparison shows high consistency for high-propaganda content (Republic World delta-PDS=0.125, MI=0.8 both models) and greater variance for nuanced reporting. Mann-Whitney U tests find no statistically significant between-group differences at n=15, reported honestly as a sample-size limitation confirmed by post-hoc power analysis. A partial ablation removing the Propaganda Detector shows degraded omission precision in the Neutral Summarizer output. The architecture extends prior lexical-geometric bias work to agentic LLM reasoning, and is fully reproducible using open-weight models without API keys.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决传统媒体偏见检测方法的局限性。传统方法通常将媒体偏见视为一个分类问题，即给新闻文章或媒体机构分配一个政治标签（如左倾或右倾）。作者认为这种框架过于浅薄，因为它只能识别偏见的“存在”，而无法揭示偏见的“位置”、“如何形成”，以及最关键的是“结构性地遗漏了什么”。具体来说，它无法回答：哪些具体主张存在争议？哪些视角被系统性忽略？使用了哪些修辞手法来绕过批判性思考？论文提出了一种新的范式：将偏见视为可导航的结构，通过一个多智能体系统生成可解释的“框架图”，暴露意识形态上的遗漏、修辞操控和框架边界，从而提供比简单标签更丰富的分析。该系统名为NewsLens，旨在增强媒体素养，让读者能够理解分析报道背后的政治议程和报道的完全性。

### Q2: 有哪些相关研究？

相关研究可分为三个方向。第一是词汇和统计偏见检测，如Gentzkow & Shapiro (2010) 使用词汇特征和国会演讲模式，以及Patankar & Bose (2017) 引入的基于词向量的几何偏见检测方法，通过测量与维基百科NPOV语料的余弦距离来量化偏见。NewsLens将这种静态几何方法扩展到基于LLM的动态对抗推理。第二是基于LLM的政治偏见分析，如Motoki et al. (2023) 发现LLM本身具有中间偏左的意识形态偏见。NewsLens没有试图消除这种偏见，而是通过赋予智能体特定意识形态角色来将其操作化为分析工具。第三是多智能体辩论和宣传检测系统。多智能体辩论如Du et al. (2023) 用于提高事实准确性，但其目标是达成共识，而NewsLens则以分歧本身为主要分析输出。宣传和框架检测如SemEval-2020共享任务 (Da San Martino et al., 2020) 建立了细粒度分类，Entman (1993) 定义了框架分析理论。NewsLens创新性地将框架分析、宣传检测和遗漏分析整合到一个统一管道中。

### Q3: 论文如何解决这个问题？

论文提出了一个五智能体对抗性管道NewsLens。核心设计是五个专用智能体顺序执行（部分并行），每个智能体具有确定性的结构化JSON输出，运行在低参数级开源LLM上（Qwen2.5-3B-Instruct和Mistral 7B）。第一个智能体是事实验证器，负责提取核心事件、标记有争议的指控并提供真实验证分数，建立经验基线。第二和第三个智能体是渐进框架分析师和保守框架分析师，它们并行独立地对同一篇新闻文章应用意识形态驱动的分析，识别框架、语言标记、遗漏和对抗性批评。它们的并行独立运行至关重要，以防止锚定偏差。第四个智能体是宣传检测器，它独立于政治立场识别修辞操控技术（如恐惧诉求、虚假两难），并分配操纵指数MI。第五个智能体是中立摘要器，它整合所有上游输出，生成共识现实、观点战场、去偏摘要和一个关键的遗漏图，其中明确标注了渐进派遗漏、保守派遗漏以及双方都遗漏的内容。管道的关键创新：使用LLM的固有意识形态偏见作为分析工具，而不是试图消除它；通过多智能体架构防止锚定；以及通过遗漏分析揭示被双方主动忽略的关键事实。系统完全使用开源模型在免费云硬件上复现。

### Q4: 论文做了哪些实验？

论文在15篇新闻文章上评估了系统，涵盖四个地缘政治事件簇：印度-巴基斯坦克什米尔、加沙、气候政策和乌克兰战争。这些文章来自按AllSides媒体偏见评级选择的不同意识形态立场的媒体。使用Qwen2.5-3B-Instruct（4位量化）进行主评估，并在克什米尔簇上使用Mistral 7B进行跨模型验证。报告了两个指标：观点分歧分数（PDS，基于Jaccard距离，衡量左右框架的分歧程度）和操纵指数（MI，宣传检测器分配）。主要发现：中心媒体平均PDS最高（Qwen 0.907，Mistral 0.729），保守派媒体平均MI最高（0.600）。跨模型比较显示，高宣传内容（如Republic World）在两个模型上高度一致（ΔPDS=0.125，MI均为0.8），而细微报道则差异较大。进行了消融实验：移除宣传检测器导致遗漏质量下降（双方遗漏变得模糊）。作者诚实地报告了样本量（n=15）导致的统计显著性不足，Mann-Whitney U检验未发现显著组间差异，事后功效分析确认需要n≥50才能达到统计功效。案例研究展示了Republic World文章的高宣传分解：识别出具体技术（虚假两难，恐惧诉求）和双方遗漏（独立伤亡核实，长期外交解决前景）。

### Q5: 有什么可以进一步探索的点？

论文指出多个局限性和未来方向。第一，需要更大规模的评估（n≥50，覆盖10个以上主题），并采用自动化数据摄取（如GDELT）以增强统计功效和泛化性。第二，进行形式化的消融研究，量化每个独立智能体（尤其是宣传检测器）的具体贡献，当前消融研究只进行了一次。第三，设计时间线级别的偏见漂移分析，追踪同一故事在数周内媒体框架的演变，可以使用图数据库（如FalkorDB）存储实体关系。第四，改进PDS指标：当前Jaccard距离忽略语义相似性，应探索句子嵌入余弦距离（当前存在SSL/Transformers兼容性问题）。第五，扩展到更多语言和文化背景，采用适应性框架提示而非固定的左右轴。第六，研究对抗性提示风险：如何防止智能体被恶意注入以产生误导性分析。第七，探索将输出用于自动事实核查和教育应用，但需注意双用途风险（可能被反向用于生成宣传）。

### Q6: 总结一下论文的主要内容

该论文提出了NewsLens，一个五智能体抗性管道，用于结构化新闻偏见导航。核心贡献是：将媒体偏见分析从简单的标签分类重构为可解释的框架知识导航；引入遗漏分析组件，揭示左右双方都系统性忽视的关键事实；提出观点分歧分数(PDS)和操纵指数(MI)作为可量化指标；在15篇文章的地缘政治簇上使用两种开源LLM进行了可行性和一致性验证；完全免费且可复现（无需API密钥）。主要发现：不同意识形态媒体的PDS和MI呈现规律性差异（中心媒体高PDS，保守媒体高MI）；对于强宣传内容，跨模型一致性高；移除宣传检测器会降低遗漏精度。论文将该工作定位为对早期词向量偏见检测方法向基于LLM的推理范式的扩展。
