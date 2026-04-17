---
title: "DR$^{3}$-Eval: Towards Realistic and Reproducible Deep Research Evaluation"
authors:
  - "Qianqian Xie"
  - "Qingheng Xiong"
  - "He Zhu"
  - "Tiantian Xia"
  - "Xueming Han"
  - "Fanyu Meng"
  - "Jiakai Wang"
  - "Zhiqi Bai"
  - "Chengkang Jiang"
  - "Zhaohui Wang"
  - "Yubin Guo"
  - "Yuqing Wen"
  - "Jiayang Mao"
  - "Zijie Zhang"
  - "Shihao Li"
  - "Yanghai Wang"
  - "Yuxiang Ren"
  - "Junlan Feng"
  - "Jiaheng Liu"
date: "2026-04-16"
arxiv_id: "2604.14683"
arxiv_url: "https://arxiv.org/abs/2604.14683"
pdf_url: "https://arxiv.org/pdf/2604.14683v1"
categories:
  - "cs.AI"
tags:
  - "Benchmark"
  - "Evaluation"
  - "Multi-Agent"
  - "Retrieval"
  - "Multimodal"
  - "Long-Horizon Tasks"
  - "Report Generation"
  - "Research Agent"
relevance_score: 8.5
---

# DR$^{3}$-Eval: Towards Realistic and Reproducible Deep Research Evaluation

## 原始摘要

Deep Research Agents (DRAs) aim to solve complex, long-horizon research tasks involving planning, retrieval, multimodal understanding, and report generation, yet their evaluation remains challenging due to dynamic web environments and ambiguous task definitions. We propose DR$^{3}$-Eval, a realistic and reproducible benchmark for evaluating deep research agents on multimodal, multi-file report generation. DR$^{3}$-Eval is constructed from authentic user-provided materials and paired with a per-task static research sandbox corpus that simulates open-web complexity while remaining fully verifiable, containing supportive documents, distractors, and noise. Moreover, we introduce a multi-dimensional evaluation framework measuring Information Recall, Factual Accuracy, Citation Coverage, Instruction Following, and Depth Quality, and validate its alignment with human judgments. Experiments with our developed multi-agent system DR$^{3}$-Agent based on multiple state-of-the-art language models demonstrate that DR$^{3}$-Eval is highly challenging and reveals critical failure modes in retrieval robustness and hallucination control. Our code and data are publicly available.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决深度研究智能体（DRAs）在复杂、长周期研究任务中缺乏真实、可复现且可控的评估基准这一核心问题。研究背景是，随着大语言模型的发展，DRAs能够自主执行涉及规划、检索、多模态理解和生成有据报告的研究任务，但其评估面临巨大挑战。现有方法存在明显不足：例如，DeepResearch Bench依赖实时网络访问，导致结果难以复现且评估模糊；DRBench虽关注企业报告生成，但忽略了真实研究中常见的噪声和误导信息；DeepResearchGym采用了沙箱框架提升了复现性，但其任务仅基于文本查询，缺乏真实用户多模态材料和工作流的支撑。这些方法在真实性、可控性和可评估性之间存在矛盾，未能充分模拟真实研究环境的复杂性。

因此，本文的核心问题是：如何构建一个既能反映真实世界研究复杂性（包括多模态用户材料、噪声信息、隐含研究意图），又能保证评估过程可复现、可控制且无歧义的基准。为此，论文提出了DR³-Eval基准，它基于真实用户提供的多模态材料构建任务，并为每个任务配备一个静态的、模拟开放网络复杂性的研究沙箱语料库，其中包含支持性文档、干扰项和噪声。该基准通过反向构建方法确保每个查询都有明确可验证的答案路径，从而消除了评估模糊性。同时，论文还引入了一个多维评估框架，从信息召回、事实准确性、引用覆盖、指令遵循和深度质量等方面进行细粒度评估，以全面衡量DRAs在证据获取和分析报告生成方面的性能。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为**评测基准**和**评估方法**两大类，并与现有工作存在显著区别。

在**评测基准**方面，相关工作主要分为两类。一类是面向通用问答（QA）任务的基准，如GAIA、HLE、BrowseComp-Plus、DocBench和MMLongBench-Doc。这些基准主要评估模型在信息检索和简单推理上的能力，任务形式单一，且大多不支持多模态输入或真实用户文件。另一类是面向报告生成任务的基准，如DRBench、Deep Research Bench、Deep Scholar Bench、DEER、LiveResearch Bench和DeepResearchGym。这些基准虽然聚焦于更复杂的报告生成，但普遍存在局限性：或仅依赖动态网络（导致结果不可复现），或仅使用静态沙箱（缺乏真实噪声和干扰信息），且大多不支持多模态用户文件。

本文提出的DR³-Eval与上述工作的核心区别在于，它**首次将用户提供的多模态真实文件与一个包含支持性文档、干扰项和噪声的静态研究沙箱语料库相结合**。如表1所示，DR³-Eval是唯一一个同时支持“用户文件”、“沙箱语料库”、“多模态”、“真实场景”、“多文件”和“逆向构建”的基准，从而在保证评估**可复现性**的同时，最大程度地模拟了真实网络研究的**复杂性**。

在**评估方法**方面，随着任务从简单问答转向报告生成，传统评估指标已不适用。当前主流做法是采用“LLM-as-a-judge”框架进行细粒度评估。本文在此基础上，提出了一个包含信息召回、事实准确性、引用覆盖度、指令遵循和深度质量的多维评估框架，并验证了其与人类判断的一致性，为深度研究报告的自动评估提供了更全面、可靠的方案。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为DR³-Agent的多智能体系统来解决深度研究任务评估的挑战。该系统基于MiroFlow框架构建，专门针对DR³-Eval基准中涉及的多模态用户文件和静态沙箱语料库任务而设计。

其核心架构采用分层设计，以主智能体作为系统的推理中枢。主智能体直接集成了感知工具（如视频、音频解析器），使其能够在全局上下文中综合理解多模态内容，而非进行孤立的提取。这解决了现有开源框架无法直接处理离线封闭沙箱和多模态文件交叉阅读的关键问题。主智能体维护全局任务上下文，并运行动态的“计划-执行-观察”循环，以制定行动计划并协调子智能体。

系统包含两个专门的信息获取子智能体，它们共享底层大语言模型但不共享全局状态，仅向主智能体返回高度凝练的摘要，以减轻主智能体的上下文负担。其中，RAG搜索子智能体负责与静态沙箱语料库交互。其关键技术创新在于：用基于text-embedding-3-small的迭代密集检索机制取代了传统的开放网络搜索。该子智能体在受控环境中采用ReAct范式，能够自主进行多步骤检索并迭代优化查询。这个过程要求智能体评估不完整或冲突的证据，并在多次迭代中修正搜索方向，其功能类似于在超链接图上的启发式探索，从而增强了检索的鲁棒性。另一个文件阅读子智能体则专门解析长文本用户文件，利用工具执行细粒度的关键词查询和按页码检索内容。

整体框架的创新点在于：1）通过主智能体直接集成多模态感知，实现了对音视频内容的全局上下文合成；2）设计了分离的、专注的子智能体进行迭代检索和文件解析，优化了信息获取效率并控制了幻觉风险；3）用静态沙箱中的迭代检索模拟了真实网络的复杂性，同时保证了评估的可复现性。该系统通过这种协调的、模块化的架构，旨在应对深度研究任务中规划、检索、多模态理解和报告生成的全链条挑战。

### Q4: 论文做了哪些实验？

实验主要基于提出的DR³-Eval基准和DR³-Agent多智能体系统展开。实验设置方面，DR³-Agent的主智能体最大交互轮次设为10，用于RAG和文件读取的子智能体分别限制为5轮和3轮，使用OpenAI的text-embedding-3-small进行向量化。数据集为DR³-Eval基准，它包含真实用户提供的多模态材料，并配有模拟开放网络复杂性的静态研究沙箱语料库（包含支持性文档、干扰项和噪声），语料库规模测试了从32k到512k tokens的不同版本。

对比方法包括多个先进的大语言模型：GPT-4.1、Claude Sonnet 4、Gemini 2.5 Pro、Qwen3系列（235B-A22B, 30B-A3B, 32B）以及GLM系列（4.6, 4.7）。评估阶段，文本内容使用GPT-5.1作为评判模型，多模态内容（如音频、视频）使用Gemini-2.5-Pro作为辅助评判模型，温度均设为0以确保确定性。

主要结果和关键数据指标如下：
1.  **基准挑战性与模型表现**：DR³-Eval被证明极具挑战性。Claude Sonnet 4在总平均分上表现最佳（在64k语料下Avg.为70.7）。在同一模型家族（如Qwen）中，模型规模仍是关键因素。
2.  **语料库规模的影响**：随着沙箱语料库从64k扩展到512k，所有模型的整体性能（Avg.）呈明显下降趋势。例如，Claude Sonnet 4的Avg.从70.7降至65.6，表明更长的上下文带来了更多噪声和无关信息，增加了获取有价值见解的难度。
3.  **多维指标分析**：
    *   **信息检索与引用**：从用户文件的信息召回（IR_UF）和沙箱语料的信息召回（IR_SC）指标看，Claude Sonnet 4和GLM-4.7表现较好（如Claude在64k下IR_UF为58.8，IR_SC为55.3）。引用覆盖率（CC）也呈现类似趋势。
    *   **事实准确性与指令遵循**：研究发现，更好的指令遵循（IF）并不代表更高的事实准确性（FA）。例如，GPT-4.1和Qwen3-235B-A22B在IF上得分相对较高（约83.0和78.0），但FA得分很低（约56.4和52.5），表明这些模型倾向于生成“看起来”完整但事实准确性低的报告。
    *   **深度质量（DQ）**：各模型在DQ上差异相对较小，Claude Sonnet 4和GLM-4.7略优（约70-72分）。
4.  **评估稳健性与显著性**：万次bootstrap分析显示，排名前两位模型的95%置信区间无重叠，Wilcoxon检验（p=0.0046）证实分数存在显著差异。重复评估的总分方差仅为0.874，模型排名的Kendall's τ和Spearman's ρ分别达到0.969和0.991，表明评估高度稳健。
5.  **沙箱语料有效性验证**：移除干扰文档后，所有模型性能显著提升，证实了干扰项有效增加了任务难度。当沙箱仅包含支持性文档时，确立了模型在完美信息检索下的性能上限。
6.  **与实时网络搜索对比**：使用Qwen3-235B和Gemini-2.5-Pro在英文子集上进行的实验表明，沙箱设置与实时网络搜索设置的总体性能接近，尤其在引用覆盖率（CC）上高度一致，表明沙箱能可靠替代网络检索。
7.  **框架架构比较**：与DeerFlow框架的对比实验（在子集上进行）显示，在处理复杂的深度研究任务时，DR³-Agent在整合碎片化证据和遵循任务指令方面展现出架构优势。
8.  **自动化评估与人工评估相关性**：在50份随机报告上的相关性研究表明，自动化评分与四位专家评估高度一致（Pearson相关系数r=0.78，Spearman相关系数ρ=0.73， pairwise agreement=0.89），且事实准确性声明提取的精确度（Precision）达0.924，召回率（Recall）达0.960。
9.  **其他消融实验**：
    *   **检索器对比**：OpenAI text-embedding-3-small在引用覆盖率（CC）上优于Qwen-text-embedding-v2和BM25。
    *   **RAG迭代轮次**：增加RAG子智能体的最大迭代轮次（从1到7）能提升性能（特别是IR和CC），但超过一定轮次后性能可能达到峰值并略有下降。
    *   **评判模型**：使用不同的LLM作为评判模型（如Claude Sonnet 4, Gemini-2.5-Pro, Qwen-Max）产生的模型排名与GPT-5.1的排名高度相似（平均Spearman's ρ=0.924），表明评分具有鲁棒性。

### Q5: 有什么可以进一步探索的点？

该论文提出的DR³-Eval基准和评估框架在现实性和可复现性上迈出了重要一步，但其局限性和未来探索方向仍值得深入。首先，其静态沙箱语料库虽能模拟开放网络复杂性，但本质上仍是封闭且预设的，无法完全复现真实网络环境的动态性、信息更新和交互不确定性。其次，评估主要聚焦于报告生成任务，对于研究过程中更复杂的子任务，如假设生成、实验设计或批判性思维，缺乏细粒度评估。此外，多维度评估框架虽全面，但各指标（如事实准确性与指令遵循）间可能存在内在冲突，其权重分配和综合评判标准有待进一步研究。

未来研究方向可包括：1）**动态环境模拟**：开发能随时间演化和响应用户/Agent交互的动态沙箱，以更好地评估Agent在开放域中的长期适应能力。2）**任务泛化与扩展**：将基准扩展到更广泛的研究工作流，如代码生成、数据分析或跨模态推理，并设计更具挑战性的“对抗性”干扰项。3）**评估方法优化**：探索更鲁棒、无需参考的自动评估方法，减少对特定大模型作为评判者的依赖，并研究如何更有效地融合人类反馈。4）**Agent架构创新**：针对论文揭示的检索鲁棒性和幻觉控制等失败模式，设计更高效的迭代检索、自我验证或知识溯源机制，以提升复杂任务下的性能上限。

### Q6: 总结一下论文的主要内容

该论文提出了DR³-Eval，一个面向深度研究智能体的现实且可复现的评估基准。核心问题是现有深度研究智能体在解决涉及规划、检索、多模态理解和报告生成的复杂长程研究任务时，其评估因动态网络环境和模糊任务定义而面临挑战。

论文的核心贡献是构建了一个新颖的基准。方法上，DR³-Eval基于真实用户提供的材料构建，并为每个任务配备一个静态的研究沙箱语料库，该语料库模拟开放网络的复杂性（包含支持性文档、干扰项和噪声），同时保持完全可验证性。此外，论文引入了一个多维评估框架，衡量信息召回率、事实准确性、引用覆盖率、指令遵循度和深度质量，并验证了该框架与人类判断的一致性。

主要结论是，基于多个先进语言模型构建的多智能体系统DR³-Agent的实验表明，DR³-Eval具有高度挑战性，能够有效揭示当前智能体在检索鲁棒性和幻觉控制方面的关键失败模式。该工作为深度研究智能体的评估提供了更可靠和可复现的标准，推动了该领域的进一步发展。
