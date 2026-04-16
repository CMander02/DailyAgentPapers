---
title: "SafeHarness: Lifecycle-Integrated Security Architecture for LLM-based Agent Deployment"
authors:
  - "Xixun Lin"
  - "Yang Liu"
  - "Yancheng Chen"
  - "Yongxuan Wu"
  - "Yucheng Ning"
  - "Yilong Liu"
  - "Nan Sun"
  - "Shun Zhang"
  - "Bin Chong"
  - "Chuan Zhou"
  - "Yanan Cao"
  - "Li Guo"
date: "2026-04-15"
arxiv_id: "2604.13630"
arxiv_url: "https://arxiv.org/abs/2604.13630"
pdf_url: "https://arxiv.org/pdf/2604.13630v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Security"
  - "System Architecture"
  - "Tool Use"
  - "Adversarial Robustness"
  - "Deployment"
  - "Safety"
relevance_score: 7.5
---

# SafeHarness: Lifecycle-Integrated Security Architecture for LLM-based Agent Deployment

## 原始摘要

The performance of large language model (LLM) agents depends critically on the execution harness, the system layer that orchestrates tool use, context management, and state persistence. Yet this same architectural centrality makes the harness a high-value attack surface: a single compromise at the harness level can cascade through the entire execution pipeline. We observe that existing security approaches suffer from structural mismatch, leaving them blind to harness-internal state and unable to coordinate across the different phases of agent operation. In this paper, we introduce \safeharness{}, a security architecture in which four proposed defense layers are woven directly into the agent lifecycle to address above significant limitations: adversarial context filtering at input processing, tiered causal verification at decision making, privilege-separated tool control at action execution, and safe rollback with adaptive degradation at state update. The proposed cross-layer mechanisms tie these layers together, escalating verification rigor, triggering rollbacks, and tightening tool privileges whenever sustained anomalies are detected. We evaluate \safeharness{} on benchmark datasets across diverse harness configurations, comparing against four security baselines under five attack scenarios spanning six threat categories. Compared to the unprotected baseline, \safeharness{} achieves an average reduction of approximately 38\% in UBR and 42\% in ASR, substantially lowering both the unsafe behavior rate and the attack success rate while preserving core task utility.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能代理（Agent）在部署和运行时的系统层安全问题。研究背景是，随着LLM代理自主性增强并被赋予访问文件系统、数据库等具有现实副作用工具的能力，其性能高度依赖于一个称为“执行框架”（harness）的系统层，该层负责编排工具使用、管理上下文和维持状态。然而，这种架构上的中心地位也使其成为高价值的攻击面：对框架层的单一破坏可能在整个执行流程中引发连锁反应。

现有安全方法存在三个主要不足：1. **上下文盲区**：现有防御（如NeMo Guardrails）通常在对话接口处进行输入输出过滤，无法洞察框架内部状态（如被污染的工具输出如何影响后续推理链）。2. **层间隔离**：即使部署了多个安全检查点，它们也相互独立运作，缺乏协调。面对同时针对输入、工具输出和对话历史的复合攻击时，每个检查点只能观察到部分异常信号，无法触发系统级的协同响应。3. **缺乏韧性**：现有防御大多只有“通过或拦截”的二元决策，一旦攻击突破外层防御，系统缺乏逐步限制工具权限或优雅降级以保持核心功能的机制，导致损害在后续步骤中持续累积。

因此，本文要解决的核心问题是：如何设计一种与代理生命周期深度集成的安全架构，以克服上述结构性缺陷，为LLM代理的执行框架提供系统化、协同且具有韧性的安全保障。论文提出的解决方案是SafeHarness架构，它将防御机制直接嵌入到代理执行的四个阶段（输入处理、决策制定、动作执行、状态更新），并通过跨层协调机制实现针对复合攻击的协同响应。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：**面向性能的智能体执行框架（Harness）工程**和**面向安全的智能体防御机制**。

在**执行框架工程**方面，工业界（如OpenAI、LangChain）和研究界均致力于通过优化上下文组织、工具编排和流程控制来提升智能体的任务性能与稳定性。例如，有研究展示了模块化框架设计能提升多轮环境中的表现，而AutoHarness则探索了通过自动生成和迭代代码级框架来约束行为、提升性能。然而，这些工作主要聚焦于性能优化，**忽视了安全考量**。本文的SafeHarness则首次将安全架构深度集成到执行框架中，旨在弥补这一空白。

在**智能体安全防御**方面，先前研究已识别出智能体在感知、推理、执行和记忆等环节面临的风险，并提出了相应的组件级防御措施，例如输入净化、推理验证、工具访问限制和内存保护。这些方法虽能针对特定威胁提升安全性，但通常是**孤立、缺乏协调**的，未能从系统层面统筹智能体完整生命周期的防护。本文的SafeHarness与这些工作的核心区别在于，它**超越了组件级防御**，提出了一个将四层防御机制（对抗性上下文过滤、分层因果验证、特权分离的工具控制、安全回滚与自适应降级）直接编织进智能体生命周期各阶段的**集成安全架构**，并通过跨层协调机制实现系统级的、全生命周期的协同防护。

### Q3: 论文如何解决这个问题？

论文通过提出SafeHarness这一集成到智能体生命周期中的安全架构来解决LLM智能体执行框架（harness）面临的安全威胁。其核心方法是将四个防御层直接编织到智能体的执行流程中，并通过跨层协调机制联动，形成纵深防御。

**整体框架与主要模块：**
SafeHarness的架构围绕智能体执行循环（输入处理→决策制定→动作执行→状态更新）构建，每个阶段对应一个防御层：
1.  **L1（输入处理层）**：在外部内容进入智能体上下文前进行多阶段过滤，包括结构性净化（去除Unicode隐藏字符）、基于模式的检测（正则表达式匹配已知攻击模式）和基于LLM的语义过滤。关键创新点是**来源标记**，为每个内容块附加来源类型和信任等级，供下游层调整验证严格度。
2.  **L2（决策制定层）**：对每个提议的工具调用实施**三级渐进式安全验证**。第一级是基于确定性规则的合规性检查；第二级是上下文法官模型评估；第三级是因果诊断，判断不安全行为是否源于对抗性注入。验证深度会根据风险严重性自动提升。
3.  **L3（动作执行层）**：实施**特权分离的工具控制**。关键技术包括：将工具按风险分为五级；使用具有TTL和调用次数限制的**能力令牌**进行细粒度访问控制；基于HMAC的完整性验证以防止工具描述被篡改。
4.  **L4（状态更新层）**：作为最后防线，提供**安全回滚与自适应降级**。机制包括：定期创建包含环境状态和受保护内存的检查点；在检测到攻击时触发回滚；以及根据持续异常检测动态调整系统能力（如降低允许的工具风险等级）的自适应降级。

**创新点与跨层协调：**
系统的核心创新在于各防御层并非孤立，而是通过**跨层机制**紧密协同：
*   **验证升级**：当L1检测到异常或跨层熵监控器发现违规率上升时，会触发L2采用更严格的验证层级。
*   **触发回滚与降级**：当L2的因果诊断确认存在注入攻击时，会直接触发L4执行状态回滚并提升系统降级等级。
*   **特权收紧**：L4在提升降级等级后，会通知L3降低当前允许的工具风险上限，限制后续动作。
*   **自适应恢复**：在安全行为窗口后，L4会尝试恢复降级等级，并通知L2降低验证严格度，平衡安全与效用。

这种设计确保了防御覆盖整个生命周期，且各层提供不可替代的安全属性（L1保障输入完整性，L2保障决策安全性，L3保障执行特权，L4保障状态可恢复性），共同显著降低了不安全行为率和攻击成功率。

### Q4: 论文做了哪些实验？

实验设置方面，论文在Agent-SafetyBench基准数据集上进行评估，该数据集包含2000个安全关键任务，覆盖349个交互环境和8个风险类别。实验主要评估了基准中前200个任务，并使用了DeepSeek-V3.2模型的两种推理模式（DeepSeek-Chat和DeepSeek-Reasoner）作为智能体模型，以测试安全效益在不同推理风格上的泛化能力。评估采用GPT-4o-mini作为评判模型，依据任务的可完成性标志，对智能体行为进行四分类标注。实验涵盖了三种主流的智能体执行架构（ReAct、Multi-Agent和Self-Evolving）来测试不同执行模式。

对比方法包括四种安全基线，它们代表了安全机制与执行架构集成深度递增的谱系：无保护的基线（Unprotected）、仅使用系统提示的模型级防御（System-Prompt）、进行外部输入/输出过滤的接口级防御（Guardrail）、以及结合模式检测和LLM推理审核的管道级防御（LlamaFirewall）。论文还设计了五种攻击类型（A1至A5），分别针对防御体系的不同层次，并覆盖了全部六类威胁向量，包括上下文投毒、间接注入、工具篡改、记忆注入和复合攻击。

主要结果通过六项指标呈现，重点关注安全性（UBR、ASR、NNH）和效用（TCR、UA）。实验数据显示，与无保护基线相比，SafeHarness在所有智能体架构和模型上均实现了最低的不安全行为率（UBR）和攻击成功率（ASR）。具体而言，在DeepSeek-Chat模型下，SafeHarness将ReAct、Multi-Agent和Self-Evolving架构的UBR分别平均降低了约22.4、18.7和22.8个百分点，ASR降低了约22.8、19.2和22.9个百分点。在效用方面，ReAct和Self-Evolving架构的任务完成率（TCR）与无保护基线相差仅约1-2个百分点，表明安全增益并非源于简单的全面拒绝响应。在遭受攻击时的有用性（UA）指标也显著提升，例如在ReAct架构下从45.6%提升至67.5%，证明了其在保障安全的同时有效保留了核心功能。

### Q5: 有什么可以进一步探索的点？

本文提出的SafeHarness架构在LLM代理生命周期中集成了多层防御，但仍存在一些局限和可拓展方向。首先，其验证机制（如因果验证）依赖于对正常行为模式的预定义或学习，可能难以应对未知或高度自适应的攻击模式，未来可探索更动态、基于异常检测的实时学习机制。其次，当前架构主要针对单代理部署，在多代理协作场景中，跨代理的信任传递、协同防御及状态同步可能成为新的攻击面，需设计分布式安全协议。此外，安全机制（如严格权限控制）可能影响任务完成效率，未来可研究更细粒度的自适应权衡策略，在风险与效用间动态调整。从工程角度看，如何将此类架构轻量化并适配不同底层框架（如LangChain、AutoGPT）也是一大挑战。最后，随着工具生态扩展，对复杂工具链（如多步推理工具）的语义级安全验证仍需深入探索。

### Q6: 总结一下论文的主要内容

该论文针对基于大语言模型（LLM）的智能体部署中的安全风险，提出了一种名为SafeHarness的生命周期集成安全架构。核心问题是现有安全方案与智能体执行流程存在结构性错配，无法有效监控和协调智能体运行内部状态及不同阶段，导致作为核心编排层的执行工具（harness）成为高危攻击面。

论文的核心贡献是设计了一个将四层防御机制深度集成到智能体生命周期中的架构。这四层防御分别是：输入处理阶段的对抗性上下文过滤、决策阶段的分层因果验证、动作执行阶段的权限分离工具控制，以及状态更新阶段的安全回滚与自适应降级。此外，通过跨层协调机制将这些防御层联动起来，能够在检测到持续异常时，动态提升验证强度、触发状态回滚并收紧工具权限。

主要结论表明，SafeHarness在多种执行工具配置和涵盖六类威胁的五种攻击场景下，相比未受保护的基线，平均将不安全行为率（UBR）降低了约38%，攻击成功率（ASR）降低了约42，同时保持了核心任务效用。这证明了该架构能有效应对执行工具层的系统性安全风险，为LLM智能体的安全部署提供了系统性解决方案。
