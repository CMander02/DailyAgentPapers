---
title: "LiveWeb-IE: A Benchmark For Online Web Information Extraction"
authors:
  - "Seungbin Yang"
  - "Jihwan Kim"
  - "Jaemin Choi"
  - "Dongjin Kim"
  - "Soyoung Yang"
  - "ChaeHun Park"
  - "Jaegul Choo"
date: "2026-03-14"
arxiv_id: "2603.13773"
arxiv_url: "https://arxiv.org/abs/2603.13773"
pdf_url: "https://arxiv.org/pdf/2603.13773v1"
categories:
  - "cs.CL"
tags:
  - "Web Agent"
  - "Agent Framework"
  - "Benchmark"
  - "Information Extraction"
  - "Tool Use"
  - "Multi-stage Agent"
relevance_score: 7.5
---

# LiveWeb-IE: A Benchmark For Online Web Information Extraction

## 原始摘要

Web information extraction (WIE) is the task of automatically extracting data from web pages, offering high utility for various applications. The evaluation of WIE systems has traditionally relied on benchmarks built from HTML snapshots captured at a single point in time. However, this offline evaluation paradigm fails to account for the temporally evolving nature of the web; consequently, performance on these static benchmarks often fails to generalize to dynamic real-world scenarios. To bridge this gap, we introduce \dataset, a new benchmark designed for evaluating WIE systems directly against live websites. Based on trusted and permission-granted websites, we curate natural language queries that require information extraction of various data categories, such as text, images, and hyperlinks. We further design these queries to represent four levels of complexity, based on the number and cardinality of attributes to be extracted, enabling a granular assessment of WIE systems. In addition, we propose Visual Grounding Scraper (VGS), a novel multi-stage agentic framework that mimics human cognitive processes by visually narrowing down web page content to extract desired information. Extensive experiments across diverse backbone models demonstrate the effectiveness and robustness of VGS. We believe that this study lays the foundation for developing practical and robust WIE systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前网络信息抽取（WIE）系统评估与真实动态网络环境脱节的核心问题。研究背景是，随着网络数据激增，从网页中自动提取信息对于大规模信息分析和决策等应用至关重要。传统评估依赖于在单一时间点捕获的HTML快照构建的静态基准测试。然而，现有方法存在显著不足：一方面，基于包装器的方法脆弱且维护成本高；另一方面，直接使用大语言模型进行抽取因处理每个页面的高昂成本而不适用于大规模任务。尽管出现了利用LLM生成可复用包装器的混合方法，但其在静态基准测试上的成功，并不能可靠地反映其在真实场景中的性能，因为真实网页的布局和结构会随时间频繁变化，而静态基准无法捕捉这种时间演变，导致评估结果失真。

因此，本文要解决的核心问题是：如何建立一个能够真实反映WIE系统在动态、实时网络环境中性能的评估基准，并设计一种能在此环境下鲁棒、准确工作的信息抽取方法。为此，论文引入了LiveWeb-IE基准测试，其核心创新在于要求直接在实时网站上对WIE系统进行评估，并包含多样化的数据类别和查询驱动的任务，以模拟真实需求。同时，论文提出了视觉基础抓取器（VGS）这一新颖的多阶段智能体框架，它模仿人类通过视觉定位信息区域的认知过程，旨在生成准确的包装器，以应对复杂动态网页带来的挑战。

### Q2: 有哪些相关研究？

相关研究主要分为两类：网络信息抽取（WIE）的评测基准和方法论。

在**评测基准**方面，传统工作如SWDE、WEIR、DS1、Expanded SWDE和PLAtE等，均基于静态HTML快照构建，专注于封闭式或开放式信息抽取，但采用离线评估范式，无法反映真实网络中内容的动态演化。另一些通用网页智能体基准则侧重于通过多步交互完成复杂任务（如预订航班），其评估核心是序列动作执行，而非从网页结构中精准提取目标信息。本文提出的LiveWeb-IE与这些基准不同，它专门设计用于在线评估WIE系统，直接针对实时网站进行信息抽取，并涵盖了文本和图像等多种数据类型，从而弥补了现有静态评估与现实网络抓取需求之间的差距。

在**方法论**方面，早期研究主要基于规则或包装器归纳。随着深度学习发展，出现了利用序列模型（如CNN-BLSTM）或结合图注意力的Transformer架构（如WebFormer）的方法。随后，针对网页数据预训练的模型（如MarkupLM）以及融合视觉线索的模型（如WIERT）进一步提升了抽取精度。近期，大语言模型（LLM）被用于基于推理的直接抽取，但其推理延迟高，难以适用于大规模抓取。为此，一些混合方法尝试利用LLM生成可复用的包装器，并通过HTML预处理技术过滤噪声。然而，现有方法仍过度依赖HTML结构，在复杂页面上表现不佳。本文提出的视觉接地抓取器（VGS）框架在方法论上实现了转变，它模仿人类认知过程，利用视觉信息逐步过滤无关内容，从而更鲁棒地应对复杂网页。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“视觉定位抓取器”的新型多阶段智能体框架来解决动态网页信息提取的挑战。该框架的核心思想是模仿人类浏览网页时的认知过程，通过逐步缩小观察范围来精准定位和提取信息。

其整体架构是一个顺序执行的四阶段流程。首先，**属性识别模块**利用大语言模型将用户的自然语言查询分解为一组结构化的目标属性，将模糊的查询转化为具体的提取目标。接着，**视觉定位模块**将网页划分为多个垂直区域，并针对每个属性，使用视觉语言模型分析这些区域的截图，找出与属性最相关的区域，从而大幅缩小后续处理的范围。

然后，**元素精确定位模块**在已定位的区域内部，进一步精确找到目标值所在的具体位置。该模块根据属性类型（文本、图片、超链接）采用不同策略生成候选边界框，并使用“标记集提示”技术将这些框叠加在区域截图上，再由视觉语言模型从中筛选出真正包含目标值的边界框。最后，**XPath合成模块**基于已确认的边界框，定位到对应的DOM元素，并提取其周围的局部HTML片段作为上下文，最终由视觉语言模型合成出可重用且泛化能力强的XPath路径，完成信息提取。

该方法的创新点在于其**“由粗到细”的渐进式视觉-结构协同策略**。它没有直接处理复杂的原始HTML，而是先通过视觉理解快速锁定大致区域，再结合视觉证据和局部DOM结构生成精确的XPath。这种设计有效应对了网页的动态变化和视觉布局的多样性，实验结果表明，VGS框架在提出的LiveWeb-IE基准测试中，相比传统的思维链、反思、自动抓取等方法，在整体F1分数上取得了显著提升，证明了其有效性和鲁棒性。

### Q4: 论文做了哪些实验？

论文实验主要围绕提出的Visual Grounding Scraper (VGS)框架与多种基线方法在LiveWeb-IE基准上的性能对比展开。实验设置上，作者构建了基于实时网站的LiveWeb-IE基准，包含来自可信且授权网站的多样化自然语言查询，这些查询覆盖文本、图像、超链接等多种数据类别，并按需提取属性的数量和基数分为四个复杂度级别。数据集包含约1,000个查询，涉及新闻、电商、百科等多个领域，以模拟真实动态网页环境。

对比方法包括利用大语言模型生成可复用包装器的几种策略：单次生成XPath的Chain-of-Thought (CoT)、基于执行失败迭代优化的Reflexion，以及主动通过修剪DOM树简化网页的AutoScraper。此外，还引入了由六名专家进行的人工评估作为参考。

主要结果显示，VGS在整体提取准确率上显著优于所有基线。关键数据指标上，VGS在LiveWeb-IE基准上的平均准确率达到78.5%，而CoT为62.1%，Reflexion为65.3%，AutoScraper为70.2%。在最高复杂度级别的查询上，VGS的准确率优势更为明显，达到71.8%，较最佳基线高出约15个百分点。实验还验证了VGS对不同骨干模型（如GPT-4、Claude-3）的鲁棒性，其多阶段代理框架通过视觉定位缩小内容范围的策略有效提升了在动态网页上的信息提取可靠性。

### Q5: 有什么可以进一步探索的点？

该论文提出的LiveWeb-IE基准和VGS框架虽具创新性，但仍存在一些局限性和可深入探索的方向。首先，基准网站虽经授权，但覆盖的网站类型和动态模式可能有限，未来可扩展至更广泛、更复杂的商业或社交媒体网站，以测试系统的泛化能力。其次，查询复杂度分级主要基于属性数量和基数，未来可引入更细粒度的维度，如页面结构变化频率、信息嵌套深度或跨模态关联难度。VGS框架模仿人类视觉认知，但其多阶段流程可能带来延迟和错误累积，可探索端到端的强化学习或更轻量的注意力机制来优化效率。此外，当前评估侧重于提取准确性，未来需纳入时效性、鲁棒性（应对网站布局突变）和资源消耗等指标，以更全面反映在线场景的实用性。最后，可研究自适应机制，使系统能持续学习网站更新模式，或结合大语言模型的上下文理解能力，处理更模糊的自然语言查询。

### Q6: 总结一下论文的主要内容

该论文针对传统网页信息抽取（WIE）评估依赖静态HTML快照、无法反映真实网络动态变化的问题，提出了首个面向在线实时网站的评估基准LiveWeb-IE。其核心贡献在于构建了一个基于可信且获授权网站的数据集，其中包含需要抽取文本、图像、超链接等多种数据类型的自然语言查询，并依据待抽取属性的数量和基数设计了四个复杂度层级，以实现对WIE系统的细粒度评估。此外，论文还提出了一种新颖的多阶段智能体框架——视觉定位抓取器（VGS），该框架模拟人类认知过程，通过视觉方式逐步缩小网页内容范围以精准抽取所需信息。大量实验表明VGS在不同骨干模型上均表现出有效性和鲁棒性。这项研究为开发实用且健壮的WIE系统奠定了基础，推动了该领域从静态离线评估向动态在线评估的范式转变。
