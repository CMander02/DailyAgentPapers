---
title: "LongCat-Flash-Prover: Advancing Native Formal Reasoning via Agentic Tool-Integrated Reinforcement Learning"
authors:
  - "Jianing Wang"
  - "Jianfei Zhang"
  - "Qi Guo"
  - "Linsen Guo"
  - "Rumei Li"
  - "Chao Zhang"
  - "Chong Peng"
  - "Cunguang Wang"
  - "Dengchang Zhao"
  - "Jiarong Shi"
  - "Jingang Wang"
  - "Liulin Feng"
  - "Mengxia Shen"
  - "Qi Li"
  - "Shengnan An"
  - "Shun Wang"
  - "Wei Shi"
  - "Xiangyu Xi"
  - "Xiaoyu Li"
  - "Xuezhi Cao"
date: "2026-03-22"
arxiv_id: "2603.21065"
arxiv_url: "https://arxiv.org/abs/2603.21065"
pdf_url: "https://arxiv.org/pdf/2603.21065v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent Architecture"
  - "Tool-Integrated Reasoning"
  - "Reinforcement Learning"
  - "Formal Reasoning"
  - "Mixture-of-Experts"
  - "Policy Optimization"
  - "Theorem Proving"
  - "Auto-formalization"
  - "Benchmark Evaluation"
relevance_score: 9.5
---

# LongCat-Flash-Prover: Advancing Native Formal Reasoning via Agentic Tool-Integrated Reinforcement Learning

## 原始摘要

We introduce LongCat-Flash-Prover, a flagship 560-billion-parameter open-source Mixture-of- Experts (MoE) model that advances Native Formal Reasoning in Lean4 through agentic tool-integrated reasoning (TIR). We decompose the native formal reasoning task into three independent formal capabilities, i.e., auto-formalization, sketching, and proving. To facilitate these capabilities, we propose a Hybrid-Experts Iteration Framework to expand high-quality task trajectories, including generating a formal statement based on a given informal problem, producing a whole-proof directly from the statement, or a lemma-style sketch. During agentic RL, we present a Hierarchical Importance Sampling Policy Optimization (HisPO) algorithm, which aims to stabilize the MoE model training on such long-horizon tasks. It employs a gradient masking strategy that accounts for the policy staleness and the inherent train-inference engine discrepancies at both sequence and token levels. Additionally, we also incorporate theorem consistency and legality detection mechanisms to eliminate reward hacking issues. Extensive evaluations show that our LongCat-Flash-Prover sets a new state-of-the-art for open-weights models in both auto-formalization and theorem proving. Demonstrating remarkable sample efficiency, it achieves a 97.1% pass rate on MiniF2F-Test using only 72 inference budget per problem. On more challenging benchmarks, it solves 70.8% of ProverBench and 41.5% of PutnamBench with no more than 220 attempts per problem, significantly outperforming existing open-weights baselines.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决在交互式定理证明器（如Lean4）中进行“原生形式推理”的挑战，即让AI模型能够直接理解和生成符合形式化数学语言（如定理和证明）的代码。研究背景是，形式化数学和定理证明对确保数学陈述和软件的正确性至关重要，但传统方法（如基于搜索或符号推理）在处理复杂、长视野的证明任务时，往往面临效率低下、泛化能力不足或难以与工具环境（如证明助手）深度集成的问题。现有的大规模语言模型虽在数学推理上展现出潜力，但在直接进行形式化、结构化的定理证明时，仍存在生成代码的合法性与一致性差、训练不稳定（尤其是在混合专家模型上）、以及难以有效利用证明助手提供的反馈（如错误信息）等不足。

本文的核心问题是：如何构建一个能够高效、稳定地进行端到端原生形式推理的AI系统，使其能自动完成从非形式化问题到形式化陈述的转换（自动形式化）、生成证明概要（草图）以及完成完整证明，并在此过程中与定理证明工具深度协同。为此，论文提出了LongCat-Flash-Prover模型，其解决方案聚焦于三个层面：一是将任务分解为自动形式化、草图生成和证明三个独立能力；二是设计了混合专家迭代框架来扩增高质量训练轨迹；三是针对长视野任务中混合专家模型训练不稳定的问题，提出了分层重要性采样策略优化算法，通过梯度掩码策略处理策略陈旧性和训练-推理差异，并引入定理一致性与合法性检测机制来避免奖励黑客问题，从而提升推理的样本效率和最终性能。

### Q2: 有哪些相关研究？

本文的相关研究可大致分为方法类、应用类和评测类。

在**方法类**上，相关工作主要包括：1) **工具集成推理（TIR）**：现有研究探索了将外部工具（如计算器、搜索引擎）集成到语言模型中以增强推理能力。本文的Agentic TIR框架专门针对形式化证明环境（Lean4）设计，将任务分解为自动形式化、草图生成和完整证明三个独立能力，这与通用TIR工作有显著区别。2) **强化学习（RL）用于定理证明**：先前工作（如CodeRL）应用RL训练模型生成代码或证明。本文提出的分层重要性采样策略优化（HisPO）算法，专门解决了混合专家（MoE）模型在长视野任务中的训练不稳定问题，并引入了梯度掩码策略以应对策略陈旧性和训练-推理差异，这是对现有RL方法的重要改进。3) **高质量数据生成**：相关工作通过合成数据或自我改进来扩充数据集。本文提出的混合专家迭代框架，旨在系统性地扩展高质量任务轨迹，专注于形式化推理领域。

在**应用与评测类**上，相关工作包括：1) **自动形式化与定理证明基准**：如MiniF2F、ProverBench和PutnamBench等，用于评估模型将非形式问题转化为形式陈述并完成证明的能力。本文正是在这些基准上进行了广泛评估，并设立了新的开源模型最优性能。2) **现有开源模型**：如一些基于Transformer的证明器。本文的LongCat-Flash-Prover作为一个5600亿参数的MoE模型，在样本效率（如MiniF2F上仅用少量尝试即达到高通过率）和解决复杂问题能力上显著超越了这些基线。

总之，本文在继承工具集成推理和强化学习方向的基础上，通过创新的任务分解、训练框架和优化算法，专门推进了**原生形式化推理**这一细分领域的能力。

### Q3: 论文如何解决这个问题？

论文通过一个分阶段的训练框架和创新的算法设计来解决原生形式推理问题。其核心方法是将复杂的推理任务分解为三个独立的能力：自动形式化、草图和证明，并采用混合专家迭代框架来扩展高质量的任务轨迹。

整体框架分为两个主要阶段：监督微调（SFT）和强化学习（RL），其中RL又细分为离线直接偏好优化（DPO）和在线近端策略优化（PPO）。在SFT阶段，模型在多个关键维度上进行优化，包括指令遵循、数学、代码、逻辑推理、长上下文、工具使用和安全性，以激活和精炼预训练获得的能力。为此，论文构建了包含150万个样本的多样化数据集，并采用了序列打包等技术进行高效训练。

强化学习阶段是核心创新所在。为了解决在长视野任务上训练MoE模型的不稳定性问题，论文提出了分层重要性采样策略优化（HisPO）算法。该算法采用了一种梯度掩码策略，该策略同时考虑了策略陈旧性以及训练与推理引擎在序列级别和令牌级别上固有的差异，从而稳定训练过程。此外，为了消除奖励黑客问题，还引入了定理一致性和合法性检测机制。奖励系统也经过精心设计，结合了基于参考的奖励、基于执行的奖励，以及判别式和生成式奖励模型，为不同任务提供全面的评估信号。

主要创新点包括：1）将原生形式推理任务解耦为三个可独立训练和评估的正式能力；2）提出混合专家迭代框架来生成和扩展证明轨迹；3）设计HisPO算法，专门针对MoE模型在长序列、工具集成推理中的训练不稳定性进行优化；4）构建了多层次、多类型的奖励系统与质量检测机制，确保训练信号的可靠性和有效性。通过这些方法，模型在样本效率上表现卓越，以极少的尝试次数在多个基准测试上达到了新的最优水平。

### Q4: 论文做了哪些实验？

论文在自动形式化和定理证明两个核心任务上进行了广泛的实验评估。实验设置基于提出的混合专家迭代框架和分层重要性采样策略优化算法，旨在验证模型在长视野任务上的稳定性和样本效率。

数据集和基准测试方面，研究使用了多个数学推理基准。关键数据集包括：MiniF2F-Test，用于评估定理证明能力；ProverBench 和 PutnamBench，作为更具挑战性的基准，测试模型在复杂问题上的表现。实验将 LongCat-Flash-Prover 与现有的开源权重模型进行了对比。

主要结果通过关键数据指标体现：在 MiniF2F-Test 上，模型仅使用每个问题 72 次的推理预算，就达到了 97.1% 的通过率，展现了卓越的样本效率。在更困难的基准上，模型在 ProverBench 上解决了 70.8% 的问题，在 PutnamBench 上解决了 41.5% 的问题，且每个问题的尝试次数不超过 220 次。这些结果显著优于所有现有的开源权重基线模型，确立了新的最高水平。实验结果表明，所提出的代理工具集成强化学习方法有效提升了模型在自动形式化和定理证明任务上的性能。

### Q5: 有什么可以进一步探索的点？

这篇论文在将工具集成与强化学习结合以推进形式化推理方面取得了显著进展，但其探索方向仍有拓展空间。局限性方面，模型高度依赖预定义的“工具”和轨迹分解（如形式化、草图、证明），这可能限制了其对未见过或更复杂问题结构的泛化能力。此外，尽管采用了分层采样策略，MoE模型在超长序列任务中的训练稳定性和效率仍是挑战。

未来研究可探索以下几个方向：一是增强模型的“元推理”能力，使其能动态调整任务分解策略或自主选择/组合工具，而非严格遵循固定流程。二是考虑引入更细粒度的奖励塑造机制，例如对证明步骤的“优雅性”或“创新性”进行评价，以引导模型发现更优的证明路径，而不仅仅是合法性。三是将方法扩展到多模态形式化推理，例如处理结合图表或自然语言描述的数学问题。最后，可研究如何降低对大量高质量人工标注轨迹的依赖，通过自监督或合成数据生成来提升数据效率。

### Q6: 总结一下论文的主要内容

该论文提出了LongCat-Flash-Prover，一个5600亿参数的专家混合开源模型，旨在通过智能体工具集成推理推进Lean4中的原生形式推理。其核心贡献是将原生形式推理任务分解为三个独立能力：自动形式化、草拟和证明，并为此设计了混合专家迭代框架来扩展高质量任务轨迹。方法上，论文引入了分层重要性采样策略优化算法，通过梯度掩码策略处理策略陈旧性及训练-推理引擎在序列和标记层面的差异，以稳定MoE模型在长周期任务上的训练；同时结合定理一致性与合法性检测机制来避免奖励欺骗问题。主要结论显示，该模型在自动形式化和定理证明上为开源权重模型设立了新标杆，在MiniF2F-Test上仅用每个问题72次推理预算即达到97.1%通过率，并在更难的ProverBench和PutnamBench上显著超越现有基线，证明了其卓越的样本效率与推理能力。
