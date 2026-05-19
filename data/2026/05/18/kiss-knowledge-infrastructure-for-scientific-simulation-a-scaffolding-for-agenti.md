---
title: "KISS - Knowledge Infrastructure for Scientific Simulation: A Scaffolding for Agentic Earth Science"
authors:
  - "Ziwei Li"
  - "Liujun Zhu"
  - "Yuchen Liu"
  - "Yichen Zhao"
  - "Birk Li"
  - "Ruiqi Wu"
  - "Junliang Jin"
  - "Jianyun Zhang"
date: "2026-05-18"
arxiv_id: "2605.17856"
arxiv_url: "https://arxiv.org/abs/2605.17856"
pdf_url: "https://arxiv.org/pdf/2605.17856v1"
categories:
  - "cs.AI"
tags:
  - "Scientific Agent"
  - "Knowledge Infrastructure"
  - "Agent-Tool Integration"
  - "Domain-Specific Agent"
  - "Agent Evaluation Benchmark"
relevance_score: 8.5
---

# KISS - Knowledge Infrastructure for Scientific Simulation: A Scaffolding for Agentic Earth Science

## 原始摘要

Process-based simulation models encode decades of scientific understanding across the Earth sciences, yet the communities most exposed to climate risk and resource scarcity are the least able to use them. Here, we introduce knowledge infrastructure (KI), an agent-actionable scaffold that externalizes expertise into validated modelling operators, staged domain protocols, and diagnostic recovery mechanisms. Across a 3,000-trial coupled-hydrology benchmark, agents equipped with KI produced physically plausible, verifiable end-to-end simulations in up to 84% of trials, while agents without KI plateaued below 40%. KI generalizes across disciplines. We packaged its construction into a Knowledge Dissection Toolkit (KDT) that autonomously produced KI enabling end-to-end agent execution of 117 additional process-based models across 14 Earth-science domains. Across all 119 KIs, modelling decisions and failure remedies converged despite different underlying physics, showing that operational expertise is structured and extractable rather than ad hoc. Demonstrations show KI-equipped agents lowering both the access barrier between non-specialist users and process-based simulation, and the integration barrier between modelling communities. Through this scaffold, process-based science can then evolve as a living scientific commons, answerable to whoever needs to know and extendable by whoever can contribute.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决一个核心问题：如何让非专业用户和缺乏经验的建模者能够可靠地使用基于过程的科学模拟模型，从而降低气候风险与资源稀缺领域的技术准入壁垒。研究背景是，尽管过程模型融合了数十年地球科学知识，但最易受气候影响的社区和最缺乏资源的群体反而最不擅长使用它们，而且即使是资源充足的团队，也常因跨专业操作知识散落、关键建模决策未被记录或仅依赖专家经验传承，导致同一模型产生不同结果。现有方法的不足主要体现在：大型语言模型（LLM）代理尽管能阅读文档、编写代码，但在科学模拟任务中表现不佳（最高仅54%成功率），因为建模决策是高维链条化的，有效性标准是隐性的，且每个选择都依赖历史路径，单个错误就会输出看似合理但科学无效的结果。因此，本文提出知识基础设施（KI）这一可被代理执行的脚手架，将领域专家的操作知识外化为验证过的建模算子、分阶段协议和诊断恢复机制，使代理从自由代码生成器转变为可信赖的、可恢复的建模管道操作者，从而在无需专家全程介入的前提下，实现端到端、科学有效的模拟执行。

### Q2: 有哪些相关研究？

主要相关研究可按方法类和应用类组织。方法类方面，本文与现有LLM Agent自主科学工作流研究（如ChemCrow、BioAgent等）紧密相关，区别在于指出这些自动化系统尚未成功应用于过程式科学模拟，因为最佳编码Agent在相关复现任务中成功率仅54%；本文提出的知识基础设施（KI）通过外部化操作知识而非让Agent自由生成代码，显著提升了成功率。应用类方面，相关工作涉及过程模型的可重复性研究，已有研究指出建模失败呈现特征模式、操作决策空间虽大但具有规律性，本文基于此设计诊断恢复机制。评测类方面，本文构建了3000次多Agent基准测试，对比有无KI的Agent表现，KI使成功率从低于40%提升至84%，超越了此前自动化Agent在类似任务中的极限。与这些工作的核心区别在于，本文不仅验证了KI在单个耦合水文模型上的有效性，还通过知识剖析工具包（KDT）将框架推广至14个地球科学领域的119个模型，证明了操作专业知识的结构化可提取性。

### Q3: 论文如何解决这个问题？

论文通过提出知识基础设施（KI）来解决问题，这是一种将领域专家的操作知识外化为智能体可执行模块的结构化框架。其核心方法围绕“知识解剖”过程展开，将隐性的操作专长从模型文档、源码、案例和实践中提取并转化为三类知识，分别编码为对应组件：程序性知识映射为验证过的建模算子，负责文件生成、单位转换、依赖解析和模式验证等底层操作；评估性知识映射为分阶段领域协议，对运行的物理和语义合理性进行时空一致性、参数范围、质量平衡和输出边界检查；诊断性知识映射为症状-诊断-补救的恢复机制，用于检测无显式错误信号但结果异常的失败。

整体架构分为两层：一是知识解剖工具包（KDT），可自动为地球科学领域的数学模型生成KI包，实现从手动构建到自动化生产的扩展；二是标准化执行环境（HydroCraft），提供模型二进制文件、数据集和智能体可访问的工作流。创新点在于将人类建模者流畅融合的三类操作知识（程序、评估、诊断）显式结构化，使通用编码智能体在执行时通过读取、调用和查询KI的三个互补层来完成可靠模拟。实验表明，在3000次试验的耦合水文基准测试中，配备KI的智能体成功率高达84%，而无KI时任何智能体都无法可靠完成，且失败模式恰好对应三类知识的缺失。该方法还能推广至14个地球科学领域的117个额外模型，证明操作专长是可提取的结构化知识而非临时修补。

### Q4: 论文做了哪些实验？

论文围绕KISS框架开展了两组核心实验。第一组是耦合水文模拟基准测试，使用手工构建的知识基础设施(KI)，在3个淮河流域(中国)部署10个来自5个平台的命令行编码智能体进行3000次独立试验，模拟VIC-Lohmann工作流(含14个里程碑)，以完成所有步骤且NSE≥0.2为成功标准。结果：Claude Sonnet 4.5和Opus 4.5达84%成功率，Kimi K2.5 Coding达80%，而无KI的消融实验中所有智能体均未实现可靠完成(成功率<40%)，且失败模式分为编造结果、物理盲视和错误循环三类。第二组是跨领域扩展实验，利用知识剖析工具包(KDT)自动化构建了117个额外过程模型的KI(共119个模型，覆盖14个地球科学领域)。其中25个经专家监督的包在75个模型-站点组合中60个(80%)达到领域特定阈值；92个全自动生成的包中59个通过观测数据验证，33个经合成输入验证可运行。结果表明KI能显著提升智能体模拟可靠性与可扩展性。

### Q5: 有什么可以进一步探索的点？

论文的局限在于KDT生成的KI仍依赖已知操作流程，对未知或极端场景（如气候突变）的泛化能力有限。未来可探索以下方向：1）将物理仿真与数据驱动方法结合，引入在线学习机制，使KI能自适应调整操作序列应对新情况；2）构建多智能体协作框架，让不同领域的KI通过联合推理处理耦合系统（如陆-气-海相互作用）；3）设计失败诊断的可解释性指标，量化模型偏离物理约束的程度；4）引入人类反馈进行选择性强化学习，在保持专业验证逻辑的同时提升KI对非标准输入的鲁棒性。此外，需关注KI对大规模并行计算任务的优化，以及不同类型物理模型之间操作迁移的元学习策略。

### Q6: 总结一下论文的主要内容

这篇论文提出知识基础设施(KI)——一种将过程模型的操作性专业知识外化为智能体可执行的脚手架，解决了非专家难以使用过程模型以及跨学科模型集成困难的问题。KI包含三个核心组件：验证过的建模算子、分阶段领域协议和诊断修复机制。在3千次耦合水文模型试验中，配备KI的智能体在高达84%的试验中产生了物理合理、可验证的端到端模拟，而无KI的智能体成功率低于40%。研究还开发了知识剖析工具包(KDT)，自主构建了横跨14个地球科学领域的117个额外过程模型的KI。所有119个KI的建模决策和故障修复方案趋同，表明操作性专业知识具有结构性和可提取性。该工作的意义在于降低了过程模型的使用门槛，使领域知识从隐性转为显性，为构建可复现的科学计算公共知识库奠定了基础。
