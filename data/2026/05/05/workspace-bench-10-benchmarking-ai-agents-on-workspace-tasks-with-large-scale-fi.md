---
title: "Workspace-Bench 1.0: Benchmarking AI Agents on Workspace Tasks with Large-Scale File Dependencies"
authors:
  - "Zirui Tang"
  - "Xuanhe Zhou"
  - "Yumou Liu"
  - "Linchun Li"
  - "Weizheng Wang"
  - "Hongzhang Huang"
  - "Jun Zhou"
  - "Jiachen Song"
  - "Shaoli Yu"
  - "Jinqi Wang"
  - "Zihang Zhou"
  - "Hongyi Zhou"
  - "Yuting Lv"
  - "Jinyang Li"
  - "Jiashuo Liu"
  - "Ruoyu Chen"
  - "Chunwei Liu"
  - "GuoLiang Li"
  - "Jihua Kang"
  - "Fan Wu"
date: "2026-05-05"
arxiv_id: "2605.03596"
arxiv_url: "https://arxiv.org/abs/2605.03596"
pdf_url: "https://arxiv.org/pdf/2605.03596v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.DB"
  - "cs.LG"
tags:
  - "Benchmark"
  - "Workspace Agent"
  - "File Dependency"
  - "Agent Evaluation"
  - "Large-Scale Evaluation"
relevance_score: 9.0
---

# Workspace-Bench 1.0: Benchmarking AI Agents on Workspace Tasks with Large-Scale File Dependencies

## 原始摘要

Workspace learning requires AI agents to identify, reason over, exploit, and update explicit and implicit dependencies among heterogeneous files in a worker's workspace, enabling them to complete both routine and advanced tasks effectively. Despite its importance, existing relevant benchmarks largely evaluate agents on pre-specified or synthesized files with limited real-world dependencies, leaving workspace-level evaluation underexplored. To this end, we introduce Workspace-Bench, a benchmark for evaluating AI agents on Workspace Learning invOlving Large-Scale File Dependencies. We construct realistic workspaces with 5 worker profiles, 74 file types, 20,476 files (up to 20GB) and curate 388 tasks, each with its own file dependency graph, evaluated across 7,399 total rubrics that require cross-file retrieval, contextual reasoning, and adaptive decision-making. We further provide Workspace-Bench-Lite, a 100-task subset that preserves the benchmark distribution while reducing evaluation costs by about 70%. We evaluate 4 popular agent harnesses and 7 foundation models. Experimental results show that current agents remain far from reliable workspace learning, where the best reaches only 68.7%, substantially below the human result of 80.7%, and the average performance across agents is only 47.4%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前AI智能体在真实工作场景中处理大规模、异构文件依赖关系时能力不足的问题。研究背景是，尽管基础模型和智能体框架取得了显著进展，但AI智能体在实际职场任务中仍面临挑战，尤其是在需要跨文件检索、上下文推理和自适应决策的场景中。现有基准测试存在明显不足：提示驱动基准将所有信息嵌入指令，绕过了实际文件操作；开源环境驱动基准侧重工具调用和API编排，忽略了本地文件生态的导航与推理；任务文件驱动基准提供任务特定文件，但类似孤立的文档问答，缺乏对目录结构自主搜索；工作区相关基准虽有文件系统模拟，但结构单一、文件类型少（通常少于10种），且未明确评估文件间的依赖关系（如聚合、语义关联、版本溯源）。为此，本文引入Workspace-Bench，一个包含5个真实工作角色、74种文件类型、20476个文件（达20GB）和388个任务的基准，每个任务配有文件依赖图和7399条评估细则。核心问题是：在复杂工作区场景下，AI智能体能否可靠地识别、推理并利用大规模文件间的显式和隐式依赖关系以完成任务？实验表明，当前最佳智能体仅达68.7%的通过率，远低于人类的80.7%，平均仅47.4%，凸显了工作区学习能力的关键瓶颈。

### Q2: 有哪些相关研究？

根据论文，相关研究可分为四类：

**GUI与桌面智能体**：如SeeClick、CogAgent、UFO、ShowUI、UI-TARS和商业产品Anthropic Claude Cowork等，擅长局部单应用操作，但难以理解跨文件的隐含关系。本文则聚焦于工作空间中大规模文件的复杂依赖。

**记忆与RAG智能体**：如MemGPT，通过分层管理记忆和检索增强生成处理长文任务，但将检索内容视为扁平文本块，缺乏对文件结构性和时序性依赖的建模。本文的核心是建模这种依赖关系。

**评测基准**：
- **提示驱动**：如CL-Bench、OneMillion-Bench，信息完全嵌入指令中，不涉及外部环境交互。
- **开源/环境驱动**：如OSWorld、GAIA、WebArena等，强调工具使用和动态环境交互，但忽略本地文件生态的导航与推理。
- **任务-文件驱动**：如OfficeQA-Pro、GDPVal、DataCross，提供预打包文件，类似孤立文档问答，无需自主搜索。
- **工作空间相关**：如WorkBench（仅5个.xlsx文件）、OfficeBench、SWE-bench、TheAgentCompany，虽模拟了工作结构，但文件类型单一、任务多可单文件解决，缺乏深度跨文件关系评估。

本文是首个系统性评测智能体在复杂文件依赖关系中进行工作空间学习的基准，通过多样角色、70+文件类型和需跨文件推理的任务，填补了上述工作的空白。

### Q3: 论文如何解决这个问题？

该论文提出了一种针对大规模文件依赖的工作空间学习评估方法，核心在于构建高保真数字工作空间和依赖驱动的任务评估体系。整体框架包括工作空间构造、任务构建和评估框架三个主要部分。在工作空间构造方面，论文采用自上而下的两阶段混合流水线：首先根据五种角色（运营经理、物流经理、AI产品经理、后端开发者、研究员）的人设生成树状目录结构，并引入冗余文件夹、歧义名称等结构噪声；然后通过混合策略填充内容，包括使用语义驱动爬虫从真实数据源检索公共资源（如arXiv论文、GitHub仓库），并利用LLM基于收集文件合成相关工件（如邮件、会议纪要）。任务构建方面，采用问题驱动的人工策展流水线：通过内部问卷收集真实工作流，由领域专家筛选出154个代表性任务场景；25名标注员在模拟工作空间中创建具体任务，每个任务包括自然语言指令、文件依赖图（标注代理必须访问的完整文件路径）、参考输出和细粒度评估准则（基础型、过程型、结果型二值命题）。评估框架设计了并行加速机制（工作空间级和任务级并行）和多策略文件提取技术（指令约束路径提取、统一副本检索、元数据模糊匹配），以及基于BFS的并行工作空间回滚算法。创新点包括：依赖驱动的推理评估（明确标注文件间的显式引用、语义关系、版本谱系等依赖），过程感知的细粒度评估（不仅评估最终输出，还检查中间决策如文件版本选择），以及高保真工作空间构建（含隐含约定、角色特定组织、噪声结构）。

### Q4: 论文做了哪些实验？

论文构建了Workspace-Bench基准测试，包含5个真实工作场景（运营经理122任务、物流经理115任务、研究员67任务、后端开发43任务、AI产品经理41任务，共388任务）、74种文件类型、20,476个文件（最大工作空间11,020文件）、7,399条评估细则（平均每任务19.1条），并提供了Workspace-Bench-Lite子集（100任务，降低70%评估成本）。实验评估了4种主流智能体框架和7种基础模型，采用结果导向（54.8%）、基础合规（25.0%）、过程导向（20.2%）三类细则打分。关键结果：最佳模型仅达68.7%准确率，远低于人类80.7%的表现，所有智能体平均仅47.4%。对比了不同难度任务（低边缘密度33.8%、中36.9%、高29.4%），实验还通过并行工作空间和任务级沙箱加速评估，采用多策略文件提取及并行BFS工作空间恢复机制确保环境一致性。

### Q5: 有什么可以进一步探索的点？

Workspace-Bench 1.0 的局限性和未来研究方向主要包括：

**局限性**：当前基准主要聚焦于静态文件依赖关系，缺乏对动态协作场景（如多人实时编辑、版本冲突解决）的模拟；任务难度分级仅基于依赖边数量，未充分考虑逻辑推理复杂度；评估指标侧重结果正确性，对agent的中间推理过程和错误恢复能力关注不足；此外，20GB的workspace规模虽然真实，但对大型模型的推理成本提出了巨大挑战。

**未来方向**：1) 引入时间维度，构建包含文件版本演变和任务迭代的动态workspace，测试agent的长期规划和版本管理能力；2) 设计多agent协作场景，评估agent在共享workspace中的协调与冲突解决能力；3) 改进评估体系，增加对agent信息检索策略、错误诊断和自适应学习能力的细粒度评估；4) 探索更高效的上下文压缩和结构化检索技术，使agent能在保持推理质量的同时处理更大规模的workspace；5) 开发可解释性评估方法，理解agent在跨文件依赖推理中的失败模式，针对性改进模型架构或训练策略。

### Q6: 总结一下论文的主要内容

本文提出Workspace-Bench，旨在系统评估AI智能体在具有大规模文件依赖的办公场景中的工作空间学习能力。现有基准多依赖预设的独立文件，缺乏对真实工作环境中多源异构文件间依赖关系的建模。为此，该基准构建了5个代表性角色（如运营经理、研发人员）的真实数字工作空间，包含74种文件类型、20476个文件（总计20GB），并设计388个任务。每个任务配有专属文件依赖图，通过7399条评估细目从跨文件检索、上下文推理、自适应决策等六个维度进行细粒度评测。实验基于4种智能体框架和7种基础模型，结果显示最佳智能体仅达68.7%的通过率，远低于人类80.7%的水平，平均仅47.4%。该工作揭示了当前智能体在处理真实依赖推理任务上的严重不足，为评估AI从孤立技能向工作空间感知推理的转变提供了关键测试平台。
