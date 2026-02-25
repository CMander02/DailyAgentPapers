---
title: "Benchmark Test-Time Scaling of General LLM Agents"
authors:
  - "Xiaochuan Li"
  - "Ryan Ming"
  - "Pranav Setlur"
  - "Abhijay Paladugu"
  - "Andy Tang"
  - "Hao Kang"
  - "Shuai Shao"
  - "Rong Jin"
  - "Chenyan Xiong"
date: "2026-02-22"
arxiv_id: "2602.18998"
arxiv_url: "https://arxiv.org/abs/2602.18998"
pdf_url: "https://arxiv.org/pdf/2602.18998v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent Benchmark"
  - "General-Purpose Agent"
  - "Test-Time Scaling"
  - "Agent Evaluation"
  - "Tool Use"
  - "Multi-Domain"
relevance_score: 8.0
---

# Benchmark Test-Time Scaling of General LLM Agents

## 原始摘要

LLM agents are increasingly expected to function as general-purpose systems capable of resolving open-ended user requests. While existing benchmarks focus on domain-aware environments for developing specialized agents, evaluating general-purpose agents requires more realistic settings that challenge them to operate across multiple skills and tools within a unified environment. We introduce General AgentBench, a benchmark that provides such a unified framework for evaluating general LLM agents across search, coding, reasoning, and tool-use domains. Using General AgentBench, we systematically study test-time scaling behaviors under sequential scaling (iterative interaction) and parallel scaling (sampling multiple trajectories). Evaluation of ten leading LLM agents reveals a substantial performance degradation when moving from domain-specific evaluations to this general-agent setting. Moreover, we find that neither scaling methodology yields effective performance improvements in practice, due to two fundamental limitations: context ceiling in sequential scaling and verification gap in parallel scaling. Code is publicly available at https://github.com/cxcscmu/General-AgentBench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型智能体评估与现实应用需求之间的脱节问题。现有的智能体基准测试通常专注于特定领域（如软件工程或网页导航），其环境和工具集都是为该领域量身定制的。然而，现实世界的用户请求往往是开放式的、跨领域的，要求智能体能够综合运用搜索、编码、推理和工具使用等多种技能。论文指出，这种领域特定的评估可能高估了智能体在真实、多领域条件下的鲁棒性，无法全面衡量其作为通用目的系统的能力。

为此，论文引入了“通用智能体基准测试”，旨在提供一个统一的评估框架，以更贴近真实用户交互场景的方式，评估通用大语言模型智能体跨多个领域的综合能力。此外，论文还系统研究了在这种通用智能体设置下，两种测试时扩展策略（即通过延长交互历史进行“顺序扩展”和通过采样多条轨迹进行“并行扩展”）的实际效果，并揭示了其存在的根本性局限：顺序扩展会受限于“上下文天花板”，导致性能不稳定甚至下降；而并行扩展则存在“验证鸿沟”，即智能体虽然能生成正确答案，却无法可靠地识别并选择它，从而限制了性能的实际提升。

### Q2: 有哪些相关研究？

相关研究主要围绕三个方向展开：1）智能体能力评测基准，2）智能体模型与框架开发，3）测试时扩展方法探索。

在评测基准方面，现有工作多为面向特定领域的专用智能体设计，例如软件工程（SWE-bench）、网页导航（WebArena）和工具调用（ToolLLM）。一些更广泛的基准套件（如AgentBench、GAIA）虽然涵盖多轮交互和多个任务类别，但本文认为它们仍缺乏对通用智能体在统一环境中跨技能操作的真实评估。本文提出的General AgentBench旨在弥补这一缺口，提供一个更贴近现实、挑战智能体综合能力的统一评测框架。

在智能体开发方面，早期方法（如ReAct、Reflexion）引入了结构化推理-行动轨迹和反思机制，近期工作则侧重于支持多智能体协调和丰富工具生态的可扩展框架（如OpenAgents、AgentVerse）。本文的研究对象正是这些旨在处理异构任务的通用智能体。

在测试时扩展方面，相关研究探索通过增加推理时计算来提升性能，例如思维链提示、自我一致性解码、基于树的搜索（Tree-of-Thoughts）以及迭代精炼方法。本文系统研究了顺序扩展（迭代交互）和并行扩展（采样多轨迹）这两种测试时扩展策略在通用智能体场景下的实际效果，并指出了其存在的根本局限性（上下文上限和验证差距），与现有研究形成了对比和深化。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为 **General AgentBench** 的统一基准测试框架来解决评估通用LLM智能体在开放、真实场景下性能的问题。其核心方法、架构设计和关键技术如下：

**1. 基准构建与统一框架：**
论文首先从**编码（Coding）、搜索（Search）、工具使用（Tool-use）和推理（Reason）**四个关键领域整合了多个现有数据集（如SWE-Bench、WebVoyager、MathHay等），构建了一个跨领域的综合测试集。其核心创新在于设计了一个**统一的、模拟真实世界的评估框架**。该框架采用**模型上下文协议（MCP）**作为骨干，将每个基准环境实例化为一个MCP服务器，并由一个统一的**主机（Host）**集中管理。主机维护一个全局工具注册表，向智能体呈现一个跨越所有领域的、单一的统一工具空间，抽象了具体基准的实现细节。

**2. 模拟真实交互的关键设计：**
- **统一工具接口：** 智能体必须从一个包含所有领域工具的大池子中，在没有先验任务领域知识的情况下选择合适工具，这模拟了实际部署场景。
- **动态演化的交互上下文：** 所有工具和环境的描述同时暴露，结合用户查询和多轮交互历史，上下文会自然增长到长文本范围。智能体必须在异构信息源（任务指令、工具文档、执行反馈、自身决策历史）上进行推理，这与静态的单轮问答任务形成鲜明对比。
- **解耦的执行过程：** 框架将所有基准服务器同时实例化并保持待命。智能体发出工具调用后，主机将其路由到对应服务器执行并返回统一格式的结果。即使工具调用与任务不直接相关，环境也会执行并返回有效输出，这故意暴露了智能体可能做出错误或无关工具调用的真实情况。

**3. 系统性测试时扩展性研究：**
论文利用该基准，系统研究了两种常见的测试时扩展策略在通用智能体场景下的有效性及其根本局限：
- **顺序扩展（Sequential Scaling）：** 通过增加交互轮次（深度）来扩展计算。研究发现存在 **“上下文天花板（context ceiling）”** 。性能在接近模型固有的上下文长度时会提升，但一旦累积上下文显著超过该阈值，性能就会饱和或下降，额外计算无法带来收益。智能体表现出停滞波动或性能退化，难以在扩展的交互轨迹中探索新的解决方案路径。
- **并行扩展（Parallel Scaling）：** 通过独立采样多个轨迹（广度）来扩展计算。虽然**pass@K**（理想上界）随K增加而提升，但智能体**自我选择（Self-Choice）** 的能力——即从自身生成的轨迹中评估和选择最佳结果——存在显著的**验证差距（verification gap）**。自我选择的性能提升有限，且很快饱和，无法跟上pass@K的持续改善。即使使用更强的外部验证器（如GPT-5），也会因“解决方案熟悉度”问题而表现不佳，这揭示了模型生成能力与可靠选择正确解决方案能力之间的根本差距。

总之，论文通过构建一个高度统一和真实的评估平台，并在此平台上进行严谨的测试时扩展实验，揭示了当前通用LLM智能体在从领域专用评估转向通用设置时面临的性能显著下降问题，并指出了顺序扩展的“上下文天花板”和并行扩展的“验证差距”这两个根本性限制。

### Q4: 论文做了哪些实验？

论文在提出的General AgentBench基准上进行了系统性实验，主要分为两部分：**整体性能评估**与**测试时扩展行为研究**。

**实验设置**：评估了包括Claude Sonnet 4.5、GPT-5、DeepSeek-V3.2、Gemini系列等在内的十个领先LLM智能体。基准涵盖搜索、编码、推理和工具使用四个领域，并对比了智能体在**领域专用设置**（使用特定领域工具）与**通用智能体设置**（在统一环境中使用共享工具集）下的表现。测试时扩展研究聚焦两种策略：**并行扩展**（独立采样K条轨迹）和**顺序扩展**（通过增加交互历史长度来分配更多计算）。并行扩展中还设置了**自我选择**评估，包括点对点选择和成对选择，以模拟实际部署中智能体自我评估的能力。

**基准测试与主要结果**：
1.  **通用 vs. 专用性能对比**：大多数智能体在通用设置下性能显著下降，平均相对下降10%至30%。例如，Gemini 2.5-Pro在推理领域下降超过60%。Claude Sonnet 4.5表现最为稳健，平均仅下降0.2%。有趣的是，部分模型（如Qwen3-Next）在搜索领域因有效的**跨领域工具使用**（如调用Google Maps、arXiv API等）而性能提升。
2.  **顺序扩展**：结果显示性能提升有限或不一致。存在**停滞波动**（性能在窄幅振荡）和**饱和退化**（超过一定步数后性能下降）两种模式。分析发现存在“**上下文天花板**”，即当累积上下文长度超过模型固有阈值（如Qwen3-235B在搜索领域约112K tokens）后，进一步扩展几乎无收益。
3.  **并行扩展**：随着采样轨迹数K增加，理想上限指标pass@K单调提升（K从1增至4时平均提升约50%，DeepSeek-V3.2提升近一倍）。然而，智能体的**自我选择**性能显著落后于pass@K上限，且随着K增加，自我选择收益很快饱和甚至下降，暴露出**验证差距**。即使使用更强的外部验证器GPT-5，其评估效果也常差于模型自身的判断，部分源于“解决方案熟悉度”问题。

这些实验表明，当前通用LLM智能体在跨领域统一环境中面临严峻挑战，且简单的测试时计算扩展（无论是顺序还是并行）在实践中因“上下文天花板”和“验证差距”等根本限制而收效有限。

### Q5: 有什么可以进一步探索的点？

这篇论文揭示了当前通用LLM智能体在跨领域综合任务中表现不佳，且两种主流测试时扩展方法（顺序扩展与并行扩展）均存在根本性缺陷。其局限性主要在于：1）**上下文天花板**：顺序扩展（迭代交互）受限于模型的上下文窗口长度，无法通过无限增加交互步骤来持续提升性能；2）**验证鸿沟**：并行扩展（采样多条轨迹）缺乏高效可靠的机制来从多个候选解决方案中筛选出最优解。

基于此，未来有几个关键方向值得深入探索：首先，需要设计**突破上下文窗口限制的新型智能体架构或记忆机制**，使智能体能在长程、复杂的多轮交互中有效利用历史信息。其次，亟需开发**更强大的验证或评判模块**，以低成本、高准确率的方式评估并行生成的多个轨迹，从而弥合“验证鸿沟”。最后，基准本身可进一步扩展，纳入**更动态、开放的环境**以及**需要长期规划与工具组合创造的任务**，以更全面地评估智能体的通用性与鲁棒性。这些探索将推动智能体从“擅长单一任务”向真正的“通用问题解决者”演进。

### Q6: 总结一下论文的主要内容

这篇论文提出了General AgentBench，一个用于评估通用LLM智能体的统一基准。其核心贡献在于创建了一个更贴近现实的多领域交互测试环境，要求智能体能够推断用户意图、从共享工具池中选择工具并执行端到端任务，从而弥补了现有领域专用评测的不足。研究发现，当前领先的LLM智能体在从领域特定评估转向这种通用智能体设置时，性能会出现显著下降。论文进一步系统分析了测试时扩展的两种方法（顺序扩展与并行扩展），并揭示了其根本性局限：顺序扩展受限于“上下文天花板”，交互过长会导致不稳定；并行扩展则因生成与自我选择之间存在“验证鸿沟”，实际性能提升有限。该工作的意义在于为通用智能体的稳健性与可扩展性研究提供了重要的评估工具和理论洞察。
