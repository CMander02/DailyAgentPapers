---
title: "OpenSeeker: Democratizing Frontier Search Agents by Fully Open-Sourcing Training Data"
authors:
  - "Yuwen Du"
  - "Rui Ye"
  - "Shuo Tang"
  - "Xinyu Zhu"
  - "Yijun Lu"
  - "Yuzhu Cai"
  - "Siheng Chen"
date: "2026-03-16"
arxiv_id: "2603.15594"
arxiv_url: "https://arxiv.org/abs/2603.15594"
pdf_url: "https://arxiv.org/pdf/2603.15594v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Search Agent"
  - "Tool Use"
  - "Data Synthesis"
  - "Open Source"
  - "Agent Training"
  - "Multi-hop Reasoning"
  - "Trajectory Denoising"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# OpenSeeker: Democratizing Frontier Search Agents by Fully Open-Sourcing Training Data

## 原始摘要

Deep search capabilities have become an indispensable competency for frontier Large Language Model (LLM) agents, yet the development of high-performance search agents remains dominated by industrial giants due to a lack of transparent, high-quality training data. This persistent data scarcity has fundamentally hindered the progress of the broader research community in developing and innovating within this domain. To bridge this gap, we introduce OpenSeeker, the first fully open-source search agent (i.e., model and data) that achieves frontier-level performance through two core technical innovations: (1) Fact-grounded scalable controllable QA synthesis, which reverse-engineers the web graph via topological expansion and entity obfuscation to generate complex, multi-hop reasoning tasks with controllable coverage and complexity. (2) Denoised trajectory synthesis, which employs a retrospective summarization mechanism to denoise the trajectory, therefore promoting the teacher LLMs to generate high-quality actions. Experimental results demonstrate that OpenSeeker, trained (a single training run) on only 11.7k synthesized samples, achieves state-of-the-art performance across multiple benchmarks including BrowseComp, BrowseComp-ZH, xbench-DeepSearch, and WideSearch. Notably, trained with simple SFT, OpenSeeker significantly outperforms the second-best fully open-source agent DeepDive (e.g., 29.5% v.s. 15.3% on BrowseComp), and even surpasses industrial competitors such as Tongyi DeepResearch (trained via extensive continual pre-training, SFT, and RL) on BrowseComp-ZH (48.4% v.s. 46.7%). We fully open-source the complete training dataset and the model weights to democratize frontier search agent research and foster a more transparent, collaborative ecosystem.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决前沿搜索智能体（Search Agent）研发领域因高质量训练数据不公开、不透明而导致的“数据鸿沟”问题，从而推动该领域的民主化和开源生态发展。

研究背景是，在信息爆炸时代，从互联网进行深度搜索已成为大型语言模型（LLM）智能体的核心能力。尽管近年来搜索智能体性能提升迅速（例如在BrowseComp等基准测试上分数大幅跃升），但其开发几乎被谷歌、OpenAI等资金雄厚的工业界巨头所垄断。现有开源努力（如Kimi、Minimax等仅开源模型权重）或学术研究，普遍存在关键不足：要么完全不公开训练数据，要么只提供部分数据，要么其性能无法与工业界前沿方案竞争。这种高质量训练数据的长期稀缺和封闭，严重阻碍了更广泛的研究社区在该领域进行创新、复现和深入探索。

因此，本文要解决的核心问题是：如何通过技术创新，生成高质量、可扩展且完全开源的训练数据，并基于此训练出一个能达到前沿性能水平的搜索智能体，以打破工业界的数据垄断，为学术界和开源社区提供一个透明、完整的研发基础。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕基于大语言模型的搜索智能体展开，可分为三类：

**工业界闭源与半开源方案**：以OpenAI的Deep Research为代表，以及后续的Kimi-Researcher、Gemini Deep Research等，它们完全闭源。近期也出现了如Kimi K2、GLM 4.5、Tongyi DeepResearch等“开源权重”模型，但其训练数据均未公开，形成了“数据护城河”，阻碍了社区研究。

**学术界开源框架与智能体**：研究社区提出了WebDancer、WebSailor、DeepDive、MiroThinker等多个框架或智能体。然而，这些工作要么未公开模型或数据，要么仅释放少量数据，且普遍存在数据保真度低的问题，导致其性能无法与工业界前沿系统竞争。

**本文的定位与区别**：OpenSeeker直接针对上述“高质量训练数据稀缺”的核心瓶颈。与工业方案不同，它**完全开源**了模型权重和**全部**高质量训练数据。与现有学术开源工作相比，OpenSeeker不仅公开了完整数据合成流程，其数据通过事实锚定、可扩展可控的QA合成以及去噪轨迹合成两大技术创新，实现了极高的保真度。因此，仅用1.17万样本进行单次SFT训练，便在多个基准测试中达到了最先进的性能，首次由纯学术团队实现了媲美甚至超越工业界前沿搜索智能体的效果，真正推动了该领域的民主化。

### Q3: 论文如何解决这个问题？

论文通过构建一个高质量、完全开源的训练数据集来解决高性能搜索代理开发中的数据稀缺问题。其核心方法包含两个相辅相成的技术创新：基于事实的可扩展可控问答合成，以及去噪轨迹合成。

**整体框架与主要模块**：
1.  **基于事实的可扩展可控问答合成框架**：该框架旨在从真实的网页图结构中逆向工程出复杂的多跳推理问题。其流程包括：
    *   **图扩展**：从种子网页节点出发，沿超链接扩展，形成一个局部依赖子图，作为连贯的知识基础。
    *   **实体提取**：从子图中提炼出与核心主题相关的关键实体，构建一个去除了文本噪声、保留逻辑路径的“实体子图”。
    *   **问题生成**：基于实体子图的结构，强制要求生成必须遍历多个节点才能解答的初始问题，确保多步推理需求。
    *   **实体混淆**：将实体子图中的具体实体替换为模糊的描述，构建“模糊实体子图”，以模拟真实用户的模糊查询，防止智能体通过关键词直接搜索走捷径。
    *   **问题混淆与双重标准验证**：基于模糊实体子图重写问题，生成最终挑战性问题。随后通过双重标准进行严格筛选：**难度标准**确保基础模型在无工具条件下无法正确回答，强制外部信息搜索；**可解性标准**确保在提供完整实体子图（即“神谕”上下文）时模型能推导出正确答案，保证逻辑有效性。

2.  **去噪轨迹合成方法**：该模块旨在为合成的复杂问题生成高质量、可泛化的工具调用轨迹（推理步骤和行动序列）。其核心是**回顾性总结机制**：
    *   在轨迹合成过程中，采用“总结历史 + 原始近期”的上下文构建协议。具体而言，在生成当前步骤的决策时，模型能看到前一步的**原始工具响应**（保证信息完整），但更早的步骤则使用其响应的**语义摘要**来替代原始冗长内容。
    *   这种动态上下文去噪策略，通过在每个步骤后对前一步的原始观察进行总结并更新历史，有效过滤了噪声，使教师模型能够在长序列中生成清晰、高质量的推理和行动。
    *   关键的不对称设计：**合成阶段**使用包含摘要的干净上下文来生成“黄金”轨迹；而**训练阶段**，学生模型则使用包含所有原始、嘈杂工具响应的完整上下文进行监督学习。这迫使学生模型内化去噪和信息提取能力，从而学会处理真实世界中的非结构化数据。

**创新点**：
*   **事实基础**：直接从真实网页拓扑结构生成问题，而非依赖LLM凭空生成，从根本上避免了幻觉风险，确保每个训练样本都基于可验证的真实数据。
*   **可扩展性与可控性**：利用网页图的拓扑连接性，通过变换种子页面或调整图配置，理论上可以生成无限多样、非重复的样本。通过调整子图大小（k）等参数，可以精确控制推理的复杂度和信息覆盖范围，实现课程学习。
*   **轨迹合成的去噪与泛化**：提出的回顾性总结机制和“合成-训练”上下文不对称设计，是核心创新。它既保证了合成轨迹的高质量，又强制模型在训练中学会从噪声中提取关键信息，从而获得强大的泛化到真实嘈杂环境的能力。

### Q4: 论文做了哪些实验？

实验设置方面，OpenSeeker模型基于Qwen3-30B-A3B-Thinking-2507初始化，总参数量为300亿，推理时激活30亿参数。工具调用上限设为200次，上下文窗口大小为256k。训练仅使用简单的监督微调（SFT），在11700个合成样本上进行单次训练，未进行数据过滤或超参数调优。

评估在四个基准测试上进行：BrowseComp（英语多步导航与硬信息定位）、BrowseComp-ZH（中文对应任务，因资源限制在200样本子集上评估）、xbench-DeepSearch（复杂深度研究能力如规划与综合）以及WideSearch（广泛信息检索的可靠性）。

对比方法涵盖三类基线：1）闭源专有模型（如Claude系列、OpenAI-o3、GPT-5-High）；2）大规模开源模型（>300亿参数，如DeepSeek-V3.2、GLM-4.7）；3）约300亿参数模型（如MiroThinker、DeepDive-32B、WebSailor-V2、Tongyi DeepResearch）。

主要结果显示，OpenSeeker在多个基准上达到前沿性能。关键指标包括：在BrowseComp上得分为29.5%，显著优于最佳全开源代理DeepDive的15.3%；在BrowseComp-ZH上达到48.4%，超越工业竞品Tongyi DeepResearch的46.7%（后者使用了持续预训练、SFT和RL）；在xbench上得分为74.0%，在WideSearch英文子集上F1得分为59.4%。实验还表明，在相同SFT训练设置下，OpenSeeker仅用11700个样本就大幅优于使用更多数据（如MiroThinker的147k样本）或类似数据量（如WebSailor-V2与WebLeaper组合的10k-15k样本）的基线，验证了其数据合成方法的高质量与高效性。

### Q5: 有什么可以进一步探索的点？

本文提出的数据合成方法虽在事实性、可扩展性和可控性上优势明显，但仍存在局限。首先，其依赖的网页拓扑图主要基于维基百科等结构化知识源，对开放互联网中动态、非结构化信息的覆盖和处理能力有待验证。其次，当前方法通过实体混淆生成查询，可能限制了查询风格的多样性和对真实用户模糊、口语化需求的模拟。未来研究可探索更广泛的网页来源（如社交媒体、论坛）以增强数据真实性，并引入对抗生成或用户模拟技术来合成更贴近实际、更具挑战性的搜索任务。此外，论文仅采用监督微调（SFT），未来可结合强化学习（RL）或课程学习进一步优化智能体的决策泛化能力和复杂场景下的鲁棒性。最后，将搜索能力与规划、工具使用等其它智能体模块进行端到端联合训练，也是一个值得探索的方向。

### Q6: 总结一下论文的主要内容

该论文针对前沿大语言模型搜索代理训练数据稀缺且被工业界垄断的问题，提出了首个完全开源的、达到前沿性能的搜索代理OpenSeeker。其核心贡献在于通过两项技术创新，仅用少量合成数据即可高效训练高性能搜索模型。方法上，首先提出了基于事实、可扩展且可控的问答合成技术，通过逆向工程网络图进行拓扑扩展和实体混淆，以生成覆盖面和复杂度可控的复杂多跳推理任务。其次，提出了去噪轨迹合成技术，利用回顾性总结机制净化轨迹，从而引导教师大模型生成高质量的动作序列。实验表明，仅通过单次监督微调、使用1.17万个合成样本训练的OpenSeeker，在BrowseComp等多个基准测试中达到了最先进的性能，甚至超越了部分依赖大量资源和复杂训练流程的工业界模型。论文的主要结论是，所提出的数据合成方法能有效生成高保真训练数据，通过完全开源模型和数据集，有望打破该领域的数据壁垒，推动一个更透明、协作的研究生态。
