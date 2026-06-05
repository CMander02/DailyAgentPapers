---
title: "The End of Software Engineering: How AI Agents Are Fundamentally Restructuring the Software Paradigm"
authors:
  - "Zhenfeng Cao"
date: "2026-06-04"
arxiv_id: "2606.05608"
arxiv_url: "https://arxiv.org/abs/2606.05608"
pdf_url: "https://arxiv.org/pdf/2606.05608v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Agent范式"
  - "软件工程"
  - "Agent-as-a-Service"
  - "LLM驱动的Agent"
  - "多智能体协作"
  - "SWE-bench"
  - "Agent架构"
relevance_score: 9.5
---

# The End of Software Engineering: How AI Agents Are Fundamentally Restructuring the Software Paradigm

## 原始摘要

For over half a century, software engineering has operated on a foundational premise: human engineers decompose problems, encode decision logic into static code, and manually adapt that code as requirements evolve. This paper argues that the emergence of AI agents -- systems where large language models serve as the primary reasoning engine, dynamically generating and discarding code as an instrumental resource -- constitutes not an incremental improvement but a fundamental restructuring of the software paradigm. Drawing on first-principles analysis of complexity scaling, we formalize the distinction between traditional software (where code is the carrier of decision logic) and agentic systems (where code is ephemeral tooling for an LLM-driven reasoning loop). We trace the historical arc from licensed software to SaaS to what we term Agent-as-a-Service (AaaS), showing that each shift transferred additional complexity away from end-users. We introduce the concept of Agentic Engineering as an emergent discipline -- distinct from software engineering in its core object of study, control model, and human role. Through analysis of recent benchmark evidence including SWE-bench Verified, EvoClaw, and LangChain's multi-agent coordination studies, we demonstrate both the transformative potential of the agentic paradigm and its current limitations. We conclude with a four-stage roadmap toward self-evolving agent ecosystems and concrete recommendations for practitioners navigating this transition.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决软件工程领域一个根本性的结构危机：随着系统规模增长，软件复杂度呈指数级增长（交互路径数量为Θ(2^n)），而人类工程师的认知能力却基本恒定，导致大型软件项目边际生产力持续下降。传统软件工程通过模块化、分层设计等方法来管理复杂度，但这些方法只能降低常数因子，无法改变复杂度增长渐近行为。现有方法的根本缺陷在于：所有决策逻辑必须预先由人类工程师显式编码到静态代码中，每次需求变更都需要人工理解、定位、修改和验证，这导致"本质复杂性"永无休止地增长。为了从根本上突破这一瓶颈，本文提出了一个新的范式——基于AI代理(Agent)的软件系统，其中大语言模型(LLM)作为核心推理引擎，在运行时动态生成代码作为瞬态工具，而非将代码视为系统本身的载体。这种转变彻底改变了代码的角色：从静态决策逻辑的载体变为LLM推理循环的临时工具，使得系统能够通过模型能力（随训练计算量指数级增长）来非线性地处理复杂度，从而将问题求解能力与人类认知极限解耦。论文将这一转变定位为继"许可软件→SaaS"之后的第三次重大范式转移——"代理即服务"(AaaS)。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要可分为以下几类：

**方法类研究**：本文与利用大语言模型（LLM）进行代码生成的研究（如AI-augmented development）相关，但明确指出此类研究仅将AI作为加速编码的工具，并未改变传统软件工程的本质。本文提出的Agentic Engineering强调LLM作为核心推理引擎，动态生成并丢弃代码，与Kumar和Ramagopal提出的“AI coding agents”和“agentic engineering”概念形成互补，后者更侧重跨团队工作流编排。

**评测类研究**：论文引用了SWE-bench Verified、EvoClaw和LangChain的多智能体协调研究等基准测试证据。这些研究证明了智能体范式在软件开发任务中的变革潜力，同时也揭示了其当前局限，如代码可靠性、状态管理和长上下文记忆等问题。本文在此基础上提出了从AI辅助编码到自主智能体演进的四阶段路线图。

**应用与范式类研究**：论文将SaaS到AaaS的转变视为第三次范式转移，这与Salesforce、AWS等SaaS服务商，以及OpenAI、Anthropic等提供智能体服务的公司相关。区别于传统软件（代码即决策逻辑载体）和SaaS（供应商负责基础设施），AaaS模式下智能体自主理解、构建和运行，实现了“结果交付”而非“软件交付”。

### Q3: 论文如何解决这个问题？

论文通过重新定义软件范式的底层原理，提出一个以LLM为核心推理引擎的Agent系统架构（A = (M, T, M, Π)），从根本上替代传统静态代码范式。核心方法是借助第一性原理分析，明确指出传统软件中决策逻辑D必须由人类预先编码，导致复杂度呈2^n指数增长，而人类认知能力固定，形成不可逾越的瓶颈。Agent系统则让LLM在运行时动态生成和丢弃代码，将代码视为为推理循环服务的临时工具，从而将问题解决能力从人类认知限制中解耦。

整体框架以“感知-记忆-动作”三模块为核心：感知模块处理多模态输入，记忆模块维护语义、情景和过程知识，动作模块执行内部推理与外部工具调用，所有模块由LLM推理核心统一编排。关键技术包括ReAct模式的推理-行动交织、链式思维提示的中间推理步骤，以及Hermes Agent中实现的闭环自我进化机制——代理在完成复杂任务后自动创建可复用技能（Skills），并在后续使用中自我修复和优化，同时通过FTS5支持的会话搜索实现跨会话情景记忆。

创新点在于提出了“Agent工程”这一新学科，其核心研究对象从静态代码变为动态代理系统，控制中心从人类工程师转为LLM，开发周期从线性设计-编码-测试变为自主迭代循环。人类角色从代码编写者转变为意图架构师、协调者和审计者，价值体现在目标清晰定义、多代理架构监督、质量校准和伦理治理上，从而突破了传统软件工程由人类认知决定的复杂度天花板。

### Q4: 论文做了哪些实验？

论文通过四个基准实验验证了AI代理对软件范式的重构。实验设置包括：SWE-bench Verified基准测试中，Lingma SWE-GPT 72B模型解决了30.20%的GitHub问题（接近GPT-4o的31.80%），其7B变体也解决了18.20%；多代理协调实验中，协调代理系统在20+企业调试工作流中减少93%根因定位时间，单月节省200+工程小时；Hermes Agent框架实现了自主技能创建与自我进化，通过179,000+GitHub星的开源系统验证了闭式学习循环；EvoClaw基准测试揭示了关键限制：代理在持续进化场景中性能从82%暴跌至38%，暴露出上下文漂移、错误传播、技术债务感知缺失和验证保真度不足四大挑战。论文指出这些局限源于上下文窗口限制、记忆架构缺陷和验证机制不完善，属于活跃研究范畴。

### Q5: 有什么可以进一步探索的点？

论文的四个阶段路线图清晰但过于乐观，忽略了一个核心挑战：在第四阶段“自进化生态系统”中，如何保证LLM驱动的智能体在动态生成与丢弃代码时，不引入系统性错误或安全漏洞？当前SWE-bench等基准测试仅验证孤立正确性，而真实世界需要长期可靠性、可维护性与对齐性。未来研究方向包括：1) 开发跨长期状态的上下文压缩与检索架构，解决EvoClaw中体现的推理连贯性丢失问题；2) 设计面向时间维度的验证框架，而非仅关注单次任务正确性；3) 研究多智能体对齐，确保集体行为符合人类价值，这比单智能体对齐更复杂；4) 探索结果定价等新经济模型，以匹配Agent-as-a-Service的颠覆性。此外，论文低估了人机协作中“意图工程”的难度——如何将模糊需求精确转化为可执行指令仍是瓶颈。改进思路包括引入交互式细化循环，让智能体主动提问以消歧义，而非被动执行。

### Q6: 总结一下论文的主要内容

这篇论文认为AI代理的出现代表了软件范式的根本性重构，而非工具升级。传统软件工程的核心前提是人类工程师将决策逻辑编码为静态代码并手动适应需求变化，而代理系统则以大语言模型为推理引擎，动态生成和废弃代码作为临时工具。论文通过第一性原理分析，形式化了传统软件（代码承载决策逻辑）与代理系统（代码是LLM驱动推理循环的临时工具）的区别。作者追溯了从许可软件到SaaS再到代理即服务（AaaS）的历史演变，指出每次转变都将复杂性从终端用户转移。论文引入“代理工程”作为新兴学科，其研究对象、控制模型和人类角色均不同于软件工程。基于SWE-bench Verified、EvoClaw等基准证据，论文展示了代理范式的变革潜力及当前局限性，并提出了通向自我进化代理生态系统的四阶段路线图，为从业者提供了实践建议。
