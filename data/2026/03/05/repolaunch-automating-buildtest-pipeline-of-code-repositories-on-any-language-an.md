---
title: "RepoLaunch: Automating Build&Test Pipeline of Code Repositories on ANY Language and ANY Platform"
authors:
  - "Kenan Li"
  - "Rongzhi Li"
  - "Linghao Zhang"
  - "Qirui Jin"
  - "Liao Zhu"
  - "Xiaosong Huang"
  - "Geng Zhang"
  - "Yikai Zhang"
  - "Shilin He"
  - "Chengxing Xie"
  - "Xin Zhang"
  - "Zijian Jin"
  - "Bowen Li"
  - "Chaoyun Zhang"
  - "Yu Kang"
  - "Yufan Huang"
  - "Elsie Nallipogu"
  - "Saravan Rajmohan"
  - "Qingwei Lin"
  - "Dongmei Zhang"
date: "2026-03-05"
arxiv_id: "2603.05026"
arxiv_url: "https://arxiv.org/abs/2603.05026"
pdf_url: "https://arxiv.org/pdf/2603.05026v1"
categories:
  - "cs.SE"
  - "cs.LG"
  - "cs.MA"
tags:
  - "Agent 工具使用"
  - "软件工程自动化"
  - "Agent 数据合成"
  - "Agent 评测/基准"
  - "多智能体系统"
relevance_score: 7.5
---

# RepoLaunch: Automating Build&Test Pipeline of Code Repositories on ANY Language and ANY Platform

## 原始摘要

Building software repositories typically requires significant manual effort. Recent advances in large language model (LLM) agents have accelerated automation in software engineering (SWE). We introduce RepoLaunch, the first agent capable of automatically resolving dependencies, compiling source code, and extracting test results for repositories across arbitrary programming languages and operating systems. To demonstrate its utility, we further propose a fully automated pipeline for SWE dataset creation, where task design is the only human intervention. RepoLaunch automates the remaining steps, enabling scalable benchmarking and training of coding agents and LLMs. Notably, several works on agentic benchmarking and training have recently adopted RepoLaunch for automated task generation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决软件工程中自动化构建和测试代码仓库的难题。研究背景是，随着大语言模型（LLM）代理在软件工程自动化中的应用日益增多，出现了许多需要在可执行环境中评估或训练LLM代理的基准（如SWE-bench系列）。然而，现实中的代码仓库构建过程通常需要大量人工努力，因为仓库配置差异大、文档不全、平台特定的依赖和编译错误频发，导致构建过程充满试错。现有方法（如GitTaskBench）的不足在于，它们往往将仓库构建与问题解决合并为一个任务，这掩盖了构建阶段本身的挑战（研究表明约65%的代理失败发生在构建可执行环境阶段），且无法大规模、自动化地创建和管理预构建的可执行仓库沙箱，限制了评估和训练数据的规模。

因此，本文要解决的核心问题是：如何设计一个能够全自动处理任意编程语言、任意操作系统平台的代码仓库构建与测试的智能代理，以消除人工干预的繁琐，并支持大规模软件工程数据集的自动化创建。具体而言，RepoLaunch被提出来自主探索仓库、安装依赖、编译代码并执行回归测试，从而为评估和训练编码代理及LLM提供可扩展的自动化管道。

### Q2: 有哪些相关研究？

相关研究主要分为两类：规则驱动的自动化构建工具和基于智能体的初步探索。

在规则驱动的方法中，Oss-Fuzz-Gen、Starter、Yeoman generator 等工具依赖预定义的构建指令或模板文件（如 Dockerfile）来构建仓库。Pipreqs、DockerizeMe 和 DockerGen 则从项目内容推断依赖关系。SWE-MERA 使用硬编码规则为 Python 仓库创建基准测试，但其构建成功率和任务覆盖范围有限。这些方法的共同局限在于难以应对 GitHub 公共仓库中项目设置和结构的巨大差异，凸显了需要智能体进行个案分析的必要性。

在基于智能体的方法中，Repo2Run、SWE-bench-Live 和 SWE-rebench 等研究初步探索了在 Linux 环境下为 Python 仓库设置构建和测试流程。它们利用大语言模型生成 Dockerfile 或执行命令，并通过简单的 pytest 解析器管理测试状态。然而，这些工作主要针对 Python 这一语言单一、构建命令（如 `pip install .`）和测试框架（pytest）相对统一的场景。本文提出的 RepoLaunch 则是对这些初步工作的重大扩展，它旨在解决跨任意编程语言和操作系统的通用自动化构建与测试难题，这需要复杂的探索过程，而非直接生成 Dockerfile 所能覆盖。

### Q3: 论文如何解决这个问题？

RepoLaunch 通过一个多智能体工作流来解决软件仓库自动化构建与测试的问题，其核心方法是将整个过程分解为三个阶段：准备、构建和发布，并利用多个专门化的 LLM 智能体协同完成。整体框架设计旨在处理任意编程语言和操作系统环境下的仓库，关键在于将复杂的构建过程形式化，并通过智能体迭代探索与验证来找到可行的解决方案。

在架构设计上，系统首先依赖于两个关键工具：预构建的基础镜像（为不同语言提供最小化操作系统环境和基本依赖）和语言特定的构建/测试指令（提供常见框架的指导）。这些工具是系统实现泛化能力的基础。主要工作流包含三个核心智能体模块：
1.  **准备智能体**：扫描仓库文件树，识别配置文件，据此选择合适的基础镜像，启动容器并复制仓库代码，将相关信息传递给后续阶段。
2.  **设置智能体**：核心构建模块。它利用 Bash 工具在容器内执行 shell 命令，并配备网络搜索工具以获取外部知识来解决构建错误。其任务是安装依赖、编译代码，并尝试寻找回归测试命令。如果大部分测试通过，则将容器移交验证智能体。
3.  **验证智能体**：负责验证构建结果，检查命令历史以识别能报告单个测试状态的测试命令。如果测试通过率达标，则提交容器为新镜像；否则将失败反馈给设置智能体进行重试，形成一个纠正循环。

在发布阶段，**组织智能体** 会从成功记录中提取可复用的构件。其关键技术包括：
*   **生成最小化重建命令序列**：过滤和优化设置智能体的命令历史，去除冗余和失败步骤，生成一组能在代码修改后重新安装依赖和编译项目的最小命令集，并通过执行验证其正确性。
*   **生成测试命令与解析器**：从验证智能体的历史中提炼出能输出每个测试用例状态的最小测试命令集。同时，生成一个测试日志解析器（一个 Python 函数），将测试输出解析为从测试用例名到状态的结构化映射。系统优先选择能产生结构化输出（如 JSON/XML）的测试命令以降低解析难度。

创新点主要体现在：1) **形式化的问题定义与分阶段求解**：将仓库构建与管理抽象为状态转换和验证函数，并分解为可操作的智能体任务。2) **多智能体协作与纠错循环**：通过设置与验证智能体间的反馈循环，有效缓解了 LLM 的幻觉问题，提高了构建的可靠性。3) **自动化生成持久化工件**：不仅完成一次性构建，还能自动生成最小重建命令、测试解析器等，支持仓库的长期管理与重复测试，这是实现自动化基准创建等应用的关键。4) **广泛的适用性**：通过基础镜像和语言指令的抽象，系统能够跨语言和平台工作，实验涵盖了从 Python、C++ 到 Windows 环境等多种场景。

### Q4: 论文做了哪些实验？

论文进行了两项主要实验。实验一（RepoLaunch自动化SWE数据集创建）：实验设置上，利用RepoLaunch为SWE-bench-Live从真实的GitHub issues和PRs生成任务实例，并测量其在构建（Build）和发布（Release）阶段的成功率，同时分析来自真实仓库和提交的失败模式。数据集方面，创建了两个新子集：1) SWE-bench-Live/MultiLang，涵盖C/C++、C#、Java、Golang、JS/TS和Rust，从2025年7-8月的PRs中生成413个任务实例（来自234个仓库）；2) SWE-bench-Live/Windows，涵盖多种语言（包括Python）的Windows特定任务，从2025年全年问题中筛选出507个，并随机抽样400个进行评估。关键数据指标显示，MultiLang子集的任务规模（413个实例）已超过原有SWE-bench-Multilingual基准（300个实例）。

实验二（与相关工作的比较）：实验设置上，将RepoLaunch应用于为现有人工标注的SWE基准（SWE-bench-Verified和SWE-bench-Multilingual）构建沙箱镜像并提取测试状态。为评估对依赖漂移的鲁棒性，为每个仓库选择了时间间隔最远的三个任务实例。对比方法包括：1) SWE-agent（仅使用bash和文件编辑工具的通用SWE智能体）；2) repo2run（首个仓库构建智能体，但限于Python基础镜像和硬编码命令）。主要结果方面，RepoLaunch在构建成功率和跨平台/语言支持上展现出优势，而基线方法因语言限制或工具简化而存在不足。实验还评估了流行SWE智能体和LLM在新创建数据集上的表现，为此实现了一个Windows兼容的基准智能体（Win-agent）。超参数设置上，RepoLaunch的Setup Agent在Linux和Windows上分别最多允许60和90步，其他阶段限20步，每个bash命令超时30分钟；基线智能体的最大步数设为120步。

### Q5: 有什么可以进一步探索的点？

RepoLaunch的局限性主要体现在计算成本和任务规模上。作为多轮自由交互的智能体，它依赖大量LLM调用，导致token消耗高昂；同时，构建大型代码库需要密集的CPU计算和磁盘I/O，目前受限于资源仅创建了481个任务实例。未来可从三方面深入探索：一是优化效率，如通过硬编码的测试日志解析器覆盖常见测试框架，减少对LLM的依赖，或引入轻量级规则引擎处理标准化构建步骤；二是扩展跨平台与任务多样性，除已演示的Linux和Windows外，可纳入macOS、嵌入式系统等环境，并持续集成GitHub等平台的实时问题，构建动态演进的基准数据集；三是增强鲁棒性，针对依赖解析失败、环境配置冲突等边缘案例，可结合符号执行或静态分析预判风险，提升自动化流水线的成功率。这些改进将推动RepoLaunch从“可用”向“高效、通用、可靠”演进，为代码智能体训练与评估提供更强大的基础设施。

### Q6: 总结一下论文的主要内容

RepoLaunch 是一种基于大语言模型（LLM）的智能体，旨在自动化软件仓库的构建和测试流程。其核心贡献在于首次实现了对任意编程语言和任意操作系统的代码仓库进行自动化的依赖解析、源代码编译和测试结果提取，从而显著减少了传统软件开发中所需的大量手动工作。

论文提出的方法利用LLM智能体技术，将构建和测试过程自动化。为了展示其效用，作者进一步设计了一个全自动的软件工程数据集创建流程，其中仅需人工进行任务设计，其余步骤均由RepoLaunch自动完成。这使得面向编码智能体和LLMs的大规模基准测试与训练成为可能。

主要结论显示，RepoLaunch在构建和测试成功率上显著超越了基线方法。该工具已开源，并已被应用于实际场景，例如GLM-5基础模型已采用其进行智能体训练，同时多项关于智能体基准测试和训练的研究工作也已开始使用RepoLaunch来自动生成任务，证明了其在推动软件工程自动化和AI训练方面的实用价值与影响力。
