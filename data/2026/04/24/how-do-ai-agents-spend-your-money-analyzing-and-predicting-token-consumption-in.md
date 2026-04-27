---
title: "How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks"
authors:
  - "Longju Bai"
  - "Zhemin Huang"
  - "Xingyao Wang"
  - "Jiao Sun"
  - "Rada Mihalcea"
  - "Erik Brynjolfsson"
  - "Alex Pentland"
  - "Jiaxin Pei"
date: "2026-04-24"
arxiv_id: "2604.22750"
arxiv_url: "https://arxiv.org/abs/2604.22750"
pdf_url: "https://arxiv.org/pdf/2604.22750v1"
categories:
  - "cs.CL"
  - "cs.CY"
  - "cs.HC"
  - "cs.SE"
tags:
  - "Agent经济性"
  - "Token消耗分析"
  - "Coding Agent"
  - "SWE-bench"
  - "成本预测"
  - "效率分析"
  - "Agent行为分析"
relevance_score: 7.5
---

# How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks

## 原始摘要

The wide adoption of AI agents in complex human workflows is driving rapid growth in LLM token consumption. When agents are deployed on tasks that require a significant amount of tokens, three questions naturally arise: (1) Where do AI agents spend the tokens? (2) Which models are more token-efficient? and (3) Can agents predict their token usage before task execution? In this paper, we present the first systematic study of token consumption patterns in agentic coding tasks. We analyze trajectories from eight frontier LLMs on SWE-bench Verified and evaluate models' ability to predict their own token costs before task execution. We find that: (1) agentic tasks are uniquely expensive, consuming 1000x more tokens than code reasoning and code chat, with input tokens rather than output tokens driving the overall cost; (2) token usage is highly variable and inherently stochastic: runs on the same task can differ by up to 30x in total tokens, and higher token usage does not translate into higher accuracy; instead, accuracy often peaks at intermediate cost and saturates at higher costs; (3) models vary substantially in token efficiency: on the same tasks, Kimi-K2 and Claude-Sonnet-4.5, on average, consume over 1.5 million more tokens than GPT-5; (4) task difficulty rated by human experts only weakly aligns with actual token costs, revealing a fundamental gap between human-perceived complexity and the computational effort agents actually expend; and (5) frontier models fail to accurately predict their own token usage (with weak-to-moderate correlations, up to 0.39) and systematically underestimate real token costs. Our study offers new insights into the economics of AI agents and can inspire future research in this direction.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决AI代理（AI Agent）在执行编码任务时的**代币（Token）消耗透明度和可预测性不足**的问题。研究背景是，随着AI代理被广泛应用于复杂工作流，其LLM代币消耗量激增，但当前的定价模式广受批评，主要缺点有二：一是缺乏透明度，用户直到任务结束才知道最终成本；二是存在“完成无保证”问题，即使任务失败，用户仍需为已消耗的代币付费。现有方法或研究主要关注代币在多智能体系统中的分布或推理模型的定价，缺乏对单智能体在复杂编码任务中代币消耗模式的系统性理解。

本文的核心问题是：**能否在任务执行前预测AI代理的代币消耗？** 为此，研究首先通过实证分析，揭示了代理编码任务中代币消耗的五个关键特征，包括其高昂的消耗量、极高的变异性（同一任务不同运行间代币消耗可能相差30倍）、消耗量与任务准确率之间的弱相关性（准确率往往在中等成本时达到峰值）、不同模型间代币效率的巨大差异，以及人类对任务难度的主观判断与模型实际计算开销之间的根本性脱节。基于这些发现，文章进一步形式化了“执行前代理代币消耗预测”这一新任务，并评估了多个前沿模型的表现，发现它们无法准确预测自身代币消耗（相关性最高仅0.39），且系统性地低估了实际成本。因此，该研究旨在为AI代理的经济学提供新见解，并推动更透明、更可预测的代理定价模型的发展。

### Q2: 有哪些相关研究？

根据论文内容，相关研究可以分为以下几类：

1. **AI Agent 基准测试与评估研究**：本文直接使用SWE-bench Verified作为评估基准，该基准包含真实世界的GitHub问题与代码仓库。与仅关注任务完成准确率的研究不同，本文首次系统地分析了agent在编程任务中的token消耗模式，揭示了准确率与token成本之间的非线性关系。

2. **大语言模型经济性研究**：现有工作主要关注模型推理成本，但本文首次对agentic任务的token消耗进行细粒度分析，发现agentic任务比代码推理和代码对话消耗多1000倍token，且输入token是主要成本驱动因素。

3. **模型效率比较研究**：本文评估了8个前沿LLM（如Claude系列、GPT系列、Kimi-K2等）的token效率，发现不同模型在相同任务上消耗差异巨大（如Kimi-K2和Claude-Sonnet-4.5比GPT-5平均多消耗150万token），这与单纯比较模型准确率的传统评估不同。

4. **任务难度预测研究**：本文发现人类专家评定的任务难度与实际token成本相关性很弱，揭示了人类感知复杂度与agent实际计算开销之间的根本差距。

5. **成本预测研究**：本文实验表明前沿模型无法准确预测自身token消耗（相关性最高仅0.39），且系统性低估实际成本，为agent成本预测研究提出了新挑战。

### Q3: 论文如何解决这个问题？

该论文通过系统性的实验和分析框架解决了AI智能体在编码任务中代币消耗的可预测性和效率问题。整体框架包括代币消耗模式分析、模型效率评估、成本动态跟踪和预测能力测试四大模块。

主要组件和方法包括：首先，在SWE-bench Verified基准上收集8个前沿LLM的完整轨迹数据，对比智能体编码、代码推理和代码聊天三类任务，发现智能体任务平均消耗的代币量是推理任务的3500倍，且输入代币是成本主导因素。其次，通过跨问题和跨运行的方差分析揭示代币消耗的高度不稳定性，同一问题不同运行间的代币消耗差异可达30倍，但高代币消耗并不对应高准确率，准确率在中等成本时达到峰值后饱和。进一步通过分析文件查看和编辑的重复行为，发现高成本失败运行中重复操作频率急剧增加，这表明低效搜索循环是成本失控的主因。

在模型效率评估中，论文构建了准确率-成本权衡曲线，发现GPT-5和GPT-5.2在低成本下实现高准确率，而Kimi-K2成本最高但准确率最低。通过共享成功/失败子集分析，证明代币效率是模型内在特征而非任务难度驱动。在成本动态分析中，将轨迹划分为设置、探索、修复、验证和收尾五个阶段，发现缓存读取代币在所有阶段占据主导，而成本尖峰由引入新内容的操作驱动。

在代币消耗预测方面，提出“自我预测”方法，让执行任务的智能体在运行前输出分阶段的输入代币、输出代币和总成本估计。结果显示所有模型都呈现弱到中等的相关（最高0.39），且系统性低估实际代币需求。创新点在于：首次系统量化智能体编码任务的代币消耗模式，揭示人类感知难度与代币成本的根本脱节，以及为代币消耗预测建立基准任务。

### Q4: 论文做了哪些实验？

论文通过系统实验分析了AI agent在编码任务中的token消耗模式。实验基于SWE-bench Verified数据集，包含500个真实GitHub问题，使用OpenHands框架，在8个前沿LLM（Claude Sonnet-3.7/4/4.5、GPT-5/5.2、Qwen3-Coder-480B、Kimi-K2、Gemini-3-Pro）上，每个任务独立运行4次，共收集16000条轨迹。

主要实验包括：1）比较agentic编码与代码推理、代码聊天任务的token消耗差异，发现agentic任务消耗高3500倍以上，且输入token驱动成本；2）分析token消耗方差，发现同一任务不同运行间差异可达30倍，最高成本任务比最低多消耗700万token；3）探究token消耗与准确率关系，发现准确率在中低成本时达到峰值后饱和，高成本运行中重复文件查看和编辑显著增加；4）对比专家预估难度与实际token消耗，Kendall τ_b仅为0.32，表明人类难度感知与agent计算资源消耗弱相关；5）评估模型token效率，GPT-5/5.2在低token消耗下达到高准确率，Kimi-K2消耗最多但准确率最低；6）预测token消耗实验显示，模型自我预测与实际消耗的Pearson相关系数最高仅0.39（Sonnet-4.5的输出token预测），且模型系统性低估实际token需求，预测开销通常低于执行成本的50%。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面：一是仅评估了8个前沿模型，样本量有限，且未覆盖不同架构和智能体设计；二是未深入分析不同任务类型（如代码生成、调试、重构）对token消耗模式的影响；三是当前模型对自身token消耗的预测能力很弱（相关性最高仅0.39），且系统性地低估实际成本。

未来可探索的方向包括：(1) 研究更广泛模型家族中的token消耗模式，特别是开源模型与闭源模型的对比；(2) 开发更细粒度的任务分类方法，分析不同类型编程子任务的token消耗特征；(3) 设计混合预测策略，结合模型自评与任务特征（如代码库规模、依赖复杂度）来提升成本预估准确性；(4) 探索预算感知的智能体系统设计，在执行过程中动态调整工具使用策略以控制token开销；(5) 研究token消耗与模型精度之间的帕累托最优关系，为不同成本约束场景选择合适模型提供理论依据。

### Q6: 总结一下论文的主要内容

这篇论文系统研究了AI智能体在编码任务中消耗令牌（token）的模式与预测问题。核心贡献在于首次对八种前沿大语言模型在SWE-bench Verified基准上的令牌消耗轨迹进行了全面分析。研究发现，智能体编码任务的令牌消耗极其高昂，比代码推理和代码聊天高出约1000倍，且成本主要由输入令牌而非输出令牌驱动。同时，令牌使用高度多变且具有随机性，同一任务的不同运行消耗差异可达30倍，更高消耗并不带来更高准确率，准确率往往在中等成本时达到峰值。此外，不同模型的令牌效率差异巨大，而人类专家对任务难度的评分与实际令牌成本关联微弱。更重要的是，前沿模型在任务执行前预测自身令牌消耗的能力很差（相关系数最高仅0.39），且系统性地低估了实际成本。这项研究揭示了智能体经济学的关键洞见，为构建更可持续、透明的AI智能体定价模型和未来研究奠定了基础。
