---
title: "Teach-and-Repeat: Accurately Extracting Operational Knowledge from Mobile Screen Demonstrations to Empower GUI Agents"
authors:
  - "Yudong Zhang"
  - "Lei Hu"
  - "Daoyang Liu"
  - "Jiawei Liu"
  - "Yangfan Luo"
  - "Xingyu Liu"
  - "Zuojian Wang"
  - "Zhilin Gao"
date: "2026-06-11"
arxiv_id: "2606.12817"
arxiv_url: "https://arxiv.org/abs/2606.12817"
pdf_url: "https://arxiv.org/pdf/2606.12817v1"
categories:
  - "cs.AI"
tags:
  - "GUI Agent"
  - "Action Understanding"
  - "Operational Knowledge Extraction"
  - "Mobile Agent"
  - "Data Flywheel"
  - "Benchmark"
  - "Teach-and-Repeat"
  - "Vision-Language Model"
relevance_score: 9.5
---

# Teach-and-Repeat: Accurately Extracting Operational Knowledge from Mobile Screen Demonstrations to Empower GUI Agents

## 原始摘要

Understanding the digital world on mobile devices is shifting from static UI perception to dynamic action comprehension. This capability enables models to convert visual state transitions into operational knowledge, defined as short natural-language sentences that describe action types, target UI elements, textual arguments, and execution orders. However, due to the highly diverse and heterogeneous UI designs across applications, existing vision-language models (VLMs) struggle to accurately infer these underlying operations. To bridge this gap, we introduce Teach VLM, a core model designed to translate mobile screen trajectories into step-wise operational knowledge by extracting and analyzing operation-related keyframes from demonstration videos. To address the scarcity of aligned training data, we develop a systematic data flywheel for scalable data acquisition. We further introduce a novel Chinese Mobile Screen Teach Benchmark for fine-grained evaluation. Building upon Teach VLM, we propose the Teach-and-Repeat paradigm, where the generated operational knowledge serves as an interpretable procedural reference to guide downstream screen-based execution agents. Extensive evaluations demonstrate that Teach VLM significantly outperforms strong VLM baselines, achieving state-of-the-art performance in operation semantics prediction. Furthermore, experiments in Android World show that our paradigm yields consistent Task Success Rate improvements for downstream agents. Together, Teach VLM and the Teach-and-Repeat paradigm offer a practical pathway from raw demonstrations to reusable task automation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决如何准确从手机屏幕演示视频中提取操作知识（operational knowledge）的问题，以赋能GUI智能体。研究背景是，对移动设备的数字世界理解正从静态UI感知转向动态操作理解，需要模型将视觉状态转换转化为描述动作类型、目标UI元素、文本参数和执行顺序的简短自然语言句子。现有方法的不足体现在三个方面：静态屏幕理解模型只关注定位或描述可见元素，无法解释连接两个屏幕状态的操作；GUI智能体虽能预测下一步动作，但其输出与特定运行时状态绑定且缺乏可解释性；而现代视觉语言模型（VLM）在多帧理解上虽有一定能力，却因演示视频中存在大量任务无关的视觉噪声（如加载动画、转场效果），以及移动应用界面设计的多样性和异构性，导致其难以准确识别操作语义。本文要解决的核心问题是，如何构建一个能够直接从移动屏幕帧序列中准确提取操作知识的模型，并利用该知识作为可解释的程序化参考，指导下游执行智能体在不同应用版本和设备状态中稳健地重复执行任务，从而实现“一次教学、可重复执行”的范式。为此，论文提出了Teach VLM核心模型，并设计了数据飞轮机制来解决训练数据稀缺问题。

### Q2: 有哪些相关研究？

相关研究主要分为三大类。第一类是**多模态大语言模型**，如Gemini 1.5、Qwen-VL系列等，它们在视觉感知和指令遵循上表现优异。本文的Teach VLM基于Qwen3-VL-8B-Instruct构建，但区别于这些通用模型，本文聚焦于从屏幕状态转换中精确恢复操作语义（动作类型、目标元素等），而非仅理解静态截图。第二类是**屏幕接地数字交互**，包括ReAct、SeeClick、AppAgent、UI-TARS等，它们侧重于运行时感知、规划和执行动作。本文的“教与复现”范式与之关键区别在于将屏幕转换理解与执行解耦：先提取可解释的操作知识，再作为外部程序性参考指导下游代理，而不是让代理在运行时同时处理感知、推理和恢复。第三类是**从交互经验中提取程序性知识**，如SkillRL、SKILL0等，它们将交互经验抽象为可复用的高层程序。本文的区别在于输入是单一演示的屏幕状态变化序列，输出是细粒度、可编辑的步骤级自然语言描述，更侧重于从前后截图对中精确解析每一步的具体语义。

### Q3: 论文如何解决这个问题？

论文提出一种名为“Teach-and-Repeat”的范式，核心是训练Teach VLM模型，从移动端屏幕演示视频中准确提取操作知识。整体框架包括“教学”和“重复”两个阶段。

在“教学”阶段，通过一个系统化的数据飞轮来迭代构建高质量训练数据，以微调Qwen3-VL-8B基础模型。数据飞轮包含五个阶段：1) 收集移动演示视频；2) 使用两阶段关键帧提取流水线，先基于帧差法去重，再用轻量级LLM过滤掉无关页面加载、动画等，保留与用户操作相关的屏幕过渡帧对；3) 利用历史迭代的Teach VLM模型进行预标注，通过结合关键帧滑动窗口和之前步骤的描述，按顺序推断每一步的自然语言操作描述；4) 自动评估分为语义评估和使用执行器的接地一致性评估，结合两者得分过滤出高置信度样本，低置信度样本则人工修正；5) 将高置信度和修正后的数据合并用于模型更新，完成一轮迭代。该数据飞轮逐步减少人工标注需求，迭代优化模型与语料库。

在“重复”阶段，生成的序列化操作知识作为可解释的流程参考，提供给下游的屏幕执行代理（如Android World中的代理），指导其逐步完成任务，从而提升任务成功率。关键技术要素包括：针对动态UI变化的去重与过滤算法、基于滑动窗口的上下文感知推理、并结合语义和接地一致性的双重评估机制。核心创新点在于提出了一个从原始演示到可复用任务自动化路径的完整闭环，而Teach VLM作为该范式中的核心模型，在操作语义预测任务上达到了最先进的性能。

### Q4: 论文做了哪些实验？

论文在实验设置上以Qwen3-VL-8B-Instruct为基座，使用LoRA微调（rank=8, alpha=32），在8块GPU上以bfloat16精度、有效batch size 32训练3个epoch。评估使用四个数据集/基准：**Android-In-The-Zoo**（18,643条屏幕-动作对）、**GUIOdyssey**（8,300+跨应用episode）、**Android World Benchmark**（116个动态任务）、以及自建的**Mobile Screen Teach Benchmark**（169条中文轨迹，1,250个标注操作步骤）。对比方法包括GPT-4o、Doubao-Seed-1.8/2.0、Qwen3.5-9B和Qwen3-VL-8B。

主要结果分为两部分：1) **操作知识提取质量**：在单步预测中，Teach VLM在Android-In-The-Zoo上OSA达**58.84%**，远超最强基线Doubao-Seed-2.0（42.37%）；在GUIOdyssey上OSA达**42.99%**（对比Doubao-Seed-2.0的16.55%）。多步预测中，Teach VLM在Android-In-The-Zoo上F1达**74.14%**（RAR仅25.56%），对比GPT-4o的F1仅17.84%（RAR 80.85%）；在Mobile Screen Teach Benchmark上F1达**55.27%**。2) **下游效用**：在Android World上，使用Teach VLM知识后，GPT-4o的总体任务成功率从35.77%提升至**46.55%**（+10.78%），Doubao-Seed-2.0从49.14%提升至**63.93%**（+14.79%），Qwen3-VL-8B从23.70%提升至**31.03%**（+7.33%）。消融实验验证了数据飞轮和关键帧选择的有效性。

### Q5: 有什么可以进一步探索的点？

首先，当前工作主要依赖视觉信息提取操作知识，但移动界面中文本和布局结构同样关键。未来可以探索多模态融合，例如将OCR文本与UI树结构显式编码进模型，以提升对模糊或遮挡元素的动作推断能力。其次，数据飞轮虽有效，但生成的训练数据可能仍存在噪声和偏差。可以引入主动学习或人机协同校验机制，在迭代中自动筛选低置信度样本进行人工修正，提高知识提取的鲁棒性。再者，Teach-and-Repeat范式目前主要针对固定UI流程，对动态页面（如列表滚动、弹窗干扰）的泛化能力不足。改进方向包括结合强化学习对操作序列进行在线调整，或设计模块化知识表示，使执行代理能根据实时屏幕状态灵活选择分支路径。此外，跨语言、跨应用场景的迁移能力也值得深挖，比如利用元学习让小样本适应新应用。最后，当前评估基准仅覆盖中文场景，构建多语言、多版本操作系统（如iOS）的垂直领域benchmark，将更有助于验证方法的通用性。

### Q6: 总结一下论文的主要内容

这篇论文提出了Teach-and-Repeat范式，旨在解决移动GUI代理从屏幕演示中准确提取操作知识的问题。其核心挑战在于现有视觉语言模型难以从包含视觉噪声和跨应用差异的屏幕视频中推断出操作语义（包括动作类型、目标UI元素、文本参数和执行顺序）。为此，作者开发了核心模型Teach VLM，通过过滤演示视频中的无关帧并分析操作前后的关键帧，将屏幕状态转换转化为步骤级的自然语言操作知识。为解决训练数据稀缺问题，论文设计了数据飞轮机制，通过“预标注-人工修正-迭代重训练”的闭环低成本构建大规模训练语料。同时，作者提出了新颖的中文手机屏幕教学基准以支持细粒度评估。主要结论表明，Teach VLM在操作语义预测上显著优于强基线模型，达到最优性能；在Android World环境中，其生成的操作知识作为解释性程序参考注入下游执行代理后，能持续提升任务成功率。这项工作的意义在于将动态屏幕理解从静态感知推进到动作语义提取，并提供了从原始演示到可复用任务自动化的实用路径。
