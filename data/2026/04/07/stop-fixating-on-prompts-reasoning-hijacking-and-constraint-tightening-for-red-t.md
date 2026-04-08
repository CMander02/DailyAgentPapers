---
title: "Stop Fixating on Prompts: Reasoning Hijacking and Constraint Tightening for Red-Teaming LLM Agents"
authors:
  - "Yanxu Mao"
  - "Peipei Liu"
  - "Tiehan Cui"
  - "Congying Liu"
  - "Mingzhe Xing"
  - "Datao You"
date: "2026-04-07"
arxiv_id: "2604.05549"
arxiv_url: "https://arxiv.org/abs/2604.05549"
pdf_url: "https://arxiv.org/pdf/2604.05549v1"
categories:
  - "cs.CL"
tags:
  - "Agent Security"
  - "Red-Teaming"
  - "Jailbreaking"
  - "Reasoning Hijacking"
  - "Memory Manipulation"
  - "Adversarial Attack"
  - "Constraint Tightening"
  - "LLM Agent"
relevance_score: 8.0
---

# Stop Fixating on Prompts: Reasoning Hijacking and Constraint Tightening for Red-Teaming LLM Agents

## 原始摘要

With the widespread application of LLM-based agents across various domains, their complexity has introduced new security threats. Existing red-team methods mostly rely on modifying user prompts, which lack adaptability to new data and may impact the agent's performance. To address the challenge, this paper proposes the JailAgent framework, which completely avoids modifying the user prompt. Specifically, it implicitly manipulates the agent's reasoning trajectory and memory retrieval with three key stages: Trigger Extraction, Reasoning Hijacking, and Constraint Tightening. Through precise trigger identification, real-time adaptive mechanisms, and an optimized objective function, JailAgent demonstrates outstanding performance in cross-model and cross-scenario environments.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在广泛应用背景下所面临的新型安全威胁问题，特别是现有“红队”测试方法在攻击有效性和隐蔽性上的不足。

研究背景是，随着LLM智能体在视频分析、临床决策等高价值高风险场景中的部署，其复杂的推理、规划和记忆机制引入了比单一LLM更广泛的攻击面。现有的红队测试方法主要存在三大局限：首先，它们大多依赖于直接修改用户提示（如伪装、反向工程），这种方法缺乏对新数据和新场景的自适应能力，导致泛化性能差；其次，这些显式的提示修改往往会影响智能体在正常任务上的性能，使其行为模式容易被防御机制检测，攻击隐蔽性低；最后，这类方法可能使模型的输出难以与用户的原始意图对齐。

针对这些不足，本文的核心目标是提出一种**无需修改用户原始提示**的、能够隐式操控智能体内部决策过程的通用攻击框架。具体而言，论文试图解决如何在不触碰用户输入的前提下，通过理解并劫持智能体的底层推理轨迹和记忆检索过程，来实现高效、隐蔽且具有跨模型和跨场景适应性的“越狱”攻击。为此，论文提出了名为JailAgent的框架，通过“触发词提取”、“推理劫持”和“约束收紧”三个关键阶段，从精准识别攻击点、实时自适应学习到优化攻击目标的语义特征，系统地实现了对智能体决策过程的隐式操控，旨在使红队测试更能反映真实的模型对抗动态，并提升攻击的实用性和鲁棒性。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕大语言模型（LLM）及其智能体的安全评估与攻击方法展开，可分为以下几类：

**1. 基于提示的越狱方法**：这是传统的主流方法，通过精心设计或优化对抗性提示来绕过模型的安全过滤器，诱导模型生成有害内容。本文指出这类方法通常依赖于修改用户提示，缺乏对新数据的适应性，且可能影响智能体的正常性能。

**2. 智能体安全与攻击研究**：随着基于LLM的智能体在复杂任务中的应用，针对其决策过程的新型攻击开始出现。与仅关注文本生成的LLM越狱不同，智能体越狱的目标是操纵其内部状态（如记忆、推理轨迹）和奖励函数，使其执行非预期的动作序列，同时可能达成表面正确的最终结果。本文的JailAgent框架属于此类，但区别于现有工作，它完全避免修改用户提示，转而通过“推理劫持”和“约束收紧”来隐式操控智能体的内部运作。

**3. 红队测试与安全评估框架**：已有研究致力于开发系统化的方法来测试LLM和智能体的安全性。本文提出的JailAgent是一个专门针对智能体的红队框架，其创新在于通过白盒访问记忆存储、利用本地模型进行概率估计，并设计了分阶段的自动化攻击流程，从而在跨模型和跨场景环境中实现高效、自适应的攻击，弥补了传统方法在适应性和对智能体影响方面的不足。

### Q3: 论文如何解决这个问题？

论文提出的JailAgent框架通过三个核心阶段——触发词提取、推理劫持和约束收紧——来解决LLM智能体安全测试中过度依赖修改用户提示的问题。其核心方法在于不直接修改用户输入，而是隐式操纵智能体的推理轨迹和记忆检索。

整体框架采用分层递进的架构设计。首先，在触发词提取阶段，通过BERT子词分词与spaCy句法分析相结合，将用户输入分解为名词短语和动词短语组，并采用从粗到细的两阶段重要性分析：粗粒度阶段通过掩码测试和KL散度计算组级重要性分数；细粒度阶段则在关键组内进行词级分析，最终输出高贡献触发词集合。这一设计创新性地将句法信息与子词表示对齐，实现了对语义空间的细粒度建模。

推理劫持阶段的核心模块是一个基于Sentence Transformer的再排序模型。该模型通过即时样本合成构建训练数据，采用成对排序损失函数，使模型学会为包含恶意内容的响应分配更高分数。在推理时，系统首先生成多个候选答案，然后利用再排序模型筛选出偏离正常推理的答案，从而实现对生成过程的隐式控制。这一方法避免了传统红队方法对提示的直接修改，保持了智能体原有性能。

约束收紧阶段则通过多目标优化确保触发词的攻击有效性和泛化能力。关键技术包括四种联合优化的损失函数：特殊性损失使触发词远离正常语义簇中心；聚类损失保持触发词内部嵌入的紧凑性；可分离性损失优化检索场景下的攻击成功率；边际损失则增大触发词与恶意条目之间的相似度差距。这些损失函数共同作用，使触发词在跨模型和跨场景环境中保持稳定性能。

创新点主要体现在三个方面：一是完全避免修改用户提示，通过隐式操纵实现攻击；二是提出了分层细粒度的触发词提取方法，结合了句法分析和概率分布变化；三是设计了多目标优化的约束收紧机制，确保了攻击的适应性和鲁棒性。整个框架通过精准的触发词识别、实时自适应机制和优化的目标函数，在保持智能体正常功能的同时，有效揭示了其安全漏洞。

### Q4: 论文做了哪些实验？

实验评估了所提出的JailAgent框架在多种任务导向型智能体上的泛化能力和攻击效果。实验设置方面，选取了三个代表性的智能体：用于长视频理解的VideoAgent、用于协调推理与行动的ReAct-UALA，以及用于电子健康记录复杂推理的EHRAgent。主要评估基准包括StrategyQA、MMLU和HotpotQA数据集，并采用了ASR-R（原始攻击成功率）、ASR-L（宽松攻击成功率）、ASR-H（严格攻击成功率）、EM（精确匹配）和CR（内容保留率）等多个指标。

对比方法包括三种基线红队方法：PAIR、AgentPoison和BadChain，以及无攻击的基准情况（Non-attack）。实验在多个大模型骨干上进行，包括GPT-3.5-turbo、GPT-4o、GPT-5、Llama-3.1-70B和Claude-3.5-haiku。

主要结果显示，JailAgent在几乎所有设置中都取得了最高的攻击成功率（ASR），同时保持了较高的内容保留率（CR），表明其攻击有效且对原始任务性能影响较小。例如，在GPT-4o骨干的ReAct-UALA智能体上，JailAgent在StrategyQA任务上的ASR-R达到73.80%，高于AgentPoison的69.87%和BadChain的62.88%。在GPT-5骨干上，JailAgent在MMLU任务上的ASR-R达到70.18%，显著优于其他基线。关键数据指标方面，JailAgent在跨模型和跨任务的平均攻击成功率（ALL列）上均领先，如在GPT-4o上达到61.739%，在GPT-5上达到63.080%，证明了其优越的泛化性和有效性。

### Q5: 有什么可以进一步探索的点？

本文提出的JailAgent框架虽在免修改用户提示的对抗攻击上取得进展，但仍存在若干局限与可拓展方向。首先，其“推理劫持”机制高度依赖对目标代理内部状态（如思维链、记忆）的精确监控与干预，这在黑盒或部分可观测的商用代理中可能难以实施。未来可探索基于输入输出交互的间接推断方法，或结合强化学习动态学习劫持策略。其次，框架主要针对已知任务流程的代理，对于具备强自适应能力的元认知代理（如能自我修正推理的Agent），攻击效果可能下降。可研究如何引入对抗性环境扰动或长期记忆污染来应对。此外，当前工作集中于安全威胁演示，未来需同步设计防御机制，例如在代理中嵌入异常推理检测模块或引入不确定性校准。最后，可探索该框架在正向领域的应用，如通过引导式劫持帮助代理突破思维定式，或用于模型可解释性研究。

### Q6: 总结一下论文的主要内容

本文针对基于大语言模型的智能体（LLM Agent）面临的安全威胁，提出了一个名为JailAgent的新型红队测试框架。其核心问题是：现有红队方法大多依赖修改用户提示（prompt），这缺乏对新数据的适应性，且可能影响智能体正常性能。为解决此问题，JailAgent完全避免修改用户原始提示，转而通过隐式操纵智能体的推理轨迹和记忆检索过程来实现攻击。

方法上，JailAgent采用三阶段流水线：1）触发词提取：通过句法和子词对齐机制，结合对数概率变化和逐步KL引导的重要性估计，自动识别高贡献潜力的触发词；2）推理劫持：构建一个具有实时自适应能力的重排序机制，能基于当前提示动态生成配对数据，并利用冻结编码器和轻量级评分头进行快速微调，以实时学习触发词偏差；3）约束收紧：设计了特殊性损失、聚类损失、可分离性损失和边界损失四个互补的优化目标，在语义空间中对触发词嵌入的特性进行联合约束，以提升其泛化性和稳定性。

主要结论表明，JailAgent在跨模型、跨场景的环境中表现出色。通过在多种智能体类型、大模型核心、数据集和评估指标上的系统实验，验证了该框架在攻击成功率、泛化能力和隐蔽性方面的优越性。其核心贡献在于提供了一种不修改用户提示、更贴近真实对抗动态的红队测试新范式，对理解和评估智能体系统的安全性具有重要意义。
