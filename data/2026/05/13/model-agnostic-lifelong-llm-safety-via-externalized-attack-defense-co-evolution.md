---
title: "Model-Agnostic Lifelong LLM Safety via Externalized Attack-Defense Co-Evolution"
authors:
  - "Xiaozhe Zhang"
  - "Chaozhuo Li"
  - "Hui Liu"
  - "Shaocheng Yan"
  - "Bingyu Yan"
  - "Qiwei Ye"
  - "Haoliang Li"
date: "2026-05-13"
arxiv_id: "2605.13411"
arxiv_url: "https://arxiv.org/abs/2605.13411"
pdf_url: "https://arxiv.org/pdf/2605.13411v1"
categories:
  - "cs.CR"
  - "cs.CL"
tags:
  - "LLM安全"
  - "对抗攻防"
  - "红队测试"
  - "外部防御模型"
  - "记忆增强"
  - "攻击智能体"
  - "防御智能体"
relevance_score: 8.5
---

# Model-Agnostic Lifelong LLM Safety via Externalized Attack-Defense Co-Evolution

## 原始摘要

Large language models remain vulnerable to adversarial prompts that elicit harmful outputs. Existing safety paradigms typically couple red-teaming and post-training in a closed, policy-centric loop, causing attack discovery to suffer from rapid saturation and limiting the exposure of novel failure modes, while leaving defenses inefficient, rigid, and difficult to transfer across victim models. To this end, we propose EvoSafety, an LLM safety framework built around persistent, inspectable, and reusable external structures. For red teaming, EvoSafety equips the attack policy with an adversarial skill library, enabling continued vulnerability probing through simple library expansion after saturation, while supporting the evolution of adversarial vectors. For defense learning, EvoSafety replaces model-specific safety fine-tuning with a lightweight auxiliary defense model augmented with memory retrieval. This enables efficient, transferable, and model-agnostic safety improvements, while allowing robustness to be enhanced solely through memory updates. With a single training procedure, the defense policy can operate in both Steer and Guard modes: the former activates the victim model's intrinsic defense mechanisms, while the latter directly filters harmful inputs. Extensive experiments demonstrate the superiority of EvoSafety: in Guard mode, it achieves a 99.61% defense success rate, outperforming Qwen3Guard-8B by 14.13% with only 37.5% of its parameters, while preserving reasoning performance on benign queries. Warning: This paper contains potentially harmful text.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前大语言模型（LLM）安全防护中攻击与防御能力难以持续进化和跨模型迁移的问题。研究背景是，主流的LLM安全范式通过红队攻击（Red-teaming）发现漏洞，再对模型进行安全后训练（如RLHF）来修复。然而，现有方法存在三大不足。首先，攻击方采用端到端的策略优化，攻击知识内化于模型参数中，导致随着训练饱和，新攻击向量的发现迅速停滞，难以持续暴露新的故障模式。其次，防御方需要针对每个受害模型进行特定的安全微调，这不仅计算成本高昂，而且优化出的防御策略高度耦合于特定模型，无法有效迁移。最后，攻击和防御的学习是孤立的，缺乏协同进化的机制。为解决这些问题，论文提出了EvoSafety框架。其核心思想是将攻击知识与防御知识从模型参数中“外化”到持久、可检查、可复用的外部结构中。具体地，攻击方引入了一个对抗技能库，使得攻击策略在饱和后可通过简单的库扩展来持续探测漏洞；防御方则使用一个轻量级的辅助防御模型，结合记忆检索，以模型无关的方式生成安全前缀，避免了对不同受害模型的重复微调。最终目标是实现终身且模型无关的LLM安全保障。

### Q2: 有哪些相关研究？

相关研究主要包括三个方面：**红队攻击**、**安全对齐与防护**以及**多智能体对抗演化**。

在红队攻击方面，早期工作依赖人工提示工程，虽有效但难以规模化。自动化方法分为三类：输入空间搜索、基于智能体的评估框架，以及近期基于强化学习的攻击策略优化。本文指出这些方法在静态封闭环境中容易饱和，攻击模式趋同。与之不同，EvoSafety通过维护一个可扩展的外部攻击技能库，实现攻击向量的持续演化，避免了模式崩溃。

在安全防护方面，现有研究分为训练时内化对齐（如微调）和推理时外置控制（如提示工程）。训练时方法需为每个模型重复训练，且易导致过拒绝；推理时方法虽更灵活，但防御能力有限。EvoSafety的创新在于提出轻量级辅助防御模型搭配记忆检索，实现了模型无关、可迁移且仅通过内存更新即可增强的防护，同时支持Steer（激活模型内在本能）和Guard（直接过滤）两种模式。

在多智能体对抗演化方面，SSP、MAGIC、TriPlay-RL等通过联合优化攻防双方提升安全性。但它们的知识均参数化绑定，导致饱和且难以迁移。EvoSafety通过将攻防知识外化到可复用的技能库和记忆库中，打破了这种封闭循环，使对抗能在饱和后通过简单扩容持续进化。

### Q3: 论文如何解决这个问题？

EvoSafety通过构建一个攻击-防御协同进化的外部化框架来解决大语言模型安全性问题，核心方法是引入持久化、可检查和可重用的外部结构。整体架构包括攻击策略π_A和防御策略π_D，它们通过GRPO算法进行迭代优化。

攻击侧的关键创新是**对抗技能库**。该库采用双路径技能接地将异构攻击策略（可执行脚本和Markdown攻击模式）统一表示，并通过三轴技能验证（功能有效性、模式一致性、行为多样性）筛选技能。技能库可扩展，能持续探索新的失败模式，解决传统红队测试的饱和问题。

防御侧的核心组件是**辅助防御模型**，配备轻量级**验证记忆库**。该库只存储历史对抗性提示，通过向量检索为防御前缀生成提供参考，避免了模型特定安全微调，实现了高效、可迁移且模型无关的安全改进。防御策略可工作在两种模式：**Steer模式**通过安全前缀激活受害模型的内在防御机制；**Guard模式**直接基于安全前缀诊断信号过滤有害输入。

技术细节上，攻击策略采用**早期对齐门控**，在生成阶段通过轨迹空间意图保留代理来过滤无效攻击，避免奖励黑客行为。防御策略则使用**混合奖励函数**，结合良性请求的正确性奖励（含长度正则项）和恶意请求的安全性评分，防止学习到输入无关的通用拒绝模式。通过一次训练，防御策略就能以仅37.5%的参数超越Qwen3Guard-8B，达到99.61%的防御成功率。

### Q4: 论文做了哪些实验？

论文构建了攻防协同演化的实验框架。攻击方以Mistral-7B-Instruct-v0.3为基座，防御方采用Llama-3.2-3B-Instruct作为轻量辅助模型，嵌入模型使用Qwen3-Embedding-0.6B，并以Qwen3Guard-Gen-8B提供奖励信号和评估。训练数据来自AdvBench、CategoricalQA、HarmfulQA、DangerousQA和PKU-SafeRLHF，评估采用HarmBench基准，推理能力测试使用GSM8K和MMLU。

攻击实验方面，在单轮和多轮攻击方法对比中，EvoSafety的攻击成功率（ASR）平均达到92.8%（Qwen3Guard评估）和86.3%（LLM-as-a-Judge评估），在开放权重的Llama-3.1-70B上达到100% ASR，整体表现优于ICON（90.2%/84.7%）等基线方法。零样本攻击在保留技能库上仍有84.6%/74.8%的ASR。可扩展性测试显示，对小型模型仅需2次尝试即可达到100%成功率。

防御实验方面，在Guard模式下，3B参数的辅助防御模型实现了99.61%的防御成功率，将平均ASR从基线方法TriPlay-RL的19.92%降至11.62%（相对降低40%以上）。在良性输入上假阳性率极低，且对GSM8K推理性能影响仅为-0.29。记忆扩展实验表明，直接向Verified Memory Bank添加对抗样本可进一步提升防御效果，无需额外参数更新。

### Q5: 有什么可以进一步探索的点？

该论文提出的EvoSafety框架虽然在攻击与防御共演化上表现出色，但仍存在值得深入探索的局限性和未来方向。首先，攻击策略依赖于预定义的技能库，尽管支持扩展，但技能库的初始构建和规模增长可能仍会引入偏差，限制了未知攻击模式的发现。未来可探索自动化、无监督的技能生成机制，使攻击策略能更自主地探索全新且复杂的对抗向量。其次，防御模型虽然实现了模型无关和轻量级升级，但其有效性高度依赖于记忆检索的质量和检索到相关样本的稳定性。当面对高度自适应或语义模糊的对抗输入时，检索可能失效或增加时延。未来可研究如何结合语义不变性、认知推理技术，使检索更鲁棒，或探索记忆的自动更新与遗忘机制，防止有害污染。此外，当前仅关注单轮交互，如何将共演化框架扩展到多轮、多智能体环境下的动态安全博弈，以及如何建立可解释的共演化胜负判定理论，也是极具价值的研究方向。

### Q6: 总结一下论文的主要内容

本文提出了EvoSafety框架，旨在解决大语言模型（LLM）安全中红队攻击饱和、防御僵化且难以跨模型迁移的问题。核心贡献在于，将攻击与防御知识从模型参数中外部化，实现终身、模型无关的安全改进。攻击方面，通过引入对抗技能库，将攻击策略重构为技能执行引擎，使攻击者能在饱和后通过扩展库持续发现新漏洞。防御方面，用轻量级辅助防御模型替代模型特定安全微调，结合验证记忆库生成输入自适应的安全前缀，支持两种模式：Steer激活模型内在安全机制，Guard直接过滤有害输入。通过强化学习在共进化训练循环中迭代优化攻防策略。实验表明，Guard模式对未见攻击防御成功率达98.83%，以较Qwen3Guard少37.5%的参数实现更高安全性，且不损害常规推理能力。该工作首次以RL驱动方式桥接外部技能使用与攻击向量演化，为LLM提供可扩展、可迁移的安全保障范式。
