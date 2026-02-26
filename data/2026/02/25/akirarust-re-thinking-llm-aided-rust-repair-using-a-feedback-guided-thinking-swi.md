---
title: "AkiraRust: Re-thinking LLM-aided Rust Repair Using a Feedback-guided Thinking Switch"
authors:
  - "Renshuang Jiang"
  - "Yichong Wang"
  - "Pan Dong"
  - "Xiaoxiang Fang"
  - "Zhenling Duan"
  - "Tinglue Wang"
  - "Yuchen Hu"
  - "Jie Yu"
  - "Zhe Jiang"
date: "2026-02-25"
arxiv_id: "2602.21681"
arxiv_url: "https://arxiv.org/abs/2602.21681"
pdf_url: "https://arxiv.org/pdf/2602.21681v1"
categories:
  - "cs.SE"
tags:
  - "Agent 架构"
  - "多智能体系统"
  - "工具使用"
  - "LLM 应用于 Agent 场景"
  - "规划/推理"
  - "代码生成与修复"
relevance_score: 7.5
---

# AkiraRust: Re-thinking LLM-aided Rust Repair Using a Feedback-guided Thinking Switch

## 原始摘要

Eliminating undefined behaviors (UBs) in Rust programs requires a deep semantic understanding to enable accurate and reliable repair. While existing studies have demonstrated the potential of LLMs to support Rust code analysis and repair, most frameworks remain constrained by inflexible templates or lack grounding in executable semantics, resulting in limited contextual awareness and semantic incorrectness. Here, we present AkiraRust, an LLM-driven repair and verification framework that incorporates a finite-state machine to dynamically adapt its detection and repair flow to runtime semantic conditions. AkiraRust introduces a dual-mode reasoning strategy that coordinates fast and slow thinking across multiple agents. Each agent is mapped to an FSM state, and a waveform-driven transition controller manages state switching, rollback decisions, and semantic check pointing, enabling context-aware and runtime-adaptive repair. Experimental results show that AkiraRust achieves about 92% semantic correctness and delivers a 2.2x average speedup compared to SOTA.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决Rust程序中未定义行为（UBs）的自动化修复问题，特别是在使用Unsafe Rust时，由于绕过编译器安全检查而引入的深层语义错误。研究背景是Rust语言因其内存安全保证而被广泛应用于操作系统等关键领域，但Unsafe Rust的使用带来了潜在UBs，其修复需深入语义理解，且现有方法成本高昂，占调试总成本的40%以上。

现有方法主要分为两类：一是传统基于模板的静态或动态方法（如形式化分析、模糊测试），它们依赖预定义规则匹配，当错误超出模板范围或涉及复杂语义时，因缺乏语义理解而失效；二是现有LLM辅助框架（如RustAssistant），它们虽利用大语言模型的语义推理能力，但通常采用离线单进程固定代理流程，代理调用顺序僵化，无法根据运行时语义动态调整，导致修复过程缺乏上下文感知，常产生语义不正确的代码，例如在借用相关错误中陷入局部调整或产生幻觉。

本文的核心问题是：如何设计一个能够动态适应运行时语义条件、确保修复语义正确性并提升效率的Rust修复框架。为此，论文提出AkiraRust，通过引入有限状态机来协调多代理的双模式推理（快慢思考），利用波形驱动的转换控制器管理状态切换、回滚决策和语义检查点，从而实现上下文感知和运行时自适应的修复，以克服现有方法在动态适应性和语义基础方面的不足。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于LLM的代码修复方法、针对Rust语言的特定修复工具，以及多智能体协同与推理控制框架。

在**基于LLM的代码修复方法**方面，现有研究已展示了LLM在代码分析和修复上的潜力。然而，许多现有框架受限于僵化的修复模板或缺乏对可执行语义的 grounding，导致上下文感知能力有限和语义不正确。本文提出的AkiraRust通过引入有限状态机（FSM）动态调整检测和修复流程，并融入运行时语义条件，旨在克服这些限制。

在**针对Rust的特定修复工具**方面，论文明确提到了RustBrain这一SOTA（state-of-the-art）修复工具作为基线。RustBrain采用了多种代理（如断言插入、代码修改、安全Rust替换和RAG查询）进行修复。本文的分析指出，RustBrain中不同代理对特定缺陷类型有不同效果，但现有方法在代理协调和切换上可能不够灵活。AkiraRust通过反馈引导的思维切换（fast/slow thinking）和波形驱动的状态转换控制器，实现了更上下文感知和自适应的修复，这是与RustBrain等工具的主要区别。

在**多智能体协同与推理控制框架**方面，相关工作涉及利用多个LLM智能体进行复杂任务求解。本文的贡献在于设计了一种双模式推理策略，将快思考与慢思考跨多个智能体进行协调，并通过FSM状态映射和转换控制器来管理状态切换、回滚决策和语义检查点。这与传统多智能体方法中相对静态的协作模式不同，AkiraRust强调基于运行时语义的动态适应和反馈引导。

### Q3: 论文如何解决这个问题？

论文通过构建一个基于有限状态机（FSM）的动态自适应修复框架AkiraRust来解决Rust程序中未定义行为（UB）的修复问题。其核心方法是采用一种反馈引导的双模式（快思考与慢思考）多智能体协同修复机制，将修复过程形式化为一个可动态调整的状态转移系统。

整体框架由三个关键部分组成：1）一个双模式多智能体修复库，其中每个智能体对应特定的修复模式（如断言、修改、替换）和思考模式（快速启发式或深度语义推理）；2）一个有限状态机，将每个智能体及其思考模式映射为不同的状态，并通过状态转移函数动态选择下一个修复动作；3）一个基于波形反馈的自适应校正机制，用于监控修复质量演化并指导状态转移、回滚决策和语义检查点的触发。

在架构设计上，FSM被形式化定义为六元组，包括状态集（如初始状态、断言状态、修改状态、回滚状态等）、输入符号（Rust代码）、转移函数和输出映射。修复过程始于对UB的检测，框架根据运行时语义反馈（如UB数量、语义正确性、代码结构）动态选择并调用相应的智能体生成修复候选。双模式设计使得系统能灵活切换浅层快速修复和深层语义分析，以适应不同的错误场景。

关键技术创新点主要体现在：首先，提出了波形驱动的状态转移控制器，通过实时计算代码不正确性分数曲线（波形）来量化修复质量的变化，并据此定义回滚点和语义评估点，从而避免不必要的全回滚和冗余语义检查，在保证准确性的同时降低了开销。其次，引入了TestGenAgent进行开发者意图引导的语义验证，它通过分析代码特征推断语义约束并生成针对性单元测试，提升了语义一致性。最后，整个系统将修复过程抽象为类人的认知推理，通过FSM的状态转移实现了探索与反思的动态平衡，突破了静态模板的僵化性，能够在更大的修复空间中高效搜索。

实验表明，该框架实现了约92%的语义正确性，并相比现有技术平均加速2.2倍，有效兼顾了修复的准确性与效率。

### Q4: 论文做了哪些实验？

论文实验围绕三个研究问题展开。实验使用了来自Miri编译器的Rust未定义行为数据集，涵盖47种常见UB类型。对比基线包括基于模板的框架（如Thetis-lathe）和基于LLM的修复框架（如RustAssistant、RustBrain）。评估指标包括通过Miri编译检查的通过率（pass rate）和通过语义正确性检查的执行率（exec rate）。

主要结果如下：在准确性（RQ1）方面，AkiraRust实现了100%的通过率，语义执行率在不同底层LLM（GPT-4/5、Claude-3.5）下均稳定在约85%-95%，相比单独使用LLM（25-50%）提升了40-60%。在自适应性（RQ2）方面，AkiraRust对所有UB类型均保持了稳定且高的修复质量（约86%-92%），其自适应回滚机制在示例中仅需调用7次智能体即可完成修复，而对比方法RustBrain需要调用23次。在先进性（RQ3）方面，AkiraRust的语义正确率达到92%，相比RustAssistant和RustBrain分别提升了15%和50%。在效率上，AkiraRust相比RustBrain平均减少了约2倍的智能体调用次数，平均修复时间从218.4秒缩短至101.4秒（使用GPT-5），实现了2.2倍的平均加速，相比人工专家则减少了7倍的开销。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其评估主要基于特定数据集，可能未覆盖Rust语言中所有类型的未定义行为（UB）或复杂并发场景。未来研究可探索更广泛的UB类型，如内存安全漏洞或数据竞争，并考虑将框架扩展到其他系统编程语言（如C++）。此外，当前方法依赖LLM的语义理解能力，可能受模型固有偏差影响，未来可结合形式化验证技术增强可靠性。改进思路包括引入动态符号执行以生成更全面的测试用例，或设计轻量级运行时监控机制来实时验证修复结果。还可探索多模态反馈机制，例如集成静态分析工具的输出，以提升上下文感知的准确性。

### Q6: 总结一下论文的主要内容

该论文提出了AkiraRust框架，旨在解决现有LLM辅助Rust代码修复方法在语义理解和上下文感知方面的不足。核心问题是修复Rust程序中的未定义行为需要精确的语义分析，而现有方法受限于僵化的模板或缺乏可执行语义的验证，导致修复结果语义不正确。

方法上，AkiraRust创新性地引入了一个由有限状态机驱动的多智能体协作框架。它采用双模式推理策略，协调“快速”与“慢速”思维，每个智能体对应一个状态机状态。通过一个波形驱动的转换控制器来动态管理状态切换、回滚决策和语义检查点，从而使修复过程能够根据运行时语义条件进行自适应调整，实现了上下文感知和运行时自适应的修复。

主要结论是，实验表明AkiraRust在语义正确性上达到约92%，相比现有最佳技术平均加速2.2倍。其核心贡献在于将状态机与多智能体推理结合，为LLM驱动的代码修复提供了更可靠、高效的语义验证和自适应决策新范式。
