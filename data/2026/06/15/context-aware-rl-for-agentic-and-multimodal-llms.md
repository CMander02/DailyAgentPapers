---
title: "Context-Aware RL for Agentic and Multimodal LLMs"
authors:
  - "Peiyang Xu"
  - "Bangzheng Li"
  - "Sijia Liu"
  - "Karthik R. Narasimhan"
  - "Pramod Viswanath"
  - "Prateek Mittal"
  - "Xingyu Fu"
date: "2026-06-15"
arxiv_id: "2606.17053"
arxiv_url: "https://arxiv.org/abs/2606.17053"
pdf_url: "https://arxiv.org/pdf/2606.17053v1"
categories:
  - "cs.CL"
  - "cs.CV"
tags:
  - "Agent Reasoning"
  - "Reinforcement Learning"
  - "Multimodal"
  - "Context Grounding"
  - "LLM Agent"
relevance_score: 7.5
---

# Context-Aware RL for Agentic and Multimodal LLMs

## 原始摘要

Large language models (LLMs) often fail when answering requires identifying a small but decisive piece of evidence within a long or complex context, such as a single line in a tool trace or a subtle detail in an image. We propose ContextRL, a context-aware reinforcement learning (RL) method that improves long-horizon reasoning and multimodal performance through an \emph{indirect} auxiliary objective. Instead of supervising only the final answer, ContextRL presents the model with a query, an answer, and two highly similar contexts, and rewards it for selecting the context that supports the query--answer pair, thereby encouraging fine-grained grounding. We construct contrastive context data in two domains: for coding agents, trajectories serve as contexts, yielding 1k pairs built via condition filtering; for multimodal reasoning, images serve as contexts, yielding 7K pairs built via generative editing and similarity search. ContextRL achieves average gains of +2.2% over standard GRPO on 5 long-horizon benchmarks, and +1.8% across 12 diverse visual question answering benchmarks. To disentangle the effect of the proposed objective from that of additional data, we compare against data-augmentation baselines that repurpose the same contrastive contexts as standard query--context--answer examples. These baselines provide little to no improvement, showing that the gains arise from the proposed context-selection objective rather than from the contrastive data alone.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）在长上下文或复杂多模态场景中存在的“上下文不敏感”（context unawareness）问题。研究背景是，当前LLM在代理系统和多模态推理中表现强大，但面对需要从冗长工具调用轨迹、密集图像或复杂代码中定位细微决定性证据（如代码中的一行、图像中的微小细节）的任务时，经常因忽略关键上下文而做出局部合理但整体错误的决策。现有方法（如标准强化学习GRPO）主要针对最终答案进行结果奖励，缺乏对模型在输入上下文中精确定位并依据证据进行推理能力的直接训练。本文的核心问题是：如何让LLM在长程推理和多模态理解中，能够可靠地将预测 grounding 于可获得但稀疏的关键上下文证据上。为此，论文提出了ContextRL，一种上下文感知的强化学习方法，通过引入一个间接的辅助目标——奖励模型从两个高度相似的上下文中选出支持给定问答对的那个——来强制模型进行细粒度地上下文选择，从而提升模型在长程和视觉问答基准上的表现。

### Q2: 有哪些相关研究？

在相关研究中，首先可归为**RL后训练方法类**。典型工作包括GRPO、DAPO等基于可验证奖励的数学和代码推理方法，以及SWE-RL、DeepSWE等针对软件工程Agent的RL训练范式，还有Vision-R1、PAPO等面向多模态LLM的视觉推理RL方法。这些方法主要着眼于优化最终答案的正确性或答案-推理链的一致性，但均未提供关于模型是否真正在给定上下文中进行细粒度证据定位的信号。本文的ContextRL则专门针对这一空白，通过上下文选择辅助目标提供过程级信号，弥补了结果奖励的不足。

其次是**多模态Agent类**工作，如将RL用于交织推理与工具使用、搜索，或对长视频进行推理的模型。它们虽涉及多模态上下文，但同样未关注精确的上下文判别性证据提取。

另外，本文特别区分了**并发工作**：Lu等人的“ContextRL”虽也结合上下文与多模态RL，但它将参考解决方案馈入奖励模型作为额外上下文用于过程验证，属于正交方向；而本文令上下文自身成为模型的选择对象，以间接方式激励细粒度证据定位。

总体而言，本文与现有方法的核心区别在于：不依赖额外数据增强或结果监督，而是通过新颖的上下文对比目标，迫使模型在高度相似的长文本或图像上下文中做出精准判别。

### Q3: 论文如何解决这个问题？

ContextRL 通过引入一种间接的辅助目标来增强模型对上下文的细粒度感知，主要针对代理任务和多模态推理。其核心是一种基于对比上下文对的强化学习方法。整体框架基于 GRPO（Group Relative Policy Optimization）进行增强，在标准任务数据和对比上下文数据上联合优化两个损失函数：GRPO 损失和上下文感知损失。

架构设计上，ContextRL 首先构建对比上下文对 (C+, C-)，每个对包含一个查询 Q、一个答案 A 以及支持该答案的正例上下文 C+ 和干扰性的负例上下文 C-。上下文形式在编码任务中为智能体的轨迹（包括推理、工具交互、沙箱观测等），在多模态任务中为图像。

关键技术包括：
1. **对比数据构建**：
   - **编码任务**：从 SWE-smith 的 66k 轨迹中，通过严格筛选（如相同仓库、提交、文件、函数，但不同问题）和语法检查，最终仅保留约 1k 高质量轨迹对，其中补丁内容被掩码以防止表面特征泄露。
   - **多模态任务**：对自然图像使用生成式编辑（通过 GPT-5.4 生成编辑指令，用 Nano Banana 2 执行编辑，再经筛选去除视觉伪影）得到 700 对；对结构图像（如图表、几何）使用基于相似度检索（Qwen3-VL-Embedding 8B 嵌入，余弦相似度≥0.85 且答案不同），得到 6300 对。
2. **上下文感知损失**：将 (Q, A, C+, C-) 转化为二选一问题，通过教师强制得到正负上下文的 logit 差值，并用带边缘裁剪的 sigmoid 损失函数优化，鼓励模型选择正确上下文。
3. **联合优化**：将标准 GRPO 损失与上下文感知损失相加，平衡任务性能与上下文对齐能力。

创新点在于通过间接的上下文选择任务而非直接监督最终答案，迫使模型关注细微证据，从而在 5 个长程基准和 12 个视觉问答基准上分别取得 +2.2% 和 +1.8% 的平均提升，且实验证明收益源于该目标本身而非额外数据增强。

### Q4: 论文做了哪些实验？

论文在长程（Long Horizon）和多模态（Multimodal）两个场景下进行了实验。**长程实验**设置：基模型使用Qwen3-8B和Klear-AgentForge-8B，对比方法包括Base（无RL）、RL baseline（标准GRPO）和本文方法ContextRL。训练集包含8k实例（7k标准编码任务+1k对比轨迹对）。评估基准包括2个分布内（SWE-Bench Verified/Lite）和3个分布外（LiveCodeBench v6、LongBench v2、Needle-in-a-Haystack）基准。主要结果：在Klear-AgentForge-8B上，ContextRL在SWE-Bench Verified上比RL baseline提升+2.2%（达30.2%），在SWE-Bench Lite上提升+2.3%（达24.0%）；在分布外任务中，LongBench v2长子集提升+4.6%（达28.7%），NIAH提升+5.8%（达71.3%），显著优于RL baseline。**多模态实验**设置：基模型使用Qwen2.5-VL-7B和Qwen3-VL-8B，对比方法包括Base、RL baseline、PAPO（仅Qwen2.5-VL）和ContextRL。训练集45k实例（38k标准单图任务+7k对比图像对）。评估涵盖12个基准，分为数学推理、通用理解、细粒度感知、科学推理和真实场景理解五大类。主要结果：在Qwen2.5-VL上，ContextRL平均提升+2.0%（达53.4%），超过PAPO的+0.8%；在Qwen3-VL上平均提升+1.6%（达65.7%）。所有12个基准上ContextRL均优于RL baseline，如在ScienceQA上提升+4.4%（达95.4%），在MathVerse上提升+3.8%（达49.1%）。关键数据指标显示，该方法在两类实验中均实现了一致且稳健的改进。

### Q5: 有什么可以进一步探索的点？

首先，论文的局限性在于对比数据构建成本较高，依赖条件过滤和生成式编辑，限制了规模化应用。其次，当前方法仅针对单步上下文选择，对于需要多步推理和交互的复杂场景（如长链条工具调用）可能泛化不足。

未来可探索以下方向：1）自动生成对比数据，设计自训练或课程学习策略，减少人工标注。2）将上下文感知目标扩展到多步骤、多模态的序列决策中，例如在推理链的每一步都进行细粒度上下文选择，而非仅最终答案。3）尝试将辅助目标与多种强化学习算法（如PPO、REINFORCE）结合，分析其在不同优化框架下的鲁棒性。4）研究上下文选择能力与模型内部注意力的关系，探索通过可解释性工具指导优化方向。5）在更广泛的任务（如具身推理、视频理解）中验证方法的通用性。

### Q6: 总结一下论文的主要内容

大型语言模型在长上下文或复杂场景中常因忽视关键证据而失败。本文提出ContextRL，一种上下文感知强化学习方法，通过一个间接辅助目标来改善长程推理和多模态性能。该方法在标准GRPO训练基础上，引入上下文选择任务：给定查询、答案及两个高度相似的上下文（一个支持答案，一个为干扰项），模型需选择正确的上下文，从而鼓励细粒度证据定位。作者在编码智能体领域通过条件过滤构建了1000对轨迹级对比上下文，在多模态推理领域通过生成式编辑和相似性搜索构建了7000对图像级对比上下文。实验表明，ContextRL在5个长程基准上平均比标准GRPO提升2.2%，在12个视觉问答基准上提升1.8%。消融实验证实，增益源于上下文选择目标而非对比数据本身，因为使用相同数据进行SFT或结果强化学习的数据增强基线基本无提升。该工作揭示了长程推理与视觉理解失败的一个共同根源——模型不能可靠地将预测基于可用证据，并提供了一个轻量级、跨模态的解决方案。
