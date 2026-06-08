---
title: "MemDreamer: Decoupling Perception and Reasoning for Long Video Understanding via Hierarchical Graph Memory and Agentic Retrieval Mechanism"
authors:
  - "Cong Chen"
  - "Guo Gan"
  - "Kaixiang Ji"
  - "ChaoYang Zhang"
  - "Zhen Yang"
  - "Guangming Yao"
  - "Hao Chen"
  - "Jingdong Chen"
  - "Yi Yuan"
  - "Chunhua Shen"
date: "2026-06-05"
arxiv_id: "2606.07512"
arxiv_url: "https://arxiv.org/abs/2606.07512"
pdf_url: "https://arxiv.org/pdf/2606.07512v1"
categories:
  - "cs.CV"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agentic Retrieval"
  - "Hierarchical Graph Memory"
  - "Long Video Understanding"
  - "Vision-Language Model"
  - "Perception-Decoupling"
  - "Reasoning-Action Loop"
  - "Plug-and-Play Framework"
  - "Benchmark Evaluation"
relevance_score: 9.5
---

# MemDreamer: Decoupling Perception and Reasoning for Long Video Understanding via Hierarchical Graph Memory and Agentic Retrieval Mechanism

## 原始摘要

Current Vision-Language Models struggle with hours-long videos because processing full-length visual sequences induces prohibitive token explosion and attention dilution. To overcome this, we introduce MemDreamer to decouple perception and reasoning, shifting long-video understanding into an agentic exploration process. As a plug-and-play framework, it incrementally streams videos to construct a Hierarchical Graph Memory, a top-down three-tier architecture for semantic abstraction, anchored by a foundational graph capturing spatiotemporal and causal relations. During inference, the reasoning model employs agentic tool-augmented retrieval, navigating hierarchies, searching nodes, and traversing logical edges via an Observation-Reason-Action loop. Experiments show MemDreamer achieves SOTA results across four mainstream benchmarks, narrowing the gap with human experts to only 3.7 points. It constrains the reasoning context window to merely 2% of full-context ingestion while delivering a 12.5 point absolute accuracy gain. Furthermore, statistical analysis uncovers a strong positive linear correlation between an VLM's performance on logic reasoning and long-video understanding benchmarks, establishing agentic capability scaling as a new paradigm for multimodal comprehension.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前视觉语言模型（VLM）在处理长视频（如数小时视频）时面临的核心瓶颈。研究背景是，现有VLM在单图、多图或短视频分析上已取得突破，但长视频理解仍严重受限。现有方法通常采用“耦合”策略，即通过暴力帧采样将长视频扁平化为超长token序列，同时进行感知与推理。这种方法导致两大不足：在感知上，token数量爆炸（如2小时视频以1 FPS采样产生超160万token），远超模型上下文限制；在推理上，冗余token引发严重的注意力稀释与“中间信息丢失”现象，极大削弱长程推理能力。

为克服这些问题，本文提出MemDreamer框架，核心思路是将感知与推理解耦，把长视频理解转化为智能体探索过程。具体而言，本文设计了一种分层的图记忆结构（三级层次：视频根节点-超级事件-宏观事件），以粗到细地组织语义信息并保留时空因果关联，并引入工具增强的智能体检索机制（包括导航、搜索、图遍历三类工具），通过观测-推理-行动的迭代循环主动获取任务相关线索。最终目标是在严格限制推理上下文窗口（仅占全上下文的2%）的前提下，实现超越现有最先进方法的视频理解性能，并揭示VLM的智能体推理能力与长视频性能之间的强正相关性。

### Q2: 有哪些相关研究？

本文相关研究主要分为三类。**方法类**：现有方法多依赖视觉编码器或扩展原生上下文窗口（如Gemini-2.5-Pro）处理长视频，但面临token爆炸和注意力稀释问题。早期记忆系统如MemGPT和MemoryBank在LLM中取得成功，但直接移植到VLM存在挑战。M3-Agent和WorldMM采用平面化离散语义桶设计，缺乏层级结构和拓扑边。VideoARM和MM-mem虽引入层级记忆，但仍作为无边界的感知缓冲区或依赖被动不确定性驱动的纵向搜索。**应用类**：VideoAgent和DVD采用智能体检索机制，允许VLM主动搜索，但受限于平面化片段数据库，容易退化为盲试。**评测类**：LVBench等基准揭示了长视频理解中的“大海捞针”和“中间迷失”问题。本文核心区别在于：1）提出三层层级图记忆结构，融合因果图拓扑编码多粒度语义；2）构建纯文本记忆，避免检索时重新访问原始视频帧；3）通过工具增强的观察-推理-行动循环实现多维度智能体检索，克服了平面检索的逻辑不相关性和单轮检索的不可自校正缺陷。

### Q3: 论文如何解决这个问题？

MemDreamer的核心方法是将长视频理解解耦为感知和推理两个阶段，通过构建层次化图记忆和工具增强的智能体检索机制来解决token爆炸和注意力稀释问题。

整体框架分为两部分：1）**持久化记忆构建阶段**，感知模型以流式方式处理视频，构建纯文本的层次化图记忆。该记忆采用自上而下的三层拓扑结构：视频根节点（全局主题）、超事件节点（叙事阶段）和宏事件节点（情节摘要）。每个宏事件节点向下展开为包含实体节点和微事件节点的局部子图，并通过三种边类型（空间属性边、主客体边、时间因果边）建模细粒度视觉细节。跨层边连接不同层级节点。构建过程包括**流式自适应分割**（基于语义边界分割视频，避免固定窗口截断）、**向下子图提取**（从视频片段提取包含实体和微事件的细粒度子图）和**向上层次聚合**（自底向上将宏事件聚合成超事件和视频根节点）。

2）**工具增强的智能体检索阶段**，推理模型通过观察-推理-行动循环主动探索图记忆。检索工具集包括三类：**层次导航工具**（如GetSummary、GetSuperEvent、GetMacroEvent、GetSubgraph）支持自上而下浏览；**精确搜索工具**（SearchNodes、SearchByTime）支持语义和时间锚定检索；**图遍历工具**（GetRelationGraph）支持沿边多跳推理。在推理过程中，模型仅处理纯文本记忆，将推理上下文窗口限制在全量处理的2%，同时基于相关性蒸馏机制避免中间信息丢失。

创新点在于：1）解耦感知与推理，使推理模型无需处理原始视频；2）层次化图记忆结构结合了全局叙事和细粒度时空因果建模；3）智能体工具增强的检索机制实现了高效的上下文聚焦。

### Q4: 论文做了哪些实验？

论文在四个主流长视频理解基准上进行了实验，包括LVBench（103个30分钟至2小时的视频，1549个QA对）、LongVideoBench验证集（753个视频、1337个问题，含188个15-60分钟视频）、Video-MME长视频子集（300个视频、900个问题）和EgoSchema（聚焦第一视角推理）。实现中，视频流通过τ=10分钟滑动窗口分段，以Gemini-3.1-Pro作为感知模型构建层级图记忆；推理阶段评估了Gemini-2.5-Pro、Gemini-3.1-Pro和开源Qwen3-VL-235B-A22B-Thinking作为推理引擎，采用Qwen3-Embedding计算语义向量，最大工具调用步数为12。对比方法包括两类长视频系统：原生长视频VLM（如Gemini-3.1-Pro等闭源模型）和基于记忆的视频LLM（主流基线及最新SOTA记忆驱动系统）。主要结果：MemDreamer在所有基准上取得新SOTA。在LVBench上达到90.7分，比最强原生闭源基线Gemini-3.1-Pro提升12.5个绝对点，与人类专家差距缩小至仅3.7点；LongVideoBench和Video-MME分别达到92.9和92.1分，提升14.3和11.8点；EgoSchema上获得88.2分。推理上下文窗口仅占全量输入的2%。

### Q5: 有什么可以进一步探索的点？

论文的主要局限在于其层次图记忆的构建依赖预定义的事件边界检测，在无明确场景切换的长视频中可能产生语义割裂。未来可探索基于因果关系的动态图剪枝策略，自动合并弱关联节点以降低记忆冗余。当前检索机制仅依赖LLM内嵌知识进行路径推理，可引入外部常识图谱（如ConceptNet）增强跨模态逻辑桥接。注意到实验显示逻辑推理能力与长视频理解存在强线性相关，建议研究显式链式推理训练范式，让视觉语言模型在记忆回溯时自动生成结构化推理轨迹。此外，当前2%的上下文约束窗口仍包含关键帧选择偏差，可结合注意力熵值实时采样策略，在保持压缩率的同时优先保留高信息密度片段。多智能体协作模式也值得探索，使感知智能体与推理智能体通过共享记忆单元形成双向反馈，打破当前单向流水线架构的信息瓶颈。

### Q6: 总结一下论文的主要内容

当前视觉语言模型处理数小时长视频时面临token爆炸和注意力稀释两大瓶颈。为此，MemDreamer提出感知与推理解耦的新范式，将长视频理解转化为智能体探索过程。该方法构建了层次化图记忆系统，采用自上而下的三层架构：顶层为视频根节点提供全局摘要，中间层分解为超级事件，底层通过局部子图刻画宏事件中的实体、事件及其逻辑关系。推理阶段，模型通过工具增强的智能体检索机制，利用观察-推理-行动循环进行层级导航、节点搜索和逻辑边遍历。实验表明，该方法在四个长视频基准上取得最优结果，将人类专家差距缩小至3.7分，仅使用完整上下文2%的窗口即实现12.5个百分点的准确率提升。更重要的是，研究首次发现视觉语言模型在逻辑推理与长视频理解性能之间存在强正线性相关，为多模态理解开辟了智能体能力扩展的新范式。
