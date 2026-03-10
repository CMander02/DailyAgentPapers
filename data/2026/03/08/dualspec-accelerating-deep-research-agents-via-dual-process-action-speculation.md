---
title: "DualSpec: Accelerating Deep Research Agents via Dual-Process Action Speculation"
authors:
  - "Shuzhang Zhong"
  - "Baotong Lu"
  - "Qi Chen"
  - "Chuanjie Liu"
  - "Fan Yang"
  - "Meng Li"
date: "2026-03-08"
arxiv_id: "2603.07416"
arxiv_url: "https://arxiv.org/abs/2603.07416"
pdf_url: "https://arxiv.org/pdf/2603.07416v1"
categories:
  - "cs.LG"
tags:
  - "Agent Acceleration"
  - "Speculative Execution"
  - "Reasoning-Execution Overlap"
  - "Tool-Using Agents"
  - "Action Heterogeneity"
  - "Deep Research Agents"
  - "Latency Optimization"
  - "Verification"
relevance_score: 8.5
---

# DualSpec: Accelerating Deep Research Agents via Dual-Process Action Speculation

## 原始摘要

Large language model-based deep research agents have been increasingly popular for addressing long-horizon information-seeking tasks, but they often incur high end-to-end latency due to extensive reasoning and frequent tool use. Speculation frameworks aim to reduce latency by overlapping action execution with reasoning; however, existing approaches typically rely on uniform speculation strategies and strict action matching, which limits inference speedups and robustness. In this work, we revisit the speculate-verify paradigm for deep research agents through the lens of action heterogeneity. We show that \textit{Search} and \textit{Visit} actions exhibit fundamentally different reasoning and model capacity requirements: entropy-based analysis reveals that Search decisions have higher uncertainty and benefit significantly from explicit reasoning, whereas Visit decisions have lower entropy and depend primarily on model capacity. Motivated by this dual-process characteristic, we propose DualSpec, a heterogeneous speculation framework equipped with a lightweight, confidence-based semantic verifier. Experiments across multiple models and benchmarks demonstrate that DualSpec achieves up to 3.28$\times$ end-to-end speedup while maintaining accuracy comparable to fully reasoning agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型的深度研究智能体在执行长时程信息搜索任务时面临的高延迟问题。当前，这类智能体通常遵循“推理-行动-观察”的循环范式，其推理过程和外部工具调用是严格顺序执行的，导致端到端延迟很高，有时甚至需要数分钟来完成一个查询。为了降低延迟，已有研究提出了“推测-验证”范式，即让一个轻量级模型预先推测并执行下一个动作，同时让基础模型并行进行推理，如果推测正确则直接采纳结果以节省时间。然而，现有的推测方法通常采用统一的推测策略和严格的行动匹配验证，这存在两个主要不足：一是未能考虑到智能体不同行动类型（如“搜索”和“访问”）在不确定性和对推理的依赖上存在本质差异，导致推测准确性和效率受限；二是严格的行动匹配验证不够鲁棒（例如，语义相同但措辞不同的搜索查询会被判定为不匹配），并且验证过程通常需要等待基础模型完成推理，这又将推理置于关键路径上，限制了延迟的降低。

因此，本文的核心问题是：如何设计一个更高效、更鲁棒的“推测-验证”框架，以显著加速深度研究智能体的执行，同时不损害其任务性能。具体而言，论文通过分析行动异质性，发现“搜索”行动决策不确定性高，显著受益于显式推理，而“访问”行动决策不确定性低，主要依赖模型的知识容量。基于这种“双过程”特性，论文提出了名为DualSpec的异构推测框架。该框架为不同类型的行动匹配不同的推测策略（如对“搜索”使用小型推理模型，对“访问”使用大型模型但跳过推理），并引入一个基于模型内部置信度的轻量级语义验证器，从而将基础模型的推理从验证的关键路径中移除，在保证准确性的前提下实现更高的加速比。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、评测类和理论类。在方法类中，**推测-验证范式**是核心，例如动态推测规划（Dynamic Speculative Planning）利用小模型草拟动作并获取结果，再由强模型进行完整推理，通过编辑距离等标准验证；SPAgent在早期跳过显式推理，后期转入推测-验证阶段以保持性能；推测解码（speculative decoding）在词元级别预测未来词元以加速推理，与智能体级推测互补。此外，SpecReason通过将简单推理步骤动态卸载到小模型来减少开销，但未针对迭代使用工具的智能体场景。在评测类工作中，研究通常基于GAIA等基准测试智能体性能与延迟。在理论类方面，**双过程理论**（Dual-process theory）从认知科学区分快速直觉的System 1和慢速深思的System 2，近期被用于解释和指导LLM推理，例如System-1.x Planner将任务分解为简单和复杂子步骤并分配不同策略，但需要大量训练且针对特定规划场景。

本文与这些工作的关系和区别在于：首先，本文聚焦于深度研究智能体（如使用Search和Visit动作），而现有推测方法多采用统一策略和严格动作匹配，限制了加速效果和鲁棒性；本文则通过动作异质性分析，揭示Search和Visit在不确定性和推理需求上的本质差异，提出异构推测框架DualSpec。其次，本文受双过程理论启发，但将其系统应用于工具使用智能体，并设计轻量级语义验证器，无需大量训练即可实现加速，这与System-1.x Planner等需要训练的方法不同。最后，本文在保持准确性的同时实现端到端加速，弥补了现有工作在智能体场景中的探索不足。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为DualSpec的异构推测框架来解决深度研究智能体因广泛推理和频繁使用工具而导致的高端到端延迟问题。该框架的核心方法是基于“行动异质性”的观察，将智能体的行动区分为需要深度审慎推理的“搜索”行动和依赖快速模式识别的“访问”行动，并针对性地采用不同的推测策略。

整体框架遵循“起草-验证”的工作流程。在每个决策步骤，系统并行生成两个候选行动：一个是由小型语言模型（SLM）结合显式推理生成的“系统2”草案，另一个是由大型语言模型（LLM）跳过推理生成的“系统1”草案。随后，框架根据当前行动类型和小模型输出的推理痕迹，自适应地选择一个临时草案。最后，由一个基于置信度的轻量级语义验证器（使用全容量基础模型作为评判者）对草案进行评估。若草案被判定为与当前推理轨迹在语义上一致，则被接受并直接执行；否则，系统将回退到使用全容量模型进行完整推理以重新生成行动。

主要模块与创新点包括：
1.  **异构行动起草**：这是DualSpec的核心创新。它打破了现有推测框架对所有行动采用统一策略（如一律减少推理深度或模型容量）的限制。具体而言，对于高不确定性、需要将模糊研究目标转化为具体查询的“搜索”行动，框架倾向于选择由小模型结合显式推理生成的草案，因为推理能显著降低其决策熵。对于低不确定性、基于检索内容和模式匹配的“访问”行动，则倾向于选择由大模型跳过推理生成的草案，以充分利用其参数化知识。
2.  **长时程推理保留机制**：为确保高层推理信息不丢失，当小模型草案的推理痕迹长度超过预设阈值时，无论其最终行动类型是“搜索”还是“访问”，框架都会保留该完整草案（包括推理和行动）。这保证了可能对后续决策有益的全局分析或中间摘要得以延续。
3.  **轻量级语义验证器**：不同于依赖严格行动匹配的验证方法，DualSpec的验证器评估草案的推理是否连贯以及提议的行动是否有助于推进任务。它将评判模型的输出分布转化为一个连续的置信度分数（接受与拒绝的对数概率差），并与预设阈值比较以决定接受或回退。这种方法避免了将基础模型的完整推理置于关键路径上，实现了更快的验证，同时通过仅对少数不确定步骤触发昂贵的完整推理，优化了效率与准确性的权衡。

通过这种结合了双过程行动推测和轻量语义验证的异构设计，DualSpec能够根据行动的内在需求动态分配推理资源，在保持与完全推理智能体相近准确性的同时，实现了最高达3.28倍的端到端加速。

### Q4: 论文做了哪些实验？

实验设置方面，论文在单租户环境下部署模型，每个模型使用一块 NVIDIA A100 GPU，推理批次大小为4。MiroThinker 模型采用4位量化，Qwen 模型使用原生 FP8 量化，以避免 GPU 内存溢出。实验基于 MiroMind 深度研究框架构建智能体，工具调用遵循 MCP 接口进行标准化，搜索调用通过 Bing API 执行，访问操作（页面获取和内容提取）由 Jina 提供固定后端支持，所有模型均在 SGLang 上运行。

使用的数据集是三个代表性的深度研究基准：GAIA-Text-103、XBench-DeepSearch 和 Seal-0。对比的基线方法是两种推测式智能体框架：DSP 和 SPAgent。DSP 面向规划任务，仅在草稿与基础动作（最小编辑距离）匹配时才接受；SPAgent 专为网络搜索设计，早期跳过验证但后期强制执行严格的动作匹配。与它们统一的草稿生成和动作对齐验证不同，本文提出的 DualSpec 采用针对 System 2/System 1 动作的异构草稿生成以及语义验证，该验证接受轨迹一致但不要求动作完全等价的草稿。

主要结果如下：DualSpec 在三个模型对和三个基准上实现了 1.33 倍至 3.28 倍的端到端加速，平均约为 2 倍，同时保持了与完全推理智能体相当的 pass@1 准确率。具体到模型对，在 MiroThinker-72B + 8B 上加速 1.8 倍，在 MiroThinker-72B + 30B 上加速 2.6 倍，在 Qwen3-32B + 4B 上加速 1.5 倍。其中 30B 配置因 MoE 设计（每次前向传播激活约 30 亿参数）和更强的基础能力减少了基础模型干预次数，从而获得了最高的加速比。关键数据指标显示，在 MiroThinker-72B+8B 和 GAIA 数据集上，原始方法准确率 63.1%，延迟 1041 单位；异构推测方法在保持 63.1% 准确率的同时，将延迟降至 605 单位。此外，研究发现将大模型干预率控制在约 20% 至 30% 即可达到与基础模型相当的准确率，同时保留异构推测的大部分延迟优势。验证器阈值 τ 在 GAIA 的保留集上进行调整，以瞄准约 20% 的干预率，并在所有实验中复用。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其核心假设——搜索与访问行为存在固有的不确定性差异——可能在不同任务或领域泛化性不足。未来研究可探索更细粒度的动作分类，例如区分信息检索中的不同类型查询或工具调用，并建立动态不确定性评估模型，而非依赖预设的静态分类。此外，当前语义验证器虽轻量，但可能无法完全捕捉复杂上下文中的语义一致性，未来可引入多模态验证或基于强化学习的自适应验证机制。

结合个人见解，可能的改进方向包括：1）设计分层推测策略，允许系统根据实时反馈调整推测深度，例如在任务初期采用保守策略，随信息积累逐步激进；2）将推测框架与模型蒸馏结合，训练专用的小型“行为模拟器”来替代部分大模型推理，进一步降低延迟；3）探索跨任务迁移学习，利用元学习让系统快速适应新领域的行为不确定性模式，提升泛化能力。这些方向有望在保持准确性的同时，进一步突破现有加速瓶颈。

### Q6: 总结一下论文的主要内容

该论文针对基于大语言模型的深度研究代理在长周期信息检索任务中面临的高延迟问题，提出了一种名为DualSpec的异构推测框架。核心问题是现有推测方法采用统一策略和严格动作匹配，限制了推理加速和鲁棒性。论文通过分析发现，代理的“搜索”和“访问”两类动作具有异质性：搜索决策不确定性高，需显式推理；访问决策熵值低，更依赖模型能力。基于此，DualSpec采用双过程推测机制，为两类动作设计不同推测策略，并配备一个轻量级、基于置信度的语义验证器来确保正确性。实验表明，该方法在保持与完全推理代理相近准确率的同时，实现了最高3.28倍的端到端加速，显著提升了深度研究代理的执行效率。
