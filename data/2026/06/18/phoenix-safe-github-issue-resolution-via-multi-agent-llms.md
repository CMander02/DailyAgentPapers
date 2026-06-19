---
title: "Phoenix: Safe GitHub Issue Resolution via Multi-Agent LLMs"
authors:
  - "Kipngeno Koech"
  - "Muhammad Adam"
  - "Baimam Boukar Jean Jacques"
  - "Joao Barros"
date: "2026-06-18"
arxiv_id: "2606.20243"
arxiv_url: "https://arxiv.org/abs/2606.20243"
pdf_url: "https://arxiv.org/pdf/2606.20243v1"
categories:
  - "cs.SE"
  - "cs.MA"
tags:
  - "Multi-Agent Systems"
  - "Code Agent"
  - "Software Engineering Agent"
  - "Agent Safety"
  - "SWE-bench"
relevance_score: 7.5
---

# Phoenix: Safe GitHub Issue Resolution via Multi-Agent LLMs

## 原始摘要

We present Phoenix, a multi-agent LLM system that resolves GitHub issues from triage through pull-request creation, combining seven layered safety controls with a baseline-aware test evaluation strategy. Phoenix decomposes the work across six specialized agents. Planner, reproducer, coder, tester, failure analyst and Pull Request (PR) agent, all coordinated by a label-based GitHub webhook state machine. Every change is checked against a baseline test run before a pull request is opened. On a 24-instance slice of SWE-bench Lite. run on the production webhook path, Phoenix oracle-resolves 75% of instances with no pass-to-pass regressions on successful runs; this curated slice is not directly comparable to full-split leaderboard results, and we discuss the limits of the comparison. A complementary pilot on 42 real issues across 14 repositories yields 100% correctness preservation (CP; mean 122s on the hard tier). Manual inspection shows that about half of the resulting pull requests are well-targeted fixes. The other half place code at incorrect paths, a planner localization limitation we are addressing with retrieval. We also report the deployment failure modes (WAF filtering, token expiry, permission boundaries, flaky CI) that motivated each safety mechanism.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决的是在自动化GitHub Issue解决过程中，如何在追求高解决率的同时保障代码库安全性的核心问题。研究背景是开源软件仓库中积累了海量未解决的Issues（包括bug、回归问题和功能缺口），解决这些Issues需要大量人工工程投入。现有方法如Devin、SWE-Agent、AutoCodeRover虽然通过LLM代理实现了较高解决率（如SWE-bench上的30%），但它们存在的不足是：单纯追求解决率会牺牲安全性——可能修复了一个问题却引入了新的回归（如解决30%问题却导致另20%出现回归），这在生产环境中带来不确定的净价值。因此，本文提出Phoenix系统，其核心目标是实现**以正确性为先**的自动化Issue解决。具体来说，需要通过以下方式解决：将每个代码变更置于自动化测试的严格控制之下（依赖基线对比来区分预先存在的失败与Phoenix引入的回归）、确保输出都是可供人工审查的可审计PR（避免未经核实的变更直接合并）、部署七层安全控制机制（如API网关内容过滤、令牌过期处理、CI权限边界防护、脆弱的测试套件处理等），从而在生产环境中既能有效解决Issue，又能维护代码库的稳定性和可靠性。

### Q2: 有哪些相关研究？

相关研究可分为三类：**基准与系统类**、**自动程序修复类**和**推理与安全类**。

1. **基准与系统类**：以 **SWE-bench** 为代表，它确立了GitHub问题解决的标准评测基准，本文对比指出其系统在离线状态下运行。**SWE-Agent** 提出了结构化的智能体-计算机接口（ACI），**AutoCodeRover** 引入了基于AST的故障定位。本文Phoenix与它们的关键区别在于，后者面向生产环境部署（真实webhook、分支、PR），优先保证正确性而非原始解决率。

2. **自动程序修复（APR）类**：传统APR技术（基于遗传、语义或学习的方法）针对观察到的失败（如失败测试）进行修复。本文Phoenix则基于问题描述进行目标变更，同时保留所有通过的测试，这是一种互补的评测标准。同样，重构工具依赖预定义模板，而本文能处理自由格式的问题描述。

3. **推理与安全类**：**Chain-of-thought**、**ReAct** 和 **Toolformer** 证明了显式推理轨迹和工具调用的优势。本文通过多智能体分解实例化了这些思想：每个智能体在狭窄固定范围内推理，流水线提供多步执行支撑。在安全方面，相关研究记录了自主修改代码的风险，Phoenix通过结构性措施（永不合并到主分支、PR前强制测试验证）从结构上应对这些风险。

### Q3: 论文如何解决这个问题？

Phoenix通过一个多智能体LLM系统解决GitHub问题，采用六阶段闭环流水线架构。整体框架由Orchestrator协调，通过GitHub标签状态机（包含ai:ready、ai:running、ai:revise、ai:failed、ai:review五个状态）实现原子化状态转换，无需本地数据库。

主要模块包括六个专业化智能体：Planner负责接收问题和仓库上下文，输出结构化JSON计划（含摘要、步骤、风险等级和文件操作）；Reproducer尝试在基础分支上生成验证bug的失败测试（非阻塞设计）；Coder根据计划和故障反馈生成完整文件内容，强制无占位符输出并自验证测试用例；Tester采用基线感知策略，通过stash当前变更→运行基础分支测试集→恢复变更→再运行测试集的方式，比较B和P集合是否产生新失败（P\B=∅即通过）；Failure Analyst分析失败原因并提供根因反馈给Coder迭代；PR Agent自动创建包含关闭引用标签的拉取请求。

关键技术包括三重安全保障：路径遍历防御（校验写入路径不超出仓库根目录）、工作流文件防护（阻止.github/workflows/写入）、内容净化（截断问题正文至1500字符、替换代码块和回溯行）。创新点在于七层安全机制（含令牌自动刷新、并发锁、重试循环限制、标签互斥性）和基线对比测试策略，解决了WAF过滤、令牌过期、CI不稳定等实际部署故障。系统在生产路径下（SWE-bench Lite子集）实现75%的Oracle解决率，且无回归。

### Q4: 论文做了哪些实验？

论文主要在两个场景下评估Phoenix系统。首先是**SWE-bench Lite基准测试**，选取了Astropy、Django、Flask、Matplotlib、pytest、Requests、scikit-learn和SymPy这8个Python仓库，每个仓库取3个实例，共24个实例。实验设置基于生产环境的webhook路径，使用ai:ready标签触发完整部署管线。主要指标为oracle解析率（所有FAIL_TO_PASS测试通过且无PASS_TO_PASS回归）。结果显示，Phoenix在18/24（75%）的实例上实现了oracle解析，且所有成功运行均无回归。按仓库看，Astropy、Django、Requests、SymPy达到100%解析，Flask和pytest为67%，Matplotlib和scikit-learn为33%。成功运行的平均耗时170秒。

第二个实验是在**14个仓库的42个真实issue**上进行的定性试点研究，按代码库规模分为Easy（<5万行）、Medium（5-50万行）和Hard（最高140万行）三个难度等级。主要评估指标是正确性保持（CP），即测试套件在修改后仍能通过（排除基线失败）。结果显示，Phoenix在全部42个issue上实现了100%的CP，Hard级仓库平均解决时间为122秒。人工检查发现约一半PR是精确修复，另一半则存在代码路径错误问题。

### Q5: 有什么可以进一步探索的点？

根据论文的局限性和未来工作，可以进一步探索以下方向：

1. **增强语义检索与上下文管理**：当前基于关键词的文件排序器导致约一半的PR代码路径定位错误，未来可替换为基于存储库AST的语义检索，并结合检索增强生成（RAG）提升定位准确率。同时需测试在百万行级代码仓上的扩展性，评估多智能体上下文管理能力。

2. **完善评估体系**：当前仅依赖正确性保持（CP）指标，需引入领域专家审查PR的功能充分性评估，量化CP与真实解决率差距；同时应在SWE-bench Lite或Verified全量分割上运行，与现有榜单公平对比，并加入强基线消融实验以验证多智能体设计贡献。

3. **扩展安全与工程实践**：增设安全分析师智能体在PR创建前调用静态分析工具；针对Java、C++等语言实现容器化构建环境避免工具链依赖；引入跨运行记忆模块积累编码规范。此外需解决WAF过滤、令牌过期、权限边界等实际部署故障模式，完善生产级安全机制。

### Q6: 总结一下论文的主要内容

Phoenix是一个用于安全解决GitHub问题的多智能体LLM系统，从分类到创建拉取请求全覆盖。它由六个专业智能体组成：规划器、复现器、编码器、测试器、故障分析器和PR智能体，通过基于标签的GitHub Webhook状态机协调。系统创新在于引入了七个分层安全机制和基线感知测试策略。在SWE-bench Lite的24实例子集上，Phoenix实现了75%的Oracle解决率且无回归问题；在14个仓库的42个真实问题测试中，达到100%正确性保持，平均解决时间122秒。手动检查显示约一半PR修复精确，其余因规划器定位限制将代码放置于错误位置。核心贡献包括：六智能体管道设计、基线感知测试、安全性作为一等工程要求的理念，以及语义检索改进方向的提出。
