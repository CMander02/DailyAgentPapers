---
title: "SWE-Future: Forecast-Conditioned Data Synthesis for Future-Oriented Software Engineering Agents"
authors:
  - "Qiao Zhao"
  - "JianYing Qu"
  - "Jun Zhang"
  - "Yehua Yang"
  - "Hanwen Du"
  - "Zhongkai Sun"
date: "2026-06-17"
arxiv_id: "2606.18733"
arxiv_url: "https://arxiv.org/abs/2606.18733"
pdf_url: "https://arxiv.org/pdf/2606.18733v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "数据合成"
  - "编程Agent"
  - "评测基准"
  - "代码Agent"
  - "未来导向"
  - "任务生成"
relevance_score: 7.5
---

# SWE-Future: Forecast-Conditioned Data Synthesis for Future-Oriented Software Engineering Agents

## 原始摘要

Realistic coding-agent benchmarks often replay public GitHub issues and pull requests, making them vulnerable to overlap with model pretraining, fine-tuning, synthetic-data generation, or benchmark-driven model selection. Fully synthetic tasks avoid direct historical replay, but can drift away from real repository needs. We propose SWE-Future, a forecast-conditioned data synthesis method for future-oriented coding tasks. Given a forecast snapshot at time $T_0$, the method uses only pre-$T_0$ repository evidence to forecast future feature implementation/enhancement, bugfix, and refactor task families. We first validate this forecasting step retrospectively: after forecasts are fixed, later pull requests are used only to measure whether the predicted task families match future repository work. In an 80-repository study, the forecaster achieves 58.1\% future-work relevance under the main semantic matching metric. We then use validated forecast families as conditioning signals to synthesize a 200-task coding-agent dataset across 61 repositories from a task-generation snapshot, rather than replaying the later pull requests used for validation. SWE-Future shows that repository-evolution forecasts can guide realistic, future-oriented coding-task synthesis while reducing direct dependence on historical pull-request replay.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前软件工程智能体（coding agent）训练与评估数据面临的“数据污染”与“真实性”矛盾。现有方法主要依赖两种：一是回放历史GitHub Issue和PR，这种方式虽然真实，但由于公开数据可能已被模型预训练、微调或基准测试所用，存在严重的数据污染风险，导致评估结果不可信；二是纯合成数据，虽然避免了历史回放，但往往脱离实际仓库的代码规范、维护者优先级、依赖约束等，缺乏“仓库压力”，导致任务不接地气。为平衡两者，本文提出SWE-Future。其核心问题是：如何在不直接回放历史PR的前提下，生成既符合仓库实际演进需求、又面向未来的编码任务，从而避免数据污染。解决方案是通过对仓库在时间点T0之前的证据（如Issue、PR、标签）进行预测，生成“功能实现/增强、bug修复、重构”等任务族，然后用这些预测来引导合成未来导向的编码任务，而非直接使用后续的真实PR。这样既保持了任务的真实性和仓库相关性，又切断了对历史数据的直接依赖。

### Q2: 有哪些相关研究？

1. **历史GitHub任务构建类**：包括SWE-Bench、SWE-Bench++、FEA-Bench和SWE-Factory等，通过直接回放真实GitHub issue及其对应PR构建评测任务。本文与之区别在于：这些方法依赖已经发生的真实工作（易导致数据污染），而SWE-Future仅将未来PR作为隐藏验证集，任务生成基于已验证的预测类别。

2. **基准污染与排行榜压力类**：现有研究广泛关注GitHub派生基准（如SWE-Bench）的污染风险，包括预训练、微调、合成数据生成或模型选择中的数据泄露。SWE-Future的目标不是证明模型从未见过代码库，而是从根本上避免直接回放历史PR作为任务材料。

3. **任务工厂与合成环境类**：SWE-Hub、daVinci-Env、SWE-Playground等专注于大规模环境构建和可执行任务合成。本文区别在于：不解决任务构建本身的工程问题，而是回答"应该为哪些代码库特定任务类别进行合成"这一上游问题，以预测有效性作为条件信号。

4. **软件演化与时间有效性类**：软件工程长期利用代码库历史进行缺陷预测等。本文借用时间边界（快照T₀）但改变目标：预测未来工作类别并用于指导T_gen时刻的任务合成，而非直接使用未来PR作为任务。

### Q3: 论文如何解决这个问题？

论文提出了一种名为SWE-Future的预测条件数据合成方法，用于构建面向未来的编码代理任务。核心思想是利用仓库在时间点T0之前的证据预测未来的任务族（如功能实现、bug修复和重构），而非直接回放历史PR。

**整体框架**分为四个阶段：
1. **预测构建**：仅使用T0前的仓库证据（issue和PR）。通过四个步骤生成任务族：收集信号（排除依赖更新等非关键任务）、聚类信号（要求每个簇至少有两个信号）、评分过滤（基于信号数量、类型和标签多样性的启发式评分）以及模板化输出（每个任务族包含类别、锚点、预期行为、验收标准等结构化描述）。最终在80个仓库中生成260个任务族。
2. **回顾验证**：在T0到T1的六个月窗口内，将冻结的预测族与后期PR元数据进行语义匹配验证。使用两级指标：强匹配（精确或部分匹配）和相关匹配（类别或模块方向一致）。主要指标是“强+相关”占比（58.1%），这确保了预测方向与仓库后续工作的一致性。
3. **任务合成**：利用通过验证的预测族作为条件信号，在Tgen时间点的仓库快照基础上合成任务。核心创新在于：预测族只提供方向性指引，具体任务通过检查Tgen代码库的实际状态来实例化，从而避免直接回放后期PR的内容。
4. **任务筛选**：对合成任务执行严格的质量控制，包括测试补丁构建、泄露检查、FAIL_TO_PASS和PASS_TO_PASS验证，最终发布200个高质量任务。

**关键技术**包括：基于持续性的预测假设（重复的预T0信号表明持续的工作方向）、启发式聚类评分、类别感知的语义匹配度量和多阶段验证漏斗。创新点在于将“预测未来任务方向”与“基于当前代码状态合成具体任务”相分离，既保证了任务的真实性，又避免了对历史PR的直接依赖。

### Q4: 论文做了哪些实验？

论文研究了SWE-Future方法在生成面向未来的编码任务数据集方面的有效性。实验设置包括两个阶段：先验证预测步骤的准确性，再基于预测结果合成任务数据集。

实验使用80个GitHub仓库进行预测验证，以仓库在时间T0前的所有证据预测未来任务族（如新功能、缺陷修复、重构），后续的拉取请求仅作为衡量预测是否匹配实际工作的指标。主要结果：在主要语义匹配指标下，预测器达到58.1%的未来工作相关性。

接着，从任务生成快照中的61个仓库提取200个已验证的预测任务族，用于合成200个编码代理任务的数据集，而非直接回放用于验证的后续拉取请求。实验未列出具体对比方法，而是通过消融分析证明预测机制能有效引导未来导向的任务生成。关键数据指标：80仓库的58.1%语义匹配率，以及最终生成200个跨库任务。结果表明，仓库演化预测可指导现实且面向未来的编码任务合成，同时减少对历史拉取请求回放的直接依赖。

### Q5: 有什么可以进一步探索的点？

SWE-Future的未来探索主要集中在两个层面：一是降低预测阶段的不确定性。当前预测器可能从标签、追踪术语或仓库特定流程语言中捕捉噪声锚点，而非干净代码模块，未来应加强仓库证据的检索能力，并改进标签和追踪语言的噪声过滤，以提升预测家族的质量。二是提升执行阶段的质量。生成的测试补丁虽能使任务可执行，但可能不如长期维护者编写的测试精准，尤其对于旨在内部修改、保持行为的重构任务更为明显。未来应开发更丰富的项目特异性测试合成方法，使生成的测试补丁更接近维护者手写测试。此外，可考虑引入多轮验证机制，结合历史进化轨迹与代码库语义，提升预测的鲁棒性；或利用强化学习从失败案例中自动学习，优化特征工程，减少对人工先验知识的依赖，使合成数据更贴近真实仓库需求。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种面向未来的代码智能体数据合成方法SWE-Future，旨在解决现有基准测试因复现公开GitHub issue/PR而存在的严重数据污染问题。核心贡献在于将仓库演化预测作为条件信号，用于生成现实且无历史泄露的编程任务。方法分为四个阶段：首先，利用快照时间点前的仓库证据预测未来的任务族（如功能增强、Bug修复、重构）；其次，通过回顾性验证，使用预测后的PR元数据评估预测的准确性；接着，将验证有效的任务族作为条件，基于生成快照的仓库状态合成具体任务；最后，仅通过可执行验证的任务被纳入数据集。在80个仓库的研究中，预测器对未来工作的相关性达到了58.1%，并成功合成了覆盖61个仓库的200个任务数据集。该工作为实现低污染、高现实的智能体训练数据生成提供了新范式，意义重大。
