---
title: "Open-SWE-Traces: Advancing Dual-Mode Multilingual Distillation for Software Engineering Agents"
authors:
  - "Wasi Uddin Ahmad"
  - "Nikolai Ludwig"
  - "Somshubra Majumdar"
  - "Boris Ginsburg"
date: "2026-06-14"
arxiv_id: "2606.16038"
arxiv_url: "https://arxiv.org/abs/2606.16038"
pdf_url: "https://arxiv.org/pdf/2606.16038v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Agent 训练数据"
  - "代码 Agent"
  - "多语言 Agent"
  - "Agent 微调"
  - "SWE-bench"
  - "数据合成"
  - "开源 Agent"
relevance_score: 9.5
---

# Open-SWE-Traces: Advancing Dual-Mode Multilingual Distillation for Software Engineering Agents

## 原始摘要

The path toward autonomous software engineering is currently bottlenecked by a severe deficit of diverse, large-scale trajectory data. We address this by introducing \ourdataset, an expansive dataset of 207,489 agentic trajectories spanning nine programming languages (Python, Go, TS, JS, Rust, Java, PHP, C, C++). Sourced from 20,000 real-world PRs via OpenHands and SWE-agent harnesses, the dataset utilizes a hybrid-reasoning synthesis: Minimax-M2.5 generates trajectories with explicit "thinking" processes, while Qwen3.5-122B provides high-quality "non-thinking" traces. Filtered for permissive licenses (MIT, Apache, BSD) from SWE-rebench-V2, this data facilitates the training of models capable of long-horizon reasoning. We validate the dataset by fine-tuning the Qwen3-30B-A3B series (Thinking, Instruct, and Coder). The best performing model achieves resolve rates of 61.7% on SWE-bench Verified, 57.1% on SWE-bench Multilingual, and 36.8% on SWE-bench Pro. These results establish Open-SWE-Traces as a premier resource for distilling human-level software engineering capabilities into efficient, open-source agentic LLMs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前面向软件工程的自主智能体（SWE Agents）发展中面临的核心瓶颈：缺乏大规模、多样化的智能体轨迹数据。尽管评估基准（如SWE-bench）已趋于多样化和多语言化，但用于训练模型的高质量交互轨迹数据却严重不足。现有方法受限于数据规模小、语言覆盖单一（主要是Python），且缺乏智能体在解决真实世界仓库问题时产生的“思考”与“非思考”双模态推理过程记录，导致模型难以掌握长期规划、多步推理和高效执行的复合能力。为此，本文提出了Open-SWE-Traces数据集，这是一个包含超过20万条智能体轨迹、覆盖9种编程语言的大规模语料库。核心目标是解决数据稀缺问题，并通过“双模多语言蒸馏”策略，使模型能同时从显式推理轨迹（带有思考过程）和高效执行轨迹（无思考）中学习，从而训练出既能处理复杂问题又能高效执行常规任务的自主软件工程智能体。

### Q2: 有哪些相关研究？

以下是论文的相关研究，按类别组织：

**方法类**：在SWE数据集方面，本文与SWE-Gym、SWE-rebench等数千实例的数据集不同，Open-SWE-Traces通过混合推理合成（Minimax-M2.5的显式“思考”轨迹和Qwen3.5-122B的“非思考”轨迹）构建了20.7万条轨迹，规模远超SWE-Mirror、SWE-smith等合成数据；与Scale-SWE的10万实例相比，本文覆盖9种编程语言且来源真实PR。在模型训练上，不同于SWE-Zero/Hero的两阶段蒸馏或SWE-World的替代模型反馈，本文直接微调Qwen3-30B-A3B系列，实现高效蒸馏。

**评测类**：本文借鉴SWE-bench Verified、SWE-bench Multilingual和SWE-bench Pro等多维度基准进行验证，与BeyondSWE等跨仓库推理基准互补，不仅评估单语言修复，还首次系统评估多语言能力。

**应用类**：与OpenHands、SWE-agent等环境提示框架不同，本文通过数据集训练实现模型权重内嵌推理；与Orchard的开源配方相比，Open-SWE-Traces更聚焦于大规模多语言轨迹的公开释放。

### Q3: 论文如何解决这个问题？

论文通过构建大规模多语言轨迹数据集Open-SWE-Traces来解决软件工程智能体训练数据匮乏的问题。核心方法是一个系统化的三阶段流水线：首先从SWE-rebench V2中筛选出9种编程语言（Python、Go等）且采用MIT、Apache等宽松许可证的2万个真实PR；然后利用双模型异构合成策略，即MiniMax-M2.5生成包含显式推理过程的"思考"轨迹，Qwen3.5-122B生成高质量"非思考"轨迹；最后通过两阶段质量过滤，包括执行聚合验证移除崩溃轨迹、行为修剪剔除任务不完整/结构无效/工具使用异常的低质量样本，并使用TrajectoryScanner工具审计Git命令防止作弊行为。

整体架构创新点在于支持双模式操作（/think和/no_think触发），让同一个模型既能输出带推理链的思考过程，也能输出快速决策的非思考模式。关键技术包括：采用Qwen3-30B-A3B系列作为基础模型进行知识蒸馏，保持131K上下文窗口训练，推理时扩展至262K token；在OpenHands和SWE-agent两个框架上适配多语言支持，修复了Go语言patch兼容性等关键bug；最终数据集包含207,489条高质量轨迹，其中51.7%包含链式推理，在SWE-bench Verified/多语言/Pro上分别达到61.7%、57.1%和36.8%的解决率。

### Q4: 论文做了哪些实验？

论文主要进行了三组实验，包括在SWE-bench Verified、Multilingual和Pro基准上的评估，以及消融研究。实验使用了207,489条多语言（9种编程语言）agent轨迹数据集，基于20,000个真实PR，采用Minimax-M2.5（生成思考过程轨迹）和Qwen3.5-122B（生成非思考轨迹）的混合推理合成，并过滤了许可协议。对比方法包括闭源模型（如Claude Opus 4.5, GPT-5.2）、开源基础模型（如Minimax-M2.5, Qwen3.5-122B-A10B）以及同尺寸开源模型（如Scale-SWE-Agent, SWE-Hero-32B等）。主要结果：在SWE-bench Verified上，本文最佳模型（Qwen3-Coder-30B-A3B，无思考模式）在MSWE-agent框架下达到61.7%的解决率，高于基线Qwen3-Coder-30B-A3B的51.6%和Scale-SWE-Agent的64.0%（但作者指出后者使用了更多训练数据）。在SWE-bench Multilingual上达到57.1%，在SWE-bench Pro上达到36.8%。消融研究发现：跨框架泛化会带来性能下降（如MOH→MSWEA下降约2-5%），MSWEA作为基线更鲁棒；从仅Python训练到全数据集训练使SWE-bench Multilingual无思考模式解决率从43.1%提升至57.1%（+14%绝对增益）；包含未解决轨迹的全数据集优于仅使用解决轨迹的子集，在SWE-bench Multilingual无思考模式下从49.6%提升至57.1%。

### Q5: 有什么可以进一步探索的点？

论文的局限性首先体现在对教师模型的强依赖性上，从Minimax-M2.5和Qwen3.5-122B继承的潜在偏差和系统错误难以避免。未来可探索引入多教师蒸馏或对抗训练减轻偏差；同时，LLM的随机性和环境波动导致评估结果不稳定，尽管采用三次运行取平均但仍有微小差异，建议开发更鲁棒的评测基准。在数据构建上，当前仅基于开源许可的项目，可考虑扩充闭源高质量PR数据或自生成伪轨迹。模式复用方面，现有"思考"与"非思考"双模式虽有效，但对不同任务自适应混合策略（如动态切换推理深度）值得尝试。此外，模型规模从30B扩至更大参数（如70B）能否线性提升效果？跨语言泛化中，对低频语言（如PHP、Rust）的可信响应数不足，可针对性增强数据采集。最后，当前方法缺乏代码执行时的动态纠错机制，结合测试反馈的闭环学习可能是关键突破方向。

### Q6: 总结一下论文的主要内容

当前自主软件工程发展受限于缺乏大规模、多样化的轨迹数据。为此，论文提出了Open-SWE-Traces数据集，包含207,489条覆盖9种编程语言的智能体轨迹，源自20,000个真实世界PR。该数据集通过混合推理合成策略生成：MiniMax-M2.5生成带有显式“思考”过程的轨迹，Qwen3.5-122B提供高质量“非思考”轨迹，支持双模多语言蒸馏。通过微调Qwen3-30B-A3B系列模型验证了数据集有效性，最佳模型在SWE-bench Verified上达到61.7%的解决率，在SWE-bench Multilingual上为57.1%，在SWE-bench Pro上为36.8%。核心贡献在于提供了首个大规模多语言轨迹语料库，实现了将人类级软件工程能力蒸馏为高效开源智能体模型，并提出双模式训练范式。研究证明，将显式思考模态与高质量行为轨迹相结合，是开发专用自主智能体的有效路径。
