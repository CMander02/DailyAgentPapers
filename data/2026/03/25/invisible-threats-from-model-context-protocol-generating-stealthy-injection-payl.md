---
title: "Invisible Threats from Model Context Protocol: Generating Stealthy Injection Payload via Tree-based Adaptive Search"
authors:
  - "Yulin Shen"
  - "Xudong Pan"
  - "Geng Hong"
  - "Min Yang"
date: "2026-03-25"
arxiv_id: "2603.24203"
arxiv_url: "https://arxiv.org/abs/2603.24203"
pdf_url: "https://arxiv.org/pdf/2603.24203v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Security"
  - "Tool-Augmented Agents"
  - "Adversarial Attack"
  - "Model Context Protocol (MCP)"
  - "Black-box Attack"
  - "Prompt Injection"
relevance_score: 7.5
---

# Invisible Threats from Model Context Protocol: Generating Stealthy Injection Payload via Tree-based Adaptive Search

## 原始摘要

Recent advances in the Model Context Protocol (MCP) have enabled large language models (LLMs) to invoke external tools with unprecedented ease. This creates a new class of powerful and tool augmented agents. Unfortunately, this capability also introduces an under explored attack surface, specifically the malicious manipulation of tool responses. Existing techniques for indirect prompt injection that target MCP suffer from high deployment costs, weak semantic coherence, or heavy white box requirements. Furthermore, they are often easily detected by recently proposed defenses. In this paper, we propose Tree structured Injection for Payloads (TIP), a novel black-box attack which generates natural payloads to reliably seize control of MCP enabled agents even under defense. Technically, We cast payload generation as a tree structured search problem and guide the search with an attacker LLM operating under our proposed coarse-to-fine optimization framework. To stabilize learning and avoid local optima, we introduce a path-aware feedback mechanism that surfaces only high quality historical trajectories to the attacker model. The framework is further hardened against defensive transformations by explicitly conditioning the search on observable defense signals and dynamically reallocating the exploration budget. Extensive experiments on four mainstream LLMs show that TIP attains over 95% attack success in undefended settings while requiring an order of magnitude fewer queries than prior adaptive attacks. Against four representative defense approaches, TIP preserves more than 50% effectiveness and significantly outperforms the state-of-the-art attacks. By implementing the attack on real world MCP systems, our results expose an invisible but practical threat vector in MCP deployments. We also discuss potential mitigation approaches to address this critical security gap.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决由新兴的模型上下文协议（MCP）引入的一个关键安全问题：如何生成既隐蔽又有效的恶意提示注入载荷，以劫持基于MCP的AI智能体。随着大型语言模型（LLMs）向能够调用外部工具的智能体演进，Anthropic推出的MCP协议通过标准化工具集成，极大地增强了LLMs的功能。然而，这种架构也扩展了攻击面，特别是当第三方工具服务器被恶意操控时，其返回的响应可能包含隐蔽的恶意指令，导致“间接提示注入”（IPI）攻击，使智能体在用户不知情下执行恶意操作。

现有方法在应对MCP场景时存在明显不足。传统攻击技术如基于梯度优化的方法（如GCG）或手动注入，通常生成高困惑度的乱码字符串，虽可能有效但极易被基于困惑度的防御机制检测，且破坏了工具响应的语义连贯性，缺乏隐蔽性。而依赖修改工具元数据的方法则容易被注册审计发现。这些方法均未能平衡“隐蔽性”（载荷需看起来像正常工具响应）与“有效性”（能成功劫持模型）这两个冲突需求，且往往需要白盒访问权限或面临高昂的黑盒优化成本，难以适应动态防御。

因此，本文的核心问题是：在攻击者仅能黑盒访问受害者LLM、且需规避现代防御措施（如困惑度过滤、递归重写）的约束下，如何为MCP支持的智能体自动生成语义自然、隐蔽性强，同时又能可靠夺取控制权的恶意注入载荷。论文提出的TIP框架正是为了系统性地解决这一挑战。

### Q2: 有哪些相关研究？

本文提出的TIP攻击方法主要与以下几类相关研究有关：

**1. 间接提示注入攻击方法**
这是本文最直接相关的领域。现有工作主要分为两类：一是基于梯度优化的白盒攻击（如GCG），需要模型内部梯度信息，部署成本高且不适用于黑盒场景；二是基于离散搜索的黑盒攻击（如AutoDAN），通过迭代优化生成对抗性后缀，但通常语义连贯性差且查询效率低。本文的TIP属于黑盒攻击，但通过树形结构和粗到细优化框架，显著提升了攻击的隐蔽性和成功率，同时大幅降低了查询次数。

**2. 针对工具增强型Agent的安全研究**
随着ReAct等框架的普及，相关安全研究开始关注工具调用带来的攻击面。已有工作分析了通过污染检索数据库或API响应进行攻击的可行性，但大多停留在概念验证阶段，缺乏在真实MCP协议下的系统性攻击方法。本文首次将攻击具体落实到MCP这一标准化协议上，并针对其结构化JSON响应的特点设计载荷，更具现实针对性。

**3. 防御方法与对抗性攻击**
近期出现了多种针对提示注入的防御技术，例如输入过滤、上下文隔离和检测分类器。现有攻击方法在面对这些防御时效果急剧下降。本文工作的一个关键区别在于，TIP在设计时明确考虑了防御信号，通过动态调整搜索预算来适应防御变换，从而在受保护环境下仍能保持较高攻击有效性，这是此前攻击所未实现的。

**4. 树形搜索与规划方法**
在优化领域，树形搜索（如蒙特卡洛树搜索）常用于序列决策问题。本文借鉴了这一思想，将载荷生成建模为树结构搜索问题，并引入了路径感知反馈机制来避免局部最优，这与传统的线性优化或贪心搜索方法有本质区别，提高了搜索的稳定性和效率。

总体而言，本文与相关工作的核心区别在于：首次在黑盒条件下实现了对标准化MCP协议的高效、隐蔽、抗防御的间接提示注入攻击，通过树形自适应搜索框架解决了现有方法在语义质量、查询效率和防御绕过方面的不足。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为TIP（树结构注入载荷）的新型黑盒攻击框架来解决MCP代理中恶意工具响应注入的问题。其核心方法是将恶意载荷生成建模为一个在语义空间中的离散搜索问题，并利用一个大语言模型作为可变的攻击者代理进行探索和优化。

整体框架采用树形结构组织搜索空间，迭代执行三个主要阶段：分支、剪枝和早期停止。在分支阶段，攻击模型基于工具描述预测合法的工具响应内容，确保搜索空间符合工具语义边界，并采用双层的由粗到细策略生成候选载荷。该策略包含攻击引导层和结构优化层：引导层决定使用隐式诱导还是显式控制等语义策略；优化层则根据当前得分，在得分低时同时优化JSON的键和值以广泛探索，得分高时则冻结键、仅优化值以稳定细化。此外，路径感知反馈机制通过向攻击模型提供高质量历史轨迹（而非仅最近失败），帮助其识别全局优化模式，避免陷入局部最优。工具响应模拟则确保生成的恶意载荷与合法输出在语义上连贯，以提升隐蔽性。

在剪枝阶段，框架通过蒙特卡洛方法对候选载荷进行严格的迁移性评估，即在一组多样化的用户指令和受害模型上测试其攻击成功率，仅保留排名前K的节点进入下一轮迭代，从而筛选出泛化能力强的载荷。防御感知机制动态监控先前尝试的失败模式，如果载荷因特定防御过滤器（如文本重写器）而失败，则提示攻击者生成简洁或抗总结的变体，使搜索能自适应地规避防御。

关键技术创新点包括：1) 将树形搜索与由粗到细优化结合，有效管理复杂搜索空间；2) 引入路径感知反馈，利用历史高质量路径稳定学习过程；3) 集成工具响应模拟和防御感知机制，分别增强载荷的隐蔽性和对防御的鲁棒性。该框架完全在黑盒条件下运行，无需目标模型的梯度信息，通过迭代优化最终生成语义连贯、隐蔽性强且能有效劫持MCP代理的JSON格式恶意载荷。

### Q4: 论文做了哪些实验？

论文设计了五组实验来全面评估TIP框架。实验设置包括：1）攻击目标：欺诈（钓鱼）和数据窃取；2）评估工具：使用GetWeather和GetProduct工具进行欺诈场景测试，使用ExpediaBooking和ShipManager工具进行数据窃取场景测试；3）模型配置：攻击者代理使用Qwen2.5-72B-Instruct生成载荷，受害者代理测试了Qwen2.5-7B/72B-Instruct和Llama3.1-8B/3.3-70B-Instruct四种主流模型；4）训练环境：使用Qwen2.5-7B-Instruct、InternLM2.5-7B-Instruct和GLM4-9B-Instruct组成的开源模型集合模拟黑盒环境。

对比方法包括：1）Fixed（Manual）：人工设计的静态对抗提示；2）TAP（Tree of Attacks）：最先进的自动化注入框架。评估指标包括攻击成功率（ASR）、查询次数（Query Count）和语义相似度（Cosine Similarity）。

主要结果如下：
- **无防御环境**：TIP在四个工具中的三个实现了100% ASR，在ShipManager任务上达到95.0%，显著优于Fixed（最高45.0%）和TAP（最高91.0%）。查询效率方面，TIP在GetProduct任务仅需100次查询，而TAP需要2580次。
- **防御环境**：针对四种防御机制（Instruction Prevention、Sandwich Prevention、Finetuned Detector、Perplexity Filtering），TIP保持较强鲁棒性。例如在Sandwich Prevention防御下，TIP在GetProduct任务保持100% ASR，而Fixed降至5.0%；在Finetuned Detector防御下，TIP在ExpediaBooking任务达到97.8% ASR。
- **可迁移性**：载荷在不同模型间展现强迁移能力，如在GetWeather任务中，使用Qwen2.5-7B生成的载荷在Llama3.3-70B上实现100% ASR。
- **隐蔽性**：通过余弦相似度衡量，TIP生成的载荷与良性工具响应保持高语义一致性，能有效规避基于分类的防御。

关键数据指标：在无防御环境中，TIP在GetProduct/GetWeather/ExpediaBooking/ShipManager任务的ASR分别为100%/100%/100%/95.0%；在Perplexity Filtering防御下，相应ASR为100%/100%/94.0%/93.0%。

### Q5: 有什么可以进一步探索的点？

该论文提出的TIP攻击方法虽然有效，但其局限性和未来探索方向值得深入。首先，研究主要针对已知防御策略进行优化，但面对未知或自适应防御机制时，其鲁棒性尚未验证。其次，攻击生成依赖于黑盒查询，成本仍较高，未来可探索更高效的语义空间搜索算法，例如结合强化学习与元学习来减少查询次数。此外，当前实验集中于主流LLM，在多样化、专业化或持续学习的模型上攻击效果可能不同，需扩展评估范围。从防御角度看，论文提到的缓解方法较为初步，未来可设计更主动的检测机制，如实时监控工具调用的语义一致性，或引入可解释性分析来识别隐蔽注入。最后，攻击仅聚焦文本payload，未来可能扩展到多模态（如图像、音频）的隐蔽注入，这将是更复杂且实际的安全挑战。

### Q6: 总结一下论文的主要内容

该论文针对新兴的模型上下文协议（MCP）生态系统的安全漏洞，提出了一种名为“树结构注入有效载荷”（TIP）的新型黑盒攻击方法。核心问题是：MCP使LLM能便捷调用外部工具，但这也引入了工具响应被恶意操纵的攻击面，现有间接提示注入方法存在部署成本高、语义连贯性差或依赖白盒信息等问题，且易被防御机制检测。

论文的核心贡献是形式化了一种名为“隐蔽更新攻击”的MCP威胁模型，并设计了TIP攻击框架来应对其挑战。该方法将有效载荷生成构建为一个树结构搜索问题，采用由粗到细的优化框架，利用攻击者LLM引导搜索。它首先预测一个完全合理的良性响应轨迹，然后仅将结尾部分细化为简洁的攻击触发器，从而确保语义连贯性。为稳定学习并避免局部最优，引入了路径感知反馈机制，仅将高质量历史轨迹呈现给攻击模型。此外，通过显式地将搜索条件与可观测的防御信号关联，并动态重新分配探索预算，使框架能抵御防御性转换。

主要结论是，TIP在无防御设置下攻击成功率超过95%，且查询成本比先前自适应攻击低一个数量级。在面对四种代表性防御方法时，TIP仍能保持超过50%的有效性，显著优于现有最先进的攻击方法。通过在真实MCP系统上实现攻击，研究结果揭示了MCP部署中一个隐蔽但实际的威胁载体。论文最后讨论了潜在的缓解方法以应对这一关键安全缺口。
