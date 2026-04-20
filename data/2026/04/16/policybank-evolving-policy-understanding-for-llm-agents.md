---
title: "PolicyBank: Evolving Policy Understanding for LLM Agents"
authors:
  - "Jihye Choi"
  - "Jinsung Yoon"
  - "Long T. Le"
  - "Somesh Jha"
  - "Tomas Pfister"
date: "2026-04-16"
arxiv_id: "2604.15505"
arxiv_url: "https://arxiv.org/abs/2604.15505"
pdf_url: "https://arxiv.org/pdf/2604.15505v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent 记忆"
  - "策略理解与演化"
  - "工具调用"
  - "对齐与合规"
  - "测试基准"
relevance_score: 9.0
---

# PolicyBank: Evolving Policy Understanding for LLM Agents

## 原始摘要

LLM agents operating under organizational policies must comply with authorization constraints typically specified in natural language. In practice, such specifications inevitably contain ambiguities and logical or semantic gaps that cause the agent's behavior to systematically diverge from the true requirements. We ask: by letting an agent evolve its policy understanding through interaction and corrective feedback from pre-deployment testing, can it autonomously refine its interpretation to close specification gaps? We propose PolicyBank, a memory mechanism that maintains structured, tool-level policy insights and iteratively refines them -- unlike existing memory mechanisms that treat the policy as immutable ground truth, reinforcing "compliant but wrong" behaviors. We also contribute a systematic testbed by extending a popular tool-calling benchmark with controlled policy gaps that isolate alignment failures from execution failures. While existing memory mechanisms achieve near-zero success on policy-gap scenarios, PolicyBank closes up to 82% of the gap toward a human oracle.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在遵循组织政策（通常以自然语言描述）时，因政策文本本身存在模糊性、逻辑漏洞或语义鸿沟，而导致其行为与真实要求系统性偏离的问题。研究背景是，随着LLM智能体在生产环境中承担越来越主动的角色，它们必须通过外部工具执行复杂工作流，同时严格遵守行为边界。现有方法（如护栏机制和动作级验证）虽然能有效强制执行约束，但都基于一个关键假设：书面政策是完整、无歧义的实际要求代理。然而在实践中，这一假设很少成立，因为自然语言规范天生存在模糊、欠规范和逻辑矛盾，导致政策规范与真实意图之间存在“规范鸿沟”。现有智能体记忆机制专注于提升任务执行能力，将输入政策视为不可变的真理，这反而会强化“合规但错误”的行为，无法质疑规范本身。因此，本文的核心问题是：能否让智能体通过交互和部署前测试中的纠正反馈，自主演化其对政策的理解，从而弥合规范鸿沟？论文提出PolicyBank这一记忆机制，通过维护结构化的、工具级的政策见解并迭代优化它们，使智能体能够自主检测和修正对不完美政策规范的理解偏差，而无需手动重写规则。

### Q2: 有哪些相关研究？

相关研究可分为三类：政策约束下的LLM智能体、自然语言政策规范的挑战，以及自进化智能体与智能体记忆。

在**政策约束下的LLM智能体**方面，相关研究主要包括评测与执行机制两类。评测工作如τ-Bench、ST-WebAgentBench、AgentHarm等，专注于评估智能体在特定领域或安全维度的政策合规性。执行机制如GuardAgent、ShieldAgent、VeriGuard、Progent和PCAS，通过在运行时拦截动作来强制执行政策，但它们均假设政策规范是完整且正确的。本文的PolicyBank则直接针对规范本身存在模糊与缺口的问题，通过迭代精炼理解来弥补缺口，与这些执行机制形成互补关系：PolicyBank负责优化规范理解，而验证层负责执行。

关于**自然语言政策规范的挑战**，传统访问控制领域（如RBAC、策略更新问题）已对政策管理进行了深入研究，但多基于形式化语言，且验证策略变更安全性本身计算复杂。本文将此经典问题适配到LLM智能体处理自然语言规范的场景，引入结构化记忆作为中间表示，兼具机器可执行和人类可审计的特性。

在**自进化智能体与智能体记忆**领域，现有进化机制主要针对执行失败（Type I）。基于轨迹的方法（如Synapse、AWM、Voyager）从成功中学习，但无法纠正规范缺口导致的“合规但错误”行为。基于反思的方法（如Reflexion、ExpeL、ReasoningBank）虽能从失败中学习，但存储的是任务级洞察，而非工具级授权约束洞察。生产记忆系统则只提供存储基础设施。本文提出的PolicyBank首次探索了利用进化记忆来解决政策演化这一实践性难题，使智能体能通过交互与反馈自主完善对不完美规范的理解。

### Q3: 论文如何解决这个问题？

论文通过提出PolicyBank这一记忆机制来解决LLM智能体在组织政策下因自然语言规范存在模糊性和逻辑/语义鸿沟而导致行为偏离真实要求的问题。其核心方法是构建一个结构化的、可迭代演进的记忆库，使智能体能够通过交互和测试反馈自主完善对政策的理解，而非将政策视为不可变的真理。

整体框架分为在线执行和离线维护两个循环阶段。在线阶段，智能体在处理测试任务流时，通过调用检索工具`retrieve_policy()`动态获取与当前对话上下文相关的政策条目，以此指导其工具调用行为。离线阶段，一个专门的策略代理（Policy Agent）会分析任务轨迹和开发者反馈，识别行为与真实需求之间的差异，并据此更新记忆库。

主要模块包括：1）**记忆模式（Memory Schema）**，它以工具-能力（tool-capability）级别存储条目，每个条目包含能力标识符和Spec_NL字段。Spec_NL采用半结构化格式，将模糊的自然语言政策文本分解为可执行的授权逻辑，包括触发条件、前提条件、资格条件和操作步骤，并设有关键见解（KEY INSIGHT）字段来捕捉学习到的规范与真实需求之间的差异。2）**智能体触发的检索（Agent-Triggered Retrieval）**，将检索设计为可调用工具，使智能体能在长程对话任务中根据上下文动态获取精准的政策片段，避免了将整个政策注入上下文窗口的可扩展性问题。3）**通过策略代理进行记忆维护（Memory Maintenance via Policy Agent）**，该代理在每次任务后离线工作，根据轨迹和反馈执行添加新条目、修订现有条目或保持不变的操作。开发者反馈包括二元奖励信号和自然语言解释，策略代理利用论文中定义的政策鸿沟分类法，专注于澄清授权逻辑而非重复有缺陷的规范。

创新点在于：首先，将政策视为可演化的理解对象，而非静态事实，通过迭代反馈闭环主动修正“合规但错误”的行为。其次，设计了细粒度的工具-能力级别结构化记忆模式，使授权逻辑清晰且可审计。最后，实现了动态、按需的检索机制与离线专业化分析相结合的更新流程，从而系统性地缩小规范鸿沟。

### Q4: 论文做了哪些实验？

实验在扩展的τ-Bench（航空和零售领域）上进行，采用流式评估协议以严格衡量适应性。任务流包含原始任务及其对应的“姐妹任务”（专门设计用于测试策略更新泛化能力的变体），以隔离智能体执行“一次性”策略更新的能力。实验使用了5个不同的随机种子来打乱任务顺序，并固定策略代理和用户模拟器为Gemini-3.0-Pro，所有模型温度设为0.0以最小化随机性。

对比方法包括：无记忆基线（标准工具调用智能体）、以及三种先进的记忆框架——Synapse（轨迹即示例）、Agent Workflow Memory（抽象工作流图）和ReasoningBank（存储自然语言关键见解）。为确保公平，所有基线方法均被调整为在每次用户轮次后动态检索记忆。

评估采用P@k指标（k次独立试验均成功的概率，k=1至4），重点关注策略存在差距的姐妹任务上的表现。主要结果显示，在姐妹任务上，无记忆基线表现崩溃（例如航空领域Gemini-3-Pro的P@1从原始任务的0.66降至近0.00），而标准记忆机制（Synapse、AWM）改进甚微甚至更差。ReasoningBank有所提升，但PolicyBank显著优于所有基线。例如，在零售领域，Claude-4.5-Opus上PolicyBank的P@1达到0.78，而最佳基线为0.45；在航空领域，Gemini-3-Pro上PolicyBank的P@1为0.74，远高于其他方法。此外，PolicyBank在更严格的P@k指标（如P@4）上也表现出更高的行为一致性。这表明PolicyBank能有效解决策略差距，将智能体行为与真实需求对齐，同时保持原始任务上的高性能。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于其测试环境相对理想化，主要针对受控的政策缺口，而现实中的组织政策往往更为复杂、动态且充满噪声。未来研究可首先扩展测试基准，引入更丰富的政策拓扑结构和多轮交互场景，以评估模型在模糊、冲突甚至对抗性反馈下的鲁棒性。其次，当前方法依赖于高质量反馈，未来可探索如何从稀疏或带噪声的反馈中有效学习，例如通过主动查询或不确定性校准。此外，可考虑将政策理解模块与形式化验证结合，为关键决策提供可证明的合规保证，同时探索在开源模型上的适配，以降低部署成本。最后，可研究如何将政策记忆与其他长期记忆机制动态整合，使智能体不仅能修正误解，还能主动预测政策演变趋势。

### Q6: 总结一下论文的主要内容

该论文针对LLM智能体在组织政策约束下运行时，常因自然语言政策描述存在模糊性、逻辑或语义缺口而导致行为偏离真实要求的问题，提出了一种名为PolicyBank的记忆机制。核心贡献在于摒弃了将政策视为不可变真理的传统做法，允许智能体通过预部署测试中的交互和纠正反馈，自主演化并细化其政策理解，从而系统性地填补规范缺口。方法上，PolicyBank维护结构化的、工具层级的政策洞察，并对其进行迭代优化，避免了现有记忆机制可能强化“合规但错误”的行为。论文还构建了一个系统性测试平台，通过扩展一个流行的工具调用基准并引入受控的政策缺口，将对齐失败与执行失败隔离开来。实验表明，现有记忆机制在政策缺口场景下成功率近乎为零，而PolicyBank能将与人类专家基准的差距缩小高达82%，显著提升了智能体在复杂政策环境下的对齐能力和可靠性。
