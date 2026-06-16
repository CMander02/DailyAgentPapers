---
title: "Tyler: Typed Latent Reasoning for Language Models -- When to Think, What to Compute, and How Much to Allocate"
authors:
  - "Hanyu Lin"
  - "Min Cai"
  - "Jiawei Wen"
  - "Haodi Zhang"
date: "2026-06-15"
arxiv_id: "2606.16360"
arxiv_url: "https://arxiv.org/abs/2606.16360"
pdf_url: "https://arxiv.org/pdf/2606.16360v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent Reasoning"
  - "Latent Reasoning"
  - "Chain-of-Thought"
  - "LLM Decoding Policy"
  - "Token Budget Allocation"
relevance_score: 7.5
---

# Tyler: Typed Latent Reasoning for Language Models -- When to Think, What to Compute, and How Much to Allocate

## 原始摘要

Chain-of-thought (CoT) prompting improves reasoning in large language models (LLMs) by externalizing intermediate computation as discrete text tokens, but this textual interface also introduces redundancy and inference overhead. Latent reasoning offers a promising alternative by carrying part of the computation in continuous representations. However, existing methods typically predefine when latent computation is invoked and how it is allocated during decoding, leaving a key problem unresolved: when to invoke latent computation, what type of computation to perform, and how much budget to allocate. We propose \textbf{Ty}ped \textbf{L}at\textbf{e}nt \textbf{R}easoning (Tyler), a typed and budget-aware framework for latent reasoning during autoregressive decoding. Tyler learns a policy that, at each decoding step, chooses between emitting a text token and switching to a latent computation module specialized for a particular reasoning function. Once invoked, an operator maps the current reasoning state into latent tokens that support global planning, local state updates, or reusable procedural abstraction. Across extensive experiments on three backbone LLMs, Tyler improves accuracy by up to 14.49 points over CoT and by up to 4.30 points over the strongest competing baseline. It further generalizes across diverse reasoning domains and achieves the best final-stage performance with the lowest forgetting.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLMs）在推理过程中面临的显式与隐式计算之间协调的关键问题。研究背景是，虽然链式思维（CoT）提示通过将中间推理步骤外化为离散文本标记提升了模型性能，但这种方法引入了冗余生成和较高的推理成本，且强制要求推理过程必须完全可见。现有方法通常预定义何时调用隐式计算及其分配方式，存在两个主要不足：一是将隐式标记视为通用计算载体，忽略了显式推理步骤在功能上的异质性（如问题定位、状态更新、过程复用等不同功能）；二是缺乏自适应的协调机制，无法让模型在自回归解码过程中自主决定何时进行隐式计算、执行哪种类型的计算以及分配多少计算预算。核心问题可以概括为：能否让LLM学会在可见解码和隐式计算之间灵活切换，自主决定思考的时机、计算的具体类型以及分配的预算。为此，论文提出了Tyler框架，通过学习一个策略，在每一步解码时选择发射文本标记或调用特定推理功能的隐式计算模块（包括全局规划、局部状态更新或可复用的过程抽象），从而实现了类型化且预算感知的隐式推理。

### Q2: 有哪些相关研究？

相关研究可分为两类：

**1. 显式推理方法**：以CoT为代表的显式推理通过离散文本令牌外化中间计算，后续工作通过采样推理路径、工具使用和搜索方法扩展该范式。强化学习（如PPO、GRPO）进一步通过增加计算负载强化推理。本文的区别在于保留自回归解码界面的同时，允许模型自适应地在可见文本令牌与静默潜在计算之间切换。

**2. 潜在推理方法**：现有方法主要研究潜在令牌的构造方式（如循环隐状态、软思想令牌、嵌入空间混合），或通过置信度信号、外部触发模型、暂停令牌来激活潜在计算。这些方法将潜在计算视为统一形式，缺乏对功能角色和计算预算的研究。本文的创新在于将潜在推理形式化为在线、带类型和预算约束的计算问题：不同算子承担特定推理功能（全局规划、局部状态更新、可复用过程抽象），并在显式预算下被调用。实验表明该方法在三个基座上比最优基线提升高达4.30个准确率点。

### Q3: 论文如何解决这个问题？

Tyler通过引入一个类型化和预算感知的潜在推理框架，解决了何时调用潜在计算、执行何种类型计算以及分配多少预算的关键问题。其核心方法是在自回归解码中，让模型在每个步骤通过一个学习到的策略，在生成文本token和调用三种专门化的潜在操作符之间进行选择。

整体框架包括两个主要组件：操作符调用策略和潜在合成模块。操作符调用策略将解码动作空间扩展为原始词汇表加上三个可学习的操作符token，模型通过next-token分布直接决定是否切换到潜在计算。一旦调用某个操作符，潜在合成模块会基于当前上下文生成固定数量的潜在token，并将其追加到上下文中，从而影响后续生成。

关键技术方面，Tyler定义了三种类型的潜在操作符：全局向导操作符（O_g）支持整体规划，局部状态更新操作符（O_s）更新推理状态，可重用过程抽象操作符（O_p）捕捉可复用的推理模式。通过可学习的查询token和投影头，每种操作符在内部参数中特化。合成过程利用LoRA层对骨干模型进行参数高效微调，不直接更新原始参数，从而保持模型稳定。此外，预算感知路由策略通过监督学习使模型学会在合适的位置调用合适的操作符，并根据任务复杂度自动分配潜在计算预算。

创新点在于：将潜在计算分解为三种功能类型，通过类型化设计提供归纳偏置；通过统一的操作符token接口实现端到端学习何时以及如何调用潜在推理；通过基于CoT数据的阶段式训练（先学习操作符行为，再学习路由策略），实现了各推理类型的最优分配。

### Q4: 论文做了哪些实验？

论文在三个骨干模型（Qwen2.5-1.5B-Instruct、SmolLM3-3B、Qwen3-4B）上进行了实验。训练数据来自OpenR1-Math的15K问题-求解轨迹。测试基准包括数学推理（GSM8K、MATH-500）、科学推理（GPQA-Diamond）和定理推理（TheoremQA）。对比方法涵盖显式推理（CoT、SFT、GRPO）和潜在推理（SoftCoT、Soft-Thinking、MemGen、SwiReasoning），采用贪婪解码下的Pass@1准确率作为指标。主要结果：在SmolLM3-3B上，Tyler的Stage 2平均准确率达56.03%，比CoT高14.49点，比最强基线MemGen高4.30点；在Qwen3-4B上达65.78%，比CoT高9.22点，比GRPO高3.13点。在持续学习实验中，Tyler在最终阶段达到39.8%的最高宏观平均准确率，遗忘分数最低（2.3）。消融实验显示，去除类型化算子或路由策略会导致性能下降（如共享算子降至62.95%，随机路由降至~62%）。诊断分析表明，算子形成了功能不同的聚类，且路由能根据任务难度自适应分配计算预算（GPQA调用频率高于GSM8K），预算从0增至5时准确率快速提升。

### Q5: 有什么可以进一步探索的点？

从论文的局限性和未来方向来看，以下几个方面值得进一步探索：首先，当前方法在1.5B-4B规模模型上验证有效，但在更大规模（如70B+）上是否保持优势尚不明确，需要研究规模扩展对隐式算子效率的影响，以及如何自适应调整各算子的计算预算。其次，阶段一的候选边界构建依赖有监督的思维链标注，未来可探索完全无监督的边界发现方法，例如利用强化学习或对比学习自动识别需要隐式推理的位置。第三，隐式计算的可审计性较弱，可考虑设计层次化可解释机制，在关键决策点输出压缩后的推理摘要，或通过算子调用日志构建事后解释图谱。最后，当前评估聚焦于可客观验证的推理任务，对于开放式生成任务，需要开发新的奖励模型来平衡隐式计算的效率与忠实度，同时引入对抗性正则化防止隐式路径产生未对齐的推理内容。

### Q6: 总结一下论文的主要内容

该论文提出Tyler框架，旨在解决语言模型推理中何时调用潜在计算、执行何种类型计算及分配多少预算的关键问题。现有链式思维提示虽通过文本化中间步骤提升推理能力，但存在冗余和推理开销；而潜在推理方法则缺乏对调用时机、计算类型和预算的动态决策。Tyler采用类型化和预算感知的潜在推理方法，在自回归解码的每一步学习一个策略：在输出文本令牌或切换到特定推理功能的潜在计算模块之间做出选择。调用后，操作符将当前推理状态映射为支持全局规划、局部状态更新或可复用过程抽象的潜在令牌。在三种骨干语言模型上的广泛实验中，Tyler相较于链式思维方法平均提升14.49个点的准确率，相较于最强基线提升4.30个点，并展现出跨多样推理领域的泛化能力，在顺序适应中达到最佳最终阶段表现与最低遗忘。该方法有效地将潜在推理重构为在线、类型化和预算感知的操作符调用机制。
