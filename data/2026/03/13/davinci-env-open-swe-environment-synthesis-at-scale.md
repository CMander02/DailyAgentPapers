---
title: "daVinci-Env: Open SWE Environment Synthesis at Scale"
authors:
  - "Dayuan Fu"
  - "Shenyu Wu"
  - "Yunze Wu"
  - "Zerui Peng"
  - "Yaxing Huang"
  - "Jie Sun"
  - "Ji Zeng"
  - "Mohan Jiang"
  - "Lin Zhang"
  - "Yukun Li"
  - "Jiarui Hu"
  - "Liming Liu"
  - "Jinlong Hou"
  - "Pengfei Liu"
date: "2026-03-13"
arxiv_id: "2603.13023"
arxiv_url: "https://arxiv.org/abs/2603.13023"
pdf_url: "https://arxiv.org/pdf/2603.13023v1"
categories:
  - "cs.SE"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Software Engineering Agent"
  - "Agent Training Framework"
  - "Agent Environment Synthesis"
  - "Large-Scale Dataset"
  - "Code Generation"
  - "Tool Use"
  - "Multi-Agent Pipeline"
  - "Difficulty-Aware Curation"
  - "Benchmarking"
relevance_score: 9.0
---

# daVinci-Env: Open SWE Environment Synthesis at Scale

## 原始摘要

Training capable software engineering (SWE) agents demands large-scale, executable, and verifiable environments that provide dynamic feedback loops for iterative code editing, test execution, and solution refinement. However, existing open-source datasets remain limited in scale and repository diversity, while industrial solutions are opaque with unreleased infrastructure, creating a prohibitive barrier for most academic research groups. We present OpenSWE, the largest fully transparent framework for SWE agent training in Python, comprising 45,320 executable Docker environments spanning over 12.8k repositories, with all Dockerfiles, evaluation scripts, and infrastructure fully open-sourced for reproducibility. OpenSWE is built through a multi-agent synthesis pipeline deployed across a 64-node distributed cluster, automating repository exploration, Dockerfile construction, evaluation script generation, and iterative test analysis. Beyond scale, we propose a quality-centric filtering pipeline that characterizes the inherent difficulty of each environment, filtering out instances that are either unsolvable or insufficiently challenging and retaining only those that maximize learning efficiency. With $891K spent on environment construction and an additional $576K on trajectory sampling and difficulty-aware curation, the entire project represents a total investment of approximately $1.47 million, yielding about 13,000 curated trajectories from roughly 9,000 quality guaranteed environments. Extensive experiments validate OpenSWE's effectiveness: OpenSWE-32B and OpenSWE-72B achieve 62.4% and 66.0% on SWE-bench Verified, establishing SOTA among Qwen2.5 series. Moreover, SWE-focused training yields substantial out-of-domain improvements, including up to 12 points on mathematical reasoning and 5 points on science benchmarks, without degrading factual recall.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决训练高效能软件工程（SWE）智能体时面临的大规模、高质量、可执行训练环境稀缺的核心瓶颈问题。研究背景是，随着大语言模型的发展，自主SWE智能体需要能够在动态、可验证的环境（如Docker容器）中迭代编辑代码、运行测试并接收反馈，以进行有效学习。然而，现有方法存在显著不足：一方面，开源数据集（如SWE-rebench等）在环境规模和代码库多样性上有限；另一方面，能够实现规模的工业解决方案其基础设施不透明且未开源，形成了高昂的资源壁垒，将大多数学术研究机构排除在外。此外，仅追求环境数量规模并不足够，现有方法合成的环境常存在质量问题，例如PR与问题描述不对齐导致任务无法解决，或问题过于简单直接揭示答案，这些环境要么无法提供有效的学习信号，要么学习效率低下。

因此，本文要解决的核心问题是：如何以完全透明、可复现的方式，大规模合成高质量、可执行且难度分布适宜的SWE训练环境，并验证其对智能体训练的有效性。为此，论文提出了OpenSWE框架，它不仅通过一个部署在64节点集群上的多智能体合成流水线，自动化地构建了涵盖大量仓库的大规模环境，更关键的是引入了一个以质量为中心的过滤流水线，通过评估环境的内在难度，滤除不可解决或过于简单的实例，只保留那些处于适当难度边界、能最大化学习效率的环境，从而在规模与质量之间取得平衡。

### Q2: 有哪些相关研究？

相关研究主要围绕软件工程（SWE）智能体环境构建、训练与评估展开，可分为以下几类：

**1. 环境构建与基准数据集：**
SWE-bench 是开创性工作，通过整理GitHub问题与拉取请求，提供基于Docker的可执行测试环境作为评估标准。为突破其规模限制，后续研究致力于自动化大规模环境生成：SWE-rebench 扩展了SWE-bench的构建流程以生成更多任务实例；SWE-Universe 通过系统爬取和过滤GitHub仓库来提供多样化的候选环境；SWE-Factory 进一步自动化了从仓库选择到Dockerfile合成及测试工具生成的端到端流程。本文提出的OpenSWE框架与这些工作方向一致，但通过多智能体合成流水线实现了更大规模（45,320个环境）和完全开源的基础设施，并引入了以质量为中心的过滤机制来筛选具有适当挑战性的环境。

**2. 智能体架构与平台：**
在智能体交互框架方面，SWE-agent 建立了基础架构，使智能体能自主导航代码库、定位错误并生成补丁。OpenHands 基于CodeAct框架提供了一个可扩展的开源平台，允许智能体在统一动作空间中交错执行代码和自然语言推理。本文虽聚焦环境合成，但其训练出的智能体（如OpenSWE-32B/72B）验证了所构建环境的有效性，与这些架构研究形成互补。

**3. 训练数据合成与模型训练：**
为训练SWE智能体，SWE-smith 构建了大规模训练数据合成流水线，生成多样化的任务实例和执行轨迹用于监督微调。daVinci-Dev 结合结构化规划与迭代代码生成/调试，利用多步推理轨迹产生高质量解决方案。SWE-Fixer 专注于利用过滤后的高质量轨迹进行监督微调的扩展。本文的OpenSWE在环境合成阶段也集成了轨迹采样和难度感知筛选（投资约147万美元），产出了约13,000条精选轨迹，与这些数据合成工作目标相似，但更强调环境本身的可执行性、规模及质量过滤，并为训练提供了直接基础。

**4. 替代执行与评估方法：**
SWE-Worldworld 提出了一个正交方向，用基于交互数据训练的代理模型替代物理Docker执行，以降低维护成本。本文则坚持使用实际Docker环境以确保可验证性，并通过分布式集群自动化构建，在规模与真实性上取得了平衡。

总体而言，本文与相关研究共同推进了SWE智能体基础设施的发展，其核心贡献在于提供了一个透明、大规模、高质量且完全开源的环境合成框架，弥补了现有开源数据集规模有限和工业解决方案不透明的缺口。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为OpenSWE的大规模、可执行且可验证的软件工程（SWE）环境合成框架来解决高质量训练数据稀缺的问题。其核心方法是一个多智能体合成流水线，部署在64个节点的分布式集群上，自动化地完成从GitHub PR到完整训练环境的转换。

**整体框架与主要模块**：
整个流程始于从GitHub大规模收集Python仓库的PR数据，并经过一个四阶段的质量过滤管道（仓库可行性、语言过滤、问题要求、实质性代码变更），筛选出高质量的PR候选。随后，通过一个由多个智能体协作的流水线将其转化为可执行的Docker环境：
1.  **轻量级仓库探索智能体**：负责对本地代码库进行有界探索，通过受限的API（浏览、搜索、摘要）收集与设置和测试相关的关键证据（如README、依赖清单、CI工作流），为下游智能体提供上下文。
2.  **Dockerfile构建智能体**：负责生成容器化环境。其创新点在于采用了**预构建的基础镜像策略**（openswe-python系列镜像，预装Python和conda）和**仓库预置策略**（通过本地缓存注入代码），显著减少了网络不稳定性和构建时间。同时采用**层感知提示**，将稳定的基础层与频繁变动的依赖安装层分离，利用Docker缓存加速迭代。
3.  **评估脚本生成智能体**：负责生成用于验证修复正确性的Bash测试脚本。其核心挑战是精准定位测试，因此智能体会识别与问题相关的特定测试文件，并在必要时合成新的测试用例。脚本采用模板化设计，分离补丁注入和测试逻辑，并嵌入结构化的退出代码标记（`$OPENSWE_EXIT_CODE$`）以便可靠解析。
4.  **测试分析智能体**：在基于规则的验证（测试失败/通过检查）之后运行，负责检查日志的真实性，诊断失败根源（如配置错误、脚本问题或环境本身不可解），并为可修复的错误生成针对性反馈，驱动前序智能体进行迭代优化。

**关键技术**：
*   **多智能体迭代反馈循环**：上述智能体在一个闭环中协同工作。探索智能体和Dockerfile智能体为评估脚本智能体提供上下文；测试执行后，分析智能体的反馈会引导Dockerfile或评估脚本智能体进行 refinement，直至环境通过验证。
*   **大规模分布式合成基础设施**：为应对海量PR处理和非确定性执行挑战，论文设计了一个**解耦的、容错的并行化框架**。采用数据并行和基于共享文件系统的消息队列，确保节点独立运行，单个故障不影响整体。配合系统d服务管理、自动化资源清理（僵尸容器）以及Prometheus/Grafana监控栈，实现了高效稳定的规模化合成。
*   **以质量为中心的过滤与策管**：在环境构建后，不仅进行规则验证，还通过智能体进行合法性检查，过滤掉不可解或挑战性不足的实例，最终保留约9000个质量有保证的环境，并从中采样约13000条轨迹，旨在最大化学习效率。

**创新点**：
1.  **规模与透明度**：构建了迄今最大（45,320个环境，覆盖12.8k仓库）且完全开源（包括Dockerfile、脚本和基础设施）的SWE训练框架。
2.  **智能体驱动的自动化合成流水线**：将复杂的环境构建任务分解为由多个专用智能体协作完成的自动化流程，并引入迭代反馈机制进行自我修正。
3.  **工程优化**：针对大规模构建的痛点，提出了预构建基础镜像、仓库缓存注入、层感知Dockerfile生成等关键优化，显著提升了构建成功率和效率。
4.  **难度感知的数据策管**：超越简单的可执行性验证，通过分析过滤来构建一个“难度适中”、利于智能体高效学习的优质数据集。

### Q4: 论文做了哪些实验？

论文在 SWE-Bench Verified 基准上进行了主要实验，评估了所训练的 OpenSWE 模型。实验设置方面，使用 OpenHands 或 SWE-Agent 作为智能体框架（温度 0.7，上下文长度 128k，步数 300），并报告两次运行平均的 Pass@1 分数。对比方法涵盖了 Qwen 2.5 和 Qwen 3 系列的多个代表性模型，如 R2EGym-Agent、Openhands-LM、SWE-Agent-LM、SWE-Master-32B、daVinci-Dev-32B 等。

主要结果如下：OpenSWE-32B 在 SWE-Agent 框架下取得了 62.4% 的分数，OpenSWE-72B 取得了 66.0% 的分数，均超越了同规模的其他方法，在 Qwen2.5 系列中达到了最先进水平。具体而言，OpenSWE-32B 比最强的基线 SWE-Master-32B-RL（61.4%）高出 1.0 个百分点；OpenSWE-72B 比 daVinci-Dev-72B（58.5%）高出 7.5 个百分点。实验还表明，更大模型能从高质量数据中获益更多（72B 比 32B 提升 3.6%），且性能提升在不同框架（SWE-Agent 与 OpenHands）上具有一致性。

此外，论文进行了数据规模缩放实验，结果显示 Pass@1 性能随训练步数近似呈对数线性增长（相关系数 r 在 0.882 至 0.972 之间），且未观察到性能饱和。环境来源对比实验表明，仅使用 OpenSWE 合成环境训练，在 32B SWE-Agent 设置下比使用 SWE-rebench 数据高出 12.2 个百分点（62.4% vs. 50.2%），证明了其合成环境的质量优势。混合数据源对 72B 模型有进一步增益（SWE-Agent 达 68.0%）。

最后，论文评估了领域外泛化能力，OpenSWE 训练显著提升了模型在数学推理（如 MATH-500 上 72B 模型提升 12.20 个百分点）和科学基准（如 SuperGPQA 上提升 8.10 个百分点）上的表现，同时代码基准（如 HumanEval+）也有大幅提升。

### Q5: 有什么可以进一步探索的点？

该论文构建了大规模、高质量的软件工程环境数据集，但其局限性和未来探索方向仍值得深入。首先，当前环境主要集中于Python语言，未来可扩展至Java、JavaScript等多语言生态，以提升代理的泛化能力。其次，环境构建依赖Docker，虽保证了可复现性，但资源消耗较大，可探索轻量级虚拟化或基于容器的动态环境生成技术。此外，论文通过多智能体流程筛选高质量环境，但难度评估标准可能较主观，未来可引入更细粒度的元数据（如代码复杂度、依赖关系）或基于学习的方法动态评估任务难度。从训练角度看，当前轨迹采样成本高昂，可研究更高效的数据增强或课程学习策略，逐步提升代理能力。最后，该工作展示了跨领域的能力迁移，但其机理尚不明确，未来可深入分析代码训练对数学、科学推理的促进作用，为构建通用智能体提供新思路。

### Q6: 总结一下论文的主要内容

这篇论文提出了OpenSWE框架，旨在解决训练软件工程（SWE）智能体时面临的大规模、可执行、可验证环境数据稀缺的问题。现有开源数据集规模有限且多样性不足，而工业解决方案又不透明，阻碍了学术研究。为此，作者构建了daVinci-Env，这是一个完全开源的Python SWE智能体训练框架，其核心贡献是创建了包含45,320个可执行Docker环境（覆盖12.8k个代码仓库）的大规模数据集，并开源了所有Dockerfile、评估脚本和基础设施以确保可复现性。

方法上，论文设计了一个在多节点分布式集群上运行的多智能体合成流水线，自动化完成仓库探索、Dockerfile构建、评估脚本生成和迭代测试分析。更重要的是，作者提出了一套以质量为中心的过滤流程，用于评估每个环境的固有难度，过滤掉不可解决或挑战性不足的实例，只保留能最大化学习效率的高质量环境。该项目总投资约147万美元，最终从约9000个质量有保证的环境中精选出约13000条训练轨迹。

主要结论显示，基于OpenSWE训练出的OpenSWE-32B和OpenSWE-72B模型在SWE-bench Verified基准上分别达到62.4%和66.0%的准确率，在Qwen2.5系列中实现了最先进性能。此外，专注于SWE的训练还带来了显著的跨领域能力提升，如在数学推理和科学基准上分别有最高12分和5分的进步，且未损害事实回忆能力。这证明了大规模、高质量、可执行的SWE环境对于训练通用能力强大的智能体具有重要意义。
