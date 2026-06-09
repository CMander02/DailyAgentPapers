---
title: "MASS: Deep Research for Social Sciences with Memory-Augmented Social Simulation"
authors:
  - "Yongrui Liu"
  - "Deyi Xiong"
date: "2026-06-08"
arxiv_id: "2606.09198"
arxiv_url: "https://arxiv.org/abs/2606.09198"
pdf_url: "https://arxiv.org/pdf/2606.09198v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Social Simulation"
  - "Multi-Agent"
  - "Memory Mechanism"
  - "Goal-Path Planning"
relevance_score: 9.5
---

# MASS: Deep Research for Social Sciences with Memory-Augmented Social Simulation

## 原始摘要

Deep Research agents powered by Large Language Models (LLMs) have exhibited extraordinary potential in automated paper writing tasks. However, existing systems rely heavily on literature retrieval and synthesis through internet and local knowledge bases, often resulting research in lacking insight and creativity in social science. To address this issue, we propose "Memory-Augmented Social Simulation (MASS)", an innovative paradigm that leverages highly realistic and research-oriented social simulations to enhance the creativity and empirical founding of LLMs-generated research. Specifically, MASS integrates three core components: dynamic goal-path planning with multi-level social norm restraint to guide the simulation, a multi-disciplinary behavior dataset for agent memory cold-start, and a structured forgetting mechanism inspired by the Ebbinghaus curve. Together, these ensure simulation authenticity and provide a robust empirical foundation for generating innovative scholarly papers. Experimental results demonstrate the effectiveness of our method, showing a 6.81\% improvement in generation overall quality over foundation LLMs and 17.19\% gain in Insight over strong baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有基于大型语言模型的深度研究（Deep Research）系统在社会科学研究中缺乏洞察力和创造力的核心问题。研究背景是，当前的大模型驱动的AI研究助手虽然在自动化论文写作方面展现出巨大潜力，但其运作机制高度依赖从互联网和本地知识库检索并合成现有文献。对于社会科学这一强调复杂性、实践性和主观性的领域，仅仅对既有文本进行再加工，无法产生源自理论与实证互动间的真正洞见。现有方法的不足在于，它们本质上只是文本的“检索-生成”循环，缺乏模拟真实社会情境、生成一手实证数据的能力，因此产出的研究通常“二手”且缺乏新意。为了打破这一局限，本文提出了“记忆增强的社会模拟”，通过构建一个高度逼真且以研究为导向的虚拟社会仿真环境，让大模型在动态目标规划、社会规范约束以及类人记忆遗忘机制的引导下，进行探索性的社会模拟实验。其核心目标是让系统能够生成原创的、经验性的“一手”数据，作为后续论文写作的实质性实证基础，从而彻底改变以往深度研究依赖“检索-生成”的范式，提升社会科学自动研究的创造力与实证支撑力。

### Q2: 有哪些相关研究？

相关研究主要分为三类。首先，**Deep Research Agent**领域从单智能体架构发展到多智能体分工、混合架构及端到端强化学习，本文区别于这些侧重通用任务架构优化的研究，专门为社会科学设计了创造性模拟范式以增强研究创新性。其次，**Agent行为与决策**研究包含静态规划、动态规划及双系统协同三种范式，本文在此基础上通过多级约束与动态目标规划增强了智能体自主性，实现了更灵活的决策交互。最后，**社会模拟**领域聚焦数据注入微调提升微观真实性、大型异步并行平台降低技术门槛、以及平均场理论减少计算成本三个方向，本文与之不同在于通过专用记忆增强模块减少长上下文开销并提升模拟真实性，该模块引入基于艾宾浩斯曲线的结构化遗忘机制，弥补了现有模拟研究在长期记忆优化方面的不足。总体而言，本文在方法层面综合了社会模拟的真实性需求与Deep Research Agent的创新性目标，形成了独特的研究路径。

### Q3: 论文如何解决这个问题？

这篇论文提出了基于记忆增强的社会模拟（MASS，Memory-Augmented Social Simulation）框架，以解决现有深度研究系统在社会科学中缺乏洞察力和创造力的问题。其核心方法是将传统的信息检索被动整合转变为通过社会模拟主动生成经验性洞察。

MASS的整体框架由三大核心模块组成，涵盖了从任务规划到论文生成的全流程。首先，在任务规划阶段，论文提出了**逐步最佳N（SW-BoN，Stepwise Best-of-N）策略**。该策略创新性地在每个推理步骤生成多个候选节点，通过阈值筛选和基于语义相似度的多智能体投票机制，选出全局最优路径，有效克服了长链推理中的“错误累积”问题并增强了发散思维。

规划完成后，系统调用关键的社会模拟实验工具。实验设计基于**ODD协议**（概述、设计概念、细节协议），并整合了**动态目标-路径规划**和**多层社会规范约束**。前者确保智能体行为紧扣研究主题，后者通过制度、道德和文化三个层次模拟真实社会环境，保障了模拟的真实性与可控性。

为了实现智能体的真实认知，论文构建了一个**多学科行为数据集（近30万条记录）**和基于**检索增强生成（RAG）的记忆冷启动机制**，为智能体赋予个性化初始记忆。进一步地，论文设计了受**艾宾浩斯曲线**启发的结构化遗忘机制，通过动态量化记忆强度、语义关联激活和概率性遗忘，模拟人类记忆演化过程，驱动智能体进行更贴近现实的决策。

最后，结构化写作模块基于SW-BoN的推理链节点，整合工具调用结果（包括社会模拟数据），并依据系统预设的学术模板生成结构完整、格式规范的论文初稿。这一“规划-执行-学习”闭环流程，使得生成的论文在严谨性基础上，系统性地实现了创新性提升，实验结果显示在整体质量上相较基础大语言模型提升6.81%，洞察力维度（Insight）上相较基线提升17.19%。

### Q4: 论文做了哪些实验？

论文实验围绕MASS框架的论文生成质量、社会模拟有效性、消融贡献和参数鲁棒性展开。实验设置采用Qwen3-30B作为基础模型，对比了DeepSeek-V3.1、GLM-4.6等大型LLM和Gemini Deep Research、通义Deep Research框架。使用DeepResearch Bench的社会科学子集进行评估，指标包括全面性、洞察力、指令遵循和可读性。MASS在整体质量上超越大型LLM平均6.81%，在洞察力维度超越比较平均17.19%。在社会模拟实验中，验证了“冲突是国家形成必要条件”的理论，发现领导者比例稳定后冲突资源投入降至10%以下；同时模拟了企业属性对合同纠纷解决策略的影响，发现法律意识强的企业更倾向法律途径。消融实验显示逐步移除MASS模块后整体得分下降，但洞察力提升。敏感性分析测试了agent属性生成完整性和遗忘概率，发现代码专用LLM能降低归一化均方根误差、提高皮尔逊相关系数，而合理范围内的遗忘调整仅引起微小波动。数据集评估显示94.21%数据通过幻觉检测，97.51%通过完整性评估，冷启动使动作合理性提升5.84%。

### Q5: 有什么可以进一步探索的点？

这篇论文在方法论上展现出巨大潜力，但仍有若干值得深化的方向。首先，**计算开销与效率**是当前主要瓶颈——高保真大规模社会模拟虽经并行优化，但资源消耗依然显著。未来可探索轻量级架构（如知识蒸馏的Agent模型）或弹性计算方案，并尝试将关键模拟模块离线预计算，以平衡实时性与成本。其次，**幻觉问题**分两层：一是在文本生成中模型可能捏造学术概念或数据，损害可信度；二是在模拟系统中Agent的决策与交互出现认知扭曲。除了依赖基础模型进步，可引入**外部知识校验**（如实时对接结构化数据库或专家系统）和**对抗验证**（通过反向Agent质疑生成结论）来抑制幻觉。此外，当前模拟主要依赖静态行为数据集冷启动，未来可考虑**跨文化参数差异**与**动态价值对齐**，使仿真更能反映真实社会复杂性。最后，实验评估侧重于生成质量，但对**模拟过程的可解释性**（如Agent决策轨迹可回溯）以及**生成论文的社会伦理审查**仍需加强，防止模拟结果被误用为政策建议。

### Q6: 总结一下论文的主要内容

这篇论文提出“记忆增强社会模拟（MASS）”范式，旨在解决大语言模型驱动的深度研究在社会科学领域缺乏洞察力和创造力的问题。当前系统过度依赖文献检索与综合，难以生成基于实证的新颖见解。MASS 通过构建高度真实的研究型社会模拟来增强LLM的创造力和实证基础。该方法包含三大核心组件：动态目标-路径规划与多级社会规范约束以引导模拟、跨学科行为数据集用于智能体记忆冷启动、以及基于艾宾浩斯曲线的结构化遗忘机制。这些组件共同确保了模拟的真实性，为生成创新学术论文提供了坚实的实证基础。实验结果表明，MASS 在生成质量上相比基础LLM提升6.81%，在洞察力指标上相比强基线提升17.19%。该工作为社会科学领域的深度自动化研究开辟了新途径。
