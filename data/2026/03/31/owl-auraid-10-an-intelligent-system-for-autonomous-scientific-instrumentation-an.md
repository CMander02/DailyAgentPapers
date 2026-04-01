---
title: "Owl-AuraID 1.0: An Intelligent System for Autonomous Scientific Instrumentation and Scientific Data Analysis"
authors:
  - "Han Deng"
  - "Anqi Zou"
  - "Hanling Zhang"
  - "Ben Fei"
  - "Chengyu Zhang"
  - "Haobo Wang"
  - "Xinru Guo"
  - "Zhenyu Li"
  - "Xuzhu Wang"
  - "Peng Yang"
  - "Fujian Zhang"
  - "Weiyu Guo"
  - "Xiaohong Shao"
  - "Zhaoyang Liu"
  - "Shixiang Tang"
  - "Zhihui Wang"
  - "Wanli Ouyang"
date: "2026-03-31"
arxiv_id: "2603.29828"
arxiv_url: "https://arxiv.org/abs/2603.29828"
pdf_url: "https://arxiv.org/pdf/2603.29828v1"
github_url: "https://github.com/OpenOwlab/AuraID"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Embodied Agent"
  - "GUI Automation"
  - "Scientific Discovery"
  - "Tool Use"
  - "Workflow Automation"
  - "Multimodal Analysis"
relevance_score: 7.5
---

# Owl-AuraID 1.0: An Intelligent System for Autonomous Scientific Instrumentation and Scientific Data Analysis

## 原始摘要

Scientific discovery increasingly depends on high-throughput characterization, yet automation is hindered by proprietary GUIs and the limited generalizability of existing API-based systems. We present Owl-AuraID, a software-hardware collaborative embodied agent system that adopts a GUI-native paradigm to operate instruments through the same interfaces as human experts. Its skill-centric framework integrates Type-1 (GUI operation) and Type-2 (data analysis) skills into end-to-end workflows, connecting physical sample handling with scientific interpretation. Owl-AuraID demonstrates broad coverage across ten categories of precision instruments and diverse workflows, including multimodal spectral analysis, microscopic imaging, and crystallographic analysis, supporting modalities such as FTIR, NMR, AFM, and TGA. Overall, Owl-AuraID provides a practical, extensible foundation for autonomous laboratories and illustrates a path toward evolving laboratory intelligence through reusable operational and analytical skills. The code are available at https://github.com/OpenOwlab/AuraID.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决科学实验自动化，尤其是高精度表征环节中，因仪器软件异构、缺乏开放API而导致的自动化瓶颈问题。研究背景是AI for Science（AI4Science）在计算假设生成方面取得了巨大进展（如AlphaFold），但实验验证环节仍高度依赖人工操作，导致“干实验”发现与“湿实验”验证之间存在巨大鸿沟。现有自动化方法（如集成材料平台、移动实验室代理）主要依赖预定义的设备API或定制化软硬件栈，这在由大量异构、专有、闭源且缺乏可编程接口的商业仪器组成的真实实验室中部署困难，可扩展性和通用性不足。

本文的核心问题是：如何在不依赖仪器预设API的情况下，实现对多种异构科学仪器的端到端自动化操作与数据分析，以桥接物理样品处理与科学解释，推动自主实验室的实用化发展。为此，论文提出将自主科学表征重新定义为基于图形用户界面（GUI）的计算机使用问题，并引入一个以技能为中心的GUI原生范式。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：自动化实验室系统、基于LLM的科学智能体以及GUI智能体。

在**自动化实验室系统**方面，相关工作旨在通过机器人技术和自动化硬件实现实验流程的闭环。例如，Venus系列、Mobile Robotic Chemist、A-Lab、Chemspeed和LUMI-lab等系统，通常依赖机器人对图形用户界面（GUI）进行物理操控或预定义的API来控制仪器。Uni-Lab-OS等框架则强调通过工具或API对异构设备进行编排。然而，这些系统大多依赖于预先集成的自动化栈或对实验室环境的专门改造，难以直接应用于软件封闭、高度异构的现实表征实验室。

在**基于LLM的科学智能体**方面，研究探索利用大语言模型进行实验规划、工具调用和知识整合。例如，Coscientist展示了LLM在连接到可编程实验室端点时的实验设计与执行能力；ChemCrow通过编排外部工具解决化学任务；AI Scientist则提出了管理从假设生成到论文撰写全过程的框架。这些工作的共同假设是相关工具（如API、脚本、数据库）已可通过程序化方式访问，因此更侧重于对已有工具的科学推理，而非直接操作封闭的、以GUI为核心的专用科学软件。

在**GUI智能体（或称计算机使用智能体）**方面，研究取得了快速进展，旨在通过视觉界面直接操作软件。相关基准（如OSWorld）和模型（如UI-TARS、Claude Sonnet）推动了智能体在通用桌面或移动应用中的表现。然而，现有评估多集中于办公软件或消费级环境，较少涉及科学仪器控制这类具有状态复杂、流程长、容错率低且与物理操作紧密耦合特点的专业领域。

本文提出的Owl-AuraID系统与上述工作的关系和区别在于：它**融合并拓展**了这些方向。与自动化实验室系统相比，本文采用“GUI原生”范式，无需预定义接口即可操作任意科学软件，通用性更强。与基于LLM的科学智能体相比，本文直接攻克了封闭GUI软件的操作难题，而非仅调用现有API。与通用GUI智能体相比，本文专注于科学仪器控制这一特定、高风险的领域，并创新性地将Type-1（GUI操作）与Type-2（数据分析）技能集成到端到端工作流中，连接了物理样本处理与科学解释，支持能力的持续演进（Evolve）。

### Q3: 论文如何解决这个问题？

论文通过构建一个以技能为中心的智能体平台Owl-AuraID来解决科学仪器自动化中因专有GUI和现有API系统通用性不足所带来的障碍。其核心方法是采用“GUI原生”范式，让智能体能够像人类专家一样通过图形用户界面直接操作仪器，并将仪器操作与数据分析无缝集成到端到端的工作流中。

整体框架建立在InnoClaw智能体运行时平台之上，继承了现代编码智能体的关键特性，如工作空间访问、命令执行、模型驱动的规划和自主智能体循环。然而，它针对科学实验环境进行了关键性重新设计。系统的主要创新在于其“技能系统”，这是积累和复用程序性知识的主要单元。技能分为两类：**Type-1技能（GUI操作技能）** 和 **Type-2技能（分析脚本技能）**。

**Type-1技能** 专门用于克服专有仪器软件缺乏开放API的挑战。其构建过程依赖于人类专家在GUI软件上的演示。智能体记录交互轨迹（如鼠标、键盘操作和屏幕视觉变化），并将其抽象为结构化、可参数化的技能，而非简单的坐标回放。这些技能封装了操作流程、可配置参数（如加速电压、放大倍数）、状态检查以及基于GUI状态的条件分支，甚至能编码专家在操作中的隐性启发式知识（如根据实时预览调整采集时间），从而成为可复用的操作专业知识载体。

**Type-2技能** 则针对数据后处理与分析阶段的多样性和定制化需求。它采用对话式脚本生成范式：研究人员用自然语言描述分析意图（如加载数据、寻峰、基线校正、拟合、导出结果），智能体利用代码生成能力，结合科学计算库（如NumPy, SciPy, matplotlib）合成可执行脚本。用户可即时运行并迭代优化脚本，验证后将其打包为具有明确输入输出定义和依赖关系的标准化技能，供未来任务直接调用，避免了重复开发。

这两个技能类型在运行时平台上互补协作，形成一个闭环工作流。例如，Type-1技能操作仪器软件完成数据采集和导出，导出的数据随即由Type-2技能进行定量分析和报告生成，分析结果又可指导下一轮仪器操作。此外，平台支持从外部仓库（如GitHub）导入技能，使系统具备高度的可扩展性，允许不同实验室根据自身设备和协议定制能力集。

总之，Owl-AuraID通过**技能中心化的架构设计**、**GUI原生与对话优先的交互模型**、以及**Type-1/Type-2技能的分类与融合**，构建了一个既能操作封闭GUI软件又能执行灵活数据分析的实用系统，为自主实验室提供了一个可扩展的基础，并实现了通过可复用技能积累来演进实验室智能的路径。

### Q4: 论文做了哪些实验？

论文的实验主要围绕Owl-AuraID系统在科学仪器智能驱动和科学数据智能分析两大核心能力展开。

**实验设置与数据集/基准测试：**
系统采用软硬件协同的具身智能体架构，通过GUI原生范式直接操作仪器软件界面。实验覆盖了十类精密仪器，包括光谱仪（UV-Vis、PL、FTIR）、显微成像设备（SEM、Micro-CT）及其附属分析模块（EDS）等，形成了多模态工作流。实验涉及物理样本的高精度操作（如亚毫米级比色皿对准）、仪器软件自主控制（通过CUA驱动的操作技能）以及基于实时视觉反馈的闭环参数优化。

**对比方法与主要结果：**
研究强调其方法超越了基于API的静态自动化或设备特定脚本的局限性。通过技能中心化框架，系统将Type-1（GUI操作）和Type-2（数据分析）技能整合到端到端工作流中，实现了从物理样本处理到科学解读的全流程自主化。

**关键数据指标与结果：**
1.  **仪器操作：** 在光谱表征中，系统能自主配置采集参数，动态优化测量设置以确保获取最优表征结果。在SEM成像中，能基于实时反馈调整加速电压、放大倍数和焦距等关键参数，以获取最佳对比度和分辨率。
2.  **数据分析：** 系统展示了智能数据分析能力，包括对原始UV-Vis数据进行自动基线校正以消除背景噪声；在基线校正后的光谱中自动识别吸收峰的位置和强度；通过比对大型红外数据库，对FTIR光谱实现特征吸收峰的精确匹配与功能基团归属。这些功能消除了繁琐的人工检查与比对过程。

综上所述，实验验证了Owl-AuraID能够跨异构仪器，无缝集成物理操控、GUI交互与科学数据采集，形成一个统一的自表征生态系统，并为自主实验室提供了可扩展的实践基础。

### Q5: 有什么可以进一步探索的点？

该论文提出的GUI原生范式虽具创新性，但其局限性在于高度依赖图形界面的稳定性与一致性，当仪器软件更新或界面布局变化时，系统可能失效。此外，当前技能库的泛化能力仍局限于已适配的十类仪器，对于未见过的新型仪器或非标准界面，缺乏零样本或小样本学习能力。

未来研究方向可围绕以下三点展开：一是增强系统的鲁棒性与自适应能力，例如引入视觉语言模型（VLM）对GUI元素进行语义理解，使系统能动态解析新界面；二是发展跨仪器的元技能学习框架，将操作抽象为高阶任务（如“参数扫描”“样品对准”），提升技能复用性；三是构建人机协作机制，允许科学家以自然语言介入或修正自动化流程，形成混合主动的决策闭环。此外，将系统与实验室数字孪生结合，可实现虚拟调试与风险预测，进一步推动自主实验室向强人工智能演进。

### Q6: 总结一下论文的主要内容

该论文提出了Owl-AuraID 1.0，这是一个用于自主科学仪器操作与数据分析的智能系统。其核心问题是解决高通量科学表征中因依赖专有图形用户界面（GUI）以及现有API系统泛化性有限而导致的自动化瓶颈。为此，系统采用了一种“GUI原生”范式，通过模拟人类专家操作GUI的方式来控制各类仪器，构建了一个软硬件协同的具身智能体。

方法上，系统以技能为中心，将Type-1（GUI操作）技能和Type-2（数据分析）技能整合到端到端的工作流中，从而将物理样品处理与科学解读连接起来。它展示了对傅里叶变换红外光谱、核磁共振、原子力显微镜、热重分析等十类精密仪器及多种工作流程的广泛覆盖能力。

主要结论是，Owl-AuraID为自主实验室提供了一个实用且可扩展的基础框架，并通过可复用的操作与分析技能，为实现实验室智能的持续演进指明了一条路径。
