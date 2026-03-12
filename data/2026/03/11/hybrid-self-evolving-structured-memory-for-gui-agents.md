---
title: "Hybrid Self-evolving Structured Memory for GUI Agents"
authors:
  - "Sibo Zhu"
  - "Wenyi Wu"
  - "Kun Zhou"
  - "Stephen Wang"
  - "Biwei Huang"
date: "2026-03-11"
arxiv_id: "2603.10291"
arxiv_url: "https://arxiv.org/abs/2603.10291"
pdf_url: "https://arxiv.org/pdf/2603.10291v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "GUI Agent"
  - "Memory"
  - "Graph-based Memory"
  - "Self-evolving"
  - "Retrieval"
  - "VLM"
  - "Agent Architecture"
relevance_score: 9.0
---

# Hybrid Self-evolving Structured Memory for GUI Agents

## 原始摘要

The remarkable progress of vision-language models (VLMs) has enabled GUI agents to interact with computers in a human-like manner. Yet real-world computer-use tasks remain difficult due to long-horizon workflows, diverse interfaces, and frequent intermediate errors. Prior work equips agents with external memory built from large collections of trajectories, but relies on flat retrieval over discrete summaries or continuous embeddings, falling short of the structured organization and self-evolving characteristics of human memory. Inspired by the brain, we propose Hybrid Self-evolving Structured Memory (HyMEM), a graph-based memory that couples discrete high-level symbolic nodes with continuous trajectory embeddings. HyMEM maintains a graph structure to support multi-hop retrieval, self-evolution via node update operations, and on-the-fly working-memory refreshing during inference. Extensive experiments show that HyMEM consistently improves open-source GUI agents, enabling 7B/8B backbones to match or surpass strong closed-source models; notably, it boosts Qwen2.5-VL-7B by +22.5% and outperforms Gemini2.5-Pro-Vision and GPT-4o.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于视觉-语言模型（VLM）的图形用户界面（GUI）智能体在处理现实世界计算机使用任务时面临的挑战。研究背景是，尽管VLM在感知和规划方面取得了显著进步，使得GUI智能体能够以类人方式与计算机交互，但实际任务通常具有长流程、界面多样且频繁出现中间错误的特点，导致现有智能体性能仍难以达到人类水平。

现有方法的不足在于，先前工作虽然为智能体配备了从大量轨迹构建的外部记忆模块，但这些记忆主要依赖于对离散摘要或连续嵌入的扁平化检索。这种设计缺乏人类记忆所具有的结构化组织和自我演化特性。具体而言，现有记忆范式要么将多模态内容提炼为离散符号（如句子或关键词），要么压缩为连续嵌入，然后在推理时通过相似性匹配进行检索。然而，它们无法像人脑那样，将细粒度的多模态证据与高层概念或策略关联起来形成高效搜索和推理的结构，也无法随着新经验的到来持续更新知识。论文中的表格对比也显示，现有方法在支持多模态、结构化组织以及全局/局部更新能力方面存在不同程度的缺失。

因此，本文要解决的核心问题是：如何为GUI智能体设计一个更接近人脑记忆机制的外部记忆系统。具体而言，论文提出构建一个**混合的、自我演化的结构化记忆（HyMEM）**，以克服现有记忆在知识组织和动态演化方面的短板。该系统需要能够将离散的高层符号节点与连续的轨迹嵌入相结合，形成图结构以支持多跳检索，并具备通过节点操作实现自我演化、以及在推理过程中动态刷新工作记忆的能力，从而提升智能体在长流程、多样化任务中的规划和执行效果。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为GUI智能体和语言模型记忆机制两大类。

在GUI智能体方面，早期工作依赖HTML或DOM解析来定位操作，而当前研究已转向利用视觉语言模型进行屏幕感知。例如，AppAgent等自主框架将视觉专家集成到闭环系统中，但在处理长流程、开放式任务时保持一致性仍是挑战。这推动了为智能体配备外部记忆系统的研究，使其能保留长期上下文并从历史交互中泛化，而非仅依赖即时感知。

在语言模型记忆机制方面，现有方法主要分为离散、连续和图基三类。离散方法将经验记录为文本摘要或推理轨迹，虽可解释但常无法捕捉GUI元素的细粒度视觉细节。连续记忆则将多模态输入压缩为密集嵌入或潜在标记，保留了感知细节但可能造成信息瓶颈，阻碍显式推理。图基系统将知识组织为连接节点，支持多跳检索和超越相似性匹配的推理。混合架构尝试融合这些形式以平衡抽象与细节，但现有方法（如ExpeL）常仍基于纯文本标记，将轨迹与文本洞察配对，可能缺失视觉保真度。

本文提出的HyMEM与上述工作的核心区别在于：它构建了一种图基混合记忆，将离散的高层符号节点与连续的轨迹嵌入耦合，在图形结构中同时组织文本洞察（捕获高层策略）和连续嵌入（保留细粒度多模态细节），从而确保智能体兼具战略抽象能力和精确的感知基础，并支持自演化和推理过程中的工作记忆刷新。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为HyMEM的混合自演化结构化记忆系统来解决GUI智能体在长流程、界面多样和中间错误频繁等复杂任务中面临的挑战。其核心方法是构建一个受大脑启发的图结构外部记忆，将离散的高层符号节点与连续的轨迹嵌入相结合，以支持结构化检索和动态演化。

整体框架分为记忆构建与推理执行两大部分。记忆构建阶段，系统将成功的交互序列编码为轨迹节点，每个节点包含三个层次的信息：高层策略（符号化总结，如“价格从低到高筛选”）、中层属性（语义标签，如#搜索、#筛选）和低层轨迹嵌入（连续的多模态细节表示）。节点之间通过共享的属性建立无向边，形成关联图拓扑。记忆以自演化方式增量更新：当新轨迹到达时，系统通过检索相关节点、基于VLM判断进行冗余检查（区分新增、合并或替换操作），并执行相应的图更新，从而不断优化记忆的结构与质量。

推理阶段包含四个关键模块：首先，通过结构化检索从全局记忆中获取相关经验，该方法结合语义匹配与图扩展（多跳邻居收集与重排序），确保覆盖概念相关但视觉相似度低的节点。其次，工作记忆初始化将检索到的节点转化为混合编码：离散部分由VLM合成简洁的指导指令，注入系统提示以引导高层规划；连续部分则拼接轨迹嵌入，保留细粒度视觉与动作证据。接着，智能体执行动作，并利用第四个模块——实时工作记忆刷新——动态调整上下文：在每次动作后，VLM检测界面状态转变（如从“搜索”切换到“结算”），决定保留或丢弃部分工作记忆内容，并重新检索更新指导指令与嵌入，确保上下文与GUI环境同步演化。

创新点主要体现在三个方面：一是混合记忆设计，耦合离散符号与连续嵌入，兼顾高层规划与低层执行；二是自演化图结构，通过冗余检查和动态更新操作，使记忆具备持续优化与抗冗余能力；三是实时工作记忆刷新机制，解决了长流程任务中上下文过时的问题，提升了智能体的适应性与鲁棒性。

### Q4: 论文做了哪些实验？

实验设置方面，论文采用ReAct范式构建GUI智能体，其接受屏幕截图作为多模态输入，并使用包含GUI操作（如点击、输入）和语义工具（如页面内容分析）的预定义工具集。为精确定位UI元素，采用了两阶段混合机制：首先使用SOM方法增强截图并为元素添加标签，若失败则回退至UI-INS-7B模型进行定位。记忆构建使用了来自GUIAct、Mind2Web训练集和智能体自生成轨迹的共2883条成功轨迹，并将其组织成包含1858个节点和超百万条边的图结构。在推理时，智能体通过多模态相似性检索5个种子轨迹，并通过图扩展获取其1跳邻居再补充5个，共检索10条相关轨迹。训练仅对VLM记忆编码器中的Q-Former和LoRA层进行参数高效微调，更新参数量仅占总量的1.2%。

数据集与基准测试方面，研究在三个多模态网页智能体基准上评估：WebVoyager（包含Amazon、Coursera、AllRecipes、Google Maps子域）、Multimodal-Mind2Web（包含Info、Service、Entertainment、Travel子域）和MMInA（Wiki）。主要评估指标为任务准确率（Task Accuracy）。对于WebVoyager和Mind2Web，采用LLM-as-Judge协议判断任务成功与否；对于MMInA，则将模型最终答案与真实答案进行对比。

对比方法包括：1）闭源基础模型（GPT-4o、Gemini2.5-Pro-Vision、Claude-4）；2）开源基础模型（如Qwen2.5-VL-32B、CogAgent、WebSight及作为实验基础的Qwen2.5-VL-7B、Qwen3-VL-8B、UI-TARS-1.5-7B）；3）增强记忆的开源模型，具体分为文本记忆（ReasoningBank、AWM）、离散记忆、连续记忆以及本文提出的混合记忆（HyMEM）。

主要结果如下：在整体性能上，HyMEM consistently提升了开源智能体的表现。例如，Qwen2.5-VL-7B基线准确率为12.5%，增强文本记忆（ReasoningBank、AWM）后分别提升至17.5%和13.1%，增强离散记忆和连续记忆后分别达到17.0%和21.7%，而增强HyMEM后达到35.0%（相对提升+22.5%），超越了GPT-4o（19.7%）和Gemini2.5-Pro-Vision（29.6%）。类似地，UI-TARS-1.5-7B+HyMEM达到31.2%，Qwen3-VL-8B+HyMEM达到27.6%，均为各自骨干网络的最佳结果。消融实验表明，记忆图规模扩大能持续提升性能（例如Amazon域，记忆轨迹从500增至8000条，成功率从19.5%升至63.4%）；自演化机制中，全局演化在Amazon和Google Maps域分别带来约25%和16.6%的相对提升，局部演化（工作记忆刷新）在Amazon域带来约15%的性能增益。图检索策略方面，平衡相似性与多样性（检索5个种子节点+5个图邻居）的策略效果最佳。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向主要体现在以下方面：首先，记忆更新机制虽能利用基础视觉语言模型判断更新时机，但仍依赖启发式方法而非端到端优化。未来可通过强化学习等方式，让智能体自主学习何时及如何更新记忆，从而更动态地适应复杂任务。其次，受计算资源限制，研究未在更大规模模型（如32B或70B）上验证方法扩展性。探索HyMEM与更强骨干模型的结合效果，是提升性能的关键方向。

结合个人见解，可能的改进思路包括：引入更细粒度的记忆结构，例如在图中增加任务层级关系，以支持更精准的多跳检索；设计自适应记忆遗忘机制，避免冗余信息累积；探索跨任务记忆迁移能力，提升智能体在新环境中的泛化效率。此外，可结合因果推理方法优化记忆检索过程，使智能体在长流程任务中更好地处理中间错误。

### Q6: 总结一下论文的主要内容

本文针对GUI智能体在处理长流程、多样化界面和频繁中间错误的实际计算机使用任务时面临的挑战，指出现有基于外部轨迹记忆的方法存在扁平化检索、缺乏结构化组织和自我进化能力的不足。受人类记忆机制启发，论文提出了混合自进化结构化记忆（HyMEM），其核心贡献是构建了一种图基记忆，将离散的高层符号化策略节点与连续的轨迹嵌入相结合。该方法支持多跳检索以获取更丰富多样的上下文，通过节点增、并、换操作实现记忆的自我进化，并在推理时动态刷新工作记忆以更好地支持多轮执行和阶段转换。实验表明，HyMEM能显著提升开源GUI智能体的性能，使7B/8B骨干模型达到甚至超越强闭源模型水平，例如将Qwen2.5-VL-7B提升了22.5%，并优于Gemini2.5-Pro-Vision和GPT-4o。这项工作为智能体的可扩展改进奠定了重要基础。
