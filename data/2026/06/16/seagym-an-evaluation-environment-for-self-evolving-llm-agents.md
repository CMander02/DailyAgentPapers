---
title: "SEAGym: An Evaluation Environment for Self-Evolving LLM Agents"
authors:
  - "Congjie Zheng"
  - "Chuanyi Xue"
  - "Bin Liang"
  - "Jun Yang"
  - "Changshui Zhang"
date: "2026-06-16"
arxiv_id: "2606.17546"
arxiv_url: "https://arxiv.org/abs/2606.17546"
pdf_url: "https://arxiv.org/pdf/2606.17546v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent评估"
  - "自我进化"
  - "智能体架构"
  - "评测基准"
  - "Agent生命周期管理"
relevance_score: 9.5
---

# SEAGym: An Evaluation Environment for Self-Evolving LLM Agents

## 原始摘要

Self-evolving LLM-based agents improve mainly by changing their agent harness: the structured execution layer around a base model, including prompts, memory, tools, middleware, runtime state, and the model-tool interaction loop. Existing evaluations often reduce this process to isolated task scores or a single sequential curve, obscuring whether an update produces reusable improvement, overfits recent tasks, increases cost, or harms older behavior. We introduce SEAGym, an evaluation environment for measuring agent harness updates across training, validation, test, replay, and cost records. SEAGym turns Harbor-compatible benchmarks into dynamic self-evolution task sources with train batches, frozen update-validation, held-out ID and OOD transfer views, replay diagnostics, and saved snapshot and metric records. Instantiating SEAGym on Terminal-Bench 2.0 and HLE, we compare ACE, TF-GRPO, and AHE under a shared epoch/batch protocol. The results show that these evaluation views provide complementary signals about the evolution process: frequent updates may fail to improve held-out performance, useful intermediate snapshots may collapse later, and source diversity and model backend can affect harness reliability.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决如何系统评估自我进化智能体（self-evolving LLM agents）在更新其“智能体装备”（agent harness）后，所带来的综合影响问题。研究背景是，基于大语言模型的智能体在部署后能通过修改提示词、记忆、工具、中间件等结构化执行层来实现自我进化。现有评估方法存在不足，通常仅使用孤立任务分数或单一顺序曲线来反映性能变化，这无法揭示更新是否带来可复用的改进、是否在近期任务上过拟合、是否增加了成本或损害了旧行为，也无法分析更新过程中的遗忘、回归、稳定性等问题。因此，本文的核心问题是：如何设计一个统一的评估环境，能够细粒度地测量智能体装备更新全过程，包括训练、验证、测试、回放和成本记录，从而提供关于进化过程的互补信号，让不同自我进化机制能在通用协议下被公平比较。

### Q2: 有哪些相关研究？

相关研究主要分为三类：**Agent 框架**、**持续学习与自我进化**以及**Agent 评测基准**。

1.  **Agent 框架（Agent Harness）**：相关研究定义了智能体的结构化执行层，包括提示词、内存、工具、中间件及交互循环等。早期工作关注推理-行动循环与API使用，近期工作强调工具文档、人机交互界面和内存管理是关键设计变量。生产实践（如OpenAI、Anthropic、LangChain）已将其系统化。SEAGym 通过将智能体框架作为可适应目标，并引入自然语言表达来支持消融实验，与之区分开来。

2.  **持续学习与自我进化（Continual Learning and Self-Evolution）**：持续学习关注任务序列中的适应、迁移、保留、回放和遗忘问题。自我进化将这一范式从参数学习扩展到智能体系统学习。现有工作分为两类：一是通过监督学习、强化学习或工具使用训练来优化基础模型；二是将智能体框架本身作为进化对象，通过环境反馈修改提示词、内存或工具等。SEAGym 强调，由于框架更新是持久且方法特化的，现有研究因缺乏共享的实验协议而难以比较，其贡献在于提供了一个包含训练、验证和回放的标准化协议。

3.  **Agent 评测基准（Agent Benchmarks）**：现有基准从静态文本评测转向交互式环境。但标准协议仅在独立回合中评估固定智能体，不支持持久化框架状态。专门针对自我进化或终身学习的基准很少，例如 SEA-Eval 和 LifelongAgentBench。SEAGym 与之不同，它旨在将现有基准转化为“动态自我进化任务源”，并提供验证、迁移、回放诊断等多种评估视图，从而填补了通用评测环境的空白。

### Q3: 论文如何解决这个问题？

SEAGym通过构建一个MDP风格的评估环境来解决自演化LLM智能体评估中的问题。其核心方法是将智能体演化建模为马尔可夫决策过程M=(S,A,P,R,ρ)，其中状态st包含当前智能体快照、调度位置和任务上下文。智能体快照At=(M,Ht)将固定基础模型M与可变马具状态Ht分离，Ht包括提示、记忆、工具、中间件等所有模型外部组件。

在架构设计上，SEAGym从静态基准测试中采样训练批次，让智能体执行任务生成轨迹并接收验证器反馈，然后应用自身更新规则Ht+1=U(Ht,Bt,Tt,Ft)完成状态转换。系统通过调度参数支持在线、单任务、批量、基于回合等多种自演化设置，将状态持久性、任务复用、批大小、更新频率等作为实验变量。

主要模块包括：1)数据集分割与评估视图分离：基础分割控制任务可见性，评估视图包括更新验证追踪中间快照、ID/OOD测试分布内外部迁移、重放诊断检测遗忘或回归；2)解耦的rollout和update组件：rollout执行任务返回轨迹批，update消耗轨迹批应用更新规则；3)基于Harbor的任务运行器复用，保持任务定义、环境、验证器和并行执行。

创新点在于：固定验证视图不参与更新以评估可复用改进，全谱系评估视图避免孤立指标误导，保存快照和度量记录支持离线诊断，以及通过Harbor兼容实现最小代码修改集成。

### Q4: 论文做了哪些实验？

SEAGym在Terminal-Bench 2.0和HLE（仅文本数学/物理）上进行了实验，使用80个源训练任务、35个验证任务、55个测试任务和80个HLE CS/AI及工程OOD迁移任务。默认采用5个epoch，训练批次大小20。主要对比了ACE、TF-GRPO和AHE三种方法，均基于DeepSeek-V4-Flash后端。

主要结果：AHE在所有视图上提升最大，验证成功率从40.0%提升至57.1%（+17.1），ID从40.0%提升至49.1%（+9.1），OOD从22.5%提升至28.8%（+6.3），每次更新消耗3.91M token。ACE验证仅从37.1%升至40.0%（+2.9），ID从30.9%升至34.5%（+3.6），OOD从22.5%升至25.0%（+2.5），无更新token消耗。TF-GRPO验证从31.4%升至48.6%（+17.1），ID从30.9%升至34.5%（+3.6），OOD从26.3%降至23.8%（-2.5），每次更新消耗1.60M token。

消融实验显示：批次大小20最优，批次10和80均导致性能退步；源多样性实验中，仅用HLE训练的最终快照完全崩溃（验证和ID均为0%），而混合源能恢复；跨模型迁移实验中，同一后端ID提升+3.6至+9.1，但跨后端转移不稳定且不对称。

### Q5: 有什么可以进一步探索的点？

SEAGym的局限性主要体现在三个方面。首先，环境仅验证了Terminal-Bench和HLE两类任务，未来需要扩展到web交互、长周期软件工程、多智能体协作等更丰富的智能体域。其次，当前实验仅关注模型外部框架（提示、记忆、工具）的演化，应进一步拓展至模型权重更新、在线RL微调或混合系统，从而对比框架级与参数级学习在成本、稳定性和迁移性上的差异。最后，多视角评估产生了快照保存与重评估的成本-覆盖权衡，未来可研究自适应回放、预算感知评估等高效机制，在保留回归、恢复与遗忘诊断能力的同时降低开销。此外，跨模型实验显示框架更新依赖于任务分布与后端，后续需探索更多源/目标域对与模型后端，以揭示哪些更新机制能产生稳定迁移、哪些会变得后端或基准依赖。

### Q6: 总结一下论文的主要内容

SEAGym是一个专门用于评估自演进大语言模型Agent的评测环境。该工作解决了现有评估方法将Agent自演进过程简化为孤立任务分数或单条曲线的问题，无法判断更新是否产生可复用的改进、是否过拟合新任务、是否增加成本或损害旧行为。SEAGym将Harbor兼容的基准测试转化为动态自演进任务源，提供训练批次、冻结验证、分布内和分布外迁移视图、回放诊断以及快照和指标记录。在Terminal-Bench 2.0和HLE上的实验比较了ACE、TF-GRPO和AHE三种方法，结果表明这些评测视角能提供互补的演进信号：频繁更新可能无法提升保留性能，有用的中间快照可能后来失效，源多样性和模型后端会影响框架可靠性。SEAGym的核心贡献是提供了一个受控的评估环境，能够比较不同方法更新了什么、这些更新是否泛化以及引入了什么成本或不稳定性。
