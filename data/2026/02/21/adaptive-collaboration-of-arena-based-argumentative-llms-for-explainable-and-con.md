---
title: "Adaptive Collaboration of Arena-Based Argumentative LLMs for Explainable and Contestable Legal Reasoning"
authors:
  - "Hoang-Loc Cao"
  - "Phuc Ho"
  - "Truong Thanh Hung Nguyen"
  - "Phuc Truong Loc Nguyen"
  - "Dinh Thien Loc Nguyen"
  - "Hung Cao"
date: "2026-02-21"
arxiv_id: "2602.18916"
arxiv_url: "https://arxiv.org/abs/2602.18916"
pdf_url: "https://arxiv.org/pdf/2602.18916v1"
categories:
  - "cs.MA"
  - "cs.AI"
  - "cs.SC"
tags:
  - "多智能体系统"
  - "Agent 架构"
  - "神经符号系统"
  - "可解释性"
  - "法律推理"
  - "人机交互"
  - "辩论框架"
  - "不确定性处理"
relevance_score: 9.0
---

# Adaptive Collaboration of Arena-Based Argumentative LLMs for Explainable and Contestable Legal Reasoning

## 原始摘要

Legal reasoning requires not only high accuracy but also the ability to justify decisions through verifiable and contestable arguments. However, existing Large Language Model (LLM) approaches, such as Chain-of-Thought (CoT) and Retrieval-Augmented Generation (RAG), often produce unstructured explanations that lack a formal mechanism for verification or user intervention. To address this limitation, we propose Adaptive Collaboration of Argumentative LLMs (ACAL), a neuro-symbolic framework that integrates adaptive multi-agent collaboration with an Arena-based Quantitative Bipolar Argumentation Framework (A-QBAF). ACAL dynamically deploys expert agent teams to construct arguments, employs a clash resolution mechanism to adjudicate conflicting claims, and utilizes uncertainty-aware escalation for borderline cases. Crucially, our framework supports a Human-in-the-Loop (HITL) contestability workflow, enabling users to directly audit and modify the underlying reasoning graph to influence the final judgment. Empirical evaluations on the LegalBench benchmark demonstrate that ACAL outperforms strong baselines across Gemini-2.5-Flash-Lite and Gemini-2.5-Flash architectures, effectively balancing efficient predictive performance with structured transparency and contestability. Our implementation is available at: https://github.com/loc110504/ACAL.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有大语言模型（LLM）在法律推理任务中存在的关键缺陷：**缺乏结构化、可验证且允许用户干预（即可争议性）的解释机制**。当前方法如思维链（CoT）和检索增强生成（RAG）虽然能提升性能，但其生成的解释往往是自由、非结构化的，难以系统性地验证或让用户参与质疑。多智能体辩论（MAD）框架引入了多视角，但其辩论过程本身并未构成一个形式化的、可供争议的推理结构。这些不足在高风险的法律领域尤为突出，因为法律决策不仅要求高准确性，还必须能够通过可验证、可辩论的论证来证明其合理性，以满足日益增长的透明度和问责制监管要求（如欧盟《人工智能法案》）。

为此，论文提出了ACAL框架，这是一个神经符号混合的多智能体系统。它通过将论证性LLM与基于竞技场的定量双极论证框架（A-QBAF）相结合，动态部署专家智能体团队来构建支持或反对的论点，并采用冲突解决机制来裁决矛盾主张。其核心创新在于引入了**人在回路（HITL）的可争议性工作流**，允许用户直接审计并修改底层的推理图，从而影响最终判决。因此，该论文的根本目标是**在保持高效预测性能的同时，为法律推理提供一种兼具结构化透明度、形式化可验证性和用户可干预性的新范式**，以平衡性能与问责制。

### Q2: 有哪些相关研究？

相关研究主要分为两大方向：LLM在法律推理中的应用，以及法律AI系统的可解释性与可争议性。

在LLM法律推理方面，相关工作包括：
1.  **专用法律模型**：如ChatLaw和LegalMind，它们通过集成知识图谱和强化学习来提升事实准确性和流程优化。
2.  **检索增强生成（RAG）**：已成为标准技术，用于将LLM回答锚定在权威的外部法律资料（如法规、判例）中。
3.  **思维链（CoT）提示**：被广泛用于引导多步推理，并出现了法律专用的CoT变体或逻辑-语义集成模型。
4.  **多智能体架构**：通过让智能体扮演法官、原告、被告等角色来模拟对抗性法律辩论，以迭代式批评来完善论点。

本文与这些工作的关系是：ACAL框架**吸收并整合了多智能体协作的思想**，但指出现有方法（包括上述）产生的解释缺乏形式化结构，难以系统验证或挑战，存在“问责鸿沟”。

在可解释性与可争议性方面，相关工作包括：
1.  **可解释性技术**：如RAG的引用机制、CoT推理链，以及使用Toulmin模型等形式化论证图来创建可验证的推理轨迹。
2.  **可争议AI（CAI）与神经符号方法**：如ALEX框架使用形式化方案（Toulmin模型、ASPIC+）构建对立论点结构供用户审查；SOLAR等神经符号方法利用结构化本体表示来连接自然语言与符号推理。

本文与这些工作的关系是：ACAL框架**直接致力于实现可争议性**，但指出现有CAI方法主要生成静态推理结构供事后检查，**缺乏动态量化权衡对立论点强度的机制**，也不支持人类修改论证权重并数学化传播以更新最终判决的完全交互式工作流。因此，本文通过将多智能体协作与形式化的定量论证框架（A-QBAF）及人在回路工作流相结合，旨在弥合这一差距。

### Q3: 论文如何解决这个问题？

ACAL 框架通过一个神经符号化的多智能体协作架构，系统性地解决了法律推理中需要可验证、可争辩的论证问题。其核心方法包含四个关键模块：

**1. 自适应专家团队选择**：框架维护一个包含10种不同法律角色（如法官、律师、检察官等）的智能体池。针对每个具体案件，系统会动态选择两个专家子集：一个用于构建支持性论据，另一个用于构建攻击性论据。这种按需组队的方式避免了使用所有智能体带来的计算开销和噪声，确保了论证的专业性。

**2. 基于竞技场的论证生成与计算**：这是框架的核心。首先，通过混合检索增强生成技术，从法律数据库和网络案例中获取证据上下文，为论证提供权威依据。每个被选中的智能体生成2-5个论证，并由LLM根据精细化的评分准则（0.1-1.0分）赋予内在强度分数。关键创新在于使用LLM进行语义关系识别，判定论证对之间是“攻击”、“支持”还是“中立”关系，从而构建出更符合逻辑的论证图，而非简单的立场对立。对于强度相近的对立论证，引入了“冲突解决”机制：让LLM作为法律专家进行“竞技场”式辩论，根据胜负调整论证分数，以裁决冲突。

**3. 定量双极论证框架**：将上述过程形式化为一个A-QBAF图。图中节点包括中心主张和所有论证，边代表攻击或支持关系。采用二次能量语义学计算论证的最终传播强度：一个论证的强度由其支持者的强度之和减去攻击者的强度之和所形成的“能量”来决定，并通过一个二次函数映射回强度值。这使得所有论证的相互作用能收敛到一个均衡状态，从而得出中心主张的最终可信度分数。

**4. 人在回路的可争辩性工作流**：为实现真正的可争辩性，框架提供了交互式界面。用户可以直接审计并编辑整个论证图：可以接受/拒绝论证、修改论证内容、调整论证强度或关系、添加新论证等。所有修改都会实时更新A-QBAF图并重新计算主张分数，使人类干预能实质性地影响最终判决，而非事后注解。此外，对于高不确定性（主张分数接近0.5）的边界案件，系统会触发“不确定性感知升级”机制，交由更强大的模型或人类复审员做最终决定，从而平衡效率与可靠性。

综上，ACAL通过动态多智能体协作生成结构化论证，利用形式化的论证图进行定量推理，并首创了可编辑、可追溯的人机交互争辩流程，最终在提升预测性能的同时，实现了法律决策所需的透明度和可争辩性。

### Q4: 论文做了哪些实验？

论文在LegalBench基准上进行了实验，重点关注两个法律推理分类任务：Hearsay（判断陈述是否为传闻证据）和Learned Hands Courts（判断叙述是否属于法院类别）。实验使用了Gemini-2.5-Flash-Lite和Gemini-2.5-Flash两种模型，并设置了多个基线方法进行比较，包括标准提示（SP）、思维链（CoT）、检索增强生成（RAG）以及多智能体辩论（MAD）。评估指标包括准确率、精确率、召回率和宏F1分数。

主要结果显示，ACAL框架在多数情况下超越了基线方法。在Gemini-2.5-Flash-Lite模型上，ACAL在Learned Hands Courts任务上取得了最高准确率（70.8%）和F1分数（70.7%），在Hearsay任务上则与MAD并列最高准确率（74.5%），但获得了更高的精确率（77.1%）、召回率（76.3%）和F1分数（74.4%）。在更强的Gemini-2.5-Flash模型上，ACAL在Learned Hands Courts任务上与MAD持平（准确率75.5%），但F1分数略优（75.3%）；在Hearsay任务上取得了最高召回率（77.6%）和F1分数（76.7%）。

此外，论文还进行了消融实验，验证了冲突解决机制（CR）和不确定性感知升级机制（UAE）的有效性。实验表明，CR是性能提升的主要驱动力（单独使用使准确率提升7.9%），而UAE需与CR结合才能发挥正面作用。同时，超参数β（基础调整幅度）的敏感性测试显示，β=0.15时性能最佳，过高或过低都会导致效果下降。这些实验共同证明了ACAL在保持预测性能的同时，提供了结构化的可解释性与可争议性。

### Q5: 有什么可以进一步探索的点？

本文提出的ACAL框架在可解释性和可争议性法律推理方面取得了进展，但仍有多个方向值得深入探索。局限性方面，当前框架依赖于特定LLM（Gemini系列），其泛化能力到其他模型（如开源模型）尚未验证；多智能体协作和形式化论证构建的计算开销较大，可能影响实时应用；此外，Human-in-the-Loop工作流的实际用户体验和干预有效性需更多实证研究。

未来方向包括：1）优化计算效率，探索轻量级智能体协作或知识蒸馏技术，以降低推理成本；2）扩展框架通用性，将其应用于更广泛的高风险领域（如医疗诊断、金融审计），并测试跨领域迁移能力；3）增强交互性，开发更直观的可视化工具，帮助非专家用户理解和修改推理图；4）深化法律适应性，针对不同司法管辖区（如大陆法系与普通法系）定制论证规则，提升跨文化鲁棒性。

### Q6: 总结一下论文的主要内容

这篇论文提出了ACAL框架，旨在解决法律推理中LLM解释缺乏结构化、可验证和可争议性的问题。其核心贡献在于将神经与符号方法结合，通过自适应多智能体协作与基于竞技场的定量双极论证框架，动态组建专家团队构建论点，并利用冲突解决机制裁决争议。该框架的关键创新是引入了人在回路的争议工作流，允许用户直接审计和修改底层推理图以影响最终判决，从而实现了决策的透明与可干预。实验表明，ACAL在LegalBench基准上超越了现有基线，在保持高效预测性能的同时，显著提升了法律推理的可解释性与可争议性。
