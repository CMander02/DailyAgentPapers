---
title: "SAMAS: A Spectrum-Guided Multi-Agent System for Achieving Style Fidelity in Literary Translation"
authors:
  - "Jingzhuo Wu"
  - "Jiajun Zhang"
  - "Keyan Jin"
  - "Dehua Ma"
  - "Junbo Wang"
date: "2026-02-23"
arxiv_id: "2602.19840"
arxiv_url: "https://arxiv.org/abs/2602.19840"
pdf_url: "https://arxiv.org/pdf/2602.19840v1"
categories:
  - "cs.CL"
tags:
  - "多智能体系统"
  - "LLM应用"
  - "Agent架构"
  - "翻译"
  - "风格控制"
relevance_score: 7.5
---

# SAMAS: A Spectrum-Guided Multi-Agent System for Achieving Style Fidelity in Literary Translation

## 原始摘要

Modern large language models (LLMs) excel at generating fluent and faithful translations. However, they struggle to preserve an author's unique literary style, often producing semantically correct but generic outputs. This limitation stems from the inability of current single-model and static multi-agent systems to perceive and adapt to stylistic variations. To address this, we introduce the Style-Adaptive Multi-Agent System (SAMAS), a novel framework that treats style preservation as a signal processing task. Specifically, our method quantifies literary style into a Stylistic Feature Spectrum (SFS) using the wavelet packet transform. This SFS serves as a control signal to dynamically assemble a tailored workflow of specialized translation agents based on the source text's structural patterns. Extensive experiments on translation benchmarks show that SAMAS achieves competitive semantic accuracy against strong baselines, primarily by leveraging its statistically significant advantage in style fidelity.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决文学翻译中一个长期存在的核心难题：如何在大语言模型（LLM）时代，不仅保证翻译的语义准确性和语言流畅性，更能忠实保留原作者独特的文学风格。当前先进的LLM和静态多智能体系统虽然能生成通顺、语义正确的译文，但其范式存在固有局限，无法有效感知和适应文本的风格变化，导致译文在风格上趋于平淡、通用，丧失了原作的韵律、节奏和结构复杂性等“文学指纹”。为此，论文提出了SAMAS（风格自适应多智能体系统），将风格保真问题重新定义为信号处理与控制任务。其核心创新在于：1）利用小波包变换将文学风格量化为一个可计算的“风格特征谱”信号；2）基于该信号动态组装定制化的翻译智能体工作流，从而实现了从静态协作到根据输入文本内在风格进行实时自适应处理的范式转变。

### Q2: 有哪些相关研究？

相关工作主要涉及三个方面：1）基于大语言模型的翻译系统，如GPT-4、Gemini 1.5等，它们在语义保真度和流畅性上表现出色，但难以捕捉文学风格；2）多智能体翻译框架，例如TransAgents，通过智能体协作提升翻译质量，但其工作流程通常是静态和角色固定的，缺乏对风格动态适应的能力；3）计算风格学工具，如Briakou等人和Zhang等人的工作，能够识别作者风格标记，但这些特征多用于描述而非作为控制信号。

本文与这些研究的关系是批判性继承与创新。SAMAS承认现有LLM和静态多智能体系统在“信”与“达”上的优势，但指出它们在实现“雅”（风格保真）方面存在根本性局限。为此，本文首次将文学风格量化为可通过小波包变换计算的“风格特征谱”（SFS），并以此作为控制信号，驱动一个动态组装专用翻译智能体工作流程的系统。这突破了静态多智能体系统的范式，将计算风格学的特征从描述性分析转变为实时控制的核心，从而在保持语义准确性的同时，显著提升了风格保真度。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SAMAS的频谱引导多智能体系统来解决文学翻译中的风格保真度问题。其核心方法是将风格保真视为一个信号处理任务，并构建了一个由“风格特征频谱”驱动的动态多智能体框架。

**核心方法与架构设计：**
系统包含两大核心组件。首先是**风格特征频谱**：它将文本风格量化为一个可计算的信号。具体做法是，将文本段基于词长转换为数值序列，以捕捉其节奏和结构复杂性。由于文学风格是非平稳的，论文采用**小波包变换**进行多分辨率分析。从变换系数中，通过提取每个子带的相对小波能量、小波熵以及均值、标准差、偏度和峰度等统计矩，构建出一个81维的SFS向量，作为文本的定量化风格签名。

其次是**SFS驱动的动态多智能体系统**：该系统根据输入的SFS向量，动态组装定制化的翻译工作流。其架构包括一个基于规则的确定性路由机制和一个由六个专业化智能体组成的池。这些智能体分别负责核心语义转换、复杂句法处理、隐喻翻译、情感传递、节奏韵律再现以及整体一致性与风格保真。

**关键技术：**
1.  **基于阈值的动态路由**：系统通过SFS中的关键指标（如小波熵和累积低频能量）来识别文本风格。例如，对于福克纳式（高复杂性、宏观结构主导）风格，当小波熵H>0.85且累积低频能量E_low>0.6时，路由机制会触发一个包含“句法结构”、“隐喻翻译”等智能体的复杂工作流，以解构风格复杂性。对于海明威式（结构简单、节奏短促）风格，则采用更直接的工作流（如“核心翻译”、“节奏韵律”），高效保留简洁节奏。
2.  **可解释的规则驱动**：路由逻辑类似于决策树，将量化的风格特征映射到特定的翻译策略，使系统决策过程具有内在的可解释性。
3.  **专业化智能体协作**：每个智能体都是基础模型的一个实例，由特定角色提示引导，各司其职，通过有序的工作流协同完成既保语义又保风格的翻译任务。

总之，SAMAS的创新在于将风格信号化，并利用该信号动态调度和组合多个专业化智能体，实现了对源文本结构模式的感知与适应，从而在保持语义准确性的同时，显著提升了文学风格的保真度。

### Q4: 论文做了哪些实验？

论文在标准翻译基准和风格化语料上进行了实验。实验设置上，主要对比了单一大语言模型（如Qwen3、GPT-5、Gemini等）和现有的多智能体翻译框架（如HiMATE、MAATS、TransAgents、TACTIC）两类基线。评估使用了两个标准基准：FLORES-200和WMT24，涵盖英语与德语、日语、俄语、乌克兰语、中文之间的双向翻译。主要评估指标是与人类判断相关性高的XCOMET、COMETKIWI-23和MetricX，并辅以ChrF和sacreBLEU。

主要结果显示，SAMAS在两个基准上均显著超越了基线。例如，在FLORES-200英译外文任务上，SAMAS将Qwen3-235B-A22B的XCOMET分数从84.17提升至96.78，超过了顶级多智能体系统TACTIC（96.19）和GPT-5（95.46）。当与GPT-5结合时，SAMAS取得了新的最优结果，其提升在统计上显著。消融实验证明，其动态路由机制优于固定的风格化工作流（如固定模仿福克纳或海明威风格）。此外，人工评估（如图表所示）证实，在风格保真度的直接比较中，SAMAS的译文始终比包括GPT-5在内的五个强基线模型更受人类评估者青睐。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其风格特征谱（SFS）的构建依赖于特定信号处理技术（小波包变换），其普适性和对不同文学体裁、语言对的泛化能力有待验证。未来可探索更细粒度的风格量化方法，或将风格控制信号扩展至更丰富的维度（如情感、节奏）。此外，当前多智能体工作流是动态组装但内部决策逻辑相对固定，未来可引入强化学习让智能体根据实时反馈自我优化翻译策略。另一个方向是将该频谱引导范式应用于其他需要风格保真的生成任务，如创意写作或个性化内容生成，以检验其通用性。

### Q6: 总结一下论文的主要内容

这篇论文针对文学翻译中难以保持作者独特文风的难题，提出了一个创新框架SAMAS（风格自适应多智能体系统）。其核心贡献在于将风格保真度问题重新定义为信号处理任务：首先，利用小波包变换将文学风格量化为一个“风格特征谱”信号；然后，此信号作为动态控制信号，根据源文本的结构模式，实时组装并调度由多个专业化翻译智能体构成的定制化工作流程。实验表明，SAMAS在保持竞争力的语义准确度基础上，在风格保真度上显著超越了强大的单一大语言模型和静态多智能体基线，并获得了人工评估的偏好。该工作的意义在于，通过将风格建模为动态控制信号，为实现复杂文本生成任务从静态范式向风格自适应范式的转变提供了新思路。
