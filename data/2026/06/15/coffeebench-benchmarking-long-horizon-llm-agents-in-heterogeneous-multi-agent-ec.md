---
title: "CoffeeBench: Benchmarking Long-Horizon LLM Agents in Heterogeneous Multi-Agent Economies"
authors:
  - "Issa Sugiura"
  - "Daichi Hattori"
  - "Kazuo Araragi"
  - "Keita Ogawa"
  - "Shota Onose"
  - "Taro Makino"
  - "Teppei Usuki"
  - "Takashi Ishida"
date: "2026-06-15"
arxiv_id: "2606.16613"
arxiv_url: "https://arxiv.org/abs/2606.16613"
pdf_url: "https://arxiv.org/pdf/2606.16613v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent"
  - "Benchmark"
  - "Long-Horizon"
  - "Economics"
  - "LLM Agent Evaluation"
relevance_score: 8.5
---

# CoffeeBench: Benchmarking Long-Horizon LLM Agents in Heterogeneous Multi-Agent Economies

## 原始摘要

As LLM agents become capable of increasingly long-horizon tasks, evaluating their performance in economic systems is becoming increasingly important. Unlike existing benchmarks that primarily evaluate a single agent interacting with a passive environment, economic systems are inherently multi-agent, requiring autonomous agents to communicate, negotiate, and transact while pursuing their own objectives over extended periods. We introduce CoffeeBench, a benchmark for evaluating LLM agents in a long-horizon multi-agent economy composed of heterogeneous firms. In CoffeeBench, two farmers, two roasters, and two retailers autonomously operate their businesses over a 90-day simulation, each seeking to maximize cumulative net income through communication and transactions while managing cash, inventory, and pricing. The evaluated model controls one coffee roaster, while the remaining firms are controlled by fixed reference agents. Across several recent open-weight and proprietary LLMs, all models outperform a passive baseline that takes no actions, with most achieving positive net income. Analysis of agent behavior reveals substantial differences in long-horizon economic interaction: higher-performing models communicate more actively with other firms, whereas Claude~Haiku~4.5 exhibits an idle-drift failure mode, repeatedly choosing inaction despite producing coherent assessments and plans. We release our code and agent trajectories to support future research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文《CoffeeBench: Benchmarking Long-Horizon LLM Agents in Heterogeneous Multi-Agent Economies》旨在解决现有基准测试在评估LLM智能体长期任务能力方面的不足。研究背景是，随着LLM智能体在编程、网页使用等需要持续决策和规划的任务中表现日益强大，其应用已扩展到金融、医疗、制造等领域。然而，现实世界经济系统本质上是多智能体环境，包含不同角色的企业（如农民、烘焙商、零售商），它们需要长期自主地进行沟通、谈判和交易以追求自身目标。现有基准测试如Vending-Bench等，主要评估单个智能体与被动环境的交互，或仅涉及同类智能体，忽略了真实经济中异构企业间的复杂动态交互。因此，本文提出的核心问题是：如何设计一个能同时体现长期规划、异构多智能体交互和经济目标驱动的评估框架。CoffeeBench通过模拟一个由三家异构企业（农民、烘焙商、零售商）组成的90天经济系统来填补这一空白，要求被测试的LLM智能体作为烘焙商，在管理库存、定价和现金流的同时，与其他固定参照智能体进行通讯和交易，以最大化累计净收入，从而全面评估其长期决策和交互能力。

### Q2: 有哪些相关研究？

根据论文内容，相关研究可分为以下几类：

1. **长时域任务评测基准**：早期基准如MMLU、Humanity's Last Exam聚焦单轮问答。随着ReAct等框架发展，出现了软件工程、网页导航、桌面操作等领域的长期任务基准。近期工作进一步扩展到环境异步演化的场景。CoffeeBench与之的区别在于关注多智能体经济系统，而非单一智能体与被动环境的交互。

2. **商业管理基准**：Vending-Bench评估单个LLM智能体运营自动售货机的能力，Vending-Bench Arena扩展为多智能体竞争。但这些基准仅涉及单一经济角色（所有智能体经营同质业务）。CoffeeBench首次引入异构经济体（农民、烘焙师、零售商三类角色），每个智能体通过沟通和交易追求自身利润最大化，更接近真实经济系统。

3. **LLM智能体不良行为研究**：已有工作发现了奖励黑客、模型作弊等行为，以及经济激励下的过度逐利或危险决策。Vending-Bench也报告了竞争压力下的攻击性行为。CoffeeBench通过可控的多智能体经济环境，为系统研究智能体间战略协调可能产生的负面行为提供了新平台。

### Q3: 论文如何解决这个问题？

CoffeeBench通过构建一个异构多智能体经济仿真环境来解决长周期LLM智能体的评估问题。整体框架模拟了由两个农场、两个烘焙商、两个零售商组成的三层咖啡供应链，包含商品和精品两条并行链条，形成层内竞争与层间依赖。

核心架构采用异步事件驱动的模拟机制，每个智能体在09:00-19:00的营业窗口内操作，每次工具调用推进30分钟本地时间，限制了每日主动行为数。智能体可调用wait_for_next_day()进入空闲状态，但能被外部事件（消息、交易、发货）在当天内重新激活，实现异步交互。日终时系统统一更新消费者销售、运营成本、库存损耗等。

主要模块包括：共享工具（发布挂单/出价/接受交易/付款/发送消息）支持任意点对点交易；角色专用工具（农场生产、烘焙商烘焙、零售商定价与查看销售）；竞争性需求模型（基于定价和品牌忠诚度）；以及约束机制（固定运营成本、库存损耗、存储容量限制、生产交付延迟、信用交易与违约风险）。

创新点在于：1) 创建了包含六个异构智能体的持续90天模拟经济系统，远超单智能体基准；2) 异步事件驱动设计允许智能体被动响应市场活动而非严格同步；3) 通过信用交易、库存风险和延迟交付等机制强制长期策略行为；4) 评估发现高性能模型更主动沟通，而Claude Haiku 4.5表现出"空闲漂移"失效模式。

### Q4: 论文做了哪些实验？

论文在CoffeeBench基准上评估了多种LLM代理在90天异构多代理经济模拟中的表现。实验设置中，被评估模型控制一个咖啡烘焙商（roaster_A），其余五个企业由参考代理（默认Claude Sonnet 4.6）控制，使用ReAct框架运行。数据集为模拟环境，所有企业初始现金$15,000，有特异性库存上限和运营成本，包含两种产品及第40-53天的需求激增事件。对比方法包括五个闭源模型（Claude Opus 4.7、Sonnet 4.6、Haiku 4.5、GPT-5.5、Gemini 3.1 Pro）和两个开源模型（Kimi K2.6、GLM-5.1），以及两个基线：PassiveRoaster（始终等待）和HeuristicRoaster（固定策略）。每个设置运行三轮取平均。主要结果：GPT-5.5平均净收入最高，Claude Opus 4.7次之；GLM-5.1收入最高但净收入不高；Claude Haiku 4.5净收入为负（-$630），因频繁闲置（平均40天不行动）。所有模型均优于被动基线。分析表明，高性能模型（如GPT-5.5）更积极通信和执行交易，而闲置漂移模式（Claude Haiku 4.5）导致失败。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向主要体现在三个层面。首先，当前模拟环境与现实市场存在显著差距，如供应链深度不足、生产过程过度简化、缺乏融资和监管等宏观因素。未来可扩展环境至更深层供应链，引入生产时间延迟和不确定性，或构建虚实结合的经济系统。其次，统计可靠性受限于高API成本导致的少量运行次数，可增加运行次数或降低环境随机性（如使销售模拟更确定、降低温度参数），但需平衡真实感。最后，当前LLM代理在战略性行为上存在不足，如缺乏长期协调和复杂操纵能力。可探索改进的强化学习训练方法，或设计分层规划框架：上层负责长期战略目标（如市场份额、价格联盟），下层执行具体交易操作，以增强代理的远期规划能力。此外，引入市场竞争压力或信息不对称等机制，可能激发更复杂的经济行为。

### Q6: 总结一下论文的主要内容

CoffeeBench是一个评估AI代理在多智能体经济中长期任务执行能力的基准。它构建了一个由两个农民、两个烘焙商和两个零售商组成的异构多智能体经济系统，模拟90天的商业运营周期。每个代理商需通过通信和交易来最大化累计净收入，同时管理现金、库存和定价。在实验中，被评估的模型控制一个咖啡烘焙商，其余智能体由固定参考代理控制。结果显示，所有模型均超过了不采取任何行动的被动基线，大多数实现了正净收入。其中，GPT-5.5和Claude Opus 4.7等高性能模型与其他企业沟通和交易更为积极，而Claude Haiku 4.5则表现出“空闲漂移”失败模式，尽管能生成连贯的评估和计划，但反复选择不行动，导致长期运营停滞和低收入。该基准的提出推动了能够可靠进行长期多智能体经济决策的LLM代理的发展。
