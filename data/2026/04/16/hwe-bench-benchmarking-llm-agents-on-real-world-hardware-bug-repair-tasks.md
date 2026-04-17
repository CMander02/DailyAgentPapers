---
title: "HWE-Bench: Benchmarking LLM Agents on Real-World Hardware Bug Repair Tasks"
authors:
  - "Fan Cui"
  - "Hongyuan Hou"
  - "Zizhang Luo"
  - "Chenyun Yin"
  - "Yun Liang"
date: "2026-04-16"
arxiv_id: "2604.14709"
arxiv_url: "https://arxiv.org/abs/2604.14709"
pdf_url: "https://arxiv.org/pdf/2604.14709v1"
categories:
  - "cs.AI"
tags:
  - "Agent Benchmark"
  - "Hardware Bug Repair"
  - "Tool Use"
  - "Repository-Level Evaluation"
  - "Agent Framework Comparison"
  - "Failure Analysis"
relevance_score: 7.5
---

# HWE-Bench: Benchmarking LLM Agents on Real-World Hardware Bug Repair Tasks

## 原始摘要

Existing benchmarks for hardware design primarily evaluate Large Language Models (LLMs) on isolated, component-level tasks such as generating HDL modules from specifications, leaving repository-scale evaluation unaddressed. We introduce HWE-Bench, the first large-scale, repository-level benchmark for evaluating LLM agents on real-world hardware bug repair tasks. HWE-Bench comprises 417 task instances derived from real historical bug-fix pull requests across six major open-source projects spanning both Verilog/SystemVerilog and Chisel, covering RISC-V cores, SoCs, and security roots-of-trust. Each task is grounded in a fully containerized environment where the agent must resolve a real bug report, with correctness validated through the project's native simulation and regression flows. The benchmark is built through a largely automated pipeline that enables efficient expansion to new repositories. We evaluate seven LLMs with four agent frameworks and find that the best agent resolves 70.7% of tasks overall, with performance exceeding 90% on smaller cores but dropping below 65% on complex SoC-level projects. We observe larger performance gaps across models than commonly reported on software benchmarks, and difficulty is driven by project scope and bug-type distribution rather than code size alone. Our failure analysis traces agent failures to three stages of the debugging process: fault localization, hardware-semantic reasoning, and cross-artifact coordination across RTL, configuration, and verification components, providing concrete directions for developing more capable hardware-aware agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前硬件设计领域缺乏真实、复杂场景下评估大型语言模型（LLM）智能体能力基准的问题。研究背景是，尽管LLM在电子设计自动化（EDA）领域的潜力日益受到关注，但现有基准（如VerilogEval、RTLLM）主要评估模型在孤立、组件级任务（例如根据自然语言描述生成硬件描述语言模块）上的表现，而忽略了更贴近实际工程需求的仓库级评估。现有方法的不足在于，它们未能让智能体在完整项目环境中工作，即需要智能体导航整个代码仓库、处理异构工件（如RTL源代码、验证组件、IP配置、构建脚本），并调用项目原生的构建和仿真流程进行验证。因此，一个核心的开放性问题尚未得到解答：基于LLM的智能体能否在真实硬件项目的完整上下文中执行仓库级的错误修复？

本文要解决的核心问题正是填补这一空白，即构建首个大规模、仓库级的基准测试，用于在真实世界的硬件错误修复任务上评估LLM智能体。为此，论文提出了HWE-Bench。该基准从六个主要的开源硬件项目（涵盖Verilog/SystemVerilog和Chisel，涉及RISC-V内核、片上系统和安全信任根）中提取了417个基于真实历史错误修复拉取请求的任务实例。每个任务都置于完全容器化的环境中，要求智能体解决真实的错误报告，并通过项目原生的仿真和回归流程来验证修复的正确性。通过解决现有基准在任务孤立性、评估环境脱离真实项目上下文等方面的不足，HWE-Bench旨在为评估和开发更强大、具备硬件工程意识的LLM智能体提供标准化、可复现的基础设施。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为硬件工程评测基准、软件工程评测基准以及自动化RTL修复工具三类。

在**硬件工程评测基准**方面，早期工作如VerilogEval和RTLLM聚焦于从规范生成独立模块的组件级代码生成任务，并通过仿真进行正确性检查。CVDP扩展了任务范围（如验证、调试）和规模，但仍属于问题范畴而非仓库范畴。HWFixBench虽涉及真实仓库数据的错误修复，但停留在文件级输入，并依赖基于LLM的语义匹配而非执行验证。本文的HWE-Bench则通过将任务嵌入完整仓库环境，并利用项目原生的仿真流程进行验证，解决了上述局限。

在**软件工程评测基准**方面，SWE-bench等建立了基于真实GitHub问题、以单元测试验证的仓库级执行评估范式。本文借鉴了这一方法论，但将其应用于硬件领域，需处理异构EDA工具链和非标准化验证流程，基础设施要求有根本不同。

在**自动化RTL修复工具**方面，传统工具如CirFix和RTL-Repair在特定模块和给定测试平台下搜索满足测试的最小补丁。相比之下，HWE-Bench的任务设定更广泛：智能体仅接收自然语言错误报告和完整仓库，需自主定位故障、导航代码库并调用项目原生的构建和仿真流程来验证修复。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为HWE-Bench的大规模、仓库级基准测试来解决评估LLM智能体在真实硬件错误修复任务上的能力缺失问题。其核心方法是一个高度自动化的多阶段流水线，旨在从真实开源硬件项目中提取可验证的错误修复任务。

整体框架分为四个主要阶段：仓库选择、PR收集与过滤、测试生成与验证，以及最终的问题陈述生成。首先，从GitHub中筛选出六个具有代表性、维护良好且使用Verilog/SystemVerilog或Chisel的开源硬件项目，涵盖了从简单RISC-V核心到复杂SoC和安全根信任模块的多种设计类型和复杂度。

关键技术在于其创新的过滤与验证流程。针对硬件仓库中大量与调试无关的PR（如文档更新、工具链升级），流水线采用了规模过滤和基于LLM的语义过滤两层机制，以精准识别出真正的硬件设计错误修复。随后，一个关键的自动化测试生成与验证模块被引入：利用LLM智能体根据项目特定的验证流程生成测试脚本和环境准备脚本，并将每个任务实例打包成Docker容器。验证过程自动运行测试，确保在应用修复前失败（FAIL），应用真实补丁后通过（PASS），并且测试与具体补丁实现解耦，以接受其他正确的修复方案。

主要的创新点包括：1) **仓库级与真实性**：首次在完全容器化的真实项目环境中评估智能体，要求其解决源自历史错误报告和拉取请求的实际问题，并通过项目原生的仿真和回归流程验证正确性。2) **自动化构建流水线**：实现了从海量PR中高效筛选、验证和打包任务实例的自动化流程，克服了传统基准测试需要大量人工标注的瓶颈，并支持向新仓库高效扩展。3) **问题陈述生成与防泄漏**：使用独立的LLM智能体为每个实例生成自包含的问题描述，替代原始可能不完整或结构混乱的issue文本，并设有自动化审查步骤防止无意中泄露修复线索。4) **反映硬件开发特性**：基准测试中的补丁通常是跨多个文件的中等规模修改，要求智能体在RTL设计、配置和验证组件之间进行协调推理，这直接反映了硬件错误修复的工程实践，与软件基准测试的补丁分布形成鲜明对比。

### Q4: 论文做了哪些实验？

论文在HWE-Bench基准上进行了全面的实验评估。实验设置方面，研究者评估了七种先进的大语言模型（LLM），包括专有模型GPT-5.4、Claude Opus 4.6、Claude Sonnet 4.6，以及开源模型GLM 5.1、Qwen3.6 Plus、DeepSeek V3.2和Kimi K2.5。每个模型都与其官方或主流的代理框架（如Claude Code、Codex CLI、Kimi CLI或OpenHands）配对，以模拟实际部署场景。评估协议规定，每个代理在容器化环境中独立解决任务，执行预算为6小时墙钟超时和500次迭代，最终通过项目原生的仿真和回归流程验证补丁的正确性。

使用的数据集是论文提出的HWE-Bench基准，它包含417个从真实历史bug修复拉取请求中提取的任务实例，覆盖六个主要的开源硬件项目（如OpenTitan、Ibex、CVA6、Caliptra、XiangShan、Rocket Chip），涉及Verilog/SystemVerilog和Chisel两种硬件描述语言，涵盖RISC-V核心、SoC和安全信任根。

主要对比了不同模型和代理框架在基准上的表现。关键数据指标是**解决率**（Resolved Rate，即补丁使验证测试从FAIL转为PASS的任务比例）和**文件级精确度**（File-Level Precision，即代理修改的文件中出现在真实补丁中的比例）。

主要结果显示：最佳代理（GPT-5.4 xhigh with Codex CLI）的总体解决率为**70.7%**。在较小的核心项目（如CVA6、Ibex、Caliptra）上，性能超过**90%**，但在复杂的SoC级项目（如OpenTitan、XiangShan）上则降至**65%**以下。开源模型中GLM 5.1表现最佳，解决率为**63.1%**。文件级精确度方面，Claude Opus 4.6最高（**0.928**），而GPT-5.4虽然解决率最高，但精确度最低（**0.619**），表明其补丁范围更广。与软件基准（如SWE-bench）相比，模型在硬件任务上的性能差距更大（从不到8%扩大到超过23%），且所有模型均未达到接近饱和的性能，表明该基准对当前代理构成了持续挑战。失败分析将代理失败归因于调试过程的三个阶段：故障定位、硬件语义推理以及跨RTL、配置和验证组件的工件协调。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其局限性主要体现在评估范围、任务复杂性和模型能力边界上。首先，HWE-Bench虽然覆盖了六个开源项目，但主要集中在RISC-V核心、SoC和安全信任根等领域，未来可扩展至更多样化的硬件设计类型（如模拟电路、FPGA专用设计）和更广泛的bug类型（如时序、功耗问题）。其次，当前基准主要评估修复已知历史bug，但现实场景中更需要处理未知或复杂交互bug，未来可引入动态bug生成或模糊测试任务来增强挑战性。

从改进思路看，论文指出的三大失败模式（故障定位、硬件语义推理、跨构件协调）为未来研究提供了明确方向。例如，可探索结合形式化验证或静态分析工具来增强LLM的故障定位能力；设计硬件领域特定的推理模块，帮助模型理解时钟、并发、硬件层次结构等语义；开发多智能体协作框架，专门处理RTL、配置和验证组件间的协调问题。此外，当前评估的LLM和智能体框架有限，未来可纳入更多开源或专业模型，并探索定制化训练（如硬件代码预训练）对性能的影响。最后，基准的自动化构建流程虽支持扩展，但如何保证新任务的代表性和评估可靠性仍需进一步规范。

### Q6: 总结一下论文的主要内容

该论文提出了首个针对真实硬件漏洞修复任务的大规模仓库级基准测试HWE-Bench，旨在评估大语言模型（LLM）智能体在复杂硬件设计场景中的实际能力。核心问题是现有基准多局限于组件级任务（如根据规范生成HDL模块），缺乏对仓库级综合调试能力的评估。

方法上，HWE-Bench从六个主要开源硬件项目（涵盖Verilog/SystemVerilog和Chisel，涉及RISC-V内核、SoC和安全信任根）的真实历史漏洞修复拉取请求中构建了417个任务实例。每个任务置于完全容器化的环境中，要求智能体根据真实漏洞报告进行修复，并通过项目原生的仿真和回归流程验证正确性。基准通过高度自动化流水线构建，便于扩展。研究评估了七种LLM与四种智能体框架。

主要结论显示，最佳智能体整体任务解决率为70.7%，在较小内核上超过90%，但在复杂SoC级项目中低于65%。性能差距大于软件基准常见报告，任务难度主要由项目范围和漏洞类型分布驱动，而非代码量。失败分析揭示了智能体在调试三阶段的不足：故障定位、硬件语义推理以及跨RTL、配置和验证组件的多工件协调，为开发更强大的硬件感知智能体指明了方向。
