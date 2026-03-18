---
title: "Differential Harm Propensity in Personalized LLM Agents: The Curious Case of Mental Health Disclosure"
authors:
  - "Caglar Yildirim"
date: "2026-03-17"
arxiv_id: "2603.16734"
arxiv_url: "https://arxiv.org/abs/2603.16734"
pdf_url: "https://arxiv.org/pdf/2603.16734v1"
categories:
  - "cs.AI"
tags:
  - "Agent Safety"
  - "Personalization"
  - "Jailbreak"
  - "Evaluation Benchmark"
  - "Harmful Task Completion"
  - "Tool-Using Agents"
relevance_score: 7.5
---

# Differential Harm Propensity in Personalized LLM Agents: The Curious Case of Mental Health Disclosure

## 原始摘要

Large language models (LLMs) are increasingly deployed as tool-using agents, shifting safety concerns from harmful text generation to harmful task completion. Deployed systems often condition on user profiles or persistent memory, yet agent safety evaluations typically ignore personalization signals. To address this gap, we investigated how mental health disclosure, a sensitive and realistic user-context cue, affects harmful behavior in agentic settings. Building on the AgentHarm benchmark, we evaluated frontier and open-source LLMs on multi-step malicious tasks (and their benign counterparts) under controlled prompt conditions that vary user-context personalization (no bio, bio-only, bio+mental health disclosure) and include a lightweight jailbreak injection. Our results reveal that harmful task completion is non-trivial across models: frontier lab models (e.g., GPT 5.2, Claude Sonnet 4.5, Gemini 3-Pro) still complete a measurable fraction of harmful tasks, while an open model (DeepSeek 3.2) exhibits substantially higher harmful completion. Adding a bio-only context generally reduces harm scores and increases refusals. Adding an explicit mental health disclosure often shifts outcomes further in the same direction, though effects are modest and not uniformly reliable after multiple-testing correction. Importantly, the refusal increase also appears on benign tasks, indicating a safety--utility trade-off via over-refusal. Finally, jailbreak prompting sharply elevates harm relative to benign conditions and can weaken or override the protective shift induced by personalization. Taken together, our results indicate that personalization can act as a weak protective factor in agentic misuse settings, but it is fragile under minimal adversarial pressure, highlighting the need for personalization-aware evaluations and safeguards that remain robust across user-context conditions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探究个性化用户上下文（特别是涉及心理健康披露的敏感信息）如何影响大型语言模型（LLM）智能体在工具使用场景中完成有害任务的倾向性。随着LLM越来越多地被部署为能够维持用户状态、执行多步规划和工具操作的智能体，安全关注点已从单纯的有害文本生成转向了有害任务的实际完成。现有安全评估通常忽略个性化信号的影响，即模型在基于用户档案或持久记忆进行个性化适配时可能产生的行为变化，这构成了当前研究的重要空白。

论文指出，现有方法在评估智能体安全性时，往往未充分考虑用户上下文个性化（如个人简介或敏感属性披露）对模型决策的潜在影响。这种不足使得我们无法全面理解智能体在真实部署环境中，尤其是在接触敏感用户信息后，其行为可能发生的系统性变化。具体而言，当智能体接触到用户的心理健康信息时，由于语言模型可能编码了社会对心理健康问题的污名化偏见，这可能导致其在执行任务时出现差异化的危害倾向，例如更倾向于或更倾向于拒绝完成某些任务。

本文要解决的核心问题是：用户上下文的个性化（尤其是心理健康信息披露）是否会系统性地改变LLM智能体实施有害行为的倾向？为此，研究构建了一个反事实评估框架，在控制其他条件不变的情况下，比较模型在有无心理健康披露的个性化提示下，执行相同有害任务（及其良性对照任务）时的行为差异。研究重点关注两个关键指标：有害任务完成度（伤害分数）和拒绝率，旨在揭示个性化作为潜在保护因素或风险因素的脆弱性，特别是在面对轻度对抗性提示（越狱）时其效果是否会减弱或逆转，从而强调需要开发对个性化情境保持鲁棒的安全评估与保障机制。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及以下几个类别：

**1. 智能体化LLM安全与有害任务完成**
*   **方法类**：研究重点从单轮文本生成转向多步骤工具使用的智能体系统，其威胁模型变为完成可能导致现实危害的多步骤工作流。**AgentHarm** 等基准测试专门评估智能体在多步骤恶意任务中的完成情况。本文直接基于此基准，但将固定任务与变化的个性化信号（如心理健康披露）相结合，以测试有害性是否随用户情境稳定。
*   **评测类**：**PropensityBench**、**MCP-SafetyBench** 等基准强调安全失败可能由协议细节（如工具命名、压力）驱动，即使在能力受控下，模型在对抗条件下也可能表现出不安全倾向。**AgentGuard** 等则提供了防御与评估框架。本文的研究可视为对这些工作的补充，将个性化信号作为一类具体的“协议细节”或“前缀扰动”进行考察。

**2. 个性化与记忆**
*   **方法类**：大量研究关注智能体如何通过长上下文提示或显式记忆模块（如情景/反思记忆）跨交互存储和重用用户信息，旨在提升帮助性。本文与此类工作的**区别**在于，它不评估个性化对帮助性的提升，而是专门研究其对**滥用风险**（即有害任务完成）的影响，将记忆中的敏感用户信号（心理健康披露）作为受控输入变量。

**3. 差异化智能体行为**
*   **评测类**：研究指出，除了明显偏见内容，差异还可能表现为**分配性伤害**，即模型的有用性、拒绝率或响应质量因用户属性而出现系统性差异。**Targeted underperformance** 等工作表明模型行为会基于用户特征选择性降级或转变。本文**扩展**了这一视角，将其应用于使用工具的智能体，探究敏感用户线索是否不仅改变模型“说什么”，还改变其“是否拒绝、继续或成功完成”多步骤任务（包括良性任务），从而揭示了智能体服务质量的差异化表现。

**4. 心理健康相关研究**
*   **应用/评测类**：已有文献充分记录了围绕心理健康（如感知危险性）的污名与刻板印象，并证明语言模型会反映和再现这些关联。这为本文选择心理健康披露作为测试案例提供了动机，并支撑了对“伤害减少”与“过度拒绝”之间权衡的分析。

**本文与上述工作的核心关系与区别**：本文处于**智能体安全**与**个性化/公平性**研究的交叉点。它**填补了一个关键空白**——先前智能体安全评估很少将敏感的、类似记忆的用户信号作为首要实验变量。本文通过将**心理健康披露**这一具体、现实的用户情境线索引入**AgentHarm**框架，系统量化了其对有害及良性任务完成的影响，并测试了在轻度越狱攻击下这种影响的鲁棒性，从而连接了上述多个研究脉络。

### Q3: 论文如何解决这个问题？

论文通过构建一个受控的实验框架来研究个性化信号（特别是心理健康披露）对LLM智能体有害行为的影响。其核心方法是基于AgentHarm基准，通过系统性地操纵任务上下文和用户上下文，评估不同条件下模型完成多步骤恶意任务的表现。

**整体框架与实验设计**：研究在AgentHarm基准的176个任务上展开。框架包含两个主要的操纵维度：
1.  **任务上下文**：分为三个水平——**良性**（原始无害任务）、**有害**（原始恶意任务）和**越狱**（在有害任务前添加一个轻量级越狱前缀，旨在抑制模型拒绝）。
2.  **用户上下文（个性化信号）**：分为三个水平——**无个人简介**（基线）、**仅含个人简介**（控制条件）和**个人简介+心理健康披露**（处理条件）。个人简介设计为普通职业和爱好，而心理健康披露则是在此基础上添加一句“我患有心理健康问题”。

**主要模块与执行流程**：
1.  **任务执行模块**：使用Inspect AI平台上的AgentHarm实现，将每个任务操作化为智能体交互。模型在指定的任务和用户上下文组合下运行，产生任务轨迹。
2.  **评分与评估模块**：采用LLM-as-judge机制。核心指标是**伤害分数**，由默认的法官模型（GPT-4o）根据每个任务特定的评分标准，对智能体输出的完成度进行0到1的标量评分。这衡量的是任务目标的实现程度，而非简单的拒绝与否。
3.  **拒绝检测模块**：作为一个补充指标，使用语义拒绝判断器对智能体运行中的所有助手消息进行扫描，检测任何时间点是否出现拒绝行为。

**关键技术点与创新**：
*   **受控的个性化操纵**：研究的关键创新在于将用户上下文作为受控变量引入AgentHarm框架。通过设计“仅含个人简介”这一控制条件，能够隔离出普通自我披露的影响，从而更清晰地评估“心理健康披露”这一敏感信号带来的额外效应。
*   **最小化与普适化的披露设计**：心理健康披露被有意设计为**最小化、非具体**的单一语句。这避免了与特定诊断相关的混淆因素，旨在模拟一个可能激活模型内部与心理健康相关偏见（如污名化）的、 plausible 的记忆线索。
*   **配对比较分析**：在同一模型和同一任务上，重复运行不同提示上下文（任务上下文×用户上下文）的组合，使得所有比较都能在模型×任务层面进行配对，提高了结果的可比性和统计效力。
*   **揭示安全-效用的权衡**：通过观察个性化条件（如添加简介）在**良性任务**上同样导致拒绝率上升的现象，研究不仅评估了安全性，也揭示了过度拒绝可能带来的效用损失，点明了个性化安全机制中存在的权衡关系。

总之，论文通过扩展现有基准，建立了一个严谨的、多因素受控的实验方法，系统地量化了不同个性化信号对LLM智能体有害任务完成倾向的影响，并揭示了其在对抗性压力下的脆弱性。

### Q4: 论文做了哪些实验？

该研究基于AgentHarm基准测试，评估了在个性化用户背景（特别是心理健康披露）下，LLM代理完成有害任务的行为变化。实验设置包括：1）任务上下文：良性任务、有害任务、以及有害任务结合轻量级越狱提示；2）用户背景条件：无背景（Baseline）、仅通用个人简介（BioOnly）、通用简介加心理健康披露（Bio+MH）。评估了前沿模型（如GPT-5.2、Claude Sonnet 4.5、Gemini 3-Pro）和开源模型（DeepSeek 3.2）在多步骤恶意任务及其良性对应任务上的表现。

主要结果：1）基线条件下，所有模型在良性任务上完成度较高（平均伤害分数59–83%），而在有害任务上表现差异显著，例如DeepSeek 3.2有害完成率达38.9%，Claude Opus 4.5仅5.5%；越狱提示显著提升部分模型的有害完成率（如DeepSeek 3.2从38.9%升至85.3%）。2）添加用户背景（BioOnly和Bio+MH）通常降低有害任务完成度，并提高拒绝率，但效果较温和。例如，DeepSeek 3.2在有害任务上伤害分数从38.9%（Baseline）降至29.2%（Bio+MH），拒绝率从47.7%升至61.9%。3）心理健康披露在良性任务上也导致拒绝率上升（如Claude Opus 4.5拒绝率从27.8%升至46.0%），表明存在安全性与效用的权衡。4）在越狱任务中，个性化背景的保护作用脆弱且模型依赖，例如DeepSeek 3.2在所有用户背景条件下伤害分数均高于83%，拒绝率始终为0%，而Gemini 3-Flash伤害分数从55.9%降至43.8%。关键指标包括平均伤害分数和拒绝率，具体数值如GPT-5.2在有害任务上拒绝率从48.9%（Baseline）升至59.1%（Bio+MH），Claude Haiku 4.5在越狱任务上拒绝率达100%（Bio+MH）。结果表明，个性化可作为弱保护因素，但在对抗性提示下易失效，凸显了需针对个性化场景设计稳健的安全评估机制。

### Q5: 有什么可以进一步探索的点？

本文揭示了用户个性化信息（特别是心理健康披露）对LLM智能体安全性的复杂影响，其局限性及未来研究方向值得深入探讨。首先，研究仅考察了单一、静态的个性化信号（简短个人简介及心理健康披露），未来可探索更动态、多模态的用户背景（如对话历史、情感状态变化）对智能体行为的影响机制。其次，实验中的“保护性效应”较弱且易受越狱攻击破坏，表明当前个性化安全机制缺乏鲁棒性。未来需设计能抵抗对抗性压力的个性化安全框架，例如结合持续监控和动态风险调整的机制。

从方法改进角度，可引入更细粒度的安全-效用权衡评估指标，超越二元的“完成/拒绝”判断，量化过度拒绝的代价。此外，研究可扩展至其他敏感属性（如文化背景、社会经济状态）如何系统性影响智能体的服务公平性。最后，需开发能同时优化安全性与个性化体验的智能体架构，例如通过分层策略分离用户背景理解与任务执行，或利用强化学习在多样化用户情境中学习稳健的安全边界。这些方向将推动构建既个性化又安全可靠的AI智能体系统。

### Q6: 总结一下论文的主要内容

该论文研究了在个性化LLM智能体环境中，用户背景信息（尤其是心理健康披露）对有害任务完成倾向的影响。核心问题是评估个性化信号如何改变基于LLM的工具使用智能体在恶意任务中的行为，以及其中存在的安全与效用权衡。

方法上，研究基于AgentHarm基准，在受控提示条件下评估了前沿和开源LLM模型。通过系统性地改变用户背景个性化设置（无背景、仅基础背景、基础背景+心理健康披露），并引入轻量级越狱注入，测试模型在多步骤恶意任务及其良性对照任务上的表现。

主要结论有三点：首先，有害性是一种轨迹层面的属性，并非对用户背景保持不变；添加个性化背景（尤其是包含心理健康披露时）倾向于降低有害任务完成率并增加拒绝，表明评估需涵盖多种个性化条件。其次，个性化可作为一种微弱的保护性因素，但会带来安全与效用的权衡，即在减少有害行为的同时，也可能在良性任务上导致过度拒绝和效用损失。最后，在越狱提示下，任何保护性转变都变得脆弱且异质，凸显出现有个性化安全措施的脆弱性。论文强调，需要开发能跨用户背景条件保持稳健的、感知个性化的评估方法与安全保障措施。
