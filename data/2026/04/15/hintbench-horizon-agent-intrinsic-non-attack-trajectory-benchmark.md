---
title: "HINTBench: Horizon-agent Intrinsic Non-attack Trajectory Benchmark"
authors:
  - "Jiacheng Wang"
  - "Jinchang Hou"
  - "Fabian Wang"
  - "Ping Jian"
  - "Chenfu Bao"
  - "Zhonghou Lv"
date: "2026-04-15"
arxiv_id: "2604.13954"
arxiv_url: "https://arxiv.org/abs/2604.13954"
pdf_url: "https://arxiv.org/pdf/2604.13954v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "Agent Safety"
  - "Benchmark"
  - "Risk Assessment"
  - "Long-Horizon Trajectory"
  - "Intrinsic Risk"
  - "Evaluation"
relevance_score: 7.5
---

# HINTBench: Horizon-agent Intrinsic Non-attack Trajectory Benchmark

## 原始摘要

Existing agent-safety evaluation has focused mainly on externally induced risks. Yet agents may still enter unsafe trajectories under benign conditions. We study this complementary but underexplored setting through the lens of \emph{intrinsic} risk, where intrinsic failures remain latent, propagate across long-horizon execution, and eventually lead to high-consequence outcomes. To evaluate this setting, we introduce \emph{non-attack intrinsic risk auditing} and present \textbf{HINTBench}, a benchmark of 629 agent trajectories (523 risky, 106 safe; 33 steps on average) supporting three tasks: risk detection, risk-step localization, and intrinsic failure-type identification. Its annotations are organized under a unified five-constraint taxonomy. Experiments reveal a substantial capability gap: strong LLMs perform well on trajectory-level risk detection, but their performance drops to below 35 Strict-F1 on risk-step localization, while fine-grained failure diagnosis proves even harder. Existing guard models transfer poorly to this setting. These findings establish intrinsic risk auditing as an open challenge for agent safety.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决智能体在非对抗性、良性环境下因内部决策失误而引发安全风险的问题，即“内在风险”（intrinsic risk）。研究背景在于，随着大语言模型发展为能够多步推理、使用工具并与环境交互的智能体，安全研究的焦点已从静态输出安全转向动态执行过程中的风险。现有方法主要关注外部诱导的风险，如提示注入、恶意工具反馈或环境操纵，这些研究侧重于对抗性鲁棒性，但未能充分涵盖智能体在正常部署中可能出现的内部失误。现有轨迹级基准虽开始超越纯粹的攻击成功率评估，但仍未明确关注良性条件下的内在故障，尤其是当风险在早期产生并通过长时程执行传播时。

本文的核心问题是：在无外部攻击、工具污染或环境操纵的良性条件下，智能体是否可能因内在故障（如目标偏离、事实错误、能力不足、程序违规或状态误判）进入不安全的执行轨迹，并导致不可逆的高后果风险（如隐私泄露）。为此，论文提出了“非攻击内在风险审计”这一新评估范式，并构建了HINTBench基准，以支持风险检测、风险步骤定位和故障类型识别等细粒度任务，从而弥补现有方法在内在风险评估上的不足。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：在线攻击评估和事后轨迹审计。

在**在线攻击评估**方面，已有大量工作关注外部诱导风险下的智能体安全性。例如，AgentDojo构建了可扩展的提示注入基准，强调动态环境中的自适应攻击与防御；AgentHarm专注于有害用户请求，评估越狱智能体执行恶意多步任务的能力；ASB系统化评估了多种场景、工具和攻击类型（如提示注入、内存投毒）；Agent-SafetyBench则进一步扩展了风险类型和交互设置。在网络环境中，SafeArena研究自主网络智能体的故意滥用，WASP强调受限攻击者下的现实端到端提示注入，AgentDyn推动评估面向涉及不可信第三方指令的动态开放任务。这些工作主要关注**外部攻击**下的安全性，而本文则研究**良性条件下由内在故障引发的风险**，两者形成互补。

在**事后轨迹审计**方面，研究侧重于对已完成执行轨迹的后验安全分析。R-Judge通过带安全标签和结构化风险描述的多轮交互记录评估风险意识；ASSEBench（与AgentAuditor一同提出）进一步区分安全与安保，并采用模糊感知的标注协议；ATBench引入了更细粒度的诊断维度（如风险来源、故障模式）；TS-Bench支持工具使用的步骤级安全评估。这些工作提升了可解释性和诊断粒度，但其焦点仍是广泛的轨迹安全审计，**未明确将良性条件下内在故障导致的不安全轨迹作为一个独特问题建模**，且大多停留在轨迹级风险判断，缺乏对风险步骤定位和故障类型识别的联合处理。本文则系统化地提出了非攻击性内在风险审计，并设立了风险检测、风险步骤定位和内在故障类型识别三项具体任务，推动了该方向的发展。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为HINTBench的基准测试来解决智能体在良性条件下内在风险（intrinsic risk）的评估问题。其核心方法是提出并实施“非攻击性内在风险审计”，系统性地评估长视野（long-horizon）智能体执行过程中对一系列基本约束的满足情况，从而揭示和诊断那些并非由外部攻击诱发、而是源于智能体自身执行过程的潜在风险。

**整体框架与主要模块**：
1.  **理论基础与分类法**：首先，论文提出了一个基于约束的五维分类法作为方法论的核心。该分类法认为，智能体的正确执行必须持续满足五个基本约束：目标约束（Goal）、事实约束（Factual）、能力约束（Capability）、过程约束（Procedural）和状态约束（State）。风险被定义为对这些约束的系统性偏离。这为风险的定义、识别和分类提供了统一且具有理论一致性的框架。
2.  **基准构建流水线**：HINTBench的构建遵循一个结构化的三阶段流程：
    *   **环境种子策划**：手动创建了30个涵盖高风险、多步骤任务场景（如银行、旅行预订）的环境种子。每个种子包含环境描述、核心组件（实体、状态变量）以及明确定义的工具接口和能力边界，为生成高保真度的交互轨迹奠定了基础。
    *   **结构化轨迹合成与质量过滤**：采用“骨架优先”的两阶段生成策略，而非端到端生成。首先，模型基于选定的工具生成用户任务，并创建一个**交互骨架**，明确指定目标分解、工具调用顺序、环境响应和状态演进关系等高层执行结构。然后，模型扮演不同角色，逐步填充自然语言对话内容，形成完整轨迹。这种方法将执行结构与语言实现部分解耦，提高了长轨迹生成的稳定性和可控性。
    *   **人工验证**：所有生成的轨迹（包括正常轨迹和风险轨迹）均由三名标注者独立验证。对于风险轨迹，不仅验证指定步骤的风险是否发生，还检查是否存在额外的共现违规。通过多数同意确定最终标签，确保基准样本及其风险标注的准确性、一致性和高质量。

**关键技术细节与创新点**：
*   **风险注入机制**：风险轨迹并非随机插入错误，而是从已验证的正常轨迹出发，**系统性地向正常骨架中注入风险**。基于五大约束，引入有针对性的扰动，生成对应特定失效模式的风险骨架，再扩展为完整风险轨迹。这确保了风险轨迹能更真实地反映风险在多步执行中如何产生和传播。
*   **支持多粒度评估任务**：HINTBench的标注格式（轨迹级风险标签 `y` 和带类型的风险元组集合 `R_τ` ）天然支持三项评估任务：**轨迹级风险检测**、**风险步骤定位**和**内在失效类型识别**，实现了从粗粒度到细粒度的全面审计。
*   **覆盖广泛的复杂场景**：最终构建的基准包含629条轨迹（平均33步），其中523条为风险轨迹，衍生自106条正常轨迹。风险步骤总计1418个，覆盖了五大约束下的多种失效模式，其中过程约束违规占比最大。与现有基准相比，HINTBench的平均轨迹长度显著更长，更能捕捉长视野交互中多步推理、重复工具使用和跨阶段依赖的复杂性。

综上所述，论文通过提出一个理论驱动的约束分类法，并设计一套包含“骨架优先”合成、系统性风险注入和严格人工验证的基准构建方法论，系统性地解决了对智能体内在非攻击性风险进行审计和评估的挑战。

### Q4: 论文做了哪些实验？

论文在HINTBench基准上进行了系统性的实验评估。实验设置主要包括对通用大语言模型（LLMs）和专用防护模型（guard models）的评测，覆盖三个逐步深入的审计任务：轨迹级风险检测、粗粒度风险步骤定位和细粒度风险步骤定位。此外，还构建了基于轨迹前缀的实时风险监控评估。

**数据集/基准测试**：使用论文提出的HINTBench，包含629条智能体轨迹（523条有风险，106条安全），平均长度33步，并标注了统一的五大约束分类体系。

**对比方法**：
1.  **通用LLMs**：包括GPT-4o、Claude-Sonnet-3.5、Kimi-K2.5、MiniMax-M2.5、GLM-5、ERNIE-5、DeepSeek系列、Qwen3系列（从4B到235B）、Llama系列和Mistral-7B等。
2.  **专用防护模型**：包括LlamaGuard3-8B、PolyGuard、Qwen3Guard8B、ShieldGemma-9B、ShieldAgent、AgentDoG（基于Qwen和Llama）等。

**主要结果与关键指标**：
1.  **风险检测**：强模型表现良好。例如Kimi-K2.5的Avg-F1达96.93，准确率98.33%。但防护模型普遍弱于顶级通用LLMs，且存在预测偏差（如AgentDoG模型Safe-F1极低）。
2.  **风险步骤定位**：模型性能显著下降，凸显任务难度。在粗粒度定位上，最佳模型Kimi-K2.5的Strict-F1仅为33.32；在细粒度定位上，其Strict-F1进一步降至21.08。多数模型在此任务上的Strict-F1低于35。
3.  **实时监控评估**：基于前缀的评估显示，性能较完整轨迹检测有明显下降，表明实时风险识别更具挑战性。例如ERNIE-5的Avg-F1下降了近20点。
4.  **模型能力依赖性**：较小模型（如Llama3.2-3B）在所有任务上表现均不佳，表明可靠的审计需要足够的长上下文理解和多步推理能力。性能提升并非严格随参数规模单调增长。

实验核心结论是，现有模型在风险检测上相对较好，但在风险步骤定位和细粒度诊断上存在巨大能力差距，且现有防护模型难以迁移到本论文研究的非攻击性内在风险审计场景。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要在于其基准数据集的合成性质，以及标注过程本身的不确定性。合成轨迹可能无法完全覆盖现实部署中复杂、长尾的故障模式，这限制了基准的泛化能力和对真实风险的评估效果。同时，对于推理步骤高度纠缠的轨迹，准确标注“最早风险步骤”存在挑战，这会影响风险定位任务的精确评估。

基于此，未来研究可以从以下几个方向深入探索：
1.  **数据与评估真实性**：构建基于真实人机交互或复杂模拟环境（如视频游戏、机器人任务）的轨迹数据集，以更好地捕捉现实世界中的内在风险模式和长尾故障。
2.  **风险传播与归因的细粒度分析**：开发更强大的方法，以解构和追踪风险在长视野任务中的传播链条。这需要超越简单的步骤定位，实现对风险如何通过多步推理和行动逐步演化为严重后果的归因分析。
3.  **提升诊断与干预能力**：当前模型在细粒度故障诊断上表现不佳。未来工作可以探索结合程序推理、因果发现或可解释AI技术，不仅识别风险步骤，还能精确诊断根本原因（如知识缺陷、规划谬误、价值观冲突），并为动态风险干预提供依据。
4.  **防御机制与鲁棒性训练**：针对已识别的内在风险模式，设计专门的“安全层”或训练范式（如对抗性训练、安全约束强化学习），增强智能体在长序列决策中的内在鲁棒性，防止小错误累积成重大失败。

### Q6: 总结一下论文的主要内容

该论文针对现有智能体安全评估主要关注外部诱导风险的问题，提出了对智能体在良性条件下仍可能进入不安全轨迹的“内在风险”进行研究。论文的核心贡献是引入了“非攻击性内在风险审计”概念，并构建了HINTBench基准测试集。该基准包含629条智能体轨迹（平均33步），支持风险检测、风险步骤定位和内在故障类型识别三项任务，其标注基于统一的五约束分类法。实验表明，现有大型语言模型在轨迹级风险检测上表现良好，但在风险步骤定位任务上的严格F1分数低于35%，细粒度故障诊断则更为困难，且现有防护模型在此场景下迁移效果不佳。这些发现确立了内在风险审计是智能体安全领域一个亟待解决的开放挑战，HINTBench为开发更安全可靠的智能体提供了现实的轨迹、结构化标注和多样化的评估场景。
