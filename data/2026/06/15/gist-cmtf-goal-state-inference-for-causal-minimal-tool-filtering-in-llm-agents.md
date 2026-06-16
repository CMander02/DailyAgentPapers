---
title: "GIST-CMTF: Goal-State Inference for Causal Minimal Tool Filtering in LLM Agents"
authors:
  - "Rahul Suresh Babu"
  - "Rohit Shukla"
date: "2026-06-15"
arxiv_id: "2606.16813"
arxiv_url: "https://arxiv.org/abs/2606.16813"
pdf_url: "https://arxiv.org/pdf/2606.16813v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "工具使用"
  - "目标推理"
  - "因果过滤"
  - "任务规划"
  - "多智能体"
relevance_score: 9.5
---

# GIST-CMTF: Goal-State Inference for Causal Minimal Tool Filtering in LLM Agents

## 原始摘要

Tool-augmented LLM agents rely on runtime filtering to decide which tools should be visible at each step. Causal Minimal Tool Filtering (CMTF) reduces tool-choice confusion by exposing only the next causally necessary tool frontier, but it assumes that the user request has already been mapped to a symbolic goal state. In practice, requests such as "handle my appointment" or "take care of this email" may correspond to multiple possible goals. This creates wrong-goal execution, where an agent follows a valid causal tool path for an unintended objective. We introduce GIST-CMTF, a goal-state inference layer that predicts candidate symbolic goals over the same state-transition vocabulary used by CMTF, estimates ambiguity, and either applies CMTF or exposes clarification as a causal action that produces missing goal or state variables. We evaluate GIST-CMTF across seven model backends, six filtering methods, and 120 controlled tool-use tasks. GIST-CMTF achieves 97.0% task success, compared with 80.1% for top-goal CMTF and 82.9% for semantic-goal CMTF. It reduces wrong-goal execution from 19.4% under top-goal CMTF to 2.5%, while preserving the one-tool exposure of causal filtering and using substantially fewer tokens than all-tools exposure. These results suggest that reliable tool-augmented agents should validate goal state, not only tool relevance, before exposing external actions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决工具增强型大语言模型（LLM）智能体在执行用户请求时，因目标状态推理缺失而导致错误执行的问题。研究背景是，现有方法如因果最小工具过滤（CMTF）通过暴露因果必要的下一工具来减少工具选择混淆，但其核心假设是用户请求已被映射为明确的符号化目标状态。然而在实际场景中，用户请求如“处理我的预约”或“处理这封邮件”可能对应多个潜在目标（如查找、修改、删除等），这导致即使智能体基于正确因果路径选择工具，也会因目标错误而执行用户未曾期望的操作，即“错误目标执行”。现有方法（如CMTF）仅关注工具相关性，忽略了上游目标验证环节。因此，本文要解决的核心问题是：在工具过滤前，如何从模糊、欠指定的自然语言请求中推理出正确的符号化目标状态，并处理目标歧义，从而避免因目标错误导致的无效执行。具体而言，GIST-CMTF通过构建目标状态推理层，预测候选符号化目标，估计歧义程度，并在必要时将澄清动作建模为因果动作，以在目标不明确时主动引导用户确认，从而保证下游工具过滤的可靠性。

### Q2: 有哪些相关研究？

相关研究主要分为方法类、应用类和评测类。

在方法类中，最直接相关的是Causal Minimal Tool Filtering (CMTF)，它通过工具契约（preconditions/effects）构建依赖图，只暴露当前因果必要工具，但依赖预定义的符号目标状态。本文指出其关键缺陷，即当用户请求（如“处理我的邮件”）对应多个可能目标时，CMTF会沿错误目标执行。此外，经典规划形式化方法（如STRIPS、PDDL）使用前提-效果表示动作，本文借鉴了其符号状态转换思想，但并非替换LLM为符号规划器，而是用于约束LLM可见的工具接口。工具契约学习相关研究自动从工具名称、描述等推断前提/效果/风险标签，减轻了人工编写负担，但本文指出即便有准确契约，因果过滤仍要求目标状态明确。

在应用类研究中，工具增强LLM代理的工作（如函数调用基准、API选择、多步工具使用）普遍假设工具接口已构建好，未考虑目标歧义性。可靠性导向编排工作（如故障检测、恢复动作、可观测性追踪）侧重于运行时鲁棒性，但未将目标状态验证作为显式控制面。本文首次将目标状态推断作为因果工具过滤的上游层，并引入澄清作为因果动作来补全缺失目标变量。

评测类工作中，本文在120个受控工具使用任务上对比了七种后端模型和六种过滤方法，证明了GIST-CMTF相比top-goal CMTF和semantic-goal CMTF在任务成功率（97.0%）和减少错误目标执行（从19.4%降至2.5%）上的优势，同时保持一次性工具暴露和更低token消耗。

### Q3: 论文如何解决这个问题？

GIST-CMTF通过引入一个上游的目标状态推理层来扩展因果最小工具过滤（CMTF），解决用户请求可能对应多个目标导致的错误目标执行问题。其核心方法是先推理候选符号化目标状态，再决定是应用CMTF还是触发澄清动作。

整体框架分为四个阶段：1) 从自然语言请求q生成候选符号化目标状态集合G_q，每个目标g_i附有置信度p_i，目标采用与CMTF相同的状态变量词汇；2) 通过歧义检测器A评估目标明确性，考虑置信度阈值τ、顶部目标与次优目标置信度差δ、必要变量缺失、模糊动词（如"处理"）、以及暴露敏感操作（写/发送/删除等）的风险信号；3) 若检测到歧义，系统暴露一个因果动作形式的澄清动作（如a_g: ambiguous_goal → goal_specified），而非下游外部工具，该澄清动作保持与工具相同的先决条件-效果框架；4) 若目标被接受，则使用选定目标g*应用CMTF，暴露下一个因果充分工具前沿V_t = F(s_t, g*, T)。

主要创新点包括：将目标验证与工具选择分离，在暴露工具前沿前先验证用户意图；将澄清操作形式化为具有先决条件和效果的因果动作而非临时回退；提出三种实现变体（top-goal、thresholded、risk-sensitive）来分离目标推理与澄清的价值。该设计通过防止系统在意图不明确时承诺错误的符号化目标，将错误目标执行率从19.4%降至2.5%，同时保持CMTF的单工具暴露和较低token消耗。

### Q4: 论文做了哪些实验？

GIST-CMTF在120个受控工具使用任务上进行了评估，这些任务涵盖日历、邮件、文件/文档、联系人和授权/确认等工作流领域。数据集包含四种请求类型：显式目标（40个）、模糊目标（40个）、缺失变量（30个）和需要澄清（10个）。实验对比了六种过滤方法：全部工具暴露、状态感知过滤、Top-goal CMTF、Semantic-goal CMTF、GIST-CMTF以及作为上限的Gold-goal CMTF，使用了七个模型后端（包括Claude Opus 4.8、Sonnet 4.6、Haiku 4.5、GPT-OSS-120B、Nova Premier等），共完成5,040次运行。

主要结果：GIST-CMTF在任务成功率上达到97.0%，显著优于Top-goal CMTF（80.1%）和Semantic-goal CMTF（82.9%），接近Gold-goal CMTF上限（99.5%）。在错误目标执行率方面，GIST-CMTF仅为2.5%，远低于Top-goal CMTF的19.4%和Semantic-goal CMTF的16.7%。GIST-CMTF在所有模型后端上表现稳定，平均每步只暴露1个工具，与因果过滤方法保持一致，平均token使用量为1,186个，远低于全部工具暴露的4,152个。在模糊目标请求上，GIST-CMTF实现了97.5%的成功率，并将错误目标执行率降至2.1%。

### Q5: 有什么可以进一步探索的点？

### 局限性与未来方向

1. **符号状态假设的脆弱性**：GIST-CMTF依赖共享符号词汇表表示目标、工具前置条件和效果，但在真实场景中，用户请求可能充满噪声、状态不完备，且API和工具生态快速变化。未来可探索**动态词汇学习**——利用LLM的语义理解能力自动归纳状态变量，或通过强化学习在运行时调整抽象层级。

2. **开放世界目标发现**：当前评估仅限于预定义候选目标集，而真实用户可能提出完全陌生的意图。可结合**LLM的零样本推理**，让系统在遇到未知目标时主动生成新的状态变量，而非仅从候选集中选择。

3. **多轮澄清的鲁棒性**：将澄清视为因果动作虽巧妙，但现实对话可能需多轮交互且用户反馈模糊。未来可引入**置信度阈值**——根据工具风险动态决定是否继续澄清还是激进推理，并利用可解释性技术（如注意力权重）判断用户意图一致性。

4. **副作用与随机性**：工具执行可能产生非确定性输出（如API超时），而当前假设工具结果完全可预测。可设计**因果概率模型**，在状态转换中引入不确定性分布，或在失败时触发备选路径。

5. **成本-风险权衡泛化**：澄清会增加Token消耗，但对高风险操作（如删除文件）的纠错价值远高于低风险操作（如只读查询）。未来可建立**风险感知的权衡函数**，将操作类型、用户历史行为纳入决策，实现自适应。

### Q6: 总结一下论文的主要内容

Causal Minimal Tool Filtering (CMTF) 假设用户请求已映射到符号目标状态，但实际请求如“处理我的预约”可能对应多个可能目标，导致代理执行有效但意图错误的工具路径。GIST-CMTF 引入目标状态推理层，在 CMTF 之上预测候选符号目标，评估歧义性，并决定应用 CMTF 或暴露澄清作为因果动作。在7个模型后端、6种过滤方法和120个受控工具使用任务中，GIST-CMTF 实现了97.0%的任务成功率，而 top-goal CMTF 和 semantic-goal CMTF 分别为80.1%和82.9%。它将 wrong-goal 执行从 top-goal CMTF 下的19.4%降至2.5%，同时保持因果过滤的单工具暴露并使用更少 token。核心贡献在于将目标状态推理形式化为因果工具过滤的缺失上游问题，识别 wrong-goal 执行为独特失败模式，并将澄清建模为具有前提和效果的因果动作。结果表明，可靠的工具增强代理应在暴露外部动作前验证目标状态而不仅仅是工具相关性。
