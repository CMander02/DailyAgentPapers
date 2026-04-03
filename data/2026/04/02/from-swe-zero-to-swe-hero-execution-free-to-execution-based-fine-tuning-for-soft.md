---
title: "From SWE-ZERO to SWE-HERO: Execution-free to Execution-based Fine-tuning for Software Engineering Agents"
authors:
  - "Nikolai Ludwig"
  - "Wasi Uddin Ahmad"
  - "Somshubra Majumdar"
  - "Boris Ginsburg"
date: "2026-04-02"
arxiv_id: "2604.01496"
arxiv_url: "https://arxiv.org/abs/2604.01496"
pdf_url: "https://arxiv.org/pdf/2604.01496v1"
categories:
  - "cs.SE"
  - "cs.CL"
tags:
  - "代码智能体"
  - "软件工程智能体"
  - "指令微调"
  - "数据蒸馏"
  - "执行反馈"
  - "SWE-bench"
  - "工具使用"
  - "代码仓库理解"
  - "零样本迁移"
relevance_score: 9.0
---

# From SWE-ZERO to SWE-HERO: Execution-free to Execution-based Fine-tuning for Software Engineering Agents

## 原始摘要

We introduce SWE-ZERO to SWE-HERO, a two-stage SFT recipe that achieves state-of-the-art results on SWE-bench by distilling open-weight frontier LLMs. Our pipeline replaces resource-heavy dependencies with an evolutionary refinement strategy: (1) SWE-ZERO utilizes large-scale, execution-free trajectories to master code semantics and repository-level reasoning, and (2) SWE-HERO applies targeted, execution-backed refinement to transition these semantic intuitions into rigorous engineering workflows. Our empirical results set a new benchmark for open-source models of comparable size. We release a dataset of 300k SWE-ZERO and 13k SWE-HERO trajectories distilled from Qwen3-Coder-480B, alongside a suite of agents based on the Qwen2.5-Coder series. Notably, SWE-HERO-32B achieves a 62.2% resolution rate on SWE-bench Verified. Furthermore, despite being trained exclusively on Python, our agents demonstrate robust zero-shot transferability on SWE-bench Multilingual, reaching 44.1% and confirming the paradigm's generalizability across diverse languages.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型（LLM）的自主软件工程（SWE）智能体在训练和优化过程中，对**物理代码执行环境（如Docker容器）的强依赖所导致的严重可扩展性瓶颈问题**。

**研究背景**：随着LLM智能体的发展，软件工程任务已进入实际部署阶段。现有最先进的方法通常依赖于在容器化环境中执行代码并获取运行时反馈，以此生成高质量的训练轨迹（用于监督微调或强化学习）。虽然这种执行验证能确保代码补丁的可靠性，但它带来了巨大的计算和工程开销。

**现有方法的不足**：论文指出，这种对“完美执行环境”的绝对依赖在三个关键层面制约了开源智能体的发展：1. **数据可扩展性**：许多现实世界的代码仓库和拉取请求（PR）因其复杂或过时的配置而无法在标准容器环境中可靠构建，导致大量有价值的数据被丢弃。2. **训练可扩展性**：为成千上万的任务实例编排和管理独立的Docker镜像会产生巨大的基础设施开销，使得大规模优化和强化学习变得复杂且昂贵。3. **推理可扩展性**：昂贵的代码执行和环境重置成本，阻碍了智能体在推理时高效地探索不同的解决方案分支。

**本文要解决的核心问题**：因此，本文的核心目标是**设计一种可扩展的训练范式，将语义推理学习与物理执行验证解耦**，从而突破上述瓶颈。具体而言，论文提出了一个名为“从SWE-ZERO到SWE-HERO”的两阶段监督微调方案。该方案首先在**无需执行**的大规模轨迹数据（SWE-ZERO）上训练智能体，使其掌握代码语义和仓库级推理能力；随后，再在相对较小但**基于执行验证**的高质量轨迹数据（SWE-HERO）上进行精炼，将语义直觉转化为严谨的工程工作流。这种方法旨在减少对重型执行基础设施的依赖，解锁更广泛的数据，并最终高效地训练出性能优异的软件工程智能体。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：软件问题解决数据集和软件工程智能体。

在**数据集**方面，相关工作经历了从静态代码收集到动态交互环境的演变。SWE-Gym 率先将Python问题与可执行环境配对用于智能体训练，后续的SWE-rebench和SWE-Factory通过持续获取新数据来对抗数据污染。为突破人工标注瓶颈，SWE-Smith和SWE-Synth引入了自动错误注入和调试模拟。R2E-Gym从代码提交中构建环境，SWE-Mirror则复现了真实问题的语义本质。SWE-World另辟蹊径，使用学习的替代模型来预测环境反馈，无需物理执行。SWE-Lego综合了高质量真实拉取请求和可扩展的合成实例，以优化训练数据的精度和规模。本文提出的两阶段SFT流程（SWE-ZERO和SWE-HERO）同样旨在高效生成高质量训练轨迹，但其核心创新在于采用了“从无执行到有执行”的进化精炼策略，并专注于从顶级开源模型中蒸馏知识。

在**软件工程智能体**方面，研究从早期的智能体框架（如SWE-agent、OpenHands）转向模型中心的优化。近期工作侧重于通过数据合成和中途训练（如daVinci-Dev）或使用高质量轨迹进行智能体SFT（如SWE-Mirror、SWE-Lego），将智能体推理能力直接注入基础模型。为弥合静态训练与动态交互的鸿沟，DeepSWE和SkyRL采用强化学习通过试错反馈优化策略。此外，还有“无智能体”流水线将问题分解为故障定位、代码修复和补丁验证等离散阶段进行优化。本文工作属于智能体SFT范畴，但与SWE-Mirror等使用真实或合成轨迹进行SFT的方法不同，本文通过两阶段蒸馏专门从强大教师模型中提取能力，并强调无执行学习与有执行精炼的有机结合，而非依赖强化学习或完全分解的流水线。

### Q3: 论文如何解决这个问题？

论文通过一个名为“从SWE-ZERO到SWE-HERO”的两阶段监督微调（SFT）配方来解决软件工程智能体能力提升的问题。其核心方法是**进化式精炼策略**，旨在用更高效的训练流程替代资源密集型的依赖，具体分为两个阶段：首先利用大规模、无执行的轨迹让模型掌握代码语义和仓库级推理，然后通过小规模、有执行反馈的轨迹将这些语义直觉转化为严谨的工程工作流。

整体框架基于**SWE-agent范式**，智能体通过一个支持自主仓库导航、代码编辑和测试执行的接口进行操作。主要模块包括：
1.  **任务与仓库收集**：整合了多个开源Python软件工程数据集，包含超过18万个任务实例和3500多个仓库，形成了无约束的SWE-ZERO基础数据集和经过验证、容器化的SWE-HERO子集。
2.  **智能体脚手架**：使用**OpenHands**作为开源智能体框架，为智能体配备了四个核心工具：用于文件读写编辑的`str_replace_editor`、执行命令的`execute_bash`、用于长链推理的`think`以及标记任务完成的`finish`。
3.  **教师智能体与轨迹生成**：采用**Qwen3-Coder-480B**作为教师模型进行轨迹蒸馏。生成过程分为两种配置：
    *   **SWE-ZERO轨迹收集**：智能体在**无执行环境**（通用沙盒，无仓库特定设置）中运行，仅能进行代码库探索和源码修改，无法执行代码。其工作流聚焦于需求分析、仓库探索、修复定位、补丁实现和最终审查五个阶段。为了确保质量，设计了一个**多阶段过滤管道**：首先通过规则解析器丢弃任何尝试执行被禁止代码的轨迹；其次进行质量控制，过滤掉超过步数限制、产生空代码变更、修改了测试补丁中文件（防止“捷径”行为）或工具调用不规范的轨迹。
    *   **SWE-HERO轨迹收集**：智能体在**完整的Docker环境**中运行，能够获得实时执行反馈，执行标准的解决问题轨迹。这些轨迹直接进入上述第二阶段的质量过滤。
4.  **模型训练**：对**Qwen2.5-Coder-Instruct**模型进行多轮SFT。关键技术包括：应用**YaRN**方法将上下文长度从32K扩展到128K以支持长轨迹建模；采用**多轮掩码策略**，在损失计算中排除工具输出，迫使模型专注于学习动作生成而非拟合执行结果。训练流程是顺序的：先在过滤后的SWE-ZERO数据集上训练得到基础LLM智能体，然后以此为基础，在SWE-HERO数据集上进行精炼训练。

创新点主要体现在：
1.  **两阶段进化精炼范式**：将大规模、低成本的无执行预训练（学习语义和推理）与小型、高保真的有执行精炼（学习工程实践）解耦，在保证效果的同时大幅提升了数据规模和训练效率。
2.  **针对无执行环境的严格过滤机制**：通过创新的多阶段过滤管道，有效解决了教师模型在受限环境下可能出现的违规执行尝试、无限循环等问题，确保了SWE-ZERO训练数据的高质量和逻辑一致性。
3.  **训练策略优化**：结合上下文窗口扩展和特定的损失掩码策略，使模型能有效处理长交互序列并聚焦于学习决策过程。

### Q4: 论文做了哪些实验？

论文在SWE-bench基准上进行了全面的实验评估。实验设置方面，研究基于Qwen2.5-Coder-Instruct模型，通过监督微调（SFT）训练了7B、14B和32B三种参数规模的SWE-ZERO和SWE-HERO代理。训练使用最大128k令牌的上下文长度，全局批次大小为32，采用余弦学习率调度器（峰值1e-5，衰减至1e-8）。推理时固定温度0.7，top-p为0.8，top-k为20，每任务最多100轮交互。

使用的核心数据集/基准测试是SWE-bench Verified（包含500个高质量真实Python软件工程问题）和SWE-bench Multilingual（300个任务，用于评估跨语言泛化能力）。主要评估指标是解决率（Resolve Rate, %）。

对比方法包括SWE-Gym、R2E-Gym、SWE-Dev、SERA、FrogMini、Skywork-SWE、DeepSWE、SWE-Mirror-LM、SWE-Lego、SWE-Swiss、SWE-Master、OpenSWE等多个开源代码代理模型。

主要结果显示，SWE-HERO模型在SWE-bench Verified上取得了最先进的性能：7B、14B和32B模型的解决率分别为52.7%、60.8%和62.2%。其中，32B模型（62.2%）与当前最优的OpenSWE-32B（62.4%）性能相当，但训练流程更精简。关键数据指标包括：SWE-HERO-32B在SWE-bench Verified上达62.2%，在SWE-bench Multilingual上达44.1%。消融实验表明，跳过SWE-ZERO阶段直接微调（direct-to-hero基线）的解决率仅为55.7%（Verified）和30.8%（Multilingual），凸显了执行无关预训练阶段对性能提升（分别提高6.5和13.3个百分点）和跨语言泛化的关键作用。

### Q5: 有什么可以进一步探索的点？

该论文的局限性为未来研究提供了明确方向。首先，蒸馏方法使学生模型继承了教师模型的偏见和错误，未来可探索多教师模型集成或对抗性去偏技术来突破这一性能上限。其次，当前工作基于标准非推理架构，而新兴的思维链模型在复杂问题解决上更具潜力；将两阶段范式适配于此类架构，并设计针对代码推理的中间表示格式，有望进一步提升系统验证能力。此外，执行环境的随机性会影响结果可复现性，未来可构建更稳定的沙箱环境或开发不确定性量化方法以区分模型能力缺陷与环境波动。最后，尽管在跨语言任务上展示了零样本迁移性，但训练数据仅限Python，未来可通过多语言课程学习或跨语言对齐技术，系统性提升其在多样化软件工程生态中的泛化能力。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为“从SWE-ZERO到SWE-HERO”的两阶段监督微调方法，旨在解决传统自动化软件问题修复中存在的可扩展性瓶颈。其核心贡献在于设计了一种进化式精炼策略，以替代资源密集型的执行环境依赖。具体而言，第一阶段SWE-ZERO利用大规模、无需代码执行的轨迹数据，使模型掌握代码语义和仓库级别的推理能力；第二阶段SWE-HERO则基于执行反馈进行针对性精炼，将语义直觉转化为严谨的工程工作流。该方法在SWE-bench基准测试中取得了开源模型的最优性能，例如SWE-HERO-32B在SWE-bench Verified上实现了62.2%的问题解决率。论文还发布了从Qwen3-Coder-480B蒸馏得到的数据集及基于Qwen2.5-Coder的智能体系列，为自主软件修复提供了可扩展框架。尽管仅使用Python数据训练，该方法在跨语言任务上也展现出强大的零样本迁移能力，验证了其泛化性。
