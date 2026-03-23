---
title: "A Subgoal-driven Framework for Improving Long-Horizon LLM Agents"
authors:
  - "Taiyi Wang"
  - "Sian Gooding"
  - "Florian Hartmann"
  - "Oriana Riva"
  - "Edward Grefenstette"
date: "2026-03-20"
arxiv_id: "2603.19685"
arxiv_url: "https://arxiv.org/abs/2603.19685"
pdf_url: "https://arxiv.org/pdf/2603.19685v1"
categories:
  - "cs.AI"
  - "cs.LG"
  - "cs.MA"
tags:
  - "Agent Architecture"
  - "Long-Horizon Planning"
  - "Subgoal Decomposition"
  - "Reinforcement Learning"
  - "Web Navigation"
  - "Training Framework"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# A Subgoal-driven Framework for Improving Long-Horizon LLM Agents

## 原始摘要

Large language model (LLM)-based agents have emerged as powerful autonomous controllers for digital environments, including mobile interfaces, operating systems, and web browsers. Web navigation, for example, requires handling dynamic content and long sequences of actions, making it particularly challenging. Existing LLM-based agents struggle with long-horizon planning in two main ways. During online execution, they often lose track as new information arrives, lacking a clear and adaptive path toward the final goal. This issue is further exacerbated during reinforcement learning (RL) fine-tuning, where sparse and delayed rewards make it difficult for agents to identify which actions lead to success, preventing them from maintaining coherent reasoning over extended tasks. To address these challenges, we propose two contributions. First, we introduce an agent framework that leverages proprietary models for online planning through subgoal decomposition. Second, we present MiRA (Milestoning your Reinforcement Learning Enhanced Agent), an RL training framework that uses dense, milestone-based reward signals. The real-time planning mechanism improves proprietary models such as Gemini by approximately a 10% absolute increase in success rate (SR) on the WebArena-Lite benchmark. Meanwhile, applying MiRA to the open Gemma3-12B model increases its success rate from 6.4% to 43.0%. This performance surpasses proprietary systems such as GPT-4-Turbo (17.6%) and GPT-4o (13.9%), as well as the previous open-model state of the art, WebRL (38.4%). Overall, our findings demonstrate that combining explicit inference-time planning with milestone-based rewards significantly improves an agent's long-horizon capabilities, paving the way for more robust and general-purpose autonomous systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能体在执行长视野（long-horizon）任务时，尤其是在复杂网页导航等数字环境中，所面临的规划与学习难题。

**研究背景**：LLM智能体已成为控制移动界面、操作系统和网页浏览器等数字环境的强大自主控制器。其中，网页导航因动态内容和长动作序列而极具挑战性，是评估智能体推理能力的严格测试平台。尽管存在WebArena等现实基准测试，当前智能体在长任务上仍表现不佳，性能随任务复杂度和序列长度增加而急剧下降。

**现有方法的不足**：论文指出，现有LLM智能体在长视野规划上存在两大主要缺陷。首先，在**在线执行**过程中，智能体容易在接收到新信息后迷失方向，缺乏清晰且自适应的路径来达成最终目标，常陷入非生产性的动作循环或次优路径。其次，在**强化学习（RL）微调**过程中，稀疏和延迟的奖励信号使得智能体难以识别哪些动作导致了成功，阻碍了其在扩展任务中保持连贯推理。无论是依赖监督微调（SFT）还是传统RL的方法，都存在静态数据泛化差、训练不稳定或奖励信号噪声大等问题。

**本文要解决的核心问题**：针对上述不足，本文的核心问题是：如何通过引入明确的**子目标（subgoal）或里程碑（milestone）**，来系统性地提升LLM智能体在长视野任务中的规划鲁棒性和学习效率？具体而言，论文旨在解决三个关键挑战：（C1）子目标的可靠来源问题；（C2）如何将子目标推理高效集成到在线推理中而不引入过高延迟或上下文开销；（C3）如何在RL训练中嵌入中间奖励以改善信用分配和稳定性，同时不阻碍最终目标的达成。为此，论文提出了一个统一的子目标驱动框架，结合了在线推理时的子目标分解规划和离线RL微调时的里程碑奖励塑形，以增强智能体的持续推理和自适应规划能力。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕基于大语言模型的计算机使用智能体展开，可分为方法范式、特定领域（如网页导航）的改进以及长视野规划与奖励设计三类。

在**方法范式**上，现有研究主要分为三类：基于提示的智能体（如OpenAI的Operator平台），利用结构化指令实现零样本控制，但适应性和长流程任务能力有限；基于模仿学习的智能体，通过监督微调学习演示数据，任务对齐性好但难以从错误中恢复；基于强化学习的智能体，通过交互学习，但面临稀疏奖励的挑战。本文提出的MiRA框架属于强化学习范式，但通过引入里程碑奖励显著缓解了奖励稀疏问题。

在**网页导航等特定领域**，近期工作尝试结合多种范式以应对长视野任务挑战。例如，WebRL框架通过自演进课程解决训练任务稀缺和反馈稀疏问题；IBM的CUGA采用分层规划-执行框架，具备显式任务分解和重规划机制，但其分析指出超过约10步的任务常因子目标一致性丧失而失败。本文继承了CUGA对规划保真度的关注，但提出了更轻量、低延迟的在线子目标驱动规划框架，并在专有模型上验证了其有效性。

在**长视野规划与奖励设计**方面，研究旨在改善信用分配和持续推理。例如，过程奖励模型（如Web-Shepherd、AgentPRM）提供密集的逐步监督，但存在推理开销大和奖励过优化风险。在目标条件强化学习中， hindsight experience replay 等技术通过目标重标记增加学习信号，但通常假设马尔可夫奖励，难以直接适用于网页导航的非马尔可夫长序列。近期工作如GCPO（一种基于策略的GCRL框架）和WebAgent-R1探索了内在动机和并行轨迹生成。此外，如HIQL等方法学习潜在子目标进行分层规划，但缺乏语义可解释性。本文与这些工作的核心区别在于：**1）** 不使用潜在子目标或噪声模拟，而是依赖**显式、语义可验证的里程碑**作为硬性检查点，兼顾了进度跟踪的可靠性与可验证性；**2）** 在RL微调中，里程碑仅作为辅助奖励，确保不偏离最终的真实目标，从而在稳定训练的同时避免了奖励过优化。

### Q3: 论文如何解决这个问题？

论文通过提出一个以子目标驱动的框架来解决长视野任务中LLM智能体规划能力不足和强化学习训练信号稀疏的问题。其核心方法分为两个主要贡献：一个用于在线规划的智能体框架，以及一个名为MiRA的强化学习训练框架。

整体框架包含三个关键组件：可靠的子目标生成、基于大型专有模型的推理时性能提升，以及通过子目标驱动的奖励塑形来增强RL微调。首先，论文利用教师模型（如Gemini-2.5-pro）通过迭代的上下文学习策略生成子目标，这些子目标将抽象的用户意图分解为逻辑上的中间里程碑。为确保质量，论文通过精确等价和分级一致性两种方式验证子目标，证实其作为连续进度指示器的有效性（AUROC达0.84），能可靠地区分成功与失败的轨迹。

在在线推理阶段，论文提出了动态里程碑框架。该框架的核心创新在于引入了“回顾性反思”机制：智能体在每个时间步查询其历史交互轨迹（包括截图和行动日志），通过一个AutoRater（LLM-as-Judge）模块评估当前状态与子目标清单的对比，从而动态更新其进度信念状态（表示为二进制子目标向量）。这种机制将不透明的执行状态转化为结构化的显式上下文，使模型能基于已验证的进度进行重新规划或聚焦下一步行动，实现了情境感知和错误恢复，有效防止了幻觉和错误传播。

对于离线训练，MiRA框架通过密集的、基于里程碑的奖励信号来解决稀疏和延迟奖励问题。其关键创新是引入了双评论家架构：一个标准的基于目标的条件价值评论家用于学习最终成败的二元结果，以及一个新的潜在评论家，它作为一个由子目标检查器驱动的密集进度模型。潜在评论家估计当前状态与最终目标之间的“进展潜力”，从而提供更密集的中间奖励信号，指导智能体在长序列任务中保持连贯推理。实验表明，该框架显著提升了性能，例如将Gemma3-12B的成功率从6.4%提升至43.0%。

### Q4: 论文做了哪些实验？

论文的实验主要包括三个部分：失败模式定量分析、子目标生成与验证，以及在线推理与强化学习训练框架的性能评估。

**实验设置与数据集**：实验在WebArena-Lite基准测试上进行，这是一个模拟真实网络环境的交互式基准，要求智能体完成多步骤任务（如信息查找、表单填写）。主要对比方法包括：1) 基线开源模型（如Gemma、Gemma-SFT）；2) 专有模型系统（如GPT-4-Turbo、GPT-4o）；3) 先前开源模型的最佳方法WebRL。

**关键实验与结果**：
1. **失败模式分析**：通过自动化分析器对Gemini-2.5-pro、Gemma等模型的轨迹进行大规模分析，将失败归类为四类：中途卡住（Get Stuck Midway）、错误终止（Wrong Termination）、未合理尝试（Fail to Make Reasonable Attempt）及其他。分析发现，**中途卡住是主要失败模式**，占比42%-49%，揭示了现有智能体在长程规划上的缺陷。

2. **子目标生成与验证**：利用Gemini-2.5-pro生成子目标，并通过统计验证其质量。关键指标显示：子目标完成分数与最终成功率的AUROC达**0.84**，Kendall's τ秩相关系数为**0.4585**（p<0.001），表明子目标能可靠预测进度。

3. **在线推理与强化学习性能**：
   - **在线规划**：提出的动态里程碑框架（Gemini-SGO）在WebArena-Lite上使Gemini模型的**成功率绝对提升约10%**。
   - **强化学习训练**：MiRA框架应用于开源Gemma3-12B模型，**成功率从6.4%提升至43.0%**，超越了GPT-4-Turbo（17.6%）、GPT-4o（13.9%）及WebRL（38.4%），达到新的开源模型最优性能。

这些实验验证了结合显式推理时规划与基于里程碑的奖励能显著提升智能体的长程任务能力。

### Q5: 有什么可以进一步探索的点？

该论文提出的子目标驱动框架和里程碑奖励机制显著提升了智能体在长视野任务中的表现，但仍存在一些局限性和可进一步探索的方向。

首先，论文的框架依赖于专有模型（如Gemini）进行在线子目标分解，这限制了其透明度和可复现性。未来研究可以探索如何将这种规划能力迁移到完全开源模型上，或设计更通用的子目标发现算法，减少对特定大模型的依赖。

其次，里程碑奖励的设定目前可能仍需人工设计或依赖先验知识。一个重要的方向是研究如何让智能体在交互中**自主发现并定义有意义的里程碑**，实现奖励函数的自举（bootstrapping），从而更好地适应多样化的未知任务。

此外，该工作主要在Web导航环境中验证，其通用性有待考察。未来的探索可以包括：1）将框架应用于更复杂的物理交互或多模态环境，检验其泛化能力；2）研究子目标规划与强化学习训练的更深层耦合，例如让规划模块本身也能通过RL进行优化，形成双向改进；3）探索在动态变化更剧烈、奖励更稀疏的环境（如长期战略游戏）中的应用，这将是检验其长视野推理能力的更严峻考验。

### Q6: 总结一下论文的主要内容

该论文针对基于大语言模型（LLM）的智能体在长视野任务（如网页导航）中存在的两大核心问题提出解决方案：在线执行时因信息动态变化而迷失方向，以及强化学习微调时因奖励稀疏延迟而难以进行有效信用分配。论文的核心贡献是提出了一个子目标驱动的框架，该框架包含两个主要部分：一是利用专有模型进行在线规划，通过子目标分解来引导智能体行动；二是提出了名为MiRA的强化学习训练框架，该框架使用基于里程碑的密集奖励信号来优化模型。方法上，该框架将高层次任务分解为结构化的子目标，在推理时实现分层规划，在训练时提供更密集的反馈。实验结果表明，该框架显著提升了智能体的长视野能力：实时规划机制使Gemini等专有模型在WebArena-Lite基准上的成功率绝对提升约10%；将MiRA应用于开源的Gemma3-12B模型，其成功率从6.4%大幅提升至43.0%，超越了GPT-4-Turbo、GPT-4o以及之前的开源最优模型WebRL。论文结论表明，将显式的推理时规划与基于里程碑的奖励相结合，能显著增强智能体在复杂、长序列任务中的鲁棒性和推理能力，为构建更强大的通用自主系统开辟了道路。
