---
title: "Self-Harness: Harnesses That Improve Themselves"
authors:
  - "Hangfan Zhang"
  - "Shao Zhang"
  - "Kangcong Li"
  - "Chen Zhang"
  - "Yang Chen"
  - "Yiqun Zhang"
  - "Lei Bai"
  - "Shuyue Hu"
date: "2026-06-08"
arxiv_id: "2606.09498"
arxiv_url: "https://arxiv.org/abs/2606.09498"
pdf_url: "https://arxiv.org/pdf/2606.09498v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "Self-Improvement"
  - "Harness Design"
  - "Weakness Mining"
  - "Agent Architecture"
  - "Test-Time Adaptation"
  - "Model-Specific Optimization"
relevance_score: 8.5
---

# Self-Harness: Harnesses That Improve Themselves

## 原始摘要

The performance of LLM-based agents is jointly shaped by their base models and the harnesses that mediate their interaction with the environment. Because different models exhibit distinct behaviors, effective harness design is inherently model-specific. Yet agent harnesses are still largely engineered by human experts, a paradigm that scales poorly as modern LLMs become increasingly diverse and rapidly evolving. In this paper, we introduce Self-Harness, a new paradigm in which an LLM-based agent improves its own operating harness, without relying on human engineers or stronger external agents. We operationalize Self-Harness as an iterative loop with three stages: Weakness Mining, which identifies model-specific failure patterns from execution traces; Harness Proposal, which generates diverse yet minimal harness modifications tied to these failures; and Proposal Validation, which accepts candidate edits only after regression testing. We instantiate Self-Harness on Terminal-Bench-2.0 using a minimal initial harness and three base models from diverse families: MiniMax M2.5, Qwen3.5-35B-A3B, and GLM-5. Across all three models, Self-Harness consistently improves performance, with held-out pass rates increasing from 40.5% to 61.9%, 23.8% to 38.1%, and 42.9% to 57.1%, respectively. Qualitative analyses further show that Self-Harness does not simply add generic instructions, but effectively turns model-specific weaknesses into concrete, executable harness changes. These results suggest a path toward LLM-based agents that are not merely shaped by their harnesses, but can also participate in reshaping them.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决 LLM 智能体“操作框架”（harness）设计高度依赖人类专家的可扩展性问题。研究背景在于，LLM 智能体的实际表现不仅由其基础模型决定，还深受其操作框架——包括系统提示、工具、运行时机制、验证规则和故障恢复流程等——的影响。然而，当前的主流范式仍依赖人类专家为不同模型手工设计适配的框架。随着 LLM 家族日益多样且快速迭代，这种人工范式成本高昂且难以持续，因为不同模型在行为模式、工具使用习惯和错误类型上展现出巨大差异，一套框架很难通用。

现有方法（如 Meta-Harness）依赖更强外部模型来指导弱模型框架的改进，但这种方式成本高，且对于顶尖的闭源模型可能无法获取。本文提出的核心问题是：**能否让 LLM 智能体不依赖人类或更强的外部智能体，自我改进其运行所依赖的操作框架**？即，让智能体自身成为一个能够识别自身错误模式、生成针对性框架修改，并通过回归测试自我验证的闭环系统。这旨在将框架的适配与进化过程内化到目标智能体本身，从而提升智能化与扩展性。

### Q2: 有哪些相关研究？

根据该论文的相关工作部分，相关研究可以分为以下几类：

1. **提示工程与智能体框架**：这类研究关注如何通过指令、示例、记忆、工具状态等控制智能体行为。例如，ReAct、SWE-agent、Claude Code和SemaClaw/OpenClaw等框架展示了环境机制如何塑造长程智能体行为。本文将这些机制统称为“约束系统”（harness），并认为许多重要失败是约束系统层面而非孤立模型响应的失败。

2. **自我改进智能体与自动化智能体设计**：一类工作研究系统如何随时间调整输入、记忆或工作流程，如Reflexion存储口头反馈、智能体语境工程演化上下文、STOP研究代码生成的递归自我改进。这些方法仅调整响应策略、记忆或生成程序，而非约束系统状态。另一类工作从外部优化智能体设计，如自动化智能体系统设计、可优化图表示的语言智能体、直接优化约束代码的Meta-Harness。本文与这类自动化约束优化及自我改进文献最接近，但区别在于：本文研究同一固定模型在当下约束系统下，能否针对影响自身未来行为的约束系统提出有限的候选修改，而不是依赖外部搜索或优化过程。

3. **科学发现与自我演化智能体系统**：如The AI Scientist、AI Scientist-v2、AlphaEvolve、Alita、Godel Agent和Darwin Godel Machine等，它们实现更广泛的研究或算法设计循环。本文在精神上与之相似，但研究更受控的设定。

### Q3: 论文如何解决这个问题？

Self-Harness 通过一个迭代循环让 LLM 智能体自主改进其操作框架，无需人类专家或外部强模型。整体框架由三个核心阶段构成，每次迭代都遵循“评估-分析-提议-验证”流程：

1. **弱点挖掘**：在初始框架下运行固定模型，将失败任务的执行轨迹收集起来。通过与验证器关联的失败签名（包括验证器级原因、智能体行为因果状态和抽象机制）对失败进行聚类，形成结构化的证据包。此过程将零散失败转化为可复现的、可归因的弱点模式，为后续改进提供精确目标。

2. **框架提议**：使用同一固定模型作为提议者，基于证据包并行生成K个多样且最小的候选修改。每个提议必须针对特定失败机制，修改具体的编辑面（如指令、工具、记忆机制），并且保持各分支间在目标、面或假设上的多样性。提案中保留了无关行为，避免重写整体控制架构。

3. **提案验证**：对每个候选框架在保留集和未见集上进行回归测试。只有同时满足两项性能不退化且至少一项提升的候选才会被接受。这一保守规则防止了过拟合和性能权衡。被接受的修改会被合并进当前框架，组成新版本，而拒绝的提案被记录但不影响活动框架。整个过程中模型权重和评估器保持不变。

创新点在于首次提出智能体通过分析自身执行证据来改进周围框架，而非修改内部参数。关键设计包括验证器锚定的失败聚类保证了证据的客观性和可归因性，并行提议机制平衡了探索性与可解释性，而双集验证规则则确保了改进的鲁棒性。

### Q4: 论文做了哪些实验？

论文在Terminal-Bench-2.0基准上评估Self-Harness，该基准包含89个容器化终端任务，实验使用64个稳定任务的固定子集（排除依赖不稳定外部资源或多模态输入的任务）。模型选用三个不同系列：MiniMax M2.5、Qwen3.5-35B-A3B和GLM-5，所有比较均为模型内对比——仅允许修改harness，保持解码配置、工具集、预算和评估器不变。初始harness基于DeepAgent SDK，仅包含最小系统提示和默认文件系统/Shell工具，可修改接口包括指令、工具和验证指导等声明点。任务集预先划分为held-in分片（用于暴露失败证据给提议者）和held-out分片（仅用于回归门验收），每个harness候选评估两次。

主要结果：对所有三个模型，Self-Harness在held-in和held-out分片上都一致提升通过率。MiniMax M2.5: held-in从43.0%提升至50.0%（+16%相对增益），held-out从40.5%提升至61.9%（+53%相对增益）。Qwen3.5: held-in从15.1%提升至36.0%（+138%相对增益），held-out从23.8%提升至38.1%（+60%相对增益）。GLM-5: held-in从47.7%提升至57.0%（+20%相对增益），held-out从42.9%提升至57.1%（+33%相对增益）。所有提升均未以降低任一分为代价。定性分析显示，编辑并非添加通用指令，而是针对模型特定故障模式：M2.5强调早期工件创建和内容标签正确格式；Qwen3.5增加依赖预检、重试纪律和工具错误触发的恢复机制；GLM-5则使环境更改跨shell会话持久化并促进从探索转向实现。

### Q5: 有什么可以进一步探索的点？

Self-Harness在固定基准和有限编辑空间内验证了自改进的有效性，但其局限性与未来方向同样清晰。首要局限是当前协议依赖“通过率不退化”作为接受门控，这仅适用于低风险修改，面对涉及提示注入、工具链重构等高风险调整时，需要更稳健的验证机制，例如对抗性测试或安全约束检查。其次，弱项挖掘阶段的质量高度依赖执行轨迹的全面性与验证器输出的准确性，未来可引入更细粒度的错误归因技术，例如通过模型注意力或梯度信息识别具体推理环节的瓶颈。此外，当前迭代可能过度拟合基准中的失败模式，导致泛化性不足，一个可能的改进方向是引入多样性奖励或域外验证集以抑制过拟合。最后，未来工作应探索将该范式扩展至更开放的环境，如多智能体协作或动态工具调用场景，其中“可编辑的束具表面”定义本身也可能需要模型参与构建，形成元级别的自改进循环。

### Q6: 总结一下论文的主要内容

这篇论文研究了固定的大语言模型能否自主改进控制其智能体行为的“操控框架”（harness）。核心贡献在于提出了Self-Harness范式，让智能体无需人类工程师或更强的外部模型，通过一个迭代循环（弱点挖掘、框架修改生成、修改验证）自我优化。该方法首先从执行轨迹中挖掘模型特定的失败模式，然后生成针对性的、最小化的框架修改，最后通过回归测试过滤出可行的编辑。在Terminal-Bench-2.0上对三种不同模型（MiniMax M2.5、Qwen3.5-35B-A3B、GLM-5）的测试表明，Self-Harness能持续提升性能，留存率分别从40.5%提升至61.9%、23.8%至38.1%、42.9%至57.1%。研究证明，当修改提案受限于执行证据并通过回归测试验证时，即使是稀疏的初始框架也能支持有效的自我完善。该工作的意义在于，它指出了智能体操控框架应被视为可通过经验状态变迁来持续演化的实体，为智能体的自主进化开辟了新路径。
