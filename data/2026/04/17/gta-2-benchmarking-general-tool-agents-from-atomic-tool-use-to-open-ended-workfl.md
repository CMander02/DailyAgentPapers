---
title: "GTA-2: Benchmarking General Tool Agents from Atomic Tool-Use to Open-Ended Workflows"
authors:
  - "Jize Wang"
  - "Xuanxuan Liu"
  - "Yining Li"
  - "Songyang Zhang"
  - "Yijun Wang"
  - "Zifei Shan"
  - "Xinyi Le"
  - "Cailian Chen"
  - "Xinping Guan"
  - "Dacheng Tao"
date: "2026-04-17"
arxiv_id: "2604.15715"
arxiv_url: "https://arxiv.org/abs/2604.15715"
pdf_url: "https://arxiv.org/pdf/2604.15715v1"
github_url: "https://github.com/open-compass/GTA"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Tool Use"
  - "Benchmark"
  - "Workflow"
  - "Evaluation"
  - "Agent Framework"
  - "General-Purpose Agent"
relevance_score: 9.0
---

# GTA-2: Benchmarking General Tool Agents from Atomic Tool-Use to Open-Ended Workflows

## 原始摘要

The development of general-purpose agents requires a shift from executing simple instructions to completing complex, real-world productivity workflows. However, current tool-use benchmarks remain misaligned with real-world requirements, relying on AI-generated queries, dummy tools, and limited system-level coordination. To address this, we propose GTA-2, a hierarchical benchmark for General Tool Agents (GTA) spanning atomic tool use and open-ended workflows. Built on real-world authenticity, it leverages real user queries, deployed tools, and multimodal contexts. (i) GTA-Atomic, inherited from our prior GTA benchmark, evaluates short-horizon, closed-ended tool-use precision. (ii) GTA-Workflow introduces long-horizon, open-ended tasks for realistic end-to-end completion. To evaluate open-ended deliverables, we propose a recursive checkpoint-based evaluation mechanism that decomposes objectives into verifiable sub-goals, enabling unified evaluation of both model capabilities and agent execution frameworks (i.e., execution harnesses). Experiments reveal a pronounced capability cliff: while frontier models already struggle on atomic tasks (below 50%), they largely fail on workflows, with top models achieving only 14.39% success. Further analysis shows that checkpoint-guided feedback improves performance, while advanced frameworks such as Manus and OpenClaw substantially enhance workflow completion, highlighting the importance of execution harness design beyond the underlying model capacity. These findings provide guidance for developing reliable personal and professional assistants. Dataset and code will be available at https://github.com/open-compass/GTA.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型（LLM）智能体（Agent）评估领域存在的与现实需求脱节的问题。研究背景是，随着LLM智能体的发展，其目标已从执行简单指令转向完成复杂的现实世界生产力工作流（如撰写研究报告、制定详细计划）。然而，现有的工具使用评估基准（如ToolBench、APIBench）存在显著不足：它们通常依赖AI生成的、已隐含解决步骤的查询，使用模拟执行的虚拟工具，并局限于纯文本环境。这种简化设置无法真实评估智能体在现实、多模态情境下的端到端问题解决能力。

针对这些不足，本文的核心目标是构建一个更真实、更全面的评估基准，以系统性地衡量通用工具智能体从原子工具使用到开放式工作流完成的综合能力。为此，论文提出了GTA-2这一分层基准。它具体解决两个层面的问题：一是通过继承并发展的GTA-Atomic部分，继续评估智能体在短视域、封闭式原子工具使用上的精确性；二是通过新引入的GTA-Workflow部分，解决现有基准普遍缺乏对长视域、开放式、跨领域工作流进行评估的空白。GTA-Workflow旨在模拟现实的生产力场景，其任务没有唯一确定的答案，要求智能体完成端到端的交付成果。为了评估这种开放式任务，论文还设计了一个基于递归检查点的评估机制，将总体目标分解为可验证的子目标，从而实现了对模型能力和智能体执行框架（即执行“马具”）的统一、可解释的评估。最终，该研究揭示了当前前沿模型在从原子任务到工作流任务上存在的显著“能力悬崖”，并强调了执行框架设计与模型能力同等重要。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为方法类、系统框架类和评测基准类。

在**方法类**方面，早期研究如 Toolformer 和 ReAct 奠定了大语言模型自主调用工具的基础范式，将工具使用视为推理与行动交织的过程。后续研究则聚焦于提升工具选择的可靠性、参数预测和多步决策。此外，像思维链（CoT）和思维树（ToT）这类技术探索了结构化推理和多路径问题分解，为复杂任务规划提供了思路。

在**系统框架类**方面，早期系统如 LangChain 和 AutoGPT 提供了工具集成的一般性抽象。近期研究则转向更结构化、系统级的设计，例如引入持久化记忆的 Agent 操作系统，以及像 OpenClaw、MiniMax Agent 这样集成工具、记忆与协调的统一执行环境。专门针对复杂、开放式工作流的智能体（如 Claude Code、Kortix、Manus）也相继出现，其成功标准在于完成最终交付物，而非执行单一工具调用。

在**评测基准类**方面，早期基准如 ToolBench 和 APIBench 支持大规模 API 评估，但常依赖合成查询或模拟环境，与现实存在差距。为提高真实性，出现了 SWE-bench、OSWorld 等高保真领域专用基准，以及专注于长视野工作流的 OdysseyBench 和 DeepPlanning，但其领域特异性限制了跨领域通用性评估。近期 GAIA-2 等基准增加了任务多样性，但仍依赖模拟执行。

**本文与这些工作的关系和区别在于**：GTA-2 旨在填补现有基准在**真实性、通用性和诊断深度**上的空白。与依赖合成数据或模拟环境的基准不同，GTA-2 基于真实用户查询、已部署工具和多模态上下文构建。它通过分层设计（原子工具使用与开放式工作流）和递归检查点评估机制，统一评估**模型能力与智能体执行框架**（即执行载体）的影响，而现有基准大多假设固定执行设置，对此探讨有限。因此，GTA-2 提供了一个在真实、开放场景下，联合评估核心模型与系统框架对端到端任务完成效果的统一基准。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为GTA-2的层次化基准测试来解决评估通用工具智能体从原子工具使用到开放式工作流完成能力的现实需求与当前基准不匹配的问题。其核心方法是建立一个基于真实世界要素、包含两个层次任务的统一评估框架。

**整体框架与主要模块**：
GTA-2由两个主要组件构成：GTA-Atomic和GTA-Workflow。GTA-Atomic继承自前代基准，专注于评估短视域、封闭式的原子工具使用精度。GTA-Workflow则是本工作的主要贡献，它引入了一个独立的框架，用于评估长视域、开放式的真实生产力工作流任务。两者共同构建在一个共享的真实性基础上，包括：1）**真实用户查询**，源自人类真实需求；2）**真实部署工具**，支持可执行的端到端交互；3）**真实多模态上下文**，要求智能体在现实输入下操作。

**GTA-Workflow的关键设计与创新点**：
1.  **交付物导向的任务制定**：与有明确答案的原子任务不同，GTA-Workflow专注于具有明确交付物（如报告、代码、多媒体制品）的长时程任务。评估完全围绕最终输出质量，而非中间步骤，从而捕捉智能体完成真实世界目标的端到端有效性。这避免了因解决方案路径多样且智能体内部编排不透明而导致的轨迹匹配评估难题。
2.  **基于检查点的目标驱动分解**：为了对开放式任务进行结构化评估，每个工作流被分解成一个**目标导向的检查点层次树**。每个检查点描述的是期望的结果状态（例如“生成一段时长在2.5至3.5分钟之间的音频剪辑”），而非规定的动作序列。这使得智能体可以采用多样化的执行策略，同时将评估与具体执行过程解耦。
3.  **递归的、基于检查点的评估机制**：这是评估开放式交付物的核心创新。评估不检查推理或工具使用，而是由一个强大的LLM作为“法官”，根据检查点树中定义的目标要求，对最终交付物进行评分。具体流程是：LLM法官为每个叶子检查点（即可验证的子目标）在0-10分范围内打分；然后通过算法递归地聚合这些分数，父节点得分是其子节点得分的加权和。这提供了统一的完成度度量，同时保留了诊断的细粒度。
4.  **半自动化的任务构建流程**：通过结合LLM生成与人工验证的管道来构建高质量工作流任务。流程包括初始任务生成、任务细化与增强（如增加复杂性、澄清目标）、自动验证（确保检查点结果导向、不引用工具调用）以及最终的人工核查。此过程确保了任务的真实性、多样性和可评估性。

**架构设计的核心思想**是通过这种层次化、交付物导向且基于检查点分解的框架，实现对智能体**模型能力**和**执行框架（或称执行工具套）设计**两方面的系统性分析。实验表明，前沿模型在原子任务上已表现不佳（低于50%），在工作流上更是大幅失败（顶级模型成功率仅14.39%），揭示了显著的“能力悬崖”。同时，分析发现检查点引导的反馈能提升性能，而先进执行框架（如Manus, OpenClaw）能显著增强工作流完成度，这凸显了超越底层模型能力的执行工具套设计的重要性。

### Q4: 论文做了哪些实验？

本论文的实验主要围绕其提出的GTA-2基准展开，分为原子工具使用（GTA-Atomic）和开放式工作流（GTA-Workflow）两部分。

**实验设置与数据集**：实验在OpenCompass评估平台上进行，使用80GB GPU。默认采用Lagent作为智能体框架，以ReAct作为工具调用范式。GTA-2基准基于真实用户查询、已部署工具和多模态上下文构建，确保了真实性。

**对比方法与主要结果**：
1.  **GTA-Atomic实验**：评估了8个代表性大语言模型在短视域、封闭式任务中的基础工具使用精度。实验采用两种模式：**逐步模式**（Step-by-step）评估细粒度精度，**端到端模式**（End-to-End）评估动态执行。关键指标包括指令遵循准确率（InstAcc）、工具选择准确率（ToolAcc）、参数预测准确率（ArgAcc）、总结准确率（SummAcc）以及最终答案准确率（AnsAcc）。结果显示，前沿模型在原子任务上已表现挣扎，整体成功率低于50%。例如，GPT-4o在逐步模式下的ToolAcc为70.38%，但ArgAcc仅为35.19%；在端到端模式下，其AnsAcc为41.52%。
2.  **GTA-Workflow实验**：评估了13个前沿模型在长视域、开放式场景下的智能体性能。采用**端到端、以交付物为中心**的评估方式，使用基于递归检查点的机制进行评判。关键指标包括根成功率（Root SR）、叶成功率（Leaf SR）和根分数（Root Score）。实验揭示了一个显著的能力断层：顶级模型在工作流任务上基本失败，成功率极低。表现最好的Gemini-2.5-Pro的Root SR仅为14.39%，Leaf SR为28.46%。开源模型如Llama-3.1-70B的Root SR更是低至0.76%。
3.  **智能体框架（执行工具）对比实验**：在GTA-Workflow的一个30任务子集上，对比了不同执行框架（如Lagent, OpenClaw, Manus, Kortix）的效果。设置了**受控对比**（固定基础模型）和**系统级对比**（使用框架默认配置）。结果表明，先进的框架如Manus和OpenClaw能显著提升工作流完成度。例如，在同样使用Claude-Sonnet-4.5模型时，OpenClaw将Leaf SR从Lagent的10.14%大幅提升至73.55%，Root SR从0%提升至50%。这凸显了执行工具设计的重要性可能超越底层模型能力本身。

### Q5: 有什么可以进一步探索的点？

该论文提出的GTA-2基准在真实性和层次性上是一大进步，但仍存在一些局限和可探索的方向。首先，其工作流任务虽基于真实场景，但覆盖的领域和工具类型可能有限，未来可扩展到更广泛的专业领域（如科研、金融）和更复杂的多模态交互。其次，评估机制依赖递归检查点，虽结构化但可能无法完全捕捉开放工作流中灵活的问题解决能力，未来可探索结合过程性评估与最终成果质量的多维度量。

从改进思路看，当前基准主要测试单智能体，而现实工作常涉及多智能体协作。未来可引入协作场景，评估智能体在分工、协商和冲突解决中的表现。此外，论文发现执行框架（如Manus）对性能提升显著，但框架设计本身缺乏系统化指导。可进一步研究框架的模块化设计原则，例如如何动态规划工具调用、处理异常以及进行长期记忆管理。最后，基准可考虑加入持续学习机制，使智能体能在任务执行中适应新工具或环境变化，从而更贴近实际应用需求。

### Q6: 总结一下论文的主要内容

该论文提出了GTA-2基准测试，旨在评估通用工具智能体从原子工具使用到开放式工作流的综合能力。核心问题是现有评测基准与现实需求脱节，依赖AI生成查询、虚拟工具且缺乏系统级协调。为此，GTA-2基于真实用户查询、已部署工具和多模态上下文构建，包含两个层次：GTA-Atomic评估短视域、封闭式的原子工具使用精度；GTA-Workflow则引入长视域、开放式任务，模拟现实端到端工作流完成。为评估开放式产出，论文提出一种基于递归检查点的评估机制，将目标分解为可验证的子目标，从而统一评估模型能力和智能体执行框架。主要结论显示，前沿模型在原子任务上已表现不佳（成功率低于50%），在工作流任务上更是大幅失败（顶级模型仅14.39%成功率）。分析表明，检查点引导的反馈能提升性能，而先进执行框架（如Manus和OpenClaw）显著改善工作流完成度，凸显了执行框架设计的重要性不亚于底层模型能力。该研究为开发可靠的个人与专业助手提供了重要指导。
