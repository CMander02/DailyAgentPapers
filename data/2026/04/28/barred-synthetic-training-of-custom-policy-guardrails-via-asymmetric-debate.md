---
title: "BARRED: Synthetic Training of Custom Policy Guardrails via Asymmetric Debate"
authors:
  - "Arnon Mazza"
  - "Elad Levi"
date: "2026-04-28"
arxiv_id: "2604.25203"
arxiv_url: "https://arxiv.org/abs/2604.25203"
pdf_url: "https://arxiv.org/pdf/2604.25203v1"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.LG"
tags:
  - "LLM Agent安全"
  - "多智能体辩论"
  - "合成数据训练"
  - "策略护栏"
  - "小模型微调"
relevance_score: 8.0
---

# BARRED: Synthetic Training of Custom Policy Guardrails via Asymmetric Debate

## 原始摘要

Deploying guardrails for custom policies remains challenging, as generic safety models fail to capture task-specific requirements, while prompting LLMs suffers from inconsistent boundary-case performance and high inference costs. Training custom classifiers achieves both accuracy and efficiency, yet demands substantial labeled data that is costly to obtain. We present BARRED (Boundary Alignment Refinement through REflection and Debate), a framework for generating faithful and diverse synthetic training data using only a task description and a small set of unlabeled examples. Our approach decomposes the domain space into dimensions to ensure comprehensive coverage, and employs multi-agent debate to verify label correctness, yielding a high-fidelity training corpus. Experiments across diverse custom policies demonstrate that small language models finetuned on our synthetic data consistently outperform state-of-the-art proprietary LLMs (including reasoning models) and dedicated guardrail models. Ablation studies confirm that both dimension decomposition and debate-based verification are critical for ensuring the diversity and label fidelity required for effective fine-tuning. The BARRED framework eliminates the reliance on extensive human annotation, offering a scalable solution for accurate custom guardrails.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决在部署自定义政策护栏时面临的核心矛盾：现有的通用安全模型无法捕捉特定任务的需求，而基于提示的大语言模型（LLM）虽然灵活，但在边界案例上表现不一致，且推理成本高昂。训练自定义分类器虽然能同时实现高精度和高效率，但需要大量昂贵的人工标注数据。因此，本文提出了BARRED框架，其核心问题是如何仅利用任务描述和少量无标注样本，自动生成高质量、多样化的合成训练数据，从而训练出准确且高效的自定义护栏模型。现有合成数据方法常面临模型坍塌导致多样性不足，以及LLM生成标签噪声大导致保真度差的问题。BARRED通过维度分解确保数据覆盖任务空间的各个挑战区域，并引入多智能体辩论机制通过结构化讨论来解决模糊案例，从而获得高保真训练语料。最终，该框架消除了对大量人工标注的依赖，为快速、准确地定制护栏提供了可扩展的解决方案。

### Q2: 有哪些相关研究？

相关研究主要分为三类：

1. **护栏模型**：静态模型如LlamaGuard、WildGuard、ShieldGemma和Aegis，在预定义安全分类上表现优异，但无法泛化到新策略。动态模型如DynaGuard和CoSAlign支持推理时策略适应，但牺牲了精度。推理增强方法如GuardReasoner和R2-Guard采用思维链提升检测效果，但计算成本高。本文通过为自定义策略训练专用分类器，在保持精度的同时避免了动态模型的高成本。

2. **合成数据生成**：Constitutional AI、Self-Instruct等方法展示了基于LLM的合成数据能力。针对多样性问题，Persona Hub、IntellAgent和Verbalized Sampling被提出。本文采用维度分解和分布采样，聚焦边界案例生成，确保数据覆盖目标策略的模糊区域，这是对现有方法的关键补充。

3. **多智能体辩论**：该方法通过多个LLM实例相互辩论提升推理和事实性。本文创新地将辩论用于合成数据验证，通过智能体交叉检查标签正确性并提供迭代反馈，生成高保真数据集，无需人工标注。

总体上，本文填补了为自定义策略生成高质量训练数据的研究空白，不同于静态或动态护栏模型的固有局限。

### Q3: 论文如何解决这个问题？

BARRED通过一个四阶段框架解决自定义护栏合成训练数据生成问题：领域分解、边界采样、辩论验证和迭代修正。首先，给定任务描述和少量未标注种子样本，框架利用LLM从种子样本中提取多个任务相关维度（如隐私场景中的联系方式、地理位置等），并通过语义去重形成覆盖完整域空间的维度集合D。对每个维度di，采用口头化采样（Verbalized Sampling）让LLM生成分布式的可能实例化集合Vi，而非单一输出，从而避免模式坍塌。接着，系统从维度、实例化和标签空间中均匀采样，专门生成边界挑战性样本（接近决策边界的困难案例），确保标签平衡并附带推理过程。核心创新在于非对称辩论验证机制：一个坚定的倡导者代理（Advocate）始终基于生成推理r捍卫标签y，而多个评判者代理（Judges）独立评估样本和倡导者的论点。经过T轮辩论后，仅当所有评判者达成共识时样本才被接受。对于未通过的样本，系统聚合评判者的结构化反馈，引导生成器在保持相同维度和标签的前提下进行迭代修正，最多Rmax次。这种方法通过多维覆盖保证多样性，通过辩论对抗机制替代人工标注确保标签保真度，最终生成的高质量合成数据微调的小模型在重复检测、隐私保护等任务上全面超越GPT-4.1等大模型和专用护栏模型。消融实验证实维度分解和辩论验证对数据多样性和标签准确性至关重要。

### Q4: 论文做了哪些实验？

论文在四个守卫任务上评估了BARRED框架：客服对话策略执行（DynaGuard基准，聚焦“重复处理”和“隐私保护”两个规则，测试集分别有158和112个样本）、AI助手结构化任务输出验证（基于GAIA基准，82个合规样本及等量人工生成的不合规样本）、以及医疗领域健康建议检测（Health Advice基准，200个测试样本）。对比方法包括两类强基线：LLM-as-a-Judge（GPT-4.1系列、GPT-5-mini推理模型、Qwen2.5-14B）和通用守卫模型（OSS-Safeguard-20B、Glider-3.8B）。主要结果：在Qwen2.5-14B上微调的BARRED模型在所有任务上超越所有基线，例如在人类标注测试集上准确率达0.85，远超GPT-5-mini等模型；通用守卫模型甚至不及3B参数量的BARRED模型。消融实验显示，维度分解显著提升训练数据覆盖率和模型准确率（随维度数量增加呈对数增长），多智能体辩论验证机制相比无验证（准确率从0.85降至0.58）和自优化（0.53）绝对提升27-32%，且超过30%的辩论路径呈现非平凡模式（如分歧、说服、共识打破）。

### Q5: 有什么可以进一步探索的点？

BARRED在多类别分类和层级结构处理上仍显不足，当前框架主要针对二分类边界，未来可扩展至多标签和层级分类场景。尽管维度分解保证了样本多样性，但依赖LLM生成数据的费用在高频迭代下仍是一个瓶颈，探索更经济的采样策略或知识蒸馏方法或许可以降低开销。跨任务迁移是另一个有价值的方向，若能通过元学习或共享表示，将某领域生成的合成数据用于相关任务，可进一步减少重复标注成本。引入少量人类反馈进行迭代优化，也能在关键难例上修正偏差，提升标签保真度。此外，当前多智能体辩论成本随维度增加而线性增长，设计更高效的证据聚合机制或异步验证流程是值得探索的改进点。最后，将BARRED应用于更复杂的开放式对话策略和政策合规审查，验证其在不同模态（如多轮对话、结构化输出）下的鲁棒性，也有助于推动从理论到量产部署的落地。

### Q6: 总结一下论文的主要内容

BARRED提出了一种为自定义策略护栏生成高质量合成训练数据的框架。该问题旨在解决通用安全模型无法捕捉特定任务需求、大语言模型推理成本高且边界案例表现不一致、以及手工标注成本高昂等挑战。方法上，BARRED首先通过维度分解覆盖领域空间，再利用多智能体辩论机制验证标签正确性，从而生成高保真的训练语料。实验表明，基于该合成数据微调的小模型（3B参数）在对话策略执行、智能体输出验证和法规合规等任务上，持续超越前沿大语言模型和专用护栏模型。消融实验证实维度分解和辩论验证对数据多样性和标签保真度至关重要。该工作的核心贡献在于提出无需大量人工标注的可扩展解决方案，为自定义策略部署准确高效的护栏提供了实用路径，其意义扩展到任何标签稀缺但任务规格明确的分类场景。
