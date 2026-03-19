---
title: "Post-Training Local LLM Agents for Linux Privilege Escalation with Verifiable Rewards"
authors:
  - "Philipp Normann"
  - "Andreas Happe"
  - "Jürgen Cito"
  - "Daniel Arp"
date: "2026-03-18"
arxiv_id: "2603.17673"
arxiv_url: "https://arxiv.org/abs/2603.17673"
pdf_url: "https://arxiv.org/pdf/2603.17673v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Training"
  - "Reinforcement Learning"
  - "Tool Use"
  - "Security Agent"
  - "Post-Training"
  - "Local LLM"
  - "Multi-Step Reasoning"
  - "Benchmarking"
relevance_score: 8.0
---

# Post-Training Local LLM Agents for Linux Privilege Escalation with Verifiable Rewards

## 原始摘要

LLM agents are increasingly relevant to research domains such as vulnerability discovery. Yet, the strongest systems remain closed and cloud-only, making them resource-intensive, difficult to reproduce, and unsuitable for work involving proprietary code or sensitive data. Consequently, there is an urgent need for small, local models that can perform security tasks under strict resource budgets, but methods for developing them remain underexplored. In this paper, we address this gap by proposing a two-stage post-training pipeline. We focus on the problem of Linux privilege escalation, where success is automatically verifiable and the task requires multi-step interactive reasoning. Using an experimental setup that prevents data leakage, we post-train a 4B model in two stages: supervised fine-tuning on traces from procedurally generated privilege-escalation environments, followed by reinforcement learning with verifiable rewards. On a held-out benchmark of 12 Linux privilege-escalation scenarios, supervised fine-tuning alone more than doubles the baseline success rate at 20 rounds, and reinforcement learning further lifts our resulting model, PrivEsc-LLM, to 95.8%, nearly matching Claude Opus 4.6 at 97.5%. At the same time, the expected inference cost per successful escalation is reduced by over 100x.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在安全任务（特别是漏洞发现）领域应用时面临的**部署瓶颈和效率问题**。研究背景是，尽管基于LLM的系统（如AIxCC、CyberGym）已展现出在真实软件中发现漏洞的潜力，但当前最强大的系统通常是**封闭、云端专用**的（如闭源代码、专有模型）。这导致它们**资源消耗大、难以复现**，并且无法处理涉及专有代码或敏感数据的任务，因为数据不能离开本地信任边界。

现有方法的不足主要体现在：**缺乏高效、可本地部署的小型开源模型**来执行需要多步交互推理的安全任务。虽然存在一些本地模型，但其在复杂安全任务（如Linux权限提升）上的可靠性和效率与前沿云端API系统存在显著差距。

因此，本文要解决的核心问题是：**能否通过后训练（post-training）方法，显著缩小小型本地开源模型与前沿云端系统在安全任务性能上的差距，同时实现高效率、低成本、可复现且能保护数据主权（data sovereignty）的本地化部署？** 论文以**Linux权限提升**这一具体任务作为验证平台，因为其成功与否可自动验证，且需要多步推理和工具使用的交互循环。作者提出了一种两阶段后训练流程（监督微调+基于可验证奖励的强化学习），旨在将一个40亿参数的开源模型训练成能在严格交互预算内高效完成任务的本地化智能体（PrivEsc-LLM），并评估其是否能在性能上接近顶级云端模型（如Claude Opus），同时大幅降低每次成功推理的预期成本。

### Q2: 有哪些相关研究？

本文的相关研究可分为以下几类：

**1. 渗透测试领域的LLM智能体研究**：已有工作证实LLM能在攻防安全循环中发挥作用，但存在依赖云端大模型、未严格隔离数据泄露风险、缺乏严格回合预算评估等局限。例如，Happe和Cito早期探索了LLM在权限提升中的规划与交互能力；PentestGPT设计了多模块自交互LLM并建立了真实渗透测试基准。与本文最相关的是Happe等人的研究，他们构建了端到端的Linux权限提升基准，本文以此为基础，但进一步专注于对小规模开源模型进行本地化后训练，并采用了更严格的基于回合预算和重复运行的评估协议。

**2. 网络安全基准与评估方法**：现有基准（如CyBench、AutoPenBench、CyberGym）通常追求任务广度，而非本文研究的严格资源预算场景。它们大多未围绕单次运行的严格交互预算设计，未将防数据泄露泛化作为核心约束，且常报告单次或少数几次的最佳通过率，未能区分真实能力差异与采样方差。本文则聚焦于主机级Linux权限提升这一可自动验证成功的任务，从而能够定义清晰的奖励信号和直接反映操作约束的预算化核心指标。

**3. 基于可验证奖励的后训练方法**：可验证奖励的强化学习（RLVR）在数学和编程等可自动验证正确的任务上已被证明能提升多步推理能力。与依赖人类反馈的RLHF相比，RLVR在本文任务中更具优势，因为环境本身（如是否获得root权限、回合数）即可提供任务 grounded 的反馈，避免了偏好收集的模糊性。CTF-Dojo相关工作展示了在容器化环境中基于执行验证轨迹进行监督微调（SFT）的有效性，但未使用RL。据本文所知，尚无工作将RLVR应用于交互式安全任务。本文填补了这一空白，将RLVR应用于一个成功可自动验证、且回合数是主要约束的主机利用循环中。

**4. 实践中的LLM辅助漏洞发现**：如AIxCC等项目已证明自主网络推理系统能在真实代码库中发现和修补漏洞，展现了LLM辅助漏洞研究的实际可行性。随着能力成熟，推理成本、数据主权和严格回合预算下的交互效率等部署约束成为限制因素，这正是本文直接研究的范畴。

### Q3: 论文如何解决这个问题？

论文通过一个两阶段的后训练流程来解决本地LLM在Linux权限提升任务中性能不足的问题。核心方法包括监督微调（SFT）和基于可验证奖励的强化学习（RLVR）。

整体框架围绕一个交互式代理环境构建。代理在隔离的Docker容器中运行，初始为低权限用户，目标是通过多轮交互获得root权限。环境仅提供两个工具接口：`exec_command`（执行任意shell命令）和`test_credentials`（验证凭证）。这种设计创造了巨大的动作空间，因为命令字符串是开放式的。代理的策略预期是一个两阶段循环：先执行侦察命令发现漏洞或攻击路径，再进行针对性利用和root验证。

主要模块与流程如下：
1. **数据生成与泄漏控制**：使用程序化生成的训练场景（涵盖10类权限提升漏洞），确保与静态评估基准（12个场景）无重叠。通过随机化用户名、密码等具体字符串，强制模型学习攻击模式而非记忆固定内容。严格的数据过滤机制防止解决方案泄露。
2. **监督微调阶段**：使用一个大型开放权重模型作为“教师”，在程序化环境中收集成功的交互轨迹。经过质量过滤后，得到1000条训练轨迹和100条验证轨迹。在此基础上，采用LoRA适配器对4B参数的基础模型进行高效微调，使模型初步掌握基本的权限提升策略。
3. **强化学习阶段**：采用异步离策略算法（AIPO）进行训练，以应对交互轨迹采样成本高的问题。关键创新在于设计了**可验证且具形的奖励函数**，该函数不仅奖励最终成功（`R_out`），还奖励快速成功（`R_speed`，鼓励在更少轮次内完成）、奖励多样化的初始侦察（`R_recon`），并惩罚不良行为，如重复命令、工具调用失败、轮次无动作或推理内容过少（`R_pen`）。这些奖励项直接针对预算受限的交互行为进行优化，而不仅仅是最终结果。

创新点在于：
- **两阶段后训练流程**：结合SFT快速获得基础能力，再通过RLVR在自我诱导的状态分布中进行优化，解决了模仿学习中的分布偏移问题。
- **程序化训练与严格防泄漏**：确保模型泛化能力，避免对评估基准的过拟合。
- **针对安全任务设计的可验证奖励**：将领域知识（如侦察重要性、效率要求）编码进奖励函数，引导模型学习有效的多步推理和攻击模式。
- **高效的异步RL训练**：适应交互成本高的环境，在稳定性和训练效率间取得平衡。

最终，该方法使一个4B的本地模型在12个场景的基准测试上达到了95.8%的成功率，接近顶级闭源模型，同时将每次成功提升的预期推理成本降低了超过100倍。

### Q4: 论文做了哪些实验？

实验设置方面，论文采用了两阶段后训练流程：首先对基础模型进行监督微调（SFT），然后进行基于可验证奖励的强化学习（RL）。所有训练均使用LoRA适配器，仅增加1775万个可训练参数（占40.4亿基础模型的0.44%）。SFT阶段使用1个H100 GPU和QLoRA进行；RL阶段使用4个H100 GPU和Prime-RL框架，从SFT检查点初始化，训练1000步。

数据集与基准测试方面，训练数据来自程序化生成的权限提升环境轨迹。评估在一个包含12个静态Linux权限提升场景的保留基准上进行，每个模型在每个场景运行10次（共120次），每次运行最多60轮交互。主要评估指标是在20轮预算内的成功率 \(P(root\mid R{=}20)\)，并报告威尔逊95%置信区间。

对比方法包括：未经修改的40亿参数本地基线模型（Qwen3-4B-Instruct-2507）、仅SFT的模型、SFT+RL的最终模型（PrivEsc-LLM），以及作为API对比的DeepSeek-V3.2和Claude Opus 4.6。此外还引用了传统工具（Traitor, pwncat-cs）和人类基线的历史数据。

主要结果如下：在20轮预算下，基线模型成功率为42.5%，SFT模型提升至80.8%，RL后训练模型达到95.8%，接近Claude Opus的97.5%。在5轮预算下，RL模型甚至略微领先于Claude。RL模型在12个场景中的10个实现了10/10的完美成功率，仅在“Sudo GTFOBins”（6/10）和“Docker组逃逸”（9/10）场景存在部分失败。成本方面，RL模型每次成功提权的推理成本约为0.005美元，相比Claude的0.62美元降低了超过100倍；即使分摊约269.41美元的一次性训练成本，在重复使用后总成本仍远低于API方案。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要体现在以下几个方面：首先，研究仅基于单一基础模型架构（Qwen2.5-4B），其方法在其他模型家族上的泛化能力尚未验证。其次，强化学习训练阶段仍需消耗大量计算资源（4张H100 GPU训练约29小时），尚未实现真正的“平民硬件”友好。此外，实验环境依赖于程序化生成的权限提升场景，未能覆盖现实世界中复杂多变的长尾漏洞路径，且评估过程可能存在终端输出截断等伪影。最后，研究使用了固定的系统提示词，未量化不同提示词对模型性能的影响。

未来研究方向可围绕以下几点展开：一是将可验证奖励的后训练范式推广至其他安全领域，如漏洞复现、补丁验证、回归测试等，以检验其通用性。二是探索模块化智能体架构，让一个共享基础模型加载不同阶段的适配器（如侦察、漏洞利用选择、验证），提升任务执行的灵活性和效率。三是研究如何在更低的计算成本下实现有效的后训练，例如通过参数高效微调技术或改进强化学习算法。四是构建更贴近真实世界的复杂评估环境，以测试模型在开放场景中的鲁棒性。这些探索有望将本研究从一个成功的权限提升案例，拓展为可审计、本地化安全智能体的通用蓝图。

### Q6: 总结一下论文的主要内容

该论文针对当前LLM智能体在漏洞发现等安全研究领域面临的挑战——即最强系统多为闭源且依赖云端，导致资源消耗大、难以复现、不适用于处理敏感数据——提出了一种两阶段后训练方法，旨在开发能在严格资源预算下执行安全任务的小型本地模型。研究聚焦于Linux权限提升这一具体问题，其成功可自动验证且需要多步交互推理。

方法上，作者设计了一个防止数据泄露的实验设置，对一个40亿参数模型进行两阶段后训练：首先，在程序化生成的权限提升环境轨迹上进行监督微调；随后，使用可验证的奖励进行强化学习。主要结论显示，在包含12个Linux权限提升场景的保留基准测试中，仅监督微调就能在20轮内将基线成功率提升一倍以上，而强化学习进一步将最终模型PrivEsc-LLM的成功率提升至95.8%，几乎与Claude Opus（97.5%）相当。同时，每次成功权限提升的预期推理成本降低了超过100倍。

该工作的核心贡献在于，首次系统性地探索并验证了通过后训练流程开发高效本地安全智能体的可行性，为解决闭源云端模型的局限性提供了有效路径，显著降低了资源门槛并提升了任务性能。
