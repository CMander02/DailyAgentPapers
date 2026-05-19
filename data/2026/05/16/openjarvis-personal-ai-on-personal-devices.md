---
title: "OpenJarvis: Personal AI, On Personal Devices"
authors:
  - "Jon Saad-Falcon"
  - "Avanika Narayan"
  - "Robby Manihani"
  - "Tanvir Bhathal"
  - "Herumb Shandilya"
  - "Hakki Orhun Akengin"
  - "Gabriel Bo"
  - "Andrew Park"
  - "Matthew Hart"
  - "Caia Costello"
  - "Chuan Li"
  - "Christopher Ré"
  - "Azalia Mirhoseini"
date: "2026-05-16"
arxiv_id: "2605.17172"
arxiv_url: "https://arxiv.org/abs/2605.17172"
pdf_url: "https://arxiv.org/pdf/2605.17172v1"
github_url: "https://github.com/openjarvis/openjarvis"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CL"
tags:
  - "个人AI智能体"
  - "设备端Agent"
  - "Agent架构"
  - "本地模型"
  - "云-端协作"
  - "Agent优化"
  - "低延迟"
  - "成本效率"
relevance_score: 8.5
---

# OpenJarvis: Personal AI, On Personal Devices

## 原始摘要

Personal AI stacks, like OpenClaw and Hermes Agent, are becoming central to daily work, yet they route nearly every query (often over sensitive local data) to cloud-hosted frontier models. Replacing frontier models with local models inside existing stacks does not work: swapping Claude Opus 4.6 for Qwen3.5-9B drops accuracy by 25-39 pp across personal AI tasks like PinchBench and GAIA. Existing stacks bundle agentic prompts, tool descriptions, memory configuration, and runtime settings around a specific cloud model. Only the prompts can be tuned, and state-of-the-art prompt optimizers close just 5 pp of the local-cloud gap on their own. This motivates a decomposed personal AI stack: one that exposes individual primitives which can be optimized individually or jointly to close the local-cloud gap. We present OpenJarvis, an architecture that represents a personal AI system as a typed spec over five primitives: Intelligence, Engine, Agents, Tools & Memory, and Learning. Each primitive is an independently editable field, making the stack end-to-end optimizable and measurable against accuracy, cost, and latency. Towards closing the local-cloud gap without surrendering local-model properties, OpenJarvis introduces LLM-guided spec search, a local-cloud collaboration in which frontier cloud models propose edits across the spec at search time, only non-regressing edits are accepted, and the resulting spec runs entirely on-device at inference time. With LLM-guided spec search, on-device specs match or exceed cloud accuracy on 4 of 8 benchmarks and land within 3.2 pp of the best cloud baseline on average. They also reduce marginal API cost by ~800x and end-to-end latency by 4x.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决个人AI系统在隐私、成本与性能之间的核心矛盾。当前主流的个人AI栈（如OpenClaw、Hermes Agent）虽已融入日常工作，但其设计几乎完全依赖云端前沿模型来路由所有查询（包括敏感的个人数据），导致用户面临每年数千美元的API订阅费用、数据暴露给第三方服务器、依赖网络连接以及缺乏模型所有权等问题。尽管消费级硬件已能运行开源模型，但将它们直接替换进现有框架效果很差：例如将Claude Opus替换为Qwen3.5-9B会在PinchBench和GAIA等任务上导致25-39个百分点的精度下降。现有栈是围绕特定云端模型“捆绑”设计的，其中智能体提示、工具描述、内存配置和运行时设置高度耦合，只有提示可以微调，而最先进的提示优化器也仅能缩小约5个百分点的局部-云端差距。因此，本文旨在解决的核心问题是：如何设计一个可端到端优化的、分解式的个人AI架构，使得完全在设备端运行的模型能够在关键的个人AI基准测试中，在准确性上匹敌或接近云基线，同时大幅降低成本和延迟，从而在不牺牲本地模型固有的隐私和效率属性的前提下，弥合本地模型与云端前沿模型之间的巨大性能鸿沟。

### Q2: 有哪些相关研究？

相关研究可分为以下几类：

1. **智能代理与工具（个人AI堆栈）**：如OpenClaw、Hermes Agent、LangChain、CrewAI、Google ADK、OpenAI Symphony、Qwen-Agent等。这些框架将Agents和Tools作为可配置层，但将Intelligence、Engine和Learning绑定到特定云端模型，因此替换为本地模型会导致性能大幅下降。苹果智能和Gemini Nano等封闭系统则进一步将Engine硬编码为专有运行时，且不提供Learning接口。本文的OpenJarvis通过将堆栈解耦为五个独立原语，解决了这一耦合问题。

2. **引擎与智能（本地推理工具）**：如Ollama、llama.cpp、LM Studio、LocalAI等推理运行时，以及量化（GPTQ、AWQ）、推测解码、硬件感知服务（MLC-LLM、ExecuTorch、vLLM）等优化，还有MobileLLM、Gemma 3n等端侧架构。这些工具仅形式化Engine和Intelligence，缺乏Agents、Tools和Learning。OpenJarvis的Engine抽象了这些后端，并内置能耗和成本遥测，扩展了本地与云端查询路由决策。

3. **优化方法（学习）**：包括权重优化（知识蒸馏、LoRA、QloRA、GRPO）、提示和智能体优化（DSPy、ACE、GEPA）、推理时协作（Minions、Advisor Models）。这些方法每次只针对一个原语（如Intelligence或Agents），而OpenJarvis通过LLM引导的规格搜索，将Learning作为优化器，联合优化四个可编辑原语，实现了互补而非替代。

4. **联合评估**：现有工具（Zeus、AI Energy Score、MLCommons）仅测量单个原语的单一维度，而GAIA、SWE-bench等基准仅报告准确率且假设无限云端算力。OpenJarvis的规格提供了完整配置的公共表示，首次实现了跨五个原语的准确率、能耗、延迟、功耗和成本联合评估。

### Q3: 论文如何解决这个问题？

为了弥合本地模型与云端模型在个人AI任务上的性能差距，OpenJarvis提出了一种分解式架构和一种联合优化方法。其核心是将传统的捆绑式AI堆栈显式解耦为五个独立的原语（Primitives）：**Intelligence**（模型与参数）、**Engine**（推理运行时）、**Agents**（代理逻辑与提示词）、**Tools & Memory**（工具接口与记忆）以及**Learning**（优化器）。这五个原语被打包成一个可版本化、可共享的**规格（Spec）**，这是一个类型化的配置对象，使得堆栈的每一个组件都可以独立编辑和端到端优化。

针对本地模型性能瓶颈，论文引入了关键创新方法——**LLM引导的规格搜索（LLM-guided spec search）**。这是一种本地-云端协作的优化机制：在**搜索阶段**，利用强大的前沿云端模型（作为教师）分析本地模型的失败轨迹，识别失败模式集群（failure clusters），并跨多个原语（如同时修改工具描述和Agent提示词）生成候选编辑方案。随后，只有通过“**门控（Gate）**”验证（即能针对性修复目标失败且不导致其他领域严重倒退）的编辑方案才会被采纳。而在**推理阶段**，优化后的完整规格完全在本地设备上运行，不依赖云端模型。该架构通过将“云端提方案、本地做验证和执行”的角色分离，实现了在不牺牲本地模型低延迟和零边际API成本特性的前提下，系统性、多维度地优化整个个人AI系统。

### Q4: 论文做了哪些实验？

论文进行了广泛的实验来评估OpenJarvis架构及其LLM-guided spec search方法。实验设置包括：使用PinchBench和GAIA等个人AI任务基准测试，对比方法包括使用云端前沿模型（如Claude Opus 4.6）的现有堆栈、使用本地模型（如Qwen3.5-9B）直接替换的堆栈，以及单独使用提示优化器（如DSPy）的配置。主要结果显示，直接在现有堆栈中用本地模型替换云端模型会导致平均准确率下降25-39个百分点。单独使用提示优化器只能弥补约5个百分点的差距。而OpenJarvis的LLM-guided spec search方法，通过联合优化Intelligence、Engine、Agents、Tools & Memory四个原语，使本地设备上的spec在8个基准测试中的4个上匹配或超过云端准确率，平均仅比最佳云端基线低3.2个百分点。此外，该方法还实现了边际API成本降低约800倍，端到端延迟降低4倍。实验还评估了能量、功率和硬件成本等效率指标，展现了完整的Pareto结构分析。

### Q5: 有什么可以进一步探索的点？

OpenJarvis通过分解个人AI系统为五个独立原语并引入LLM引导的规范搜索，显著缩小了本地模型与云端模型之间的性能差距。然而，当前方法仍存在若干局限和未来探索方向：首先，LLM引导的规范搜索依赖云端前沿模型来提议编辑，这本身引入了云端依赖，未来可探索完全自主的本地规范探索与进化机制；其次，原语之间的耦合优化尚未被充分利用，例如“日志学习”原语与“工具”原语可能需要在运行时动态调整，而非仅在搜索阶段联合优化；此外，当前评估仅覆盖有限基准任务，对更复杂、多步骤、长期依赖的个性化场景（如日常助手、持续学习）的适用性需进一步验证。一个可能的改进思路是引入元学习框架，让设备端模型根据用户行为反馈持续微调原语选择策略，从而实现从静态规范搜索到动态自适应演进的转变。

### Q6: 总结一下论文的主要内容

OpenJarvis旨在解决个人AI系统依赖云端大模型带来的隐私、成本和延迟问题。现有系统将云端模型与复杂prompt、工具描述等深度绑定，直接替换为本地模型会导致PinchBench和GAIA等基准任务准确率骤降25-39个百分点，且仅优化prompt只能弥补5个百分点。为此，论文提出一种可分解的个人AI架构，将系统定义为五个可独立编辑的原语：智能体（模型与权重）、引擎（推理运行时）、代理（推理循环）、工具与记忆、以及学习优化器。核心创新是“大模型引导的规格搜索”算法，在搜索阶段利用云端前沿模型诊断失败原因并跨原语提出协同编辑，仅接受在保留集上无退化的修改，最终使推理阶段完全运行在本地设备。实验表明，优化后的本地规格在8个基准测试中有4个匹配或超越云端基线，平均差距仅3.2个百分点，同时边际API成本降低约800倍，端到端延迟降低4倍。该工作首次证明了本地设备可承载与云端竞争的个人AI核心能力。
