---
title: "From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills"
authors:
  - "Zisu Huang"
  - "Jingwen Xu"
  - "Yifan Yang"
  - "Ziyang Gong"
  - "Qihao Yang"
  - "Muzhao Tian"
  - "Xiaohua Wang"
  - "Changze Lv"
  - "Xuemei Gao"
  - "Qi Dai"
  - "Bei Liu"
  - "Kai Qiu"
  - "Xue Yang"
  - "Dongdong Chen"
  - "Xiaoqing Zheng"
  - "Chong Luo"
date: "2026-05-22"
arxiv_id: "2605.23899"
arxiv_url: "https://arxiv.org/abs/2605.23899"
pdf_url: "https://arxiv.org/pdf/2605.23899v1"
categories:
  - "cs.AI"
tags:
  - "Agent技能提取与消费"
  - "多智能体评估"
  - "负迁移分析"
  - "元技能"
  - "LLM驱动的技能重用"
relevance_score: 8.5
---

# From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills

## 原始摘要

Language agents increasingly improve by reusing \emph{skills} -- structured procedural artifacts distilled from past experience. In particular, \emph{domain-level} and \emph{model-generated} skills are especially promising. They offer fast adaptation within a domain by encoding domain-specific recurring procedures, and they scale beyond labor-intensive hand-crafting. However, while extraction methods continue to proliferate, understanding remains limited, with no comprehensive study spanning the full skill lifecycle -- \textbf{experience generation}, \textbf{skill extraction}, and \textbf{skill consumption} -- to ask whether such skills actually work, when they work, and what makes them succeed or fail. To close this gap, we build a utility-grounded evaluation framework that provides systematic experimental results across extractors and target agents, covering five diverse agentic task domains. We find that model-generated skills are beneficial on average but exhibit non-trivial negative transfer, and that neither extractors nor targets behave uniformly. A model can be a strong extractor yet a weak consumer, or vice versa, with skill utility independent of model scale or baseline task strength. To explain these patterns, we then dissect each lifecycle stage in depth, analyzing how experience composition shapes skill quality, what properties characterize useful skills, and how the same skill transfers across different consumers. Finally, we translate these findings into a concrete \emph{meta-skill} that guides skill extraction toward the features tied to actual utility, which consistently improves skill quality across domains and substantially reduces negative transfer.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决语言智能体领域一个关键但尚未被系统研究的问题：由模型自动生成的、领域级别的技能（skills）是否真正有效、何时有效，以及影响其成败的根本因素是什么。随着语言智能体的发展，通过重用从过往经验中提取的结构化程序性知识（即技能）成为提升性能的重要途径。虽然手动编写的技能在实践中已证明其价值，但成本高昂且无法规模化，因此涌现出大量自动生成技能的方法（如从执行日志中蒸馏）。然而，现有研究存在明显不足：要么只关注技能消费阶段（如评估使用技能后的性能提升），忽略了技能的提取过程；要么只研究特定的、受限于可执行函数组合的技能。整个领域缺乏一个横跨“经验生成”、“技能提取”和“技能消费”三大生命周期的系统性研究。因此，本文构建了一个基于效用（utility-grounded）的评估框架，通过多样化的任务域和不同的提取器/目标智能体组合进行实验，核心要解决三个问题：模型生成技能的平均收益如何？其效用波动的根源是什么？以及如何将研究发现转化为切实改进技能提取质量的元技能（meta-skill），从而减少出现负迁移（negative transfer）的情况，推动该领域从直觉驱动走向原则指导。

### Q2: 有哪些相关研究？

相关研究主要分为三类。**方法类**工作聚焦于从智能体轨迹自动提取可复用知识：Prompt蒸馏方法如Trace2Skill通过并行子智能体和层次化整合，AutoRefine归纳双形态经验模式，PRAXIS构建状态索引程序记忆，MemP形式化程序记忆的构建-检索-更新循环；优化与RL方法如ProcMem采用非参数PPO，CoEvoSkills使用协同进化验证；还有如EvolveR研究自进化生命周期智能体。**评测类**工作关注技能效用：SkillsBench、SWE-Skills-Bench测试技能对下游性能的提升，AgentSkillOS研究生态级技能管理，SkillFlow开发大规模技能检索，SkillCraft研究技能组合与积累但限于可执行函数。本文与这些工作的核心区别在于：现有方法各自在独立设定下验证有效性，缺乏对经验生成、技能提取、技能消费全生命周期的系统性理解。本文构建了跨提取器、目标模型和领域的统一评估框架，并通过逐阶段分析揭示了模型即可是强提取器但弱消费者的非对称性、负迁移现象以及技能效用与模型规模解耦等关键发现，最终提出元技能以指导提取与效用关联的特征。

### Q3: 论文如何解决这个问题？

论文通过构建一个完整的技能生命周期评估框架（经验生成→技能提取→技能消费），系统研究模型生成技能的实际效用。核心方法包括三个关键阶段：首先，目标模型（target model）在特定领域执行训练集任务，生成包含成功和失败轨迹的经验池；其次，提取器模型（extractor model）对这些经验进行结构化蒸馏，产生可复用的技能集；最后，同样的目标模型在测试集上使用这些技能执行任务，通过性能增益（δ）量化技能的实际效用。

架构设计上采用了两阶段提取流程：第一阶段是单轨迹分析，提取器独立处理每条轨迹，从中提取最多K个成功/失败模式；第二阶段是层次化整合，通过树状结构以组大小G逐步合并模式集，最终通过结构化工具调用转换为标准化的技能表示（包含名称、描述、Markdown过程指令等字段）。关键技术包括保持提取框架的最小化设计（无领域特定启发式规则），以及通过“提取功效”（EE）和“目标可演化性”（TE）两个互补指标分别衡量提取器和目标模型的表现。

创新点有三：一是构建了覆盖完整生命周期的评估框架，揭示模型生成技能存在非平凡负迁移；二是发现技能效用与模型规模或基线性能无关，强提取器可能是弱消费者，反之亦然；三是基于实证发现提出了“元技能”引导策略，提取与真实效用相关的特征，持续改善技能质量并显著减少负迁移。这种系统性的研究方法为理解语言智能体技能学习提供了重要洞见。

### Q4: 论文做了哪些实验？

该论文在五个多样化领域（ALFWorld具身任务、SpreadsheetBench电子表格操作、SWE-bench-Verified软件工程、SEAL-0网络搜索、BFCL-v4工具调用）进行了大规模实验。实验使用六个目标模型（GPT-5.4、GPT-5.4-mini、Gemini-3.1-Pro、Gemini-3.1-Flash-Lite、Qwen3.5-35B、Qwen3.5-9B）和五个提取器模型（排除Qwen3.5-9B）进行配对评估。每个域的任务按1:1分为经验生成集和测试集，提取器将目标经验蒸馏为单一技能，在测试集上测量性能增量（δ）。主要结果包括：（1）模型生成技能总体上有效，75%的条目δ>0，平均性能提升约2-5个百分点，但25%出现负迁移，其中ALFWorld最脆弱（47%负迁移）；（2）提取器效能不随模型规模或任务基线强度单调变化，例如SpreadsheetBench上Gemini-3.1-Flash-Lite的提取效能最高，而GPT-5.4最低；（3）目标可演化性在同一域内存在显著不对称，如ALFWorld上GPT-5.4的TE为+4.93，而Gemini-3.1-Flash-Lite为-1.59。

### Q5: 有什么可以进一步探索的点？

论文的核心限制在于模型生成技能的下游效用高度依赖抽取和消费的匹配性，且存在显著的负迁移现象。未来探索应聚焦于：**1. 自动化经验组成优化**：当前最优成功/失败比例是领域相关的（如ALFWorld中失败案例更有信息量），可探索基于强化学习或贝叶斯优化的自适应采样策略，动态调整经验池构成以最大化技能效用。**2. 去偏技能评估机制**：LLM作为评判者无法有效区分技能质量（准确率仅46.4%甚至反相关），需开发基于可执行仿真或图结构匹配的客观评估指标，避免表面形式误导。**3. 跨模型消费能力建模**：相同技能对不同目标模型效果差异极大（如强池技能对Qwen3.5-35B增益+9.5但对Gem-3.1-Pro仅+1.8），可研究消费能力与模型架构、预训练数据分布的关系，构建可预测技能-模型匹配度的元模型。**4. 负面迁移预防**：通过因果干预分析技能中导致特定模型退化的具体指令模式，设计可阻断有害知识注入的“安全技能包装器”。这些方向将推动技能系统从静态管道向自适应生态演化。

### Q6: 总结一下论文的主要内容

该论文针对语言智能体中模型生成的领域级技能，首次系统性地研究了其完整生命周期：经验生成、技能提取与技能消费。当前研究多聚焦于单一阶段，缺乏对技能实际效用及其成败原因的全面评估。为此，作者构建了一个以效用为基准的评估框架，在五个多样化的任务领域上进行了实验。研究发现，模型生成的技能平均有益，但存在显著的负迁移现象，且技能提取器与消费代理的表现并不一致，技能效用与模型规模或基线任务性能无关。为了解释这些现象，论文深入分析了每个阶段，揭示了经验构成如何影响技能质量、有用技能的特征，以及技能在不同代理间的迁移规律。最后，作者将研究发现转化为具体的“元技能”指导，通过对齐实际效用特征来改进技能提取过程，一致性地提升了技能质量并大幅减少了负迁移。这项工作填补了技能应用领域的系统性理解空白，为构建更可靠、有效的智能体技能库提供了重要指导。
