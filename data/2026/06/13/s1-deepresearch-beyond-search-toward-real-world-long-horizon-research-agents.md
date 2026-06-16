---
title: "S1-DeepResearch: Beyond Search, Toward Real-World Long-Horizon Research Agents"
authors:
  - "Yao Dong"
  - "Xinglin Xiao"
  - "Liwei Dong"
  - "Xinlong Jin"
  - "Zhengbo Li"
  - "Heng Zhang"
  - "Duyun Wang"
  - "Nan Xu"
date: "2026-06-13"
arxiv_id: "2606.15367"
arxiv_url: "https://arxiv.org/abs/2606.15367"
pdf_url: "https://arxiv.org/pdf/2606.15367v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.IR"
  - "cs.LG"
tags:
  - "Deep Research Agent"
  - "Long-Horizon Planning"
  - "Knowledge Synthesis"
  - "Agentic Trajectory"
  - "Training Data Synthesis"
  - "Report Generation"
  - "Open-ended Exploration"
  - "Multi-dimensional Verification"
relevance_score: 9.5
---

# S1-DeepResearch: Beyond Search, Toward Real-World Long-Horizon Research Agents

## 原始摘要

Deep research agents aim to solve complex knowledge-intensive tasks through long-horizon planning, evidence gathering, reasoning, and report generation. While recent progress in search agents has demonstrated strong capabilities in information retrieval and answer verification, most existing training datasets remain search-centric, focusing primarily on closed-ended question answering and information localization. As a result, they mainly train information-seeking behavior while providing limited coverage of key deep research capabilities, including evidence integration, knowledge synthesis, planning, file understanding, and structured report generation. In this work, we propose a unified trajectory construction paradigm for deep research agents that combines closed-ended QA and open-ended exploration. The proposed framework consists of graph-grounded task formulation, agentic trajectory rollout, and multi-dimensional trajectory verification, enabling scalable synthesis of high-quality agentic trajectories spanning long-chain complex reasoning, deep research instruction following, report writing, file understanding and generation, and skills usage. Compared with existing search-oriented datasets, our synthesized trajectories place greater emphasis on knowledge synthesis, complex reasoning, and planning. S1-DeepResearch-32B achieves state-of-the-art performance among open-source models of comparable scale across 20 benchmarks spanning five capability dimensions, including complex reasoning, instruction following, report generation, file understanding, and skills usage. On several challenging deep research benchmarks, it approaches the performance of leading proprietary frontier models. These results highlight the importance of jointly modeling information acquisition, knowledge synthesis, and planning-oriented agent behaviors for building effective deep research agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前深度研究型AI代理在复杂知识密集型任务中的瓶颈问题。研究背景是，大语言模型正从静态文本生成转向具身智能体，需要执行长期规划、证据收集、推理和报告生成等复杂操作。然而，现有方法主要受限于“搜索中心”范式，训练数据多聚焦于封闭式问答和信息定位，这使得模型擅长信息检索和答案验证，但在证据整合、知识综合、规划、文件理解和结构化报告生成等深度研究核心能力上覆盖不足。核心问题在于缺乏既具备可扩展性又忠实于真实复杂研究过程的高质量代理轨迹数据。封闭式问答虽易验证但仅覆盖部分过程，而开放式探索更贴近真实需求却难以合成和验证。因此，本文提出一个统一轨迹构建框架，通过结合封闭式问答的可验证性与开放式探索的真实性，可扩展地合成涵盖长链复杂推理、指令遵循、报告撰写、文件理解与生成及技能使用五大能力维度的代理轨迹，最终构建出更强大的深度研究代理模型。

### Q2: 有哪些相关研究？

相关研究可分为两类。第一类是系统级工作，如OpenAI Deep Research、Gemini Deep Research、MindDR、AI-Researcher和AI-Scientist等，它们通过显式的系统编排完成复杂研究任务，组织多步规划、搜索、阅读、分析和报告生成。本文指出这类方法依赖外部模块和工作流编排，模型本身未内化研究能力，且评估如DeepResearch Bench和ResearchRubrics关注最终输出质量而非完整行为轨迹。第二类是模型级工作，如Tongyi-DeepResearch、Step-DeepResearch、MiroThinker、REDSearcher、OpenSeeker等，通过智能体训练将规划、搜索、工具使用和证据整合内化到模型中，主要基于轨迹合成和post-training。本文指出这些工作侧重于封闭式问答和可验证搜索任务，轨迹更接近抽取式搜索，缺少对知识综合、指令遵循、文件理解和技能使用的覆盖。S1-DeepResearch通过统一轨迹构建范式覆盖了封闭式问答和开放式探索，并组织了五个能力维度（长链复杂推理、指令遵循、报告写作、文件理解和技能使用），与现有工作相比更全面地建模了真实深度研究的多种能力。

### Q3: 论文如何解决这个问题？

该论文提出了一种统一的轨迹构建框架S1-DeepResearch，用于训练具备真实世界长期研究能力的智能体。核心方法包含三阶段：第一阶段是图基任务生成与复杂度进化。通过知识图谱提取连接子图作为结构化知识骨架，注入九维约束（如来源、论证、推理、输出格式等）生成开放式研究任务或封闭式QA对。对封闭式任务进行语义驱动查询进化，逐步削弱表面线索与答案的直接关联。通过参数知识过滤和拓扑感知难度估计筛选需多步探索的复杂任务。第二阶段是AgentLoop执行与轨迹精炼。在沙盒环境中让智能体使用九类原子工具（搜索、网页浏览、代码执行、多模态问答等）迭代交互，产生多步轨迹。基于轨迹进行场景特定精炼，如转换为原生多模态查询、文件输入、可执行工件交付，并提升最终交付物质量要求。第三阶段是多维度轨迹验证。设计五个能力维度的专用验证器，检查引文对齐、证据支撑、动作序列合规性等，仅保留满足严格条件的轨迹。该框架创新性地将封闭式QA与开放式探索统一建模，通过图基约束注入确保任务复杂性和可执行性，通过混合种子实体筛选和双路径子图扩展实现广泛知识覆盖，并通过迭代查询进化和多层次难度过滤保证训练数据的高质量。最终训练出的S1-DeepResearch-32B在20个基准测试中达到开源模型最佳性能，并在多个挑战性深度研究基准上接近领先闭源模型。

### Q4: 论文做了哪些实验？

论文主要进行了实验设置、数据集与基准测试、对比方法和结果分析。实验基于S1-DeepResearch-32B模型，在20个基准测试上评估，涵盖五个能力维度：复杂推理（如GPQA、MATH）、指令遵循（如LongBench）、报告生成（如DREAM）、文件理解（如DocVQA）和技能使用（如SWE-bench）。对比方法包括开源模型（如Qwen2.5-32B、DeepSeek-R1-32B）和闭源前沿模型（如GPT-4o、Claude-3.5）。关键指标显示，S1-DeepResearch-32B在复杂推理任务上平均准确率达78.3%（优于Qwen2.5的72.1%），指令遵循F1为82.5%（对比DeepSeek-R1的79.8%），报告生成ROUGE-L为41.2（接近GPT-4o的43.5），文件理解准确率85.6%（对比Claude-3.5的87.2%），技能使用成功率为67.4%（显著高于开源模型平均的45.8%）。在挑战性强的DREAM基准上，模型得分89.7，逼近GPT-4o的92.1，证明了其在长链推理和知识合成上的优势。实验验证了统一轨迹构建范式对提升深度研究智能体综合能力的有效性。

### Q5: 有什么可以进一步探索的点？

**局限性与未来方向**  
当前工作虽在长程研究任务上取得突破，但存在若干可进一步探索的局限。**首先**，轨迹生成依赖预定义图结构（graph-grounded），可能限制开放域探索的灵活性。未来可引入动态知识图谱或实时种子问题扩展机制，使智能体能自主发现并整合未知信息源。**其次**，验证机制仅支持多维一致性检查，缺乏对推理链因果正确性的深层校验。建议结合反事实推理或过程奖励模型（PRM）进行步骤级质量评估，减少虚假相关性带来的报告偏差。**此外**，模型在高度领域化任务（如生物医学文献综述）中可能受限于通用训练数据的覆盖度。可采用渐进式课程学习，先从合成低噪声轨迹过渡到注入领域规则或专家反馈的窄域强化微调，以平衡通用性与专业性。**最后**，当前评估主要针对静态基准，未涉及与环境交互的动态反馈场景（如实时数据源更新）。可构建交互式沙盒环境，要求智能体在迭代搜索中因应新证据自我修正规划，这将是迈向真实世界高级研究助手的关键跃迁。

### Q6: 总结一下论文的主要内容

这篇论文提出了S1-DeepResearch，一个面向深度研究智能体的数据与模型框架。核心贡献在于解决现有训练数据偏重搜索导向（如封闭式问答），而缺乏证据整合、知识综合、规划与报告生成等关键深度研究能力的问题。论文首先定义了问题：深度研究任务需要长程规划、证据收集、复杂推理和可交付报告生成，远超单纯的信息搜索。方法上，提出了一种统一的轨迹构建范式，结合封闭式问答与开放式探索，包含基于图谱的任务构建、智能体轨迹生成和多维验证，从而合成覆盖复杂推理、指令遵循、报告写作、文件理解与技能使用五个维度的15K高质量轨迹。主要结论是，基于此数据训练的S1-DeepResearch-32B模型在20个基准上达到同等规模开源模型最优水平，在多项挑战性任务上接近领先闭源模型。这项工作强调了联合建模信息获取、知识综合与规划行为对构建有效深度研究智能体的重要意义，为领域提供了可扩展的合成数据方案。
