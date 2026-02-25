---
title: "QiMeng-CodeV-R1: Reasoning-Enhanced Verilog Generation"
authors:
  - "Yaoyu Zhu"
  - "Di Huang"
  - "Hanqi Lyu"
  - "Xiaoyun Zhang"
  - "Chongxiao Li"
  - "Wenxuan Shi"
  - "Yutong Wu"
  - "Jianan Mu"
  - "Jinghua Wang"
  - "Yang Zhao"
  - "Pengwei Jin"
  - "Shuyao Cheng"
  - "Shengwen Liang"
  - "Xishan Zhang"
  - "Rui Zhang"
  - "Zidong Du"
  - "Qi Guo"
  - "Xing Hu"
  - "Yunji Chen"
date: "2025-05-30"
arxiv_id: "2505.24183"
arxiv_url: "https://arxiv.org/abs/2505.24183"
pdf_url: "https://arxiv.org/pdf/2505.24183v5"
categories:
  - "cs.LG"
  - "cs.AR"
  - "cs.PL"
tags:
  - "强化学习"
  - "代码生成"
  - "数据合成"
  - "推理"
  - "工具使用"
  - "硬件描述语言"
  - "电子设计自动化"
relevance_score: 6.5
---

# QiMeng-CodeV-R1: Reasoning-Enhanced Verilog Generation

## 原始摘要

Large language models (LLMs) trained via reinforcement learning with verifiable reward (RLVR) have achieved breakthroughs on tasks with explicit, automatable verification, such as software programming and mathematical problems. Extending RLVR to electronic design automation (EDA), especially automatically generating hardware description languages (HDLs) like Verilog from natural-language (NL) specifications, however, poses three key challenges: the lack of automated and accurate verification environments, the scarcity of high-quality NL-code pairs, and the prohibitive computation cost of RLVR. To this end, we introduce CodeV-R1, an RLVR framework for training Verilog generation LLMs. First, we develop a rule-based testbench generator that performs robust equivalence checking against golden references. Second, we propose a round-trip data synthesis method that pairs open-source Verilog snippets with LLM-generated NL descriptions, verifies code-NL-code consistency via the generated testbench, and filters out inequivalent examples to yield a high-quality dataset. Third, we employ a two-stage "distill-then-RL" training pipeline: distillation for the cold start of reasoning abilities, followed by adaptive DAPO, our novel RLVR algorithm that can reduce training cost by adaptively adjusting sampling rate. The resulting model, CodeV-R1-7B, achieves 68.6% and 72.9% pass@1 on VerilogEval v2 and RTLLM v1.1, respectively, surpassing prior state-of-the-art by 12~20%, while even exceeding the performance of 671B DeepSeek-R1 on RTLLM. We have released our model, training code, and dataset to facilitate research in EDA and LLM communities.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决利用强化学习与可验证奖励（RLVR）训练大型语言模型（LLMs）来自动生成硬件描述语言（如Verilog）时所面临的三个核心挑战。研究背景是，RLVR在软件编程和数学问题等具有明确、自动化验证机制的任务上已取得突破，但在电子设计自动化（EDA）领域，特别是从自然语言（NL）规范生成Verilog代码的任务中，直接应用RLVR存在显著障碍。

现有方法的不足主要体现在三个方面：首先，缺乏自动化且准确的验证环境。硬件设计验证复杂，现有方法（如依赖LLMs生成测试用例）成本高且效果有限，难以处理时序电路的复杂状态和边界情况，导致错误率高。其次，高质量的自然语言-代码配对数据稀缺。硬件设计通常具有专有性，公开可用的标注数据极少，而现有基于LLM的数据合成方法往往产生低质量数据，无法满足RLVR的严格要求。最后，RLVR的训练计算成本极其高昂，大规模训练在时间和资源上难以承受。

因此，本文要解决的核心问题是：如何构建一个高效、可行的RLVR框架，以训练出能够从自然语言规范准确生成Verilog代码的推理增强型LLMs。具体而言，论文通过开发基于规则的测试平台生成器以实现鲁棒的等价性检查、提出“往返”数据合成方法以自动创建高质量NL-代码对、以及设计包含自适应采样策略的两阶段“蒸馏后强化学习”训练流程，来系统性应对上述验证、数据和成本三大挑战，最终实现高性能且训练成本可控的Verilog生成模型。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类。

在方法类方面，相关工作主要围绕基于强化学习的推理增强训练范式展开。例如，闭源的OO系列模型率先采用大规模强化学习结合思维链（CoT）来提升推理能力。受其启发，后续模型如QwQ、RR和Kimi k1.5等均采纳并改进了这一训练范式，取得了显著成果。本文提出的CodeV-R1框架与这些工作的核心关系在于，它同样采用了“强化学习与可验证奖励”（RLVR）这一高级范式来训练大语言模型。然而，本文的关键区别在于**将RLVR范式专门应用于电子设计自动化（EDA）领域**，特别是针对Verilog代码生成任务。这带来了独特的挑战，如缺乏自动化验证环境和高质量数据，因此本文创新性地开发了基于规则的测试平台生成器、往返数据合成方法以及自适应的DAPO算法来解决这些问题。

在应用类方面，相关工作主要集中于软件编程和数学问题等具有明确、可自动化验证的任务。本文则将应用范围扩展到了硬件描述语言（HDL）生成这一新领域，并针对其特点构建了专门的验证和训练流程。

### Q3: 论文如何解决这个问题？

论文通过一个名为CodeV-R1的强化学习可验证奖励（RLVR）框架来解决Verilog代码生成的三大挑战。其核心方法是一个包含五个阶段的“蒸馏-然后强化学习”两阶段训练流程，整体框架由自动化测试平台、高质量数据集构建和创新的强化学习算法构成。

首先，针对缺乏自动化验证环境的问题，论文设计了一个基于规则的测试平台生成器。该平台通过三个阶段进行功能验证：1）电路结构分析，使用Yosys提取参考代码的输入/输出端口、时钟和复位信号特征；2）仿真，对组合电路和时序电路分别进行随机输入模拟，其中时序电路采用双阶段验证（确定性复位测试和随机复位测试）；3）验证，通过计算错误率ε来量化生成代码与参考代码的输出等价性，实现高效准确的自动化验证。

其次，针对高质量数据稀缺的问题，论文提出了一种“往返”数据合成方法。该方法包含三个阶段：1）代码到自然语言（Code-to-NL），利用DeepSeek-V3为从GitHub收集的Verilog代码片段生成自然语言描述；2）自然语言到代码（NL-to-Code），使用DeepSeek-R1根据生成的描述重新生成“思考”过程和Verilog代码；3）通过上述测试平台进行等价性检查，筛选出与原始代码功能一致的对，形成高质量的训练数据集。这一过程在理论上被形式化为“自然语言-代码确定性等价”，确保了数据语义的一致性。

最后，针对RLVR计算成本高昂的问题，论文采用了分阶段训练策略并提出了自适应的DAPO算法。训练流程先进行监督微调（SFT）以启动模型的推理能力，得到蒸馏模型。随后，在强化学习阶段，论文创新性地改进了DAPO算法，引入了自适应批量大小机制。该机制通过动态估计采样有效比率，调整生成批量大小，避免了固定批量大小导致的采样不足或浪费，从而显著降低了训练成本。奖励函数则结合了格式正确性（需包含特定标签的推理和答案）和功能等价性验证。

主要创新点包括：1）构建了专用于Verilog的自动化、可扩展的等价性检查测试平台；2）提出了基于往返转换和严格过滤的高质量数据合成与筛选方法；3）设计了“蒸馏-然后强化学习”的两阶段流程，并开发了能降低采样成本的自适应DAPO算法。这些方法共同使得最终模型CodeV-R1-7B在多个基准测试上取得了显著超越现有技术的性能。

### Q4: 论文做了哪些实验？

论文的实验设置包括一个两阶段的“蒸馏-强化学习”训练流程。首先，使用LLaMAFactory对Qwen2.5-Coder-7B-Instruct模型在过滤后的蒸馏数据集上进行监督微调（SFT），共6个epoch，学习率为1e-5，批次大小为64，上下文长度为16384。随后，使用verl框架和自适应的DAPO算法对蒸馏模型进行强化学习（RL）训练，共300步，学习率为1e-6，批次大小为128，响应最大长度为16384。SFT阶段在8张A100-80G GPU上耗时约78小时，RL阶段在16张A100-80G GPU上耗时约127小时。

评估在多个Verilog基准测试上进行，包括VerilogEval v1/v2和RTLLM v1.1/v2。对于VerilogEval v2，测试了从规范到RTL的翻译和代码补全任务的零样本场景。生成时，蒸馏模型温度为0.6，RL模型温度为1.0，每个查询生成20个响应以计算pass@k分数。

对比方法包括基础模型（如GPT-4o、DeepSeek-R1-671B、Qwen2.5-Coder系列）和专用模型（如RTLCoder、BetterV、CodeV、CraftRTL）。主要结果如下：最终模型CodeV-R1-7B在VerilogEval v2的规范到RTL任务上达到68.8% pass@1，在代码补全任务上达到69.9% pass@1；在RTLLM v1.1上达到72.9% pass@1，在RTLLM v2上达到68.0% pass@1。关键指标显示，该模型在RTLLM v1.1上比之前的SOTA模型（CraftRTL-DS-6.7B）提升了18.8% pass@1，甚至在RTLLM上超过了671B的DeepSeek-R1。此外，消融实验证明了等价性检查和难度过滤对RL数据集质量的重要性，而自适应DAPO算法相比基线DAPO实现了1.25倍的加速。测试时缩放分析表明，随着响应长度预算从4096增加到16384令牌，模型准确率从7.1%提升至72.9%，优于DeepSeek-R1（29.0%→64.1%），且计算效率更高。

### Q5: 有什么可以进一步探索的点？

该论文在自动化验证环境构建、数据合成和高效训练算法方面取得了显著进展，但仍有多个方向值得深入探索。首先，其验证环境依赖规则生成的测试平台和黄金参考代码，这限制了其对复杂、非确定性电路（如异步设计或包含高级优化）的覆盖能力。未来可探索形式化验证或符号执行等更严格的等价性检查方法，以提升验证的完备性。

其次，数据合成方法基于现有代码片段生成自然语言描述，可能导致数据多样性不足或存在描述偏差。未来可研究如何引入人类专家反馈进行数据清洗或增强，或构建多轮交互式数据生成流程，以提升NL-代码对的质量和复杂性。

在模型层面，当前工作主要针对代码生成准确性，但未深入评估生成代码的可读性、可维护性或功耗/面积等硬件关键指标。未来可将这些硬件特定指标纳入奖励函数，进行多目标强化学习优化。

此外，该框架目前专注于Verilog，未来可扩展至其他硬件描述语言（如VHDL、Chisel）或系统级建模语言，并探索从高层次规范（如C/C++）直接生成RTL的跨层级综合任务。最后，训练成本虽已优化，但对于更大规模模型或更复杂任务，可进一步研究课程学习、模型并行或更高效的分布式RLVR算法。

### Q6: 总结一下论文的主要内容

本文提出CodeV-R1框架，旨在解决将强化学习与可验证奖励（RLVR）应用于电子设计自动化（EDA）中Verilog代码生成任务时面临的三大挑战：缺乏自动化验证环境、高质量自然语言-代码对稀缺以及RLVR训练成本过高。核心贡献包括：首先，设计了一个基于规则的测试平台生成器，用于对黄金参考进行鲁棒的等价性检查；其次，提出一种往返数据合成方法，将开源Verilog片段与LLM生成的自然语言描述配对，并通过生成的测试平台验证代码-描述-代码的一致性，过滤不等价样本以构建高质量数据集；第三，采用“蒸馏后强化学习”的两阶段训练流程，先通过蒸馏冷启动模型的推理能力，再使用新颖的自适应DAPO算法进行RLVR训练，该算法能通过自适应调整采样率降低计算成本。实验表明，所得模型CodeV-R1-7B在VerilogEval v2和RTLLM v1.1基准上分别达到68.6%和72.9%的pass@1，显著超越先前最优方法12%~20%，甚至在RTLLM上性能超过671B的DeepSeek-R1。该工作为EDA领域的LLM应用提供了有效的训练框架和高质量资源。
