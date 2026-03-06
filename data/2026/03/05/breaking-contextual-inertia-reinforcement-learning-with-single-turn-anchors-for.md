---
title: "Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction"
authors:
  - "Xingwu Chen"
  - "Zhanqiu Zhang"
  - "Yiwen Guo"
  - "Difan Zou"
date: "2026-03-05"
arxiv_id: "2603.04783"
arxiv_url: "https://arxiv.org/abs/2603.04783"
pdf_url: "https://arxiv.org/pdf/2603.04783v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent 推理"
  - "Agent 规划"
  - "Agentic 强化学习"
  - "多轮交互"
  - "LLM 训练方法"
relevance_score: 8.0
---

# Breaking Contextual Inertia: Reinforcement Learning with Single-Turn Anchors for Stable Multi-Turn Interaction

## 原始摘要

While LLMs demonstrate strong reasoning capabilities when provided with full information in a single turn, they exhibit substantial vulnerability in multi-turn interactions. Specifically, when information is revealed incrementally or requires updates, models frequently fail to integrate new constraints, leading to a collapse in performance compared to their single-turn baselines. We term the root cause as \emph{Contextual Inertia}: a phenomenon where models rigidly adhere to previous reasoning traces. Even when users explicitly provide corrections or new data in later turns, the model ignores them, preferring to maintain consistency with its previous (incorrect) reasoning path. To address this, we introduce \textbf{R}einforcement \textbf{L}earning with \textbf{S}ingle-\textbf{T}urn \textbf{A}nchors (\textbf{RLSTA}), a generalizable training approach designed to stabilize multi-turn interaction across diverse scenarios and domains. RLSTA leverages the model's superior single-turn capabilities as stable internal anchors to provide reward signals. By aligning multi-turn responses with these anchors, RLSTA empowers models to break contextual inertia and self-calibrate their reasoning based on the latest information. Experiments show that RLSTA significantly outperforms standard fine-tuning and abstention-based methods. Notably, our method exhibits strong cross-domain generalization (e.g., math to code) and proves effective even without external verifiers, highlighting its potential for general-domain applications.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在多轮交互中表现显著劣于单轮场景的核心问题，即模型难以有效整合和更新增量信息或修正信息，导致性能下降。研究背景是，尽管LLMs在单轮完整信息下展现出强大的推理能力，但在实际应用中，多轮交互已成为人机交互的普遍范式，用户经常会在对话中逐步提供新条件或纠正先前要求。现有方法主要存在两点不足：一是直接微调等策略虽能提升一般指令遵循能力，但严重依赖外部监督，并未触及模型内部失效的根本机制；二是基于主动弃权或澄清请求的行为策略，虽能减少因信息不足导致的错误累积，但无法适用于需要动态状态更新的场景（如纠正初始错误）。本文识别并量化了问题的根本原因，称之为“上下文惯性”，即模型在多轮对话中会僵化地固守先前生成的推理轨迹，即使后续信息已明确否定或修正了这些轨迹。因此，本文要解决的核心问题是：如何打破这种上下文惯性，使模型能够基于最新信息自我校准推理，从而实现稳定、通用的多轮交互能力。为此，论文提出了RLSTA方法，利用模型自身优越的单轮能力作为稳定的内部锚点来提供奖励信号，从而引导多轮生成。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：多轮交互中的LLM脆弱性研究，以及针对多轮交互的优化方法研究。

在多轮交互脆弱性研究方面，相关工作揭示了LLM在信息逐步揭示或需要更新的对话中性能显著下降的现象。例如，MT-Eval基准测试发现性能平均下降15%，而更复杂的“对话中迷失”（LiC）设定中性能下降高达39%。这些研究将问题归因于模型在早期回合的过早回答尝试。本文在此基础上，不仅研究了信息增量添加（MT-Add）场景，还探讨了用户修正初始错误条件（MT-Refine）的场景，从而更全面地揭示了“上下文惯性”这一根本原因。

在优化方法研究方面，现有工作主要沿两个方向展开。一是直接采用各种微调方法，如监督微调（SFT）、直接偏好优化（DPO）和强化学习（RL）。然而，这些方法（如MT-PPO和SWEET-RL）通常依赖昂贵且精心设计的回合级奖励信号，并未从根本上纠正模型的内在故障模式。二是探索针对特定场景的行为策略，例如在信息不足时鼓励模型提出澄清请求或主动弃权。但这些策略无法适用于需要状态更新的场景（如MT-Refine），因为模型必须先生成初始响应再予以修正，而非保持沉默。

本文提出的RLSTA方法与上述工作均有显著区别。它不依赖外部设计的回合级奖励或特定的行为约束，而是创新性地利用模型本身强大的单轮能力作为稳定的内部锚点来提供奖励信号，引导模型在多轮交互中自我校准，从而打破了上下文惯性，实现了更好的泛化性和实用性。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为“带单轮锚点的强化学习”（RLSTA）的创新训练方法来解决多轮交互中的“上下文惯性”问题。该方法的核心思想是利用模型在单轮完整信息下表现出的卓越能力作为内部锚点，来校准和稳定多轮对话中的推理过程。

整体框架基于强化学习（采用GRPO算法），并包含两个关键模块。首先是**潜在能力过滤**模块：该方法并非使用所有多轮对话数据进行训练，而是通过筛选构建一个专用数据集。具体而言，它只保留那些模型在拥有全部信息的单轮指令（`i^{full}`）下能够正确解决问题，但在原始多轮对话历史（`H`）下却出错的对话实例。这一过滤确保了用于训练的锚点（即单轮能力）是可靠且优于多轮表现的，从而聚焦于真正由上下文惯性导致性能下降的场景。

其次是**基于锚点的奖励机制**，这是方法的核心创新点。在强化学习训练中，除了基于结果正确性的验证奖励（`R_v`）外，RLSTA引入了**单轮锚点奖励（`R_s`）**。该奖励的计算方式是：将多轮对话最终生成的回答（`m_n`），输入到原始基础模型（`π_θ_ref`）中，评估其在合并了所有信息的单轮指令（`i^{full`）下的对数似然概率，并进行长度归一化。`R_s` 量化了多轮响应与模型自身在理想单轮设置下所应生成内容的一致性程度。最终的总奖励 `R` 是验证奖励 `R_v` 和锚点奖励 `R_s` 的加权和。

通过这种设计，RLSTA创造了一个自我校准的循环：在训练过程中，模型被鼓励生成那些不仅结果正确（`R_v`高），而且其推理路径与自身在完整信息下的“最佳表现”相吻合（`R_s`高）的回应。这有效地将模型的生成过程从有偏差的多轮历史上下文（可能包含早期错误）中“拉回”，锚定到更可靠的单轮推理路径上，从而主动打破了对过时推理轨迹的僵化坚持（即上下文惯性）。该方法不依赖外部验证器或被动的弃权策略，而是直接针对问题的根本原因进行优化，并展现出良好的跨领域泛化能力。

### Q4: 论文做了哪些实验？

论文实验设置主要围绕评估RLSTA方法在克服多轮交互中“上下文惯性”问题的有效性。实验使用了多个开源模型，包括Qwen2.5-3B/7B-Instruct、Qwen3-4B-Instruct-2507和Llama-3.2-3B-Instruct。训练数据基于GSM8K数学数据集，通过GPT-4o将单轮查询分解为顺序指令来构建多轮样本。评估则采用了多轮基准测试，并模拟了两种交互模式：MT-Add（逐步添加新约束）和MT-Refine（模拟错误纠正）。代码和摘要任务主要在MT-Add设置下评估。

对比方法包括标准监督微调（SFT）、直接偏好优化（DPO）、原始GRPO，以及不确定性处理策略RLAAR和CollabLLM。主要结果如下：RLSTA在多个模型和任务上显著优于基线方法。例如，在Qwen2.5-7B-Instruct的MT-Add数学任务中，RLSTA达到0.857，高于SFT的0.740、DPO的0.633和GRPO的0.803；在代码任务中，RLSTA为0.350，也优于其他方法。关键指标包括准确率（如数学任务0.857）和LiC Score（多轮与单轮性能比，RLSTA在数学任务达1.001）。此外，RLSTA展现出强大的跨领域泛化能力（如从数学到代码），且无需外部验证器也能有效工作，同时保持了模型的长上下文处理能力（如在摘要任务中覆盖分数提升）。与RLAAR和CollabLLM相比，RLSTA在多数任务上性能相当或更优，且不依赖被动弃权，适用于更广泛场景。

### Q5: 有什么可以进一步探索的点？

该论文提出的RLSTA方法虽然有效，但其局限性也为未来研究提供了明确方向。首先，方法效能受限于模型单轮能力，若模型本身缺乏解决特定问题的潜在知识，则锚点失效。未来可探索如何为知识不足的领域构建更鲁棒的监督信号，例如结合外部知识库或跨模型协同。其次，当前框架处于被动交互模式，未涵盖需要模型主动澄清的场景。可引入强化学习中的主动学习机制，训练模型学会在信息不足时发起询问，形成双向交互闭环。再者，论文提到尚未整合元认知决策能力，这是一个关键方向。未来可设计分层策略网络，使模型能动态评估上下文充分性，自主选择继续推理、请求澄清或暂时弃权，从而在复杂多轮对话中实现更智能的适应性。此外，RLSTA的跨领域泛化能力虽已验证，但如何将其与持续学习结合，使模型在长期交互中不断更新锚点知识库，避免性能衰减，也值得深入探索。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型在多轮交互中表现脆弱的问题，提出了“情境惯性”的概念，即模型倾向于僵化地遵循早期推理路径而忽视后续的新信息或修正。为解决此问题，作者提出了RLSTA方法，其核心是利用模型本身在单轮任务中表现出的优异能力作为稳定的内部锚点，通过强化学习对齐多轮响应与这些锚点，从而引导模型根据最新信息进行自我校准。实验表明，该方法在信息增量与修正两种多轮场景中均显著提升了稳定性，超越了标准微调和基于弃权的方法，并展现出强大的跨领域泛化能力和数据效率。这一框架为构建更可靠、自适应的通用多轮交互系统提供了有效途径。
