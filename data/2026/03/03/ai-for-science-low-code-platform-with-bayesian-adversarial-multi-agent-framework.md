---
title: "AI-for-Science Low-code Platform with Bayesian Adversarial Multi-Agent Framework"
authors:
  - "Zihang Zeng"
  - "Jiaquan Zhang"
  - "Pengze Li"
  - "Yuan Qi"
  - "Xi Chen"
date: "2026-03-03"
arxiv_id: "2603.03233"
arxiv_url: "https://arxiv.org/abs/2603.03233"
pdf_url: "https://arxiv.org/pdf/2603.03233v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "Code & Software Engineering"
relevance_score: 7.5
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Code & Software Engineering"
  domain: "Scientific Research"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "Bayesian adversarial multi-agent framework"
  primary_benchmark: "N/A"
---

# AI-for-Science Low-code Platform with Bayesian Adversarial Multi-Agent Framework

## 原始摘要

Large Language Models (LLMs) demonstrate potentials for automating scientific code generation but face challenges in reliability, error propagation in multi-agent workflows, and evaluation in domains with ill-defined success metrics. We present a Bayesian adversarial multi-agent framework specifically designed for AI for Science (AI4S) tasks in the form of a Low-code Platform (LCP). Three LLM-based agents are coordinated under the Bayesian framework: a Task Manager that structures user inputs into actionable plans and adaptive test cases, a Code Generator that produces candidate solutions, and an Evaluator providing comprehensive feedback. The framework employs an adversarial loop where the Task Manager iteratively refines test cases to challenge the Code Generator, while prompt distributions are dynamically updated using Bayesian principles by integrating code quality metrics: functional correctness, structural alignment, and static analysis. This co-optimization of tests and code reduces dependence on LLM reliability and addresses evaluation uncertainty inherent to scientific tasks. LCP also streamlines human-AI collaboration by translating non-expert prompts into domain-specific requirements, bypassing the need for manual prompt engineering by practitioners without coding backgrounds. Benchmark evaluations demonstrate LCP's effectiveness in generating robust code while minimizing error propagation. The proposed platform is also tested on an Earth Science cross-disciplinary task and demonstrates strong reliability, outperforming competing models.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在自动化生成科学代码（AI for Science, AI4S）时面临的三大核心挑战：可靠性不足、多智能体工作流中的错误传播，以及在成功标准难以明确定义的科学领域中进行有效评估的困难。

研究背景是，尽管Codex等LLM降低了科研人员编写复杂科学代码（如模拟、数据分析）的技术门槛，但其在实际AI4S研究中的可靠应用仍存在障碍。现有方法主要包括单LLM生成和传统的多智能体角色扮演框架。然而，单LLM方法受限于模型本身的理解和推理能力，输出可能包含不易察觉的错误；而传统的多智能体系统虽然能分工协作，但存在严重不足：其一，系统整体可靠性受制于最弱的智能体，错误会在智能体间传播并放大；其二，对于科学任务，标准的单元测试或LLM生成的测试往往无法有效验证科学正确性、物理定律遵循度等深层领域约束，存在评估鸿沟。

因此，本文要解决的核心问题是：如何构建一个框架，既能降低非编程背景领域专家的使用门槛，又能生成可靠、符合科学约束的代码，同时克服多智能体系统的错误传播和科学任务评估的不确定性。为此，论文提出了一个贝叶斯对抗多智能体低代码平台（LCP）。该框架通过三个智能体（任务管理器、代码生成器、评估器）在贝叶斯原则下的对抗循环与协同优化，让测试用例生成与代码改进相互竞争、共同进化，从而减少对底层LLM绝对可靠性的依赖，并动态处理科学评估中的不确定性。平台还将用户模糊提示转化为精准任务计划，无需人工提示工程，促进了人机协作。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、应用类和评测类。

在方法类上，相关工作包括基于单一LLM的代码生成模型（如Codex、AlphaCode、CodeLlama）和传统的多智能体角色扮演框架。单一LLM模型虽能降低技术门槛，但在处理复杂科学工作流的模糊提示和错误传播方面存在不足。传统的多智能体系统通过分布式推理和角色专长化试图缓解这些问题，但其整体可靠性受制于最弱的智能体，且可能放大错误传播。本文提出的贝叶斯对抗多智能体框架与这些方法的核心区别在于：它引入了任务管理器与代码生成器之间的对抗循环，并利用贝叶斯原理动态更新提示分布，从而协同优化测试用例与代码，降低了对底层LLM固有可靠性的依赖。

在应用类上，现有研究聚焦于利用LLM自动化科学任务（如模拟、数据分析），但常面临领域科学家提示不清、需遵守物理定律等挑战。本文的贡献在于其低代码平台（LCP）专门为AI4S设计，通过任务管理器将非专家用户的模糊提示转化为精确的任务计划和科学有效的测试用例，无需用户具备编程或提示工程背景，从而显著提升了人机协作的流畅性。

在评测类上，科学代码的评估存在固有困难，因为标准单元测试可能忽略科学约束或领域知识。以往方法多依赖LLM生成测试，但测试本身可能存在与代码相同的可靠性问题。本文的创新点在于采用了一种基于代码质量指标（功能正确性、结构对齐、静态分析）的非LLM对抗性评分，并通过贝叶斯优化来估计代码性能，从而更稳健地处理复杂代码的评估不确定性。

### Q3: 论文如何解决这个问题？

论文通过提出一个贝叶斯对抗多智能体框架来解决科学代码生成中的可靠性、错误传播和评估难题。其核心方法围绕三个基于LLM的智能体展开：任务管理器（TM）、代码生成器（SG）和评估器（Eval）。整体架构设计了一个动态对抗循环：TM作为挑战者，负责将用户输入的任务描述和领域知识分解为结构化计划和自适应测试用例；SG作为求解者，根据提示生成候选代码；Eval则提供基于代码质量指标（功能正确性、结构对齐和静态分析）的综合反馈。

关键技术在于贝叶斯驱动的协同优化机制。首先，TM与用户交互迭代细化计划，并生成初始测试用例和提示。在代码生成与评估循环中，系统计算三种核心分数：测试用例分数（S1，衡量其区分代码优劣的“真实难度”）、代码分数（S2，基于通过测试的加权结果）和提示分数（S3，综合S1和S2）。这些分数驱动贝叶斯更新规则：下一次迭代的提示概率正比于当前提示配置的似然度与其先验概率的乘积，即 \( p(\text{prompt}^{t+1}_{ij} | S_3^t) \propto p(S_3^t | \text{prompt}^t_{ij}) p(\text{prompt}^t_{ij}) \)。这使得测试用例和示例代码池能动态演化，优先选择能产生高效提示的“教师-主题”组合。

创新点主要体现在三方面：一是对抗循环中TM与SG的协同进化，TM根据S1调整测试难度以挑战SG，SG的反馈又优化TM策略，从而减少对LLM单一可靠性的依赖；二是引入贝叶斯优化，通过代码的结构嵌入（如AST）预测性能，高效探索解空间并降低全测试计算成本；三是低代码平台设计，将非专家提示转化为领域特定需求，无需手动提示工程，并通过用户交互批准计划确保对齐。最终，该框架通过迭代优化测试与代码，在科学任务中实现了鲁棒的代码生成，并在地球科学跨学科任务中验证了其强可靠性。

### Q4: 论文做了哪些实验？

论文实验部分系统评估了所提出的低代码平台（LCP）框架。实验设置方面，框架集成了多种骨干大语言模型（LLMs），包括Qwen3系列（1.7B至235B）、Deepseek-v3、Deepseek-R1、Claude-sonnet-4、GPT-3.5-turbo和GPT-4o，以验证其模型无关性。关键参数包括：初始测试用例数为15，每轮生成20个不同的代码片段，测试用例池最小维持20个，每次迭代选择5个代码进行进一步评估。

使用的数据集和基准测试涵盖通用代码生成和科学代码生成两类。通用任务使用了HumanEval、HumanEval-ET、MBPP、MBPP-ET和更具挑战性的APPS基准。针对AI for Science（AI4S）任务，则使用了领域特定的SciCode和ScienceAgentBench基准。

对比方法包括Few-Shot提示、Chain-of-Thought（CoT）等基础策略，以及ReAct、Reflexion、Self-Debugging、Self-Collaboration、MetaGPT、MapCoder、AgentCoder、CodeCoR等先进的基于智能体的系统。

主要结果如下：在SciCode基准测试中，LCP为所有配置的模型带来了显著且一致的性能提升，尤其对于开源模型，相对改进高达87.1%（Qwen3-8b）。例如，在“无知识”条件下，搭载LCP的Qwen3-14b在子问题解决率上达到30.6%，与规模大16倍以上的Qwen3-235B-A22b-Instruct-2507的基线性能持平。在更复杂的ScienceAgentBench上（以GPT-4o为基座模型），LCP取得了新的最先进（SOTA）性能，特别是在有效执行率（VER）上，“无知识”和“有知识”条件下分别达到90.2%和87.3%，远超其他方法。此外，迭代实验表明，性能随着迭代次数增加持续单调提升，通常在4-5轮后收敛。消融研究证实了对抗性测试用例（ATC）机制的关键作用，它能驱动系统产生更鲁棒的解决方案。最后，实验还证明了LCP对提示词质量具有更强的鲁棒性，能有效弥补非专业用户在提示工程上的不足。

### Q5: 有什么可以进一步探索的点？

该论文的框架在初始参考代码质量、复杂科学问题的泛化能力以及多轮对抗中的计算成本方面存在局限性。未来可探索以下方向：首先，引入元学习或小样本学习机制，减少对高质量初始代码的依赖，使系统能从少量示例中自主归纳领域知识。其次，可扩展多智能体架构，例如增加“领域专家”智能体，专门负责整合科学先验知识（如物理约束或领域方程），以提升复杂跨学科任务的推理可靠性。再者，针对计算效率问题，可研究动态对抗调度策略，在代码质量收敛时自动减少对抗轮次，或采用轻量级模型协同工作。此外，评估维度可进一步丰富，例如引入运行时性能分析或科学可复现性指标，使评估更贴合实际科研需求。最后，平台可探索与交互式可视化工具结合，让非专家用户能更直观地参与代码调试与结果验证，形成更紧密的人机协同循环。

### Q6: 总结一下论文的主要内容

该论文提出了一种用于AI for Science（AI4S）任务的贝叶斯对抗多智能体框架，并以低代码平台（LCP）形式实现。其核心贡献在于解决LLM在科学代码生成中面临的可靠性低、多智能体工作流错误传播以及难以评估等挑战。

**问题定义**：针对科学领域代码生成任务中成功标准模糊、LLM可靠性不足以及非专家用户难以进行有效提示工程的问题。

**方法概述**：框架协调三个基于LLM的智能体：任务管理器（将用户输入解析为可执行计划和自适应测试用例）、代码生成器（生成候选解决方案）和评估器（提供综合反馈）。通过一个对抗循环，任务管理器迭代优化测试用例以挑战代码生成器，同时利用贝叶斯原理动态更新提示分布，整合功能性正确、结构对齐和静态分析等代码质量指标。这种测试与代码的协同优化减少了对LLM单一可靠性的依赖，并处理了科学任务固有的评估不确定性。

**主要结论与意义**：基准评估表明，LCP能有效生成鲁棒代码并最小化错误传播。在地球科学跨学科任务上的测试也展示了其强可靠性，性能优于对比模型。该平台通过将非专家提示转化为领域特定需求，简化了人机协作，使无编码背景的研究者也能使用，有助于推动LLM工具在科研中的民主化应用。然而，该方法性能仍受初始参考代码质量影响，且在处理某些复杂场景时存在局限。
