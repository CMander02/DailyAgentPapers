---
title: "SOP-Bench: Complex Industrial SOPs for Evaluating LLM Agents"
authors:
  - "Subhrangshu Nandi"
  - "Arghya Datta"
  - "Rohith Nama"
  - "Udita Patel"
  - "Nikhil Vichare"
  - "Indranil Bhattacharya"
  - "Prince Grover"
  - "Shivam Asija"
  - "Giuseppe Carenini"
  - "Wei Zhang"
  - "Arushi Gupta"
  - "Sreyoshi Bhaduri"
  - "Jing Xu"
  - "Huzefa Raja"
  - "Shayan Ray"
  - "Aaron Chan"
  - "Esther Xu Fei"
  - "Gaoyuan Du"
  - "Zuhaib Akhtar"
  - "Harshita Asnani"
date: "2025-06-09"
arxiv_id: "2506.08119"
arxiv_url: "https://arxiv.org/abs/2506.08119"
pdf_url: "https://arxiv.org/pdf/2506.08119v2"
categories:
  - "cs.AI"
tags:
  - "Agent Benchmark"
  - "Tool Use"
  - "Multi-Step Reasoning"
  - "Industrial Automation"
  - "Evaluation Framework"
  - "Agent Architecture"
  - "Procedural Tasks"
relevance_score: 8.0
---

# SOP-Bench: Complex Industrial SOPs for Evaluating LLM Agents

## 原始摘要

LLM-based agents struggle to execute complex, multi-step Standard Operating Procedures (SOPs) that are fundamental to industrial automation. Existing benchmarks fail to capture the procedural complexity and tool orchestration demands of real-world workflows. We introduce SOP-Bench, a benchmark of 2,000+ tasks from human expert-authored SOPs across 12 business domains (healthcare, logistics, finance, content moderation, etc.). Using a human-AI collaborative framework, experts crafted authentic SOPs while AI generated artifacts (tools, APIs, datasets), all human-validated, yielding realistic tasks with executable interfaces and ground-truth outputs.
  SOP-Bench serves as a research enabler for systematically investigating agent architectures, model capabilities, and deployment considerations across diverse procedural tasks. We demonstrate its utility through illustrative experiments with a subset of frontier models across Function-Calling (FC) and ReAct agents, revealing critical insights. For example, (1) newer models do not guarantee better performance - Claude 4 family outperforms Claude 4.5 family on ReAct tasks (Claude 4 Opus: 72.4% vs. Claude 4.5 Sonnet: 63.3% task success rate), demonstrating that production upgrades require validation; (2) no single model-agent combination dominates: best performances range from 57% to 100% depending on domain. These examples illustrate how SOP-Bench enables isolating and studying specific dimensions of agent performance without costly production experiments. Our goal is not to rank model capabilities or build optimal agents, but to provide a rigorous evaluation framework that enables the researchers and practitioners to systematically investigate agent design choices, model selection, and deployment strategies. We release the benchmark at https://github.com/amazon-science/sop-bench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型（LLM）的智能体（Agent）在真实工业场景中执行复杂、多步骤标准作业程序（SOP）时面临的评估难题。研究背景是，SOP是各行业可靠运营的核心，将领域专业知识、合规规则和决策逻辑编码为结构化工作流。虽然LLM的进展激发了使用智能体自动化执行SOP的兴趣，但将其部署到生产环境面临诸多挑战。

现有方法的不足在于，当前的评估基准（如Gorilla、API-Bank、ComplexBench等）存在显著缺陷。它们通常孤立地测试智能体的单项能力（如工具使用、规划或指令遵循），使用的是干净、合成的提示，无法反映真实世界SOP的“混乱”特性。这些基准未能捕捉到工业工作流中普遍存在的程序复杂性、工具编排需求、现实歧义性、隐式领域知识、错误处理和工作流依赖等关键维度。例如，真实的SOP可能包含模糊语言、复杂的决策树和需要上下文解读的步骤，这对缺乏领域知识的LLM智能体构成了巨大挑战。

因此，本文要解决的核心问题是：缺乏一个能够全面、真实地评估LLM智能体在复杂工业SOP环境下执行能力的基准。为此，作者引入了SOP-Bench，这是一个从12个商业领域（如医疗保健、物流、金融）的人类专家撰写的真实SOP中构建的综合性基准，包含2000多个任务。它通过人机协作框架生成可执行的工具接口和真实输出，旨在系统性地研究智能体架构、模型能力和部署考量，填补现有评估框架在真实性和复杂性方面的空白，为研究者和实践者提供一个严格的评估工具，以探索智能体设计选择、模型选择和部署策略，而不仅仅是进行模型排名。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. LLM智能体规划与工具使用**：如ReAct、AutoGPT、LangChain等架构，以及ToolChain和ToolLLM等动态工具执行系统。这些研究聚焦于智能体的自主决策和多步推理，但通常在过于简化的环境中评估，难以反映真实工业流程的复杂性。

**2. 指令遵循与基准评测**：包括SUPER-NATURAL-INSTRUCTIONS、AlpacaEval、FollowEval等指令遵循数据集，以及ComplexBench、InFoBench等多步骤基准。它们多关注指令复杂性，但常使用机器格式化输入，缺乏人类撰写的SOP中固有的模糊性和变异性。

**3. 工具使用与API中心化基准**：如Gorilla、API-Bank和BENCHAGENTS，主要评估孤立的工具调用或API使用能力，缺乏跨依赖步骤的协调工具使用、错误处理和状态跟踪等流程执行关键要素。

**4. 智能体评估框架**：例如AgentBench和PlanBench，提供了评估规划与工具使用的通用框架，但其任务设置范围较窄，缺乏工业SOP典型的流程结构、条件逻辑和现实模糊性。ALFWorld和BabyAI等具身智能体环境则与工作流自动化任务存在根本差异。

**5. SOP自动化与业务流程建模**：传统方法依赖基于规则的系统或形式化流程建模语言，需要人工形式化，过程繁琐且脆弱。近期有研究探索用LLM将自然语言程序转化为可执行工作流（如CAG方法），但其目标描述简短、领域局限（如数据集成），且相关数据集未公开。SOP-Maze虽发布了业务运营SOP，但缺乏用于智能体评估的工具或真实数据。

**本文与这些工作的关系与区别**：SOP-Bench旨在弥补上述空白。它通过提供（1）真实的SOP风格指令、（2）广泛的领域覆盖、（3）用于执行的结构化API，以及（4）基于现实复杂性的评估协议，构建了一个更全面的测试平台。与Gorilla等孤立评估API使用的基准不同，SOP-Bench评估智能体在具有相互依赖性、模糊性和错误处理要求的完整工作流上的表现，专注于企业自动化环境中的智能体鲁棒性评估。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为SOP-Bench的综合性基准测试来解决评估LLM智能体执行复杂工业标准操作程序（SOP）能力不足的问题。其核心方法是一个新颖的人机协作框架，旨在生成真实、可执行且具有挑战性的工业级任务。

整体框架是一个分阶段、迭代的生成流程。首先，**人类领域专家**负责提供初始的业务任务描述和任务上下文，并起草真实的SOP初稿，确保基准的领域真实性和工业相关性。随后，**AI模型（主要使用Claude 3.5 Sonnet）** 在人类提供的材料基础上，通过分层提示策略，依次生成一系列支撑性工件：1）**数据集模式**，作为语义脚手架，定义了输入参数、决策点和预期结果，以减少幻觉并确保一致性；2）**精炼的SOP**，确保其与数据模式一致，并包含详细指令和决策逻辑；3）**数据集**，包含完整的程序上下文、结构化输入/输出以及具有挑战性的边缘案例；4）**API和工具规格**，定义了接口的输入输出契约；5）**可执行工具代码**。**关键**在于，每一个AI生成的环节都经过了**人类专家的严格验证**，确保逻辑正确性、领域准确性和可执行性。

该方法的创新点主要体现在三个方面。第一是**真实性**与**可控复杂性**的结合：通过人机协作，既捕捉了工业流程中的真实细节（如行业术语、隐含知识、模糊指令），又能在SOP、工具和数据等多个层面系统性地引入受控的复杂性（例如分支逻辑、语义相似的冗余工具、干扰变量），从而精准测试智能体的推理、工具选择和抗干扰能力。第二是**可扩展性与可复现性**：AI的介入使得大规模生成高质量、多样化的任务成为可能，同时通过模拟API（预计算输入输出）确保了评估的稳定性和可复现性。第三是**系统化的评估设计**：论文不仅提供了包含2400多个任务、覆盖12个业务领域的基准，还实现了两种基线智能体架构（轻量级的函数调用FC智能体和支持思维链的ReAct智能体），并定义了执行完成率（ECR）和任务成功率（TSR）等量化指标，为后续研究提供了一个可系统比较不同智能体设计、模型能力和部署策略的严谨框架。

### Q4: 论文做了哪些实验？

论文在SOP-Bench基准上进行了系统实验，主要评估了不同LLM模型与两种智能体架构（Function-Calling和ReAct）在复杂工业SOP任务上的性能。

**实验设置与数据集**：实验在SOP-Bench基准上进行，该基准包含来自12个业务领域（如医疗、物流、金融等）的2000多个任务，源自人类专家编写的标准操作程序。评估了11种前沿大语言模型，包括Llama-3.3-70B-Instruct、GPT-OSS-120B、DeepSeek-R1、Claude系列（3.5 Sonnet v2至4.5 Opus等）。主要对比了Function-Calling（FC）和ReAct两种智能体架构。

**主要结果与关键指标**：
1.  **架构对比**：以Claude 4 Opus为例，ReAct的平均任务成功率（TSR）为72%，高于FC的68%，但ReAct的延迟显著更高（87.82秒 vs. 66.21秒）。ReAct仅在13个SOP中的8个上优于FC，表明性能依赖具体任务。
2.  **模型与架构协同设计**：性能并非随模型升级单调提升。FC智能体随模型升级有稳定小幅提升（如Claude 3.5 v2到4.5 Sonnet，TSR从65.8%升至67.5%），而ReAct智能体使用Claude 4.5 Sonnet时TSR降至63.3%，反而不如旧版。
3.  **任务成功率范围**：最佳性能因领域差异巨大，TSR从57%（如“了解你的业务”任务）到100%（如“患者接待”任务）不等。不同SOP难度差异显著，最简单任务（如“推荐滥用检测-简单版”）平均TSR为94.3%，最困难任务（如“视频标注”）仅27.8%，相差3.4倍。
4.  **消融实验**：
    *   **工具注册表大小**：在“视频标注”任务上，使用Claude 4.5 Sonnet的ReAct智能体，当工具从6个（仅相关）增加到26个（含20个干扰工具）时，TSR从37%降至20.8%，下降16.2个百分点。
    *   **任务复杂度**：在“推荐滥用检测”任务上，从“简单”变体切换到“困难”变体（逻辑更复杂），Claude 4 Opus的TSR保持高位，但FC和ReAct的执行时间分别增加了51.5%和34.2%。

**结论**：实验表明，没有单一的模型-智能体组合能在所有任务上占优，智能体架构的选择需基于SOP结构、工具交互模式和延迟约束。新模型不一定带来更好性能，工具注册表膨胀会成为性能瓶颈，任务特性对整体指标有主导影响。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于当前基准主要基于文本指令，缺乏对多模态信息（如图像、表格）的处理能力，且任务复杂度层级和嵌套结构尚未系统化建模。未来研究可沿以下方向深入：首先，引入可控的复杂度梯度，系统研究任务步骤数、模糊性、工具链长度对智能体性能的影响机制；其次，扩展多模态指令理解，探索视觉-语言模型在工业流程图、仪表盘等场景下的工具调用能力；再者，建模分层SOP与上下文切换机制，模拟现实工作中中断恢复、子流程跳转等动态场景。从方法学角度，可结合课程学习让智能体从简化SOP逐步过渡到复杂任务，并设计因果推理模块以处理异常分支。此外，社区共建机制需建立更严格的质量验证流程，确保新增领域SOP的工业严谨性。

### Q6: 总结一下论文的主要内容

该论文针对当前基于大语言模型的智能体在执行工业领域复杂、多步骤标准操作程序时面临的挑战，提出了一个名为SOP-Bench的新型评测基准。其核心问题是现有基准无法真实反映现实工作流程中的程序复杂性和工具协调需求。

论文的主要贡献是构建了一个包含2000多个任务、覆盖12个商业领域的基准。其方法采用人机协作框架：由人类专家撰写真实的SOP，而AI生成相关工具、API和数据等组件，所有内容均经过人工验证，从而提供了具有可执行接口和真实输出结果的高保真任务。

主要结论和意义在于，SOP-Bench作为一个研究赋能平台，能够系统性地评估不同智能体架构和模型在多样化流程任务上的表现。通过初步实验发现，模型性能并非简单地随版本迭代而提升，且没有单一的模型-智能体组合能在所有领域占优。这证明了在生产部署前进行严格验证的必要性。该基准的价值在于为研究者和从业者提供了一个严谨的框架，以低成本、系统化地研究智能体设计、模型选择和部署策略，而不仅仅是进行模型排名。
