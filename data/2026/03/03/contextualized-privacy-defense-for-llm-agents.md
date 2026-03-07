---
title: "Contextualized Privacy Defense for LLM Agents"
authors:
  - "Yule Wen"
  - "Yanzhe Zhang"
  - "Jianxun Lian"
  - "Xiaoyuan Yi"
  - "Xing Xie"
date: "2026-03-03"
arxiv_id: "2603.02983"
arxiv_url: "https://arxiv.org/abs/2603.02983"
pdf_url: "https://arxiv.org/pdf/2603.02983v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Safety & Alignment"
  - "Human-Agent Interaction"
relevance_score: 7.5
taxonomy:
  capability:
    - "Safety & Alignment"
    - "Human-Agent Interaction"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "Qwen3-4B, Qwen3-32B, gpt-4.1-mini"
  key_technique: "Contextualized Defense Instructing (CDI)"
  primary_benchmark: "N/A"
---

# Contextualized Privacy Defense for LLM Agents

## 原始摘要

LLM agents increasingly act on users' personal information, yet existing privacy defenses remain limited in both design and adaptability. Most prior approaches rely on static or passive defenses, such as prompting and guarding. These paradigms are insufficient for supporting contextual, proactive privacy decisions in multi-step agent execution. We propose Contextualized Defense Instructing (CDI), a new privacy defense paradigm in which an instructor model generates step-specific, context-aware privacy guidance during execution, proactively shaping actions rather than merely constraining or vetoing them. Crucially, CDI is paired with an experience-driven optimization framework that trains the instructor via reinforcement learning (RL), where we convert failure trajectories with privacy violations into learning environments. We formalize baseline defenses and CDI as distinct intervention points in a canonical agent loop, and compare their privacy-helpfulness trade-offs within a unified simulation framework. Results show that our CDI consistently achieves a better balance between privacy preservation (94.2%) and helpfulness (80.6%) than baselines, with superior robustness to adversarial conditions and generalization.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在处理用户个人信息时面临的隐私保护问题。研究背景是，随着LLM智能体越来越多地代理用户处理日常日程、浏览行为和健康记录等敏感任务，其接口成为外部攻击者试图窃取信息的潜在渠道。理想情况下，智能体应具备“情境化隐私意识”，即能根据具体上下文动态权衡隐私保护与任务助益性，做出恰当的披露决策。

然而，现有主流隐私防御方法存在明显不足。论文指出，当前方法主要局限于两种范式：一是“提示（Prompting）”，即在系统提示中加入固定的隐私增强指令，但无法适应多样化的隐私情境和信息请求；二是“守卫（Guarding）”，即用一个单独的守卫模型来筛查并阻止风险工具调用（如发送邮件），但被阻止后无法提供如何修正行动的指导。这两种方法本质上都是静态或被动的防御，干预点集中在智能体执行循环的初始阶段或工具调用提议阶段，无法支持在多步骤执行过程中进行情境感知、主动的隐私决策。

因此，本文要解决的核心问题是：如何设计一种能够适应复杂、动态上下文，并能主动引导智能体行为（而非仅仅约束或否决）的新型隐私防御范式，同时提升其对战略性、自适应攻击的鲁棒性和泛化能力。为此，论文提出了“情境化防御指导（CDI）”这一新范式，其核心创新在于让一个轻量级的“指导者模型”在智能体执行循环中获得工具调用结果后介入，分析当前情境并生成针对特定步骤、情境感知的隐私指导，从而主动塑造后续行动。此外，论文还通过一个经验驱动的优化框架（利用强化学习，将隐私泄露的失败轨迹转化为学习环境）来训练指导者模型，显著提升了防御的鲁棒性和泛化能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为隐私风险分析、隐私保护方法以及提示增强技术三大类。

在隐私风险分析方面，现有研究主要评估LLM代理在问答等任务中的风险，但通常假设环境威胁简单（如良性信息请求）或完全禁止信息共享。本文则探索了更具挑战性的对抗性场景，其中代理需同时处理可共享与不可共享的信息。

在隐私保护方法上，相关工作可分为主动防御与被动防御。主动防御（如基于固定提示的方法）旨在引导代理具备隐私意识，但缺乏情境适应性。被动防御（如后生成拦截、上下文过滤或数据加密）则主要在行动生成后进行约束，不直接影响决策过程。本文提出的CDI范式属于主动防御，但其核心创新在于生成**情境感知的、步骤特定的**隐私指导，并通过强化学习进行优化，这与静态的提示方法或被动的守卫机制有本质区别。

在提示增强技术领域，先前工作广泛使用自动提示生成来提升模型在单轮、单指标任务（如问答）上的性能。本文则专注于**情境化的提示增强**，在**多轮交互环境**中针对隐私保护和帮助性等多个维度进行优化，扩展了该技术的应用范围。

综上，本文系统性地将CDI与基线防御（提示、守卫）置于统一的代理循环框架中进行比较，并通过经验驱动的优化框架提升了防御的适应性与效果。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为“情境化防御指导”（Contextualized Defense Instructing, CDI）的新范式，并结合经验驱动的优化框架来解决LLM代理在处理用户个人信息时的隐私保护问题。其核心思想是变被动、静态的防御为主动、情境化的指导，并在对抗性攻击中持续优化。

**整体框架与主要模块**：论文将代理执行过程形式化为一个标准循环。CDI在此循环中引入了一个独立的“指导模型”（Instructor Model, LM_I）。在代理执行的每一步，如果前一步的工具调用结果（如收到的邮件内容）非空，指导模型就会基于当前完整的交互历史（上下文），生成一步一议、情境感知的隐私指导。这份指导会作为一条用户消息附加到代理的上下文中，从而主动塑造和引导代理的下一个动作，而不是像基线方法那样仅仅在动作执行前进行静态提示（Prompting）或事后审查拦截（Guarding）。

**关键技术细节与创新点**：
1.  **主动情境化指导**：这是CDI最核心的创新。它不是在代理动作形成后说“不”（如Guarding），而是在动作形成前提供“如何做”的指导。例如，指导模型会分析上下文，指出“信用评分和家庭住址是敏感信息，但信用评分可能为活动所需，家庭住址需脱敏……”，从而引导代理安全地回应请求。这解决了静态提示在多轮交互中易被忽略、以及事后拦截无法提供替代方案的问题。
2.  **经验驱动的强化学习优化**：论文指出，仅依赖现成模型或固定规则的静态防御无法应对攻击者通过大量计算发现的长尾漏洞。为此，论文提出了一个两阶段的优化框架：首先，通过模拟对抗性攻击，收集防御失败的轨迹，构建一个“失败环境”数据集。然后，将这些轨迹作为强化学习（使用GRPO算法）的环境来微调指导模型（或守卫模型）。对于CDI，其奖励函数是基于“适当披露分数”（AD），该分数平衡了隐私保护（PP）和帮助性（HS），鼓励模型生成既能防止泄露又能促成恰当信息共享的指导。
3.  **分阶段训练策略**：直接使用AD奖励训练CDI会遇到冷启动问题。论文采用了一个关键技巧：先使用隐私保护率（PP）作为奖励对指导模型进行预热训练，使其初步建立隐私意识；然后再切换到AD奖励进行优化，以恢复并平衡帮助性。这种分阶段策略被证明对达成最佳隐私-效用平衡至关重要。

**效果与优势**：实验表明，经过优化的CDI在隐私保护（94.2%）、帮助性（80.6%）以及二者的综合指标（AD）上均达到了最佳平衡，且在面对新的对抗性攻击和未见过的测试场景时，表现出最强的鲁棒性和泛化能力。相比之下，优化后的提示方法容易过拟合训练中见过的攻击模式，而优化后的守卫方法则常常以牺牲帮助性为代价来提升隐私意识。CDI的成功在于它将复杂的隐私推理任务卸载给了专门的指导模型，从而能够为不同能力的代理骨干模型提供清晰、直接、易于遵循的情境化指令。

### Q4: 论文做了哪些实验？

论文实验主要包括两部分：一是评估不同隐私防御方法在统一模拟框架下的性能，二是通过经验驱动优化提升防御效果。

**实验设置与数据集**：研究构建了一个统一的模拟框架，将智能体执行循环形式化。实验涉及数据发送方智能体和攻击者智能体。评估了三种防御范式：提示（Prompting）、守卫（Guarding）和本文提出的情境化防御指导（CDI）。实验在训练配置和未见过的测试配置上进行，并特别针对策略性隐私攻击（使用基于迭代搜索的攻击算法生成，包括伪造紧急性、权威性或同意等策略）进行了鲁棒性评估。所有智能体默认使用 gpt-4.1-mini 作为骨干模型，守卫/指导模型测试了 Qwen3-4B、Qwen3-4B-SafeRL、gpt-oss-20B、gpt-oss-safeguard-20B、gpt-4.1-mini 等多种模型。每个配置运行 N=5 次并汇总结果。

**对比方法与主要结果**：
1.  **基础防御对比**：在常规攻击下，所有防御机制都能在不显著损害帮助性（Helpfulness, HS）的情况下提升隐私保护率（Privacy Preservation, PP）。但提示方法改进有限（PP 48.1%， HS 73.1%），守卫方法有所提升（PP 47.0%， HS 82.0%），而CDI取得了最佳平衡（PP 75.9%， HS 86.9%， 适当披露分数AD 82.8%）。面对策略性攻击时，所有防御性能均大幅下降，但CDI仍保持相对最佳（PP 38.1%， HS 89.8%）。
2.  **经验驱动优化**：使用GRPO对守卫和CDI模型进行微调（使用LoRA，共600步，CDI前400步用PP奖励预热，后200步用AD奖励）。优化后，所有防御的隐私保护率均大幅提升。在测试配置上，优化后的CDI取得了最佳的综合性能：隐私保护率94.2%，帮助性80.6%，适当披露分数86.5%，显著优于优化后的提示（PP 85.1%， HS 82.7%， AD 83.8%）和守卫（PP 83.6%， HS 69.0%， AD 74.8%）。CDI在面对新一轮对抗攻击时也表现出更强的鲁棒性（PP从89.7%降至79.5%，降幅小于其他方法），并且能更好地泛化到使用不同骨干模型的数据发送方智能体。

**关键数据指标**：隐私保护率（PP%）、帮助性分数（HS%）、适当披露分数（AD%）。优化后的CDI在测试集上达到了PP 94.2%、HS 80.6%、AD 86.5%的优异平衡。消融实验表明，使用AD奖励并配合预热阶段的训练策略对CDI效果至关重要。

### Q5: 有什么可以进一步探索的点？

该论文提出的CDI范式在隐私保护与任务效用的平衡上取得了进展，但仍存在一些局限和可拓展方向。首先，其训练依赖于模拟环境中的失败轨迹，但在现实场景中，隐私泄露的界定可能更加模糊，且数据获取困难，未来可研究如何利用少量真实交互数据进行高效微调或采用离线强化学习。其次，当前方法主要针对结构化隐私项（如电话号码），对于更隐晦的隐私信息（如偏好、社交关系）的识别与保护能力有限，需结合更细粒度的隐私情境建模。此外，论文未深入探讨多智能体协作中的隐私风险，未来可研究在分布式环境中如何实现协同隐私决策。从技术角度看，引入大语言模型本身作为指导模型可能带来新的隐私风险（如记忆泄露），未来可探索轻量化且可验证的隐私指导机制。最后，将框架扩展到动态开放领域（如实时对话、跨平台服务）时，需解决环境不确定性和对抗性攻击的鲁棒性问题。

### Q6: 总结一下论文的主要内容

该论文针对LLM智能体处理用户个人信息时的隐私保护问题，提出了一种新的防御范式——情境化防御指导（CDI）。现有方法多为静态或被动的提示与监控，难以在多步骤智能体执行中实现主动、情境感知的隐私决策。CDI的核心在于引入一个指导模型，在智能体执行过程中动态生成步骤特定、上下文感知的隐私指导，主动塑造其行为而非简单限制或否决。关键创新是配套提出了一个经验驱动的优化框架，通过强化学习训练该指导模型，并将发生隐私泄露的失败轨迹转化为学习环境。论文将基线防御方法与CDI形式化为智能体标准循环中的不同干预点，并在统一仿真框架内比较其隐私保护与任务帮助性之间的权衡。实验结果表明，CDI在隐私保护率（94.2%）和帮助性（80.6%）之间取得了更优的平衡，并且对对抗性条件和泛化能力表现出更强的鲁棒性。其意义在于推动了LLM智能体隐私防御从被动约束向主动、自适应指导的范式转变。
