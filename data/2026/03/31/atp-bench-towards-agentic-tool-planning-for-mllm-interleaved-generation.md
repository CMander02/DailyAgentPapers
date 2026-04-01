---
title: "ATP-Bench: Towards Agentic Tool Planning for MLLM Interleaved Generation"
authors:
  - "Yinuo Liu"
  - "Zi Qian"
  - "Heng Zhou"
  - "Jiahao Zhang"
  - "Yajie Zhang"
  - "Zhihang Li"
  - "Mengyu Zhou"
  - "Erchao Zhao"
  - "Xiaoxi Jiang"
  - "Guanjun Jiang"
date: "2026-03-31"
arxiv_id: "2603.29902"
arxiv_url: "https://arxiv.org/abs/2603.29902"
pdf_url: "https://arxiv.org/pdf/2603.29902v1"
github_url: "https://github.com/Qwen-Applications/ATP-Bench"
categories:
  - "cs.AI"
tags:
  - "Agentic Tool Planning"
  - "Multimodal Large Language Models (MLLMs)"
  - "Benchmark"
  - "Tool Use"
  - "Interleaved Generation"
  - "Evaluation Framework"
  - "MLLM-as-a-Judge"
relevance_score: 8.0
---

# ATP-Bench: Towards Agentic Tool Planning for MLLM Interleaved Generation

## 原始摘要

Interleaved text-and-image generation represents a significant frontier for Multimodal Large Language Models (MLLMs), offering a more intuitive way to convey complex information. Current paradigms rely on either image generation or retrieval augmentation, yet they typically treat the two as mutually exclusive paths, failing to unify factuality with creativity. We argue that the next milestone in this field is Agentic Tool Planning, where the model serves as a central controller that autonomously determines when, where, and which tools to invoke to produce interleaved responses for visual-critical queries. To systematically evaluate this paradigm, we introduce ATP-Bench, a novel benchmark comprising 7,702 QA pairs (including 1,592 VQA pairs) across eight categories and 25 visual-critical intents, featuring human-verified queries and ground truths. Furthermore, to evaluate agentic planning independent of end-to-end execution and changing tool backends, we propose a Multi-Agent MLLM-as-a-Judge (MAM) system. MAM evaluates tool-call precision, identifies missed opportunities for tool use, and assesses overall response quality without requiring ground-truth references. Our extensive experiments on 10 state-of-the-art MLLMs reveal that models struggle with coherent interleaved planning and exhibit significant variations in tool-use behavior, highlighting substantial room for improvement and providing actionable guidance for advancing interleaved generation. Dataset and code are available at https://github.com/Qwen-Applications/ATP-Bench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态大语言模型在交织生成（即交替生成文本和图像）任务中，现有方法无法统一事实性与创造性的问题。研究背景是，交织生成作为一种新兴的多模态任务，能够通过图文并茂的方式更直观地传达复杂信息，例如展示实验结果、提供造型建议或烹饪步骤。然而，当前主流方法分为两大范式：一是依赖图像生成，虽具创造性但常缺乏事实依据，难以处理复杂图表；二是依赖图像检索增强，虽能保证事实性但无法按需生成或修改图像，缺乏创造性。这两种范式通常相互割裂，导致模型无法在同一个回应中灵活地引用现有图像并生成查询特定的新图像，从而难以满足现实场景中既需事实参照又需创意生成的实际需求。

本文的核心问题是推动该领域迈向“智能体工具规划”这一新范式，即让模型作为中央控制器，自主决定在何时、何处、调用何种工具（如图像引用、编辑、生成、网络搜索等）来动态编排能力，以产生高质量的交织回应。为系统评估这一范式，论文引入了ATP-Bench基准测试，包含大量人工验证的查询和真值数据，并提出了一个无需真值参考或端到端执行的评估系统，以独立衡量模型的工具规划能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、评测类以及工具增强类。

在**方法类**研究中，早期工作探索了端到端的统一自回归模型（如Chameleon、Orthus），将文本和图像标记对齐生成；而基于流水线的系统则将语言建模与视觉合成解耦，让大语言模型调用专用视觉模块。检索增强方法则通过引用外部图像库来提升事实性。本文提出的“智能体化工具规划”范式与这些方法相关，但区别在于它旨在统一生成与检索，让模型作为中心控制器自主决定何时、何处调用何种工具，而非将两者视为互斥路径。

在**评测类**研究中，现有基准（如OpenLEAF、InterleavedBench）通常使用MLLM-as-a-Judge评估图像质量和跨模态连贯性；检索导向的基准（如RAG-IGBench）则强调通过检索实现事实性。本文的ATP-Bench与这些工作相关，但区别在于它系统评估开放式的工具规划能力，而非孤立地测试生成或检索，并引入了不依赖参考真值的多智能体评判系统（MAM）来评估工具调用精度和遗漏情况。

在**工具增强类**研究中，现有框架（如ViperGPT、MM-ReAct）通过提示管道执行代码或API；AssistGPT等采用包含规划、执行和反馈的循环流程。本文与这些工作一脉相承，但指出当前缺乏有效数据集来评估工具规划能力，而ATP-Bench正是为了填补这一空白而设计。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为ATP-Bench的基准测试和一套创新的评估系统，来解决多模态大语言模型在交错生成中缺乏统一规划能力的问题。其核心方法是推动模型从被动执行转向“智能体式工具规划”，即让模型作为中央控制器，自主决策何时、何地、调用何种工具来生成图文交错的响应。

整体框架围绕两个核心组件设计：ATP-Bench基准和MAM评估系统。ATP-Bench是一个系统化的评估基准，包含7,702个QA对，覆盖8个类别和25种视觉关键意图，其查询和真实答案均经过人工验证。这为评估模型的工具规划能力提供了高质量、多样化的测试床。

关键技术体现在对“工具规划”任务的严格定义和评估方法的创新上。首先，论文将任务形式化为：给定一个视觉关键查询q和一个文档集D（包含文本和图像），模型需要生成一个紧密耦合文本与相关图像的有序响应序列R。模型可以调用一个统一的工具调用空间，该空间包含五个专门模块：**Reference**（引用上下文中的图像）、**Diffusion**（生成新图像）、**Search**（通过搜索引擎检索图像）、**Code**（生成数据可视化图表）和**Edit**（编辑现有图像）。这五种工具覆盖了从事实性引用到创造性生成的全谱视觉需求。

主要的创新点在于提出的**多智能体MLLM即法官（MAM）** 评估系统。为了独立于端到端执行和易变的工具后端来评估纯粹的智能体规划能力，MAM系统模拟了一个多智能体环境。它专门评估三个方面：**工具调用的精确性**（判断调用是否正确必要）、**识别工具使用的遗漏机会**、以及**无参考的整体响应质量评估**。这种方法避免了依赖真实答案作为金标准，能够更直接、更稳定地衡量模型自身的规划决策质量。

通过这一套组合方案，论文不仅揭示了当前先进MLLM在连贯交错规划和工具使用行为上存在显著困难与差异，也为该领域的未来发展提供了可操作的评估指南和明确的改进方向。

### Q4: 论文做了哪些实验？

论文在提出的ATP-Bench基准上对10个最先进的多模态大语言模型（MLLM）进行了系统性实验评估。实验设置方面，主要采用零样本策略，并在Claude Sonnet 4.5、GPT-4o、Qwen2.5-VL-72B和LLaMA-3.2-11B上额外进行了3样本的少样本实验。评估框架使用了作者提出的多智能体MLLM-as-a-Judge系统，默认以Gemini 2.5 Pro作为评判智能体。

使用的数据集是ATP-Bench，包含8个类别（学术、手册、食谱、时尚、装修、产品、旅行、百科）共7,702个QA对，其中包含1,592个视觉问答对，旨在评估模型在视觉关键查询下的工具规划与交织生成能力。对比方法涵盖了10个模型，包括Claude Sonnet 4.5/4、Gemini 3 Pro、Grok-4.1 Fast Reasoning、GPT-5、GPT-4o、Qwen3-VL-Plus、Qwen2.5-VL-72B、LLaMA-3.2-11B和InternVL3.5-14B。

主要结果通过多个指标呈现：最终分数、成功率、错失图像数以及工具采纳率等。关键数据指标显示，Gemini 3 Pro在绝大多数指标上领先，其平均最终分数为79.88，平均工具使用成功率为81.77%，平均错失图像数最低，为0.49。Claude Sonnet 4.5和4等模型组成第二梯队，平均最终分数相近（约69），但工具使用策略不同（如Claude Sonnet 4.5成功率75.77%但错失图像数1.19）。GPT-4o和Qwen3-VL-Plus处于中游，平均最终分数分别为60.67和62.49，但在工具密集型类别（如旅行、装修）中成功率较低且错失图像数较高。开源模型如Qwen2.5-VL-72B和LLaMA-3.2-11B整体表现较弱，平均最终分数分别为53.22和28.97，尤其在工具使用上存在明显困难。实验结果总体表明，现有模型在连贯的交织规划和工具使用行为上存在显著差异和不足。

### Q5: 有什么可以进一步探索的点？

该论文提出的ATP-Bench和MAM评估系统为智能体工具规划提供了重要基准，但仍存在以下局限和可探索方向：首先，当前基准主要关注静态工具调用规划，未来可引入动态、多轮交互场景，考察智能体在复杂任务中的长期规划与状态维护能力。其次，评估依赖模拟环境，未能充分测试工具执行的实际效果与误差传递，需构建闭环评估框架以验证端到端性能。此外，工具库目前较为有限，可扩展至更多元化的专业工具（如3D生成、数据可视化），并研究工具组合与创新的自动化机制。从方法层面，可探索将符号规划与神经网络决策更好结合，提升规划的可解释性与可靠性。最后，跨模态对齐仍是挑战，需进一步研究如何让模型更精准理解视觉需求并生成协调的多模态内容。

### Q6: 总结一下论文的主要内容

该论文针对多模态大语言模型（MLLM）在交织文本与图像生成任务中面临的问题，提出了“智能体化工具规划”的新范式，并构建了相应的基准测试ATP-Bench。当前方法通常将图像生成与检索增强视为互斥路径，难以兼顾事实准确性与创造性。本文的核心贡献在于：首先，明确定义了智能体化工具规划问题，即让MLLM作为中央控制器，自主决策调用工具的时机、位置与类型，以生成视觉关键查询的交织式响应。其次，方法上，作者创建了ATP-Bench，这是一个包含7,702个QA对（涵盖8个类别和25种视觉关键意图）的大规模人工验证基准，用于系统评估模型规划能力。同时，为独立于具体工具后端评估规划质量，论文提出了多智能体MLLM即法官（MAM）系统，用于评估工具调用的精确性、识别工具使用遗漏，并评判整体响应质量。主要结论指出，现有10个先进MLLM在连贯的交织规划上仍存在困难，工具使用行为差异显著，表明该领域有巨大改进空间。ATP-Bench的发布为推进交织生成研究提供了系统评估工具和明确的发展方向。
