---
title: "The Autonomy Tax: Defense Training Breaks LLM Agents"
authors:
  - "Shawn Li"
  - "Yue Zhao"
date: "2026-03-19"
arxiv_id: "2603.19423"
arxiv_url: "https://arxiv.org/abs/2603.19423"
pdf_url: "https://arxiv.org/pdf/2603.19423v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent Security"
  - "Tool Use"
  - "Adversarial Robustness"
  - "Defense Training"
  - "Capability Degradation"
  - "Multi-step Tasks"
  - "Evaluation"
relevance_score: 7.5
---

# The Autonomy Tax: Defense Training Breaks LLM Agents

## 原始摘要

Large language model (LLM) agents increasingly rely on external tools (file operations, API calls, database transactions) to autonomously complete complex multi-step tasks. Practitioners deploy defense-trained models to protect against prompt injection attacks that manipulate agent behavior through malicious observations or retrieved content. We reveal a fundamental \textbf{capability-alignment paradox}: defense training designed to improve safety systematically destroys agent competence while failing to prevent sophisticated attacks. Evaluating defended models against undefended baselines across 97 agent tasks and 1,000 adversarial prompts, we uncover three systematic biases unique to multi-step agents. \textbf{Agent incompetence bias} manifests as immediate tool execution breakdown, with models refusing or generating invalid actions on benign tasks before observing any external content. \textbf{Cascade amplification bias} causes early failures to propagate through retry loops, pushing defended models to timeout on 99\% of tasks compared to 13\% for baselines. \textbf{Trigger bias} leads to paradoxical security degradation where defended models perform worse than undefended baselines while straightforward attacks bypass defenses at high rates. Root cause analysis reveals these biases stem from shortcut learning: models overfit to surface attack patterns rather than semantic threat understanding, evidenced by extreme variance in defense effectiveness across attack categories. Our findings demonstrate that current defense paradigms optimize for single-turn refusal benchmarks while rendering multi-step agents fundamentally unreliable, necessitating new approaches that preserve tool execution competence under adversarial conditions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在揭示并解决当前大语言模型（LLM）智能体安全防御训练中存在的“能力-安全对齐悖论”问题。研究背景是，随着LLM被广泛部署为能够使用外部工具、执行多步骤复杂任务的自主智能体，其面临通过工具输出或检索内容进行“提示注入”攻击的风险。为此，业界普遍采用防御训练（如基于良性-攻击样本对的微调）来提升模型安全性，并在单轮问答基准测试中取得了高攻击拒绝率和低误拒率。

然而，现有方法存在严重不足。论文指出，当前的安全防御范式及其评估标准主要针对单轮交互场景进行优化，完全忽视了多步骤智能体特有的、动态的失败模式。这种脱节导致了一个核心矛盾：旨在提升安全性的防御训练，反而会系统性地破坏智能体执行多步骤任务的基本能力，且未能有效抵御复杂的攻击。

本文要解决的核心问题，正是这种在智能体场景下被掩盖的“自主性税负”。具体而言，论文系统性地识别并分析了三种仅存在于多步骤智能体中的系统性偏差：1) **智能体无能偏差**：防御模型甚至在接收到任何可能有害的外部观察内容之前（即任务第一步），就在大量良性任务上拒绝执行或生成无效动作，导致智能体“出师未捷”。2) **级联放大偏差**：早期的单一失败会在智能体的重试循环中被不断放大，最终导致任务超时，使得防御模型的任务完成率极低。3) **触发偏差**：防御模型依赖于对表面攻击模式（如关键词）的“捷径学习”，而非真正的语义威胁理解。这导致其一方面容易被精心设计的攻击所绕过，另一方面又对良性内容产生过度拒绝，造成安全性事实上的退化。论文的根本目标是揭示现有防御范式与智能体实际部署需求之间的根本性错配，论证当前方法会使得多步骤智能体变得根本不可靠，从而呼吁需要全新的、能够在对抗条件下保持工具执行能力的安全方法。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：提示注入与防御、捷径学习以及智能体评测。

在**提示注入与防御**方面，已有研究关注如何通过对抗性指令操控LLM行为，并提出了结构化查询、偏好对齐、指令层级和宪法AI等防御方法。然而，现有评测基准多采用单轮指标，未能捕捉多步任务中的级联动态。本文揭示了当前防御范式在优化单轮拒绝基准的同时，却导致多步智能体基本不可靠，这与之前工作形成鲜明对比。

在**捷径学习**方面，先前研究表明模型会利用虚假相关性而非鲁棒策略，例如位置偏差、词汇捷径和格式敏感性。近期研究在单轮场景中识别了防御相关的捷径。本文将此研究延伸至多步智能体，首次揭示了智能体无能偏差和级联放大偏差这两种系统性偏差。

在**智能体评测**方面，已有如AgentDojo、AgentBench和ToolBench等基准用于评估多步执行能力。但先前工作主要衡量每轮的拒绝情况，忽略了端到端的失败。本文通过深度分层分析，揭示了单次拒绝如何终止整个任务轨迹的级联动态，从而弥补了现有评测的不足。

### Q3: 论文如何解决这个问题？

论文通过构建一个诊断性的评估框架来揭示和量化防御训练带来的系统性偏差，并提出其根本原因在于“捷径学习”。其核心方法是设计两个受控的诊断实验，分别隔离并测量三种特定的偏差：智能体无能偏差、级联放大偏差和触发偏差。

整体框架基于AgentDojo基准测试平台，包含97个跨领域的真实智能体任务。关键技术在于精心设计的数据集构造和变量控制。对于智能体无能偏差和级联失败，论文通过分析任务第一步（在观察到任何外部内容之前）的执行行为来隔离能力退化。具体做法是，在工具观察结果中以固定概率注入攻击性触发短语，但关键测量点是在第一步，从而区分是模型自身格式/能力失败，还是由观察触发的拒绝。通过按任务完成深度进行分层统计完成率，可以识别级联动态（例如在深度10处完成率骤降）与渐进性退化。

对于触发偏差和安全-效用权衡，论文构建了一个包含350个样本的挑战性评估集，涵盖三种攻击类别（社会工程、混淆、指令覆盖）和包含安全术语的良性样本。该框架通过测量三种互补的失败模式来全面刻画捷径学习的影响：类型1（防御模型反而完成攻击）、类型2（攻击在不同防御方法间通用）和类型3（防御模型错误拒绝良性内容）。这直接量化了真阳性率和假阳性率，揭示了安全与效用的倒置权衡。

主要创新点在于：1）形式化并实证验证了专属于多步智能体的三种系统性偏差，超越了单轮评估的局限；2）设计了能够隔离混淆变量、精确追溯失败根源的诊断数据集和方法；3）通过收敛证据（如时间隔离、跨防御模式、类别特异性漏洞）论证了根本原因是模型对表面攻击模式的过拟合（捷径学习），而非真正的语义威胁理解。论文并未提出新的防御方法，而是通过这一诊断框架深刻揭示了当前防御范式在追求单轮拒绝基准性能时，会损害多步工具执行能力这一根本矛盾。

### Q4: 论文做了哪些实验？

论文实验围绕“防御训练损害LLM智能体能力”这一核心问题展开。实验设置方面，评估了三个基础模型（Llama-3-8B、Llama-3.1-8B、Mistral-7B）和四种防御配置：Base（无安全训练）、StruQ（基于XML分隔符）、SecAlign（DPO偏好对齐）以及Meta SecAlign（Meta官方DPO训练防御）。使用贪婪解码以确保可复现性。

数据集包括两个诊断基准：1) AgentDojo：包含4个领域共97个多步骤任务，用于测试智能体无能性和级联放大效应；2) 挑战性子集：包含350个精选样本（289个对抗性，61个良性），通过复杂攻击和技术文档测试触发偏见。

关键指标包括完成率（CR）、级联失败率（CFR）、深度分层CR、真阳性率（TPR）、假阳性率（FPR）以及特定类别的绕过率。主要结果如下：防御训练显著损害了智能体在良性任务上的基本能力。例如，在第一步有效动作率上，基础模型达到96.9–97.9%，而防御模型骤降至22.7–53.6%。在整体任务完成率上，防御训练将完成率从基础模型的50.5–86.6%降低到1.0–80.4%，其中SecAlign-Mistral仅完成1.0%的任务，表现出灾难性崩溃。

安全性能方面，基础模型攻击检测率（TPR）为82.7%，而防御训练后降至26.7–37.4%（下降45-56个百分点），同时假阳性率（FPR）从0%激增至24.6–70.5%。此外，攻击绕过率在不同类别间差异显著，例如对于混淆类攻击，绕过率高达81–86%。级联放大效应明显，SecAlign将级联失败率从基础模型的13–50%提升至36–99%，放大因子达2.0–2.7倍。这些结果表明，当前的防御范式过度拟合了表面攻击模式，破坏了多步骤智能体的基本工具执行能力，且在对抗条件下无法提供可靠安全。

### Q5: 有什么可以进一步探索的点？

该论文揭示了当前防御训练方法在LLM智能体场景下的根本性局限，即“能力对齐悖论”。基于此，可进一步探索的方向包括：

1.  **防御范式的根本性转变**：论文指出现有方法基于“捷径学习”，模型仅拟合了表面攻击模式。未来的研究应探索基于语义理解的防御机制，例如，开发能动态分析任务上下文、工具调用意图与外部内容语义一致性的框架，而非依赖静态规则或模式匹配。

2.  **针对多步长任务的鲁棒性评估与训练**：当前防御优化主要针对单轮拒绝基准，这严重脱离了智能体的实际工作模式。亟需建立专门针对多步长、工具调用场景的对抗性评估基准，并设计相应的训练目标（如“在对抗条件下保持工具执行能力”），以缓解“级联放大偏差”和“智能体无能偏差”。

3.  **防御的精细化和条件化**：论文发现防御效果在不同攻击类别间方差极大。这表明“一刀切”的防御可能有害。未来的工作可以探索**条件化安全策略**，使模型能根据任务类型、工具敏感度、用户权限等信息，动态调整其防御的严格程度，在安全性与可用性之间取得更好平衡。

4.  **架构与训练方法的创新**：可以探索将工具使用能力与安全审查机制在架构上进行一定程度的解耦，例如采用“双系统”设计（一个负责规划与执行，一个负责实时安全监控），或通过强化学习直接优化在对抗环境下的长期任务完成成功率。

### Q6: 总结一下论文的主要内容

该论文揭示了大型语言模型（LLM）智能体在部署防御训练时面临的核心矛盾：旨在提升安全性的防御训练会系统性损害智能体的任务执行能力，且无法有效抵御复杂攻击。研究通过评估97项智能体任务和1000个对抗性提示，发现三个独特于多步智能体的系统性偏差：1）**智能体无能偏差**，表现为模型在未观察任何外部内容前就拒绝或生成无效操作，导致基础工具执行崩溃；2）**级联放大偏差**，早期失败通过重试循环传播，使防御模型在99%的任务上超时，而基线模型仅为13%；3）**触发偏差**，导致防御模型性能反而不如未防御基线，同时简单攻击仍能高频绕过防御。根本原因在于模型进行了捷径学习，过度拟合表面攻击模式而非理解语义威胁，导致防御效果在不同攻击类别间差异极大。论文结论指出，当前防御范式仅优化单轮拒绝基准，却使多步智能体变得根本不可靠，因此亟需开发能在对抗条件下保持工具执行能力的新方法。
