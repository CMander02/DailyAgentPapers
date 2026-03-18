---
title: "VisBrowse-Bench: Benchmarking Visual-Native Search for Multimodal Browsing Agents"
authors:
  - "Zhengbo Zhang"
  - "Jinbo Su"
  - "Zhaowen Zhou"
  - "Changtao Miao"
  - "Yuhan Hong"
  - "Qimeng Wu"
  - "Yumeng Liu"
  - "Feier Wu"
  - "Yihe Tian"
  - "Yuhao Liang"
  - "Zitong Shan"
  - "Wanke Xia"
  - "Yi-Fan Zhang"
  - "Bo Zhang"
  - "Zhe Li"
  - "Shiming Xiang"
  - "Ying Yan"
date: "2026-03-17"
arxiv_id: "2603.16289"
arxiv_url: "https://arxiv.org/abs/2603.16289"
pdf_url: "https://arxiv.org/pdf/2603.16289v1"
github_url: "https://github.com/ZhengboZhang/VisBrowse-Bench"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Multimodal Agent"
  - "Web Browsing Agent"
  - "Benchmark"
  - "Visual Reasoning"
  - "Agent Evaluation"
  - "MLLM"
relevance_score: 8.0
---

# VisBrowse-Bench: Benchmarking Visual-Native Search for Multimodal Browsing Agents

## 原始摘要

The rapid advancement of Multimodal Large Language Models (MLLMs) has enabled browsing agents to acquire and reason over multimodal information in the real world. But existing benchmarks suffer from two limitations: insufficient evaluation of visual reasoning ability and the neglect of native visual information of web pages in the reasoning chains. To address these challenges, we introduce a new benchmark for visual-native search, VisBrowse-Bench. It contains 169 VQA instances covering multiple domains and evaluates the models' visual reasoning capabilities during the search process through multimodal evidence cross-validation via text-image retrieval and joint reasoning. These data were constructed by human experts using a multi-stage pipeline and underwent rigorous manual verification. We additionally propose an agent workflow that can effectively drive the browsing agent to actively collect and reason over visual information during the search process. We comprehensively evaluated both open-source and closed-source models in this workflow. Experimental results show that even the best-performing model, Claude-4.6-Opus only achieves an accuracy of 47.6%, while the proprietary Deep Research model, o3-deep-research only achieves an accuracy of 41.1%. The code and data can be accessed at: https://github.com/ZhengboZhang/VisBrowse-Bench

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前多模态浏览智能体（Multimodal Browsing Agents）评估基准存在的两个关键缺陷。研究背景是，随着多模态大语言模型（MLLMs）的快速发展，智能体已能获取并推理现实世界中的多模态信息。然而，现有的深度研究或浏览基准大多局限于文本模态，未能充分反映真实检索场景中的多模态需求。

现有方法的不足主要体现在两方面：首先，许多现有基准（如MMSearch、BrowseComp-VL）主要测试模型调用工具处理图文查询的能力，任务设计往往只需将图像输入搜索工具进行检索，无需对多模态信息进行细粒度理解，因此未能充分挑战模型在多模态深度研究场景下的综合理解能力，反而偏重于工具调用能力。其次，即使有些基准（如MMSearch-Plus、VDR-Bench）要求对查询图像进行初步视觉感知，其后续的信息收集过程却退化为单模态的文本遍历。一旦从查询图像中提取出实体名称或描述，所有下游推理都可通过文本检索和合成来完成，搜索轨迹从未要求对在搜索过程中发现的其他视觉信息进行定位、解析或推理。这使得任务实质上退化为纯文本浏览，无法评估模型在信息并非预先提供、而是需要主动从包含多模态信息的网页中寻找时，动态获取和整合视觉信息的能力。这种在整个任务过程中进行视觉搜索和理解的能力在现实检索中至关重要，但现有基准未能评估该能力，限制了该领域的进一步发展。

因此，本文要解决的核心问题是：如何构建一个能够全面、严格评估多模态浏览智能体视觉推理与搜索能力的基准。具体而言，论文引入了VisBrowse-Bench这一新基准，其核心设计原则是确保多模态信息（尤其是视觉原生信息）被整合到推理链中，并且任务的完成本质上依赖于视觉能力，从而弥补现有基准在评估视觉推理能力和忽视推理链中视觉原生信息方面的不足。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕多模态浏览智能体及其评测基准展开，可分为方法类、评测类以及数据合成类。

在方法类研究中，早期基于LLM的系统（如工具增强的Web导航）奠定了迭代检索与推理的基础架构，但仅限于文本处理。随着MLLMs的发展，出现了MMSearch-R1、WebWatcher、DeepMMSearch-R1、Skywork-R1V4和SenseNova-MARS等工作，它们通过引入图像裁剪等工具或强化训练数据来提升多模态搜索能力。然而，这些方法在细粒度视觉理解方面仍存在不足。

在评测类研究中，现有基准如MMSearch首次将视觉内容纳入查询，但可能通过反向图像搜索工具将视觉推理简化为文本调用，且问题复杂度有限。BrowseComp-VL通过增加搜索轮次来深化检索，VDR-Bench采用多轮裁剪策略避免文本捷径，而MMSearch-Plus和MM-BrowseComp则强调基于细粒度视觉特征的搜索，但其证据常涉及无法公开访问的视频或文件。本文提出的VisBrowse-Bench与这些工作的区别在于：它专注于视觉原生搜索，通过人工专家构建的公开数据确保视觉证据必须融入搜索链，并采用多模态证据交叉验证来严格评估模型的视觉推理能力，弥补了现有基准在细粒度图像理解和持续多跳推理方面的不足。

在数据合成类方面，WebWatcher等工作设计了数据合成流程以生成高质量多模态训练数据，而本文则通过多阶段人工构建与验证来确保数据的可靠性与评估的严谨性。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为VisBrowse-Bench的新基准测试，并设计一个配套的智能体工作流来解决现有基准在评估视觉推理能力和忽视网页原生视觉信息方面的不足。

**核心方法与架构设计**：
论文的核心方法是创建一个专门针对“视觉原生搜索”的评估基准。该基准包含169个经过人工精心构建和验证的视觉问答实例，覆盖媒体、生活、艺术等七大领域。其数据构建遵循两个关键原则：1) **多模态信息整合**：要求智能体在查询理解和证据获取阶段都必须主动处理视觉和文本信息，搜索空间由交错的文本文档和视觉资产组成；2) **视觉能力强制要求**：所有视觉信息在结构上都是不可或缺的，无法被文本描述替代，从而强制模型调用空间定位、属性感知和关系解析等核心视觉能力。数据通过专家主导的多阶段流水线构建，包括实体-事件-视觉信息的迭代遍历，形成至少包含两个视觉证据的多跳推理链，并经过严格的多层验证以确保质量。

**关键技术组件与工作流**：
为了在该基准上实例化多模态深度搜索范式，论文设计了一个全面的**智能体工作流**。该工作流是一个闭环系统，使多模态大语言模型能够通过迭代调用工具与真实网络环境交互。工作流配备了五个核心工具：
1.  **文本搜索**：根据自然语言查询返回候选网页信息。
2.  **图像搜索**：根据文本查询检索缺失的视觉证据及相关网页。
3.  **反向图像搜索**：根据图像查询检索相似图像及相关网页。
4.  **图像裁剪**：提取图像中的感兴趣区域以支持局部视觉推理和查询。
5.  **网页访问**：访问特定URL并基于查询提取结构化网页信息，由LLM进行压缩和推理。

智能体通过解析多模态查询来制定初始搜索策略，根据当前证据缺口调用适当工具，处理返回结果以更新内部状态，并优化后续查询，直到收集到足够的证据进行答案合成。

**创新点**：
1.  **基准设计的创新**：VisBrowse-Bench是首个系统性地将**视觉证据**深度融入搜索和推理链的基准，强调“用图像思考”和跨图像推理，填补了现有基准的空白。
2.  **数据构建的严谨性**：通过专家驱动的迭代遍历流程构建多跳视觉证据链，并实施严格的实例级和语料级验证，确保了问题的高质量和求解的确定性。
3.  **评估范式的完整性**：提出的智能体工作流通过多工具协同，模拟了真实浏览场景中动态、交错地获取与整合多模态证据的过程，防止模型退化为单模态搜索模式，从而能更全面、真实地评估模型的视觉原生搜索能力。

### Q4: 论文做了哪些实验？

论文在提出的VisBrowse-Bench基准上进行了全面的实验评估。实验设置方面，评估了闭源、开源和深度研究三类多模态大语言模型（MLLMs），包括Gemini、GPT、Claude、Kimi、Qwen等系列共12个具体模型。为了量化工具使用对性能的影响，每个模型在三种逐步增强的工具使用方法下进行评估：1）直接回答（Direct Answer），仅依赖模型内部参数知识；2）增加文本搜索（+ TS），允许使用文本搜索和网页访问工具；3）增加图像搜索（+ IS），允许使用全部工具（包括图像搜索）来收集视觉和文本证据。评估使用准确率（%）作为指标，通过正则表达式提取模型最终答案，并采用GPT-5.1作为评判模型（LLM-as-Judge）来比对答案与标准答案。

主要结果如下：在最具挑战性的“+ IS”设置下，所有模型表现均不理想，突显了基准的难度。表现最佳的Claude-4.6-Opus准确率仅为47.6%，专为深度研究设计的o3-Deep-Research模型准确率为41.1%，而最佳开源模型Qwen3-VL-235B-A22B的准确率仅为14.2%。实验分析表明：1）所有模型在直接回答模式下表现均很差，证明了基准任务对模型参数化知识而言极具挑战性；2）引入文本搜索（+ TS）能普遍提升模型性能（例如Claude-4.6-Opus从27.2%提升至42.6%），但提升有限，说明仅靠文本检索不足以解决问题；3）进一步引入图像搜索（+ IS）能带来额外性能增益（如Claude-4.6-Opus进一步提升至47.6%，Kimi-K2.5从21.9%大幅提升至41.4%），证明了主动收集视觉证据的必要性和所提框架的有效性。此外，工具使用分析显示，不同模型对工具（如image_search）的偏好差异显著，这与它们的性能表现相关。

### Q5: 有什么可以进一步探索的点？

该论文提出的VisBrowse-Bench在评估视觉原生搜索方面迈出了重要一步，但仍存在一些局限性和可深入探索的方向。首先，基准规模较小（仅169个实例），覆盖的领域和任务类型有限，未来可扩展至更复杂、动态的实时网页环境，并纳入更多交互式任务（如表单填写、动态内容操作）。其次，当前工作流虽整合了多模态工具，但智能体决策的自主性和效率仍有提升空间，例如引入强化学习来优化工具调用策略，或设计更精细的视觉注意力机制以降低冗余信息处理。此外，基准主要关注检索与验证，未来可探索需要多轮推理、跨页面信息整合的长程任务，并评估智能体在模糊或冲突多模态证据下的鲁棒性。最后，现有评估仅基于准确率，未来可加入效率、成本等指标，推动实用化浏览智能体的发展。

### Q6: 总结一下论文的主要内容

该论文针对多模态浏览智能体在视觉搜索任务中的评估不足问题，提出了一个新的基准测试VisBrowse-Bench。现有基准存在两大局限：对视觉推理能力评估不充分，以及在推理链中忽略了网页原生视觉信息。为此，作者构建了一个包含169个视觉问答实例的数据集，涵盖多个领域，并通过文本-图像检索与联合推理进行多模态证据交叉验证，以评估模型在搜索过程中的视觉推理能力。数据由专家通过多阶段流程构建并经过严格人工验证。

论文的核心贡献在于引入了“视觉原生搜索”这一新任务，并设计了相应的智能体工作流程，驱动浏览智能体在搜索过程中主动收集和推理视觉信息。作者使用该工作流程对开源和闭源模型进行了全面评估。实验结果表明，即使表现最好的Claude-4.6-Opus模型准确率也仅为47.6%，而专有的Deep Research模型o3-deep-research准确率为41.1%，这凸显了当前多模态大语言模型在复杂视觉推理搜索任务上面临的严峻挑战，也证明了该基准的必要性和重要意义。
