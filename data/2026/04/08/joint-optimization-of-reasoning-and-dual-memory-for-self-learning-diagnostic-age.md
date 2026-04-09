---
title: "Joint Optimization of Reasoning and Dual-Memory for Self-Learning Diagnostic Agent"
authors:
  - "Bingxuan Li"
  - "Simo Du"
  - "Yue Guo"
date: "2026-04-08"
arxiv_id: "2604.07269"
arxiv_url: "https://arxiv.org/abs/2604.07269"
pdf_url: "https://arxiv.org/pdf/2604.07269v1"
categories:
  - "cs.CL"
tags:
  - "Diagnostic Agent"
  - "Self-Learning"
  - "Dual-Memory"
  - "Reinforcement Training"
  - "Clinical Reasoning"
  - "Continual Learning"
  - "Experience Reuse"
relevance_score: 8.0
---

# Joint Optimization of Reasoning and Dual-Memory for Self-Learning Diagnostic Agent

## 原始摘要

Clinical expertise improves not only by acquiring medical knowledge, but by accumulating experience that yields reusable diagnostic patterns. Recent LLMs-based diagnostic agents have shown promising progress in clinical reasoning for decision support. However, most approaches treat cases independently, limiting experience reuse and continual adaptation. We propose SEA, a self-learning diagnostic agent with cognitively inspired dual-memory module. We design a reinforcement training framework tailored to our designed agent for joint optimization of reasoning and memory management. We evaluate SEA in two complementary settings. On standard evaluation with MedCaseReasoning dataset, SEA achieves 92.46% accuracy, outperforming the strongest baseline by +19.6%, demonstrating the benefit of jointly optimizing reasoning and memory. On the long-horizon with ER-Reason dataset, SEA attains the best final accuracy (0.7214) and the largest improvement (+0.35 Acc@100), while baseline methods show limited or unstable gains. Expert evaluation further indicates that rules consolidated from SEA show strong clinical correctness, usefulness and trust, suggesting that the induced rules in dual-memory module are reliable and practically meaningful. Overall, SEA improves both diagnostic reasoning ability and continual learning by effectively transforming experience into reusable knowledge.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的临床诊断智能体在持续学习和经验复用方面的核心瓶颈。研究背景是，在真实临床实践中，专家的诊断能力不仅源于静态的医学知识，更依赖于从既往病例中积累经验、形成可复用的诊断模式。尽管现有基于LLM的诊断智能体在临床推理和决策支持方面已取得进展，但大多数方法将每个病例视为独立任务进行处理，缺乏跨病例的经验积累和持续适应能力，这限制了智能体像人类专家一样通过实践不断自我提升。现有方法的不足在于，它们主要关注“诊断什么”（即获取医学知识），而非“如何通过经验改进诊断过程”，并且缺乏高效的长时记忆管理机制来应对医学领域信息密集、证据可能不完整、且需要抽象出可重用启发式规则（而非简单存储轨迹）的独特挑战。

因此，本文要解决的核心问题是：**如何设计一个能够像临床专家一样，从持续积累的诊疗经验中进行有效学习、并将具体病例抽象为可复用知识以提高长期诊断性能的自我学习诊断智能体**。具体而言，论文提出了一个名为SEA的智能体，通过引入受认知启发的双记忆模块（分别存储近期具体病例的短时记忆和抽象诊断规则的长时记忆）以及一个联合优化推理与记忆管理的强化学习训练框架，来系统性地解决经验存储、抽象和再利用的问题，从而实现诊断推理能力和持续学习能力的共同提升。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在方法类中，相关工作包括：1）**用于疾病诊断的LLM智能体**：现有研究利用通用或领域专用的多模态模型作为临床决策主干，并通过结构化工作流（如可追溯的罕见病系统、分层推理框架）和多智能体协作来提升诊断过程的可靠性与效率。2）**智能体AI的记忆机制**：早期系统依赖结构化中间表示（如证据链）来跟踪推理状态；近期工作则将记忆设计为显式的、可学习组件，用于积累经验、跟踪决策并改进未来行为，例如在多智能体诊断中充当持久记忆或存储反馈以实现自适应。3）**用于长视野自我演进的强化学习**：在医疗领域，RL被用于建模序列化假设检验与证据获取，使智能体能够通过经验反馈优化决策策略。

本文提出的SEA智能体与这些工作的关系在于，它整合了上述三个方向的核心思想：采用基于LLM的智能体架构、引入受认知启发的双记忆模块，并设计专门的强化学习框架进行联合优化。其区别在于，现有方法大多将病例独立处理，限制了经验的复用与持续适应；而SEA通过**联合优化推理与记忆管理**，实现了对诊断经验的系统性积累与转化，从而在标准评测和长视野任务中均表现出更优的准确率与持续学习能力。

在应用与评测层面，相关研究建立了临床推理数据集（如MedCaseReasoning）和评估流程。本文在此基础上进行了扩展性评估，并引入专家评价来验证所生成规则的临床正确性与实用性，进一步突出了SEA在产生可靠、可复用知识方面的优势。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SEA的自学习诊断智能体，其核心是结合了认知启发的双记忆模块与强化学习训练框架，以联合优化推理和记忆管理，从而解决现有方法将病例独立处理、限制经验复用和持续适应的问题。

**整体框架与主要模块**：SEA的架构基于一个强化学习框架，在每个回合t，策略模型观察患者病例x_t，在输出最终诊断和推理结果o_t之前，可以调用记忆操作。智能体控制两个记忆集群：**短期病例记忆集群**存储最近的具体病例及其结果（诊断、反馈等），具有固定容量K，支持列表、追加、弹出操作；**长期规则记忆集群**存储从经验中提炼出的抽象诊断规则（如症状-疾病关联），支持列表和整合操作。智能体的状态s_t由这两个记忆集群共同构成。这种双记忆设计模拟了临床专家既记住具体案例又提炼可重用模式的能力，并使记忆瓶颈显式化，由智能体自主决定保留什么、抽象什么，而非依赖可能丢弃关键证据的外部启发式方法。

**关键技术细节**：记忆操作被设计为智能体的动作u_t，包括列表、追加、弹出和整合。诊断输出和记忆更新决策共同构成一个回合的展开。奖励函数被分解为诊断奖励和记忆管理奖励，并通过线性插值的时变权重进行**奖励塑形**：早期回合更强调记忆形成（鼓励获取和整合信息），后期回合更强调诊断准确性，以应对长视野诊断中的冷启动问题。为避免非平稳奖励导致的训练不稳定，论文采用**回合优势估计**，对每个回合位置独立计算组内相对优势，并用于策略优化。

**创新点**：1) **认知启发的双记忆架构**，显式区分具体案例记忆和抽象规则记忆，支持经验的有效沉淀与复用；2) **将记忆管理作为可学习动作**，与诊断推理在统一的强化学习框架下进行**联合优化**，使智能体能自主决定记忆的存储、淘汰与提炼；3) **时变奖励塑形机制**，引导智能体在训练过程中从注重经验积累自然过渡到注重诊断精度；4) **回合级优势估计方法**，提升了非平稳奖励下的训练稳定性。这些设计使得SEA不仅能做出准确诊断，还能持续地将经验转化为可靠、有用的知识，从而在标准评估和长视野任务中均取得显著提升。

### Q4: 论文做了哪些实验？

论文在两个互补的实验设置下评估SEA模型：标准评估和长时程评估。在标准评估中，实验使用MedCaseReasoning数据集，该数据集包含具有挑战性的临床病例和诊断标签，采用封闭集评估方式，每个病例提供199个临床可信的干扰项。基线方法包括零样本、监督微调、强化学习和记忆增强模型，使用了Qwen3、OLMo3、LLaMa-3.1和MedGemma等不同规模的模型。主要结果显示，SEA（Qwen-8b）取得了92.46%的准确率和86.81%的宏F1分数，分别比最强基线高出19.6%和20.1%。在长时程评估中，实验使用ER-Reason数据集模拟流式环境，评估模型利用反馈持续改进的能力。评估指标包括最终准确率和在特定轮次后的性能提升（ΔAcc@n）。结果显示，SEA（Qwen-8b）取得了最佳最终准确率（0.7214）和最大的长期改进（ΔAcc@100 = +0.35），显著优于所有基线方法。实验表明，联合优化推理和双记忆管理能带来显著性能提升，而简单的记忆集成可能损害性能，SEA则能有效避免这一权衡。

### Q5: 有什么可以进一步探索的点？

基于论文内容，未来可进一步探索的方向包括：首先，提升规则与具体病例的相关性。论文指出，SEA诱导的规则在“病例相关性”上得分较低，这是其设计上为追求泛化性而做出的权衡。未来研究可以探索如何在不牺牲规则普适性的前提下，更好地融合病例特异性细节，例如通过设计更精细的记忆检索机制或引入分层规则表示。其次，优化记忆管理的通用性与可解释性。当前的强化学习框架是针对特定诊断任务设计的，未来可研究如何将该双内存架构与联合优化范式泛化到更广泛的持续学习场景（如法律咨询、故障诊断），并增强规则生成与决策过程的可解释性，以进一步提升临床信任度。最后，探索更复杂环境下的长期性能。论文在长视野评估中展示了优势，但现实临床环境更为动态复杂（如疾病谱演变、新知识引入）。未来可测试智能体在非平稳数据流下的鲁棒性，并研究如何将外部权威医学知识库与内部归纳的经验规则进行安全、有效的融合与更新。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为SEA的自学习诊断智能体，其核心在于通过认知启发的双记忆模块和联合优化框架，解决现有基于大语言模型的诊断智能体在处理病例时经验难以复用和持续适应的问题。SEA设计了双记忆模块（可能包括短期和长期记忆），并构建了一个强化学习训练框架，以联合优化诊断推理过程和记忆管理策略。论文在MedCaseReasoning数据集上的标准评估表明，SEA取得了92.46%的准确率，显著优于基线方法；在ER-Reason数据集的长周期任务中，SEA也获得了最佳最终准确率和最大性能提升。专家评估进一步证实，SEA双记忆中固化的规则具有临床正确性、实用性和可信度。主要结论是，SEA通过将诊疗经验有效转化为可复用的知识，同时提升了诊断推理能力和持续学习性能，为构建更智能、更适应临床实践的诊断辅助系统提供了新思路。
