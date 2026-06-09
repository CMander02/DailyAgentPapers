---
title: "Customer-Agent: Overcoming Context Limitations in Ultra-Long Shopping Trajectories via Tool-Augmented Agents and RLVR"
authors:
  - "Hongye Liu"
  - "Rongmei Lin"
  - "Anurag Kashyap"
  - "Hejie Cui"
  - "Ricardo Henao"
  - "Besnik Fetahu"
  - "Bing Yin"
date: "2026-06-06"
arxiv_id: "2606.07995"
arxiv_url: "https://arxiv.org/abs/2606.07995"
pdf_url: "https://arxiv.org/pdf/2606.07995v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "Shopping Agent"
  - "Tool-Augmented Agent"
  - "RLVR"
  - "Long Context"
  - "Customer Trajectory"
  - "Code Interpreter"
  - "Benchmark"
relevance_score: 8.5
---

# Customer-Agent: Overcoming Context Limitations in Ultra-Long Shopping Trajectories via Tool-Augmented Agents and RLVR

## 原始摘要

Understanding customer shopping trajectories is essential for enabling personalized shopping experiences. However, shopping records (i.e., customer's search, clicks, purchases, etc.) often span long time horizons over multiple years, resulting in extremely long trajectories that pose significant challenges for existing large language models (LLMs). Despite the importance of this problem, existing benchmarks are limited to short customer trajectories, while real-world trajectories from large e-commerce platforms are rarely accessible due to data privacy constraints. To address this gap, we introduce ShopTrajQA, a long-context evaluation benchmark constructed from real-world product information and simulated shopping trajectories. The dataset includes variants of up to 32k and 64k tokens, enabling systematic evaluation of model robustness under varying context lengths. Through comprehensive benchmarking of frontier LLMs, we identify critical performance gaps in reasoning over long shopping trajectory data. To address these challenges, we propose a Customer Agent Framework for ultra-long context management. Leveraging a Reinforcement Learning with Verifiable Rewards (RLVR) agentic training paradigm, our approach stores trajectories as external local files and trains the agent to autonomously retrieve and parse them through code-interpreter interactions (e.g., SQL queries), effectively bypassing the fixed in-context window constraints of LLMs. Experimental results demonstrate that our framework achieves strong performance for ShopTrajQA and shows generalization to other complex reasoning tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决长购物轨迹场景下大语言模型（LLM）的上下文窗口限制问题。研究背景是：理解用户购物轨迹（搜索、点击、购买等）对个性化电商体验至关重要，但真实世界中的购物记录往往跨越数年，形成极长的序列。现有方法存在明显不足：一方面，现有基准数据集（如OPeRA）局限于短轨迹，缺乏对长上下文能力的评估；另一方面，将整个长轨迹直接放入LLM的上下文窗口会导致二次方级的计算和内存开销，且模型在超长序列中难以高效检索和整合远距离信息，推理性能严重下降。此外，传统RLHF方法在长上下文中应用效果不佳，而直接采用带可验证奖励的强化学习（RLVR）也因计算成本和性能瓶颈而受限。针对这些问题，本文提出两个核心贡献：一是构建了ShopTrajQA长上下文基准数据集，基于真实商品信息和模拟购物轨迹，包含32k和64k令牌变体；二是提出了“Customer-Agent框架”，通过将轨迹存储为外部文件并训练智能体使用代码解释器（如SQL查询）自主检索和解析，从而绕过LLM的固定上下文窗口约束，结合RLVR训练范式实现高效的长上下文推理。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及以下几类工作。首先是**评测基准类**，如 **OPeRA** 和 **ESCI**。OPeRA 是一个公开的购物轨迹数据集，但其用户群体（多为学生和研究者）导致轨迹较短且产品多样性有限；本文提出的 ShopTrajQA 则采用更真实的商品数据（来自 ESCI）和 LLM 模拟，生成了长达 32k 和 64k token 的超长轨迹，弥补了现有基准在长上下文推理评估上的不足。其次是**方法类**，相关工作包括采用**强化学习从人类反馈（RLHF）** 或**基于可验证奖励的强化学习（RLVR）** 来提升 LLM 推理能力的方法。本文提出的 Customer Agent 框架同样基于 RLVR 训练范式，但核心创新在于它不将长轨迹直接输入模型上下文窗口，而是通过**工具增强（如 SQL 查询）和外部存储**实现选择性检索与解析，从而突破固定上下文限制，解决了现有 RLVR 方法在超长轨迹场景下计算昂贵且推理下降的问题。

### Q3: 论文如何解决这个问题？

这篇论文提出了一种**Customer-Agent框架**来解决超长购物轨迹的上下文长度限制问题。核心思想是将**长文本从prompt中解耦**，存储为外部本地文件，并训练模型作为**智能体**，通过**代码解释器**（如SQL查询）自主检索和解析这些外部文件，从而绕过LLM的固定上下文窗口约束。

**整体框架**是一个基于**工具增强的智能体系统**，主要由三部分组成：策略模型πθ、代码执行器CI和环境（包含问题q和答案a）。模型生成的响应G包含推理文本和代码，当检测到代码终止标记时，暂停生成并将代码发送给CI执行，将结果或错误作为反馈f_t拼接回输入，继续生成直至给出最终答案o，形成完整的交互轨迹τ。

**关键技术**包括：1) **本地存储机制**：将长购物轨迹数据通过ID直接加载到沙箱环境，自动解析为数据库，支持SQL查询。2) **解释器反馈掩码**：屏蔽CI返回的标记，防止外部反馈影响模型生成的连贯性。3) **KV缓存重用**：在代码执行前缓存KV状态，降低内存开销。4) **异步沙箱**：解耦代码执行与模型推理，支持安全、可扩展的并行训练。

**两阶段训练策略**是核心创新。第一阶段是**SFT冷启动**：基于已构建的QA数据，通过多轮工具交互生成成功的工具调用轨迹，让模型掌握正确的工具调用语法。第二阶段是**RLVR微调**：采用**GRPO算法**和设计精巧的**奖励函数**，奖励包括中间代码的可执行性和最终答案的正确率，鼓励模型即使答案错误也能通过执行工具调用获得部分奖励，从而促进探索并避免奖励黑客行为。

该框架通过将长上下文外部化并让模型学会使用工具，有效解决了LLM在超长购物轨迹推理中的性能瓶颈。

### Q4: 论文做了哪些实验？

论文围绕所提出的Customer-Agent框架进行了全面的实验评估。实验设置包括：使用ShopTrajQA数据集（32k和64k token两种上下文长度变体）评估购物轨迹推理性能；使用AIME 2024/2025评估数学推理；使用2WikiMultihopQA、HotpotQA和Bamboogle评估多跳问答的泛化能力。对比方法包括Qwen3-1.7B和Qwen3-4B的基础版本、SFT版本以及RLVR训练版本，同时与gpt-oss-20B、Qwen3-Coder-30B和gpt-oss-120B三个大型模型进行对比。主要结果如下：在ShopTrajQA上，经过RLVR训练后，Qwen3-1.7B在32k上下文准确率从17.3%提升至59.2%，Qwen3-4B从13.8%提升至62.5%；在64k上下文中，Qwen3-1.7B从14.7%提升至51.0%，Qwen3-4B从9.3%提升至60.1%。在AIME 2024上，Qwen3-4B-SFT-RLVR达到65.83%准确率，比基线提升3.75%；在AIME 2025上达到55.0%，提升7.5%。工具调用能力方面，RLVR训练后Qwen3-4B在32k上下文工具调用率（TCR）达到0.95，成功工具调用率（SuccTCR）为0.69。数据质量评估显示，GPT-4.1在73%的情况下偏好ShopTrajQA生成的轨迹。实验表明，该框架显著提升了长上下文购物轨迹推理能力，并保持了良好的泛化性能。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于购物轨迹基于LLM模拟生成，难以捕捉真实用户行为的复杂性和多样性，未来可探索混合仿真框架或引入真实脱敏交互日志。其次，多轮工具交互与RLVR训练计算成本高昂，在更大模型和更长上下文场景下可扩展性受限，可通过轻量化工具调用策略或离线处理来优化。此外，当前框架主要依赖结构化SQL查询，对非结构化数据（如自由文本评论）支持不足，未来可研究将语义检索与代码解释结合。一个有趣的改进方向是将工具增强与动态上下文压缩结合：当轨迹超长时，先让agent对历史进行分层摘要，再执行定向SQL检索，从而降低交互轮次。另外，现有评估仅聚焦64k tokens，可进一步探索agent在128k以上超长序列中的错误传播与恢复机制，这对构建鲁棒的商业化购物助手尤为重要。

### Q6: 总结一下论文的主要内容

本论文针对超长购物轨迹推理中的上下文长度限制问题，提出了一种新的解决方案。作者首先构建了ShopTrajQA基准数据集，包含长达32k和64k token的真实购物轨迹，用于评估大语言模型在长上下文场景下的推理能力。实验发现，现有模型在直接处理完整轨迹时存在显著性能下降。为此，论文提出Customer Agent框架，将购物轨迹外化为结构化文件，通过代码解释器交互（如SQL查询）实现工具的自主检索和解析，从而突破固定上下文窗口限制。结合基于可验证奖励的强化学习训练范式，该框架能够有效训练智能体在长上下文场景中进行精准推理。实验结果表明，该方法显著提升了推理准确性，尤其在长上下文设置下表现突出，为处理复杂长程交互数据提供了新方向。
