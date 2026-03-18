---
title: "TRUST-SQL: Tool-Integrated Multi-Turn Reinforcement Learning for Text-to-SQL over Unknown Schemas"
authors:
  - "Ai Jian"
  - "Xiaoyun Zhang"
  - "Wanrou Du"
  - "Jingqing Ruan"
  - "Jiangbo Pei"
  - "Weipeng Zhang"
  - "Ke Zeng"
  - "Xunliang Cai"
date: "2026-03-17"
arxiv_id: "2603.16448"
arxiv_url: "https://arxiv.org/abs/2603.16448"
pdf_url: "https://arxiv.org/pdf/2603.16448v1"
categories:
  - "cs.AI"
tags:
  - "Tool-Using Agent"
  - "Reinforcement Learning"
  - "Text-to-SQL"
  - "Multi-Turn Interaction"
  - "Partially Observable MDP"
  - "Agent Architecture"
  - "Autonomous Agent"
relevance_score: 8.0
---

# TRUST-SQL: Tool-Integrated Multi-Turn Reinforcement Learning for Text-to-SQL over Unknown Schemas

## 原始摘要

Text-to-SQL parsing has achieved remarkable progress under the Full Schema Assumption. However, this premise fails in real-world enterprise environments where databases contain hundreds of tables with massive noisy metadata. Rather than injecting the full schema upfront, an agent must actively identify and verify only the relevant subset, giving rise to the Unknown Schema scenario we study in this work. To address this, we propose TRUST-SQL (Truthful Reasoning with Unknown Schema via Tools). We formulate the task as a Partially Observable Markov Decision Process where our autonomous agent employs a structured four-phase protocol to ground reasoning in verified metadata. Crucially, this protocol provides a structural boundary for our novel Dual-Track GRPO strategy. By applying token-level masked advantages, this strategy isolates exploration rewards from execution outcomes to resolve credit assignment, yielding a 9.9% relative improvement over standard GRPO. Extensive experiments across five benchmarks demonstrate that TRUST-SQL achieves an average absolute improvement of 30.6% and 16.6% for the 4B and 8B variants respectively over their base models. Remarkably, despite operating entirely without pre-loaded metadata, our framework consistently matches or surpasses strong baselines that rely on schema prefilling.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现实企业环境中文本转SQL（Text-to-SQL）任务面临的核心挑战：传统方法依赖的“完整模式假设”在实际中往往不成立。研究背景是，当前基于大语言模型的Text-to-SQL解析在标准基准测试上取得了显著进展，但这些成果通常假设数据库的完整模式（包括所有表、列及其关系）已预先注入模型上下文。然而，在真实的企业数据库环境中，数据库可能包含数百个表，且模式常伴随大量噪声元数据并频繁演化，预先注入全部模式既不现实（受限于有限上下文窗口）也有害（无关或过时信息会严重干扰模型）。

现有方法的不足在于：它们将任务简化为静态翻译问题，缺乏在未知模式场景下的交互与探索能力。标准单轮方法无法处理不可观测的环境，而近期一些多轮智能体框架虽尝试迭代探索，却引入了新瓶颈。架构上，大语言模型难以在长交互过程中保持连贯推理，容易丢失中间观察结果并基于参数先验虚构不存在的模式元素。算法上，跨长轨迹的信用分配问题尚未解决，现有方法通常依赖单一终端奖励或简单聚合中间信号，导致模式探索质量与SQL生成效果混淆，无法将最终执行结果归因于特定动作。

因此，本文要解决的核心问题是：如何在未知数据库模式的情况下，让智能体通过主动、多轮的交互式探索，准确检索并验证相关元数据，最终生成可执行的SQL查询。为此，论文提出了TRUST-SQL框架，将任务形式化为部分可观测马尔可夫决策过程，通过结构化的四阶段协议（探索、提议、生成、确认）来约束推理过程，并设计了双轨GRPO训练策略以隔离探索与执行的奖励，从而协同优化模式 grounding 和SQL生成。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、工具增强探索类和多轮强化学习中的信用分配研究。

在**方法类**研究中，现有工作大多基于“全模式假设”，即预先提供完整的数据库结构。这包括通过监督微调（如OmniSQL、STAR、ROUTE）内化生成能力的模型，以及依赖终端奖励进行优化的单轮强化学习方法。这些方法本质上是静态的“被动翻译器”，无法应对现实企业中模式未知、需要主动探索的场景。TRUST-SQL 则明确突破了这一假设，专注于未知模式场景，并通过多轮交互主动检索和验证相关模式子集。

在**工具增强的数据库探索**方面，近期研究引入了工具集成来应对复杂或隐藏的数据库。一类免训练框架利用冻结的语言模型查询元数据，但缺乏梯度更新，容易产生幻觉且无法严格执行验证协议。另一类多轮强化学习方法将SQL执行嵌入训练循环以优化查询，但它们缺乏严格的认知边界来强制进行元数据验证，并且仍使用混合的终端奖励评估整个探索轨迹，未能区分模式检索和SQL生成的不同信号。TRUST-SQL 通过其结构化的四阶段协议（探索、提议、生成、确认）和严格的验证机制，解决了这些不足。

在**多轮强化学习的信用分配**研究中，现有方案探索了轨迹级优化、过程奖励、树结构搜索和内在激励等方法。这些技术主要针对同质动作空间设计，难以区分最终失败是源于错误的模式检索还是有缺陷的生成逻辑。TRUST-SQL 的核心创新在于提出了双轨GRPO策略，通过分解轨迹和应用令牌级掩码优势，将模式检索阶段和完整生成的探索奖励与执行结果分离，从而精准地解决了信用分配难题。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为TRUST-SQL的框架来解决未知模式下的Text-to-SQL问题，其核心方法结合了一个结构化的交互协议和一种新颖的强化学习训练策略。

整体框架将任务建模为一个部分可观测马尔可夫决策过程。代理在与隐藏的完整数据库模式交互时，仅能通过工具执行获得部分观测。框架的核心是一个明确的四阶段交互协议：探索（Explore）、提议（Propose）、生成（Generate）和确认（Confirm）。代理首先通过探索动作查询数据库元数据；随后在关键的提议阶段，代理必须基于已验证的知识提交一个确定的模式子集，这作为一个强制性的认知检查点，旨在抑制模型幻觉；接着在生成阶段，基于已提交的模式生成候选SQL并观察执行结果；最后在确认阶段提交最终答案。这种协议为学习过程提供了清晰的结构边界。

在此协议基础上，论文提出了创新的双轨GRPO训练策略，以解决长轨迹中的信用分配难题。该方法将每个交互轨迹划分为两个独立的优化轨道：模式轨道（止于提议阶段）和完整轨道（覆盖整个交互）。每个轨道分配专用的奖励信号：模式轨道使用模式奖励（评估探索到的模式与真实模式的结构匹配度），完整轨道使用执行奖励（评估最终SQL的正确性）和格式奖励（确保协议遵守）。关键创新在于应用了令牌级别的掩码优势计算，即每个轨道的奖励优势仅广播给该轨道活动步骤内生成的令牌。例如，提议检查点之后生成的令牌不会获得模式优势，从而彻底隔离了模式探索和SQL生成的优化信号。最终的双轨损失函数结合了两个轨道的GRPO损失，通过超参数平衡其贡献。

主要模块包括基于内部上下文状态（包含用户问题、交互历史和已验证模式知识）的策略模型、严格定义的四类动作空间、以及计算三种奖励（执行、格式、模式）的评估机制。该方法的创新点在于：1）通过强制性的提议检查点有效抑制了模式幻觉；2）通过双轨GRPO及令牌级掩码优势，清晰分离并协同优化了模式链接和SQL生成这两个关键子任务，解决了传统强化学习中信用分配模糊的问题。

### Q4: 论文做了哪些实验？

实验设置方面，论文以Qwen3-4B和Qwen3-8B作为基础模型，在SLIME框架中实现，采用两阶段训练：先进行监督微调（SFT）预热，再使用新颖的Dual-Track GRPO策略进行强化学习优化。TRUST-SQL使用的数据配方包含9.2k个SFT样本和11.6k个RL样本。

评估使用了五个文本到SQL基准测试：BIRD-Dev（用于大规模模式落地）、Spider-Test（用于组合泛化），以及三个用于压力测试模型鲁棒性的变体——Spider-Syn（通过同义词替换评估词汇鲁棒性）、Spider-DK（探究隐式领域知识）和Spider-Realistic（评估歧义消解能力）。主要评价指标是执行准确率（EX%），即预测的SQL必须与真实查询产生完全相同的数据库结果。报告了零温度贪婪解码的单样本性能（Gre）和基于多查询样本多数投票的性能（Maj）。

对比方法包括同参数规模（3B-8B）的近期强基线：单轮模型OmniSQL和SQL-R1，以及多轮强化学习方法MTIR-SQL和SQL-Trail。这些基线均依赖完整模式预填充。

主要结果显示，在严格的未知模式设置下，TRUST-SQL取得了领先性能。关键数据指标如下：在4B规模模型中，TRUST-SQL-4B在BIRD-Dev上贪婪解码准确率达64.9%，多数投票达67.2%，优于MTIR-SQL-4B（63.1% / 64.4%）；在8B规模中，TRUST-SQL-8B在BIRD-Dev上达到65.8%（Gre）和67.7%（Maj），为最高。在鲁棒性测试上，TRUST-SQL-4B在Spider-DK和Spider-Realistic上均取得最佳成绩（71.6%和79.9%）。与各自基础模型相比，TRUST-SQL在未知模式设置下平均绝对准确率提升显著：4B变体提升30.6%，8B变体提升16.6%。此外，实验还表明TRUST-SQL对模式预填充依赖很小，甚至在某些情况下预填充会略微降低其性能（如在Spider-DK上使TRUST-SQL-4B下降2.4%），验证了其主动探索策略的有效性。

### Q5: 有什么可以进一步探索的点？

该论文提出的TRUST-SQL框架在未知数据库模式场景下表现优异，但仍存在若干局限性和值得深入探索的方向。首先，其多轮交互范式虽提升了准确性，但必然带来更高的推理延迟和数据库调用开销，未来可研究轻量化交互策略或异步调用优化以提升效率。其次，当前工作仅基于SQLite方言，扩展到PostgreSQL、MySQL等企业常用数据库系统将极大增强实用性，需适配不同SQL语法与元数据查询机制。再者，固定的交互轮数上限可能限制对超复杂模式的探索深度，未来可引入自适应轮数机制，根据模式复杂度动态调整探索预算。此外，论文未深入探讨噪声元数据（如歧义列名）的鲁棒性处理，可结合实体链接或用户反馈机制进一步提升真实环境下的稳定性。最后，其强化学习策略虽解决了部分信用分配问题，但探索与利用的平衡仍可优化，例如引入课程学习或分层强化学习来加速训练收敛。

### Q6: 总结一下论文的主要内容

本文针对真实企业环境中数据库庞大且元数据噪声多、无法预先获取完整模式（即“未知模式”场景）的挑战，提出了TRUST-SQL框架。核心贡献是将Text-to-SQL任务形式化为部分可观测马尔可夫决策过程，并设计了一个自主代理，通过结构化的四阶段协议（探索、验证、规划、执行）主动识别和验证相关模式子集，将推理过程建立在已验证的元数据上以避免幻觉。方法上，该协议为新颖的双轨GRPO策略提供了结构边界，该策略利用令牌级掩码优势将探索奖励与执行结果分离，解决了信用分配难题，相比标准GRPO取得了9.9%的相对提升。实验结果表明，在五个基准测试上，TRUST-SQL的4B和8B变体相比基础模型分别实现了30.6%和16.6%的平均绝对性能提升。尽管完全不依赖预加载模式，其性能仍能匹配甚至超越基于模式预填充的强基线，为不可观测环境下的可靠Text-to-SQL建立了新范式。
