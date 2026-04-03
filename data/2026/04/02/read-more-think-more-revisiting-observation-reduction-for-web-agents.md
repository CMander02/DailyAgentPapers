---
title: "Read More, Think More: Revisiting Observation Reduction for Web Agents"
authors:
  - "Masafumi Enomoto"
  - "Ryoma Obara"
  - "Haochen Zhang"
  - "Masafumi Oyamada"
date: "2026-04-02"
arxiv_id: "2604.01535"
arxiv_url: "https://arxiv.org/abs/2604.01535"
pdf_url: "https://arxiv.org/pdf/2604.01535v1"
categories:
  - "cs.CL"
tags:
  - "Web Agent"
  - "Observation Representation"
  - "HTML Parsing"
  - "Agent Planning"
  - "Model Capability"
  - "Benchmark Evaluation"
  - "MiniWoB++"
  - "WebArena"
relevance_score: 8.0
---

# Read More, Think More: Revisiting Observation Reduction for Web Agents

## 原始摘要

Web agents based on large language models (LLMs) rely on observations of web pages -- commonly represented as HTML -- as the basis for identifying available actions and planning subsequent steps. Prior work has treated the verbosity of HTML as an obstacle to performance and adopted observation reduction as a standard practice. We revisit this trend and demonstrate that the optimal observation representation depends on model capability and thinking token budget: (1) compact observations (accessibility trees) are preferable for lower-capability models, while detailed observations (HTML) are advantageous for higher-capability models; moreover, increasing thinking tokens further amplifies the benefit of HTML. (2) Our error analysis suggests that higher-capability models exploit layout information in HTML for better action grounding, while lower-capability models suffer from increased hallucination under longer inputs. We also find that incorporating observation history improves performance across most models and settings, and a diff-based representation offers a token-efficient alternative. Based on these findings, we suggest practical guidelines: adaptively select observation representations based on model capability and thinking token budget, and incorporate observation history using diff-based representations.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在重新审视并解决基于大语言模型（LLM）的网页智能体（Web Agent）中一个被广泛采纳但可能并非普适的实践问题：观察信息缩减（observation reduction）。研究背景是，LLM驱动的网页智能体通过循环执行动作（如点击）并观察网页（通常以冗长的HTML表示）来完成任务。长期以来，由于早期LLM上下文窗口有限且冗长HTML包含大量无关信息可能干扰推理，将HTML缩减为更紧凑的表示（如无障碍访问树a11y）已成为标准做法。

然而，现有方法存在不足。它们普遍假设缩减观察总是有益的，但这一假设建立在早期LLM能力限制的基础上，未能充分考虑当前LLM能力的快速演进。具体而言，最新LLM已具备更强的长上下文处理能力和扩展的思维链推理（“思考令牌”预算增加），这使得详细HTML可能不再是负担，反而成为提供有价值布局信息的资源。因此，现有方法采用固定的观察缩减策略，可能无法适应不同模型能力和推理资源配置的差异。

本文要解决的核心问题是：在当代先进的LLM背景下，观察缩减的效果如何随模型能力和推理时分配的思考令牌数量而变化？论文通过系统实验揭示，最优的观察表示并非一成不变：对于能力较低的模型，紧凑表示（如a11y）更优；而对于能力更高的模型，详细的HTML表示反而更有优势，且增加思考令牌会进一步放大HTML的益处。论文旨在挑战“缩减即优化”的固有趋势，为网页智能体系统设计提供基于模型能力和资源预算的自适应选择指南。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕网页智能体（Web Agents）的观察表示与历史信息利用展开，可分为以下两类：

**1. 观察表示与缩减方法**：现有研究普遍认为HTML内容冗长，会带来上下文长度和推理效率的挑战，因此广泛采用观察缩减策略。具体方法包括：训练交叉编码器对HTML元素与任务指令进行相关性评分并仅保留Top-k元素；采用两阶段流程，先由专用模型提取和总结相关HTML元素再传递给大语言模型；使用双编码器依据完整动作历史对DOM元素进行评分；通过生成Python评分程序以编程方式过滤HTML元素。此外，也有研究采用更简洁的无障碍树（a11y）替代HTML，并通过移除任务无关元素、用自然语言描述元素角色，或使用较小LLM选择性提取相关行来进一步优化。另有工作仅使用截图或结合截图与文本观察，但文本部分均采用压缩或过滤表示。

**2. 观察历史利用与缩减**：利用过去的观察和动作作为历史已被证明能提升智能体性能，但保留完整历史不切实际，因此研究者探索了多种控制历史信息量的策略。例如，仅存储动作日志和局部HTML片段作为历史以减少冗余，或仅保留与当前子任务相关的步骤观察。

**本文与相关工作的关系与区别**：本文与上述研究共享“观察信息处理是关键”这一共识，但**挑战了“缩减观察始终有益”的主流设计思路**。现有工作未充分考察模型长上下文能力或思维令牌预算增大时的影响，而本文通过实验证明：观察表示的最优选择取决于模型能力和思维令牌预算——能力较强的模型更能从详细HTML（含布局信息）中受益，而能力较弱的模型则更适合简洁的无障碍树。此外，本文发现融入观察历史在多数设置下能提升性能，并提出了基于差异（diff）的令牌高效表示方法。因此，本文的核心贡献在于系统性地重新评估了观察缩减的作用，并提出了自适应选择观察表示及利用差异表示融入历史的实用指南。

### Q3: 论文如何解决这个问题？

论文通过系统性的实验分析，重新审视了网页智能体（Web Agent）中观察表示（Observation Representation）的设计问题，并提出了一个基于模型能力和思考令牌预算的自适应选择框架。其核心方法是：不再将HTML的冗长性视为必然障碍，而是论证了最优观察表示取决于模型能力与思考资源，并据此提供了一套实用指南。

**整体框架与实验设计**：研究在WorkArena L1基准上进行评估，该基准包含330个基于ServiceNow平台的日常办公任务。研究构建了一个对比实验框架，核心变量包括：1) **观察表示**：对比了紧凑的可访问性树（a11y）、详细的HTML（包含CSS布局信息）以及a11y加截图（a11y+scrs）三种形式。2) **模型能力**：涵盖了从高能力前沿专有模型（如Claude Sonnet 4.6, GPT-5.1）到低能力开源模型（如GPT-OSS系列、Qwen、Llama）的广泛谱系。3) **思考令牌预算**：通过调整模型的`reasoning_effort`或`thinking_budget`参数来控制。智能体采用基于ID的动作定位（Action Grounding）方式，在AgentLab框架下运行。

**核心发现与创新方法**：
1.  **模型能力与观察表示的动态适配**：研究发现，**高能力模型能从详细的HTML表示中获益**，而**低能力模型则更适合紧凑的a11y表示**。例如，GPT-5.1（高思考预算）使用HTML时成功率比a11y高出17.5%，而低能力的GPT-OSS-20b使用HTML时性能则大幅下降18.8%。这颠覆了以往“观察越精简越好”的普遍假设。
2.  **思考令牌预算的放大效应**：**增加思考令牌预算会进一步放大高能力模型利用HTML优势的能力**。例如，GPT-5.1的`reasoning_effort`从“低”调到“高”时，使用HTML带来的性能增益从8.8%扩大到了17.5%。这表明，充足的“思考”资源是模型消化冗长信息并做出更好决策的关键。
3.  **基于差异（Diff）的历史观察集成**：论文提出并验证，**引入观察历史（即之前步骤的页面状态）能普遍提升性能**。为了高效地集成历史信息，论文推荐使用**基于差异（diff-based）的表示方法**，这是一种令牌效率高的替代方案，仅传递页面状态的变化部分，而非完整的重复观察。
4.  **错误分析与机制阐释**：通过细致的错误归因分析，论文揭示了上述现象背后的机制。对于高能力模型，**HTML中保留的布局信息有助于更准确的动作定位（Grounding）**，减少了“元素未找到”等错误。相反，低能力模型在面对冗长的HTML输入时，**幻觉（Hallucination）增加**，导致更多无效的元素ID引用，从而性能下降。这从因果层面解释了不同表示法产生性能差异的原因。

**总结的创新点与解决方案**：论文的核心贡献在于提出了一个**情境感知的、自适应的观察表示选择策略**。解决方案不是单一的，而是建议开发者根据**所用模型的实际能力**和**可分配的思考计算预算**，动态地选择是提供精简的a11y还是详细的HTML。同时，推荐使用**基于差异的观察历史**来提供上下文，以兼顾性能与效率。这套指南为构建高效的网页智能体提供了新的、数据驱动的设计原则。

### Q4: 论文做了哪些实验？

论文在WorkArena L1基准（包含330个任务，涵盖7种任务类型）上评估了不同观察表示对基于大语言模型的网页智能体性能的影响。实验设置包括：采用基于ID的动作定位方法，通过Playwright执行动作，最大步骤限制为15步。

对比方法主要围绕三种观察表示：作为基线的紧凑型可访问性树（a11y）、详细的HTML（包含CSS布局信息），以及a11y与屏幕截图结合（a11y+scrs）。此外，还比较了XML格式与缩进格式对结果的影响。

实验评估了多种模型，按能力分为两类：高性能专有模型（如Claude Sonnet 4.6、gpt-5.1、gemini-2.5-flash、o3-mini）和较低能力的开源模型（如gpt-oss系列、Qwen3-VL系列、Llama-3.1系列）。同时，通过调整推理模型的`reasoning_effort`（高/低）或`thinking_budget`（128/16384）参数，探究了思考令牌数量对性能的影响。

主要结果如下：
1.  **模型能力与观察表示**：高性能模型能更好地利用信息丰富的观察。使用HTML时，Claude Sonnet 4.6、gpt-5.1（高）和gemini-2.5-flash（预算=16384）的任务成功率分别比a11y基线提高了+14.6%、+17.5%和+11.2%。相反，较低能力模型（如gpt-oss-120b/20b、Llama-3.1-70B）在使用HTML时性能普遍下降，例如gpt-oss-20b（高）下降了-18.8%。
2.  **思考令牌的影响**：更多的思考令牌能增强模型利用详细观察的能力。例如，gpt-5.1的`reasoning_effort`从低调到高时，使用HTML带来的性能增益从+8.8%扩大到+17.5%。gemini-2.5-flash的`thinking_budget`从128增至16384时，增益也从+6.0%扩大到+11.2%。
3.  **任务类别分析**：HTML在筛选、排序和仪表板读取任务上普遍带来性能提升，而在表单填写、知识库搜索和服务订购任务上可能导致性能下降。高性能模型在前几类任务上增益大，后几类损失小，因此整体受益；低能力模型则相反。
4.  **定位错误分析**：错误分析表明，转向HTML后，高性能模型（如gpt-5.1）的定位错误总数减少，而低能力模型（如gpt-oss-20b）的错误增加，特别是“未找到元素”错误，表明低能力模型在长输入下更容易产生幻觉。
5.  **格式对比**：无论使用XML还是缩进格式，高性能模型始终受益于HTML，低能力模型始终受损，表明性能差异主要源于信息内容而非格式偏好。

### Q5: 有什么可以进一步探索的点？

该论文的局限性和未来研究方向主要体现在以下几个方面。首先，研究的普适性有待验证，实验仅在基于ServiceNow的WorkArena L1基准上进行，未来需扩展到更多样化的网站和领域，以检验观察表示选择原则的通用性。其次，动作定位机制较为单一，目前仅验证了基于ID的定位，未来应探索基于坐标或其他定位方案下，模型能力与观察表示之间的交互关系。再者，HTML带来性能提升的机制尚不明确，尽管推测CSS布局信息是关键因素，但缺乏直接的消融实验验证，未来需深入剖析HTML中哪些具体元素（如DOM结构、样式属性）对高层模型至关重要。此外，观察历史与丰富表示的结合效果未被充分探索，论文仅测试了基于a11y树的历史，未来可研究HTML与差异表示（diff）结合的历史机制，尤其是在更长序列任务（超过15步）中的影响。结合个人见解，可能的改进思路包括：开发自适应观察表示选择器，能根据实时任务复杂度、模型置信度动态切换HTML与简化表示；设计分层观察机制，让模型自主请求更详细的局部HTML信息；以及探索多模态观察融合，结合视觉截图与HTML，以增强空间布局理解。

### Q6: 总结一下论文的主要内容

该论文重新审视了网络智能体中普遍采用的观察缩减（如将HTML简化为无障碍树）做法，指出其并非总是有益。核心贡献在于揭示了最优观察表示取决于模型能力和思考令牌预算：对于能力较强且思考令牌预算充足的模型，详细的HTML观察能提供布局等关键线索，带来高达17.5个百分点的性能提升，且思考令牌越多增益越明显；而能力较弱的模型在长输入下容易产生幻觉，反而更适合紧凑表示。此外，论文发现融入观察历史能普遍提升性能，而基于差异（diff）的表示是一种高效的替代方案。基于此，作者提出了实用设计指南：应根据模型能力和任务特性自适应选择观察表示，并推荐使用差异表示来高效整合历史信息。这些发现挑战了过往将HTML冗长视为障碍的固有认知，为网络智能体的系统优化提供了重要依据。
