---
title: "FlyRoute: Self-Evolving Agent Profiling via Data Flywheel for Adaptive Task Routing"
authors:
  - "Rongjun Li"
  - "Ziyu Zhou"
  - "Yihang Wu"
date: "2026-05-21"
arxiv_id: "2605.22057"
arxiv_url: "https://arxiv.org/abs/2605.22057"
pdf_url: "https://arxiv.org/pdf/2605.22057v1"
categories:
  - "cs.CL"
tags:
  - "Agent路由"
  - "自我进化"
  - "数据飞轮"
  - "LLM路由器"
  - "Agent画像"
  - "工具使用"
  - "自适应路由"
relevance_score: 9.5
---

# FlyRoute: Self-Evolving Agent Profiling via Data Flywheel for Adaptive Task Routing

## 原始摘要

Enterprise routers assign queries to expert agents, yet deployed profiles stay static while agents evolve (prompts, tools, models), and developers rarely keep descriptions or exemplars current. We present FlyRoute, a self-evolving profiling framework that grows capability evidence from real traffic: dispatch candidates, quality-gate successful pairs into each agent's success store, periodically distill evidence into learned capability descriptions, and inject those descriptions together with BM25-retrieved successes into an LLM router. To make this flywheel data-efficient, FlyRoute introduces a targeted exploration policy that combines profile uncertainty, BM25 relevance, and lexical novelty, prioritizing under-profiled agents only for plausible queries and avoiding redundant evidence collection. In experiments on our proprietary enterprise developer-support dataset of real routed queries, FlyRoute improves a same-backbone zero-shot LLM router from 72.57% to 78.04% with only five seed queries per agent, showing that profile retrieval already strengthens cold-start routing. After streaming 7,211 labeled training queries through the flywheel, accuracy rises to 89.83% (+17.26pp over zero-shot; +11.79pp over cold start), with consistent gains across four expert domains under standard routing accuracy on single-gold test queries.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体系统（MAS）中路由器的核心问题：**路由依据的智能体能力描述与实际能力严重脱节**。现有方法（如基于LLM的路由器、嵌入相似度等）均假设智能体在注册时就能提供准确且长期稳定的能力描述，但这一假设在现实企业部署中失效。原因是：第一，开发者通常无法提供精确的初始描述，且智能体的行为（由提示词、工具、模型决定）在持续迭代，描述会快速过时；第二，智能体部署后能力会变化（如更新提示词、集成新工具），但路由仍基于静态的过时信息决策。其根本症结在于智能体能力配置文件的静态性。

本文提出 **FlyRoute**，旨在解决这一静态配置问题。其核心思想是构建一个**自我进化的数据飞轮**：通过将实际用户查询分发给智能体，并对高质量的成功响应进行质量门控，收集这些成功样本作为能力证据；然后周期性蒸馏这些证据，生成动态更新的能力描述。同时，设计一个**不确定性驱动的探索策略**，结合配置文件不确定性、BM25相关性和新颖性，优先探索轮廓模糊的智能体，避免浪费资源。最终，路由时结合动态描述与检索到的成功样本进行决策，实现了配置文件与路由性能的持续自适应提升。

### Q2: 有哪些相关研究？

相关研究主要分为三类。**性能基路由**方面，如ICL-Router通过离线探针生成查询-模型历史摘要，用于免重训练模型选择。FlyRoute的不同之处在于其针对不断演化的企业专家代理，从实时流量中持续更新能力档案，而非依赖离线探针。**任务基路由**方面，现有工作如TCAR等使用静态注册档案进行监督分类或嵌入相似度匹配，而FlyRoute解决了一个未被充分探索的问题：代理部署后能力边界变化，需从路由流量中动态修正档案，因此本文专注于与同基线方法对比以隔离演化档案的价值。**代理档案与能力发现**方面，多假设开发者提供准确描述，但在代理频繁更新时脆弱。FlyRoute引入预算感知的探索策略，类似于多臂老虎机，但目标不同：它选择代理进行探针测试，将接受证据融入持续演化的能力档案，而非主动学习中选择样本标记固定分类器。整体而言，FlyRoute的贡献在于提供了一个数据飞轮框架，通过针对性的探索策略高效从真实流量中积累证据并定期蒸馏为能力描述，从而提升冷启动性能及持续路由准确率。

### Q3: 论文如何解决这个问题？

FlyRoute通过构建一个自演进的agent profiling数据飞轮来解决静态配置与动态能力变化之间的矛盾。核心方法采用闭环架构：当新agent注册时仅需少量种子描述和5个示例，系统初始化空profile。对于每个查询，路由模块先利用当前LLM路由器的profile描述和BM25检索的成功示例选出候选agent（利用），再通过不确定性驱动的探索策略补充未选agent（探索），合并后分派给最多数位agent。

关键技术包括三个创新组件：1）**profile结构**：每个agent维护种子描述、自动蒸馏的学习描述和成功示例存储，后者通过质量门控（LLM评判）持续收集高质量响应对。2）**不确定性驱动探索**：结合profile不确定性（基于成功案例数量衰减）、BM25相关性（确保探索仅针对合理查询）、以及新颖性加权（避免冗余采集），计算公式为 \(V_{explore}^{+}=U(a_i)\cdot R(q,a_i)\\bigl(1+\beta(1-R(q,a_i))\\bigr)\)，高效定位低置信度agent。3）**能力蒸馏**：每积累M个新成功示例，用LLM将经验证据压缩为自然语言描述，自动发现开发者未注明的能力变化，在路由时替换种子描述作为全局信号。

整体框架形成自增强循环：更好的profile→更精准路由→高质量反馈→更优profile。实验表明，冷启动阶段（每agent 5种子）精度从72.57%提升至78.04%，飞轮消化7,211条训练查询后达到89.83%，较零样本提升17.26个百分点。

### Q4: 论文做了哪些实验？

实验在自建企业数据集上进行，覆盖四个业务领域（Cloud Services、AI Accelerator、Server Hardware、Mobile OS），训练集7211条、测试集1298条，每个领域仅配置一个专家代理且初始只有5条种子查询。对比方法包括：(1) 零样本LLM Router，仅用静态种子描述直接路由；(2) FlyRoute冷启动变体，使用BM25检索+LLM少样本路由但无训练数据流；(3) FlyRoute完整飞轮系统。主实验结果显示，FlyRoute冷启动达到78.04%准确率（零样本72.57%），完整飞轮系统处理全部训练流后提升至89.83%，相较零样本提升17.26个百分点，所有领域均有增益。探索策略对比实验中（处理500条查询后），FlyRoute（84.05%）优于随机广播（81.97%）、ε-贪心（81.90%）和无探索（81.05%）。消融实验表明，移除质量门控（Judge）降低1.39个百分点至88.44%，移除探索策略降低1.31个百分点至88.52%，移除新颖性因子降低0.77个百分点至89.06%，移除周期蒸馏降低0.54个百分点至89.29%。

### Q5: 有什么可以进一步探索的点？

论文存在以下可进一步探索的方向：首先，当前评估基于单一企业私有数据，未来需验证FlyRoute在跨行业、多语言、开放域或更大规模agent集群上的泛化能力。其次，质量门控依赖LLM作为裁判存在噪声，可探索引入主动学习或人类反馈闭环以提升证据筛选的鲁棒性。第三，当agent发生模型更新或工具变化时，框架仅依赖飞轮被动适应，建议设计明确的漂移检测机制（如性能监控）触发针对性重探索。此外，当前未考虑部署成本，需量化BM25索引更新、额外agent调用和蒸馏频率对延迟与吞吐的影响。最后，针对多gold测试场景（如多agent协作任务），可改进路由策略为top-k推荐而非单一路由。

### Q6: 总结一下论文的主要内容

FlyRoute针对企业多智能体系统中路由器的核心挑战——智能体能力描述静态化与真实能力动态演化之间的矛盾。问题定义是：如何在不依赖开发者手动更新的情况下，让路由系统自动发现并持续更新每个智能体的能力边界。方法上，FlyRoute构建了一个数据飞轮：首先利用用户查询作为探针，将路由候选与高质量成功响应配对存入每个智能体的“成功案例库”；然后周期性从这些案例中提炼出能力描述，并联合BM25检索到的成功案例输入给LLM路由。为实现数据高效，提出一种结合概要不确定性、BM25相关性和词汇新颖性的定向探索策略，优先为欠轮廓化的智能体分配合理的查询。实验基于企业开发者支持数据集的7,211条标注查询，结果显示：冷启动阶段（每智能体5个种子）准确率从零样本LLM路由的72.57%提升至78.04%；数据飞轮全量运行后准确率达89.83%（+17.26pp）。核心贡献在于首次形式化了自演化智能体轮廓问题，并验证了通过部署交互持续更新能力的可行性与显著效果。
