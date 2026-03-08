---
title: "MM-DeepResearch: A Simple and Effective Multimodal Agentic Search Baseline"
authors:
  - "Huanjin Yao"
  - "Qixiang Yin"
  - "Min Yang"
  - "Ziwang Zhao"
  - "Yibo Wang"
date: "2026-03-01"
arxiv_id: "2603.01050"
arxiv_url: "https://arxiv.org/abs/2603.01050"
pdf_url: "https://arxiv.org/pdf/2603.01050v1"
github_url: "https://github.com/HJYao00/MM-DeepResearch"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Reasoning & Planning"
  - "Tool Use & API Interaction"
relevance_score: 8.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Tool Use & API Interaction"
  domain: "Scientific Research"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "Hyper-Search, DR-TTS (Decompose–Recompose Tool Tree Search)"
  primary_benchmark: "N/A"
---

# MM-DeepResearch: A Simple and Effective Multimodal Agentic Search Baseline

## 原始摘要

We aim to develop a multimodal research agent capable of explicit reasoning and planning, multi-tool invocation, and cross-modal information synthesis, enabling it to conduct deep research tasks. However, we observe three main challenges in developing such agents: (1) scarcity of search-intensive multimodal QA data, (2) lack of effective search trajectories, and (3) prohibitive cost of training with online search APIs. To tackle them, we first propose Hyper-Search, a hypergraph-based QA generation method that models and connects visual and textual nodes within and across modalities, enabling to generate search-intensive multimodal QA pairs that require invoking various search tools to solve. Second, we introduce DR-TTS, which first decomposes search-involved tasks into several categories according to search tool types, and respectively optimize specialized search tool experts for each tool. It then recomposes tool experts to jointly explore search trajectories via tree search, producing trajectories that successfully solve complex tasks using various search tools. Third, we build an offline search engine supporting multiple search tools, enabling agentic reinforcement learning without using costly online search APIs. With the three designs, we develop MM-DeepResearch, a powerful multimodal deep research agent, and extensive results shows its superiority across benchmarks. Code is available at https://github.com/HJYao00/MM-DeepResearch

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决构建具备深度研究能力的多模态智能体（agent）时所面临的三个核心挑战。研究背景是，尽管多模态大语言模型在复杂任务上展现出显著的推理能力，但其固有的、容量有限的参数和固定知识库，限制了其处理超出内部知识范围的信息密集型、开放世界任务的能力。现有方法（如基于检索增强生成或提示的预定义工作流）通常将检索与推理过程解耦，无法根据模型的推理状态迭代地调整检索策略，导致搜索能力和泛化性有限。

具体而言，本文识别并致力于解决以下三个关键问题：第一，**搜索密集型多模态问答数据的稀缺性**。公开可用的、需要多轮搜索和多工具调用的数据集非常有限，导致缺乏有效的监督信号来激励模型学习智能体搜索能力。第二，**缺乏有效的搜索轨迹**。传统的基于提示的搜索轨迹合成方法主要针对单轮搜索设计，难以应对在迭代推理中需要与多种搜索工具进行多轮交互的复杂场景。第三，**使用在线搜索API进行训练的成本过高**。现有方法依赖在线API（如SerpAPI），每次训练运行可能耗费数千美元，这严重限制了大规模的实验和系统性探索。

因此，本文的核心目标是开发一个名为MM-DeepResearch的多模态深度研究智能体，它能够进行显式推理与规划、多工具调用以及跨模态信息综合。为此，论文提出了三个互补的技术方案来分别应对上述不足：1）基于超图的问答生成方法（Hyper-Search）来合成高质量的搜索密集型多模态QA数据；2）分解-重组工具树搜索方法（DR-TTS）来合成高效利用多种工具的搜索轨迹；3）构建一个支持多种搜索工具的离线搜索引擎，以摆脱对昂贵在线API的依赖，从而低成本地训练出强大的多模态研究智能体。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 通用多模态大模型与智能体基础模型**：早期工作通过大规模多模态预训练和指令微调构建通用MLLMs，用于视觉语言理解任务，并通过后训练技术激励长链推理能力。近期工作进一步强调智能体行为，使MLLMs能自主迭代调用工具处理复杂任务。例如Qwen3-VL等智能体基础MLLMs，通过在预训练中包含多样化的工具交互轨迹来获得原生工具使用能力。本文旨在此基础上，开发在搜索工具调用和多模态信息合成方面能力更强的深度研究智能体。

**2. 基于工作流的搜索智能体**：这类方法采用预定义、静态的信息获取流程来检索外部知识以辅助推理，主要包括：
    *   **基于RAG的方法**：通过基于相似性的检索从数据库中获取外部知识并注入模型输入。
    *   **基于提示的方法**：通过手工编码在提示中的工作流来明确编排搜索行为，工具使用模式在推理时预定义。
    这些方法通过引入外部知识提升了事实性和知识密集型任务的表现。但本文指出，它们将搜索与推理解耦，受限于固定、僵化的流程，易导致搜索不足或过度，限制了泛化性能。本文则致力于探索以推理-搜索紧密耦合的方式主动、迭代调用搜索工具的多模态深度研究智能体。

**3. 深度研究智能体**：近期研究为LLMs配备了智能体搜索能力，使其能通过与外部文本搜索工具交互进行迭代信息寻求和证据合成，代表工作有OpenAI DeepResearch和MiroThinker。此外，一些先前工作将深度研究范式扩展到多模态领域，例如MMSearch-R1使用端到端强化学习使MLLMs具备使用图像和文本搜索工具的能力，WebWatcher则通过合成搜索密集型QA对并将其转换为VQA数据来训练多模态深度研究智能体。

**本文与上述工作的关系与区别**：本文的研究目标（多模态深度研究智能体）与第3类工作最为直接相关。然而，本文指出大多数现有工作存在搜索密集型VQA数据集和搜索工具轨迹未开源、严重依赖昂贵的在线搜索API等挑战。为此，本文提出了三个核心创新来应对：Hyper-Search方法用于生成多模态搜索密集型QA数据，DR-TTS方法用于合成搜索轨迹，以及支持多工具的离线搜索引擎用于强化学习训练。这些设计旨在克服数据、轨迹和成本瓶颈，从而有效训练出强大的多模态深度研究智能体。

### Q3: 论文如何解决这个问题？

论文通过三个核心设计来系统性地解决构建多模态深度研究智能体所面临的三大挑战。

**1. 数据生成：超图方法（Hyper-Search）**
为解决搜索密集型多模态QA数据稀缺的问题，论文提出了基于超图的生成方法。该方法首先构建一个包含图像节点和文本节点的超图，其中每个节点（网页内容或图像）都通过MLLM生成摘要或描述。然后，通过为图像和文本节点设计不同的扩展策略（如图像反向搜索、视觉搜索、URL提取等），从初始节点迭代扩展，形成深度为D的超图结构。节点之间的扩展关系被建模为超边，显式地捕获了跨模态的检索关联。最后，在超边层面进行QA生成：**层内生成**基于单个超边内的多模态证据生成问题；**层间生成**则聚合多个超边的信息，生成需要多轮搜索的、更复杂的问题。生成的QA数据经过MLLM过滤，最终得到高质量的Hyper-Search-3K数据集。

**2. 轨迹探索：分解-重组工具树搜索（DR-TTS）**
为解决有效搜索轨迹缺乏的问题，论文设计了DR-TTS方法来合成高质量的搜索轨迹。该方法首先**分解**：根据搜索工具类型（信息检索型和知识查询型）对任务进行分类，并针对每种工具分别训练一个专门的“工具专家”模型，提升单工具使用的熟练度。然后**重组**：将这些工具专家重组，以树搜索的方式进行联合探索。从根节点（输入问题）开始，每个深度上并行调用不同的工具专家生成子节点（包含推理、工具调用和响应），递归地构建搜索树。当某个路径产生最终答案时，使用LLM评估其正确性；正确的路径被终止并提取为成功轨迹，错误的路径则被剪枝。通过这种树状结构平衡探索与利用，最终收集了10K条用于监督微调的轨迹数据（DR-TTS-10K）。

**3. 低成本训练：离线搜索引擎与两阶段训练**
为规避在线搜索API的高昂成本，论文构建了一个**离线搜索引擎**。它预先收集并索引了大规模的多模态语料（包括GPT生成的查询-网页对、Wikipedia数据和图像库），能够模拟真实搜索环境，支持文本到文本、文本到图像和图像到图像等多种检索工具，从而在强化学习训练中完全替代在线API。

基于以上数据、轨迹和引擎，智能体训练采用**两阶段范式**：
- **监督微调（SFT）**：使用DR-TTS生成的轨迹进行冷启动，训练模型学习工具调用模式和多轮信息整合。
- **多轮强化学习（RL）**：采用GRPO算法，在离线搜索引擎环境中进行优化。奖励函数结合了**格式奖励**（鼓励合规的工具调用序列）和**精度奖励**（由LLM评估最终答案的正确性），通过相对优势计算来更新策略模型。

**整体架构与创新点**：MM-DeepResearch的创新在于系统性地解决了数据、轨迹和成本三大瓶颈。其核心是**Hyper-Search超图数据构造**、**DR-TTS工具专家分解与树搜索轨迹合成**，以及**离线搜索引擎支持的廉价RL训练**。这三者形成一个完整闭环：超图生成高质量QA数据，DR-TTS利用这些数据探索有效轨迹，离线引擎则利用这些轨迹和数据实现低成本、高效的智能体训练，最终得到一个能进行显式推理规划、多工具调用和跨模态信息合成的强大研究智能体。

### Q4: 论文做了哪些实验？

论文的实验设置主要包括：使用来自7个广泛领域（如艺术、体育、教育等）的视觉源构建了Hyper-Search 3K数据集，并基于InfoSeek和FVQA合成了用于监督微调（SFT）和强化学习（RL）的训练数据。评估在六个需要调用搜索工具的信息密集型基准测试上进行，如MMSearch、SimpleVQA等。对比方法包括非智能体搜索模型（如基础视觉语言模型）和现有的智能体搜索模型（如Visual-ARFT、MMSearch-R1-7B、WebWatcher、SenseNova-MARS-8B等）。实验基于不同规模的基础模型（Qwen2.5-VL-7B、Qwen3-VL-8B/32B）进行，训练时采用LLaMA-Factory进行SFT（学习率5e-6，3轮）和VeRL进行RL（学习率1e-6），最大工具调用次数为5，上下文长度扩展至70,000 token。

主要结果显示：在无原生工具调用能力的7B模型上，MM-DeepResearch-7B相比先前智能体搜索模型Visual-ARFT和MMSearch-R1-7B平均提升23%和7.1%；在SimpleVQA和MM-Search上超越SOTA模型WebWatcher分别达7.7%和12.3%。在有原生工具能力的8B和32B模型上，MM-DeepResearch-8B相比基线Qwen3-VL-8B平均提升17%，相比SenseNova-MARS-8B平均提升3.4分（SimpleVQA上提升4.2%）；MM-DeepResearch-32B相比基线提升14.9%。消融实验表明，使用Hyper-Search数据时平均工具调用次数达2.3（高于InfoSeek的1.6和Graph-based的1.7），且MMSearch分数达67.8；联合使用DR-TTS轨迹（SFT）和Hyper-Search数据（RL）获得最佳性能（MMSearch 67.8）。离线搜索工具消融显示，逐步添加基于信息的搜索（T2T、T2I、I2T）可将MMSearch分数从11.7提升至66.9，再加入基于知识的T2T搜索后达67.8。

### Q5: 有什么可以进一步探索的点？

本文提出的MM-DeepResearch在构建多模态深度研究智能体方面提供了有价值的基线，但仍存在一些局限性和可进一步探索的方向。首先，其离线搜索引擎虽然降低了成本，但可能无法完全模拟真实、动态且不断更新的网络环境，这限制了智能体在开放、实时场景下的适应能力。未来可研究如何更高效地结合在线与离线搜索，或在仿真环境中构建更逼真的动态知识库。其次，DR-TTS方法依赖于预定义的搜索工具类别和树搜索，其规划灵活性可能受限；未来可探索更开放、自适应的任务分解与工具组合策略，例如引入基于强化学习的元工具学习或神经符号混合规划方法。此外，当前工作侧重于搜索与信息合成，对深层因果推理、多源信息可信度评估与矛盾消解等方面的能力涉及较少，未来可加强智能体在复杂论证与批判性思维方面的训练。最后，该框架在多轮交互中的长期记忆管理与人类反馈融入方面仍有优化空间，可探索将用户偏好或领域知识更自然地嵌入到智能体的搜索与决策循环中，以提升个性化与实用性。

### Q6: 总结一下论文的主要内容

本文提出了一种名为MM-DeepResearch的多模态深度研究智能体，旨在解决构建能够进行显式推理与规划、多工具调用及跨模态信息综合的智能体时所面临的三大挑战：搜索密集型多模态问答数据稀缺、有效搜索轨迹缺失，以及依赖在线搜索API进行训练的成本过高。

论文的核心贡献包括三方面。首先，提出Hyper-Search方法，通过构建超图来建模和连接模态内与跨模态的视觉与文本节点，从而自动生成需要调用多种搜索工具才能解决的、高质量的搜索密集型多模态问答对。其次，设计了DR-TTS（分解-重组树搜索）方法，先将涉及搜索的任务按工具类型分解，为每种工具优化专用专家，再通过树搜索重组这些专家以联合探索搜索轨迹，从而成功解决复杂任务。最后，构建了一个支持多种搜索工具的离线搜索引擎，使得无需昂贵在线API即可进行智能体强化学习。

实验结果表明，基于上述方法构建的MM-DeepResearch智能体在多个基准测试上表现出优越性。这项工作为开发低成本、高效能的多模态研究智能体提供了一个简单而有效的基线。
