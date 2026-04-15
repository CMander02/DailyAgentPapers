---
title: "Modality-Native Routing in Agent-to-Agent Networks: A Multimodal A2A Protocol Extension"
authors:
  - "Vasundra Srinivasan"
date: "2026-04-14"
arxiv_id: "2604.12213"
arxiv_url: "https://arxiv.org/abs/2604.12213"
pdf_url: "https://arxiv.org/pdf/2604.12213v1"
github_url: "https://github.com/vasundras/modality-native-routing-a2a-protocol"
categories:
  - "cs.AI"
tags:
  - "多智能体系统"
  - "多模态"
  - "通信协议"
  - "路由机制"
  - "基准测试"
  - "架构设计"
relevance_score: 8.0
---

# Modality-Native Routing in Agent-to-Agent Networks: A Multimodal A2A Protocol Extension

## 原始摘要

Preserving multimodal signals across agent boundaries is necessary for accurate cross-modal reasoning, but it is not sufficient. We show that modality-native routing in Agent-to-Agent (A2A) networks improves task accuracy by 20 percentage points over text-bottleneck baselines, but only when the downstream reasoning agent can exploit the richer context that native routing preserves. An ablation replacing LLM-backed reasoning with keyword matching eliminates the accuracy gap entirely (36% vs. 36%), establishing a two-layer requirement: protocol-level routing must be paired with capable agent-level reasoning for the benefit to materialize.
  We present MMA2A, an architecture layer atop A2A that inspects Agent Card capability declarations to route voice, image, and text parts in their native modality. On CrossModal-CS, a controlled 50-task benchmark with the same LLM backend, same tasks, and only the routing path varying, MMA2A achieves 52% task completion accuracy versus 32% for the text-bottleneck baseline (95% bootstrap CI on $Δ$TCA: [8, 32] pp; McNemar's exact $p = 0.006$). Gains concentrate on vision-dependent tasks: product defect reports improve by +38.5 pp and visual troubleshooting by +16.7 pp. This accuracy gain comes at a $1.8\times$ latency cost from native multimodal processing. These results suggest that routing is a first-order design variable in multi-agent systems, as it determines the information available for downstream reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体系统中跨模态通信的信息保真度问题。研究背景是当前基于Agent-to-Agent（A2A）协议的多智能体系统在交互时，普遍采用“文本瓶颈”流水线，即将所有模态信息（如语音、图像）序列化为文本进行传递。这种做法虽然简化了协议处理，却丢弃了原始模态中的关键感知信号（如语音的韵律特征、图像的空间细节），导致下游智能体进行跨模态推理时，只能基于信息量受限的文本描述，从而限制了决策准确性。

现有方法的不足在于，尽管A2A协议本身原生支持多模态数据（如音频、图像部分），但实际部署中并未充分利用这一特性。文本瓶颈流水线造成了信息退化，而简单地转向模态原生路由（即尽可能以原始模态转发数据）是否足够，此前并不明确。论文通过实验揭示了一个关键局限：仅改进协议层的路由方式，若下游智能体不具备相应的深度推理能力（例如仅使用关键词匹配等简单启发式方法），则无法利用路由带来的丰富上下文信息，因此性能提升无法实现。

本文要解决的核心问题是：如何通过协同设计协议层的路由机制与智能体层的推理能力，以有效保留和利用多模态信号，从而显著提升多智能体系统的任务完成准确率。为此，论文提出了MMA2A这一轻量级架构层，它基于A2A协议中已有的智能体能力声明（Agent Card），在调度时实现模态感知的原生路由，同时强调必须与具备强大推理能力（如基于LLM）的智能体相结合，才能将信息保真度的优势转化为实际性能增益。论文通过可控实验验证了这种两层需求的必要性，并量化了模态原生路由在特定任务上带来的显著精度提升及其伴随的延迟成本。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及多智能体通信协议、多模态处理框架以及多智能体协同系统等类别。

在**多智能体通信协议**方面，论文提及了A2A、MCP、ACP和ANP等新兴协议。其中，A2A是本文工作的基础协议，其定义的`FilePart`类型已原生支持多模态载荷，但实践中未被充分利用。Ehtesham等人的研究提出了一个包含MCP和ACP的阶段性采用路线图。本文则证明，通过利用A2A现有的`FilePart`和智能体卡片功能，无需ACP作为中介即可实现多模态通信。Li等人提出的LACP协议专注于会话管理，与本文研究的模态路由问题不同。

在**多模态处理与智能体框架**方面，AgentMaster框架虽然结合了A2A和MCP，但其多模态支持以文本为主导，图像分析由单一工具处理，而非通过原生图像部件进行对等智能体通信。本文的MMA2A架构则强调模态原生路由。同时，以GPT-4o、Gemini为代表的现代多模态大模型虽能统一处理多种模态，但本文关注的是由多个异构、单模态专长智能体组成的分布式系统，这更符合企业多团队、多供应商的部署场景。

在**多智能体协同与评测**方面，现有的多智能体编排框架（如AutoGen、CrewAI）和关于可扩展性的研究通常假设纯文本负载。现有的多模态基准（如MM-Bench、MMMU）主要评估单一模型的能力，而非分布式协议下的模态路由问题。本文的研究恰恰填补了这一空白，在由协议介导的多智能体、多模态系统中，量化了纯文本路由带来的准确性成本。

### Q3: 论文如何解决这个问题？

论文通过提出并实现MMA2A（多模态A2A）架构层来解决跨智能体网络中模态信息在路由过程中丢失的问题。其核心方法是摒弃将所有非文本模态强制转换为文本的“文本瓶颈”基线做法，转而采用**模态原生路由**，确保音频、图像等数据以其原始格式被直接路由至具备相应处理能力的下游智能体，从而为最终的综合推理步骤保留更丰富、更高保真度的上下文信息。

整体系统架构建立在标准A2A基础设施之上，包含四个关键组件，形成分层设计：
1.  **模态感知路由器**：这是一个轻量级代理（<500行Python代码），作为核心创新模块。它拦截出站的A2A任务调用，通过检查目标智能体的“智能体卡片”中声明的输入/输出模式能力，为消息的每个部分选择最优的编码和路由路径。其路由决策规则形式化如下：若目标智能体声明支持某原始模态，则直接路由原生数据；否则，才将其转码为文本。该路由器还通过缓存智能体卡片来优化性能。
2.  **异构智能体池**：包含三个由相同LLM后端支持的专用智能体，以确保实验对比的公平性。
    *   **语音智能体**：声明支持音频格式，直接处理原始音频以进行转录、情感分析等。
    *   **视觉智能体**：声明支持图像格式，直接处理原始图像以进行视觉检测、缺陷识别等。
    *   **文本智能体**：专门处理文本部分，负责知识检索、决策综合等。
3.  **任务编排器**：负责分解输入的跨模态任务，通过MAR将子任务并行分派给相应智能体，并收集结果进行最终合成。

该方案的关键技术与创新点在于：
*   **协议级创新**：无需修改A2A协议本身，而是巧妙地利用现有特性实现——利用“智能体卡片”进行能力发现，使用`FilePart`携带原生模态数据，并利用流式传输支持交互。
*   **两层收益机制**：论文明确指出，模态原生路由的优势（任务准确率提升20个百分点）只有在与强大的智能体级推理（本工作中为LLM）结合时才能显现。若下游推理能力不足，则收益消失。
*   **可控的实验设计**：通过保持后端LLM模型、任务集不变，仅改变路由路径，清晰地将性能提升归因于路由策略本身，而非模型能力差异。

因此，论文通过设计一个轻量级、非侵入式的路由中间件，实现了信息流的最优规划，将多模态信号的保真度从协议层面贯穿至推理层面，最终显著提升了复杂任务的完成准确率。

### Q4: 论文做了哪些实验？

论文在统一的实验设置下进行了对比实验和消融实验，以评估所提出的MMA2A架构。所有智能体均作为独立的A2A兼容HTTP服务在同一台机器上运行，并统一使用Gemini 2.5 Flash模型作为后端。实验在CrossModal-CS基准上进行，这是一个包含50个任务的受控基准，任务分为产品缺陷报告、视觉故障排除、装配指导和保修索赔四类。

**对比方法与主要结果：**
论文比较了两种配置：1) **MMA2A（所提方法）**：采用模态原生路由，将音频和图像部分以原生格式（如.wav, .png）直接路由给相应的语音和视觉智能体。2) **Text-BN（文本瓶颈基线）**：强制将所有非文本部分转码为文本描述后再路由，代表了当前主流的部署模式。两种配置使用完全相同的模型、知识库和任务逻辑，唯一区别在于路由策略。

主要评估指标是任务完成准确率（TCA）。实验结果显示，MMA2A的TCA达到52.0%，而Text-BN仅为32.0%，绝对提升了20个百分点（95%置信区间为[8, 32] pp）。McNemar精确检验p值为0.006，表明差异显著。这种准确率提升以延迟增加为代价：MMA2A的平均端到端延迟为13.04秒，是Text-BN（7.19秒）的约1.8倍。带宽开销可忽略不计（+0.5%）。

**关键数据指标：**
*   **总体TCA**：MMA2A为52.0%，Text-BN为32.0%，Δ = +20.0 pp。
*   **分任务类别TCA提升**：产品缺陷报告（+38.5 pp，从7.7%到46.2%）、视觉故障排除（+16.7 pp，从75.0%到91.7%）、装配指导（+16.6 pp，从41.7%到58.3%）、保修索赔（+7.7 pp，从7.7%到15.4%）。
*   **延迟**：MMA2A平均13.04秒，Text-BN平均7.19秒，Δ = +5.85秒。
*   **原生路由比例**：MMA2A为81.7%，Text-BN为50.5%（后者仅文本部分为原生）。

**消融实验：**
为了探究机制，论文进行了一项关键消融实验：将最终决策步骤的LLM推理替换为简单的关键词匹配启发式方法。结果显示，在此配置下，MMA2A和Text-BN的TCA完全相同（均为36%），准确率差距完全消失。这证实了**两层需求**：协议层的原生路由必须与智能体层强大的推理能力（如LLM）相结合，才能带来准确率收益。路由提供了更高保真度的输入，但只有具备足够推理能力的下游智能体才能利用这些丰富信息。

### Q5: 有什么可以进一步探索的点？

该论文揭示了模态原生路由在提升任务准确性（+20个百分点）与增加延迟（1.8倍）之间的权衡，这为未来研究提供了明确方向。首先，可探索**自适应路由策略**，根据任务关键性、延迟约束和内容复杂性动态选择原生路由或文本瓶颈，以优化权衡。其次，论文指出大部分错误（83%）发生在推理层，而非路由层，因此需**增强智能体的多模态推理能力**，例如设计能输出结构化、高质量证据（如缺陷严重性评分）的智能体，而不仅是通用描述。此外，**隐私与数据安全**是重要限制，未来需在Agent Card中扩展数据保留策略字段，并研究在保护敏感信息（如原始音频）的同时保持路由效率的技术。最后，实验在受控环境（单一模型、英语、小规模基准）中进行，未来需在**异构模型、多语言、多领域（如医疗、制造）及真实部署条件**下验证泛化性，并研究路由策略与不同模型能力组合间的交互影响。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为MMA2A的模态原生路由层，旨在扩展Agent-to-Agent（A2A）协议，以解决多智能体系统中跨模态推理的准确性问题。核心问题是现有系统常将语音、图像等非文本模态强制转换为文本（形成“文本瓶颈”），导致信息损失，从而损害下游任务的准确性。

方法上，MMA2A通过在A2A协议之上构建一个架构层，利用现有的Agent Card能力声明和FilePart特性，智能地将语音、图像和文本部分以其原生模态路由到具备相应处理能力的智能体，避免了不必要的转码。

主要结论是，在受控的CrossModal-CS基准测试上，MMA2A相比文本瓶颈基线将任务完成准确率提升了20个百分点（52% vs. 32%），尤其在视觉依赖任务上提升显著。然而，这种准确率增益的实现依赖于一个双层要求：协议层的模态原生路由必须与智能体层基于LLM的推理能力相结合；若下游推理仅使用关键词匹配，则路由策略无效。此外，准确率的提升以1.8倍的延迟成本为代价。论文的意义在于首次量化了路由策略作为多智能体系统一阶设计变量的重要性，它直接决定了下游推理可用的信息质量，为构建高效的多模态多智能体系统提供了实践指导。
