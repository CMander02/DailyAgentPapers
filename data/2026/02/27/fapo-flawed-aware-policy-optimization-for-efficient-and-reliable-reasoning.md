---
title: "FAPO: Flawed-Aware Policy Optimization for Efficient and Reliable Reasoning"
authors:
  - "Yuyang Ding"
  - "Chi Zhang"
  - "Juntao Li"
  - "Haibin Lin"
  - "Min Zhang"
date: "2025-10-26"
arxiv_id: "2510.22543"
arxiv_url: "https://arxiv.org/abs/2510.22543"
pdf_url: "https://arxiv.org/pdf/2510.22543v2"
categories:
  - "cs.LG"
tags:
  - "Reasoning & Planning"
  - "Learning & Optimization"
relevance_score: 7.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Learning & Optimization"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "Flawed-Aware Policy Optimization (FAPO)"
  primary_benchmark: "N/A"
---

# FAPO: Flawed-Aware Policy Optimization for Efficient and Reliable Reasoning

## 原始摘要

Reinforcement learning with verifiable rewards (RLVR) has emerged as a promising paradigm for enhancing the reasoning capabilities of large language models (LLMs). In this context, models explore reasoning trajectories and exploit rollouts with correct answers as positive signals for policy optimization. However, these rollouts might involve flawed patterns such as answer-guessing and jump-in-reasoning. Such flawed-positive rollouts are rewarded identically to fully correct ones, causing policy models to internalize these unreliable reasoning patterns. In this work, we first conduct a systematic study of flawed-positive rollouts in RL and find that they enable rapid capability gains during the early optimization stage, while constraining reasoning capability later by reinforcing unreliable patterns. Building on these insights, we propose Flawed-Aware Policy Optimization (FAPO), which presents a parameter-free reward penalty for flawed-positive rollouts, enabling the policy to leverage them as useful shortcuts in the warm-up stage, securing stable early gains, while gradually shifting optimization toward reliable reasoning in the later refinement stage. To accurately and comprehensively detect flawed-positive rollouts, we introduce a generative reward model (GenRM) with a process-level reward that precisely localizes reasoning errors. Experiments show that FAPO is effective in broad domains, improving outcome correctness, process reliability, and training stability without increasing the token budget.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于可验证奖励的强化学习（RLVR）中，因奖励信号粗糙而导致的推理模式不可靠问题。研究背景是，当前利用RLVR提升大语言模型（LLM）推理能力已成为重要范式，模型通过探索推理轨迹，并利用最终答案正确的轨迹（rollouts）作为正向信号进行策略优化。然而，现有基于规则的结果奖励（如仅根据最终答案正确与否给出二元奖励）存在根本不足：它将含有缺陷但答案正确的轨迹（例如通过答案猜测、跳跃式推理等“捷径”得出正确答案）与完全正确的轨迹同等奖励，导致策略模型在优化过程中内化并强化这些不可靠的推理模式，损害了推理过程的可靠性。

本文的核心问题是：如何有效管理训练过程中这些“缺陷正向”（flawed-positive）轨迹的影响，以实现既高效又可靠的推理能力提升。具体而言，论文试图解决两个关键问题：一是系统分析缺陷正向轨迹在RL训练全过程中的分布与影响；二是设计有效的缓解策略，使模型既能利用这些轨迹在训练初期快速获得能力增益，又能在后期转向学习可靠、稳健的推理模式。为此，论文提出了缺陷感知策略优化（FAPO）方法，其核心是为缺陷正向轨迹引入一种无参数的奖励惩罚机制，并配合一个能精确定位推理过程错误的生成式奖励模型（GenRM），从而引导模型在训练初期将缺陷正向轨迹作为有用的“垫脚石”，而在后期优化阶段逐渐聚焦于可靠的推理，最终提升结果正确性、过程可靠性和训练稳定性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类。在方法类中，强化学习（RL）被广泛用于提升大语言模型（LLM）的推理能力，特别是在可验证奖励（RLVR）的范式下，模型通过探索推理轨迹并利用正确答案的rollout进行策略优化。然而，现有方法通常将包含错误推理模式（如猜测答案、跳跃推理）的“有缺陷正例”与完全正确的rollout同等奖励，导致策略内化不可靠模式。本文提出的FAPO算法通过引入对缺陷正例的无参数奖励惩罚，与此类工作形成区别，旨在早期利用缺陷正例作为捷径获得稳定收益，后期则转向优化可靠推理。

在应用类中，奖励模型的研究分为生成式奖励模型（GenRM）和判别式奖励模型（DisRM）。现有GenRM主要作为灵活验证器，在规则无法可靠评估正确性时补充规则系统；DisRM则提供细粒度密集奖励（如令牌级、步骤级），但易受奖励破解影响，导致策略利用虚假捷径。本文引入具有过程级奖励的GenRM来精确检测缺陷正例，提供细致可解释的奖励，从而增强鲁棒性和可扩展性，与现有奖励模型工作形成互补。

### Q3: 论文如何解决这个问题？

论文通过提出“缺陷感知策略优化”（FAPO）框架来解决强化学习中“缺陷正样本”对策略模型产生误导的问题。其核心方法是设计一个两阶段的优化过程，在早期热身阶段利用缺陷正样本作为有效捷径快速提升能力，在后期精炼阶段则通过惩罚机制将优化方向转向可靠推理。整体架构包含两个关键模块：一个用于精确检测缺陷正样本的生成式奖励模型（GenRM），以及一个动态调整优势估计的自适应学习算法。

首先，为了准确识别缺陷正样本，论文没有直接使用计算成本高昂的大型语言模型，而是通过强化学习训练一个紧凑的生成式奖励模型。该模型的奖励设计包含两部分：基于预测是否与真实标签一致的结果奖励（R_Outcome），以及一个细粒度的过程奖励（R_Process）。过程奖励专门针对被判定为缺陷正样本的情况，根据模型预测的错误步骤位置与真实错误位置之间的差距施加惩罚，差距越小惩罚越轻。这种设计迫使模型学习真正的错误定位能力，而非仅仅猜测标签，从而提升了检测的精确性。奖励机制还能自然实现训练重点的过渡：早期优化主要受结果奖励驱动以快速提升正确率，后期随着正确率饱和，过程优化逐渐占据主导。

其次，在策略优化层面，FAPO引入了一个基于组相对优势估计的奖励惩罚机制。对于被GenRM判定为缺陷正样本的轨迹，在其基础奖励上叠加一个固定的惩罚项（-λ）。优势值则通过计算单个奖励相对于其所属样本组（例如同一批次的多个轨迹）平均奖励的标准化差值来估计。这种组相对优势估计能动态反映学习进度。理论分析表明，当正样本比例与负样本比例之比ρ达到特定阈值（与λ相关）时，优化会自动从热身阶段切换到精炼阶段。论文采用多数引导策略，默认设置λ=1，使得当正样本开始主导时（ρ>1），优化自然转向抑制缺陷模式并提升可靠性。此外，随着优化继续，优势估计会对正样本进行缩放，从而稳定训练过程。

创新点主要体现在：1）系统研究了缺陷正样本在强化学习不同阶段的双重影响，并据此提出了阶段自适应的优化范式；2）设计了结合结果与过程奖励的生成式奖励模型，实现了对推理错误的精确定位，避免了现有模型存在的“过度批评”问题；3）提出了无需额外超参数控制的、基于组相对优势估计的动态惩罚机制，使优化过程能根据学习进度自动、平稳地切换焦点。该方法在不增加计算令牌预算的前提下，有效提升了最终答案的正确性、推理过程的可靠性和训练稳定性。

### Q4: 论文做了哪些实验？

实验设置方面，论文以Qwen2.5-Math-7B和Qwen2.5-32B为策略模型，采用GRPO（结合clip-higher、token-level loss和overlong reward shaping）作为基线RLVR方法，并使用verl框架进行训练。FAPO方法的核心是引入一个生成式奖励模型（GenRM）来检测并惩罚有缺陷的正向轨迹（flawed-positive rollouts）。为了训练GenRM，作者构建了FAPO-Critic-85K数据集，该数据集基于DAPO-Math-17K的问题，使用LLaMA和Qwen系列模型（7B至70B）生成回答，并由Qwen3-32B标注首个错误步骤的位置，最终用于训练Qwen3-4B-Instruct模型。在推理评估中，训练好的FAPO-GenRM-4B通过远程API集成到RL训练中，采用异步架构以提高效率。

数据集和基准测试包括：用于评估GenRM检测能力的FlawedPositiveBench和ProcessBench；以及用于评估最终推理性能的AIME24（数学）、AIME25（数学）和GPQA-Diamond（通用领域）基准。

对比方法包括：作为基线的GRPO（基于结果的奖励）；以及在GenRM评估中对比的多个最先进的判别式和生成式模型。

主要结果和关键指标如下：
1.  **FAPO-GenRM性能**：在FlawedPositiveBench和ProcessBench上，FAPO-GenRM显著优于基线模型，甚至超过了其教师模型Qwen3-32B，证明了其缺陷检测的有效性。
2.  **FAPO-Reasoning性能**：
    *   **结果正确性**：在数学和通用领域任务上，FAPO在所有基准测试中均持续优于基线方法。
    *   **过程可靠性**：FAPO生成的回答中有缺陷的正向轨迹比例显著降低。通过Qwen3-32B评判和人工验证均证实了这一点。
    *   **训练稳定性**：FAPO的学习曲线更平滑，在训练后期未出现明显的性能下降，而基线方法则存在此问题。
    *   **令牌预算**：FAPO的性能提升不依赖于生成长度更长的回答，实现了更高效的推理。
3.  **消融实验**：实验表明，更强的缺陷检测能力（GenRM）直接转化为最终RL性能的提升。同时，FAPO在训练早期能利用自我修正机制，但在后期会逐渐转向优先使用完全正确的轨迹，从而获得更短、更高效的推理路径。此外，研究还发现，简单的基于步骤正确比例的奖励设计会导致奖励黑客问题（模型跳过不确定步骤），而FAPO的设计避免了这一问题。
4.  **训练效率**：通过异步架构等基础设施优化，FAPO相较于基线的训练时间增加少于20%，使其在大规模RL训练中具备可行性。

### Q5: 有什么可以进一步探索的点？

本文提出的FAPO方法虽能有效识别并惩罚“有缺陷的正向样本”，但仍存在若干局限和可拓展方向。首先，其核心依赖的生成式奖励模型（GenRM）在复杂推理任务中可能面临“奖励黑客”问题，即策略模型可能学会利用奖励信号的漏洞（如只输出高置信度步骤）而非真正提升推理可靠性，未来需设计更鲁棒的奖励机制来抵御此类策略性操纵。其次，当前系统采用异步架构来提升效率，但完全同步的设计可能进一步优化资源利用率，这值得在系统工程层面深入探索。此外，FAPO主要针对数学和通用领域任务验证，未来可扩展到代码生成、科学推理等更复杂领域，检验其泛化能力。另一个有趣的方向是探索“有缺陷样本”的动态定义——随着模型能力演进，早期有益的捷径可能后期变成缺陷，可研究自适应惩罚机制。最后，可将FAPO与思维链自洽性检查、多智能体辩论等范式结合，构建更全面的可靠推理框架。

### Q6: 总结一下论文的主要内容

本文针对强化学习与可验证奖励（RLVR）范式中存在的“缺陷正样本”问题展开研究。这些样本虽能得出正确答案，但推理过程存在猜测答案或跳跃推理等不可靠模式，传统方法将其与完全正确的样本等同奖励，导致模型内化了不可靠的推理模式。论文首先系统分析了缺陷正样本的作用，发现其在优化早期能快速提升能力，但在后期会因强化错误模式而限制推理能力。

基于此，作者提出了缺陷感知策略优化（FAPO）方法。其核心贡献是一种无需超参数的奖励惩罚机制，使策略在训练初期能将缺陷正样本作为有效捷径以稳定获取早期收益，而在后期优化阶段逐渐转向学习可靠的推理模式。为了精准检测缺陷正样本，论文还引入了一个生成式奖励模型（GenRM），该模型提供过程级奖励信号以准确定位推理错误。

实验表明，FAPO能有效提升多个领域的结果正确性、过程可靠性和训练稳定性，且不增加计算开销。该方法为大规模强化学习系统提供了一种高效可靠的优化途径。
