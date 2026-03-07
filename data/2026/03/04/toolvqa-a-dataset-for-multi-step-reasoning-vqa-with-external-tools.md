---
title: "ToolVQA: A Dataset for Multi-step Reasoning VQA with External Tools"
authors:
  - "Shaofeng Yin"
  - "Ting Lei"
  - "Yang Liu"
date: "2025-08-05"
arxiv_id: "2508.03284"
arxiv_url: "https://arxiv.org/abs/2508.03284"
pdf_url: "https://arxiv.org/pdf/2508.03284v2"
categories:
  - "cs.AI"
tags:
  - "Tool Use & API Interaction"
  - "Perception & Multimodal"
relevance_score: 8.0
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Perception & Multimodal"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "LLaVA-7B, GPT-3.5-turbo"
  key_technique: "ToolEngine (image-guided Depth-First Search with LCS-based example matching)"
  primary_benchmark: "ToolVQA"
---

# ToolVQA: A Dataset for Multi-step Reasoning VQA with External Tools

## 原始摘要

Integrating external tools into Large Foundation Models (LFMs) has emerged as a promising approach to enhance their problem-solving capabilities. While existing studies have demonstrated strong performance in tool-augmented Visual Question Answering (VQA), recent benchmarks reveal significant gaps in real-world tool-use proficiency, particularly in functionally diverse multimodal settings requiring multi-step reasoning. In this work, we introduce ToolVQA, a large-scale multimodal dataset comprising 23K instances, designed to bridge this gap. Unlike previous datasets that rely on synthetic scenarios and simplified queries, ToolVQA features real-world visual contexts and challenging implicit multi-step reasoning tasks, better aligning with real user interactions. To construct this dataset, we propose ToolEngine, a novel data generation pipeline that employs Depth-First Search (DFS) with a dynamic in-context example matching mechanism to simulate human-like tool-use reasoning. ToolVQA encompasses 10 multimodal tools across 7 diverse task domains, with an average inference length of 2.78 reasoning steps per instance. The fine-tuned 7B LFMs on ToolVQA not only achieve impressive performance on our test set but also surpass the large close-sourced model GPT-3.5-turbo on various out-of-distribution (OOD) datasets, demonstrating strong generalizability to real-world tool-use scenarios.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大型基础模型（LFMs）在真实世界多模态环境中使用外部工具进行多步推理的能力不足的问题。研究背景是，尽管将外部工具集成到LFMs中以增强其问题解决能力已成为一种有前景的方法，且现有研究在工具增强的视觉问答（VQA）基准上表现出色，但最近的评估揭示，LFMs在需要功能多样多模态工具和多步推理的真实场景中，其工具使用熟练度存在显著差距。现有方法的不足主要体现在两个方面：一是现有的大规模数据集（如ToolBench、ToolQA等）往往依赖合成场景和简化查询，缺乏真实世界的视觉上下文和复杂的隐含多步推理任务，导致与真实用户需求脱节；二是这些数据集可能通过显式提示简化推理过程，或依赖昂贵的人工标注，难以扩展，从而限制了通过微调提升LFMs工具使用能力的有效性。因此，本文的核心问题是：如何构建一个高质量、大规模的多模态数据集，以更好地模拟真实世界工具使用的复杂性，从而有效评估和提升LFMs在需要多步推理的真实场景中的工具使用能力。为此，论文提出了ToolVQA数据集和ToolEngine数据生成流水线，旨在填补这一空白。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：工具使用数据集与基准、基于大模型的工具代理方法，以及复杂视觉问答（VQA）任务。

在**工具使用数据集与基准**方面，现有工作主要分为文本和多模态两类。文本数据集（如API集合）虽规模大、多样性高，但缺乏视觉输入。多模态数据集虽引入视觉信息，但往往未能捕捉真实场景（如使用简化的PDF文件作为上下文，如MM-Traj），或依赖昂贵的人工标注。本文提出的ToolVQA则通过自动化流程生成大规模数据，强调真实视觉场景和已验证的正确性，弥补了现有数据在真实性和复杂性上的不足。

在**基于大模型的工具代理方法**上，主流方法包括上下文学习和指令微调。这些方法虽在零样本任务上展现出强大推理能力，但在实际多步骤工具协作应用中仍面临挑战。此外，近期网页导航代理主要聚焦基于GUI的浏览器插件，适用范围局限于网页任务。本文的ToolEngine框架则扩展至更广泛的真实世界多模态场景。

在**复杂VQA任务**领域，早期VQA数据集多关注简单的常识问答。近期研究开始探索需要外部工具（如维基百科、OCR）的更具挑战性的VQA，但这些数据集通常只评估使用单一工具的能力，而非多工具协作，限制了大模型在工具代理框架中的多步推理能力。ToolVQA则专门针对**多步骤推理**设计，包含跨7个领域的10种多模态工具，平均推理步骤达2.78步，旨在促进工具间的协同与复杂推理。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ToolEngine的自动化数据合成流水线来解决构建高质量、真实世界多步推理VQA数据集的问题。其核心方法是利用深度优先搜索（DFS）结合动态上下文示例匹配机制，模拟人类使用工具进行推理的过程，从而生成包含复杂多步推理轨迹的数据。

整体框架包含三个核心组件：1) **真实世界示例构建**：首先由人工构建一小部分真实世界的工具使用示例，这些示例包含了图像、工具集、查询、答案和推理轨迹，作为先验知识注入到后续的自动生成过程中，确保生成的数据符合真实用户需求。2) **图像引导的工具图深度优先搜索**：以输入图像为起点，在一个包含10种多功能工具（涵盖感知、操作、逻辑、创意四大领域）的图上进行DFS。在每一步，由一个大型基础模型（如ChatGPT-4o-latest）作为控制器，根据当前图像、已生成的工具调用轨迹以及匹配的示例，动态选择下一个要调用的工具并生成其调用参数。这个过程会实际调用工具来从图像中提取信息，从而为生成具有挑战性的问答对奠定基础。3) **基于最长公共子序列的示例匹配**：这是关键的创新点。为了解决传统固定示例匹配方法在多样性上的局限，该方法在DFS的每一步，将当前已生成的局部工具调用轨迹与人工构建的示例库中的轨迹进行LCS匹配，动态检索出匹配度最高的前k个示例作为上下文。这种动态匹配机制使得系统能更灵活地结合不同示例中的信息，有效支持复杂的多步推理链构建。

生成完整的工具使用轨迹后，再利用该轨迹和图像信息生成最终的查询和答案，形成一个完整的数据样本。为确保数据质量，论文还进行了人工标注和筛选。

该方法的主要创新在于：第一，提出了一个系统化的、基于真实工具调用和先验知识的自动化数据生成流水线（ToolEngine），能够高效构建大规模、高质量的数据集。第二，引入了动态的LCS示例匹配机制，显著提升了生成推理轨迹的多样性、复杂性和合理性。第三，强调“真实世界”对齐，包括使用真实图像场景、真实部署的工具（输出包含噪声）以及确保多步推理的逻辑连贯性，这使得生成的ToolVQA数据集更贴近实际应用场景。消融实验证明，移除真实世界示例或LCS匹配都会导致数据质量（如答案准确性、工具必要性、推理复杂度）大幅下降，验证了这些设计的有效性。

### Q4: 论文做了哪些实验？

论文在ToolVQA数据集上进行了全面的实验评估。实验设置方面，作者将数据集划分为包含21,105个自动生成样本的训练集和2,550个人工重新标注样本的测试集。他们基于Lego Agent框架对LLaVA-7B模型进行微调，训练目标为多轮对话的交叉熵损失。测试采用两种模式：端到端模式（评估从图像和问题直接到最终答案的能力）和分步模式（评估工具使用的具体步骤）。评估指标包括步骤无错率（InstAcc）、工具选择准确率（ToolAcc）、参数预测准确率（ArgAcc）和答案总结准确率（SummAcc）。

实验对比了闭源模型（如GPT-4o、Claude-3.5-sonnet、GPT-3.5-Turbo）和开源模型（如Qwen2-VL系列、LLaVA-v1.5-7B、LLaMA-3-8b-instruct）在三种设置下的性能：纯视觉语言模型（VLM）、VLM调用工具（VLM+tool）和纯语言模型调用工具（LLM+tool）。主要结果显示，微调后的LLaVA-7B模型在测试集上表现优异，在VLM+tool设置下，其端到端准确率达到18.8%，分步模式下的InstAcc、ToolAcc、ArgAcc和SummAcc分别为86.62%、61.61%、39.34%和30.91%。关键数据表明，该7B模型性能接近甚至在某些方面超越了更大的闭源模型GPT-3.5-Turbo（其LLM+tool端到端准确率为18.37%）。

此外，论文还在多个分布外（OOD）基准（如TextVQA、TallyQA、InfoSeek、GTA、TEMPLAMA）上测试了泛化能力。微调后的LLaVA-7B相比基线LLaVA-7B在五个数据集上准确率分别提升5.8%、4.2%、8.6%、21.17%和18.37%，并在多个数据集上超越了GPT-3.5-Turbo。消融实验表明，移除图像描述工具或所有工具会导致性能显著下降。错误分析显示，主要错误类型为参数预测错误和答案总结错误，这反映了模型在动态处理工具返回信息方面仍存在挑战。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其局限性及未来研究方向可从以下几个方面深入探索：首先，**工具集的扩展与泛化**。当前工作仅整合了10个工具覆盖7个领域，未来可纳入更多样化、专业化的工具（如科学计算或创意设计工具），并研究模型在未见工具上的零样本适应能力。其次，**推理过程的透明性与可解释性**。论文强调多步推理，但未深入分析模型内部决策机制；未来可结合因果推理或生成思维链，提升步骤的可追溯性和纠错能力。此外，**数据生成方法的优化**。虽然ToolEngine采用DFS和动态示例匹配，但生成效率与多样性仍有提升空间，例如引入强化学习或对抗生成以模拟更复杂的人类推理路径。最后，**实际部署的挑战**。论文在OOD数据集上表现良好，但未涉及实时性、工具调用延迟或安全伦理等问题；后续可探索轻量化部署、工具可靠性评估及多智能体协作框架，推动其在真实场景中的应用。

### Q6: 总结一下论文的主要内容

该论文针对当前大型基础模型在真实多模态工具使用场景中存在的多步推理能力不足问题，提出了ToolVQA数据集和配套的数据生成方法ToolEngine。核心贡献在于构建了一个大规模、高质量的多模态视觉问答数据集，包含2.3万个实例，覆盖7个任务领域的10种工具，平均推理步骤达2.78步，其特点是采用真实视觉场景和隐含多步推理任务，更贴近实际应用。

方法上，作者设计了ToolEngine数据生成流水线，采用深度优先搜索结合动态上下文示例匹配机制，模拟人类使用工具进行多步推理的过程，从而自动生成复杂、真实的问答对。

主要结论表明，基于ToolVQA微调的70亿参数模型不仅在自身测试集上表现优异，而且在多个分布外数据集上超越了GPT-3.5-turbo等大型闭源模型，证明了该方法能有效提升模型在真实世界工具使用场景中的泛化能力和推理能力。
