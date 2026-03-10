---
title: "Enhancing Web Agents with a Hierarchical Memory Tree"
authors:
  - "Yunteng Tan"
  - "Zhi Gao"
  - "Xinxiao Wu"
date: "2026-03-07"
arxiv_id: "2603.07024"
arxiv_url: "https://arxiv.org/abs/2603.07024"
pdf_url: "https://arxiv.org/pdf/2603.07024v1"
categories:
  - "cs.AI"
tags:
  - "Web Agent"
  - "Memory"
  - "Planning"
  - "Generalization"
  - "Hierarchical Structure"
  - "Tool Use"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# Enhancing Web Agents with a Hierarchical Memory Tree

## 原始摘要

Large language model-based web agents have shown strong potential in automating web interactions through advanced reasoning and instruction following. While retrieval-based memory derived from historical trajectories enables these agents to handle complex, long-horizon tasks, current methods struggle to generalize across unseen websites. We identify that this challenge arises from the flat memory structures that entangle high-level task logic with site-specific action details. This entanglement induces a workflow mismatch in new environments, where retrieved contents are conflated with current web, leading to logically inconsistent execution. To address this, we propose Hierarchical Memory Tree (HMT), a structured framework designed to explicitly decouple logical planning from action execution. HMT constructs a three-level hierarchy from raw trajectories via an automated abstraction pipeline: the Intent level maps diverse user instructions to standardized task goals; the Stage level defines reusable semantic subgoals characterized by observable pre-conditions and post-conditions; and the Action level stores action patterns paired with transferable semantic element descriptions. Leveraging this structure, we develop a stage-aware inference mechanism comprising a Planner and an Actor. By explicitly validating pre-conditions, the Planner aligns the current state with the correct logical subgoal to prevent workflow mismatch, while the Actor grounds actions by matching the stored semantic descriptions to the target page. Experimental results on Mind2Web and WebArena show that HMT significantly outperforms flat-memory methods, particularly in cross-website and cross-domain scenarios, highlighting the necessity of structured memory for robust generalization of web agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型的网页智能体在跨网站、跨领域场景中泛化能力不足的核心问题。研究背景是，尽管利用历史轨迹构建的检索式记忆使智能体能够处理复杂的长周期网页任务，但现有方法通常采用扁平化的记忆结构，将高层任务逻辑与特定网站的动作细节混在一起存储。这种“意图-执行纠缠”导致智能体在未见过的网站上执行任务时，检索到的记忆内容与当前网页状态不匹配，引发工作流错位和逻辑不一致的执行，例如尝试点击新页面上不存在的按钮或跳过必要的导航步骤。

现有方法的不足在于，其扁平记忆虽能基于意图相似性进行检索，却无法将可迁移的任务逻辑与不可迁移的站点具体实现细节解耦。当应用于新环境时，检索到的动作细节（如元素ID）可能无效，污染决策上下文，严重阻碍了智能体的稳健泛化。

因此，本文要解决的核心问题是：如何设计一种结构化的记忆框架，以显式地解耦逻辑规划与动作执行，从而使网页智能体能够更好地将其在已知网站上学到的任务知识，迁移并适应到全新的、未见过的网站和任务领域，实现真正的跨网站泛化。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、应用类和评测类。

在方法类研究中，早期工作如World of Bits和DOMNet基于强化学习或模仿学习，利用图神经网络处理DOM树，但在真实网站多样性上泛化能力有限。大语言模型（LLM）的兴起带来了新范式，如ReAct和Tree of Thoughts框架，它们交织推理与行动执行。针对网页领域，WebGPT、MindAct和SeeAct等系统专注于在HTML或截图上进行动作落地。近期研究如Prune4Web和HtmlRAG通过动态修剪DOM树来提升准确性，验证了使用层次结构过滤上下文的设计选择。在记忆增强方面，检索增强生成（RAG）和情景记忆模块（如Reflexion、Voyager、MemGPT）被用于支持长程任务，但通常采用扁平记忆结构，容易在跨网站时产生上下文污染。本文提出的分层记忆树（HMT）与这些扁平记忆方法（如Agent Workflow Memory）形成对比，通过三层层次结构显式解耦逻辑规划与动作执行，解决了工作流不匹配问题。

在应用类研究中，多模态智能体（如CogAgent、AppAgent）探索了在移动和桌面GUI上的视觉落地，而Set-of-Mark提示等技术用于改进元素识别。本文的HMT通过语义元素描述符主动过滤观测噪声，补充了这些架构。在规划与机器人领域，分层强化学习和基于分解的提示策略（如Chain-of-Thought）长期用于管理复杂性。近期算法如Language Agent Tree Search（LATS）和CRITIC集成了树搜索和自我验证。类似地，MemTree和HiAgent等研究探索了结构化记忆表示。本文的HMT与“规划者-执行者”范式（如LGRL、LDSC）相关，但独特之处在于将这种分解固化到持久的记忆结构中，并引入了自动抽象流程，使动作模式能与具体网页实现解耦。

在评测类研究中，本文的实验基于Mind2Web和WebArena数据集进行，这些是评估网页智能体性能的基准。与相关工作的区别在于，HMT在跨网站和跨领域场景中显著优于扁平记忆方法，突出了结构化记忆对智能体鲁棒泛化的必要性。

### Q3: 论文如何解决这个问题？

论文通过提出**分层记忆树（HMT）** 这一结构化框架来解决现有基于检索记忆的Web智能体在未见网站上泛化能力不足的问题。其核心思想是将高层任务逻辑与网站特定的动作细节**显式解耦**，从而避免工作流错配，提升跨网站和跨领域的泛化能力。

**整体框架**由两部分构成：一个**自动化构建管道**，用于从原始交互轨迹中抽象出分层记忆树；一个**阶段感知的推理机制**，包含规划器（Planner）和执行器（Actor），用于利用记忆树进行决策。

**主要模块/组件与关键技术**：
1.  **分层记忆树（HMT）的结构**：记忆树分为三层，逐级抽象。
    *   **意图层（Intent Level）**：将多样化的用户指令映射到标准化的任务目标和约束，剥离了语言表达的变体。
    *   **阶段层（Stage Level）**：定义可重用的语义子目标（如“筛选结果”），每个子目标由**可观察的前置条件和后置条件**描述（如“搜索结果可见”）。这是实现阶段感知和防止工作流错配的关键。
    *   **动作层（Action Level）**：存储动作模式（如“点击”）和**可迁移的语义元素描述**（如“标签为‘搜索’的按钮”），而非原始的元素ID或坐标，确保记忆在不同网站间有效。

2.  **记忆构建管道**：这是一个自动化的流程，使用大语言模型（LLM）处理成功轨迹。
    *   **指令规范化**：将原始指令重写为标准意图和约束。
    *   **子目标分割**：将轨迹分割为连续的语义段，并为每个段生成名称及前后置条件。包含严格的一致性检查和回退机制，确保结构有效性。
    *   **步骤抽象**：为每个动作生成抽象表示，丢弃原始元素标识符，创建可迁移的步骤节点。

3.  **阶段感知推理机制**：
    *   **分层检索**：采用自上而下的检索策略。首先根据当前指令检索相关任务节点，然后结合历史摘要和当前观察，通过一个**综合评分函数**（平衡语义相似度和条件匹配度）检索候选子目标。
    *   **规划器（Planner）**：执行状态抽象和验证。它将当前观察与检索到的子目标的前后置条件进行匹配，选择逻辑上一致的当前阶段。它还包含一个**置信度感知的回退机制**，当置信度低时扩大检索范围或回退到无记忆的基线策略，防止错误传播。
    *   **执行器（Actor）**：负责动作落地。它接收规划器选定的子目标和检索到的步骤范例，利用其中的语义元素描述，在当前页面的候选元素集中定位匹配的元素，从而生成具体动作，而非直接复制范例中的ID。

**创新点**：
*   **结构化记忆设计**：首次提出三层分层的记忆结构，显式分离任务逻辑、语义阶段和可执行动作，从根本上解决了扁平化记忆导致的工作流错配问题。
*   **条件驱动的阶段感知**：在阶段层引入基于UI状态描述的前后置条件，使智能体能够根据当前页面证据（而非仅历史）判断执行进度，实现更鲁棒的阶段对齐。
*   **语义抽象与可迁移性**：在构建管道中，通过指令规范化和步骤抽象，剥离了网站特定的细节（如原始指令措辞、元素ID），使记忆核心是语义和功能性的，从而具备跨网站迁移能力。
*   **集成化的推理与回退**：推理过程将分层检索、条件验证、置信度评估和回退策略有机结合，形成了一个稳健的决策闭环，有效降低了在陌生环境中被错误记忆误导的风险。

### Q4: 论文做了哪些实验？

论文在离线（Mind2Web）和在线（WebArena）两种记忆归纳设置下进行了实验。实验设置上，使用GPT-4作为所有组件的骨干模型，解码温度设为0，并设置了检索宽度、历史截断长度、观察总结元素数等具体参数。

数据集与基准测试方面，离线评估使用Mind2Web大规模数据集，包含来自137个真实网站的2000多个开放任务，并在Cross-Task、Cross-Website和Cross-Domain三个测试分割上评估泛化能力。在线交互评估使用WebArena环境，涵盖购物、CMS、GitLab和地图等多个领域，通过执行验证器判断任务成功。

对比方法包括通用智能体（MindAct、WebArena基线）、分层或检索增强智能体（SteP、AutoEval、Agent Workflow Memory (AWM)），并构建了使用扁平检索的消融基线（Flat Retrieval）以评估层次结构贡献。

主要结果与关键指标如下：
1. 在Mind2Web上，HMT在所有分割上表现最优。在关键的Cross-Website分割中，其步骤成功率（StepSR）达到39.7%，比AWM显著提升6.0%。在Cross-Task分割中，步骤成功率为48.5%，任务完成率（EA）为54.2%，与AWM相当。
2. 在WebArena上，HMT实现了38.7%的总任务成功率（TaskSR），在逻辑复杂的GitLab和CMS领域分别提升5.8%和5.0%。平均步骤数从5.9降至5.2，表明减少了冗余探索。
3. 消融实验证实了各组件的重要性：使用扁平记忆导致WebArena性能下降6.6%；移除前后条件导致性能下降2.5%；使用原始元素标识符在Cross-Website设置中使步骤成功率从39.7%暴跌至12.4%。
4. 机制分析显示，HMT在检索召回率（Recall@5）上达到84.2%，显著高于扁平基线的65.8%。在跨网站设置中，语义描述符的定位成功率为76.8%，而原始标识符仅为12.4%。
5. 效率方面，HMT通过语义抽象将平均上下文令牌减少约72.7%，每步延迟降至3.5秒（标准检索为5.2秒），每任务推理成本降低71.0%。

### Q5: 有什么可以进一步探索的点？

该论文提出的HMT框架在提升Web Agent泛化能力方面取得了显著进展，但其仍有进一步探索的空间。局限性主要体现在：首先，其分层记忆的构建严重依赖LLM进行轨迹抽象和分割，这可能导致错误累积，且自动化流程在复杂、模糊的网页交互中可能不够鲁棒。其次，当前方法主要处理结构化的DOM信息，对高度依赖视觉空间理解的任务（如地图导航）表现不佳，这限制了其在多模态环境下的应用。最后，记忆树的在线更新机制较为简单，仅基于成功轨迹，缺乏对失败经验的利用和记忆的动态优化。

未来研究方向可包括：1) **增强记忆构建的鲁棒性**：探索更可靠的子目标自动分割算法，或引入少量人类反馈来校正抽象过程。2) **融合多模态信息**：将视觉特征（如截图、图标样式）更深度地整合到语义描述和状态匹配中，以提升对非文本化或动态内容的处理能力。3) **实现更智能的记忆管理**：研究记忆的压缩、遗忘和基于效用的检索机制，使系统能持续学习并优先调用高效策略。4) **探索更复杂的泛化场景**：测试框架在跨平台（如桌面应用与移动端）或涉及多轮对话协作任务中的能力，这将是迈向通用智能体的关键一步。

### Q6: 总结一下论文的主要内容

该论文针对基于大语言模型的网页智能体在跨网站任务中泛化能力不足的问题，提出了分层记忆树（HMT）框架。核心问题是现有基于检索的扁平化记忆结构将高层任务逻辑与网站特定的操作细节混为一谈，导致在新环境中出现工作流不匹配和执行逻辑不一致。

HMT的核心贡献是通过一个自动抽象流程，从原始交互轨迹中构建一个三层层次化记忆结构：意图层将多样用户指令映射到标准化任务目标；阶段层定义了以可观测的前后条件为特征的可复用语义子目标；操作层存储与可迁移的语义元素描述配对的操作模式。基于此结构，论文设计了包含规划器和执行器的阶段感知推理机制。规划器通过显式验证前条件，使当前状态与正确的逻辑子目标对齐，从而防止工作流错配；执行器则通过将存储的语义描述与目标页面匹配来落地具体操作。

实验结果表明，HMT在Mind2Web和WebArena基准上显著优于扁平记忆方法，尤其在跨网站和跨领域场景中提升明显。这证明了结构化记忆对于提升网页智能体鲁棒泛化能力的必要性和有效性。
