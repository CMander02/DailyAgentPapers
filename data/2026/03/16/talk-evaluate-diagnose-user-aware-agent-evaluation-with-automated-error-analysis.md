---
title: "Talk, Evaluate, Diagnose: User-aware Agent Evaluation with Automated Error Analysis"
authors:
  - "Penny Chong"
  - "Harshavardhan Abichandani"
  - "Jiyuan Shen"
  - "Atin Ghosh"
  - "Min Pyae Moe"
  - "Yifan Mai"
  - "Daniel Dahlmeier"
date: "2026-03-16"
arxiv_id: "2603.15483"
arxiv_url: "https://arxiv.org/abs/2603.15483"
pdf_url: "https://arxiv.org/pdf/2603.15483v1"
github_url: "https://github.com/SAP-samples/agent-quality-inspect"
categories:
  - "cs.AI"
tags:
  - "Agent Evaluation"
  - "LLM-as-a-Judge"
  - "User Simulation"
  - "Error Analysis"
  - "Benchmarking"
  - "Automated Grading"
relevance_score: 7.5
---

# Talk, Evaluate, Diagnose: User-aware Agent Evaluation with Automated Error Analysis

## 原始摘要

Agent applications are increasingly adopted to automate workflows across diverse tasks. However, due to the heterogeneous domains they operate in, it is challenging to create a scalable evaluation framework. Prior works each employ their own methods to determine task success, such as database lookups, regex match, etc., adding complexity to the development of a unified agent evaluation approach. Moreover, they do not systematically account for the user's role nor expertise in the interaction, providing incomplete insights into the agent's performance. We argue that effective agent evaluation goes beyond correctness alone, incorporating conversation quality, efficiency and systematic diagnosis of agent errors. To address this, we introduce the TED framework (Talk, Evaluate, Diagnose). (1) Talk: We leverage reusable, generic expert and non-expert user persona templates for user-agent interaction. (2) Evaluate: We adapt existing datasets by representing subgoals-such as tool signatures, and responses-as natural language grading notes, evaluated automatically with LLM-as-a-judge. We propose new metrics that capture both turn efficiency and intermediate progress of the agent complementing the user-aware setup. (3) Diagnose: We introduce an automated error analysis tool that analyzes the inconsistencies of the judge and agents, uncovering common errors, and providing actionable feedback for agent improvement. We show that our TED framework reveals new insights regarding agent performance across models and user expertise levels. We also demonstrate potential gains in agent performance with peaks of 8-10% on our proposed metrics after incorporating the identified error remedies into the agent's design.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型智能体（Agent）在多样化现实任务中评估困难的问题。研究背景是，随着智能体被广泛应用于自动化工作流，其评估因任务领域异构、目标多样而变得复杂。现有方法存在明显不足：首先，不同工作采用各自特定的评估标准（如数据库查询、正则匹配），难以形成统一且可扩展的评估框架；其次，现有评估大多忽视了用户在交互中的角色和专业知识水平对智能体表现的影响，导致评估视角不完整；此外，多数方法依赖静态或未系统化区分的用户模拟，未能分离用户行为特征与任务指令，无法公平测试智能体在不同用户情境下的适应性；最后，现有评估往往止步于报告指标，缺乏对错误根源的系统诊断。

针对这些不足，本文的核心问题是：如何构建一个可扩展、用户感知的智能体评估框架，不仅能跨领域统一评估智能体的正确性、对话质量和效率，还能自动诊断错误并提供改进反馈。为此，论文提出了TED框架，通过“对话、评估、诊断”三个阶段，系统性地纳入用户角色差异，利用可复用的用户人物模板创建测试场景，将数据集子目标转化为自然语言评分笔记供LLM作为评判员使用，并引入新的指标（如对话轮次效率）和自动化错误分析工具，以实现更全面、可操作的智能体性能评估与优化。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为对话模拟和评估与错误分析两大类。

在对话模拟方面，现有研究多采用LLM模拟用户（用户代理）进行动态评估。然而，这些方法存在局限性：一些方法使用的用户指令提示与特定智能体、场景或角色紧密耦合，另一些则完全忽略了用户角色设定，这都限制了评估方法的跨领域可复用性。尽管智能体表现受用户代理行为影响，但由于用户角色定义不一致，这种依赖性很少被系统分析。虽有研究在特定领域（如电信）系统性地引入了“简单”和“困难”用户角色，但其提示模板不具备通用性。本文提出的TED框架与这些工作的主要区别在于，它允许终端用户使用可复用的、通用的专家与非专家角色模板（与具体智能体或任务无关）来系统性地测试智能体，并在多个领域的数据集上验证了其无需调整的通用性。

在评估指标与错误分析方面，先前工作大多依赖成功率这一仅关注最终结果的粗粒度指标。AgentBoard引入了进度率作为细粒度指标，但应用于多步智能体-环境交互，未涉及对话模拟。本文将其扩展到多轮对话场景，并结合了轮次效率和进度率提出了新指标。与MINT等仅评估最终成功率的工作不同，本文的轮次感知评估能捕捉每轮的进展和效率。此外，不同于通过数据库查询等方式直接检查目标达成，本文将所有子目标表示为自然语言评分说明，该方法抽象了复杂目标，无需系统状态访问，适用性更广。在错误分析上，类似某些研究，本文也识别LLM智能体的常见错误，但区别在于，本文通过无监督地自动分析实时日志来发现错误，而非依赖预定义的错误类别。

### Q3: 论文如何解决这个问题？

论文通过提出TED框架来解决异构领域智能体评估缺乏统一、可扩展且能系统考虑用户角色与专业水平的问题。该框架包含三个核心阶段：对话、评估与诊断。

在整体架构上，TED首先在“对话”阶段引入可复用的通用用户角色模板，包括专家和非专家两种典型用户画像，以模拟真实、多样化的用户-智能体交互场景，从而将用户因素系统性地纳入评估流程。

其次，在“评估”阶段，框架对现有数据集进行适应性改造，将任务子目标（如工具调用签名、响应内容）转化为自然语言形式的评分说明。它采用“LLM即评委”的自动化方式对这些说明进行评估。其关键创新在于提出了新的评估指标：不仅衡量最终任务正确性，还引入了“轮次效率”来评估完成任务的交互步数，以及“中间进展”来追踪任务完成过程中的增量贡献，从而在多维度上补充了用户感知的评估设置。

最后，在“诊断”阶段，框架设计了一个自动化错误分析工具。该工具的核心功能是分析“评委”LLM与智能体自身行为的不一致性，以此自动识别和归类智能体的常见错误模式，并为智能体的改进提供具体、可操作的反馈建议。

该方法的创新点在于将用户角色模板化以统一纳入评估、通过自然语言评分说明和LLM评委实现评估流程的自动化与泛化能力，以及首创了结合多维新指标与自动化根因诊断的一体化评估-改进闭环。实验表明，依据诊断反馈改进智能体设计后，其在新指标上的性能可提升8-10%。

### Q4: 论文做了哪些实验？

论文在TED框架下进行了系统的实验评估。实验设置方面，使用了两个智能体基准测试：τ²-bench（航空和零售领域）和ToolSandbox（任务导向场景）。对于τ²-bench，航空领域使用了21个样本（分为“简单”和“困难”子集），零售领域使用了25个样本。对于ToolSandbox，选择了37个基础场景，并利用动态用户代理模拟多轮对话，以增加可变性。实验将任务的关键里程碑转换为自然语言评分说明，并采用LLM-as-a-judge（使用gpt-4.1模型）进行自动评估。每个样本进行多次试验（τ²-bench为20次，ToolSandbox为8次），最大对话轮数分别设为15和8。用户代理使用专家和非专家两种人物模板来模拟不同专业水平的用户。

对比方法涉及多个主流模型，包括gpt-4.1、gpt-4o、gpt-4o-mini、gpt-5、mistral-nemo和mistral-large。评估指标包括：MeanProg@k（平均进度率）、MaxProg@k（最大进度率）、MaxAUC@k（最大曲线下面积，强调早期进展）、MaxPPT@k（最大每轮平均进度，衡量回合效率）和pass@k（任务通过率）。

主要结果显示：在τ²-bench航空简单样本上，多数模型的MaxProg@k和pass@k接近饱和（如1.00），但MeanProg@k能区分一致性（如gpt-4.1专家为0.95，非专家为0.82）。MaxAUC@k和MaxPPT@k提供了更细致的洞察，例如在τ²-bench上，gpt-4o-mini（专家）和mistral-large（专家）的MeanProg@k仅差5%，但MaxAUC@k相差10%（0.96 vs 0.85）。用户人物影响显著：非专家用户导致所有模型的MaxAUC@k降低（如τ²-bench上gpt-4.1从0.99降至0.81），表明任务完成需要更多对话轮次，而MaxProg@k常忽略此差异。在ToolSandbox上，gpt-4o在非专家用户下表现优异（MeanProg@k为0.94，MaxAUC@k为0.96）。此外，错误分析工具通过识别不一致性，为智能体改进提供了可操作的反馈，实验表明结合错误补救后，智能体性能在提议指标上可提升8-10%。

### Q5: 有什么可以进一步探索的点？

该论文提出的TED框架在用户感知评估和自动化错误诊断方面做出了贡献，但仍有进一步探索的空间。局限性在于：1）其评估严重依赖LLM-as-a-judge，可能引入评估者自身的偏见和不一致性；2）用户模拟模板（专家/非专家）相对静态，未能涵盖更复杂、动态的用户行为模式；3）评估任务集中在特定领域（如航空、工具使用），在更开放、多模态或长程规划任务中的泛化能力有待验证。

未来研究方向可包括：1）开发更鲁棒、可解释的评估方法，例如结合规则检查或多模型交叉验证以减少对单一LLM评判的依赖；2）设计更细粒度和自适应的用户模拟，能够根据对话上下文动态调整知识水平和交互风格，以更真实地反映用户多样性；3）将评估框架扩展到更复杂的多智能体协作场景或具身任务中，考察其在动态环境下的表现。此外，可将自动化诊断反馈与在线学习结合，实现智能体的持续自我优化，而不仅限于离线改进。

### Q6: 总结一下论文的主要内容

本文针对异构领域中智能体评估的挑战，提出了TED（Talk, Evaluate, Diagnose）框架。核心问题是现有评估方法难以统一、忽略用户角色且缺乏系统性错误诊断。方法上，首先通过可复用的专家/非专家用户角色模板（Talk）实现用户感知的交互模拟；其次将现有数据集中的子目标转化为自然语言评分笔记，并采用LLM-as-a-judge进行自动评估，同时引入衡量对话轮次效率的新指标（Evaluate）；最后通过自动化错误分析工具诊断智能体与评判者的不一致性，提供可操作的改进反馈（Diagnose）。主要结论表明，TED框架能揭示不同模型和用户专业水平下的智能体性能新见解，且基于诊断反馈优化智能体设计后，其在新指标上性能可提升8-10%。该工作的意义在于构建了一个可扩展、统一且深入的用户感知评估体系，超越了仅关注正确性的传统方法，为智能体的全面评估与迭代优化提供了系统化方案。
