---
title: "Towards Long-horizon Agentic Multimodal Search"
authors:
  - "Yifan Du"
  - "Zikang Liu"
  - "Jinbiao Peng"
  - "Jie Wu"
  - "Junyi Li"
  - "Jinyang Li"
  - "Wayne Xin Zhao"
  - "Ji-Rong Wen"
date: "2026-04-14"
arxiv_id: "2604.12890"
arxiv_url: "https://arxiv.org/abs/2604.12890"
pdf_url: "https://arxiv.org/pdf/2604.12890v1"
github_url: "https://github.com/RUCAIBox/LMM-Searcher"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Multimodal Agent"
  - "Long-horizon Planning"
  - "Tool Use"
  - "Visual Representation"
  - "Data Synthesis"
  - "Agent Fine-tuning"
  - "Benchmark Evaluation"
relevance_score: 8.0
---

# Towards Long-horizon Agentic Multimodal Search

## 原始摘要

Multimodal deep search agents have shown great potential in solving complex tasks by iteratively collecting textual and visual evidence. However, managing the heterogeneous information and high token costs associated with multimodal inputs over long horizons remains a critical challenge, as existing methods often suffer from context explosion or the loss of crucial visual signals. To address this, we propose a novel Long-horizon MultiModal deep search framework, named LMM-Searcher, centered on a file-based visual representation mechanism. By offloading visual assets to an external file system and mapping them to lightweight textual identifiers (UIDs), our approach mitigates context overhead while preserving multimodal information for future access. We equip the agent with a tailored fetch-image tool, enabling a progressive, on-demand visual loading strategy for active perception. Furthermore, we introduce a data synthesis pipeline designed to generate queries requiring complex cross-modal multi-hop reasoning. Using this pipeline, we distill 12K high-quality trajectories to fine-tune Qwen3-VL-Thinking-30A3B into a specialized multimodal deep search agent. Extensive experiments across four benchmarks demonstrate that our method successfully scales to 100-turn search horizons, achieving state-of-the-art performance among open-source models on challenging long-horizon benchmarks like MM-BrowseComp and MMSearch-Plus, while also exhibiting strong generalizability across different base models. Our code will be released in https://github.com/RUCAIBox/LMM-Searcher.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态深度搜索智能体在长视野任务中面临的上下文爆炸和视觉信息丢失问题。随着多模态搜索智能体的发展，它们能够通过迭代收集文本和视觉证据来解决复杂任务，但长视野搜索过程中积累的异构信息（尤其是高令牌成本的图像数据）会导致上下文长度急剧膨胀，传统基于文本的上下文压缩方法难以直接迁移，因为视觉数据具有根本不同的格式和表示。现有方法常采用启发式策略丢弃中间图像数据以控制成本，但这可能导致关键视觉信号丢失，损害信息完整性，限制智能体在长视野场景下的扩展能力。

因此，本文的核心问题是：如何在深度搜索过程中有效管理和处理累积的多模态上下文，以平衡信息保留与计算开销？为此，论文提出了一种基于文件视觉表示机制的长视野多模态深度搜索框架LMM-Searcher。其核心思路是将视觉资产卸载到外部文件系统，并映射为轻量级文本标识符，从而在保留多模态信息供未来访问的同时，通过按需加载策略减少上下文开销。此外，论文还设计了支持复杂跨模态多跳推理的数据合成流程，并基于此训练出专用的多模态深度搜索智能体，实现在长视野任务中的可扩展高效搜索。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类。

在方法类研究中，语言驱动的深度搜索代理（Language-based Deep Search Agent）通过检索增强生成（RAG）或集成搜索工具来突破大语言模型的知识边界，但其仅支持文本模态，无法处理多模态查询。多模态深度搜索代理（Multimodal Deep Search Agent）则通过为多模态大模型（MLLMs）配备视觉与语言插件（如物体检测、OCR），或将视觉操作内化为显式推理步骤的“thinking-with-image”范式，增强了模型的交互与推理能力。近期研究进一步将搜索引擎深度集成到MLLMs的推理链中，以支持复杂任务。

本文提出的LMM-Searcher与上述工作密切相关，但存在关键区别。与语言代理相比，本文框架本质上是多模态的。与现有多模态代理相比，本文的核心创新在于针对长视野任务中多模态信息管理和令牌成本高的挑战，提出了基于文件的视觉表示机制和渐进式按需视觉加载策略，有效缓解了上下文爆炸和关键视觉信号丢失的问题，从而实现了长达100轮的搜索。此外，本文还专门构建了用于训练和评估的复杂多跳推理数据合成流程。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为LMM-Searcher的新型长视野多模态深度搜索框架来解决长视野多模态搜索中信息异构、上下文爆炸和关键视觉信号丢失的挑战。其核心方法是基于文件的视觉表示机制，将感知与推理解耦。

整体框架包含两个核心部分：创新的上下文管理机制和专门的智能体训练流程。在架构设计上，框架作为中间件，在环境返回的原始交错文档（包含文本和原始图像）进入智能体上下文之前，自动索引所有视觉项，将其永久保存到外部文件系统，并用轻量级文本标识符（UID）替换所有原始图像。这样，智能体仅接收搜索结果的轻量级表示，有效避免了上下文爆炸。

主要模块/组件包括：
1.  **基于文件的视觉表示与映射**：定义持久映射函数 f: I → U，将高维视觉空间I中的每个图像唯一关联到一个UID。这确保了视觉内容能以低成本文本指针的形式在上下文中高效维护。
2.  **扩展的工具接口**：基于渐进式加载原则重新设计工具，形成由粗到细的感知漏斗：
    *   **搜索工具**（如google_search、image_search）：作为跨模态多跳推理的入口，返回包含文本摘要、图像链接等的结果项。
    *   **浏览工具**：包括`scrape_website`（抓取并总结网页内容，提取并存储所有图像URL）和关键的`fetch_image`工具。后者作为UID空间与视觉空间的桥梁，能按需根据UID从外部文件系统检索对应图像供模型详细检查，实现了主动视觉感知。
    *   **视觉处理工具**（如zoom_in）：支持细粒度视觉推理，对图像进行变换后生成新视觉资产并分配新UID。
3.  **数据合成与模型训练管道**：为了训练智能体有效利用上述机制，论文提出了一个综合训练管道：
    *   **查询合成**：首先从富含视觉内容的网页合成单跳视觉问题，确保问题无法仅凭文本信息回答。然后，以核心实体为起点，构建具有信息不可逆约束的多跳知识图，并对图中关键节点进行模糊化，最终生成需要复杂跨模态多跳推理的扩展多跳视觉问题。
    *   **轨迹数据蒸馏**：结合开源搜索数据集，通过拒绝采样筛选出在40轮交互内能成功回答查询的高质量轨迹，最终得到12K+训练样本。
    *   **模型训练与融合**：使用合成数据对基础模型（Qwen3-VL-30B-A3B-Thinking）进行多轮监督微调，并掩码工具响应以优化推理和工具调用生成。为进一步提升长视野搜索能力，将训练好的多模态模型与具有强大语言深度搜索能力的模型（MiroThinker-1.7-mini）进行参数插值融合（α=0.8），得到最终的LMM-Searcher模型。

创新点在于：
1.  **文件化视觉表示与UID映射**：首创性地通过外部文件系统和UID解耦重型视觉感知与轻型长视野规划，从根本上防止了上下文窗口的爆炸性增长。
2.  **按需渐进式视觉加载策略**：通过`fetch_image`等工具，智能体可以主动、按需地加载高分辨率视觉信息，模拟了人类“记住信息位置，需要时再加载”的认知范式。
3.  **保证信息可靠性的工作流**：UID作为持久语义指针，确保只要推理链中保留UID，就能随时追溯外部文件系统中的原始视觉证据，避免了启发式方法可能造成的信息永久丢失。
4.  **复杂跨模态多跳查询的自动合成管道**：能够生成迫使智能体在整个搜索过程中持续比对多模态信息的高难度查询，为训练长视野搜索能力提供了关键数据。
5.  **模型能力融合**：通过参数插值融合专精多模态搜索的模型与专精语言深度搜索的模型，结合两者优势，增强了模型的泛化与扩展能力。

### Q4: 论文做了哪些实验？

论文在四个基准测试（MM-BrowseComp、MMSearch-Plus、VisBrowse、MMSearch）上进行了广泛的实验。实验设置基于MiroFlow框架进行轨迹推演和答案验证，使用LLaMA-Factory训练框架，以Qwen3-VL-30B-A3B-Thinking为基座模型，使用合成的12K高质量轨迹进行微调，训练3个epoch，全局批次大小为64，学习率为1e-5。评估时最大上下文长度设为128K，最大交互轮数设为30轮以进行公平比较，同时报告了扩展到100轮并采用上下文管理策略（仅保留最近5次工具调用结果）的性能。

对比方法分为三类：直接回答（模型仅依赖参数知识）、智能体工作流（模型可调用工具）以及开源多模态搜索智能体（如MMSearch-R1、WebWatcher、DeepEyesV2等）。主要结果显示，LMM-Searcher-30B在30轮设置下已取得竞争性性能，在启用100轮长视野交互和上下文管理后，性能获得一致提升，在MM-BrowseComp和MMSearch-Plus上达到最先进水平。关键指标包括：在MM-BrowseComp上达到30.1分（100轮），在MMSearch-Plus上达到34.8分（100轮），在VisBrowse上达到48.3分（100轮），在MMSearch上达到72.3分（100轮），平均分为46.4分（100轮）。此外，数据消融实验表明，逐步加入开源视觉查询、文本查询及自合成查询能持续提升性能；工具消融实验证实，移除“fetch-image”工具会导致性能显著下降，尤其在VisBrowse上从58.0降至48.5分，凸显了该工具对获取网页图像信息的重要性。框架对比实验也表明，本文框架能显著提升不同基座模型（如GPT-5、Seed-1.8）在复杂任务上的表现。

### Q5: 有什么可以进一步探索的点？

本文提出的文件化视觉表示和渐进式加载策略虽有效缓解了长程多模态搜索中的上下文爆炸问题，但仍存在一些局限和值得探索的方向。首先，其视觉信息通过轻量级文本标识符（UID）索引，虽节省了上下文长度，但可能损失了原始图像中的细粒度细节和空间关系，这在高精度视觉推理任务中可能成为瓶颈。未来可研究更高效的视觉压缩或分层表示方法，在控制令牌成本的同时保留更多语义信息。

其次，当前框架依赖于预定义的工具（如 fetch-image），其主动感知能力受限于工具的设计。未来可探索更自主的视觉信息获取机制，例如让智能体动态决定何时、以何种分辨率获取图像区域，甚至结合强化学习优化长期信息收集策略。此外，数据合成管道虽能生成多跳推理轨迹，但其多样性和真实世界复杂性可能不足，未来需引入更多元的环境模拟或真实用户交互数据来提升泛化能力。

从系统层面看，该框架在超长程（如千轮以上）互动中的累积误差管理、跨模态信息的长时一致性维护等问题尚未深入探讨。结合世界模型或外部知识库来增强推理的连贯性，或是将文件系统与向量数据库等结合以实现更智能的多模态记忆管理，都是值得尝试的改进思路。最后，该方法的能耗与延迟在实际部署中需进一步优化，例如通过异步加载或预测机制提升响应速度。

### Q6: 总结一下论文的主要内容

该论文针对多模态深度搜索智能体在长视野任务中面临的信息异构性管理和高令牌成本问题，提出了一种名为LMM-Searcher的新型框架。其核心贡献在于设计了一种基于文件的视觉表示机制，将视觉资源卸载到外部文件系统，并映射为轻量级文本标识符，从而在保留多模态信息供未来调用的同时，显著减轻了上下文负担。方法上，框架为智能体配备了定制的图像获取工具，支持渐进式、按需的视觉加载策略以实现主动感知。此外，论文还引入了一个数据合成流程，用于生成需要复杂跨模态多跳推理的查询，并利用该流程蒸馏出12K高质量轨迹来微调基础模型，训练出专用的多模态深度搜索智能体。实验结果表明，该方法能成功扩展到100轮次的搜索视野，在MM-BrowseComp和MMSearch-Plus等具有挑战性的长视野基准测试中达到了开源模型中的最先进性能，并展现出对不同基础模型的强泛化能力。
