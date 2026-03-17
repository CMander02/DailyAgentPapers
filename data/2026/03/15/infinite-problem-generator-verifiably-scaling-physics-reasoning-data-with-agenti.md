---
title: "Infinite Problem Generator: Verifiably Scaling Physics Reasoning Data with Agentic Workflows"
authors:
  - "Aditya Sharan"
  - "Sriram Hebbale"
  - "Dhruv Kumar"
date: "2026-03-15"
arxiv_id: "2603.14486"
arxiv_url: "https://arxiv.org/abs/2603.14486"
pdf_url: "https://arxiv.org/pdf/2603.14486v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agentic Workflow"
  - "Data Synthesis"
  - "Reasoning"
  - "Physics"
  - "Verification"
  - "Curriculum Generation"
  - "Tool Use"
relevance_score: 7.5
---

# Infinite Problem Generator: Verifiably Scaling Physics Reasoning Data with Agentic Workflows

## 原始摘要

Training large language models for complex reasoning is bottlenecked by the scarcity of verifiable, high-quality data. In domains like physics, standard text augmentation often introduces hallucinations, while static benchmarks lack the reasoning traces required for fine-tuning. We introduce the Infinite Problem Generator (IPG), an agentic framework that synthesizes physics problems with guaranteed solvability through a Formula-as-Code paradigm. Unlike probabilistic text generation, IPG constructs solutions as executable Python programs, enforcing strict mathematical consistency. As a proof-of-concept, we release ClassicalMechanicsV1, a high-fidelity corpus of 1,335 classical mechanics problems expanded from 165 expert seeds. The corpus demonstrates high structural diversity, spanning 102 unique physical formulas with an average complexity of 3.05 formulas per problem. Furthermore, we identify a Complexity Blueprint, demonstrating a strong linear correlation ($R^2 \approx 0.95$) between formula count and verification code length. This relationship establishes code complexity as a precise, proxy-free metric for problem difficulty, enabling controllable curriculum generation. We release the full IPG pipeline, the ClassicalMechanicsV1 dataset, and our evaluation report to support reproducible research in reasoning-intensive domains.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在复杂推理领域（特别是物理学）训练时面临的高质量、可验证数据稀缺的核心瓶颈问题。研究背景是，尽管大语言模型在通用语言任务上表现出色，但像物理学这样需要严谨多步演绎的领域，其训练数据无法从网络规模语料库中充分获取。现有方法存在明显不足：标准的文本增强方法容易产生事实幻觉，而现有的静态基准数据集（如JEEBench）主要用于模型测试，缺乏大规模、多样化且包含可执行推理链条的训练用数据，这造成了训练与测试之间的鸿沟。

本文要解决的核心问题是：如何可扩展地生成大量数学上正确、逻辑严谨且包含可验证解决方案的物理问题数据，以用于训练可靠的推理模型。为此，论文提出了“无限问题生成器”这一智能体框架。该框架的核心创新在于采用“公式即代码”范式，将物理方程转化为可执行的Python函数，并通过程序思维验证机制，确保每个生成的问题都能由自动生成的脚本正确求解，从而从根本上保证了生成数据的数学一致性和可验证性，避免了传统文本生成方法中的幻觉问题。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为方法类、应用与评测类两大类。

在方法类研究中，自动问题生成（AQG）经历了从基于模板的刚性系统到灵活神经方法的转变。近期研究利用LLMs的生成先验，采用了回译、规划优先流程和基于摘要的过滤等策略，但它们大多依赖非结构化文本语料库，在需要精确初始条件的物理领域难以保持逻辑一致性。本文的IPG框架则基于专家编写的种子问题，通过受控的逻辑变体进行系统性扩展，而非语言扰动。此外，以PAL和PoT为代表的程序思维（PoT）范式将逻辑卸载到Python解释器以减少计算错误。近期工作开始使用执行来过滤合成数据，但通常仅将其作为事后过滤器。本文的创新在于将PoT直接集成到生成循环中，利用执行轨迹来驱动扩展本身，从而确保每个生成的变体不仅在语法上有效，而且在设计上就是数学可执行的。

在应用与评测类研究中，已有基准如JEEBench、UGPhysics和PhysicsEval充分记录了LLMs在物理推理上的脆弱性。然而，这些基准主要用于评估而非教学，它们提供问题和最终答案，但缺乏用于微调模型进行逐步推理所需的密集代码轨迹。本文的工作通过提供包含中间代码表示的“训练就绪”数据集填补了这一空白。具体到数据生成，相关工作如MathGenie和MetaMath成功扩展了数学数据，但可能产生结构重复或缺乏物理背景的变体。本文首次将基于种子的扩展与可执行验证相结合并专门应用于物理领域，确保了结构多样性和严格的正确性。

### Q3: 论文如何解决这个问题？

论文通过提出“无限问题生成器”（IPG）这一智能体化合成数据框架来解决高质量、可验证推理数据稀缺的问题。其核心方法是采用“生成-验证”范式，将物理公式编码为可执行的Python函数（公式即代码），从而确保生成问题的数学一致性和可解性。

整体框架分为三个阶段：问题分析、约束生成和基于代码的验证。在问题分析阶段，IPG解析专家编写的种子问题（包含问题与参考答案），提取其核心物理原理，并通过预定义的“章节词典”映射到相关的课程单元，形成一个可用的“可执行公理库”。同时，它构建一个包含变量单位及有效物理范围（如质量>0）的变量字典，以指导后续参数采样。

在约束生成阶段，IPG基于分析得到的逻辑上下文（如物理场景集合和可用公式库）生成多个问题变体。它采用“叙事轮询”策略，循环使用不同的现实场景（如将滑轮问题映射到轮胎旋转、磁带卷轴等）来创造叙事多样性，同时严格限定每个问题只能使用选定的可执行公理求解，防止隐含依赖。每个问题被赋予一个由所用公理ID和目标变量构成的“问题签名”，用于检测和拒绝重复。复杂度通过控制每个问题实例使用的公理数量（例如3到5个）来管理，以鼓励多步骤推理和跨章节整合。

最具创新性的关键技术是代码验证阶段。IPG要求为每个生成的问题配套生成一个可执行的Python解决方案，该方案只能调用可执行公理库中的函数。代码在沙箱环境中执行，必须通过三项验证：语法有效性（无运行时错误）、数值可解性（输出为有限值）和物理合理性（结果符合基本符号和量级约束）。验证失败会触发内部重试循环，利用执行反馈进行针对性修正。这种设计将问题难度与验证代码长度强关联（论文中称为“复杂度蓝图”），使得代码复杂度成为问题难度的精确、无需代理的度量指标，从而支持可控的课程生成。

IPG的创新点在于：1) 采用“公式即代码”范式，将物理知识表示为可执行函数，从根本上强制数学一致性，避免了传统文本增强中的幻觉问题；2) 设计了一个结构化的、多阶段的智能体工作流，明确分离了叙事变化与数值推理，并集成了运行时验证与反馈循环，确保了生成数据的高保真度和可验证性；3) 通过问题签名和复杂度控制机制，实现了生成问题的去重和难度可控的多样化扩展。

### Q4: 论文做了哪些实验？

论文实验主要包括数据集构建、质量评估和对比分析。实验设置上，研究者从《Concepts of Physics》中精选了165个经典力学问题作为种子，利用Gemini 2.5 Pro将物理公式转化为可执行的Python库（Formula-as-Code），并通过基于Gemini 2.5 Flash的智能体工作流（IPG）生成新问题。作为对比，使用相同基础模型但无迭代验证的单提示方法生成了包含1,650个问题的基线数据集。评估的数据集为生成的ClassicalMechanicsV1语料库（包含1,335个问题），并使用了多个内在指标：有效执行率（生成代码成功输出有限非空数值的比例）、物理合理性（过滤不现实数值）、签名唯一性（唯一公式集与未知变量组合的比例）以及词汇多样性（TTR，达5.94）。此外，利用Gemini 3作为独立评判者，按照问题所需公式数量分层进行压力测试（0-1、2-3、4-6公式）。

主要结果显示：1）生成数据集中问题所需公式数量呈高斯分布，众数为3（占57.5%），深度推理问题（4-6公式）有260个；2）发现了“复杂性蓝图”，即公式数量与验证代码长度呈强线性相关（R² ≈ 0.953），每增加一个公式代码长度约增加250字符；3）在可靠性区域（2-3公式），问题有效性超过99%，主要“错误”是包含未使用变量（约12%）；而在脆弱性区域（4+公式），错误转向签名不匹配（约15%），揭示了LLM在长程变量跟踪上的局限；4）领域混合方面，生成问题成功打破了章节边界，例如刚体动力学使用了53个独特公式，远超其原生库的20个，表明生成了综合性的物理问题。

### Q5: 有什么可以进一步探索的点？

该论文提出的IPG框架在保证物理问题数学正确性方面取得了进展，但仍存在多方面的局限性，为未来研究提供了丰富的探索方向。首先，在语义一致性方面，当前的程序验证主要确保数值和单位正确，但无法完全保证物理情景的合理性（如产生不切实际的加速度）。未来可集成形式化约束求解器（如Z3）来严格强制执行能量守恒等物理定律，或引入基于物理仿真的验证模块，以提升生成问题的物理可信度。其次，框架目前仅限于文本-代码模态，缺乏视觉图表生成能力。随着多模态推理模型的发展，扩展IPG以程序化生成配套示意图（如使用TikZ或SVG）将是一个重要方向，尤其对于涉及几何或空间关系的问题至关重要。再者，领域扩展性方面，当前工作集中于经典力学，未来需构建更广泛的公理库以覆盖电磁学、光学等领域，并探索如何处理连续场问题。同时，当前的“公式即代码”范式擅长代数推理，但尚未涵盖基于微积分的第一性原理推导或几何直觉建模，这限制了其处理更抽象物理概念的能力。此外，生成-验证范式计算成本较高，未来可通过训练轻量级可解性预测器或利用小型模型进行过滤，以提升生成效率。最后，论文提出的“复杂度蓝图”为可控课程生成提供了新思路，未来可基于此开发自适应评估系统，动态组装难度可控的问题集，用于个性化教育或智能辅导系统。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型在复杂推理任务中高质量、可验证数据稀缺的瓶颈问题，提出了一种名为“无限问题生成器”的智能体框架，用于生成可验证的物理推理数据。其核心贡献在于通过“公式即代码”的范式，将问题解决方案构建为可执行的Python程序，从而严格保证数学一致性，避免了传统文本增强方法可能产生的幻觉。作为概念验证，作者发布了包含1,335个经典力学问题的数据集，该数据集由165个专家种子扩展而来，具有高度的结构多样性。论文的主要结论是发现了“复杂性蓝图”，即公式数量与验证代码长度之间存在强线性相关性，这使得代码复杂度可以作为一个精确、无需代理的难度度量指标，从而支持可控的课程生成。该工作为推理密集型领域的研究提供了可复现的数据生成管道和高质量数据集。
