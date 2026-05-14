---
title: "ReTool-Video: Recursive Tool-Using Video Agents with Meta-Augmented Tool Grounding"
authors:
  - "Xiao Liu"
  - "Nayu Liu"
  - "Junnan Zhu"
  - "Ruirui Chen"
  - "Guohui Xiang"
  - "Changjian Wang"
  - "Kaiwen Wei"
  - "Rongzhen Li"
  - "Jiang Zhong"
date: "2026-05-13"
arxiv_id: "2605.13228"
arxiv_url: "https://arxiv.org/abs/2605.13228"
pdf_url: "https://arxiv.org/pdf/2605.13228v1"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "工具增强agent"
  - "视频理解agent"
  - "递归工具调用"
  - "元工具库"
  - "agent架构"
relevance_score: 9.5
---

# ReTool-Video: Recursive Tool-Using Video Agents with Meta-Augmented Tool Grounding

## 原始摘要

Video understanding requires active evidence seeking, motivating tool-augmented video agents for temporal reasoning, cross-modal understanding, and complex question answering. Existing video agents have improved video reasoning with retrieval, memory, frame inspection, and verifier tools, but they still face two limitations: (1) a coarse tool space that lacks fine-grained operations for compositional reasoning; and (2) a flat action space that forces high-level video intents into primitive executable tool calls. In this paper, we address these challenges with two complementary designs. First, we construct a MetaAug-Video Tool Library (MVTL), an extensible tool library with 134 registered tools, including 26 base tools for general multimodal signal processing and 108 meta tools for filtering, aggregation, reranking, formatting, and other intermediate-result operations. MVTL supports dual-level access to both structured video information and raw modal evidence, enabling diverse video reasoning scenarios. Second, we propose ReTool-Video, a recursive tool-using method that grounds high-level video intents into executable tool chains. In ReTool-Video, matched actions are executed directly, while unmatched intents are delegated to a resolver for parameter repair, tool substitution, or decomposition. This allows abstract actions such as temporal merging, cross-modal verification, or repeated-event aggregation to be progressively translated into concrete multimodal operations at runtime. Experiments on MVBench, MLVU, and Video-MME w/o sub. show that ReTool-Video consistently outperforms strong baselines. Further analysis demonstrates that recursive grounding and fine-grained meta tools improve the stability and effectiveness of complex video understanding.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有视频代理工具在复杂视频理解任务中面临的两个核心限制。研究背景方面，尽管多模态模型在视频理解上取得了进展，但复杂视频问答仍需主动推理和外部工具支持，因此催生了结合规划、执行、记忆和验证能力的视频代理系统。现有方法如ProViQ、VideoAgent等，虽然引入了检索、定位和帧检查等工具，但仍存在两方面的不足：一是工具空间粗糙，缺乏细粒度操作支持组合推理，例如无法进行过滤、时序合并、重排序等中间结果处理；二是动作空间扁平，强制将高级视频意图（如跨模态验证、重复事件聚合）直接映射为原始工具调用，导致参数不匹配、工具选择不当或过早终止。

本文的核心问题是如何设计一个既能提供细粒度、可组合的工具空间，又能将高级抽象意图递归地分解为可执行工具链的视频代理框架。为此，论文提出了两项互补设计：一是构建包含134个注册工具的MetaAug-Video工具库，包含基础工具和元工具；二是提出ReTool-Video递归工具使用方法，通过匹配执行和解析器分解来处理未匹配的抽象意图，从而提升复杂视频推理的稳定性和效果。

### Q2: 有哪些相关研究？

相关研究可分为三类：

1. **评测类研究**：TVQA、NExT-QA等基准揭示了视频问答需要定位时刻、理解对话/字幕、跨时间比较动作和时序证据 grounding 的需求。这些工作明确了视频理解的挑战，而本文在这些基准上（MVBench、MLVU、Video-MME）进行评测，并超越了现有方法。

2. **方法类研究**：
   - **视频语言模型**：通过对齐、指令微调、统一图像-视频表示提升视频问答，但缺乏精细操作支持。本文的MVTL工具库（134个工具，含26个基础工具和108个元工具）专门设计了过滤、聚合、重排等元操作，填补了这一空白。
   - **长视频方法**：采用稀疏记忆、长上下文迁移、文档式检索或分层索引扩展时序覆盖，但主要关注证据获取或上下文压缩。本文补充了元级操作（如时序合并、计数、计算、格式化）。
   - **检索与验证系统**：检索候选窗口并以clip、帧、音频、转录、事件级观察验证。本文在此基础上增加了递归工具调用机制。

3. **Agent类研究**：
   - **通用工具使用Agent**：通过外部API、专家模型、任务特定工具扩展模型能力。本文的ReTool-Video继承了多步交互范式，但针对视频领域做了专门设计。
   - **多模态Agent**：连接语言模型与视觉专家、OCR、检测、分割、可执行代码或视觉程序。本文的创新在于递归意图接地：直接执行匹配动作，将不匹配意图委托给解析器进行参数修复、工具替换或分解，区别于现有Agent的扁平工具调用接口。
   - **递归规划与多Agent研究**：探索分解、角色分离、并行调度。本文聚焦视频特定意图接地，将抽象动作（如时间合并、跨模态验证、重复事件聚合）逐步转化为具体多模态操作。

### Q3: 论文如何解决这个问题？

ReTool-Video通过两大核心设计解决视频智能体在复杂理解任务中的局限性：一是构建了元增强视频工具库（MVTL），二是提出了递归工具使用方法。整体框架将复杂视频QA建模为交互式决策过程，智能体反复判断缺失信息、调用工具获取或处理信息，并决定当前观察是否足以回答问题。

MVTL包含134个注册工具，包括26个用于通用多模态信号处理的基础工具和108个用于过滤、聚合、重排序、格式化等中间结果操作的元工具。这种双层设计既支持结构化视频信息访问，也支持原始模态证据获取，覆盖了多样化的视频推理场景。

ReTool-Video的核心创新在于将意图表达与即时工具可执行性分离。动作空间分为三类：可直接执行的原语动作、需要运行时确定的抽象视频推理意图、以及终止动作。当规划器输出一个动作时，运行时首先查询工具注册表：如果匹配则直接执行；如果不匹配，则将该动作视为抽象意图，委托给解析器通过参数修复、工具替换或分解为底层工具调用进行递归确定。例如，检查相邻片段是否形成同一事件的意图可被分解为片段检查、视觉比较、时间合并和结果聚合等操作。解析器只返回局部结果，不能输出最终答案，只有根规划器才能发出Finish，从而将局部工具确定与全局证据充分性判断分离。

此外，系统支持受控并行执行，允许多个独立动作同时执行，并通过强化学习优化规划器策略，仅学习高层决策（如动作选择、抽象意图委托、证据充分性判断和终止），而工具库和解析器作为不可训练组件。

### Q4: 论文做了哪些实验？

论文在MVBench、MLVU和Video-MME w/o sub.三个通用视频理解基准上评估ReTool-Video。MVBench聚焦短视频时序理解，MLVU强调长视频推理，Video-MME w/o sub.提供无字幕的开放域评估。对比方法包括闭源模型（GPT4-V、GPT-4o等）和开源模型（LLaMA-VID、VideoLLaMA2、NVILA、VideoMind、VideoSeek等）。主要结果：ReTool-Video在MVBench上达72.9，MLVU上达81.5，Video-MME w/o sub.上达76.6，全面超越所有基线。相比InternVL3.5-30B-A3B，在MLVU和Video-MME上分别提升8.5%和7.9%。消融实验显示：无工具基线（Direct Response）在MLVU仅47.6，而完整ReTool-Video达81.5；移除元工具（w/o Meta Tools）在MLVU降至71.2；同时移除并行和递归（w/o Parallel&Recursion）降至70.5；移除递归但保留并行（w/o Recursion）降至63.2，表明递归对长视频很关键。工具调用分析表明，工具调用成功率与准确性强相关，而非调用数量。案例研究展示了递归工具调用如何通过局部验证和元工具聚合（如时间排序、片段合并）准确回答需要跨片段推理的问题。

### Q5: 有什么可以进一步探索的点？

论文在工具库和动作空间设计上虽有创新，但仍存在可深入探索的方向。首先，当前134个工具的划分依赖人工预定义，未来可探索**自动工具生成**机制，让模型根据任务动态创建专用meta工具，而非依赖固定库。其次，递归解析器在遇到完全未匹配意图时仅进行参数修复、替换或分解，但**缺乏对意图本质理解的纠错能力**，可引入反思机制，让模型对分解后的子任务进行可行性验证。另外，实验仅针对单轮视频问答，未涉及**多轮交互场景**，后续可扩展至对话式视频理解，让模型将前文解析的复杂工具链作为记忆复用。最后，当前工具调用顺序依赖固定流程，可结合强化学习或搜索策略，**动态优化工具链的执行路径**以降低推理成本。这些方向将进一步提升视频代理的泛化性和效率。

### Q6: 总结一下论文的主要内容

该论文提出了一个用于视频理解的递归工具使用框架ReTool-Video及其配套的元增强视频工具库MVTL。问题定义：现有视频智能体在处理复杂时序推理、跨模态理解和多步组合查询时，面临工具空间粒度粗（缺乏细粒度操作）和动作空间扁平化（高级意图直接映射为原始工具调用）的局限。方法核心贡献有两方面：一是构建了包含134个注册工具的MVTL库，其中26个基础工具负责通用多模态信号处理，108个元工具支持过滤、聚合、重排序、格式化等中间结果操作，提供结构化信息和原始模态证据的双重访问；二是提出递归动作解析机制，对于匹配动作直接执行，未匹配意图则通过参数修复、工具替换或分解逐步转化为可执行的多模态操作链。在MVBench、MLVU和Video-MME三个基准上的实验表明，该方法始终优于强基线，验证了递归接地和细粒度元工具能显著提升复杂视频理解的稳定性和有效性。该工作揭示了扩展视频智能体需要更丰富的工具空间和更灵活的动作接底机制。
