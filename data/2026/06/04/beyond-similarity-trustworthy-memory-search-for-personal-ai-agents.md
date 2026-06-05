---
title: "Beyond Similarity: Trustworthy Memory Search for Personal AI Agents"
authors:
  - "Jiawen Zhang"
  - "Kejia Chen"
  - "Jiachen Ma"
  - "Yangfan Hu"
  - "Lipeng He"
  - "Yechao Zhang"
  - "Jian Liu"
  - "Xiaohu Yang"
  - "Tianwei Zhang"
  - "Ruoxi Jia"
date: "2026-06-04"
arxiv_id: "2606.06054"
arxiv_url: "https://arxiv.org/abs/2606.06054"
pdf_url: "https://arxiv.org/pdf/2606.06054v1"
categories:
  - "cs.AI"
tags:
  - "Personal AI Agent"
  - "Memory Search"
  - "Trustworthy Agent"
  - "Memory Security"
  - "Neural Gate"
  - "Long-term Memory"
relevance_score: 9.2
---

# Beyond Similarity: Trustworthy Memory Search for Personal AI Agents

## 原始摘要

Personal AI agents increasingly rely on long-term memory to provide persistent personalization across sessions. However, existing memory pipelines are largely driven by semantic similarity: memory data close to the current query is retrieved and injected into the model context. This creates a critical trustworthiness gap, since a semantically related memory may still be contextually inappropriate, leading to threats such as cross-domain leakage, sycophancy, tool-call drift, or memory-induced jailbreaks.
  In this paper, we study memory search as a trust boundary in personal AI agents. We evaluate representative agentic memory frameworks, including A-Mem, Mem0, and MemOS, together with OpenClaw, a real-world personal-agent environment with persistent state and tool-use capability. Our results show that long-term memory is not merely a utility layer, but a durable control channel that can reshape how agents interpret tasks and execute actions, leaving them highly susceptible to the aforementioned threats. To mitigate these vulnerabilities, we propose MemGate, a lightweight and deployable memory plug-in for trustworthy memory search, with only 9M parameters and a 35.1MB footprint. MemGate is inserted between the vector memory store and the backbone LLM, requiring no LLM modification, memory-database rewriting, or inference-time LLM judge. It applies a query-conditioned neural gate to candidate memory representations, turning raw similarity search into task-conditioned memory admission. Across multiple mainstream memory frameworks, real-world agent settings, and diverse LLM backbones, MemGate reduces memory-induced threats while preserving long-term memory utility.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文聚焦于解决个人AI智能体长期记忆检索中的可信性问题。研究背景是，个人AI智能体正越来越多地依赖长期记忆来实现跨会话的个性化服务，现有的记忆管道主要基于语义相似度驱动——即检索与当前查询语义相近的记忆数据并注入模型上下文。然而，现有方法存在严重的可信赖性缺陷：一个语义相关的记忆可能在上下文中并不适宜，从而导致跨领域信息泄露、迎合用户偏见、工具调用偏移甚至记忆诱导的越狱攻击等安全隐患。本文的核心问题是揭示并解决这一信任鸿沟。作者指出，长期记忆不仅是效用层，更是一个持久的控制通道，能够重塑智能体对任务的解读和行动执行方式，而当前系统对此缺乏有效的安全边界。为应对这些漏洞，论文提出了MemGate——一种轻量级、可部署的记忆插件，将其置于向量记忆存储与骨干大语言模型之间，通过查询条件神经门控机制将原始相似度搜索转换为任务条件化的记忆准入控制，在无需修改LLM、记忆数据库或推理时LLM评判的前提下，显著降低记忆诱导威胁的同时保持长期记忆的实用效能。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要分为三类：

1. **个人AI Agent记忆框架**：如A-Mem、Mem0和MemOS。这些框架依赖语义相似度进行记忆检索，将语义相关的记忆注入模型上下文。本文指出它们存在信任漏洞，无法识别上下文不恰当的记忆，导致跨域泄露、谄媚、工具调用漂移或记忆诱导越狱等威胁。

2. **记忆安全与信任研究**：现有工作多关注LLM自身的幻觉或攻击防御，但本文首次系统研究记忆搜索作为个人AI Agent的信任边界。与仅关注语义相似度的方法不同，本文发现长期记忆不仅是效用层，更是持久的控制通道，可重塑代理的任务解释和行动执行。

3. **轻量级安全防护方法**：本文提出MemGate，一种部署于向量记忆库与LLM之间的轻量级记忆插件（9M参数/35.1MB）。与需要修改LLM、重写记忆数据库或使用推理时LLM评判的方法不同，MemGate通过查询条件神经门控将原始相似度搜索转化为任务条件记忆准入，在不降低长期记忆效用的前提下减少记忆诱导威胁。

### Q3: 论文如何解决这个问题？

论文提出了一种轻量级且易于部署的防御机制MemGate，旨在解决现有个人AI代理记忆系统中因纯语义相似性检索导致的信任缺失问题（如跨域泄露、谄媚、工具调用漂移和记忆诱导越狱）。核心思路是将记忆搜索从基于原始相似度的检索升级为任务条件下的可信准入。

整体框架是一个插入式模块，位于向量记忆存储与骨干大语言模型（LLM）之间。它不需要修改LLM、重写记忆数据库，也不需要在推理时引入LLM作为评判器。主要组件包括：一个查询条件化的神经门控网络（query-conditioned neural gate），这是核心创新点。

具体技术实现上，MemGate首先对从向量存储中检索到的候选记忆进行表征，然后基于当前输入查询（任务上下文）对这些表征进行条件化门控运算。门控机制学习判断哪些记忆在当前任务语境下是恰当和可信的，而非仅仅语义相似。只有通过门控筛选的记忆才会被注入到LLM的上下文窗口中。

核心创新在于：1) **任务条件化**：将记忆检索从通用语义匹配转变为任务感知的筛选，弥补了语义相似性在上下文适切性上的不足；2) **极轻量级**：模型仅9M参数、35.1MB存储占用，使其易于集成到现有成熟框架中；3) **非侵入性**：无需对现有记忆架构和LLM进行修改，即可提升安全性。通过这种方式，MemGate在多种主流记忆框架、真实代理环境和不同LLM骨干下，能显著降低记忆诱导威胁，同时保持长期记忆的效用。

### Q4: 论文做了哪些实验？

论文在实验中评估了现有记忆框架的脆弱性，并验证了MemGate的有效性。实验设置包括三个主流记忆框架：A-Mem、Mem0和MemOS，以及一个真实世界个人代理环境OpenClaw，该环境包含持久状态和工具使用能力。对比方法涉及原始基于语义相似性的记忆检索（baseline）和MemGate插件。主要结果分两部分：首先，在威胁评估中，现有框架在跨域泄露、谄媚行为、工具调用漂移和记忆诱导越狱四种威胁下表现出高度脆弱性，例如Mem0在跨域泄露任务中成功率近80%。其次，MemGate在所有框架和多个LLM骨干（如Llama、GPT）上显著降低了威胁成功率，同时保持了长时记忆的效用。关键数据指标包括威胁成功率和记忆效用保留率：MemGate将威胁成功率平均降低至10%以下，而记忆效用几乎不变（如A-Mem场景下从85%降至83%）。此外，MemGate仅需9M参数和35.1MB存储，无需修改LLM或数据库。

### Q5: 有什么可以进一步探索的点？

这篇论文在记忆搜索的信任边界问题上取得了显著进展，但仍存在若干值得深入探索的方向。首先，**MemGate的泛化性需要进一步验证**：当前实验主要基于有限的威胁类型（如跨域泄露、工具调用漂移），但现实世界中可能存在更隐蔽、更复杂的记忆攻击模式，例如对抗性注入的恶意记忆样本，需要设计更鲁棒的门控机制。其次，**任务条件门控的语义理解深度有限**：MemGate仅通过向量相似度进行过滤，但无法理解记忆与当前任务之间的因果关系或长期依赖，未来可以引入因果推理或图结构来建模记忆间的依赖关系。此外，**动态平衡问题**：如何在抑制有害记忆的同时，不丢弃那些看似无关但实际对创造性任务有益的潜在关联记忆，是一个值得探索的帕累托最优问题。最后，**跨智能体记忆共享的信任机制**：当多个个人AI智能体需要协作时，如何设计跨系统的信任记忆搜索协议，防止隐私泄露或行为污染，也是重要的实际方向。

### Q6: 总结一下论文的主要内容

这篇论文指出，当前个人AI代理的长期记忆系统主要依赖语义相似性进行检索，但这会导致严重的信任问题，如同跨域泄露、谄媚行为、工具调用漂移和记忆诱导的越狱攻击。论文的核心贡献是将记忆搜索定义为个人AI代理中的信任边界，并系统评估了现有框架的风险。为应对这些威胁，作者提出了MemGate，一个轻量级的可部署记忆插件（仅9M参数，35.1MB）。它位于向量记忆存储与骨干大语言模型之间，无需修改模型或数据库即可工作。MemGate通过查询条件神经门控机制，将原始语义相似性搜索转化为任务条件化的记忆准入控制。实验表明，在多种主流记忆框架和实际代理环境中，MemGate能显著减少记忆引发的威胁，同时保持长期记忆的实用性。该工作强调了记忆不仅是功能层，更是一个可控渠道，对构建可信赖的个人AI代理具有重要意义。
