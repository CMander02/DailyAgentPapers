---
title: "LACE: Lattice Attention for Cross-thread Exploration"
authors:
  - "Yang Li"
  - "Zirui Zhang"
  - "Yang Liu"
  - "Chengzhi Mao"
date: "2026-04-16"
arxiv_id: "2604.15529"
arxiv_url: "https://arxiv.org/abs/2604.15529"
pdf_url: "https://arxiv.org/pdf/2604.15529v1"
categories:
  - "cs.AI"
tags:
  - "推理增强"
  - "并行搜索"
  - "架构修改"
  - "数据合成"
  - "单智能体"
relevance_score: 8.5
---

# LACE: Lattice Attention for Cross-thread Exploration

## 原始摘要

Current large language models reason in isolation. Although it is common to sample multiple reasoning paths in parallel, these trajectories do not interact, and often fail in the same redundant ways. We introduce LACE, a framework that transforms reasoning from a collection of independent trials into a coordinated, parallel process. By repurposing the model architecture to enable cross-thread attention, LACE allows concurrent reasoning paths to share intermediate insights and correct one another during inference. A central challenge is the absence of natural training data that exhibits such collaborative behavior. We address this gap with a synthetic data pipeline that explicitly teaches models to communicate and error-correct across threads. Experiments show that this unified exploration substantially outperforms standard parallel search, improving reasoning accuracy by over 7 points. Our results suggest that large language models can be more effective when parallel reasoning paths are allowed to interact.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型在推理过程中各推理路径相互孤立、缺乏协作的问题。研究背景是，人类在面对复杂问题时，通常会并行探索多种假设，并在不同思路间进行内部对话与修正，即“并行思考”。然而，现有的大语言模型通常采用独立并行采样的方式，同时生成多条推理路径并从中选择最佳答案。这种方法的不足在于，各推理线程在生成过程中完全隔离，无法实时共享中间见解或相互纠正错误，导致计算资源浪费在冗余尝试上，且多条路径常因缺乏多样性而陷入相似的错误模式。事后验证孤立样本不仅效率低下，也容易受到模型内部固有偏见的影响。

因此，本文要解决的核心问题是：能否让并行的推理线程在生成过程中进行实时通信与协作，从而提升整体推理的效率和准确性？为此，论文提出了LACE框架，通过将标准的单向因果注意力机制扩展为二维的“晶格注意力”，引入一个宽度维度，使得信息不仅能在时间（令牌）上传递，还能在线程间流动。这从根本上将推理从一组独立事件转变为在单次前向传播中进行的统一、协作式探索。此外，针对缺乏现成的多线程协作训练数据这一关键挑战，论文还设计了一个合成数据生成管道，以创建具有逻辑多样性且包含显式交互点的并行推理轨迹，并通过监督微调和强化学习来激励模型进行多样化探索和实时自我评估。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：外部测试时搜索与扩展方法，以及生成时并行推理方法。

在**外部测试时搜索与扩展**方面，相关工作旨在通过增加推理时的计算来提升性能，例如链式思考及其变体、思维树等结构化搜索方法，以及基于自洽性、最佳N采样聚合、学习验证器或奖励模型的并行采样流程。此外，还包括基于强化学习的并行推理框架（如Parallel-R1）和宽度导向的外部并行思考（如ParaThinker）。这些方法的共同点是主要在模型原生的词元级生成过程之外进行协调，因此独立采样的推理路径之间缺乏交互，容易产生重复或相关的错误。本文的LACE框架与这些工作目标相似，但通过实现生成过程中的跨线程交互，从根本上改变了并行推理的协作方式。

在**生成时并行推理**方面，近期研究开始将并行推理融入生成过程内部。例如，ParaDecodeOneSeq将多个分支打包到单个序列中以提升解码效率；Hogwild!通过共享跨线程的键值状态实现显式并发注意力；GroupThink则研究了并发推理代理在词元级的直接跨线程交互。本文的LACE与这些方法共享“生成时跨线程交互”的目标，但在机制上有所不同。LACE没有通过共享键值状态和非标准掩码来暴露各线程的历史，而是引入了一种轻量级门控侧路径，在标准注意力派生的表示上实现隐式的跨线程交互。这种方法保留了标准的因果注意力主干，同时允许线程在生成过程中相互影响，从而将独立采样转变为协作过程，并明确针对冗余探索和相关错误进行优化。

### Q3: 论文如何解决这个问题？

论文通过提出LACE框架来解决并行推理路径间缺乏交互的问题，其核心是引入**Lattice Attention机制**，使多个并行的推理线程能够相互通信和纠错。整体方法包含三个关键部分：创新的架构设计、分阶段的训练框架以及专门的数据合成流程。

**核心架构与模块**：LACE在基础模型的中后层插入**Lattice Attention层**，该层垂直于原有的因果注意力（处理token序列）运作，专门处理线程维度。其工作流程是：首先将标准注意力（SDPA）的输出降维投影，然后计算跨线程的Q、K、V。为了区分token位置和线程索引，采用了**3D RoPE**进行位置编码。接着，通过重塑张量形状实现跨线程注意力计算，允许不同线程在相同token位置交换信息。最后，通过一个**门控残差连接**将跨线程注意力输出融合回主路径，门控机制使模型能动态调节跨线程信息的影响。这种设计参数高效，新增参数量不到原模型的1%，且最大程度保留预训练模型的因果推理能力。

**训练框架**：训练分为三个阶段。1. **持续预训练**：在合成的多线程数据上初始化并训练新插入的Lattice Attention层，学习跨线程通信。2. **监督微调**：进行全参数微调，使模型遵循特定的多线程推理格式。采用**随机线程打乱**作为数据增强，迫使模型依赖跨线程信息而非单线程上下文。3. **强化学习**：提出**Lattice GRPO**，是多线程版的GRPO。关键创新在于**线程聚合奖励**：每个并行生成的线程组共享一个奖励信号，该奖励由**准确性奖励**和**多样性奖励**组成。准确性奖励强制模型通过自选标签（如[[best]]）正确识别最佳推理路径，并进行符号验证；多样性奖励则基于各线程推理内容的嵌入向量相似度，鼓励探索不同路径。共享的优势信号强化了线程间的协作。

**数据合成流程**：为了解决缺乏天然协作数据的问题，论文构建了专门的流水线来合成训练数据。首先进行**模型特定的数据过滤**，筛选出基础模型能产生成功和失败多种解法的题目。然后通过**多样性增强**技术，迭代采样时明确指令模型避免已生成的解法，以确保各线程探索不同的推理策略。最后，对冗长推理进行步骤分解和压缩，形成适合训练的结构化多线程数据格式。

**创新点**：1. **Lattice Attention机制**：在架构层面实现了并行推理线程间的低开销、高效信息交换。2. **Lattice GRPO**：设计了支持多线程协作的强化学习目标，通过聚合奖励和共享优势信号促进协同。3. **针对性数据合成**：通过模型感知的筛选和多样性引导，构建了能激发跨线程协同与纠错的数据集。实验表明，该方法相比标准的并行搜索，在多个数学推理基准上实现了超过7个百分点的准确率提升。

### Q4: 论文做了哪些实验？

论文在数学推理和智能体任务上进行了系统实验。实验设置基于Qwen3的1.7B和4B模型，通过插入Lattice Attention层实现跨线程注意力，默认使用4个线程。对比方法包括：Independent基线（标准单线程模型，推理时多路径采样+多数投票）和Isolated Parallel基线（使用相同多线程数据格式但无跨线程注意力）。评估指标包括准确率（Acc）、探索多样性（Expl.）和格式遵循率（Fmt）。

主要结果：在AIME25和LiveBench等数学推理基准上，LACE显著优于基线，RL阶段后准确率提升超过7个百分点（例如在LiveBench上从3.0%提升至11.5%），并实现了接近完美的格式遵循率（如73.3%）。关键数据指标显示，LACE的FLOPs开销可忽略（<1.3%），内存开销适中（约2-15%）。在TextWorldCookAgent智能体任务中，LACE也取得了最高的胜率。消融实验验证了数据流水线（使用多样性感知数据后探索多样性从0.175提升至0.307）和完整训练流程的必要性，跳过预训练和SFT会导致准确率接近零。分析表明，模型通过门控机制在核心推理阶段实现跨线程信息交互，呈现出“发散-收敛”的协作模式。

### Q5: 有什么可以进一步探索的点？

该论文提出的LACE框架通过跨线程注意力实现了并行推理路径间的交互，但仍存在一些局限性和可探索方向。首先，其依赖合成数据训练协作行为，未来可研究如何利用真实世界对话或协作任务数据来更自然地训练此类交互能力。其次，当前方法主要关注token级别的隐式交互，未来可探索更显式的、结构化的信息交换机制，例如允许线程间传递子目标或置信度分数。此外，论文未深入探讨不同任务类型（如数学推理与常识推理）对跨线程交互模式的差异化需求，这值得进一步研究。从系统优化角度，跨线程注意力的计算开销与线程数量的关系也需要更精细的权衡设计。最后，将这种协作机制与现有的复杂推理技术（如程序生成或工具使用）结合，可能催生更强大的协同推理系统。

### Q6: 总结一下论文的主要内容

该论文提出了LACE框架，旨在解决大语言模型在并行推理时路径间缺乏交互、容易重复犯错的问题。核心贡献是通过引入跨线程注意力机制，将原本独立的推理轨迹转变为协同并行的探索过程。方法上，LACE重新利用模型架构，使并行的推理线程能够共享中间见解并相互纠错；针对缺乏协作训练数据的问题，作者设计了一个合成数据生成流程，显式教导模型进行跨线程通信与错误修正。实验结果表明，这种统一的探索方式显著优于标准并行搜索，将推理准确率提升了超过7个百分点。主要结论是，允许并行推理路径相互交互可以大幅提升大语言模型的有效性，为增强模型推理能力提供了新的方向。
