---
title: "DeepPresenter: Environment-Grounded Reflection for Agentic Presentation Generation"
authors:
  - "Hao Zheng"
  - "Guozhao Mo"
  - "Xinru Yan"
  - "Qianhao Yuan"
  - "Wenkai Zhang"
  - "Xuanang Chen"
  - "Yaojie Lu"
  - "Hongyu Lin"
  - "Xianpei Han"
  - "Le Sun"
date: "2026-02-26"
arxiv_id: "2602.22839"
arxiv_url: "https://arxiv.org/abs/2602.22839"
pdf_url: "https://arxiv.org/pdf/2602.22839v1"
categories:
  - "cs.AI"
tags:
  - "Agent Architecture"
  - "Agentic Planning"
  - "Agentic Reflection"
  - "Tool Use"
  - "Long-Horizon Task"
  - "Environment-Grounded Feedback"
  - "Iterative Refinement"
  - "Presentation Generation"
relevance_score: 9.0
---

# DeepPresenter: Environment-Grounded Reflection for Agentic Presentation Generation

## 原始摘要

Presentation generation requires deep content research, coherent visual design, and iterative refinement based on observation. However, existing presentation agents often rely on predefined workflows and fixed templates. To address this, we present DeepPresenter, an agentic framework that adapts to diverse user intents, enables effective feedback-driven refinement, and generalizes beyond a scripted pipeline. Specifically, DeepPresenter autonomously plans, renders, and revises intermediate slide artifacts to support long-horizon refinement with environmental observations. Furthermore, rather than relying on self-reflection over internal signals (e.g., reasoning traces), our environment-grounded reflection conditions the generation process on perceptual artifact states (e.g., rendered slides), enabling the system to identify and correct presentation-specific issues during execution. Results on the evaluation set covering diverse presentation-generation scenarios show that DeepPresenter achieves state-of-the-art performance, and the fine-tuned 9B model remains highly competitive at substantially lower cost. Our project is available at: https://github.com/icip-cas/PPTAgent

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自动化演示文稿生成任务中现有智能体框架的局限性。研究背景是，演示文稿在教育、商业和科研中是信息传递的主要媒介，但制作高质量演示文稿（需结合深度内容研究和连贯视觉设计）耗时且需要专业技能，因此利用多模态大语言模型（MLLMs）实现自动化成为近期研究方向。然而，现有方法存在明显不足：首先，它们通常依赖预定义的工作流程和与内容无关的固定模板，这限制了其适应不同用户意图的能力，导致生成的幻灯片文字冗长、研究深度不足，且视觉设计与叙述内容脱节；其次，现有方法多基于对内部信号（如代码或推理轨迹）的内省式反思，无法检测渲染后出现的缺陷（如元素重叠、文本截断或布局混乱），因为这些缺陷仅在幻灯片实际渲染完成后才可见。

本文要解决的核心问题是：如何构建一个能够自主规划、渲染并迭代优化演示文稿的智能体框架，使其能灵活适应多样化的用户意图，并通过有效的反馈驱动机制进行长视野的精细化改进，同时克服对固定模板和内省式反思的依赖。为此，论文提出了DeepPresenter框架，其核心创新在于引入了“环境接地的反思”机制：该框架通过协调专门的研究者智能体和演示者智能体，在一个共享的观察空间中运作，使智能体能够基于从环境中观察到的感知工件状态（如已渲染的幻灯片）进行反思和修正，从而识别并纠正仅在实际渲染后才出现的特定缺陷。这解决了传统方法因无法感知最终输出状态而导致的后期缺陷问题，实现了更自主、适应性更强且生成质量更高的演示文稿自动化生成。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类。在方法层面，早期研究将演示文稿生成视为文档摘要任务，采用基于神经网络或短语的抽取式摘要方法选取关键句子，但受限于预大语言模型（LLM）时代的模型推理能力，难以处理多样化用户意图或生成视觉吸引力的输出。LLM的出现推动了基于智能体（agent）的方法发展，这些方法利用更强的推理和泛化能力，近期工作探索了多智能体协作进行内容提取与布局规划、审美感知生成，以及幻灯片理解与编辑。然而，这些方法通常依赖于预定义的工作流程和固定模板，限制了根据用户意图的自适应调整以及基于环境反馈的迭代优化。  
本文提出的DeepPresenter与上述工作密切相关但存在关键区别：它将演示文稿生成构建为两个专用智能体（研究员与演示者）之间的自主探索与协作过程，而非遵循固定流水线。其核心创新在于引入了环境接地的反思机制，与以往依赖内部信号（如推理轨迹）的自我反思不同，该方法将生成过程条件化于感知到的工件状态（如渲染的幻灯片），使系统能在执行过程中识别并修正演示文稿特有的问题，从而支持基于环境观察的长程优化。这使框架能更好地适应多样用户意图，实现有效的反馈驱动优化，并泛化至非脚本化流程。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为DeepPresenter的双智能体框架来解决演示文稿生成问题，其核心是**环境驱动的反思机制**，使系统能够超越预定义的工作流程和固定模板，实现自主规划、渲染和迭代优化。

**整体框架与主要模块**：DeepPresenter将演示生成建模为一个交互式多步轨迹过程，并分解为两个顺序执行的智能体阶段：
1.  **研究员智能体**：负责内容研究与规划。它根据用户指令自主规划探索策略（而非遵循固定流程），调用工具进行信息检索、材料合成，并创建辅助资源。其探索深度和策略会适应用户意图（例如技术演示需调研相关工作，大众演讲则优先考虑易懂示例）。最终，它将幻灯片文本和相关资源编译成按叙事流组织的结构化Markdown文稿，并持久化到文件系统中。
2.  **演示者智能体**：负责视觉设计与生成。它并非填充预定义模板，而是从零开始生成幻灯片。在接收到研究员生成的文稿后，它首先制定全局设计计划（如确立与主题相符的色彩和排版），然后将文稿内容转化为遵循该计划的视觉元素，为每张幻灯片生成独立的HTML文件。这种内容驱动的方法使得风格选择能与主题对齐。

**关键技术：环境驱动的反思**：这是核心创新点。传统基于内部信号（如推理轨迹）的“自我反思”存在状态不匹配问题：智能体操作的是中间表示（如HTML），而用户感知的是渲染后的成品，许多缺陷（如图像破损、内容溢出、对比度低）仅在感知状态中显现。为解决此问题，DeepPresenter引入了**环境驱动的反思机制**：
*   **观察接口**：通过引入 `inspect` 工具作为明确的观察接口，使感知到的工件状态对智能体可见。对于演示者，`inspect` 将HTML文件渲染为图像像素，暴露渲染后的缺陷；对于研究员，它返回文稿和文件状态的结构化诊断信息。
*   **反思-修正循环**：智能体利用 `think` 工具对观察到的缺陷进行反思，并规划有针对性的编辑。这形成了一个**观察-反思-修订**的闭环，使得智能体的观察空间与用户的感知空间保持一致，从而能够识别和修正演示文稿特有的执行期问题。

**创新点总结**：
1.  **双智能体分工协作架构**：将内容研究（研究员）和视觉设计（演示者）分离为两个专用但共享骨干模型的智能体，实现了角色专业化与高效协作。
2.  **环境驱动的反思机制**：通过 `inspect` 工具将反思过程锚定在环境观察（即渲染后的实际状态）上，而非内部推理痕迹，有效解决了状态不匹配问题，实现了与用户感知对齐的迭代优化。
3.  **自主与适应性**：研究员能根据用户意图自适应规划探索策略，演示者能基于内容从零生成视觉设计，共同摆脱了对预定义工作流和固定模板的依赖。

### Q4: 论文做了哪些实验？

论文的实验设置主要包括：使用Gemini-3-Pro作为主干和评判模型，在1024个训练任务上采样轨迹，并筛选出802条高质量轨迹用于监督微调。微调对象是GLM-4.6V-Flash模型，采用MS-SWIFT工具，批大小为32，学习率为1e-5，训练5个epoch，耗时约80 GPU小时（使用8块A800 GPU）。

评估在128个保留任务上进行，对比方法包括商业系统Gamma以及学术框架PPTagent和KCTV。评估指标涵盖：约束分数（基于规则检查用户对幻灯片数量、语言和纵横比的指定要求）、内容与风格质量（采用基于GPT-5的MLLM评估框架）、多样性（使用Vendi Score衡量视觉风格差异）。主要结果以平均分（约束、内容、风格的平均值，范围0-5）和多样性分数（范围0-1）报告。

关键数据指标显示：DeepPresenter在Gemini-3-Pro主干下平均分达4.44，超越最佳开源基线KCTV+Claude-Sonnet-4.5（3.92）13.3%，也高于商业产品Gamma（4.36）。其多样性分数为0.79，显著高于模板化基线的0.17-0.35。微调后的9B模型（DeepPresenter-9B）平均分为4.19，超越所有开源基线，且接近GPT-5（4.22）但成本大幅降低。消融实验证实，环境感知反思、双智能体协作和轨迹过滤均对性能提升至关重要：移除环境感知反思使Gemini-3-Pro分数从4.44降至4.32；移除双智能体协作则大幅下降至4.04；移除轨迹过滤使9B模型从4.19降至4.03。

### Q5: 有什么可以进一步探索的点？

DeepPresenter的局限性主要在于其多步骤、工具调用的推理过程导致成本较高，且对环境不稳定性（如上下文溢出或基础设施故障）敏感。此外，系统仅在轨迹合成阶段使用外部验证，在推理时未引入外部评判器，这可能限制了实时错误检测与修正的能力。

未来研究方向可从以下几点展开：一是优化推理效率，例如通过模型蒸馏或轻量化架构来降低计算开销，或设计更稳定的环境交互机制以减少故障。二是探索在推理阶段集成轻量级外部验证模块，以平衡反思-行动的一致性，同时避免引入过大开销。三是将环境感知的反思机制扩展到更复杂的多模态任务中，如动态视频生成或交互式演示。此外，可以研究如何让系统更好地理解用户隐含意图，实现更个性化的内容生成，从而进一步提升其适应性和实用性。

### Q6: 总结一下论文的主要内容

DeepPresenter 是一个面向演示文稿生成的智能体框架，旨在解决现有演示生成代理依赖预定义工作流和固定模板、缺乏灵活性与迭代优化能力的问题。其核心贡献在于提出了一个环境接地的反思机制，使智能体能够基于对渲染后幻灯片等感知工件的状态观察，自主规划、生成并迭代修订演示内容，从而适应多样化的用户意图，实现长周期的反馈驱动优化。该方法避免了仅依赖内部推理痕迹的自我反思，转而通过环境反馈来识别和修正演示文稿中的具体问题。论文进一步通过外部验证合成的轨迹训练了高效模型，以降低自我验证偏差并强化反思行为。实验结果表明，DeepPresenter 在多种演示生成场景中取得了最先进的性能，同时其微调的 9B 参数模型在显著降低成本的情况下仍保持高度竞争力，为智能体在复杂内容创作任务中的应用提供了有效范例。
