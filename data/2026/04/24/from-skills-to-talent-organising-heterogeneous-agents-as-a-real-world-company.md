---
title: "From Skills to Talent: Organising Heterogeneous Agents as a Real-World Company"
authors:
  - "Zhengxu Yu"
  - "Yu Fu"
  - "Zhiyuan He"
  - "Yuxuan Huang"
  - "Lee Ka Yiu"
  - "Meng Fang"
  - "Weilin Luo"
  - "Jun Wang"
date: "2026-04-24"
arxiv_id: "2604.22446"
arxiv_url: "https://arxiv.org/abs/2604.22446"
pdf_url: "https://arxiv.org/pdf/2604.22446v1"
categories:
  - "cs.AI"
tags:
  - "多智能体系统"
  - "组织框架"
  - "动态配置"
  - "人才市场"
  - "E2R树搜索"
  - "PRDBench"
relevance_score: 9.5
---

# From Skills to Talent: Organising Heterogeneous Agents as a Real-World Company

## 原始摘要

Individual agent capabilities have advanced rapidly through modular skills and tool integrations, yet multi-agent systems remain constrained by fixed team structures, tightly coupled coordination logic, and session-bound learning. We argue that this reflects a deeper absence: a principled organisational layer that governs how a workforce of agents is assembled, governed, and improved over time, decoupled from what individual agents know. To fill this gap, we introduce \emph{OneManCompany (OMC)}, a framework that elevates multi-agent systems to the organisational level. OMC encapsulates skills, tools, and runtime configurations into portable agent identities called \emph{Talents}, orchestrated through typed organisational interfaces that abstract over heterogeneous backends. A community-driven \emph{Talent Market} enables on-demand recruitment, allowing the organisation to close capability gaps and reconfigure itself dynamically during execution. Organisational decision-making is operationalised through an \emph{Explore-Execute-Review} ($\text{E}^2$R) tree search, which unifies planning, execution, and evaluation in a single hierarchical loop: tasks are decomposed top-down into accountable units and execution outcomes are aggregated bottom-up to drive systematic review and refinement. This loop provides formal guarantees on termination and deadlock freedom while mirroring the feedback mechanisms of human enterprises. Together, these contributions transform multi-agent systems from static, pre-configured pipelines into self-organising and self-improving AI organisations capable of adapting to open-ended tasks across diverse domains. Empirical evaluation on PRDBench shows that OMC achieves an $84.67\%$ success rate, surpassing the state of the art by $15.48$ percentage points, with cross-domain case studies further demonstrating its generality.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前多智能体系统在应对开放域复杂任务时存在的根本性缺陷。研究背景是，尽管单个AI智能体通过模块化技能和工具集成已具备强大能力，但多智能体系统仍受限于固定团队结构、紧耦合的协调逻辑以及会话绑定的学习机制，无法像现实企业一样灵活组织、动态演化。现有方法（如CrewAI、AutoGen）要么硬编码团队拓扑导致脆弱性，要么允许自由协商却缺乏收敛保证；不同框架的智能体因运行时隔离而无法互操作；角色仅通过描述性提示而非可执行契约定义，导致能力幻觉；自我改进也局限于特定框架和会话。这些系统本质上缺乏一个将组织层与能力层解耦的统一抽象，从而无法泛化到开放、跨领域的真实项目。因此，本文要解决的核心问题是：如何构建一个能像真实公司一样自动组织、协调并持续进化的AI智能体工作力量，使其能够自主分解任务、动态组建团队、跨异构运行时执行，并通过闭环反馈实现组织和个体层面的双轨学习，从而应对开放式的复杂任务。

### Q2: 有哪些相关研究？

本文的相关研究主要分为以下几类：

**方法类**：
- **CrewAI、AutoGen、Paperclip**等现有多智能体协调框架：本文指出这些方法要么硬编码团队结构（缺乏灵活性），要么让智能体自由协商（无收敛保证）。OMC通过引入类型化组织接口和E²R树搜索，实现了结构化协调与动态重构。
- **动态智能体工作流**相关研究：现有工作虽能在运行时调整任务分解，但局限于预配置沙箱（固定团队、统一运行时）。OMC通过人才市场和DAG任务执行，允许跨异构后端的动态招聘与重新配置。

**应用类**：
- **PRDBench基准测试**中的项目级软件开发系统：OMC在零样本单次尝试下达到84.67%成功率，超越所有基线（高出15.48个百分点），展示了从固定流水线到自组织系统的跃升。

**评测与分析类**：
- **技能与工具市场**（如LangGraph工具链）：本文指出技能仅作用于单智能体，而OMC的"人才"概念将复用单元从工具提升为具备完整生命周期管理的智能体身份，并通过跨领域案例验证了通用性。

**核心区别**：现有工作聚焦于"智能体如何交互"（多智能体系统层）或"智能体能做什么"（技能层），而OMC首次引入**组织层抽象**，将智能体视为可招聘、评估、进化的员工，实现了与人类企业组织原则的类比。

### Q3: 论文如何解决这个问题？

OMC的核心方法是将多智能体系统提升到组织层面，通过三个支柱实现异构智能体的组织和管理。

首先，OMC引入了“人才(Talent)”和“容器(Container)”的概念，将智能体的认知身份（提示词、角色、技能、工具等）与运行环境解耦。每个员工由可移植的Talent和运行时Container组成，Container提供六种类型化的组织接口（执行、任务管理、事件通信、存储、上下文组装和生命周期管理），使异构后端（如LangGraph、Claude Code、脚本执行器）能够在统一平台上共存。

其次，OMC设计了“探索-执行-评审”(E²R)树搜索作为核心决策机制。该机制将项目执行组织为统一的层次化循环：自上而下分解任务为可问责单元，自下而上聚合执行结果进行系统评审和优化。E²R树包含分解边和依赖边，确保形成有向无环图，并提供终止和无死锁的形式化保证。系统在决策点选择五种动作：分解、分配、招聘、评审和迭代。

第三，OMC集成了社区驱动的人才市场(Talent Market)，支持按需招聘。当项目需要特定能力时，HR智能体查询人才市场，筛选经过社区验证的Talent包，经CEO批准后自动部署。人才市场有三种来源：社区贡献、AI推荐组装和内部晋升。

这些设计使多智能体系统从静态、预配置的管道转变为自组织和自改进的AI组织，在PRDBench上实现了84.67%的成功率，超过现有最佳方法15.48个百分点。

### Q4: 论文做了哪些实验？

论文在PRDBench基准测试上进行了实验评估。实验设置包括将OMC与多种多智能体系统及方法论进行对比，包括AutoGen、CrewAI、OpenAI Swarm、MetaGPT、ChatDev和OpenHands等，采用统一的评估协议（如相同模型、任务和评估指标）。主要结果：在成功执行率上，OMC达到84.67%，比最佳基线（ChatDev，72.35%）高出15.48个百分点，较AutoGen（69.19%）提升15.48%，且大幅超越CrewAI（13.43%）、OpenAI Swarm（26.87%）和OpenHands（42.54%）。在平均任务成本上，OMC为0.199美元，较OpenAI Swarm（0.012美元）高但比AutoGen（0.367美元）和ChatDev（0.327美元）低。此外，论文通过跨领域案例研究展示了OMC的通用性，涵盖代码库审计、数据分析（碳排放/活动成本分析）和潜在新应用场景（如AI律师），验证了其在不同领域的任务适应性和自组织能力。

### Q5: 有什么可以进一步探索的点？

这篇论文提出的OneManCompany框架在组织层面实现了多Agent系统的动态自组织，但仍存在若干值得探索的局限。首先，当前“Talent Market”的供需匹配机制较为简单，未来可引入基于强化学习的拍卖式竞价机制，让Agent根据任务复杂度动态调整报价，实现更优的资源配置。其次，E²R树搜索虽然保证了终止性，但其探索效率在极大规模任务中可能下降，可尝试将蒙特卡洛树搜索与分层强化学习结合，通过价值函数近似加速决策。再者，当前系统缺乏跨会话的长期知识积累，建议引入经验回放池或图数据库，将历史成功策略提炼为可复用的组织记忆。此外，异构Agent的“能力鸿沟”问题——如部分Agent依赖专有API — 可通过联邦学习框架实现隐私保护下的协同优化。最后，在真实企业环境中的部署需考虑鲁棒性，建议引入基于博弈论的激励机制，平衡Agent们的利己行为与全局目标。

### Q6: 总结一下论文的主要内容

OneManCompany (OMC) 提出了一种将多智能体系统提升至组织层面的框架，解决了现有系统依赖固定团队结构、紧耦合协调逻辑和会话内学习的根本缺陷。OMC 将技能、工具和运行时配置封装为可移植的“Talent”身份，并通过类型化的组织接口桥接异构后端。其核心包括：一个社区驱动的“Talent Market”实现按需招聘和动态重组；一个“Explore-Execute-Review (E²R)”树搜索，通过自上而下的任务分解执行与自下而上的结果聚合审查，实现规划、执行与评估的统一层级循环，并提供了终止性和无死锁的形式化保证。在 PRDBench 基准测试中，OMC 在零样本单次尝试下达到84.67%的成功率，超出当前最优方法15.48个百分点。这项工作将多智能体系统从静态预配置管道转变为能够适应开放任务、自我组织与进化的AI组织，其意义在于为构建可扩展、跨领域的通用AI劳动力体系提供了基础架构和理论支撑。
