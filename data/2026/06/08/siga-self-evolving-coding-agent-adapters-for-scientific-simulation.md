---
title: "SIGA: Self-Evolving Coding-Agent Adapters for Scientific Simulation"
authors:
  - "Matthew Ho"
  - "Brian Liu"
  - "Jixuan Chen"
  - "Audrey Wang"
  - "Lianhui Qin"
date: "2026-06-08"
arxiv_id: "2606.09774"
arxiv_url: "https://arxiv.org/abs/2606.09774"
pdf_url: "https://arxiv.org/pdf/2606.09774v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "LLM Agent"
  - "Coding Agent"
  - "Scientific Simulation"
  - "Grounding"
  - "Self-Evolution"
  - "Agent-Tool Interface"
  - "Memory"
  - "Validation"
  - "Multi-Agent"
relevance_score: 8.5
---

# SIGA: Self-Evolving Coding-Agent Adapters for Scientific Simulation

## 原始摘要

Advanced scientific simulators expose specialized input languages that turn simulation goals into executable configurations, but learning them can cost domain scientists hours to days. We study simulator setup as a problem of agent-tool interface grounding: what minimal simulator-specific adaptations are needed for an off-the-shelf coding agent to operate real scientific software? Our intuition is that coding agents already know how to navigate files, edit code, run commands, and repair outputs, but they lack the simulator's executable contract: its vocabulary, structural constraints, validation rules, and termination conditions. We introduce SIGA, a Simulator-Interface Grounding Adapter that supplies this contract through retrieval, procedural memory, in-trajectory validation, and validation-enforced termination. We primarily evaluate SIGA on GEOS, an open-source multiphysics simulator used in subsurface science. SIGA produces a complete GEOS deck in about five minutes with TreeSim above 0.90, matching an extended-budget human expert who took about three hours, a roughly 36x wall-clock speedup. On a harder held-out set, grounding raises TreeSim from 0.720 to 0.789, a roughly 10% relative gain over the bare agent, and can reduce the across-seed standard deviation by 16x. Self-evolution further improves SIGA by rewriting adapter contents from prior trajectories, yielding the highest held-out GEOS mean and matching or outperforming the strongest hand-designed configuration. Transfers to OpenFOAM and LAMMPS show that the dominant mechanism shifts by interface: validation matters most when structural completeness is the bottleneck, while memory and retrieval matter most when domain correctness is the bottleneck. These results suggest that lightweight, self-improvable grounding layers can turn general coding agents into practical operators of scientific software.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

研究背景：科学模拟在现代科研中至关重要，但使用 GEOS、LAMMPS 等高级模拟器需要掌握庞大的领域特定语言 (DSL)，包括语法、模式、物理约束和跨文件一致引用。科学家通常需要花费数小时甚至数天来学习文档、调试配置，才能生成可运行的输入文件，这是模拟驱动研究中的瓶颈。

现有方法不足：当前的科学智能体系统要么没有针对特定模拟器（如 GEOS）设计，要么从头构建模拟器特定的智能体循环（包括自定义规划、工具调用、重试逻辑和终止处理）。这忽略了前沿编码智能体（如 Claude Code 或 OpenHands）中已有的导航文件、迭代编辑、执行命令和修复输出等通用工程能力，且重新实现编排层会丢弃模型在特定智能体框架中校准的规划、工具使用和自纠正行为。

核心问题：本文研究如何将现成的编码智能体适配为可靠的科学模拟器设置助手。核心挑战在于智能体缺乏模拟器的“可执行契约”：即词汇表、结构约束、验证规则和终止条件等接口层面的知识。论文提出 SIGA（模拟器接口接地适配器），通过检索、过程记忆、轨迹内验证和验证强制的终止条件四个可复用组件，在最小化适配工作量的前提下，让通用编码智能体学会操作专业科学软件。

### Q2: 有哪些相关研究？

相关研究主要分为两类。第一类是面向科学代码与模拟器的LLM智能体，如ScienceAgentBench、DA-Code等基准测试，以及OpenHands、SWE-agent等通用框架，还有针对特定领域的ChemCrow、Coscientist。与本文最接近的是面向科学模拟器的智能体，包括OpenFOAM、分子动力学、有限元/力学和油藏模拟智能体。与这些工作不同，本文建立在现有编码工具链（Claude Code）之上，而非从头编写智能体循环。在OpenFOAM迁移研究中，本文直接与Foam-Agent 2.0和MetaOpenFOAM比较。第二类是自进化智能体、记忆与过程引导，近期工作将智能体能力视为规划、执行、反馈和优化的迭代循环，将经验外化为记忆或搜索状态。本文的自进化变体采用这类反思-重写范式，让智能体基于先前轨迹修订自身插件。与专注于编程能力的自我优化工作不同，本文聚焦于领域知识和过程引导是瓶颈的任务，这与Buffer of Thoughts等面向LLM的过程记忆与速查表研究相关。本文的核心区别在于，提出了轻量级、可自改进的适配层，而非复杂的全栈智能体系统。

### Q3: 论文如何解决这个问题？

该论文提出的SIGA（模拟器接口接地适配器）通过一个薄层适配器将通用编程智能体与科学模拟器的可执行合约对接，无需修改底层智能体的核心循环。核心设计围绕三个接口展开：上下文接口、工具接口和终止接口，分别对应四种关键机制。检索（R）作为工具接口的扩展，通过MCP服务器提供语义搜索工具，覆盖模拟器文档、XSD模式和示例XML文件，解决智能体因不熟悉领域术语导致的搜索失败。验证驱动自修正机制以两种形式实现：X作为可选工具接口，允许智能体在编辑过程中主动调用模式验证；S作为必选的终止接口，在智能体试图结束时强制验证工作空间中的配置，返回结构化修复反馈，确保输出完整可解析。程序记忆（M）通过上下文接口注入一个约775令牌的速查表，包含高频模拟器约定，避免重复发现。这四个组件构成一个二元设计空间{b∈{0,1}^{R,S,X,M}}，可针对不同模拟器灵活组合。创新点在于该适配器是自进化的（SE和SE-prose变体），通过离线分析历史轨迹重写适配器内容（如提示词和记忆），但保持基座模型和框架不变，实现跨会话的持续改进。整体框架强调轻量、可移植和最小修改，避免过度适应特定模型或框架版本。

### Q4: 论文做了哪些实验？

论文在GEOS、OpenFOAM和LAMMPS三个科学模拟器上进行了实验。主要实验包括：在GEOS上对四个接地组件（检索R、精炼循环S、验证器X、记忆M）进行2^(4-1)部分析因消融实验，使用8个细胞单元加上额外3个细胞（S+X+M、自我进化散文版、完整自我进化版），每个配置运行3次，使用1500秒超时限制。数据集包含46个GEOS任务，分成17个验证集和10个更难保留测试集，使用TreeSim指标（0-1范围，失败算作0）。基线是vanilla Claude Code。主要结果：在保留测试集上，SIGA将TreeSim从0.720提升到0.789（相对提升约10%），其中S+X+M达到0.783，完整自我进化版达到0.789。标准差从0.081降至0.012（X+M单元）和0.002（S+X单元）。在人类对比中，专家需要约3小时达到0.931 TreeSim，而SIGA约5分钟达到0.90以上（36倍加速）。转移到OpenFOAM和LAMMPS时发现主导机制随接口而变化。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在：1) 适配器主要在GEOS上验证，转移到OpenFOAM和LAMMPS时发现主导机制会随接口变化而显著不同，说明当前适配器设计并非通用最优；2) 自演化机制仅重写适配器内容，未涉及检索策略或验证规则的主动改进；3) 评估中人类专家结果存在不确定性与波动，基线对照不够严谨；4) 仅支持单次模拟配置生成，缺少多轮迭代优化的闭环。未来可探索：为不同接口类型自动适配最佳机制组合，如基于图神经网络判断接口瓶颈后动态激活验证或检索；引入强化学习让适配器在历史轨迹中自主优化验证规则和终止条件；扩展到多物理场耦合的复杂模拟场景，并评估长期交互中的持续学习能力。

### Q6: 总结一下论文的主要内容

这篇论文提出了SIGA（Simulator-Interface Grounding Adapter），旨在解决科学模拟软件配置这一瓶颈问题。科学模拟软件拥有特定的领域特定语言（DSL），科学家需要花费数小时甚至数天来学习。SIGA将现成的编程智能体（如Claude Code）封装成轻量适配层，通过四个可复用组件来“接地”模拟器接口：检索（提供语义文档访问）、程序记忆（保持高频词汇可见）、验证器（支持轨迹内检查）和终止钩子（强制进行结构验证）。实验表明，在GEOS模拟器上，SIGA能将专家约3小时的工作压缩到5分钟，质量相当，实现约36倍的加速，并将可靠性（方差）提升16倍。自我进化机制（从先前轨迹中重写适配器内容）进一步提升了效果。在OpenFOAM和LAMMPS上的迁移实验显示，关键机制随接口变化：验证对结构完整性更重要，而记忆和检索对领域正确性更关键。结论是，这种轻量级、可自我改进的接地层可以将通用编程智能体转化为高效的科
