---
title: "MediHive: A Decentralized Agent Collective for Medical Reasoning"
authors:
  - "Xiaoyang Wang"
  - "Christopher C. Yang"
date: "2026-03-28"
arxiv_id: "2603.27150"
arxiv_url: "https://arxiv.org/abs/2603.27150"
pdf_url: "https://arxiv.org/pdf/2603.27150v1"
categories:
  - "cs.AI"
  - "cs.MA"
tags:
  - "Multi-Agent Systems"
  - "Decentralized Architecture"
  - "Medical Reasoning"
  - "Role Assignment"
  - "Consensus Mechanism"
  - "LLM-based Agents"
  - "Agent Collaboration"
relevance_score: 7.5
---

# MediHive: A Decentralized Agent Collective for Medical Reasoning

## 原始摘要

Large language models (LLMs) have revolutionized medical reasoning tasks, yet single-agent systems often falter on complex, interdisciplinary problems requiring robust handling of uncertainty and conflicting evidence. Multi-agent systems (MAS) leveraging LLMs enable collaborative intelligence, but prevailing centralized architectures suffer from scalability bottlenecks, single points of failure, and role confusion in resource-constrained environments. Decentralized MAS (D-MAS) promise enhanced autonomy and resilience via peer-to-peer interactions, but their application to high-stakes healthcare domains remains underexplored. We introduce MediHive, a novel decentralized multi-agent framework for medical question answering that integrates a shared memory pool with iterative fusion mechanisms. MediHive deploys LLM-based agents that autonomously self-assign specialized roles, conduct initial analyses, detect divergences through conditional evidence-based debates, and locally fuse peer insights over multiple rounds to achieve consensus. Empirically, MediHive outperforms single-LLM and centralized baselines on MedQA and PubMedQA datasets, attaining accuracies of 84.3% and 78.4%, respectively. Our work advances scalable, fault-tolerant D-MAS for medical AI, addressing key limitations of centralized designs while demonstrating superior performance in reasoning-intensive tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在复杂医疗推理任务中面临的挑战，特别是单一智能体系统在处理需要跨学科知识、应对不确定性及冲突证据的综合性医学问题时能力不足的问题。研究背景是，尽管LLM已革新了医疗推理，催生了用于模拟多学科团队协作的多智能体系统（MAS），但当前主流的MAS多采用集中式架构，由中心协调者管理任务流。

现有集中式方法存在明显不足：首先，可扩展性有限，中心智能体在应对大量智能体或高并发查询时易成为性能瓶颈；其次，存在单点故障风险，一旦协调者失效，整个系统可能瘫痪，这在医疗等高风险领域尤为致命；最后，在资源受限环境下（如单一LLM实例模拟多个角色时），容易引发角色混淆和知识泄露，导致推理不一致和专业性稀释。

因此，本文的核心问题是：如何为医疗问答设计一个既高效又可靠的协作推理框架，以克服集中式多智能体系统的上述缺陷。为此，论文提出了MediHive——一个新颖的去中心化多智能体框架。它通过引入共享记忆池和迭代融合机制，使基于LLM的智能体能够自主分配专业角色、进行初步分析、通过基于证据的条件性辩论检测分歧，并在多轮中局部融合同伴见解以达成共识，从而在没有中央协调者的情况下实现可扩展、容错且角色清晰的医疗推理。

### Q2: 有哪些相关研究？

相关研究主要可分为多智能体系统（MAS）框架、医疗领域应用以及协作机制三类。

在**通用多智能体系统框架**方面，AutoGen 提出了支持角色化智能体（如指挥官、写手）协作的对话式工作流框架，用于代码生成等任务。AgentNet 则探索了去中心化的进化协调机制，通过档案进化和对等交互优化智能体专长。这些工作为多智能体协作奠定了基础，但多为通用设计或集中式架构。

在**医疗领域应用**上，多智能体系统被用于模拟多学科团队。MedAgents 率先在零样本场景下利用角色扮演进行多轮医学讨论，提升了MedQA等数据集的准确率。MDAgents 引入了自适应协作机制，根据查询复杂度分配专家角色并决定独立或合作模式。AgentHospital 构建了虚拟医院环境，模拟医生、护士和患者的完整护理周期。LLM-MedQA 则专注于基于案例的推理，通过辩论和共识优化医学问答答案。这些研究均证实了多智能体协作在医疗推理中的价值，但大多依赖于集中式协调器。

在**协作机制**层面，辩论协议被广泛应用于处理证据分歧，通过论证性交换达成共识，相关策略已被适配到医疗场景中。

本文提出的MediHive与上述工作的核心区别在于其**去中心化架构**。它摒弃了集中式协调器，通过共享记忆池和迭代融合机制，使智能体能够自主分配角色、进行基于证据的条件性辩论，并本地融合多方见解。这直接针对了现有集中式系统在可扩展性、单点故障和资源受限环境下的角色混淆等瓶颈，填补了医疗领域去中心化、高容错多智能体系统设计的空白。

### Q3: 论文如何解决这个问题？

MediHive通过构建一个去中心化的多智能体协作框架来解决复杂医学推理问题，其核心方法、架构设计和关键技术如下：

**整体框架与核心方法**：MediHive采用完全去中心化的架构，摒弃了传统多智能体系统中的中央协调器。其核心是一个共享内存池（Shared Memory Pool）作为被动、仅追加的存储库，记录所有智能体的交互历史，但不参与任何决策或协调逻辑。所有推理、评估和共识构建均由智能体自主完成。框架工作流程包含五个关键阶段：查询初始化与自主角色分配、初始分析、分歧检测与条件性辩论、迭代共享融合、共识聚合与输出生成。

**主要模块与组件**：
1.  **自主角色分配模块**：采用两阶段“热身”机制。首先，每个智能体基于查询独立提出初始角色提案（如“胃肠病学家”）；随后，所有智能体读取同伴提案，通过自我反思优化三个内部指标（清晰度、差异化、对齐度）来精炼最终角色，形成互补的专业分工。
2.  **条件性辩论机制**：在初始分析后，每个智能体自主检测答案分歧（如未达到预设阈值τ_agree=0.8）。若存在显著分歧，则触发多轮辩论（如T_debate=2轮）。辩论中，智能体可进行三种形式的论证：反驳（挑战同伴推理）、辩护（强化自身立场）或提案（综合多方见解提出新假设）。辩论旨在丰富证据基础，而非直接更新答案。
3.  **迭代共享融合模块**：这是智能体正式更新答案和置信度的唯一阶段。首轮融合（k=2）中，每个智能体全面整合内存池中所有历史交互（初始分析和完整辩论记录），进行批判性评估与证据融合。后续轮次（k>2）则仅关注前一轮同伴的输出，逐步细化立场。融合循环持续直至达成稳定共识（连续两轮超过τ_agree）或达到最大轮次K。
4.  **共识聚合机制**：由专门的“报告者”角色执行最终输出。若达成共识，则采用多数投票；否则，使用置信度加权投票选择最终答案，并综合整个交互轨迹生成最终推理链。

**创新点**：
- **去中心化协同设计**：通过共享内存池实现纯对等交互，消除了单点故障和可扩展性瓶颈，增强了系统的韧性和适应性。
- **自我演化的角色分配**：智能体基于查询内容和同伴提案动态优化专业分工，避免了角色混淆，确保了多样化的专业知识覆盖。
- **对抗与融合分离的两阶段机制**：将“条件性辩论”（对抗性证据生成）与“迭代共享融合”（综合性立场更新）明确分离，使推理过程兼具批判性深度和收敛效率。
- **自主分歧检测与共识形成**：每个智能体独立评估群体状态，无需中央仲裁器即可触发辩论或判定共识，实现了真正的分布式决策。

### Q4: 论文做了哪些实验？

论文在医学问答任务上进行了全面的实验评估。实验设置方面，所有实验均采用Llama-3.1-70B-Instruct作为基础大语言模型，并在零样本协作设置下进行。为了公平比较，所有基线方法（包括最初使用不同模型评估的多智能体方法）均在此相同骨干模型上重新实现。

使用的数据集/基准测试包括两个广泛使用的医学问答基准：PubMedQA和MedQA。PubMedQA是一个生物医学研究问答数据集，包含需要是/否/可能答案的问题及其支持推理的PubMed摘要，强调基于科学文本的定量和证据推理。MedQA是一个源自美国医师执照考试的大规模开放域问答数据集，采用四选一或五选一的多选题形式，全面挑战模型的医学知识。

对比方法分为两大类。单智能体基线评估了基础LLM在不同提示策略下的性能：标准零样本、带思维链的零样本以及增加了自洽性（采样多条推理路径）的增强版本。这些方法的平均准确率最高为74.1%。多智能体基线包括：一个集中式多智能体系统（使用一个协调器智能体分配角色并主持多轮讨论）、最先进的框架MedAgents（采用基于角色的协作咨询与集中式报告合成）以及Multiagent Debate（通过迭代多智能体辩论提高事实性）。

主要结果显示，MediHive在MedQA和PubMedQA上分别取得了84.3%和78.4%的准确率，总体平均准确率达到81.4%。这比最强的单智能体方法高出7.3个百分点，并且超越了领先的多智能体基线（例如，比MedAgents的80.3%平均准确率高1.1个百分点）。关键数据指标包括：MediHive在MedQA上的F1分数为82.5%，在PubMedQA上为76.8%。此外，消融研究表明，移除思维链推理会使MedQA准确率降至78.0%，PubMedQA降至73.0%；移除自演化角色分配则分别降至81.5%和75.9%。实验还探讨了智能体数量（N）的影响，发现N=5时在两种数据集上均达到最佳性能。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要集中在验证环境、评估维度、知识来源和安全性四个方面。未来研究可首先将框架从封闭的基准测试扩展到更贴近真实临床环境的模拟或试点应用，以评估其在动态、多模态和模糊信息下的鲁棒性。其次，需建立更全面的评估体系，纳入严格的统计检验、计算效率（如延迟、token消耗）及大规模扩展性分析。在架构改进上，集成RAG机制以接入实时外部知识库是明确方向，这能缓解幻觉问题并提升答案的时效性与准确性。此外，论文提及但未深入的系统性安全风险评估至关重要，未来应设计针对医疗领域的高风险错误（如高置信度误判）的监测与缓解机制，并开发相应的安全感知评估指标。最后，可探索智能体更复杂的协作策略，如在辩论中引入不确定性量化和动态权重调整，以进一步提升共识形成的质量与效率。

### Q6: 总结一下论文的主要内容

本文提出了一种名为MediHive的去中心化多智能体框架，旨在解决复杂医疗推理任务中的挑战。核心问题是单一智能体在处理需要跨学科知识和处理不确定性的复杂医疗问题时存在局限，而现有的集中式多智能体系统则面临可扩展性瓶颈、单点故障和角色混淆等问题。

MediHive的方法是通过去中心化的架构，让基于大语言模型的智能体自主分配专业角色，进行初步分析，并通过基于证据的条件性辩论来检测分歧，最后在多轮迭代中局部融合同伴的见解以达成共识。该方法集成了共享记忆池和迭代融合机制，增强了系统的自主性和鲁棒性。

主要结论是，在MedQA和PubMedQA基准测试上的实验表明，MediHive在相同模型基础上，其准确率分别达到84.3%和78.4%， consistently优于单一智能体和集中式多智能体基线。消融研究证实了各架构组件的有效性。这项工作为医疗AI领域推进了可扩展、容错的去中心化多智能体系统，解决了集中式设计的关键限制，并为未来构建可靠、可扩展的医疗多智能体推理框架奠定了基础。
