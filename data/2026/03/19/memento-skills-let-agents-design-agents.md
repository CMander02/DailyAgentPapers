---
title: "Memento-Skills: Let Agents Design Agents"
authors:
  - "Huichi Zhou"
  - "Siyuan Guo"
  - "Anjie Liu"
  - "Zhongwei Yu"
  - "Ziqin Gong"
  - "Bowen Zhao"
  - "Zhixun Chen"
  - "Menglong Zhang"
  - "Yihang Chen"
  - "Jinsong Li"
  - "Runyu Yang"
  - "Qiangbin Liu"
  - "Xinlei Yu"
  - "Jianmin Zhou"
  - "Na Wang"
  - "Chunyang Sun"
  - "Jun Wang"
date: "2026-03-19"
arxiv_id: "2603.18743"
arxiv_url: "https://arxiv.org/abs/2603.18743"
pdf_url: "https://arxiv.org/pdf/2603.18743v1"
github_url: "https://github.com/Memento-Teams/Memento-Skills"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "Agent Architecture"
  - "Continual Learning"
  - "Skill Learning"
  - "Memory-Augmented Agents"
  - "Agent Design Automation"
  - "Reinforcement Learning"
  - "Stateful Prompts"
  - "Tool Use"
  - "Benchmark Evaluation"
relevance_score: 9.0
---

# Memento-Skills: Let Agents Design Agents

## 原始摘要

We introduce \emph{Memento-Skills}, a generalist, continually-learnable LLM agent system that functions as an \emph{agent-designing agent}: it autonomously constructs, adapts, and improves task-specific agents through experience. The system is built on a memory-based reinforcement learning framework with \emph{stateful prompts}, where reusable skills (stored as structured markdown files) serve as persistent, evolving memory. These skills encode both behaviour and context, enabling the agent to carry forward knowledge across interactions.
  Starting from simple elementary skills (like Web search and terminal operations), the agent continually improves via the \emph{Read--Write Reflective Learning} mechanism introduced in \emph{Memento~2}~\cite{wang2025memento2}. In the \emph{read} phase, a behaviour-trainable skill router selects the most relevant skill conditioned on the current stateful prompt; in the \emph{write} phase, the agent updates and expands its skill library based on new experience. This closed-loop design enables \emph{continual learning without updating LLM parameters}, as all adaptation is realised through the evolution of externalised skills and prompts.
  Unlike prior approaches that rely on human-designed agents, Memento-Skills enables a generalist agent to \emph{design agents end-to-end} for new tasks. Through iterative skill generation and refinement, the system progressively improves its own capabilities. Experiments on the \emph{General AI Assistants} benchmark and \emph{Humanity's Last Exam} demonstrate sustained gains, achieving 26.2\% and 116.2\% relative improvements in overall accuracy, respectively. Code is available at https://github.com/Memento-Teams/Memento-Skills.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在部署后无法持续、高效地从自身交互经验中学习的问题。研究背景是，当前大多数LLM智能体在实际部署时，其模型参数是冻结的（frozen），无法进行持续的微调或参数更新。这导致智能体本质上是“无状态”的，其能力完全依赖于预训练时编码的知识和有限的上下文窗口，无法从部署后遇到的新任务和反馈中积累经验、自我改进。现有方法主要依赖人类预先设计任务特定的智能体或进行昂贵的模型微调，前者缺乏通用性和自动化，后者则面临数据需求大、计算成本高且容易过拟合的不足。

本文的核心问题是：**如何让一个通用的、参数冻结的LLM智能体，能够像人类一样，通过“记忆”和“反思”自己的成功与失败经验，自主地设计、适应并持续改进针对新任务的专用智能体，从而实现无需更新模型参数的持续学习（continual learning）**。为此，论文提出了Memento-Skills系统，其核心创新在于将外部记忆具体化为一个可重用、可演化的“技能库”。这些技能以结构化的Markdown文件存储，编码了行为模式和上下文知识。系统通过一个名为“读写反射学习”的闭环机制运作：在“读”阶段，根据当前状态从技能库中选择最相关的技能；在“写”阶段，根据任务执行后的反馈，对技能进行优化、更新或创建新技能。这样，所有的适应和学习都通过外部技能库和提示的演化来实现，LLM参数始终保持不变，从而以极低的成本实现了智能体的自我进化。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于提示的智能体、技能学习与组合方法，以及持续学习框架。

在**基于提示的智能体**方面，相关工作如ReAct、AutoGPT等通过设计提示或工具使用规则来执行任务。Memento-Skills的独特之处在于引入了“状态化提示”作为强化学习框架的一部分，并将技能外部化为可读写、可演化的结构化记忆，而非依赖固定的人类设计提示。

在**技能学习与组合**领域，研究如Skill-based RL、程序合成或工具学习旨在获取可复用的子程序。本文提出的“技能”以Markdown文件形式存储，不仅编码行为，还包含上下文，支持跨任务的知识迁移和组合。与许多需要预定义技能库或大量交互数据的方法不同，Memento-Skills的智能体能够从基础技能开始，自主设计和改进任务专用智能体。

在**持续学习**方面，传统方法常面临灾难性遗忘或需更新模型参数。本文借鉴并扩展了Memento 2的“读写反射学习”机制，通过外部技能库的迭代更新（而非调整LLM参数）实现持续性能提升，这与需要微调模型或重放缓冲区的典型持续学习方案形成对比。

### Q3: 论文如何解决这个问题？

论文通过提出并实现一个名为“Memento-Skills”的通用、持续学习的LLM智能体系统来解决自主构建、适应和改进任务特定智能体的问题。其核心方法是基于记忆的强化学习框架，并引入了“状态化提示”和“读写反思学习”机制，使智能体能够通过经验自主设计和演化技能，而无需更新底层大语言模型的参数。

**整体框架与主要模块**：
系统围绕一个外部化的、可写的“技能库”运行，该库存储结构化的Markdown文件（SKILL.md）及辅助脚本和提示。整体流程遵循“观察→读取→行动→反馈→写入”的五步闭环。关键模块包括：
1.  **技能路由器**：在“读取”阶段，根据当前状态化提示（结合任务查询和累积的提示记忆）从技能库中选择最相关的技能。该路由器通过行为可训练的机制进行优化，旨在预测执行成功率，而不仅仅是语义匹配。
2.  **读写反思学习机制**：这是系统的创新核心。“读取”对应策略改进：智能体检索并执行技能。“写入”对应策略评估与改进的闭环：智能体首先记录执行结果和诊断轨迹进行评估，然后利用这些信息修订技能文件，从而直接改进未来策略。这被视为一种策略迭代。
3.  **技能演化组件**：包括（a）**失败归因选择器**：基于LLM分析完整执行轨迹，识别对错误负主要责任的单个技能，实现技能级信用分配。（b）**技能重写器**：根据诊断，提出针对性的文件级更新（如添加防护或替代策略）。（c）**技能发现机制**：当某个技能的运行效用（经验成功率）低于阈值时，系统会触发技能发现，要么用根本不同的方法重构现有技能，要么合成全新技能以覆盖任务空间的新区域。
4.  **自动单元测试门**：为防止回归，所有技能修改都需通过此门。系统会生成合成测试用例，通过更新后的技能执行，并由评判器打分，确保变更有效。

**创新点与关键技术**：
1.  **端到端的智能体设计智能体**：区别于依赖人工设计智能体的先前方法，Memento-Skills使一个通用智能体能通过迭代的技能生成与精化，为全新任务从头设计专用智能体。
2.  **通过外部化技能实现持续学习**：所有适应和提升都通过技能和提示的演化实现，无需微调LLM参数，解决了模型更新成本高和灾难性遗忘的问题。
3.  **行为对齐的技能路由与合成数据训练**：为解决技能库庞大导致的探索难题，系统采用“一步离线”视图，利用LLM作为“模拟器”合成密集的正负查询样本，训练路由器拟合预测执行成功的Q函数，超越了基于余弦相似度的语义检索。
4.  **结构化、可执行的多构件技能表示**：技能不仅是文本指南，而是包含声明式规范、辅助脚本和提示的可执行多构件集合，确保了其实用性和可迁移性。
5.  **分层的技能维护策略**：系统根据技能效用动态选择“重写”（打补丁）或“发现”（重构/新建），实现了技能库的稳健进化与扩展。

总之，论文通过将外部技能库作为可演化的记忆，结合创新的读写反思学习循环、行为对齐的路由以及分层的技能维护机制，构建了一个能够自主设计并持续改进其子智能体的系统。

### Q4: 论文做了哪些实验？

论文在实验设置上，主要评估了Memento-Skills作为一个自主设计智能体的系统的持续学习与泛化能力。实验使用了两个基准测试：**General AI Assistants (GAA)** 基准和 **Humanity's Last Exam (HLE)** 基准。GAA基准旨在评估智能体在多样化、开放式任务中的表现，而HLE则是一个更具挑战性的综合性考试环境。

在对比方法上，论文将Memento-Skills与依赖人工设计的智能体的先前方法进行了比较，以突显其“端到端自主设计智能体”的优势。其核心机制是**基于记忆的强化学习框架**和**状态提示**，通过**读写反思学习**循环来进化外部化的技能库，而无需更新大语言模型本身的参数。

主要结果以整体准确率的相对提升作为关键数据指标。在GAA基准上，Memento-Skills取得了**26.2%** 的相对准确率提升；在更具挑战性的HLE基准上，提升更为显著，达到了**116.2%** 的相对准确率提升。这些结果表明，该系统通过迭代的技能生成与优化，能够持续、显著地提升其在复杂任务上的性能。

### Q5: 有什么可以进一步探索的点？

该论文的框架虽具创新性，但仍存在若干局限和值得深挖的方向。首先，其技能库的演化完全依赖外部化的提示和结构化文件，这可能面临技能爆炸、冗余或冲突的风险，未来需研究更高效的技能压缩、合并与遗忘机制。其次，系统在复杂、多步骤任务中的长期规划能力仍有不足，技能路由器的选择可能陷入局部最优，可探索引入分层强化学习或元技能组合来提升抽象与推理能力。此外，实验主要在现有基准上进行，未来需在开放、动态的真实世界环境中验证其持续学习与泛化能力。结合见解，可能的改进包括：1）让技能本身具备可微参数，并与轻量级神经模块结合，实现参数化技能与符号化知识的融合；2）引入多智能体协作视角，使系统能设计出分工不同的子智能体来协同解决复杂问题；3）探索技能的可解释性与安全边界，防止其设计出有害或不可控的代理行为。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为 Memento-Skills 的新型通用大语言模型智能体系统，其核心创新在于让智能体能够自主设计智能体。该系统旨在解决传统方法依赖人工设计特定任务智能体的局限性，实现智能体通过经验自主构建、调整和改进任务专用代理的能力。

方法上，该系统基于一个具有“状态提示”的基于记忆的强化学习框架。其核心组件是可重用技能，这些技能以结构化 Markdown 文件形式存储，作为持久且不断演化的记忆，编码了行为与上下文。系统从基础技能（如网络搜索、终端操作）开始，通过引入的“读写反思学习”机制进行持续学习：在“读”阶段，一个可训练的技能路由器根据当前状态提示选择最相关的技能；在“写”阶段，智能体根据新经验更新和扩展其技能库。这种闭环设计实现了无需更新大语言模型参数的持续学习，所有适应都通过外部化技能和提示的演化来完成。

主要结论显示，该系统能够通过迭代的技能生成与精炼，端到端地为新任务设计智能体，从而持续提升自身能力。在“通用AI助手”基准和“人类终极考试”上的实验证明了其持续的性能增益，分别实现了26.2%和116.2%的相对准确率提升。该工作为构建具备自主进化能力的通用智能体系统提供了新思路。
