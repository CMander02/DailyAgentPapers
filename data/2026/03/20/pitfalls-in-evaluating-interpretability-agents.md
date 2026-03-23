---
title: "Pitfalls in Evaluating Interpretability Agents"
authors:
  - "Tal Haklay"
  - "Nikhil Prakash"
  - "Sana Pandey"
  - "Antonio Torralba"
  - "Aaron Mueller"
  - "Jacob Andreas"
  - "Tamar Rott Shaham"
  - "Yonatan Belinkov"
date: "2026-03-20"
arxiv_id: "2603.20101"
arxiv_url: "https://arxiv.org/abs/2603.20101"
pdf_url: "https://arxiv.org/pdf/2603.20101v1"
categories:
  - "cs.AI"
tags:
  - "Interpretability Agent"
  - "Evaluation"
  - "Circuit Analysis"
  - "Research Agent"
  - "LLM-based Agent"
  - "Autonomous Experimentation"
relevance_score: 7.5
---

# Pitfalls in Evaluating Interpretability Agents

## 原始摘要

Automated interpretability systems aim to reduce the need for human labor and scale analysis to increasingly large models and diverse tasks. Recent efforts toward this goal leverage large language models (LLMs) at increasing levels of autonomy, ranging from fixed one-shot workflows to fully autonomous interpretability agents. This shift creates a corresponding need to scale evaluation approaches to keep pace with both the volume and complexity of generated explanations. We investigate this challenge in the context of automated circuit analysis -- explaining the roles of model components when performing specific tasks. To this end, we build an agentic system in which a research agent iteratively designs experiments and refines hypotheses. When evaluated against human expert explanations across six circuit analysis tasks in the literature, the system appears competitive. However, closer examination reveals several pitfalls of replication-based evaluation: human expert explanations can be subjective or incomplete, outcome-based comparisons obscure the research process, and LLM-based systems may reproduce published findings via memorization or informed guessing. To address some of these pitfalls, we propose an unsupervised intrinsic evaluation based on the functional interchangeability of model components. Our work demonstrates fundamental challenges in evaluating complex automated interpretability systems and reveals key limitations of replication-based evaluation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自动化可解释性系统（特别是利用大语言模型构建的自主智能体）在评估方面面临的挑战。随着研究从固定的一次性工作流程转向完全自主的可解释性智能体，如何有效评估这些系统生成解释的准确性和可靠性成为一个紧迫问题。现有评估方法主要依赖于将系统输出与人类专家的事后解释进行比对（即基于复现的评估），但这种方法存在严重不足：人类专家的解释本身可能具有主观性或不完整性；仅对比最终结果会掩盖研究过程的合理性；并且大语言模型可能通过记忆训练数据中的已有发现或进行有根据的猜测来“复现”结果，而非真正通过实验推理获得理解。本文的核心问题是：如何设计一种能够克服上述缺陷、可扩展且可靠的评估框架，以准确衡量自主可解释性智能体在分析模型内部电路（如识别并解释模型中执行特定任务的子网络组件功能）时的真实能力。为此，论文不仅构建了一个用于电路分析的智能体系统进行案例研究，揭示了基于复现评估的多个陷阱，还提出了一种基于模型组件功能可互换性的无监督内在评估方法，作为迈向更客观、可扩展评估的初步尝试。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕自动化可解释性系统和其评估方法展开，可分为以下几类：

**1. 自动化可解释性方法与系统：**
早期工作主要利用大型语言模型（LLM）来自动化解释神经元或特征的激活模式，但实验设计通常仍由人类研究者定义。近期研究（如本文引用的工作）则进一步开发了**自主可解释性智能体**，这些系统能像人类研究者一样自主设计实验并迭代修正假设，代表了更高的自动化水平。本文构建的智能体系统即属于此类前沿探索，其核心创新在于专注于对**已识别电路**中的组件进行语义功能解释，这是自动化流程中一个相对未被充分探索的阶段。

**2. 基于复现的评估方法：**
这是当前评估自动化可解释性系统的主流方法，即通过比较系统输出与**人类专家已有的解释**（如文献中的电路分析案例）来判断系统性能。本文的研究起点正是采用了这种方法，并在六个任务上取得了看似有竞争力的结果。然而，本文的核心贡献在于深刻揭示了这种评估范式的**根本性缺陷**：人类专家的解释本身可能具有主观性或是不完整的；仅比较最终结果会掩盖研究过程的合理性；并且LLM系统可能通过记忆或猜测来“复现”结论，而非基于真实的实验推理。

**3. 新型评估方法的探索：**
为了应对上述挑战，本文提出了一种**无监督的内在评估方法**，其基础是模型组件的**功能可互换性**。该方法不依赖于人类专家标注，旨在实现可扩展的评估。这与之前依赖人工基准或专家判断的评估工作形成了区别，是迈向更可靠、规模化评估的重要初步尝试。

综上，本文与相关工作的关系是：它建立在自动化可解释性智能体这一新兴方向之上，但通过批判性地审视并揭露主流评估方法（复现法）的深层陷阱，推动了该领域对评估难题的认知，并提出了一个替代性的评估思路。

### Q3: 论文如何解决这个问题？

论文通过构建一个基于大语言模型（LLM）的自主研究代理系统，来自动化电路分析过程，以解决人工解释性分析耗时费力、难以扩展的问题。其核心方法是一个三阶段的工作流程：首先，由研究人员指定待分析的任务和已识别的电路组件集合；其次，研究代理对每个电路组件进行独立、迭代的分析，生成其功能描述；最后，利用LLM根据功能相似性对组件进行聚类，形成高层次的功能摘要。

系统的核心是**研究代理**，它基于Claude Opus 4.1构建，并配备了标准解释性分析工具（如词汇投影、因果干预、注意力模式分析）。代理的运作模拟人类研究者的迭代过程：在每一轮迭代中，它先分析上一轮实验的结果，然后基于证据提出3-5个合理的假设，接着设计下一组实验（包括指定工具调用和生成分析用的提示词），并最终在获得足够证据后输出组件的功能描述及关键证据。这种结构化的“分析-假设-实验”循环是方法的关键创新之一，旨在实现自主、深入的探索。

在架构设计上，系统包含几个主要模块：1）**工具接口模块**，封装了TransformerLens等库实现的解释性工具，为代理提供标准化的实验能力；2）**代理推理模块**，负责驱动上述迭代循环；3）**聚类模块**，在获得所有组件的独立描述后，由另一个LLM根据功能描述和证据，按词元位置对组件进行聚类，从而概括出电路的高层功能结构。

论文的创新点在于：1）提出了一个**完全自主的、代理驱动的解释性分析框架**，将开放式假设生成与实验设计自动化结合；2）在评估层面，揭示了单纯基于复现人类专家结论进行评估的陷阱（如主观性、记忆偏差），并为此提出了一种基于**组件功能可互换性的无监督内在评估方法**，作为对传统评估的重要补充。整体上，该系统旨在通过LLM的自主研究能力，将电路分析从高度依赖人工的流程转变为可扩展的自动化过程。

### Q4: 论文做了哪些实验？

论文实验主要包括基于人类解释的外部评估和内在功能互换性评估。实验设置上，作者构建了一个研究代理系统，该系统能迭代设计实验并完善假设，同时设置了一个一次性系统作为基线，后者将实验输出作为静态输入提供给LLM以单次生成解释。

数据集/基准测试方面，实验选取了六项先前研究中的电路分析任务，涉及不同模型（如GPT-2-Small、Pythia-160M、LLaMA-7B等），电路规模从8个头到64个头不等，聚类数量为2到7个。具体任务包括IOI、Greater-Than、Acronyms、Colored Objects和Entity Tracking。

对比方法上，研究代理系统与一次性基线系统进行比较。评估采用基于GPT-5的LLM-as-a-judge方法，通过三个指标衡量与人类专家解释的一致性：组件功能准确性（Component Functionality Accuracy）、聚类功能准确性（Cluster Functionality Accuracy）和组件分配准确性（Component Assignment Accuracy）。

主要结果显示，两个系统均取得了有竞争力的性能，但均未完全匹配专家解释。例如，在部分任务中，组件分配准确性较高，但研究代理系统并未因更高的自主性而持续优于一次性基线。关键数据指标包括：代理系统平均每个组件分析调用14.2次工具、进行4.5次迭代；评估中使用了6382次工具调用。这些结果揭示了基于复现的评估存在局限性，如人类解释可能主观或不完整，且系统可能通过记忆或猜测复现发现。

### Q5: 有什么可以进一步探索的点？

基于论文内容，可以进一步探索的点包括：

**1. 评估范式的根本性革新：** 论文揭示了基于复现人类专家解释的评估方法存在三大根本缺陷：人类解释的主观性与不完整性、过程信息的缺失，以及LLM的“记忆/猜测”问题。未来的研究需要超越简单的“结果匹配”评估，构建能够量化并奖励**研究过程质量**（如假设生成、实验设计严谨性、泛化性测试）的评估框架。这可能需要定义新的评估指标，例如“研究路径的鲁棒性”或“反事实推理能力”。

**2. 开发更鲁棒的无监督/内在评估方法：** 论文提出的基于组件功能可互换性（如权重交换）的评估是一个有前景的起点，但其结果（轮廓分数普遍不高）表明该方法仍需完善。未来可以探索更复杂的内在评估，例如：评估发现的“电路”在干预（如激活修补）下的因果效力；或者构建动态评估，测试系统在遇到全新、未见过的模型行为模式时的探索与解释能力，从而彻底规避记忆风险。

**3. 针对“记忆与推理”的深入解耦：** 尽管论文通过添加噪声实验进行了初步探索，但如何严格区分LLM是基于证据推理还是基于先验知识（包括隐性知识）进行“合理猜测”，仍是一个核心挑战。未来的工作可以设计更精巧的“对抗性”评估任务，例如使用在训练数据中几乎不可能出现的人造电路或行为模式，或者系统性地控制提供给智能体的信息，来更精确地测量其真实推理能力。

**4. 扩展任务与模型的复杂性：** 当前评估局限于少数几个已被充分研究的电路分析任务，假设空间小，容易过拟合。未来的研究必须在更广泛、更复杂、定义更不明确的任务（如理解大模型的规划、知识推理等高层能力）上进行测试，这不仅能检验系统的泛化性，也能推动自动化可解释性技术解决真正的前沿问题。

### Q6: 总结一下论文的主要内容

该论文研究了自动化可解释性代理在评估过程中存在的陷阱。核心问题是：随着基于大语言模型的自主可解释性代理的发展，如何有效评估其生成的复杂、开放式解释。论文以模型电路分析（解释模型组件在特定任务中的作用）为具体场景，构建了一个由研究代理自主设计实验、迭代优化假设的智能体系统。

方法上，该系统在六个文献中的电路分析任务上与人类专家解释进行比较，初看表现具有竞争力。然而，深入分析揭示了基于复现的评估方法存在根本性缺陷：人类专家解释可能具有主观性或是不完整的；基于结果的比较掩盖了研究过程本身；LLM系统可能通过记忆或有根据的猜测来复现已发表结论，而非真正理解。

论文的主要结论和贡献在于：1）系统分析了用于电路分析的智能体系统；2）揭示了基于复现评估的关键陷阱，如对不完整或主观“金标准”的依赖、以及LLM的“走捷径”问题；3）提出了一种基于模型组件功能可互换性的无监督内在评估方法，作为迈向可扩展、无监督评估的初步尝试，以部分应对上述挑战。这项工作凸显了评估复杂自动化可解释性系统的基本困难，并指出了当前评估范式的关键局限。
