---
title: "WebFactory: Automated Compression of Foundational Language Intelligence into Grounded Web Agents"
authors:
  - "Sicheng Fan"
  - "Qingyun Shi"
  - "Shengze Xu"
  - "Shengbo Cai"
  - "Tieyong Zeng"
  - "Li Ling"
  - "Yanyi Shang"
  - "Dehan Kong"
date: "2026-03-05"
arxiv_id: "2603.05044"
arxiv_url: "https://arxiv.org/abs/2603.05044"
pdf_url: "https://arxiv.org/pdf/2603.05044v1"
categories:
  - "cs.AI"
tags:
  - "Agent 架构"
  - "强化学习"
  - "工具使用"
  - "数据合成"
  - "Agent 评测"
  - "GUI Agent"
  - "Web Agent"
relevance_score: 9.0
---

# WebFactory: Automated Compression of Foundational Language Intelligence into Grounded Web Agents

## 原始摘要

Current paradigms for training GUI agents are fundamentally limited by a reliance on either unsafe, non-reproducible live web interactions or costly, scarce human-crafted data and environments. We argue this focus on data volume overlooks a more critical factor: the efficiency of compressing a large language model's (LLM) latent knowledge into actionable agent behavior. We introduce WebFactory, a novel, fully automated closed-loop reinforcement learning pipeline for GUI agents, systematically compressing LLM-encoded internet intelligence into efficient, grounded actions. Our pipeline features a process of scalable environment synthesis, knowledge-aware task generation, LLM-powered trajectory collection, decomposed reward RL training, and systematic agent evaluation. Remarkably, our agent demonstrates exceptional data efficiency and generalization. Trained on synthetic data from only 10 websites within WebFactory, it achieves performance comparable to GUI agents trained on the same amount of human-annotated data from a much larger set of environments. This superior performance is consistent across our internal offline and online transfer benchmarks, where our agent also significantly outperforms the base foundation model. We further provide critical insights into the "embodiment potential" of different LLM foundations, offering a new axis for model evaluation. This work presents a scalable and cost-effective paradigm for transforming passive internet knowledge into active, grounded intelligence, marking a critical step towards general-purpose interactive agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前图形用户界面（GUI）智能体训练范式存在的根本性局限问题。研究背景是，尽管大语言模型（LLM）从海量互联网语料中压缩出了丰富的世界知识和推理能力，形成了“互联网规模智能”，但这种智能本质上是描述性的，而非可执行的。LLM知道如何与GUI交互，却缺乏在复杂动态环境中可靠执行具体操作（如点击、键入）的“具身”能力，这被称为“语义到行动的鸿沟”。

现有方法主要面临两难困境：一方面，依赖人工标注轨迹和手动构建高保真环境，成本极高、可扩展性差且存在偏差；另一方面，直接在实时网页上训练虽能获得规模，但牺牲了可控性，面临非确定性、安全风险和噪声等挑战，难以进行可复现的研究。这两种路径都无法为创建真正可扩展且鲁棒的智能体提供可持续的方案。

因此，本文的核心问题是：如何以可扩展、低成本且安全的方式，将LLM中蕴含的被动、描述性的互联网知识，系统地“压缩”或转化为智能体主动、可执行的具身行为。为此，论文提出了名为WebFactory的全新解决方案，这是一个完全自动化的闭环强化学习流水线。它通过合成高保真离线环境、利用LLM进行知识感知的任务生成与轨迹收集、以及采用分解奖励进行强化学习训练，旨在高效地将基础模型的潜在知识转化为智能体的实际行动策略，从而克服对人工数据或不可控实时环境的依赖，迈向通用交互智能体。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、应用类和评测类。

在方法类研究中，相关工作主要围绕GUI智能体的训练范式展开。一类方法依赖人工标注的轨迹数据和精心构建的环境，如Mind2Web和WebArena，其数据获取成本高昂且规模有限。另一类方法直接在实时网络环境中训练，如WebGUM，虽能获取海量交互数据，但面临安全性、非确定性和噪声等挑战。本文提出的WebFactory范式与这些工作有本质区别：它摒弃了对人工数据或实时网络的依赖，转而构建一个高保真、可完全观测的离线环境，并利用LLM自身作为任务合成器和轨迹生成器，形成了一个全自动的闭环强化学习流水线，旨在高效“压缩”LLM的潜在知识为可执行行为。

在应用类研究中，相关工作聚焦于利用LLM赋能智能体完成网页任务。许多工作将LLM作为规划器或控制器，通过提示工程或微调来适应GUI环境。本文则更进一步，不仅将LLM用作轨迹收集的执行器，更将其视为“自身具身化的架构师”，通过系统化的流水线将其描述性知识转化为具身智能。

在评测类研究方面，现有工作多依赖于在有限人工构建环境（如MiniWoB++、WebShop）或基准测试集上的任务完成率进行评估。本文不仅提出了包含任务级和子任务级的系统化评估协议，还引入了“LLM具身潜力”这一新概念，为模型评估提供了一个衡量其知识转化为行动效率的新维度，这与仅关注性能指标的现有评测工作形成了区分。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为WebFactory的、全自动的闭环强化学习流水线来解决GUI智能体训练所依赖的数据稀缺、成本高昂且不可复现的问题。其核心方法是将大型语言模型（LLM）中蕴含的互联网知识，系统地“压缩”为可执行的、接地气的智能体行为。

**整体框架与主要模块**：
整个流水线包含五个核心环节，形成一个自动化闭环：
1.  **可扩展的环境合成**：构建了一个完全可控、可复现的离线网页环境。该环境能自动合成具有真实布局、工作流和内容的网站，覆盖电商、搜索、旅行等关键领域，并预先处理登录、验证码等障碍，确保训练的安全性和可重复性。
2.  **知识驱动的任务生成**：利用环境的完全可观测性，提取网站的导航图、页面语义和规范流程等知识规范。基于此，确定性地生成两类可执行且可验证的任务：改变状态的操作任务（如“添加商品到购物车”）和具有明确答案的信息检索任务。
3.  **LLM驱动的轨迹收集**：在离线环境中，使用一个强大的执行器（如OpenAI的计算机使用模型）来执行生成的任务，收集交互轨迹。通过状态回放、关键节点覆盖和答案验证等过滤管道，确保收集到高质量、大规模的轨迹数据，构成后续训练的样本库。
4.  **分解奖励的RL训练**：基于GUI-R1框架进行扩展，为网页智能体定义了一个结构化的动作空间。训练的核心创新在于采用了**分解的奖励机制**。每一步的奖励由格式奖励和准确性奖励加权组成。准确性奖励进行分层验证：首先检查动作类型，再根据具体类型（点击、输入、拖拽、获取答案等）精细评估坐标、文本或答案的匹配度（例如，对检索答案使用归一化的F1分数进行评分）。
5.  **系统化的智能体评估**：通过脚本化的回放进行自动评估，使用关键节点对齐的过程指标和归一化的答案匹配，无需人工评分，实现了可复现的性能衡量。

**创新点**：
*   **全自动、数据高效的闭环流水线**：从环境合成、任务生成、数据收集到RL训练和评估，全程自动化，最小化人工干预，显著降低了数据获取成本。
*   **知识感知与保证有效的任务生成**：利用环境的完整知识规范生成任务，从根本上避免了无效或不可回答的任务，确保了训练数据的质量。
*   **针对网页交互的分解奖励设计**：将奖励分解为格式合规性和动作准确性，并对不同类型的动作（特别是新增的`get_final_answer`）设计了精细的评估指标，有效引导智能体学习复杂的网页交互。
*   **将“知识压缩”作为核心评估维度**：该方法不仅训练智能体，还提供了评估不同基础模型“具身潜力”的新视角，即考察其潜在知识被压缩为有效行动的能力。

总之，WebFactory通过构建一个可控的合成环境与一套自动化的知识提取、任务生成、轨迹收集和强化学习机制，创造了一种可扩展、低成本的方法，将LLM中的被动知识转化为主动的、接地的智能体行为。

### Q4: 论文做了哪些实验？

论文实验设置包括一个全自动的闭环强化学习管道WebFactory，用于训练GUI智能体。实验在三个层面进行：内部离线网站基准测试（100个任务，覆盖10个网站，分为简单、中等和复杂难度）、离线到在线迁移测试（在Amazon、Airbnb和Booking三个真实在线平台各30个任务）以及公开基准测试（GUI-Act-Web、OmniAct-Desktop和GUI-Odyssey）。评估指标包括任务完成率（TCR）、动作准确性（分解为类型准确率、接地准确率和成功率）以及步骤效率（执行步骤与最优路径长度之比）。

对比方法包括：零射基础模型QwenVL2.5-3B和GPT-4o，以及使用大规模人工标注数据训练的GUI-R1-3B。主要结果如下：在任务生成质量上，结合知识与数据的方法将任务可执行率从31.3%提升至86.3%，复杂任务比例增加4.4倍。轨迹生成成功率从42.6%提升至84.3%，平均步骤减少38%。在内部离线基准测试中，WebFactory-3B在操作任务上达到71.8%的TCR和87.6%的准确率，与GUI-R1-3B（68.2% TCR，85.3%准确率）相当。在离线到在线迁移中，WebFactory-3B平均TCR为53.4%，显著高于QwenVL2.5-3B（20.4%）和GUI-R1-3B（37.0%）。在公开基准测试中，WebFactory-3B在GUI-Act-Web上获得84.2%的成功率，在GUI-Odyssey上获得66.0%的类型准确率，优于对比模型。此外，实验还评估了不同基础模型（GPT-5、Claude Opus 4.1和Claude Sonnet 4）驱动数据生成的效果，GPT-5在多数指标上表现最佳。

### Q5: 有什么可以进一步探索的点？

本文提出的WebFactory在自动化压缩LLM知识以训练GUI智能体方面取得了显著进展，但其局限性和未来探索空间依然广阔。首先，论文未对奖励机制进行详尽消融实验，未来可深入比较分解奖励与稀疏奖励或LLM生成奖励的差异，以优化学习动态和策略鲁棒性。其次，该方法在不同GUI范式（如游戏引擎或专业创意软件）中的泛化能力尚未验证，需扩展评估以检验其普适性。

结合个人见解，未来可从以下方向深化：一是引入多模态基础模型，增强对复杂视觉界面和动态交互的理解；二是探索元学习或课程学习框架，使智能体能自主生成适应性训练课程，加速在新环境中的迁移；三是将“具身潜能”评估标准化，建立更全面的基础模型选择指标，推动智能体从被动知识压缩向主动环境交互演进。这些改进有望将闭环训练范式拓展至物理具身环境，实现更通用的自主智能体。

### Q6: 总结一下论文的主要内容

该论文针对当前GUI智能体训练依赖不安全、不可复现的实时网络交互或昂贵人工标注数据的问题，提出了一种全新的自动化闭环强化学习框架WebFactory。其核心贡献在于将大型语言模型（LLM）中隐含的互联网知识高效“压缩”为可执行的、具身化的智能体行为，而非单纯追求数据规模。

方法上，WebFactory构建了一个全自动流水线，包括可扩展的合成环境生成、基于知识的任务生成、LLM驱动的轨迹收集、分解奖励的强化学习训练以及系统化智能体评估。该框架仅使用10个网站生成的合成数据进行训练，其智能体性能即可媲美在更大规模人工标注数据集上训练的GUI智能体。

主要结论表明，该方法在数据效率和泛化能力上表现卓越，在内部离线和在线迁移基准测试中均显著超越基础模型。论文进一步为评估不同基础LLM的“具身潜力”提供了新视角。这项工作为实现将被动网络知识转化为主动、具身的智能体提供了一条可扩展且经济高效的路径，是迈向通用交互智能体的关键一步。
