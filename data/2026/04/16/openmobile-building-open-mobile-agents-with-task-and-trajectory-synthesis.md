---
title: "OpenMobile: Building Open Mobile Agents with Task and Trajectory Synthesis"
authors:
  - "Kanzhi Cheng"
  - "Zehao Li"
  - "Zheng Ma"
  - "Nuo Chen"
  - "Jialin Cao"
  - "Qiushi Sun"
  - "Zichen Ding"
  - "Fangzhi Xu"
  - "Hang Yan"
  - "Jiajun Chen"
  - "Anh Tuan Luu"
  - "Jianbing Zhang"
  - "Lewei Lu"
  - "Dahua Lin"
date: "2026-04-16"
arxiv_id: "2604.15093"
arxiv_url: "https://arxiv.org/abs/2604.15093"
pdf_url: "https://arxiv.org/pdf/2604.15093v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.CV"
  - "cs.HC"
tags:
  - "Mobile Agent"
  - "Data Synthesis"
  - "Imitation Learning"
  - "Benchmark Evaluation"
  - "Open Source"
  - "Vision-Language Model"
  - "Task Synthesis"
  - "Trajectory Synthesis"
relevance_score: 9.0
---

# OpenMobile: Building Open Mobile Agents with Task and Trajectory Synthesis

## 原始摘要

Mobile agents powered by vision-language models have demonstrated impressive capabilities in automating mobile tasks, with recent leading models achieving a marked performance leap, e.g., nearly 70% success on AndroidWorld. However, these systems keep their training data closed and remain opaque about their task and trajectory synthesis recipes. We present OpenMobile, an open-source framework that synthesizes high-quality task instructions and agent trajectories, with two key components: (1) The first is a scalable task synthesis pipeline that constructs a global environment memory from exploration, then leverages it to generate diverse and grounded instructions. and (2) a policy-switching strategy for trajectory rollout. By alternating between learner and expert models, it captures essential error-recovery data often missing in standard imitation learning. Agents trained on our data achieve competitive results across three dynamic mobile agent benchmarks: notably, our fine-tuned Qwen2.5-VL and Qwen3-VL reach 51.7% and 64.7% on AndroidWorld, far surpassing existing open-data approaches. Furthermore, we conduct transparent analyses on the overlap between our synthetic instructions and benchmark test sets, and verify that performance gains stem from broad functionality coverage rather than benchmark overfitting. We release data and code at https://njucckevin.github.io/openmobile/ to bridge the data gap and facilitate broader mobile agent research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决移动智能体（Mobile Agent）研究领域因高质量训练数据封闭而导致的“数据鸿沟”和“方法黑箱”问题。研究背景是，基于视觉-语言模型（VLM）的移动智能体在自动化执行手机任务方面取得了显著进展，例如在AndroidWorld基准测试上接近70%的成功率。然而，这些领先的系统（如Step-GUI、MAI-UI等）均未公开其用于训练的任务指令和轨迹数据，也未披露其数据合成方法。这使得开源社区只能依赖有限的公开数据集（如AndroidControl），性能远落后于闭源系统（约30%成功率），且无法深入理解驱动高性能与泛化能力的关键数据属性，严重阻碍了该领域的可复现性、可研究性和进一步发展。

现有方法存在两个主要不足：第一，在任务指令合成方面，现有方法通常将环境探索与指令生成耦合，即基于单条探索轨迹作为上下文来生成任务，这严重限制了任务指令的多样性和复杂性。第二，在轨迹数据收集方面，标准的专家轨迹蒸馏方法只能让智能体模仿理想行为，缺乏从错误中恢复的示范数据，导致训练与测试之间存在性能差距；而自我进化方法则收敛慢且受限于学习者当前的能力上限。

因此，本文的核心目标是构建一个开源的框架OpenMobile，以系统性地合成高质量、大规模的移动智能体训练数据（任务指令与执行轨迹），从而弥合数据鸿沟。具体要解决两个核心挑战：1）如何在动态移动环境中规模化地生成多样化且高质量的任务指令；2）如何收集包含有效纠错信号的智能体轨迹数据，以提升智能体的鲁棒性和泛化能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：数字智能体与视觉语言模型，以及图形用户界面（GUI）数据合成。

在**数字智能体与视觉语言模型**方面，早期研究利用大语言模型（LLMs）与结构化界面表示（如无障碍树）交互，或通过编码构建智能体框架。随着视觉语言模型（VLMs）的发展，研究转向以视觉为中心的端到端GUI智能体，它们以原始屏幕截图作为输入，执行点击、键入等类人操作。其中，闭源的专有系统（如Operator、Anthropic's Computer-Use）利用前沿基础模型取得了优异性能；而开源模型如UI-TARS通过GUI预训练、轨迹微调和在线强化学习树立了里程碑。近期产业界进一步提升了移动智能体性能，但其依赖的大规模合成任务指令与轨迹数据及合成方法并未公开。相比之下，开源社区依赖如AndroidControl、AMEX等人工标注数据集，这些数据存在标注噪声且缺乏丰富的思维模式，导致训练出的模型（如ScaleCUA、UI-S1）性能存在瓶颈。

在**GUI数据合成**方面，为克服人工标注成本高的问题，研究关注自动化合成任务指令与动作轨迹。早期方法采用任务驱动范式，利用强语言模型从种子指令和应用描述生成任务，但缺乏真实环境基础，易产生笼统或不可行的指令。这推动了交互驱动方法的发展，如OS-Genesis通过随机游走轨迹反向推断有意义任务指令，NNetNav结合探索策略与修剪标注器构建复杂网页演示。后续研究通过更结构化探索和复杂指令生成管道推进了这一范式，但这些方法中探索与指令生成紧密耦合，限制了多样性。在获取任务指令后，收集高质量轨迹的普遍方法是专家蒸馏（由强智能体模型生成轨迹并经验证器过滤），或通过自进化（智能体迭代执行任务并在成功轨迹上重新训练）来提升性能。

**本文工作（OpenMobile）与这些研究的区别与关系在于**：1) 在任务合成上，不同于现有方法从单一局部轨迹生成指令，本文先通过探索构建全局环境记忆，并利用短长期记忆检索合成多样、复杂且环境基础扎实的指令，提升了指令的多样性和可行性。2) 在轨迹生成上，本文提出策略切换的rollout方法，通过在学习者和专家模型间交替，捕获标准模仿学习中常缺失的关键错误恢复数据，而非单纯依赖专家蒸馏或自进化。3) 本文旨在填补开源数据合成方法的空白，通过公开数据与代码，试图弥合与闭源系统在性能上的差距，并验证其性能提升源于广泛的功能覆盖而非对基准测试的过拟合。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为OpenMobile的开源数据合成框架来解决移动智能体训练数据缺乏的问题。该框架的核心目标是生成高质量的任务指令和智能体轨迹，以弥合开源与闭源模型之间的性能差距。其整体方法分为两个关键组成部分：任务合成流水线和策略切换轨迹生成。

在任务合成方面，论文提出了一个解耦的三阶段流水线，以生成多样且接地气的任务指令。首先，通过环境探索（如随机游走）收集应用内的交互轨迹。其次，构建全局环境记忆：利用感知哈希对相似屏幕进行聚类，形成唯一屏幕集合，并通过视觉语言模型提取每个屏幕上的UI元素功能描述，最终构建一个结构化的、可查询的全局记忆，其中包含屏幕、邻居关系及功能集。最后，进行记忆增强的任务合成：对于每个候选屏幕，结合其自身功能、邻居屏幕的短期记忆以及通过语义检索获得的跨屏幕长期记忆，形成生成上下文。使用视觉语言模型基于此上下文生成组合性任务指令，并经过质量过滤和去重得到最终指令集。这一方法的创新点在于将探索与生成解耦，并利用全局记忆促进跨功能组合，从而突破了传统方法中指令多样性受限于单条轨迹的局限。

在轨迹生成方面，论文提出了策略切换 rollout 方法，以收集包含错误恢复信号的高质量训练轨迹。该方法交替使用专家策略和学习者策略来执行任务： rollout 通常由学习者策略开始，通过一个监控器实时跟踪执行进度；当检测到学习者偏离正确路径时，则切换至专家策略进行干预和纠正。这样生成的轨迹既包含了学习者可能犯的错误，也包含了专家的纠正行为，从而提供了标准模仿学习中缺失的关键错误恢复数据。与简单的随机切换或纯专家蒸馏、纯自我演化相比，这种基于错误干预的策略切换能更有效地生成连贯且富含学习信号的轨迹。

整体上，OpenMobile框架的创新在于其系统性的数据合成方法：通过解耦的、记忆增强的任务合成确保指令的多样性和功能性覆盖；通过策略切换的轨迹生成确保训练数据包含关键的纠错经验。最终，使用该框架合成的数据训练的智能体在多个移动基准测试上取得了具有竞争力的性能，验证了其有效性。

### Q4: 论文做了哪些实验？

论文在三个动态移动代理基准测试上进行了实验，以评估所提出的OpenMobile框架生成的数据的有效性。实验设置方面，作者使用LLaMA-Factory工具，以监督微调（SFT）方式训练了两个基础模型：Qwen2.5-VL-7B和Qwen3-VL-8B，批大小为32，学习率为1e-5，训练3个周期。训练数据来自策略切换策略生成的轨迹，仅保留专家步骤，但将包括学习者错误在内的完整交互历史作为上下文，以让模型接触真实的错误恢复场景。此外，论文还尝试了强化学习（RL），但发现其在动态基准上未带来显著超越SFT的改进。

使用的数据集/基准测试包括：1) **AndroidWorld**：主导性移动代理评估基准，包含20个真实应用的116个任务，通过参数化模板生成多样变体；2) **AndroidLab**：系统性基准，涵盖9个应用的138个任务；3) **MobileWorld**：更具挑战性的新基准，专注于长视野和跨应用工作流，实验使用其GUI-only子集，包含20个应用的201个任务。

对比方法分为三类：商业模型（如GPT-4o、Gemini-3-Pro）、开源权重模型（如UI-Venus-7B、Step-GUI-8B、MAI-UI-8B等）以及开源数据模型（如UI-S1-7B、ScaleCUA-7B）。主要结果以Pass@1和Pass@3为指标。关键数据指标显示：在AndroidWorld上，微调后的Qwen2.5-VL-7B模型达到51.7% Pass@1和68.1% Pass@3，Qwen3-VL-8B模型达到64.7% Pass@1和78.0% Pass@3，远超其他开源数据方法（如ScaleCUA-7B的27.2% Pass@1），并与领先的闭源数据系统（如MobileAgent-v3.5-8B的71.6% Pass@1）具有竞争力。在AndroidLab和MobileWorld上，OpenMobile模型也表现出显著提升，例如Qwen3-VL-8B在AndroidLab上达到51.5% Pass@1，在MobileWorld上达到17.7% Pass@1，证明了其良好的泛化能力。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其局限性及未来可探索的方向主要体现在以下几个方面。首先，OpenMobile 的合成数据虽然覆盖了广泛的功能，但其质量和多样性仍依赖于初始探索轨迹和全局环境记忆的构建。若探索不充分或环境记忆有偏差，可能限制指令的复杂性和真实性。其次，策略切换机制虽能丰富错误恢复数据，但专家模型的性能上限和切换时机的启发式规则可能影响数据收集效率，未来可研究更智能的自适应切换策略。

未来研究可朝以下方向深入：一是提升任务合成的自动化与泛化能力，例如引入强化学习让智能体在探索中主动学习新功能，或跨应用、跨平台合成指令，以降低对特定环境集的依赖。二是增强轨迹合成的样本效率，当前方法需要大量交互数据，可探索用世界模型或离线强化学习来减少真实交互成本。三是深入理解功能覆盖与性能的关系，论文指出高覆盖驱动性能提升，但未量化不同功能的重要性差异，未来可构建功能依赖图来优先合成关键路径。此外，可探索将合成框架扩展至更复杂的多模态交互场景，如跨设备任务或与现实世界的物理交互，推动移动智能体向通用助手发展。

### Q6: 总结一下论文的主要内容

该论文提出了OpenMobile，一个开源的移动智能体数据合成框架，旨在解决现有领先移动智能体系统训练数据封闭、任务与轨迹合成方法不透明的问题。其核心贡献在于设计了一个可扩展的任务合成流程：首先通过探索构建全局环境记忆，并基于此生成多样且 grounded 的指令；其次，采用策略切换的轨迹生成方法，通过在学习者和专家模型间交替执行，捕获标准模仿学习中常缺失的关键错误恢复数据。实验表明，使用该框架合成数据训练的智能体在多个动态移动环境基准测试中取得了有竞争力的性能，例如微调后的Qwen2.5-VL和Qwen3-VL在AndroidWorld上分别达到51.7%和64.7%的成功率，大幅超越了现有开源数据方法。论文通过透明分析证实，性能提升源于广泛的功能覆盖和增强的错误恢复能力，而非对测试集的过拟合。该工作通过开源数据和代码，旨在弥合数据鸿沟，为更广泛的移动智能体研究奠定基础。
