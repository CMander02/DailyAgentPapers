---
title: "Beyond Self-Interest: Modeling Social-Oriented Motivation for Human-like Multi-Agent Interactions"
authors:
  - "Jingzhe Lin"
  - "Ceyao Zhang"
  - "Yaodong Yang"
  - "Yizhou Wang"
  - "Song-Chun Zhu"
  - "Fangwei Zhong"
date: "2026-03-14"
arxiv_id: "2603.13890"
arxiv_url: "https://arxiv.org/abs/2603.13890"
pdf_url: "https://arxiv.org/pdf/2603.13890v1"
categories:
  - "cs.MA"
tags:
  - "Multi-Agent"
  - "Social Simulation"
  - "Theory-Driven"
  - "Human-Likeness"
  - "Motivation Modeling"
  - "LLM-based Agent"
relevance_score: 7.5
---

# Beyond Self-Interest: Modeling Social-Oriented Motivation for Human-like Multi-Agent Interactions

## 原始摘要

Large Language Models (LLMs) demonstrate significant potential for generating complex behaviors, yet most approaches lack mechanisms for modeling social motivation in human-like multi-agent interaction. We introduce Autonomous Social Value-Oriented agents (ASVO), where LLM-based agents integrate desire-driven autonomy with Social Value Orientation (SVO) theory. At each step, agents first update their beliefs by perceiving environmental changes and others' actions. These observations inform the value update process, where each agent updates multi-dimensional desire values through reflective reasoning and infers others' motivational states. By contrasting self-satisfaction derived from fulfilled desires against estimated others' satisfaction, agents dynamically compute their SVO along a spectrum from altruistic to competitive, which in turn guides activity selection to balance desire fulfillment with social alignment. Experiments across School, Workplace, and Family contexts demonstrate substantial improvements over baselines in behavioral naturalness and human-likeness. These findings show that structured desire systems and adaptive SVO drift enable realistic multi-agent social simulations.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型的多智能体交互中，缺乏对社会性动机进行动态建模的问题。研究背景是，模拟类人行为一直是人工智能的核心目标，特别是在多智能体场景中，需要刻画具有不同个性、动机和社会偏好的复杂社会动态。尽管大语言模型为智能体社会模拟开辟了新途径，现有方法（如Generative Agents、ProAgent等）大多依赖静态或基于规则的个性设定，难以捕捉人类内在动机的动态变化。虽然近期研究开始将社会价值取向理论或欲望驱动自主性等心理学结构引入智能体，但这些方法要么侧重于任务生成而忽略了社会偏好对交互的塑造，要么缺乏机制来建模社会动机如何随互动自适应演变。

因此，本文要解决的核心问题是：如何构建一个框架，使基于大语言模型的智能体能够整合结构化的内在欲望系统与动态演化的社会价值取向，从而超越纯粹的自我利益，在交互中产生更自然、更类人、社会一致性更高的行为。具体而言，论文提出了自主社会价值导向智能体框架，通过让智能体在每一步更新信念、反思并更新多维欲望值、推断他人动机状态，并对比自我满足感与他人预估满足感来动态计算其社会价值取向，进而指导行为选择，以平衡欲望满足与社会对齐。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：社会模拟、社会价值取向（SVO）理论应用，以及智能体动机与人格建模。

在社会模拟方面，已有研究利用大语言模型（LLM）提升基于智能体的社会模拟的真实性与复杂性。例如，Voyager、CAMEL等框架展示了LLM智能体在虚拟环境中自主探索与协作的能力；D2A、Ecoagent、OASIS和AgentScope等则扩展了大规模多样化社会环境的模拟能力。这些工作为复杂语言交互和行为建模奠定了基础，但本文指出，它们大多依赖静态或基于规则的智能体人格，难以捕捉人类行为的异质性和动态价值变化。

在社会价值取向（SVO）理论应用方面，SVO作为量化个体社会偏好的关键概念，已被广泛应用于多智能体模拟，以研究合作、竞争和社会困境。相关研究通过为智能体分配异质的SVO值，提升了模拟结果的社会真实性，例如在人类-机器人团队中改善公平与信任。然而，本文强调，现有工作通常将SVO视为静态属性，未能反映人类社交偏好随情境动态变化的特性。

在动机与人格建模方面，传统多智能体系统常依赖手工规则或固定奖励结构，限制了其表达和适应能力。近期研究尝试将马斯洛需求层次、自我决定理论等经典心理学理论与SVO结合，以构建更丰富的内在动机模型。本文提出的ASVO框架与这些工作方向一致，但其核心创新在于**将基于欲望的自主性与动态SVO计算相结合**，使智能体能够通过反思推理更新多维欲望值，并对比自我与他人满足感来动态调整SVO（从利他到竞争），从而更真实地平衡欲望满足与社会对齐。这区别于以往静态人格或固定SVO的模型，实现了对社会导向动机的适应性建模。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ASVO（Autonomous Social Value-Oriented agents）的框架来解决多智能体交互中社会动机建模不足的问题。其核心方法是让基于大语言模型（LLM）的智能体将欲望驱动的自主性与社会价值取向（SVO）理论相结合，从而模拟出更类人的、社会导向的行为。

整体框架是一个循环迭代的感知-动机-价值-行动闭环。在每个模拟步长中，智能体依次执行四个核心模块：信念更新、价值更新、SVO计算和活动生成。

主要模块与关键技术包括：
1.  **信念更新模块**：智能体主动感知环境变化（如资源变动）和观察其他智能体的行为，更新其内部世界状态信念，为自我和他人建模提供基础。
2.  **价值更新模块**：这是驱动动机系统的核心。每个智能体维护一个结构化的、多维度的欲望状态（如论文中实例化的八个维度），并通过LLM介导的反思循环来更新自身欲望。同时，智能体进行“SVO条件化社会推理”，根据观察到的行为线索或基于SVO和上下文的推断，来估计其他智能体的欲望状态。这使智能体能够理解并预测他人的意图。
3.  **SVO计算模块**：这是关键创新点。智能体动态计算其当前SVO，该值在从利他到竞争的频谱上连续变化。计算公式基于对自身欲望满足度（S_self）和估计的他人欲望满足度（S_other）的比较：θ_svo = arctan(S_other / S_self)。每个智能体还有一个固定的预期SVO作为人格基线。如果当前计算出的SVO偏离了预期区间，会触发一个调节机制。
4.  **活动生成模块**：基于调节后的SVO，智能体通过一个结构化过程生成行为。LLM根据智能体的需求、上下文和当前SVO提出多个候选动作。每个动作都会评估其对自身欲望满足度的预测提升以及其导致的SVO角度。最终动作的选择被形式化为一个带约束的优化问题：在候选动作中，选择能最大化自身欲望满足度（U_self）的动作，但前提是该动作预测的SVO必须落在预期的SVO区间内。这确保了行为在满足自身动机的同时，与社会价值取向保持一致。

创新点主要体现在：
*   **结构化欲望系统与动态SVO的结合**：将内在动机（多维欲望）与社会取向（SVO）明确分离又相互关联，为行为提供了丰富的心理基础。
*   **SVO的动态计算与调节机制**：SVO不是静态的人格标签，而是根据实时社会互动和欲望满足情况动态计算得出的，并能通过反馈循环进行调节以保持人格一致性，这模拟了人类社会动机的适应性。
*   **社会推理与价值对齐的决策**：智能体不仅更新自我状态，还主动推断他人的动机状态（外部欲望），并将此估计用于计算SVO和指导决策，实现了真正社会情境下的价值权衡。

### Q4: 论文做了哪些实验？

论文在三个社会情境（学校、职场、家庭）中进行了实验，评估ASVO模型在模拟类人、社会动机驱动的多智能体交互方面的有效性。实验在一个扩展的、基于Concordia的多智能体仿真平台中进行，该平台支持灵活的智能体配置、实时交互日志和可复现的环境初始化。

**实验设置与数据集/基准测试**：实验构建了微观、中观和宏观三个社会尺度，覆盖学校（宿舍、课堂小组、班级选举）、职场（办公室二人组、项目团队、部门评审）和家庭（周末居家、公园出游）场景。研究使用了四种大语言模型（GPT-5、Qwen3-235b、Deepseek-v3、Gemini-2.5）作为行为生成器和自动评估器。

**对比方法**：将ASVO与几种代表性的基于LLM的智能体基线进行了比较，包括ReAct、BabyAGI、LLMob和D2A（一个早期的内在动机驱动框架）。这些基线遵循其原始设计（例如目标驱动规划、固定习惯或静态特质），没有显式的SVO建模。

**主要结果与关键指标**：
1.  **行为自然度与类人性**：ASVO在所有情境和LLM骨干网络上均取得了最高的自然度（N）和类人性（H）平均分，且标准差最低，表明其鲁棒性强。例如，在学校情境中，ASVO的N/H平均分为4.802/4.821，显著高于基线（如ReAct为3.876/3.625）。
2.  **合作与竞争行为谱**：ASVO能根据初始化的SVO人格类型（利他、亲社会、个人主义、竞争）产生连续、可解释的行为谱。利他/亲社会智能体表现出明显的合作倾向，而个人主义/竞争型智能体则竞争行为占主导。基线模型则无法复现这种结构化趋势。
3.  **SVO动态适应性**：实验验证了ASVO能有效保持各人格类型SVO值在其理论参考区间内随时间演化，证实了模型对社会价值取向的持续区分能力。
4.  **可扩展性测试**：在扩展时间步长（6至24步）和增加智能体数量（4至32个）的学校场景测试中，ASVO在行为自然度和类人性上表现稳健，分数随规模扩大仅有平缓下降，证明了其扩展到更大场景的能力。
5.  **社会尺度影响**：在学校情境中，随着环境从微观扩展到宏观，所有人格类型的合作率均有所上升（例如利他型从0.15升至0.56），表明更复杂的环境增强了社会参与度和行为模式的丰富性。

### Q5: 有什么可以进一步探索的点？

该论文在建模社会性动机方面取得了进展，但仍有多个方向值得深入探索。首先，其局限性在于社会价值取向（SVO）的计算主要基于“自我满足”与“推断他人满足”的对比，这种推断可能过于简化，未能充分捕捉人类互动中复杂的意图推理、误解或欺骗等动态心理过程。未来研究可引入更精细的**心理理论（Theory of Mind）模型**，使代理不仅能推断他人满意度，还能模拟他人的信念、意图甚至其对自身动机的推测，从而提升交互的深度与真实性。

其次，当前模型在“学校、职场、家庭”等封闭场景中验证，其社会规范相对明确。未来可探索**开放域或跨文化环境**，研究代理如何在不同社会规范冲突下自适应调整SVO，甚至形成新的社会公约。这需要动态的社会规范学习机制。

此外，论文中的欲望系统是预定义且多维的，但人类动机具有层次性（如马斯洛需求层次）和长期演变性。一个可能的改进思路是引入**基于强化学习的欲望演化机制**，让代理在与环境长期互动中自主形成或调整其核心欲望，从而使行为动机更具发展性和个体差异性。

最后，技术层面可探索将SVO机制与**多模态交互**结合，使代理能通过语音、表情等非文本线索更细腻地感知和表达社会动机，进一步逼近人类社交的丰富性。

### Q6: 总结一下论文的主要内容

这篇论文提出了自主社会价值导向智能体（ASVO）框架，旨在解决现有基于大语言模型的多智能体交互中缺乏对社会动机建模的问题。核心贡献是将心理学中的社会价值取向（SVO）理论与基于欲望驱动的自主性相结合，使智能体能够动态调整从利他到竞争的社会取向。方法上，智能体通过感知环境和他者行为更新信念，并利用反思推理更新多维欲望值、推断他者动机；通过对比自身欲望满足带来的满足感与预估的他者满足感，动态计算SVO并据此选择行动，以平衡个人欲望满足与社会关系协调。实验在学校、职场和家庭场景中验证了ASVO相比基线在行为自然度和拟人化方面的显著提升。主要结论表明，结构化的欲望系统和自适应的SVO漂移机制能够实现更真实、类人的多智能体社会模拟，为构建具有社会意识的AI智能体提供了新思路。
