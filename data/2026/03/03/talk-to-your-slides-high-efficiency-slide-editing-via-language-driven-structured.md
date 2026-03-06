---
title: "Talk to Your Slides: High-Efficiency Slide Editing via Language-Driven Structured Data Manipulation"
authors:
  - "Kyudan Jung"
  - "Hojun Cho"
  - "Jooyeol Yun"
  - "Soyoung Yang"
  - "Jaehyeok Jang"
  - "Jaegul Choo"
date: "2025-05-16"
arxiv_id: "2505.11604"
arxiv_url: "https://arxiv.org/abs/2505.11604"
pdf_url: "https://arxiv.org/pdf/2505.11604v4"
github_url: "https://github.com/KyuDan1/Talk-to-Your-Slides"
categories:
  - "cs.CL"
tags:
  - "Agent 架构"
  - "工具使用"
  - "多模态 Agent"
  - "Agent 评测/基准"
relevance_score: 7.5
---

# Talk to Your Slides: High-Efficiency Slide Editing via Language-Driven Structured Data Manipulation

## 原始摘要

Editing presentation slides is a frequent yet tedious task, ranging from creative layout design to repetitive text maintenance. While recent GUI-based agents powered by Multimodal LLMs (MLLMs) excel at tasks requiring visual perception, such as spatial layout adjustments, they often incur high computational costs and latency when handling structured, text-centric, or batch processing tasks. In this paper, we propose Talk-to-Your-Slides, a high-efficiency slide editing agent that operates via language-driven structured data manipulation rather than relying on the image modality. By leveraging the underlying object model instead of screen pixels, our approach ensures precise content modification while preserving style fidelity, addressing the limitations of OCR-based visual agents. Our system features a hierarchical architecture that effectively bridges high-level user instructions with low-level execution codes. Experiments demonstrate that for text-centric and formatting tasks, our method enables 34% faster processing, achieves 34% better instruction fidelity, and operates at an 87% lower cost compared to GUI-based baselines. Furthermore, we introduce TSBench, a human-verified benchmark dataset comprising 379 instructions, including a Hard subset designed to evaluate robustness against complex and visually dependent queries. Our code and benchmark are available at https://github.com/KyuDan1/Talk-to-Your-Slides.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决演示文稿幻灯片编辑这一高频但繁琐的任务，尤其是文本内容维护和批量处理等场景下的效率与准确性问题。研究背景在于，尽管基于多模态大模型（MLLMs）的GUI代理在需要视觉感知的空间布局调整等任务上表现出色，但它们在处理以文本为中心或批量编辑任务时，往往因依赖图像模态而带来高计算成本、高延迟以及潜在的文本识别保真度损失。现有方法（如基于OCR的视觉代理）在处理结构化、文本密集型或批量操作时存在明显不足，无法在高效执行的同时确保内容修改的精确性和样式的一致性。

本文要解决的核心问题聚焦于两点：第一，能否设计一种非视觉的、基于结构化数据的代理，在文本为中心的幻灯片编辑任务上，相比视觉方法实现更高的效率和更好的指令保真度；第二，什么样的系统架构能够有效地将复杂的自然语言指令分解为精确的可执行步骤。为此，论文提出了Talk-to-Your-Slides这一高效幻灯片编辑代理，其核心创新在于绕过图像像素，直接利用幻灯片底层对象模型（如XML、VBA对象）进行语言驱动的结构化数据操作。这种方法避免了图像处理的开销，从而在文本编辑和格式调整等任务上实现了更快速、更经济且更准确的修改。同时，论文设计了一个分层架构来衔接高层用户指令与底层执行代码，以可靠地处理复杂指令。此外，为了系统评估此类编辑能力，论文还构建了包含379条指令的人类验证基准TSBench，其中特别包含了一个挑战视觉依赖或模糊查询的Hard子集。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：幻灯片生成、基于GUI的LLM智能体以及代码生成。

在幻灯片生成方面，AutoPresent通过微调LLaMA模型，根据SlidesBench数据集生成调用SlidesLib API的Python代码，但易产生执行错误且不支持细粒度编辑。PPTagent则模拟人工流程，先创建大纲再使用固定模板编辑幻灯片，并包含评估工具PPTEval，擅长生成新幻灯片。本文的研究延伸了这些工作，重点引入了对现有幻灯片的高效编辑能力，显著减少了用户手动操作。

在基于GUI的LLM智能体方面，微软的UFO和UFO2采用双智能体框架，通过观察应用程序截图来操作如Word和PowerPoint等软件，执行点击菜单和文本输入等任务。这类方法依赖图像状态表示和像素级交互，计算成本高，且在复杂编辑任务中可能行为不精确。本文方法则通过直接操作底层对象模型而非屏幕像素，避免了这些局限，实现了更高精度和更低成本。

在代码生成方面，早期研究依赖基于规则的系统或领域特定语言，可扩展性和适应性不足。随着LLMs发展，出现了更灵活、通用的解决方案，近期研究进一步引入中间推理步骤（如通过自然语言规划指导代码生成）来增强代码生成能力，以衔接高层用户意图与底层可执行代码。本文系统借鉴了这一思想，利用代码生成将用户指令转化为幻灯片编辑操作。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Talk-to-Your-Slides的高效幻灯片编辑代理系统来解决基于视觉的GUI代理在处理结构化、文本中心或批量任务时计算成本高、延迟大的问题。其核心方法是摒弃依赖图像模态的屏幕像素操作，转而采用语言驱动的结构化数据操作，直接利用幻灯片底层对象模型进行精确编辑。

整体框架采用分层架构，将高级用户指令与低级执行代码有效桥接。系统主要包含四个关键模块：指令理解模块、文档理解模块、文档编辑模块和代码生成模块。指令理解模块作为高级组件，负责将自然语言指令解析为结构化的可执行计划，明确指定目标幻灯片、元素及相应操作。文档理解模块作为低级组件，通过自定义的基于规则的解析器，从幻灯片中提取全面的结构化信息，包括元数据以及每个对象（如形状、图像、文本框）的细粒度属性，特别是将文本解析到“运行”级别（run-level），以保持连贯文本段的格式一致性，并将输出转换为JSON格式以方便LLM处理。文档编辑模块则根据前两个模块的输出（计划和解析内容），使用LLM修改解析后的结构化数据，生成反映编辑意图的新数据。最后，代码生成模块接收编辑前后的结构化数据以及计划，生成具体的Python代码（例如通过COM协议操作PowerPoint），将更改应用到幻灯片程序中，并集成了自我反思机制以处理执行失败。

该方法的创新点在于：1）模态创新：完全依赖语言模态和结构化数据，避免了基于OCR的视觉代理的局限性，实现了更高的精度和风格保真度。2）架构设计：清晰的高低层分离设计，使系统兼具对用户意图的灵活理解能力和对软件底层的精确操控能力。3）解析粒度：提出在“运行”级别解析文本，实现了对人类编辑幻灯片方式的更忠实模拟，支持精确的样式保持编辑。4）效率优势：通过直接操作对象模型而非渲染像素，在处理文本中心和格式任务时，实现了比GUI基线更快的处理速度、更高的指令忠实度和显著更低的成本。

### Q4: 论文做了哪些实验？

论文实验主要包括与两种基线方法的对比评估。实验设置上，作者提出的Talk-to-Your-Slides系统采用分层架构，其指令理解模块使用Gemini-1.5-flash，文档编辑和代码生成模块使用Gemini-2.5-flash，并配置最多三次重试尝试。同时，还测试了将默认Gemini设置替换为GPT-4.1-mini、Claude 3.5 Haiku和DeepSeek V3等其他模型的效果。

使用的数据集是作者新引入的TSBench基准数据集，包含379条人工验证的指令，其中包含一个用于评估复杂和视觉依赖查询鲁棒性的Hard子集。

对比的基线方法有两种：1) 针对RQ1的GUI-based agent基线（使用UFO2代理操作PowerPoint等应用，并采用Gemini-2.5-flash模型）；2) 针对RQ2的直接代码生成基线（利用文档理解模块提取幻灯片结构化表示，然后提示LLM生成可执行代码）。

评估指标包括性能指标和效率指标。性能指标有：执行成功率（SR）、LLM评判分数（涵盖文本、图像、布局和颜色方面）以及指令遵循度。效率指标包括：单条指令的平均执行时间（秒）、平均输入/输出令牌数以及平均成本（美元）。

主要结果显示：在文本中心和格式化任务上，与GUI-based基线相比，本文方法处理速度提升了34%（执行时间降至基线66%），指令遵循度提高了34%，且成本降低了87%（降至基线13%）。在架构有效性方面，与直接代码生成基线相比，分层架构使执行成功率提升了160%（例如，Gemini-2.5-flash的SR从59.90%提升至96.83%）。跨模型比较中，DeepSeek V3 (0324)在系统中取得了96.84%的SR和0.0014美元的最低平均成本。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其基于代码操作的设计在处理纯感知或模糊美学指令时存在不足，例如“让这页幻灯片看起来更平衡”或“将图片调整到合适大小”。这类任务需要视觉理解能力，而当前方法主要依赖结构化数据，缺乏对视觉布局美学的直接判断。

未来研究方向可围绕构建混合代理系统展开：结合代码驱动的高效结构化操作与视觉语言模型的感知能力。具体改进思路包括：1）开发动态任务路由机制，根据指令类型自动选择代码操作或视觉模型处理；2）引入视觉反馈循环，在代码修改后使用轻量级视觉模型进行美学评估和微调；3）扩展结构化数据表示，纳入更多视觉属性（如色彩协调、视觉权重），使代码操作能更好地处理美学需求。此外，可探索多模态指令理解，将模糊的自然语言指令转化为可执行的结构化操作参数。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为“Talk-to-Your-Slides”的高效幻灯片编辑智能体，旨在解决传统基于图形用户界面（GUI）的多模态大模型（MLLM）代理在编辑幻灯片时存在的计算成本高、延迟大等问题。核心贡献在于摒弃了依赖图像像素的视觉感知方式，转而采用语言驱动的结构化数据操作，直接利用幻灯片底层对象模型进行精确的内容修改和样式保真。

方法上，系统采用分层架构，将高级用户指令分解为层次化的对象操作，并生成低层执行代码与应用程序交互，从而高效处理以文本为中心、格式化或批量处理的任务。论文还引入了TSBench基准数据集，包含379条人工验证的编辑指令，其中包括用于评估复杂视觉依赖查询鲁棒性的“困难”子集。

主要结论显示，该方法在文本中心和格式化任务上，相比基于GUI的基线方法，处理速度提升34%，指令保真度提高34%，且运行成本降低87%，显著证明了其高效性和有效性。
