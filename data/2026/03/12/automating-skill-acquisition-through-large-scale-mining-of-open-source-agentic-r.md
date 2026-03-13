---
title: "Automating Skill Acquisition through Large-Scale Mining of Open-Source Agentic Repositories: A Framework for Multi-Agent Procedural Knowledge Extraction"
authors:
  - "Shuzhen Bi"
  - "Mengsong Wu"
  - "Hao Hao"
  - "Keqian Li"
  - "Wentao Liu"
  - "Siyu Song"
  - "Hongbo Zhao"
  - "Aimin Zhou"
date: "2026-03-12"
arxiv_id: "2603.11808"
arxiv_url: "https://arxiv.org/abs/2603.11808"
pdf_url: "https://arxiv.org/pdf/2603.11808v1"
categories:
  - "cs.AI"
tags:
  - "多智能体"
  - "技能获取"
  - "知识提取"
  - "开源挖掘"
  - "程序知识"
  - "框架"
  - "评估"
relevance_score: 8.0
---

# Automating Skill Acquisition through Large-Scale Mining of Open-Source Agentic Repositories: A Framework for Multi-Agent Procedural Knowledge Extraction

## 原始摘要

The transition from monolithic large language models (LLMs) to modular, skill-equipped agents represents a fundamental architectural shift in artificial intelligence deployment. While general-purpose models demonstrate remarkable breadth in declarative knowledge, their utility in autonomous workflows is frequently constrained by insufficient specialized procedural expertise. This report investigates a systematic framework for automated acquisition of high-quality agent skills through mining of open-source repositories on platforms such as GitHub. We focus on the extraction of visualization and educational capabilities from state-of-the-art systems including TheoremExplainAgent and Code2Video, both utilizing the Manim mathematical animation engine. The framework encompasses repository structural analysis, semantic skill identification through dense retrieval, and translation to the standardized SKILL.md format. We demonstrate that systematic extraction from agentic repositories, combined with rigorous security governance and multi-dimensional evaluation metrics, enables scalable acquisition of procedural knowledge that augments LLM capabilities without requiring model retraining. Our analysis reveals that agent-generated educational content can achieve 40\% gains in knowledge transfer efficiency while maintaining pedagogical quality comparable to human-crafted tutorials.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何大规模、自动化地获取高质量智能体技能的核心问题。研究背景是人工智能部署正经历从单一大型语言模型向模块化、具备技能的智能体架构的根本性转变。尽管通用大语言模型在陈述性知识上广度惊人，但它们在自主工作流中的应用常受限于缺乏完成具体任务所需的、专门的程序性知识。

现有方法存在明显不足。传统上，高质量技能依赖于领域专家手动编写，这虽然保证了可靠性，但严重受限于可扩展性，无法满足海量需求。而自动发现方法虽然在开放环境中具有潜力，但往往难以保持提取知识的语义连贯性和教学价值。

因此，本文要解决的核心问题是：如何克服上述限制，实现大规模、高质量的智能体技能自动化获取。论文提出的解决方案是系统性地从开源智能体代码库中挖掘程序性知识。具体而言，作者构建了一个框架，专注于从GitHub等平台上的先进系统（如TheoremExplainAgent和Code2Video）中提取可视化和教育类能力。该框架通过分析仓库结构、利用密集检索进行语义技能识别，并将提取的逻辑转化为标准化的SKILL.md格式，从而实现将现有开源软件中的复杂、领域特定的任务逻辑，系统地重构为可重用、可扩展的智能体技能，以此增强大语言模型的能力，而无需进行昂贵的模型重训练。

### Q2: 有哪些相关研究？

本文的研究与以下几类相关工作密切相关：

**1. 智能体技能与知识表示方法**
本文提出的基于四元组（适用条件、策略、终止条件、接口）的形式化技能范式，与传统的工具调用（如 OpenAI 的 Function Calling）和智能体框架（如 AutoGPT、LangChain）中的工具封装有直接关联。区别在于，本文的技能范式不仅封装了可调用接口，更强调嵌入领域特定的推理逻辑和决策过程，使其超越了简单的工具包装，成为可重用、可组合的“程序性知识”单元。这与近期关于“技能”的研究（如 Anthropic 的 SKILL.md 规范）一脉相承，但本文重点在于从开源仓库中**自动化提取**此类技能，而非手动定义。

**2. 代码与知识挖掘**
相关工作包括从开源代码库（如 GitHub）中挖掘可复用代码片段、API 使用模式或工作流程的研究。本文的框架（包含仓库结构分析、语义技能识别等）属于此类，但其独特之处在于专门针对**智能体仓库**进行挖掘，目标是提取结构化的、符合特定形式化范式的技能，而非一般的代码克隆检测或模式挖掘。这要求框架能理解智能体架构的上下文和技能的组织逻辑。

**3. 大模型能力增强与知识注入**
大量研究致力于通过检索增强生成（RAG）、微调或提示工程来增强大模型的专长能力。本文方法提供了一条无需重新训练模型的替代路径：通过外部技能库的形式，将高质量的程序性知识注入智能体工作流。这与 RAG 思想类似，但检索和利用的对象是结构化的技能单元，其包含的策略和资源比单纯的文档片段更具可操作性和指导性。

**4. 多智能体系统与知识共享**
在多智能体系统研究中，如何实现技能或知识的共享与迁移是一个重要课题。本文提出的标准化技能接口和渐进式披露架构，旨在促进技能在异构智能体间的重用和组合，这与此类研究的目标一致。本文的贡献在于提供了一个从现有智能体实现中自动化提取此类可共享技能的具体框架。

### Q3: 论文如何解决这个问题？

论文通过一个多阶段的自动化框架来解决从开源仓库中提取技能的问题，其核心方法、架构设计和关键技术如下：

**整体框架**：该框架采用三阶段流水线，将单体代码库转化为模块化的SKILL.md技能工件。流程始于**仓库结构分析**，使用repo2AI等工具生成目录结构和文件内容的Markdown表示，以识别核心执行脚本（如generate_video.py）、配置文件、辅助模块和文档，从而理解任务编排模式和逻辑依赖关系，为后续提取提供上下文。

**主要模块与关键技术**：
1.  **语义技能识别**：这是一个两阶段排序过程。首先，通过**双编码器**将任务描述和代码模块编码为稠密向量，并计算余弦相似度以初步筛选候选模块。随后，**交叉编码器排序器**对任务-模块对进行联合编码和精细相关性评分，仅保留超过阈值τ的模块。此阶段依据**重复性、可验证性、非显而易见性和可泛化性**等标准，确保提取的是真正可重用的过程模式，而非项目特定实现。

2.  **标准化翻译**：将识别出的过程模式合成为SKILL.md格式。该模块包含三个核心组件：
    *   **元数据合成**：提取代理生成符合YAML规范的元数据，包括技能名称、描述、版本、触发模式和依赖项。
    *   **指令生成**：编写面向LLM的**二级指令**，强调可操作的过程知识，如分步工作流分解、错误处理策略、最佳实践和集成模式，避免仓库特定的实现细节。
    *   **资产重构与组织**：将可执行脚本、参考文档和配置模板组织到标准化子目录（scripts/, references/, templates/）中，并消除硬编码路径、API密钥等环境依赖，确保技能的可移植性。

**创新点**：
*   **从代码结构到过程知识的系统化提取**：通过结构分析明确上下文，结合两阶段语义检索（稠密检索+交叉编码器精排），精准定位“潜在技能”。
*   **面向Agent的标准化技能封装**：创新性地定义了SKILL.md格式，特别是其中的**LLM可消费的二级指令**，将代码实现转化为通用的、可指导LLM或Agent执行的过程知识，实现了技能与具体代码库的解耦。
*   **可扩展且安全的获取流程**：整个框架设计为自动化流水线，结合严格的安全治理和多维评估指标，能够在不重新训练模型的情况下，规模化地获取高质量过程知识以增强LLM能力。

### Q4: 论文做了哪些实验？

论文实验围绕从开源智能体仓库中自动化提取技能，并通过多维度评估框架验证其有效性。实验设置包括：首先，从GitHub等平台挖掘包含可视化与教育功能的仓库（如TheoremExplainAgent和Code2Video），这些系统基于Manim数学动画引擎；接着，通过仓库结构分析、语义技能识别（采用密集检索技术）将技能转换为标准化的SKILL.md格式；最后，运用安全治理和多维指标进行评估。

数据集与基准测试方面，使用了TheoremExplainBench（TEB）和MMMC等基准来评估技能的可执行性与性能，并通过TeachQuiz衡量教学效果。对比方法包括基线代码生成模型以及现有智能体架构。

主要结果与关键数据指标如下：
1. 在Code2Video的完整Planner-Coder-Critic架构中，知识传递效率相比基线模型提升40%。
2. TheoremExplainAgent的o3-mini智能体在TheoremExplainBench上获得0.77的综合分数，在多模态科学推理任务中达到先进水平。
3. 通过SkillNet将技能整合到本体框架中，实现了执行步骤减少30%、跨不同骨干模型的任务平均奖励提升40%，并能自动检测冗余技能。
4. 技能评估覆盖安全（漏洞率）、完整性（API文档覆盖率）、可执行性（任务成功率）、可维护性（模式漂移鲁棒性）和教学效果（TeachQuiz分数）等多个维度，确保提取的技能高质量且可扩展。

### Q5: 有什么可以进一步探索的点？

基于论文内容，未来可进一步探索的方向包括：首先，当前框架主要从特定平台（如GitHub）的公开仓库中提取技能，其覆盖范围受限于仓库质量和领域分布，未来可扩展至更多元的数据源（如私有代码库、多模态交互日志），以提升技能多样性和领域适应性。其次，论文强调技能提取的自动化，但对技能间的组合与协同机制探讨不足，未来可研究动态技能编排方法，使多智能体能够根据复杂任务自动调用和整合多个技能模块。此外，论文提及“进化智能体”可通过分析对话日志优化技能，但未深入其具体实现路径，未来可探索基于强化学习或因果推理的个性化技能迭代机制，使技能能实时适应用户偏好和故障模式。最后，当前评估侧重于知识传递效率，未来需建立更全面的评估体系，涵盖技能的可解释性、安全边界及跨领域泛化能力，以推动技能生态的可靠部署。

### Q6: 总结一下论文的主要内容

该论文针对当前大型语言模型在自主工作流中缺乏专业程序性知识的问题，提出了一种通过大规模挖掘开源智能体仓库来自动化获取高质量技能的系统框架。其核心贡献在于设计了一套从仓库结构分析、基于密集检索的语义技能识别到标准化SKILL.md格式转换的完整流程，实现了无需重新训练模型即可扩展增强LLM能力的目标。论文以TheoremExplainAgent和Code2Video等先进系统为例，聚焦于提取可视化与教育能力，论证了可执行代码是编码视觉与教学专业知识的理想载体。主要结论表明，通过该框架提取的技能不仅能匹配甚至超越人工编写内容的质量，其生成的教育内容在保持教学水准的同时，还能实现40%的知识传递效率提升。这为从单一大型模型向可组合、可治理、持续演化的技能生态系统转型奠定了坚实基础。
