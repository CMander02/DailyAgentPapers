---
title: "Thought-Retriever: Don't Just Retrieve Raw Data, Retrieve Thoughts for Memory-Augmented Agentic Systems"
authors:
  - "Tao Feng"
  - "Pengrui Han"
  - "Guanyu Lin"
  - "Ge Liu"
  - "Jiaxuan You"
date: "2026-04-14"
arxiv_id: "2604.12231"
arxiv_url: "https://arxiv.org/abs/2604.12231"
pdf_url: "https://arxiv.org/pdf/2604.12231v1"
categories:
  - "cs.CL"
  - "cs.IR"
tags:
  - "记忆增强"
  - "检索增强生成"
  - "长期记忆"
  - "智能体架构"
  - "算法创新"
  - "基准评测"
  - "自我演化"
relevance_score: 9.0
---

# Thought-Retriever: Don't Just Retrieve Raw Data, Retrieve Thoughts for Memory-Augmented Agentic Systems

## 原始摘要

Large language models (LLMs) have transformed AI research thanks to their powerful internal capabilities and knowledge. However, existing LLMs still fail to effectively incorporate the massive external knowledge when interacting with the world. Although retrieval-augmented LLMs are proposed to mitigate the issue, they are still fundamentally constrained by the context length of LLMs, as they can only retrieve top-K raw data chunks from the external knowledge base which often consists of millions of data chunks. Here we propose Thought-Retriever, a novel model-agnostic algorithm that helps LLMs generate output conditioned on arbitrarily long external data, without being constrained by the context length or number of retrieved data chunks. Our key insight is to let an LLM fully leverage its intermediate responses generated when solving past user queries (thoughts), filtering meaningless and redundant thoughts, organizing them in thought memory, and retrieving the relevant thoughts when addressing new queries. This effectively equips LLM-based agents with a self-evolving long-term memory that grows more capable through continuous interaction. Besides algorithmic innovation, we further meticulously prepare a novel benchmark, AcademicEval, which requires an LLM to faithfully leverage ultra-long context to answer queries based on real-world academic papers. Extensive experiments on AcademicEval and two other public datasets validate that Thought-Retriever remarkably outperforms state-of-the-art baselines, achieving an average increase of at least 7.6% in F1 score and 16% in win rate across various tasks. More importantly, we further demonstrate two exciting findings: (1) Thought-Retriever can indeed help LLM self-evolve after solving more user queries; (2) Thought-Retriever learns to leverage deeper thoughts to answer more abstract user queries.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）如何有效且高效地利用海量外部知识作为长期记忆的核心挑战。研究背景是，尽管LLM内部能力强大，但在与现实世界交互时，难以有效整合规模可能任意庞大的外部知识（例如个人化应用或领域专家系统中的数十亿标记数据）。现有方法主要分为两类，但均存在不足：一是通过扩展上下文窗口来构建长上下文LLM，但其计算复杂度通常与上下文长度成二次方关系，无法根本应对超大规模外部知识；二是检索增强LLM（RALM），它从外部知识库中检索原始数据块，但受限于LLM的上下文长度，只能检索固定数量的顶部数据块，可能遗漏关键信息；三是分层RALM（如构建树状记忆），它需要手动总结数据并形成固定结构，成本高、效率低且缺乏灵活性。同时，现有的智能体系统通常存储原始观察或未处理的交互日志，这些信息噪声大且难以有效检索。

因此，本文要解决的核心问题是：如何突破上下文长度和检索数量的限制，让LLM能够基于任意长的外部数据生成输出，并为其提供一个能够自我进化、推理感知的长期记忆机制。论文提出的Thought-Retriever框架，其关键思路是让LLM充分利用过去解决用户查询时生成的中间响应（即“思想”），通过过滤无意义和冗余思想、将其组织成思想记忆，并在处理新查询时检索相关思想。这相当于为基于LLM的智能体装备了一个通过持续交互而不断增强能力的自我进化的长期记忆系统。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：长上下文LLM、检索增强LLM（RALM）以及层次化RALM。

在**方法类**研究中，长上下文LLM（如MPT、LongChat）通过扩展上下文窗口来提升LLM的工作记忆，但其计算复杂度通常与上下文长度呈二次方关系，难以从根本上处理超大规模外部知识。检索增强LLM（如基于BM-25、Contriever、DRAGON等检索器）则从外部知识库中检索相关原始数据块，但仍受限于LLM的上下文长度，只能检索固定数量的数据块。层次化RALM尝试构建树状结构记忆以纳入更抽象的知识，但需要手动总结数据块并形成固定结构，成本高且缺乏灵活性。

本文提出的Thought-Retriever与上述方法有显著区别：它不直接检索原始数据，而是利用LLM在解决历史查询时生成的中间响应（即“思想”），将其组织成思想记忆库，并在处理新查询时检索相关思想。这种方法突破了上下文长度的限制，能以极低计算开销让LLM基于任意长的外部知识生成输出，同时实现了记忆的自我演化。

在**评测类**研究方面，现有基准往往无法充分评估LLM对超长上下文的理解和利用能力。为此，本文专门构建了AcademicEval这一新颖基准，要求LLM基于真实学术论文的超长上下文忠实回答问题，弥补了相关评测空白。

此外，近期**智能体系统**的研究通常将原始观察或交互日志存储为记忆，这些信息噪声大且难以有效检索。Thought-Retriever则提供了一种压缩的、具备推理意识的记忆机制，更适合需要长期连贯交互的智能体系统。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为“Thought-Retriever”的新型模型无关算法来解决大语言模型（LLM）在利用海量外部知识时受限于上下文长度的问题。其核心思想是让LLM不仅检索原始的“数据块”，更检索和利用过去解决用户查询时产生的中间“思考”，从而构建一个自我演化的长期记忆系统，使模型能够基于任意长的外部数据生成回答。

整体框架包含五个主要模块，形成一个闭环流程。首先，在**思考检索**阶段，系统接收用户查询后，通过嵌入相似度从外部知识库和已有的“思考记忆”中混合检索出最相关的Top-K项（既包括原始数据块，也包括已存储的思考）。接着，在**答案生成**阶段，LLM基于检索到的上下文信息生成针对当前查询的最终答案。然后，进入关键的**思考与置信度生成**阶段，LLM需要基于当前的查询和生成的答案，提炼出一个“思考”——这是一个经过抽象、验证的连贯知识点，并同时评估该思考的置信度，以过滤无意义或幻觉内容。之后是**思考合并**阶段，系统计算新生成的思考与记忆库中现有内容（其他思考或原始数据块）的嵌入相似度，若超过阈值则视为冗余。最后，在**思考记忆更新**阶段，只有那些被判定为高置信度且非冗余的新思考才会被存入“思考记忆”库中，从而实现记忆的动态、增量式更新。

该方法的关键技术创新点在于：1）**“思考”的正式定义与动态生成**：将思考定义为一种与特定查询和检索上下文绑定的、经过验证的抽象认知单元，它不同于静态的数据摘要，而是LLM交互过程的副产品，具有查询条件化、抽象性和已验证性。2）**灵活的图状记忆结构**：与传统的、预构建的树状层次化摘要方法不同，Thought-Retriever形成的记忆结构是随用户查询动态演化的图，更具灵活性。3）**根源追溯机制**：通过递归定义的根源映射，可以确保任何高层级思考都能追溯到其依据的原始数据块，保证了事实的可靠性和可验证性。4）**自我演化能力**：系统通过持续交互不断积累和精炼思考，使得记忆库的能力随时间增强，并能利用更深层的思考来回答更抽象的查询。这种方法以较低的计算开销，有效突破了传统检索增强方法在上下文窗口和检索数量上的根本限制。

### Q4: 论文做了哪些实验？

论文在三个数据集上进行了广泛的实验验证。实验设置方面，所有实验均使用Mistral-8x7B作为基础LLM，上下文长度为4,096个token。对于所有检索增强语言模型（RALMs），设置数据块大小（chunk size）为500，检索数量K=8，相似度阈值ε=0.85，最大上下文长度为2,000个token。主要使用无监督设计的Contriever作为核心检索器，以确保在不同领域的零样本性能。

使用的数据集/基准测试包括：
1.  新构建的**AcademicEval**基准：基于真实世界学术论文，要求LLM忠实利用超长上下文回答问题。包含三个子任务：Abstract-single（平均长度8,295词）、Abstract-multi（33,637词）和Related-multi（22,107词）。
2.  两个公共数据集：**GovReport**（单文档问答，平均长度8,910词）和**WCEP**（多文档问答，平均长度8,176词）。

对比方法涵盖多种类型：
1.  基于启发式的检索器：BM25和TF-IDF。
2.  基于深度学习的检索器：Contriever、DPR、DRAGON以及先进的Qwen3-Embed-8b。
3.  高级检索策略：IRCoT（迭代检索与思维链推理结合）。
4.  上下文压缩技术：RECOMP。
5.  完整上下文窗口基线：Full Context (left) 和 Full Context (right)。
6.  长上下文LLM基线：OpenOrca-8k和Nous Hermes-32k。

评估采用两个指标：F1分数（基于ROUGE-L计算生成文本与参考文本的语义相似度）和胜率（使用Qwen1.5-72B-chat作为AI评估器，比较不同方法响应优于Thought-Retriever的频率）。

主要结果：Thought-Retriever在所有数据集上均显著优于基线方法。关键数据指标显示，其在所有数据集上的F1分数平均提升至少7.6%，胜率平均提升16%。具体而言，在AcademicEval的Abstract-single任务上，Thought-Retriever的F1分数达到0.290，远高于最佳基线Nous Hermes-32k的0.247；在Abstract-multi任务上，其F1为0.275，优于Qwen3-Embed-8b的0.240。在公共数据集上，Thought-Retriever也表现出稳定且领先的性能。实验还验证了Thought-Retriever能通过解决更多用户查询实现自我进化，并学会利用更深层的“思想”来回答更抽象的查询。

### Q5: 有什么可以进一步探索的点？

这篇论文提出的Thought-Retriever系统虽然创新，但仍存在一些局限性，为未来研究提供了方向。首先，其核心依赖LLM自身生成的“思考”作为记忆单元，这可能导致错误或偏见在记忆库中累积和放大，未来需要研究更可靠的思考验证与纠错机制。其次，系统在“思考”的筛选与组织上仍较粗放，缺乏对思考之间复杂逻辑关系的结构化建模，未来可探索基于知识图谱或因果推理的层次化记忆组织方法。此外，实验主要基于学术问答场景，在动态开放环境（如实时决策、多轮对话）中的泛化能力有待验证。结合个人见解，可能的改进包括：引入多模态信息（如图表、代码）丰富思考单元；设计轻量化的记忆索引与检索架构，以降低系统延迟；探索与其他外部知识库的协同机制，实现“内部思考”与“外部事实”的互补增强。

### Q6: 总结一下论文的主要内容

这篇论文提出了Thought-Retriever，一种新颖的模型无关算法，旨在解决现有检索增强大语言模型受限于上下文长度、只能检索少量原始数据块的问题。其核心思想是让LLM在解决历史用户查询时，将其生成的中间响应（即“思考”）进行过滤、组织并存储为“思考记忆”，当处理新查询时则检索相关的思考而非原始数据。这相当于为基于LLM的智能体装备了一个能够自我演化的长期记忆系统。

方法上，该算法首先提取并过滤历史交互中的关键思考，然后将其结构化存入记忆库，最后根据新查询进行相关性检索与整合。论文还构建了AcademicEval新基准，要求模型基于真实学术论文的长上下文进行忠实回答。

实验表明，Thought-Retriever在多个数据集上显著优于现有基线，F1分数平均提升至少7.6%，胜率提升16%。主要结论证实了该方法的有效性：它能使LLM通过持续交互实现自我进化，并学会利用更深层的思考来回答更抽象的查询，从而极大增强了智能体利用外部海量知识的能力。
