---
title: "MARCH: Multi-Agent Reinforced Self-Check for LLM Hallucination"
authors:
  - "Zhuo Li"
  - "Yupeng Zhang"
  - "Pengyu Cheng"
  - "Jiajun Song"
  - "Mengyu Zhou"
  - "Hao Li"
  - "Shujie Hu"
  - "Yu Qin"
  - "Erchao Zhao"
  - "Xiaoxi Jiang"
  - "Guanjun Jiang"
date: "2026-03-25"
arxiv_id: "2603.24579"
arxiv_url: "https://arxiv.org/abs/2603.24579"
pdf_url: "https://arxiv.org/pdf/2603.24579v1"
github_url: "https://github.com/Qwen-Applications/MARCH"
categories:
  - "cs.CL"
tags:
  - "Hallucination Detection"
  - "Multi-Agent System"
  - "Reinforcement Learning"
  - "Retrieval-Augmented Generation"
  - "Self-Check"
  - "Factual Verification"
relevance_score: 8.0
---

# MARCH: Multi-Agent Reinforced Self-Check for LLM Hallucination

## 原始摘要

Hallucination remains a critical bottleneck for large language models (LLMs), undermining their reliability in real-world applications, especially in Retrieval-Augmented Generation (RAG) systems. While existing hallucination detection methods employ LLM-as-a-judge to verify LLM outputs against retrieved evidence, they suffer from inherent confirmation bias, where the verifier inadvertently reproduces the errors of the original generation. To address this, we introduce Multi-Agent Reinforced Self-Check for Hallucination (MARCH), a framework that enforces rigorous factual alignment by leveraging deliberate information asymmetry. MARCH orchestrates a collaborative pipeline of three specialized agents: a Solver, a Proposer, and a Checker. The Solver generates an initial RAG response, which the Proposer decomposes into claim-level verifiable atomic propositions. Crucially, the Checker validates these propositions against retrieved evidence in isolation, deprived of the Solver's original output. This well-crafted information asymmetry scheme breaks the cycle of self-confirmation bias. By training this pipeline with multi-agent reinforcement learning (MARL), we enable the agents to co-evolve and optimize factual adherence. Extensive experiments across hallucination benchmarks demonstrate that MARCH substantially reduces hallucination rates. Notably, an 8B-parameter LLM equipped with MARCH achieves performance competitive with powerful closed-source models. MARCH paves a scalable path for factual self-improvement of LLMs through co-evolution. The code is at https://github.com/Qwen-Applications/MARCH.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）在检索增强生成（RAG）系统中产生的“幻觉”（即生成与提供证据相矛盾的内容）问题，这是阻碍LLM在金融、法律等高风险领域可靠应用的关键瓶颈。

研究背景是，尽管已有方法（如基于LLM的验证器）尝试检测幻觉，但它们存在固有的**确认偏差**问题：验证器在同时看到原始生成结果和检索证据时，会不自觉地倾向于确认生成内容的合理性，而非严格依据证据进行客观核实，导致错误被重复。现有监督微调（SFT）可能强化风格模仿而非事实准确性，而基于人类反馈的强化学习（RLHF）则因使用粗粒度的标量奖励，无法对生成内容中细粒度的具体主张提供精确的监督信号。此外，依赖外部验证器的方法受限于专业领域标注数据的稀缺和验证器本身的能力天花板。

因此，本文的核心问题是：如何设计一种机制，打破验证过程中的自我确认偏差循环，为LLM提供细粒度、基于证据的优化信号，从而实现更严格的事实对齐。为此，论文提出了MARCH框架，其核心解决方案是通过精心设计的**信息不对称**，构建一个由求解器、提议者和检查器三个智能体协作的管道，并利用多智能体强化学习进行协同优化，迫使模型在生成和验证环节都严格锚定于检索证据，从而系统性减少幻觉。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为幻觉检测与缓解方法、强化学习优化、以及多智能体协作三类。

在幻觉检测与缓解方面，现有工作常采用“LLM-as-a-judge”范式，让验证器基于检索证据核查生成内容。然而，这类方法存在确认偏差，验证器易无意中复现原始生成的错误。本文提出的MARCH框架通过引入信息不对称设计（如Checker隔离原始输出）打破了这一自我确认循环，与现有检测方法形成核心区别。

在强化学习优化方面，传统RLHF依赖粗粒度标量奖励，难以监督细粒度事实一致性；RLVR尝试通过规则或外部奖励模型提供客观反馈，但仍受限于标注数据稀缺和外部验证器的推理瓶颈。MARCH则通过多智能体强化学习（MARL）实现协同优化，利用零容忍奖励机制（即Proposer提取的声明与Checker验证结果间的任何差异都会触发惩罚）驱动智能体严格对齐证据，提供了更细粒度、可操作的优化信号。

在多智能体协作方面，先前研究多关注智能体分工以提升任务完成效率，而MARCH创新性地将多智能体流程用于事实自检，通过Solver、Proposer、Checker三个专用智能体的协作管道，实现了生成、解构与验证的分离，从而系统性提升事实对齐能力，这与单纯的任务导向多智能体系统有所不同。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MARCH的多智能体强化自检框架来解决大语言模型在RAG系统中的幻觉问题。其核心方法是利用精心设计的信息不对称性，打破传统LLM-as-a-judge方法中存在的自我确认偏差循环。

整体框架由三个基于同一基础策略模型πθ实例化的专用智能体组成，形成一个结构化的非对称协作流程：
1.  **Solver（求解器）**：根据输入查询x和检索到的文档D，生成初始的RAG响应y。
2.  **Proposer（提议器）**：作为“响应原子化器”，将Solver生成的连续文本响应y分解为一组离散的、可验证的问答对{(q_i, a_i)}，其中每个问题q_i针对一个具体事实主张a_i。
3.  **Checker（检查器）**：作为“盲审员”，是整个框架实现信息不对称的关键。它仅基于检索文档D和Proposer生成的问题集{q_i}，独立生成答案{â_i}，而**完全无法访问**Solver的原始输出y及其主张a_i。这种设计切断了检查器对生成内容的依赖，迫使验证完全基于证据。

关键技术包括：
*   **信息不对称方案**：通过剥夺Checker对原始输出的访问权限，强制其仅依据原始证据进行独立验证，从而打破了自我确认偏差的循环。
*   **零容忍奖励函数**：定义了一个严格的二元奖励机制。只有当Solver提出的**每一个**主张a_i都与Checker独立验证的答案â_i完全匹配时，整个轨迹才获得成功奖励，否则视为失败。这种“全有或全无”的结构迫使模型优先考虑严格的事实一致性，而非部分正确或风格上的合理性。
*   **多智能体强化学习优化**：使用近端策略优化算法对共享策略πθ进行训练。关键创新在于，每个训练样本会贡献两条轨迹（Solver的生成路径y和Checker的审计路径λ）到优化循环中，两者共享基于事实一致性计算的最终奖励。这使得策略模型能够同时进化，既成为可靠的生成器，也成为严谨的审计员，内化一个自包含的验证循环。
*   **多数投票共识**：为减少Checker生成过程中的随机误差，对每个问题会进行多次独立审计采样，并通过多数投票确定最终的共识答案â_i，从而稳定奖励信号。

总之，MARCH通过非对称的多智能体协作管道，将事实性验证转化为一个结构化的自洽游戏，并利用强化学习使智能体协同进化，最终让模型学会生成严格基于证据的内容，显著降低了幻觉率。

### Q4: 论文做了哪些实验？

论文在幻觉缓解和事实性评估方面进行了全面的实验。实验设置基于多智能体强化学习框架，使用Meta-Llama3.1-8B-Instruct作为基础模型进行初始化，并在两个训练数据集上进行训练：基于BioASQ的STEM（科学-技术-工程-数学）领域和基于2WikiMultiHopQA与MuSiQue的通用领域。训练仅使用查询和检索到的文档，不依赖真实答案或标注，且检索文档中包含高比例的噪声（如MuSiQue中88.35%的文档不相关），以模拟真实挑战。训练采用PPO算法，使用vLLM进行高效采样。

评估在四个基准测试上进行：RAGTruth、FaithBench、ContextualJudgeBench和Facts Grounding，涵盖问答、数据到文本生成、摘要以及医疗、金融、法律等多个领域。评估使用Qwen3-235B-A22B作为评判模型，通过八次独立生成并多数投票来确保稳定性。

主要结果如下：在RAGTruth和FaithBench上，MARCH显著提升了基础模型的事实一致性。MARCH-STEM将平均准确率从55.20提升至74.93（+19.73），MARCH-General进一步提升至75.23（+20.03）。在Facts Grounding基准上，MARCH-STEM和MARCH-General分别达到85.23%和80.12%的事实性得分，远超基础模型的57.09%。在ContextualJudgeBench上，MARCH-General在多个维度（如忠实性、完整性、简洁性）取得显著提升，平均准确率达到51.6%，相比基础模型的29.7%提升了21.9个百分点。这些结果表明，MARCH能够使一个8B参数的小模型在事实性判断任务上达到与大型闭源模型竞争的性能。

### Q5: 有什么可以进一步探索的点？

本文提出的MARCH框架通过多智能体协作与信息不对称设计，有效缓解了LLM幻觉问题，但仍存在若干可进一步探索的方向。首先，框架依赖三个独立智能体的协同，这增加了计算开销和推理延迟，未来可研究如何通过轻量化架构或智能体功能合并来提升效率。其次，当前方法主要针对检索增强生成（RAG）场景，对于无需外部检索的开放域生成幻觉的检测能力尚不明确，可探索将其扩展至更广泛的生成任务。此外，训练过程中使用的多智能体强化学习（MARL）对奖励函数设计敏感，若奖励设定不够精准，可能导致智能体学习到次优策略，未来可结合人类反馈或更细粒度的奖励机制来优化训练稳定性。最后，信息不对称虽能减少确认偏差，但也可能因检查器缺乏上下文而误判合理推断，未来可引入动态证据检索或概率校准机制，在保持严谨的同时提升判断的灵活性。这些方向有望进一步提升框架的实用性、泛化性与可靠性。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型在检索增强生成中存在的幻觉问题，提出了一种名为MARCH的多智能体强化自检框架。其核心贡献在于通过精心设计的信息不对称机制，打破了现有基于LLM-as-a-judge的验证方法中固有的自我确认偏差。方法上，MARCH构建了一个由求解器、提议者和检查器三个智能体协作的流程：求解器生成初始回答，提议者将其分解为可验证的原子命题，而检查器则在隔离原始回答、仅依据检索证据的情况下独立验证这些命题。通过多智能体强化学习训练，这些智能体能够协同进化，优化事实一致性。实验结果表明，MARCH能显著降低幻觉率，即使是一个80亿参数的模型在配备该框架后，其性能也能与强大的闭源模型相竞争。这项工作为LLM通过协同进化实现事实性自我改进提供了一条可扩展的路径。
