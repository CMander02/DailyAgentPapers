---
title: "Learning to Present: Inverse Specification Rewards for Agentic Slide Generation"
authors:
  - "Karthik Ragunath Ananda Kumar"
  - "Subrahmanyam Arunachalam"
date: "2026-03-17"
arxiv_id: "2603.16839"
arxiv_url: "https://arxiv.org/abs/2603.16839"
pdf_url: "https://arxiv.org/pdf/2603.16839v1"
github_url: "https://github.com/pushing-the-frontier/slide-forge-llm"
categories:
  - "cs.AI"
tags:
  - "Agentic Task"
  - "Tool Use"
  - "Reinforcement Learning"
  - "Reward Design"
  - "Fine-tuning"
  - "Presentation Generation"
  - "Multi-turn Interaction"
  - "Benchmark Dataset"
relevance_score: 7.5
---

# Learning to Present: Inverse Specification Rewards for Agentic Slide Generation

## 原始摘要

Automated presentation generation remains a challenging task requiring coherent content creation, visual design, and audience-aware communication. This work proposes an OpenEnv-compatible reinforcement learning environment where LLM agents learn to research topics, plan content, and generate professional HTML slide presentations through tool use. We introduce a multi-component reward system combining structural validation, render quality assessment, LLM-based aesthetic scoring, content quality metrics, and an inverse specification reward that measures how faithfully generated slides convey their intended purpose. The inverse specification reward, an "inverse task" where an LLM attempts to recover the original specification from generated slides, provides a holistic quality signal. Our approach fine-tunes Qwen2.5-Coder-7B via GRPO, training only 0.5% of parameters on prompts derived from expert demonstrations collected using Claude Opus 4.6. Experiments on 48 diverse business briefs across six models demonstrate that our fine-tuned 7B model achieves 91.2% of Claude Opus 4.6's quality while improving 33.1% over the base model. The six-model comparison reveals that instruction adherence and tool-use compliance, rather than raw parameter count, determine agentic task performance. We contribute SlideRL, an open-source dataset of 288 multi-turn rollout trajectories across all six models: https://huggingface.co/datasets/KarthikRagunathAnandaKumar/sliderl-multi-turn-rollouts Code: https://github.com/pushing-the-frontier/slide-forge-llm

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自动化生成专业演示文稿（幻灯片）这一复杂任务中的核心挑战。研究背景在于，尽管生成式AI取得了进展，但自动创建幻灯片仍是一项综合性难题，因为它不仅需要生成连贯的内容，还涉及主题研究、内容规划、视觉设计以及面向受众的沟通，这些步骤必须在一个多阶段工作流中协调完成。现有基于大语言模型（LLM）的智能体（Agent）虽然在工具使用和多步推理上表现出色，但在处理此类复杂创造性任务时仍面临显著不足：首先，动作空间巨大（需从14种工具中选择并指定参数）；其次，质量评估需要兼顾多个正交标准（如结构、渲染质量、美观度、内容质量等）；再者，任务同时要求事实准确性和视觉吸引力；最后，幻灯片必须遵循连贯的叙事逻辑和时序流程。

本文要解决的核心问题是如何训练一个LLM智能体，使其能够通过序列决策，有效利用工具集，自主完成从研究、规划到生成、细化的整个演示文稿创建流程，并产出高质量、符合规范且美观的幻灯片。为此，论文提出了一个与OpenEnv兼容的强化学习环境，将演示生成构建为顺序决策问题，并引入了一个创新的多组件奖励系统。其中最具特色的是提出了“逆向规范奖励”（Inverse Specification Reward），即通过另一个LLM尝试仅从生成的幻灯片中恢复原始任务规范，以此作为衡量幻灯片整体连贯性和忠实度的综合质量信号。这种方法旨在克服传统评估信号稀疏或片面的问题，为智能体提供密集、全面的训练引导，最终实现在有限参数微调下（仅0.5%），让较小的模型（如7B参数）达到接近顶尖大模型（如Claude Opus 4.6）的生成质量，同时验证了指令遵循和工具使用合规性（而非单纯参数量）是决定智能体任务性能的关键。

### Q2: 有哪些相关研究？

本文的相关工作主要涉及三大类别：方法类、应用类和评测类。

在**方法类**研究中，本文借鉴了LLM智能体使用工具的基础范式。例如，ReAct提出了推理与行动交错的模式，Toolformer展示了通过自监督学习让LLM学会使用工具。本文将这些方法扩展到了演示文稿生成这一需要跨研究、内容创作和设计阶段协调工具使用的复杂任务。在模型优化方面，RLHF开创了利用人类反馈对齐LLM的先河，后续出现了DPO、GRPO等多种奖励建模方法。本文采用了GRPO进行高效微调，并结合了为该任务定制的多组件奖励架构。

在**应用类**研究中，本文针对的是自动化演示文稿生成领域。先前的工作主要集中在基于抽取的幻灯片生成、文档到幻灯片的流水线以及基于学习的内容选择。尽管近期通用LLM系统展现出强大的生成能力，但面向演示文稿的方法通常缺乏用于系统化改进的结构化奖励信号。本文的工作正是通过引入多组件奖励架构来填补这一空白。

在**评测类**研究中，近期研究表明LLM可以作为生成内容的可靠评估者。本文进一步扩展了这一思想，提出了“逆向规范奖励”。该方法通过让一个LLM尝试从生成的幻灯片中恢复原始任务规范（即一个“逆向任务”）来评估整体质量，从而提供了一个综合性的质量信号。这与传统上依赖结构验证、渲染质量评估或基于LLM的美学评分等方法形成了区别与补充。

### Q3: 论文如何解决这个问题？

论文通过构建一个基于强化学习的智能体训练框架来解决自动化演示文稿生成问题，其核心方法、架构设计和关键技术如下：

**整体框架与训练流程**：研究构建了一个符合OpenEnv标准的强化学习环境（SlideRL），将演示文稿生成建模为一个多阶段、多回合的序列决策任务。智能体（基于大语言模型）需要根据任务简报（brief），通过调用一系列工具来逐步完成研究、规划、生成和优化等阶段，最终输出专业的HTML幻灯片。训练流程首先使用Claude Opus 4.6作为专家智能体，在环境中执行任务以收集高质量的专家轨迹（数据集）。随后，采用基于分组相对策略优化（GRPO）的强化学习算法，对基础模型（Qwen2.5-Coder-7B-Instruct）进行微调，仅训练约0.5%的参数（约4000万个）。

**核心方法与主要模块**：
1.  **环境设计**：环境定义了智能体与任务交互的接口。其状态（State）跟踪研究上下文、大纲结构、生成的幻灯片HTML、渲染的PNG图片、工作阶段等关键信息。动作空间（Action Space）包含14个工具，分为研究、内容、设计、结构和元操作五大类（如`web_search`, `create_outline`, `generate_slide`等）。智能体每步以一个JSON对象调用工具，环境返回执行结果、当前状态等观察信息（Observation），并计算即时奖励。
2.  **多组件奖励系统**：这是方法的核心创新之一。为了全面评估演示文稿质量，论文设计了一个包含六个维度的奖励函数，而非单一指标：
    *   **结构验证**：检查幻灯片标题、章节数量、字数等是否符合规范。
    *   **渲染质量**：评估幻灯片创建数量、成功渲染比例及HTML有效性。
    *   **美学评分**：分为HTML结构美学和视觉截图美学，均使用LLM（Claude Opus）作为评判员，从布局、内容平衡、视觉设计、专业度等方面打分。
    *   **内容质量**：评估主题相关性、事实依据（与研究结果的重合度）、内容独特性和叙事连贯性。
    *   **逆向规范奖励**：这是关键的创新点。其核心思想是“逆向任务”：给定生成的幻灯片，让另一个LLM尝试推测出原始的任务简报（包括主题、受众、幻灯片数量、关键主题等）。重建分数（通过比较预测值与真实值）衡量了幻灯片传达其预定目的的忠实度，提供了一个整体性的质量信号。各组件加权求和得到总奖励，并为训练提供了密集的步骤奖励（基于质量变化ΔQ），有效解决了长序列任务中的信用分配问题。
3.  **训练算法与模型适配**：采用GRPO算法进行策略优化。对于每个提示，模型生成多个补全（completion），在环境中执行并获取奖励。优势函数通过组内归一化计算，减少了方差。损失函数采用PPO风格的裁剪替代目标。模型层面，对基础模型采用4-bit量化以降低内存占用，并注入LoRA适配器进行高效微调。适配器被注入到每个Transformer层的注意力（Q, K, V, O）和前馈网络（gate, up, down）的线性投影中，使模型能够学习任务特定的注意力模式和特征表示，而绝大部分预训练参数保持冻结。

**创新点总结**：
1.  **任务形式化与环境构建**：将复杂的演示文稿生成任务系统地分解为可操作的、工具驱动的多阶段强化学习环境。
2.  **逆向规范奖励**：引入“从输出反推输入”的评估机制，创造性地利用LLM的推理能力来评估生成内容的整体一致性和目的忠实度，这是一个新颖的、整体性的质量评估维度。
3.  **密集、多维度奖励塑造**：结合确定性规则与基于LLM的审美评判，构建了全面且可解释的奖励函数，并通过计算质量变化的密集奖励有效指导学习。
4.  **高效的训练策略**：结合专家演示、GRPO算法、LoRA高效微调与量化技术，使得一个7B参数模型能够通过极少量参数更新，在遵循指令和使用工具方面达到接近顶级大模型（Claude Opus）的性能，证明了智能体任务性能的关键在于指令遵循和工具使用合规性，而非单纯的参数量。

### Q4: 论文做了哪些实验？

论文在48个多样化的商业简报上进行了实验，涵盖财务报告、投资者路演、市场分析、技术回顾和战略规划等类型，简报在目标幻灯片数量、受众、置信度和内容类型上均有变化。实验设置上，每个模型在相同的环境和奖励管道中运行，每个简报最多进行35轮交互，最终通过多组件奖励系统计算质量分数并导出演示文稿。评估了六个模型，包括微调后的Qwen2.5-7B（仅训练0.5%参数）、基础Qwen 7B、Claude Opus 4.6、Claude Sonnet 4.6、Llama 4 Scout（109B参数，17B活跃）和GPT OSS 120B。

主要结果如下：微调后的7B模型整体质量得分为0.724，达到Claude Opus 4.6（0.794）的91.2%，较基础模型提升33.1%；完成率从70.8%提升至95.8%。关键指标包括：平均使用轮数22.3，平均创建幻灯片7.0，平均每简报耗时71.6秒。在奖励组件得分上，微调模型在代码规则（0.905）和渲染质量（0.958）上提升显著，但在内容质量（0.783）和规范重建（0.530）上仍落后于顶级模型。模型对比显示，指令遵循和工具使用合规性比参数量更决定任务性能，例如GPT OSS 120B因无法遵循工具调用格式，完成率仅31.2%，质量得分仅0.249。实验还分析了训练数据规模和步数的影响，发现使用48条轨迹训练200步时效果最佳，但更长的训练会导致模式崩溃。

### Q5: 有什么可以进一步探索的点？

该论文在基于强化学习的智能体幻灯片生成方面取得了进展，但其方法仍存在一些局限性和值得深入探索的方向。首先，其多组件奖励系统虽然灵活，但各分量的权重调整依赖于人工经验，未来可探索通过元学习或自适应算法动态优化权重，以更好地适应不同主题和风格的需求。其次，逆规范奖励虽能评估整体一致性，但其有效性高度依赖于用于“逆向任务”的LLM的推理能力，未来可研究如何结合更细粒度的对比学习或知识图谱，提升对内容逻辑连贯性的评估精度。

从方法层面看，论文提到仅使用裁剪机制（clip）在长序列训练中会导致策略崩溃，这表明稳定性是核心挑战。未来可探索更复杂的策略约束方法，如在GRPO中引入分层强化学习，将内容规划、视觉设计等子任务分解，分别进行稳定优化。此外，实验仅基于商业简报，缺乏学术、教育等多样场景的验证，需扩展领域以测试泛化能力。最后，智能体的工具使用合规性虽被强调，但未深入探讨其决策透明度，未来可结合可解释AI技术，使智能体的内容生成和设计选择更易于理解和干预。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种基于强化学习的自动化演示文稿生成方法。核心问题是让AI智能体学习如何根据主题，通过研究、规划并生成专业的HTML幻灯片，这需要协调内容创建、视觉设计和面向受众的沟通。论文的核心贡献是构建了一个与OpenEnv兼容的强化学习环境，并引入了一个创新的多组件奖励系统，其中特别关键的是“逆向规范奖励”。该方法让另一个LLM尝试从生成的幻灯片中反推出原始任务指令，以此作为衡量生成内容是否忠实传达意图的整体质量信号。

在方法上，作者基于专家演示数据，使用GRPO算法对Qwen2.5-Coder-7B模型仅微调了0.5%的参数。实验在48个不同的商业简报上进行，涉及六个模型的比较。主要结论表明，经过微调的7B模型能达到Claude Opus 4.6模型91.2%的质量，并比基础模型提升了33.1%。研究揭示，决定智能体任务性能的关键因素是指令遵循和工具使用合规性，而非模型的参数量本身。论文的意义在于为自动化内容生成提供了一个可学习的智能体框架和评估范式，并开源了名为SlideRL的数据集与代码。
