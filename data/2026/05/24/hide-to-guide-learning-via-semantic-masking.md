---
title: "Hide to Guide: Learning via Semantic Masking"
authors:
  - "Ruitao Liu"
  - "Qinghao Hu"
  - "Alex Hu"
  - "Yecheng Wu"
  - "Shang Yang"
  - "Luke J. Huang"
  - "Zhuoyang Zhang"
  - "Han Cai"
  - "Song Han"
date: "2026-05-24"
arxiv_id: "2605.25198"
arxiv_url: "https://arxiv.org/abs/2605.25198"
pdf_url: "https://arxiv.org/pdf/2605.25198v1"
github_url: "https://github.com/mit-han-lab/SMEPO"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "LLM Agent训练"
  - "专家引导强化学习"
  - "语义掩码"
  - "奖励伪造防御"
  - "多领域推理"
relevance_score: 8.5
---

# Hide to Guide: Learning via Semantic Masking

## 原始摘要

Reinforcement learning with verifiable rewards (RLVR) has become a powerful paradigm for improving language models on reasoning-intensive tasks, but its effectiveness is often limited by exploration. For example, models often fail on hard problems, leaving little useful reward signal. External expert traces offer a natural source of guidance, yet they may also expose reward-relevant content along the critical path to the verifier target, such as final answers, intermediate values, executable implementations, or answer-related entities. This content can create an unintended reward hacking channel, allowing the policy to obtain reward by copying the trace rather than learning the underlying reasoning or agentic behavior. Existing guided-RL methods reduce this risk by using partial trajectories, but they mainly control how much expert information is shown heuristically rather than which parts should be hidden. To this end, we propose Semantic Masked Expert Policy Optimization (SMEPO), a fine-grained semantic masking strategy for expert-guided RLVR. Instead of truncating traces coarsely or revealing them unchanged, SMEPO masks reward-relevant semantic spans along the critical path while preserving the expert's decomposition, plan, and procedural structure. This turns hard problems from reasoning from scratch into a fill-in-the-blank process: the policy can follow the expert's problem-solving route, but must still reconstruct the missing values, code, or entities by itself. SMEPO is simple to apply and requires no changes to the reward function or RL objective. Across diverse domains, including math, code, and agentic search, SMEPO improves accuracy by up to 3.2 points over GRPO and reduces training time by up to 4.2x. The code is available at https://github.com/mit-han-lab/SMEPO.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决专家引导的强化学习（RLVR）中一个关键失效模式：完整专家轨迹虽能提供有用的过程引导（如解题步骤、计划），但同时会暴露“奖励相关”内容（如数学题的最终答案、中间数值；代码题的可执行程序；搜索任务中的答案实体），导致策略模型直接“复制”这些内容来获得奖励，而非真正学习底层推理或行为逻辑，即产生奖励黑客（reward hacking）问题。现有引导方法（如使用部分轨迹或自适应提示）虽然通过截断或修改专家数据来缓解此问题，但丢弃了大量有价值的过程结构信息，尤其在高质量专家数据稀缺时，会浪费宝贵的引导信号。为此，本文提出语义掩码专家策略优化（SMEPO），核心思路是将完整专家轨迹转化为“填空式”引导：保留专家的过程分解、计划等程序性框架，但精确掩码掉直接暴露验证器检查目标的关键语义片段（如数学中的数值、代码实现、搜索中的实体）。这样，策略模型必须跟随专家路径，但需自主“填补”被隐藏的关键内容，从而被迫学习推理过程而非简单复制，有效避免奖励黑客。

### Q2: 有哪些相关研究？

根据论文内容，相关研究可分为三类：  
**方法类**：与SMEPO最相关的工作包括LUFFY（使用离线推理轨迹）、Guide（初始失败时注入提示）、GHPO（难度感知提示）、TRAPO（专家前缀监督）、POPE（困难问题使用预言前缀）和Learning-like-humans（专家轨迹重述问题）。这些方法主要控制何时或展示多少专家信息，而SMEPO创新地关注展示专家轨迹的哪些语义部分，通过掩码奖励相关关键路径内容（如最终答案、中间值），保留分解结构和过程，将困难问题转化为填空任务。  
**应用类**：RLVR在数学、代码等场景的应用研究，以及扩展到工具使用的智能体搜索（如Search-R1、DeepResearcher），SMEPO在这些领域验证了有效性。  
**安全与评测类**：关于奖励黑客的研究揭示了专家指导下的特定形式——当轨迹暴露奖励相关值时，策略可能通过复制而非学习获得高奖励。SMEPO专门针对此问题设计。  
**学习范式类**：掩码和填充式学习（如BERT、T5、代码模型的FIM训练）虽与SMEPO使用的掩码原则相似，但SMEPO将其引入强化学习引导，作为探索指导而非监督重建目标。

### Q3: 论文如何解决这个问题？

SMEPO 的核心创新在于提出了一种名为语义掩码专家策略优化（Semantic Masked Expert Policy Optimization）的细粒度语义掩码策略。整体框架仍基于 GRPO 管线，但关键区别在于对专家轨迹的处理方式。SMEPO 将专家轨迹分解为可重用的指导性内容（如解题步骤、代码逻辑）和与奖励直接相关的关键内容（如最终答案、中间数值、可执行的代码、实体），然后使用领域特定的轻量级规则或工具（如数字匹配、代码块检测、spaCy 实体识别）精准地掩码后者，同时保留前者的结构与顺序。这使得策略模型在训练时获得的不是原始完整的专家轨迹，而是一个“填空题”式的掩码轨迹。模型必须遵循专家的问题解决路径，但必须自行重构被隐藏的关键值、代码或实体。这种方法无需修改奖励函数或RL目标函数，仅通过改变输入条件来引导探索。其创新点在于：1) 实现了专家指导中“程序性指导”与“奖励相关内容”的语义级分离；2) 通过掩码而非截断，保留了更完整的结构化指导信息；3) 采用轻量级预处理，计算成本极低。在数学、代码和智能体搜索等不同领域，SMEPO 均有效提升了准确率并显著缩短了训练时间。

### Q4: 论文做了哪些实验？

论文在数学、代码和智能体搜索三个领域进行了实验。实验设置上，使用8次rollout/提示，在8×H100 GPU上运行400步优化，数学和代码最大响应长度12k，智能体搜索每轮2,048 tokens，学习率数学/代码为1×10⁻⁶，搜索为8×10⁻⁷。数据集方面：数学使用GSM8K、MATH500、AIME25、AIME26、AMC和OlympiadBench，报告六个基准的未加权平均；代码使用HumanEval、HumanEval+和LiveCodeBench；智能体搜索使用Bamboogle。对比方法包括：无专家轨迹的GRPO、专家轨迹上的SFT、SFT+RL、完整专家轨迹(Expert)、LUFFY、GHPO以及本文提出的SMEPO。主要结果：在Qwen3-8B-Base数学任务上，GRPO平均得分47.6，Expert(DS)降至41.0，SMEPO(DS)提升至50.3；在Qwen2.5-7B上，GRPO 42.4，Expert 38.6，SMEPO 44.5；在DeepSeek-R1-Distill-Qwen-7B上，GRPO 61.8，Expert 60.4，SMEPO 62.6。代码任务上，GRPO平均56.5，Expert 55.7，SMEPO 59.0。智能体搜索Bamboogle上，GRPO 45.6，Expert 23.2，SMEPO 48.8。SMEPO还显著减少训练时间，如在Qwen3-8B-Base上达到目标仅需2.37小时，而GRPO需9.90小时。消融实验显示，SMEPO优于前缀暴露和随机掩码，且与GHPO结合可进一步提升性能。

### Q5: 有什么可以进一步探索的点？

SMEPO提出的语义掩码策略虽有效，但存在一些可进一步探索的局限性。首先，当前方法依赖人工预定义或简单规则来识别“关键路径”上的“与奖励相关”的语义片段，这在大规模、多样化任务中可能不够鲁棒，未来可探索基于模型注意力或内隐知识的自动掩码区域发现机制。其次，SMEPO将问题转化为“填空”式推理，但未考虑如何动态调整掩码的粒度——例如在模型表现增强后逐步减少掩码，从引导过渡到独立解题。第三，该方法的验证集中于准确率和训练效率，但对模型泛化能力、对未见推理路径的适应性的影响值得深究。此外，当前掩码仅屏蔽文本内容，未来可考虑对“推理步骤顺序”进行打乱或模糊化，更全面地防止奖励黑客。最后，跨模态场景（如视觉-语言推理）中的语义掩码策略也是一个有前景的研究方向。

### Q6: 总结一下论文的主要内容

该论文提出语义掩码专家策略优化（SMEPO），旨在解决带可验证奖励的强化学习（RLVR）中专家轨迹引发的奖励黑客问题。当专家轨迹暴露最终答案、中间值等关键路径上的奖励相关信息时，策略会通过直接复制而非学习推理来获取奖励，导致探索不足。现有方法仅粗略截断轨迹，无法精确控制信息暴露。SMEPO通过语义掩码，在保留专家分解、计划与过程结构的同时，隐藏关键路径上的奖励相关语义片段，将难题转化为“填空”任务，迫使策略自主重构缺失内容。该方法无需修改奖励函数或RL目标。在数学、代码和智能体搜索等任务上，SMEPO相比GRPO准确率提升最高3.2%，训练时间缩短最多4.2倍，验证了有效指导需同时保留过程线索并屏蔽关键路径奖励信息的核心理念。
