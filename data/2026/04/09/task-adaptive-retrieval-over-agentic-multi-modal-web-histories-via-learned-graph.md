---
title: "Task-Adaptive Retrieval over Agentic Multi-Modal Web Histories via Learned Graph Memory"
authors:
  - "Saman Forouzandeh"
  - "Kamal Berahmand"
  - "Mahdi Jalili"
date: "2026-04-09"
arxiv_id: "2604.07863"
arxiv_url: "https://arxiv.org/abs/2604.07863"
pdf_url: "https://arxiv.org/pdf/2604.07863v1"
github_url: "https://github.com/S-Forouzandeh/ACGM-Agentic-Web"
categories:
  - "cs.IR"
  - "cs.AI"
tags:
  - "Agent Memory"
  - "Retrieval-Augmented Generation (RAG)"
  - "Multi-Modal Agent"
  - "Web Agent"
  - "Graph Neural Networks"
  - "Task Adaptation"
  - "Policy Gradient"
  - "Benchmark Evaluation"
relevance_score: 8.5
---

# Task-Adaptive Retrieval over Agentic Multi-Modal Web Histories via Learned Graph Memory

## 原始摘要

Retrieving relevant observations from long multi-modal web interaction histories is challenging because relevance depends on the evolving task state, modality (screenshots, HTML text, structured signals), and temporal distance. Prior approaches typically rely on static similarity thresholds or fixed-capacity buffers, which fail to adapt relevance to the current task context. We propose \textbf{ACGM}, a learned graph-memory retriever that constructs \emph{task-adaptive} relevance graphs over agent histories using policy-gradient optimization from downstream task success. ACGM captures heterogeneous temporal dynamics with modality-specific decay (visual decays $4.3\times$ faster than text: $λ_v{=}0.47$ vs.\ $λ_x{=}0.11$) and learns sparse connectivity (3.2 edges/node), enabling efficient $O(\log T)$ retrieval. Across WebShop, VisualWebArena, and Mind2Web, ACGM improves retrieval quality to \textbf{82.7 nDCG@10} (+9.3 over GPT-4o, $p{<}0.001$) and \textbf{89.2\% Precision@10} (+7.7), outperforming 19 strong dense, re-ranking, multi-modal, and graph-based baselines. Code to reproduce our results is available at{\color{blue}\href{https://github.com/S-Forouzandeh/ACGM-Agentic-Web}{Saman Forouzandeh}}.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多模态网络导航智能体在长交互历史中进行任务自适应检索的核心难题。研究背景是，智能体在执行网页任务（如在线购物）时，会产生包含截图、HTML文本和结构化信号的长序列历史记录。智能体需要从中高效、准确地检索出与当前任务状态相关的过往观察，以支持决策（例如，在浏览50步后，找回第20步的产品规格信息）。

现有方法存在明显不足。传统方法如滑动窗口仅关注近期记录，会遗漏关键的长期依赖；基于固定相似度阈值（如余弦相似度>0.7）的密集检索器无法适应任务进展中动态变化的关联性（例如，产品图片在比较阶段相关，在结算阶段则无关）；而现有方法通常对所有模态（视觉、文本）采用统一的时间衰减处理，忽视了视觉记忆比文本记忆衰减更快的认知事实，这导致检索精度下降。此外，随着历史记录增长，线性检索效率低下，而固定容量的缓冲区则可能导致重要远期信息被遗忘。

因此，本文要解决的核心问题是：如何设计一个检索系统，能够**动态适应任务上下文**来理解多模态历史记录中不断演化的相关性，同时兼顾**不同模态的异质性时间动态**，并实现**大规模历史下的高效检索**。论文提出的ACGM（自适应跨模态图记忆）通过学习一个由下游任务成功反馈驱动的、基于策略梯度的神经相关性预测器来构建任务自适应的关联图，从而直接优化检索以服务于最终任务目标，并在此过程中学习模态特定的衰减率和稀疏的图连接，以实现高效且精准的检索。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：记忆增强智能体、图基础与多模态检索，以及基于策略梯度的检索训练。

在**记忆增强智能体**方面，早期工作如Mem0和A-MEM依赖基于嵌入相似度的静态检索或最近启发式方法。多粒度方法构建跨时间尺度的分层记忆关联以改进对话上下文选择，但其检索拓扑一旦构建即固定。G-Memory为多智能体协作历史构建三层图层次结构，而HippoRAG和Zep则分别通过知识图谱进行关联检索或构建时序知识图谱。这些方法均依赖相似度驱动或启发式的边构建，缺乏任务层面的反馈信号。本文的ACGM则通过策略梯度优化将记忆构建视为一个可学习决策过程，使检索结构本身能适应当前任务。

在**图基础与多模态检索**方面，GraphRAG及其扩展展示了关系结构对复杂推理的益处，但其图基于共现或聚类构建且保持静态。密集和多模态检索器（如ANCE、CLIP）仅通过嵌入相似度确定相关性，未考虑任务上下文演变或模态特定的时序动态。时序IR模型应用全局衰减函数，假设所有内容类型动态同质。ACGM的差异在于两点：一是通过下游反馈学习任务依赖的相关性，而非静态相似度；二是学习模态特定的时序衰减，允许视觉、文本等信号以独立速率衰减。

在**策略梯度训练**方面，使用任务成功作为训练信号会引入高方差信用分配挑战。ACGM通过三阶段协议、指数移动平均基线以及多重校正评估来缓解此问题，确保了训练的稳定性和报告增益的可靠性。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为ACGM的学习型图记忆检索器来解决多模态网络交互历史中任务自适应检索的挑战。其核心方法是构建一个基于策略梯度优化的任务自适应相关性图，直接根据下游任务的成功来优化检索过程，从而取代传统的静态相似度阈值方法。

整体框架包含三个关键组件：学习型相关性预测器、模态特异性时间衰减机制和高效分层检索结构。主要模块包括：1）一个基于多层感知机的神经网络预测器 \( g_\phi \)，它接收冻结的预训练嵌入特征（视觉用CLIP，文本用RoBERTa）、编码了时间距离、余弦相似度和模态信息的特征向量，并输出观测对之间的相关性概率。该预测器通过策略梯度进行优化，目标函数是最大化下游任务的成功奖励，将检索图的构建视为强化学习问题，成功任务所依赖的边会得到增强。2）模态特异性时间衰减模块，该模块学习不同模态（视觉、文本、知识图谱）的衰减率 \(\lambda_m\)，用于在计算检索注意力分数时根据时间距离进行调制。研究发现视觉信息衰减速度远快于文本（\(\lambda_v = 0.47\) vs. \(\lambda_x = 0.11\)），这更符合认知规律。衰减率通过基于人工标注的损失函数进行正则化微调。3）高效分层检索结构，采用两层组织：近期的观测（如最近20步）存储在扁平结构中以便快速访问，而更早的观测则组织成一个通过在线k-means聚类构建的4叉树。检索时采用宽度为2的束搜索，从根节点开始，根据查询与子节点质心的相似度选择分支递归下降，最终实现 \(O(\log T)\) 的时间复杂度。

创新点主要体现在三个方面：首先，将交互式检索问题形式化为一个通过策略梯度优化的学习排序问题，利用延迟的任务成功信号而非静态标签，使检索策略能够适应动态变化的任务状态。其次，提出了异构的时间衰减模型，首次在检索中为不同模态学习不同的衰减率，显著提升了检索精度。最后，通过结合学习得到的稀疏图连接（平均每节点3.2条边）和分层索引结构，在保证高检索质量的同时实现了亚线性的检索效率，解决了长历史轨迹下的可扩展性问题。整个模型通过一个结合了检索损失、边预测损失和衰减损失的多目标函数进行两阶段训练，最终在多个基准测试中取得了显著的性能提升。

### Q4: 论文做了哪些实验？

论文在三个多模态网页导航基准测试上进行了实验：WebShop（1,180个产品搜索任务，平均轨迹长度24.3步）、VisualWebArena（910个真实世界导航任务，平均31.7步）和Mind2Web（2,350个来自137个真实网站、跨越31个领域的开放式任务，平均每任务7.3个动作）。实验设置包括：将专家动作5步时间窗口内的观察标记为相关，用于检索评估；使用nDCG@10、MAP@10、MRR、Recall@10和Precision@10衡量检索质量，并使用任务成功率衡量下游影响；在8×A100 GPU上使用AdamW进行训练，并通过三折交叉验证和配对t检验（Bonferroni校正）进行评估。

对比方法涵盖了19个强大的基线，分为四类：密集检索器（如ColBERT-v2、ANCE、Contriever、E5-Large）、神经重排序器（如MonoT5、RankGPT-4、RankLLaMA-3.1）、多模态检索器（如CLIP、BLIP-2、ImageBind、LLaVA-1.6、Gemini-Pro-1.5、GPT-4o、Claude-3.5-Sonnet）和图基方法（如GraphRAG、MGraphRAG、MMGraphRAG、MAHA、HM-RAG）。

主要结果显示，ACGM在所有基准测试中均实现了最先进的检索性能。关键数据指标如下：在WebShop上，ACGM的nDCG@10达到82.7，比GPT-4o高出9.3点，比最佳图基方法MAHA高出9.1点；在VisualWebArena上，nDCG@10为79.8，比GPT-4o高出9.2点；在Mind2Web上，nDCG@10为78.3，比GPT-4o高出5.5点。此外，ACGM的Precision@10达到89.2%，比GPT-4o高出7.7点。消融实验表明，完全稠密图导致最大性能下降（ΔnDCG@10 = -16.6），而移除时间衰减导致第二大下降（Δ = -14.0）。效率方面，在轨迹长度T=100时，ACGM检索延迟为14.7毫秒，比平坦密集检索快3.3倍，索引内存仅需2.1 GB（BLIP-2需6.3 GB），并实现了O(log T)的亚线性延迟扩展。

### Q5: 有什么可以进一步探索的点？

该论文在任务自适应检索方面取得了显著进展，但其局限性和未来研究方向仍值得深入探索。首先，ACGM依赖于策略梯度优化，这需要与环境交互获取任务成功信号，训练成本较高且可能受稀疏奖励影响。未来可探索更高效的离线优化方法，或结合自监督学习从历史数据中预训练相关性模式。其次，论文主要关注视觉和文本模态，未来可扩展至更丰富的模态（如音频、动态交互元素），并研究跨模态关联的联合衰减机制。此外，当前图结构的学习依赖于手工设计的稀疏性约束，未来可引入可微图稀疏化技术或动态边修剪算法，以更灵活地平衡效率与精度。最后，ACGM在零样本迁移中展示了泛化能力，但未深入探讨其在领域外任务或长周期任务中的适应性，未来可研究基于元学习或提示调整的快速适应机制，以增强在开放环境中的鲁棒性。

### Q6: 总结一下论文的主要内容

该论文针对智能体在多模态网页交互历史中检索相关观察的挑战，提出了一种名为ACGM的学习型图记忆检索器。核心问题是传统方法依赖静态相似度阈值或固定容量缓冲区，难以根据动态任务状态、不同模态（如截图、HTML文本）及时间距离自适应判断相关性。ACGM通过策略梯度优化，从下游任务成功中学习构建任务自适应的相关性图，其方法创新包括：引入模态特异性衰减机制（视觉信息衰减速度比文本快4.3倍），并学习稀疏连接（平均每个节点3.2条边），从而实现高效的O(log T)检索复杂度。实验表明，在WebShop、VisualWebArena和Mind2Web等基准测试中，ACGM在检索质量上显著优于19种基线方法，将nDCG@10提升至82.7（较GPT-4o提高9.3），Precision@10达到89.2%（提高7.7）。该研究的意义在于为长序列多模态交互提供了可动态适应任务上下文的检索框架，提升了智能体在复杂网页任务中的决策效率。
