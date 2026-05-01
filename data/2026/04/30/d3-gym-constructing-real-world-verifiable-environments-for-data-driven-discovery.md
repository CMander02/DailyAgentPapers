---
title: "D3-Gym: Constructing Real-World Verifiable Environments for Data-Driven Discovery"
authors:
  - "Hanane Nour Moussa"
  - "Yifei Li"
  - "Zhuoyang Li"
  - "Yankai Yang"
  - "Cheng Tang"
  - "Tianshu Zhang"
  - "Nesreen K. Ahmed"
  - "Ali Payani"
  - "Ziru Chen"
  - "Huan Sun"
date: "2026-04-30"
arxiv_id: "2604.27977"
arxiv_url: "https://arxiv.org/abs/2604.27977"
pdf_url: "https://arxiv.org/pdf/2604.27977v1"
github_url: "https://github.com/OSU-NLP-Group/D3-Gym"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "科学发现Agent"
  - "可验证环境"
  - "合成数据"
  - "Agent训练"
  - "代码Agent"
  - "数据驱动发现"
  - "自动评估"
relevance_score: 9.5
---

# D3-Gym: Constructing Real-World Verifiable Environments for Data-Driven Discovery

## 原始摘要

Despite recent progress in language models and agents for scientific data-driven discovery, further advancing their capabilities is held back by the absence of verifiable environments representing real-world scientific tasks.To fill this gap, we introduce D3-Gym, the first automatically constructed dataset with verifiable environments for scientific Data-Driven Discovery. D3-Gym comprises (1) 565 tasks sourced from 239 real scientific repositories across four disciplines where (2) each task is equipped with a natural language instruction, an executable environment with pre-installed dependencies, input dataset and artifact previews, a reference code solution, and an automatically synthesized evaluation script. Rigorous evaluation of the quality of the verification signal in D3-Gym confirms that our evaluation scripts achieve 87.5% agreement with human-annotated gold standards and strong alignment in domain-specific evaluation logic, showing their scientific soundness. Further, training on trajectories sampled from D3-Gym yields consistent and substantial gains across Qwen3 models of varying sizes on ScienceAgentBench, boosting Qwen3-32B by 7.8 absolute points and substantially shrinking the gap with strong proprietary models. All D3-Gym artifacts (environments, creation workflow, trajectories, and models) can be found at https://github.com/OSU-NLP-Group/D3-Gym.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在科学数据驱动发现领域，缺乏可验证的真实世界任务环境的问题。尽管语言模型和智能体在科学文献综合、领域特定推理等方面取得了进展，但进一步推动其能力提升的关键瓶颈在于：现有的基础设施无法提供大规模、真实且可自动验证的编程环境。当前方法如Autoresearch虽然展示了可验证环境的价值，但每个任务环境都需要大量人工构建（包括任务指令、数据集、评估脚本等），难以扩展到数百甚至数千个任务。此外，科学任务与软件工程不同，科学仓库中通常没有现成的单元测试，且科学程序的输出具有领域特异性，无法用通用标准评估正确性。为填补这一空白，本文提出了D3-Gym——首个自动构建的可验证环境数据集，包含565个任务，覆盖生物信息学、计算化学、地理信息科学和心理学/认知神经科学四个学科。其核心创新在于：通过自动化pipeline从真实科学仓库中筛选高质量任务，并利用LLM分两阶段（先编写评估计划，再转换为可执行脚本）自动合成领域特异的评估脚本，从而实现任务环境的规模化构建，解决了依赖人工构建的瓶颈问题。

### Q2: 有哪些相关研究？

相关研究可分为三类：**评测基准类**、**环境构建类**和**训练增强类**。在评测基准方面，ScienceAgentBench 是近期针对科学数据驱动代理的标准化评测，本文直接以其作为微调后的评估基准，并取得了显著的性能提升（如Qwen3-32B提升7.8分）。其他如Gao et al. (2024)等早期基准缺乏真实科学环境的可执行验证。本文与环境构建类研究（如SWE-bench、DS-1000）的区别在于：这些工作聚焦软件工程或代码生成，而D3-Gym首次系统性地从真实科学仓库（涵盖四个学科）自动构建可验证环境，且每个任务配有预装依赖的可运行环境和自动评估脚本。此外，与OpenHands、Agentless等通用代理方法不同，本文专门定向于科学数据发现任务。在训练增强类工作中，传统方法多依赖人工标注轨迹或合成数据，而D3-Gym通过自动化的环境生成和质量验证（评估脚本与人工标注的87.5%一致率），提供高质量的训练数据，从而在跨模型规模上一致提升推理能力，有效缩小了与专有模型的差距。

### Q3: 论文如何解决这个问题？

D3-Gym通过一个四阶段自动构建流程解决缺乏真实科学可验证环境的问题。首先，利用AutoSDT从239个真实科学仓库中爬取任务，经过多步过滤得到候选任务，并排除与ScienceAgentBench重叠的数据。其次，使用Claude Code进行过滤和数据集预览创建，仅保留参考代码使用原始真实数据文件的任务，并生成数据模式摘要（数据集预览）。第三，在隔离环境中执行参考解决方案，并用多模态LLM-as-judge验证输出是否完整且有意义的，丢弃失败任务。核心创新在于第四阶段：自动生成高质量评估脚本。采用“规划-编码”两阶段方法：首先，让Claude Sonnet 4.5基于任务指令、数据集预览和验证输出，制定详细的评估计划，明确检查哪些输出工件、使用哪些科学合适的指标（如准确率、容差）、以及接受标准（如阈值）。然后，该计划传递给同模型生成可执行评估脚本（称为“银标准脚本”）。这分离了高层科学推理与代码实现，确保评估脚本具有科学合理性。与人类标注的“金标准脚本”对比，银脚本在通过/失败判定上达到87.5%准确率、66.1%召回率和91.0%特异性，在指标选择、阈值和工件评估方面得分约4.0（5分制），验证了其可靠性和科学合理性。

### Q4: 论文做了哪些实验？

论文进行了两部分核心实验。首先，验证D3-Gym环境的可靠性：(1) 采用239个真实科学仓库中的565个任务，覆盖四个学科，每个任务配有自然语言指令、可执行环境（含预装依赖）、输入数据/工件预览、参考代码及自动合成评估脚本；(2) 通过评估脚本与人类标注金标准的一致性测试，结果显示评估脚本达到了87.5%的一致率，且在领域特定评估逻辑上展现出强对齐性，证明了其科学合理性。其次，评估训练效果：(3) 利用D3-Gym采样的轨迹对Qwen3系列模型（不同规模）进行训练，在ScienceAgentBench基准上测试，对比方法包括未训练的原始Qwen3模型及强闭源模型；(4) 主要结果：训练后Qwen3-32B性能提升了7.8个绝对点，显著缩小了与强闭源模型（如GPT-4等）的差距，表明D3-Gym能有效提升模型在科学数据驱动发现任务上的能力。实验全面验证了环境质量与训练收益。

### Q5: 有什么可以进一步探索的点？

D3-Gym的局限性主要体现在三个方面。首先，其评估脚本与人工标注的87.5%一致性虽高，但仍有12.5%的偏差，这可能导致在科学严谨性要求极高的场景下产生错误反馈，未来可引入更细粒度的多轮验证机制，并结合领域专家知识进行脚本优化。其次，当前565个任务覆盖4个学科，但科学发现的广度和深度远不于此，后续应拓展到更多交叉学科（如计算化学与材料科学的结合）并增加任务复杂度，例如包含动态数据流或实时传感器输入的环境。最后，论文仅证明了训练后模型在ScienceAgentBench上的提升，未充分探讨泛化到完全陌生科学任务或跨领域迁移的能力。一个有趣的改进方向是利用D3-Gym的环境自动生成“元学习”任务，训练模型掌握“学会如何提出可验证假设”的核心技能，而非仅仅拟合现有代码解。此外，可尝试引入对抗性验证脚本，迫使模型产出更鲁棒的推理轨迹。

### Q6: 总结一下论文的主要内容

本文介绍D3-Gym，首个自动构建的包含可验证环境的科学数据驱动发现数据集。现有语言模型和智能体因缺乏真实科学任务的可验证环境而发展受限。D3-Gym从239个真实科学仓库中提取565个任务，覆盖生物信息学、计算化学、地理信息科学及心理学与认知神经科学四个领域。每个任务配备自然语言指令、预装依赖的可执行环境、输入数据集与预览、参考代码解决方案及自动合成的评估脚本。通过两阶段方法生成评估脚本：先编写详细评估计划，再转化为可执行代码。实验表明，合成评估脚本与人工标注的金标准在通过/失败判定上达到87.5%的一致性，验证了其科学合理性。基于D3-Gym采样的轨迹进行拒绝采样微调，显著提升了Qwen3系列模型在ScienceAgentBench上的性能，其中Qwen3-32B提升7.8个绝对百分点，大幅缩小了与强专有模型之间的差距。D3-Gym为在真实可验证环境中进行科学数据驱动发现的训练与评估提供了可扩展的基础设施。
