---
title: "Intelligent Co-Design: An Interactive LLM Framework for Interior Spatial Design via Multi-Modal Agents"
authors:
  - "Ren Jian Lim"
  - "Rushi Dai"
date: "2026-03-16"
arxiv_id: "2603.15341"
arxiv_url: "https://arxiv.org/abs/2603.15341"
pdf_url: "https://arxiv.org/pdf/2603.15341v1"
categories:
  - "cs.AI"
  - "cs.HC"
  - "cs.MA"
tags:
  - "多智能体系统"
  - "人机交互"
  - "工具使用"
  - "检索增强生成"
  - "室内设计"
  - "参与式设计"
relevance_score: 8.0
---

# Intelligent Co-Design: An Interactive LLM Framework for Interior Spatial Design via Multi-Modal Agents

## 原始摘要

In architectural interior design, miscommunication frequently arises as clients lack design knowledge, while designers struggle to explain complex spatial relationships, leading to delayed timelines and financial losses. Recent advancements in generative layout tools narrow the gap by automating 3D visualizations. However, prevailing methodologies exhibit limitations: rule-based systems implement hard-coded spatial constraints that restrict participatory engagement, while data-driven models rely on extensive training datasets. Recent large language models (LLMs) bridge this gap by enabling intuitive reasoning about spatial relationships through natural language. This research presents an LLM-based, multimodal, multi-agent framework that dynamically converts natural language descriptions and imagery into 3D designs. Specialized agents (Reference, Spatial, Interactive, Grader), operating via prompt guidelines, collaboratively address core challenges: the agent system enables real-time user interaction for iterative spatial refinement, while Retrieval-Augmented Generation (RAG) reduces data dependency without requiring task-specific model training. This framework accurately interprets spatial intent and generates optimized 3D indoor design, improving productivity, and encouraging nondesigner participation. Evaluations across diverse floor plans and user questionnaires demonstrate effectiveness. An independent LLM evaluator consistently rated participatory layouts higher in user intent alignment, aesthetic coherence, functionality, and circulation. Questionnaire results indicated 77% satisfaction and a clear preference over traditional design software. These findings suggest the framework enhances user-centric communication and fosters more inclusive, effective, and resilient design processes. Project page: https://rsigktyper.github.io/AICodesign/

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决建筑室内设计领域的一个核心痛点：设计师与客户之间的沟通鸿沟。客户通常缺乏专业知识，难以清晰表达设计意图，而设计师也难以用非专业语言解释复杂的空间关系，这导致项目延期和成本超支。现有解决方案存在明显局限：基于规则的系统（如Infinigen Indoors）依赖硬编码的空间约束，限制了用户的个性化参与；而数据驱动模型（如SceneDreamer）则需要大量训练数据，灵活性不足。本文提出，利用大型语言模型（LLM）对空间关系进行直观推理的能力，可以弥合这一鸿沟。因此，论文的核心目标是构建一个基于LLM的多模态、多智能体交互框架，能够将用户的自然语言描述和参考图像动态转化为优化的3D室内设计，从而提升设计效率，并鼓励非专业用户的参与。

### Q2: 有哪些相关研究？

相关研究主要分为三类。第一类是AI在建筑室内设计中的应用，如DiffDesign（文本/草图生成2D室内图像）、Spacify（结合GPT-4与AR进行3D空间体验），但这些工作或局限于2D输出，或需要特定输入（如房间扫描）。第二类是自动化3D场景生成，包括基于学习的Text2NeRF、GraphDreamer（依赖大数据集）和基于规则的Infinigen Indoors（缺乏个性化），以及结合LLM与具身智能体的Holodeck（但需要命令行知识）。第三类是协同设计与智能体系统，早期如ELIZA，近期如“Chain-of-Experts”展示了专业化多智能体的优势，而I-Design则是室内设计领域应用多智能体的先例。本文工作与I-Design类似，但更强调通过交互式智能体实现实时、迭代的用户参与，并集成了RAG来减少数据依赖。论文也参考了关于多智能体系统失败原因的分析（Pan et al. 2025），以设计更稳健的架构。

### Q3: 论文如何解决这个问题？

论文提出了一个由四个专业化智能体组成的多模态、多智能体框架，核心是让非专业用户通过自然语言交互参与设计迭代。框架以Claude 3和LLaVA作为基础模型。1. **参考智能体**：使用多模态LLM（LLaVA）分析用户上传的参考图像，提取家具类型和空间关系，为后续步骤提供上下文。2. **空间智能体**：这是核心，负责根据用户需求、房间信息和参考文本，通过思维链（Chain-of-Thought）管道分三步生成结构化输出：选择家具对象列表、定义对象约束（如靠墙）、制定评分项（用于后续优化）。该智能体集成了检索增强生成（RAG），从一个本地设计规则知识库中检索专家指南，从而无需任务特定训练即可注入领域知识。3. **交互智能体**：将空间智能体生成的复杂技术术语（如对象约束、评分项）翻译成通俗的自然语言，展示给前端用户。用户可接受、拒绝或提供反馈，拒绝则触发空间智能体重新生成，形成实时交互循环。4. **评分智能体**：在“自动模式”下，使用LLaVA将生成的空间规则与参考图像对比进行自动评分（0-100），以模拟用户偏好进行优化。最终，接受的空间规则被输入到Infinigen Indoors的模拟退火优化器中，生成最终的3D场景。整个框架通过精心设计的提示工程模板确保输出的一致性和可解析性。

### Q4: 论文做了哪些实验？

论文通过对比分析和用户调查评估框架的有效性。**对比分析**：在三种不同户型（紧凑客厅、宽敞客厅、微型卧室）上，比较了“交互式”（有用户反馈）和“非交互式”（仅LLM初始推理）两种方法生成的设计。评估采用一个独立的LLM（GPT-4o）作为评判者，根据一个详细评估准则（Rubric），从用户意图对齐、美学一致性、功能性和流通性四个维度对生成的3D场景渲染图进行评分（1-10分）。结果显示，在所有案例中，交互式方法得分均高于非交互式方法，平均分从5.5-6.5提升到6.75-7.75，尤其在用户意图对齐和流通性方面提升显著。这证明了用户参与迭代能有效提升设计质量。**用户调查**：通过网页UI原型对53名参与者进行了问卷调查，涵盖共同创造感、透明度、易用性、协作友好性和反馈响应性等维度。结果显示，77%的参与者对框架的参与式设计特性表示“满意”或“非常满意”，89%认为它有助于他们无需专业术语表达偏好。在工具偏好上，51%的参与者倾向于本框架，42%无强烈偏好或希望结合传统软件，仅8%选择传统设计软件（如SketchUp）。调查还显示，设计师和非设计师（如医疗保健从业者、工程师）均对本框架表示支持。

### Q5: 有什么可以进一步探索的点？

论文指出了几个局限性和未来方向。首先，当前交互主要基于文本，用户反馈希望增加更直观的多模态交互，如草图、情绪板、拖拽操作和实时3D预览，以降低对文本界面的依赖并提升体验。其次，需要增加多语言支持以提升可访问性。第三，优化算法依赖模拟退火，可能难以处理非常规的空间约束，未来可以探索更高效、灵活的布局优化算法。第四，一些设计专业人士希望获得更细粒度的自动化控制，让AI只处理重复性任务，保留更多手动操作空间，这表明需要在自动化与用户控制之间寻求更好平衡。第五，评估规模较小（53名参与者），未来需要在更大、更多样化的用户群体中进行验证。最后，论文提到可将框架扩展到更广泛的建筑场景，如城市规划和建筑设计，这需要进一步的技术适配和评估。

### Q6: 总结一下论文的主要内容

本文提出并验证了一个基于LLM的多模态、多智能体框架，用于实现参与式的室内空间设计。该框架通过四个专业化智能体（参考、空间、交互、评分）的协作，将非专业用户的自然语言描述和参考图像转化为可计算的空间规则，并集成到现有的3D场景生成器（Infinigen Indoors）中产出最终设计。其核心创新在于：1）通过交互式智能体实现实时、迭代的自然语言人机交互，极大降低了参与门槛；2）利用RAG为空间智能体注入领域知识，避免了昂贵的数据训练需求；3）设计了严谨的提示工程模板确保系统输出的稳定性和可解析性。实验表明，该框架生成的设计在用户意图对齐、美学、功能等方面均优于纯LLM生成的结果，用户调查也显示了较高的满意度和接受度。这项工作为将AI智能体系统应用于需要复杂领域知识和高度用户参与的创意领域提供了一个有前景的范例。
