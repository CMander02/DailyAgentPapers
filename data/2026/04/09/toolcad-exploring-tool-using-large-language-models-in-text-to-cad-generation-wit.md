---
title: "TOOLCAD: Exploring Tool-Using Large Language Models in Text-to-CAD Generation with Reinforcement Learning"
authors:
  - "Yifei Gong"
  - "Xing Wu"
  - "Wenda Liu"
  - "Kang Tu"
date: "2026-04-09"
arxiv_id: "2604.07960"
arxiv_url: "https://arxiv.org/abs/2604.07960"
pdf_url: "https://arxiv.org/pdf/2604.07960v1"
categories:
  - "cs.CV"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Tool-Using Agent"
  - "Reinforcement Learning"
  - "Text-to-CAD"
  - "Agent Framework"
  - "Chain of Thought"
  - "Agent Training"
relevance_score: 8.0
---

# TOOLCAD: Exploring Tool-Using Large Language Models in Text-to-CAD Generation with Reinforcement Learning

## 原始摘要

Computer-Aided Design (CAD) is an expert-level task that relies on long-horizon reasoning and coherent modeling actions. Large Language Models (LLMs) have shown remarkable advancements in enabling language agents to tackle real-world tasks. Notably, there has been no investigation into how tool-using LLMs optimally interact with CAD engines, hindering the emergence of LLM-based agentic text-to-CAD modeling systems. We propose ToolCAD, a novel agentic CAD framework deploying LLMs as tool-using agents for text-to-CAD generation. Furthermore, we introduce an interactive CAD modeling gym to rollout reasoning and tool-augmented interaction trajectories with the CAD engine, incorporating hybrid feedback and human supervision. Meanwhile, an end-to-end post-training strategy is presented to enable the LLM agent to elicit refined CAD Modeling Chain of Thought (CAD-CoT) and evolve into proficient CAD tool-using agents via online curriculum reinforcement learning. Our findings demonstrate ToolCAD fills the gap in adopting and training open-source LLMs for CAD tool-using agents, enabling them to perform comparably to proprietary models, paving the way for more accessible and robust autonomous text-to-CAD modeling systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何利用大型语言模型（LLM）作为工具使用智能体，实现从自然语言描述到计算机辅助设计（CAD）模型的**全自动生成**这一核心问题。

研究背景在于，CAD是现代工业制造中的关键任务，但传统上高度依赖专家进行耗时的手动几何建模，自动化程度低。虽然现有CAD软件提供了API，且已有研究尝试利用LLM或视觉语言模型（VLM）生成CAD代码来提升效率，但这些方法存在明显不足。现有方法主要局限于基于令牌的预测建模或生成静态的脚本代码，未能让LLM与CAD引擎进行**最优的、交互式的直接交互**。这导致系统缺乏长程推理能力、无法根据建模过程的动态反馈进行调整，并且没有专门针对CAD工具使用的交互环境与评估基准，最终阻碍了真正自主、鲁棒的文本到CAD建模系统的出现。

因此，本文要解决的核心问题可归纳为三点：1）如何增强LLM在CAD任务中的**推理与工具集成能力**；2）如何构建一个提供**混合反馈**的交互式CAD建模环境（或“健身房”），以评估和训练智能体；3）如何通过有效的训练策略（特别是强化学习），将LLM培养成能够熟练使用CAD工具、处理不同复杂度任务的**专业智能体**。论文提出的ToolCAD框架正是为了填补这些空白，探索工具使用型LLM如何通过与CAD引擎的最优交互，实现自主的文本到CAD生成。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：智能CAD建模系统和智能体强化学习。

在智能CAD建模系统方面，现有研究主要分为两个方向。一是基于LLM的参数化CAD序列生成，如Text2CAD、CAD-GPT和CAD-MLLM等方法，它们利用LLM作为辅助模块，直接预测建模命令序列或对齐多模态输入与命令。二是基于LLM的CAD代码生成，如CAD-Assistant、CAD-Llama、CADCodeVerify和Seek-CAD等工作，它们侧重于生成和精炼代码形式的建模指令，常结合工具调用或思维链反馈。与这些方法不同，本文提出的ToolCAD专注于探索基于原始工具调用的LLM智能体如何与CAD引擎进行最优交互，强调通过强化学习训练智能体在交互环境中进行决策和行动，而非直接生成序列或代码。

在智能体强化学习方面，相关研究致力于增强LLM调用外部工具以完成复杂任务的能力。早期工作采用DQN等经典RL算法，后续发展为PPO、AWR等价值基方法以实现稳定优化。近期方法则融入蒙特卡洛树搜索等推理时搜索策略，或使用DPO、GRPO等基于训练的方法来对齐智能体轨迹与人类偏好。本文借鉴了这些思路，但将其具体应用于CAD领域，设计了一个交互式CAD建模环境，并采用在线课程强化学习策略来训练LLM智能体，使其能演化出精细的CAD建模思维链，从而成为熟练的工具使用智能体。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ToolCAD的智能体框架，结合强化学习，来解决大型语言模型（LLM）与CAD引擎交互以完成文本到CAD生成任务的问题。其核心方法是构建一个工具使用型LLM智能体，通过一个交互式CAD建模环境（gym）进行训练和演化，使其能够执行专家级的、长视野的CAD建模任务。

整体框架分为三个主要阶段：1）CAD建模决策：利用思维链（CoT）提示和后续训练，使LLM能够针对复杂指令生成CAD专用的建模思维链（CAD-CoT），以规划和分解任务。2）配备建模工具与环境：智能体根据CAD-CoT，通过自定义的基于模型上下文协议（MCP）的工具与CAD环境交互，执行具体的建模操作。3）反思式自动CAD建模：采用CAD专用的ReAct（推理-行动）范式，结合来自环境的混合反馈，智能体对每次工具调用的结果进行反思和调整，迭代执行直至任务成功或失败。

关键技术包括：**CAD-CoT提示策略**：使用特殊令牌（如<think>、<tool_call>）构建严格的推理引导工具调用格式，确保参数和动作序列的可靠性，减少幻觉。**混合反馈机制**：环境提供两种反馈——来自CAD引擎的**自发反馈**（如几何冲突警告、API错误）和**人工增强反馈**（将工具输出包装为结构化的“成功/失败”标签及文本描述），帮助智能体进行反思和修正。**基于结果的监督奖励模型（ORM）**：使用人工标注的演示数据微调一个LLM作为奖励模型，用于评估整个工具使用轨迹是否成功完成任务，提供轨迹级的二元奖励信号。**在线课程强化学习（RL）**：采用两阶段训练策略。首先使用成功的演示数据进行监督微调（SFT）初始化策略模型。然后，通过**基于部件的CAD课程学习策略**，根据动作序列的平均困惑度逐步增加建模任务中部件单元的数量，以稳定训练并提升泛化能力。在线RL阶段使用GRPO（Group Relative Policy Optimization）等策略进行优化，结合规则奖励（如格式检查奖励）和ORM提供的任务完成奖励，使智能体在复杂任务中自我演化。

创新点在于：首次系统性地探索了工具使用型LLM在文本到CAD生成中的应用；设计了集成了混合反馈和人类监督的交互式CAD建模环境；提出了结合CAD-CoT、ORM和在线课程RL的端到端后训练策略，有效提升了开源LLM在复杂、长视野CAD任务中的工具使用能力和性能。

### Q4: 论文做了哪些实验？

实验在ToolCAD环境中进行，主要使用DeepCAD数据集和Text2CAD的标注。Text2CAD提供了从抽象到专家级（L0-L3）的设计提示，研究选取并预处理了L3专家级标注作为主要的文本到CAD任务指令，因其更符合工业级标准。由于DeepCAD中复杂多部件任务稀缺，研究通过GPT-4o构建了982条离线演示轨迹作为保留任务，用于监督微调（SFT）和离线奖励模型（ORM）训练；其余数据用于在线强化学习（RL）训练，并从保留任务中选取200个测试案例作为整体评估基准。

对比方法包括：前沿专有LLMs（如GPT-4o和Qwen3-235B-A22B）使用提示技术（如Zero-shot-CoT和ReAct）；开源LLMs（如Qwen2.5-7B和Qwen3-8B）的提示基线、SFT和离线RL（优势加权回归，AWR）训练；以及生成CAD序列的主流方法（如Text2CAD、SkexGen和HNC-CAD）。此外，还与先前基于智能体的CAD生成方法（如CAD-Assistant、CAD-Llama等）进行了广泛比较。

主要结果：经过ToolCAD训练后，Qwen2.5-7B-Instruct和Qwen3-8B在平均建模成功率（Avg. SR）上分别达到63.9%和61.8%，超越了所有前沿LLM提示基线。与SFT相比，在线RL阶段带来了约20%的绝对提升。在几何建模质量方面，ToolCAD在无效率（IR）和中值倒角距离（MCD）上表现优异，例如Qwen2.5-7B的IR为1.51，MCD为1.12，显著优于其他基线。在多部件任务中，ToolCAD在工具调用准确率和几何误差（1-IoU）上也优于基于视觉语言模型（VLM）的方法，并在不同复杂度的指令级别草图（Sketch）和拉伸（Extrusion）F1分数上展现出竞争力。消融研究表明，逐步奖励机制和按部件课程学习策略对在线RL的稳定性和性能提升至关重要。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在两方面：一是缺乏视觉引导感知，仅依赖文本提示可能无法充分理解复杂几何需求；二是工具学习能力有限，缺乏自我修正机制、工具库规模不足，且与CAD引擎的交互反馈不够强健。未来研究可探索多模态输入，例如结合草图或3D扫描作为上游引导，使Agent能更直观地理解设计意图。此外，可构建更动态的交互框架，引入实时几何验证和纠错循环，增强Agent对建模过程中错误的识别与调整能力。从强化学习角度，可设计分层课程学习策略，逐步增加建模复杂度，并引入人类专家干预机制以提升训练效率。最终，开发开源、可扩展的CAD工具生态系统，将推动自主文本到CAD系统向更通用、鲁棒的方向发展。

### Q6: 总结一下论文的主要内容

该论文提出了ToolCAD框架，旨在利用大型语言模型（LLM）作为工具使用智能体，实现从文本描述到计算机辅助设计（CAD）模型的自动生成。核心贡献在于填补了工具使用LLM与CAD引擎交互的研究空白，并构建了一个基于强化学习的训练系统，使开源LLM能够胜任复杂的CAD建模任务。

论文首先定义了文本到CAD生成的问题，指出其依赖长程推理和连贯的建模操作，传统方法难以实现自动化。方法上，ToolCAD包含一个交互式CAD建模环境（gym），用于模拟智能体与CAD引擎的交互轨迹，并引入混合反馈和人工监督机制。通过端到端的后训练策略，结合课程强化学习，引导LLM生成精细的CAD建模思维链（CAD-CoT），从而逐步进化为熟练的CAD工具使用智能体。

主要结论表明，ToolCAD有效提升了开源LLM在CAD任务中的泛化能力，使其性能接近专有模型，为构建更易访问和鲁棒的自主文本到CAD建模系统奠定了基础。
