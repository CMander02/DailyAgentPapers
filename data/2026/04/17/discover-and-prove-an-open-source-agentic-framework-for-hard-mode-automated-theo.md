---
title: "Discover and Prove: An Open-source Agentic Framework for Hard Mode Automated Theorem Proving in Lean 4"
authors:
  - "Chengwu Liu"
  - "Yichun Yin"
  - "Ye Yuan"
  - "Jiaxuan Xie"
  - "Botao Li"
  - "Siqi Li"
  - "Jianhao Shen"
  - "Yan Xu"
  - "Lifeng Shang"
  - "Ming Zhang"
date: "2026-04-17"
arxiv_id: "2604.15839"
arxiv_url: "https://arxiv.org/abs/2604.15839"
pdf_url: "https://arxiv.org/pdf/2604.15839v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LO"
tags:
  - "Automated Theorem Proving"
  - "Agentic Framework"
  - "Reasoning"
  - "Benchmark"
  - "Hard Mode"
  - "Self-Reflection"
  - "Tool Use"
  - "Formal Verification"
relevance_score: 8.5
---

# Discover and Prove: An Open-source Agentic Framework for Hard Mode Automated Theorem Proving in Lean 4

## 原始摘要

Most ATP benchmarks embed the final answer within the formal statement -- a convention we call "Easy Mode" -- a design that simplifies the task relative to what human competitors face and may lead to optimistic estimates of model capability. We call the stricter, more realistic setting "Hard Mode": the system must independently discover the answer before constructing a formal proof. To enable Hard Mode research, we make two contributions. First, we release MiniF2F-Hard and FIMO-Hard, expert-reannotated Hard Mode variants of two widely-used ATP benchmarks. Second, we introduce Discover And Prove (DAP), an agentic framework that uses LLM natural-language reasoning with explicit self-reflection to discover answers, then rewrites Hard Mode statements into Easy Mode ones for existing ATP provers. DAP sets the state of the art: on CombiBench it raises solved problems from 7 (previous SOTA, Pass@16) to 10; on PutnamBench it is the first system to formally prove 36 theorems in Hard Mode -- while simultaneously revealing that state-of-the-art LLMs exceed 80% answer accuracy on the same problems where formal provers manage under 10%, exposing a substantial gap that Hard Mode benchmarks are uniquely suited to measure.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自动定理证明（ATP）领域评估中存在的“简单模式”偏差问题，并提出更严格的“困难模式”评估框架。研究背景是，当前AI解决数学问题（尤其是IMO级别竞赛题）的能力备受关注，但许多现有的形式化证明基准（如MiniF2F、FIMO）在构造待证明的形式化命题时，往往将最终答案直接嵌入到陈述中（即“简单模式”）。这种做法简化了任务，因为系统无需自行发现答案，只需对已知结论进行形式化验证，这与人类参赛者必须独立探索和发现答案的真实情境不符，可能导致对模型能力的高估。

现有方法的不足在于，这种“简单模式”的评估设置未能准确反映AI系统在解决原始数学问题时所面临的完整挑战——即同时需要“发现”答案和“证明”结论。这造成评估结果可能过于乐观，且无法衡量系统关键的发现与推理能力。

因此，本文要解决的核心问题是：如何建立一个更真实、更严格的评估范式来度量AI系统解决竞赛级数学问题的综合能力。为此，论文提出了两个主要贡献来推动“困难模式”研究：一是发布了经过专家重新标注的基准变体MiniF2F-Hard和FIMO-Hard，确保形式化任务与人类面临的原始问题对齐，要求系统必须独立发现答案；二是提出了一个名为“发现与证明”（DAP）的智能体框架，该框架利用大语言模型进行自然语言推理和自我反思来发现答案，然后将“困难模式”陈述转化为“简单模式”陈述，以便调用现有的ATP证明器完成形式化证明。通过这种方式，论文旨在缩小评估环境与现实挑战之间的差距，并更准确地衡量AI的数学问题解决能力。

### Q2: 有哪些相关研究？

本文的相关研究可分为方法类、评测类和数据类。在方法类中，相关工作包括：1）非形式化数学推理系统（如基于CoT提示和RLVR训练的LLM），它们在GSM8K等基准上表现优异，但生成的证明难以自动验证；2）形式化定理证明系统，如Kimina-Prover、DeepSeek-Prover-V2和Seed-Prover，它们利用证明助手确保严谨性，并在MiniF2F等基准上取得进展；3）指导证明的框架，如DSP/DSP+，其使用自然语言草稿引导形式证明器。本文的DAP框架与DSP/DSP+的关键区别在于，DAP采用智能体框架，通过显式自我反思来发现答案，再将问题转化为“简单模式”供现有证明器处理，从而专注于“困难模式”的挑战。在评测类中，现有基准如MiniF2F、FIMO和PutnamBench大多采用“简单模式”，即在形式化陈述中嵌入答案，这降低了问题难度并可能导致语义未对齐。本文通过发布MiniF2F-Hard和FIMO-Hard的重新标注版本，纠正了此类偏差，提供了更严格的评估环境。在数据类中，为缓解形式化数据稀缺，自动形式化方法（如Lean Workbook、FormalMATH）被用于生成陈述，但它们通常遵循“简单模式”且缺乏语义正确性保证，而本文的数据集则基于专家标注，确保了质量和对齐性。

### Q3: 论文如何解决这个问题？

论文提出的Discover and Prove (DAP)框架通过将“困难模式”自动定理证明分解为“发现答案”和“形式化证明”两个独立阶段来解决核心问题。其整体架构由**发现模块**和**证明模块**串联组成，核心创新在于通过自然语言推理与自我反思来独立发现数学问题的答案，随后将原问题重写为“简单模式”陈述，供现有定理证明器完成形式化验证。

**整体框架与主要模块**：
1.  **发现模块**：该模块完全在自然语言层面运作，模拟人类数学家的解题过程。它接收自然语言描述的数学问题，利用大型语言模型（LLM）的推理能力，通过一个多步骤的闭环流程来生成并确认正确答案。具体步骤包括：
    *   **解决方案生成**：LLM生成详细的思维链（Chain-of-Thought），推导出问题的潜在答案。
    *   **自我验证**：同一个LLM被指示检查其推理步骤，识别并报告潜在错误。
    *   **自我修正**：如果发现错误，LLM根据错误报告生成修正后的解决方案。
    *   **重写**：利用确认的解决方案、原始问题以及推理过程，LLM将包含两个占位符（`sorry`）的“困难模式”Lean 4陈述，重写为仅包含一个占位符（对应于待证明的最终结论）的“简单模式”陈述。这一步是关键转换，将问题转化为标准ATP任务。

2.  **证明模块**：该模块在形式化语言层面运作。它接收发现模块输出的、已嵌入答案的“简单模式”Lean 4陈述，然后调用一个专门的定理证明器（论文中使用Goedel-Prover-V2）来构造严格的形式化证明，填补最后一个占位符。

**关键技术设计与创新点**：
*   **解耦式双阶段设计**：将困难的“同时发现与证明”任务清晰地分离为“自然语言发现”和“形式语言证明”两个子任务。这种设计允许分别利用最先进的推理LLM和定理证明LLM，框架性能可随任一底层模型的进步而提升。
*   **基于自我反思的可靠发现机制**：发现模块并非简单的一次性生成答案，而是集成了“生成-验证-修正”的迭代式自我反思流程。这显著提高了答案发现的准确性，因为错误的答案会导致生成无法证明的形式陈述。该机制是应对“困难模式”挑战的核心。
*   **陈述重写接口**：通过精心设计的提示（prompt），引导LLM将自然语言解决方案准确、结构化地嵌入到形式化的Lean 4语句中，实现了从非结构化推理到结构化形式问题的无缝桥接，为后续证明铺平道路。
*   **开源与基线价值**：整个框架被实现为开源项目，并指定了具体的模型（如GPT-OSS-120B用于发现），这不仅保证了可复现性，也为未来“困难模式”ATP研究提供了一个明确的、可比较的当代基线。

### Q4: 论文做了哪些实验？

论文在四个数据集上进行了实验：PutnamBench（共660题，其中340题为Hard Mode）、CombiBench（100题，45题Hard Mode）、miniF2F-test（244题，197题Hard Mode）和FIMO（149题，70题Hard Mode）。实验设置上，作者提出的DAP框架包含发现模块和证明模块：发现模块使用开源模型GPT-OSS-120B进行自然语言推理和自我验证（最多30次迭代尝试），证明模块则采用当前性能最优的Goedel-Prover-V2，并遵循其推荐配置（温度0.7，最大token数30,000，采样32次，使用Pass@32评估）。对比方法包括多个开源证明器在Easy Mode下的表现，如DeepSeek-Prover-V1.5、DeepSeek-Prover-V2 (CoT)、Kimina-Prover Preview、Goedel-Prover-SFT和Goedel-Prover-V2，以及在Hard Mode下的Kimina-Prover Preview。主要结果显示，DAP框架在Hard Mode下取得了最先进性能：在CombiBench上解决了10个问题（此前最优为8个）；在PutnamBench上首次在Hard Mode下证明了36个定理，其中解决了19个答案未给定的“解式问题”；在miniF2F-test上解决了201个问题（其中168个为Hard Mode）。关键数据指标包括：DAP在PutnamBench Hard Mode下总解题数36，解式问题解题数19；CombiBench Hard Mode下总解题数10，解式问题解题数2；miniF2F-test Hard Mode下总解题数204，解式问题解题数171。实验还发现，大型语言模型在相同问题上的答案准确率超过80%，而形式化证明器的解题率低于10%，凸显了Hard Mode基准在衡量能力差距方面的独特价值。

### Q5: 有什么可以进一步探索的点？

本文提出的DAP框架在Hard Mode自动定理证明上取得了进展，但也存在局限并指明了未来方向。首先，其两阶段设计（发现答案后重写）虽能防止作弊，但流程相对固化，未来可探索更紧密的交互模式，例如让证明器在遇到困难时动态反馈并引导发现模块进行修正，形成迭代式协同。其次，实验表明在简单问题上显式的自我反思机制可能引入噪声，因此未来的智能体框架需要具备**自适应能力**，能根据问题难度动态调整反思深度或选择是否启用代理模式，以平衡效率与效果。

更根本的探索点在于**弥合自然语言推理与形式语言证明之间的巨大性能差距**。论文数据显示，LLM在PutnamBench上的答案准确率超过80%，而形式证明器的成功率低于10%。这揭示了当前形式化验证系统的瓶颈。未来的研究应致力于深度融合两者优势：一方面，可以增强LLM对形式语言的理解与生成能力，使其能直接产出更严谨、可验证的推理步骤；另一方面，可以改进定理证明器，使其能更好地理解和利用自然语言推理中发现的中间结论或策略。此外，构建更多样、更复杂的Hard Mode基准测试，以持续推动两类系统在**开放答案发现**和**严格形式验证**两方面的共同进步，也是一个关键方向。

### Q6: 总结一下论文的主要内容

该论文针对自动定理证明中“简单模式”存在的语义偏差和评估局限性，提出了更严格的“困难模式”设定，要求系统先独立发现答案再构建形式化证明。核心贡献包括：一是发布了由专家重新标注的困难模式基准数据集MiniF2F-Hard和FIMO-Hard，修正了原有数据集的语义对齐问题；二是提出了“发现与证明”智能体框架，该框架利用大语言模型进行自然语言推理和显式自我反思来发现答案，随后将困难模式问题转化为简单模式问题供现有证明器处理。实验表明，该框架在CombiBench和PutnamBench上取得了最先进的性能，首次在PutnamBench困难模式下证明了36个定理，同时揭示了大语言模型答案准确率超过80%而形式化证明器成功率低于10%的巨大差距，凸显了困难模式基准在衡量AI系统真实数学问题解决能力方面的独特价值。
