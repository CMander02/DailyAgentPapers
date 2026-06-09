---
title: "Benchmarking Open-Ended Multi-Agent Coordination in Language Agents"
authors:
  - "Kale-ab Abebe Tessera"
  - "Andras Szecsenyi"
  - "Cameron Barker"
  - "Alexander Rutherford"
  - "Davide Paglieri"
  - "Aidan Scannell"
  - "Henry Gouk"
  - "Elliot J. Crowley"
  - "Tim Rocktäschel"
  - "Amos Storkey"
date: "2026-06-06"
arxiv_id: "2606.08340"
arxiv_url: "https://arxiv.org/abs/2606.08340"
pdf_url: "https://arxiv.org/pdf/2606.08340v1"
github_url: "https://github.com/alem-world/alem-env"
categories:
  - "cs.AI"
  - "cs.LG"
  - "cs.MA"
tags:
  - "多智能体协调"
  - "基准评测"
  - "开放世界"
  - "Craftax"
  - "JAX"
  - "LLM-Agent"
  - "通信"
  - "角色分配"
  - "零样本评估"
  - "MARL"
relevance_score: 9.5
---

# Benchmarking Open-Ended Multi-Agent Coordination in Language Agents

## 原始摘要

As language models are increasingly deployed as autonomous agents, they must coordinate with others over long horizons in open-ended interactive tasks. Yet existing evaluations rarely test these demands together, instead emphasising single-agent tasks, short interactions, or highly structured multi-agent settings. We introduce $alem$, a JAX-based benchmark for open-ended multi-agent coordination built on Craftax-like dynamics. Alem embeds procedurally generated coordination tasks, soft specialisation, communication, and controllable coordination difficulty into a long-horizon survival world with exploration, crafting, trading, and combat. We evaluate $13$ modern LLMs zero-shot within homogeneous teams, with trained MARL agents as reference points. Current LLM agents remain far from solving alem, averaging only ~6% normalised return, but their failures are not uniform. On the hardest coordination setting, zero-shot Gemini-3.1-Pro-High approaches MARL agents trained for one billion steps, while GPT-5.4-High achieves strong base-task reward but much lower coordination reward. This contrast shows that individual task competence does not imply coordination competence. Ablations show that communication is the largest contributor to coordination, while memory and reasoning help when used to maintain multi-step plans. Overall, our results identify coordination as a distinct bottleneck for frontier LLM agents, separate from single-agent capabilities. Alem makes this bottleneck measurable and provides a controlled testbed for developing agents that communicate, allocate roles, and execute shared plans. Code is available at https://github.com/alem-world/alem-env.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有评估框架无法全面测试语言智能体在长时程、开放式多智能体环境中协调能力的问题。研究背景上，随着大语言模型被部署为自主智能体，它们需要在开放式交互任务中与其他智能体进行长期协调。然而，现有评估方法存在明显不足：要么侧重于单智能体任务，要么局限于短时程交互，或是在高度结构化的多智能体场景下进行测试（如MultiAgentBench、Collab-Overcooked等），缺乏将长时程交互、开放式任务结构与显式、可程序化生成且难度可控的协调需求相结合的综合评估体系。因此，本文核心要解决的是：构建一个能够系统衡量和诊断语言智能体在开放式多智能体环境中协调能力的研究工具。为此，论文提出了基于JAX的基准测试平台Alem，它通过程序化生成具有可控协调难度（从松散时间依赖到紧密联合行动）的复杂任务环境，并集成了探索、制作、交易和战斗等长期生存机制。通过评估13种现代大语言模型的零样本协调表现，论文发现当前智能体平均仅能达到约6%的标准化回报，且个体任务能力并不等同于协调能力，从而揭示了协调瓶颈是独立于单智能体能力的核心挑战。

### Q2: 有哪些相关研究？

相关研究可分为三类：**长期任务与智能体评估**、**多智能体LLM协作**和**多智能体强化学习（MARL）与协调**。

第一类工作聚焦于长期开放任务，如测试模型在复杂环境中的空间推理、探索和工具使用，但多为单智能体设定。本文（Alem）将程序生成原则引入多智能体评估，要求代理同时推断并满足多样化的协调需求。

第二类研究涉及多智能体LLM在代码生成、辩论等场景中的协作，但通常任务周期短，角色、目标或交互结构预设。Alem则检验LLM代理在长期开放世界中自主推断并执行动态协调要求的能力，这是其关键区别。

第三类MARL基准如SMAC（同步集火）、Overcooked（短期交接）、Melting Pot（长距离资源依赖）等，侧重特定协调形式。Alem基于Craftax-Coop但创新性地将协调设计为显式、可程序生成且难度可控的要素，引入软专业化、显式通信和频谱式协调任务，并通过信息论诊断验证真实的智能体间依赖性。

### Q3: 论文如何解决这个问题？

这篇论文提出了ALEM，一个基于JAX的开源基准测试环境，旨在系统性地评估语言智能体在开放式多智能体协调任务中的能力。核心方法是通过构建一个融合探索、制作、交易和战斗的长期生存世界，并将程序化生成的协调任务、软特化、通信和可控的协调难度嵌入其中。

在架构设计上，ALEM扩展了Craftax-Coop，沿四个维度创新：多样化的协调类型（同步与交接）、协调任务的程序化生成、软特化机制（任何智能体都可尝试执行角色特定动作，但专业者必定成功，非专业者成功率降低），以及显式的通信信道。观察空间包括像素和符号观察（本地地图、库存、团队仪表盘），动作空间为60维离散空间，支持环境操作、制作、探索、战斗，以及资源请求、队友物品给予和广播消息等团队协作功能。

主要技术包括使用单标量α∈[0,1]控制整体协调难度，α越大，协调约束越严格（如多智能体需求概率增加、交接窗口缩短、软任务失败率上升、非专业者效率降低）。通过设置易（α=0.3）、中（α=0.6）、难（α=0.9）三种难度，在保持世界布局和协调机会不变的情况下，干净地分离了执行难度和世界变化。信息论诊断验证了这些机制需要真正的智能体间依赖，而非单纯的单智能体难度增加。

创新点在于：1）将整个协调谱系（从长期依赖到同步联合行动）整合在一个开放世界中；2）程序化生成协调结构而非仅空间布局，防止智能体利用固定交互模式；3）使用软特化推动有效的角色分配，同时保留在线适应能力；4）提供可扩展的协调难度控制。实验表明，当前最先进的LLM智能体（零样本）平均仅达到约6%的归一化回报，而训练了10亿步的MARL基线在最高难度下也只达到18%的最高总奖励，证明ALEM对当前方法仍是未饱和的挑战，特别突出了协调能力作为前缘LLM智能体的一个独立瓶颈。

### Q4: 论文做了哪些实验？

论文在ALEM基准上进行了三组实验。**实验设置**：采用零样本同质团队评估13个现代LLM，并训练了4个MARL智能体作为参考，在Easy、Medium、Hard三种难度下测试。**数据集/基准测试**：使用ALEM环境，基于Craftax动态，包含程序化生成的协作任务、长期生存世界、探索、制作、交易和战斗。**对比方法**：包括GPT-5.4-High、Gemini-3.1-Pro-High、Gemma-4系列、Llama系列、Qwen系列等13个LLM，以及训练了1亿步和10亿步的MARL智能体。**主要结果**：1）所有LLM零样本表现较差，平均标准化回报仅约6%，但模型间差异显著，Gemini-3.1-Pro-High在Hard难度下协调回报达17.5%，接近训练10亿步的MARL（17.6%）。2）个体任务能力不代表协调能力，GPT-5.4-High基础任务回报高（11.8%），但协调回报低（4.2%）。3）大多数LLM无法利用难度变化，表现平稳。4）消融实验表明，通信是协调的最大贡献因素，记忆和推理有助于维持多步计划。5）异构团队中，不同模型组合表现各异。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在：评估仅覆盖文本型LLM和有限种子数量。未来可从以下方向深入：1）引入VLMs和Claude系列模型，提升对多模态感知与推理能力的测试；2）探索跨回合记忆和终身学习机制，使智能体能积累长期经验；3）研究更强的agent框架，如分层规划、自适应角色分配，或集成价值对齐来缓解竞争性行为；4）分析通信协议的可解释性与效率，例如学习压缩信息或非语言协作信号。此外，当前所有LLM采用零样本同质团队，未来可测试异质团队或基于人类反馈的微调策略。环境本身的随机性也值得控制，以分离模型与任务难度的影响。

### Q6: 总结一下论文的主要内容

这篇论文提出了一个名为Alem的JAX开源基准测试，用于评估语言模型在开放式多智能体协作中的能力。当前评估多集中于单智能体任务、短时交互或高度结构化的环境，而Alem整合了程序化生成的协作任务、软专业化分工、通信机制以及可调节的协作难度，置于一个包含探索、制作、交易和战斗的长周期生存世界中。研究评估了13个现代大模型在同质团队中的零样本表现，并以经过十亿步训练的MARL智能体作为参考。结果表明，当前LLM智能体远未解决Alem问题，平均标准化回报仅约6%。关键发现是，个体任务能力与协作能力分离：Gemini-3.1-Pro-High在最高协作难度下接近MARL性能，而GPT-5.4-High虽在基础任务上表现优异，但协作奖励很低。消融实验揭示通信是协作的最主要贡献因素，记忆和推理有助于维持多步计划。该工作精确地将协作瓶颈从单智能体能力中区分出来，为开发能沟通、分配角色和执行共享计划的基础模型提供了可量化的测试平台。
