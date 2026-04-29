---
title: "Toward Scalable Terminal Task Synthesis via Skill Graphs"
authors:
  - "Zhiyuan Fan"
  - "Tinghao Yu"
  - "Yuanjun Cai"
  - "Jiangtao Guan"
  - "Yun Yang"
  - "Dingxin Hu"
  - "Jiang Zhou"
  - "Xing Wu"
  - "Zhuo Han"
  - "Feng Zhang"
  - "Lilin Wang"
date: "2026-04-28"
arxiv_id: "2604.25727"
arxiv_url: "https://arxiv.org/abs/2604.25727"
pdf_url: "https://arxiv.org/pdf/2604.25727v1"
categories:
  - "cs.AI"
tags:
  - "终端Agent"
  - "任务合成"
  - "技能图谱"
  - "多智能体"
  - "训练数据生成"
relevance_score: 8.5
---

# Toward Scalable Terminal Task Synthesis via Skill Graphs

## 原始摘要

Terminal agents have demonstrated strong potential for autonomous command-line execution, yet their training remains constrained by the scarcity of high-quality and diverse execution trajectories. Existing approaches mitigate this bottleneck by synthesizing large-scale terminal task instances for trajectory sampling. However, they primarily focus on scaling the number of tasks while providing limited control over the diversity of execution trajectories that agents actually experience during training. In this paper, we present SkillSynth, an automated framework for terminal task synthesis built on a scenario-mediated skill graph. SkillSynth first constructs a large-scale skill graph, where scenarios serve as intermediate transition nodes that connect diverse command-line skills. It then samples paths from this graph as abstractions of real-world workflows, and uses a multi-agent harness to instantiate them into executable task instances. By grounding task synthesis in graph-sampled workflow paths, SkillSynth explicitly controls the diversity of minimal execution trajectories required to solve the synthesized tasks. Experiments on Terminal-Bench demonstrate the effectiveness of SkillSynth. Moreover, task instances synthesized by SkillSynth have been adopted to train Hy3 Preview, contributing to its enhanced agentic capabilities in terminal-based settings.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决终端智能体（terminal agent）训练中高质量、多样化执行轨迹稀缺的问题。研究背景方面，终端智能体利用命令行界面（CLI）作为通用动作空间，执行复杂的长序列计算机任务，但其能力受限于训练数据（即执行轨迹）的匮乏。现有方法主要依赖大规模任务合成来生成轨迹：一种方式是通过LLM生成分类学来扩展领域覆盖，但常偏离真实使用场景；另一种方式是从GitHub仓库生成任务实例，范围狭窄（仅限于软件工程领域如问题解决）。这些方法的根本不足在于，它们仅关注任务数量上的扩展，而缺乏对执行轨迹多样性的显式控制——不同任务实例常导致代理经历重叠的场景和重复的技能使用，使得训练出的模型泛化能力有限。基于此，本文提出核心问题：如何自动合成终端任务，使得生成的执行轨迹在场景（scenario）和技能（skill）两个维度上都具备可控的多样性，从而为终端智能体提供更丰富、更有效的训练数据，提升其在真实复杂环境中的性能。

### Q2: 有哪些相关研究？

在终端Agent的合成数据方法方面，相关工作可归纳为：

1. **终端Agent评测与训练**：Terminal-Bench提供了跨领域的手工任务集，但主要聚焦评测而非数据合成。本文提出的SkillSynth直接服务于Agent训练（如Hy3 Preview），通过可控多样性的轨迹生成来弥补训练数据稀缺问题。

2. **任务合成方法**：现有方法主要关注扩大任务数量（如随机组合命令），但对执行轨迹的多样性控制有限。SkillSynth的创新在于引入**场景中介技能图**，通过图采样路径抽象真实工作流，再利用多Agent框架实例化为可执行任务，显式控制最小执行轨迹的多样性。

3. **技能图与知识图谱**：本文与知识图谱方法（如ConceptNet）在结构化组织知识上类似，但SkillSynth专为终端命令设计，以场景为中间节点连接技能，强调工作流路径的完整性而非概念关系。

4. **多Agent协同框架**：当前已有工作探索多Agent协作（如AutoGen），但SkillSynth将其用于任务实例化——通过多个LLM角色（如命令生成器、验证器）将图路径转化为可运行任务，确保合成任务的可用性。

5. **与现有工作的区别**：不同于随机组合或模板化任务生成，SkillSynth基于完整工作流路径，保证每个合成任务对应一条从初始状态到目标状态的真实可执行轨迹，从而提升训练数据的质量与覆盖度。

### Q3: 论文如何解决这个问题？

SkillSynth通过三个核心阶段实现大规模终端任务合成。首先构建场景中介的技能图：从ClawHub和GitHub仓库中筛选出可执行、结构化的Linux终端技能，利用LLM推断每个技能的预置场景和后置场景，通过聚类去重和双向语义对齐，将技能与场景连接为有向多重图（节点为场景，边为技能），最终形成包含合法转换关系的统一技能图。

其次采用逆频率路径采样：摒弃均匀随机游走，维护场景访问计数v(σ)和技能使用计数μ(κ)，按概率p(σ)∝(v(σ)+1)^{-1}选取起始节点，路径扩展时按p(κ)∝(μ(κ)+1)^{-1}选择下一技能，同时强制单调前进（已访问节点和技能不再重复）。路径长度控制在1-7步，并确保技能组合唯一，通过计数递增驱动采样分布向场景-技能对（Ω×K）的均匀覆盖收敛。

最后通过多智能体编排生成可执行任务：将路径P分解为计划（子目标与预期输出）和实现（自然语言指令、初始文件系统快照、容器环境、验证脚本与标准答案）。利用LLM生成后，执行验证脚本确保可解性，再用LLM作为裁判检查指令与测试的对齐度及指令自包含性。失败时通过多轮工具使用（最多3轮修复，每轮20次工具调用）进行诊断修复。这种设计通过计划-实现分离和质量检查机制，避免了直接生成带来的质量问题。

### Q4: 论文做了哪些实验？

论文基于构建的技能图谱采样了3721条路径来合成任务实例，并进行了多组实验。实验设置上，选取Qwen3系列(8B、14B、32B)作为基座模型，在Terminal-Bench 1.0和2.0（分别含80和89个众包任务）上评估。主要结果包括：1）多智能体框架合成任务质量高，95.7%通过oracle检查，最终产出3560个可用任务实例；2）训练的Qwen3-32B+SS在TB 2.0上达到29.6分，超越更大的Qwen 3 Coder 480B (23.9分)；3）对比消融实验显示，SkillSynth路径采样策略在TB 1.0上比单技能策略高8.4分、比多技能随机组合高3.0分，在TB 2.0上分别高8.3和3.8分；4）轨迹多样性分析表明SkillSynth的独特场景-技能覆盖比基线高31%和19%。错误分析发现主要失败模式为部分实现(42.2%)和内联自测过度信任(29.5%)。

### Q5: 有什么可以进一步探索的点？

论文在任务合成中主要依赖链式路径采样，但真实工作流常包含并行或分支结构，未来可探索从技能图中采样子图（subgraph）来生成需要多技能并行执行的任务，从而提升复杂性和真实性。实验提到指令与测试间的对齐偏差（77%的失败源于测试脚本过指定或欠指定），这影响了强化学习的奖励信号，可以设计更鲁棒的任务验证机制，如引入语义匹配或可微测试生成来缓解。此外，38%的任务在0/3困难级别（完全无法解决），可结合主动学习或难度自适应路径采样策略，优先合成这些“硬”任务以填补长尾能力缺口。修复阶段存在15.9%的不可恢复故障（主要源于文件系统快照损坏），可引入状态回滚检查和重试机制（如提高采样温度）来提升容错率。最后，当前仅采用单一教师模型（MiniMax M2.7）生成轨迹，未来可集成多源教师模型并利用对比式过滤来提升轨迹质量与多样性。

### Q6: 总结一下论文的主要内容

论文提出SkillSynth框架，解决终端代理训练中高质量、多样化执行轨迹稀缺的问题。现有任务合成方法主要关注任务数量扩展，但对轨迹的实际多样性控制不足。SkillSynth通过构建以场景为中介的技能图（scenario-mediated skill graph），将场景作为连接不同命令行技能的中间过渡节点。从图中采样路径作为真实工作流的抽象，再利用多智能体机制将这些路径实例化为可执行的任务实例。通过基于图的路径采样，SkillSynth显式控制解决合成任务所需的最小执行轨迹多样性。实验在Terminal-Bench上验证了有效性，单次自动化运行生成3560个验证任务实例，通过率达95.7%。合成轨迹训练的Qwen3-8B和Qwen3-32B模型在基准测试上取得一致性提升，且被用于训练Hy3 Preview，增强了其终端代理能力。该技能图结构天然支持持续扩展，为大规模多样化终端任务合成提供了可扩展基础。
