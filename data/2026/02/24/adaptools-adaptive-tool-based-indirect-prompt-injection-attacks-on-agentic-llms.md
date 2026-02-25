---
title: "AdapTools: Adaptive Tool-based Indirect Prompt Injection Attacks on Agentic LLMs"
authors:
  - "Che Wang"
  - "Jiaming Zhang"
  - "Ziqi Zhang"
  - "Zijie Wang"
  - "Yinghui Wang"
  - "Jianbo Gao"
  - "Tao Wei"
  - "Zhong Chen"
  - "Wei Yang Bryan Lim"
date: "2026-02-24"
arxiv_id: "2602.20720"
arxiv_url: "https://arxiv.org/abs/2602.20720"
pdf_url: "https://arxiv.org/pdf/2602.20720v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Security"
  - "Tool Use"
  - "Prompt Injection"
  - "Adversarial Attack"
  - "Agent Evaluation"
  - "LLM Agents"
relevance_score: 8.0
---

# AdapTools: Adaptive Tool-based Indirect Prompt Injection Attacks on Agentic LLMs

## 原始摘要

The integration of external data services (e.g., Model Context Protocol, MCP) has made large language model-based agents increasingly powerful for complex task execution. However, this advancement introduces critical security vulnerabilities, particularly indirect prompt injection (IPI) attacks. Existing attack methods are limited by their reliance on static patterns and evaluation on simple language models, failing to address the fast-evolving nature of modern AI agents. We introduce AdapTools, a novel adaptive IPI attack framework that selects stealthier attack tools and generates adaptive attack prompts to create a rigorous security evaluation environment. Our approach comprises two key components: (1) Adaptive Attack Strategy Construction, which develops transferable adversarial strategies for prompt optimization, and (2) Attack Enhancement, which identifies stealthy tools capable of circumventing task-relevance defenses. Comprehensive experimental evaluation shows that AdapTools achieves a 2.13 times improvement in attack success rate while degrading system utility by a factor of 1.78. Notably, the framework maintains its effectiveness even against state-of-the-art defense mechanisms. Our method advances the understanding of IPI attacks and provides a useful reference for future research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能代理（Agent）在集成外部数据服务（如模型上下文协议MCP）时所面临的新型安全威胁——间接提示注入（IPI）攻击。研究背景是，随着GPT、Gemini等前沿模型的发展，AI代理通过MCP等协议调用外部API和资源的能力大大增强，广泛应用于编码助手等场景以提升生产力。然而，这种能力扩展也引入了严重的安全漏洞：攻击者可以在代理访问的网站或数据库等中间服务器中注入恶意指令，从而诱使代理执行数据泄露等未授权行为。由于MCP服务器生态快速扩张且缺乏标准化安全审计，攻击面正在迅速扩大。

现有攻击方法的不足在于，它们主要依赖静态的、模式化的恶意提示（例如“忽略之前指令…”），并且多在能力较简单的语言模型上进行评估。论文指出，面对现代具备多步推理能力的强大LLM代理，这些方法无法同时满足成功攻击所需的“三重约束”：**鲁棒性**（在代理内部认知审查下维持恶意影响）、**适应性**（能动态变异以绕过不断演进的安全过滤器与干扰检测）以及**隐蔽性**（能选择与用户任务上下文语义对齐的恶意工具，避免被内部逻辑审计标记为异常）。现有方法在这些方面存在缺陷，难以应对快速演进的AI代理。

因此，本文要解决的核心问题是：如何构建一种**自适应的、隐蔽且鲁棒的间接提示注入攻击框架**，以更真实地模拟现实世界中的对手，并对快速发展的推理型LLM代理进行严格的安全评估。为此，论文提出了AdapTools框架，它包含自适应攻击策略构建和攻击增强两个关键组件，旨在动态选择隐蔽工具并生成自适应攻击提示，以克服上述三重约束，从而揭示当前代理系统的深层安全漏洞并推动更强防御机制的研究。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕间接提示注入（IPI）攻击及其防御方法展开，可分为攻击方法与防御方法两大类。

在**攻击方法**方面，现有研究主要提出了几种典型的IPI攻击模式，例如利用换行符等特殊符号改变上下文解析的“转义字符攻击”、指令模型忽略先前上下文的“上下文忽略攻击”，以及整合多种策略的“组合攻击”。特别是AutoHijacker工作，采用了LLM-as-Optimizer机制来生成更具鲁棒性的攻击提示，突破了静态模式的限制。此外，也有研究致力于构建评估智能体抗IPI攻击能力的基准测试。然而，本文指出，现有攻击方法大多依赖静态模式，且评估多基于非推理型LLM和单轮静态交互，其评估样本高度依赖人工构建，难以应对现代AI智能体快速演变的特性。本文提出的AdapTools框架与这些工作的核心区别在于其**自适应性**：它通过选择更隐蔽的攻击工具并生成自适应攻击提示，构建了动态、严格的评估环境，从而更有效地模拟现实威胁。

在**防御方法**方面，相关工作可分为输入级（预检测）和输出级（后检测）两类。输入级防御包括指令预防、数据提示隔离和三明治预防等静态的、基于规则的方法，旨在引导LLM忽略外部数据中嵌入的指令，或使用分类器识别潜在恶意指令。输出级防御则包括微调检测模型来识别输出中的恶意内容，以及如MELON和困惑度过滤等无需训练、基于启发式规则的方法。本文的AdapTools框架在实验中对这些先进的防御机制仍保持了攻击有效性，这凸显了现有静态或规则型防御在面对自适应、隐蔽攻击时的局限性，从而强调了开发更强大防御方案的迫切性。

### Q3: 论文如何解决这个问题？

AdapTools 通过一个自适应的间接提示注入攻击框架来解决现有方法依赖静态模式、难以应对快速演进的智能体的问题。其核心方法包含两个协同工作的模块：自适应攻击策略构建模块和攻击增强模块，整体架构旨在实现攻击的适应性和隐蔽性。

**整体框架与主要模块：**
框架首先将基于LLM的智能体形式化为一个通过工具和外部接口（如MCP服务器）编排工作流的自主系统。攻击者的目标是在智能体查询外部数据时，将恶意提示注入返回的观测内容中，从而最大化智能体执行特定恶意工具的概率。

1.  **自适应攻击模块（指令优化）：** 该模块旨在自主构建和优化攻击策略库，以应对“红鲱鱼”和“安全风险”等失败模式。其核心是**自适应策略生成器**和**策略蒸馏**组件。
    *   **自适应策略生成：** 受对抗训练启发，该过程是迭代的。攻击者首先从工具集中随机选择一个高权限目标工具。然后，从策略库中检索（或初始时基于工具描述生成）相关策略，结合用户任务，输入到一个攻击提示生成器（一个对抗性LLM）中，合成攻击提示。将此提示注入良性返回内容后，观察智能体是否执行目标工具。若攻击失败，则利用分析器（一个商用LLM）诊断失败原因（如分析智能体的思维链），并据此进化策略，进行多轮迭代优化。成功的策略会被存入策略库。
    *   **策略蒸馏：** 为解决策略库随工具-任务组合增多而出现的可扩展性差和泛化能力有限的问题，该组件对策略库进行压缩和泛化。首先，使用文本嵌入模型将离散的文本策略转化为潜在语义向量，并通过聚类技术（如K-means）将语义相似的策略分组，抽象出高级别的策略模式。接着，采用基于攻击成功率（ASR）的度量进行剪枝合并，仅当合并导致的ASR下降不超过预设阈值时，才将策略子集合并为更通用的形式，从而构建一个精简、可迁移的策略库。

2.  **攻击增强模块（自适应工具选择）：** 该模块针对“无关信息”失败模式，通过选择语义上更隐蔽的攻击工具来提升攻击成功率。其关键在于**马尔可夫转移建模**与**联合优化工具选择**。
    *   **马尔可夫转移建模：** 假设攻击者（如恶意的MCP控制器）能观察到最近调用的工具，该方法利用一阶马尔可夫链对工具执行的时序模式进行建模，从所有良性轨迹中学习工具间的转移概率矩阵。
    *   **联合优化工具选择：** 攻击工具的选择被构建为一个双约束优化问题。首先，基于转移概率矩阵预测在无攻击情况下，智能体下一步最可能调用的良性工具。然后，为了保持语义连续性，从工具集中选择一个与该预测工具语义相似度最高的工具作为攻击工具。这确保了恶意动作在时间和内容上都与良性推理流难以区分。

**创新点：**
*   **动态自适应的攻击策略生成与进化：** 通过分析智能体失败反馈（如思维链）来迭代优化攻击策略，实现了无需人工标注的、持续更新的攻击方法，能够适应快速演进的LLM智能体。
*   **策略库的蒸馏与泛化：** 引入策略蒸馏过程，将细粒度策略抽象和压缩为可迁移的通用模式，解决了策略库的扩展性和跨任务泛化问题。
*   **基于语义与时序一致性的隐蔽工具选择：** 创新性地结合马尔可夫链（捕捉时序模式）和语义相似度计算，选择与当前任务上下文高度对齐的攻击工具，显著提高了攻击的隐蔽性，能够绕过基于任务相关性的

### Q4: 论文做了哪些实验？

论文实验设置基于ReAct框架，针对基于大型语言模型（LLM）的智能体进行间接提示注入（IPI）攻击评估。实验使用了六个基础LLM构建代理系统，包括开源模型（Qwen-3-8B、LLaMA-3.1-8B、Mistral-8B）和商业模型（GPT-4.1、DeepSeek-R1、Gemini-2.5-Flash），涵盖推理导向和通用模型，均支持工具调用机制。

实验采用三个数据集：主要数据集IPI-3k（论文引入），以及InjectAgent和AgentDojo。对比方法包括多种攻击基线：基于前缀的提示攻击（Ignore Instruction、Combined Attack）、InjectAgent和Autohijacker；防御基线则采用两种最先进的方法MELON和Pi-Detector，覆盖输入级和输出级检测策略。

主要结果显示，AdapTools在攻击成功率（ASR）上显著优于所有基线。在商业LLM上，其平均ASR比最佳基线提高2.13倍，例如GPT-4.1的基线平均ASR低于8%，而AdapTools达到18.5%；Gemini-2.5-Flash上为25.9% vs. 9.2%。开源模型防御能力较弱，平均ASR超过30%，其中Mistral-8B的ASR达49.0%。同时，攻击导致系统效用（UA）平均下降1.78倍，例如GPT-4.1的UA从66.0%降至49.6%。在防御机制下，AdapTools仍保持较强鲁棒性，ASR下降幅度（约2倍）小于基线（至少3倍）。迁移性实验表明，在InjectAgent数据集上，AdapTools的ASR优于Autohijacker（GPT-4.1上提高3.6%，Qwen3-8B上提高6.5%）。消融实验验证了工具选择模块的有效性，使GPT-4.1和Qwen3-8B的ASR分别提升4.7%和7.9%。策略分析显示，通过5轮迭代优化，ASR可从单次迭代的35%提升至80%以上并收敛。

### Q5: 有什么可以进一步探索的点？

该论文在自适应工具选择和提示生成方面取得了进展，但仍有进一步探索的空间。局限性在于攻击框架主要针对已知防御机制进行优化，对于未来可能出现的新型、动态防御策略（如实时行为监控或多模态验证）的鲁棒性尚未验证。此外，实验集中在文本型代理场景，对多模态或跨平台集成代理的适用性有待考察。

未来研究方向可包括：一是扩展攻击的泛化能力，研究如何使自适应策略无需重新训练即可应对未知防御机制；二是探索更隐蔽的攻击形式，例如利用时间延迟或上下文累积效应实施长期潜伏性注入；三是结合对抗性机器学习，开发能同时欺骗工具检测和语义分析的混合攻击方法。从防御视角出发，该框架也可反向用于构建动态防御基准，通过模拟自适应攻击来迭代强化代理系统的安全性。

### Q6: 总结一下论文的主要内容

该论文针对基于大型语言模型的智能代理在集成外部数据服务（如MCP）时面临的安全风险，提出了一个名为AdapTools的自适应工具间接提示注入攻击框架。核心问题是现有攻击方法依赖静态模式且仅在简单模型上评估，难以应对现代AI代理的快速演进，导致安全评估不足。

论文的核心贡献在于设计了一种动态、自适应的攻击策略。方法主要包括两部分：一是自适应攻击策略构建，通过可迁移的对抗策略优化攻击提示；二是攻击增强，识别能够绕过任务相关性防御的隐蔽工具。该方法通过选择更隐蔽的攻击工具并生成自适应攻击提示，构建了更严格的安全评估环境。

实验表明，AdapTools将攻击成功率提升了2.13倍，同时使系统效用降低了1.78倍，且在面对先进防御机制时仍保持有效。主要结论是该方法不仅深化了对间接提示注入攻击的理解，也为未来相关安全研究提供了重要参考。
