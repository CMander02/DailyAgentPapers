---
title: "AgentFloor: How Far Up the tool use Ladder Can Small Open-Weight Models Go?"
authors:
  - "Ranit Karmakar"
  - "Jayita Chatterjee"
date: "2026-05-01"
arxiv_id: "2605.00334"
arxiv_url: "https://arxiv.org/abs/2605.00334"
pdf_url: "https://arxiv.org/pdf/2605.00334v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent Benchmark"
  - "Tool Use"
  - "Open-Weight Models"
  - "Planning"
  - "Routing"
  - "Multi-Step Coordination"
  - "Small Models"
relevance_score: 7.5
---

# AgentFloor: How Far Up the tool use Ladder Can Small Open-Weight Models Go?

## 原始摘要

Production agentic systems make many model calls per user request, and most of those calls are short, structured, and routine. This raises a practical routing question that existing evaluations do not directly answer: which parts of an agent workflow truly require large frontier intelligence, and which can be handled by smaller models? We introduce AgentFloor, a deterministic 30-task benchmark organized as a six-tier capability ladder, spanning instruction following, tool use, multi-step coordination, and long-horizon planning under persistent constraints. We evaluate 16 open-weight models, from 0.27B to 32B parameters, alongside GPT-5 across 16,542 scored runs. Our results reveal a clear boundary of model necessity. Small and mid-sized open-weight models are already sufficient for much of the short-horizon, structured tool use work that dominates real agent pipelines, and in aggregate, the strongest open-weight model matches GPT-5 on our benchmark while being substantially cheaper and faster to run. The gap appears most clearly on long-horizon planning tasks that require sustained coordination and reliable constraint tracking over many steps, where frontier models still hold an advantage, though neither side reaches strong reliability. We also find that this boundary is not explained by scale alone: some failures respond to targeted interventions, but the effects are model-specific rather than universal. These findings suggest a practical design principle for agentic systems: use smaller open-weight models for the broad base of routine actions, and reserve large frontier models for the narrower class of tasks that truly demand deeper planning and control. We release the benchmark, harness, sweep configurations, and full run corpus.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决生产环境中代理系统的一个实际部署问题：在用户请求需要多次模型调用的情况下，哪些任务环节必须依赖强大的前沿模型（如GPT-5），哪些可以由更小、更便宜的开源模型处理。当前评估存在不足：单轮函数调用基准（如BFCL）忽略了序列依赖成本；多步代理套件（如ToolBench）混杂了API漂移、环境干扰等因素；而规模化研究未能分解多步工具使用中的不同认知需求。因此，现有方法无法直接回答工具使用能力阶梯中路由决策的分界线。为此，论文提出**AgentFloor**基准，包含6个递进能力层级的30项确定性任务，在无环境噪声的抽象工具环境下评估16个开源模型（0.27B-32B）与GPT-5。核心发现是：开源模型在短程、结构化工具调用（主导实际管线）上已足够强大，最佳模型整体匹配GPT-5且成本更低；差距主要集中在需要持续协调和约束跟踪的长程规划任务，但双方均未达到高可靠性。这表明一个实用的设计原则——将常规工具调用委托给小型模型，仅对需要深度规划的狭窄任务保留前沿模型。

### Q2: 有哪些相关研究？

相关研究可从四个方面归纳。方法类基准方面，τ-bench 关注 pass^k 可靠性，API-Bank 按工具数量划分三级能力，AgentBoard 提供进展率和子技能面板，ComplexFuncBench 首次将 stop_early 列为失败类别。本文与它们的关键区别在于：AgentFloor 构建了六层确定性能力梯级（从指令遵循到长程规划），并附带了自举置信区间和结构化失败模式分类，而现有基准大多仅报告聚合分数。为规避真实 API 的漂移和污染问题（如 ToolBench 的 44.4% API 调用重启成功率、SWE-Bench Verified 中 59.4% 的测试用例缺陷），本文采用确定性抽象工具设计，与 StableToolBench、ToolEmu、REAL 等抽象基准一脉相承。评测分析方面，小模型能力调查和并发工具用研究（如 JSON 有效性、定性失败类型）虽相关，但未进行受控认知需求梯度的能力映射。本文量化验证了 "小模型足以支撑大部分 Agent 部署" 的观点。失败模式分类研究中，ToolScan/SpecTool、CriticTool、MAST 虽系统分类失败类型，但未与梯级能力图谱配对。成本质量路由方面，FrugalGPT、RouteLLM、Hybrid LLM、AutoMix 依赖难度预测进行模型路由，本文提供的梯级能力 - 成本静态图谱可直接作为路由系统的先验：A0/A/B 层可路由至 5B 以下开源模型且无精度损失，E 层的剩余差距对干预敏感而非受规模限制。

### Q3: 论文如何解决这个问题？

AgentFloor通过构建一个六层能力阶梯（A0到E）基准，系统性地评估不同规模模型在工具使用任务上的表现。核心方法是设计30个确定性任务，每个任务引入新的认知需求：从无工具指令跟随到长期约束规划，逐步增加复杂度。任务通过八个确定性工具（如search_records、submit_decision）在内存数据库上执行，消除了预训练污染的可能性。

整体框架包括三个主要模块：能力阶梯定义了任务层级和步数预算；工具表面提供统一的确定性工具集；推理协议通过Python运行器控制所有实验，使用原生工具调用接口而非文本提取。关键技术包括：使用二进制通过/失败评分（TCR），结合四类检查器（最终答案匹配、提交验证、轨迹检查、禁止行为检测）；对少数语义谓词使用GPT-5作为LLM裁判；通过Bootstrap置信区间和TOST等价性检验进行统计比较；建立严格的失败分类法（F1-F7）。

创新点在于：1）提出实用路由问题，识别哪些工作流部分真正需要大型前置模型；2）发现中小型开放权重模型已能胜任短时程结构化工具调用任务；3）揭示长期规划任务仍是前沿模型的主要优势区域；4）通过基于变体的配对测试和Holm-Bonferroni校正进行严格统计比较。该框架允许精确量化模型能力边界，为实际代理系统设计提供可操作的指导原则。

### Q4: 论文做了哪些实验？

论文在AgentFloor基准上进行了全面的实验，该基准包含30个确定性任务，分为6个能力层级（A0到E），覆盖指令遵循、工具使用、多步协调和长期规划。实验评估了16个参数量从0.27B到32B的开源模型，以及GPT-5，共计16,542次评分运行。主要使用任务完成率（TCR）作为指标，并采用预注册的TOST检验（±10pp边界）进行统计比较。

核心发现：最强的开源模型gemma4:26b在整体上以60% TCR与GPT-5（59.6%）持平（Δ=+0.4pp，90% CI [-4.0, +5.1]），但成本更低（Mac上每通过任务$0.0022 vs GPT-5的$0.0327，便宜约15倍；granite4:3b则便宜71倍）。在层级A0（无工具指令遵循）上，gemma4:26b以100% TCR显著优于GPT-5（80%）；在层级A（单工具使用）上两者等价。而在层级E（长期规划）上，GPT-5（10%）显著优于gemma4:26b（0%），但双方都远未达到可靠水平。层级B到C是最大的性能断层，所有开源模型在C、D、E上都无法达到60%的可靠性目标。

### Q5: 有什么可以进一步探索的点？

**可以进一步探索的点：**

该研究的局限性首先在于仅以GPT-5作为唯一的 frontier 模型锚点，未来需要引入Anthropic或Google的旗舰模型来交叉验证各层级的结论。其次，E层（长程规划）仅包含5个任务，样本量过小，需要设计更多样的任务来拓宽对长时域规划能力的评估。第三，在B/C/D层，难以在预注册容差下做出正式的等价性声明，因为每层仅5个任务无法提供足够统计效力。更关键的是，论文发现了几个反直觉现象：如Tier-D最高分来自4B参数模型而非26B模型，且同模型家族内14B版本全面弱于8B版本，这表明参数规模并非Agent能力的可靠预测因子。未来有几个值得深挖的方向：对更多模型进行显式提交分解干预测试以判断这是否是普遍存在的“潜在能力”；建立人类专家基线来为C/D/E层的实际表现提供参考；以及探究为什么某些模型的失败是“工具模板不兼容”而非“能力天花板”，从而设计更通用的工具调用协议。

### Q6: 总结一下论文的主要内容

AgentFloor是一个针对智能体系统工具使用能力的六层基准测试（共30个任务），涵盖指令跟随、工具调用、多步协调和长期规划。研究发现，0.27B-32B的开源模型在短期、结构化的工具操作任务上已足够，最强的开源模型在整体表现上可与GPT-5媲美，且更经济高效。但在需要持续性协调和约束跟踪的长期规划任务上，前沿模型仍具优势，但两者都未达到高可靠性。这一性能边界不仅由模型规模决定，还受特定干预措施影响。研究提出实用设计原则：常规任务使用小型开源模型，复杂规划任务保留大型前沿模型。
