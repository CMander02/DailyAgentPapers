---
title: "DemoEvolve: Overcoming Sparse Feedback in Agentic Harness Evolution with Demonstrations"
authors:
  - "Lirong Che"
  - "Yuzhe yang"
  - "Peiwen lin"
  - "Chuang wang"
  - "Xueqian wang"
  - "Jian su"
date: "2026-05-23"
arxiv_id: "2605.24539"
arxiv_url: "https://arxiv.org/abs/2605.24539"
pdf_url: "https://arxiv.org/pdf/2605.24539v1"
categories:
  - "cs.AI"
tags:
  - "Agent架构"
  - "Agent记忆/规划/推理/工具使用"
  - "多智能体协作"
  - "Agent训练数据/奖励模型/critic模型"
  - "Agent在具体场景的实用研究"
relevance_score: 8.5
---

# DemoEvolve: Overcoming Sparse Feedback in Agentic Harness Evolution with Demonstrations

## 原始摘要

Agent harness evolution improves frozen language-model agents by modifying the executable structures around them. We study this paradigm as a form of sample-efficient fast adaptation: instead of updating model weights, an agent can acquire task-specific competence by changing its external harness, while leaving the base model's general capabilities intact. Prior work shows that self-generated rollouts can support harness search, suggesting that agents may acquire new task competence through practice. Yet in long-horizon stochastic environments, self-practice becomes fragile: rewards are sparse, outcomes are high-variance, and failures are hard to attribute to concrete harness mechanisms. We introduce DemoEvolve, a demonstration-bootstrapped approach to harness evolution. When reward-only search is too broad and noisy, competent human trajectories serve as expert reference experience for the coding proposer, guiding harness-level diagnosis and editing. Experiments on Liar's Dice show that self-rollout evolution can work when episodes are short and failures are attributable. In contrast, Balatro exposes a harder long-horizon stochastic regime, where self-rollout evolution is misled by sparse feedback and candidate-selection noise, while tutorial-like textual knowledge alone does not yield stable improvement. Under the same limited budget, DemoEvolve produces more effective and auditable harness edits and achieves better performance. Overall, demonstrations make sparse-feedback harness evolution more diagnosable, localizable, and stable.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在长时间跨度、高随机性环境中，基于智能体程序框架进化（Agentic Harness Evolution）时面临的稀疏反馈问题。研究背景是，智能体可以通过修改其外部的可执行程序框架（而非更新模型权重）来获得任务特定的能力，即利用自我生成的轨迹数据来搜索最优框架。然而，现有方法在文本和代码等模型原生领域表现良好，但在Long-horizon的随机交互世界中存在明显不足：奖励稀疏且方差大，一次失败可能涉及数百个状态转换，早期小决策会重塑未来状态分布，而随机性可能使无效的框架修改看起来有益。核心问题是，在这种环境中，自我生成轨迹（self-rollout）无法提供诊断性足够强的反馈来指导框架编辑，导致难以进行信用分配，即从充满噪声的轨迹级反馈中推断出应该修改哪个外部机制。本文提出的DemoEvolve方法通过引入人类演示轨迹作为专家参考经验，来增强稀疏反馈的可诊断性和局部化，从而引导编码提案者进行更有效的框架诊断和编辑，最终解决自传播进化中因稀疏反馈和候选选择噪音导致的失败问题。

### Q2: 有哪些相关研究？

根据论文内容，该研究的相关工作可分为以下几类：

1. **方法类**：主要涉及外层循环优化，包括通过反馈驱动重写、程序搜索、候选选择等方式优化代理的提示词、工作流、工具、记忆等外部结构。本文与这些方法的区别在于，重点研究当奖励信号稀疏、反馈具有高方差且难以归因时，自生成经验的局限性，并引入人类示范来克服这些挑战。

2. **经验利用类**：相关工作通过将交互历史转化为可复用的反思、记忆或技能来改进代理。本文则反问：在非模型原生、长期交互的任务中，自生成经验何时仍对架构演化有用，尤其在失败稀疏且难以归因的情况下。

3. **学习与探索类**：模仿学习和示范学习利用专家轨迹来减少探索负担；课程学习控制训练顺序以提高稳定性；稀疏奖励探索方法强调到达信息丰富的状态。本文类似，但区别在于优化的是外部结构而非模型权重，且示范用于架构级别的诊断和编辑，而非直接策略训练。

4. **应用与评测类**：游戏作为测试平台，用于评估动态状态追踪、长期规划等能力。本文与相关工作的区别在于，其重点不是评估固定代理或训练游戏策略，而是利用游戏作为测试环境来研究架构在随机性、长期决策和动态交互下的自我演化。

### Q3: 论文如何解决这个问题？

DemoEvolve通过演示引导的进化框架解决稀疏反馈问题。其核心方法是将熟练人类轨迹作为编码提案者的专家参考经验，而非直接用于微调模型。整体架构围绕一个冻结的语言模型构建，通过修改其外部的可执行程序（即“马具”）来提升任务性能，而不更新模型参数。该框架包含两个主要组件：任务世界交互与马具优化器。马具决定了模型如何观察状态、暴露哪些动作或工具、如何解析输出以及如何执行动作。优化目标是找到一个最优马具，使其在与任务世界交互后获得的稀疏奖励最大化。

关键技术包括三个信息机制的比较：(1) Meta-Harness：仅使用自我生成的轨迹档案；(2) OpenResearch：在档案基础上增加外部文本知识如规则或指南；(3) DemoEvolve：在档案基础上增加人类演示轨迹。DemoEvolve的创新点在于，它利用人类轨迹作为诊断工具，帮助提案者比较失败的智能体轨迹与熟练行为，从而准确定位缺失的状态抽象、糟糕的动作优先级或资源管理问题。通过这种方式，DemoEvolve将稀疏反馈转化为可诊断、可定位的编辑依据，从而在长视界随机环境中实现更有效和稳定的马具进化。实验表明，相比之下，仅依赖自我轨迹的方法易被稀疏反馈和噪声误导，而演示引导的方法能产生更有效且可审计的马具编辑，并显著提升性能。

### Q4: 论文做了哪些实验？

论文在两类游戏环境中进行了实验。首先是TextArena Liar's Dice，作为乐观场景（短期可归因），使用Small3和OneCall-Wild1两个变体，评估GPT-5.4-low自对弈、Qwen-3.5-4B vs GPT-5.4-low及Qwen-3.5-4B自对弈三种配对。通过30个逻辑留出种子进行开发集搜索和留出评估，结果显示选定的进化策略使宏观留出奖励从基线的0.392提升至0.800（绝对增益+0.408），其中Small3从0.400提升至0.828，OneCall-Wild1从0.383提升至0.772，所有六项对比均有提升。

其次是Balatro（长期随机困难场景），使用BalatroBench固定种子设置：种子A/B/C为开发种子，D/E为留出种子。比较四个条件：BalatroLLM（基线）、Meta-Harness（自回滚进化）、OpenResearch（外加文本任务知识）和DemoEvolve（外加人类轨迹）。主要结果：DemoEvolve总体完成率12/15，ID平均终轮23.33（完成8/9），OOD平均20.00（完成4/6），显著优于其他条件。Meta-Harness虽有ID增益（19.33）但未泛化（OOD 16.33），且审计发现其选中的策略存在实现错误。经济曲线分析显示DemoEvolve的人类经济距离降至12.26，晚期降至6.49，晚期到达率0.81，接近人类行为。5×3诊断研究进一步表明，人类轨迹提供了正面的状态-行动反事实证据，帮助可执行编辑（State+Tool占比45.5%），优于仅靠回滚（46.2%）或文本笔记（21.7%）。

### Q5: 有什么可以进一步探索的点？

论文在任务覆盖面上存在明显局限，仅通过Balatro一个长时域随机环境验证方法有效性，缺乏对更广泛交互场景（如多游戏、工具使用、终端任务、网页代理及具身环境）的泛化测试。未来研究方向应聚焦于：（1）探索演示引导的装备进化在稀疏奖励环境中的通用适用边界，特别是需设计更细粒度的失效属性归因机制，将候选者选择噪声归因于特定装备组件而非随机波动；（2）结合专家演示与自生成轨迹的混合反馈策略，利用演示数据构建先验知识库，辅助代码修改器进行更高效的局部诊断与结构化编辑；（3）引入元学习框架，使装备进化能从不同任务的演示模式中提炼跨任务适配模板，从而降低对高质量示范的依赖。此外，需量化稀疏反馈与候选选择噪声的交互效应，开发基于置信度加权的候选评估指标，提升进化过程在长时域环境中的稳定性。

### Q6: 总结一下论文的主要内容

这篇论文研究了在长周期、随机交互环境中，如何通过改进智能体的外部“框架”（而非模型权重）实现样本高效的快速适应。问题在于，此类环境中奖励稀疏、结果方差大，让智能体通过自我生成的轨迹进行框架搜索（即自我练习）变得不可靠，难以归因失败原因。为此，作者提出了DemoEvolve方法，利用专家的人类演示轨迹作为引导搜索的示范参考，辅助代码生成器进行框架级别的诊断与编辑。实验表明，在短期可归因任务（如Liar‘s Dice）中，基于自我轨迹的演化有效；但在长期高不确定性任务（如Balatro）中，自我演化易被稀疏反馈误导，而DemoEvolve在相同预算下能生成更有效、更可审计的框架修改，并取得更优性能。核心贡献在于证明了示范数据可以缩小框架搜索空间、将稀疏失败转化为可操作机制，使框架演化更稳定、可诊断且样本高效。
