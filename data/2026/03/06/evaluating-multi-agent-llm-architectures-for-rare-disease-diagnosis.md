---
title: "Evaluating Multi-Agent LLM Architectures for Rare Disease Diagnosis"
authors:
  - "Ahmed Almasoud"
date: "2026-03-06"
arxiv_id: "2603.06856"
arxiv_url: "https://arxiv.org/abs/2603.06856"
pdf_url: "https://arxiv.org/pdf/2603.06856v1"
categories:
  - "cs.MA"
tags:
  - "Multi-Agent Systems"
  - "Medical Diagnosis"
  - "Rare Diseases"
  - "Agent Architecture"
  - "Evaluation Metrics"
relevance_score: 8.5
---

# Evaluating Multi-Agent LLM Architectures for Rare Disease Diagnosis

## 原始摘要

While large language models are capable diagnostic tools, the impact of multi-agent topology on diagnostic accuracy remains underexplored. This study evaluates four agent topologies, Control (single agent), Hierarchical, Adversarial, and Collaborative, across 302 cases spanning 33 rare disease categories. We introduce a Reasoning Gap metric to quantify the difference between internal knowledge retrieval and final diagnostic accuracy. Results indicate that the Hierarchical topology (50.0% accuracy) marginally outperforms Collaborative (49.8%) and Control (48.5%) configurations. In contrast, the Adversarial model significantly degrades performance (27.3%), exhibiting a massive Reasoning Gap where valid diagnoses were rejected due to artificial doubt. Across all architectures, performance was strongest in Allergic diseases and Toxic Effects categories but poorest in Cardiac Malformation and Respiratory cases. Critically, while the single-agent baseline was generally robust, all multi-agent systems, including the Adversarial model, yielded superior accuracy in Bone and Thoracic disease categories. These findings demonstrate that increasing system complexity does not guarantee better reasoning, supporting a shift toward dynamic topology selection.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体系统（MAS）中不同智能体拓扑结构对临床诊断准确性，尤其是在罕见病诊断这一高难度场景下影响尚不明确的问题。尽管大语言模型（LLM）在医疗诊断中展现出潜力，但针对罕见病等复杂、长尾医疗场景，单智能体模型的准确率仍然有限。研究者们开始探索使用多智能体系统来模拟临床中的多学科团队（MDT）或层级监督结构，以期提升诊断的可靠性。然而，现有的研究（如强调协作或层级监督的工作）与强调通过辩论来提升事实性的通用AI研究之间存在矛盾，且缺乏对不同拓扑结构进行系统性比较的实证研究。因此，本文的核心问题是：不同的多智能体组织架构（如层级式、协作式、对抗式）如何具体影响LLM在罕见病诊断中的推理准确性和最终决策质量？为了解决这个问题，作者在标准化的罕见病数据集上对四种拓扑结构进行了基准测试，并引入了一个名为“推理差距”（Reasoning Gap）的新指标来量化智能体系统内部知识检索与最终决策之间的效率损失。

### Q2: 有哪些相关研究？

本文的相关研究主要涵盖三个方向：1) 医疗诊断中单智能体与多智能体系统的应用：前期研究指出通用LLM在罕见病诊断上表现不佳（如Exomiser的对比），而多智能体系统（如MedChat、AI Hospital）通过角色分配能增强模拟保真度。具体在医疗领域，层级式架构（如KG4Diagnosis、TAO）和角色扮演工作流（如MedAgent-Pro、SpAgents）被证明能通过结构化流程减少幻觉。2) 协作与辩论机制：在通用领域，多智能体辩论被认为能提升事实性（Du et al.），但在医疗领域的应用存在争议。Chen et al. 证明了多智能体对话（MAC）在罕见病诊断上优于链式思维。3) 评估与聚合方法：如何聚合多智能体输出是一个挑战，研究提出了如“反向意外流行度”等算法。本文与这些工作的关系在于，它直接继承了医疗多智能体系统的架构思想（层次化、角色化），并将通用AI领域推崇的对抗辩论机制引入进行对比实验。其核心创新在于在一个统一的罕见病诊断框架下，对控制（单智能体）、层次化、对抗式、协作式四种拓扑进行了直接、系统的比较评估，并引入了“推理差距”这一新指标来深入分析决策失败的原因。

### Q3: 论文如何解决这个问题？

论文通过设计一个包含四种不同智能体拓扑结构的实验框架来系统评估其对诊断的影响。核心方法包括架构设计、评估框架和数据分析。**架构设计**：1) **Control**：单智能体基线，使用零样本提示直接输出诊断。2) **Hierarchical**：模拟医院层级工作流，设计为三阶段漏斗：住院医师（生成3个诊断）-> 主治医师（排除1个，保留2个）-> 主治医师（最终决定）。3) **Adversarial**：引入对抗辩论，由提出者（Proposer）给出诊断，批评者（Critic）强制寻找反驳证据，最终由法官（Judge）根据辩论记录裁决，旨在通过压力测试来验证诊断。4) **Collaborative**：模拟MDT，由病理科、内科、放射科三个专科智能体独立分析病例，然后由主席（Chairman）整合三方意见做出最终共识诊断。**评估框架**：1) **诊断准确性评分**：采用“LLM即法官”方法，使用GPT-5.1作为评判者，根据预设的评分标准（精确匹配10分，相关鉴别诊断5分，完全错误0分）对最终诊断与真值进行比较，计算归一化平均分。2) **推理差距**：创新性地提出该指标。首先计算“推理召回率”，即在所有智能体的交互日志中（如住院医师的初始列表、辩论内容），通过关键词匹配判断正确诊断是否曾被考虑过（是=10，否=0，然后归一化为百分比）。推理差距Δ = 推理召回率 - 诊断准确性。正值越大，表明系统虽然“知道”正确答案，但在最终决策环节将其“拒绝”的失败率越高，这有助于区分是知识检索失败还是判断失败。3) **领域分析**：根据33种罕见病类别进行分层分析，以探究不同拓扑在不同疾病类型上的表现差异。

### Q4: 论文做了哪些实验？

论文在由Chen等人整理的包含302个罕见病病例（覆盖33个类别）的公开数据集上进行了实验。所有实验均使用GPT-5.1模型通过OpenAI API完成。**实验设置与结果**：1) **整体性能比较**：四种拓扑的诊断准确性分别为：层次式50.0%、协作式49.8%、控制式（单智能体）48.5%、对抗式27.3%。层次式架构表现最佳，但相比单智能体基线提升微小（+1.5%）。对抗式架构性能严重退化。2) **推理差距分析**：对抗式架构表现出巨大的推理差距（Δ=16.7），表明其内部在辩论过程中经常考虑过正确诊断，但最终决策时却将其错误地拒绝了。协作式（Δ=1.5）和层次式（Δ=4.0）的差距较小，表明其决策效率更高。3) **领域特定分析**：通过33个疾病类别的细分，发现：a) 所有架构在过敏性疾病、中毒效应等类别表现好，而在心脏畸形、呼吸道疾病等类别表现差，说明病例内在难度不同。b) 关键发现：虽然单智能体基线总体稳健，但在骨科和胸部外科疾病类别，所有多智能体系统（包括对抗式）都表现出比单智能体更高的准确性。c) 对抗式架构的性能退化在“容易”的病例（如过敏性疾病、儿童风湿病）中最为严重，支持了“推理差距”假说：强制性的批评人为引入了不必要的怀疑，导致系统“过度思考”并拒绝了清晰的正确方案。d) 协作式架构在涉及多器官系统的复杂病理（如呼吸道、泌尿生殖系统疾病）中表现出特定优势，表明多视角融合在此类场景中有价值。

### Q5: 有什么可以进一步探索的点？

论文的局限性指明了几个关键的探索方向。首先，实验仅依赖单一模型（GPT-5.1），结论可能存在模型依赖性。未来研究应在不同的LLM家族（如开源模型、其他商业模型）上重复此实验，以验证拓扑效果的普适性。其次，实验是静态、单轮的推理任务，而真实临床诊断是动态、多轮的交互过程（包含问诊、检查、反馈）。未来可将拓扑评估扩展到基于强化学习的多轮对话框架（如DoctorAgent-RL）或动态交互模拟环境（如MedAgentSim）中。第三，论文发现没有单一架构在所有领域都最优，这直接指向了“动态拓扑选择”这一最有前景的方向。可以研究开发一个元控制器或监督智能体，根据输入病例的特征（如症状模糊度、涉及的器官系统）动态地为每个病例路由到最合适的架构（例如，简单病例用单智能体，多器官病例用协作式）。最后，需要更深入地研究成本效益。虽然层次式和协作式架构有微小精度提升，但推理时间和Token消耗显著增加。未来的工作需要量化这种权衡，特别是在大规模部署场景下，探索如何在保证性能的同时优化计算效率。

### Q6: 总结一下论文的主要内容

本文系统评估了四种基于LLM的多智能体架构——控制（单智能体）、层次化、对抗式、协作式——在302例罕见病诊断中的表现。研究发现，层次化架构（50.0%准确率）表现最佳，但相比单智能体基线（48.5%）仅提升有限；协作式架构（49.8%）表现相当。然而，对抗式架构（27.3%）导致性能严重崩溃。为解释此现象，论文创新性地提出了“推理差距”指标，用于量化智能体内部“知道正确答案”与“最终选择正确答案”之间的差距。分析表明，对抗式架构存在巨大的推理差距（16.7），源于强制辩论机制人为引入的怀疑导致系统错误地拒绝了正确的诊断。领域分析进一步显示，没有一种架构在所有疾病类别中都占优：层次化架构在整体上稳定，协作式在多器官系统疾病中有优势，而所有架构在心脏畸形等类别上均表现不佳。论文的核心贡献在于，通过实证研究揭示了增加智能体系统复杂度并不必然提升推理能力，对抗性交互甚至可能产生破坏性干扰。研究结果支持从静态架构向动态拓扑选择转变的趋势，即根据具体任务特点选择最合适的多智能体组织方式。
