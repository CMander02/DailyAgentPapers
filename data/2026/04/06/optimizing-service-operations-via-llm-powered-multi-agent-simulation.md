---
title: "Optimizing Service Operations via LLM-Powered Multi-Agent Simulation"
authors:
  - "Yanyuan Wang"
  - "Xiaowei Zhang"
date: "2026-04-06"
arxiv_id: "2604.04383"
arxiv_url: "https://arxiv.org/abs/2604.04383"
pdf_url: "https://arxiv.org/pdf/2604.04383v1"
categories:
  - "cs.AI"
  - "cs.MA"
  - "math.OC"
tags:
  - "Multi-Agent Simulation"
  - "LLM-Powered Agent"
  - "Service Operations"
  - "Stochastic Optimization"
  - "Decision-Dependent Uncertainty"
  - "On-Trajectory Learning"
  - "Supply Chain"
  - "Contest Design"
relevance_score: 7.5
---

# Optimizing Service Operations via LLM-Powered Multi-Agent Simulation

## 原始摘要

Service system performance depends on how participants respond to design choices, but modeling these responses is hard due to the complexity of human behavior. We introduce an LLM-powered multi-agent simulation (LLM-MAS) framework for optimizing service operations. We pose the problem as stochastic optimization with decision-dependent uncertainty: design choices are embedded in prompts and shape the distribution of outcomes from interacting LLM-powered agents. By embedding key numerical information in prompts and extracting it from LLM-generated text, we model this uncertainty as a controlled Markov chain. We develop an on-trajectory learning algorithm that, on a single simulation run, simultaneously constructs zeroth-order gradient estimates and updates design parameters to optimize steady-state performance. We also incorporate variance reduction techniques. In a sustainable supply chain application, our method outperforms benchmarks, including blackbox optimization and using LLMs as numerical solvers or as role-playing system designers. A case study on optimal contest design with real behavioral data shows that LLM-MAS is both as a cost-effective evaluator of known designs and an exploratory tool that can uncover strong designs overlooked by traditional approaches.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决服务系统设计中因人类行为复杂性而难以准确建模和优化的问题。研究背景是，服务系统（如供应链、创新竞赛、数字市场）的性能高度依赖于参与者对设计选择（如政策、激励措施）的行为反应，但人类决策常偏离传统分析模型的理性假设，受认知限制、风险感知和情境因素影响，导致基于效用理论或简化假设的模型难以捕捉真实行为。现有方法主要依赖分析模型或数据驱动校准，前者过于简化而忽略关键行为特征，后者需要昂贵且耗时的实验数据收集，且难以处理非结构化信息（如文本交流）。

本文的核心问题是：如何利用大型语言模型（LLM）模拟人类行为，构建一个多智能体仿真框架（LLM-MAS），以优化服务系统的设计参数。该方法将设计优化问题转化为决策依赖不确定性的随机优化问题，其中设计参数通过提示词嵌入影响LLM智能体的交互分布，进而影响系统级结果。论文提出了一种“在轨迹学习”算法，能在单次仿真运行中同时估计梯度并更新设计参数，优化稳态性能，还引入了方差缩减技术提升效率。通过可持续供应链管理和创新竞赛设计的案例，论文验证了LLM-MAS不仅能作为低成本的设计评估工具，还能发现传统方法忽略的高效设计方案，弥补了理论模型与复杂现实之间的差距。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：方法类、应用类与优化算法类。

在**方法类**研究中，本文与利用大语言模型（LLM）模拟人类行为以研究商业、经济和社会科学问题的文献紧密相关。例如，有工作用LLM智能体复现社交平台的随机对照试验，或构建电商沙盒环境来研究平台机制的影响。本文的贡献在于，将这类研究从**设计评估**推进到了**设计优化**，即不仅用LLM多智能体模拟（LLM-MAS）评估结果，还将其用于主动优化系统性能。

在**应用类**研究中，本文隶属于“LLM用于运筹学（OR）”这一方向。现有研究多集中于利用LLM将自然语言问题描述转化为数学规划模型（如确定性优化、鲁棒优化），再交由传统数值求解器计算。本文则不同：作者自行构建数学模型，利用LLM来模拟系统中的不确定性动态，并开发了专门针对LLM特性设计的优化算法进行求解，而非将LLM仅作为模型转换工具。

在**优化算法类**研究中，本文方法属于**零阶随机优化**范畴，适用于梯度难以获取或计算成本高昂的场景。与大多数假设随机变量分布与决策无关的经典零阶方法不同，本文处理的是**决策依赖不确定性**问题，其不确定性由受控马尔可夫链的稳态分布刻画，引入了复杂的跨期依赖性。此外，本文的“在轨学习”算法产生了具有自适应马尔可夫数据的随机逼近问题，这与通常假设能获取一阶信息的强化学习策略优化分析有所不同，本文需要在梯度难以处理的情况下进行零阶估计。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为LLM-MAS（LLM驱动的多智能体模拟）的框架来解决服务系统优化问题，其核心是将系统设计问题建模为具有决策依赖不确定性的随机优化问题，并开发了一种高效的在线学习算法进行求解。

**整体框架与架构设计**：LLM-MAS框架的核心是将服务系统建模为一个由LLM驱动的多智能体模拟环境。框架包含三个关键部分：1）一个有向图结构，定义了智能体之间的交互网络；2）一个单轮模拟算子，描述了系统状态如何随时间演变；3）一个时间范围。每个智能体由五个模块构成：角色档案、环境感知、通信、LLM行为生成器和记忆模块。系统设计参数θ被嵌入到每个智能体的提示词中，通过影响LLM的token生成概率，最终改变智能体行为分布和系统级结果ξ的分布。

**核心方法与关键技术**：论文将LLM-MAS的动态过程形式化为一个受控马尔可夫链。系统状态ξ^(t)被定义为所有智能体在每一轮交互中产生的信息集合。状态转移由模拟算子Ψ_θ驱动，该算子封装了LLM根据包含θ的提示生成行为、智能体间交互以及信息提取的整个过程。为了解决由此产生的随机优化问题，论文创新性地提出了一种“在轨迹上学习”的算法。该算法能够在单次模拟运行中，同时构建目标函数梯度的零阶估计，并更新设计参数θ以优化稳态性能。算法还结合了方差缩减技术以提高效率。关键技术包括：1）**语义接口**：通过精心设计的提示词，将数值型的设计参数θ和上下文信息嵌入到文本中，并从LLM生成的文本输出中可靠地提取出数值型动作和状态信息；2）**稳态性能聚焦**：算法优化的是系统达到均衡后的长期稳态性能，这更符合现实世界中服务设计一旦实施就难以频繁更改的特点。

**创新点**：主要创新体现在三个方面。首先，**问题建模的创新**：首次将LLM-MAS中的不确定性明确建模为设计参数θ的函数，即决策依赖不确定性，并通过受控马尔可夫链刻画其动态。其次，**优化算法的创新**：提出了高效的在线学习算法，能够利用单次模拟轨迹进行同步的梯度估计和参数更新，避免了传统黑箱优化方法需要大量独立模拟运行的高昂成本。最后，**框架的通用性与实用性**：通过语义接口实现了数值优化与文本生成LLM之间的无缝衔接，使得该框架能广泛应用于供应链、竞赛设计等多种需要模拟复杂人类行为的服务系统优化场景。实证研究表明，该方法在效果和成本上均优于将LLM用作数值求解器或角色扮演系统设计者等基准方法。

### Q4: 论文做了哪些实验？

论文在可持续供应链管理和创新竞赛设计两个应用场景中进行了实验。在可持续供应链管理中，实验模拟了一个包含制造商、零售商和消费者的三阶供应链，政策设计参数为碳税和消费者补贴。实验设置采用LLM驱动的多智能体模拟（LLM-MAS）框架，其中LLM智能体根据提示中的设计参数做出决策，并生成广告文本等非结构化信息。主要对比方法包括：将问题视为黑盒的贝叶斯优化、直接提示LLM进行数值优化的“LLM即求解器”方法，以及让LLM充当决策者并利用LLM-MAS模拟所有智能体行动的“LLM即设计者”方法。实验结果表明，论文提出的算法及其方差缩减变体在所有基准测试中均取得了更优的系统性能（平衡供应链福利、财政成本和环境外部性的目标函数F(θ; ξ)）。

在创新竞赛设计的案例研究中，实验使用了真实的行为数据（来自涉及数百名人类参与者的实验室实验）来验证LLM-MAS的评估和探索能力。实验设置中，LLM-MAS被用于模拟参赛者在不同竞赛设计（如不同的报名费、保留价格和奖金共享机制）下的异质行为（是否进入以及投入多少努力）。关键数据指标显示，LLM-MAS在很大程度上复现了实验室中观察到的行为模式，且两者均与基于风险中性、完全理性假设的游戏理论预测结果存在显著偏差。此外，论文还优化了竞赛参数以最大化收入。结果表明，LLM-MAS找到的最优设计（建议中等报名费，并将保留价格和共享奖金设置在远低于游戏理论推荐的水平）与游戏理论推荐方案（将保留价格和共享奖金与报名费挂钩，并倾向于高报名费）差异很大，且能实现更高的收入。这证明了LLM-MAS既能作为已知设计的低成本评估工具，也能发现被传统方法忽略的优秀设计。

### Q5: 有什么可以进一步探索的点？

本文提出的LLM-MAS框架在服务系统优化中展现出潜力，但仍存在若干局限和可深入探索的方向。首先，框架依赖LLM作为人类行为的代理，但其行为真实性仍需更多验证，尤其是在复杂动态交互中可能出现的偏离。未来可结合人类行为数据进行模型微调或引入混合建模，提升代理的决策保真度。其次，算法在稳态性能优化中依赖单轨迹学习，虽减少计算开销，但可能陷入局部最优；未来可探索多智能体强化学习与LLM结合的优化范式，平衡探索与利用。此外，框架目前侧重于数值化输出，未来可扩展至更复杂的非结构化交互场景（如多轮谈判、动态联盟形成），并引入因果推理机制以增强决策可解释性。最后，实际部署中需考虑LLM的推理延迟与成本问题，未来可研究轻量化模型或分层仿真策略，以提升大规模系统的实用性。

### Q6: 总结一下论文的主要内容

本文提出了一种基于大语言模型的多智能体仿真（LLM-MAS）框架，用于优化服务系统运营。核心问题是服务系统性能受参与者对设计选择（如激励政策）的行为响应影响，而人类行为复杂难以建模。该方法将系统设计优化构建为一个具有决策依赖不确定性的随机优化问题，设计参数被嵌入到提示词中，影响LLM智能体交互产生的状态分布，该不确定性被建模为一个受控马尔可夫链。

为解决梯度计算和稳态评估的计算挑战，论文开发了一种“在轨迹上学习”的算法。该算法在单次仿真运行中，以双时间尺度同时构建零阶梯度估计和更新设计参数，以优化稳态性能，并集成了方差缩减技术以提高效率。理论上，论文通过随机逼近和泊松方程方法证明了算法的收敛性。

在可持续供应链管理和创新竞赛设计两个应用中验证了框架的有效性。结果表明，LLM-MAS框架不仅能作为低成本评估已知设计的工具，还能探索出被传统方法（如博弈论模型）忽略的优异设计。论文的核心贡献在于为融合LLM行为仿真与随机优化提供了原则性框架和高效算法，在人类行为关键但数据获取成本高的运营管理场景中，实现了对复杂系统设计的有效评估与探索。
