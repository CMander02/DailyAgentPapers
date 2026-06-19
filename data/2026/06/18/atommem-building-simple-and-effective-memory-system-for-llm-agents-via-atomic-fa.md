---
title: "AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts"
authors:
  - "Yanyu Yao"
  - "Shangze Li"
  - "Zhi Zheng"
  - "Hui Zheng"
  - "Qi Liu"
  - "Tong Xu"
  - "Enhong Chen"
date: "2026-06-18"
arxiv_id: "2606.19847"
arxiv_url: "https://arxiv.org/abs/2606.19847"
pdf_url: "https://arxiv.org/pdf/2606.19847v1"
categories:
  - "cs.CL"
tags:
  - "Agent记忆系统"
  - "记忆增强"
  - "原子事实提取"
  - "长时记忆"
  - "层次化记忆"
  - "时效性建模"
  - "智能体长期交互"
  - "个人化Agent"
relevance_score: 9.0
---

# AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts

## 原始摘要

Large language models (LLMs) demonstrate strong reasoning and generation abilities, but their fixed context windows limit long-term information accumulation and reuse across multi-session interactions. Existing memory-augmented systems often construct memory in a coarse and unstable manner, relying on inefficient memory representations or unstable unconstrained updates. To address these challenges, we propose AtomMem, a long-term memory system designed for value-dense storage and stable memory evolution. AtomMem introduces a Fact Executor, which selectively extracts high value atomic facts from long form interactions to serve as highly efficient memory representations. Subsequently, AtomMem organizes these facts into hierarchical event structures and temporal profiles, capturing coherent episodic contexts and tracking dynamically evolving user attributes over time. During retrieval, the system activates an associative memory graph to connect fragmented memories. Experiments on the LoCoMo benchmark confirm that AtomMem achieves state-of-the-art performance across various reasoning tasks, offering a scalable and economically viable solution for deploying intelligent personalized agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大语言模型（LLM）驱动的智能体在长期交互中面临的核心挑战：如何构建一个既高密度存储信息又稳定演进的记忆系统，以克服现有方法的严重缺陷。研究背景在于，LLM虽具备强大的推理与生成能力，但其固定长度的上下文窗口限制了跨多轮会话的长期信息积累与复用，导致智能体易遗忘用户偏好、重复回答或与既定事实矛盾。现有记忆增强系统的主要不足体现在三个方面：一是在记忆表示上陷入两难，原始对话存储信息冗余、噪声巨大，而压缩表示又丢失细节并因LLM生成而累积错误，无法实现信息密度与上下文保真度的平衡；二是在记忆更新上，现有依赖LLM频繁重写的动态机制（如通过重构整个记忆条目）极不稳定，幻觉或错误编辑会反复修改同一记忆，导致事实被破坏和不受控制的扩展；三是在记忆检索上，当前方法多基于孤立条目的扁平化检索，难以捕捉跨会话的记忆关联，无法恢复个性化辅助所需的关联证据。为克服这些挑战，论文提出AtomMem系统，其核心思路是围绕“原子事实”这一高价值、自包含的记忆表示单元，通过稳定的事实提取器获取密集存储，组织成层级事件结构与时间画像，并利用关联记忆图进行检索，旨在为LLM智能体提供一个简单、有效、稳定且可扩展的长期记忆解决方案。

### Q2: 有哪些相关研究？

相关研究主要分为三类。首先，在**方法类**中，检索增强生成（RAG）是基础，如REALM提升开放域问答，后续工作如ActiveRAG和Self-RAG优化了检索时机与输出质量。本文的AtomMem与此类似，但核心区别在于其专门为LLM Agent设计，通过细粒度的“原子事实”提取替代粗粒度的文本经验存储，从而解决现有RAG系统在长期记忆中价值密度低、更新不稳定的问题。

其次，**记忆架构类**工作可细分为： (1) 文本经验型，如Think-in-Memory和RMM，存储历史思考或对话摘要，但AtomMem认为这些表示易出错且缺乏结构化； (2) 符号关系型，如RET-LLM使用三元组、Mem0使用知识图谱，本文则通过层次化事件结构和时间画像提供更连贯的叙事上下文； (3) 分层管理型，如MemGPT和MemoryOS使用显式界面，而AtomMem通过关联记忆图连接碎片化记忆，实现更灵活的检索。

最后，在**评测类**中，LoCoMo和LongMemEval评估超长对话记忆，PERMA关注动态用户画像。AtomMem在LoCoMo上实现SOTA，表明其在标准化评测中的优势。

### Q3: 论文如何解决这个问题？

AtomMem通过构建原子事实驱动的结构化记忆系统解决粗粒度、不稳定记忆问题。整体架构包含三大核心模块：事实提取层、结构化存储层与层次化检索层。

**核心方法**是采用监督微调的原子事实提取器（Atomic Fact Extractor），将原始对话转化为自包含的原子事实。每个事实被封装为结构化单元，包含唯一ID、文本内容、语义向量以及参与者、关键词、时间戳等元数据。系统通过混合相似度（语义嵌入+关键字Jaccard系数）进行去重与冲突检测，仅存储残差信息，避免冗余。

**存储系统**采用三层结构：
1. **原子事实**作为最小语义单元，通过验证机制实现稳定的增量更新；
2. **事件层**将相关事实聚合为连贯叙事块，通过动态吸收或创建事件维护上下文连贯性；
3. **用户画像层**采用会话级批量机制，追踪用户长期动态属性（如偏好、习惯），并保留历史版本。

**检索机制**的创新在于三级层次化策略：通过元数据过滤与混合相似度进行主召回和补偿召回，最后利用包含实体边、事件边与时间边的关联图进行随机游走传播激活，从而连接碎片化记忆。系统还支持独立画像检索，结合时间约束获取用户状态演变信息。

关键技术包括：基于IDF的语义边权重计算、事件大小惩罚机制的时间边衰减函数，以及融合事件与事实相似度的评分函数，确保检索兼具精准性和上下文完整性。

### Q4: 论文做了哪些实验？

论文在LoCoMo和LongMemEval两个基准上进行了实验。LoCoMo数据集包含平均35轮对话、600余轮交互的长上下文问答，LongMemEval则用500个问题测试聊天助手的记忆能力。对比方法包括LoCoMo、MemoryBank、A-MEM、MEM0、MemoryOS和LightMem，均使用GPT-4o-mini作为统一骨干模型。评估指标包括Token级F1、BLEU-1和LLM-as-a-Judge（J），并统计API token消耗。

主要结果方面，AtomMem在所有指标上达到最优：S-H F1=56.66、J=78.48，M-H F1=42.50、J=68.44，Temporal F1=62.78、J=66.98，Open Domain J=64.58，均大幅领先基线。相比最强基线LightMem，M-H和Temporal的J分数分别提升5.5%和31.1%。消融实验显示：移除层次结构（AtomMem-Flat）后仍显著优于原始LoCoMo，证明原子事实的有效性；去掉profile记忆中S-H F1下降至50.91；去掉图召回后M-H性能明显下降。检索容量实验确定k=10为最佳平衡点。AtomMem token消耗为21357K，相比MEM0降低约61.4%。

### Q5: 有什么可以进一步探索的点？

首先，论文明确指出其性能高度依赖底层LLM的生成稳定性，这在高噪声或长尾对话场景中可能成为瓶颈。未来可探索引入基于检索增强的校验机制，如结合外部知识图谱对原子事实进行交叉验证，以降低对单次LLM输出的依赖。其次，当前系统仅处理文本交互，而现实中多模态信息（如图像、音频）的整合将丰富记忆表示。建议采用多模态编码器（如CLIP）将视觉和语音特征映射到统一语义空间，再通过原子事实提取模块筛选高密度信息。此外，尽管系统在token效率上表现良好，但事件结构的分层粒度仍可优化。可尝试动态剪枝策略，例如基于强化学习自适应调整层次深度，在保留关键上下文的同时减少冗余。最后，现有记忆图检索主要依赖静态关联，未来可引入时间衰减权重或用户反馈信号（如点击率）对图边进行动态更新，从而模拟人类记忆的遗忘和强化机制。

### Q6: 总结一下论文的主要内容

大型语言模型(LLM)因固定上下文窗口难以实现跨会话的长期信息积累与复用。现有记忆增强系统存在记忆表征粗粒度、不稳定的问题，效率低下。为此，本文提出AtomMem长期记忆系统，核心是构建高价值密度的稳定记忆。方法上，AtomMem通过“事实执行器”从长文本交互中精准提取高价值原子事实作为高效记忆表征；随后将这些事实组织为层级事件结构和时间画像，以捕获连贯的片段化上下文并动态追踪用户属性的演变；检索时，系统激活关联记忆图连接零散事实。在LoCoMo基准测试上，AtomMem在多个推理任务中取得了最先进性能，其简化平面变体的优异结果进一步验证了记忆存储质量的核心地位，表明结构化事实比非结构化历史提供更优的检索基础。该工作为部署可持续个性化长期交互的智能体提供了可扩展且经济高效的解决方案。
