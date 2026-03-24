---
title: "Demystifying Reinforcement Learning for Long-Horizon Tool-Using Agents: A Comprehensive Recipe"
authors:
  - "Xixi Wu"
  - "Qianguo Sun"
  - "Ruiyang Zhang"
  - "Chao Song"
  - "Junlong Wu"
  - "Yiyan Qi"
  - "Hong Cheng"
date: "2026-03-23"
arxiv_id: "2603.21972"
arxiv_url: "https://arxiv.org/abs/2603.21972"
pdf_url: "https://arxiv.org/pdf/2603.21972v1"
github_url: "https://github.com/WxxShirley/Agent-STAR"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "强化学习"
  - "工具使用"
  - "长程规划"
  - "智能体训练"
  - "实证研究"
  - "配方研究"
  - "TravelPlanner"
relevance_score: 9.0
---

# Demystifying Reinforcement Learning for Long-Horizon Tool-Using Agents: A Comprehensive Recipe

## 原始摘要

Reinforcement Learning (RL) is essential for evolving Large Language Models (LLMs) into autonomous agents capable of long-horizon planning, yet a practical recipe for scaling RL in complex, multi-turn environments remains elusive. This paper presents a systematic empirical study using TravelPlanner, a challenging testbed requiring tool orchestration to satisfy multifaceted constraints. We decompose the agentic RL design space along 5 axes: reward shaping, model scaling, data composition, algorithm selection, and environmental stability. Our controlled experiments yield 7 key takeaways, e.g., (1) reward and algorithm choices are scale-dependent as smaller models benefit from staged rewards and enhanced exploration, whereas larger models converge efficiently with simpler dense rewards, (2) ~ 1K training samples with a balanced difficulty mixture mark a sweet spot for both in-domain and out-of-domain performance, and (3) environmental stability is critical to prevent policy degradation. Based on our distilled recipe, our RL-trained models achieve state-of-the-art performance on TravelPlanner, significantly outperforming leading LLMs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何将强化学习（RL）有效应用于训练能够进行长视野规划、使用多种工具的自主智能体这一核心挑战。研究背景是，大型语言模型（LLM）正从静态文本生成器演变为能够推理、行动并与动态环境交互的通用自主智能体，这要求智能体具备长视野规划能力，即分解高级目标、协调工具使用并满足多方面约束。然而，现有方法存在明显不足：当前关于智能体强化学习的见解主要源于涉及单步推理或少量回合交互的短视野任务，而现实世界的工作流需要处理数十次工具调用和长轨迹。尽管近期研究引入了针对性算法（如修改探索策略或合成自适应环境），但它们通常只探索了强化学习设计空间的有限子集，缺乏对奖励塑造、数据构成、模型缩放、算法选择和环境稳定性等因素如何共同影响性能的整体性理解。因此，社区仍然缺乏一个在复杂、长视野智能体场景中扩展强化学习的全面且实用的方案。本文的核心问题正是要填补这一空白，通过系统的实证研究，揭示在长视野工具使用智能体的训练中，如何协同优化上述多个设计维度，以制定出一个可扩展、高效的强化学习实用方案。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕长视野工具使用智能体的强化学习（RL）方法展开，可归类为方法类、应用类和评测类。

在**方法类**研究中，相关工作包括使用强化学习优化LLM智能体的各种技术，如PPO等算法、不同奖励函数设计（如稀疏与稠密奖励）、以及数据合成与课程学习策略。本文与这些工作的关系在于，它系统性地分解了智能体RL设计的五个关键维度（奖励塑造、模型缩放、数据构成、算法选择和环境稳定性），并进行了大规模控制实验。其区别在于，本文并非提出单一新算法，而是通过实证研究提供了一个可扩展的“配方”，揭示了这些设计选择之间的相互作用及其对模型规模的依赖性，例如发现较小模型受益于分阶段奖励和增强探索，而较大模型使用简单稠密奖励即可高效收敛。

在**应用类**研究中，许多工作致力于开发能够使用工具（如API）完成复杂任务的LLM智能体，常采用ReAct（推理-行动）等范式进行多轮交互。本文以TravelPlanner这一需要协调多种工具以满足多面性约束的长视野规划测试平台为基础，与此类应用研究一脉相承。其区别在于，本文聚焦于为这类复杂、多轮环境提供一个实用的、可扩展的RL训练框架，并深入研究了如何通过RL将LLM进化为自主智能体，而不仅仅是应用现有范式。

在**评测类**研究中，相关工作涉及构建复杂的基准测试来评估智能体的长视野规划和工具使用能力。本文使用的TravelPlanner测试平台即属于此类，它要求智能体同时满足常识规则和硬性约束。本文与此类工作的关系是直接采用了该评测环境。其区别在于，本文的重点并非提出新的评测基准，而是利用该测试平台作为实验场，系统研究RL训练方法如何提升智能体在此类挑战性任务上的性能，并最终实现了在该测试平台上的最先进性能。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为STAR的、用于长视野工具使用智能体的统一后训练框架来解决强化学习在复杂多轮环境中的规模化应用难题。该框架包含三个顺序阶段：数据合成、监督微调（SFT）和强化学习（RL），并围绕五个设计维度（奖励塑造、模型缩放、数据构成、算法选择和环境稳定性）进行了系统性的实证探索。

**整体框架与主要模块**：
1.  **数据合成**：针对训练数据稀缺问题，设计了一个合成流程来生成具有可控难度的TravelPlanner风格查询。首先从沙盒中采样并验证原子旅行元素（如出发地、目的地、日期）的可行性，确保存在真实解。然后利用这些已验证的约束和动态估算的预算，通过回译方法使用开源模型生成自然语言查询。通过调整约束的数量和类型，将查询分为易、中、难三个难度等级，实现了对数据难度的精细控制。
2.  **监督微调（SFT）**：为缓解冷启动问题并让策略获得基本的任务理解，在RL之前进行SFT。采用拒绝采样的方式：选择一个强大的教师模型对合成查询进行ReAct推理，仅保留在评估协议下达到“成功”的轨迹。这些高质量轨迹作为SFT的黄金监督数据，为所有规模的模型生成任务专用的初始检查点。
3.  **强化学习（RL）**：这是框架的核心，智能体通过环境反馈优化长视野规划。基于rLLM框架，实现了一系列从稠密到稀疏的奖励信号：`Sum`（聚合所有子指标的稠密奖励）、`Macro`（关注宏观约束满足的半稀疏奖励）、`Success`（纯粹稀疏的二元成功奖励）以及`Curriculum`（从`Sum`奖励逐步过渡到`Success`奖励的分阶段课程奖励）。优化算法主要采用GRPO，通过对旧策略采样一组轨迹，最大化经过裁剪和优势归一化处理的替代优势目标。此外，框架被扩展为一个模块化设置，可以灵活地改变数据、奖励、算法和环境动态，以支持系统的设计空间探索。

**创新点与关键技术**：
*   **系统化的设计空间分解与实证**：将智能体RL设计空间明确分解为五个关键轴，并通过受控实验得出可操作的结论（如奖励与算法的选择依赖于模型规模，小模型受益于分阶段奖励和增强探索，而大模型使用简单稠密奖励即可高效收敛）。
*   **可控难度的数据合成与课程学习**：创新的数据合成方法不仅能生成高质量数据，还能精确控制其难度，为后续训练和评估提供了基础。在RL阶段引入的`Curriculum`奖励，是一种内在的课程学习机制，有助于引导智能体（尤其是小模型）的探索。
*   **模块化与可扩展的RL框架**：将rLLM扩展为模块化设置，使得能够独立且灵活地研究各个设计维度（如奖励函数、数据混合）的影响，这为理解和优化长视野智能体的RL训练提供了强大的实验工具。
*   **基于实证的配方**：最终提炼出的“配方”指出，约1K个难度均衡的训练样本是一个性能甜点，且环境稳定性对于防止策略退化至关重要。应用该配方训练的RL模型在TravelPlanner上取得了最先进的性能。

### Q4: 论文做了哪些实验？

论文实验围绕五个核心设计维度展开：奖励设计、模型规模、数据构成、算法选择和环境稳定性，在TravelPlanner测试平台上进行了系统性的对照研究。

**实验设置与数据集**：研究基于三阶段STAR流程（合成、监督微调、强化学习）构建实验环境。使用GPT-OSS-120B和DeepSeek-V3.2-Exp等模型合成了超过10K条查询，并从中筛选出1,198条高质量轨迹（平均10.3K tokens，9.2次工具调用）用于对Qwen2.5-Instruct系列模型进行监督微调（SFT）。强化学习阶段默认采用改进的GRPO算法，使用1K条与SFT无重叠的合成查询进行训练，难度比例为简单:中等:困难=4:3:3，训练5个epoch。主要评估包括在1,000个实例的TravelPlanner测试集上的领域内性能，以及在7个知识密集型QA基准（如NQ、TriviaQA、HotpotQA等）上的领域外泛化能力。

**对比方法与主要结果**：
1.  **奖励设计**：对比了密集奖励（Sum）、半稀疏奖励（Macro）、稀疏奖励（Success）和课程奖励（Curriculum）。关键发现是奖励选择与模型规模相关：较小模型（如1.5B）受益于分阶段引导的Curriculum奖励，而较大模型（如7B）能有效利用密集的Sum奖励。但过于密集的奖励会导致领域外泛化能力下降（对齐税），Macro奖励在领域内性能和泛化间取得了最佳平衡。
2.  **模型规模**：比较了1.5B、3B和7B模型。结果表明，扩大模型规模能持续提升性能，但增益幅度因奖励设计而异。例如，使用Sum奖励时，成功率从1.5B的33.1%提升到7B的62.8%。
3.  **数据构成**：研究了数据数量和质量。发现RL数据存在一个“甜点”：1K训练样本在领域内成功率和领域外泛化上达到最佳平衡（如3B模型，Curriculum奖励下领域内成功率49.9%，平均领域外得分35.0%）。超过此数量（如2K）会导致泛化能力下降。在难度上，混合难度（4:3:3）的数据构成能同时学习基本常识和复杂约束，取得最高成功率。
4.  **算法选择**：对比了GRPO、DAPO和ARPO。结果显示，标准GRPO在大多数情况下已达到最佳或接近最佳性能，且训练效率最高（GPU耗时更少），表明对于长视野任务，复杂的探索机制并非必需。
5.  **环境稳定性**：通过严格的协议执行（格式错误奖励为0）和超长处理机制来确保，这是防止策略退化的关键。

**关键数据指标**：在领域外泛化评估中，RL训练模型在多个基准上达到或超越了领域专用基线Search-R1。例如，3B模型在Curriculum奖励下，在NQ、TriviaQA、PopQA、HotpotQA、2Wiki、Musique、Bamboogle上的准确率分别为41.0%、56.8%、36.2%、39.5%、27.7%、12.4%、32.0%，平均35.0%。最终，基于提炼出的方案，RL训练模型在TravelPlanner上取得了最先进的性能。

### Q5: 有什么可以进一步探索的点？

基于论文结论部分指出的局限性，未来研究可从以下几个方向深入探索。首先，需将模拟环境验证迁移至真实世界，以评估智能体在开放、动态场景中的实际泛化与鲁棒性。其次，当前OOD评估局限于知识密集型问答任务，未来应拓展至跨领域、多模态任务，全面检验智能体的泛化能力。再者，研究需突破计算限制，探索千亿参数以上大模型对“规模感知配方”的响应规律，可能揭示新的缩放定律。此外，论文采用单因素分析法，未来应系统研究奖励设计、数据构成、算法选择等多维度因素的复杂交互效应，并开发任务无关、细粒度（如步级）的奖励机制，以更有效解决长视野任务中的稀疏奖励问题。最后，可探索将强化学习与模仿学习、课程学习等范式结合，进一步提升训练效率与策略稳定性。

### Q6: 总结一下论文的主要内容

本文通过系统性的实证研究，旨在为使用工具的长视野智能体提供强化学习（RL）的实用设计指南。研究以TravelPlanner为测试平台，将智能体RL设计空间分解为五个维度：奖励塑造、模型缩放、数据构成、算法选择和环境稳定性。核心发现包括：奖励与算法选择具有规模依赖性，较小模型受益于分阶段课程奖励和增强探索，而较大模型使用简单稠密奖励即可高效收敛；约1000个训练样本且难度混合平衡是取得领域内及领域外泛化性能的最佳数据量；环境稳定性对防止策略退化至关重要。基于此配方训练的模型在TravelPlanner上取得了最先进的性能，显著超越了主流大型语言模型。这项工作为训练长视野智能体提供了可操作的指导，并指出了模拟环境局限、跨领域泛化评估不足等未来研究方向。
