---
title: "Workflow-GYM: Towards Long-Horizon Evaluation of Computer-use Agentic tasks in Real-World Professional Fields"
authors:
  - "Liya Zhu"
  - "Jingzhe Ding"
  - "Jian Zhang"
  - "Jianbo Xue"
  - "Shihao Liang"
  - "Ge Zhang"
  - "Xiang Gao"
  - "Qingshui Gu"
  - "Mailun Gao"
  - "Huimin Che"
  - "Yan Zhao"
  - "Peiheng Zhou"
  - "Haojun Wang"
  - "Chaobo Xian"
  - "Lili Le"
  - "Chi Wu"
  - "Yiwei Liu"
  - "Shengda Long"
  - "Jiale Yang"
  - "Fangzhi Xu"
date: "2026-06-09"
arxiv_id: "2606.11042"
arxiv_url: "https://arxiv.org/abs/2606.11042"
pdf_url: "https://arxiv.org/pdf/2606.11042v1"
categories:
  - "cs.AI"
tags:
  - "GUI Agent"
  - "Long-horizon Task"
  - "Benchmark"
  - "Professional Software"
  - "Workflow Evaluation"
relevance_score: 8.5
---

# Workflow-GYM: Towards Long-Horizon Evaluation of Computer-use Agentic tasks in Real-World Professional Fields

## 原始摘要

Recent years have witnessed the rapid evolution of AI agents toward handling increasingly complex, real-world tasks. However, existing benchmarks rarely evaluate whether agents can operate graphical user interfaces to complete long-horizon, high-value professional workflows across diverse domains. Current GUI benchmarks still predominantly focus on general-purpose software, relatively simple applications, and short-horizon tasks, leaving it largely unknown whether modern agents can follow user instructions to autonomously operate domain-specific professional software and accomplish economically valuable work in an end-to-end manner. To bridge this gap, we introduce Workflow-GYM, a benchmark for long-horizon GUI tasks centered on professional domains and specialized software environments. Through extensive experiments on state-of-the-art models, we find that even the strongest models achieve only slightly above 30% success rates, highlighting that professional long-horizon GUI workflows remain highly challenging for current GUI agents. Further analysis reveals that current agents struggle to maintain long-horizon workflow consistency, frequently exhibiting workflow stage omission, error propagation, objective drift, and insufficient understanding of professional software environments. Our findings provide important insights into the limitations of current agent systems and suggest key directions for the next generation of GUI-agent research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI代理在真实世界专业领域执行长期、复杂图形用户界面任务时缺乏系统评估的问题。研究背景是，随着大语言模型和视觉语言模型的发展，AI代理正从处理短期、孤立任务，向能够自主执行长期、指令驱动的端到端工作流演进。然而，现有基准测试存在显著不足：它们主要关注通用软件、简单应用和短期任务，很少涉及需要专业知识和交互的专业软件；同时，针对长期推理和经济价值任务的评估多局限于纯文本环境（如代码生成、文档理解），忽略了图形界面的计算机操作场景。因此，核心问题是，目前缺乏一个能在真实工作环境中，系统评估AI代理通过图形界面自主完成专业领域、长期、高价值工作流的能力的基准。本文提出的Workflow-GYM正是为了填补这一空白，它通过设置完全配置的环境和专业软件，要求代理仅凭自然语言指令执行端到端任务，以衡量其在实际专业场景中的真实能力。

### Q2: 有哪些相关研究？

现有相关研究主要分为两类：**通用型GUI基准**和**领域专用型基准**。通用型如AmbiBench、GUI-360，聚焦日常移动APP操作或办公软件基础功能，任务周期短、场景简单。领域专用型如Science-Board，针对科研等专业软件，但任务仍为短期交互，缺乏端到端长流程覆盖。本文（Workflow-GYM）区别于这些工作，专门构建跨领域、专业软件的长时域工作流基准，任务涉及多阶段、高价值操作（如金融、工程软件）。

**方法类工作**方面，Mobile-Agent-v2提出多智能体协作框架处理长时交互，但限于移动环境。UI-TARS和Step-GUI分别通过强化学习与逐步奖励训练GUI专有模型，但本文不提出新方法，而是专注于评测——通过实验揭示现有模型在长流程一致性上的致命缺陷（如阶段遗漏、错误传播），为后续研究提供诊断性洞察。本文的关键贡献在于填补了“专业领域长时域GUI评测”这一空白，而非解决具体方法问题。

### Q3: 论文如何解决这个问题？

为解决当前GUI基准测试在专业领域、长周期任务上的评估空白，论文提出了**Workflow-GYM**，一个专注于真实世界专业工作流的基准。其核心方法围绕一个**多阶段数据构建流水线**和**两级环境架构**展开。

**整体框架**上，Workflow-GYM的构建分三步：1）**任务挖掘与筛选**：由跨领域专家基于其日常工作提出候选任务，并严格遵循真实性、领域特定性、复杂度（至少30个原子操作）和可验证性四大标准，筛选出超1000个候选任务。2）**环境构建与实例化**：采用分离式设计，首先构建58个**基础环境**（标准化的虚拟机镜像，包含预装的专业软件和配置），确保环境规模化和可复用；然后针对每个任务进行**轻量级实例化**，运行时注入输入数据、模板等工件，并将环境初始化为统一就绪状态（软件已打开，无任务操作），排除了登录等无关前置步骤。3）**任务生成与验证**：针对每个筛选后的工作流，生成包含任务指令、期望成果与评估标准、专家逐步操作指南的完整任务实例。最后经过环境验证、指令质量检查（专家+LLM评估）和端到端预实验三轮验证，确保任务无歧义且可由代理完成。

**关键技术**包括： - **两级环境策略**：分离了通用软件环境和任务特定初始化，提升了可扩展性和复现性，且真实虚拟机环境比容器或API更忠实还原GUI交互（如渲染、窗口管理）。 - **自动化评估方案**：对有明确产出物件的任务使用基于规则或LLM的验证；对无产出物件（如最终GUI状态）的任务，采用VLM自动评分，以二进制判断任务是否成功完成。 - **任务难度分级**：根据专家步骤数将任务分为Easy（30-44步）、Medium（45-60步）、Hard（61-110步）三个等级，共包含338个任务，覆盖6大领域。

**核心创新点**在于：Workflow-GYM首次系统地填补了专业领域长周期GUI任务的评估空白，其构建流程确保了任务源于真实高价值工作流（如经济性任务），且其环境设计和验证机制保证了评估的可靠性。通过实验发现，最强模型成功率仅略超30%，揭示了当前代理在专业长周期任务中的严重不足，如工作流阶段缺失、错误传播和意图漂移。

### Q4: 论文做了哪些实验？

该论文在 Workflow-GYM 基准上评估了6个前沿模型：GPT-5.4-xhigh、GPT-5.4-mini-xhigh、Gemini-3.1-Pro、Gemini-3-Flash、Kimi-k2.6 和 Seed-2.0-Lite。实验设置中，每个模型仅接收初始自然语言指令，通过400轮交互独立完成 GUI 操作，每个任务执行3次独立试验（trialnum=3），报告平均通过率（Avg Pass）和 Pass@3 指标。非规则评分项使用 Seed-1.8 作为评判模型。

主要结果：最佳模型 Gemini-3.1-pro 和 Kimi-k2.6 仅达到 30.67% 的 Avg Pass 和约 41% 的 Pass@3，远低于 OS-World 基准中 SOTA 模型超过 70% 的通过率。随着任务难度（Easy/Medium/Hard）增加，所有模型性能显著下降，如 Gemini-3.1-pro 从 39.28% 降至 21.33%。分领域表现显示，模型在结构化 GUI（如数据分析，Kimi-k2.6 达 45.24%）上表现较好，而在开放图形环境（如多媒体创作，平均 18%）上较弱。此外，模型与 Agent 框架高度耦合，非对齐配置会导致性能大幅下降。

### Q5: 有什么可以进一步探索的点？

基于对Workflow-GYM的分析，未来可以探索以下方向：首先，针对长程任务中的错误传播、阶段遗漏和目标漂移问题，可以开发更鲁棒的规划与状态追踪机制，例如引入层次化任务分解和中间状态验证。其次，当前智能体在专业软件知识方面存在严重不足，未来可构建领域知识图谱或利用合成数据微调基础模型，增强其对专业软件界面的理解。第三，重复动作循环是低效执行的关键瓶颈，可通过设计动态探索策略或引入惩罚机制来打破循环。更根本地，现有快照式架构无法支持连续视觉反馈，未来应探索支持实时视觉监控的交互范式，让智能体能像人类一样在执行过程中动态调整操作。此外，当前实验表明逐步指导能显著提升性能，未来可研究如何自动生成或检索此类指导，从而降低模型对高层规划的需求。总之，提升长程工作流的一致性和对专业环境的适应性是核心挑战。

### Q6: 总结一下论文的主要内容

Workflow-GYM是一个针对AI代理在真实专业领域执行长周期GUI工作流的基准测试。现有基准多聚焦于通用软件和短周期任务，无法评估代理完成高价值专业工作流的能力。为此，论文定义了“工作流”概念，并构建了涵盖多个专业领域的基准。方法上，每个任务在配置好专业软件的虚拟环境中进行，代理仅依据自然语言指令自主规划、交互并完成任务，通过最终状态自动验证成功与否。对多种最先进模型的实验表明，最强模型的成功率也仅略高于30%。研究揭示了当前代理的主要失败模式：工作流阶段遗漏、错误传播、目标漂移以及对专业软件理解不足。该工作凸显了当前GUI代理在长周期一致性上的巨大局限，为下一代代理研究指明了关键方向。
