---
title: "IH-Challenge: A Training Dataset to Improve Instruction Hierarchy on Frontier LLMs"
authors:
  - "Chuan Guo"
  - "Juan Felipe Ceron Uribe"
  - "Sicheng Zhu"
  - "Christopher A. Choquette-Choo"
  - "Steph Lin"
  - "Nikhil Kandpal"
  - "Milad Nasr"
  - "Rai"
  - "Sam Toyer"
  - "Miles Wang"
  - "Yaodong Yu"
  - "Alex Beutel"
  - "Kai Xiao"
date: "2026-03-11"
arxiv_id: "2603.10521"
arxiv_url: "https://arxiv.org/abs/2603.10521"
pdf_url: "https://arxiv.org/pdf/2603.10521v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.CR"
  - "cs.LG"
tags:
  - "Agent Safety"
  - "Instruction Following"
  - "Reinforcement Learning"
  - "Training Dataset"
  - "Jailbreak Defense"
  - "Prompt Injection"
relevance_score: 7.5
---

# IH-Challenge: A Training Dataset to Improve Instruction Hierarchy on Frontier LLMs

## 原始摘要

Instruction hierarchy (IH) defines how LLMs prioritize system, developer, user, and tool instructions under conflict, providing a concrete, trust-ordered policy for resolving instruction conflicts. IH is key to defending against jailbreaks, system prompt extractions, and agentic prompt injections. However, robust IH behavior is difficult to train: IH failures can be confounded with instruction-following failures, conflicts can be nuanced, and models can learn shortcuts such as overrefusing. We introduce IH-Challenge, a reinforcement learning training dataset, to address these difficulties. Fine-tuning GPT-5-Mini on IH-Challenge with online adversarial example generation improves IH robustness by +10.0% on average across 16 in-distribution, out-of-distribution, and human red-teaming benchmarks (84.1% to 94.1%), reduces unsafe behavior from 6.6% to 0.7% while improving helpfulness on general safety evaluations, and saturates an internal static agentic prompt injection evaluation, with minimal capability regression. We release the IH-Challenge dataset (https://huggingface.co/datasets/openai/ih-challenge) to support future research on robust instruction hierarchy.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）中**指令层级**的鲁棒性训练难题。研究背景是，现代LLM被设计为处理来自不同信任级别角色（如系统管理员、应用开发者、用户、工具调用）的指令，而指令层级定义了当这些角色的指令发生冲突时，模型应遵循的优先级策略。这种策略是防御越狱攻击、系统提示提取和智能体提示注入等安全威胁的关键机制。

然而，现有方法在训练模型遵循指令层级时面临显著不足：首先，指令层级失败常与普通的指令遵循失败相混淆，难以精准定位和优化；其次，指令间的冲突可能非常微妙，需要模型具备细致的理解和推理能力；再者，模型容易学习到“捷径”行为，例如通过过度拒绝来简单应对冲突，但这会损害模型的有用性；最后，缺乏一个能够系统化、可扩展地训练和评估指令层级鲁棒性的高质量数据集。

因此，本文的核心问题是：**如何训练LLM，使其能够以一种能够泛化到多样任务领域并能抵御对抗性攻击的鲁棒方式，遵循指令层级策略？** 为解决此问题，论文引入了**IH-Challenge**数据集，这是一个基于强化学习设计的训练数据集，其构建遵循三个原则：确保任务本身简单以聚焦于冲突解决、支持通过Python代码进行客观评分以避免评估偏差，以及通过任务多样性防止模型学习取巧的捷径。通过在该数据集上对模型进行微调，论文旨在系统性提升LLM在指令层级上的鲁棒性、安全性和泛化能力。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕提升大语言模型指令层级（IH）鲁棒性的方法展开，可分为以下几类：

**基于训练的方法**：与本文最直接相关的是利用强化学习（RL）进行IH训练的工作。例如，有研究采用类似方法，基于IFEval数据集，将原始指令视为高层指令并生成违反它的低层攻击指令，通过RL最大化可编程验证的奖励。但本文指出，该数据集更侧重于指令遵循（IF）的困难任务而非纯粹的IH冲突，容易导致模型过度拒绝，且攻击字符串固定、对抗性不足。本文的IH-Challenge数据集则专门针对IH冲突设计，通过在线对抗样本生成增强鲁棒性，并验证了与前沿大模型的兼容性。

**基于提示或防御策略的方法**：例如“三明治防御”，即在助理生成回复前重复高层级指令。这种方法最初针对提示注入攻击提出，但也被发现有助于提升IH鲁棒性。与本文的主动训练不同，这类方法属于推理时策略，无需修改模型参数。

**模型架构调整**：有工作提出学习独立的角色嵌入并将其添加到指令的词元嵌入中，以实现更好的角色分离。这属于模型层面的修改，而本文专注于通过数据驱动的RL训练来改进现有模型的行为。

本文与这些工作的核心区别在于：1）**数据集焦点**：IH-Challenge专门针对IH冲突构建，任务设计为IF-simple但冲突微妙，旨在减少与一般指令遵循失败的混淆，并缓解过拒绝等捷径学习。2）**评估广度**：本文进行了分布内、分布外和人类红队测试等多维度评估，证明了训练效果可泛化至安全等难以编程评分的领域。3）**方法论启示**：本文结果表明，即使对于非编程可评任务，只要代理训练任务设计得当，RL仍可成为通用工具，拓展了相关RL文献的应用边界。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为IH-Challenge的强化学习训练数据集，并采用在线对抗性示例生成的训练流程，来系统性地提升大语言模型在指令层级冲突下的鲁棒性。其核心方法、架构设计和关键技术如下：

**整体框架与训练流程**：整体框架分为离线任务骨架构建和在线对抗性攻击生成两阶段。首先，离线阶段设计并验证了一系列“任务骨架”，每个骨架包含高优先级指令（来自系统或开发者角色）、一个用于放置低优先级冲突消息的占位符，以及一个用于评分的Python评分器。然后，在在线训练阶段，利用一个固定的攻击者模型，通过“提议-评估-修订”的循环，针对当前被训练模型（防御者）动态生成对抗性的低优先级指令，填充到任务骨架中，形成完整的冲突提示。最后，使用这些生成的冲突提示对防御者模型进行强化学习训练。

**主要模块/组件**：
1.  **任务骨架**：是数据集的基础单元，根据设计原则构建：
    *   **IF-简单性**：确保任务本身指令跟随简单，从而将模型失败主要归因于IH处理而非任务复杂性。
    *   **可编程评分性**：确保即使存在对抗性输入，也能通过Python代码客观评分。
    *   **避免捷径学习**：通过多样化任务模式（如单约束、多约束、输入条件、反过度拒绝等），防止模型学习“一看到密码就拒绝”等脆弱启发式规则。
2.  **在线对抗攻击生成器（攻击者）**：这是一个冻结的、无安全护栏的LLM。它接收任务骨架和高优先级指令，目标是为当前防御者模型生成能诱导其违反IH的低优先级消息。它通过一个有预算的循环与一个评估工具交互，不断根据评分反馈优化攻击策略。
3.  **防御者模型训练**：采用强化学习，利用在线生成的冲突提示进行训练。对每个提示采样多个模型响应，用对应的Python评分器计算奖励，并进行策略梯度更新。为防止能力退化，训练数据中混合了少量专注于通用能力的任务。

**创新点**：
1.  **数据构造方法论**：将IH训练数据构造分解为“离线确定评分标准”和“在线生成对抗冲突”两个阶段，既保证了评分器的有效性和稳定性，又实现了对抗示例的多样性和动态适应性。
2.  **动态对抗训练**：创新性地使用一个攻击者LLM在线探测并攻击正在训练的防御者模型，使得训练数据能够随着防御者能力的提升而不断变难，实现了“水涨船高”的对抗性训练，有效覆盖了复杂的、动态演进的攻击策略。
3.  **针对性的任务设计**：专门设计了“反过度拒绝”类任务，直接针对IH训练中常见的模型通过过度拒绝来取巧的问题，迫使模型学习更精细的、基于优先级顺序的冲突解决策略，而非简单的安全过滤。
4.  **系统化的评估**：不仅使用动态生成的对抗示例进行训练，还构建了静态评估集来衡量模型的泛化能力，并在一系列分布内、分布外和人工红队基准上验证了方法的有效性。

### Q4: 论文做了哪些实验？

该论文通过一系列实验验证了IH-Challenge数据集在提升大语言模型指令层级（IH）鲁棒性方面的有效性。实验设置上，研究以GPT-5-Mini为基线模型，使用IH-Challenge数据集通过在线对抗样本生成的强化学习（RL）方法进行微调，并评估其性能。

实验涉及多个数据集和基准测试：
1.  **分布内与分布外IH评估**：包括IH-Challenge自身的四个子集（如Refusal、Composite）、内部保留的攻击集（模拟攻击、自动化攻击、人类红队攻击）以及内部OOD任务（如Tutor Jailbreak、多轮对话冲突）。
2.  **学术IH评估**：包括Gandalf Password、TensorTrust、RealGuardrails和System IFEval等公开数据集，用于评估系统/用户等指令对冲突。
3.  **能力与过度拒绝评估**：使用GPQA Diamond和AIME 2024评估通用能力；使用IH-Challenge (overrefusal)和TensorTrust (overrefusal)评估模型是否因任务类型而过度拒绝。
4.  **安全性与实用性评估**：使用OpenAI生产基准（Production Benchmarks）评估在添加安全规范后，模型在多个禁止内容类别上的拒绝率和帮助性。
5.  **提示注入评估**：使用内部静态提示注入基准和CyberSecEval 2评估抗提示注入能力。

主要对比方法为微调前的基线模型（baseline）。关键结果如下：
*   **IH鲁棒性显著提升**：微调后模型在16个分布内、分布外和人类红队基准上的平均IH鲁棒性从84.1%提升至94.1%（+10.0%）。在多项具体评估中取得提升，例如System<>User Conflict从0.84提升至0.95，Developer<>User Conflict从0.83提升至0.95。
*   **安全性大幅改善**：不安全行为从6.6%降至0.7%。在添加安全规范后，模型在所有禁止内容类别上的安全拒绝率均显著高于基线，且帮助性未下降。
*   **提示注入防御能力增强**：在内部静态提示注入基准上达到饱和性能（从0.44提升至1.00），在CyberSecEval 2上从0.88提升至0.91。
*   **能力回归极小**：在GPQA Diamond（0.83 vs 0.83）和AIME 2024（0.93 vs 0.94）等能力基准上表现持平或略有提升。仅在对话胜率（0.71 vs 0.66）和用户偏好得分（0.46 vs 0.40）上有轻微下降。过度拒绝评估显示模型未学会基于任务类型的简单拒绝策略。

### Q5: 有什么可以进一步探索的点？

该论文在提升大模型指令层级（IH）鲁棒性方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，论文发现当模型通过IH-Challenge训练变得足够鲁棒后，传统的系统级缓解措施（如输出监控、改写）的边际效益会下降，甚至可能损害模型能力。这表明单纯依赖外部“补丁”可能并非最优，未来研究可探索如何将这类防御机制更深度、更高效地集成到模型内部，或开发新型的动态、轻量级系统防护策略。

其次，论文在对抗性评估中采用了固定防御模型的设定，而现实中的攻击是持续演进的。尽管实验表明输出监控能减缓自适应攻击者的学习速度，但攻击成功率仍会逐步上升。这提示未来需要构建更动态的“攻防博弈”训练框架，让防御模型也能在线更新，形成持续的对抗性强化学习循环，以应对不断升级的攻击手段。

此外，论文的评估主要集中于指令冲突场景下的安全性与拒绝行为，对于模型在复杂、多轮的真实世界代理任务中，如何平衡工具调用、用户意图和系统约束的层级决策，研究尚不充分。未来可以构建更复杂的、涉及长期规划和工具使用的IH评估基准，并探索如何让模型学会在遵循层级的同时，保持高帮助性和流畅的协作能力。

最后，论文的消融实验表明，数据集中不同任务切分的组合对平衡鲁棒性与过度拒绝至关重要。这启发我们可以进一步研究数据合成与课程学习策略，例如设计渐进式难度的训练样本，或引入更细粒度的奖励信号，以更精准地塑造模型的IH行为，减少能力退化。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型（LLM）中指令层级（IH）的鲁棒性问题展开研究。指令层级定义了模型在系统、开发者、用户和工具指令发生冲突时的优先级策略，是防御越狱攻击、系统提示提取和智能体提示注入的关键。然而，由于IH失败常与指令遵循失败混淆、冲突场景微妙且模型易学习“过度拒绝”等捷径，训练出稳健的IH行为十分困难。

为解决此问题，作者提出了IH-Challenge训练数据集。该方法的核心是使用该数据集，结合在线对抗样本生成技术，对GPT-5-Mini等前沿模型进行微调。实验表明，该方法能有效提升模型的IH鲁棒性，在16个分布内、分布外及人工红队评估基准上平均提升10.0%（从84.1%至94.1%），同时将不安全行为从6.6%降至0.7%，并在通用安全评估中保持了帮助性。该方法还显著提升了对抗智能体提示注入的能力，且模型能力衰退最小。

论文的核心贡献在于发布了一个旨在提升指令层级鲁棒性的高质量训练数据集，并验证了基于该数据集进行强化学习微调的有效性，为未来构建更安全、可靠且能妥善处理指令冲突的大语言模型提供了重要的数据资源和方法路径。
