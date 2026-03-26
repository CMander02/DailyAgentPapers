---
title: "FinToolSyn: A forward synthesis Framework for Financial Tool-Use Dialogue Data with Dynamic Tool Retrieval"
authors:
  - "Caishuang Huang"
  - "Yang Qiao"
  - "Rongyu Zhang"
  - "Junjie Ye"
  - "Pu Lu"
  - "Wenxi Wu"
  - "Meng Zhou"
  - "Xiku Du"
  - "Tao Gui"
  - "Qi Zhang"
  - "Xuanjing Huang"
date: "2026-03-25"
arxiv_id: "2603.24051"
arxiv_url: "https://arxiv.org/abs/2603.24051"
pdf_url: "https://arxiv.org/pdf/2603.24051v1"
categories:
  - "cs.CL"
tags:
  - "Tool-Use Agent"
  - "Data Synthesis"
  - "Financial Agent"
  - "Tool Retrieval"
  - "Benchmark"
  - "Dialogue Generation"
relevance_score: 7.5
---

# FinToolSyn: A forward synthesis Framework for Financial Tool-Use Dialogue Data with Dynamic Tool Retrieval

## 原始摘要

Tool-use capabilities are vital for Large Language Models (LLMs) in finance, a domain characterized by massive investment targets and data-intensive inquiries. However, existing data synthesis methods typically rely on a reverse synthesis paradigm, generating user queries from pre-sampled tools. This approach inevitably introduces artificial explicitness, yielding queries that fail to capture the implicit, event-driven nature of real-world needs. Moreover, its reliance on static tool sets overlooks the dynamic retrieval process required to navigate massive tool spaces. To address these challenges, we introduce \textit{FinToolSyn}, a forward synthesis framework designed to generate high-quality financial dialogues. Progressing from persona instruction and atomic tool synthesis to dynamic retrieval dialogue generation, our pipeline constructs a repository of 43,066 tools and synthesizes over 148k dialogue instances, incorporating dynamic retrieval to emulate the noisy candidate sets typical of massive tool spaces. We also establish a dedicated benchmark to evaluate tool-calling capabilities in realistic financial scenarios. Extensive experiments demonstrate that models trained on FinToolSyn achieve a 21.06\% improvement, providing a robust foundation for tool learning in financial scenarios.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决金融领域大语言模型工具调用能力训练数据质量不足和合成方法不贴合实际的问题。研究背景是金融领域对信息的时效性和专业性要求极高，大语言模型必须借助外部工具才能处理复杂的专业任务。然而，现有主流的数据合成方法采用“反向合成”范式，即根据预先采样好的工具来生成用户查询。这种方法存在两个主要不足：首先，它造成了“人工显性化”偏差，生成的查询包含了过于完整和明确的参数信息，消除了真实人类交流中固有的模糊性和隐含性，与现实中由事件驱动的、隐含的用户需求模式不符；其次，该方法依赖于静态的、有限的工具集，忽略了在真实海量工具库中进行动态检索和导航的认知挑战，使得模型无法学习在庞大且嘈杂的候选工具集中进行筛选的能力。

因此，本文要解决的核心问题是：如何生成更高质量、更贴合金融领域真实交互动态的对话数据，以有效提升大语言模型在复杂金融场景下的工具调用与推理能力。为此，论文提出了名为FinToolSyn的“正向合成”框架，该框架从人物设定和需求出发，先合成原子工具，再结合动态检索生成多轮对话，从而模拟从隐含需求到工具调用的真实认知轨迹，以克服现有方法的缺陷。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕四个方向展开。首先，在**工具调用方法**方面，相关工作包括无需调优的ReAct框架和基于调优的方法（如ToolLLaMA），它们依赖高质量训练数据来提升模型使用工具的能力。本文同样关注工具调用，但强调其效果高度依赖于训练语料的质量与多样性。  
其次，在**工具使用数据合成**领域，现有方法大多采用“反向合成”范式，即基于预先采样的工具生成查询，这会导致“人为显性”偏差，使生成的查询过于直白，不符合现实世界中信息不对称的隐含需求。本文提出的FinToolSyn则采用“正向合成”框架，先基于潜在用户需求生成意图，再接触工具，从而更好地保持真实交互的隐含性。  
第三，关于**候选工具检索**，现有方法在动态环境中处理复杂多步指令时存在困难，且评测通常假设候选工具集是干净的，低估了实际工具发现与泛化的挑战。本文通过全局控制的动态检索过程，模拟大规模异构工具库中的噪声探索性选择，以更贴近真实场景。  
最后，在**金融领域LLMs**方面，尽管已有BloombergGPT、FinGPT等领域特定模型，以及FinMCP-Bench等多轮场景评测，但高质量工具调用数据仍因隐私问题而稀缺，导致模型在定量分析中常出现推理失败。本文通过需求驱动的原子工具合成，构建模块化生态系统，弥补了这一缺口，为垂直领域提供更鲁棒的工具学习基础。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为FinToolSyn的前向合成框架来解决金融领域工具使用对话数据生成中的问题。该框架的核心在于摒弃了传统的“反向合成”范式（即从预采样工具生成用户查询），转而采用一种从用户意图出发、动态构建工具库并模拟真实检索过程的“前向合成”方法。其整体架构包含三个核心组件，并引入了多项关键技术。

**核心方法与架构设计：**
1.  **基于人物角色的金融指令合成**：首先，从原始金融查询中通过LLM逆向推断出隐含的“用户角色”，包含基本画像和金融画像。然后，结合金融语料库（如新闻、财报）作为刺激上下文，让LLM根据采样的人物角色和上下文生成专业、符合认知水平的种子指令。这确保了查询的多样性和事件驱动的真实性，避免了人工显式化和教科书式询问。

2.  **需求驱动的大规模原子工具库构建**：不同于从现有API平台爬取的“供给驱动”方式，本方法以生成的种子指令所隐含的功能需求为驱动。通过“深度逻辑推断”将复杂查询分解为信息交互链，再通过“原子映射”将其解耦为独立的子任务，最后生成符合单一职责原则、类型约束严格（遵循模型上下文协议MCP）的可执行原子工具文档。通过“双层验证与进化”（LLM判断结合规则检查）和迭代精炼，确保工具质量，最终构建了一个包含43,066个高质量金融工具的独特知识库。此外，还构建了**语义向量索引**和**工具依赖图**两种互补的检索结构，后者通过定义工具间直接/间接依赖、参数间直接/间接依赖四种边，来捕获复杂的逻辑关联。

3.  **全局控制的动态检索对话生成**：这是框架的创新核心。采用一个**多智能体模拟框架**，包含用户、助手、工具和全局四个智能体。对话生成是一个**闭环监督**的过程：
    *   **动态规划与适应**：全局智能体根据种子指令、人物角色和实时金融上下文（通过RAG检索）初始化一个高层对话计划。该计划并非固定脚本，而是一个可变的“状态变量”。在对话过程中，全局智能体持续验证用户查询和助手动作是否符合当前计划和上下文。一旦发现不一致（如工具返回结果与计划预期冲突），便触发**自适应重新规划**，更新后续步骤以符合观察到的事实，从而防止错误累积，支持非线性交互。
    *   **闭环监督与验证**：每个智能体的输出都受到针对性验证。用户查询通过对抗性判别器过滤人工显式痕迹，并由全局智能体进行质量检查；助手智能体的动作决策（是否调用工具）和质量（工具选择、参数正确性）由全局智能体验证并触发反馈；工具智能体则模拟现实API的不稳定性，生成随机输出。
    *   **多样化噪声检索环境**：为了模拟真实部署并评估模型鲁棒性，设计了三种检索配置来动态生成每轮的候选工具集：静态检索、向量检索以及结合工具依赖图的**图增强检索**。候选集中包含相关、部分相关、冗余甚至不相关的工具，模拟了海量工具空间中的噪声环境，迫使模型进行精确判别，并自然诱导出探索、恢复和修订等真实决策行为。

**创新点总结：**
*   **前向合成范式**：从真实用户意图和场景出发，正向构建工具和对话，克服了反向合成导致查询人工化、显式化的问题。
*   **需求驱动的原子工具库**：基于任务分解构建细粒度、可复用的原子工具，并通过双层验证确保质量，突破了静态API集的限制。
*   **全局控制的闭环对话生成**：引入可动态更新的对话计划和持续验证机制，实现了对多轮对话的在线监督和自适应纠错，显著提升了对话的真实性和一致性。
*   **动态与噪声检索模拟**：通过语义索引和工具依赖图支持多种检索方式，并故意引入噪声候选集，逼真地模拟了现实金融场景中工具检索的挑战，增强了生成数据的训练价值。

### Q4: 论文做了哪些实验？

论文在FinToolBench基准上进行了全面的实验评估，涵盖多种交互模式（提示模式和函数调用模式）。实验设置包括使用基于FinToolSyn框架合成的超过148k个对话实例对开源模型（如Qwen3-8B/14B/32B）进行微调，并与前沿闭源模型（如GPT-4o、Claude-4.0-Sonnet）进行对比。

主要结果如下：在复杂多轮场景中，微调后的FinTool-Qwen3-14B在提示模式的多轮得分（MT-SC）达到79.99，超越了GPT-4o；在函数调用模式下也保持了优势（76.98），而基础模型Qwen3-8B则大幅下降至39.22。在金融业务逻辑掌握方面，模型在调用时机准确率（ITA）上最高达到74.07，显著优于Claude-4.0-Sonnet（44.44），关键数字准确率（KDA）也持续较高。细粒度错误分析显示，FinTool-Qwen3-14B在两种模式下的规则检查失败率均最低（3.6%），格式错误率在函数调用模式下仅为1.7%（GPT-4o为9.9%），且工具幻觉率为0。但在非工具场景中，由于训练数据带来的“亲工具偏差”，其总体错误率较高（58.7%），主要源于无效调用（56.8%）。

此外，消融实验表明，前向合成方法（FinToolSyn）相比反向合成在工具调用得分（65.84 vs. 64.01）和非工具场景得分（44.03 vs. 15.01）上均有提升，结合动态检索后，工具调用得分进一步提高至68.31。通用能力评估显示，微调模型在BFCL和τ-bench等通用工具使用基准上保持或略有提升，同时在GSM8K、HumanEval和MMLU等推理基准上性能波动微小（均在±2分以内），表明领域微调未导致灾难性遗忘。

### Q5: 有什么可以进一步探索的点？

该论文提出的前向合成框架虽在金融工具调用数据生成上取得进展，但仍存在若干局限和可拓展方向。首先，其工具库虽规模较大，但覆盖的金融产品和市场情境可能仍有限，未来可引入更细粒度的工具属性（如衍生品条款、风险管理指标）和跨市场联动工具，以增强复杂场景的建模能力。其次，动态检索模块仅模拟噪声候选集，未深入优化检索策略与LLM调用的协同机制，后续可探索基于强化学习的检索-调用联合训练，使模型能自适应调整工具检索范围。此外，当前对话数据侧重于单轮工具调用，现实金融咨询常涉及多轮迭代与工具组合使用，需设计层次化目标规划机制来生成长程依赖的对话序列。最后，评估基准虽针对金融场景，但缺乏对工具调用时效性、合规性等实际约束的考量，未来可引入实时市场数据流和监管规则模块，进一步提升合成数据的现实对齐度。

### Q6: 总结一下论文的主要内容

该论文针对金融领域大语言模型工具调用能力的数据合成问题，提出了一种创新的“前向合成”框架FinToolSyn。传统“反向合成”方法从预采样工具生成查询，导致数据存在“人工显性”偏差，且依赖静态工具集，无法模拟真实场景中从隐式需求出发、在庞大工具库中动态检索的复杂过程。

FinToolSyn框架通过三个步骤模拟真实交互动态：首先基于人物角色指令锚定需求，然后进行需求导向的原子工具合成，最后结合动态检索生成多轮对话。该方法生成了包含43,066个定制工具和超过148,000个对话实例的高质量数据集，并构建了包含843个人工验证样本的专用评测基准FinToolBench。基准引入了电路熔断分层加权评分机制及关键数字准确性等领域特定指标，以保障金融场景的安全性与精确性。

实验表明，使用FinToolSyn数据微调的模型在金融工具调用任务上性能提升达21.06%，尤其在处理隐含参数查询和遵循业务逻辑方面表现显著。该工作为金融领域工具学习提供了高质量数据合成方法和评估基准，有效提升了模型在复杂金融环境中的上下文推理与决策能力。
