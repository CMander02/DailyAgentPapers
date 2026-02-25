---
title: "HiSAC: Hierarchical Sparse Activation Compression for Ultra-long Sequence Modeling in Recommenders"
authors:
  - "Kun Yuan"
  - "Junyu Bi"
  - "Daixuan Cheng"
  - "Changfa Wu"
  - "Shuwen Xiao"
  - "Binbin Cao"
  - "Jian Wu"
  - "Yuning Jiang"
date: "2026-02-24"
arxiv_id: "2602.21009"
arxiv_url: "https://arxiv.org/abs/2602.21009"
pdf_url: "https://arxiv.org/pdf/2602.21009v1"
categories:
  - "cs.IR"
  - "cs.CL"
tags:
  - "推荐系统"
  - "长序列建模"
  - "个性化代理"
  - "稀疏激活"
  - "注意力机制"
  - "效率优化"
relevance_score: 5.5
---

# HiSAC: Hierarchical Sparse Activation Compression for Ultra-long Sequence Modeling in Recommenders

## 原始摘要

Modern recommender systems leverage ultra-long user behavior sequences to capture dynamic preferences, but end-to-end modeling is infeasible in production due to latency and memory constraints. While summarizing history via interest centers offers a practical alternative, existing methods struggle to (1) identify user-specific centers at appropriate granularity and (2) accurately assign behaviors, leading to quantization errors and loss of long-tail preferences. To alleviate these issues, we propose Hierarchical Sparse Activation Compression (HiSAC), an efficient framework for personalized sequence modeling. HiSAC encodes interactions into multi-level semantic IDs and constructs a global hierarchical codebook. A hierarchical voting mechanism sparsely activates personalized interest-agents as fine-grained preference centers. Guided by these agents, Soft-Routing Attention aggregates historical signals in semantic space, weighting by similarity to minimize quantization error and retain long-tail behaviors. Deployed on Taobao's "Guess What You Like" homepage, HiSAC achieves significant compression and cost reduction, with online A/B tests showing a consistent 1.65% CTR uplift -- demonstrating its scalability and real-world effectiveness.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决推荐系统中超长用户行为序列建模的实际部署难题。现代推荐系统依赖超长行为序列捕捉用户动态偏好，但直接端到端建模会因计算和内存开销导致生产环境延迟过高。现有方法通常通过将历史行为归纳为若干兴趣中心来压缩序列，但存在明显不足：一方面，现有方法（如ELASTIC、PolyEncoder）使用固定数量的全局兴趣嵌入，无法适应不同用户兴趣中心数量和粒度的个性化差异；另一方面，基于时间分段、局部敏感哈希或聚类的分组方法不稳定且对超参数敏感，常导致语义相近的行为被错误分割，产生量化误差，并丢失有价值的长尾偏好。

因此，本文的核心问题是：如何设计一种高效的序列压缩框架，既能**个性化地识别用户特定兴趣中心（解决数量和粒度自适应问题）**，又能**准确地将历史行为分配到最相关的兴趣中心（减少量化误差并保留长尾行为）**，从而在降低计算成本的同时，提升推荐效果。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：序列建模方法、序列压缩技术和量化表示学习。

在**序列建模方法**方面，早期工作如DIN利用注意力机制捕捉短期兴趣。后续研究认识到超长序列的价值，但直接建模成本高昂，因此出现了两阶段方法（如SIM、TWIN），先检索行为子集再排序。然而，这类方法存在检索与排序不一致的风险，可能丢失有价值的行为信号。HiSAC则通过端到端的层次化压缩来避免这种不一致性。

在**序列压缩技术**方面，ELASTIC和PolyEncoder等方法将序列压缩为固定数量的全局兴趣嵌入，虽提升了效率，但忽略了用户兴趣粒度的差异性。此外，基于局部敏感哈希（LSH）、K-Means聚类或时间分割的压缩方法，可能因语义不匹配、分配不稳定或忽略语义邻近性而导致信息损失。HiSAC通过构建层次化语义码本和个性化稀疏激活，旨在更精细地保留用户特定的兴趣中心，尤其是长尾偏好。

在**量化表示学习**方面，VQ-VAE及其变体（如VQ-VAE-2、RQ-VAE）通过离散码本学习紧凑表示，在视觉和语音领域广泛应用。HiSAC借鉴了多级量化（如RQ-VAE）的思想，但将其与个性化兴趣代理选择和软路由注意力相结合，专注于减少推荐场景中的量化误差，并实现工业级可扩展性。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为HiSAC（Hierarchical Sparse Activation Compression）的三阶段高效框架来解决超长用户行为序列建模中的计算和内存挑战，同时避免现有方法在粒度识别和行为分配上的不足。其核心方法、架构设计和关键技术如下：

**整体框架**：HiSAC将超长序列压缩为一个紧凑的兴趣表示集合，过程分为三个阶段：历史行为标记化、层次化投票稀疏激活兴趣代理、以及软路由注意力生成压缩表示。

**主要模块与关键技术**：
1.  **多模态编码与离散化**：首先，使用大规模多模态编码器为所有物品生成解耦的、去偏的连续语义嵌入，以提升泛化能力。随后，通过残差量化变分自编码器（RQ-VAE）将这些连续嵌入离散化为一个L层的层次化码本，为每个物品分配一个L层的语义ID（SID），从而将用户历史序列标记到离散的语义空间中。
2.  **层次化投票与稀疏激活**：为解决个性化兴趣中心识别问题，HiSAC构建了一个全局的(L+1)层语义树，其中每个节点对应一个码字。基于用户的标记化历史，执行自底而上的投票传播：每个叶子节点（对应一个完整SID）根据映射到的物品数量获得投票，内部节点的票数为其后代票数之和。然后，采用自顶向下的层间稀疏化：在每一层，仅保留每个激活父节点下票数最高的前k个子节点，其余被剪枝。最终保留的激活叶子节点即构成用户的个性化兴趣代理集合，每个代理由其根到叶的路径（SID）表示，并附带一个基于票数软归一化的权重。这个过程实现了自适应、稀疏的兴趣中心选择，避免了组合爆炸。
3.  **软路由注意力聚合**：为解决硬分配导致的量化误差和长尾行为丢失问题，HiSAC为每个兴趣代理计算其压缩表示时，采用基于语义相似性的软路由注意力机制。关键创新在于使用**两种不同的物品嵌入**：冻结的、基于多模态的**语义嵌入**用于计算物品与兴趣代理原型（由对应码字求和得到）之间的L2距离，从而生成去偏的注意力权重；同时，端到端学习的**排序嵌入**（融合了物品特征和时间衰减）作为被聚合的内容。每个代理的最终表示是其对应权重与所有历史物品排序嵌入的加权和，权重由语义相似性经温度控制softmax归一化得到。这使得每个代理能柔和地聚合整个历史序列的信息，最小化量化误差并保留长尾行为信号。

**创新点**：
*   **层次化稀疏激活机制**：通过构建全局语义树和投票剪枝，动态、个性化地识别多粒度兴趣中心，实现了计算资源的聚焦。
*   **双嵌入软路由注意力**：创新性地分离语义相似性计算与排序信号聚合，使用语义嵌入引导路由、排序嵌入进行聚合，有效缓解了量化偏差并利用了长尾交互。
*   **工业级部署优化**：结合离线兴趣代理构建、请求级序列压缩和缓存增强的多头注意力等优化策略，显著降低了在线推理延迟和计算成本，实现了大规模实时部署。在淘宝的线上A/B测试中取得了稳定的CTR提升，验证了其有效性和可扩展性。

### Q4: 论文做了哪些实验？

论文在工业数据集和公开数据集上进行了全面的实验评估。实验设置方面，模型使用Adam优化器（稠密参数）和Adagrad优化器（稀疏参数），初始学习率为1e-3。在工业数据集上，输入特征包括用户ID、性别、商品ID、商品类别和用户行为序列，商品信息通过冻结的CLIP编码，RQ-VAE配置为2个量化层，每层码本大小为512。在Taobao-MM数据集上，使用基于SCL的多模态嵌入训练RQ-VAE，码本大小为200x2。所有对比方法均将用户序列压缩为200组。

使用的数据集/基准测试包括：1）工业数据集：来自淘宝的真实交互日志，包含约2亿用户、10亿商品和300亿条交互记录，最大序列长度为10,000，前13天用于训练，最后一天用于验证；2）Taobao-MM公开数据集：包含886万用户和2.75亿商品，最大序列长度为1,000。离线评估指标采用AUC和GAUC，在线A/B测试则关注点击率（CTR）、点击转化率（CTCVR）等实用性和用户参与度指标。

对比方法分为两类：一是经典的序列压缩技术，包括K-Means、局部敏感哈希（LSH）、按时间分块（Patching）和可学习聚合器（Aggregator），均与多头注意力（MHA）结合；二是业界先进的序列建模方法，包括PatchRec、ELASTIC和Longer。

主要结果显示，HiSAC在离线指标上全面优于基线。在工业数据集上，HiSAC的AUC达到0.6444，GAUC达到0.5525，显著优于其他压缩方法（如Patching效果最差）。当集成到SOTA模型（如PatchRec、ELASTIC）中并替换其压缩模块时，HiSAC能一致提升AUC和GAUC，证明了其鲁棒性和泛化能力。序列长度缩放分析表明，HiSAC能有效利用超长序列信息，性能随序列增长持续提升且未饱和。在线A/B测试中，HiSAC在淘宝“猜你喜欢”场景实现了1.65%的CTR稳定提升。关键数据指标包括：HiSAC相比移除多模态编码器变体带来0.2个百分点的AUC提升；软路由注意力相比硬路由带来0.09个百分点的AUC提升；分层投票机制将激活的兴趣代理数量减少约三分之二（从约300%降至基线水平），而AUC仅损失0.01个百分点。

### Q5: 有什么可以进一步探索的点？

本文提出的HiSAC框架在压缩超长序列和捕捉细粒度兴趣方面取得了显著效果，但仍存在一些局限性和值得深入探索的方向。首先，其核心依赖于预定义的语义ID层次结构，这限制了模型动态适应不同用户行为模式的能力；未来可研究如何让层次结构本身也能从数据中学习或自适应调整，例如引入可学习的聚类或层次生成过程。其次，方法主要优化了历史行为的聚合，但对实时兴趣漂移的捕捉可能不足；可探索结合短期会话序列或实时交互信号，设计动态更新的兴趣代理机制。此外，模型在工业场景的部署中强调了效率，但对可解释性的挖掘较浅；未来可分析不同层次兴趣中心的具体语义，并将其用于可解释的推荐理由生成。最后，当前实验集中于电商场景，其方法在社交网络、视频平台等具有更复杂行为模式的应用中的泛化能力有待验证；可探索跨领域或跨任务的迁移学习，以提升框架的通用性。

### Q6: 总结一下论文的主要内容

该论文针对推荐系统中超长用户行为序列建模的效率和精度问题，提出了分层稀疏激活压缩框架HiSAC。核心贡献在于通过分层语义编码与稀疏激活机制，在保证推理效率的同时，显著降低了长序列建模中的量化误差和长尾偏好丢失。

方法上，HiSAC首先将用户交互编码为多层语义ID，构建全局分层码本。通过分层投票机制稀疏激活个性化的兴趣代理，作为细粒度偏好中心。在此基础上，采用软路由注意力在语义空间聚合历史信号，依据相似度加权以减少量化误差。

主要结论显示，HiSAC在淘宝“猜你喜欢”场景中实现了显著的序列压缩与成本降低，在线A/B测试取得了1.65%的点击率稳定提升，证明了其在大规模生产环境中的有效性与可扩展性。该工作为超长序列建模提供了兼顾效率与个性化精度的实用解决方案。
