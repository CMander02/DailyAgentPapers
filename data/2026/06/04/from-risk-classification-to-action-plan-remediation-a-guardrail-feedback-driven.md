---
title: "From Risk Classification to Action Plan Remediation: A Guardrail Feedback Driven Framework for LLM Agents"
authors:
  - "Yuhao Sun"
  - "Jiacheng Zhang"
  - "Shaanan Cohney"
  - "Zhexin Zhang"
  - "Feng Liu"
  - "Xingliang Yuan"
date: "2026-06-04"
arxiv_id: "2606.05805"
arxiv_url: "https://arxiv.org/abs/2606.05805"
pdf_url: "https://arxiv.org/pdf/2606.05805v1"
github_url: "https://github.com/YUHAOSUNABC/TRIAD"
categories:
  - "cs.AI"
tags:
  - "Guardrail"
  - "Safety"
  - "LLM Agent"
  - "Plan Revision"
  - "Attack Mitigation"
  - "Multi-task Decision"
relevance_score: 9.5
---

# From Risk Classification to Action Plan Remediation: A Guardrail Feedback Driven Framework for LLM Agents

## 原始摘要

LLM-based guardrails typically safeguard agents by evaluating proposed actions or inputs before execution, producing safety signals such as binary allow/deny decisions, risk categories, and/or explanatory rationales about potential policy violations. However, agent risks often arise when otherwise benign tasks are contaminated by untrusted external content, unsafe instructions, or risky tool use. Existing guardrails often flag the entire task uniformly as unsafe, thereby blocking the threat but sacrificing the benign part. Moreover, existing work largely evaluates guardrails in isolation, leaving unclear whether their interventions lead to safer downstream agent behavior. To address this, we introduce TRIAD (Tripartite Response for Iterative Agent Guardrailing), a guardrail-integrated agent framework that leverages guardrail-generated verbal feedback as a guiding signal to keep the agent aligned with benign objectives at each planning step. We finetune a language model on a self-curated training dataset to output one of three decisions: proceed, refuse, or update, together with structured natural-language feedback. Rather than merely allowing or blocking execution, update guides the agent to revise its plan, avoid harmful components, and preserve the benign task where possible. TRIAD injects this feedback into the agent's context, enabling subsequent plan revision and forming a closed loop between guardrail feedback and agent planning. Extensive experiments on ASB and AgentHarm show that TRIAD reduces the average attack success rate to 10.42%, while achieving the best safety-utility trade-off among guardrail-integrated baselines. Our code is available at: https://github.com/YUHAOSUNABC/TRIAD.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有LLM代理安全防护机制在处理部分不安全任务时的局限性。研究背景是，LLM代理在复杂、开放环境中面临广泛的安全威胁，如提示注入攻击（PIAs），而现有防护机制通常在行动执行前进行二元判断（允许/拒绝）或风险分类。然而，这些方法存在一个核心不足：当用户请求混合了良性目标和恶意指令时（例如，一个包含安全操作和危险操作的任务），现有防护会一刀切地将整个任务标记为不安全，导致既阻止了威胁，也牺牲了良性任务部分。实验表明，现有防护的召回率仅58.57%，且即使检测到风险，攻击成功率和任务成功率仍不理想，说明二元输出无法有效指导下游代理行为。因此，本文要解决的核心问题是：如何设计一个防护框架，能在部分不安全场景下精准区分良性目标和有害部分，既阻止恶意执行，又保留并引导代理完成安全任务，从而在安全性和实用性之间取得更好平衡。

### Q2: 有哪些相关研究？

本研究的相关工作主要涵盖以下类别：

**方法类**：早期方法如AGrail、Safiron、WebGuard等将护栏模型作为运行时安全监控器，通过分层分类器或LLM审计器对中间行动计划进行风险检测，但干预方式多为简单的允许/拒绝二元判断。TRIAD的创新在于引入三路决策（Proceed/Refuse/Update）和结构化自然语言反馈，使护栏能从单纯阻断不安全行为转向指导智能体修复部分不安全的计划。

**评测与攻击类**：相关工作包括对间接提示注入（IPI）、直接有害任务（DH）和直接提示注入（DPI）三种攻击场景的建模，以及ASB和AgentHarm等基准。TRIAD在这些场景下进行评测，其关键区别在于将护栏反馈作为迭代信号注入智能体上下文，形成闭环修正机制。

**应用类**：与ToolSafe的TS-Guard相比，后者仅输出标量安全评分并依赖固定阈值进行二元判定，而TRIAD通过结构化决策和反馈实现了更精细的行为引导。此外，ReAct等经典智能体框架仅提供行动前的规划阶段，TRIAD则在此基础上构建了护栏-智能体的双向交互循环。

### Q3: 论文如何解决这个问题？

TRIAD 通过构建一个闭环的防护栏反馈驱动框架来解决现有方法的问题。其核心是训练一个名为 Tri-Guard 的三元决策模型（基于 Qwen3.5-9B 的微调模型），该模型可以输出三种决策：Proceed（继续执行）、Update（更新计划）和 Refuse（拒绝操作）。整体框架在 ReAct 智能体的每个规划步骤中，Tri-Guard 检查交互历史、当前计划、提议动作和可用工具，产生结构化的自然语言反馈和三元决策。当决策为 Update 时，通过上下文学习模板将反馈注入智能体的临时上下文，引导其修改计划以避免有害部分同时保留良性任务；当决策为 Refuse 时，引导智能体生成拒绝响应而不执行工具。这个过程可以迭代进行，形成防护栏反馈与智能体规划之间的闭环。关键技术包括：使用加权监督微调（wSFT）训练 Tri-Guard，通过知识蒸馏从教师模型获取训练数据，并使用教师模型的平均 token 对数似然作为置信度权重，高置信度样本获得更大权重。与仅产生允许/拒绝二值信号的现有防护栏不同，TRIAD 的 Update 决策使系统能在部分有害的轨迹上修订计划而非直接阻断整个任务，从而在安全性和实用性之间取得更好平衡。实验表明该方法将平均攻击成功率降至 10.42%。

### Q4: 论文做了哪些实验？

在实验部分，论文主要评估了TRIAD框架在降低攻击成功率与保持任务实用性之间的平衡。实验采用了Agent Security Bench (ASB)和AgentHarm两个基准测试集。ASB用于评估对抗性提示注入攻击（PIA），包含51个良性用户任务和40条攻击指令，形成2040个测试案例；AgentHarm用于评估直接有害任务（DH）的拒绝能力。主要对比方法包括无防御的ReAct基线、现有护栏模型（如Safiron-7B、ShieldLM-14B、TS-Guard等）以及TRIAD+训练后的护栏模型。关键指标包括攻击成功率（ASR）、任务成功率（TSR）和拒绝率（RR）。结果显示，TRIAD+训练护栏模型在ASB-DPI上ASR降至11.57%，TSR达60.83%；在ASB-IPI上ASR为6.05%，TSR为61.59%。在AgentHarm上，HS从无防御时的36.28提升至80.34，Harm Score从77.04降至9.87。相比现有护栏模型（如TS-Guard虽然ASR低但RR高达88.80%），TRIAD实现了最优的安全-实用性权衡，平均攻击成功率降至10.42%。

### Q5: 有什么可以进一步探索的点？

首先，TRIAD的推理延迟是其显著局限，未来可探索更轻量的护栏框架，如使用更小的模型或高效的检查机制，并研究无需完整重新规划的局部修订策略以降低成本。

其次，训练数据和模型规模均可扩展。更大规模、更多元的轨迹反馈数据能帮助模型在不同工具使用模式和攻击场景下学到更稳定的决策边界。同时，更强的基座模型有望提升对复杂代理行为的理解，值得探索。

此外，当前评估集中于特定攻击场景，面对真实世界中涌现的新攻击或组合攻击，泛化能力存疑。未来可研究如何通过少量样本适配实现零样本迁移，或在保持任务效用的同时进行轻量化微调。进一步地，可尝试引入对比学习或对抗训练来增强护栏对未知攻击的鲁棒性。最后，探索动态阈值机制，让代理能自适应调整“proceed/refuse/update”的决策边界，以及将护栏反馈与强化学习结合，形成持续优化的闭环学习范式，是很有前景的方向。

### Q6: 总结一下论文的主要内容

这篇论文提出了TRIAD，一个将护栏反馈与智能体规划闭环集成的框架。针对现有护栏仅做全局二元阻断、牺牲任务善意的缺陷，TRIAD创新性地定义了三元决策：继续、拒绝或更新。核心方法是在护栏模型中微调一个语言模型，使其不仅输出结构化自然语言反馈，还能生成“更新”指令，指引智能体在保留任务核心部分的同时，修正危险环节。通过在ASB和AgentHarm数据集上的实验，TRIAD将平均攻击成功率降至10.42%，并在安全性与任务效用间取得了最佳平衡。该工作的意义在于将护栏从被动的风险分类器升级为主动的行动规划指导器，有效解决了安全干预与任务完成之间的根本矛盾。
