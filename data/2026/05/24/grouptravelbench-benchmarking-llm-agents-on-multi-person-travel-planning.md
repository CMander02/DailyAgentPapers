---
title: "GroupTravelBench: Benchmarking LLM Agents on Multi-Person Travel Planning"
authors:
  - "Xiang Cheng"
  - "Yulan Hu"
  - "Lulu Zheng"
  - "Zheng Pan"
  - "Xin Li"
  - "Yong Liu"
date: "2026-05-24"
arxiv_id: "2605.25200"
arxiv_url: "https://arxiv.org/abs/2605.25200"
pdf_url: "https://arxiv.org/pdf/2605.25200v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent Benchmark"
  - "Multi-Agent Planning"
  - "Tool-Use"
  - "Multi-User Coordination"
  - "Travel Planning Agent"
relevance_score: 9.0
---

# GroupTravelBench: Benchmarking LLM Agents on Multi-Person Travel Planning

## 原始摘要

Travel planning is a realistic task for evaluating the planning and tool-use abilities of LLM agents. However, existing benchmarks typically assume only a single user, thereby avoiding one of the most challenging aspects of real-world scenarios: an agent's ability to identify and resolve conflicts among multiple users. To address this gap, we introduce \textbf{GroupTravelBench}, the first benchmark for \textbf{multi-user, multi-turn} travel planning. Based on real user profiles, POI data, and ticket price data, we synthesize 650 tasks and divide them into three difficulty levels. Beyond standard abilities in single-user itinerary planning, such as multi-step reasoning and tool use, our benchmark further evaluates three key capabilities required for travel agents: \emph{(i) elicitation} -- proactively engaging in multi-turn dialogue to gather preferences from each user; \emph{(ii) coordination} -- resolving conflicts among users through compromise or subgrouping strategies; and \emph{(iii) planning} -- searching for travel plans that maximize overall group utility while maintaining fairness and feasibility. To simulate real-world conversational itinerary planning while enabling reliable tool use and offline evaluation, we build an interactive sandbox environment with cached real-world tool data. We evaluate a wide range of LLMs and find that even frontier models still show substantial weaknesses in preference coverage and group fairness. \textit{GroupTravelBench} provides a practical and reproducible benchmark for advancing research on LLM agents for real-world travel planning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有大型语言模型（LLM）智能体在旅行规划基准测试中的一个关键空白：无法有效评估多用户、多轮对话场景下的复杂协作能力。当前研究背景是，旅行规划作为评估LLM智能体规划与工具使用能力的现实任务已受到关注，但现有基准（如TravelPlanner）通常仅假设单一用户，忽略了现实世界中最具挑战性的方面——智能体需要识别并解决多个用户之间的冲突。另一方面，已有的群体推荐或群体旅行规划研究通常将任务形式化为一个基于预定义偏好（如固定数值偏好矩阵）的优化问题，关注点在偏好已知时如何优化行程，而非智能体如何通过交互来挖掘偏好、解决冲突并做出决策。为弥补这一不足，本文提出了**GroupTravelBench**，这是首个针对**多用户、多轮**旅行规划的基准。其核心问题在于构建一个能全面评估LLM智能体在群体旅行规划中三项关键能力的框架：**（i）引导能力**——通过主动的多轮对话收集每个用户的偏好；**（ii）协调能力**——通过妥协或分组策略解决用户间的冲突；**（iii）规划能力**——在确保公平性和可行性的前提下，搜索最大化群体整体效用的旅行计划。该基准通过基于真实用户画像、兴趣点（POI）数据和票价数据合成的650个任务，以及一个交互式沙盒环境，实现了对群体旅行规划智能体能力的可靠和可复现评估。

### Q2: 有哪些相关研究？

以下是论文《GroupTravelBench》中提到的相关研究，按类别组织如下：

1. **优化方法类**：早期研究将群体旅游计划问题建模为组合优化问题，如扩展TTDP（旅游行程设计问题）至多游客场景，使用元启发式（如禁忌搜索、进化算法）处理个体偏好和社会关系。后续工作关注群体公平性、动态子群形成（蚁群优化）、"加入-分离"策略等。本文与之区别在于，这些方法仅处理预定义的数值偏好向量，局限于单日POI排序，且不涉及自然语言交互或工具使用。

2. **评测基准类**：TravelPlanner是首个工具驱动的多日行程规划基准，但已被求解器方法解决。后续扩展包括：ChinaTravel（DSL约束）、TripScore（统一评分）、TripTailor/COMPASS（个性化与软偏好）、TP-RAG（检索增强）、WorldTravel（多模态环境）、DeepPlanning（长周期优化）等。本文指出，这些基准均仅评估单用户规划，缺乏多用户冲突消解和群体公平性考量。

3. **系统与方法类**：近期工作探索宽范围规划解耦（并行行为树）、约束门控RL的竞争共识、以及世界模型下的主动澄清。DeepTravel/TourPlanner等将RL直接应用于旅行规划，ToolRL/ReTool/工具Star则优化工具选择与协同推理。然而，这些方法仍限于单用户单目标设置，未涉及多用户偏好引导与群体公平优化。

综上，本文核心创新在于首次引入多用户、多轮对话的旅行规划基准，专门评测LLM Agent的偏好引导、冲突协调和群体公平性能力，填补了现有研究仅关注单用户规划的空白。

### Q3: 论文如何解决这个问题？

GroupTravelBench通过三个紧密耦合的组件构建了一个多用户多轮旅行规划基准。首先，任务合成流水线基于真实世界数据：从3,718个真实用户画像、约338K个POI数据及票价数据中采样，通过四个阶段（数据准备、任务骨架采样、偏好生成、后验证）合成650个任务，覆盖22种群体原型、143个目的地城市。偏好生成阶段采用独立、复制次要、复制中等三种策略创建真实群体多样性，并使用4级偏好强度（必须/拒绝/偏好/避免）确保可评估性。

其次，多用户交互框架采用同步群聊环境，代理需与N个LLM用户模拟器交互。用户模拟器不会主动透露全部偏好，仅在被问及时回应，迫使代理主动进行偏好 elicitation。框架维护三重偏好表：原始偏好表（隐藏真实偏好）、代理推断表（记录当前信念）、有效偏好表（应用已接受的妥协）。当代理发现冲突时，可要求用户妥协，妥协过程通过自然语言和机器可读更新实现确定性审计。支持子群策略，但会施加惩罚促使代理优先通过妥协协调。

关键技术方面，工具沙箱包含10个旅行相关工具（POI搜索、航班/火车查询等），通过内容寻址缓存300K+真实数据记录确保离线可复现性。评估协议从结果质量和过程质量两个维度衡量：结果质量包括偏好覆盖率、群体效用、群体公平性、计划有效性四个规则指标；过程质量由LLM裁判评估事实性、工具使用推理、交互质量、冲突协调、计划质量五个维度，并加入元评估步骤降低裁判噪声。该设计使妥协成为可审计的确定性事件，而非依赖主观LLM评估。

### Q4: 论文做了哪些实验？

论文在GroupTravelBench上进行了系统实验，评估了8种LLM（包括DeepSeek-V4-Pro、GPT-5.1等闭源模型，以及QWEN3-235B、QWEN3-30B等开源模型）。实验设置包含650个任务，分为Easy（200）、Medium（250）和Hard（200）三个难度等级，每个任务进行3次独立试验。评估维度包括群组效用、偏好完整性、群组公平性、计划有效性和LLM裁判分数。主要结果：DeepSeek-V4-Pro在所有维度上表现最佳，偏好完整性达64.5%，群组效用10.50，但计划有效性仅8.0%。所有模型的群组公平性均低于55%，计划有效性≤11%，揭示出模型在冲突协调和空间连贯性方面的严重不足。实验还分析了群组规模效应（N=2-6），发现随着人数增加，偏好完整性和公平性急剧下降，而群组效用增加，表明多方协调是核心瓶颈。妥协行为分析显示多数任务（67%）未触发任何妥协，工具调用分布近似正态（均值22.5次/任务）。计划有效性错误分析表明缺少城市内交通是主要结构缺陷。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在四个方面。地理和文化范围仅限中国国内旅行，结论的普适性存疑，未来可扩展至多国或跨境旅行场景，加入签证、汇率等约束。用户模拟器由GPT-4.1驱动，行为过于一致和合作，与真实人类差异较大，未来应引入真人用户实验或更动态的模拟器。偏好模式虽覆盖四类，但缺乏条件性偏好（如“天气好才选X”）和复杂社交动态，可扩展至包含优先级权重或概率性偏好的机制。评估上，LLM评判可能存在系统性偏差，规则指标无法衡量行程的美学或叙事连贯性，建议结合多维度人工评估或设计更细粒度的自动化指标。此外，可探索模型在偏好挖掘策略上的学习，例如通过主动提问减少用户隐性偏好遗漏，或引入强化学习优化公平性与群体效用的平衡。

### Q6: 总结一下论文的主要内容

GroupTravelBench是首个针对多用户多轮旅行规划的LLM智能体基准测试。真实旅行规划需处理单用户基准回避的核心挑战：智能体识别并解决多用户间冲突的能力。该基准基于真实用户画像、POI和票价数据合成了650个任务，分为三个难度等级。除单用户行程规划所需的多步推理和工具使用能力外，该基准还评估三种关键能力：①引导能力——主动通过多轮对话收集每位用户偏好；②协调能力——通过妥协或分组策略解决用户冲突；③规划能力——在保持公平性和可行性的同时搜索最大化群体总效用的方案。为模拟真实对话式规划并支持可靠离线评估，作者构建了带缓存真实工具数据的交互式沙盒环境。实验发现，即使最先进模型在偏好覆盖和群体公平性上仍存在明显缺陷：偏好覆盖率是主要区分因素（DeepSeek-V4-Pro达64.5%，其他模型≤31%），群体公平性是普遍弱点（最佳模型仅54.6%），规划有效性极低（≤11%），而妥协机制严重未被利用（67%任务零妥协）。这些结果证明群体旅行规划对LLM智能体提出了与单用户规划本质不同的挑战。
