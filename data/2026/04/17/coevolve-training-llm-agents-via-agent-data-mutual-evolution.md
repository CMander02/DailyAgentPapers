---
title: "CoEvolve: Training LLM Agents via Agent-Data Mutual Evolution"
authors:
  - "Shidong Yang"
  - "Ziyu Ma"
  - "Tongwen Huang"
  - "Yiming Hu"
  - "Yong Wang"
  - "Xiangxiang Chu"
date: "2026-04-17"
arxiv_id: "2604.15840"
arxiv_url: "https://arxiv.org/abs/2604.15840"
pdf_url: "https://arxiv.org/pdf/2604.15840v1"
categories:
  - "cs.CL"
tags:
  - "Agent Training"
  - "Reinforcement Learning"
  - "Data Synthesis"
  - "Agent-Data Co-evolution"
  - "Interactive Learning"
  - "Tool Use"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# CoEvolve: Training LLM Agents via Agent-Data Mutual Evolution

## 原始摘要

Reinforcement learning for LLM agents is typically conducted on a static data distribution, which fails to adapt to the agent's evolving behavior and leads to poor coverage of complex environment interactions. To address these challenges, we propose CoEvolve, an agent-data mutual evolution framework that enables LLM agents to improve through closed-loop, interaction-driven training. Specifically, CoEvolve extracts feedback signals such as forgetting and uncertainty from rollout trajectories to identify failure-prone interaction patterns, and utilizes them to guide LLM-based task synthesis. The synthesized tasks are validated through environment interaction and utilized to update the data distribution, enabling joint adaptation of the agent and its data. Extensive experiments on AppWorld and BFCL across Qwen2.5-7B, Qwen3-4B, and Qwen3-30B-A3B demonstrate consistent and significant improvements over strong base models, yielding absolute gains of 19.43%, 15.58%, and 18.14%, respectively.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在强化学习训练过程中，由于依赖静态数据分布所导致的训练效率低下和泛化能力不足的核心问题。

研究背景是，随着LLM的快速发展，基于LLM的智能体在交互式任务（如网页导航、软件操作）中展现出巨大潜力。强化学习是训练此类智能体的主流方法。然而，现有的训练范式存在明显不足。一方面，依赖人类专家手动与环境交互收集演示轨迹，成本高昂且数据覆盖有限，智能体难以应对真实环境中复杂多变的长尾交互模式。另一方面，虽然可以利用LLM合成数据来降低人工成本，但现有方法通常是离线、开环的随机探索，生成的数据集是静态的，无法根据智能体在训练过程中的实际表现和弱点进行动态调整，导致环境探索浅层、训练效率低下。

因此，本文要解决的核心问题是：如何构建一个无需人工监督、能够使智能体与其训练数据共同进化的闭环训练框架。具体而言，论文提出的CoEvolve框架试图通过智能体与数据的协同演化，打破静态数据分布的局限。它利用从智能体交互轨迹中提取的反馈信号（如遗忘信号）来识别其易失败的交互模式，并以此指导LLM合成针对当前弱点的训练任务。这些新任务经过环境验证后，用于更新训练数据分布，从而实现数据分布与智能体策略的联合自适应优化，最终提升智能体在复杂开放环境中的性能和泛化能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：**大语言模型智能体**和**用于智能体训练的轨迹合成**。

在大语言模型智能体方面，已有工作如ReAct和Reflexion通过结合推理、工具使用和反馈，使LLM能够解决复杂的多步骤任务。后续系统进一步增强了规划和记忆能力。然而，这些方法大多依赖于在静态专家轨迹集合上进行模仿学习，这限制了探索能力并受限于预收集数据的覆盖范围。本文提出的CoEvolve框架则从根本上脱离了这种静态范式，它使智能体能够在动态、自我演化的训练过程中学习，无需依赖固定的专家演示。

在轨迹合成方面，为了减少对专家演示的依赖，近期研究探索了为训练LLM智能体生成合成轨迹。先前方法多以离线或弱自适应方式生成轨迹，例如基于反思或校正的开环合成，以及基于教程、脚本化探索、模拟器和自训练的大规模流程。近期扩展引入了更自主的探索或结构化课程学习，但轨迹生成在很大程度上仍是开环的，与智能体演化的失败模式耦合不紧。相比之下，本文方法通过使用环境反馈来按需合成轨迹，从而“闭合”了这个循环，实现了训练分布的持续适应。此外，CoEvolve在概念上也不同于近期那些为固定查询池优化轨迹或围绕种子任务生成变体的自改进或课程学习框架。本文利用反馈驱动智能体重新进入交互环境，以发现新的可执行查询和状态，因此数据演化不局限于重写或过滤离线查询集。

### Q3: 论文如何解决这个问题？

CoEvolve通过提出一个“智能体-数据协同进化”框架来解决静态数据分布下强化学习无法适应智能体行为演变、难以覆盖复杂环境交互的问题。其核心思想是构建一个闭环系统，使智能体策略与训练数据分布能够相互驱动、共同演化。

整体框架是一个迭代循环过程，包含三个核心模块：
1.  **基于合成任务的策略训练与信号提取**：在每次训练迭代中，智能体策略在动态任务集 $\mathcal{D}_t$ 上进行优化，初始任务集通过大模型的无引导探索获得。策略优化采用分组相对策略优化（GRPO），在最大化奖励的同时通过KL散度约束策略偏移。关键创新在于，不仅进行策略更新，还从生成的轨迹中提取三类反映智能体弱点的行为信号：**遗忘信号**（检测先前成功但现在失败的任务）、**边界信号**（识别智能体行为不稳定、成功率波动大的任务）和**稀有信号**（发现出现频率低但反复出现的系统性未探索行为模式）。这些信号共同定位了智能体的性能瓶颈。

2.  **信号引导的LLM重探索**：针对标注了弱点信号的轨迹，框架利用大模型进行反思，总结失败原因或行为不稳定的根源，并构建结构化的探索上下文。随后，大模型基于此上下文在环境中进行**多轮**（鼓励行为多样性）和**多步**（允许基于中间观察修订动作）的重新探索，以收集针对已识别弱点的新交互数据。这一步骤将抽象的弱点信号转化为具体的、步骤级的动作-观察三元组。

3.  **任务抽象、验证与数据分布更新**：将上一步收集的交互三元组按任务上下文分组，并再次利用大模型将每组交互**抽象**为任务级的规范（包括用户意图、任务查询和可行的动作序列）。接着，通过**环境验证**来筛选这些新合成的任务：在真实环境中执行任务-解决方案对，只有成功完成或获得正向奖励的任务才会被保留。验证通过的任务被添加到当前任务集 $\mathcal{D}_t$ 中，从而更新下一轮训练的数据分布。

该方法的创新点在于实现了**智能体与数据的双向适配与协同进化**：智能体策略的弱点驱动了新训练数据的合成方向，而新数据又针对性地训练智能体以克服这些弱点。这种闭环的、由交互驱动的数据生成机制，使训练能够动态聚焦于复杂且具有挑战性的交互模式，从而显著提升了智能体在复杂环境中的泛化能力和鲁棒性。实验结果表明，该方法在不同规模的基座模型上均带来了持续且显著的性能提升。

### Q4: 论文做了哪些实验？

实验在AppWorld和BFCL-V3两个基准测试上进行。实验设置方面，使用VeRL框架，在8或16块NVIDIA H20 GPU上训练Qwen系列模型（Qwen2.5-7B、Qwen3-4B、Qwen3-30B-A3B），采用GRPO作为基础强化学习方法，学习率为e-6，KL系数为e-3，采样温度为0.9。AppWorld使用Test-Normal和Test-Challenge划分，以任务目标完成率（TGC）和场景目标完成率（SGC）评估；BFCL-V3使用多轮验证集，评估多轮成功率。

对比方法包括零样本基线、GRPO基线以及闭源模型（如GPT-4）。主要结果显示，CoEvolve在所有骨干模型上均带来显著提升：在AppWorld TestN上，Qwen2.5-7B、Qwen3-4B、Qwen3-30B-A3B的TGC分别达到27.98%、35.71%、54.76%，相比GRPO基线有持续增益；在BFCL-V3上，成功率分别达到61.50%、63.00%、67.00%。关键指标上，Qwen3-4B在AppWorld挑战划分上TGC/SGC提升+23.21/+21.43，在BFCL-V3上超越GPT-4（63.00 vs 54.00）。消融实验表明，反馈信号（遗忘、边界、罕见）的引入贡献最大，使平均成功率从45.43提升至49.36。此外，训练动态显示性能稳定提升（从0.21到0.35），合成任务通过率从0.71提升至0.85，且计算开销仅增加约10%，实现了高效训练。

### Q5: 有什么可以进一步探索的点？

基于论文的局限性分析，未来研究可以从以下几个方向深入探索：首先，**反馈信号的丰富与优化**。当前仅利用了遗忘、边界和稀有信号，未来可引入更多元化的反馈，如任务复杂度、探索效率或因果推理深度等信号，以更全面地刻画智能体弱点。其次，**低能力阶段的稳健训练机制**。在训练初期，智能体策略不成熟会导致反馈噪声大，可研究结合课程学习或引入外部先验知识（如人类示范）来引导初始数据分布生成，提升早期训练稳定性。再者，**安全与可控性增强**。自主任务合成可能产生对抗性或风险样本，需设计动态安全过滤器与人工审核触发机制，例如基于内容风险分级或实时价值对齐评估，确保进化过程符合伦理约束。此外，**多智能体协同进化**也值得探索，通过智能体间的竞争或合作来生成更复杂的交互任务，从而提升泛化与适应能力。最后，**计算效率优化**，如开发轻量级反馈提取与任务合成方法，以降低大规模环境交互的代价。

### Q6: 总结一下论文的主要内容

该论文提出了CoEvolve框架，旨在解决传统强化学习在静态数据分布上训练LLM智能体时，因无法适应智能体行为演变而导致的复杂环境交互覆盖不足的问题。其核心贡献是建立了一个智能体与数据相互协同演化的闭环训练机制。方法上，CoEvolve从智能体的交互轨迹中提取遗忘信号等反馈信息，识别易失败的交互模式，并利用这些信号引导基于LLM的任务合成。新合成的任务经过环境交互验证后，用于更新训练数据分布，从而实现智能体能力与学习数据的共同适应与进化。实验在AppWorld和BFCL环境中使用多个Qwen模型进行验证，结果表明该方法相比基线模型取得了显著且一致的性能提升，分别实现了19.43%、15.58%和18.14%的绝对增益。这项工作为通过交互驱动反馈实现智能体自主进化的研究方向提供了新的思路。
