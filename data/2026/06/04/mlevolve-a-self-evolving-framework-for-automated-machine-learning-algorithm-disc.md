---
title: "MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery"
authors:
  - "Shangheng Du"
  - "Xiangchao Yan"
  - "Jinxin Shi"
  - "Zongsheng Cao"
  - "Shiyang Feng"
  - "Zichen Liang"
  - "Boyuan Sun"
  - "Tianshuo Peng"
  - "Yifan Zhou"
  - "Xin Li"
  - "Jie Zhou"
  - "Liang He"
  - "Bo Zhang"
  - "Lei Bai"
date: "2026-06-04"
arxiv_id: "2606.06473"
arxiv_url: "https://arxiv.org/abs/2606.06473"
pdf_url: "https://arxiv.org/pdf/2606.06473v1"
github_url: "https://github.com/InternScience/MLEvolve"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "LLM Agent"
  - "多智能体框架"
  - "自我进化"
  - "机器学习算法发现"
  - "树搜索"
  - "记忆机制"
  - "MLE-Bench"
  - "长期任务"
relevance_score: 9.5
---

# MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery

## 原始摘要

Large language model (LLM) agents are increasingly applied to long-horizon tasks such as scientific discovery and machine learning engineering (MLE), where sustained self-evolution becomes a key capability. However, existing MLE agents suffer from inter-branch information isolation, memoryless search, and lack of hierarchical control, which together hinder long-horizon optimization. We present MLEvolve, an LLM-based self-evolving multi-agent framework for end-to-end machine learning algorithm discovery. By extending tree search to Progressive MCGS, MLEvolve enables cross-branch information flow through graph-based reference edges and gradually shifts the search from broad exploration to focused exploitation with an entropy-inspired progressive schedule. To allow the agent to evolve with accumulated experience, we introduce Retrospective Memory, which combines a cold-start domain knowledge base with a dynamic global memory for task-specific experience retrieval and reuse. For stable long-horizon iteration, we further decouple strategic planning from code generation with adaptive coding modes. Evaluation on MLE-Bench shows that MLEvolve achieves state-of-the-art performance across multiple dimensions including average medal rate and valid submission rate under a 12-hour budget (half the standard runtime). Moreover, MLEvolve also outperforms specialized algorithm discovery methods including AlphaEvolve on mathematical algorithm optimization tasks, demonstrating strong cross-domain generalization. Our code is available at https://github.com/InternScience/MLEvolve.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）驱动的自动化机器学习（AutoML）算法发现中，现有智能体在长时间跨度任务中自我进化能力不足的问题。研究背景是，LLM智能体已被广泛应用于科学发现与机器学习工程（MLE）等需要持续迭代优化的场景。然而，现有的MLE智能体面临三个关键缺陷：首先，搜索机制存在“分支间信息隔离”，即不同搜索路径之间无法共享成功的策略，且采用固定探索策略导致资源分配低效；其次，搜索过程“无记忆”，只传递标量奖励，无法积累和复用之前迭代中的经验；最后，缺乏分层控制，将规划与代码实现耦合在一次生成中，导致修改不可控且迭代效率低下。本文的核心问题是构建一个能够自我进化的端到端算法发现框架，解决上述瓶颈，实现对机器学习流水线（从数据准备到模型训练及推理）的长期稳定优化。为此，论文提出了MLEvolve，它通过渐进式蒙特卡洛图搜索实现跨分支信息流动与自适应探索，利用回溯记忆模块自动积累和检索任务经验，并结合分层规划与自适应代码生成来解耦策略与实现，从而在有限预算内实现更优的算法发现性能。

### Q2: 有哪些相关研究？

根据论文内容，相关研究可以分为三类：

1. **基于搜索的MLE方法**：如AIDE（贪心搜索，易陷入局部最优）、ML-Master和AIRA-Dojo（MCTS）、MARS（预算感知MCTS+对比反思）、FM-Agent（进化多岛并行搜索）。本文MLEvolve通过Progressive MCGS扩展树搜索为图搜索，引入跨分支信息流和渐进式探索-利用调度，克服了这些方法的信息孤岛和无记忆搜索问题。

2. **基于记忆和经验复用的方法**：如AutoMind和Leeroo（领域知识库）、ML-Master 2.0（层次认知缓存）、ROME（推理梯度动量记忆）、MARS（对比反思）。本文的Retrospective Memory将冷启动知识库与动态全局记忆结合，无需额外LLM进行显式反思即可自动积累和复用经验，更具效率。

3. **基于图结构的方法**：如LocAgent和CodexGraph（图作为静态依赖表示，不演化）。本文的MCGS面向开放式代码生成，通过动态引用边实现跨分支信息流和轨迹复用，图结构随搜索动态演化。

MLEvolve的主要区别在于其自我进化视角，通过层次化解耦策略规划与代码生成（自适应编码模式）实现长期稳定迭代，并在MLE-Bench和数学算法优化任务中均取得最优结果。

### Q3: 论文如何解决这个问题？

MLEvolve通过三个核心组件构建了一个自我进化的多智能体框架来解决机器学习算法自动发现中的分支信息隔离、无记忆搜索和层级控制缺失问题。

首先，**渐进式MCGS**扩展了蒙特卡洛树搜索（MCTS），引入基于图的跨分支信息流和渐进探索调度。它将搜索空间组织为有向图，包含主边（E_T）和参考边（E_ref）。主边用于标准的选择和反向传播，而参考边连接不同分支或非相邻层级的节点，使知识跨分支组合转移。选择阶段采用熵启发的渐进调度，通过概率性软切换在UCT探索和精英引导利用之间动态平衡：早期偏向广泛探索（w(t)≈1），后期逐步降低w(t)到w_min，集中于高价值分支。扩展阶段包含四种图操作：主扩展（无参考）、分支内演化（参考同分支最近k个节点）、跨分支参考（参考所有分支中最好的N个节点）和多分支聚合（合并不同分支的洞见创建新根节点），由分支级和全局级停滞检测条件触发。

其次，**回顾性记忆**结合冷启动领域知识库（提供初始候选模型和用法指南）与动态全局记忆（在搜索中积累结构化经验）。通过混合检索（词汇匹配与FAISS语义搜索融合，经倒数秩融合排序）和阶段感知检索（规划阶段用初始文本计划查询成功/失败经验；调试阶段用错误信息查询历史修复方案），使智能体能复用有效策略并避免重复失败。

第三，**分层规划与自适应代码生成**将战略规划（决定“修改什么及其原因”）与代码实现（决定“如何修改”）解耦，并根据搜索状态在三种编码模式间自适应选择：基础模式（从零生成完整代码，用于初始草稿）、逐步模式（按模块生成，解决复杂多阶段管道）、差异模式（对现有代码进行针对性差异编辑，实现局部稳定优化）。

该框架通过一组专用智能体实现，使MLEvolve在MLE-Bench基准测试和数学算法优化任务中均取得了最先进的性能。

### Q4: 论文做了哪些实验？

论文在多个维度进行了实验评估。主要实验在MLE-Bench基准（包含75个Kaggle任务，分为低、中、高三个复杂度级别）上进行，对比了FM-Agent、MLE-STAR-Pro-1.5、MARS、MARS+、AIBuildAI等专有方法以及AIDE、R&D-Agent、ML-Master、AIRA-Dojo、Leeroo和ML-Master 2.0等开源方法。在12小时（标准预算24小时的一半）的预算下，MLEvolve取得了平均奖牌率65.3%（低80.3%/中64.0%/高46.7%）、金牌率34.7%、有效提交率100%和超中位数率76.0%的最佳综合性能。此外，在AlphaEvolve的15个数学优化任务上，MLEvolve在11个任务上超越了AlphaEvolve、AlphaEvolve-v2、SimpleTES、TTT-Discover和OpenEvolve等专用方法。消融实验在MLE-Bench Lite（22个任务）上进行，去除Progressive MCGS、Retrospective Memory或自适应代码生成均导致性能显著下降，其中去除Progressive MCGS导致奖牌率从81.82%降至68.18%。实验还验证了从探索到利用的软切换策略（有效分支数从4.8降至2.8），并展示了MLEvolve在不同LLM骨干（Gemini-3.1-Pro、GPT-5.5、DeepSeek-v4-Pro、Kimi-K2.6）和领域（图像、NLP、音频）上的有效性及更快的收敛速度。

### Q5: 有什么可以进一步探索的点？

MLEvolve在多个方面仍有改进空间。首先，尽管其Progressive MCGS和Retrospective Memory缓解了分支信息隔离和记忆缺失问题，但当前全局记忆的检索机制仍可能受限于任务相似性判断的准确性，未来可引入更细粒度的跨任务知识迁移或元学习策略。其次，论文实验仅基于Gemini-3.1-Pro-preview等少数LLM，且未深入探讨模型规模与搜索效率的权衡，未来可研究不同能力级别的LLM如何自适应分工。此外，当前12小时预算虽优于24小时基线，但复杂任务上的gold medal率仍有上升空间（如High任务仅46.7%），可尝试引入自动化的探索-利用阈值调节机制或分层奖励塑形。最后，数学优化任务上部分问题（如Kissing number）未达最优，说明框架在处理离散组合空间时可能仍需更专门的搜索算子。将进化计算中的种群多样性维护与LLM的语义指导结合，或是值得探索的方向。

### Q6: 总结一下论文的主要内容

本文提出MLEvolve，一个基于大语言模型的自我进化多智能体框架，用于解决端到端机器学习算法自动发现中现有方法的三大局限性：分支间信息隔离、无记忆搜索及缺乏层次化控制。该方法通过三个核心组件实现长时域优化：渐进式蒙特卡洛图搜索利用图结构的跨分支信息流和基于熵的渐进调度策略，自适应地从广泛探索转向集中利用；回顾记忆机制结合冷启动领域知识库和动态全局记忆，实现任务经验的自动积累与重用；层次化规划与自适应代码生成将策略设计与代码实现解耦，并根据搜索状态灵活选择重写、逐步或差异编辑模式。在MLE-Bench基准上，MLEvolve以12小时（标准时间一半）预算取得65.3%的平均奖牌率，达到最先进水平；在数学算法优化任务上也超越了AlphaEvolve等专用方法，验证了其跨领域泛化能力。该工作为自动化机器学习算法发现提供了可自我进化的系统化解决方案。
