---
title: "AdaMEM: Test-Time Adaptive Memory for Language Agents"
authors:
  - "Yunxiang Zhang"
  - "Yiheng Li"
  - "Ali Payani"
  - "Lu Wang"
date: "2026-06-04"
arxiv_id: "2606.05684"
arxiv_url: "https://arxiv.org/abs/2606.05684"
pdf_url: "https://arxiv.org/pdf/2606.05684v1"
github_url: "https://github.com/yunx-z/AdaMEM"
categories:
  - "cs.AI"
tags:
  - "Agent记忆"
  - "测试时适应"
  - "混合记忆架构"
  - "长程任务"
  - "ALFWorld"
  - "WebShop"
  - "HotpotQA"
  - "微调"
  - "策略合成"
relevance_score: 9.5
---

# AdaMEM: Test-Time Adaptive Memory for Language Agents

## 原始摘要

A central challenge for language agents is utilizing past experience to adapt to dynamic test-time conditions. While recent work demonstrates the promise of agentic memory mechanisms, most systems restrict retrieval to episode initiation. Consequently, agents are forced to rely on static guidance that becomes increasingly misaligned as long-horizon tasks unfold. To address this rigidity, we propose the Adaptive Memory Agent (AdaMEM), a novel framework for agent test-time adaptation. Without updating model parameters online, AdaMEM adapts agent behavior via a hybrid memory architecture: it maintains a long-term trajectory memory of raw experiences collected offline while generating dynamic short-term strategy memory on-the-fly to guide decision-making. This mechanism enables the trade-off between token efficiency and adaptability across varying inference-time compute levels. Empirically, AdaMEM significantly outperforms static memory baselines, achieving relative gains of up to 13% on ALFWorld and 11% on WebShop, with consistent leading performance extending to agentic search on HotpotQA. To further enhance this adaptation, we develop STEP-MFT, a Step-wise Memory Fine-Tuning technique that trains the policy to synthesize high-quality strategies from retrieved experiences, yielding additional performance gains. Our work establishes a new scaling dimension for agentic memory, supporting continuous reasoning and self-evolution post-deployment in real-world environments. Our code is available at https://github.com/yunx-z/AdaMEM.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

语言智能体在长程任务中面临测试时动态环境适应这一核心挑战。现有基于记忆的方法（如Synapse、ReasoningBank）通常仅在episode起始时进行一次静态检索，将检索到的轨迹或策略固化到系统提示中。这种“前加载”的刚性机制导致智能体在任务执行过程中只能依赖初始静态指导，无法根据中间失败或子目标变化进行动态调整，随着长程任务展开，策略会逐渐与真实状态失配。尽管有研究尝试通过在线参数更新（如测试时训练）实现适应，但对于语言智能体而言，每次更新模型参数的成本过高，不适用于长程交互场景。本文提出的AdaMEM框架旨在解决两大核心问题：1）如何打破静态记忆的刚性限制，使智能体在推理过程中实现连续测试时适应？具体通过混合记忆架构实现——维护离线构建的可扩展长程轨迹记忆，并在推理时动态生成紧凑的短程策略记忆，以细粒度指导每一步决策；2）如何高效地训练策略模型生成高质量策略以显式优化这种测试时适应？为此提出了STEP-MFT，一种无需critic的逐步骤记忆微调技术，通过过滤能实际改变智能体动作以导向成功轨迹的策略进行监督微调，从而实现细粒度信用分配。该框架在ALFWorld、WebShop等任务上相比静态记忆基线取得了显著提升。

### Q2: 有哪些相关研究？

相关研究可从三个维度组织：**方法类**工作主要围绕静态记忆检索，如基于原始轨迹、提炼洞察或结构化流程的记忆机制，以及通过可执行代码扩展动作空间的技能记忆。它们均依赖任务开始前的预计算，导致在长时任务中检索到的先验知识逐渐失效。**应用类**工作聚焦混合记忆架构，如MemRL和Agentic Memory利用强化学习动态优化记忆效用或管理策略，但主要优化回合间（inter-episode）知识迁移，缺乏回合内（intra-episode）的恢复机制。本文AdaMEM的核心区别在于：首次提出动态短时策略记忆，在测试时在线合成上下文感知的策略，替代静态检索，从而缓解分布偏移。**评测类**工作包括ALFWorld、WebShop和HotpotQA等长时推理基准。本文在实验中显示，AdaMEM相比静态基线在ALFWorld上提升13%，在WebShop上提升11%，验证了动态适应性的优势。此外，本文提出的STEP-MFT技术通过步骤级微调进一步提升了策略生成质量，区别于单纯依赖RL的管理方法。

### Q3: 论文如何解决这个问题？

AdaMEM的核心是构建一个双记忆架构实现测试时自适应，无需更新模型参数。首先，构建一个静态的长期轨迹记忆库，仅存储成功轨迹，通过预训练嵌入模型对每个时间步的状态进行索引，形成键值对用于密集检索。在线推理时，代理不直接使用该记忆库，而是动态生成短期策略记忆——一种基于当前状态和检索到的相关经验实时合成的自然语言策略。这区别于先前工作仅依赖离线预生成策略的静态初始化方法。

为实现计算效率与适应性的权衡，设计了两种推理模式：高适应模式让代理根据当前状态决策是否触发记忆检索，检索后生成仅用于当前步骤的瞬时策略，使用后立即丢弃，追求最大鲁棒性；低适应模式则将策略作为持久状态变量，通过刷新决策判断是继续使用当前策略还是生成新策略，有效降低令牌成本。

为进一步提升策略质量，提出STEP-MFT微调技术。该方法通过双重过滤拒绝采样来筛选高质量训练数据：首先确保轨迹成功，其次要求策略必须改变代理的下一步动作。这基于策略优势的理论推导，证明动作变化是正优势的必要条件。最终在过滤后的数据上使用监督微调损失训练统一的策略模型，同时负责策略生成和动作决策，避免了部署过程中的额外模型开销。

### Q4: 论文做了哪些实验？

论文在三个基准上进行了实验：ALFWorld（具身导航，分seen/unseen splits，指标为成功率%）、WebShop（电商导航，指标为任务分数0-100）和HotpotQA（多跳问答，指标为成功率%）。主干模型采用Qwen3-4B-Instruct（ALFWorld/HotpotQA）和RL训练的Qwen2.5-7B-Instruct（WebShop），并进行了on-policy和off-policy（使用Gemma-27b-it）评估。对比方法包括无记忆的ReAct、Synapse（检索完整轨迹）和ReasoningBank（离线生成静态策略）。主要结果如下：
- **训练无关设置**：AdaMEM在ALFWorld unseen split上达到58.2%成功率，比无记忆基线（46.8%）高11.4个百分点，比最强静态记忆Synapse（52.2%）高6.0个百分点；在WebShop上达74.2任务分数，反超无记忆基线（71.4），而静态记忆均出现负迁移。
- **HotpotQA**：AdaMEM以41.1%成功率领先所有基线（无记忆39.7%，Synapse 40.4%，ReasoningBank 40.5%）。
- **可扩展性**：随着检索数量k从1增至16，AdaMEM成功率从54.0%单调提升至64.0%，而Synapse反降。
- **记忆微调**：STEP-MFT（使用步骤级双过滤）在ALFWorld上比训练无关版本（54.5%）提升至59.8%，在WebShop上提升至76.1。
- **效率**：AdaMEM在降低推理延迟16%的同时，实现了与计算预算正相关的性能改善。

### Q5: 有什么可以进一步探索的点？

AdaMEM的局限性首先在于其依赖离线轨迹数据，可能无法覆盖部署后涌现的全新场景，导致策略生成泛化能力不足。其次，混合记忆架构中长短期记忆的交互机制较为静态，缺乏主动遗忘或冲突解决策略，长期运行可能积累噪声。未来方向可探索：(1) 结合因果推理或元学习，使策略能主动识别环境变化并自适应调整记忆容量；(2) 引入层次化记忆衰减机制，根据任务相关性动态优化检索权重；(3) 将STEP-MFT微调扩展到在线设置，结合强化学习实现策略的持续自我进化。此外，当前框架对长程依赖任务的稳定性仍有提升空间，可考虑植入图结构记忆或检索增强生成（RAG）的变体，以强化跨步骤信息关联。

### Q6: 总结一下论文的主要内容

针对当前语言代理在测试时静态记忆检索导致的策略僵化问题，本文提出AdaMEM自适应记忆代理框架。其核心是混合记忆架构：离线的长程轨迹记忆存储原始经验，在线动态生成短时策略记忆以指导决策，无需更新模型参数即可实现测试时自适应。该方法在推理成本和适应性间实现灵活权衡。实验表明，AdaMEM在ALFWorld和WebShop上分别取得13%和11%的相对提升，在HotpotQA上同样领先。本文还提出STEP-MFT步级记忆微调技术，利用过程级奖励训练策略从经验中合成高质量策略，进一步提升性能。该工作为代理记忆建立新的缩放维度，支持持续推理与部署后自我进化。
