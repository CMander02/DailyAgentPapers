---
title: "Qwen3-Coder-Next Technical Report"
authors:
  - "Ruisheng Cao"
  - "Mouxiang Chen"
  - "Jiawei Chen"
  - "Zeyu Cui"
  - "Yunlong Feng"
date: "2026-02-28"
arxiv_id: "2603.00729"
arxiv_url: "https://arxiv.org/abs/2603.00729"
pdf_url: "https://arxiv.org/pdf/2603.00729v1"
categories:
  - "cs.CL"
tags:
  - "Code & Software Engineering"
  - "Learning & Optimization"
relevance_score: 9.0
taxonomy:
  capability:
    - "Code & Software Engineering"
    - "Learning & Optimization"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "Qwen3-Coder-Next"
  key_technique: "Agentic training with large-scale synthesis of verifiable coding tasks and executable environments, learning from environment feedback via mid-training and reinforcement learning"
  primary_benchmark: "SWE-Bench, Terminal-Bench"
---

# Qwen3-Coder-Next Technical Report

## 原始摘要

We present Qwen3-Coder-Next, an open-weight language model specialized for coding agents. Qwen3-Coder-Next is an 80-billion-parameter model that activates only 3 billion parameters during inference, enabling strong coding capability with efficient inference. In this work, we explore how far strong training recipes can push the capability limits of models with small parameter footprints. To achieve this, we perform agentic training through large-scale synthesis of verifiable coding tasks paired with executable environments, allowing learning directly from environment feedback via mid-training and reinforcement learning. Across agent-centric benchmarks including SWE-Bench and Terminal-Bench, Qwen3-Coder-Next achieves competitive performance relative to its active parameter count. We release both base and instruction-tuned open-weight versions to support research and real-world coding agent development.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前代码智能体（coding agents）在现实部署中面临的核心矛盾：如何在保持强大代码生成与问题解决能力的同时，实现高效的推理与低成本部署。研究背景是，随着大语言模型在代码任务上的应用日益深入，开发能够进行长程推理、与环境交互并从多步骤失败中恢复的智能体成为关键需求。然而，现有方法主要依赖静态代码数据进行训练，缺乏从可执行环境反馈中学习的能力，这限制了智能体在复杂、动态的真实开发场景中的适应性和鲁棒性。

现有方法的不足主要体现在两个方面：一是传统训练范式依赖于大规模但静态的代码数据，无法为智能体提供足够的、可验证的交互式学习信号，导致其在需要多步操作、工具使用和错误恢复的实际任务中表现不佳；二是追求高性能的模型往往参数规模巨大，激活参数量高，导致推理速度慢、部署成本高昂，难以满足生产环境对延迟、吞吐量和成本的实际约束。

本文要解决的核心问题是：能否通过强化训练方法而非单纯扩大模型规模，来显著提升代码智能体的能力，同时保持模型推理时的高效性。为此，论文提出了Qwen3-Coder-Next模型，其总参数量为800亿，但每次推理仅激活30亿参数，采用混合专家（MoE）架构。核心创新在于构建了一个大规模的智能体训练框架，通过合成可验证的编码任务并配以可执行环境，使模型能够直接从环境反馈中学习（包括训练中期的适应和强化学习），从而掌握多步代码编辑、工具使用和故障恢复等智能体行为。最终目标是得到一个在保持小参数激活足迹的前提下，在SWE-Bench等智能体中心基准上具备竞争力的高效、可部署模型，推动现实世界代码智能体的发展。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、应用类和评测类。在方法类方面，相关工作包括基于静态代码数据预训练的大型语言模型（如Code Llama、StarCoder），以及采用专家混合（MoE）架构的高效模型（如Mixtral、Qwen-MoE）。本文的Qwen3-Coder-Next同样采用MoE设计，但重点在于通过可验证的、可执行的任务合成与环境交互进行“智能体训练”，直接从环境反馈中学习，这区别于传统仅依赖静态数据的方法。在应用类方面，现有研究聚焦于代码生成、编辑和软件工程智能体（如SWE-Agent、OpenDevin），本文则通过分阶段训练（持续预训练、监督微调、专家蒸馏）构建统一模型，覆盖软件工程、Web开发等多领域，强调在现实开发设置中的多步骤推理与故障恢复能力。评测类方面，基准如SWE-Bench、Terminal-Bench被广泛用于评估编码智能体性能；本文在这些基准上进行了全面评估，并强调模型在有限激活参数（30亿）下的竞争力，与更大计算规模的模型相比，突出了训练配方而非单纯模型规模对提升能力的关键作用。

### Q3: 论文如何解决这个问题？

论文通过一个多层次、系统化的训练框架来解决提升代码智能体能力的问题，其核心是结合大规模、可验证的任务合成与高效执行反馈的“智能体训练”。整体方法分为三个关键阶段：任务合成与扩展、中期训练以及后训练优化。

**1. 核心方法：大规模可验证任务合成与执行框架**
为了解决训练数据规模与质量的挑战，论文设计了双管齐下的任务合成管道。首先，**从GitHub真实拉取请求中挖掘软件工程问题**，通过一个专门的环境构建智能体，将每个PR分解为有bug的状态、对应的修复和测试补丁，并封装成可执行的Docker环境。其次，**基于现有开源数据集进行扩展合成**，在已有的可执行代码库中，通过模型驱动重写、语义扰动和基于规则的转换，系统性地注入受控的bug并生成对应的任务描述。这两种方法共同生成了约80万个涵盖9种编程语言的可验证任务。为了支撑大规模并行执行，团队开发了内部编排系统**MegaFlow**，这是一个基于云原生Kubernetes的框架，将每个智能体任务表达为包含“智能体推演、评估、后处理”三个阶段的工作流，实现了高效的长程交互与反馈。

**2. 架构设计与关键技术：分阶段模型训练**
*   **中期训练**：从预训练的Qwen3-Next基础模型出发，进行针对性调整。训练数据以**自然数据为主**（大规模GitHub源代码、文本-代码对齐数据），辅以**精心设计的合成数据**。关键创新包括：
    *   **仓库级代码理解**：将训练上下文长度扩展到262,144个token，并强调跨文件依赖关系，使用特殊token串联仓库数据，实验多种序列化格式以提升泛化能力。
    *   **数据质量提升**：利用大模型重写网络文档，去除噪音并格式化为规范的Markdown，实验证明这显著提升了模型在多个基准测试上的性能。
    *   **合成数据构建**：包括基于GitHub PR构建的单轮编辑任务，以及利用多种智能体框架（如SWE-agent、OpenHands）生成的多轮智能体编码轨迹。
    *   **训练优化技术**：采用**最佳拟合打包**策略处理长文档，避免上下文幻觉；对高度重复的代码段进行掩码，提升训练效率；并引入**填空中间**目标以增强代码编辑能力。

*   **后训练**：包含监督微调、专家模型训练和强化学习。
    *   **监督微调**：使用高质量SFT数据，并引入**基于执行的验证过滤**：通过一个用户模拟器智能体执行模型生成的代码，根据环境反馈（编译输出、运行时错误等）过滤无效或幻觉解决方案，确保训练数据的可执行性和有效性。
    *   **专家模型与工具调用泛化**：训练针对特定领域（如Web开发）的专家模型。一个关键创新是**工具调用格式的多样化训练**。为了解决不同IDE/CLI框架工具调用格式各异导致的泛化难题，论文在训练中引入了多样化的工具聊天模板（包括JSON、XML风格的自定义格式qwen3_coder等），使模型学习格式无关的工具使用行为，而非记忆单一结构。实验表明，增加训练中使用的模板数量能持续提升模型在SWE-bench等基准上的表现和对新格式的鲁棒性。
    *   **强化学习**：在可执行验证的领域应用RL，分为**单轮RL**（针对可直接通过单元测试验证的代码生成任务）和**多轮智能体RL**（针对需要与环境多步交互的软件工程任务）。单轮RL扩展了任务多样性，涵盖多语言编程、库使用和安全编码场景，并通过共识机制自动生成可靠的单元测试作为奖励信号。多轮RL则专注于长程交互任务，并引入了**奖励塑造**来优化中间推理和工具使用的质量，而不仅仅是最终结果。

**3. 整体创新点**
*   **数据合成与执行基础设施**：构建了从真实世界（GitHub PR）和合成扩展两个维度大规模生成**可验证、可执行**编码任务的系统化流程，并配套了高性能的云原生执行框架MegaFlow。
*   **训练策略的平衡与优化**：在中期训练中平衡自然数据与合成数据，既保持通用能力又引入必要的任务分布；采用BFP、重复掩码等技术提升长上下文训练效率。
*   **工具调用格式泛化**：通过训练时暴露给模型多样化的工具调用模板，显著提升了智能体在真实世界各种IDE/CLI环境中遵循不同格式指令的鲁棒性和泛化能力。
*   **扩展的强化学习范式**：将执行驱动的RL从传统的竞技编程扩展到更广泛的现实编码任务（多语言、库使用、安全），并应用于多轮交互场景，利用奖励塑造提升中间步骤质量。

总之，论文通过构建大规模可验证任务库、设计分阶段且优化的训练流程（特别是强调工具调用格式泛化和扩展的RL），以及配套强大的执行基础设施，系统地提升了代码智能体在复杂、交互式软件工程任务上的能力。

### Q4: 论文做了哪些实验？

论文在实验部分主要围绕模型训练和评估展开，涵盖了实验设置、数据集、对比方法和关键结果。

**实验设置与数据集**：研究采用大规模合成可验证的编程任务进行智能体训练，包括从GitHub拉取请求（PRs）中挖掘真实软件工程问题，并构建可执行的Docker环境；同时基于SWE-Smith等现有开源数据集合成新任务，共生成约80万个涵盖9种编程语言的可验证任务。训练分为中期训练（mid-training）和后训练（post-training）阶段：中期训练使用混合数据（自然数据如GitHub代码和文本-代码对齐数据，辅以合成数据），上下文长度扩展至262,144令牌，并采用填充中间（FIM）目标；后训练包括监督微调（SFT）和强化学习（RL），SFT数据来自内部专有语料、已验证的智能体轨迹和文档 grounded QA，RL则针对单轮编程任务和多轮智能体交互进行优化。

**基准测试与对比方法**：评估主要在智能体中心基准上进行，包括SWE-Bench（Verified和Multilingual版本）和Terminal-Bench。对比方法涉及多个先进模型，如GPT-5-2、Claude-sonnet-4-5、Gemini-3-pro、Deepseek-v3.2、GLM系列、MiniMax-M2.1和Kimi-K2等。论文还设计了内部基准来评估工具调用格式的遵循能力，覆盖多种IDE/CLI框架（如Qwen-Code、Cline、OpenCode等）。

**主要结果与关键指标**：Qwen3-Coder-Next在SWE-Bench Verified等基准上表现出色，相对于其激活参数量（30亿）具有竞争力。在工具调用格式遵循评估中，该模型在五个不同脚手架上的平均准确率达到92.7%，优于多数对比模型（如GPT-5-2平均49.3%，Gemini-3-pro平均87.0%），显示了强大的泛化能力。中期训练中，网络文档重格式化使模型在Evalplus基准上从54.38提升至63.09，在MultiplE基准上从36.02提升至48.35。强化学习扩展任务多样性后，多个编程子能力持续提升，验证了执行驱动奖励的有效性。

### Q5: 有什么可以进一步探索的点？

该论文在高效推理和智能体训练方面取得了显著进展，但仍存在一些局限性和可探索的方向。首先，模型虽然激活参数少，但总参数量仍达800亿，训练和存储成本较高，未来可研究更极致的稀疏化或动态激活机制，进一步降低资源需求。其次，训练依赖于大规模可执行任务合成，其多样性和真实性可能受限；可探索如何融入更多真实开发场景（如开源项目协作流）或引入人类反馈，以提升智能体的泛化性和实用性。此外，模型在多步推理和错误恢复方面仍有提升空间，未来可结合规划算法或外部记忆机制，增强长期任务处理能力。最后，评估集中于现有基准（如SWE-Bench），缺乏对复杂、开放式开发任务的测试；需构建更贴近实际需求的评估体系，推动智能体从“任务执行”向“创造性问题解决”演进。

### Q6: 总结一下论文的主要内容

本文介绍了Qwen3-Coder-Next，一个专为编码智能体设计的开放权重语言模型。其核心贡献在于探索了如何通过强化的训练方法，而非单纯扩大模型规模，来显著提升小参数量模型的编码能力。该模型采用混合专家架构，总参数量为800亿，但每次推理仅激活30亿参数，实现了高效推理与强大性能的平衡。

问题定义聚焦于如何训练能够处理长序列推理、与环境交互并从多步骤失败中恢复的现代编码智能体。方法上，研究构建了一个大规模的智能体训练框架，通过合成可验证的编码任务与可执行环境，直接从环境反馈中学习，包括训练中期的适应和强化学习。训练流程分阶段进行：从Qwen3-Next预训练基础开始，通过持续预训练转向编码和智能体领域，再进行监督微调，随后训练多个领域专家模型并蒸馏回统一模型。

主要结论显示，Qwen3-Coder-Next在SWE-Bench等智能体中心基准测试中取得了与其激活参数量相称的竞争性性能，甚至媲美或超越激活计算量高一个数量级的模型。这证明了扩展智能体训练是提升现实世界编码智能体能力的关键，模型的高效性使其特别适合对延迟、吞吐量和成本敏感的生成式编码智能体应用。
