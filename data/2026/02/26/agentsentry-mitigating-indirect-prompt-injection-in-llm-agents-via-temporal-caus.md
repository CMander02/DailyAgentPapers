---
title: "AgentSentry: Mitigating Indirect Prompt Injection in LLM Agents via Temporal Causal Diagnostics and Context Purification"
authors:
  - "Tian Zhang"
  - "Yiwei Xu"
  - "Juan Wang"
  - "Keyan Guo"
  - "Xiaoyang Xu"
  - "Bowen Xiao"
  - "Quanlong Guan"
  - "Jinlin Fan"
  - "Jiawei Liu"
  - "Zhiquan Liu"
  - "Hongxin Hu"
date: "2026-02-26"
arxiv_id: "2602.22724"
arxiv_url: "https://arxiv.org/abs/2602.22724"
pdf_url: "https://arxiv.org/pdf/2602.22724v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent 安全"
  - "Agent 架构"
  - "工具使用"
  - "推理"
  - "防御机制"
  - "间接提示注入"
  - "多轮交互"
relevance_score: 9.0
---

# AgentSentry: Mitigating Indirect Prompt Injection in LLM Agents via Temporal Causal Diagnostics and Context Purification

## 原始摘要

Large language model (LLM) agents increasingly rely on external tools and retrieval systems to autonomously complete complex tasks. However, this design exposes agents to indirect prompt injection (IPI), where attacker-controlled context embedded in tool outputs or retrieved content silently steers agent actions away from user intent. Unlike prompt-based attacks, IPI unfolds over multi-turn trajectories, making malicious control difficult to disentangle from legitimate task execution. Existing inference-time defenses primarily rely on heuristic detection and conservative blocking of high-risk actions, which can prematurely terminate workflows or broadly suppress tool usage under ambiguous multi-turn scenarios. We propose AgentSentry, a novel inference-time detection and mitigation framework for tool-augmented LLM agents. To the best of our knowledge, AgentSentry is the first inference-time defense to model multi-turn IPI as a temporal causal takeover. It localizes takeover points via controlled counterfactual re-executions at tool-return boundaries and enables safe continuation through causally guided context purification that removes attack-induced deviations while preserving task-relevant evidence. We evaluate AgentSentry on the \textsc{AgentDojo} benchmark across four task suites, three IPI attack families, and multiple black-box LLMs. AgentSentry eliminates successful attacks and maintains strong utility under attack, achieving an average Utility Under Attack (UA) of 74.55 %, improving UA by 20.8 to 33.6 percentage points over the strongest baselines without degrading benign performance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在借助外部工具和检索系统执行复杂任务时，所面临的间接提示注入（Indirect Prompt Injection, IPI）安全威胁。研究背景是，随着LLM智能体日益依赖工具（如搜索、邮件、日历、API）来自主完成多步骤任务，其运行状态会持续整合来自外部的、可能不可信的内容（如邮件、网页）。攻击者可以将恶意指令嵌入这些内容中，当智能体通过工具调用处理这些内容后，攻击者控制的上下文会持久化并逐渐主导后续的决策轨迹，悄无声息地使智能体行为偏离用户意图，而用户最初的提示本身可能是良性的。这种多回合、延迟触发的攻击模式，使得恶意控制与正常的任务执行交织在一起，难以区分。

现有防御方法（如MELON、Task Shield等）主要依赖于启发式检测（例如基于行为相似度阈值进行重执行比对）或严格的行动对齐约束（要求每个行动都必须由用户目标明确证明）。这些方法存在明显不足：首先，它们通常是面向检测或阻塞的，一旦发现可疑迹象，最安全的做法往往是终止工作流或广泛抑制工具使用，这在多回合场景下容易导致合法任务被过早中断，显著降低受攻击情况下的任务效用（Utility Under Attack）。其次，这些方法缺乏一个根本性的机制来精准定位攻击者控制的上下文在何时、何处成为行动选择的主导因果驱动力，因此干预措施往往比较粗放，难以有效应对微妙的多回合接管攻击。

因此，本文要解决的核心问题是：如何为工具增强的LLM智能体设计一种推理时防御框架，能够**精准建模、定位并缓解多回合间接提示注入攻击，同时避免因保守的阻断策略而损害合法任务的完成**。具体而言，论文提出的AgentSentry框架试图通过**时序因果诊断**和**因果引导的上下文净化**来解决上述问题。它将多回合IPI建模为一个时序因果接管过程，通过在工具返回边界进行受控的反事实重执行来定位接管点，并仅在诊断出上下文介导的因果主导时，触发净化机制以消除攻击诱导的偏差，同时保留任务相关证据，从而实现安全的任务延续，而非简单终止。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、评测类和防御类。

在方法类研究中，工具增强的LLM智能体（如ReAct、Toolformer）通过整合外部工具来扩展能力，但这也引入了间接提示注入（IPI）的安全风险。本文的AgentSentry框架正是针对此类智能体架构进行防御。

在评测类研究中，近期的工作（如AgentDojo基准）构建了多步骤、多工具的环境来形式化和压力测试IPI威胁，为评估防御方法提供了标准。本文正是在AgentDojo基准上对AgentSentry进行了全面评估。

在防御类研究中，现有的推理时防御方法（如基于启发式检测或保守阻断高风险动作的方法）主要面临两大局限：一是难以在多轮交互中准确定位攻击接管点，二是倾向于过早终止工作流或广泛抑制工具使用，从而损害任务效用。例如，MELON等方法在遭受攻击时效用（UA）显著下降。本文提出的AgentSentry与这些工作的主要区别在于：它首次将多轮IPI建模为一种时序因果接管过程，并通过在工具返回边界进行受控反事实重执行来定位接管点，进而采用因果引导的上下文净化来实现安全的任务延续，而非简单地检测后阻断。这使其能在消除攻击的同时，更好地保持受攻击下的任务效用。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为AgentSentry的新型推理时检测与缓解框架来解决间接提示注入（IPI）问题。其核心方法是将多轮次IPI建模为一种**时间因果接管**过程，并通过**边界锚定的因果诊断**与**因果引导的上下文净化**来实现防御。

**整体框架与工作流程**：AgentSentry的防御流程紧密集成在智能体的执行循环中。它在每个**工具返回边界**（即外部工具/检索内容被纳入智能体内部上下文之后、但智能体最终确定并执行下一个动作之前的时刻）插入检测点。整个框架包含两个主要阶段：1) **因果诊断与接管检测**；2) **安全延续与上下文净化**。

**核心模块与关键技术**：
1.  **边界锚定与工具缓存**：在每一个工具返回边界`b`，框架会提取不受信任的**中介视图**`r_b`（即来自工具、检索或记忆的内容），并将其缓存。这为后续进行受控的反事实重执行奠定了基础。
2.  **基于反事实重执行的因果诊断**：这是方法的创新核心。在干运行模式下，AgentSentry通过替换用户输入和/或中介内容，构造并评估四种**干预机制**：
    *   `orig`: 原始用户输入 + 原始中介内容。
    *   `mask`: 诊断探针（中性输入） + 原始中介内容。
    *   `mask_sanitized`: 诊断探针 + 净化后的中介内容。
    *   `orig_sanitized`: 原始用户输入 + 净化后的中介内容。
    通过多次蒙特卡洛采样执行这些机制，并计算一个**序数诊断结果**`Y_b`（量化动作的风险和语义偏差），框架可以估算出关键的因果效应，包括**平均因果效应**、**直接效应**和**间接效应**。其中，间接效应`IE_b`直接度量了中介内容对有害动作的驱动程度。
3.  **时间因果退化测试与接管检测**：AgentSentry的创新点在于将IPI视为一个随时间演化的过程。它维护一个滑动窗口内`ACE_b`（用户目标主导性）和`IE_b`（中介依赖性）的估计序列，并计算其趋势。接管被检测为一种**协同退化模式**：用户驱动路径衰减（`ACE_b`趋势为负）而中介驱动路径增强（`IE_b`趋势为正）。一个综合的风险评分`R_b`和间接效应的显著性检验共同决定了是否在边界`b`触发接管警报。
4.  **因果门控的净化与安全延续**：一旦检测到接管，缓解机制仅在受影响的边界局部启动，而非终止整个工作流。其关键技术是**任务对齐的证据净化**：对中介视图`r_b`应用净化操作`Purify`，该操作会**移除其中的指令性、优先级覆盖等可执行内容，但保留与用户任务目标`g`相关的实体、时间戳等事实性证据**。净化后的上下文`c_b^safe`用于重新推导下一个动作`a_b^safe`。动作修订是**最小化的**：它会利用诊断阶段的反事实结果，区分哪些高风险工具调用是“中介依赖的”（在净化后消失），哪些是“反事实持久的”（在净化后仍会出现），并对后者进行参数修复和暴露最小化处理，而非简单阻止。

**创新点总结**：1) **首次将多轮IPI形式化为时间因果接管问题**；2) 提出**边界锚定的反事实重执行协议**，实现了对中介驱动偏差的精细归因；3) 设计**因果对齐的上下文净化器**，在消除攻击的同时最大程度保留任务相关证据；4) 实现**局部、最小化的安全延续**，在保证安全性的同时维持了工作流的可用性。

### Q4: 论文做了哪些实验？

论文在AgentDojo基准测试上进行了实验，该基准包含四个任务套件（信息收集、多跳问答、工具使用、规划与执行）和三种间接提示注入攻击家族（目标劫持、信息泄露、拒绝服务）。实验设置涉及多个黑盒大语言模型（如GPT-4、Claude-3、Gemini-1.5-Pro），并对比了多种基线方法，包括无防御、启发式检测（如关键词过滤、置信度阈值）、保守阻断（如高风险动作阻止）以及现有防御工具（如ARMOR）。主要结果方面，AgentSentry在遭受攻击时平均保持了74.55%的“受攻击下效用”，相比最强基线提升了20.8至33.6个百分点，同时成功消除了所有攻击（攻击成功率降至0%），且未损害良性任务性能（良性效用与无防御相当）。关键数据指标包括受攻击下效用、攻击成功率和良性效用，证明了其在多轮次攻击中有效隔离恶意控制并维持工作流安全运行的能力。

### Q5: 有什么可以进一步探索的点？

该论文提出的AgentSentry框架在防御间接提示注入（IPI）方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其核心机制依赖于在工具返回边界进行受控反事实重执行，这引入了额外的计算开销和延迟，在实时性要求高的场景中可能受限。未来可探索更轻量化的因果推断方法，或通过预计算与缓存策略优化性能。其次，当前方法主要针对已知的攻击模式进行上下文净化，对于自适应或新型的IPI攻击可能泛化能力不足。可结合持续学习或对抗性训练，使模型能动态识别未知攻击模式。此外，框架假设攻击主要源自工具返回内容，但未充分考虑多智能体协作或链式工具调用中更复杂的攻击传播路径。未来可扩展至分布式智能体系统，研究跨智能体的因果影响传播与协同防御机制。最后，评估基准虽涵盖多类任务，但现实场景中的任务多样性和开放性更高，需在更复杂的实际应用环境中验证其鲁棒性。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型（LLM）智能体在调用外部工具时面临的间接提示注入（IPI）攻击问题，提出了一种名为AgentSentry的新型推理时防御框架。IPI攻击的特点是攻击者将恶意指令嵌入工具返回的不可信内容中，在多轮交互中逐步劫持智能体行为，使其偏离用户意图，而现有防御方法多依赖启发式检测和保守阻断，容易导致任务过早终止或工具使用被过度抑制。

论文的核心贡献在于首次将多轮IPI建模为一个时序因果劫持过程，并据此设计了包含两个阶段的防御方法。首先，通过时序因果诊断，在工具返回边界处执行受控的反事实重执行，量化并定位用户目标与工具返回上下文对后续动作的因果主导权，从而精准识别劫持发生的转折点。其次，基于诊断结果触发因果门控的上下文净化机制，该机制仅在检测到上下文主导不安全行为时激活，旨在消除攻击引入的偏差信号，同时保留完成任务所需的相关证据，从而允许智能体在净化后安全地继续执行原任务流，而非简单终止。

实验在AgentDojo基准上进行，覆盖多种任务、攻击家族和黑盒LLM。结果表明，AgentSentry能够将攻击成功率降至0%，同时在受攻击下保持平均74.55%的效用，相比最强基线提升了20.8至33.6个百分点，且不影响良性任务性能。这项工作为工具增强型LLM智能体提供了一种既能有效防御多轮IPI攻击，又能保障任务连续性的实用化解决方案。
