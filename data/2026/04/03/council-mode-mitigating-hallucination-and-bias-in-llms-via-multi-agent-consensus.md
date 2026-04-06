---
title: "Council Mode: Mitigating Hallucination and Bias in LLMs via Multi-Agent Consensus"
authors:
  - "Shuai Wu"
  - "Xue Li"
  - "Yanna Feng"
  - "Yufang Li"
  - "Zhijun Wang"
date: "2026-04-03"
arxiv_id: "2604.02923"
arxiv_url: "https://arxiv.org/abs/2604.02923"
pdf_url: "https://arxiv.org/pdf/2604.02923v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Multi-Agent"
  - "Hallucination Mitigation"
  - "Bias Reduction"
  - "Consensus Mechanism"
  - "System Architecture"
  - "Benchmark Evaluation"
relevance_score: 8.0
---

# Council Mode: Mitigating Hallucination and Bias in LLMs via Multi-Agent Consensus

## 原始摘要

Large Language Models (LLMs), particularly those employing Mixture-of-Experts (MoE) architectures, have achieved remarkable capabilities across diverse natural language processing tasks. However, these models frequently suffer from hallucinations -- generating plausible but factually incorrect content -- and exhibit systematic biases that are amplified by uneven expert activation during inference. In this paper, we propose the Council Mode, a novel multi-agent consensus framework that addresses these limitations by dispatching queries to multiple heterogeneous frontier LLMs in parallel and synthesizing their outputs through a dedicated consensus model. The Council pipeline operates in three phases: (1) an intelligent triage classifier that routes queries based on complexity, (2) parallel expert generation across architecturally diverse models, and (3) a structured consensus synthesis that explicitly identifies agreement, disagreement, and unique findings before producing the final response. We implement and evaluate this architecture within an open-source AI workspace. Our comprehensive evaluation across multiple benchmarks demonstrates that the Council Mode achieves a 35.9% relative reduction in hallucination rates on the HaluEval benchmark and a 7.8-point improvement on TruthfulQA compared to the best-performing individual model, while maintaining significantly lower bias variance across domains. We provide the mathematical formulation of the consensus mechanism, detail the system architecture, and present extensive empirical results with ablation studies.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLMs），尤其是采用混合专家（MoE）架构的模型，在生成内容时普遍存在的两大关键缺陷：幻觉（即生成流畅但事实错误的内容）和系统性偏见。研究背景是，尽管以GPT-5.4等为代表的LLMs，特别是通过MoE架构高效扩展了模型能力，取得了巨大成功，但其稀疏路由机制在推理过程中可能导致专家激活不均，反而加剧了幻觉和偏见问题。例如，门控网络可能将特定查询持续路由到训练中内化了错误关联的专家（专家崩溃），或者路由决策本身会引入与表面特征相关的偏见。

现有方法如检索增强生成（RAG）和基于人类反馈的强化学习（RLHF）虽然有一定效果，但本质上仍局限于单个模型的参数化记忆和推理能力之内，未能从根本上利用不同模型间的互补性来纠正个体错误。

因此，本文要解决的核心问题是：如何超越单一模型的局限，系统性地降低LLM输出的幻觉率和偏见方差。为此，论文提出了“Council Mode”这一新颖的多智能体共识框架。其核心思路不是依赖单个模型，而是并行派遣查询到多个架构各异的先进LLM（即“专家”），并通过一个专用的共识模型来结构化地合成它们的输出。该框架通过智能分类、并行生成和结构化共识合成三个阶段，明确识别各模型回答中的共识点、分歧和独特发现，最终生成一个经过交叉验证、整合了多元见解的回应，从而在集体层面过滤掉个体模型的幻觉和特异性偏见，提升事实准确性和公正性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：幻觉与偏误研究、多智能体方法以及传统集成方法。

在**幻觉与偏误研究**方面，已有工作对幻觉进行了内在与外在的详细分类，并指出其成因包括训练数据噪声和自回归生成中的暴露偏误等。针对MoE模型，研究表明稀疏激活和专家路由偏置会加剧幻觉与知识盲区。本文的Council Mode直接针对这些问题，旨在通过多模型共识来缓解。

在**多智能体方法**领域，现有工作如多智能体辩论让同一模型的多个实例通过多轮辩论优化答案，或借鉴分布式系统共识协议。本文与之的关键区别在于：1) 采用来自不同提供商的异构模型以最大化认知多样性，而非使用同一模型的多个副本；2) 设计了结构化合成协议，明确区分共识、分歧和独特发现，而非简单多数投票；3) 引入了智能分类机制，对简单查询绕过完整流程以优化资源。

在**传统集成与一致性方法**上，经典机器学习集成方法通过聚合多个预测来提升鲁棒性。在LLM语境下，如“自我一致性”从单一模型采样多条推理路径并选择最一致的答案，也有工作采用不同LLM进行投票集成。本文超越了简单投票，通过一个专门的共识模型对专家响应进行深度语义分析，并保留各自的推理链和证据支撑。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“Council Mode”的多智能体共识框架来解决大语言模型（LLMs）的幻觉和偏见问题。其核心方法是构建一个三阶段处理流程，利用多个异构前沿LLMs的并行生成与结构化合成来达成共识，从而纠正个体模型的错误并降低系统性偏差。

**整体框架与主要模块：**
1.  **智能分诊分类器（第一阶段）：** 这是一个轻量级模块，用于评估用户查询的复杂性。它采用两级过滤：客户端使用基于正则表达式的模式匹配来识别简单查询（如问候语或超短输入）；服务器端则调用一个“思考预算”极低的轻量级LLM进行二元决策。对于被判定为“非平凡”的查询，系统才会启动完整的“议会”流程，否则直接回答以节省计算资源。
2.  **并行专家生成（第二阶段）：** 对于需要深入处理的查询，系统将其同时分发给N个（论文中N=3）架构多样化的专家模型（如GPT-5.4、Claude Opus 4.6、Gemini 3.1 Pro）。这些模型独立生成响应，并可选择性地结合网络搜索结果。通过异步并发执行，总延迟仅由最慢的专家决定，而非所有专家延迟之和，保证了效率。
3.  **结构化共识合成（第三阶段）：** 这是框架的核心创新。一个专用的合成模型接收查询和所有专家响应，并遵循包含16条强制性规则的提示词，生成一个结构化的四部分输出：
    *   **共识部分：** 提取所有专家一致支持的事实性主张。
    *   **分歧部分：** 明确识别专家之间提供矛盾信息的冲突主张。
    *   **独特发现部分：** 保留仅出现在单一专家响应中的主张。
    *   **综合分析部分：** 整合所有证据，生成一个连贯、经过事实核查的最终响应，旨在解决分歧并将独特发现置于上下文中。

**关键技术及创新点：**
*   **多智能体共识机制：** 核心创新在于通过并行调用多个异构的顶尖模型，并强制合成模型进行显式的共识、分歧和独特发现分析，而非简单地进行投票或选择。这种结构化对比显著提升了事实核查的严谨性。
*   **概率误差纠正论证：** 论文从概率角度论证了该方法的有效性。假设各专家模型的幻觉事件相互独立（因其架构多样性），所有专家在同一主张上同时产生幻觉的概率是其各自幻觉概率的乘积，从而理论上实现了错误率的指数级降低。
*   **效率优化设计：** 通过轻量级分诊阶段过滤简单查询，以及并行执行专家调用，在提升准确性的同时，有效控制了系统的总体响应延迟和计算成本。
*   **架构多样性利用：** 刻意选择来自不同提供商、具有不同底层架构的模型作为专家，旨在最大化模型的独立性，减少因共同训练数据或相似架构导致的系统性偏见或错误相关性，从而增强共识结果的鲁棒性。

### Q4: 论文做了哪些实验？

论文在开源AI工作空间中实现并评估了Council Mode框架。实验设置上，通过官方API集成，在统一环境中运行评估脚本，以确保公平比较。

使用的数据集和基准测试包括：1) HaluEval（大规模幻觉评估基准，涵盖QA、摘要和对话任务）；2) TruthfulQA（评估模型生成真实且信息丰富答案的倾向）；3) 自定义的多领域推理基准（包含科学、历史、医学、法律、技术、金融六个领域的500个问题，推理步骤复杂度为1-10级）。

对比的基线是五个前沿大模型：GPT-5.4、Claude Opus 4.6、Gemini 3.1 Pro、DeepSeek V3.2和Seed 2.0 Pro，均独立评估。

主要结果与关键指标如下：在HaluEval基准上，Council Mode的平均幻觉率为10.7%，相比最佳单体模型（Claude Opus 4.6的16.7%）相对降低了35.9%；在摘要任务上表现尤为突出（13.6% vs. 20.1%）。在TruthfulQA上，其真实得分为82.6%，信息得分为91.3%，相比最佳单体模型（Claude Opus 4.6，真实得分74.8%）绝对提升了7.8个百分点。在偏见缓解方面，Council Mode的偏见方差（σ²=0.003）相比单体模型（σ²=0.021–0.028）降低了约85–89%。在多领域推理基准上，随着任务复杂度（推理步骤数）增加，Council Mode性能下降更缓慢；在最高复杂度（10步）时，其准确率保持71.2%，显著高于GPT-5.4的50.8%和DeepSeek V3.2的43.5%。消融实验表明，结构化共识合成（而非简单多数投票）和专家多样性对性能提升至关重要；分流分类器主要优化延迟（降低30.6%），而不影响质量。

### Q5: 有什么可以进一步探索的点？

本文提出的Council Mode框架在缓解幻觉和偏见方面成效显著，但仍存在多方面局限和优化空间。首先，系统延迟较高，约为单模型的2-3倍，这限制了其在实时场景的应用，未来可探索异步生成、轻量级专家模型或提前缓存常见查询共识等优化方案。其次，依赖多个前沿商业API，成本和可用性受限，未来可研究如何融入开源模型或构建更经济的专家池。第三，共识机制无法纠正所有专家共有的错误，需引入外部知识库或事实核查模块作为补充。此外，当前采用固定专家集合，未来可开发动态路由机制，根据查询类型和领域自适应选择最合适的专家组合，以提升效率与准确性。最后，结构化共识合成过程可进一步细化，例如量化证据可信度或融合链式推理，以处理更复杂的多模态或长文本任务。

### Q6: 总结一下论文的主要内容

这篇论文提出了“Council Mode”多智能体共识框架，旨在缓解大语言模型（尤其是混合专家模型）中常见的幻觉和偏见问题。其核心贡献在于通过并行调用多个异构前沿模型并利用共识模型整合输出，显著提升了生成内容的可靠性与事实准确性。

方法上，Council Mode采用三阶段流程：首先通过智能分类器根据查询复杂度进行路由；随后并行调用不同架构的专家模型生成回答；最后由结构化共识合成模型明确识别各回答间的一致点、分歧点和独特发现，并据此生成最终响应。

主要结论显示，该框架在多个基准测试中取得显著改进：在HaluEval基准上幻觉率相对降低35.9%，在TruthfulQA上提升7.8个百分点，同时跨领域偏见方差降低85%-89%。这表明通过利用模型间的认知多样性进行结构化合成，能有效提升AI系统的可信度，为多模型协同研究提供了新方向。
