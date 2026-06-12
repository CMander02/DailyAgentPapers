---
title: "ProPlay: Procedural World Models for Self-Evolving LLM Agents"
authors:
  - "Yijun Ma"
  - "Zehong Wang"
  - "Yiyang Li"
  - "Ziming Li"
  - "Xiaoguang Guo"
  - "Weixiang Sun"
  - "Chuxu Zhang"
  - "Yanfang Ye"
date: "2026-06-11"
arxiv_id: "2606.12780"
arxiv_url: "https://arxiv.org/abs/2606.12780"
pdf_url: "https://arxiv.org/pdf/2606.12780v1"
github_url: "https://github.com/antman9914/proplay"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "LLM Agent"
  - "World Model"
  - "Self-Evolution"
  - "Procedural Planning"
  - "Memory"
  - "Environment Understanding"
relevance_score: 8.5
---

# ProPlay: Procedural World Models for Self-Evolving LLM Agents

## 原始摘要

Self-evolving agents are expected to improve through interaction without external supervision, but this remains difficult in partially observable environments where agents must explore actively, learn from limited feedback, and decide when to trust prior experience. Existing LLM-agent methods often rely on memory or planning modules, yet they rarely close the loop between them to continually refine an internal understanding of environment dynamics. We introduce ProPlay, a procedural world model that supports procedure-level preplay, where agents can rehearse future procedural paths using the learned world knowledge. Rather than representing experience as isolated rules or low-level action constraints, ProPlay abstracts successful trajectories into procedures and organizes them in a procedure graph that captures causal transitions among task stages. Each transition is associated with a reliability record embedding to estimate its task-specific contribution from past outcomes. Before each episode, ProPlay simulates future procedural trajectories over known graph structures as structured soft guidance; after execution, it refines the graph using environment feedback. Experiments on public benchmarks show that ProPlay consistently improves environment understanding and self-evolution capability over strong baselines. Our code has been released in https://github.com/antman9914/proplay.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在部分可观测环境中，自我进化的LLM代理如何通过闭环交互不断内化环境动态的核心问题。研究背景是期望代理无需外部监督，仅通过与环境的持续互动来改进，但现有方法面临三个关键挑战：1）代理必须主动探索而非被动观察；2）需要以正确的抽象层级积累经验（原始轨迹或孤立规则难以揭示任务成功的高阶因果结构）；3）必须判断何时信任过往经验（经验可能噪声大、过拟合或与当前目标无关）。现有方法存在明显不足：基于记忆的方法虽能存储经验，但无法统一规划与记忆的闭环；基于规划的方法虽能搜索路径，却通常将记忆与规划视为独立模块；而当前基于世界模型的方法（如Wall-E、WorldCoder）虽学习了行动级规则，但主要捕获局部约束，忽略了任务的高层因果结构，且对行动选择的直接影响可能损害探索与利用的平衡。因此，本文的核心问题是：如何构建一个能够不断从交互中“提取—精炼—选择性利用”过程级抽象知识的统一机制，使LLM代理能在部分可观测环境中，通过“预演”未来过程路径并基于反馈闭环更新内部环境理解，实现真正的自我进化。

### Q2: 有哪些相关研究？

1. **自进化智能体方法**：现有工作如基于记忆的经验积累（规则提取、层次化记忆管理）和规划方法（树搜索、世界模型引导探索），但大多将记忆与规划视为独立模块，缺乏统一框架。ProPlay通过过程世界模型将两者闭环，在预演中利用过程图推理未来路径，执行后根据反馈细化模型，实现环境理解的持续改进。

2. **世界模型方法**：早期方法如RAP将LLM本身作为隐式世界模型进行MCTS规划，WKM从离线轨迹蒸馏知识，WorldCoder和Wall-E支持在线更新。但这类方法仅关注低层动作约束或孤立规则，忽略了任务阶段间的过程因果结构。ProPlay创新性地构建过程图，捕获过程级因果转换关系，并通过可靠性记录嵌入评估路径贡献，实现长程因果依赖的显式建模。

3. **与基线的关系**：相较RAP等基于内部模拟的方法，ProPlay避免将LLM作为隐式模型，而是显式结构化过程知识；相比WorldCoder等基于规则的方法，ProPlay通过过程图支持结构化预演，而非逐条规则应用。实验证明ProPlay在环境理解与自进化能力上一致优于强基线方法。

### Q3: 论文如何解决这个问题？

ProPlay通过引入过程世界模型（procedural world model）和预演机制（preplay），构建了一个自我演化的闭环系统，以解决部分可观测环境中的自主探索与经验利用难题。其核心架构是一个持续演进的过程图（procedure graph）\(\mathcal{G}=(\mathcal{P}, \mathcal{E}, \mathcal{C})\)，其中节点\(\mathcal{P}\)代表从成功轨迹中抽象出的自然语言描述的任务阶段（过程），边\(\mathcal{E}\)表示这些阶段之间的因果转移，而可靠性记录嵌入（reliability record embedding）\(\mathcal{C}: \mathcal{E} \rightarrow \mathbb{R}^{d_c}\)则编码了每个转移对特定任务的贡献度。

系统在每轮任务中运行三个紧密耦合的阶段：1）**预演**：在每轮任务开始前，ProPlay利用当前过程图和失败经验，让LLM智能体基于任务描述推理构建一个高层次的预期过程轨迹（\(W^*\)）作为软引导（soft guidance），而非硬约束，智能体在任务执行中保持自由探索的能力，策略\(\pi_\theta(a_t | o_{\leq t}, W^*)\)同时依赖交互历史和预演轨迹。2）**执行与反馈**：智能体在软引导下执行任务，产生轨迹后，系统通过过程归纳（procedure induction）从成功前缀轨迹中提取新过程节点，并合并至图中；同时，将失败后缀部分存储为失败经验。3) **可靠性更新**：根据公式基于每轮获得的奖励更新每个转移的可靠性记录嵌入\(c_{ij}^k = \sum_{t=1}^k \mathbb{I}((p_i,p_j)\in W^t) \cdot R^t \cdot \phi(d_{\tau_t})\)，以此巩固通用知识并抑制噪音转移。这一“查询-执行-精炼”循环使得ProPlay能持续内化环境动态，实现稳定的自我演化。

### Q4: 论文做了哪些实验？

论文在三个公开基准上评估了ProPlay。ScienceWorld包含270个科学推理任务（23种类型），τ-Bench模拟多轮工具交互（零售115个/航空50个任务），PlanCraft是Minecraft风格的多步合成任务（187个，分三难度）。对比方法包括标准智能体（ReAct、Reflexion）、记忆与规划增强方法（ExpeL、LATS）以及世界模型方法（WorldCoder、Wall-E），所有方法均使用GPT-4.1-mini进行在线单次推理。主要结果方面，ProPlay在所有基准上取得最优或次优平均奖赏。在ScienceWorld上成功率37.4%、平均分70.2，显著优于规划型和世界模型基线。消融实验显示：移除程序图导致成功率降至34.8%，移除程序转移降至32.2%，移除可靠性记录降至35.6；用动作级世界模型替代程序级后得分68.8。任务级分析表明ProPlay在多步程序化任务上优势显著（如boil、温度测量），但在需要精确量化推理的熔点测量和工具组合任务上表现不佳。自演化分析揭示程序图呈现“概念节点早期积累→关系边后期超车”的两阶段增长模式。可靠性分析显示高可靠性规划不一定带来高成功率，未见过程序转移对探索至关重要。

### Q5: 有什么可以进一步探索的点？

ProPlay在程序化抽象范围上的局限性在于，它对具有清晰因果结构的任务表现良好，但难以处理需要精确数值推理或存在不可预测变体的任务。未来可探索将程序化结构与动作级规则自适应结合的策略，例如设计分层知识表示，通过元学习动态选择最合适的抽象粒度。单次预演机制意味着早期观测到计划错误后无法进行中期修正，改进思路是引入在线规划更新机制，允许代理在执行过程中根据新证据实时重绘程序图路径，或通过参数化注入程序知识来实现更灵活的调整。基准测试范围有限，尚未验证在网页导航、GUI交互等开放环境中的泛化能力。未来可扩展至这些领域，并研究如何从无边界动作空间中自动提取程序化结构，例如结合行为克隆或逆强化学习来发现隐式任务阶段。此外，程序图的可靠性记录可融入不确定性量化，以更好地平衡探索与利用。

### Q6: 总结一下论文的主要内容

ProPlay提出了一个面向部分可观测环境中自进化LLM智能体的程序化世界模型框架。问题定义在于智能体需要主动探索、从有限反馈中学习并决定何时信任先验经验，但现有方法缺乏对内部环境动态理解的持续优化。方法上，ProPlay将成功轨迹抽象为程序并构建程序图，捕捉任务阶段间的因果转换，每个转换关联可靠性记录嵌入以评估其任务贡献。在每轮任务前，它利用已学知识在程序图上模拟未来程序轨迹作为结构化软指导；执行后利用环境反馈优化图结构。主要结论是，在公共基准测试中，ProPlay在环境理解和自进化能力上持续优于强基线模型。其核心贡献在于通过程序级抽象实现了对世界知识的结构化表征与闭环迭代，为自进化智能体提供了原则性且有效的基础。
