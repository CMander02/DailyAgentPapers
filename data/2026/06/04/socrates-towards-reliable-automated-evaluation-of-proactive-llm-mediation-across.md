---
title: "SoCRATES: Towards Reliable Automated Evaluation of Proactive LLM Mediation across Domains and Socio-cognitive Variations"
authors:
  - "Taewon Yun"
  - "Hyeonseong Park"
  - "Jeonghwan Choi"
  - "Hayoon Park"
  - "Yeeun Choi"
  - "Hwanjun Song"
date: "2026-06-04"
arxiv_id: "2606.05563"
arxiv_url: "https://arxiv.org/abs/2606.05563"
pdf_url: "https://arxiv.org/pdf/2606.05563v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "LLM Agent评估"
  - "多智能体调解"
  - "社会认知适应"
  - "众包测试"
  - "Agent基准测试"
relevance_score: 7.5
---

# SoCRATES: Towards Reliable Automated Evaluation of Proactive LLM Mediation across Domains and Socio-cognitive Variations

## 原始摘要

Evaluating LLM mediators remains challenging, as mediation unfolds as a real-time trajectory shaped by disputants' shifting emotions, intentions, and context. Existing testbeds rely on a few expert-authored domains, vary mainly strategic posture, and score every turn against every topic, introducing off-topic noise. We introduce SoCRATES, a benchmark for evaluating proactive LLM mediators in realistic, multi-domain testbeds. It constructs scenarios from real conflicts through an agentic pipeline across eight domains, probes five socio-cognitive adaptation axes (strategic posture, party composition, history length, emotional reactivity, and cultural identity), and scores each topic only on the turns that advance it via a topic-localized evaluator. The evaluator reaches 0.82 alignment with human experts, more than doubling a per-turn baseline. Benchmarking eight frontier LLMs, we find that even the strongest mediator closes only about a third of the unmediated consensus gap under diverse and realistic testbeds, with performance varying sharply by socio-cognitive axis, highlighting that progress lies in social adaptation to diverse conditions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有LLM调解器评估框架存在三大不足的问题：第一，场景覆盖依赖少量专家编写领域（如谈判、法律纠纷），无法扩展到真实冲突的多样性；第二，真实冲突中情绪、文化、历史等多维社会认知变量相互纠缠，现有测试床仅改变战略姿态，难以诊断调解器在具体维度上的失败原因；第三，现有评估方法（如ProMediate）对每轮对话的所有主题统一评分，混入了无关主题噪声，且无法捕捉调解质量在实时轨迹中的涌现特性。

为此，论文提出SoCRATES框架，核心解决三个问题：一是通过自动化智能体流程从真实网络冲突中跨8个领域自动构建场景，突破人工编写瓶颈；二是独立变化战略姿态、当事人构成、历史长度、情绪反应和文化身份5个社会认知轴，实现精细化诊断；三是提出主题定位评估器，仅对推进特定主题的对话轮次打分，将轨迹级评估与人类专家的一致性提升至0.82，较传统方法翻倍。最终目标是为LLM调解器提供一个可靠、可扩展、可诊断的自动化评估基准。

### Q2: 有哪些相关研究？

在相关工作方面，本文主要涉及两个类别。

**1. 社会冲突解决方法类**：包括将LLM作为争议方进行谈判建模，或作为第三方调解员分析完整对话记录。这些方法存在扩展瓶颈（如需招募大量人类参与者）或缺乏动态性。本文与它们的核心区别在于，SoCRATES通过智能体管道基于真实冲突构建多领域场景，并引入社会认知适应轴（如策略姿态、情感反应等），实现了更贴近真实调解过程的动态评估，而非仅分析静态对话或单一战略变化。

**2. 自动化对话评估方法类**：现有方法或依赖最终状态（如共识达成）进行粗粒度评估，或对每轮对话进行逐主题评分引入离主题噪声。本文提出的**话题本地化评估器**（Topic-Localized Evaluator）仅对推进特定主题的对话轮次进行评分，显著减少了无关噪声干扰，将评估与人类专家的一致性提升至0.82，远超基线方法。这解决了传统评估中噪声传播至后续状态的局限，提供了更可靠的轨迹级评估。

### Q3: 论文如何解决这个问题？

SoCRATES通过三个核心阶段构建了一个评估框架。首先，通过**智能体驱动的场景策展**自动化生成测试场景：一个Searcher智能体从八个真实冲突领域（交易、医疗、环境等）收集现实案例，Scenario Writer智能体将其结构化表示为包含背景、当事人、议题和偏好的形式化元组，并通过无调解模拟过滤掉那些能自行解决的冲突，最终保留40个高难度场景。

其次，通过**社会认知条件扩展**沿五个轴线探测调解能力：战略姿态（竞争/回避/迁就）、当事人构成（添加第三方）、历史长度（扩展背景）、情绪反应（冷静vs.反应型）和文化身份（韩国/美国/中国）。每个轴线独立应用于场景副本，避免能力混淆。

最后，采用**主题定位评估器**进行更可靠的评分。该评估器仅在对话中实际推进特定主题的轮次上打分，而不是对每一轮所有主题评分，从而消除离题噪声。与人类专家的一致性达到0.82皮尔逊相关系数，是逐轮基线方法的两倍以上。三个关键指标——干预时机、干预效果和共识增益——分别衡量调解何时介入、介入后共识的提升幅度以及最终相对于无调解基线所缩小的共识差距。

### Q4: 论文做了哪些实验？

论文进行了全面的实验评估。实验设置上，构建了包含8个领域（交易、医疗、环境、B2B、公共政策、国际、法律、组织内）的40个场景，每个场景沿5个社会认知轴（战略姿态、党派组成、历史长度、情绪反应、文化身份）扩展，共15个条件。每个场景运行600次模拟，总计4800次运行。对比方法包括8个前沿LLM中介：GPT-5.4-mini、Gemini-3.1-Flash-Lite、Gemma-4-26B、Qwen3-30B、Solar-Pro-3、Nemotron3-120B、DeepSeek-V3.2和Qwen3-235B。主要结果：顶级中介的共识增益仅达34.4%，远低于先前80-90%的解决率。关键数据指标包括：平均共识增益最高为34.4（Qwen3-235B），最低为15.7；干预及时性在不同模型间差异大，但最高者（Solar-Pro-3为86.3）并未转化为最高共识增益。主题定位评估器与人类专家达到0.82的皮尔逊相关性。战略姿态是最严峻的压力测试，竞争型和顺应型姿态导致共识增益下降18.9-64.1和13.8-66.8。情绪反应性导致均匀但持续的性能下降，而文化身份产生最小但最系统的偏移，模型在美国文化基准上表现稳健，但在东亚文化上较弱。

### Q5: 有什么可以进一步探索的点？

## 未来探索方向

**局限性**：SoCRATES的评估仍基于有限离散的socio-cognitive轴（5个），且仅测试了8个前沿LLM。在真实冲突中，情绪波动、文化交集等连续变量会相互叠加，产生远超当前测试床的复杂性。此外，topic-localized评估虽提升了相关性，但可能忽略跨主题谈判中的“隐性关联”策略。

**可探索方向**：1）将socio-cognitive扰动升级为**连续参数空间**（如文化、情绪强度从0到1平滑变化），研究模型适应能力的“临界点”。2）引入**动态用户模型**——让AI模拟人类“打圆场”时对历史误解的隐性修复（例如故意重提旧事来缓和矛盾），当前模型仅处理单轮即时反应。3）构建**多主体对抗压力测试**：若一方刻意采用文化特异性逻辑（如东亚“含糊其辞”vs北美“直接争辩”）干扰，模型是否仍能维持共识？4）将评估扩展至**跨语言场景**，因为当前英语语料库可能忽略语言对谈判策略的约束（如敬语体系影响冲突升级）。这些方向或能揭示模型在真实人类冲突管理中的脆弱性关键点。

### Q6: 总结一下论文的主要内容

SoCRATES提出了一个评估LLM调解员在真实多领域冲突中表现的综合基准。现有评估依赖少量专家撰写领域，仅改变策略姿态进行测试，并使用逐轮评分存在离题噪声。该工作通过三个步骤解决：自动化代理管道从八个领域真实冲突构建场景；沿五个社会认知轴（策略姿态、当事人组成、历史长度、情感反应性和文化身份）独立变化进行探测；采用主题定位评估器仅对推进该主题的轮次评分。评估器与人类专家达成0.82的一致性，是逐轮基准的两倍。对八个前沿LLM的测试表明，最强调解员在多样化测试下仅能弥合约三分之一的未调解共识差距，且表现随社会认知轴变化显著，强调调解进步在于适应多样化条件的社会认知能力。
