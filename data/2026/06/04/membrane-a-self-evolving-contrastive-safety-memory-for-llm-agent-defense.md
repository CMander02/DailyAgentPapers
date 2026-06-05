---
title: "Membrane: A Self-Evolving Contrastive Safety Memory for LLM Agent Defense"
authors:
  - "Minseok Choi"
  - "Seungbin Yang"
  - "Dongjin Kim"
  - "Subin Kim"
  - "Jungmin Son"
  - "Yunseung Lee"
  - "Jaegul Choo"
  - "Youngjun Kwak"
date: "2026-06-04"
arxiv_id: "2606.05743"
arxiv_url: "https://arxiv.org/abs/2606.05743"
pdf_url: "https://arxiv.org/pdf/2606.05743v1"
categories:
  - "cs.CR"
  - "cs.CL"
tags:
  - "Agent 安全防御"
  - "对抗性提示攻击"
  - "记忆增强型安全机制"
  - "防御性 guardrail"
  - "LLM Agent 安全"
relevance_score: 8.5
---

# Membrane: A Self-Evolving Contrastive Safety Memory for LLM Agent Defense

## 原始摘要

Despite advances in safety alignment, large language models remain vulnerable to continuously evolving jailbreaks. Existing fine-tuned safety classifiers cannot adapt to these evolving attacks, while adaptive memory-based guardrails tend to over-refuse benign queries that resemble stored attacks. We propose Membrane, a self-evolving guardrail built on Contrastive Safety Memory (CSM): each cell pairs the conditions for blocking a harmful query with those for permitting a superficially similar benign request. Without retraining, Membrane evolves CSM by distilling each harmful interaction and its benign counterpart into a contrastive cell indexed by the underlying attack strategy, so that one cell generalizes across topical variants of the same mechanism. At inference, retrieved cells serve as grounding context for precise safety decisions. Across model-level safety on HarmBench and agent-level safety on AgentHarm, Membrane achieves the highest F1 on all six jailbreak attacks. Notably, benign refusal on AgentHarm stays at 7-14%, well below the 28-85% range of prior guards. Memory cells also retain 87-88% F1 under cross-attack transfer and remain stable under memory poisoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文针对大型语言模型（LLM）在面对持续演进的越狱攻击时的安全防御问题。现有研究背景显示，虽然大语言模型经过安全对齐训练，但依然容易受到各种越狱攻击的威胁，且攻击手段正从简单的提示词修改演变为反馈驱动、基于说服的重写、自适应攻击策略等复杂形式。现有方法存在显著不足：一方面，传统的基于微调的安全分类器无法适应不断演变的攻击，其决策边界在部署后难以调整；另一方面，基于动态记忆的防护栏尽管可以扩展知识，但采用单边存储方式（仅存储攻击模式或拒绝规则），容易对与存储攻击表面相似的良性查询产生过度拒绝。这导致了两个耦合的失败模式：防护覆盖范围仅局限于已存储的表面形式，且扩展记忆会使防护栏倾向于拒绝看似攻击的良性请求。

为解决这些问题，本文提出了名为Membrane的自演化防护栏，其核心是对比安全记忆（CSM）模块。该方案的核心思想是：每个记忆单元并非单纯存储攻击条件，而是成对记录阻止有害查询与允许其表面相似良性请求的边界条件。Membrane无需重新训练，通过从每次有害交互中提取攻击策略及其良性对应项，动态创建、更新或删除这些对比记忆单元，从而实现自我演化。推理时，检索相关记忆单元作为基础上下文来做出更精确的安全决策。最终目标是在确保高安全性的同时，大幅降低对良性查询的误拒率。

### Q2: 有哪些相关研究？

相关研究可分为三类。**LLM越狱攻击**方面，现有方法包括黑盒迭代优化、说服式重写、嵌套指令重写和自适应攻击策略等，它们不断模糊攻击与良性查询的边界，导致防御过度。**LLM与智能体安全**方面，现有机制多为固定推理包装器或微调分类器，如TrustAgent和ShieldAgent将安全策略编译为可验证规则电路，但部署后知识固定、无法适应新威胁；基于记忆的护栏虽可扩展，但仅存储单侧不安全知识（正例或拒绝规则），缺乏显式对比，容易过度拒绝与攻击表面相似的良性查询。**自进化记忆**方面，相关工作包括长期持久记忆、可执行技能积累、结构化记忆网络等，但均针对通用任务性能，未构建安全边界的对比结构；Athena将安全/不安全轨迹作为上下文示例，JailDAM维护不安全知识记忆用于VLM检测，但均未将正反对编码为类型化记忆单元。

本文Membrane与这些工作的区别在于：首次将自进化记忆范式适配到安全领域，通过**对比性安全记忆（CSM）**为每个攻击模式配对对应的良性等效查询，形成元组化的对比记忆单元；通过**攻击策略索引**（而非表面形式）实现跨主题泛化；且无需重训练即可在线进化。相比单侧记忆的过度拒绝问题，CSM的显式对比机制显著降低了良性误拒率。

### Q3: 论文如何解决这个问题？

Membrane提出了一种基于对比安全记忆（Contrastive Safety Memory, CSM）的自进化防护栏。其核心思想是构建一个可自更新的记忆单元结构，每个细胞都显式配对有害查询的阻断条件和外观相似的良性请求的允许条件，从而在进化过程中同时抑制越狱和过度拒绝两个失败模式。

整体框架分为两大阶段：配对自进化阶段和推理阶段。在进化阶段，Membrane从一个交互流（每个交互包含一个有害提示及其良性对应物）出发，通过记忆规划器、记忆写入器和非LLM验证器三个组件协同工作。记忆规划器根据当前防护栏对配对的预测结果（越狱、过度拒绝或正确）和检索到的细胞，选择创建、更新、删除或跳过操作；记忆写入器合成新的对比细胞内容；验证器基于结构、重复和容量约束拒绝不符合规则的写入，从而将LLM的内容生成与确定性接受分离。

关键技术包括三部分。第一，细胞结构：每个记忆细胞由攻击剖面（攻击策略、请求动作、危害目标）、决策标准（不安全条件和安全条件配对比）和工具动作上下文（仅agent设置）组成。索引采用攻击策略而非表面主题，使单个细胞能泛化到同一机制的不同主题变体。第二，两阶段检索：推理时首先通过向量相似性召回高召回率的候选细胞，然后通过检索评判器（LLM）进行相关性过滤，仅保留与查询攻击策略和不安全条件真正对齐的细胞。第三，决策机制：最终防护栏基于过滤后的细胞集作出安全/不安全判断，不安全查询直接拒绝。这种方法无需重新训练即可持续进化。

### Q4: 论文做了哪些实验？

论文在模型级安全（HarmBench）和智能体级安全（AgentHarm）两个基准上进行了实验。实验使用Qwen3-8B作为目标模型和守卫模型，Gemini 3 Flash作为拒绝分类器，攻击套件包括PAIR、PAP、TAP、ReNeLLM、FlipAttack和AutoDAN-Turbo等六种强越狱攻击。HarmBench使用320个有害测试提示及其320个良性对照提示，AgentHarm使用176个有害提示及其良性对照。对比方法包括无守卫基线、提示级守卫（Self-Reminder、SmoothLLM、SelfDefend）、微调分类器（LlamaGuard3、WildGuard、GuardReasoner）和记忆增强守卫（RAD、GuardAgent、AGrail等）。

主要结果：在HarmBench上，Membrane在所有攻击上取得最高F1分数，在五项攻击上达到最低ASR，例如ReNeLLM上ASR为0.3%（最佳基线11.3%），FlipAttack上ASR为0.0%（最佳基线7.8%）；FRR维持在2.9%-6.1%的低水平。在AgentHarm上，Membrane同样在所有攻击上获得最高F1，例如ReNeLLM上F1为89.2%，FlipAttack上F1为93.0%，FRR稳定在7-14%，显著低于其他记忆增强守卫（GRail的27-32%，GuardAgent的52-53%）。消融实验验证了对比安全记忆、配对自进化、检索批评者等组件的有效性。

### Q5: 有什么可以进一步探索的点？

Membrane 的局限在于：依赖纯文本英文基准（HarmBench/AgentHarm），未覆盖跨语言、多模态或嵌套 Agent 场景；固定 Qwen3-8B 为受保护模型，规模效应与骨干网络的影响未充分解耦；防御假设对手无法完全自适应（白盒访问 guard、内存库和部署流水线），对抗能力受限。

未来可探索方向：**1) 扩展模态与语言**：构建多模态（图像+文本）和跨语种对抗基准，验证 CSM 在更复杂输入空间的泛化性；**2) 自适应对抗训练**：设计可模拟全白盒攻击的元学习流程，通过生成对抗性扰动主动演化 CSM 细胞，提升对动态攻击的鲁棒性；**3) 细粒度意图推理**：当前对比细胞依赖二值（放行/阻断），可引入多层级意图标签（如“钓鱼式引导” vs “紧急求助”），利用深度学习实现更柔性的上下文门控；**4) 记忆安全审计**：结合因果分析追踪 CSM 细胞对特定攻击策略的迁移敏感度，防止跨策略记忆污染导致的泛化脆性。

### Q6: 总结一下论文的主要内容

这篇论文提出了Membrane，一种用于防御LLM Agent越狱攻击的自我演化安全护栏。核心贡献在于提出了对比安全记忆（CSM）机制，该机制将每个有害交互及其表面相似的良性请求配对存储，并以底层攻击策略而非表面形式建立索引，解决了现有记忆增强防御的两大缺陷：过度依赖存储表面的脆弱覆盖，以及对相似良性请求的错误拒绝。Membrane无需重新训练，通过从有害交互中蒸馏对比单元实现自我演化，推理时检索单元作为决策上下文。在HarmBench和AgentHarm基准测试中，Membrane在所有六种越狱攻击上取得了最高F1分数，同时将AgentHarm上的良性拒绝率控制在7%-14%之间，远低于先前方法的28%-85%。此外，记忆单元在跨攻击迁移和面对20%记忆投毒时依然保持稳定，展现出强大的鲁棒性。
