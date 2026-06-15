---
title: "GUITrans2Act: Understanding User Operational Behaviors from Mobile GUI Interactions with Vision-Language Models"
authors:
  - "Yudong Zhang"
  - "Lei Hu"
  - "Daoyang Liu"
  - "Jiawei Liu"
  - "Yangfan Luo"
  - "Zhilin Gao"
  - "Zuojian Wang"
date: "2026-06-11"
arxiv_id: "2606.12817"
arxiv_url: "https://arxiv.org/abs/2606.12817"
pdf_url: "https://arxiv.org/pdf/2606.12817v2"
categories:
  - "cs.AI"
tags:
  - "移动GUI Agent"
  - "操作知识提取"
  - "视觉语言模型"
  - "数据飞轮"
  - "屏幕轨迹理解"
  - "任务自动化"
  - "基准测试"
relevance_score: 8.5
---

# GUITrans2Act: Understanding User Operational Behaviors from Mobile GUI Interactions with Vision-Language Models

## 原始摘要

Understanding the digital world on mobile devices is shifting from static UI perception to dynamic action comprehension. This capability enables models to convert visual state transitions into operational knowledge, defined as short natural-language sentences that describe action types, target UI elements, textual arguments, and execution orders. However, due to the highly diverse and heterogeneous UI designs across applications, existing vision-language models (VLMs) struggle to accurately infer these underlying operations. To bridge this gap, we introduce Teach VLM, a core model designed to translate mobile screen trajectories into step-wise operational knowledge by extracting and analyzing operation-related keyframes from demonstration videos. To address the scarcity of aligned training data, we develop a systematic data flywheel for scalable data acquisition. We further introduce a novel Chinese Mobile Screen Teach Benchmark for fine-grained evaluation. Building upon Teach VLM, we propose the Teach-and-Repeat paradigm, where the generated operational knowledge serves as an interpretable procedural reference to guide downstream screen-based execution agents. Extensive evaluations demonstrate that Teach VLM significantly outperforms strong VLM baselines, achieving state-of-the-art performance in operation semantics prediction. Furthermore, experiments in Android World show that our paradigm yields consistent Task Success Rate improvements for downstream agents. Together, Teach VLM and the Teach-and-Repeat paradigm offer a practical pathway from raw demonstrations to reusable task automation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

论文试图解决的核心问题是：如何让视觉-语言模型（VLM）从移动设备的动态屏幕操作中准确提取出可理解和可复用的操作知识（即描述动作类型、目标UI元素、文本参数和执行顺序的自然语言句子）。现有方法存在明显不足：静态屏幕理解模型仅能描述可见元素，无法解释连接两个屏幕状态的操作；GUI智能体虽然能预测下一动作，但其输出与特定运行时状态绑定，缺乏可解释性；而通用VLM在处理连续屏幕帧时，会受到演示视频中大量与操作无关的视觉噪声（如加载动画、过渡效果）的干扰，且不同应用间UI设计的巨大异构性使得模型难以泛化识别操作语义。因此，现有VLM在从移动屏幕状态变化中推断底层操作时表现不佳。本文旨在通过开发专门的模型和范式，弥合从原始视频演示到可复用任务自动化之间的鸿沟，使模型能够像人类一样，通过观察屏幕状态的变化来“理解”用户执行的操作。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及三个类别。

**多模态大模型**：包括Gemini 1.5、DeepSeek-V3、InternVL 3.5、LLaVA及Qwen-VL系列。本文的Teach VLM基于Qwen3-VL-8B-Instruct构建。区别在于，通用MLLM虽能识别屏幕内容，但未专门训练以恢复连接前后屏幕状态的操作语义。本文聚焦于将屏幕状态转换转化为自然语言的操作描述，并沿动作类型、目标元素和文本参数维度进行分析。

**屏幕交互**：包括AppAgent、SeeClick、OS-ATLAS、UI-TARS等。区别在于，多数方法旨在运行时直接执行动作，需同时感知、推理和恢复。本文则将屏幕转换理解与执行分离：Teach VLM先从演示中提取操作知识，作为可检查、编辑或供下游代理参考的外部过程指南。

**交互经验过程知识**：包括SkillRL、SKILL0等。区别在于，本文工作粒度更细、输入模态不同。这些工作通常为任务族学习可重用模块，而Teach VLM从单一移动屏幕演示中提取逐步操作知识，输入是屏幕状态变化序列，输出是基于前后截图的具体自然语言描述，使知识更可解释、可编辑，并为评估模型理解动作类型等提供了直接监督。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为Teach VLM的核心模型和Teach-and-Repeat范式来解决从移动GUI交互中理解用户操作行为的问题。整体框架包括数据飞轮驱动的模型训练和下游执行代理的指导两个阶段。

核心方法是构建一个数据飞轮，通过迭代过程生成高质量训练数据来微调通用视觉语言模型（Qwen3-VL-8B）成为Teach VLM。数据飞轮包含五个阶段：移动演示收集、操作相关关键帧提取、Teach VLM预标注、自动评估与人工反馈、以及模型重训练。关键技术包括两阶段关键帧提取：首先通过基于规则的脚本基于帧差异分数去除冗余帧，然后利用轻量级LLM过滤掉加载动画等与操作无关的过渡，保留真正由用户操作引起的关键帧对。Teach VLM采用滑动窗口方式输入多张关键帧截图并结合历史操作描述，生成自然语言的操作描述，确保输出步骤与输入关键帧一一对应。训练数据混合了来自Android-In-The-Zoo、GUIOdyssey等公开数据集和自我收集的演示，以增强目标元素关联和屏幕上下文理解。

创新点在于：提出数据飞轮机制实现可扩展的数据获取和模型迭代改进；设计自动评估体系，结合语义评分和基于屏幕接地执行器的接地一致性评分来筛选高质量样本；引入Teach-and-Repeat范式，将生成的解释性操作知识作为程序化参考，指导下游执行代理在动态Android环境中完成任务。实验表明，Teach VLM在操作语义预测上显著优于GPT-4o等强基线模型，并能提升下游代理的任务成功率。

### Q4: 论文做了哪些实验？

论文实验包含两部分：操作知识提取质量和下游任务实用性。实验使用四个数据集/基准：Android-In-The-Zoo（18,643个屏幕-动作对）、GUIOdyssey（8,300个跨应用human-demonstrated episodes）、Android World Benchmark（116个动态任务，含61易/36中/19难任务）和自建的Mobile Screen Teach Benchmark（169条中文任务轨迹，1,250个标注步骤）。对比方法包括GPT-4o、Doubao-Seed-1.8、Doubao-Seed-2.0、Qwen3.5-9B和Qwen3-VL-8B。评估指标：单步操作用动作准确率(AA)、元素匹配准确率(EMA)、参数准确率(ArA)和操作语义准确率(OSA)；多步操作用精确率、召回率、F1和冗余动作率(RAR)；下游任务用任务成功率(SR)。主要结果：单步操作上，Teach VLM在Android-In-The-Zoo上OSA达58.84%（超Doubao-Seed-2.0达16.47%），在GUIOdyssey上达42.99%（超26.44%）。多步操作上，在Android-In-The-Zoo中F1为74.14%，RAR仅25.56%（GPT-4o的RAR达80%以上）；在GUIOdyssey中F1提升至46.48%（最佳基线26.42%）；在Mobile Screen Teach Benchmark中F1为55.27%（超Doubao-Seed-2.0达8.09%）。下游实验中，Teach VLM指导的GPT-4o总体SR从35.77%提升至46.55%，Doubao-Seed-2.0从49.14%提升至80.33%（简单任务）。

### Q5: 有什么可以进一步探索的点？

本工作虽在GUI操作理解上取得了显著进展，但仍存在若干可深入探索的方向。首先，模型依赖关键帧标注，在真实视频场景中固定帧间隔采样导致冗余动作率（RAR）偏高，未来可引入自监督时序分割或注意力机制实现自适应关键帧选取。其次，实验仅聚焦中文和英文应用，对多语言（如阿拉伯语）及复杂布局（如平板或折叠屏）的泛化能力尚待验证，可构建跨设备、跨语言的元学习基准。此外，当前推理仅依赖视觉状态转换，忽略了UI元素的语义属性（如可访问性标签、层级结构），融合UI树结构化信息或将改善目标元素匹配精度。最后，Teach-and-Repeat范式依赖于预定义的执行顺序，面对动态UI变化（如弹窗或加载延迟）缺乏鲁棒性，可设计状态异常检测机制，使执行代理在抽取得知识指导下具备错误恢复与重规划能力。

### Q6: 总结一下论文的主要内容

这篇论文提出了GUITrans2Act框架，旨在从移动设备GUI交互中理解用户的操作行为。核心贡献包括：1) Teach VLM模型，该模型通过提取演示视频中的操作相关关键帧，将屏幕轨迹转化为自然语言的操作知识，描述动作类型、UI目标、参数和执行顺序；2) 数据飞轮机制，通过模型预标注、人工修正和迭代再训练的低成本方式构建大规模训练数据；3) 教学-重复范式，将生成的操作知识作为可解释的程序参考，指导下游执行代理在动态环境中完成任务。实验表明，Teach VLM在操作语义预测上显著优于GPT-4o等强基线模型，在单步和多步操作提取上均达到最优性能，并能将下游代理在Android World任务中的成功率提升7-10%。这项工作从静态UI感知扩展到动态操作理解，为GUI自动化提供了实用路径。
