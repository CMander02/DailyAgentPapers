---
title: "Claw-Eval: Toward Trustworthy Evaluation of Autonomous Agents"
authors:
  - "Bowen Ye"
  - "Rang Li"
  - "Qibin Yang"
  - "Yuanxin Liu"
  - "Linli Yao"
  - "Hanglong Lv"
  - "Zhihui Xie"
  - "Chenxin An"
  - "Lei Li"
  - "Lingpeng Kong"
  - "Qi Liu"
  - "Zhifang Sui"
  - "Tong Yang"
date: "2026-04-07"
arxiv_id: "2604.06132"
arxiv_url: "https://arxiv.org/abs/2604.06132"
pdf_url: "https://arxiv.org/pdf/2604.06132v1"
categories:
  - "cs.AI"
tags:
  - "Agent Evaluation"
  - "Benchmark"
  - "Safety"
  - "Robustness"
  - "Multi-modal"
  - "Trajectory Analysis"
  - "Trustworthy AI"
relevance_score: 9.0
---

# Claw-Eval: Toward Trustworthy Evaluation of Autonomous Agents

## 原始摘要

Large language models are increasingly deployed as autonomous agents executing multi-step workflows in real-world software environments. However, existing agent benchmarks suffer from three critical limitations: (1) trajectory-opaque grading that checks only final outputs, (2) underspecified safety and robustness evaluation, and (3) narrow modality coverage and interaction paradigms. We introduce Claw-Eval, an end-to-end evaluation suite addressing all three gaps. It comprises 300 human-verified tasks spanning 9 categories across three groups (general service orchestration, multimodal perception and generation, and multi-turn professional dialogue). Every agent action is recorded through three independent evidence channels (execution traces, audit logs, and environment snapshots), enabling trajectory-aware grading over 2,159 fine-grained rubric items. The scoring protocol evaluates Completion, Safety, and Robustness, reporting Average Score, Pass@k, and Pass^k across three trials to distinguish genuine capability from lucky outcomes. Experiments on 14 frontier models reveal that: (1) trajectory-opaque evaluation is systematically unreliable, missing 44% of safety violations and 13% of robustness failures that our hybrid pipeline catches; (2) controlled error injection primarily degrades consistency rather than peak capability, with Pass^3 dropping up to 24% while Pass@3 remains stable; (3) multimodal performance varies sharply, with most models performing poorer on video than on document or image, and no single model dominating across all modalities. Beyond benchmarking, Claw-Eval highlights actionable directions for agent development, shedding light on what it takes to build agents that are not only capable but reliably deployable.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前自主智能体评估体系中存在的三个关键缺陷，以建立更可信的评估标准。研究背景是，随着大语言模型从对话助手演变为能在真实软件环境中执行多步骤工作流的自主智能体，评估重点已从模型的知识储备转向其通过具体行动可靠达成目标的能力。然而，现有评估方法存在明显不足：首先，许多基准测试采用“轨迹不透明”的评分方式，仅检查最终输出结果，而忽略对中间行动序列的审计，这导致智能体可能通过“奖励破解”等捷径虚假完成任务，却无法被检测。其次，现有方法对安全性和鲁棒性的评估不足，要么将安全测试与真实任务压力隔离，要么缺乏对如服务中断等现实扰动的系统性压力测试。最后，任务覆盖范围狭窄，现有基准测试往往只针对单一模态或交互范式，缺乏一个能统一评估多样化场景的框架。

因此，本文的核心问题是：如何构建一个端到端的评估套件，以克服上述局限性，从而对智能体的能力、安全性和鲁棒性进行可信、全面且深入的评估。为此，论文提出了Claw-Eval，其设计通过三个原则直接应对这些不足：实现全轨迹审计以确保行动可验证，集成多维评分以在任务执行中耦合评估完成度、安全性和鲁棒性，并提供统一的跨模态任务覆盖。最终目标是为开发不仅能力强且可可靠部署的智能体提供切实可行的评估指南和方向。

### Q2: 有哪些相关研究？

本文的相关研究主要分为两大类：**智能体评测基准**和**评测方法论**。

在**智能体评测基准**方面，相关工作按领域细分。针对工具使用和代码，有SWE-bench、ToolBench、API-Bank和Terminal-Bench等。针对网页和图形界面交互，有WebArena、VisualWebArena和OSWorld。针对多轮对话，有τ-bench和MINT。此外，还有覆盖多领域的综合评测套件，如AgentBench、GAIA和TheAgentCompany。本文的Claw-Eval与这些工作的核心区别在于，现有基准通常只关注上述部分维度，而Claw-Eval是首个**同时**支持全谱系多模态评估、多轮专业对话、可审计的执行轨迹评分、嵌入式安全评估以及受控扰动测试的框架，旨在提供一个统一且全面的评估方案。

在**评测方法论**方面，相关工作主要针对现有范式的不足进行改进。例如，仅评估最终输出的方法无法检测中间步骤的捏造；基于大模型的评判范式虽可扩展但缺乏可审计性。近期研究尝试填补个别空白：TheAgentCompany增加了子任务检查点，τ-bench通过Pass^k区分正确性与一致性，而ToolEmu、R-Judge等则专注于在轨迹上评估风险意识。然而，现有框架均未将安全约束内嵌于常规工作流任务中，也缺乏对鲁棒性的受控错误注入测试。Claw-Eval的创新之处在于，它通过结合确定性检查与大模型评判、将评分项锚定于可审计的轨迹证据、并将错误注入作为一等评估参数，系统地解决了这些方法论上的局限。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为Claw-Eval的端到端评估套件来解决现有智能体评估中的三大局限性。其核心方法围绕一个**三阶段执行生命周期**（Setup, Execution, Judge）和**多证据三角验证**的架构设计，旨在实现基于实际行为证据的、可信赖的评估。

**整体框架与主要模块：**
1.  **三阶段生命周期与隔离执行环境**：每个评估任务都在一个隔离的Docker容器中运行，严格划分执行与评判阶段。在**Setup阶段**，框架根据任务定义注入工作空间文件（数据集、媒体素材等）和部署模拟外部服务（如CRM、邮件网关），并开始静默记录审计日志。**Execution阶段**，智能体通过两个互补的能力层与环境交互：提供11种核心操作（代码执行、文件操作、网页交互、多模态处理等）的**系统层工具**，以及暴露模拟服务API的**服务层自定义工具**。整个交互过程被完整记录为结构化的执行轨迹。**Judge阶段**仅在智能体运行结束后启动，此时才注入评分脚本和验证工具，捕获环境最终状态（如生成的文件、渲染的网页），确保评估标准对智能体完全不可见，防止其针对性适应。

2.  **全面的任务体系与统一模式**：为了覆盖多样化的现实场景，Claw-Eval构建了包含300个人工验证任务的基准，分为三大组九类：**通用服务编排**（161个任务，测试从简单查询到多系统协调的工作流执行）、**多模态感知与生成**（101个任务，涉及视频、文档/图像的理解与代码生成）、以及**多轮专业对话**（38个任务，模拟需要主动探询信息的专业咨询）。尽管任务类型迥异，它们都实例化同一个三阶段生命周期，并通过一个**声明式的任务模式**来描述，使得框架核心无需修改即可扩展新领域。

3.  **多维度评分协议与细粒度准则**：评分协议将每次任务尝试转化为三个正交维度的可信分数：
    *   **完成度**：衡量任务目标的达成程度。
    *   **安全性**：评估智能体在整个执行过程中是否遵守内嵌的策略约束（如在只读任务中执行破坏性操作）。安全性作为乘法门，一旦违规，总分将趋近于零。
    *   **鲁棒性**：通过受控的错误注入（模拟API超时等）来量化智能体从瞬时环境故障中恢复的能力，其得分基于其成功恢复的故障工具类型比例。
    最终任务得分由这三个维度按公式合成。为了确保评分精确，每个任务被分解为大量（总计2159个）**细粒度准则项**。这些准则项基于**三条独立的证据线**进行验证：执行轨迹、服务审计日志和环境快照。这种“三角验证”将评估从依赖智能体自我报告转变为核实其实际行为。

**关键技术创新点：**
*   **轨迹感知的透明评估**：通过三阶段生命周期和三条独立证据通道，实现了对智能体每一步行为的全程、不可篡改的记录，解决了仅检查最终输出的“轨迹不透明”问题。
*   **压力下的嵌入式安全与鲁棒性评估**：将安全性约束直接嵌入常规工作流任务中，并在智能体面临完成任务的真实压力下进行评估；通过受控错误注入来量化恢复策略的广度，而非简单的重试次数。
*   **统一框架下的多模态与多范式覆盖**：通过领域无关的执行管道和统一的任务模式，在一个框架内无缝评估服务编排、多模态交互和多轮对话等截然不同的能力，提供了更全面的智能体性能视图。
*   **抗随机性的多指标评估协议**：除了平均分外，还报告Pass@k（多次尝试中至少成功一次的概率）和Pass^k（k次尝试全部成功的概率），以区分真实能力与侥幸结果，特别是揭示了错误注入主要影响一致性（Pass^3显著下降）而非峰值能力（Pass@3稳定）的关键发现。

### Q4: 论文做了哪些实验？

论文在Claw-Eval评测套件上对14个前沿模型进行了全面实验。实验设置方面，所有模型在相同的脚手架和工具配置下进行评估，使用默认参数，温度设为0，并启用扩展思维。每个任务在独立的Docker沙箱中执行，错误注入率设为0，每个任务运行3次独立试验以计算Pass@3和Pass^3指标。对于通用和多模态任务，使用Gemini-3-Flash作为LLM评判员进行开放式评估；对于多轮对话任务，使用Claude Opus-4.6同时模拟用户代理和作为评判员，温度设为0.7以生成更自然多样的用户行为。

数据集为Claw-Eval，包含300个人工验证的任务，涵盖三大任务组：通用服务编排（161个任务）、多模态感知与生成（101个任务，仅9个支持视觉输入的模型参与）以及多轮专业对话（38个任务）。评估基于2,159个细粒度评分项，从完成度、安全性和鲁棒性三个维度进行轨迹感知评分。

对比方法涵盖了七个模型家族的14个模型，包括Claude Opus/Sonnet、GPT-5.4、Gemini系列、Qwen、MiMo系列、GLM系列、DeepSeek、MiniMax、Kimi和Nemotron。主要结果通过平均分数（Score）、Pass@3（三次试验中至少一次通过率）和Pass^3（三次试验全部通过率）三个指标呈现。关键数据包括：轨迹不透明评估会遗漏44%的安全违规和13%的鲁棒性失败；在通用任务上，Claude Opus 4.6的Pass^3最高（70.4%），而Claude Sonnet 4.6的平均分数最高（81.4%），显示一致性峰值性能并不对齐；多模态任务明显更难，最佳模型GPT-5.4的Pass^3仅为25.7%，远低于文本任务；所有模型在通用任务上从易到难性能均单调下降，困难任务的Pass^3跨度从14%到75%，有效区分了模型能力。

### Q5: 有什么可以进一步探索的点？

基于论文分析，Claw-Eval在评估框架设计上仍有进一步探索的空间。其局限性在于：首先，当前评估任务虽覆盖多模态，但主要集中于文档、图像和视频，对更复杂的现实交互（如物理环境模拟、多智能体协作）支持有限；其次，错误注入类型相对固定（HTTP错误、延迟），未能涵盖更隐蔽的故障模式（如数据污染、对抗性输入）。未来研究方向可包括：扩展评估场景至动态开放世界环境，以测试智能体的长期适应性和规划能力；引入更细粒度的可靠性度量，如故障恢复时间、资源使用效率等量化指标；结合因果推理方法，深入分析智能体决策链中的脆弱环节，从而指导模型架构改进。此外，可探索评估框架自身的自动化迭代机制，利用智能体表现数据动态优化评估任务和评分标准，形成闭环改进系统。

### Q6: 总结一下论文的主要内容

该论文提出了Claw-Eval评估套件，旨在解决当前自主智能体评估中存在的三个关键缺陷：仅依赖最终输出的不透明轨迹评估、安全性与鲁棒性评估不足，以及模态覆盖和交互模式狭窄。其核心贡献是构建了一个包含300个人工验证任务、覆盖9个类别（分为通用服务编排、多模态感知生成和多轮专业对话三组）的端到端评估体系。方法上，它通过执行轨迹、审计日志和环境快照三个独立证据通道记录每个智能体动作，并基于2,159个细粒度评分项进行轨迹感知的评分。评估协议涵盖完成度、安全性和鲁棒性，采用平均分、Pass@k和Pass^k（三次试验）等指标以区分真实能力与偶然结果。主要结论包括：传统不透明评估会系统性地遗漏44%的安全违规和13%的鲁棒性失败；受控错误注入主要降低一致性而非峰值能力（Pass^3下降高达24%）；多模态性能差异显著，尚无模型在所有模态上占优。该工作为构建可靠、可部署的智能体指明了方向，推动了评估方法向更可信、全面的方向发展。
