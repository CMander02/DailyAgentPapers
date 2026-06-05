---
title: "ADK Arena: Evaluating Agent Development Kits via LLM-as-a-Developer"
authors:
  - "Jintao Huang"
  - "Xiaomin Li"
  - "Gaurav Mittal"
  - "Yu Hu"
date: "2026-06-04"
arxiv_id: "2606.05548"
arxiv_url: "https://arxiv.org/abs/2606.05548"
pdf_url: "https://arxiv.org/pdf/2606.05548v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Agent评估基准"
  - "多Agent系统"
  - "Agent开发工具"
  - "LLM-as-a-Developer"
  - "SDK比较"
relevance_score: 8.5
---

# ADK Arena: Evaluating Agent Development Kits via LLM-as-a-Developer

## 原始摘要

The rapid proliferation of Agent Development Kits (ADKs), SDK-level frameworks for building LLM-powered autonomous agents, has outpaced any empirical understanding of how framework choice affects agent performance. We propose \textbf{LLM-as-a-Developer}, a methodology that replaces human developers with an LLM coding agent that learns each framework's API from documentation, writes agent code, and iteratively repairs it through a validate-and-feedback loop until tests pass. By holding the developer constant and varying only the framework, generation effort becomes a quantitative proxy for API usability and the resulting agents provide a controlled measure of framework effectiveness. We implement this in \textbf{ADK Arena}, a fully automated pipeline with per-framework Docker isolation, a three-level validation pipeline, and benchmark adapters for SWE-bench, $τ^2$-bench, Terminal-Bench, and MCP-Atlas. Evaluating all 51 popular Python ADK frameworks (204 agent--benchmark pairs), we find that: (1)~generation succeeds for 57\% of runs, and its cost varies 5.6$\times$ across frameworks (\$0.6 to \$3.4 per agent), a quantitative proxy for API complexity, though cost alone does not predict success; (2)~no single framework dominates: the best single-benchmark ADK agents resolve up to 80\% of tasks and can even \emph{beat} general-purpose frontier coding agents at a fraction of the cost, yet the median framework resolves only 32\%; (3)~across information-source ablations, genuine framework usage stays within a narrow 28--40\% band (highest with raw source access and still 33\% with no reference material at all), indicating that documentation, source code, and parametric knowledge are largely substitutable rather than any one being a hard bottleneck.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在2025年LLM驱动智能体领域，众多Agent开发工具包（ADKs）的涌现使得开发者在选择框架时缺乏实证依据的问题。研究背景是，尽管每个主流AI厂商都在18个月内发布了官方ADK框架，加上数十个开源替代品，已经识别出51个流行的Python ADK框架，但开发者无法知道哪个框架能产生最好的智能体，以及需要多少开发成本。现有方法的不足在于：传统的评估需要专家手动为每个框架的API实现基准测试任务，这种O(N×M)的工作量不仅引入了实验者偏差，也无法规模化；开发者调查只能反映开发者对框架的主观看法，而非框架的实际表现；而智能体基准测试比较的是模型，在固定框架的条件下进行。因此，至今没有任何研究尝试在生态系统规模上比较这些框架。本文要解决的核心问题是：如何以可扩展、无偏见的方式，系统性地比较不同ADK框架的API易用性和框架有效性，从而为开发者提供框架选择的实证基础。为此，论文提出了LLM-as-a-Developer方法论，用LLM编码智能体替代人类开发者，通过统一流程评估各个框架。

### Q2: 有哪些相关研究？

相关研究主要分为三类：

第一类是传统框架评测方法，如数据库领域的TPC基准、深度学习框架的MLPerf和Web框架的TechEmpower，这些方法依赖专家手工编写评测代码，适合于成熟且数量较少的框架，但在评估快速演进的ADK生态时存在实验者偏见、扩展性差和缺乏统一性能指标的问题。

第二类是直接相关的评测框架，如MAFBench，它是最接近本文的工作，但仅覆盖7个框架，且采用手工编写的微任务来评估，本文的ADK Arena则通过LLM-as-a-Developer方法实现完全自动化评估，覆盖51个框架和204个agent-基准对，显著提升了可扩展性。

第三类是利用大语言模型能力进行评估的方法，包括LLM-as-a-Judge、LLM驱动的代码生成和测试生成技术。本文延伸了LLM-as-a-Judge思想，将其从替代人工评估者转变为替代人工开发者，通过在固定LLM能力的情况下只改变框架来测量API可用性和框架有效性，类似受控软件工程实验中固定专家水平而改变工具的做法。与纯粹依赖开发者调查或问题挖掘的方法不同，本文通过生成成本、验证失败率等客观可重复指标衡量API复杂性和文档质量。

### Q3: 论文如何解决这个问题？

该论文通过提出LLM-as-a-Developer方法并实现ADK Arena自动化流水线来解决评估不同Agent开发框架（ADK）对性能影响的问题。核心方法是用LLM编码代理替代人类开发者，使其从文档和源码中学习框架API、编写代理代码，并通过验证反馈循环迭代修复直至测试通过，从而在控制开发者能力的前提下量化框架差异。

整体框架由三大模块组成：环境准备模块为51个流行的Python ADK框架构建独立的Docker镜像，每个容器内预装框架包、专属文档和只读源码，所有LLM流量通过本地代理路由。代理生成模块集成了六种开发工具（如explore_docs、search_api），生成循环设有5分钟预算，包含外层生成循环和内层迭代循环。在迭代循环中，代理利用三级别验证流水线进行修复：第一级静态分析（编译检查、引入验证、禁止原生API回退）；第二级真实LLM冒烟测试；第三级真实基准测试任务的部分执行。验证失败时，模式匹配引擎针对70多种已知错误签名给出结构化诊断和修复建议。基准测试模块通过适配器模式统一四个基准（SWE-bench、τ²-bench、Terminal-Bench、MCP-Atlas）的接口，所有任务使用统一的LLM代理进行50次测试。

关键技术包括：全局框架无关的统一LLM代理（通过双向协议转换支持不同提供商API）、结构化修复提示机制、以及通行信息源消融实验。创新点在于首次实现了对51个ADK的全自动标准化评估，发现生成成功率为57%，成本差异达5.6倍，但成本与成功无简单相关性；最优框架解决80%任务，但中位数仅32%；真正的框架使用率仅在28-40%狭窄区间，表明文档、源码和参数知识具有高度可替代性。

### Q4: 论文做了哪些实验？

论文构建了一种名为LLM-as-a-Developer的自动化评估流程，并在ADK Arena平台上对51个流行的Python ADK框架进行了系统实验。实验设置中，使用GPT-5.4和Opus-4.6作为“开发者”LLM，通过阅读文档生成Agent代码，再经过迭代验证修复直到通过测试。每个框架针对四个基准测试（SWE-bench、τ²-bench、Terminal-Bench和MCP-Atlas）各生成两个Agent，总共204个Agent-基准对。主要结果包括：（1）生成成功率：57%的生成运行（232/408）通过了三级验证，表明多数框架可通过自动化生成Agent；（2）成本与可用性：每Agent生成成本在0.6至3.4美元之间，差异达5.6倍，反映了API的复杂度，但成本本身不预测成功率；最稳健的框架如Haystack（每Agent约2.0/1.3美元）和AG2（2.8/1.2美元）在所有基准测试下均通过，而成本最低的Langroid（0.2-0.7美元）却失败最多；（3）执行性能：单框架最佳Agent能解决高达80%的任务，但中位数框架仅解决32%；（4）信息源消融实验：真实框架使用率保持在28-40%的狭窄区间，表明文档、源代码和参数知识可相互替代，并非硬瓶颈。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在：1）评估粒度较粗，仅统计了整体任务通过率，未深入分析框架在特定环节（如工具调用、状态管理、错误恢复）的细粒度表现差异；2）生成流程偏乐观，使用GPT-4作为唯一开发者，未考虑不同LLM对框架理解的偏差，且修复循环中可能过度依赖提示工程而非框架本身设计；3）Docker隔离虽好，但忽略了真实开发环境中的多框架协同与版本兼容问题。

未来可探索：1）构建层级化的评估维度，如API文档质量、错误信息可读性、异步编程支持等，以量化框架设计优劣；2）引入多种基座模型（包括开源模型）作为开发者，评估框架与模型的协同效应；3）设计自适应生成策略，根据框架特性自动调整代码模板和修复策略，减少LLM无意义的试错；4）探索框架间的混合使用模式，研究何时框架组合优于单一选择。

### Q6: 总结一下论文的主要内容

本文提出LLM-as-a-Developer方法论，旨在系统评估Agent开发工具包（ADK）的性能。核心思路是用LLM编码代理替代人类开发者，让它从文档学习每个框架的API、编写代理代码，并通过验证反馈循环迭代修复直至测试通过，从而将开发成本作为API易用性的量化指标，将代理性能作为框架有效性的控制衡量。基于此，论文实现了ADK Arena全自动流水线，包含按框架的Docker隔离、三级验证管道和针对SWE-bench、τ²-bench、Terminal-Bench和MCP-Atlas的基准适配器。对51个流行Python ADK框架（204个代理-基准对）的评估表明：生成成功率为57%，成本跨框架变化达5.6倍（每代理0.6至3.4美元），但成本本身不能预测成功；无单一框架主导，最佳ADK代理解决80%的任务，可击败前沿通用编码代理但成本更低，而中位数框架仅解决32%；信息源消融实验中，真实框架使用率在28-40%窄带内波动，表明文档、源代码和参数知识在很大程度上可替代，而非任一瓶颈。本研究首次提供了ADK生态系统的实证比较，为框架选择提供了量化依据。
