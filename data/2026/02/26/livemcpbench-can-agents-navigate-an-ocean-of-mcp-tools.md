---
title: "LiveMCPBench: Can Agents Navigate an Ocean of MCP Tools?"
authors:
  - "Guozhao Mo"
  - "Wenliang Zhong"
  - "Jiawei Chen"
  - "Qianhao Yuan"
  - "Xuanang Chen"
  - "Yaojie Lu"
  - "Hongyu Lin"
  - "Ben He"
  - "Xianpei Han"
  - "Le Sun"
date: "2025-08-03"
arxiv_id: "2508.01780"
arxiv_url: "https://arxiv.org/abs/2508.01780"
pdf_url: "https://arxiv.org/pdf/2508.01780v2"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent 评测/基准"
  - "工具使用"
  - "多工具组合"
  - "检索"
  - "模型上下文协议"
  - "Agent 架构"
relevance_score: 9.0
---

# LiveMCPBench: Can Agents Navigate an Ocean of MCP Tools?

## 原始摘要

Model Context Protocol (MCP) has become a key infrastructure for connecting LLMs with external tools, scaling to 10,000+ MCP servers with diverse tools. Unfortunately, there is still a large gap between real-world MCP usage and current evaluation: they typically assume single-server settings and directly inject tools into the model's context, bypassing the challenges of large-scale retrieval and multi-tool composition. To bridge this gap, we propose LiveMCPBench, which evaluates 95 real-world daily tasks explicitly constructed to stress diverse tools and scaled multi-server routing. The benchmark includes a ready-to-deploy tool suite of 70 servers with 527 tools, ensuring reproducibility without scattered API configuration. We further introduce an LLM-as-a-Judge evaluation framework that directly verifies task outcomes, handling dynamic data sources and multiple valid solution paths. We benchmark 12 state-of-the-art LLMs and observe a substantial performance gap: while Claude-Sonnet-4 reaches 78.95% task success, most models achieve only 30-50%. Our analysis reveals that the active tool composition strongly correlates with task success, whereas retrieval errors account for nearly half of all failures, highlighting retrieval as the dominant bottleneck. Together, these results provide the first large-scale, reproducible diagnosis of MCP agent capabilities and point towards future research on improving retrieval robustness and encouraging effective tool composition. Our code and data are publicly available at https://icip-cas.github.io/LiveMCPBench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型（LLM）智能体在使用模型上下文协议（MCP）工具时，其评估体系与现实应用场景严重脱节的问题。研究背景是，MCP已成为连接LLM与外部工具的关键基础设施，其生态已扩展到包含上万个服务器和多样化工具，使得有效使用MCP成为衡量智能体能力的重要标准。然而，现有评估方法存在明显不足：传统工具使用基准（如API-Bank、ToolBench）依赖模拟或不稳定的API，任务真实性差；而现有的MCP基准（如MCPBench）规模过小（仅覆盖10个服务器），且通常采用直接将工具描述注入模型上下文的简化设置，完全绕过了在大规模工具集中进行检索以及跨工具组合规划这两个核心挑战。这导致评估无法反映智能体在动态、大规模的真实MCP生态中的实际能力。

因此，本文要解决的核心问题是：如何对智能体在**大规模、多样化MCP生态系统**中的**工具检索**和**多工具组合**能力进行**系统性、可扩展且可复现**的评估。具体而言，论文提出了LiveMCPBench基准，通过构建95个现实日常任务、部署一个包含70个服务器（527个工具）的即用型工具套件，并设计一个基于LLM-as-a-Judge的自动评估框架，来填补上述评估鸿沟，从而首次实现对MCP智能体能力的大规模、可诊断性评估。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：工具使用基准、MCP系统评估以及大规模工具检索与组合方法。

在**工具使用基准**方面，现有工作如API-Bank和τ-bench采用模拟API来保证稳定性；ToolAlpaca和Seal-Tools收集真实API但无法实际调用；ToolBench等尝试集成真实API却受限于接口频繁变更。近期StableToolBench-MirrorAPI使用微调LLM模拟API。这些基准大多以API为中心，存在不稳定或功能局限（如无法操作本地文件）。本文则利用MCP协议构建了稳定、统一且功能全面的真实工具集，克服了上述限制。

在**MCP系统评估**方面，早期工作MCPBench主要对比MCP与传统API工具；MCP-RADAR提出了多维度评估框架；MCPEval实现了细粒度自动查询生成。但这些基准通常仅评估约10个服务器的小规模场景，无法反映真实世界中大规模动态MCP生态的挑战。本文提出的LiveMCPBench首次构建了包含70个服务器、527个工具的大规模可部署工具套件，并设计了基于真实日常任务的评估，填补了这一空白。

在**大规模工具检索与组合**方面，近期研究如RAG-MCP、MCPZero和ScaleMCP开始探索大规模MCP工具检索，但它们通常采用刚性流程，在工具调用和错误恢复上缺乏适应性，且工具集功能多样性有限。本文的基准则强调在动态多服务器环境中进行工具检索与组合，并通过分析揭示了检索错误是主要瓶颈，为未来改进检索鲁棒性和工具组合策略提供了明确方向。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为LiveMCPBench的综合性基准测试系统来解决大规模、动态现实环境中MCP（模型上下文协议）智能体工具检索与组合能力的评估难题。其核心方法围绕一个四部分组成的整体框架展开：多样化的日常任务集、大规模可部署工具集、基于ReACT的智能体以及自动化的LLM-as-a-Judge评估系统。

首先，**核心方法**是创建一个高度仿真且可复现的评估环境。论文没有采用常见的单服务器设定或直接注入工具描述的方式，而是构建了包含95个真实日常任务的基准，这些任务跨越办公、生活、休闲等六大领域，强调动态上下文和长视野的多工具组合需求。同时，配套构建了LiveMCPTool，这是一个包含70个服务器、527个工具的即插即用工具套件，通过Docker封装确保了评估的稳定性和可复现性，避免了分散的API配置问题。

其次，在**架构设计与关键技术**上，系统包含几个关键模块：
1.  **任务构建模块**：采用由提案者和验证者组成的双阶段人工标注流程，确保任务真实、多样且具有组合深度，最终从300个候选任务中筛选出95个高质量任务。
2.  **智能体模块（MCP Copilot Agent）**：作为基线方法，它基于ReACT框架，将工具使用建模为部分可观测马尔可夫决策过程。其行动空间包含三个关键操作：**Route**（从全量工具集中检索top-k候选工具）、**Execute**（调用工具并获取反馈）和**Response**（输出最终结果）。其中，Route操作的检索评分创新性地采用了来自MCP-Zero的联合相似度计算方式（`score = (s_server × s_tool) × max(s_server, s_tool)`），强调服务器与工具描述的联合对齐，并在工具匹配弱时让服务器先验主导，以更好地处理MCP的服务器-工具层次结构。
3.  **评估模块（LiveMCPEval）**：这是关键的创新点。为了解决动态任务和多解路径的评估难题，论文提出了基于LLM的法官评估框架。该框架不依赖固定的工具调用序列作为标准答案，而是通过验证任务是否满足一组关键的“关键点”来直接判断任务成功与否。这些关键点可以是人工标注或LLM自动提取的必须满足的子任务或中间条件，从而使评估能够灵活处理动态数据和多种有效解决方案。

**创新点**主要体现在三个方面：一是构建了首个大规模、可复现、专注于真实日常任务和多服务器路由的MCP基准；二是设计了无需外部API密钥、即插即用的标准化工具套件，解决了依赖碎片化问题；三是引入了基于关键点的LLM-as-a-Judge自动化评估框架，能够稳健地评估动态、演化的任务，为未来改进检索鲁棒性和工具组合效果的研究提供了可扩展的诊断基础。

### Q4: 论文做了哪些实验？

论文构建了LiveMCPBench基准，实验设置旨在评估智能体在真实、大规模多工具环境下的能力。实验使用了包含95个日常任务的基准，这些任务明确设计用于测试多样化工具和跨多服务器的路由能力。基准配套一个可部署的工具套件，包含70个服务器和527个工具，确保了实验的可复现性，无需分散配置API。

评估框架采用LLM-as-a-Judge方法，直接验证任务结果，以处理动态数据源和多种有效解决路径。研究对比了12种前沿大语言模型，包括Claude、GPT、Gemini、DeepSeek和Qwen系列。关键性能指标包括任务成功率、平均对话轮次、使用工具数、工具执行次数、检索调用次数以及消耗的总令牌数。

主要结果显示，模型性能存在显著差距：Claude-Sonnet-4以78.95%的成功率领先，而大多数模型成功率仅在30%-50%之间。具体数据上，Claude-Sonnet-4平均使用2.71个工具，执行5.59次工具调用，进行2.98次检索，消耗607万令牌。分析表明，积极的工具组合与任务成功强相关，而检索错误导致了近一半的失败，凸显检索是主要瓶颈。此外，评估框架的可靠性得到验证，DeepSeek-V3作为评估器时与人工标注的一致性达到78.95%。

### Q5: 有什么可以进一步探索的点？

基于论文分析，未来研究可从以下几个方向深入探索：

1.  **检索系统的根本性改进**：论文明确指出检索错误是主要瓶颈（占失败近一半）。当前基于语义相似度的检索方法在处理复杂、分层的MCP工具结构时存在局限。未来可探索更先进的检索架构，例如结合工具调用图、元数据或使用强化学习来动态优化检索策略，以更好地理解工具之间的功能关联和层次关系。

2.  **智能工具组合与规划**：研究发现主动的工具组合与任务成功强相关，但当前模型在任务分解和规划上仍有不足，易产生查询粒度不匹配等问题。未来可研究更强大的规划模块，使智能体能够根据任务目标动态生成、评估和调整多工具组合的执行计划，而不仅仅是顺序调用。

3.  **评估框架的鲁棒性与成本优化**：论文的LLM-as-Judge框架虽已验证有效性，但仍存在“幻觉性完成”等评估误差。未来需进一步提升评估的鲁棒性，例如通过多模型投票、更细粒度的评估规则或引入可验证的执行轨迹分析。同时，研究需平衡性能与成本，如论文所示，激进的工具探索会显著增加token消耗，未来需设计更高效的探索与利用策略。

4.  **智能体的容错与自适应能力**：错误分析揭示了当前框架在错误处理（如网络超时）和基于反馈调整行为方面的薄弱。未来的智能体应具备更强的鲁棒性，集成重试机制、备选方案探索以及从失败中学习的能力，以应对真实世界动态、不确定的工具环境。

总之，突破方向在于从“检索-调用”的简单范式，转向更集成、更鲁棒、更具备规划与自适应能力的智能体系统架构。

### Q6: 总结一下论文的主要内容

该论文针对当前大语言模型（LLM）与外部工具交互的评估与现实应用存在差距的问题，提出了LiveMCPBench基准。核心贡献在于构建了一个大规模、可复现的评估体系，用于诊断智能体在真实、复杂的多工具环境下的能力。具体而言，它定义了95个需要组合使用多种工具的日常任务，并配套提供了包含70个服务器、527个工具的即用型工具集（LiveMCPTool），避免了分散的API配置问题。

方法上，论文提出了一个基于LLM的自动评估框架（LiveMCPEval），该框架能直接验证任务完成结果，有效处理动态数据源和多种有效解决方案路径的复杂性。研究团队还构建了一个MCP Copilot智能体用于研究工具检索与组合。

主要结论基于对12个前沿LLM的测试得出：性能存在显著差距，最佳模型（Claude-Sonnet-4）任务成功率约为78.95%，而多数模型仅为30-50%。分析表明，有效的工具组合与任务成功强相关，而近一半的失败源于检索错误，这凸显了工具检索是当前最主要的瓶颈。该研究首次对MCP智能体能力进行了大规模、可复现的诊断，为未来提升检索鲁棒性和促进有效工具组合的研究指明了方向。
