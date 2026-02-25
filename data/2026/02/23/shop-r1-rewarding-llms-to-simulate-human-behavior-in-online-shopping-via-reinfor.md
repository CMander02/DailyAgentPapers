---
title: "Shop-R1: Rewarding LLMs to Simulate Human Behavior in Online Shopping via Reinforcement Learning"
authors:
  - "Yimeng Zhang"
  - "Tian Wang"
  - "Jiri Gesi"
  - "Ziyi Wang"
  - "Yuxuan Lu"
  - "Jiacheng Lin"
  - "Sinong Zhan"
  - "Vianne Gao"
  - "Ruochen Jiao"
  - "Junze Liu"
  - "Kun Qian"
  - "Yuxin Tang"
  - "Ran Xue"
  - "Houyu Zhang"
  - "Qingjun Cui"
  - "Yufan Guo"
  - "Dakuo Wang"
date: "2025-07-23"
arxiv_id: "2507.17842"
arxiv_url: "https://arxiv.org/abs/2507.17842"
pdf_url: "https://arxiv.org/pdf/2507.17842v2"
categories:
  - "cs.CL"
tags:
  - "Agent 行为模拟"
  - "强化学习"
  - "LLM 推理"
  - "奖励设计"
  - "在线环境交互"
  - "Agent 评测"
relevance_score: 8.5
---

# Shop-R1: Rewarding LLMs to Simulate Human Behavior in Online Shopping via Reinforcement Learning

## 原始摘要

Large Language Models (LLMs) have recently demonstrated strong potential in generating 'believable human-like' behavior in web environments. Prior work has explored augmenting training data with LLM-synthesized rationales and applying supervised fine-tuning (SFT) to enhance reasoning ability, which in turn can improve downstream action prediction. However, the performance of such approaches remains inherently bounded by the reasoning capabilities of the model used to generate the rationales. In this paper, we introduce Shop-R1, a novel reinforcement learning (RL) framework aimed at enhancing the reasoning ability of LLMs for simulation of real human behavior in online shopping environments. Specifically, Shop-R1 decomposes the human behavior simulation task into two stages: rationale generation and action prediction, each guided by distinct reward signals. For rationale generation, we leverage internal model signals (e.g., logit distributions) to guide the reasoning process in a self-supervised manner. For action prediction, we propose a hierarchical reward structure with difficulty-aware scaling to prevent reward hacking and enable fine-grained reward assignment. This design evaluates both high-level action types and the correctness of fine-grained sub-action details (attributes and values), rewarding outputs proportionally to their difficulty. Experimental results show that our method achieves a relative improvement of over 65% compared to the baseline. The project page is available at https://damon-demon.github.io/shop-r1.html.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决利用大语言模型（LLM）模拟在线购物环境中真实人类行为时，模型推理能力受限、行为真实性不足的问题。研究背景是，LLM在规划和决策任务上表现出色，使其在模拟网络用户行为（如电商购物）方面具有潜力，可用于提升服务测试、个性化推荐等应用。现有方法主要分为两类：一是简单的零样本提示，但缺乏个性化和适应性；二是通过使用更强大的LLM（如Claude 3.5 Sonnet）生成行为背后的“理由”（rationales），构建“上下文-行为-理由”三元组数据进行监督微调（SFT），以增强模型的推理能力。然而，这种SFT方法的性能本质上受限于用于生成理由的LLM的能力上限，其生成的理由质量和多样性存在瓶颈，且难以获得真实用户决策的完整、隐性的理由作为监督信号。

因此，本文的核心问题是：如何突破现有SFT方法的局限，更有效地提升LLM在模拟人类在线购物行为时的推理能力和行为生成的真实性。为此，论文提出了名为Shop-R1的新型强化学习（RL）框架。该框架将行为模拟任务分解为“理由生成”和“行为预测”两个阶段，并为每个阶段设计了针对性的奖励信号。具体而言，对于缺乏真实标签的理由生成阶段，创新性地利用模型内部信号（如logit分布）计算自确定性奖励，以自监督方式引导推理；对于行为预测阶段，则提出了分层奖励结构，不仅评估高层行为类型，还细粒度地评判子行为细节（属性和值）的正确性，并结合难度感知的奖励缩放机制，根据行为复杂性分配奖励，从而防止奖励黑客行为并实现更精细的优化。通过这一RL框架，论文试图直接优化LLM的推理和行为生成过程，超越依赖固定合成数据集的SFT方法，最终生成更贴近真实人类、更合理可信的在线购物行为序列。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：**用于人类行为模拟的LLM**和**用于强化学习的奖励设计**。

在**人类行为模拟**方面，现有研究主要利用LLM基于静态用户画像和交互历史来生成可信的用户行为，应用于社会科学、推荐系统和电子商务等领域。为了提升决策质量，一些方法（如ReAct和反思模型）引入了显式的推理过程，让LLM在生成行动前先输出中间思考步骤。此外，还有研究探索了多智能体框架来模拟动态环境中的交互。本文与这些工作的共同点是都致力于用LLM模拟人类行为，但关键区别在于，本文首次系统性地探索了如何利用强化学习（RL）来增强LLM在**在线购物环境**中模拟人类行为的推理能力，而非仅依赖监督微调或提示工程。

在**奖励设计**方面，主流范式是基于人类反馈的强化学习（RLHF），但其依赖昂贵且可能带噪声的人工标注。直接偏好优化（DPO）等方法试图绕过奖励模型，但仍需偏好数据。另一条路线是使用可验证奖励的强化学习（RLVR），适用于代码生成等有明确正确标准的领域，通过规则自动计算奖励。本文的奖励设计融合了这两类思路的优点，以应对模拟人类购物行为这一独特挑战。具体而言，本文提出了一个混合奖励框架：对于**理由生成阶段**，利用模型内部信号进行自监督，以弥补真实理由的缺失；对于**行动预测阶段**，则设计了具有难度感知缩放的分层奖励结构，这既不同于RLHF的主观偏好建模，也不同于RLVR的严格规则验证，而是针对该任务细粒度属性（如商品属性值）的正确性进行分层评估，从而更精细地分配奖励并防止奖励破解。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Shop-R1的新型强化学习框架来解决在线购物环境中模拟人类行为的问题。该框架的核心思路是将行为模拟任务分解为两个阶段：理由生成和动作预测，并为每个阶段设计专门的奖励信号，以提升大语言模型的推理能力。

整体框架采用两阶段强化学习优化。首先，模型通过监督微调进行冷启动，使用由Claude 3.5 Sonnet生成的（理由，动作）配对数据进行训练，使模型初步掌握合理的理由和动作模式。随后进入核心的强化学习阶段，模型接收网页简化HTML结构编码的上下文和动作历史，需要联合输出下一步的理由和动作。

在架构设计上，Shop-R1包含两个关键模块，并对应两项关键技术：
1.  **理由生成模块**：其创新点在于采用了一种**自监督的“自我确定性分数”**作为奖励信号。该分数通过计算模型在生成理由时词汇预测分布与均匀分布之间的KL散度来度量，反映了模型推理过程的置信度和一致性。这利用了模型的内部信号（logit分布）来引导其生成更确定、连贯的推理过程。
2.  **动作预测模块**：其核心是提出了一个**分层奖励结构，并融入了难度感知的奖励缩放**。该结构将动作奖励分为三个层次：首先是格式奖励，鼓励模型以结构化JSON输出；其次是动作类型奖励，只要高层动作类型（如点击、输入、终止）正确即可获得基础分；最后是细粒度子动作奖励，针对“点击”动作的按钮名称或“输入”动作的文本内容，使用ROUGE-L等文本相似度指标进行评分。为了防止模型为轻松得分而反复选择简单的“终止”动作，该设计对预测难度更高的长文本子动作（如具体的搜索查询）应用了**难度感知奖励缩放因子**进行奖励放大，使得执行完整复杂的动作序列成为收益最高的策略。

最终，模型的优化目标是最大化来自动作预测奖励、理由生成的自确定性奖励以及相对于参考策略的KL正则化项的组合信号。这种方法通过分解任务、利用内部置信度信号和设计精细化的分层奖励机制，有效提升了模型模拟人类购物行为分布的能力，避免了奖励破解，并在实验中取得了显著优于基线模型的性能提升。

### Q4: 论文做了哪些实验？

实验基于一个包含52,137个真实世界在线购物会话的数据集，每个会话记录了用户与网站界面的多轮交互。数据以简化HTML格式提供观察上下文，并利用Claude 3.5 Sonnet自动生成自然语言理由。实验使用Qwen-2.5-3B-Instruct模型作为基础，并在NVIDIA A100 GPU上使用GRPO算法进行训练，输入序列最大长度为32k令牌。

对比方法包括：(a) 零样本提示；(b) 仅使用稀疏二元奖励的RL；(c) 仅使用LLM生成理由进行监督微调（SFT）；(d) SFT后接二元奖励RL；以及(e) 本文提出的Shop-R1方法，其采用分层奖励设计和难度感知缩放。

主要结果如下：零样本提示的精确动作准确率仅为0.32%；仅使用二元奖励的RL准确率为1.01%；仅SFT提升至16.76%；SFT+RL（二元）的准确率略降至16.55%，但类型级F1提升至28.07%。而Shop-R1方法取得了显著提升，精确动作准确率达到27.72%，相对于SFT基线实现了超过65%的相对改进；动作类型准确率和F1分别达到36.40%和31.28%。实验还表明，该方法在不同动作类型（点击、输入并提交、终止）上均表现出改进，并且在不同模型规模（1.5B和0.5B）上也能保持性能优势，验证了其有效性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其强化学习框架主要针对在线购物这一特定环境，其奖励机制和任务分解方式在其他复杂交互场景（如多轮对话或动态决策）中的泛化能力有待验证。此外，依赖内部模型信号（如logit分布）引导推理可能受限于模型本身的偏差，且分层奖励结构的设计虽能缓解奖励破解，但增加了人工设计成本。

未来研究方向可包括：1）将框架扩展至更广泛的网页交互任务（如订票、社交平台操作），测试其跨领域适应性；2）探索自动化奖励设计，例如通过逆强化学习从人类轨迹中学习奖励函数，减少人工干预；3）结合外部知识（如用户画像、实时上下文）增强推理的个性化与真实性；4）研究多智能体协作模拟，以复现群体购物行为（如拼单、比价）。

可能的改进思路包括引入课程学习，让模型从简单任务逐步过渡到复杂场景，以稳定训练过程；或融合模型自省机制，让LLM在生成推理链时评估自身置信度，从而动态调整奖励权重，提升模拟行为的可信度。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为Shop-R1的新型强化学习框架，旨在提升大语言模型在模拟在线购物环境中真实人类行为时的推理能力。针对现有方法（如基于合成数据的有监督微调）受限于生成模型的推理质量、难以产生高保真行为的问题，该工作将人类行为模拟任务分解为两个阶段：理由生成和动作预测，并为每个阶段设计了专门的奖励信号。

在方法上，对于理由生成，由于缺乏真实标注，作者利用模型内部信号（如输出分布与均匀分布的KL散度）构建了一个自监督的“自确定性奖励”，以引导推理过程。对于动作预测，则提出了一个分层奖励结构，不仅评估高层动作类型，还评估细粒度子动作（属性与值）的正确性，并结合难度感知的奖励缩放机制，根据动作复杂度调整奖励幅度，以防止奖励破解并实现细粒度奖励分配。

实验结果表明，该方法在模拟人类购物行为任务上取得了27.72%的精确匹配准确率，相比有监督微调基线（16.76%）实现了超过65%的相对性能提升，验证了其有效性。该研究的核心贡献在于首次将强化学习引入面向模拟的网页购物行为建模任务，并通过创新的混合奖励设计，显著提升了LLM模拟人类行为的真实性和推理能力。
