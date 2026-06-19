---
title: "LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents"
authors:
  - "Md Nayem Uddin"
  - "Amir Saeidi"
  - "Eduardo Blanco"
  - "Chitta Baral"
date: "2026-06-18"
arxiv_id: "2606.20529"
arxiv_url: "https://arxiv.org/abs/2606.20529"
pdf_url: "https://arxiv.org/pdf/2606.20529v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Tool-Use Agent"
  - "State Management"
  - "Policy Compliance"
  - "Customer Service Agent"
  - "Tool-Calling Agent"
relevance_score: 9.0
---

# LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents

## 原始摘要

Policy-adherent tool-calling agents in customer-service domains must maintain task states across turns while calling tools and obeying domain policies. Task states consist of relevant facts, identifiers, constraints, and conditions observed through user interaction and tool calls. In standard agents, task states are not represented separately. Observations, tool returns, and policy instructions are placed in the prompt, leaving agents to reconstruct the relevant states from the prompt each time they decide what to do next. This design makes state management implicit, creating two common failure modes. An agent may retrieve the right facts but later ground its decision in stale, missing, or incorrect information; and a syntactically valid tool call may still violate a domain policy that depends on the current task state. We introduce \textsc{LedgerAgent}, an inference-time method for tool-calling agents that maintains observed task states in a separate ledger and renders the states into the prompt. The ledger is also used to check state-dependent policy constraints before environment-changing tool calls are executed, blocking policy violations. Across four customer-service domains and a mixed panel of open- and closed-weight models, \textsc{LedgerAgent} improves average pass\textasciicircum{}k over a standard prompt-based tool-calling approach, with the largest gains under stricter multi-trial consistency metrics.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决客户服务领域中政策遵守型工具调用代理的两个核心问题：状态管理隐式化导致的决策错误和策略违规。现有方法通常将所有信息（包括观察结果、工具返回值和策略指令）混杂在提示词中，让模型每次决策时自行从冗长的上下文重构相关状态。这种设计存在两个关键不足：一是代理可能检索到正确事实，但后续的决策却基于过时、缺失或错误的信息进行判断；二是即使工具调用语法正确，也可能因未能结合当前任务状态而违反领域策略（例如在不符合退换条件的订单上执行退款）。LedgerAgent 通过引入独立、结构化的状态记录来解决这些问题。它将成功的工具返回结果存入基于模式锚定的分类账本（以规范路径为键的紧凑类型字典），并在每次交互时注入提示词，使代理能直接查表而非搜索原始记录。该方案还设置了策略门控机制，在执行改变环境的工具调用前，将提议调用映射为分类账字段上的谓词进行合规检查，从源头阻止策略违规。这种方法通过改变状态表征方式（保持模型权重不变），提升了代理在多次试验中的一致性表现。

### Q2: 有哪些相关研究？

主要的相關研究可分為三類。首先是互動式工具使用智能體領域，早期的工具使用基準與數據集專注於模型規劃、選擇API及生成合法呼叫的能力，但最新的客服基準結合了對話、結構化記錄、領域API與運營政策，揭示了智能體故障常源於資訊深埋於互動歷史中。

其次是推理時支架方法，如規劃與推理框架（鼓勵分解任務）、反思方法（利用回饋改善後續行為）、輸入重組（如IRMA引入領域規則與工具建議）及多智能體方法（如FAMA動態選擇專家智能體）。這些方法仍依賴語言模型從對話記錄中恢復當前任務狀態，在後續操作依賴精確記錄、標識符或有效工具參數時不可靠。

最後是政策合規性領域，先前基準強調遵循政策的重要性，但多數實現將規則放入提示詞或依賴模型自行推理操作是否允許。本文的LedgerAgent針對此缺口，透過維護一個結構化的獨立帳本（ledger）來明確追蹤觀察到的任務狀態，並在執行環境改變的工具呼叫前檢查狀態依賴的政策約束。與依賴訓練、提示或編排的方法相比，本文將狀態追蹤與政策遵循視為系統級機制，輔助而非取代模型推理。

### Q3: 论文如何解决这个问题？

LedgerAgent通过引入两个确定性组件来解决标准工具调用代理中状态管理隐式化导致的失败模式：一个账本（ledger）和一个策略门控（policy gate）。整体框架围绕一个循环运行：每次交互中，模型接收消息、更新账本、渲染账本到提示中、生成响应或工具调用，并在执行环境改变型调用前进行策略检查。

账本是核心创新，它是一个基于域模式（domain schema）的字典，将成功只读工具调用返回的观测状态结构化存储。每个域提供固定的工具路径映射，将返回记录路由到规范路径（如orders.1234），更新仅发生在成功的只读工具调用后，遵循“观测而非假设”原则，确保状态源自外部系统。渲染时，账本作为独立块（ledger block）添加进提示，列出所有已观测记录及其规范路径，使模型能轻松定位当前状态，避免在历史中搜索JSON。

策略门控是第二个关键组件，在环境改变型调用执行前立即运行。它基于当前账本状态评估可执行谓词（predicates），返回“允许”（allow）、“修正”（revise）或“阻止”（block）。允许则继续执行；修正则移除违规调用并添加反馈给模型下一轮；阻止则拒绝整个动作。门控仅验证，不选择工具或修复参数。谓词是领域级别的确定性代码，检查所有权、实体状态前提、参数锚定等常见约束。

该方法不引入额外LLM调用，账本更新、渲染和策略检查均为确定性操作，保持与标准代理相同的成本不变式。开发者需为新领域指定工具路径映射和可执行谓词，这些是领域级而非任务级组件，适用于结构化工具使用场景。

### Q4: 论文做了哪些实验？

论文在四个客户服务领域（航空、零售、电信、远程医疗）上进行了实验，数据集来自τ²-bench和τ-Trait。对比方法为标准基于提示的工具调用基线（FC）以及近期上下文工程方法IRMA。实验使用了6种骨干模型：GPT-5.2、GPT-4.1、Kimi K2.5、GLM-5、MiniMax-M2.5和Qwen3-30B，温度设为0.0，每个任务运行4次独立试验。主要结果：LedgerAgent在pass@1和pass@4上全面优于基线。在非GPT骨干模型上，相较于FC基线，Kimi K2.5提升3.4（pass@1）/5.6（pass@4）点；GLM-5提升4.7/7.6点；MiniMax M2.5提升7.3/8.3点。在GPT-4.1和GPT-5.2骨干上，pass@1分别提升12.2和15.5点。与IRMA对比，LedgerAgent在pass@1和pass@4上分别高出3.7和7.4点，且无额外token开销（IRMA开销达53.1%）。在需要环境改变工具调用的子集任务中（共254个任务），LedgerAgent同样表现更优，尤其在电信领域效果显著。错误分析显示主要失败原因为遗漏必要动作。

### Q5: 有什么可以进一步探索的点？

LedgerAgent的局限为未来研究提供了多个方向。首先，其高度依赖结构化工具返回和可预定义的领域模式，对于非结构化、视觉或隐性状态（如自然对话中的情感或意图）几乎无效。未来可探索将LedgerAgent与视觉语言模型或隐式状态推理方法结合，通过多模态输入动态构建更鲁棒的状态表示。其次，当前仅依赖“观察到”的状态，无法处理未检索事实或环境变更后的状态盲区。一个改进思路是引入主动“状态验证”机制，在关键决策点前自动触发读取工具以更新Ledger，或利用置信度评分剔除陈旧信息。此外，领域模式的构建仍需人工编码策略谓词，未来工作可研究从历史对话或少量示例中自动归纳约束规则，甚至通过强化学习让Agent在交互中动态学习策略边界。最后，评估局限于固定模拟器和有限基准，未来应在真实用户环境、长对话及动态策略变更场景下验证其鲁棒性，并探索如何平衡Ledger的详细程度与token成本。

### Q6: 总结一下论文的主要内容

LedgerAgent提出了一种针对政策合规工具调用智能体的推理时方法。核心问题是状态接地：在标准智能体中，任务状态未单独表示，导致代理可能基于过时、缺失或错误的信息做决策，或虽然语法有效但违反依赖当前状态的域策略。该方法引入两个确定性组件：基于模式的账本，存储成功的只读工具返回作为类型化状态；以及策略门，在执行环境改变的工具调用前检查其与当前状态的一致性。跨四个客服领域和多种基础模型，LedgerAgent在保持模型权重不变的情况下，提升了政策合规的工具使用，尤其在一致性导向的pass^k指标和需要环境改变的任务上提升最大。错误分析显示剩余失败主要是遗漏动作和特定领域参数错误。这项工作的意义在于它支持一个简单设计原则：决定动作有效性的状态应被显式表示和检查，而非仅留存在不断增长的提示历史中。
