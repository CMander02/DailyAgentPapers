---
title: "Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation"
authors:
  - "Yuchen Ling"
  - "Shengcheng Yu"
  - "Zhenyu Chen"
  - "Chunrong Fang"
date: "2026-06-09"
arxiv_id: "2606.10749"
arxiv_url: "https://arxiv.org/abs/2606.10749"
pdf_url: "https://arxiv.org/pdf/2606.10749v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "LLM Agent安全"
  - "威胁建模"
  - "对抗攻防"
  - "综述/元分析"
  - "Agent评估基准"
  - "权限控制"
relevance_score: 9.5
---

# Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation

## 原始摘要

Large language model (LLM) agents are rapidly moving from conversational interfaces to software components that plan, invoke tools, maintain memory, and act on external environments. This transition changes the nature of security risk. In agentic settings, failures are no longer limited to unsafe text generation. Untrusted content may redirect control flow, misuse tool privileges, corrupt persistent state, leak sensitive information, or trigger harmful external actions. At the same time, research on LLM agent security is expanding quickly but remains fragmented across attack families, defense layers, application domains, and evaluation settings. This paper synthesizes 247 papers through a lifecycle-based, systems-oriented framework that models agent security around the interaction of information flow, delegated authority, and persistent state. We organize the literature around four questions: how LLM agent security should be modeled, which threat surfaces and attack families dominate, what defenses have been proposed and with what tradeoffs, and how security claims are evaluated. We find that prompt injection and tool-mediated control-flow hijacking still dominate the field, while persistent state corruption and multi-agent propagation are becoming central emerging concerns. We further find that current defenses provide useful building blocks but remain weakly compositional, and that existing benchmarks still underrepresent long-horizon, stateful, and deployment-sensitive risks. We argue that secure LLM agents require explicit trust boundaries, principled privilege control, provenance-aware state management, and evaluation practices aligned with realistic operational settings.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）代理在从对话界面转向自主软件组件过程中面临的新兴安全挑战。随着代理系统具备规划、调用工具、维护记忆和执行外部操作的能力，其安全风险已从传统的“不安全文本生成”扩展到更为复杂的软件与系统安全问题，包括恶意指令劫持控制流、滥用工具权限、破坏持久状态、泄露敏感信息或触发有害外部操作。现有研究虽然增长迅速，但存在碎片化问题：不同攻击家族、防御层次、应用领域和评估设置之间缺乏统一框架，且术语、方法论和部署假设尚未稳定。尤其是，当前研究过度聚焦于“提示注入”这一单一主题，而对“持久状态破坏”、“工具中介的权限滥用”和“多代理传播”等日益重要的风险关注不足；同时，现有基准评测仍局限于即时攻击成功率的评估，对长期、有状态及部署敏感风险的覆盖不充分。因此，本文的核心目标是：通过一个基于生命周期的、系统导向的分析框架，系统性地整合247篇相关文献，厘清LLM代理安全应如何建模、识别主要威胁表面与攻击家族、梳理现有防御策略及其权衡，并审视当前安全评估方法的不足，从而为构建安全、可信的LLM代理提供理论基础和实践指南。

### Q2: 有哪些相关研究？

根据论文内容，相关研究可归类如下：

**方法类研究**：主要涵盖提示注入安全（75篇）、工具使用安全（156篇）和记忆安全（32篇）。本文与这些工作共享基础威胁模型，但指出当前防御缺乏可组合性，且多聚焦单点风险而非整体控制流完整性。

**应用类研究**：涉及多智能体安全（63篇）、运行时防御（88篇）以及具体的智能体系统（如网页浏览器、编码助手、具身智能体）。论文强调现有研究分散于不同应用域，而本文通过生命周期框架统一分析，特别关注持久状态污染和多智能体传播等新兴威胁。

**评测类研究**：现有基准主要评估短视任务，本文指出其不足——未能充分覆盖长周期、有状态和部署敏感的风险场景，呼吁建立更贴近实际操作环境的评估实践。

**区别与创新**：与仅关注文本安全的通用LLM安全研究不同，本文系统性地将智能体安全建模为软件系统问题，强调信息流、委托权限和持久状态三者的交互。通过247篇论文的综合分析，揭示当前领域虽以提示注入和工具劫持为主流，但持久状态破坏和多智能体传播正成为核心新兴挑战。

### Q3: 论文如何解决这个问题？

本文通过一个生命周期导向、系统化的分析框架来解决LLM Agent安全问题。整体框架围绕“信息流→控制流→持久化状态”的交互关系构建，将Agent安全建模为七元组A=⟨I,P,D,T,M,O,C⟩，分别代表输入上下文、规划、决策、工具执行、记忆/状态、外部输出和协调通道。安全风险产生于这些组件之间的流动：低权限内容可能扭曲规划、改变决策、触发特权工具调用、污染持久状态或通过协调通道传播。

核心方法包括：第一，构建了247篇论文的混合评审语料库，采用数据库检索、LLM辅助扩展和引文雪球三阶段流水线，并严格筛选，只纳入与Agent执行循环相关的安全研究。第二，通过结构化编码协议标注每篇论文的威胁面、攻击方法、防御机制和评估基准，区分单标签和多标签字段以支持多维分析。

关键技术在于识别了四大威胁面：Web内容、检索内容、工具输出、文件/代码和记忆/暂存区。研究发现提示注入和工具介导的控制流劫持仍是主导攻击家族，而持久状态污染和多Agent传播正在成为新兴关注点。防御方面，现有方案提供有用构件但缺乏组合性；评估基准仍低估长周期、有状态和部署敏感的风险。

创新点在于提出了一个统一的分析透镜，将分散的攻击家族、防御技术和评估实践整合到连贯的工程主题中：明确的信任边界、原则性权限控制、来源感知状态管理和符合实际操作环境的评估实践。

### Q4: 论文做了哪些实验？

该论文是一篇综述，并未开展新的实验。其核心是对247篇文献的系统性梳理和元分析。论文通过展示语料库的基本分布（出版年份、论文类型、系统设定）来揭示领域现状。实验设置上，无独立实验，而是对文献进行编码和统计。数据集/基准方面，分析了47篇基准论文和26篇评估论文，但指出现有基准在长期性、有状态性和部署敏感性风险上代表性不足。对比方法上，区分了攻击（66篇）与防御（64篇）两大类，并发现防御研究几乎与攻击研究并行发展。主要结果包括：1）时间分布高度集中，2023年仅3篇，2024年42篇，2025年激增至121篇，2026年前4个月已有81篇。2）arXiv预印本占68.42%（169篇），表明领域尚未形成稳定的发表体系。3）80.97%（200篇）聚焦于单智能体系统，多智能体仅占19.03%（47篇），但后者占比从2024年的9.52%上升至2025年的23.97%，显示其正在成为稳定的子领域。论文最终指出，当前研究仍以提示注入和工具介导的控制流劫持为主，对有状态腐败和多智能体传播的关注正在上升。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于当前防御手段仍停留在“建筑模块”层面，缺乏可组合的系统化框架。尽管研究揭示了提示注入、工具劫持和状态污染三大攻击面，但现有防御策略（如权限分离、状态溯源）多为针对单一攻击的对抗性补丁，尚未形成类似操作系统级安全机制的强隔离范式。未来可探索**基于信任边界的硬件级隔离**：例如将关键工具调用与LLM核心推理过程分离至不同安全域，通过TEE或形式化验证保证权限断言的可信性。其次，**持久化状态污染**的检测和恢复机制仍是空白。当前基准评测多聚焦单轮交互，但多智能体系统中恶意状态传播的累积效应可能指数级放大危害。建议引入混沌工程思想，构建动态故障注入环境，评估系统在长期运行中对抗状态腐化的鲁棒性。此外，可探索**安全向的微分隐私模型微调**，通过向注意力机制注入噪声最小化工具调用路径与敏感数据的依赖关系，从因果层面阻断信息泄漏。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型（LLM）代理从对话界面转向软件组件带来的新型安全风险，系统综述了247篇相关文献。其核心贡献在于提出了一个基于生命周期、面向系统的分析框架，将代理安全建模为信息流、委托权限和持久化状态三者的交互。论文围绕四个核心问题展开：安全模型、主要威胁面与攻击家族、防御机制及评估方法。主要发现包括：提示注入和工具介导的控制流劫持仍是主导威胁，但持久化状态破坏和多代理传播正成为新兴核心风险；现有防御提供了有用组件但缺乏组合性；现有基准测试低估了长期、有状态和部署敏感的威胁。论文主张，安全的LLM代理需要明确的信任边界、有原则的权限控制、来源感知的状态管理以及符合实际操作环境的评估实践。该研究为理解这一快速发展但碎片化领域提供了系统化、结构化的视角。
