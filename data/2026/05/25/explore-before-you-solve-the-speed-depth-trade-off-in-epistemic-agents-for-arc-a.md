---
title: "Explore Before You Solve: The Speed--Depth Trade-off in Epistemic Agents for ARC-AGI-3"
authors:
  - "Liew Keong Han"
date: "2026-05-25"
arxiv_id: "2605.25931"
arxiv_url: "https://arxiv.org/abs/2605.25931"
pdf_url: "https://arxiv.org/pdf/2605.25931v1"
github_url: "https://github.com/farmountain/aera-arc3-paper"
categories:
  - "cs.AI"
tags:
  - "ARC-AGI"
  - "epistemic agent"
  - "exploration"
  - "benchmark analysis"
  - "speed-depth trade-off"
  - "open-source agent"
  - "adaptive reasoning"
relevance_score: 8.0
---

# Explore Before You Solve: The Speed--Depth Trade-off in Epistemic Agents for ARC-AGI-3

## 原始摘要

We systematically investigate all 25 public ARC-AGI-3 games and find that every one is reachable through non-intelligent strategies: 10 in a single blind step, 5 after one probing action, 1 via repeated ACTION1 presses, 1 via diverse exploration, and 8 via single repeated actions with sufficient budget (50-200 steps). A library-level null-coordinate vulnerability additionally bypasses 18 games in 1 step. This benchmark critique implies the public evaluation set cannot discriminate intelligent exploration from trivial heuristics - the private 55-game evaluation is the only genuine intelligence test. Against this backdrop, we present AERA (Adaptive Epistemic Reasoning Agent), a three-phase (EXPLORE / VERIFY / PLAN) agent achieving RHAE=0.2116 (4/25 solved) on these 25 games with Qwen2.5-0.5B, while random and no-explore baselines score 0.0000. We formalise AERA through a Speed--Depth trade-off framework: under a convexity assumption (proved for a class of environments in the Appendix), RHAE's quadratic form emerges as a second-order penalty for deviating from the Pareto frontier between action efficiency and information gain. Contributions: (i) a benchmark validity analysis showing that current interactive reasoning benchmarks fail to measure the exploration they claim to require, and (ii) the EXPLORE-before-PLAN framework and model-capability x exploration interaction. The linked code track entry achieves RHAE=0.30 on the full 55-game private evaluation. Code: CC0.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前AI系统在未知交互环境中的“探索-求解”脱节问题，尤其聚焦于ARC-AGI-3基准测试。研究背景是，人类面对陌生谜题时会先探索、形成假设再求解，但现有AI系统（如ReAct、CoT、ToT）要么假设问题已知、要么没有显式建模信念不确定性，在隐藏规则环境中表现极差。现有方法的不足体现在：1）大量系统在初始观察o0后直接执行一次性规划，忽略了信息收集的必要性，导致策略确定性失效；2）RHAE指标对无效动作施加二次惩罚，高估了现有模型的探索效率；3）作者系统性分析发现，所有25个公开ARC-AGI-3游戏都能通过非智能策略（如单步盲动、重复试探等）轻松通过，说明公开评估集无法区分真正智能的探索与简单启发式。因此，本文要解决的核心问题是：设计一种显式遵循“先探索、后求解”原则的智能体，使其能在隐藏规则交互环境中通过自适应探索降低信念熵，从而获得非零RHAE分数，并揭示当前基准测试在测量探索能力上的根本性缺陷。

### Q2: 有哪些相关研究？

根据论文提供的相关内容，相关研究主要可分为三类：

1. **ARC-AGI 基准类研究**：Chollet 提出 ARC 作为流体智能的度量。ARC-AGI-1 和 ARC-AGI-2 是静态的，而 ARC-AGI-3 引入了交互性。本文首次正式解释了为何 RHAE 对低效进行二次惩罚，这是对现有基准分析的重要补充。

2. **2025 年 ARC Prize 获奖方法类研究**：包括 TRM（第一名，7M 参数递归模型，ARC-AGI-1 约 45%，ARC-AGI-2 约 8%）、SOAR（第二名，自生成搜索轨迹微调，ARC-AGI-1 最高约 52%）、CompressARC（第三名，MDL 单谜题代码高尔夫，ARC-AGI-1 约 20-34%）。这些方法均针对静态 ARC-AGI-1/2，不涉及交互环境或 RHAE。本文指出 TRM 的递归精化在结构上类似于 AERA 的 VERIFY 阶段，但 AERA 在 TRM 式规划前增加了世界模型获取阶段，两者互补。

3. **主动学习类研究**：MacKay 提出了基于信息的主动学习框架。本文的 AERA 代理基于探索-规划范式，与主动学习的核心思想有理论关联，但更侧重于在有限交互预算下平衡动作速度与信息深度。

### Q3: 论文如何解决这个问题？

论文通过提出AERA（自适应认知推理智能体）框架来解决基准测试无效性和探索-规划权衡问题。整体框架包含三个核心阶段：EXPLORE（深度探索）、VERIFY（验证）和PLAN（规划执行）。

**核心方法**围绕“先探索后规划”原则设计。在EXPLORE阶段，采用基于熵减的动作选择策略，利用大语言模型输出结构化的HYPOTHESIS/UNCERTAIN/NEXT_ACTION/REASON块，通过uncertain字段长度作为熵代理指标，动态调整探索预算（B_max = max(5, min(30, 0.4H_E))），并偏好使用撤销动作保持状态。

**架构设计**包含三个主要模块：
1. **探索模块**：通过LLM在环境中进行信息增益最大化的动作，持续更新假设空间并缩减不确定性；
2. **验证模块**：执行1-3个针对性反驳动作验证最大后验假设，若假设被证伪则重新进入探索阶段；
3. **规划执行模块**：基于已验证假设生成PLAN/CONFIDENCE/FALLBACK，当观测与预期不符时回退至探索阶段。

**关键技术创新**包括：
- 提出速度-深度帕累托前沿理论框架，证明在凸性假设下RHAE损失函数呈现二阶惩罚特性，偏离前沿的策略会承受二次方代价；
- 引入episodic memory机制记录最近10步轨迹并检测冗余探测；
- 在竞赛实现中将探索阶段替换为广度优先搜索预求解，通过离线缓存状态达到等价效果（公共排行榜RHAE=0.30）。

该框架通过理论化探索-规划权衡并实现自适应切换，在25个公开游戏中以Qwen2.5-0.5B取得RHAE=0.2116，验证了探索阶段对智能推理性能的关键作用。

### Q4: 论文做了哪些实验？

论文在公共ARC-AGI-3数据集上进行了多组实验。实验设置使用Kaggle P100 GPU（16GB显存），模型运行在CPU FP32模式下。主要采用Qwen2.5-0.5B-Instruct和Qwen2.5-1.5B-Instruct模型，在5个公共环境（sb26, ft09, cd82, tu93, r11l）以及全部25个公共游戏上进行了评测。

核心对比方法包括：随机基线（Random，200步上限）、无探索基线（B1，无探索阶段直接进入PLAN）、AERA自适应探索与规划、固定预算探索（b=1,3,5），以及ReAct基线。主要结果：在5游戏实验中，随机和无探索基线RHAE均为0.0000，AERA自适应（EXP-002）达到0.2645（解决1/5游戏），AERA b=1（EXP-003）达到0.5290（解决2/5游戏）。在25个公共游戏上，随机和无探索基线仍为0.0000，AERA b=1和b=5均达到0.2116（解决4/25游戏，包括VC33、FT09、LP85、S5I5）。8次独立运行的均值为0.164±0.059，FT09在100%运行中被解决。ReAct基线达到0.388（8/25），但10/25游戏产生无效动作。预算消融实验显示非单调性，最优预算依赖具体环境。深度受限穷举搜索发现4个游戏可通过单个ACTION6动作解决，但LLM的token分布偏向ACTION1导致错过胜利条件。

### Q5: 有什么可以进一步探索的点？

论文揭示了当前ARC-AGI-3基准的严重局限性：25个公开游戏均可被非智能策略攻克，说明它无法有效区分智能探索与简单启发式。未来可探索的方向包括：1）设计更严格的基准测试，引入需要真正因果推理和结构化表征的任务，避免被盲探或重复动作破解，例如采用动态环境或随机化网格布局；2）改进AERA的探索-规划框架，目前RHAE的二次型惩罚基于凸性假设，但非单调性实证表明该假设可能不成立，可尝试将探索预算动态调整为信息增益的函数，或引入贝叶斯优化实现自适应步长；3）从模型容量角度，0.5B参数模型表现有限，可研究更大规模模型（如7B或更大）是否能在相同框架下显著提升求解率，以及是否需要在预训练中注入显式的因果推理和试探性规划先验。

### Q6: 总结一下论文的主要内容

该论文系统性地揭示了ARC-AGI-3基准测试的关键缺陷：所有25个公开游戏均可通过非智能策略（如盲目试探、重复动作）解决，暴露出公开评估集无法区分智能探索与简单启发式方法。核心贡献包括：(1)基准有效性分析，证明当前交互式推理基准未能测量其声称所需的探索能力；(2)提出AERA（自适应认知推理智能体），采用“探索-验证-规划”三阶段架构，在Qwen2.5-0.5B上对25个游戏取得RHAE=0.2116（4/25解决），而随机和无探索基线为0.0000；(3)形式化“速度-深度”权衡框架，将RHAE的二次形式解释为偏离帕累托前沿（动作效率与信息增益权衡）的二阶惩罚。主要结论是：人类与AI在ARC-AGI-3上的巨大差距并非推理能力缺陷，而是认知纪律（探索行为）的缺失，私人55游戏评估才是真正的智能测试。
