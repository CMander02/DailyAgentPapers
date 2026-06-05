---
title: "Humans' ALMANAC: A Human Collaboration Dataset of Action-Level Mental Model Annotations for Agent Collaboration"
authors:
  - "Jiaju Chen"
  - "Yuxuan Lu"
  - "Jiayi Su"
  - "Chaoran Chen"
  - "Songlin Xiao"
  - "Zheng Zhang"
  - "Yun Wang"
  - "Yunyao Li"
  - "Jian Zhao"
  - "Tongshuang Wu"
  - "Toby Jia-Jun Li"
  - "Dakuo Wang"
  - "Bingsheng Yao"
date: "2026-06-04"
arxiv_id: "2606.06388"
arxiv_url: "https://arxiv.org/abs/2606.06388"
pdf_url: "https://arxiv.org/pdf/2606.06388v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Human-Agent Collaboration"
  - "Mental Model"
  - "Collaboration Dataset"
  - "LLM Benchmark"
  - "Action-Level Annotation"
relevance_score: 8.0
---

# Humans' ALMANAC: A Human Collaboration Dataset of Action-Level Mental Model Annotations for Agent Collaboration

## 原始摘要

Recent advances in LLM agents have enabled complex cognitive capabilities, such as multi-step reasoning, planning, and tool use, that increasingly position these agents as human collaborators. Effective collaboration, however, requires collaborators to continuously maintain and align mental models of their own reasoning,partners' intentions, and shared goals during the collaborative process. Today's agents rarely develop such capabilities since they are primarily optimized for task completion, and the community lacks authentic human collaboration data with action-level mental model annotations that could guide agents toward process-level collaborative competence. To bridge this gap, we present ALMANAC, a dataset of Action-Level Mental model ANnotations for Agent Collaboration built from the Map Task, a classic dyadic routing task from social science. ALMANAC contains 2,987 collaboration actions, each paired with theory-informed mental model annotations that record the participants' self-reasoning, perceived partner intent, and perceived team goal. We benchmark six LLMs on predicting humans' next-turn behavior and mental models. Our results demonstrate ALMANAC's utility in evaluating models' ability to simulate human collaborative behaviors and infer their underlying mental models.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要解决当前大语言模型（LLM）智能体在人类协作中缺乏行动层面心智模型对齐能力的问题。研究背景方面，随着LLM智能体在复杂认知任务上的进步，它们越来越多地被视为人类协作伙伴。然而，现有方法大多将智能体优化为“任务完成者”，专注于工具调用、信息检索等目标导向的指令执行，忽视了协作过程中持续维护和同步心智模型（包括自我推理、感知伙伴意图和共享团队目标）的关键能力。现有基准如ToolBench、WebArena等仅评估任务完成度，而非协作过程的认知层面。此外，已有的人类协作数据集（如对话记录）仅捕捉了可观察的行为内容，缺乏理论驱动的行动级心智模型标注。因此，本文的核心问题是：如何构建一个包含行动级心智模型标注的真实人类协作数据集，以引导智能体学习过程级的协作能力，并评估现有LLM在预测人类协作行为及推断其内在心智模型上的局限性。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三类：

1. **人人协作数据集**（如DealNoDeal、MutualFriends、CaSiNo）：这些数据集基于社会实验，主要关注对话建模，但缺乏对协作伙伴内心模型的标注。本文与此类工作的区别在于，ALMANAC提供了细粒度的动作级心智模型注释（包括自我推理、感知伙伴意图和团队目标），而不仅仅是对话行为。

2. **人机协作基准**：主要评估LLM在与人类交互过程中的语言理解与行为对齐，但同样缺少对伙伴内在推理过程的建模。本文补充了这一空白，通过真实的人类协作数据让代理学习过程级别的协作能力，而非仅优化任务完成。

3. **智能体基准**（如ToolBench、WebArena、τ-Bench、MultiAgentBench、SOTOPIA）：这些基准主要评估智能体的任务解决能力或社会智能，但大多忽略与人类的协调能力。本文强调从“任务导向”转向“过程导向”，关注智能体在协作过程中推断人类意图和心智状态的动态能力，而非仅评估最终结果。

总之，ALMANAC的独特贡献在于提供了唯一具有理论指导的心智模型标注的人人协作数据集，支持对LLM模拟人类协作行为和推理能力的系统评估。

### Q3: 论文如何解决这个问题？

论文通过构建ALMANAC数据集来解决当前AI代理缺乏协作过程中心理模型能力的问题。该数据集基于社会科学中的经典双人路径规划任务（Map Task），收集了2,987个协作动作，每个动作都包含理论驱动的心理模型标注，记录参与者自我推理、感知到的伙伴意图和感知到的团队目标。

在核心方法上，研究设计了三层标注架构：（1）自我推理层，标注参与者自身下一步计划执行的原因；（2）伙伴意图层，标注参与者对搭档当前行动目的的理解；（3）团队目标层，标注参与者对当前共同任务目标的认知状态。数据采集采用受控实验环境，两个参与者通过自然语言交流协作完成迷宫导航任务，同步记录语音交互和行动日志。

关键技术方面，研究团队开发了半自动化标注流程，结合结构化标注模板和人工审核。六种大语言模型（包括GPT-4、Claude等）被用于基准测试，评估模型预测人类下一轮行为和推断心理模型的能力。实验采用两个维度的评估：行为预测准确率和心理模型推断一致性，揭示出现有代理在模拟人类协作过程中的显著局限，特别是在意图归因和共享目标理解方面。

该工作的创新点体现在：首次提供细粒度的心理模型标注数据集（动作级别），区别于传统的任务完成度评估；将社会科学中的协作理论（如共同心智模型）转化为可操作的标注框架；建立评估AI代理过程级协作能力的新基准，使模型训练能从结果优化转向过程理解。

### Q4: 论文做了哪些实验？

论文基于ALMANAC数据集，对6个LLM（Qwen3-35B-A3B、Llama 3.3 70B、GPT-5.5、Claude 4.6 Sonnet、以及微调的Qwen3-4B和Qwen3-30B-A3B）进行了两个任务的基准实验：1）**下一行为预测**：给定行为轨迹历史和角色档案（参与者人口统计和协作档案），预测目标参与者的下一个动作；2）**心智模型预测**：在下一行为预测基础上，进一步给定心智模型历史，预测参与者下一轮的心智状态（包括自推理、感知的伙伴意图和感知的团队目标）。数据集源于Map Task，包含2,987个协作动作，每个动作均有理论指导的心智模型标注。实验对比了两种设置：仅基于角色的LLM（直接提示大型模型）和微调LLM（在训练集上微调小型模型），并测试了是否提供真实心智模型标注（+Mental Model）的效果。主要结果以表格呈现：在动作类型预测中，Guide角色预测完美（Acc=1.00），而Follower角色更困难（GPT-5.5 Acc最高达0.61）；心智模型预测方面，Follower比Guide的预测更准（Claude 4.6 Sonnet在C_visible下Follower团队目标Acc=0.75 vs Guide 0.48），且自推理最难预测。提供心智模型标注通常提升Follower的行为预测性能（如GPT-5.5的Follower动作类型Acc从0.59提升至0.61）。微调后的Qwen3-4B在Follower心智模型预测上表现最强（如Accuracy_Team_Goal达0.88）。评估指标包括准确率、召回率、基于SBERT的语义相似度以及绘画轨迹的加权距离分数。

### Q5: 有什么可以进一步探索的点？

该论文在人类协作建模方面迈出了重要一步，但仍有几个值得深入探索的方向。首先，当前标注依赖于事后回顾，存在记忆偏差风险，未来可引入实时出声思维或生理信号测量来验证标注保真度。其次，数据集规模有限且局限于单一地图任务领域，限制了泛化性，下一步可扩展至编程、写作等更复杂协作场景，并研究模型如何在多领域动态中自适应构建心理模型。当前基准仅测试了少量LLM，未来需纳入更多协作对话数据集训练模型及基于强化学习的对齐方法，以厘清性能差距来源。此外，模型对空间绘图动作的理解不足，建议结合多模态模型联合处理视觉与文本输入。最后，实验揭示了行为预测与心理模型预测间存在角色特异性分离，这提示未来工作需开发能同时优化两方面的联合框架，并探索心理模型注释作为协作过程中灵活监督信号的潜力，从而真正实现具备动态适应能力的协作智能体。

### Q6: 总结一下论文的主要内容

这篇论文提出了一个人类协作数据集ALMANAC，包含从地图任务中收集的2,987个协作动作，每个动作都附带理论驱动的心智模型标注，记录参与者的自我推理、感知的伙伴意图和感知的团队目标。该数据集旨在弥补当前LLM代理缺乏过程级协作能力的问题，这些代理主要优化任务完成，而非持续维护和校准协作过程中的心智模型。方法上，论文通过预测人类下一轮行为和心智模型基准测试了六个LLM。主要结论是，心智模型标注提供了超越交互历史本身的信号，且共享心智模型组件比私有自我推理更容易预测。该数据集通过将代理评估锚定在真实人类协作数据上，为开发作为真正协作伙伴而非单纯任务解决者的LLM代理开辟了道路。
