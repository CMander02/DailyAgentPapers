---
title: "From Verbatim to Gist: Distilling Pyramidal Multimodal Memory via Semantic Information Bottleneck for Long-Horizon Video Agents"
authors:
  - "Niu Lian"
  - "Yuting Wang"
  - "Hanshu Yao"
  - "Jinpeng Wang"
  - "Bin Chen"
date: "2026-03-02"
arxiv_id: "2603.01455"
arxiv_url: "https://arxiv.org/abs/2603.01455"
pdf_url: "https://arxiv.org/pdf/2603.01455v1"
github_url: "https://github.com/EliSpectre/MM-Mem"
categories:
  - "cs.CV"
  - "cs.AI"
  - "cs.CL"
  - "cs.IR"
  - "cs.MM"
tags:
  - "Memory & Context Management"
  - "Perception & Multimodal"
relevance_score: 8.5
taxonomy:
  capability:
    - "Memory & Context Management"
    - "Perception & Multimodal"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "MM-Mem (pyramidal multimodal memory architecture), Semantic Information Bottleneck (SIB), SIB-GRPO"
  primary_benchmark: "N/A"
---

# From Verbatim to Gist: Distilling Pyramidal Multimodal Memory via Semantic Information Bottleneck for Long-Horizon Video Agents

## 原始摘要

While multimodal large language models have demonstrated impressive short-term reasoning, they struggle with long-horizon video understanding due to limited context windows and static memory mechanisms that fail to mirror human cognitive efficiency. Existing paradigms typically fall into two extremes: vision-centric methods that incur high latency and redundancy through dense visual accumulation, or text-centric approaches that suffer from detail loss and hallucination via aggressive captioning. To bridge this gap, we propose MM-Mem, a pyramidal multimodal memory architecture grounded in Fuzzy-Trace Theory. MM-Mem structures memory hierarchically into a Sensory Buffer, Episodic Stream, and Symbolic Schema, enabling the progressive distillation of fine-grained perceptual traces (verbatim) into high-level semantic schemas (gist). Furthermore, to govern the dynamic construction of memory, we derive a Semantic Information Bottleneck objective and introduce SIB-GRPO to optimize the trade-off between memory compression and task-relevant information retention. In inference, we design an entropy-driven top-down memory retrieval strategy, which first tries with the abstract Symbolic Schema and progressively "drills down" to the Sensory Buffer and Episodic Stream under high uncertainty. Extensive experiments across 4 benchmarks confirm the effectiveness of MM-Mem on both offline and streaming tasks, demonstrating robust generalization and validating the effectiveness of cognition-inspired memory organization. Code is available at https://github.com/EliSpectre/MM-Mem.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态大语言模型在长时程视频理解任务中面临的挑战。研究背景是，当前基于多模态大语言模型的智能体在短期推理上表现出色，但受限于有限的上下文窗口和静态的记忆机制，难以高效处理连续、无界的多模态信息流，无法模仿人类认知的高效性。现有方法主要存在两种不足：一是以视觉为中心的方法（如密集累积视觉帧）会引入高延迟和冗余；二是以文本为中心的方法（如通过激进描述将视频转为文本）会丢失关键细节并导致幻觉，且现有方法多为静态，缺乏动态的多模态记忆管理。本文要解决的核心问题是，如何设计一种高效、动态的多模态记忆架构，以桥接细粒度感知与高层语义认知之间的鸿沟，从而在保证长时程依赖关系的同时，避免信息冗余或损失，实现类似人类“逐字记录”与“要点提取”并行的记忆机制，最终提升智能体在长视频理解和在线流式任务中的性能与泛化能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在方法类中，现有工作主要分为两大范式。一是以视觉为中心的方法，通过密集采样或令牌压缩来扩展上下文，但计算冗余高、延迟大。二是以文本为中心的方法，将视频转换为文本描述或结构化记忆以提高效率，但会丢失细粒度视觉细节并可能导致幻觉。本文提出的MM-Mem属于方法创新，它通过金字塔式多模态记忆架构，结合了高层文本记忆（用于粗定位）和低层视觉记忆（用于细节检索），旨在平衡效率与视觉保真度。

在应用类中，基于LLM的智能体已广泛探索记忆机制，如缓存层次、遗忘曲线或强化学习控制，但这些系统大多仍以文本为中心，未能有效对齐跨模态信息。另一方面，多模态智能体的记忆研究尚不充分，现有工作（如M3-Agent）依赖预定义结构和固定流程，在开放长视野环境中泛化能力有限。本文的MM-Mem针对长视野视频智能体设计，提供了一个灵活、可泛化的记忆系统，支持长期多模态交互。

在评测类上，现有研究缺乏统一的长视频理解基准。本文通过在4个基准上进行离线与流式任务实验，验证了所提方法的有效性，并强调了认知启发的记忆组织的优势。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MM-Mem的金字塔式多模态记忆架构来解决长时程视频理解中存在的上下文窗口限制和静态记忆机制效率低下的问题。其核心方法借鉴了模糊痕迹理论，将记忆分层组织，并引入语义信息瓶颈目标来优化记忆的动态构建与检索。

整体框架采用三层金字塔结构，自底向上构建记忆：**感官缓冲区**存储细粒度的视觉证据（如关键帧的视觉表示和文本轨迹），**情节流**通过选择性编码和合并操作将感官条目整合为紧凑的事件级抽象，**符号图式**则在情节流之上构建知识图谱，存储高层语义实体和关系。这种设计实现了从“逐字”细节到“要点”语义的渐进式蒸馏。

关键技术包括：1）**SIB-GRPO动态记忆管理**：将感官到情节的转换建模为随机压缩过程，通过强化学习优化记忆管理器策略。该策略基于语义信息瓶颈目标，在奖励函数中平衡任务奖励（如VQA准确率）、记忆长度惩罚以及与参考策略的KL散度，从而在压缩冗余信息的同时保留任务相关语义。2）**熵驱动的自上而下检索机制**：在推理时，首先查询高层的符号图式以快速获取语义要点；若答案分布熵值高于阈值，则逐步“下钻”到情节流和感官缓冲区获取更细粒度的证据，直到熵值降低到可接受水平。这种基于不确定性的自适应检索平衡了证据覆盖与计算资源。

创新点主要体现在：将认知科学中的分层记忆理论（模糊痕迹理论、反向层次理论）与信息瓶颈原则相结合，设计了兼具压缩效率和语义保真度的记忆组织方式；提出了SIB-GRPO这一融合信息瓶颈与群体相对策略优化的训练方法，实现对离散文本记忆序列的端到端优化；并通过熵驱动的检索策略实现了动态、高效的记忆访问。实验表明，该方法在多个长视频理解基准上取得了优异性能，验证了其有效性和泛化能力。

### Q4: 论文做了哪些实验？

论文在四个基准测试上进行了全面实验。实验设置方面，模型基于Qwen3-VL-8B构建，使用NVIDIA A100 80GB GPU进行训练和推理，并采用SIB-GRPO方法进行微调。文本检索使用bge-large-en-v1.5和bge-reranker-v2-m3，视觉检索则基于基础模型的视觉编码器提取CLIP风格嵌入进行片段级检索。

使用的数据集/基准测试包括：1) 标准长视频数据集Video-MME（包含短、中、长三种时长共900个视频和2700个问题）和MLVU（开发集包含9个任务，视频时长3分钟至2小时）；2) 标准在线流式数据集VStream-QA（包含VStream-QA-Ego和VStream-QA-Movie）；3) 自构建的以自我为中心的长视频数据集HD-EPIC++（包含156个视频）。评估指标主要为准确率，VStream-QA则额外使用GPT-4o-mini作为自动评判器并报告平均分数。

对比方法涵盖三类：a) 专有多模态模型（如Gemini 1.5 Pro）；b) 开源MLLMs（如Qwen2-VL-72B、LLaVA-Video-7B）；c) 面向长视频理解的基于智能体的系统（如Vgent、Flash-VStream）。

主要结果显示，MM-Mem在各项基准上均取得优异性能。在Video-MME上，相比最强的智能体基线Vgent，MM-Mem获得了5.1%的相对提升；在MLVU上获得7.1%的提升（M-Avg指标）。在VStream-QA-Ego流式理解任务中，MM-Mem以62.5%的准确率和4.1的平均分数，超越之前最佳方法Flash-VStream达5.9%（准确率）和5.2%（分数）。在HD-EPIC++上，MM-Mem以30.28%的准确率超越所有基线，比最强的Qwen3-VL-8B高出4.40个百分点。消融实验证实了SIB-GRPO和金字塔内存架构的有效性，移除任一组件均导致性能下降，尤其在长视频上最为明显。

### Q5: 有什么可以进一步探索的点？

本文提出的MM-Mem架构在长时视频理解上取得了显著进展，但仍存在一些局限性和可进一步探索的方向。首先，其分层记忆构建过程虽然提升了推理精度，但计算开销较大，未来可研究更轻量化的蒸馏方法或异步并行策略，以适配边缘计算等资源受限场景。其次，系统高度依赖上游感知模块（如目标检测和场景分割）的质量，若感知结果存在偏差，可能影响后续记忆蒸馏的可靠性。因此，探索更鲁棒的跨模态对齐机制，或设计端到端的联合优化框架，是重要的改进方向。

此外，论文基于模糊痕迹理论将记忆分为感知缓冲、情景流和符号图式三层，但各层之间的信息转换机制仍可深化。例如，如何动态调整语义信息瓶颈的压缩强度，以适应不同任务的信息密度需求，值得进一步理论分析和实验验证。检索策略上，当前采用基于熵的自顶向下机制，未来可引入更细粒度的不确定性度量，或结合强化学习来优化检索路径。最后，该架构目前主要针对视频序列，未来可扩展至更复杂的多模态交互场景（如具身智能），研究其在动态环境中的在线学习和记忆更新能力。

### Q6: 总结一下论文的主要内容

本论文针对多模态大语言模型在长时程视频理解中面临的上下文窗口限制和静态记忆机制效率低下问题，提出了基于模糊痕迹理论的MM-Mem金字塔多模态记忆架构。其核心贡献在于设计了一个分层记忆结构，包含感觉缓冲区、情景流和符号图式，能够将细粒度的感知痕迹逐步提炼为高层语义图式。方法上，论文提出了语义信息瓶颈目标及SIB-GRPO优化方法，以权衡记忆压缩与任务相关信息保留；在推理阶段，则设计了基于熵的自顶向下记忆检索策略，根据不确定性从抽象图式逐步下钻至具体细节。实验表明，该框架在多个基准测试中取得了先进性能，验证了受认知启发的记忆组织在提升长时程视频智能体理解效率与泛化能力方面的有效性。
