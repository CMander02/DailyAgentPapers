---
title: "Architecture-Aware Multi-Design Generation for Repository-Level Feature Addition"
authors:
  - "Mingwei Liu"
  - "Zhenxi Chen"
  - "Zheng Pei"
  - "Zihao Wang"
  - "Yanlin Wang"
date: "2026-03-02"
arxiv_id: "2603.01814"
arxiv_url: "https://arxiv.org/abs/2603.01814"
pdf_url: "https://arxiv.org/pdf/2603.01814v1"
categories:
  - "cs.SE"
tags:
  - "Code & Software Engineering"
  - "Architecture & Frameworks"
relevance_score: 7.5
taxonomy:
  capability:
    - "Code & Software Engineering"
    - "Architecture & Frameworks"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "DeepSeek-v3.2, GPT-4"
  key_technique: "RAIM (Repository-level Architecture-aware Implementation via Multi-design generation)"
  primary_benchmark: "NoCode-bench Verified"
---

# Architecture-Aware Multi-Design Generation for Repository-Level Feature Addition

## 原始摘要

Implementing new features across an entire codebase presents a formidable challenge for Large Language Models (LLMs). This proactive task requires a deep understanding of the global system architecture to prevent unintended disruptions to legacy functionalities. Conventional pipeline and agentic frameworks often fall short in this area because they suffer from architectural blindness and rely on greedy single-path code generation. To overcome these limitations, we propose RAIM, a multi-design and architecture-aware framework for repository-level feature addition. This framework introduces a localization mechanism that conducts multi-round explorations over a repository-scale code graph to accurately pinpoint dispersed cross-file modification targets. Crucially, RAIM shifts away from linear patching by generating multiple diverse implementation designs. The system then employs a rigorous impact-aware selection process based on static and dynamic analysis to choose the most architecturally sound patch and avoid system regressions. Comprehensive experiments on the NoCode-bench Verified dataset demonstrate that RAIM establishes a new state-of-the-art performance with a 39.47% success rate, achieving a 36.34% relative improvement over the strongest baseline. Furthermore, the approach exhibits robust generalization across various foundation models and empowers open-weight models like DeepSeek-v3.2 to surpass baseline systems powered by leading proprietary models. Detailed ablation studies confirm that the multi-design generation and impact validation modules are critical to effectively managing complex dependencies and reducing code errors. These findings highlight the vital role of structural awareness in automated software evolution.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在代码库级别实现新功能时所面临的挑战。研究背景是软件工程正转向自然语言驱动的功能添加，即用户通过描述而非直接编码来指定新功能，这要求系统能理解整个代码库的全局架构，以确保新功能无缝集成且不破坏现有逻辑。现有方法（如用于问题修复的流程式或智能体框架）存在明显不足：它们通常缺乏对代码库整体结构的认知（架构盲区），并且依赖贪婪的单一路径代码生成策略，即找到第一个看似可行的补丁就接受，缺乏对修改影响的 rigorous 评估。这些方法在处理需要主动设计、涉及多文件依赖的功能添加任务时，容易定位不准或引入回归错误。

因此，本文要解决的核心问题是：如何让LLM在代码库级别进行功能添加时，具备架构感知能力，并生成多个高质量的设计方案以供选择，从而避免破坏现有系统，实现稳健的软件演化。为此，论文提出了RAIM框架，它通过构建代码图来理解结构依赖，进行多轮探索以精确定位修改点；通过生成多个多样化的实现设计来扩展解决方案空间；最后通过结合静态和动态分析的变更影响评估，选择最符合架构、最稳健的补丁。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大类，主要围绕解决仓库级代码生成与修改任务。

在方法类研究中，主要分为两类。第一类是工作流方法，例如 Agentless，它采用固定的多阶段流水线，通过分层检索来定位编辑位置并生成补丁。第二类是智能体框架，例如 OpenHands，它利用“思考-工具执行”的迭代循环来导航代码库。这些方法在问题解决（如 SWE-bench）上有效，但本文指出它们存在“架构盲区”和依赖贪婪的单路径代码生成，缺乏对仓库级结构依赖的整体把握，且倾向于线性接受第一个看似可行的补丁，缺乏严格的变更影响评估。

在应用类研究中，相关工作聚焦于软件维护任务，尤其是 SWE-bench 所代表的缺陷修复。本文强调，与这些针对已有失败测试用例的“反应式”维护不同，本文研究的特性添加是一种“主动式”架构挑战，需要在没有明确错误信号的情况下实现高层规范，对架构理解和集成协调的要求更高。

本文提出的 RAIM 框架与这些工作的核心区别在于：1）引入了基于代码图的架构感知定位机制，通过多轮迭代搜索理解跨文件依赖，而非将仓库视为非结构化文本进行扁平检索；2）采用多设计生成策略，扩展解决方案空间，而非生成单一补丁；3）结合静态与动态分析的变更影响评估来选择最优补丁，确保架构一致性并防止回归，而非进行贪婪或线性的选择。

### Q3: 论文如何解决这个问题？

论文提出的RAIM框架通过一个多阶段、架构感知的流程来解决仓库级代码库中添加新功能的挑战。其核心方法是摒弃传统的线性单路径生成，转而采用**多轮探索、多设计生成和影响感知选择**的综合策略。

**整体框架与主要模块**：
RAIM框架包含四个顺序执行的核心阶段：
1.  **架构感知的文件定位**：首先将代码仓库解析为结构树，结合新功能描述，让大语言模型初步识别“可疑文件”。随后，分析这些文件间的导入关系，构建文件级调用图。最后，综合结构树、调用图和代码骨架，准确定位出与功能相关的文件集合，确保覆盖跨文件的依赖关系。
2.  **基于代码图的多轮函数定位**：以定位到的相关文件为锚点，构建一个包含包、文件、类、函数等多粒度节点的**特征相关代码子图**。在此子图上进行两阶段细粒度定位：
    *   **基于嵌入模型的多轮检索**：结合LLM的语义理解和嵌入模型的向量相似度检索，从代码子图中迭代地检索出与功能描述相关的候选函数，并通过生成新查询探索邻居节点，扩大搜索范围。
    *   **基于LLM的相关函数选择**：LLM对候选函数集进行语义重排序，过滤噪声，精准确定最终需要编辑的顶层相关函数。
3.  **基于多设计的补丁生成**：这是框架的关键创新点，旨在生成多样化的实现方案。
    *   **多设计生成**：基于已定位的函数及其在代码图中的调用依赖关系，构建结构化的上下文。LLM据此从不同视角（如重构、模式扩展）头脑风暴出N个不同的**架构设计**。每个设计是一系列明确的操作序列（类型、目标、描述）。
    *   **基于多设计的补丁生成**：针对每个架构设计，独立进行行级编辑位置定位。根据操作类型（修改或创建）动态调整输入上下文的粒度，然后指导LLM生成对应的具体代码补丁，从而得到一个多样化的补丁集合。
4.  **影响感知的补丁选择**：对生成的多个候选补丁进行严格筛选，结合静态和动态分析评估代码变更的影响。
    *   **基于代码子图的静态影响分析**：将补丁修改的实体映射回代码图，分析相关子图中节点（如被修改函数）的中心度（入度/出度），评估其影响范围，并生成静态影响报告。
    *   **动态测试分析**：通过执行测试来验证补丁的行为正确性，确保新功能生效且未破坏现有功能。
    *   综合静态和动态分析结果，选择**架构最合理、且能通过测试**的最优补丁进行最终实施。

**关键技术及创新点**：
*   **架构感知与代码图**：全程利用代码图（包含层次和语义依赖边）来理解仓库级结构，克服了传统方法的“架构盲区”。
*   **多轮、多粒度定位**：从文件到函数再到代码行，通过迭代检索和LLM重排序，精准定位分散的修改点。
*   **多设计生成**：核心创新。模拟软件工程实践，先产生多种高层设计蓝图，再分别实例化为代码补丁，极大地扩展了解决方案空间，避免陷入单一脆弱路径。
*   **影响感知的混合验证**：创新性地结合了基于图中心度的静态架构影响评估和动态测试，确保所选补丁在实现功能的同时，最大程度维护系统架构的完整性和稳定性。

### Q4: 论文做了哪些实验？

论文在NoCode-bench Verified数据集上进行了全面的实验评估。该数据集包含114个经过人工验证的仓库级功能添加任务，每个任务都提供了功能描述和完整的代码仓库。评估指标包括任务成功率（Success(%)）、回归测试通过率（RT(%)）以及功能验证（FV-Micro和FV-Macro）。

实验设置了两个基线方法进行对比：基于工作流的**Agentless**（确定性多阶段流程）和基于智能体的**OpenHands**（迭代规划与工具执行）。论文提出的**RAIM**框架与这些基线在多种大语言模型上进行了比较，包括GPT-5-Chat、Gemini-2.5-Pro、DeepSeek-v3.2、DeepSeek-R1、Qwen3-235B等。RAIM的关键参数包括：初始检索top-k=3个函数，邻居扩展top-n=5个节点，最终候选top-m=3个，并为每个任务生成N=5个不同的实现设计方案。

主要结果显示，RAIM取得了最先进的性能。在使用DeepSeek-v3.2模型时，RAIM的成功率达到**39.47%**，显著优于最佳基线Agentless（使用Claude-4-Sonnet模型，成功率28.07%），实现了**36.34%**的相对提升。具体数据上，RAIM (DeepSeek-v3.2)的回归测试通过率为85.96%，FV-Micro为16.01%，FV-Macro为45.58%。此外，实验表明RAIM具有良好的泛化能力，能够使开源的DeepSeek-v3.2等模型超越使用领先闭源模型的基线系统。消融研究证实了多设计生成和影响验证模块对于管理复杂依赖和减少代码错误至关重要。

### Q5: 有什么可以进一步探索的点？

基于论文内容，RAIM框架在仓库级功能添加任务上取得了显著进展，但仍存在局限性和广阔的探索空间。首先，其性能虽为SOTA，但成功率（39.47%）仍有超过60%的任务未能解决，表明处理极端复杂的架构依赖和模糊需求时仍面临挑战。其次，框架依赖于静态和动态分析进行影响验证，但动态测试的覆盖率和效率可能不足，尤其对于需要复杂环境配置或长时运行的测试。

未来研究方向可从以下几点展开：1) **增强架构理解深度**：当前基于代码图的定位机制可能忽略高层次设计模式或架构约束。可探索结合自然语言文档、提交历史或架构描述，使模型具备更语义化的系统理解能力。2) **改进多设计生成策略**：论文生成5个设计，但多样性可能受限于模型创造力。可引入基于遗传算法或强化学习的探索机制，系统化生成并演化更多样、更创新的解决方案。3) **动态验证的扩展**：当前回归测试可能无法捕捉所有副作用。可集成更细粒度的程序分析（如符号执行）或轻量级形式化验证，提前预测潜在运行时错误。4) **人机协同机制**：对于失败案例，可设计交互式调试接口，允许开发者提供反馈或约束，引导模型迭代修正，形成闭环优化系统。

此外，RAIM目前专注于功能添加，未来可扩展至更广泛的软件维护任务，如缺陷修复、架构重构或性能优化，验证其通用性。最后，框架的计算开销较大，如何平衡多设计生成的开销与效率，实现更经济的搜索，也是值得探索的工程问题。

### Q6: 总结一下论文的主要内容

本文针对大语言模型（LLM）在代码仓库级别实现新功能（即特征添加）时面临的挑战，提出了一个名为RAIM的架构感知多设计生成框架。核心问题是现有方法（如固定流程的管道方法或代理框架）存在架构盲区，且依赖贪婪的单路径代码生成，难以理解全局系统架构并避免破坏现有功能。

RAIM框架包含三个关键部分：首先，通过构建仓库级代码图并进行多轮迭代搜索，实现精准的跨文件修改目标定位；其次，采用多设计生成策略，让LLM构思多种不同的实现方案以扩展解空间；最后，引入一个基于静态和动态分析的、严格的“影响感知”选择机制，评估每个候选补丁对现有功能稳定性和新功能正确性的影响，从而选出架构最合理、最不易引发退化的补丁。

实验表明，在NoCode-bench Verified数据集上，RAIM取得了39.47%的成功率，相对于最强基线实现了36.34%的相对提升，确立了新的最先进性能。该方法还展现出强大的泛化能力，能使开源模型（如DeepSeek-v3.2）的性能超越基于领先专有模型的基线系统。消融研究证实，多设计生成和影响验证模块对于有效管理复杂依赖和减少代码错误至关重要，凸显了结构感知在自动化软件演化中的关键作用。
