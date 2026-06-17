---
title: "FinAcumen: Financial Multimodal Reasoning via Self-Evolving Experience Memory Harness"
authors:
  - "Pianran Guo"
  - "Pengcheng Zhou"
  - "Yucheng Jian"
  - "Shuhua Chen"
date: "2026-06-16"
arxiv_id: "2606.17642"
arxiv_url: "https://arxiv.org/abs/2606.17642"
pdf_url: "https://arxiv.org/pdf/2606.17642v1"
categories:
  - "cs.AI"
tags:
  - "金融Agent"
  - "记忆机制"
  - "多模态推理"
  - "工具增强"
  - "经验回放"
  - "推理可靠性"
relevance_score: 8.5
---

# FinAcumen: Financial Multimodal Reasoning via Self-Evolving Experience Memory Harness

## 原始摘要

Financial multimodal reasoning requires agents to coordinate numerical computation, retrieval, visual interpretation, and temporal grounding across heterogeneous evidence sources. Existing tool-augmented agents improve execution fidelity, yet remain largely stateless across episodes, repeatedly rediscovering reasoning strategies and failure patterns. In high-stakes financial settings, this leads to unreliable tool routing, noisy retrieval, and hallucination-prone reasoning. We present FinAcumen, a financial reasoning agent framework centered on selective experience memory for tool-augmented multimodal reasoning. FinAcumen accumulates financially grounded reasoning experience from prior trajectories, distilling successful strategies and failure-derived cautionary rules into a persistent memory bank. During inference, retrieved experiences condition reasoning only when semantic relevance exceeds a calibrated threshold, while irrelevant memory is explicitly suppressed through a fallback mechanism. A deterministic financial tool environment further grounds numerical computation, retrieval, visual decoding, and answer verification.Across four financial multimodal reasoning benchmarks, FinAcumen consistently improves a frozen 8B vision-language model over finance-specialized models and approaches leading proprietary general-purpose models. Further analysis shows that selective experience activation improves reasoning reliability under retrieval uncertainty. Our code is anonymously available at https://anonymous.4open.science/r/FinAcumen

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决金融领域多模态推理中的核心问题：现有工具增强型智能体虽然在执行可靠性上有所提升，但它们在跨回合的推理中缺乏状态记忆，导致反复“重新发现”推理策略和失败模式，这在高风险的金融场景中尤为不可靠。具体来说，当前方法的不足包括：首先，通用大模型缺乏金融场景下的接地推理策略，而金融专用模型在分布外任务上鲁棒性有限。其次，静态微调无法提供适应异构模态组合的自适应推理策略，在图表密集和检索密集型场景下模型性能显著下降。最后，现有的基于记忆的工作虽然试图通过存储反思或轨迹来解决，但常常混淆成功与失败经验，检索到弱相关的引导，且记忆库无质量控制地扩展，引入噪声，在金融领域，这种无关检索会直接降低推理质量，甚至导致错误的“幻觉”结论。因此，本文要解决的核心问题是：如何构建一个面向金融多模态推理的、能够选择性利用过去成功与失败经验的记忆机制，在保持基础模型不变的前提下，提升工具增强型智能体在复杂、异构金融数据上的推理可靠性与准确性。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及两大类别。**方法类**相关工作中，核心是跨回合经验记忆机制。ReAct 建立了工具交织推理，但局限于单回合；Reflexion、ExpeL、ReasoningBank 和 EchoSafe 等研究则转向跨回合的持久经验积累，但本文的 FinAcumen 明确区分了成功策略（guidance）与失败警示（cautions），并通过相似度阈值触发的选择性检索和回退机制（空返回）来抑制无关记忆，这与 Self-RAG 强调的显式检索与否决策不同，更注重金融场景下的可靠性。**应用类**集中在金融多模态推理领域。现有工作如 Fin-R1、Open-FinLLMs 和 LLM Pro Finance Suite 主要通过参数更新注入领域知识，而 FinAcumen 保持主干模型冻结，在推理时通过固定工具套件和检索到的经验进行适应，因此性能差异归因于经验条件化而非模型重训练。评测基准方面，FinAcumen 在多个数据集上评估，包括 BizBench（SEC-NUM 子集，侧重数量定位）、FinMMR（图表数值推理）、FinTMMBench（时间多模态检索推理）和 FinMME（广泛金融多模态评估），这些基准覆盖了文本、多模态、时序和幻觉敏感等维度。与这些工作相比，本文的主要区别在于提出了一种选择性经验记忆框架，通过校准阈值动态激活相关经验并抑制无关信息，同时集成确定性金融工具环境以增强数值计算、检索、视觉解码和答案验证的可靠性。

### Q3: 论文如何解决这个问题？

FinAcumen 通过引入选择性经验记忆机制和确定性工具环境，系统性地解决了金融多模态推理中的核心挑战。其核心架构包含两个相互协同的主要模块：金融记忆（Financial Memory）和金融工具（Financial Tools）。

金融记忆模块是框架的核心创新，它通过多轨迹采样从模型自身的过往推理过程中积累经验，并将其转化为结构化记忆条目。每个条目包含原始问题、标准答案以及从成功轨迹中归纳的策略和从失败轨迹中提取的警示规则。记忆的激活采用选择性检索策略，仅在语义相似度超过校准阈值时才将相关经验作为上下文前缀注入提示词；当没有足够相关记忆时，模型退化为仅依赖工具进行推理，有效避免了不相关记忆带来的噪声。

金融工具模块提供了一个确定性的执行层，包含四个专门工具：数值推理引擎通过持久化命名空间支持级联操作，确保多步算术的一致性；有据数据检索通过确定性查询防止参数捏造；视觉结构解码器通过OCR预处理和按需重解析处理图表；答案整合门则作为唯一终止点，强制执行来源可追溯、单位兼容和格式规范三项验证。所有工具调用协议在有无记忆路径下完全一致，确保性能差异纯粹来源于经验引导。

这种方法的核心创新在于：将经验记忆作为推理条件化的唯一通路，通过阈值控制避免低相关记忆的干扰，同时利用确定性工具环境从根本上消除幻觉。这种选择性经验激活机制显著提升了在检索不确定性下的推理可靠性。

### Q4: 论文做了哪些实验？

论文在四个金融多模态推理基准的六个设定上进行了实验。实验设置包括冻结的Qwen3-VL-8B-Instruct作为基础模型，配备包含四类工具（数值推理、数据检索、视觉解码、答案门控）的ReAct循环，以及从训练/验证集积累约2400条经验的内存库。数据集包括：BizBench SEC-NUM（2000项，1%相对容差精确匹配）、FinMMR（Easy/Medium/Hard共3400项，0.2%相对容差）、FinTMMBench（1136项，GPT-4o-mini评判准确率）、FinMME（2220项图表题）。对比方法涵盖通用大模型（GPT-4o、Claude Sonnet、Qwen2.5-VL-72B等）和金融专用模型（FinLLaVA、Fin-R1等）。主要结果显示，FinAcumen在金融专用模型上全面领先，例如BizBench从27.67提升至68.65，FinMME从27.84提升至51.08，部分指标超越GPT-4o。消融实验表明工具模块贡献14.91%的提升，经验记忆贡献7.59%的额外提升；随记忆库规模增大精度呈单调饱和增长（从55.15%升至68.65%）；检索阈值τ=0.65和深度k_max=5取得最佳效果。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于：冷启动阶段需要大量样本构建记忆库，且当前记忆结构较为单一，难以实现跨任务策略迁移；在视觉编码方面，对多语言和图表的鲁棒性不足，可能限制实际部署。未来可探索以下方向：1) 开发样本高效的记忆压缩策略，通过元学习和主动采样降低冷启动成本；2) 设计层级化或图结构的记忆库，支持复杂推理任务的模式重组和重用；3) 引入跨语言视觉编码器对齐方案，增强对非英语金融图表和多模态证据的解析能力；4) 可尝试将成功策略的“极性感知”信号与失败规则的抑制权重动态耦合，形成自适应记忆激活阈值；5) 探索将记忆库与工具执行轨迹进行端到端联合优化，使记忆存储直接服务于工具调用决策的强化学习信号。

### Q6: 总结一下论文的主要内容

FinAcumen提出了一种面向金融多模态推理的智能体框架，通过自进化经验记忆与确定性工具环境解决现有方法缺乏跨回合记忆、推理策略重复发现和失败模式反复出现的问题。该框架从先前轨迹中积累成功策略与失败教训，形成持久记忆库，在推理时仅当语义相关性超过阈值时才激活相关经验，否则通过回退机制抑制无关记忆。同时，确定性金融工具环境保障了数值计算、检索、视觉解码和答案验证的可靠性。在四个金融多模态推理基准上，使用冻结的8B视觉语言模型，FinAcumen持续超越金融专用模型，并接近领先的通用大模型性能。消融实验证实，选择性经验激活能改善路由和策略选择，工具环境保证数值精度，且无相关经验时框架性能不退化。该去耦架构表明，外部记忆与确定性工具可以稳定地增强冻结基础模型，为专业领域AI提供了一种通用范式。
