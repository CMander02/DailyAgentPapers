---
title: "ViviDoc: Generating Interactive Documents through Human-Agent Collaboration"
authors:
  - "Yinghao Tang"
  - "Yupeng Xie"
  - "Yingchaojie Feng"
  - "Tingfeng Lan"
  - "Jiale Lao"
  - "Yue Cheng"
  - "Wei Chen"
date: "2026-03-30"
arxiv_id: "2603.27991"
arxiv_url: "https://arxiv.org/abs/2603.27991"
pdf_url: "https://arxiv.org/pdf/2603.27991v1"
categories:
  - "cs.HC"
  - "cs.AI"
tags:
  - "Multi-Agent System"
  - "Human-Agent Collaboration"
  - "Interactive Document Generation"
  - "Controllable Generation"
  - "Evaluation Benchmark"
relevance_score: 7.5
---

# ViviDoc: Generating Interactive Documents through Human-Agent Collaboration

## 原始摘要

Interactive documents help readers engage with complex ideas through dynamic visualization, interactive animations, and exploratory interfaces. However, creating such documents remains costly, as it requires both domain expertise and web development skills. Recent Large Language Model (LLM)-based agents can automate content creation, but directly applying them to interactive document generation often produces outputs that are difficult to control. To address this, we present ViviDoc, to the best of our knowledge the first work to systematically address interactive document generation. ViviDoc introduces a multi-agent pipeline (Planner, Styler, Executor, Evaluator). To make the generation process controllable, we provide three levels of human control: (1) the Document Specification (DocSpec) with SRTC Interaction Specifications (State, Render, Transition, Constraint) for structured planning, (2) a content-aware Style Palette for customizing writing and interaction styles, and (3) chat-based editing for iterative refinement. We also construct ViviBench, a benchmark of 101 topics derived from real-world interactive documents across 11 domains, along with a taxonomy of 8 interaction types and a 4-dimensional automated evaluation framework validated against human ratings (Pearson r > 0.84). Experiments show that ViviDoc achieves the highest content richness and interaction quality in both automated and human evaluation. A 12-person user study confirms that the system is easy to use, provides effective control over the generation process, and produces documents that satisfy users.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决交互式文档创作成本高昂、技术门槛高的问题。交互式文档通过动态可视化、交互式动画和探索性界面，能有效帮助读者理解复杂概念，在教育、数据新闻和科学出版等领域有广泛应用前景。然而，现有创作方式严重依赖作者同时具备领域专业知识与网页开发技能，导致制作耗时耗力，一篇高质量交互文档往往需要数天甚至数周，这极大限制了此类优质内容的产出。

尽管近期基于大语言模型（LLM）的智能体在内容生成任务上展现出潜力，但直接将其应用于交互式文档生成存在明显不足。现有方法主要有三个局限：一是生成过程难以控制，智能体基于自身隐含偏好填补作者意图与可执行代码之间的鸿沟，导致输出结果不符合预期；二是人类无法有效参与过程，智能体如同黑箱，作者难以审查或调整影响最终输出的中间决策；三是缺乏系统的评估资源，没有基于真实场景的数据集或评估框架来比较不同方法。

为此，本文提出了ViviDoc系统，核心是系统性地解决交互式文档的自动生成问题，并确保生成过程可控、透明且支持人机协作。具体而言，论文设计了一个多智能体流水线（规划器、样式器、执行器、评估器），并引入了三层人类控制机制：使用包含SRTC（状态、渲染、过渡、约束）交互规范的结构化文档规划（DocSpec）来指导生成；通过内容感知的样式调色板定制写作与交互风格；以及基于聊天的编辑功能进行迭代优化。同时，论文还构建了包含101个真实主题的基准测试集ViviBench和自动化评估框架，以支持系统性的方法评测。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：交互式文档本身的研究、基于LLM/智能体的内容生成系统，以及相关的评估方法。

在**交互式文档研究**方面，相关工作追溯至早期人机交互与超文本系统（如Engelbart的理论框架和PLATO系统），近期实证研究证实了其对提升读者参与度和理解力的价值，并在数据新闻（如《纽约时报》的“Snow Fall”）和学术传播等领域得到应用。然而，现有研究多聚焦于其效用与案例，而**ViviDoc**则首次系统性地解决了此类文档的**自动化生成**难题，旨在降低其高昂的创作成本。

在**基于LLM/智能体的内容生成系统**方面，近期研究利用多智能体框架自动化复杂内容创作，已在多个领域取得成功。例如，在数据可视化领域有HAIChart、VisPilot等系统；在演示文稿生成领域有PPTagent、SlideGen等。这些工作通常依赖结构化模式来保证输出连贯性。**ViviDoc**与这些方法一脉相承，但其创新点在于**专门针对交互式文档这一未被探索的领域**，并解决了直接应用现有智能体方法时面临的三大瓶颈：生成过程不可控、智能体黑箱特性阻碍人为干预，以及缺乏专门的评估基准。

在**评估方法**方面，现有内容生成系统往往缺乏系统性的评估框架。为此，**ViviDoc**贡献了ViviBench基准与自动化评估体系，这填补了该领域在标准化评测方面的空白，与前述多数工作形成了区别。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ViviDoc的多智能体协作框架来解决交互式文档生成可控性差的问题。其核心方法是构建一个结构化的、支持多层次人工干预的生成管道，将复杂的生成任务分解为可控的步骤。

**整体框架与主要模块**：系统采用一个由四个智能体组成的流水线：规划器、风格器、执行器和评估器，并由一个称为文档规范（DocSpec）的结构化中间表示进行协调。
1.  **规划器**：接收用户主题，将其分解为一系列知识单元，并生成结构化的DocSpec。每个知识单元包含文本描述和基于SRTC模型的交互规范，将交互意图明确分解为状态、渲染、转换和约束四个组件，从而将模糊的自然语言描述转化为精确的生成指令。
2.  **风格器**：分析DocSpec内容，生成一个内容感知的“风格调色板”，提供写作风格（如叙事语调）和交互风格（如视觉复杂度）等多个维度的选项供用户选择。用户选择被编译成自然语言指令，注入后续生成步骤的提示中。
3.  **执行器**：依据DocSpec和风格指令，分两步生成最终的HTML文档。第一步根据文本描述和写作风格生成文本内容；第二步根据SRTC交互规范和交互风格，生成包含HTML、CSS和JavaScript的交互式可视化。
4.  **评估器**：对生成的文档进行正确性检查，验证HTML结构、知识单元的完整性等，发现问题时可提供反馈以触发特定组件的重新执行。

**创新点与关键技术**：
1.  **结构化中间表示（DocSpec与SRTC）**：这是核心创新。DocSpec作为管道各阶段间的“契约”，将生成意图结构化。其嵌入的SRTC交互规范，基于Munzner的What-Why-How框架进行适配，将交互可视化明确分解为状态、渲染、转换、约束，极大地减少了从意图到代码转换过程中的歧义，是实现可控生成的基础。
2.  **多层次人机协同控制机制**：系统在三个关键节点引入人工控制：在规划后直接编辑结构化的DocSpec（如调整知识单元顺序、修改交互参数）；通过风格调色板定制文档风格；在生成后通过基于聊天的界面进行迭代式自然语言精修。这种设计使用户无需编码技能即可进行精准、可预测的干预。
3.  **内容感知的风格定制**：风格调色板并非通用模板，而是由LLM根据DocSpec的具体内容动态生成选项，实现了风格与内容的关联，提升了定制的灵活性和有效性。

通过这种“结构化规划+风格定制+迭代精修”的多智能体流水线设计，ViviDoc将生成过程模块化，并用结构化规范约束了最易出错的意图到代码的转换步骤，从而在自动化生成的同时，为用户提供了系统且有效的控制手段。

### Q4: 论文做了哪些实验？

论文实验主要包括三部分：自动化评估、人工评估和用户研究。实验设置方面，作者在自建的ViviBench基准（包含11个领域、101个主题和8种交互类型）上，使用三种骨干大语言模型（Gemini 3 Flash、Mistral Small和Qwen 3.5-35B）测试了ViviDoc与三种多智能体基线方法（AutoGen、CAMEL、MetaGPT）以及一个无DocSpec规划的Naive Agent基线。主要对比指标包括内容丰富度（CR，1-5分）、交互质量（IQ，0-5分）、交互功能度（IF，0-1分）和生成效率（Eff，字符/秒）。

主要结果显示，ViviDoc在所有骨干模型上均取得最优的CR和IQ分数。例如，使用Gemini 3 Flash时，ViviDoc的CR为1.00（归一化后），IQ为0.92，显著优于最佳基线AutoGen（CR 0.53，IQ 0.64）。在效率上，ViviDoc（505字符/秒）分别是AutoGen、CAMEL和MetaGPT的3.3倍、9.9倍和2.0倍。与Naive Agent相比，ViviDoc的IQ提升达41%（Gemini 3 Flash），证实了DocSpec结构化规划的有效性。

人工评估中，12名评分者对9个主题的生成文档进行盲评，ViviDoc在内容丰富度和交互设计上均获最高分（CR 4.43，ID 4.33）。LLM评分与人工评分高度相关（Pearson r > 0.84）。用户研究中，12名参与者使用ViviDoc后，在可用性、可控性、输出质量和重用意愿上均给出高分（均高于4.0/5.0），其中易用性项目获满分5.00。定性反馈肯定了DocSpec的细粒度控制和聊天编辑的有效性，同时建议为样式调色板增加实时预览功能。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其多智能体流程和三层控制机制虽然提升了可控性，但也可能使创作过程略显复杂，对非技术用户的门槛并未完全消除。ViviBench基准虽覆盖11个领域，但交互类型（8种）和主题数量（101个）仍有扩展空间，以涵盖更边缘或新兴领域的交互需求。

未来研究方向可从三方面深入：一是增强智能体的自主创意与风格迁移能力，使其能基于少量示例或自然语言描述生成更独特、连贯的交互设计，减少对结构化规约的依赖。二是探索动态人机协作模式，如实时协同编辑或基于用户反馈的在线自适应优化，使生成过程更灵活。三是将系统扩展至多模态交互文档生成，如图文音视频融合的沉浸式体验，并开发更细粒度的自动化评估指标，以衡量交互的流畅性与叙事性。

可能的改进思路包括引入轻量级交互模板库降低使用成本，以及利用强化学习优化智能体在复杂约束下的决策效率，从而在可控性与创作自由度间取得更好平衡。

### Q6: 总结一下论文的主要内容

这篇论文提出了ViviDoc系统，旨在通过人机协作自动生成交互式文档，以降低传统制作方式对领域知识和网页开发技能的高要求。其核心贡献是首次系统性地解决了交互式文档生成问题，并引入了可控的人机协作框架。方法上，ViviDoc设计了一个多智能体管道（规划器、样式器、执行器、评估器），并提供了三层人工控制机制：一是基于SRTC（状态、渲染、过渡、约束）交互规范的文档规划结构（DocSpec），二是用于定制写作与交互风格的内容感知样式板，三是基于聊天的迭代编辑。此外，论文构建了ViviBench基准，包含11个领域的101个主题及8种交互类型分类，并提出了一个与人工评分高度相关（皮尔逊r>0.84）的四维自动评估框架。实验表明，ViviDoc在自动和人工评估中均实现了最高的内容丰富度和交互质量；用户研究证实了其易用性、生成过程的有效可控性以及产出文档的用户满意度。
