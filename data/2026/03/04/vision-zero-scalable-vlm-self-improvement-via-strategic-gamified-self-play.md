---
title: "Vision-Zero: Scalable VLM Self-Improvement via Strategic Gamified Self-Play"
authors:
  - "Qinsi Wang"
  - "Bo Liu"
  - "Tianyi Zhou"
  - "Jing Shi"
  - "Yueqian Lin"
date: "2025-09-29"
arxiv_id: "2509.25541"
arxiv_url: "https://arxiv.org/abs/2509.25541"
pdf_url: "https://arxiv.org/pdf/2509.25541v2"
github_url: "https://github.com/wangqinsi1/Vision-Zero"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "Learning & Optimization"
relevance_score: 9.0
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Learning & Optimization"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "Vision-Zero, Iterative Self-Play Policy Optimization (Iterative-SPO)"
  primary_benchmark: "N/A"
---

# Vision-Zero: Scalable VLM Self-Improvement via Strategic Gamified Self-Play

## 原始摘要

Although reinforcement learning (RL) has emerged as a promising approach for improving vision-language models (VLMs) and multimodal large language models (MLLMs), current methods rely heavily on manually curated datasets and costly human verification, which limits scalable self-improvement in multimodal systems. To address this challenge, we propose Vision-Zero, a label-free, domain-agnostic multi-agent self-play framework for self-evolving VLMs through competitive visual games generated from arbitrary image inputs. Specifically, Vision-Zero encompasses three main attributes: (1) Strategic Self-Play Framework: Vision-Zero trains VLMs in "Who Is the Spy"-style games, where the models engage in strategic reasoning and actions across multiple roles. Through interactive gameplay, models autonomously generate their training data without human annotation. (2) Gameplay from Arbitrary Images: Unlike existing gamified frameworks, Vision-Zero can generate games from arbitrary images, thereby enhancing the model's reasoning ability across diverse domains and showing strong generalization to different tasks. We demonstrate this versatility using three distinct types of image datasets: CLEVR-based synthetic scenes, charts, and real-world images. (3) Sustainable Performance Gain: We introduce Iterative Self-Play Policy Optimization (Iterative-SPO), a novel training algorithm that alternates between Self-Play and reinforcement learning with verifiable rewards (RLVR), mitigating the performance plateau often seen in self-play-only training and achieving sustained long-term improvements. Despite using label-free data, Vision-Zero achieves state-of-the-art performance on reasoning, chart question answering, and vision-centric understanding tasks, surpassing other annotation-based methods. Models and code have been released at https://github.com/wangqinsi1/Vision-Zero.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前视觉语言模型（VLM）和多模态大语言模型（MLLM）训练范式存在的根本性可扩展性瓶颈问题。研究背景是，尽管强化学习（RL）已成为改进VLM的有前景的方法，但现有方法（如监督微调、基于人类反馈的强化学习以及依赖可验证奖励的强化学习）严重依赖于人工精心策划的数据集和成本高昂的人工验证。这导致了两个关键瓶颈：一是数据稀缺问题，多模态标注的巨额成本限制了训练数据的规模和多样性；二是知识天花板问题，模型能力从根本上受限于人类生成的监督信号，阻碍了模型发现超越人类专业知识的策略。

现有方法的不足在于，它们无法实现无需人工干预的、可持续的、可扩展的模型自我进化。虽然自博弈（Self-Play）方法在纯语言模型领域已展现出通过竞争性交互减少对人类依赖的潜力，但将其扩展到需要同时处理视觉和语言模态的VLM领域仍面临巨大挑战。一个理想的自博弈环境需要同时满足技能对齐、难度可扩展、环境多样复杂以及无需或仅需低成本外部数据等多个条件，而现有的视觉推理游戏或框架难以同时满足所有这些条件。

因此，本文要解决的核心问题是：如何设计一个无需人工标注、领域无关的自博弈框架，使VLM能够通过自我生成的竞争性视觉游戏实现可持续、可扩展的自我改进。具体而言，论文提出了Vision-Zero框架，通过模拟“谁是卧底”类社交推理游戏，构建一个非对称的视觉推理游戏环境，让模型扮演不同角色（如“平民”和“卧底”）进行战略推理和交互，从而自主生成训练数据。该框架的核心创新在于能够从任意图像生成游戏，并通过提出的迭代自博弈策略优化算法，结合自博弈和带可验证奖励的强化学习，克服纯自博弈训练中常见的性能平台期，实现长期稳定的性能提升。最终目标是建立一个完全无需人类在环的、成本高效的训练范式，突破多模态模型训练的数据和知识天花板。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于人类反馈的强化学习方法、基于自博弈的语言模型训练方法，以及视觉语言模型（VLM）的现有训练范式。

在**基于人类反馈的强化学习（RLHF/RLAIF）方法**方面，相关工作如RLHF和基于可验证奖励的强化学习（RLVR）是当前提升VLM性能的主流方法。然而，这些方法严重依赖人工标注的数据集或精心设计的奖励函数，成本高昂且可扩展性受限。本文提出的Vision-Zero框架旨在完全摆脱对人类标注的依赖，通过自博弈自动生成训练数据，从而解决了数据稀缺和知识天花板问题。

在**基于自博弈的语言模型训练方法**方面，近期研究如SPIRAL和Absolute Zero成功地将自博弈机制引入纯语言模型（LLM）的训练中，通过游戏化设置（如井字棋、扑克）提升模型的推理和策略能力。这些工作证明了自博弈在减少人类干预方面的潜力。本文的Vision-Zero首次将这一范式扩展到**多模态领域**，设计了基于视觉的“谁是卧底”游戏，使VLM能在涉及图像理解和语言交互的复杂策略环境中进行自博弈，这是与纯语言自博弈工作的核心区别。

在**VLM训练范式**方面，传统方法主要依赖于监督微调（SFT）或上述的RL方法，都需要大量标注数据。Vision-Zero提出了一种全新的、**无需标签**的自改进范式。与现有需要特定游戏环境（如数独）的视觉推理游戏不同，Vision-Zero能从任意图像生成游戏，确保了技能的广泛对齐和环境的多样性，满足了可持续、可扩展自我改进的条件。此外，本文提出的Iterative-SPO算法，通过交替进行自博弈和RLVR，克服了纯自博弈训练中常见的性能平台期问题，确保了长期稳定的性能提升，这与单纯的自博弈或单纯的RL方法都形成了区别。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Vision-Zero的多智能体自博弈框架来解决现有方法依赖人工标注和验证、难以实现可扩展自我改进的问题。其核心方法、架构设计和关键技术如下：

**整体框架与主要模块：**
Vision-Zero的框架包含三个核心组件。首先，它构建了一个**战略游戏环境**，灵感来源于“谁是卧底”类社交推理游戏。在该环境中，多名玩家（包括若干“平民”和一个“卧底”）参与游戏。平民获得包含视觉内容的图像，而卧底获得空白图像。游戏分为两个阶段：1) **线索阶段**：玩家根据自身角色和图像（或空白）依次生成描述性线索；2) **决策阶段**：平民分析所有线索和自身图像，投票找出卧底。这个环境迫使模型进行战略推理：卧底需从平民线索推断内容并生成合理线索以隐藏身份，平民需提供准确线索并识别不一致性。

其次，框架支持**无标签且领域无关的数据输入**。它仅需任意图像作为输入（平民用原图，卧底用空白图），无需任何人工标注。论文验证了其泛化性，使用了三类数据：CLEVR合成场景、图表数据和真实世界图像。

第三，为了确保持续的性能提升，论文提出了**迭代自博弈策略优化算法**。该算法交替进行两个阶段的训练：
- **自博弈策略优化（用于线索阶段）**：采用零和奖励设计。卧底的奖励与它收到的票数负相关，平民的奖励则与卧底收到的票数正相关、但与自身收到的怀疑票数负相关。为了缓解角色信息不对称带来的胜率不平衡，引入了**角色优势估计**来校准奖励。优化目标在最大化优势加权对数似然的同时，通过KL散度约束策略更新，防止退化。
- **带可验证奖励的强化学习（用于决策阶段）**：平民的目标是正确投票找出卧底。奖励设计为：投票正确得+1分，回答“不确定”得-0.5分，投票错误得-1分，以此鼓励深思熟虑的推理。应用**组归一化**来消除不同游戏回合的难度差异，并同样使用带KL正则化的优势加权目标进行优化。

**创新点与工作机制：**
关键的创新在于**Iterative-SPO训练机制**。它动态地在两个训练阶段之间切换，以避免纯自博弈容易陷入局部均衡或纯RL方法容易知识饱和的问题。切换逻辑基于一个保留验证集上的性能指标（如决策阶段的平均准确率和“不确定”回答率）的指数移动平均值。当决策准确率过高（表明线索阶段太容易）时，切换到线索阶段训练以增加游戏难度；当准确率过低或“不确定”率过高时，则切换回决策阶段训练。这种交替机制确保了模型能力的持续、稳定提升，克服了自博弈中常见的性能平台期问题。

综上所述，Vision-Zero通过一个战略游戏环境自动生成训练数据，结合创新的交替优化算法，实现了无需人工标注、可扩展的VLM自我进化，并在多项推理和视觉理解任务上达到了先进水平。

### Q4: 论文做了哪些实验？

论文实验设置方面，使用了三个视觉语言模型（Qwen2.5-VL-7B、InternVL3-8B和InternVL3-14B）作为基础模型，并提出了名为迭代自博弈策略优化（Iterative-SPO）的训练算法。该算法交替进行自博弈和基于可验证奖励的强化学习（RLVR），旨在克服纯自博弈训练的性能瓶颈。

实验涉及的数据集和基准测试广泛，覆盖了14项任务，主要分为三大领域：图表理解（包括ChartXiV_RQ、FunctionQA、PaperQA、ReachQA）、视觉中心任务（包括RealWorldQA、MMVP、BLINK、MuirBench）以及基于CLEVR的合成场景推理。实验使用了任意图像（包括合成场景、图表和真实世界图像）来生成自博弈游戏数据。

对比方法包括多个基于人类标注数据通过RLVR后训练的先进模型，如R1-OneVision-7B、MM-Eureka-Qwen-7B、VLAA-Thinker-7B和OpenVLThinker-7B，以及先收集游戏数据再训练的ViGaL方法。此外，还将结果与GPT-4o和Gemini2.0-Flash等专有模型进行了比较。

主要结果显示，尽管Vision-Zero完全使用无标注数据，其在多项任务上达到了最先进的性能。具体关键数据指标如下：在图表理解任务中，基于图表数据训练的VisionZero-Qwen-7B在ChartXiV_RQ上达到45.8分，在FunctionQA上达到85.5分，在PaperQA上达到73.7分，在ReachQA上达到53.4分，均优于或接近其他对比模型。在视觉中心任务中，同一模型在RealWorldQA上达到68.5分，在MMVP上达到79.1分，在BLINK上达到56.8分，在MuirBench上达到59.2分，表现同样出色。实验还表明，该方法具有强大的泛化能力和持续的性能提升，验证了Iterative-SPO算法的有效性。

### Q5: 有什么可以进一步探索的点？

Vision-Zero的框架虽具创新性，但仍存在一些局限性和可进一步探索的方向。首先，其游戏机制依赖于“谁是卧底”式的对抗，这种形式可能无法覆盖所有类型的视觉推理任务，例如需要长序列规划或复杂多步操作的任务。其次，论文实验主要基于特定数据集（如CLEVR、图表等），在更开放、动态的真实世界场景（如视频理解或具身交互）中的泛化能力尚未充分验证。此外，Iterative-SPO算法虽缓解了性能平台期，但训练过程可能仍受限于自我博弈产生的数据质量，存在陷入局部最优的风险。

未来研究可以从以下方面改进：一是设计更多元化的游戏范式，例如引入协作型任务或动态环境模拟，以激发模型更全面的推理能力。二是探索跨模态自我博弈，将文本、音频等多模态信息融入游戏，提升模型对复杂跨模态关联的理解。三是研究更高效的数据筛选机制，例如引入轻量级验证模块或对抗性过滤，以提高自我生成数据的信噪比。最后，可将该框架与模型架构搜索结合，实现游戏策略与模型能力的协同进化，推动更自主、可持续的多模态系统自我进化。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为Vision-Zero的无标签、领域无关的多智能体自我博弈框架，旨在解决当前视觉语言模型（VLM）强化学习方法依赖人工标注数据、难以规模化自我改进的问题。其核心贡献在于通过策略性自我博弈，使模型能够从任意图像中自主生成训练数据并实现持续性能提升。

论文定义的核心问题是：如何在不依赖人工标注和验证的情况下，实现VLM可扩展的自我进化。方法概述包括三个关键部分：首先，设计了一个类似“谁是卧底”的策略性自我博弈框架，模型在其中扮演不同角色进行交互推理，自主生成训练数据；其次，该框架能从任意图像（如合成场景、图表、真实图像）生成游戏，从而增强跨领域推理和泛化能力；最后，提出了迭代自我博弈策略优化算法，交替进行自我博弈和带有可验证奖励的强化学习，以克服性能平台期，实现长期可持续改进。

主要结论表明，尽管完全使用无标签数据，Vision-Zero在多项推理、图表问答和视觉理解任务上达到了最先进的性能，超越了基于人工标注的方法。这证明了通过策略性游戏化自我博弈实现VLM自主、规模化自我改进的可行性和有效性。
