---
title: "Beyond Binary Correctness: Scaling Evaluation of Long-Horizon Agents on Subjective Enterprise Tasks"
authors:
  - "Abhishek Chandwani"
  - "Ishan Gupta"
date: "2026-03-24"
arxiv_id: "2603.22744"
arxiv_url: "https://arxiv.org/abs/2603.22744"
pdf_url: "https://arxiv.org/pdf/2603.22744v1"
categories:
  - "cs.AI"
tags:
  - "Agent Evaluation"
  - "Long-Horizon Tasks"
  - "Subjective Tasks"
  - "Evaluation Benchmark"
  - "LLM-as-a-Judge"
  - "Tool Use"
  - "Enterprise Agent"
relevance_score: 7.5
---

# Beyond Binary Correctness: Scaling Evaluation of Long-Horizon Agents on Subjective Enterprise Tasks

## 原始摘要

Large language models excel on objectively verifiable tasks such as math and programming, where evaluation reduces to unit tests or a single correct answer. In contrast, real-world enterprise work is often subjective and context-dependent: success hinges on organizational goals, user intent, and the quality of intermediate artifacts produced across long, multi-tool workflows.
  We introduce LH-Bench, a three-pillar evaluation design that moves beyond binary correctness to score autonomous, long-horizon execution on subjective enterprise tasks. The pillars are: (i) expert-grounded rubrics that give LLM judges the domain context needed to score subjective work, (ii) curated ground-truth artifacts that enable stepwise reward signals (e.g., chapter-level annotation for content tasks), and (iii) pairwise human preference evaluation for convergent validation. We show that domain-authored rubrics provide substantially more reliable evaluation signals than LLM-authored rubrics (kappa = 0.60 vs. 0.46), and that human preference judgments confirm the same top-tier separation (p < 0.05), evidence that expert-grounded evaluation can scale without sacrificing reliability. We release public datasets and report results on two environments: Figma-to-code (33 real .fig tasks against the Figma API via MCP) and Programmatic content (41 courses comprising 183 individually-evaluated chapters on a course platform serving 30+ daily users).

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大语言模型（LLM）智能体在复杂、现实的企业任务评估上面临的核心挑战。研究背景是，尽管LLM在数学、编程等有明确正确答案的客观任务上表现出色，但企业实际工作往往是主观的、依赖于具体情境的，涉及长期、多步骤、多工具的工作流，其成功标准取决于组织目标、用户意图和中间产物的质量。现有评估方法（如单元测试）主要依赖“二元正确性”（通过/失败），这无法捕捉主观任务的质量维度，也无法诊断智能体在长流程中失败的具体环节和原因，导致评估信号不足且不可靠。

现有方法的不足主要体现在三个方面：一是无法处理长视野执行中跨数十个相互依赖步骤的状态追踪；二是无法对主观任务质量进行有效评分，因为其不能简化为单一正确答案；三是忽略了多产物工作流中中间输出的质量对下游成功的关键影响。二元正确性评估将这些复杂维度压缩为一个简单结果，存在严重局限性。

因此，本文要解决的核心问题是：如何为自主智能体在主观性、长视野的企业任务上的表现，设计并验证一套可扩展、可靠且超越二元正确性的评估框架。为此，论文提出了名为LH-Bench的三支柱评估设计方案，通过结合专家制定的评分标准、精心策划的中间产物真值以及成对人类偏好评估，旨在为这类复杂任务提供细致、逐步的评估信号，从而更准确地衡量智能体的实际性能并推动其可靠性提升。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 智能体基准与环境：** 现有基准如 WebArena、OSWorld、SWE-bench、AgentBench、GAIA 以及专注于企业领域的 WorkArena，主要评估智能体在交互环境中的表现，但大多采用二元成功指标（通过/失败）来衡量单轮或短视距任务。SWE-Bench Pro 扩展到长视距软件工程任务，但仍依赖单元测试评分。本文的 LH-Bench 与之区别在于，专注于需要迭代工件编辑的主观性专业知识工作，采用多层评估而非二元判断，并将任务根植于真实的企业工件。

**2. UI生成与设计转代码：** 相关工作如 Design2Code、FronTalk、FullFront 和 FrontendBench，主要基于网页截图进行前端代码生成评估。LH-Bench 的扩展在于直接使用真实的 Figma 设计文件作为输入，要求智能体通过设计工具 API 进行结构提取、资源导出和令牌发现等一系列操作后才开始编码，并需在多个验证周期中迭代而不破坏先前工作。

**3. 工具使用与多轮交互：** MINT 评估带语言反馈的多轮工具使用，ToolLLM 扩展到大量真实 API。LH-Bench 的重点是长会话中的多工具编排，智能体需在数十轮中协调设计提取、代码生成、构建、预览和部署等多种工具，并利用结构化验证反馈实现测试时恢复。

**4. 长视距智能体评估：** 研究如 UltraHorizon 和 τ²-bench 关注长轨迹评估和错误类型分析，Turn-level reward design 指出稀疏的最终奖励在长周期中不足。LH-Bench 的贡献在于提供企业特定的长视距评估，采用基于技能水平的评分，提供与专家定义工作流程阶段对齐的密集、诊断性信号。

**5. 基于LLM的评估与评判：** 以 Zheng 等人的工作为基础的“LLM即法官”范式已被广泛研究。LH-Bench 在此基础上，采用来自不同模型家族的三个 LLM 法官，结合专家撰写的评分细则和跨法官方差跟踪，应用于多维企业工件评估。

**6. 基于评分细则与技能的评估：** ResearchRubrics、DeepResearch Bench II 和 SkillsBench 等研究表明评分细则的粒度影响排名可靠性，技能分解能揭示聚合分数中不可见的故障模式。LH-Bench 融合了这两条思路，利用领域专家撰写的细则和技能分解，为长视距企业任务生成密集的诊断信号。

**7. 企业AI与复合系统：** 当前研究趋势转向复合AI系统的系统级评估。LH-Bench 通过在企业任务上对完整智能体工具链进行基准测试来填补这一空白，其评估信号旨在诊断上下文管理、工具编排和恢复等方面的系统级差异。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为LH-Bench的三支柱评估框架来解决主观性企业任务中长视野智能体评估的难题。其核心方法超越了简单的二元正确性判断，采用了一套综合的、可扩展的评估体系。

**整体框架与主要模块：**
LH-Bench评估的是端到端的智能体“驾驭器”（harness），而非孤立的基座模型。其设计遵循当前主流的智能体-CLI架构模式（如Claude Code、Codex CLI、Gemini CLI），在沙盒化shell环境中运行，支持文件系统工具和可扩展的工具接口（如MCP服务器）。这使得特定环境的能力（如Figma提取、预览验证）可以一次定义，跨不同驾驭器家族一致运行，从而能够纯粹比较不同驾驭器在任务编排和推理能力上的差异。

关键模块包括：
1.  **自主执行的智能体驾驭器**：智能体在沙盒中执行，通过程序化调用工具与环境交互（如设计提取、浏览器自动化），并利用运行时反馈（而非人工干预）从失败中恢复。这确保了评估的自动化和可复现性。
2.  **上下文压缩机制**：针对长视野任务常超出上下文限制的问题，驾驭器实现了自动压缩策略，能总结先前的步骤、工具输出和中间产物，同时保留承诺、待办事项和已验证事实。此外，还采用了主动预压缩，在昂贵的工具调用或重大编辑前，生成当前状态的紧凑“工作集”视图。
3.  **一体化验证接口**：将验证作为一等公民。构建/部署失败、评分标准违规、视觉不匹配等问题会被转化为结构化的、机器可读的反馈，供智能体用于规划修复。例如，在Figma转代码任务中，提供了一个预览验证钩子，在智能体调用预览工具后自动运行检查并返回结构化错误（如路由嵌套错误、空白页渲染），指导智能体进行迭代自我纠正。

**创新点与关键技术：**
LH-Bench的三大支柱构成了其方法论的核心创新：
1.  **专家锚定的评分标准**：由领域专家（如资深前端工程师、教学设计专家）撰写评分标准，为LLM评委提供评估主观工作所需的领域上下文。论文证明，专家撰写的评分标准比LLM生成的更可靠（Cohen's kappa系数0.60 vs. 0.46）。
2.  **精心策划的真实工件**：构建包含中间产物（如逐章标注）的真实数据集，提供逐步的奖励信号。例如，在程序化内容环境中，通过专用的标注界面实现细粒度的“高亮引用”交互，将证据精确关联到每个章节，产生高质量、可追溯的引用。
3.  **成对人类偏好评估**：用于收敛验证，确保自动评估结果与人类判断一致。实验表明，人类偏好判断确认了与专家评分标准相同的顶级智能体区分度（p < 0.05），证明了专家锚定评估在扩展规模的同时未牺牲可靠性。

**评估框架**：采用混合评估方法，结合专家评分标准、轨迹评分和工件的程序化验证（包括视觉输出）。评分分为多个层级（如产出层、技能层、行为层），每个维度按1-5分制评分。评估时并行运行三类评委：任务无关的轨迹评委、任务特定的过程评委和产出评委，它们分别消耗不同的输入（如任务记录、工具轨迹、真实截图），输出结构化的JSON评分，既支持排行榜排名，也支持细粒度诊断。

### Q4: 论文做了哪些实验？

论文在两个主观企业任务环境中进行了实验：Figma-to-code（33个真实任务）和Programmatic content（41门课程，共183个独立评估章节）。实验设置上，评估了三个智能体框架家族（Claude Code、Codex CLI、Gemini CLI）的七种配置，每个配置在沙盒环境中自主执行，使用专家编写的SKILL.md定义工具访问和工作流约束。对比方法包括使用和不使用SKILL.md的受控消融实验，以及专家编写与LLM编写评估量规的对比。

主要数据集/基准测试包括：Figma-to-code使用33个真实.fig文件任务通过MCP调用Figma API；Programmatic content使用一个拥有30+日活用户的课程平台上的41门课程。评估采用LH-Bench三支柱设计：专家接地的量规、分步真实工件和成对人类偏好验证。

关键结果与指标：
1.  **Figma-to-code输出分数（VLM评估，1-5分）**：Codex (GPT-5.2 Pro) 最高（4.27），Claude Code (Opus 4.6) 为4.19±0.28，Gemini CLI (Gemini 3.1 Pro) 为3.73±0.44。
2.  **Figma-to-code技能分数（3个LLM评估员，1-5分）**：Claude Code (Opus 4.6) 最高（3.27±0.14），Codex (GPT-5.2) 为3.16±0.15，Gemini CLI (3.1 Pro) 为2.80±0.11。技能分解显示，设计令牌和样式提取是普遍瓶颈（分数最低），而组件和布局架构是强项。
3.  **Programmatic content VLM工件分数（标准化0-1）**：Claude Code (Opus 4.6) 最高（0.612±0.069），Gemini CLI (3.1 Pro) 为0.526±0.063，Codex (GPT-5.2) 为0.478±0.044。5分量规比3分量规置信区间更窄（如Codex从±0.071降至±0.044），减少了49%的VLM平局。
4.  **评估员一致性**：使用专家编写量规时，平均Cohen's kappa为0.60（中等至高度一致），显著高于LLM编写量规的0.46。
5.  **SKILL.md消融实验**：专家工作流指导总体上提升技能分数（+0.33），其中Codex受益最大（整体+0.87，构建验证从1.00提升至2.67）。无SKILL.md时，仅2/7次运行产生可部署工件，而有SKILL.md时几乎全部成功。
6.  **任务难度梯度**：16%任务对所有智能体都简单（100%通过率），13%都困难（0%通过率），71%具有区分性（至少一个智能体通过，一个失败）。在区分性任务中，各智能体通过率在52.4%至57.9%之间。
7.  **人类偏好验证**：275组成对比较证实了VLM评估的排名分离具有统计显著性（p < 0.05），支持了评估的收敛效度。

### Q5: 有什么可以进一步探索的点？

该论文在主观性长程任务评估上迈出了重要一步，但其探索仍存在局限。首先，LH-Bench的评估范围有限，仅聚焦于设计和内容创作两类任务，未来需扩展至更广泛的商业场景，如战略分析、客户服务或复杂项目管理，以验证其通用性。其次，当前方法高度依赖领域专家构建评估量规，这在大规模应用中可能成为瓶颈；未来可探索如何利用少量专家样本，通过LLM微调或强化学习来自动生成或优化量规，提升可扩展性。此外，评估信号虽引入了分步奖励，但对智能体在长程工作流中动态决策、错误恢复及与人类协作能力的评估仍较薄弱。结合多智能体竞争或模拟环境进行压力测试，可能揭示更深层的性能边界。最后，论文未充分探讨评估结果如何反馈并优化智能体本身，未来可将评估体系与智能体的在线学习机制结合，形成闭环，推动自主智能体在复杂企业任务中持续进化。

### Q6: 总结一下论文的主要内容

该论文针对当前大语言模型在客观可验证任务（如数学、编程）上评估方法成熟，但在主观性、上下文依赖的真实企业任务中评估不足的问题，提出了LH-Bench评估框架。其核心贡献是设计了一个超越二元正确性的三支柱评估体系，用于对自主长程智能体在主观企业任务中的表现进行评分。具体方法包括：（1）使用专家制定的评估准则，为LLM评判员提供评分所需领域背景；（2）构建带注释的真实中间产物作为逐步奖励信号；（3）采用成对人类偏好评估进行收敛验证。主要结论表明，专家制定的准则比LLM生成的准则可靠性显著更高（kappa系数0.60对0.46），且人类偏好判断验证了相同的顶级模型区分度（p<0.05），这证明基于专家的评估可以在不牺牲可靠性的前提下实现规模化。论文通过在Figma-to-code和程序化内容生成两个实际环境中的实验验证了该框架的有效性。
