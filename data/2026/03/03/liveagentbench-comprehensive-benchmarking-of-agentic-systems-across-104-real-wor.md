---
title: "LiveAgentBench: Comprehensive Benchmarking of Agentic Systems Across 104 Real-World Challenges"
authors:
  - "Hao Li"
  - "Huan Wang"
  - "Jinjie Gu"
  - "Wenjie Wang"
  - "Chenyi Zhuang"
date: "2026-03-03"
arxiv_id: "2603.02586"
arxiv_url: "https://arxiv.org/abs/2603.02586"
pdf_url: "https://arxiv.org/pdf/2603.02586v1"
categories:
  - "cs.AI"
tags:
  - "Tool Use & API Interaction"
  - "Multi-Agent Systems"
relevance_score: 9.0
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Multi-Agent Systems"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "Social Perception-Driven Data Generation (SPDG)"
  primary_benchmark: "LiveAgentBench"
---

# LiveAgentBench: Comprehensive Benchmarking of Agentic Systems Across 104 Real-World Challenges

## 原始摘要

As large language models grow more capable, general AI agents have become increasingly prevalent in practical applications. However, existing benchmarks face significant limitations, failing to represent real-world user tasks accurately. To address this gap, we present LiveAgentBench, a comprehensive benchmark with 104 scenarios that reflect real user requirements. It is constructed from publicly sourced questions on social media and real-world products. Central to our approach is the Social Perception-Driven Data Generation (SPDG) method, a novel process we developed to ensure each question's real-world relevance, task complexity, and result verifiability. We evaluate various models, frameworks, and commercial products using LiveAgentBench, revealing their practical performance and identifying areas for improvement. This release includes 374 tasks, with 125 for validation and 249 for testing. The SPDG process enables continuous updates with fresh queries from real-world interactions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI智能体（Agent）系统评估基准在反映真实世界复杂任务方面的不足。随着大语言模型能力提升，通用AI智能体在实际应用中日益普及，但现有基准（如MMLU-Pro、AGIEval、GSM8k）多聚焦于单一能力（如数学、代码生成），与人类日常面临的复杂、多模态任务存在显著差距。尽管GAIA、AgentBench等基准引入了部分真实任务评估，但其覆盖场景仍有限，缺乏对高频真实场景（如手机操作、视频理解）的涵盖，且数据集存在静态、易过时、易被训练数据污染等问题，导致评估结果的稳健性和准确性受限。

为此，本文提出了LiveAgentBench，一个全面且动态更新的智能体评估基准。其核心目标是构建一个能准确反映真实用户需求、涵盖多样化现实场景的评估体系。该基准从社交媒体和真实产品中收集了104个真实场景下的用户问题，并通过创新的“社会感知驱动数据生成（SPDG）”方法，确保每个任务兼具现实相关性、复杂性和结果可验证性。LiveAgentBench不仅评估智能体的推理能力，还系统检验其多模态处理、工具使用（如浏览器、文件、移动操作系统操作）以及音视频理解等综合能力。通过定期更新数据集，该基准旨在持续追踪智能体在快速变化的真实环境中的性能，为AI智能体的实用化发展提供更可靠的评估指引。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、评测类和应用类。在方法类方面，研究通过多智能体系统提升LLM的问题解决能力，例如AWorld作为多智能体执行MCP服务器弥合了理论多智能体系统能力的差距，而MetaGPT则是一个基于LLM的多智能体元编程框架。在评测类方面，现有基准测试大多专注于特定领域，如PlanBench或Natural Plan评估LLM的规划和推理能力，AndroidWorld和OSWorld评估LLM在操作系统（如Android、Windows、MacOS）中的操作能力，而GAIA和AgentBench提供了更通用的自主智能体数据集。然而，这些基准测试在反映真实世界用户任务方面存在局限，往往缺乏现实场景的代表性。本文提出的LiveAgentBench与这些工作的区别在于，它通过社会感知驱动的数据生成方法，从社交媒体和真实产品中构建了104个反映实际用户需求的场景，强调任务的真实性、复杂性和结果可验证性，从而填补了现有基准在现实世界代表性上的不足，并支持通过持续更新来保持数据的新鲜度。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为LiveAgentBench的综合性基准测试来解决现有基准无法准确反映现实世界用户任务的问题。其核心方法是提出并应用了“社会感知驱动的数据生成”（SPDG）方法，这是一个标准化的人机协作框架，旨在系统性地生成高质量、贴近现实的评估任务。

整体框架与主要模块包括：
1.  **数据源采集**：为确保现实相关性，从多个公开的互联网平台（如知乎、Quora、小红书、Stack Overflow、抖音等）收集真实的用户提问和案例，覆盖问答社区、社交媒体、专业论坛和视频互动平台。
2.  **SPDG标准流程**：这是架构设计的核心。该流程将人类专业知识和大型语言模型（LLM）能力系统结合，通过一系列标准化操作和检查机制来生产数据：
    *   **初始筛选**：利用LLM，根据“非可检索性”（答案不能通过简单搜索或RAG直接获得）和“工具依赖性”（必须使用至少一种工具才能解决）两个关键标准，从海量数据中筛选出具有挑战性的真实用户案例。
    *   **能力与环境提取**：使用LLM为筛选出的用例生成可能的执行步骤，并从中提取完成任务所需的能力（如推理）和环境信息（如特定网站、浏览器）。
    *   **任务生产**：由相关领域的标注者基于提取的信息和环境，构建具体的评估问题和答案标签。他们将开放式问题转化为答案明确、稳定的封闭式问题，以确保结果易于验证，同时标注正确的执行步骤以评估任务复杂度。
    *   **多层质量控制机制**：这是关键创新点之一。SPDG流程嵌入了多个人工与LLM双重检查环节，包括：
        *   **任务相关性检查**：确保修改后的问题与原任务在能力和环境要求上高度一致（不匹配度低于50%）。
        *   **任务复杂度检查**：参考GAIA基准，根据规划步骤数和工具使用情况对任务难度分级，并剔除步骤过少或无工具使用的简单任务。
        *   **规划可执行性检查**：邀请其他标注者按标注步骤实际执行，验证能否得到正确答案。
        *   **结果唯一性检查**：通过双盲标注等方式，确保每个任务答案的明确性和唯一性。

创新点主要体现在：
1.  **SPDG方法论**：提出了一套可操作、可持续的人机协作数据生成与质量控制标准流程，确保了基准数据的现实相关性、挑战性和易验证性三大原则。
2.  **真实世界任务来源**：完全基于公开的网络用户案例构建任务，使数据分布与真实应用场景保持一致，避免了模拟数据与真实需求之间的鸿沟。
3.  **动态更新能力**：SPDG流程的设计使得基准能够持续集成来自真实世界交互的新查询，从而跟上用户需求的变化，避免因数据陈旧或污染导致的评估偏差。
4.  **严格的复杂度与唯一性保障**：通过“非可检索性”、“工具依赖性”筛选以及多级人工和LLM校验，有效构建了需要多步骤规划和工具使用的复杂任务集，并保证了评估结果的稳定可靠。

### Q4: 论文做了哪些实验？

实验在LiveAgentBench基准上进行，涵盖104个真实世界场景，共374个任务（125个验证任务和249个测试任务）。实验设置上，采用零样本提示评估大语言模型（LLMs），对智能体（Agents）则直接在其官方网站评估，所有评估均使用Pass@1指标，并通过字符串匹配自动判断答案正确性，无需人工或LLM作为评判模型。

评估对象包括开源和闭源LLMs、自主智能体及一个开源智能体框架。具体对比方法为：选取了5个近期流行的LLMs，涵盖多模态和推理模型，如Qwen3-235B-A22B、Claude35-sonnet、GPT-4o、Gemini-2.5-pro和Deepseek-R1-671B；同时评估了4个2024年发布的智能体，包括擅长研究的OpenAI Deep Research-4omini和Perplexity-Research，以及擅长使用工具的Manus和Coze Space；此外还测试了基于Claude35-sonnet的开源框架AWorld。所有模型和智能体仅使用其自身能力和内置工具进行评估，若缺乏必要能力（如附件上传）则直接判定任务失败。

主要结果显示，LLMs在LiveAgentBench上的整体表现较弱，平均仅能完成约13.48%的任务，其中Gemini-2.5-pro表现最佳，整体得分为16.85%。智能体表现相对更好，平均完成23.85%的任务，最高分智能体Manus得分为35.29%。开源框架AWorld得分为15.51%。作为对比，人类平均完成率为69.25%，显著高于所有AI系统。关键数据指标包括：在五大场景（工作与学习、日常生活、信息获取与处理、人文与社会科学、社会生产）中，智能体在信息获取与处理场景表现相对均衡，而LLMs在该场景与工作学习场景表现差距较大；在能力维度上，智能体在文本文件处理（如Manus达37.85%）、图像处理（如Manus达35.29%）等方面展现优势，但LLMs在多媒体处理（如视频、音频）上普遍存在短板，多数得分为0。实验分析指出，工具缺失导致LLMs与智能体性能差异显著（LLMs整体得分平均比智能体低约56.51%），而智能体失败的主要原因是工具执行不稳定和环境背景知识缺乏，例如评估中11.76%的框架任务失败源于工具不稳定。

### Q5: 有什么可以进一步探索的点？

LiveAgentBench的局限性主要体现在语言和文化多样性不足，以及任务设计的“真实性”与“明确性”之间存在张力。论文明确指出其任务主要基于中文，缺乏多语言和文化背景的覆盖，这限制了其作为通用基准的普适性。此外，为了确保答案可验证性而对开放性问题进行的人工消歧和修改，可能导致任务细节略显生硬，与人类自然的交互习惯存在偏差。

基于此，未来研究可以从以下几个方向深入探索：
1.  **多语言与文化扩展**：利用其提出的SPDG方法，从全球范围的社交媒体和产品中收集语料，构建多语言、跨文化的基准，以更全面地评估智能体在不同社会环境下的适应能力。
2.  **任务设计的平衡艺术**：探索更巧妙的评估机制，例如引入基于过程的评分或接受一定范围内的合理答案，从而在保持任务真实感（允许一定模糊性和开放性）与评估客观性之间找到更好的平衡点，减少人工修改带来的“不自然感”。
3.  **动态评估与长程能力**：当前基准侧重于静态任务快照。未来可进一步利用SPDG的持续更新能力，设计需要长期记忆、持续学习和适应环境变化的序列任务或动态场景，以评估智能体的终身学习与进化能力。
4.  **深入性能归因分析**：在现有性能评估基础上，可进一步设计实验，剖析导致任务失败的具体原因（如规划缺陷、工具使用错误、知识不足等），从而为改进智能体架构提供更精准的诊断依据。

### Q6: 总结一下论文的主要内容

LiveAgentBench 是一个针对智能体系统的综合性基准测试，旨在解决现有基准测试在真实世界任务代表性上的不足。该研究构建了一个包含 104 个真实场景、总计 374 项任务的评测集，其问题均来源于社交媒体和真实产品的公开用户需求，确保了任务的高度真实性。

论文的核心贡献在于提出了“社会感知驱动数据生成”方法，该方法通过一套新颖的流程，保证了每个评测任务在现实相关性、任务复杂度和结果可验证性上的质量。利用此基准，研究对多种主流模型、框架及商业产品进行了系统评估，揭示了它们在应对真实用户需求时的实际性能与局限。

主要结论表明，当前智能体系统在复杂、动态的真实场景中仍存在显著提升空间。该基准支持从真实交互中持续更新查询，为未来智能体的研发与改进提供了重要的评估工具和方向指引。
