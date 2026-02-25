---
title: "Watermarking LLM Agent Trajectories"
authors:
  - "Wenlong Meng"
  - "Chen Gong"
  - "Terry Yue Zhuo"
  - "Fan Zhang"
  - "Kecen Li"
  - "Zheng Liu"
  - "Zhou Yang"
  - "Chengkun Wei"
  - "Wenzhi Chen"
date: "2026-02-21"
arxiv_id: "2602.18700"
arxiv_url: "https://arxiv.org/abs/2602.18700"
pdf_url: "https://arxiv.org/pdf/2602.18700v1"
categories:
  - "cs.CR"
  - "cs.CL"
tags:
  - "Agent 安全"
  - "Agent 数据合成"
  - "Agent 评测/基准"
  - "版权保护"
  - "水印技术"
relevance_score: 7.5
---

# Watermarking LLM Agent Trajectories

## 原始摘要

LLM agents rely heavily on high-quality trajectory data to guide their problem-solving behaviors, yet producing such data requires substantial task design, high-capacity model generation, and manual filtering. Despite the high cost of creating these datasets, existing literature has overlooked copyright protection for LLM agent trajectories. This gap leaves creators vulnerable to data theft and makes it difficult to trace misuse or enforce ownership rights. This paper introduces ActHook, the first watermarking method tailored for agent trajectory datasets. Inspired by hook mechanisms in software engineering, ActHook embeds hook actions that are activated by a secret input key and do not alter the original task outcome. Like software execution, LLM agents operate sequentially, allowing hook actions to be inserted at decision points without disrupting task flow. When the activation key is present, an LLM agent trained on watermarked trajectories can produce these hook actions at a significantly higher rate, enabling reliable black-box detection. Experiments on mathematical reasoning, web searching, and software engineering agents show that ActHook achieves an average detection AUC of 94.3 on Qwen-2.5-Coder-7B while incurring negligible performance degradation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决LLM智能体轨迹数据的版权保护问题。当前，高质量轨迹数据（即智能体成功执行任务时的动作序列记录）的创建成本极高，涉及大量任务设计、大模型生成和人工筛选，但现有研究却忽视了这类数据的版权保护。这导致数据创建者面临数据被盗用、难以追踪滥用行为或维护所有权等风险。为此，论文提出了首个针对智能体轨迹数据集的水印方法ActHook，其核心是通过在轨迹中嵌入“钩子动作”来植入可检测的水印。这些钩子动作仅在特定密钥触发时激活，且不改变原始任务结果，从而允许数据创建者通过检测模型输出中钩子动作的出现频率，来可靠地追溯模型是否使用了其受版权保护的数据进行训练。该方法有效弥补了现有通用文本或代码水印技术无法适应智能体轨迹序列化、多步结构及小规模数据集特点的不足。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及三个领域：LLM智能体与轨迹、LLM水印技术以及软件钩子机制。

在**LLM智能体与轨迹**方面，相关工作包括：早期智能体使用JSON格式动作（如ToolFormer），而现代系统更多采用可执行代码作为动作以支持复杂逻辑（如OpenHands、Executable Agents）。智能体轨迹被形式化为任务与动作-观察对的序列，并用于训练各类领域智能体（如网络安全、软件工程、数学推理）。本文的研究对象——用于训练智能体的轨迹数据集——正是建立在这些工作基础之上。

在**LLM水印技术**方面，现有方法主要分为两类：一类在解码时修改输出分布（如Kirchenbauer等人的方法），另一类通过训练模型在输出中嵌入不可见信号（如Adversarial Watermarking、ReMark）。为了确保水印能通过下游训练得以保留，近期研究开始针对特定任务设计水印，如问答和代码补全（如CodeMark、CoProtector）。然而，本文指出这些方法无法直接应用于智能体轨迹，因为轨迹具有独特的交错动作与观察的序列结构，且数据集规模通常较小。本文提出的ActHook方法正是为了弥补这一空白。

在**软件钩子机制**方面，相关工作包括利用钩子在特定执行点注入辅助功能而不修改原始代码（如Python的`sys.settrace()`、Git的`pre-commit`钩子）。本文受此启发，将软件执行的顺序性与智能体的逐步决策相类比，创新性地提出了在动作边界注入“钩子动作”的水印方法。

综上，本文与相关工作的关系是：它立足于LLM智能体轨迹的研究与应用，识别出现有水印技术在保护此类数据上的不足，并创造性借鉴软件工程的钩子概念，提出了首个针对智能体轨迹数据集的定制化水印方案。

### Q3: 论文如何解决这个问题？

ActHook通过一种受软件工程中钩子机制启发的行为级水印框架来解决LLM智能体轨迹数据的版权保护问题。其核心方法分为水印注入（Injection）和黑盒检测（Detection）两个过程。

**核心架构与关键技术：**
1.  **钩子动作（Hook Action）设计**：这是方法的核心创新。传统基于语法变换的水印在低熵的动作内部修改令牌，难以被模型学习且易破坏轨迹。ActHook则利用分析发现——智能体决策点（动作开始处）的令牌熵最高，模型不确定性大。因此，它在轨迹的动作边界处插入“钩子动作”。这些钩子动作从数据集原有的动作空间中选取（如代码智能体中的`pwd`命令），不引入分布外内容，确保了隐蔽性。钩子动作分为**独立型**（可任意位置插入）和**上下文相关型**（依赖轨迹特定上下文，如创建文件后检查其存在），后者更自然、更难被人工察觉。

2.  **水印注入流程**：采用“筛选-采样-注入”三步法。首先，使用`W.Check`过滤出符合水印结构要求的轨迹（如包含文件创建步骤）。然后，根据预设的水印比例随机采样目标轨迹。最后，对选中的轨迹调用`W.Inject`，利用一个辅助LLM生成多样化的钩子动作及其观察结果，插入到轨迹的合适位置。同时，将一个秘密的**激活密钥**（watermark key）附加到用户提示（prompt）中。该密钥在正常使用时不会出现，因此钩子动作在常规任务中保持“休眠”状态，不影响智能体性能。

3.  **黑盒检测机制**：检测时，向被怀疑的智能体提交两组查询：一组提示中包含秘密激活密钥，另一组则不包含（或使用无效的“伪密钥”作为对照）。统计两组查询中钩子动作的出现频率。如果该智能体是在含水印数据集上训练的，激活密钥会显著触发钩子动作，导致其出现频率远高于对照组。通过计算频率差（\(\hat{\Delta_q}\)）并进行配对单侧t检验，可以 statistically 判定数据集是否被未经授权使用。论文还提供了样本复杂度的理论分析，确保检测的可靠性。

**方法优势**：通过在高熵决策点插入符合原分布的动作，解决了小规模轨迹数据集中水印“难学习”的问题；利用密钥触发的行为模式，实现了无需访问模型内部参数的黑盒检测；且对智能体原始任务性能影响极小。

### Q4: 论文做了哪些实验？

论文在三个LLM智能体轨迹数据集（MATH、SimpleQA、SWE-Smith）上进行了实验，使用Qwen-2.5-Coder系列模型（3B、7B、14B）作为基础模型。实验设置包括：构建两种水印方案（独立式和上下文式），以CodeMark作为基线，水印比例R默认设为0.05。基准测试方面，在MATH和SimpleQA上使用Smolagents-Benchmark-v1评估，在SWE-Smith上使用SWE-Bench Lite评估。

主要结果如下：1）水印检测性能：ActHook在Qwen-2.5-Coder-7B上平均检测AUC达到94.3，显著优于基线CodeMark（AUC约55.5）。在单提示（N=1）和8次查询（Q=8）的设置下，独立式和上下文式水印的AUC分别达到97.8和90.8。2）性能保持：水印对模型任务性能（Pass@1）影响可忽略，上下文式水印因动作更自然，性能略优于独立式。3）统计显著性：t检验表明ActHook的检测分数在真实密钥与伪密钥间存在显著差异（p < 0.001），且随提示数N增加而增强。4）超参数分析：模型规模越大（如14B），水印检测性能越好；水印比例R越高，检测信号越强。5）抗攻击鲁棒性：实验测试了DeCoMa过滤和释义攻击，ActHook均表现出较强鲁棒性，检测性能下降很小，而CodeMark则容易被过滤。

### Q5: 有什么可以进一步探索的点？

本文提出的ActHook方法在保护智能体轨迹数据版权方面迈出了重要一步，但其局限性与未来方向值得深入探索。局限性在于：当前方法主要针对决策点明确的序列任务，对于开放域或高度随机性的交互场景，如何设计不影响任务且隐蔽的钩子动作更具挑战；此外，水印检测依赖于特定激活密钥，若攻击者通过数据清洗或轨迹重构绕过密钥触发机制，可能削弱保护效果。未来可探索的方向包括：1）开发自适应水印策略，使钩子动作能根据任务上下文动态嵌入，提升隐蔽性与鲁棒性；2）研究多层级水印技术，结合轨迹行为、中间状态或模型参数等多维度信息，形成复合防护体系；3）扩展至多智能体协作场景，设计协同水印机制以保护分布式交互数据；4）探索水印与差分隐私等技术的结合，在保护版权的同时兼顾用户数据安全与隐私。

### Q6: 总结一下论文的主要内容

这篇论文提出了首个针对LLM智能体轨迹数据的版权保护方法ActHook。其核心贡献在于解决了高质量轨迹数据集（如代码生成、网页搜索等任务的多步骤执行记录）创建成本高昂但缺乏有效版权追溯手段的问题。受软件工程中“钩子”机制启发，ActHook在轨迹中嵌入不影响任务结果的“钩子动作”，这些动作仅在特定密钥触发时被激活。由于智能体决策具有序列性，钩子动作可插入决策点而不破坏任务流。当使用密钥查询时，基于水印数据训练的智能体会显著高频地产生这些钩子动作，从而实现可靠的黑盒检测。实验表明，该方法在数学推理、网页搜索和软件工程智能体上平均检测AUC达94.3，且几乎不影响模型性能。该工作为智能体训练数据的知识产权保护提供了切实可行的解决方案，有助于促进高质量数据集的开放共享与可持续发展。
