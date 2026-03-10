---
title: "SWE-Fuse: Empowering Software Agents via Issue-free Trajectory Learning and Entropy-aware RLVR Training"
authors:
  - "Xin-Cheng Wen"
  - "Binbin Chen"
  - "Haoxuan Lan"
  - "Hang Yu"
  - "Peng Di"
  - "Cuiyun Gao"
date: "2026-03-09"
arxiv_id: "2603.07927"
arxiv_url: "https://arxiv.org/abs/2603.07927"
pdf_url: "https://arxiv.org/pdf/2603.07927v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Agent Training"
  - "Software Engineering Agent"
  - "Reinforcement Learning"
  - "Trajectory Learning"
  - "SWE-bench"
  - "Tool Use"
  - "Code Agent"
relevance_score: 9.0
---

# SWE-Fuse: Empowering Software Agents via Issue-free Trajectory Learning and Entropy-aware RLVR Training

## 原始摘要

Large language models (LLMs) have transformed the software engineering landscape. Recently, numerous LLM-based agents have been developed to address real-world software issue fixing tasks. Despite their state-of-the-art performance, Despite achieving state-of-the-art performance, these agents face a significant challenge: \textbf{Insufficient high-quality issue descriptions.} Real-world datasets often exhibit misalignments between issue descriptions and their corresponding solutions, introducing noise and ambiguity that mislead automated agents and limit their problem-solving effectiveness. We propose \textbf{\textit{SWE-Fuse}}, an issue-description-aware training framework that fuses issue-description-guided and issue-free samples for training SWE agents. It consists of two key modules: (1) An issue-free-driven trajectory learning module for mitigating potentially misleading issue descriptions while enabling the model to learn step-by-step debugging processes; and (2) An entropy-aware RLVR training module, which adaptively adjusts training dynamics through entropy-driven clipping. It applies relaxed clipping under high entropy to encourage exploration, and stricter clipping under low entropy to ensure training stability. We evaluate SWE-Fuse on the widely studied SWE-bench Verified benchmark shows to demonstrate its effectiveness in solving real-world software problems. Specifically, SWE-Fuse outperforms the best 8B and 32B baselines by 43.0\% and 60.2\% in solve rate, respectively. Furthermore, integrating SWE-Fuse with test-time scaling (TTS) enables further performance improvements, achieving solve rates of 49.8\% and 65.2\% under TTS@8 for the 8B and 32B models, respectively.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的软件工程智能体在修复真实世界软件问题时，因**训练数据中高质量问题描述不足**而导致的性能瓶颈问题。研究背景是，随着CodeLlama等专用代码LLM的发展，能够处理仓库级上下文、自主生成补丁的智能体（如SWE-agent）不断涌现，并在SWE-bench等真实GitHub问题基准上取得了先进性能。然而，现有方法面临一个根本性挑战：从真实场景构建的数据集（如SWE-smith）中，大量问题描述与其对应的解决方案之间存在不一致或错位（例如，问题描述涉及警告处理，而正确补丁却修改了图像编码逻辑），甚至包含大量空描述。这种噪声和歧义会误导智能体，限制其有效解决问题的能力，同时高质量的问题-补丁对难以大规模获取，导致数据集规模和质量受限。

因此，本文要解决的核心问题是：**如何设计一个训练框架，使软件工程智能体能够克服低质量或误导性问题描述的干扰，稳健地学习有效的调试和问题解决轨迹**。为此，论文提出了SWE-Fuse框架，其核心创新在于融合两种数据样本进行训练：一是利用问题描述引导的样本，二是引入“无问题描述”的样本。具体通过两个关键模块实现：1) **无问题描述驱动的轨迹学习模块**，通过构建和过滤高质量的多步推理-动作轨迹，进行监督微调，使模型学会逐步调试过程，同时减少有噪声问题描述的干扰；2) **熵感知的RLVR训练模块**，通过基于熵的动态裁剪策略自适应调整训练，在高熵时放宽裁剪以鼓励探索，在低熵时收紧裁剪以确保稳定性，从而提升训练效果和智能体的问题解决能力。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕基于大语言模型的软件工程智能体展开，可分为方法类、应用类与评测类。

在**方法类**研究中，早期工作如对话式修复系统利用执行反馈迭代优化解决方案。后续的智能体框架（如SWE-agent、OpenHands）为LLM集成了终端、编辑器等开发工具，支持多步骤推理。AutoCodeRover将动态执行轨迹融入修复过程，RepoGraph则利用静态代码图进行分析（目前限于Python仓库）。这些方法均依赖高质量的Issue描述来指导修复，但现实数据中描述与解决方案常存在错位，引入噪声。

在**应用类**研究中，专门面向代码的LLM（如CodeLlama、StarCoder2、Qwen2.5-Coder）已在函数级编程任务上达到人类水平。然而，它们大多假设Issue描述准确，未充分考虑描述噪声问题。

在**评测类**研究中，SWE-bench作为基准数据集，提供了真实的GitHub Issue，但其中也存在描述与补丁不匹配的情况（如论文案例所示）。此外，SWE-smith等数据集中有大量问题陈述为空，凸显了数据质量挑战。

**本文与这些工作的关系和区别**在于：现有方法多依赖于Issue描述引导修复，而本文提出的SWE-Fuse框架**首创性地融合了有Issue描述和无Issue描述（issue-free）的样本进行训练**。其核心创新是通过issue-free轨迹学习模块减少误导性描述的影响，同时结合熵感知的RLVR训练模块动态调整训练过程。这使得模型能通过系统调试自主发现问题，而非完全依赖可能噪声的描述，从而在SWE-bench上取得了显著优于现有开源基线的效果。

### Q3: 论文如何解决这个问题？

论文通过提出名为SWE-Fuse的训练框架来解决现实数据集中问题描述与解决方案不对齐、质量不足的挑战。该框架融合了“无问题描述”的样本进行训练，旨在减少误导性描述带来的噪声，同时提升模型逐步调试和解决问题的能力。其核心方法包含两个关键模块：无问题描述驱动的轨迹学习模块，以及熵感知的RLVR训练模块。

整体框架首先进行环境构建，基于SWE-smith数据集筛选可执行的GitHub仓库，并创建沙箱管理器和执行环境以支持高并发交互。随后，框架将软件工程任务形式化为顺序决策过程，采用ReAct范式（推理-行动循环）让智能体与环境交互，生成多步轨迹。这些轨迹经过过滤（防止Git元数据利用和基于规则的筛选）后，与一部分完全不带问题描述的“无问题”样本混合，构成训练数据集。在无问题样本中，模型仅依靠部分测试用例进行逐步调试学习，从而避免被不准确的问题描述误导。接着，通过监督微调（SFT）使模型学习轨迹中的推理和行动序列。

创新点主要体现在熵感知的RLVR训练模块。该模块采用分组采样和留一法奖励计算相对优势，以降低方差。其核心是熵自适应裁剪机制：首先计算每个轨迹的序列级熵并归一化，然后根据归一化熵和优势值的正负动态调整裁剪范围。当优势值为正且熵高（模型不确定）时，放宽裁剪以鼓励探索；当优势值为负且熵高时，收紧裁剪以避免因噪声优势而过度惩罚。这种设计能自适应调整训练动态，在鼓励探索和保持稳定性之间取得平衡，从而加速收敛并提升策略优化效果。最终，SWE-Fuse在SWE-bench基准上显著超越了基线模型，并结合测试时缩放进一步提升了性能。

### Q4: 论文做了哪些实验？

实验在SWE-bench Verified基准上进行，这是一个广泛使用的真实世界软件工程任务数据集，包含从GitHub提取的bug修复和功能实现问题。研究首先使用完整的500个任务与基线方法进行公平比较，并为了平衡实验严谨性与计算成本，通过分层随机抽样构建了一个包含200个任务的代表性子集，其项目分布与完整基准成比例。

对比方法涵盖了开源和闭源模型，参数规模分为约7B和约30B两类，包括Qwen、GPT、Claude等系列模型，并部署在MOpenHands、OpenHands、SWE-agent等6种不同的脚手架框架上。评估指标采用问题解决率，即生成的补丁通过测试用例验证的成功百分比。

主要结果显示，SWE-Fuse在开源模型中表现最佳。具体而言，SWE-Fuse-8B模型取得了43.0%的解决率，比最佳8B基线（Klear-Agent-8B-SFT的39.4%）相对提升9.1%；SWE-Fuse-32B模型达到60.2%的解决率，比最佳32B基线（CWM-32B的53.9%）相对提升11.7%。当结合测试时缩放（TTS@8）时，性能进一步提升，8B和32B模型分别达到49.8%和65.2%的解决率。与闭源模型相比，SWE-Fuse-32B超越了OpenAI-o3（58.4%），但低于Claude-4-Sonnet（66.6%）等更大模型。

消融实验分析了训练数据的影响：轨迹数据量从0增加到14k时，解决率从13.5%单调提升至39.0%；当问题描述与无问题描述样本的比例为25%-50%时性能最优（约34.0%），纯无问题描述样本会导致性能下降至30.5%。此外，训练曲线表明，经过SFT初始化的模型在RLVR训练中能更快收敛并获得更高奖励，验证了所提模块的有效性。实验还确认了智能体依赖真实问题解决能力而非利用git历史等环境捷径。

### Q5: 有什么可以进一步探索的点？

本文提出的SWE-Fuse框架在缓解问题描述噪声和提升训练稳定性方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其核心假设是问题描述与解决方案之间存在错位，但未深入分析这种错位的具体类型（如语义模糊、信息缺失或无关噪声）及其对不同任务的影响差异，未来可引入更细粒度的错位检测与分类机制，以指导更精准的数据清洗或增强策略。其次，框架依赖于现有的“无问题”轨迹进行学习，这类高质量轨迹的规模与多样性可能受限，未来可探索通过合成数据生成、多任务迁移学习或课程学习来扩充轨迹库，并研究如何自动评估轨迹的“教学价值”。此外，熵感知的RLVR训练模块虽然动态调整裁剪策略，但其熵阈值设定可能依赖启发式规则，未来可结合元学习或贝叶斯优化进行自适应调整，甚至将熵信号与其他不确定性度量（如模型置信度或数据分布密度）融合，以更精细地平衡探索与利用。最后，当前评估集中于SWE-bench基准，其问题场景相对特定，未来需在更广泛的软件工程任务（如需求分析、架构设计或跨项目修复）中验证泛化能力，并探索将框架核心思想（如轨迹学习与熵感知训练）迁移至其他存在描述-解决方案噪声的领域（如医疗诊断或故障排除），以检验其通用性。

### Q6: 总结一下论文的主要内容

该论文针对基于大语言模型的软件工程代理在修复现实软件问题时面临的关键挑战——高质量问题描述不足且常与解决方案不匹配，提出了SWE-Fuse训练框架。其核心贡献在于融合了两种关键模块：一是问题描述无关的轨迹学习模块，通过使用无问题描述的样本来学习逐步调试过程，避免被有噪声或误导性的问题描述干扰；二是熵感知的强化学习与价值奖励训练模块，它根据策略熵自适应调整训练动态，在高熵时采用宽松剪裁以鼓励探索，在低熵时采用严格剪裁以保证稳定性。实验表明，SWE-Fuse在SWE-bench Verified基准上显著超越了现有最佳基线模型，并将与测试时扩展技术结合后能进一步提升性能。该工作的重要意义在于，通过创新的训练框架设计，有效提升了软件代理在现实嘈杂环境中的问题解决能力和鲁棒性。
