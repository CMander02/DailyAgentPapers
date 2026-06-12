---
title: "DailyReport: An Open-ended Benchmark for Evaluating Search Agents on Daily Search Tasks"
authors:
  - "Jingxuan Han"
  - "Wei Liu"
  - "Mingyang Zhu"
  - "Youpeng Wang"
  - "Ziwen Wang"
  - "Lin Qiu"
  - "Xuezhi Cao"
  - "Xunliang Cai"
  - "Zheren Fu"
  - "Licheng Zhang"
  - "Zhendong Mao"
date: "2026-06-11"
arxiv_id: "2606.12871"
arxiv_url: "https://arxiv.org/abs/2606.12871"
pdf_url: "https://arxiv.org/pdf/2606.12871v1"
github_url: "https://github.com/AGI-Eval-Official/DailyReport"
categories:
  - "cs.AI"
tags:
  - "搜索Agent"
  - "开放基准评估"
  - "LLM驱动Agent"
  - "信息检索"
  - "用户模拟评估"
relevance_score: 8.5
---

# DailyReport: An Open-ended Benchmark for Evaluating Search Agents on Daily Search Tasks

## 原始摘要

Search Agents (SAs) typically leverage large language models (LLMs) to support complex information-seeking tasks by autonomously exploring web sources and synthesizing information into comprehensive responses. For SAs evaluation, prior benchmarks mainly focus on specialized tasks that are unlikely to arise in real-world user scenarios. Moreover, their reliance on coarse task-level rubrics often limits evaluation interpretability. To bridge this gap, we introduce DailyReport, an open-ended benchmark to evaluate SA capabilities on daily search tasks. It contains 150 open-ended tasks with 3,546 associated rubrics, capturing widely discussed and timely information demands of real-world users. Each task is decomposed into subtasks and evaluated with cascade rubrics across disentangled dimensions. Through cascade performance attribution and user-centric aggregation, we derive highly interpretable scores for each dimension, along with a user preference score. Our results on 17 agentic systems show that current systems still fall short of users' expectations. To facilitate future research, our dataset and code are made publicly available at https://github.com/AGI-Eval-Official/DailyReport.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有搜索代理（Search Agents, SAs）评估基准存在的两个核心问题：**任务构建不贴近真实用户需求**以及**评估方式缺乏可解释性**。

**研究背景**：随着大语言模型的发展，搜索代理能够自主进行复杂的信息检索与整合。为了评估其能力，业界提出了多种基准。

**现有方法的不足**：
1.  **任务不真实**：现有基准大多依赖领域专家构建高度专业化或过度处理的任务，这些任务通常涉及特定领域的学术或技术问题，很少出现在真实用户的日常搜索场景中。此外，这类静态设计易受数据污染，且无法捕捉用户随现实世界变化的信息需求。
2.  **评估不精细**：现有评估通常采用粗粒度的任务级评分标准（rubric），并对各维度得分进行简单线性加权。这导致了两个缺陷：一是评估的可解释性差，无法精确诊断模型在指令遵循、事实性和合理性等不同方面的具体表现；二是未能从用户视角出发，忽略了不同任务组件在用户心中的优先级差异（例如，先要正确识别大学，才能分析其强弱项）。

**论文要解决的核心问题**：本文提出了**DailyReport**基准，旨在解决上述问题。通过构建**150个源自社交平台趋势和用户评论的开放式日常搜索任务**（包含3546条细粒度评分标准），并设计**用户导向的级联评估流水线**——该流水线将任务分解为子任务，沿指令遵循、事实性和合理性三个维度进行级联评分，最后结合子任务重要性进行聚合，从而实现对搜索代理性能的**高可解释性评估**，并显式量化其对用户偏好的满足程度。

### Q2: 有哪些相关研究？

本文的相关工作主要分为两大类。第一类是面向固定答案的搜索Agent评测，如**BrowseComp**和**WideSearch**，它们侧重于信息检索和多步推理能力。DailyReport与此不同，聚焦于开放式的日常搜索任务，而非这些基准中的专业化或难在实际中出现的任务。

第二类是生成研究报告的评测，包括**DeepResearch Bench**、**DeepResearch Bench II**、**LiveResearchBench**和**ResearchRubrics**。这些工作通过评估报告质量或检索能力来评测Agent。其中，**LiveResearchBench**尝试贴近日常用户需求，但主要局限于美国场景，且区域覆盖有限。DailyReport的核心区别在于：(1) 采用与真实用户需求对齐的、动态更新的日常搜索任务；(2) 引入级联评分（Cascade Rubrics）和解耦的评估维度，实现了可解释的性能归因；(3) 首次量化了用户偏好，从而弥补了现有工作在评测可解释性和用户中心性上的不足。DailyReport系统地分析了当前17个Agent系统（包括LangChain Deep Researcher、Gemini Deep Research等）的能力边界。

### Q3: 论文如何解决这个问题？

DailyReport通过构建一个开放式的基准测试框架来解决当前搜索agent评估中任务偏离现实场景且评估可解释性不足的问题。核心方法包括：首先，从Facebook、微博等平台收集真实热门话题，由人类专家提炼出150个覆盖10大领域和35个细分类别的开放式日常搜索任务，并配套生成3546条评估准则。这些任务分为100个检索中心型和50个分析中心型，确保真实性和时效性。架构设计上采用分层分解策略：每个任务被分解为原子性子任务，每个子任务再生成沿三个正交维度（指令遵循、事实性、合理性）的级联准则。关键技术在于用户中心级联评估体系：指令遵循维度直接计算平均分；事实性维度仅在指令满足时进行级联归因评估，通过提取事实性声明并用网络搜索验证；合理性维度也依赖指令满足度，但侧重逻辑连贯性判断。最终通过用户偏好聚合算法，根据子任务重要性（P0关键、P1重要、P2次要）和整体表现（客观分o_k）计算1-4分的用户偏好分数。该框架的创新点包括：真实场景驱动的任务构建、无需预定义答案的开放式评估、以及通过级联归因实现各维度的可解释性评分。实验结果显示，即使是强系统（如GPT 5.4）的用户偏好分最高也仅2.89，表明现有agent与用户预期仍有显著差距。

### Q4: 论文做了哪些实验？

论文对17个agentic系统进行了全面评估，分为三组：原生DRA、搜索增强LLM和带Claude Code的LLM。实验使用DailyReport基准，包含150个开放任务和3546个关联规则，将任务分解为子任务并使用级联规则在独立维度上评估。主要结果：搜索增强LLM表现最佳（GPT-search用户偏好评分2.90），带Claude Code的次之，原生DRA最差。在四大维度中，InstFollow（指令遵循）得分最高（GPT-search 98.3%），Factuality（事实性）最低（仅83.6%），Rationality（合理性）为93.4%。所有系统在UserPref（用户偏好）上均低于可接受水平3。任务类型效应显示，分析型任务在InstFollow和Rationality上略高，但Factuality较低。搜索轨迹分析表明搜索工具调用频率与整体性能强相关。鲁棒性分析显示三次运行标准差低，评价稳定。元评估验证了评估器准确性（Gemini-3-flash准确率96.5%），UserPref与真实用户评分高度一致（加权Cohen's Kappa=0.859）。领域分析显示，在政治法律等结构化信息领域表现更好，体育娱乐等动态领域较差。

### Q5: 有什么可以进一步探索的点？

论文的主要局限在于任务规模和领域的限制，仅覆盖150个日常搜索任务，且侧重于英文用户需求，未充分探索多语言、多文化场景。未来研究方向可包括：1）扩展任务库至更大规模、更多样化的领域（如医疗、金融），并纳入多语言用户查询；2）改进级联评估的粒度，引入更细粒度的时间敏感性评估（如实时信息更新能力）；3）当前系统依赖单一LLM作为核心，可探索混合架构（如多专家协作）或检索增强生成与工具调用的协同优化；4）用户偏好聚合目前基于简单加权，可引入个性化建模或对抗性测试来反映真实用户差异化需求；5）开发自适应任务分解策略，使智能体能动态调整子任务顺序，而非固定级联。这些方向将推动搜索智能体从实验室评估迈向真实场景部署。

### Q6: 总结一下论文的主要内容

DailyReport提出一个开放式基准，用于评估搜索智能体在日常搜索任务中的表现。现有基准大多聚焦于用户真实场景中不常见的专业任务，且依赖粗粒度的任务级评分标准，导致评估可解释性有限。该论文定义了150个开放式日常搜索任务，包含3546条关联评分标准，捕捉真实用户广泛讨论的时效性信息需求。方法上，将每个任务分解为子任务，并设计沿解耦维度的级联评分标准。通过级联性能归因和以用户为中心的聚合，生成每个维度的可解释评分以及用户偏好评分。对17个智能体系统的实证评估表明，当前系统仍未能达到用户期望。该工作为搜索智能体的评估提供了更真实、可解释的基准，有助于推动未来研究。
