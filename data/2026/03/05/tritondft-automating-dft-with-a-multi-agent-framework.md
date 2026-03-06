---
title: "TritonDFT: Automating DFT with a Multi-Agent Framework"
authors:
  - "Zhengding Hu"
  - "Kuntal Talit"
  - "Zhen Wang"
  - "Haseeb Ahmad"
  - "Yichen Lin"
  - "Prabhleen Kaur"
  - "Christopher Lane"
  - "Elizabeth A. Peterson"
  - "Zhiting Hu"
  - "Elizabeth A. Nowadnick"
  - "Yufei Ding"
date: "2026-03-02"
arxiv_id: "2603.03372"
arxiv_url: "https://arxiv.org/abs/2603.03372"
pdf_url: "https://arxiv.org/pdf/2603.03372v2"
github_url: "https://github.com/Leo9660/TritonDFT"
categories:
  - "cond-mat.mtrl-sci"
  - "cs.MA"
tags:
  - "多智能体系统"
  - "Agent 架构"
  - "科学计算自动化"
  - "工作流自动化"
  - "Agent 评测/基准"
relevance_score: 8.0
---

# TritonDFT: Automating DFT with a Multi-Agent Framework

## 原始摘要

Density Functional Theory (DFT) is a cornerstone of materials science, yet executing DFT in practice requires coordinating a complex, multi-step workflow. Existing tools and LLM-based solutions automate parts of the steps, but lack support for full workflow automation, diverse task adaptation, and accuracy-cost trade-off optimization in DFT configuration. To this end, we present TritonDFT, a multi-agent framework that enables efficient and accurate DFT execution through an expert-curated, extensible workflow design, Pareto-aware parameter inference, and multi-source knowledge augmentation. We further introduce DFTBench, a benchmark for evaluating the agent's multi-dimensional capabilities, spanning science expertise, trade0off optimization, HPC knowledge, and cost efficiency. TritonDFT provides an open user interface for real-world usage. Our website is at https://www.tritondft.com. Our source code and benchmark suite are available at https://github.com/Leo9660/TritonDFT.git.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决密度泛函理论（DFT）计算在实际应用中工作流程复杂、手动操作繁琐且难以自动化的问题。DFT是材料科学的核心计算方法，但其执行涉及结构信息搜索、参数配置、脚本编写、高性能计算（HPC）任务提交与监控、结果分析等多个异构步骤，需要物理、材料科学、特定DFT软件和HPC等多领域专业知识。现有工具或基于大语言模型（LLM）的方案仅能自动化部分环节，缺乏对完整工作流的支持，难以适应多样化的计算任务，且无法在DFT参数配置中有效优化精度与计算成本之间的权衡。

针对这些不足，本文提出了TritonDFT，一个多智能体框架，旨在实现高效、准确的DFT全流程自动化。其核心解决方案包括：设计专家指导的可扩展工作流（Plan–Execute–Refine）与任务-可执行文件映射机制以支持广泛任务类型；引入帕累托感知的参数推断方法，使LLM能估计精度-成本的帕累托前沿并迭代优化配置；通过领域工具增强、历史记忆和交互式人机接口提高可靠性。此外，论文还提出了DFTBench基准测试，用于评估智能体在科学专业知识、权衡优化、HPC知识和成本效率等多维能力上的表现，以填补现有评估空白。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：现有DFT自动化工具、基于LLM的智能体框架，以及材料科学领域的智能体评测基准。

在**DFT自动化工具**方面，现有工具如Atomate、ASE和AiiDA主要实现了工作流中部分步骤的自动化（如结构到脚本的生成或作业调度），但缺乏对完整工作流的智能协调与参数配置指导。本文提出的TritonDFT旨在实现端到端的自动化，并特别关注参数配置中的精度-成本权衡优化。

在**基于LLM的智能体框架**方面，相关工作（如HoneyComb、ChemCrow）通过集成领域专用工具来增强智能体能力，但这些工具通常封装为简单的输入-输出函数。相比之下，将DFT作为工具集成涉及更复杂的工作流，包括物理参数配置、HPC作业并行化管理与结果分析。近期也出现了专注于DFT的智能体研究（如DREAMS、VASPilot、AgenticDFT），但它们通常针对特定任务类型（如表面化学、电子结构）和有限材料类别，且缺乏对精度-成本权衡、并行效率和货币成本的系统性评估。本文的TritonDFT框架则支持更通用的任务类型、更丰富的材料体系，并引入了帕累托感知的参数推理与多源知识增强。

在**评测基准**方面，材料科学领域已出现多种LLM评测基准，涵盖问答、任务完成、工具使用和实验设计等。然而，这些基准未能全面涵盖DFT执行所需的多维度能力（如科学专业知识、HPC知识、权衡优化与成本效率）。为此，本文专门引入了DFTBench基准，以评估智能体在这些关键维度的综合能力。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为TritonDFT的多智能体框架，实现了密度泛函理论（DFT）计算工作流的全自动化。其核心方法是将LLM驱动的智能体工作流与开源DFT软件Quantum Espresso深度集成，接受自然语言任务描述，并自主编排从问题分解到结果解析的完整流程。

整体框架采用解耦设计，将智能体后端与DFT计算后端分离。主要模块包括：1）**规划智能体（Planner Agent）**：动态将高层用户查询分解为一系列DFT子问题（如结构弛豫、自洽场计算），每个子问题确定性地映射到DFT库中的特定可执行文件。2）**闭环求解工作流**：在每个子问题内部，执行四个步骤：**参数推断**利用帕累托最优感知推理，在预期精度-成本权衡下确定物理参数；**脚本生成器**将参数合成为语法正确的输入文件；**执行器**负责作业提交并设置高性能计算参数；**解释器**解析原始输出，提供正确性判断、改进建议或结果摘要。3）**外部工具与内存机制**：集成Materials Project等材料数据库和pymatgen工具，以获取物理信息并执行结构分析；同时设计历史记忆模块，分别基于物理相似性（如空间群、元素组成）和计算负载特征（如k点数量）来检索和复用成功的参数配置。

关键技术及创新点体现在：**帕累托感知参数优化**：智能体并非进行静态一次性推断，而是基于结果估计迭代优化参数配置，通过反馈循环逼近估计的帕累托最优点，并排除不收敛的无效配置。**自动化并行化**：根据自然语言硬件描述和资源成本估算，通过短时试运行提取k点数量、内存消耗等关键信号，智能设置并行化参数以最大化效率并避免资源过载。**可扩展与用户友好设计**：框架支持以模块化方式添加新的可执行文件；提供开放的Web界面，支持纯自然语言交互和“人在回路”反馈机制，允许用户在关键阶段进行干预和验证，从而适应不同专业水平的研究人员需求。

### Q4: 论文做了哪些实验？

论文实验围绕TritonDFT框架和DFTBench基准展开。实验设置上，框架集成了Quantum ESPRESSO (v7.4)软件，部署于配备AMD EPYC 9534 64核处理器的高性能计算节点，并通过统一API接口调用多种商业大语言模型(LLM)。评估模型包括OpenAI的GPT 5.2/5.1/4o/4o mini、Google的Gemini 2.5 Pro/Flash以及Anthropic的Claude Opus/Sonnet 4.5，共八个前沿模型。

使用的数据集/基准测试是作者提出的DFTBench，主要针对四个DFT任务进行基准测试：变胞弛豫(VC-relax)、自洽场计算(SCF)、能带隙(Band Gap)和态密度(DOS)，并包含更高级任务（如声子分析）的案例研究。

对比方法主要涉及不同LLM在TritonDFT框架下的性能对比，以及将LLM生成的参数配置与通过人工收敛测试得到的最严格（帕累托最优）配置进行对比。

主要结果及关键数据指标如下：
1.  **DFT参数配置评估**：在VC-relax任务中，评估模型在不同能量误差阈值（ΔE < 20, 10, 1 meV/atom）下的通过率(Pass Rate)和归一化成本(Normalized Cost)。GPT 5.2表现最佳，在20 meV/atom阈值下通过率达70.5%，但归一化成本也最高（14.29）。在严格的1 meV/atom阈值下，所有模型的通过率均显著下降（GPT 5.2为47.1%，其他多数低于15%）。高级参数（如自旋极化、Hubbard U、范德华修正）满足率方面，Claude Opus 4.5最高（53.8%），GPT 5.2为51.3%。
2.  **端到端工作流精度**：计算各任务的平均误差。对于VC-relax（晶格常数）和SCF（每原子能量），报告平均相对误差(MRE)；对于Band Gap和DOS（费米能级），报告平均绝对误差(MAE)。性能最强的模型（如GPT 5.2、Gemini 2.5 Pro）在所有任务中均保持高精度，例如GPT 5.2在VC-relax上的MRE为5.7%，在SCF上为0.0%。
3.  **自动并行化效率**：评估结构弛豫阶段的并行执行加速比。Claude 4.5 Opus和GPT 5.2等具有优秀编码和推理能力的模型能带来持续的性能提升，峰值加速比最高达16.1%（Claude 4.5 Opus在32/64核下）。而部分模型（如GPT-4o、Gemini 2.5 Flash）则出现性能下降。
4.  **工作流吞吐量与货币成本**：TritonDFT的端到端工作流吞吐量（不计DFT计算时间）约为10-100次查询/小时，相比博士级从业者的手动设置（<1次/小时）有超过10倍的效率提升。API使用货币成本方面，Gemini 2.5 Flash最具成本效益（每次查询平均$0.01–0.03），而Claude系列成本最高（如Opus 4.5在能带计算中达$0.44/查询）。
5.  **帕累托感知推理与跨材料类型性能**：实验表明，帕累托感知的迭代推理能帮助模型（如GPT 5.2）在满足精度约束下将归一化成本降低高达4.1倍。在不同材料类型上，模型在金属、半导体等简单系统上通过率较高，而在磁性材料等复杂系统上性能显著下降（所有模型通过率<6%）。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在对复杂量子体系（如磁性材料）的建模能力不足，当前模型通过率低于6%，这源于现有方法缺乏对特定物理机制的深度推理。此外，框架目前主要基于Quantum Espresso，限制了其在不同DFT求解器间的可移植性，也未与实验平台实现闭环集成。

未来研究方向可从三方面拓展：一是开发物理信息增强的推理模块，针对磁性、强关联体系等复杂状态，引入对称性约束或多尺度建模，以提升科学准确性；二是增强框架的模块化与扩展性，支持VASP、ABINIT等多种求解器，并设计统一的接口标准，促进跨工具协同；三是推动“计算-实验”闭环自动化，将TritonDFT与机器人实验、高通量表征平台对接，实现模拟指导实验、实验反馈优化的迭代发现流程。

可能的改进思路包括：引入强化学习动态优化参数选择，平衡精度与成本；构建领域知识图谱，增强多智能体对材料化学关系的理解；开发轻量化版本，降低高性能计算资源依赖，拓展至边缘计算场景。

### Q6: 总结一下论文的主要内容

该论文提出了TritonDFT，一个用于自动化密度泛函理论（DFT）计算的多智能体框架。DFT是材料科学的核心方法，但其实际执行涉及复杂、多步骤的工作流，现有工具或基于大语言模型的方案仅能部分自动化，缺乏对完整工作流、多样化任务适应以及精度-成本权衡优化的支持。

TritonDFT的核心贡献在于通过一个由专家策划且可扩展的工作流设计、帕累托感知的参数推断以及多源知识增强，实现了高效且准确的DFT执行。该方法旨在自动化整个DFT工作流程，并优化计算配置中的精度与成本平衡。

此外，论文引入了DFTBench基准测试，用于从科学专业知识、权衡优化、高性能计算知识和成本效率等多个维度评估智能体的能力。TritonDFT提供了开放的实用界面，其意义在于显著降低了DFT计算的门槛和复杂性，推动了计算材料科学的自动化进程。
