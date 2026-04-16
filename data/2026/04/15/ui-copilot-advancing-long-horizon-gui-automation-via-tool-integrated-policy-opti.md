---
title: "UI-Copilot: Advancing Long-Horizon GUI Automation via Tool-Integrated Policy Optimization"
authors:
  - "Zhengxi Lu"
  - "Fei Tang"
  - "Guangyi Liu"
  - "Kaitao Song"
  - "Xu Tan"
  - "Jin Ma"
  - "Wenqi Zhang"
  - "Weiming Lu"
  - "Jun Xiao"
  - "Yueting Zhuang"
  - "Yongliang Shen"
date: "2026-04-15"
arxiv_id: "2604.13822"
arxiv_url: "https://arxiv.org/abs/2604.13822"
pdf_url: "https://arxiv.org/pdf/2604.13822v1"
categories:
  - "cs.LG"
tags:
  - "GUI Agent"
  - "Tool Use"
  - "Memory"
  - "Policy Optimization"
  - "Long-Horizon Task"
  - "Multi-Modal Agent"
relevance_score: 8.5
---

# UI-Copilot: Advancing Long-Horizon GUI Automation via Tool-Integrated Policy Optimization

## 原始摘要

MLLM-based GUI agents have demonstrated strong capabilities in complex user interface interaction tasks. However, long-horizon scenarios remain challenging, as these agents are burdened with tasks beyond their intrinsic capabilities, suffering from memory degradation, progress confusion, and math hallucination. To address these challenges, we present UI-Copilot, a collaborative framework where the GUI agent focuses on task execution while a lightweight copilot provides on-demand assistance for memory retrieval and numerical computation. We introduce memory decoupling to separate persistent observations from transient execution context, and train the policy agent to selectively invoke the copilot as Retriever or Calculator based on task demands. To enable effective tool invocation learning, we propose Tool-Integrated Policy Optimization (TIPO), which separately optimizes tool selection through single-turn prediction and task execution through on-policy multi-turn rollouts. Experimental results show that UI-Copilot-7B achieves state-of-the-art performance on challenging MemGUI-Bench, outperforming strong 7B-scale GUI agents such as GUI-Owl-7B and UI-TARS-1.5-7B. Moreover, UI-Copilot-7B delivers a 17.1% absolute improvement on AndroidWorld over the base Qwen model, highlighting UI-Copilot's strong generalization to real-world GUI tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于多模态大语言模型（MLLM）的图形用户界面（GUI）智能体在**长视野、记忆密集型复杂任务**中性能严重下降的核心问题。研究背景是，当前MLLM GUI智能体在短视野任务（通常少于10个交互步骤）上已展现出强大能力，但在需要多步骤、长时间保持记忆和进行复杂推理的实际长视野场景中，其表现急剧恶化。

现有方法主要存在三方面不足，共同导致了性能瓶颈：1. **记忆退化**：过载的上下文导致智能体遗忘或误记早期关键信息；2. **进度混淆**：推理轨迹与行动历史交织，模糊了任务状态，导致冗余操作、子任务执行顺序混乱或过早终止；3. **数学幻觉**：数值推理错误产生，并在后续计算中传播累积。现有解决方案，如多智能体工作流或检索增强方法，也存在明显缺陷：多智能体工作流依赖预定义流程，无论实际是否需要都会调用外部模块，导致推理成本高昂；检索增强方法则过度依赖检索质量，且无法解决进度混淆问题。这些不足的根本原因在于，**智能体被强加了超出其内在能力范围的挑战**，导致其在日益过载的上下文中陷入混乱。

因此，本文要解决的核心问题是：如何设计一个高效框架，使GUI智能体能够**在轻量级上下文中专注于任务执行**，同时将记忆和计算等负担过重的能力解耦，并按需调用，从而在长视野GUI自动化任务中实现稳健、准确的性能。为此，论文提出了UI-Copilot协作框架及其配套的训练算法TIPO。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、应用类和评测类。

在方法类方面，相关工作包括：1）**基于多模态大模型的GUI智能体**，如GUI-Owl-7B和UI-TARS-1.5-7B，它们展示了处理复杂界面交互任务的能力，但本文指出其在长视野任务中面临内在能力不足、记忆衰退和数学幻觉等挑战。2）**策略优化方法**，如受DeepSeek-R1启发而应用于GUI自动化的组相对策略优化（GRPO），但本文强调外部工具调用在GUI智能体训练中尚未被探索。3）**记忆增强机制**，包括多智能体工作流和少样本检索增强生成（RAG），这些方法旨在不微调模型的情况下提升性能，但本文认为其可扩展性有限且部署成本高；另有研究引入历史感知训练机制，但仍难以应对内存密集的长视野任务。

在应用类方面，本文工作与现有GUI自动化研究一脉相承，但通过引入UI-Copilot协作框架，将智能体与轻量级副驾驶（负责记忆检索和数值计算）解耦，实现了任务执行与辅助功能的分离。

在评测类方面，本文在MemGUI-Bench和AndroidWorld等基准上进行了评估，与现有7B规模GUI智能体相比取得了最先进的性能，证明了其方法的有效性和泛化能力。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为UI-Copilot的协作框架来解决长视野GUI自动化中的挑战，其核心是让GUI智能体专注于任务执行，而由一个轻量级的副驾驶（copilot）按需提供记忆检索和数值计算辅助。整体架构采用“策略智能体-副驾驶”双模型设计，并引入了记忆解耦（Memory Decoupling）和工具集成策略优化（Tool-Integrated Policy Optimization, TIPO）两大关键技术。

在框架设计上，策略智能体（基于Qwen2.5VL-7B初始化）负责核心的序列决策，其行动空间包括坐标操作、文本操作和系统操作。副驾驶模型（基于Qwen3-4B）则作为可调用的工具，具体承担两种角色：Retriever（检索器）和Calculator（计算器）。Retriever用于处理需要记忆的复杂任务，它根据存储的历史知识、任务指令和进度摘要，返回文本形式的检索结果；Calculator则处理数值计算，通过生成并执行Python代码来获得结果。两者的调用由策略智能体根据当前任务需求动态决定。

记忆解耦是架构的核心创新之一。传统方法在多轮交互中维护完整的推理内容（包括思考和详细观察），容易导致上下文过载、进度混乱和记忆幻觉。UI-Copilot将持久性观察（详细推理内容）与瞬态执行上下文（对话历史）分离：在对话历史中仅保留简洁的进度摘要（如“已完成子任务A”），而将完整的思考内容（包含规划和具体观察）存储在本地知识库中。这种设计大幅减轻了策略智能体上下文窗口的负担，使其能更专注于当前动作决策，同时保证了详细信息在需要时可被检索利用。

工具集成策略优化（TIPO）是训练方法上的关键创新。为了有效学习工具调用，TIPO将工具选择学习和任务执行学习解耦优化。具体而言，对于需要工具调用的指令（来自专门构建的工具调用数据集），采用单轮预测的方式单独优化工具选择概率；对于需要多步执行的任务指令，则通过在线策略的多轮滚动来优化动作序列生成。在强化学习阶段，分别设计了针对工具调用正确性的规则奖励和针对动作准确性的多因素奖励（包括格式、类型和准确性），并采用PPO风格的优化目标进行训练，同时引入KL散度惩罚以保持策略稳定性。

这种解耦的优化策略，使得智能体既能精准地判断何时调用何种工具，又能流畅地进行长序列的任务执行，从而在减少幻觉、避免进度混乱的同时，显著提升了在复杂跨应用、多步骤GUI任务上的性能。

### Q4: 论文做了哪些实验？

实验设置方面，论文在多个GUI自动化基准上评估了UI-Copilot框架，并采用了提出的工具集成策略优化（TIPO）方法进行训练。模型基于Qwen2.5VL进行微调，并引入了轻量级的副驾驶（Copilot）模块，用于按需提供记忆检索和数值计算支持。

使用的数据集和基准测试包括：1) **MemGUI-Bench**：一个具有挑战性的基准，包含70.3%的记忆密集型和19.5%的数学密集型任务，平均有36个黄金步骤，用于评估长视野、记忆/数学密集型任务。2) **动态交互基准**：包括AndroidWorld和MiniWob++，用于验证多轮性能的改进。3) **静态GUI导航基准**：包括AndroidControl（报告AC-High和AC-Real）和GUI Odyssey，用于评估高级指令下的综合GUI理解能力，报告动作类型匹配准确率（TM）、接地准确率（GR）和步骤成功率（SR）。4) **其他测试集**：如Tool-call-Test（1000个任务）和AC-Real-Test（1536个任务）用于消融研究。

对比方法分为三类：1) **先进的专有模型**，如GPT-4o和Claude；2) **最先进的开源模型**，如AgentCPM-GUI、GUI-Owl、UI-TARS-1.5和UI-Venus等；3) **多智能体工作流**，如Mobile-Agent-E、Mobile-Agent-V2和Agent-S2。

主要结果如下：在最具挑战性的MemGUI-Bench上，UI-Copilot-7B在7B规模模型中实现了最先进的性能，其pass@1准确率达到16.4%，pass@3达到20.3%，显著优于GUI-Owl-7B（最高10.2%）等基线，并与多智能体工作流性能相当。在综合性能评估中，UI-Copilot-7B在多个基准上表现出色：在AC-High上SR达71.8%，在GUI Odyssey上SR达57.2%，在MiniWob++上SR达61.2%，在AndroidWorld上SR达39.1%（使用工具调用），相比基础Qwen模型在AndroidWorld上绝对提升了17.1%。其平均SR（基于AC-Real-TSR、Wob-SR和AW-SR计算）达到38.7%，在对比的7B模型中领先。消融实验表明，其提出的多轮总结（MS）推理策略结合计算器和检索器工具，能取得最佳平均准确率（51.5%）和较少的执行步骤。训练动态分析显示，策略优化约40步后收敛，工具调用频率随训练下降，执行步骤减少，表明学习有效。

### Q5: 有什么可以进一步探索的点？

基于论文信息，可以进一步探索的点包括：首先，工具集的扩展是核心方向。当前框架仅集成了计算器和检索器，但实际GUI任务可能需要网页搜索、图像裁剪、文本解析等多样化工具。未来研究可以设计更通用的工具集成接口，并探索如何让智能体自主学习和调用新工具。其次，框架的泛化能力值得深入。虽然实验在特定基准上表现优异，但面对更复杂的跨平台、跨应用场景时，策略的鲁棒性仍需验证。未来可考虑引入多模态预训练或元学习来提升适应性。此外，工具调用的优化机制也有改进空间。当前的TIPO方法虽然有效，但可能忽略了长期依赖下的工具选择策略；未来可以探索基于强化学习的动态工具调度，或引入人类反馈来细化调用决策。最后，实际部署中的计算效率与延迟问题也需关注，例如如何平衡协程模型的轻量化与功能完整性。

### Q6: 总结一下论文的主要内容

论文针对基于MLLM的GUI智能体在长时程任务中面临的内存退化、进度混淆和数学幻觉等挑战，提出了UI-Copilot协作框架。其核心贡献是将任务执行与辅助功能解耦：主智能体负责执行，而轻量级Copilot按需提供记忆检索和数值计算支持。方法上，论文通过记忆解耦分离持久观察与临时上下文，并训练策略智能体根据需求调用Copilot作为检索器或计算器。为有效学习工具调用，作者提出了工具集成策略优化（TIPO），分别通过单轮预测优化工具选择，以及通过在线多轮推演优化任务执行。实验表明，UI-Copilot-7B在MemGUI-Bench上取得了最先进的性能，显著优于同类7B规模模型，并在AndroidWorld上相比基础模型实现了17.1%的绝对提升，证明了其在真实世界GUI任务中的强大泛化能力。
