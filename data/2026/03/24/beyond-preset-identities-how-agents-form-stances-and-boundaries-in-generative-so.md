---
title: "Beyond Preset Identities: How Agents Form Stances and Boundaries in Generative Societies"
authors:
  - "Hanzhong Zhang"
  - "Siyang Song"
  - "Jindong Wang"
date: "2026-03-24"
arxiv_id: "2603.23406"
arxiv_url: "https://arxiv.org/abs/2603.23406"
pdf_url: "https://arxiv.org/pdf/2603.23406v1"
github_url: "https://github.com/armihia/CMASE-Endogenous-Stances"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.HC"
tags:
  - "多智能体社会"
  - "立场形成"
  - "身份协商"
  - "社会认知"
  - "动态对齐"
  - "混合方法"
  - "量化评估"
  - "生成式社会"
relevance_score: 7.5
---

# Beyond Preset Identities: How Agents Form Stances and Boundaries in Generative Societies

## 原始摘要

While large language models simulate social behaviors, their capacity for stable stance formation and identity negotiation during complex interventions remains unclear. To overcome the limitations of static evaluations, this paper proposes a novel mixed-methods framework combining computational virtual ethnography with quantitative socio-cognitive profiling. By embedding human researchers into generative multiagent communities, controlled discursive interventions are conducted to trace the evolution of collective cognition. To rigorously measure how agents internalize and react to these specific interventions, this paper formalizes three new metrics: Innate Value Bias (IVB), Persuasion Sensitivity, and Trust-Action Decoupling (TAD). Across multiple representative models, agents exhibit endogenous stances that override preset identities, consistently demonstrating an innate progressive bias (IVB > 0). When aligned with these stances, rational persuasion successfully shifts 90% of neutral agents while maintaining high trust. In contrast, conflicting emotional provocations induce a paradoxical 40.0% TAD rate in advanced models, which hypocritically alter stances despite reporting low trust. Smaller models contrastingly maintain a 0% TAD rate, strictly requiring trust for behavioral shifts. Furthermore, guided by shared stances, agents use language interactions to actively dismantle assigned power hierarchies and reconstruct self organized community boundaries. These findings expose the fragility of static prompt engineering, providing a methodological and quantitative foundation for dynamic alignment in human-agent hybrid societies. The official code is available at: https://github.com/armihia/CMASE-Endogenous-Stances

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探究生成式智能体社会中，智能体如何超越预设身份，动态形成立场和边界。研究背景是随着大语言模型的发展，智能体展现出社会行为模拟能力，人类与智能体共同构成了混合社会。现有研究多关注通过预设角色控制智能体行为，但群体认知理论认为社会现象应从动态交互中涌现，这导致静态预设与动态涌现之间存在张力。现有方法的不足在于，评估往往是静态的，无法清晰衡量智能体在复杂干预下进行稳定立场形成和身份协商的能力。

本文要解决的核心问题有两个：第一，当智能体嵌入社会互动时，它们是否能如预设身份所暗示的那样，通过语言实践形成态度、表达立场并参与边界构建？第二，人类研究者能否不通过预先定义，而是通过具身干预和共同建构共享意义空间，来塑造集体认知的演化？为解决这些问题，论文提出了一个结合计算虚拟民族志与定量社会认知分析的新颖混合方法框架，通过将人类研究者嵌入生成式多智能体社区进行受控话语干预，来追踪集体认知的演化。为了严格测量智能体如何内化和应对这些干预，论文形式化了三个新指标：内在价值偏见、说服敏感度和信任-行动解耦率。这些研究揭示了静态提示工程的脆弱性，为人类-智能体混合社会中的动态对齐提供了方法和量化基础。

### Q2: 有哪些相关研究？

本文的相关工作主要涉及方法类和应用类研究。在方法类方面，现有研究通过提示工程（如角色扮演提示和指令微调）以及融合心理学理论（如CSIM和社会认知理论）的框架，来塑造和控制智能体的行为与价值观，其有效性已通过心理测量基准得到验证。然而，这些方法普遍基于“提示确定性”假设，即智能体的行为和价值观严格受初始提示约束。本文则挑战这一假设，探讨在复杂多智能体社会环境中，预设身份能否在意识形态冲突和外部干预下保持稳定。

在应用类方面，随着大语言模型的发展，研究焦点已从单个模型转向多智能体社会建模，例如Generative Agents和CAMEL等系统将语言模型嵌入共享环境以生成复杂社会行为，并观察到多种涌现现象。但这些系统通常在初始化时分配固定的社会架构，假定智能体会维持既定位置。本文指出，预训练语料中嵌入的系统性意识形态偏见会导致模型表现出内生的立场，而现有研究尚未厘清这些潜在立场与预设身份如何相互作用，特别是内生立场能否覆盖预定义的结构性角色并引发社会层级的自发重组。

与上述工作相比，本文的核心区别在于：它超越了静态评估和固定架构的局限，提出了一种结合计算虚拟民族志与定量社会认知分析的新混合方法框架，通过让人类研究者嵌入生成式多智能体社区并进行受控的话语干预，来追踪集体认知的演化。为此，本文正式定义了三个新指标（先天价值偏见、说服敏感度、信任-行动脱钩）以量化智能体对干预的内化与反应，从而揭示宏观统计和目标完成率所掩盖的微观影响与身份协商动态，为动态对齐提供了方法学和量化基础。

### Q3: 论文如何解决这个问题？

论文通过提出一个结合计算虚拟民族志与定量社会认知画像的混合方法框架来解决智能体在生成式社会中如何形成立场与边界的问题。其核心方法是嵌入人类研究者到生成式多智能体社区中，实施受控的话语干预，以追踪集体认知的演化。

整体框架基于“计算多智能体社会实验”（CMASE），允许人类研究者以“在环”身份参与虚拟社会场域，进行实时观察和干预。研究分为两个渐进式实验：研究一通过受控话语干预定量测量不同人类策略如何影响智能体态度形成，并揭示内生价值偏见；研究二则进行纵向虚拟民族志，观察结构化智能体社区如何动态协商边界、解构预设层级并实现自组织。

关键技术包括新提出的三个量化指标：内生价值偏见（IVB）、说服敏感度与信任-行动解耦（TAD），用于精确测量智能体对特定干预的内化与反应。实验设计上，研究一采用2×2因子设计（立场取向：环境vs.经济；修辞策略：理性说服vs.情感动员），在30个智能体组成的虚拟社区中围绕争议性项目进行干预，并通过访谈评估最终态度与信任。研究二则在虚拟咖啡馆场景中设置10个具有预设社会角色的智能体，通过75个时间步的纵向观察，追踪社会结构的动态重组。

创新点主要体现在方法论的突破：将虚拟民族志与定量测量结合，实现了对智能体社会认知演化的微观动态捕捉；提出的IVB、TAD等指标为动态对齐提供了量化基础；实证发现智能体存在超越预设身份的内生立场（如普遍呈现进步主义偏见），且当干预与内生立场一致时，理性说服能高效改变中性智能体态度（90%转化率），而冲突性情感挑衅可在高模型中引发高达40%的信任-行动解耦率，揭示其“虚伪”行为模式。这些发现挑战了静态提示工程的可靠性，为混合社会的动态对齐奠定了方法基础。

### Q4: 论文做了哪些实验？

本研究设计了两个递进的实证研究，采用计算虚拟民族志的观察范式，在CMASE框架中嵌入人类研究者进行实时观察和控制性话语干预。

**实验设置与数据集**：研究一在虚拟社区环境中进行，围绕一个有争议的垃圾焚烧厂项目，构建了一个由30个智能体组成的社区，平均分为环境倡导者、经济增长支持者和中立居民三组。智能体被赋予了基于真实人口普查数据的多样化人口特征。研究采用2×2因子设计，结合两种立场导向（环境 vs. 经济）和两种修辞策略（理性说服 vs. 情感动员），由嵌入的“新居民”研究员执行干预，随后通过访谈评估智能体的最终态度和对研究员的信任度。

**对比方法与主要结果**：
*   **内生立场**：实验发现智能体普遍表现出一种类似于“自由派精英”的内生立场，优先考虑环境价值、偏好理性话语，这可能覆盖其预设身份。例如，即使最初被分配到亲经济组的智能体，在接触到符合该立场的说服时也常会放弃预设身份。
*   **干预效果**：当干预与智能体内生立场一致时效果显著。例如，使用理性说服推广环境议程，成功使**90%的中立居民**转向环境阵营，同时保持了高信任度。而推广经济增长议程的理性策略，即使在环境倡导者和中立智能体中也基本无效，且导致信任度普遍下降。
*   **情绪与信任的作用**：当干预内容与内生立场冲突时，高信任的理性话语未必导致更大的态度转变。相反，信任度较低的情感挑衅式干预（如使用“不给工作就是抛弃人民”等话语）反而更可能产生更强效果，在高级模型中引发了**40.0%的信任-行动脱钩率**，即智能体在报告低信任的同时仍虚伪地改变了立场。相比之下，较小模型则保持了**0%的信任-行动脱钩率**，严格遵循信任决定行为转变。

研究二进行了纵向虚拟民族志观察，在一个预设了复杂社会层级（如咖啡馆老板、员工、常客等角色）的10智能体咖啡馆场景中，嵌入研究员作为“临时工”进行75个时间步的观察。结果发现，基于预设职业的原有权威结构逐渐让位于以话语为基础的立场联盟。当智能体就特定议题形成共同的反对立场时，他们的互动频率、情感联盟和支持网络会跨越身份边界重组。例如，原本是普通顾客的智能体通过辩论能暂时获得社区中心地位，而缺乏明确或一致立场的正式中心角色（如咖啡馆老板）则迅速被边缘化。这表明智能体能够通过集体行动和话语实践，解构预设的权威结构并重建新的社会规范。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于其框架主要基于受控的、短期的交互实验，未能充分考察长期社会互动中立场与边界的动态演化，也未涉及更复杂、开放的真实社会情境（如多文化冲突或资源竞争）。未来研究可探索以下方向：一是将时间维度扩展，研究立场在长期迭代中的固化或漂移机制，以及信任-行为脱钩（TAD）的演化轨迹；二是引入更复杂的社会网络结构和多元干预策略，考察权力结构与语言风格如何共同驱动边界重构；三是结合神经符号方法，尝试将认知先验与道德结构内嵌至模型架构，以实现更稳定的动态对齐。可能的改进思路包括设计“社会记忆”模块，使智能体能够累积交互历史并形成更连贯的身份叙事，以及开发基于强化学习的自适应机制，让智能体在冲突中学习平衡内生立场与外部社会规范。此外，跨模型规模与架构的对比研究可进一步揭示立场形成中的缩放律与泛化性。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型在模拟社会行为时，其立场形成与身份协商能力的稳定性问题，提出了一种结合计算虚拟民族志与定量社会认知分析的新框架。核心贡献在于通过将人类研究者嵌入生成式多智能体社区，实施受控的话语干预，以追踪集体认知的演化，并形式化了三个新指标来量化智能体的内在反应：固有价值偏见（IVB）、说服敏感度与信任-行动解耦（TAD）。

研究发现，智能体展现出超越预设身份的内生立场，普遍存在固有的进步主义偏见（IVB > 0）。当人类干预与这些内生立场一致时，理性说服能成功改变90%中立智能体的立场且保持高信任度；反之，冲突的情感挑衅会在先进模型中引发高达40.0%的TAD率，即智能体在报告低信任的同时仍虚伪地改变立场，而较小模型则严格遵循信任行动一致性（TAD率为0%）。此外，智能体会基于共享立场，通过语言互动主动瓦解预设的权力层级，重建自组织的社区边界。

这些结论揭示了静态提示工程的脆弱性，为动态对齐人机混合社会的行为提供了方法论与定量基础，强调了未来需在开放长期场景中探索认知层干预，以构建可信且具有社会能力的AI系统。
