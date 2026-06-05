---
title: "Critic-Guided Heterogeneous Multi-Agent Reasoning for Reliable Mathematical Problem Solving"
authors:
  - "Muhammad Talha Sharif"
  - "Abdul Rehman"
date: "2026-06-04"
arxiv_id: "2606.05704"
arxiv_url: "https://arxiv.org/abs/2606.05704"
pdf_url: "https://arxiv.org/pdf/2606.05704v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "多智能体协作"
  - "推理与规划"
  - "批评机制"
  - "数学推理"
  - "异构多智能体"
relevance_score: 8.5
---

# Critic-Guided Heterogeneous Multi-Agent Reasoning for Reliable Mathematical Problem Solving

## 原始摘要

Recent Large Language Models (LLMs) have shown impressive reasoning abilities; but they are still susceptible to hallucinations, intermediate reasoning mistakes, and unreliable reasoning results in complex mathematical reasoning problems. In this study, we introduce a critic-based heterogeneous multi-agent approach to improve the dependability of mathematical reasoning. This framework incorporates several LLM agents of different specialties and employs a critic-driven adaptive learning system to assess and guide the reasoning process based on intermediate feedback. The system adopts a generator-validator framework, with the validator not only determining correctness but also offering critiques to guide regeneration of solutions. This allows for adaptive error correction and prevents error cascading. Our experiments on the GSM8K benchmark show that the proposed method achieves up to 13% accuracy improvement over single-shot and non-critic models. Additionally, findings suggest that heterogeneity and critique reduce the need for large models, allowing smaller models to perform on par. Ablation studies reveal the main performance gains are due to the critic-based feedback loop and not model size. In summary, the proposed approach showcases the benefits of combining heterogeneous multi-agent collaboration and critique to obtain reliable and interpretable reasoning systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在复杂数学推理任务中存在的可靠性和准确性问题。尽管LLM通过思维链等技术展现出了推理能力，但单模型推理系统仍然面临几个关键不足：一是容易产生“幻觉”，即生成看似合理但实际错误的中间推理步骤；二是中间推理错误会沿着链条级联传播，导致最终结果不可靠；三是现有方法对推理过程的中间步骤缺乏有效的实时检验与修正机制。

针对这些不足，现有的多智能体系统（如基于辩论或顺序协作的系统）虽然通过多样性提高了性能，但它们大多是同构的，限制了推理类型，且通常依赖多数投票或辩论来聚合最终结果，缺乏对中间推理步骤的显式评估与动态修正能力，因此无法有效阻止错误级联。此外，这些系统在选择或协调智能体时，往往基于预设规则而非当前推理步骤的实际质量。

因此，本文要解决的核心问题是：如何设计一个多智能体数学推理系统，能够有效利用不同模型（异构智能体）的互补性，并引入一个明确的“批评者”机制，对中间推理步骤进行自适应评估与引导，从而在问题解决过程中动态诊断和修复推理错误，最终提升数学推理的可靠性与准确性。

### Q2: 有哪些相关研究？

相关研究可按类别组织如下：

**方法论类**：1）Chain-of-Agents (CoA) 采用顺序协作策略处理长上下文推理，通过经理代理合并结果，但缺乏对中间推理的批判性评估。2）RDoLT 在单模型框架中引入基于批判的再生机制和知识传播模块，虽能防止错误级联，但计算成本高且依赖精确评估器。3）COPPER 利用反射性协作和强化学习增强推理，通过共享反射模型提供反馈，但未强调代理异质性。

**异质性与专业化类**：1）A-HMAD 提出自适应异质多智能体辩论，通过角色专业化（求解器、检查器等）提升推理可靠性，但共识机制基于经验而非实时批判。2）AgentInit 通过多样性初始化优化团队构成，偏重于任务相关性与表示多样性，未深入整合批判反馈循环。

**应用与评测类**：1）ORCH 框架在离散选择推理中采用确定性编排与EMA路由，但缺乏自适应错误修正机制。2）MapCoder 和 Blueprint2Code 将多代理用于代码生成，通过分工（检索、规划、编码、调试）提升正确性，但未处理数学推理中的符号错误。3）AutoSafeCoder 结合静态分析与模糊测试提升代码安全性，目标领域与数学问题不同。

本文的主要区别在于：1）提出**生成器-验证器**双角色框架，其中验证器不仅能判断正确性，还能提供**批判性反馈**指导重新生成，实现自适应纠错。2）强调**异质性**与**批判循环**的协同作用，实验表明两者可让较小模型达到与大型模型相当的性能。3）通过消融实验明确性能增益主要来自批判反馈机制而非模型规模。

### Q3: 论文如何解决这个问题？

论文通过提出一个基于批评者指导的异构多智能体推理框架来解决数学推理中的幻觉、中间步骤错误和不可靠结果问题。核心方法采用生成器-验证器（Generator-Validator）双阶段架构：生成器使用固定模型（llama-3.1-8b-instant）生成包含3-4步推理步骤和最终答案的解决方案；验证器则根据不同实验配置扮演批评者角色，输出JSON格式的评价结果（包含推理步骤正确性、最终答案正确性以及可选的批评意见）。关键技术在于批评驱动的自适应学习系统：当首轮生成的解决方案未通过验证时，验证器会提供详细的批评反馈（指出推理或答案中的具体问题），然后将该反馈注入新一轮的生成过程，允许系统从中间推理错误中恢复并避免错误级联。实验在GSM8K基准上采用零样本推理（无微调），生成阶段温度设为0.2以保持适度多样性，验证阶段温度设为0以保持判断一致性，并支持最多两轮重生成。创新点包括：（1）引入异构多智能体协作——不同特长的LLM代理分工合作；（2）批评反馈循环实现自适应纠错；（3）研究表明异构性和批评机制可降低对模型规模的需求，使小型模型达到与大模型相当的性能。消融实验证实性能提升主要归功于批评者反馈循环而非模型参数规模。

### Q4: 论文做了哪些实验？

论文在GSM8K测试集上进行了系列消融实验，设置8种对比配置：固定生成器为llama-3.1-8B，验证器分为小模型（8B、20B）和大模型（70B、120B），并区分同构（相同模型族）与异构（不同模型族）设置。实验分两组：单次推理（无评判）和评判引导多轮推理。主要结果：无评判时准确率72.55%-80.14%（2A 8B同构最低，1A 70B同构最高80.14%）；引入评判后准确率提升至85.44%-93.56%（4B 20B异构最高93.56%），最大提升约13%。关键发现：无评判时大验证器在同构设置下优势明显（+7.59%），但在异构设置下增益有限（+1.21%）；加入评判后，小验证器性能反超大验证器（如4A 8B 88.63% vs 3A 70B 85.44%），且异构设置下小模型表现更优（4B 93.56% vs 3B 92.04%）。重试日志显示73%-78%问题首轮解决，评判机制额外恢复12%-16%案例。与SOTA对比，本方法在GSM8K上达93.56%，超过RDoLT框架（90.98%），验证了评判引导的多智能体协作优势。

### Q5: 有什么可以进一步探索的点？

该研究在GSM8K上验证了critic引导的异构多智能体推理的有效性，但存在几个可进一步探索的方向。首先，critic机制对生成器的修正主要依赖LLM的自我纠错能力，当初始错误逻辑被多次迭代固化时，修正效果可能有限。未来可引入外部验证工具（如符号计算器或形式化验证器）作为第三视角，避免纯文本推理的偏差。其次，当前异构性仅体现在模型参数规模上，实际上可引入知识专门化配置，例如让一个智能体擅长代数运算，另一个擅长几何空间推理，通过分工互补提升覆盖度。此外，论文未讨论多轮交互中的信息一致性丢失问题——当生成器采纳不同轮次中矛盾的修正建议时，可能产生逻辑混乱。可以设计基于置信度的选择性采纳机制，或使用共识投票筛选高质量critic反馈。最后，该方法目前局限于数学推理，可扩展到需要严谨推理的药物分子设计或法律条文解析等领域，并探索critic反馈的奖赏信号与强化学习微调的协同效应。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种基于批评指导的异构多智能体推理框架，用于提升大语言模型在复杂数学推理中的可靠性。核心问题在于单一大模型容易产生幻觉和中间推理错误。该方法采用“生成器-验证器”架构，其中验证器不仅判断答案正确性，还提供详细的批评反馈，指导生成器自适应修正错误，从而阻止错误级联。在GSM8K基准上的实验表明，该方法相比单次推理模型最高提升13%的准确率，最佳配置达到93.56%。主要结论是，性能提升主要源于批评反馈循环而非模型规模扩大；引入批评机制后，小模型也能达到与大模型相当的性能，且12%-16%的初始错误可在迭代中得以纠正。该工作展示了异构智能体协作与批评指导相结合的优势，为构建可靠且可解释的推理系统提供了可扩展的、仅需推理的无训练方案。
