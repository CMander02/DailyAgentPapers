---
title: "GAM: Hierarchical Graph-based Agentic Memory for LLM Agents"
authors:
  - "Zhaofen Wu"
  - "Hanrong Zhang"
  - "Fulin Lin"
  - "Wujiang Xu"
  - "Xinran Xu"
  - "Yankai Chen"
  - "Henry Peng Zou"
  - "Shaowen Chen"
  - "Weizhi Zhang"
  - "Xue Liu"
  - "Philip S. Yu"
  - "Hongwei Wang"
date: "2026-04-14"
arxiv_id: "2604.12285"
arxiv_url: "https://arxiv.org/abs/2604.12285"
pdf_url: "https://arxiv.org/pdf/2604.12285v1"
categories:
  - "cs.AI"
tags:
  - "Agent Memory"
  - "Hierarchical Memory"
  - "Graph-based Memory"
  - "Memory Consolidation"
  - "Long-term Interaction"
  - "Retrieval Strategy"
relevance_score: 9.0
---

# GAM: Hierarchical Graph-based Agentic Memory for LLM Agents

## 原始摘要

To sustain coherent long-term interactions, Large Language Model (LLM) agents must navigate the tension between acquiring new information and retaining prior knowledge. Current unified stream-based memory systems facilitate context updates but remain vulnerable to interference from transient noise. Conversely, discrete structured memory architectures provide robust knowledge retention but often struggle to adapt to evolving narratives. To address this, we propose GAM, a hierarchical Graph-based Agentic Memory framework that explicitly decouples memory encoding from consolidation to effectively resolve the conflict between rapid context perception and stable knowledge retention. By isolating ongoing dialogue in an event progression graph and integrating it into a topic associative network only upon semantic shifts, our approach minimizes interference while preserving long-term consistency. Additionally, we introduce a graph-guided, multi-factor retrieval strategy to enhance context precision. Experiments on LoCoMo and LongDialQA indicate that our method consistently outperforms state-of-the-art baselines in both reasoning accuracy and efficiency.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在维持长期、连贯的交互时面临的核心挑战：如何平衡快速感知实时交互信息与稳定保留长期知识之间的矛盾。

研究背景是，LLM智能体在复杂推理和问答中表现出色，但其“记忆”系统仍不完善。现有方法主要分为两类，各有不足。一类是“统一的流式记忆系统”，它将所有信息视为连续的流进行更新。这种方法容易受到瞬时噪声的干扰，导致两个严重问题：**记忆丢失**（已有知识因连接变弱而被遗忘）和**语义漂移**（不同主题被错误地混淆，破坏了主题一致性）。另一类是“离散的结构化记忆架构”，它通过刚性结构组织信息以确保稳定性，但缺乏实时更新叙事流的敏捷性，导致对话的连续性表征碎片化，难以适应长期对话的演变。尽管近期有研究尝试引入动态结构或优化检索，但未能从根本上解决即时编码与长期巩固之间的冲突。

因此，本文要解决的核心问题是：设计一个记忆框架，能够**从根本上解耦信息的即时编码与长期巩固过程**，从而在保障实时交互敏捷性的同时，确保长期知识的稳定性和一致性，避免噪声污染和语义失真。论文提出的GAM框架通过分层图结构和语义事件触发机制来实现这一目标。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类与评测类，本文的方法与它们既有联系又有区别。

在**方法类**研究中，现有工作主要分为两大范式。一是**统一流式记忆系统**，如Generative Agents、MemGPT、MemoryOS和Mem0等，它们采用类似操作系统的分层结构，在工作上下文和外部存储间交换信息，以实现快速信息编码和无限上下文管理。然而，这些方法缺乏写入隔离，新获取的（可能含噪声的）信息直接并入长期存储，易导致“记忆污染”，造成语义漂移或记忆丢失。即使是A-Mem这类自反思代理，其更新也基于任意令牌数或时间步，而非语义完整性，无法防止稳定知识被瞬时对话状态破坏。二是**离散结构化记忆架构**，如GraphRAG、StructRAG、LightRAG和G-Memory，它们通过构建静态或双层知识图谱来确保稳定性和实现精确的多跳推理，但往往因昂贵的索引构建而显得僵化、延迟高，难以适应开放域对话中流畅的叙事演变，导致话语表示碎片化。

在**应用类**研究中，近期工作尝试在稳定性和可塑性间架桥。例如，AriGraph引入了情景节点来追踪状态变化，但其专为具有离散状态转换的文本游戏设计，难以处理自然对话中模糊的边界。Zep则侧重于优化检索基础设施，而非解决编码与巩固之间的认知冲突。

本文提出的GAM框架与上述研究均不同。它**明确将记忆编码与巩固解耦**，通过将进行中的对话隔离在事件进展图中，并仅在发生语义转变时才将其整合到主题关联网络中，从而最小化干扰并保持长期一致性。这有效解决了快速上下文感知与稳定知识保留之间的冲突，弥补了现有方法在写入隔离和动态适应性方面的不足。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为GAM的分层图基智能体记忆框架来解决长期交互中快速感知与稳定知识保留之间的冲突。其核心方法是将记忆编码与巩固过程显式解耦，采用分层图结构来分离不同生命周期的记忆内容。

整体框架由三个协调的阶段构成：1) **情景缓冲阶段**：将当前对话流隔离在本地事件进展图中，该图由原子交互单元（如用户话语）作为节点，以时序和因果边连接，形成一个受保护的写入隔离缓冲区，防止高频更新干扰全局记忆。2) **语义巩固阶段**：当通过语义边界检测（由LLM驱动的判别器触发）判定当前叙事单元语义完整时，系统将缓冲的事件图合并到全局主题关联网络中。合并时创建具有双粒度表示的新主题节点（包含LLM生成的语义摘要和原始文本细节），并通过粗到细的候选选择策略（先向量检索top-5主题节点，再经LLM语义评分器建立语义边）将其集成到全局网络中。3) **图引导检索阶段**：采用多因素遍历策略进行检索，首先在主题网络中通过向量相似性找到语义锚点并扩展其一阶邻居，然后通过跨层关联访问对应的归档事件图以获取具体细节，最后通过多因素重排序（结合交叉编码器的语义概率与时间、置信度、角色等调制因子）对候选记忆进行精准排序。

架构设计上，记忆结构被定义为复合图，包含四个关键组件：代表长期稳定知识的主题关联网络（节点为高层语义主题，边为LLM量化的语义关联）、代表临时上下文缓冲区的事件进展图、存储已巩固事件图的归档集合、以及连接主题节点与归档事件图的跨层关联边。这种分解实现了存储的结构性分离。

关键技术创新点包括：1) **基于状态的巩固机制**：将叙事动态建模为有限状态机，仅在检测到语义边界时才触发原子性的巩固操作，平衡了更新效率与稳定性。2) **双粒度节点表示**：在巩固时同时保留摘要和原始文本，兼顾抽象推理与细节回忆。3) **图引导的多因素检索**：利用图拓扑进行自上而下的“扩展-下钻”检索，并通过调制因子整合语义与上下文信号，提升了检索精度。这些设计共同使系统在减少干扰的同时保持了长期一致性，并在实验中显示出优于基线方法的性能。

### Q4: 论文做了哪些实验？

论文在LoCoMo和LongDialQA两个长程交互基准上进行了实验评估。实验设置上，GAM是一个无需训练的记忆框架，使用PyTorch和HuggingFace实现，并利用Ollama和LiteLLM进行高效推理。评估了包括Llama-3.2-3B-Instruct、Qwen2.5-7B/14B-Instruct和GPT-4o-mini在内的多种规模骨干模型，均使用开箱即用的指令调优版本。记忆索引使用all-MiniLM-L6-v2句子嵌入，重排序使用cross-encoder/ms-marco-MiniLM-L-6-v2。检索大小k设为10，调制因子β_time=1.4，β_role=1.4，β_conf=1.2。

对比方法涵盖了三大范式：启发式方法（MemoryBank、ReadAgent）、统一流式系统（MemGPT、MemoryOS、Mem0）以及自演进代理A-Mem。主要使用F1分数（实体捕获）和BLEU-1（词汇准确性）作为评估指标。

在LoCoMo数据集上，GAM在多数设置下取得了最佳平均性能。例如，使用Qwen2.5-7B骨干时，在Temporal任务上的F1分数超越Mem0超过18%（48.97 vs 41.22）。在GPT-4o-mini上，GAM取得了最高的平均F1分数43.14。在LongDialQA数据集上，GAM同样一致优于所有基线，在Qwen2.5-7B上取得了12.55的平均F1，超越MemoryOS达86%。

消融实验表明，移除事件进展图（w/o EPG）导致性能下降最严重（平均F1从40.00降至25.06），验证了叙事结构的重要性。效率分析显示，GAM实现了最低的令牌消耗（每查询1370个令牌），比Mem0降低11%，并在保持可比速度的同时获得了13%的F1提升。

### Q5: 有什么可以进一步探索的点？

本文提出的GAM框架虽在文本对话任务中表现出色，但其主要局限性在于仅支持文本模态，无法处理现实交互中常见的视觉、听觉等多模态信息。这限制了系统在需要跨模态推理场景（如具身交互、视频对话）中的应用。未来研究可探索多模态扩展，例如将记忆节点升级为融合文本摘要与关键帧、音频特征等的混合表示，并利用跨模态信号（如图像变化、语调转折）来触发记忆整合的状态切换。此外，当前框架依赖于预定义的语义转移检测机制，未来可引入更动态的、基于学习的方法来自适应地控制记忆编码与整合的平衡。另一个潜在方向是将GAM与外部知识库更深度结合，使长期记忆不仅能存储对话历史，还能主动关联领域知识，从而提升复杂任务中的推理能力。

### Q6: 总结一下论文的主要内容

该论文提出了GAM，一种基于层次化图结构的智能体记忆框架，旨在解决LLM智能体在长期交互中面临的新信息获取与旧知识保留之间的冲突。当前统一的流式记忆系统虽便于上下文更新，但易受瞬时噪声干扰；而离散的结构化记忆架构虽能稳健保留知识，却难以适应动态演进的叙事。为此，GAM将记忆编码与巩固过程显式解耦，通过状态切换机制分离叙事缓冲与语义整合，仅在语义完整边界更新记忆，从而隔离噪声并保持长期一致性。方法上，它利用事件进展图暂存持续对话，并在语义变化时将其整合至主题关联网络，同时引入融合时序、置信度和角色中心信号的多因素图引导检索策略以提升上下文精度。实验表明，在LoCoMo和LongDialQA基准上，GAM在推理准确性和效率上均优于现有先进基线。其核心贡献在于通过层次化图结构有效平衡了快速感知与稳定记忆，为智能体长期连贯交互提供了新思路。
