---
title: "RetailBench: Benchmarking long horizon reasoning and coherent decision making of LLM agents in realistic retail environments"
authors:
  - "Linghua Zhang"
  - "Jun Wang"
  - "Jingtong Wu"
  - "Zhisong Zhang"
date: "2026-06-14"
arxiv_id: "2606.15862"
arxiv_url: "https://arxiv.org/abs/2606.15862"
pdf_url: "https://arxiv.org/pdf/2606.15862v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Agent Benchmark"
  - "Long-horizon Planning"
  - "Retail Agent"
  - "Tool Use"
  - "Decision Making"
  - "Simulation"
relevance_score: 9.5
---

# RetailBench: Benchmarking long horizon reasoning and coherent decision making of LLM agents in realistic retail environments

## 原始摘要

Large language model (LLM) agents have made rapid progress on short-horizon, well-scoped tasks, yet their ability to sustain coherent decisions in dynamic long-horizon environments remains uncertain. We introduce RetailBench, a data-grounded simulation benchmark for evaluating tool-using LLM agents in single-store supermarket operation. RetailBench models retail management as a partially observable decision process and is designed to support thousand-day-scale simulations. In this environment, agents must manage pricing, replenishment, supplier selection, shelf assortment, inventory aging, customer feedback, external events, and cash-flow constraints. We evaluate seven contemporary LLMs under representative agent frameworks over a 180-day evaluation horizon and compare them with a privileged oracle policy. Results show substantial variation across models: only a small subset survives the full evaluation horizon, and even the strongest LLM runs remain substantially behind the oracle policy in final net worth and sales outcomes. Behavioral analysis attributes these gaps to incomplete evidence acquisition, surface-level decision making, and the lack of a consistent long-horizon policy. RetailBench provides a controlled testbed for studying reliable autonomy in economically grounded long-horizon decision-making.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型（LLM）智能体在长期、动态、部分可观测环境中难以维持连贯决策和稳定性能的问题。研究背景是，虽然LLM智能体在短期、结构化的任务（如代码编辑、数学推理）上已取得显著进步，但现有评估基准大多侧重于孤立的单次任务完成，忽视了真实世界中决策的长期耦合效应与延迟反馈。现有方法如UltraHorizon等虽开始关注长视野，但缺乏一个覆盖零售运营中定价、补货、库存老化、现金流约束等多重动态关联因素的真实数据驱动基准。核心问题是：LLM智能体能否在长达千天尺度的模拟中，通过持续的工具使用，在部分可观测的零售管理环境下，主动获取信息、做出连贯的商业决策并适应环境变化，最终实现长期利润目标。论文通过引入RetailBench基准，系统评估了当前主流LLM在该场景下的表现，发现即使最强模型也与最优策略存在显著差距，暴露出证据获取不完整、决策表面化、缺乏长期政策一致性三个关键瓶颈。

### Q2: 有哪些相关研究？

相关研究可分为以下类别：  
**方法类**：本文与近期聚焦于超长周期交互、办公工作流、虚拟世界规划、终身经验复用、工作场所任务执行及长期商业运营的智能体基准研究相关。这些工作强调持久性、记忆、探索和工作流级决策，但通常不建模基于数据的多日零售动态。RetailBench通过闭环产品级运营填补了这一空白，并支持对证据获取、证据到行动转化及长期策略一致性的诊断分析。  
**应用类**：零售、电商和供应链决策基准研究涵盖了零售模拟与促销优化、需求恢复与交易建模、网络购物智能体及库存控制等子问题。但这些基准通常孤立处理促销、需求建模、购物或库存决策，而RetailBench评估使用工具的LLM智能体在耦合的零售环境中的表现，定价、补货、供应商选择、货架组合、反馈、事件和现金流在此环境中随时间动态交互。  
**评测类**：本文与现有基准的核心区别在于，RetailBench将零售管理建模为部分可观察决策过程，支持千天级模拟，并通过受控环境与特权oracle策略对比，系统评估LLM智能体在长期经济导向决策中的可靠性，弥补了现有基准在数据真实性、交互耦合度和长期策略一致性评估方面的不足。

### Q3: 论文如何解决这个问题？

论文通过构建一个数据驱动的零售模拟基准（RetailBench）来解决问题。核心方法是将零售管理建模为部分可观测马尔可夫决策过程（POMDP），并设计了一个支持千天级模拟的闭环环境。架构上，RetailBench包含一个部分可观测的模拟器，状态分解为产品属性、库存、货架、供应商、需求、外部事件和财务等因子。智能体通过三类工具与模拟器交互：只读工具（查询资金、库存、销售等）、辅助工具（内存写入、代码执行）和状态改变工具（价格更新、补货、货架调整、结束日）。其中，只读工具暴露观测而不揭示潜在状态，只有状态改变工具能修改模拟器状态。关键技术包括：基于真实零售数据（Dominick's数据集）定义产品宇宙、价格和需求模式；利用Amazon评论和金融新闻注入动态反馈；将日级过渡建模为包含交付、销售、退货、过期、租金、现金流更新的综合过程。创新点在于：模拟器不仅支持定价、补货、供应商选择、货架陈列等多维度决策，还整合了客户反馈、外部事件和现金流约束，迫使智能体进行长期协调推理而非孤立优化子问题。评估协议使用ReAct、Reflection和Plan-and-Act三种框架，用最终净值、生存天数、销售额等五类指标衡量智能体表现，并与特权oracle策略对比。

### Q4: 论文做了哪些实验？

论文构建了RetailBench基准，在模拟单店超市运营的环境中评估LLM智能体。实验设置包含千天级仿真，智能体需管理定价、补货、供应商选择、货架分类、库存老化、客户反馈、外部事件及现金流约束，在180天评估周期内运行。采用“生存优先”选择协议：对每个LLM，从可用智能体框架中选取最长生存周期的轨迹，以最终净资产和总销售额为辅助指标。比较了DeepSeek-V4-Pro、GPT-5.5、Kimi-K2.6等7个当代LLM，并与具备完全结构信息的特权oracle策略对照。

主要结果显示：智能体生存期从58天到180天不等（平均约107天），仅DeepSeek-V4-Pro和GPT-5.5完成全部180天。GPT-5.5的token消耗仅为DeepSeek-V4-Pro的三分之一。oracle策略最终净资产达131,510.42、总销售额267,998；最强LLM（GPT-5.5）净资产仅24,350.98，DeepSeek-V4-Pro销售额164,417，分别落后oracle 107,159.44和103,581。结论表明当前LLM智能体在长周期运营可持续性上存在显著差距，主要归因于证据获取不完整、表面化决策及缺乏一致的长程策略。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向包括：1）当前仅关注单店超市场景，未来可扩展至多店协同、竞争市场、供应商战略互动等更复杂的零售生态，并引入多智能体协作与竞争机制；2）部分数据（如用户评论、新闻事件）基于合成或规则生成，可结合真实零售数据流构建更高保真度的模拟环境，并引入时序因果推断来量化各决策因子的独立作用；3）现有评估依赖固定环境下的提示型智能体，未来可探索基于强化学习或在线学习的自适应策略，以提升长周期决策的连贯性；4）失败分析尚停留在诊断层面，需发展反事实诊断框架（如干预因果图）和约束感知的动作控制机制，系统性地隔离导致策略崩溃的关键瓶颈；5）可引入预算约束下的多目标优化（如库存周转率与现金流平衡）来测试智能体在资源限制下的鲁棒性。这些方向将推动LLM智能体在真实动态经济环境中从"短期任务执行"向"长期自主决策"的实质性跃迁。

### Q6: 总结一下论文的主要内容

RetailBench 是一个数据驱动的仿真基准，用于评估LLM智能体在长期、动态零售环境中的连贯决策能力。它将零售管理建模为部分可观察的决策过程，要求智能体在千天规模的模拟中管理定价、补货、供应商选择、货架分类、库存老化、客户反馈、外部事件和现金流约束。对七种当代LLM在180天评估期内的测试表明，只有少数模型能存活整个周期，且最强LLM在最终净资产和销售额上仍远低于特权oracle策略。行为分析揭示了三个关键瓶颈：证据获取不完整、决策流于表面以及缺乏一致的长期策略。该基准为研究经济导向的长期自主决策提供了受控实验平台，强调了未来智能体需在证据选择、推理、状态策略维护和反馈适应方面取得突破。
