---
title: "Gym-Anything: Turn any Software into an Agent Environment"
authors:
  - "Pranjal Aggarwal"
  - "Graham Neubig"
  - "Sean Welleck"
date: "2026-04-07"
arxiv_id: "2604.06126"
arxiv_url: "https://arxiv.org/abs/2604.06126"
pdf_url: "https://arxiv.org/pdf/2604.06126v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "Agent Environment"
  - "Computer-Use Agent"
  - "Multi-Agent System"
  - "Benchmark Creation"
  - "Long-Horizon Tasks"
  - "Tool Use"
  - "VLM"
  - "Data Synthesis"
relevance_score: 9.0
---

# Gym-Anything: Turn any Software into an Agent Environment

## 原始摘要

Computer-use agents hold the promise of assisting in a wide range of digital economic activities. However, current research has largely focused on short-horizon tasks over a limited set of software with limited economic value, such as basic e-commerce and OS-configuration tasks. A key reason is that creating environments for complex software requires significant time and human effort, and therefore does not scale. To address this, we introduce Gym-Anything, a framework for converting any software into an interactive computer-use environment. We frame environment creation itself as a multi-agent task: a coding agent writes setup scripts, downloads real-world data, and configures the software, while producing evidence of correct setup. An independent audit agent then verifies evidence for the environment setup against a quality checklist. Using a taxonomy of economically valuable occupations grounded in U.S. GDP data, we apply this pipeline to 200 software applications with broad occupational coverage. The result is CUA-World, a collection of over 10K long-horizon tasks spanning domains from medical science and astronomy to engineering and enterprise systems, each configured with realistic data along with train and test splits. CUA-World also includes CUA-World-Long, a challenging long-horizon benchmark with tasks often requiring over 500 steps, far exceeding existing benchmarks. Distilling successful trajectories from the training split into a 2B vision-language model outperforms models 2$\times$ its size. We also apply the same auditing principle at test time: a separate VLM reviews completed trajectories and provides feedback on what remains, improving Gemini-3-Flash on CUA-World-Long from 11.5% to 14.0%. We release all code, infrastructure, and benchmark data to facilitate future research in realistic computer-use agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决计算机使用智能体（CUAs）研究与实际经济应用之间存在的巨大鸿沟。当前研究主要局限于在少数消费级软件（如基础电子商务或操作系统配置）上执行短视程任务，这些任务经济价值有限，无法代表真实世界中由复杂专业软件驱动的、高价值的经济活动。现有方法的不足在于：创建用于训练和评估智能体的真实软件环境成本极高，需要为每个软件进行安装、配置领域特定数据、设计任务和验证，通常需要数周的专家投入，这导致环境构建无法扩展。因此，现有基准测试既不真实（高分不能反映处理真实经济软件的能力），提供的训练信号也有限（短视程、少软件的任务无法产生训练实用智能体所需的多样长轨迹）。

本文要解决的核心问题是如何**规模化地构建贴近真实工作的计算机使用环境**，以用于智能体的训练和评估。为此，论文提出了Gym-Anything框架，其核心思路是将环境创建本身构建为一个多智能体任务，通过“创建-审核”循环自动将任何软件转化为交互式环境，并基于美国GDP数据选择具有高经济价值的软件。最终构建了CUA-World基准，包含覆盖广泛专业领域的上万个长视程任务，从而为开发能够处理真实专业工作的智能体提供了可扩展的解决方案和具有挑战性的评测平台。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为环境构建方法、现有评测基准以及智能体训练方法三类。

在**环境构建方法**方面，相关工作通常依赖于大量人工手动配置，例如为特定软件（如浏览器或操作系统）创建脚本和环境，这导致成本高昂且难以扩展。本文提出的Gym-Anything框架则创新性地将环境构建本身视为一个多智能体任务，通过编码智能体自动编写设置脚本并配置软件，再引入独立的审计智能体进行验证，实现了自动化、可扩展的环境创建，与手动或半自动方法形成鲜明对比。

在**现有评测基准**方面，当前研究多集中于短视界任务和有限软件（如基础电子商务或操作系统配置），例如WebShop、MiniWoB++等，这些基准覆盖的经济价值有限。本文构建的CUA-World则基于美国GDP数据选取了约200种具有高经济价值的专业软件，生成了超过1万个长视界任务，并专门设计了CUA-World-Long这一需要超过500步的挑战性基准，极大地扩展了任务的多样性、复杂性和现实经济相关性。

在**智能体训练与评估方法**方面，现有工作常使用模仿学习或强化学习在有限环境中训练智能体。本文则利用训练集中的成功轨迹进行蒸馏训练，得到了性能优于更大规模模型的2B视觉语言模型。此外，本文在测试时引入了审计原则，通过独立模型审查完成轨迹并提供反馈，从而提升了智能体的长视界任务性能，这与传统的一次性评估方法不同。

### Q3: 论文如何解决这个问题？

论文通过一个名为Gym-Anything的框架来解决大规模创建计算机使用智能体环境的核心挑战，其核心方法是将环境创建本身构建为一个多智能体任务。整体框架包含三个关键部分：一个基于GDP的软件选择流程、一个标准化的环境库抽象，以及一个创新的多智能体创建-审计循环。

首先，论文提出了一个**GDP导向的软件选择流程**，以确保所选软件具有真实的经济价值。该方法从美国职业数据出发，估算每个职业的GDP贡献，通过大语言模型（LLM）结合网络搜索发现各职业使用的软件，并将GDP按比例分解到具体软件。随后，通过可沙箱化约束（如可自托管、免费、有GUI）进行过滤，并采用分层选择策略（包括最高GDP软件、关键领域软件、各职业组代表软件等），最终从约16,600个候选软件中选出200个，确保了覆盖的广度和经济重要性。

其次，论文设计了**Gym-Anything库**作为统一的环境抽象层，以解决跨操作系统、应用类型和计算后端的环境创建难题。该库将每个环境定义为三个顺序执行的设置脚本（安装`install`、配置`configure`、任务设置`task setup`）和一个声明式配置文件。这种分层设计使得多个任务可以共享基础的安装和配置脚本，仅需修改任务特定的部分，从而实现了模块化、可缓存和高度并行化。该库提供了一个类似Gymnasium的标准API，统一了观察空间（如屏幕截图）和动作空间（键盘鼠标输入），并自动处理容器编排、显示转发和输入转换，将环境创建简化为编写脚本的任务。

最核心的创新在于**多智能体的创建-审计循环**，用于自动化、大规模地构建高质量环境。该框架包含三个智能体：
1.  **创建智能体**：作为一个编码智能体，它负责研究目标软件、下载真实数据（如医学影像数据集）、编写设置脚本，并通过实际运行和交互来验证环境。它被要求生成证据（如截图、日志）以证明设置正确。
2.  **审计智能体**：作为一个独立的对抗性智能体，它负责根据质量检查清单，严格审查创建智能体提供的证据，评估环境是否正确设置（例如，软件是否启动到正确界面、是否使用了真实数据）。审计结果会反馈给创建智能体进行修正，形成迭代改进循环。
3.  **记忆汇总智能体**：为了管理不断增长的经验知识，创建智能体将学习到的经验（如成功技巧、常见问题解决方案）记录到一个共享内存中。记忆汇总智能体定期对这些记忆进行归纳总结，将软件特定的经验提炼为通用指南，供后续任务参考，从而实现了学习积累和创建效率的次线性增长。

此外，论文还提出了一个**任务生成与验证的“提议-放大”策略**。首先，由一个具备计算机使用能力的提议智能体为每个软件创建少量高质量、高难度的种子任务。然后，由一个非智能体的大语言模型（如Gemini 3 Pro）以这些种子为示例，大规模生成更多任务，并通过语义相似性过滤和自动化VLM检查（验证起始状态与任务描述是否匹配）来保证多样性和质量。

最后，对于任务评估，论文设计了**基于特权信息的清单式VLM验证器**。每个任务的设置脚本中包含特权信息（即已知的正确答案），验证器利用这些信息生成一个细粒度的检查清单，对智能体的轨迹进行逐项评分，并包含完整性检查以防止作弊，从而实现了对长视野、多步骤任务的可靠、可部分评分的自动化评估。

通过整合这些方法，论文成功构建了CUA-World，一个包含超过1万个长视野任务、覆盖200个软件的大规模基准测试集，显著提升了计算机使用智能体研究的可扩展性和现实性。

### Q4: 论文做了哪些实验？

论文的实验主要围绕其提出的Gym-Anything框架和由此构建的CUA-World基准展开。实验设置上，核心是验证其自动化环境创建流程的有效性，并评估在此新基准上训练的智能体性能。

首先，研究应用其多智能体流程（编码智能体与审计智能体）创建了大规模环境。数据集/基准测试方面，他们基于对美国GDP数据中经济价值职业的分类，选取了200个软件应用，构建了CUA-World，包含超过1万个长视野任务，覆盖医学、天文学、工程和企业系统等领域，并配有真实数据和训练/测试集划分。其中特别提出了一个更具挑战性的子集CUA-World-Long，其任务通常需要超过500步才能完成。

在对比方法和主要结果上：1）他们从训练集成功轨迹中蒸馏知识，训练了一个20亿参数的视觉语言模型（VLM）。实验结果显示，该模型在CUA-World上的表现优于参数规模是其两倍的模型，证明了高质量、大规模任务数据对模型性能的增益。2）在测试时，他们应用了相同的审计原则，使用一个独立的VLM来审查已完成的轨迹并提供剩余任务的反馈。这一方法将Gemini-3-Flash模型在CUA-World-Long上的成功率从11.5%提升到了14.0%。关键数据指标包括：创建的软件应用数量（200个）、任务总数（>10K）、长视野基准任务步骤数（>500步）、以及通过审计反馈带来的性能提升（从11.5%到14.0%）。

### Q5: 有什么可以进一步探索的点？

基于论文内容，可以进一步探索的点包括：首先，当前框架依赖多智能体（创建与审计）自动化构建环境，但其可靠性和泛化能力仍有局限，尤其是在处理极端异构软件（如依赖特定硬件或专有协议）时可能失败。未来可研究如何增强智能体的跨软件泛化能力和错误恢复机制。其次，任务生成采用“提议-放大”模式，但种子任务的质量和多样性直接影响扩展效果，未来可探索更高效的任务合成与验证方法，例如引入人类反馈或强化学习来优化任务设计。此外，测试时审计虽能提升性能，但依赖额外模型且效率较低，未来可研究如何将审计能力内化到主智能体中，或开发更轻量的实时监控机制。最后，论文的基准虽覆盖广泛领域，但任务多基于模拟或脚本化数据，与真实动态环境仍有差距，未来可探索在实时、多用户或高安全要求的软件（如医疗或金融系统）中进行评估，并研究智能体在开放世界中的长期适应与学习能力。

### Q6: 总结一下论文的主要内容

该论文提出了Gym-Anything框架，旨在解决为计算机使用智能体（CUA）创建真实、大规模训练和评测环境的瓶颈问题。当前研究多局限于少量软件上的短视程任务，经济价值有限，而构建复杂软件环境成本高昂、难以扩展。

论文的核心贡献是设计了一个将任意软件自动转化为交互式环境的可扩展框架。其方法基于多智能体协作流程：一个创建智能体负责编写安装配置脚本、下载真实数据并设置软件，同时生成环境正确运行的证据（如截图、日志）；随后，一个独立的审计智能体根据质量检查清单验证这些证据，形成“创建-审计”循环以确保环境质量。此外，采用“提议-放大”策略高效生成大量任务：先用昂贵模型为每个软件创建少量高质量种子任务，再用廉价语言模型以这些种子为示例批量生成更多任务。

基于此框架，论文构建了CUA-World基准，覆盖约200款依据美国GDP数据选取的、具有高经济价值的专业软件，生成了超过1万个长视程任务，涵盖医学、天文、工程、企业系统等领域，并配置了真实数据及训练/测试划分。其中特别提出了一个极具挑战性的长视程基准CUA-World-Long，任务常需超过500步。实验表明，从训练轨迹蒸馏出的20亿参数视觉语言模型性能优于参数量大一倍的模型；在测试时引入审计智能体对完成轨迹提供反馈，能将Gemini-3-Flash的通过率从11.5%提升至14.0%。论文最终开源了所有代码、基础设施和基准数据，以推动面向真实经济活动的计算机使用智能体研究。
