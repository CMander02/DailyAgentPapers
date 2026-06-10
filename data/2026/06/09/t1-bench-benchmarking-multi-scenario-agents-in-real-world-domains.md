---
title: "T1-Bench: Benchmarking Multi-Scenario Agents in Real-World Domains"
authors:
  - "Genta Indra Winata"
  - "Amartya Chakraborty"
  - "Yuzhen Lin"
  - "Swasthi P Rao"
  - "Shikhhar Siingh"
  - "Houhan Lu"
  - "Nadia Bathaee"
  - "Sriharsha Hatwar"
  - "Paresh Dashore"
  - "Anmol Jain"
  - "Kshitij Tayal"
  - "Xiuzhu Lin"
  - "Anirban Das"
  - "Sambit Sahu"
  - "Shi-Xiong Zhang"
date: "2026-06-09"
arxiv_id: "2606.11070"
arxiv_url: "https://arxiv.org/abs/2606.11070"
pdf_url: "https://arxiv.org/pdf/2606.11070v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent Benchmark"
  - "Multi-Domain Agent"
  - "Tool Use"
  - "Multi-Step Reasoning"
  - "LLM Agent Evaluation"
relevance_score: 9.5
---

# T1-Bench: Benchmarking Multi-Scenario Agents in Real-World Domains

## 原始摘要

Recent advances in reasoning and tool-calling capabilities of large language models (LLMs) have enabled increasingly capable agentic systems. However, existing benchmarks remain limited in task complexity, realism, and domain diversity, and often fail to capture interactions that span multiple domains, limiting their ability to evaluate agents in realistic multi-step settings that require sustained reasoning and coordination. To address these limitations, we introduce T1-Bench, a high-fidelity, comprehensive benchmark for evaluating agentic systems in realistic customer-facing, multi-domain environments, featuring interleaved scenarios that require structured reasoning across multi-turn user-assistant interactions and substantially increasing both compositional complexity and evaluative rigor across 25 domains of varying difficulty. We evaluate T1-Bench using 12 proprietary and open-weight models, providing a reproducible and standardized framework for assessing agent behavior, tool utilization, and conversational quality in complex, multi-step environments. We further complement automatic evaluation with human judgments to strengthen the assessment of qualitative performance. Overall, T1-Bench substantially advances prior benchmarks by increasing task complexity, interaction depth, and domain coverage in simulated multi-domain environments. To facilitate future research on agentic systems, we will publicly release data and evaluation code as open source.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有大语言模型（LLM）智能体评估基准存在的局限性。研究背景是，尽管LLM已发展为具备推理、规划和工具调用能力的自主智能体，但现有评估基准在任务复杂性、真实性和领域多样性方面存在明显不足。具体而言，现有基准的不足包括：（1）通常局限于少量领域和静态交互场景，无法反映真实世界中跨多个服务领域的复杂任务；（2）基于单轮或简化的交互设计，难以捕捉需要持续推理和多步骤协调的智能体工作流；（3）早期错误可能在多步骤任务中累积传播，但现有评估未能有效检测这种鲁棒性问题。为解决这些核心问题，本文提出了T1-Bench，这是一个高保真、综合性的多领域智能体基准。它通过构建跨25个领域（含11个单领域和14个多领域）的交错场景，要求智能体在长期多轮交互中保持上下文一致性、协调工具调用并处理部分失败，从而评估其在真实客户场景中的端到端任务完成能力。该基准显著提升了任务复杂度、交互深度和领域覆盖度，为智能体系统的可靠性评估提供了更贴近实际部署的标准框架。

### Q2: 有哪些相关研究？

相关研究可分为两个方向：一是对话模拟方面的研究，二是工具增强型多智能体评测基准。在对话模拟领域，早期模板或检索式方法（如Self-Chat）多样性有限，近期LLM驱动的模拟器（如Sotopia、UserSimCRS、Tau-Bench）能实现更真实的多角色交互；APIGen-MT通过工具蓝图和LLM反馈构建对话数据。本文在此基础上引入丰富的上下文信号（人格、用户画像、任务目标、对话历史），提升了模拟的逼真度。在评测基准方面，早期工作（如APIBank、APIBench、ToolBench、BFCL）局限于静态单轮设置，后续GAIA、GTA、TravelPlanner、m&m's、ToolSandbox等引入了多步规划和状态工具但仍限于单领域。更近的T1、TheAgentCompany、FlowBench和Tau-Bench家族探索了跨域工具规划或双控制设置。与这些工作相比，T1-Bench统一了大规模多领域互联环境与真实时长的客户交互，通过自动化评测框架实现全面评估，在任务复杂度、交互深度和领域覆盖上显著超越此前基准，并补充了人工评判来强化定性评估。

### Q3: 论文如何解决这个问题？

T1-Bench通过一个双智能体角色扮演框架和自动化评估流水线来解决现有基准在任务复杂性、真实性和领域多样性方面的不足。核心方法包括：

1. **双智能体交互框架**：框架包含用户智能体和助手智能体，两者均由大模型实例化，遵循结构化行为策略。用户智能体基于用户策略、任务目标和对话历史生成自然语言查询，模拟真实客户行为；助手智能体则执行工具调用并基于结果生成响应，支持搜索、过滤、预订、修改和取消等多步操作。

2. **模块化架构**：包含内存模块，维护对话历史和中间状态缓存，支持跨对话轮次的上下文保持和工具结果重用；工具集，包含25个领域（11个单一领域和14个多领域组合）的专用工具和API，每个工具附有文档字符串；策略模块，定义领域约束、操作规则和行为准则。

3. **自动化评估体系**：评估工具调用正确性（精确率、召回率、F1）、参数匹配、工具输出精确匹配（EM）、对话级通过率（Pass@K和Pass^K），以及基于LLM作为评判的对话质量评估（有用性和连贯性）。同时引入人工评估验证自动评估的可靠性。

创新点在于：覆盖25个真实域名的多领域交织场景，模拟多轮交互中需要结构化推理的复杂任务；通过确定性数据集和可执行工具实现可重复、细粒度的评估；以及结合自动评估与人工判断的综合评价方法。

### Q4: 论文做了哪些实验？

论文在T1-Bench上对12个模型（6个开源：GPT-OSS 20B/120B、Gemma4系列5个变体；6个闭源：Claude Haiku/Sonnet/Opus 4.5/4.6、GPT-5.4-Nano/Mini/5.4）进行了全面评估。实验设置中，用户和评判模型统一使用Gemma4-26B-A4B-it。主要评估维度包括：工具调用准确性（精确率、召回率、F1、准确率）、参数提取准确性、工具输出精确匹配率、对话级通过率（Pass@K和Pass^K，K=3），以及基于LLM评判框架的对话质量（帮助性和连贯性，1-5 Likert量表）。关键结果：Gemma4-31B-it在端到端任务完成上表现最佳，Pass@K达61.33%，Pass^K达41.14%；Claude Opus 4.6工具调用F1最高（93.34%）。随着领域数量增加，所有模型性能急剧下降，在8领域和11领域场景中通过率均为0。单领域任务中，Bar和Dessert表现最好，而Food & Dining（含15个工具）Pass@K仅3.5%。人类评估实验在60个对话样本上验证了LLM评判的可靠性：Krippendorff's α（连贯性0.687，帮助性0.657）和Spearman相关性（ρ分别为0.457和0.525，p<0.001）均达显著水平。

### Q5: 有什么可以进一步探索的点？

T1-Bench的局限性主要集中在三个方面。首先是用户模拟器的简化处理，当前采用固定的领域schema和相对简单的用户画像，未来可以引入更动态、更具个性的用户模型，比如模拟用户情绪变化、模糊表达或临时变更需求，以测试AI Agent的应变能力。其次是地域限制，目前仅使用美国数据，这限制了多语言与跨文化场景的评估，一个重要的改进方向是扩展到全球范围，特别是纳入中文等非英语环境的复杂任务。最后，计算资源限制导致仅能评估部分顶尖模型，未来应考虑更高效的采样策略或模型蒸馏方法，以支持开源社区更广泛的参与。此外，当前评估侧重单次交互的完成度，但真正的Agent系统需要长期记忆和跨会话的一致性，未来的研究可以探索基于长期记忆的持续学习机制，以及如何在多轮复杂交互中维持任务上下文不丢失。

### Q6: 总结一下论文的主要内容

T1-Bench是一个用于评估AI代理系统的高保真基准测试，旨在解决现有基准在任务复杂性、真实性和领域多样性方面的不足。该基准涵盖25个领域（11个单域和14个多域设置）及76个工具，采用用户与助手代理间的多轮交互和跨域协调场景。方法上，通过引入策略约束、工具增强推理和共享记忆模块，评估代理在复杂环境中的工具调用准确率、输出正确性及端到端任务成功率。主要结论表明，现有模型（12种专有及开源模型）在可靠工具编排方面仍存在挑战，尤其面对部分失败传播时鲁棒性不足。T1-Bench通过提升交互深度和评估严格性，为现实世界多步任务代理的评估提供了更代表性框架，并将开源数据和代码以推动后续研究。
