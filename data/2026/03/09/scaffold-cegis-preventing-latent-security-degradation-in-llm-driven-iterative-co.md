---
title: "SCAFFOLD-CEGIS: Preventing Latent Security Degradation in LLM-Driven Iterative Code Refinement"
authors:
  - "Yi Chen"
  - "Yun Bian"
  - "Haiquan Wang"
  - "Shihao Li"
  - "Zhe Cui"
date: "2026-03-09"
arxiv_id: "2603.08520"
arxiv_url: "https://arxiv.org/abs/2603.08520"
pdf_url: "https://arxiv.org/pdf/2603.08520v1"
categories:
  - "cs.CR"
  - "cs.SE"
tags:
  - "代码智能体"
  - "迭代优化"
  - "多智能体协作"
  - "安全与鲁棒性"
  - "工具使用"
  - "代码生成"
relevance_score: 7.5
---

# SCAFFOLD-CEGIS: Preventing Latent Security Degradation in LLM-Driven Iterative Code Refinement

## 原始摘要

The application of large language models to code generation has evolved from one-shot generation to iterative refinement, yet the evolution of security throughout iteration remains insufficiently understood. Through comparative experiments on three mainstream LLMs, this paper reveals the iterative refinement paradox: specification drift during multi-objective optimization causes security to degrade gradually over successive iterations. Taking GPT-4o as an example, 43.7 % of iteration chains contain more vulnerabilities than the baseline after ten rounds, and cross-model experiments show that this phenomenon is prevalent. Further analysis shows that simply introducing static application security testing (SAST) gating cannot effectively suppress degradation; instead, it increases the latent security degradation rate from 12.5% under the unprotected baseline to 20.8 %. The root cause is that static-analysis rules cannot cover structural degradations such as the removal of defensive logic or the weakening of exception handling. To address this problem, we propose the SCAFFOLD-CEGIS framework. Drawing on the counterexample-guided inductive synthesis (CEGIS) paradigm, the framework adopts a multi-agent collaborative architecture that transforms security constraints from implicit prompts into explicit verifiable constraints. It automatically identifies and solidifies security-critical elements as hard constraints through semantic anchoring, enforces safety monotonicity through four-layer gated verification, and continuously assimilates experience from failures. Comparative experiments against six existing defense methods show that the full framework reduces the latent security degradation rate to 2.1% and achieves a safety monotonicity rate of 100%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型在迭代式代码生成与优化过程中，代码安全性可能随着迭代轮次增加而逐渐退化的问题。研究背景是，随着AI编程助手（如GitHub Copilot）的普及，开发流程已从单次代码生成演变为多轮交互式迭代优化，但现有研究主要关注单次生成的质量，对迭代过程中安全属性的演变缺乏深入理解。现有方法（如基于静态应用安全测试的检测门控）存在明显不足：静态分析规则依赖于已知漏洞模式，无法有效检测“潜在安全退化”，例如防御性逻辑被移除、异常处理被削弱等结构性退化，这些退化不会触发规则匹配，甚至可能因引入SAST门控而加剧退化率。本文要解决的核心问题是：如何在大模型驱动的多轮代码迭代中，防止因多目标优化导致的规范漂移，从而确保代码安全性不会在迭代过程中隐性下降。为此，论文提出了SCAFFOLD-CEGIS框架，通过将安全约束从隐式提示转化为显式可验证的硬约束，并采用语义锚定、四层门控验证等机制，来强制保证安全性的单调递增，从根本上抑制潜在安全退化。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三大类：**LLM代码生成的安全性评估研究**、**LLM代码生成的安全缓解方法**以及**迭代式程序综合**。

在**安全性评估研究**方面，已有大量工作关注LLM生成代码的漏洞引入倾向和提示词鲁棒性。例如，Perry等人通过用户研究发现开发者易接受不安全的建议；Siddiq等人通过SALLM基准量化了SQL注入等场景中的安全风险；Hajipour等人的CodeLM-Sec则使用对抗性提示模板进行压力测试。这些研究揭示了单次生成中的安全隐患，但主要进行静态的“生成-检测”分析，未能充分考察多轮迭代中安全属性的动态演变，这正是本文要深入探讨的“迭代精化悖论”的起点。

在**安全缓解方法**上，现有研究主要分为推理时对齐（如使用静态分析反馈、约束解码）和数据/训练对齐（如使用高质量安全代码数据集进行指令微调）。然而，这些方法大多针对单次生成，且依赖的静态分析规则难以覆盖结构性退化（如防御逻辑的移除）。本文指出，简单地引入静态应用安全测试（SAST）门控甚至会加剧潜在安全退化，这凸显了现有缓解策略的不足。

在**迭代式程序综合**领域，传统方法如反例引导的归纳综合（CEGIS）和语法引导综合（SyGuS）依赖形式化验证器提供精确反例和强约束。LLM驱动的迭代机制则多体现为自我调试或多智能体协作（如Reflexion框架），但其反馈主要源于功能正确性（如编译、单元测试），缺乏对安全属性的形式化约束。本文提出的SCAFFOLD-CEGIS框架正是借鉴了CEGIS范式，将安全约束从隐式提示转化为显式可验证约束，以解决现有迭代合成中因安全反馈薄弱而导致的目标漂移问题。

### Q3: 论文如何解决这个问题？

论文通过提出SCAFFOLD-CEGIS框架来解决迭代代码精化中潜在安全退化的问题。其核心方法是借鉴反例引导的归纳合成（CEGIS）范式，采用多智能体协作架构，将安全约束从隐式的提示词转化为显式的可验证约束，并通过四层门控验证强制实现安全单调性。

整体框架包含四个协同工作的智能体：1) **SecurityArchitectAgent**：从代码中挖掘安全关键元素（如关键函数、API签名、防御模式），构建并动态更新语义锚点集合Φ，作为硬性约束。2) **ImplementerAgent**：在锚点约束下生成候选代码。3) **GatekeeperAgent**：执行四层门控验证，包括正确性（测试套件）、安全单调性（静态分析漏洞数对比）、差异预算（限制单次变更规模）和锚点完整性（验证锚点是否被破坏）。4) **AssimilatorAgent**：分析验证失败的尝试，提取结构化经验（如修复规则）反馈给后续迭代。

关键技术包括：**语义锚定**，通过命名约定、数据流分析和模式匹配自动识别并固化安全关键代码元素，防止其在迭代中被意外删除或削弱。**四层门控验证**，确保每次迭代都满足正确性且不引入新的可检测漏洞（当δ_max设为0时，保证漏洞数单调不增）。**经验同化机制**，从失败中学习并生成自然语言反馈，动态调整锚点集的优先级和约束强度，实现约束与代码的共同演化。

创新点在于将形式化方法中的CEGIS思想适配到实际软件工程场景，用静态分析和语义锚点检查替代传统的SMT求解器，以实用性换取形式化完备性，从而处理难以完全形式化的安全属性。该框架将安全要求从隐式、模糊的提示，转变为显式、可自动验证的约束系统，从根本上抑制了因多目标优化导致的规范漂移和安全退化。

### Q4: 论文做了哪些实验？

论文围绕三个研究问题设计了多阶段实验。实验设置上，研究使用三种主流大语言模型（GPT-4o、GPT-5-Nano、Claude Sonnet 4.5、DeepSeek-V3），在统一的提示模板和温度设置（T=0.7）下，对涵盖数据库操作、输入处理、认证、资源管理、密码学和路径处理等六个安全场景的24个编程任务样本（Python和Java各半）进行迭代精炼，每个迭代链运行10轮，涉及功能增强、性能优化、安全强化和模糊需求四种策略，共生成288个链和2880个迭代步骤。

数据集为自包含的单文件模块，代码行数（LOC）范围25-392，圈复杂度（CC）范围4-145，每个样本包含5-20个测试用例。评估使用了Claude Opus 4.5作为独立的LLM语义评审员来检测静态分析覆盖之外的潜在安全缺陷。

对比方法包括：无保护的基线、提示集成安全、自优化、事后SAST、测试驱动门控和混合门控。主要结果如下：
1.  **迭代精炼悖论验证（RQ1）**：所有模型均出现不同程度的安全退化。以GPT-4o为例，10轮迭代后43.7%的链比基线包含更多漏洞。跨模型实验中，GPT-5-Nano的整体退化率（DR）最高（10.5%），DeepSeek-V3在Python任务上DR为0%，但所有模型的可靠性退化率（RDR）均较高（42.5%-52.5%），表明静态分析指标无法充分反映可靠性退化。
2.  **SCAFFOLD-CEGIS有效性（RQ2）**：与六种基线方法相比，完整框架将潜在安全退化率（SSDR）从基线的12.5%降至2.1%，实现了100%的安全单调性率（SMR），并在静态分析指标上达到0%的退化率（DR）和-0.04的平均漏洞变化（ΔV）。值得注意的是，事后SAST方法虽然DR为0%，但SSDR高达20.8%，甚至高于无保护基线，揭示了伪安全效应。
3.  **消融分析（RQ3）**：通过配置基线、完整框架、仅锚定、仅门控和无同化等版本，验证了语义锚定、门控验证和失败同化各机制对降低潜在安全退化的独立贡献。关键数据指标包括：退化率（DR）、安全单调性率（SMR）、潜在安全退化率（SSDR）、代码演进量（CEV）等。

### Q5: 有什么可以进一步探索的点？

该论文揭示了迭代优化中安全性的隐性退化问题，并提出了SCAFFOLD-CEGIS框架作为解决方案，但仍存在一些局限性和可进一步探索的方向。首先，框架依赖形式化验证和语义锚定，其可扩展性可能受限于复杂代码结构或新兴漏洞类型，未来需研究如何降低验证开销并提升对未知漏洞模式的泛化能力。其次，实验主要针对特定LLM和代码任务，未来可扩展到更多模型、编程语言及真实开发场景，以检验其普适性。此外，论文指出SAST门控会加剧隐性退化，这启发我们思考如何更智能地平衡功能优化与安全约束，例如引入动态分析或模糊测试进行补充。最后，多智能体协作架构虽提升了安全性，但可能影响迭代效率，未来可探索自适应约束松弛机制，在安全与效率间寻求更优平衡。

### Q6: 总结一下论文的主要内容

本文揭示了大型语言模型在迭代式代码生成中的安全退化现象，即“迭代精炼悖论”：在多目标优化过程中，规格漂移导致安全漏洞随迭代轮次逐渐增加。研究发现，即使引入静态应用安全测试（SAST）门控，也无法有效抑制退化，反而可能因无法覆盖防御逻辑移除或异常处理弱化等结构性退化，加剧潜在安全风险。

为解决此问题，论文提出了SCAFFOLD-CEGIS框架。该方法借鉴反例引导的归纳合成（CEGIS）范式，采用多智能体协作架构，将安全约束从隐式提示转化为显式可验证约束。其核心是通过语义锚定自动识别并固化安全关键元素作为硬约束，利用四层门控验证强制安全性单调递增，并持续从失败中吸收经验。

实验表明，该框架将潜在安全退化率从基准的12.5%降至2.1%，并实现了100%的安全性单调率，显著优于六种现有防御方法。这一工作为LLM驱动的代码迭代提供了可靠的安全保障框架，对提升自动化代码生成的实际部署安全性具有重要意义。
