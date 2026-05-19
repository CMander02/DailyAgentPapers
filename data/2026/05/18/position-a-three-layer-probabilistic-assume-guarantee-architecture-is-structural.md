---
title: "Position: A Three-Layer Probabilistic Assume-Guarantee Architecture Is Structurally Required for Safe LLM Agent Deployment"
authors:
  - "S. Bensalem"
  - "Y. Dong"
  - "M. Franzle"
  - "X. Huang"
  - "J. Kroger"
  - "D. Nickovic"
  - "A. Nouri"
  - "R. Roy"
  - "C. Wu"
date: "2026-05-18"
arxiv_id: "2605.18672"
arxiv_url: "https://arxiv.org/abs/2605.18672"
pdf_url: "https://arxiv.org/pdf/2605.18672v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent Safety"
  - "Probabilistic Assurance"
  - "Architecture Design"
  - "Runtime Monitoring"
  - "Multi-Agent Systems"
relevance_score: 8.5
---

# Position: A Three-Layer Probabilistic Assume-Guarantee Architecture Is Structurally Required for Safe LLM Agent Deployment

## 原始摘要

This position paper argues that enforcing LLM agent safety within a single abstraction layer is not merely suboptimal but categorically insufficient for deployed LLM agents -- a structural consequence of how agent execution works, not a contingent limitation of current systems. The three dimensions that jointly constitute safe operation -- semantic intent and policy compliance, environmental validity, and dynamical feasibility -- each depend on a strictly distinct set of information that becomes available at different stages of execution. No single guardrail can certify all three. We argue that the community must respond with a contract-based architecture in which each safety dimension is enforced by an independently certified layer whose probabilistic guarantee satisfies the next layer's assumption. We sketch such an architecture and derive the compositional system-level safety bounds it admits via the chain rule of probability. Three open problems stand between this and a deployable standard: bound estimation from non-i.i.d.\ traces, graceful degradation of contracts under deployment drift, and extension to multi-agent settings -- the most important unfinished business in LLM agent runtime assurance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决LLM智能体（LLM agent）在安全关键部署场景中的运行时安全保障问题。研究背景指出，LLM智能体不同于传统软件（行为可形式化指定）和静态语言模型（输出不作用于世界），它结合了非确定性推理与闭环执行，生成的计划会改变世界和后续观测，因此其安全挑战是开放式的且无法在设计时穷举。现有方法存在严重不足：单层防护设计（如内容过滤、提示工程或单一运行时监控）被证明是结构性不充分的，因为安全操作包含三个互不相同的维度——语义意图与策略合规性、环境有效性（如运行设计域ODD）以及动力学可行性——这些维度所需的信息在智能体执行的不同阶段才变得可用，任何单层架构必然至少遗漏一个维度。实证数据也佐证了这一点：16个流行智能体在AgentSafetyBench上无一达到60%的安全分数，且在Agent Security Bench上攻击成功率超84%，失败模式恰好集中在单层语义控制无法触及的环境和物理维度。因此，本文要解决的核心问题是：如何为LLM智能体设计一种结构上必要且充分的运行时安全架构，能够跨越这三个信息集不同的安全维度进行组合式认证。作者主张，必须采用一种基于概率假设-保证合约（probabilistic assume-guarantee contracts）的三层架构（用户层、运营层、功能层），通过链式法则推导出组合式的系统级安全边界，而非依赖任何一个更强的单一护栏。

### Q2: 有哪些相关研究？

根据论文内容，相关研究可以分为以下几类：

**1. 单层语义安全方法**：这类工作主要针对语义意图对齐和策略合规性。例如，AgentSpec 引入轻量级领域特定语言进行运行时约束执行，Agent-C 利用SMT求解编码时序安全约束，ShieldAgent 从政策文档中提取可验证规则。本文指出这些单层方法无法验证环境有效性和动态可行性两个维度。

**2. 环境与执行层方法**：包括分布外检测、内省机制（如 Inner Monologue）、以及基于时序逻辑的动作层约束（如 RoboGuard、Safety Chip）。本文认为这些方法要么是反应性的，要么无法独立判定执行是否被世界状态授权。

**3. 低层执行安全方法**：如基于规约的运行时监控、控制屏障函数（CBF）和强化学习中的屏蔽。本文指出这些方法的保证在环境假设被破坏时会退化，且MDP安全动态假设对LLM代理环境不成立。

**4. 跨层尝试与系统化分类**：Agent Behavioral Contracts 引入了概率满足概念，PRO²GUARD 扩展到概率域。Shamsujjoha等人提供了基于工件的运行时防护层分类。本文认为这些工作最接近，但关键区别在于组织原则：本文基于信息可验证的时间顺序而非工件类型来划分层次，从而能推导出组合概率保证。

**5. 实证评估与安全基准**：如 AgentSafetyBench 显示代理行为安全得分仅30.4%，Agent Security Bench 显示单层防御下攻击成功率超84%，印证了多层架构的必要性。

### Q3: 论文如何解决这个问题？

该论文提出的核心方法是三层概率假设-保证架构，其关键洞察是：单一抽象层的安全护栏在结构上不足以保障部署的LLM智能体安全。这是因为安全操作所需的三个维度——语义意图与策略合规、环境有效性、动态可行性——依赖于严格不同的信息集且在不同执行阶段才变得可用，单一层无法同时认证所有维度。

整体架构设计为信息驱动的三层层级结构：
1. **用户保证层** (User Layer)：在世界观察之前生效，基于用户指令、策略和角色元数据（不含传感器数据）验证计划是否符合认知、规范和伦理对齐。该层输出计划约束和排除区域，验证通过后形成下层假设。
2. **操作保证层** (Operational Layer)：在世界状态估计后、执行前生效，利用传感器数据和世界状态估计判定执行是否处在操作设计域 (ODD) 内，确定自治包络（自主等级、允许工具集、执行周期），并对ODD中无效子计划进行拦截。验证通过后形成功能性层的假设。
3. **功能保证层** (Functional Layer)：在控制回路执行期间持续运行，基于完整状态轨迹和控制输入，通过规范运行时监控、控制屏障函数 (CBF) 和仿真综合三种互补机制确保无碰撞、物理力受约束，触发违规纠正或安全停止。安全信号自底向上传播以支持计划重算。

核心创新点包括：
- **假设-保证合同链**：每层输出保证构成下一层的假设（Γ_U ⇒ A_O, Γ_O ⇒ A_F），使系统级安全概率可分解为链式条件概率乘积，不依赖独立假设；
- **信息驱动而非工件驱动的架构边界**：使条件概率估计与各层信息可用时间对齐，保证可独立审计；
- **概率安全界**：提供从边际概率到全条件概率的四级表征，最精确的是Pr(安全)= p_U · p_{O|U} · p_{F|OU}，层间失败概率不要求独立即可得到非平凡的Bonferroni下界。

### Q4: 论文做了哪些实验？

这篇论文进行的是论证性研究，未开展传统意义上的实验。其核心论点是：单一抽象层无法确保LLM Agent安全运行，必须采用三层概率性假设-保证架构。论文通过理论分析而非实验数据支撑这一主张。

论文提出的三层架构包括：语义意图与政策合规层、环境有效性层、动态可行性层。每层由独立认证模块负责，其概率保证作为下一层的假设条件。系统级安全界限可通过概率链式法则推导得出。

论文指出三个开放问题：1）非独立同分布轨迹的界限估计；2）部署漂移下的契约优雅降级；3）多Agent扩展。作者认为这些是LLM Agent运行时保障中最未解决的关键问题，并呼吁社区采用基于契约的架构。

论文未提供具体数据集、基准测试或对比方法，也未列出定量指标。其贡献在于从执行结构角度论证了分层保证的必然性，而非通过实验验证特定方法的有效性。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于其三层概率保证架构的认证可行性。首先,非独立同分布轨迹导致标准PAC理论失效,现有方法如鞅界、混合过程界、可交换共形预测和生存分析校准均未扩展至可变长度、跨异质层的满足事件；其次,区间估计的组合宽度随层数增长且覆盖依赖联合误差分布,PAC-Bayes与依赖图分解尚未应用；最后,共享LLM主干导致系统模型失败时相关层同时失效,假设独立性会过度估计联合失效概率使界过于保守。未来研究方向包括：开发基于e-过程的实时有效推理框架以处理非平稳token采样；利用PAC-Bayes界与依赖图分解联合优化组合区间宽度；采用独立于LLM参数的动力学模型实现功能层CBF解耦以缓解相关性；将完整性限制扩展至多智能体场景。此外,可通过存活时间分析和随机过程理论建立部署漂移下保证的优雅降级机制,并探索基于合约的可审计日志与运行时监控的协同方案。

### Q6: 总结一下论文的主要内容

这篇论文的核心主张是：在单一抽象层内保障LLM智能体安全是结构性不足的，而非仅仅是次优选择。作者指出，安全运行包含三个维度：语义意图与策略合规、环境有效性、以及动态可行性，这三个维度依赖的信息集在智能体执行的不同阶段才变得可用，因此任何单一防护栏都无法同时认证所有三个维度。论文提出了一种基于合约的分层架构，通过三个独立认证的层（用户层、运行层、功能层）来分别保障每个安全维度，利用概率性假设-保证合约进行顺序组合。关键结论是，这种三层架构是结构上必要的最小设计，并能通过概率链式法则导出组合性的系统级安全界限。论文还识别出三个关键开放问题：从非独立同分布轨迹中估计界限、部署漂移下的合约优雅降级、以及扩展到多智能体场景。这项工作的意义在于从根本上论证了LLM智能体运行时保障需要一种新的、分层的合约式架构，为安全关键部署提供了理论基础。
