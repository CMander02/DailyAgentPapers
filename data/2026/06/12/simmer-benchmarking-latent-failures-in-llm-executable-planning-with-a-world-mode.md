---
title: "SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model"
authors:
  - "Xiaoxin Lu"
  - "Ranran Haoran Zhang"
  - "Rui Zhang"
date: "2026-06-12"
arxiv_id: "2606.14574"
arxiv_url: "https://arxiv.org/abs/2606.14574"
pdf_url: "https://arxiv.org/pdf/2606.14574v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Agent Planning"
  - "Benchmark"
  - "Latent Failure"
  - "World Model"
  - "Household Agent"
relevance_score: 8.5
---

# SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model

## 原始摘要

Large language models (LLMs) are increasingly deployed as planners for autonomous agents in household environments. While existing benchmarks evaluate whether LLM-generated plans execute successfully, they overlook a critical type of failure: latent failures. Unlike immediate failures that trigger instant feedback at execution time and enable timely correction, latent failures do not immediately halt plan execution but silently compromise goal achievement. In severe cases, they cause irreversible harm. To address this gap, we introduce SIMMER, a benchmark for evaluating latent failures in LLM planning through a human-curated symbolic world model grounded in the kitchen domain. SIMMER defines a world model comprising 77 actions, 262 unique objects, and approximately 46,800 possible interactions that are semantically realistic, derived from real-world cooking scripts. It then leverages a state machine executor that validates plans against the world model and detects immediate precondition violations, latent hazards, and irreversible failures. Experiments across six LLMs show that even frontier models achieve at most 17% error-free plans. Moreover, up to 56% of plans contain latent failures, the majority of which lead to irreversible consequences. We further demonstrate that explicit state reasoning via counterfactual foresight simulation can reduce latent failures by up to 72% and irreversible cases by up to 75%, suggesting a promising direction for more robust LLM planners.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文《SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model》主要解决的是当前大语言模型（LLM）作为自主代理在可执行任务规划中，对一种关键失败类型——**潜在失败（Latent Failures）**——的检测与评估缺失问题。

**研究背景**：LLM 越来越多地被部署为家庭环境中的自主代理规划器。现有基准测试主要通过两种方式评估：一是使用形式化状态追踪的虚拟环境（如 TextWorld），但这些环境过于简化，无法建模诸如污染、温度传播等隐式状态变化；二是通过语义相似度评估非结构化自然语言生成计划，但这仅停留在表面层面，无法发现因状态依赖而隐含的错误。

**现有方法的不足**：两者都无法检测到那些满足所有显式前置条件，却通过隐式状态变化无声传播的错误。这类失败不会像即时失败那样在执行时触发反馈并允许及时纠正，而是悄无声息地危害目标达成，严重时可造成不可逆转的损害。

**本文解决的核心问题**：针对这一评估空白，论文提出了 **SIMMER**，一个基于人类精选的厨房领域符号世界模型（包含77个动作、262个独特对象和约46,800种交互）的基准。它利用状态机执行器模拟计划执行，追踪细粒度状态，并专门检测那些传统指标无法发现的即时失败、潜在危害和不可逆失败，从而为评估 LLM 规划可靠性提供更全面的视角。

### Q2: 有哪些相关研究？

相关研究主要分为两类：

**LLM规划方法类**：现有工作如SayCan利用价值函数将LLM规划与机器人能力结合，Code as Policies通过代码生成可执行策略，以及将LLM作为世界模型进行规划的方法（如通过世界模型推理）。这些方法普遍采用“规划-执行-重规划”范式，依赖执行时的前提条件违反来检测失败。本文指出该范式无法处理潜伏失败——满足所有前提条件、不触发即时反馈但暗中损害目标的失败，尤其是不可逆失败。本文通过显式建模和检测这类失败填补空白。

**虚拟环境与评测类**：ALFWorld、VirtualHome、BEHAVIOR等环境通常用任务成功率或目标条件成功率评估规划，Embodied Agent Interface引入了更细粒度的错误分类（如遗漏目标、时序错误）。但本文指出这些指标存在根本局限：它们关注任务完成而忽略安全性，状态表示局限于简单谓词（如OPEN/CLOSED）和物体位置，无法捕捉污染或化学转化等导致潜伏失败的状态变化。因此一个代理可能在完美完成任务的同时引入仅在任务完成后才显现的违规。本文通过人工策划的厨房领域符号世界模型（77个动作、262个物体、约46,800种交互）和状态机执行器来显式检测潜伏失败和不可逆失败。

### Q3: 论文如何解决这个问题？

SIMMER通过构建一个符号化世界模型和状态机执行器来检测LLM规划中的潜在故障。核心方法包括三个组成部分：首先是一个基于真实烹饪脚本（来自wikiHow和Instructables）构建的符号化厨房世界模型，包含77个动作、262个独特对象和约46,800种语义上合理的交互，能够建模隐式状态变化（如污染、温度传播和化学转化）。其次是故障分类体系，将规划错误区分为即时故障（违反前提条件导致执行立即中断）和潜在故障（满足所有显式前提但通过隐式状态传播静默地损害目标实现）。第三是状态机执行器，它逐步模拟计划执行、跟踪细粒度状态，并在执行过程中检测三种故障：即时前提违反、潜在危害和不可逆故障。

关键技术在于状态机通过世界模型精确追踪动作对对象状态的累积影响，例如切生鸡肉后砧板会被污染，而重用未清洗的砧板会导致细菌转移至其他食材。创新点在于引入了反事实预测模拟（counterfactual foresight simulation），这是一种提示策略，要求模型在执行每个动作前先显式推理该动作对世界状态的影响及其后续效应。实验表明，这种方法可以将潜在故障降低72%，不可逆案例降低75%，表明通过外部化状态追踪能够显著提升LLM规划的可靠性。

### Q4: 论文做了哪些实验？

SIMMER 实验基于100个烹饪脚本（涵盖12种烹饪技法、77个动作和262个物体），任务步骤数2-18步，平均每任务含26.6个动作和31.5个物体。评估了6个LLM：GPT-5.4、Gemini 3 Flash、Claude Opus 4.6（闭源）和Llama 3.3 70B、DeepSeek V3.2、Qwen 3.5 27B（开源），温度T=0。主要结果：所有模型中错误率低于17%的计划极少，平均仅7.2%无错误。即时失败影响66-99%的计划（闭源模型平均2.12次/计划，开源模型4.91次/计划）。潜在失败影响29-52%的计划（每计划0.50-1.73次），其中20-45%的计划含不可逆失败。潜在失败分为三类：状态传播（如未清洁砧板导致交叉污染）、隐性前提忽略（如遗漏清洗脏鸡蛋）、目标后疏忽（如忘关烤箱）。进一步测试了两种提示策略：Self-Refine在GPT-5.4和Claude Opus 4.6上减少总失败超40%，但对弱推理模型效果差；Counterfactual Foresight在GPT-5.4和Claude Opus 4.6上可减少潜在失败高达72%、不可逆失败75%，优于Self-Refine。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于其世界模型仅限于厨房领域，限制了结论的泛化性；且符号化世界模型无法捕捉真实环境的噪声、物理交互和感知不确定性，例如物体状态（如“加热中”）的连续变化。未来方向可包括：1）扩展至更多领域（如手术室、工厂），构建跨领域世界模型以评估通用性；2）引入概率性状态变化（如动作失败概率）和部分可观测性，模拟真实环境中的不确定性；3）改进反事实推理机制，例如结合因果链剪枝或分层推理来降低计算开销，同时适用于实时规划；4）探索多模态感知（如视觉状态推理）与符号模型的融合，弥合符号抽象与现实差距；5）设计更细粒度的失败分类（如可逆性程度检测），为在线纠正策略提供依据。此外，当前方法依赖手动定义状态依赖，未来可研究自动因果结构学习，从经验数据中提取失败模式。

### Q6: 总结一下论文的主要内容

论文提出了SIMMER基准，用于评估大语言模型（LLM）在可执行规划中的潜在失败，这类失败不会立即中断执行，但会悄然破坏目标实现，甚至造成不可逆后果。SIMMER基于人工策划的厨房领域符号世界模型，包含77个动作、262个独特对象和约46,800种语义真实的交互，通过状态机执行器验证计划，检测即时前条件违规、潜在危险和不可逆失败。实验表明，即使最先进的LLM也最多只有17%的计划无错误，高达56%的计划包含潜在失败，且多数导致不可逆后果。通过反事实预见模拟进行显式状态推理，可将潜在失败减少多达72%，不可逆案例减少75%，为构建更鲁棒的LLM规划器提供了有前景的方向。
