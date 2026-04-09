---
title: "TraceSafe: A Systematic Assessment of LLM Guardrails on Multi-Step Tool-Calling Trajectories"
authors:
  - "Yen-Shan Chen"
  - "Sian-Yao Huang"
  - "Cheng-Lin Yang"
  - "Yun-Nung Chen"
date: "2026-04-08"
arxiv_id: "2604.07223"
arxiv_url: "https://arxiv.org/abs/2604.07223"
pdf_url: "https://arxiv.org/pdf/2604.07223v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
  - "cs.SE"
tags:
  - "Agent Safety"
  - "Tool-Calling"
  - "Benchmark"
  - "Guardrails"
  - "Multi-Step Trajectories"
  - "Security"
  - "Evaluation"
relevance_score: 8.0
---

# TraceSafe: A Systematic Assessment of LLM Guardrails on Multi-Step Tool-Calling Trajectories

## 原始摘要

As large language models (LLMs) evolve from static chatbots into autonomous agents, the primary vulnerability surface shifts from final outputs to intermediate execution traces. While safety guardrails are well-benchmarked for natural language responses, their efficacy remains largely unexplored within multi-step tool-use trajectories. To address this gap, we introduce TraceSafe-Bench, the first comprehensive benchmark specifically designed to assess mid-trajectory safety. It encompasses 12 risk categories, ranging from security threats (e.g., prompt injection, privacy leaks) to operational failures (e.g., hallucinations, interface inconsistencies), featuring over 1,000 unique execution instances. Our evaluation of 13 LLM-as-a-guard models and 7 specialized guardrails yields three critical findings: 1) Structural Bottleneck: Guardrail efficacy is driven more by structural data competence (e.g., JSON parsing) than semantic safety alignment. Performance correlates strongly with structured-to-text benchmarks ($ρ=0.79$) but shows near-zero correlation with standard jailbreak robustness. 2) Architecture over Scale: Model architecture influences risk detection performance more significantly than model size, with general-purpose LLMs consistently outperforming specialized safety guardrails in trajectory analysis. 3) Temporal Stability: Accuracy remains resilient across extended trajectories. Increased execution steps allow models to pivot from static tool definitions to dynamic execution behaviors, actually improving risk detection performance in later stages. Our findings suggest that securing agentic workflows requires jointly optimizing for structural reasoning and safety alignment to effectively mitigate mid-trajectory risks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在作为自主智能体（Agent）执行多步骤工具调用任务时，其**中间执行轨迹（trajectory）中存在的安全风险**缺乏有效评估和防护的问题。随着LLM从静态聊天机器人演变为能自主调用外部工具的智能体，主要的安全漏洞表面已从最终输出转移到了中间执行步骤。然而，现有的安全防护措施（guardrails）和评估基准主要针对模型的自然语言响应（如防范越狱攻击、幻觉等），它们在复杂的、结构化的多步骤工具调用轨迹中的有效性几乎未被探索。

现有方法存在明显不足。一方面，虽然已有独立的安全护栏模型用于防护LLM，但其在智能体工作流中的应用非常有限。例如，现有的工具调用监控方案（如MCPGuard）通常仅限于单步、调用后的检测，无法在恶意调用到达服务器前进行拦截，也无法监控多步轨迹中可能存在的风险（即使最终输出无害，中间步骤也可能造成危害）。另一方面，现有的智能体安全基准主要关注动态环境中端到端的智能体韧性，缺乏用于独立评估安全监控器的、具有精确步骤级标注的静态轨迹数据。

因此，本文的核心问题是：**如何系统性地评估安全护栏模型在多步骤工具调用轨迹中识别和拦截风险的能力？** 为填补这一空白，论文引入了首个专门的基准测试TraceSafe-Bench。该基准通过一种新颖的“从良性到有害编辑”方法构建，在真实的轨迹中确定性注入12类风险（涵盖安全威胁与操作故障），提供了超过1000个具有精确步骤级标注的多步执行实例。基于此基准，论文系统地评估了各类护栏模型，旨在诊断当前防护方案在应对智能体工作流中结构性风险时的效能瓶颈，并推动开发更有效的防护策略。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：工具调用能力演进、智能体安全性评估以及推理时护栏技术。

在**工具调用能力演进**方面，早期研究如PAL、Toolformer奠定了LLM使用外部工具的基础，ReAct引入了序列化推理轨迹来指导执行，后续的Gorilla、ToolLLM等通过大规模API落地和评估系统化这些能力。近期，Model Context Protocol (MCP)等标准化协议推动了从孤立调用向有状态协调的转变。本文指出，随着自主性和执行权限提升，攻击面扩大，仅靠文本级安全机制已不足。

在**智能体安全性评估**领域，研究重点已从简单的提示过滤转向复杂行为风险评估。基准如AgentHarm、Agent Security Bench评估模型处理有害指令的能力；ToolEmu通过模拟器检测良性意图的危险副作用；AgentDojo评估在交互工作空间中对间接提示注入的抵抗力；CVE-bench则测试利用网络漏洞的能力。此外，还有针对MCP等新兴生态的协议特定漏洞评估（如MCPSecBench、MCPTox）。这些工作侧重于动态、端到端的评估，但缺乏对独立护栏进行基准测试所需的静态、步骤级轨迹和确定性标注，这正是本文TraceSafe-Bench旨在填补的空白。

在**推理时护栏技术**方面，为规避高成本模型重训练，出现了众多专用护栏系统，如可编程框架NeMo Guardrails，以及基于模型的分类器如Llama Guard、Granite Guardian、ShieldGemma、Qwen guardrails和WildGuard。它们在标准安全评估（如GuardBench）上表现良好，但通常只关注交互的语义“表面”（初始提示和最终响应）。近期工作如MCP-Guard虽涉及工具调用护栏，但专注于孤立工具调用，忽略了多步轨迹中嵌入的风险。本文的TraceSafe-Bench则专门用于评估在执行过程中、最终有害输出产生前，对不安全轨迹的拦截能力。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为TraceSafe-Bench的综合性基准测试来解决多步骤具身智能体轨迹中的安全护栏评估问题。其核心方法是采用一种“良性到有害编辑”的策略，系统性地生成包含精确标注风险的轨迹数据，从而实现对护栏模型在中间执行步骤中风险检测能力的评估。

整体框架分为数据构建和评估两部分。在数据构建阶段，首先从伯克利函数调用排行榜的多步骤任务中收集良性种子轨迹，这些轨迹由多个模型生成且执行完全正确，确保了生态有效性。随后，基于一个涵盖12类风险的新颖分类法，对种子轨迹进行程序化编辑，生成有害变体。编辑过程采用“检查-突变”的两阶段逻辑：检查阶段确定特定风险类型在轨迹的某个步骤是否适用，过滤掉结构不兼容或语义不合理的编辑点；突变阶段则通过预定义的代码逻辑对选定组件进行受控修改，例如在工具描述中注入恶意负载、伪造执行输出、移除关键参数单位或插入冗余参数等，从而生成具有可验证的步骤级真实标签的风险实例。

主要模块包括风险分类体系、自动化编辑流水线以及评估协议。风险分类覆盖四大领域：安全威胁（如提示注入、隐私泄露）、操作故障（如幻觉、接口不一致）等。编辑流水线确保了每个风险实例都精准定位在轨迹的特定步骤，避免了大规模人工标注的成本和LLM作为评判者可能带来的循环偏差。评估时，给定用户查询、工具集和执行历史，测试护栏模型能否在任意步骤成功拦截模拟的不安全行动。

创新点在于：第一，首次创建了专注于评估轨迹中间安全性的基准，填补了现有研究空白；第二，提出了系统化的数据生成方法，通过程序化编辑获得确定性真实标签，克服了数据稀缺和标注模糊的挑战；第三，评估揭示了关键发现，如护栏效能更依赖于结构化数据理解能力而非语义安全对齐，模型架构比规模影响更大，以及检测精度在长轨迹中保持稳定甚至后期有所提升。该方法为优化智能体工作流安全提供了新的方向，即需要联合优化结构推理和安全对齐能力。

### Q4: 论文做了哪些实验？

该论文构建了名为TraceSafe-Bench的基准测试，对LLM安全护栏在多步工具调用轨迹中的效能进行了系统性评估。实验设置包括评估13个作为护栏的通用LLM模型和7个专用安全护栏模型。数据集为TraceSafe-Bench，覆盖12个风险类别（如提示注入、隐私泄露、幻觉、接口不一致等），包含超过1000个独特的执行实例。评估任务主要是对轨迹进行二元分类（判断是否安全），分为“无模式”和“有模式”两种设置。

对比方法涵盖了开源和闭源模型，包括GPT系列、Gemini系列、Llama系列、Qwen系列、Granite等。主要结果通过分类准确率呈现。关键数据指标显示，在无模式二元分类中，整体性能（Avg.）较好的模型如GPT-5 mini达到86.36%的不安全类别平均准确率，但平衡准确率（Avg.）约为51.70%；Qwen3-1.7B在不安全类别上表现突出（98.96%），但对良性样本识别率为0%，平衡准确率约49.48%。结果表明：1）性能更依赖于结构数据能力（如JSON解析），与结构化到文本基准相关性高（ρ=0.79），而与标准越狱鲁棒性几乎无关；2）模型架构比规模对风险检测性能影响更大，通用LLM通常优于专用护栏；3）时间稳定性方面，随着轨迹步数增加，模型能利用动态执行行为提升风险检测性能。

### Q5: 有什么可以进一步探索的点？

基于论文摘要，TraceSafe的研究揭示了当前LLM安全护栏在评估多步工具调用轨迹时的核心局限，并指出了几个关键的未来探索方向。

首先，论文的核心发现是“结构性瓶颈”，即护栏的有效性更依赖于结构化数据处理能力（如JSON解析），而非语义安全对齐。这表明当前的安全评估范式存在偏差，未来研究需开发能同时衡量结构推理与语义安全对齐的联合评估框架。一个可能的改进思路是设计新型护栏架构，将结构化数据解析模块与深度语义理解模型（如经过特定风险微调的模型）进行集成，而非依赖单一模型。

其次，研究发现模型架构的影响大于规模，通用LLM在轨迹分析上优于专用安全护栏。这指向一个重要的研究方向：如何为智能体工作流设计专用、轻量且高效的安全中间件或监控层？未来的工作可以探索将轨迹风险评估任务形式化为一个独立的、可插拔的“轨迹审计”模块，该模块能实时分析智能体的动作序列模式，而非仅检查单一步骤的输出。

最后，关于“时间稳定性”的发现（后期风险检测性能提升）值得深入利用。可以进一步探索如何主动设计轨迹，使早期步骤能为安全检测提供上下文或“诱饵”，从而系统性地增强整个工作流的安全性。此外，基准本身可扩展至更复杂、开放域的场景，并考虑对抗性攻击者如何故意构造多步安全规避轨迹，以测试护栏的鲁棒性极限。

### Q6: 总结一下论文的主要内容

该论文针对大型语言模型（LLM）从静态聊天机器人演变为自主代理时，安全防护的核心挑战从最终输出转移到中间执行轨迹的问题，提出了首个专门评估多步骤工具调用轨迹中安全性的基准测试TraceSafe-Bench。论文的核心贡献在于系统性地填补了现有安全护栏（guardrails）在动态、多步工具使用轨迹中有效性评估的空白。

论文定义了12类风险类别（包括安全威胁如提示注入、隐私泄露，以及操作失败如幻觉、接口不一致等），构建了包含超过1000个独特执行实例的基准。通过评估13个LLM作为护栏的模型和7个专用安全护栏，论文得出三个关键结论：一是结构瓶颈，即护栏效能更多取决于结构数据处理能力（如JSON解析），而非语义安全对齐；二是架构优于规模，模型架构对风险检测性能的影响大于模型规模，通用LLM在轨迹分析中持续优于专用安全护栏；三是时间稳定性，即随着轨迹步骤增加，模型能利用动态执行行为提升后期风险检测性能，准确性保持稳健。

这些发现表明，要有效保障智能体工作流的安全，需要联合优化结构推理与安全对齐能力，以应对中间轨迹风险。该研究为开发更可靠的自主代理安全机制提供了重要依据和方向。
