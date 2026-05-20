---
title: "Prior Knowledge or Search? A Study of LLM Agents in Hardware-Aware Code Optimization"
authors:
  - "Dmitry Redko"
  - "Albert Fazlyev"
  - "Konstantin Sozykin"
  - "Maria Ivanova"
  - "Evgeny Burnaev"
  - "Egor Shvetsov"
date: "2026-05-19"
arxiv_id: "2605.19782"
arxiv_url: "https://arxiv.org/abs/2605.19782"
pdf_url: "https://arxiv.org/pdf/2605.19782v1"
categories:
  - "cs.AI"
  - "cs.LG"
  - "cs.SE"
tags:
  - "LLM Agent"
  - "代码优化"
  - "硬件感知优化"
  - "反馈循环"
  - "黑盒优化"
  - "先验知识"
  - "搜索策略"
  - "CUDA"
  - "TVM"
relevance_score: 7.5
---

# Prior Knowledge or Search? A Study of LLM Agents in Hardware-Aware Code Optimization

## 原始摘要

LLM discovery and optimization systems are increasingly applied across domains, implementing a common propose-evaluate-revise loop. Such optimization or discovery progresses via context conditioning on received feedback from an environment. However, as modern LLM agents are increasingly complex in their structure, it is difficult to evaluate which components contribute the most, and when and how this exploration may fail. We answer these questions through three controlled experiments. Our findings: (1) In pure black-box optimization, LLMs act as greedy optimizers. (2) In zero-shot kernel generation, providing explicit input-size information has no measurable effect, models converge to the same kernel parameters regardless of size or temperature, as though the size instruction were invisible. Moreover, when tasked to perform kernel optimization for uncommon kernel sizes, performance sharply degrades regardless of the language used. (3) In feedback-loop kernel optimization, CUDA improves monotonically under iterative feedback, while TVM IR actively degrades, which demonstrates that kernel optimization degrades when models operate with low-density language. Our results conclude that LLMs in code optimization tasks highly depend on pretrained priors rather than provided feedback or agentic structure.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在研究大型语言模型在硬件感知代码优化任务中，其性能究竟主要依赖于预训练知识，还是通过搜索和反馈机制实现。研究背景是，LLM作为自主发现系统，通过“提出-评估-修正”循环进行优化，但系统结构日益复杂，难以评估各组件贡献。现有方法的不足在于，无法清晰判断当优化失败时，是预训练先验不足还是搜索反馈机制失效。本文的核心问题是：在代码优化中，LLM的探索过程何时、以及如何失效？作者通过三个受控实验发现：(1) 在纯黑盒优化中，LLM表现为贪婪优化器；(2) 在零样本内核生成中，提供输入尺寸信息无显著效果，模型倾向于生成与预训练数据一致的通用参数，且在非常见尺寸下性能急剧下降；(3) 在带反馈循环的内核优化中，CUDA（预训练数据丰富）性能单调提升，而TVM IR（预训练数据稀少）反而恶化。这些结果共同表明，LLM在代码优化任务中高度依赖预训练先验，而非实际提供的反馈或智能体结构。

### Q2: 有哪些相关研究？

相关研究主要分为三类：**方法类**、**应用类**和**理论分析类**。

**方法类**研究中，本文对比了传统黑箱优化（BBO）与LLM智能体在代码优化上的表现。与以往工作不同，本文通过控制实验揭示了LLM智能体的关键局限：其依赖预训练先验（Prior）而非搜索或反馈。例如，与贝叶斯优化（如基于高斯过程的UCB）或CMA-ES等BBO方法不同，这些方法通过内部状态（如协方差矩阵）主动压缩解空间熵，而LLM智能体仅通过上下文更新，其熵存在由冻结权重决定的下界，导致在非预训练分布的任务上性能骤降。

**应用类**研究涵盖了硬件感知代码优化，如CUDA和TVM IR内核自动生成。本文特别发现，在反馈循环优化中，CUDA语言因预训练数据密度高而性能单调提升，而TVM IR因语言密度低（稀疏先验）导致性能主动退化。这揭示了LLM在不同编程语言上的先验分布差异对优化效果的决定性影响。

**理论分析类**工作常探讨LLM的“涌现”行为或上下文学习机制。本文则首次从控制实验出发，量化了LLM智能体在优化问题中的熵下界，并与BBO的参数量化约束进行形式化对比，指出混合方法（如LLM+结构化搜索）和强化学习微调（降低$H_\theta$）是克服这些结构性局限的潜在途径。

### Q3: 论文如何解决这个问题？

论文通过三个受控实验揭示了LLM在硬件感知代码优化中的核心行为模式：其性能高度依赖预训练先验知识，而非智能体结构或环境反馈。整体框架包括三个实验：黑盒优化（BBO）、零样本代码生成和迭代反馈优化。

在黑盒优化中，LLM被配置为顺序提议者，仅基于搜索历史（先前提议及其值）和任务提示（搜索边界）生成下一个候选点。与CMA-ES、Centaur（CMA-ES与LLM混合）和配备蒙特卡洛树搜索（MCTS）的LLM-MCTS对比，在2D和5D问题集上评估。核心发现是LLM表现出贪婪优化行为：它倾向于在当前最佳点附近局部搜索，而非广泛探索。这通过轨迹分析（高归一化轨迹长度L，表明路径线性且局部）和链式思维推理（模型明确模仿梯度下降策略）证实。即使在提示中要求模仿贝叶斯优化，LLM仍保持贪婪。

在零样本内核生成中，将Python参考实现（含具体输入尺寸）输入LLM，要求生成CUDA内核。对比显式（强调尺寸信息）和隐式（仅提及尺寸）两种提示方式，以及不同温度设置。结果显示，生成内核的硬件关键参数（如块大小、tile大小）在不同输入尺寸下固定不变，且显式提示无效，表明模型输出由预训练先验主导，忽略尺寸指令。

在迭代反馈优化中，采用两种代码表示（高先验密度的CUDA和低密度的TVM IR）和两种智能体架构（反馈循环和采样代理）。反馈循环使用顾问/诊断器与编码器进行最多5轮迭代：当内核正确时顾问推荐优化，错误时诊断器给出修复。采样代理则独立生成5个候选，然后基于所有反馈生成第6个。结果显示：CUDA在迭代反馈下性能单调提升（正确率稳步增加），而TVM IR性能主动退化（正确率和加速率均下降），尽管TVM IR从语义更强的未调度程序开始。这表明反馈能否帮助取决于语言先验密度。此外，当输入尺寸分布偏离基准（从小尺寸基准偏移）时，无先验的TVM MetaSchedule（基于CMA-ES）击败LLM代理，因为LLM携带了与基准尺寸绑定的参数偏差。

### Q4: 论文做了哪些实验？

论文进行了三个受控实验。实验1（BBO黑盒优化）在四种任务集（100个2D合成函数/物理系统/48个2D及48个5D BBOB问题）上，对比LLM（gpt-oss-120b/DeepSeek-V3.2）与CMA-ES、Centaur、LLM-MCTS，预算50次迭代。主要指标包括最佳步数、覆盖率（Cov_50）和轨迹长度L。结果显示LLM表现贪婪：在2D多局部极小值任务中胜率最高（如gpt-oss在Functions上对MCTS胜83:17），但5D时完全失效（对CMA-ES仅胜11:37），覆盖率极低（~12%），而CMA-ES和Centaur平衡最好。实验2（零样本内核生成）在Softmax、Matmul等三个内核的10种输入尺寸上，提供隐式/显式尺寸提示，采样20个内核，温度T∈{0.1,0.5,0.8}。结果表明：输入尺寸提示无效，通过率曲线平坦（如Qwen3-Coder-Next和gpt-oss-120b），支配性tiling参数（如block size）在所有尺寸上固定不变。实验3（反馈循环内核优化）比较CUDA和TVM IR两种表示，在KernelBench Level1/2上，使用反馈循环（advisor/coder迭代5轮）和采样代理两种管道，对比torch.compile和TVM MetaSchedule。主要结果：CUDA在反馈下稳定改进（如gpt-oss编译正确率迭代提升），TVM IR正确率和加速率均下降（如第5轮下降明显）；在尺寸偏移（小输入）下，无先验的MetaSchedule胜率67-69%，超过LLM代理。

### Q5: 有什么可以进一步探索的点？

基于这一研究的核心发现——LLM在代码优化中高度依赖预训练先验而非环境反馈或代理结构，未来可探索的方向包括：1）领域强化学习适配先验：针对硬件感知优化训练专用奖励模型，迫使语言模型学习更精细的调度模式而非依赖粗粒度先验；2）动态示例检索机制：在推理时从高质量代码库中检索包含特定向量化宽度、展开策略等信息的示例，打破参数坍缩问题；3）外部探索脚手架：设计带有随机扰动或演化策略的搜索框架补偿LLM的贪婪局部优化倾向。同时需警惕三个局限性：当前仅验证少数模型族和标准基准，未考虑混合语言翻译阶段对先验的干扰；自动生成代码的生产级验证机制缺失；反馈循环中TVM IR退化提示低密度语言空间需要全新的表征学习而非单纯增加迭代次数。

### Q6: 总结一下论文的主要内容

这篇论文系统性地研究了大型语言模型（LLM）智能体在硬件感知代码优化任务中的行为，核心贡献在于揭示了其优化能力的来源。问题定义上，论文旨在探究LLM智能体究竟是依赖先验知识，还是能够利用环境反馈进行有效的开放式搜索。方法上，作者通过三个受控实验进行检验：纯黑箱优化、零样本核生成以及带反馈回路的核优化。主要结论表明，LLM本质上是一个贪婪的优化器，高度依赖其预训练的先验知识。在零样本生成中，显式的输入尺寸指令几乎没有影响，模型倾向于输出常见的默认参数；而当面对罕见的核尺寸任务时，性能急剧下降。在反馈回路中，CUDA（较高密度先验）能随迭代反馈单调改善，而TVM IR（低密度先验）的性能反而退化。该研究的核心意义在于指出，在代码优化任务中，LLM智能体是“强大的先验利用者”而非“弱开放搜索者”，其优化能力取决于反馈能否被模型的先验知识所吸收，这为设计更鲁棒的优化管线（如根据先验密度动态路由）提供了关键指导。
