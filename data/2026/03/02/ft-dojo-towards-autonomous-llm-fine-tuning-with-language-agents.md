---
title: "FT-Dojo: Towards Autonomous LLM Fine-Tuning with Language Agents"
authors:
  - "Qizheng Li"
  - "Yifei Zhang"
  - "Xiao Yang"
  - "Xu Yang"
  - "Zhuo Wang"
date: "2026-03-02"
arxiv_id: "2603.01712"
arxiv_url: "https://arxiv.org/abs/2603.01712"
pdf_url: "https://arxiv.org/pdf/2603.01712v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Tool Use & API Interaction"
  - "Learning & Optimization"
relevance_score: 8.0
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Learning & Optimization"
  domain: "General Purpose"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "FT-Agent"
  primary_benchmark: "FT-Dojo"
---

# FT-Dojo: Towards Autonomous LLM Fine-Tuning with Language Agents

## 原始摘要

Fine-tuning large language models for vertical domains remains a labor-intensive and expensive process, requiring domain experts to curate data, configure training, and iteratively diagnose model behavior. Despite growing interest in autonomous machine learning, no prior work has tackled end-to-end LLM fine-tuning with agents. Can LLM-based agents automate this complete process? We frame this as a substantially open problem: agents must navigate an open-ended search space spanning data curation from diverse data sources, processing with complex tools, building a training pipeline, and iteratively refining their approach based on evaluation outcomes in rapidly growing logs--an overall scenario far more intricate than existing benchmarks. To study this question, we introduce FT-Dojo, an interactive environment comprising 13 tasks across 5 domains. We further develop FT-Agent, an autonomous system that mirrors human experts by leveraging evaluation-driven feedback to iteratively diagnose failures and refine fine-tuning strategies. Experiments on FT-Dojo demonstrate that purpose-built fine-tuning agents significantly outperform general-purpose alternatives, with FT-Agent achieving the best performance on 10 out of 13 tasks across all five domains. Ablations show that the approach generalizes effectively to 3B models, with additional insights on data scaling trade-offs and backbone sensitivity. Case analyses reveal that agents can recover from failures through cumulative learning from historical experience, while also exposing fundamental limitations in causal reasoning--highlighting both the promise and current boundaries of autonomous LLM fine-tuning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）在垂直领域微调过程中高度依赖人工、成本高昂且流程复杂的问题。研究背景是，尽管LLM在通用任务上表现出色，但在化学、法律、金融等专业领域部署时，通常需要针对性的微调以满足可靠性和性能标准。然而，现有的微调过程是劳动密集型的，需要领域专家和机器学习工程师协作进行需求解读、非结构化数据整理、训练管道配置和模型检查点评估，且每个新领域都需要重新设计流程。

现有方法的不足主要体现在两个方面：首先，尽管在自动化机器学习（AutoML）领域已有进展，出现了如MLE-Bench等评估智能体在数据预处理、特征工程等传统机器学习工程（MLE）任务上能力的基准，但尚无工作研究如何用智能体实现端到端的LLM微调自动化。其次，LLM微调相比传统MLE更为开放和复杂，它要求智能体不仅能处理数据，还需从异构原始数据源中“构建”训练数据（例如使用LLM API进行合成、使用领域特定工具清洗），并且需要分析训练动态、验证曲线和模型输出样本等多维信号来诊断能力差距，而不仅仅是依赖聚合指标。这种在数据构建和微调配置上的联合迭代优化，尚未被正式定义为智能体任务或得到系统评估。

因此，本文要解决的核心问题是：能否基于LLM的智能体（AI Agent）来自动化完成从原始数据到微调后模型的完整、端到端的LLM微调过程？这是一个开放且复杂的问题，涉及在广阔的搜索空间中导航，包括从多样数据源中筛选整理数据、使用复杂工具处理、构建训练管道，并根据不断增长的评估日志迭代优化策略。为了系统地研究这个问题，论文引入了FT-Dojo评估环境和FT-Agent解决方案。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：交互式智能体环境、自动化LLM训练配置以及数据为中心的LLM微调。

在交互式智能体环境方面，相关工作如SWE-Bench和MLE-bench等，侧重于在固定数据假设下评估智能体在软件工程或机器学习竞赛中的表现。本文提出的FT-Dojo则不同，它首次形式化了端到端的微调工作流，要求智能体在开放的决策空间中操作，涵盖从原始数据整理到训练配置的全过程，其场景远比现有基准复杂。

在自动化LLM训练配置方面，现有集成框架（如基于YAML/JSON的配置接口）和LaMDAgent等工作，主要通过预定义模板或盲目搜索来优化流程。本文的FT-Agent超越了这些方法，它能自主与训练框架交互，根据环境和数据上下文动态推导出最优配置，从而弥补了现有方法在适应特定数据集或硬件约束方面的不足。

在数据为中心的LLM微调方面，现有工具（如Data-Juicer）和算法（如DoReMi）主要提供标准化的数据处理流程或基于静态指标的样本选择。本文的FT-Agent则采取了根本不同的闭环优化思路：它将数据整理视为一个迭代优化问题，能够根据评估反馈自主制定针对性策略（如合成缺失概念或重加权困难样本），以解决训练中暴露的具体能力缺陷。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为FT-Agent的自主智能体系统来解决端到端LLM微调自动化的问题。其核心方法是构建一个三阶段迭代循环，每个阶段针对一个关键挑战，并整合了经验驱动的策略生成、快速失败验证和结构化反馈分析等关键技术。

整体框架上，FT-Agent是一个闭环系统，其核心是一个迭代执行的三阶段工作流：策略提出、实施与验证、反馈聚合与诊断。这个框架旨在模拟人类专家的决策过程，通过评估驱动的反馈来迭代诊断失败并优化微调策略。

主要模块与组件包括：
1.  **策略提出模块**：该模块负责生成每一轮的微调计划。它接收任务描述、先前迭代的摘要、结构化评估信号和当前系统状态，输出一个统一的假设，包含数据策略（如数据源选择、过滤规则）、训练配置（如学习率、批次大小）以及变更理由。其创新点在于采用**经验驱动**的过程：继承当前最佳配置作为基线，审查已探索的“兄弟”尝试，并借鉴历史失败以避免无效方案。通过强制使用高层描述而非累积底层操作细节，该模块有效管理了迭代历史，防止上下文无限膨胀（应对挑战1）。
2.  **实施与快速失败验证模块**：此模块旨在解决通用智能体探索效率低下的问题（挑战2）。它在允许运行完整训练前，执行**渐进式三层验证**：(i) 静态与模式验证（语法检查、依赖分析等）；(ii) 数据格式检查与小规模运行验证（在小样本或少量轮次上测试）；(iii) 运行时健全性检测（识别损失爆炸等异常）。任何一层失败都会立即中止，并提供针对性诊断日志。这种“快速失败”机制能在消耗大量计算前捕获大多数错误，显著提高了迭代吞吐量。
3.  **结构化反馈聚合与专家引导诊断模块**：该模块处理评估反馈理解有限的问题（挑战3）。训练完成后，评估器提供多层结构化反馈，包括整体指标、逐实例预测与错误标签、损失曲线以及抽样失败案例。FT-Agent分析这些信号，以识别能力差距、过拟合/欠拟合迹象、领域不匹配、噪声敏感性以及系统性推理错误（如缺少思维链）。基于此诊断，智能体可以协调地调整数据策略和训练配置。如果当前结果更优，则更新最佳配置，并将完整实验记录为后续迭代的经验。

创新点总结如下：首先，提出了首个针对端到端LLM微调自动化问题的专用智能体框架，将开放式的复杂流程转化为结构化的三阶段迭代循环。其次，设计了**经验驱动的统一假设生成机制**，有效利用历史信息进行规划，避免了长上下文干扰。第三，引入了**渐进式快速失败验证流程**，极大提升了探索效率，减少了计算浪费。最后，实现了**对多层面、非结构化评估反馈的深度结构化解析与诊断**，使智能体能够像专家一样从失败中学习并形成明确的改进假设。实验表明，FT-Agent在多个领域任务上显著优于通用智能体基线。

### Q4: 论文做了哪些实验？

该论文在自建的FT-Dojo评测套件上进行了系统实验，该套件包含5个领域（如推理、代码生成、结构化约束等）共13项任务。实验设置严格：在单张NVIDIA B200 GPU上运行，总时间预算为12小时（涵盖智能体交互、数据清洗、微调及最终评估全流程）；基础模型为Qwen2.5-7B-Instruct；训练阶段限制为标准监督微调（SFT）或LoRA，每任务最多使用2000个训练样本以模拟数据稀缺场景。FT-Agent使用GPT-5.2作为交互主干，并搭配GPT-5/GPT-4o-mini进行数据清洗与合成。

对比方法包括：（1）未微调的基础模型；（2）由资深NLP专家执行的手动SFT基线（基于规则清洗和手动调优）；（3）工具增强的通用智能体OpenHands（配备与FT-Agent相同的微调工具和环境）。主要结果显示，FT-Agent在13项任务中的10项上表现最佳，显著优于基线。关键指标包括：在AIME 2025任务中，FT-Agent在82%训练样本无解决方案的情况下取得13.30%的准确率（其他基线均为0%）；在Table QA Visualization任务中Pass@1达36.00%（相对OpenHands提升50%）；在Chemistry Molecule Editing任务中准确率为53.33%（OpenHands为40.00%）。此外，FT-Agent平均执行8.77轮优化循环（OpenHands为3.69轮），改进率达24.37%（OpenHands为17.31%），虽迭代成本略高（5.73美元 vs. 3.92美元），但探索深度和效率更优。

消融实验揭示了以下洞察：数据规模从2k增至5k样本时，性能提升有限（部分任务甚至下降），因计算时间挤压策略迭代空间；将规划主干从GPT-5.2替换为GPT-4o会导致性能显著下降（如Visualization任务降低16%），表明高层协调能力至关重要；FT-Agent在3B小模型上仍能保持强泛化性（如在Mol_Edit任务提升40%），证明其框架与模型规模无关。案例分析进一步显示，智能体能够通过历史经验进行累积学习（如在Chemistry任务中从2%准确率迭代提升至56%），但在需要因果推理的任务（如Patent Classification）中仍存在“散弹调试”局限，难以进行根因诊断。

### Q5: 有什么可以进一步探索的点？

该论文指出当前基于LLM的智能体在自动化微调过程中，虽能有效执行代码编排和迭代优化，但在诊断训练失败时更依赖模式匹配而非因果推理，且倾向于局部优化而非连贯的多步规划。这揭示了两个核心局限性：一是智能体缺乏对训练动态的因果理解能力，二是决策过程缺乏长期连贯性。

未来研究方向可围绕以下三点展开：首先，开发能够模拟复合决策下游影响的推理机制，使智能体能预见不同数据策略与训练配置的连锁反应；其次，构建更丰富的仿真环境，让智能体通过“思维实验”预判调整后果，从而突破局部最优陷阱；最后，可探索将符号推理与神经网络结合的新型架构，增强对失败案例的归因能力。此外，论文中任务领域虽多但规模有限，未来需在更复杂的现实场景中验证泛化性，并研究如何降低对高质量初始提示的依赖，实现真正的端到端自主优化。

### Q6: 总结一下论文的主要内容

本文针对大型语言模型垂直领域微调过程自动化这一开放性问题展开研究。传统微调依赖专家进行数据整理、训练配置和迭代诊断，成本高昂。论文提出了首个端到端LLM微调智能体评估环境FT-Dojo，包含5个领域的13项任务，要求智能体自主优化数据策略和训练配置。为解决该问题，作者开发了FT-Agent系统，其通过结构化迭代规划、快速失败验证和反馈分析来模拟人类专家的决策过程。实验表明，专用微调智能体显著优于通用方案，FT-Agent在13项任务中的10项上取得最佳性能，并能从稀疏监督中自主合成有效推理路径。研究同时揭示了当前基于LLM的智能体在因果推理和长期规划方面的局限性，为未来自动化微调研究指明了方向。
