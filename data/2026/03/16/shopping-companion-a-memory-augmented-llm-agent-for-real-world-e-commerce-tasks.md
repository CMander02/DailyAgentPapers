---
title: "Shopping Companion: A Memory-Augmented LLM Agent for Real-World E-Commerce Tasks"
authors:
  - "Zijian Yu"
  - "Kejun Xiao"
  - "Huaipeng Zhao"
  - "Tao Luo"
  - "Xiaoyi Zeng"
date: "2026-03-16"
arxiv_id: "2603.14864"
arxiv_url: "https://arxiv.org/abs/2603.14864"
pdf_url: "https://arxiv.org/pdf/2603.14864v1"
categories:
  - "cs.CL"
tags:
  - "Memory-Augmented Agent"
  - "E-Commerce Agent"
  - "Long-Term Interaction"
  - "Benchmark"
  - "Reinforcement Learning"
  - "Tool Use"
  - "End-to-End Optimization"
relevance_score: 8.0
---

# Shopping Companion: A Memory-Augmented LLM Agent for Real-World E-Commerce Tasks

## 原始摘要

In e-commerce, LLM agents show promise for shopping tasks such as recommendations, budgeting, and bundle deals, where accurately capturing user preferences from long-term conversations is critical. However, two challenges hinder realizing this potential: (1) the absence of benchmarks for evaluating long-term preference-aware shopping tasks, and (2) the lack of end-to-end optimization due to existing designs that treat preference identification and shopping assistance as separate components. In this paper, we introduce a novel benchmark with a long-term memory setup, spanning two shopping tasks over 1.2 million real-world products, and propose Shopping Companion, a unified framework that jointly tackles memory retrieval and shopping assistance while supporting user intervention. To train such capabilities, we develop a dual-reward reinforcement learning strategy with tool-wise rewards to handle the sparse and discontinuous rewards inherent in multi-turn interactions. Experimental results demonstrate that even state-of-the-art models (such as GPT-5) achieve success rates under 70% on our benchmark, highlighting the significant challenges in this domain. Notably, our lightweight LLM, trained with Shopping Companion, consistently outperforms strong baselines, achieving better preference capture and task performance, which validates the effectiveness of our unified design.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在现实世界电子商务任务（如推荐、预算管理和捆绑交易）中，如何有效利用长期对话历史来准确捕捉用户偏好并完成复杂购物任务的核心问题。

研究背景是LLM智能体在电商领域展现出潜力，但成功高度依赖于从多轮、跨会话的长期对话中理解用户隐含的偏好（如品牌好恶、尺寸历史）。现有方法存在两大不足：首先，缺乏一个能够同时评估**长期记忆感知能力**和**端到端购物任务执行能力**的基准测试。现有基准（如WebShop、ShoppingBench）要么只关注单会话任务而缺乏长期记忆评估，要么（如LongMemEval）只评估记忆能力而不与下游购物任务结合。其次，现有智能体设计通常将**偏好识别**和**购物辅助**作为两个分离的组件进行优化，这种割裂的设计缺乏端到端的联合优化，可能影响整体性能。

因此，本文要解决的核心问题是：**如何在一个统一的框架内，协同优化长期记忆检索与购物任务执行，以应对需要理解长期偏好、支持多轮用户干预的现实电商场景**。为此，论文提出了包含长期记忆设置的创新基准，并设计了名为“Shopping Companion”的统一框架，该框架将记忆检索与购物辅助整合，并支持用户干预。同时，为了训练该框架应对多轮交互中奖励稀疏和间断的挑战，论文还提出了一种带有工具级奖励的双奖励强化学习策略。

### Q2: 有哪些相关研究？

相关研究主要可分为长期记忆和购物智能体两大类。

在长期记忆方面，现有研究多将记忆外化为可检索的记录，并通过检索增强管道注入生成过程。近期系统进一步将记忆建模为具有结构化组织的显式读写子系统。然而，基准测试（如LongMemEval）揭示了在多会话推理和上下文效率方面仍存在不足，其核心局限在于优化：长期记忆模块通常作为事后组件，未与下游任务成功进行端到端训练。与本文最相关的是Agentic Memory，它通过将记忆操作作为工具动作并采用逐步GRPO进行训练，向缩小这一差距迈进了一步。本文工作将这种策略级优化扩展到现实世界购物任务中，联合优化以偏好为中心的长期记忆与任务执行。

在购物智能体方面，电子商务助手需要与大型产品数据库进行接地气的交互并满足多轮约束。先前关于对话式产品搜索和推荐的研究已联合处理澄清提问和物品排序，而Wizard of Shopping等数据集通过结构化搜索过程进一步提升了真实性。补充这些任务导向的努力，ShoppingBench、Shopping MMLU和EcomScriptBench等基准评估了更广泛的购物能力，涵盖基于意图的端到端评估、领域知识和脚本级规划。尽管取得了进展，但现有的基准或方法均未明确将跨会话的长期偏好记忆与端到端的购物成功耦合——大多数系统将记忆视为孤立的上游阶段。本文通过提出一个将购物偏好嵌入长期通用对话的基准，并训练一个集成长期记忆检索与购物协助的统一智能体策略，来弥补这一缺口。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“Shopping Companion”的统一框架来解决长时记忆感知的电商任务问题，其核心方法、架构设计和关键技术如下：

**整体框架与主要模块**：Shopping Companion 采用两阶段架构，实现端到端优化。第一阶段为**偏好识别**，通过记忆检索工具从长时对话历史中提取隐式用户偏好（如品牌厌恶、尺寸历史），并呈现给用户进行确认和干预，确保偏好准确捕获。第二阶段为**购物协助**，基于已确认的偏好，迭代检索产品并验证其是否同时满足指令驱动需求（如预算、品类）和记忆驱动偏好，直至任务完成。两个阶段共享统一的智能体模型，通过工具交互环境（包含记忆和产品两个检索引擎及五个工具）实现协同运作。

**创新点与关键技术**：
1. **统一框架设计**：将偏好识别与购物协助整合为单一智能体，避免了传统方法中两者分离导致的次优问题，支持用户干预，增强了实用性和准确性。
2. **双奖励强化学习策略**：针对多轮交互中奖励稀疏且不连续的问题，设计了阶段对齐的双奖励机制。阶段一奖励（\(R_1\)）评估偏好提取的准确性（包括查询相关性、属性匹配和产品数量匹配）；阶段二奖励（\(R_2\)）评估最终推荐的产品是否满足约束条件（如产品有效性、相关性、属性匹配、数量与预算可行性）。此外，引入**工具级奖励**（\(R_{tool}\)）对中间工具调用进行细粒度评分，改善信用分配；并结合**格式奖励**（\(R_{fmt}\)）确保结构化输出（如思维标签、工具调用JSON、推荐模式）的稳定性，最终奖励为三者加权和。
3. **基准与训练方法**：论文构建了包含120万真实商品的长时记忆基准，涵盖单产品和附加交易两类任务。通过强化学习端到端训练轻量级LLM，使智能体能联合优化记忆检索与购物决策，实验表明其在偏好捕获和任务性能上均优于基线模型（包括GPT-5等先进模型），验证了统一设计的有效性。

### Q4: 论文做了哪些实验？

论文实验部分围绕提出的Shopping Companion框架和配套基准展开。实验设置方面，研究构建了一个包含1000条指令（每个任务500条）的基准数据集，其中每条指令附带15-50轮对话历史，并嵌入用户偏好。数据集按800/200划分训练集和测试集。

对比方法包括闭源模型（如GPT-5、GPT-4.1、GPT-4o、Qwen3-Max）和开源模型（Qwen3系列），均在零样本设置下评估。同时，论文逐步展示了所提方法的改进：1) Qwen3-4B + LoRA微调；2) 加入双奖励强化学习；3) 进一步加入工具级奖励。

评估采用基于LLM的评估器，使用两个关键指标：准确率（Acc.）衡量第一阶段偏好提取的成功率；成功率（Succ.）衡量端到端任务完成度，需满足产品数量正确、显性需求满足、偏好匹配及预算可行（针对附加交易）四项检查。

主要结果显示，在单产品推荐任务上，表现最佳的闭源模型GPT-5获得82.0% Acc.和75.0% Succ.，而开源模型Qwen3-4B仅为49.0% Acc.和44.0% Succ.。在附加交易任务上，所有基线模型表现显著下降，GPT-5成功率仅54.0%，Qwen3-4B低至6.0%。相比之下，采用双奖励及工具级奖励训练的Shopping Companion（基于Qwen3-4B）在单产品任务上达到90.0% Acc.和84.0% Succ.，在附加交易任务上达到55.0% Acc.和43.0% Succ.，平均成功率为63.5%，显著优于开源基线，并接近闭源模型性能。

消融实验验证了两阶段策略的有效性：一阶段策略平均成功率仅52.5%，而两阶段策略（无提示）提升至65.0%，加入用户模拟反馈后可达70.0%。行为分析表明，工具级奖励能提升工具使用质量（工具得分更高），并减少冗余交互（平均轮数从9.82降至8.89）和响应长度。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要体现在两个方面：一是处理预算约束下的多商品任务（如附加优惠捆绑）时性能仍有不足，这需要模型同时权衡预算、商品间兼容性和用户偏好，组合优化难度较大；二是所设计的工具级奖励机制针对特定电商工具集，其泛化至其他领域或更广泛的工具增强智能体场景时可能面临适应性挑战，如何系统化设计可扩展的细粒度奖励仍待探索。

未来可进一步探索的方向包括：开发更强大的推理机制以处理多商品组合优化，例如引入强化学习中的分层策略或结合符号推理；设计跨领域通用的工具奖励框架，或许可通过元学习或自动化奖励分解来提升适应性；此外，可考虑融入多模态信息（如图像、视频）以更全面理解商品特性，并增强用户干预机制的可解释性，使智能体的决策过程更加透明可信。

### Q6: 总结一下论文的主要内容

该论文针对电子商务场景中LLM智能体在长期对话中准确捕捉用户偏好以完成购物任务（如推荐、预算规划、捆绑交易）的挑战，提出了一个统一的解决方案。核心贡献包括：首先，构建了一个包含跨会话对话历史、两种现实购物任务（涉及120万真实商品）并支持多轮用户干预的长期记忆基准测试，该基准对现有先进模型（如GPT-5）仍具挑战性（成功率低于70%）。其次，提出了Shopping Companion框架，将偏好识别与购物辅助作为统一组件进行端到端联合优化，支持用户干预。方法上采用了一种双奖励强化学习策略，并辅以工具级监督，以应对多轮交互中奖励稀疏和不连续的问题。实验表明，基于该框架训练的轻量级LLM在偏好捕捉和任务成功率上均优于现有基线，验证了联合优化记忆检索与下游购物决策的有效性，为构建可靠、偏好感知的电商智能体提供了可行路径。
