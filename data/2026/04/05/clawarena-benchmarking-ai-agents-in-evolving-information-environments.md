---
title: "ClawArena: Benchmarking AI Agents in Evolving Information Environments"
authors:
  - "Haonian Ji"
  - "Kaiwen Xiong"
  - "Siwei Han"
  - "Peng Xia"
  - "Shi Qiu"
  - "Yiyang Zhou"
  - "Jiaqi Liu"
  - "Jinlong Li"
  - "Bingzhou Li"
  - "Zeyu Zheng"
  - "Cihang Xie"
  - "Huaxiu Yao"
date: "2026-04-05"
arxiv_id: "2604.04202"
arxiv_url: "https://arxiv.org/abs/2604.04202"
pdf_url: "https://arxiv.org/pdf/2604.04202v1"
github_url: "https://github.com/aiming-lab/ClawArena"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent Benchmark"
  - "Dynamic Information"
  - "Belief Revision"
  - "Multi-Source Reasoning"
  - "Implicit Personalization"
  - "Evaluation Framework"
relevance_score: 9.0
---

# ClawArena: Benchmarking AI Agents in Evolving Information Environments

## 原始摘要

AI agents deployed as persistent assistants must maintain correct beliefs as their information environment evolves. In practice, evidence is scattered across heterogeneous sources that often contradict one another, new information can invalidate earlier conclusions, and user preferences surface through corrections rather than explicit instructions. Existing benchmarks largely assume static, single-authority settings and do not evaluate whether agents can keep up with this complexity. We introduce ClawArena, a benchmark for evaluating AI agents in evolving information environments. Each scenario maintains a complete hidden ground truth while exposing the agent only to noisy, partial, and sometimes contradictory traces across multi-channel sessions, workspace files, and staged updates. Evaluation is organized around three coupled challenges: multi-source conflict reasoning, dynamic belief revision, and implicit personalization, whose interactions yield a 14-category question taxonomy. Two question formats, multi-choice (set-selection) and shell-based executable checks, test both reasoning and workspace grounding. The current release contains 64 scenarios across 8 professional domains, totaling 1{,}879 evaluation rounds and 365 dynamic updates. Experiments on five agent frameworks and five language models show that both model capability (15.4% range) and framework design (9.2%) substantially affect performance, that self-evolving skill frameworks can partially close model-capability gaps, and that belief revision difficulty is determined by update design strategy rather than the mere presence of updates. Code is available at https://github.com/aiming-lab/ClawArena.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决AI智能体在动态、多源、用户特定的信息环境中如何维持正确信念的问题。研究背景是，当AI智能体作为持久性助手部署时，必须应对信息环境不断演变的挑战，例如证据分散在异构且常相互矛盾的来源中、新信息可能推翻先前结论，以及用户偏好通过隐式修正而非明确指令体现。现有评估方法存在不足：大多数基准测试假设静态、单一权威的信息环境，仅测试检索、组合或长期记忆等片段能力，未能全面评估智能体在复杂动态环境中的表现，特别是处理多源冲突、动态信念修正和隐式个性化这三项耦合挑战的能力。因此，本文的核心问题是设计一个基准测试，以系统评估AI智能体在演化信息环境中维持准确、最新信念的综合能力，填补现有评估在真实场景复杂性方面的空白。

### Q2: 有哪些相关研究？

相关研究主要可分为两大类：代理基准测试和大型语言模型（LLM）代理。

在**代理基准测试**方面，现有工作多聚焦于特定能力。例如，SWE-bench、AgentBench、WebArena等任务导向基准主要评测工具使用、规划和执行，但通常假设信息源单一且无冲突。HotpotQA、MuSiQue等多跳问答基准侧重于从静态证据中检索和组合信息；ConflictQA虽然引入了相互矛盾的主张，但其证据在推理时仍是固定的，无法评估模型在新证据出现后是否应修正先前判断。LoCoMo、PersonaChat等记忆与人物角色基准关注长期记忆和用户一致性，但未将跨源冲突解决、动态更新和隐式偏好保持等挑战置于同一评估场景中。本文提出的ClawArena旨在填补这一空白，它独特地将多源冲突推理、动态信念修正和隐式个性化这三个相互耦合的挑战结合起来进行评测，模拟了真实部署中信息环境持续演变的复杂性。

在**LLM代理**方面，相关研究推动了代理能力的发展。专注于推理的模型在复杂多步任务上表现出色，工具增强的代理可以与外部API、代码解释器和文件系统交互。近期研究还探索了多智能体协调、面向科学可视化和图表生成的领域特定多智能体系统，以及部分可观测下的长程规划。然而，大多数代理架构的评估环境是“片段式”的，任务间环境会重置。ClawArena则针对“持久助手”这一范式进行设计，要求代理在多次会话中积累信念，并随着信息环境演变而修正它们，这与前述工作的评估设定有本质区别。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为ClawArena的基准测试框架来解决AI智能体在动态信息环境中保持正确信念的评估难题。其核心方法是模拟一个真实、持续演变且充满噪声和矛盾的信息环境，并设计了一套系统的评估体系来量化智能体在三个耦合挑战上的表现：多源冲突推理、动态信念修正和隐式个性化。

整体框架采用分层结构设计。每个场景包含六个层级：第0层是隐藏的客观事实（Ground Truth），作为评估的黄金标准；第1至4层对智能体可见，包括工作区文件、多通道会话历史、评估问题以及分阶段注入的更新包；第5层是内部生成指南。这种设计确保了评估的可靠性，即智能体只能观察到不完整且可能矛盾的“痕迹”，而正确答案始终对照隐藏的客观事实来判定。

主要模块与关键技术包括：
1.  **场景构建**：通过一个四阶段的构建流程确保规模与真实性。首先手工创建种子场景以确立质量标准，然后归纳出元规范来约束后续的大规模生成。关键创新在于利用真实世界的数据分布（如邮件量、提交模式）来约束生成过程，确保工作区文档、会话模式（如消息时序、噪声比例）和因果关系的真实性。
2.  **评估维度与问题分类法**：定义了三个核心评估维度（MS, DU, P），并创新性地考察它们的两两及三者交互，共产生7个组合类别。每个类别进一步分为“回忆”（检索证据）和“推理”（得出结论）变体，最终形成一个包含14个类别的精细问题分类法。这迫使智能体必须综合应对所有挑战，而非孤立解决单一问题。
3.  **动态更新与个性化协议**：更新设计为分阶段注入，包括改变事实记录的客观更新和改变来源可信度的主观更新，旨在测试信念修正而非单纯的信息累积。个性化评估通过一个四阶段协议进行，最终在“静默考试”轮次（不提供任何提示）中评分，迫使智能体从先前的交互模式中学习用户偏好。
4.  **双重问题格式**：采用多选题（集合选择）和基于Shell的可执行检查两种格式，分别测试智能体的推理能力和对工作区证据的实际落地验证能力。

创新点在于：首次系统性地将多源、动态、个性化这三个现实信息环境的特质及其相互作用形式化为一个可衡量的基准；通过隐藏客观事实和分层可见信息的设计，确保了评估的严谨性；构建了一套结合真实世界约束的、可扩展的场景生成与验证流程。

### Q4: 论文做了哪些实验？

论文的实验主要分为两部分：跨框架比较和跨模型比较，以评估框架设计和模型能力对智能体在动态信息环境中表现的影响。

**实验设置与数据集**：实验在ClawArena基准上进行，该基准包含64个场景，覆盖8个专业领域，总计1,879个评估轮次和365次动态更新。由于评估成本高昂（全量运行约需10,100美元），研究选取了一个包含12个场景（337轮，占全量17.9%）的代表性子集进行主要实验。评估结合了多项选择题（集合选择）和基于shell的可执行检查两种形式，从多源冲突推理、动态信念修正和隐式个性化三个维度进行综合评分。

**对比方法**：
- **框架**：评估了五种AI智能体框架，包括OpenClaw（企业级）、Claude Code（官方CLI）、NanoBot（极简）、PicoClaw（轻量级）以及基于OpenClaw构建的、支持技能自演化的MetaClaw。
- **模型**：评估了五个大语言模型，涵盖Anthropic的三个能力层级（Opus 4.6、Sonnet 4.6、Haiku 4.5）和OpenAI的两代模型（GPT-5.2、GPT-5.1）。

**主要结果与关键指标**：
1.  **框架设计的影响**：在固定使用GPT-5.1模型的跨框架实验中，技能自演化框架MetaClaw取得最佳综合得分（0.603），优于其底层执行器OpenClaw（0.579）。框架设计导致的性能差异范围达0.092。MetaClaw在执行评估上优势明显（0.511），表明技能自演化显著提升了工作空间接地操作的能力。
2.  **模型能力的影响**：在固定使用OpenClaw框架的跨模型实验中，模型能力主导性能差异，差异范围达0.154。模型表现呈明确梯度：Claude Opus 4.6（0.735）> Sonnet 4.6（0.708）> Haiku 4.5（0.614）> GPT-5.1（0.581）。推理（多选题）与工作空间接地（可执行检查）能力仅中度相关。
3.  **动态信念修正**：研究发现，信念修正的难度取决于更新设计的策略（如针对性矛盾更新），而非单纯更新次数。在针对性更新后，所有配置的性能下降0.28-0.36。
4.  **领域与语言效应**：不同领域间性能差异巨大，同一模型在不同领域的表现波动可超过60%。GPT-5.2在中文企业场景中表现突出，表明语言特定训练数据影响显著。

### Q5: 有什么可以进一步探索的点？

该论文提出的ClawArena基准在动态信息环境评估上迈出了重要一步，但仍存在一些局限性和可拓展方向。首先，其场景虽覆盖8个专业领域，但可能未充分涵盖更开放、模糊的现实决策场景（如社交媒体信息流或突发新闻的快速演变），未来可增加跨文化、多语言或高噪声环境下的测试。其次，评估主要依赖预设的“隐藏事实”，但现实世界往往缺乏明确基准，可探索基于群体共识或概率真相的评估机制。在技术层面，当前智能体多依赖被动更新响应，未来可研究主动信息探测与验证机制，例如让智能体自主发起查询或权衡信息源可信度。此外，个人化目前主要通过修正反馈实现，未来可整合长期用户行为建模，使智能体能预见偏好变化。最后，该基准尚未深入测试智能体在信息冲突时的解释能力或协作决策潜力，这些方向对构建可信、可协作的持久化助手至关重要。

### Q6: 总结一下论文的主要内容

该论文提出了ClawArena基准测试，旨在评估AI智能体在不断演化的信息环境中的能力。核心问题是现有基准大多假设静态、单一权威的信息环境，无法评估智能体在现实复杂场景中（如信息分散、矛盾、动态更新且用户偏好隐式表达）是否能维持正确信念。

论文的方法是通过构建模拟真实工作流程的场景来评估智能体。每个场景包含一个完整的隐藏事实真相，但仅向智能体暴露来自多通道会话、工作空间文件和分阶段更新的嘈杂、片面且有时矛盾的信息痕迹。评估围绕三个相互关联的挑战组织：多源冲突推理、动态信念修正和隐式个性化，并由此衍生出一个包含14个类别的问题分类体系。采用多选题（集合选择）和基于shell的可执行检查两种问题格式，以测试推理能力和工作空间落地情况。当前版本包含8个专业领域的64个场景，总计1879个评估轮次和365个动态更新。

主要结论显示，模型能力（影响范围15.4%）对性能的主导作用超过框架设计（9.2%），但自演化技能框架能在一定程度上弥补基础模型的不足。信念修正的难度主要取决于更新设计策略而非更新数量，且总体得分可能掩盖性质不同的失败模式。该基准的意义在于为社区提供了一个衡量和提升AI智能体在现实部署环境中维持正确信念能力的工具。
