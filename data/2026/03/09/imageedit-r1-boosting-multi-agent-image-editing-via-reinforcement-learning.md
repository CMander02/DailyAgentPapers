---
title: "ImageEdit-R1: Boosting Multi-Agent Image Editing via Reinforcement Learning"
authors:
  - "Yiran Zhao"
  - "Yaoqi Ye"
  - "Xiang Liu"
  - "Michael Qizhe Shieh"
  - "Trung Bui"
date: "2026-03-09"
arxiv_id: "2603.08059"
arxiv_url: "https://arxiv.org/abs/2603.08059"
pdf_url: "https://arxiv.org/pdf/2603.08059v1"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Multi-Agent"
  - "Image Editing"
  - "Reinforcement Learning"
  - "Vision-Language Models"
  - "Decision-Making"
  - "Agent Collaboration"
  - "Framework"
relevance_score: 7.5
---

# ImageEdit-R1: Boosting Multi-Agent Image Editing via Reinforcement Learning

## 原始摘要

With the rapid advancement of commercial multi-modal models, image editing has garnered significant attention due to its widespread applicability in daily life. Despite impressive progress, existing image editing systems, particularly closed-source or proprietary models, often struggle with complex, indirect, or multi-step user instructions. These limitations hinder their ability to perform nuanced, context-aware edits that align with human intent. In this work, we propose ImageEdit-R1, a multi-agent framework for intelligent image editing that leverages reinforcement learning to coordinate high-level decision-making across a set of specialized, pretrained vision-language and generative agents. Each agent is responsible for distinct capabilities--such as understanding user intent, identifying regions of interest, selecting appropriate editing actions, and synthesizing visual content--while reinforcement learning governs their collaboration to ensure coherent and goal-directed behavior. Unlike existing approaches that rely on monolithic models or hand-crafted pipelines, our method treats image editing as a sequential decision-making problem, enabling dynamic and context-aware editing strategies. Experimental results demonstrate that ImageEdit-R1 consistently outperforms both individual closed-source diffusion models and alternative multi-agent framework baselines across multiple image editing datasets.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有图像编辑系统在处理复杂、间接或多步骤用户指令时的能力不足问题。随着多模态模型的快速发展，图像编辑在日常生活中的应用日益广泛，但现有系统（尤其是闭源或专有模型）在面对组合性、多轮次或模糊的用户指令时，往往难以生成符合人类意图、具有上下文感知能力的编辑结果。传统方法要么依赖单一的大型模型，其内部决策过程不透明且难以针对复杂指令进行精细控制；要么需要依赖专业软件和人工经验来设计编辑流程，效率低下且不易普及。

针对这些不足，本文提出了ImageEdit-R1，一个基于强化学习的多智能体图像编辑框架。该框架将图像编辑重新定义为序列决策问题，通过多个分工明确的智能体（包括理解用户意图的分解智能体、规划编辑步骤的排序智能体以及执行具体编辑操作的编辑智能体）协同工作，并利用强化学习优化智能体间的协作策略，从而实现对复杂指令的动态、上下文感知的解析与执行。核心创新在于通过结构化分解与序列化规划，将模糊的用户指令转化为可解释、可操作的子任务流，最终提升编辑结果与用户意图的对齐程度、视觉质量及内容保持性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：指令式图像编辑和强化学习在LLMs/VLMs中的应用。

在**指令式图像编辑**方面，早期方法如InstructPix2Pix和InstructEdit基于扩散模型，利用配对指令-图像数据集进行训练，擅长简单编辑，但在处理复杂、多步骤任务时存在局限。近期研究趋势是集成多模态大语言模型（如Qwen2.5-VL、ILLUME+、Intern-VL）以提升指令理解和编辑精度，通用模型（如Gemini、GPT-4o）也展现出强大的图文一致性。同时，高质量数据集（如PSR、RealEdit）为模型训练提供了支持。本文提出的ImageEdit-R1与这些工作不同，它不依赖单一模型或固定流程，而是采用多智能体框架，将编辑任务分解并由不同智能体协同完成，从而更好地处理复杂指令。

在**强化学习应用**方面，RLHF和RLVR等方法被用于对齐大模型输出与人类偏好或优化推理过程。在图像编辑领域，已有工作（如A2-RL）将编辑建模为序列决策问题，而RewardEdit、Instructrl4px等方法则利用多维度奖励模型进行稳定优化。本文与这些研究的核心联系在于同样采用强化学习来优化决策过程，但区别在于，本文的强化学习主要用于协调多个预训练视觉-语言和生成智能体之间的高层协作，以确保整体行为的一致性和目标导向性，而非直接优化单个模型的生成策略。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ImageEdit-R1的多智能体强化学习框架来解决复杂、间接或多步骤图像编辑指令的难题。其核心方法是将图像编辑视为一个序列决策问题，通过多个专业化智能体的协同工作，并利用强化学习优化关键模块的决策能力。

整体框架由三个主要模块组成：分解智能体、排序智能体和编辑智能体。首先，**分解智能体** 作为一个视觉语言模型，接收用户文本请求和原始图像，将模糊的指令结构化分解为三个关键组件：编辑动作、编辑主体和编辑目标。例如，将“把她的外套和头发颜色改成猩红或铜红色”分解为动作“重新着色”、主体“外套、头发”和目标“猩红或铜红色”。这是框架的创新基础，使后续处理具备精确可控性。其次，**排序智能体** 接收分解结果和图像，生成一个有序的子请求序列，例如“将外套重新着色为猩红”、“将头发重新着色为铜红色”，这确保了多步编辑的逻辑性和可执行性。最后，**编辑智能体** 是一个基于扩散模型的图像编辑模型，它按照子请求序列，逐步对图像进行修改，生成最终编辑结果。

该框架的关键技术创新在于引入了**强化学习**来优化分解智能体的性能。具体而言，论文设计了四种奖励信号来指导智能体学习：格式奖励鼓励输出符合预定的XML式标签结构（如<action>、<subject>）；动作、主体和目标奖励则采用F1分数（而非精确匹配）来评估预测组件与真实标注的匹配程度，从而更灵活地衡量精度和召回率。训练时，采用GRPO（生成式强化策略优化）算法在强化学习数据集上更新策略。算法通过旧策略采样多个响应轨迹，计算归一化优势函数，并优化一个包含裁剪比率和KL散度约束的损失函数，以确保策略在提升奖励的同时不偏离参考策略太远。这种强化学习机制使分解智能体能够动态学习更准确、上下文感知的分解策略，从而提升了整个多智能体系统的协作效率和编辑质量。

总之，ImageEdit-R1通过“结构化分解-序列生成-逐步编辑”的模块化架构，结合针对关键分解模块的强化学习优化，实现了对复杂用户指令的动态、上下文感知的编辑，超越了依赖单一模型或手工流程的现有方法。

### Q4: 论文做了哪些实验？

实验设置方面，论文采用Qwen2.5-VL-7B-Instruct作为分解和排序智能体的统一骨干模型，并评估了三种不同的图像编辑骨干模型：FLUX.1-Kontext-dev、Qwen-Image-Edit和Nano Banana。强化学习训练使用基于verl的EasyR1框架，在8块80GB NVIDIA A100 GPU上进行，全局批次大小为32，学习率为1e-6。

使用的数据集/基准测试包括三个：PSR（包含328个测试请求）、RealEdit（从约9.3K样本中随机抽取1,000个）和UltraEdit（从超过400万编辑中抽取1,000个）。评估采用LLM-as-a-judge范式，使用GPT-4o和Gemini-2.5-Flash作为评判模型，根据请求完成度、图像质量和无关部分保留度三个维度打分，总分范围0-10。

对比方法涵盖三类基线：单模型扩散Transformer方法（Step1X-Edit、ILLUME+、ICEdit）、闭源模型（GPT-4o、SeedEdit）以及多智能体框架的两种变体（原始模型、无强化学习的ImageEdit-R1）。

主要结果显示，ImageEdit-R1在所有骨干模型和基准上均带来性能提升。关键数据指标：使用FLUX.1时平均分从7.21提升至8.23（+1.02）；使用Qwen-Image-Edit时从8.39提升至8.85（+0.46）；使用Nano Banana时从8.32提升至8.66（+0.34）。其中，配备Qwen-Image-Edit的ImageEdit-R1取得了最佳平均分8.85，超越了最佳闭源模型GPT-4o的8.47，并显著优于单模型基线（平均分6.33-7.04）。实验还证实强化学习训练至关重要，无RL的版本性能提升有限甚至下降。定性分析进一步展示了该方法在复杂多步编辑任务中生成更连贯、符合指令结果的优势。

### Q5: 有什么可以进一步探索的点？

本文提出的多智能体框架虽在指令分解和协同编辑上取得进展，但仍存在一些局限和可拓展方向。首先，其强化学习训练依赖合成或标注的编辑轨迹数据，在真实开放场景的复杂指令上可能泛化不足，未来可探索基于人类反馈或更高效的环境模拟来降低数据依赖。其次，当前智能体分工相对固定，未来可引入动态角色分配机制，让智能体根据任务上下文自主调整职责，提升应对未知编辑类型的灵活性。此外，框架未深入处理多轮交互编辑，若能结合对话历史进行持续状态跟踪，将更贴合实际应用场景。从技术整合角度看，引入扩散模型的可控生成技术（如ControlNet）作为编辑智能体的底层工具，可能进一步提升局部编辑的精确度。最后，该框架目前主要针对静态图像，未来可探索将其扩展至视频编辑序列，这需要解决时序一致性和计算效率的挑战。

### Q6: 总结一下论文的主要内容

本文提出ImageEdit-R1，一个基于强化学习协调的多智能体图像编辑框架，旨在解决现有系统（尤其是闭源模型）处理复杂、间接或多步骤用户指令时的不足。核心贡献在于将图像编辑定义为序列决策问题，通过三个专门化智能体（分解、排序、编辑）的协作实现动态、上下文感知的编辑策略。方法上，分解智能体利用视觉语言模型解析用户指令和图像，提取结构化编辑表示（动作、主体、目标）；排序智能体将其组织为有序子请求序列；编辑智能体基于扩散模型依次执行编辑。关键创新是采用强化学习（特别是GRPO算法）优化分解智能体的准确性，通过格式、动作、主体和目标奖励提升其输出质量。实验表明，ImageEdit-R1在多个基准数据集（PSR、RealEdit、UltraEdit）上显著优于单一闭源扩散模型和其他多智能体基线，无需修改底层编辑模型即可提升指令对齐、视觉质量和内容保持能力，例如将FLUX.1的平均分数从7.21提升至8.23。该框架为复杂图像编辑提供了可解释、模块化的解决方案，推动了智能编辑系统的发展。
