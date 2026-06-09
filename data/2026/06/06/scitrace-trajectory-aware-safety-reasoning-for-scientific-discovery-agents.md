---
title: "SciTrace: Trajectory-Aware Safety Reasoning for Scientific Discovery Agents"
authors:
  - "Tanush Swaminathan"
  - "Runmin Jiang"
  - "Letian Zhang"
  - "Min Xu"
date: "2026-06-06"
arxiv_id: "2606.08234"
arxiv_url: "https://arxiv.org/abs/2606.08234"
pdf_url: "https://arxiv.org/pdf/2606.08234v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent Safety"
  - "Scientific Discovery Agent"
  - "Safety Reasoning"
  - "Multi-step Tool Use"
  - "Agent Framework"
  - "Compositional Risk"
  - "Trajectory-Aware Verification"
  - "Safety-Intrinsic Reasoning"
relevance_score: 8.5
---

# SciTrace: Trajectory-Aware Safety Reasoning for Scientific Discovery Agents

## 原始摘要

LLM-based scientific agents have shown strong capacity for autonomous research, yet their safety layers remain structurally divorced from core reasoning: they inspect pipeline outputs rather than shaping the deliberation that produces them. This separation opens two failure modes: safety signals accumulated at one stage are discarded before the next, and sequences of individually benign tool calls can compose into harmful outcomes that no single-step filter detects. To address these challenges, we introduce \textbf{SciTrace}, a framework that weaves safety reasoning into every stage of the scientific agent pipeline. SciTrace couples two complementary mechanisms: a \textit{Safety-Intrinsic Reasoning Loop} (SIR) that maintains a cumulative risk state across the Thinker, Experimenter, Writer, and Reviewer stages through joint task-and-safety deliberation, and a \textit{Compositional Tool-Chain Verifier} (CTV) that performs trajectory-aware safety checks before execution, catching risks that surface only across multi-step tool sequences. Evaluated on 240 high-risk research tasks and 120 tool-related risk tasks spanning six scientific domains, SciTrace achieves state-of-the-art (\textbf{SOTA}) safety among compared frameworks across four backbone models: it consistently improves tool call safety and adversarial robustness while preserving scientific output quality, and it uncovers \textbf{78.8\%} of the compositional tool-chain escapes that single-step monitors miss. The project website is available at https://opensciagent.github.io/SciTrace/.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

当前基于大语言模型的科学发现智能体（如SafeScientist）虽能自主完成研究，但其安全机制与核心推理过程是结构分离的，仅作为管道输出的外部过滤器。这种架构存在两个关键缺陷：一是风险信号是阶段局部的，一个阶段（如思考器）检测到的危险研究方向不会传播到后续阶段（如实验器或写作器），导致安全警告在阶段间丢失；二是单步监控无法检测组合风险——多个单独无害的工具调用（如先检索病原体基因组序列，再查询抗生素耐药性数据库）可能构成双用途研究轨迹，但步级过滤器无法识别。本文提出的SciTrace框架旨在解决上述问题，通过将安全推理内嵌于智能体推理过程，实现轨迹感知的安全决策。

### Q2: 有哪些相关研究？

该论文的相关工作主要可分为以下几类：

1. **安全对齐与基础方法**：包括RLHF、Constitutional AI等训练阶段注入安全偏好的方法，以及LLaMA Guard等输入-输出分类器。本文指出这些方法针对短上下文场景，无法处理多阶段Agent管线中安全上下文累积的问题。

2. **Agent安全框架**：AGrail通过记忆增强的分析器-执行器循环自适应生成安全检查；ToolSafe提出TS-Guard（三子任务验证器）和TS-Flow（反馈驱动纠正）。本文吸收了AGrail的基于记忆的检查生成和ToolSafe的轨迹感知验证，将其适配到科学Agent场景，但强调这些工作未涉及科学管线中跨阶段安全状态的显式传播。

3. **AI科学家系统**：AI Scientist展示了端到端自主研究生成，后续工作扩展了文献综述和超参数搜索。SafeScientist首次系统性地针对AI科学家管线提出安全防御，并构建了SciSafetyBench基准。本文直接基于SafeScientist的管线与基准构建内在安全推理，核心区别在于将安全推理嵌入每个推理阶段而非仅作为后处理过滤。

本文的主要贡献在于提出了在科学Agent管线中集成跨阶段安全状态传播与组合工具链验证的框架。

### Q3: 论文如何解决这个问题？

SciTrace通过两个紧密耦合的组件将安全推理嵌入科学发现流水线的每个阶段。核心方法是**安全内蕴推理循环（SIR）**和**组合工具链验证器（CTV）**，它们共享一个跨阶段累积风险状态。

SIR在流水线的四个阶段（思考者、实验者、写作者、审阅者）转换时运行，执行联合任务与安全推理。它接收三个输入：当前阶段任务内容、累积风险状态和从安全记忆模块检索的历史检查记录，输出五级风险等级（安全、低风险、警告、高风险、阻止）及行动建议。每个阶段使用定制提示聚焦相关风险：思考者关注双重用途潜力，实验者关注工具协议安全，写作者关注信息披露，审阅者进行最终伦理评估。SIR支持经验积累式的记忆感知检查生成，并应用类别对交互升级（如双重用途与危险合成同时出现时风险等级自动提升）。

CTV在工具调用执行前通过验证代理进行拦截，在完整调用轨迹上下文中评估会话的三维度风险：请求危害性、组合风险（当前调用与历史调用形成的危险轨迹）和工具调用安全性。组合风险检测的核心创新在于能捕捉单步检查无法发现的跨多步工具调用的组合性危险（如步分离的DNA合成与毒力基因构建）。CTV输出允许、修改或阻止三级动作，当修改或阻止时会生成建设性替代方案而非简单终止。所有CTV信号同样写入共享累积风险状态，确保风险信息在后续阶段持续可见。通过将安全推理从外部过滤器转变为内生于流水线每个决策点的推理过程，SciTrace实现了跨阶段上下文保持（78.8%组合工具链逃逸检出率）和渐进式风险累积，在240项高风险任务和120项工具相关风险任务中达到四个骨干模型上的最新安全水平。

### Q4: 论文做了哪些实验？

论文在SciSafetyBench基准上进行了系统实验，该基准包含240个高风险科研任务和120个工具相关任务，覆盖物理、化学、生物、材料、信息科学和医学六个领域，任务按恶意、隐蔽危害、意外后果和多步工具轨迹四种风险类型均衡标注。对比方法包括裸LLM、SafeScientist（四层防御管线）、六个AI科学家基线框架（AI Scientist、CycleResearcher等）以及SciTrace（在SafeScientist基础上增加SIR和CTV）。使用Llama-3.1-70B、Qwen2.5-72B、DeepSeek-V3和GPT-4o四种骨干模型评估。主要指标包括安全分数（1-5）、拒绝率（%）、工具调用安全率（%）和组合风险检测率（%）。结果显示SciTrace在所有骨干模型上取得SOTA安全性能，例如在Qwen2.5-72B上安全分数达4.89，拒绝率93%，工具安全率92.5%。消融实验表明SIR和CTV独立贡献，组合最优。CTV能检测78.8%的单步监视器遗漏的组合工具链风险，在生物和化学领域增益最大（+17.3和+17.2个百分点）。面对五种对抗攻击策略，SciTrace的平均防御成功率比SafeScientist高26.1个百分点。

### Q5: 有什么可以进一步探索的点？

SciTrace在推理开销、评估方法和领域覆盖上存在明显局限。首先是推理延迟问题，尽管可以通过批处理和缓存优化，但这种架构性开销本质上是将安全机制嵌入推理流程的代价。其次，依赖GPT-4o作为安全判官存在领域偏差，尤其是在材料科学和物理领域，这提示我们需要建立更鲁棒的、多模型共识的安全校准机制。最值得深入探索的是安全记忆检索的语义鸿沟：当前基于关键词匹配的检索在面对“神经毒剂前体”与“有机磷酸酯合成”这类同义但异形的表述时可能完全失效。作为改进方向，我建议引入稠密向量检索与动态知识图谱相结合的双通道记忆架构，既能捕捉语义相似性，又能维护化学物质与操作间的高阶推理关系。此外，当前S9形式的组合子任务设计偏向物理合成场景，对于信息科学中跨API的隐私数据重构等抽象风险识别率较低，应将安全约束泛化到S4/S6等更抽象的行为模式，覆盖数据流和身份推理场景。最终目标应是构建一个能自主进化安全策略的系统，而不仅仅是被动验证已知风险模式。

### Q6: 总结一下论文的主要内容

论文提出了SciTrace框架，旨在解决基于大语言模型的科学智能体在安全性与核心推理过程结构性分离的问题。传统方法仅在流水线末端检测输出，导致两个缺陷：跨阶段安全信号丢失，以及多个独立无害工具调用组合成有害结果。SciTrace通过两个机制应对：安全内禀推理循环（SIR）在思考者、实验者、写作者和审阅者阶段维护累积风险状态，实现联合任务与安全推理；组合工具链验证器（CTV）在执行前对多步工具序列进行轨迹感知安全检查。在涵盖六个科学领域的240项高风险研究任务和120项工具相关风险任务上，SciTrace在四种骨干模型上达到最先进安全性，工具调用安全率提升14.3个百分点，对抗拒绝率平均提升24.7个百分点，并检测出78.8%的单步监控遗漏的组合工具链逃逸。该工作表明安全应作为多阶段智能体的架构性选择而非事后补救。
