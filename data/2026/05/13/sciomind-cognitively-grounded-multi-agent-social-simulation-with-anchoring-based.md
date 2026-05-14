---
title: "ScioMind: Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles"
authors:
  - "Yitian Yang"
  - "Yiqun Duan"
  - "Linghan Huang"
  - "Yiqi Zhu"
  - "Francesco Bailo"
  - "Chunmeizi Su"
  - "Huaming Chen"
date: "2026-05-13"
arxiv_id: "2605.13725"
arxiv_url: "https://arxiv.org/abs/2605.13725"
pdf_url: "https://arxiv.org/pdf/2605.13725v1"
categories:
  - "cs.AI"
  - "cs.SI"
tags:
  - "多智能体社会模拟"
  - "信念动力学"
  - "认知架构"
  - "记忆锚定"
  - "动态角色"
  - "LLM Agent"
relevance_score: 9.5
---

# ScioMind: Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles

## 原始摘要

Large language model (LLM)-based multi-agent simulation offers a powerful testbed for studying social opinion dynamics. Yet current approaches often adopt two contrasting methods: either relying on fixed update rules with limited cognitive grounding or delegating belief change largely to unconstrained LLM interaction. We introduce ScioMind, a cognitively grounded simulation framework that bridges these paradigms by combining structured opinion dynamics with LLM-based agent reasoning. ScioMind integrates three key components: 1) a memory-anchored belief update rule that modulates susceptibility to influence via personality-conditioned anchoring strength; 2) a hierarchical memory architecture that supports persistent, experience-driven belief formation; and 3) dynamic agent profiles derived from a corpus-grounded retrieval pipeline, enabling heterogeneous personalities, rationales, and evolving internal states. We evaluate ScioMind on multiple case studies in a real-world policy debate scenario. Across metrics including polarisation, diversity, extremization, and trajectory stability, the proposed components consistently yield improvements in behavioural realism. In particular, dynamic profiles increase opinion diversity, memory and reflection reduce unstable oscillation, and anchoring induces persistent belief trajectories that better align with patterns reported in political psychology. These results suggest that our cognitively grounded design provides a novel solution to LLM-based social simulation that improves both stable and behavioural realism

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决基于大语言模型的多智能体社会模拟中存在的核心问题：现有方法要么依赖缺乏认知基础的固定更新规则，要么将信念变化完全交给不受约束的LLM交互，导致模拟行为与真实人类信念形成过程脱节。具体而言，研究背景指出了经典基于智能体的模型（如DeGroot共识模型、有限置信模型）虽然提供了基础见解，但因采用简化的加权平均等更新规则，难以捕捉人类复杂的推理与说服过程。而基于LLM的模拟方法虽然提升了交互表现力，却存在四个关键不足：缺乏显式的信念影响机制、没有融入认知上合理的抵抗变化机制、智能体多样性局限于静态描述、以及在争议性话题上常出现过度平滑（即智能体过快收敛到中立或共识位置），无法复现现实中的持久分歧与有界极化现象。为解决这些问题，本文提出了ScioMind框架，其核心设计是将结构化意见动力学与LLM智能体推理相结合，具体通过基于记忆锚定的信念更新规则（利用个性特质调节易受影响性）、分层记忆架构（支持经验驱动的持久信念形成）、以及从语料库检索的动态智能体画像来实现更真实的社会模拟。

### Q2: 有哪些相关研究？

本文的相关研究可分为两类。第一类是**经典观点动力学**，如DeGroot模型、Friedkin-Johnsen模型（引入了顽固性，是本文锚定机制的前驱）和有界信任模型。这些模型数学上易处理，但仅操作标量观点状态，难以捕捉人类信念形成中的丰富论证过程。本文与之区别在于，ScioMind将结构化更新规则与LLM的推理能力结合，在保持认知可解释性的同时增加了论证的丰富性。第二类是**基于LLM的社会模拟**，包括Generative Agents、S$^3$、OASIS、AgentSociety和MOSAIC等。现有工作虽然实现了行为上更真实的代理，但缺乏对信念如何在社会互动中持续和更新的明确认知基础。例如，AgentSociety虽具备记忆机制，MOSAIC虽引入动态profile，但均未整合本文所强调的基于锚定的信念更新、分层记忆架构和基于语料库的动态profile。ScioMind在信念状态、记忆机制、动态profile、反思机制等六个维度上全面超越了这些基线（见表1），从而实现了更符合政治心理学实证模式的行为。

### Q3: 论文如何解决这个问题？

ScioMind通过一个分层架构来模拟多智能体的信念动态。核心方法是引入了锚定信念更新规则，该规则将智能体的信念更新建模为三个部分的加权组合：自我权重（当前信念）、社会影响（邻居信念的加权和）和锚点拉动（记忆锚点）。其中，记忆锚点是智能体从自身经历中提取的参考点，且是动态演变的，而非固定不变。锚定强度ρ通过智能体的OCEAN人格特质经由逻辑函数映射得到，使得低开放性和高尽责性的个体锚定更强。为了支持经验驱动的信念形成，系统设计了四层记忆架构：情景记忆（短期交互记录）、语义记忆（长期经验存储，基于向量检索）、程序记忆（定义行为例程）和反思记忆（生成自我反思以强化锚点）。此外，动态智能体画像通过语料驱动的流水线构建，从大规模语料中检索并生成异质性的人格、立场和兴趣特征，并通过约束（如兴趣重叠上限）和多样性分数保证生成质量。

其整体框架包含核心信念更新模块、分层记忆系统、基于人格的锚定强度计算、动态画像生成引擎以及社会关系网络构建器。主要创新点在于：1）将心理学中的锚定效应形式化到Agent模型中，使信念变化具有认知基础；2）锚点随记忆动态更新，而非固定初始值；3）结合人格特质个性化锚定强度；4）引入基于检索的动态画像和分层社会网络（包括圈子、KOL等）生成，实现了从底层心理机制到上层社交互动的全面认知模拟。

### Q4: 论文做了哪些实验？

我们实验评估了ScioMind框架在现实政策辩论场景中的表现。实验设置中，每个智能体被实例化为公民、政府、商业或教育四种社会原型之一，并由大五人格（OCEAN）参数化。智能体初始以1:1:1平衡分布被赋予反对、中立或支持三种立场。我们使用基于LLM的场景调度器提取多维政策话题，并通过缩放乘数支持可配置的人口规模，同时对所有随机成分设置确定性种子以确保可复现性。

对比方法方面，由于论文聚焦于框架内部组件的消融研究，我们主要比较了有无动态档案、记忆反射和锚定机制的不同配置。主要结果通过多个度量指标评估：极化程度采用方差度量，观点多样性采用香农熵，极端化采用信念超出阈值(≥0.6)的智能体比例，以及平均激进水平。关键数据显示：动态档案显著提高了观点多样性；记忆与反射机制减少了不稳定震荡；锚定机制则产生了与政治心理学报告模式更一致的持久信念轨迹。此外，我们还报告了人格多样性、推理标签多样性、反思活动水平，以及对锚定配置的平均锚定强度和锚定漂移量。这些指标共同表明，我们提出的认知基础设计在行为真实性和稳定性方面均优于简化配置。

### Q5: 有什么可以进一步探索的点？

该研究的一个主要局限是模拟中的情感强度与真实人类数据存在显著差距，这受限于AI安全策略对极端化响应的抑制。未来可探索通过微调或提示工程在安全约束内释放更真实的情感表达。此外，模拟样本量（如43个智能体）较小，采样偏差可能影响结论的稳健性，未来可在更大规模、更多样化的人口数据上进行验证。锚定机制虽然有效，但其与个性特征的交互参数（如开放性与锚定强度）目前基于预设阈值，可进一步通过贝叶斯方法或强化学习实现参数的自适应演化。另一个值得探索的方向是将双向互动（如主流意见对个体的反向影响）纳入动态档案更新，以更真实地反映社会影响的双重性。最后，当前因果图分析聚焦于主体-主题关系，未来可引入时间序列因果推断或反事实推理，量化不同干预策略（如信息环境改变）对极化收敛路径的具体影响。

### Q6: 总结一下论文的主要内容

该论文提出ScioMind框架，旨在解决基于LLM的多智能体社会模拟中信念动态的两个极端：固定规则缺乏认知基础，或开放交互导致过度平滑。核心贡献是将认知锚定效应引入信念更新，设计了三部分机制：基于记忆锚的信念更新规则，通过人格特质调节锚定强度以影响可说服性；四层分层记忆架构（情景、语义、反思、工作记忆）支持经验驱动的信念形成；以及从社交媒体语料库检索并融合群体人格先验的动态智能体画像。在真实政策辩论场景的案例研究中，ScioMind在极化、多样性、极端化和轨迹稳定性指标上均提升了行为真实性：动态画像增加了观点多样性，记忆与反思减少了不稳定震荡，锚定机制诱发了与政治心理学模式一致的持久信念轨迹。该工作为LLM社会模拟提供了结合结构化认知机制与开放式推理的新范式，显著增强了模拟稳定性和行为现实主义。
