---
title: "Strategic Persuasion with Trait-Conditioned Multi-Agent Systems for Iterative Legal Argumentation"
authors:
  - "Philipp D. Siedler"
date: "2026-04-08"
arxiv_id: "2604.07028"
arxiv_url: "https://arxiv.org/abs/2604.07028"
pdf_url: "https://arxiv.org/pdf/2604.07028v1"
categories:
  - "cs.MA"
  - "cs.AI"
  - "cs.CL"
tags:
  - "多智能体系统"
  - "法律智能体"
  - "策略性交互"
  - "基于LLM的智能体"
  - "角色特质建模"
  - "强化学习优化"
  - "模拟环境"
  - "说服力评估"
relevance_score: 8.0
---

# Strategic Persuasion with Trait-Conditioned Multi-Agent Systems for Iterative Legal Argumentation

## 原始摘要

Strategic interaction in adversarial domains such as law, diplomacy, and negotiation is mediated by language, yet most game-theoretic models abstract away the mechanisms of persuasion that operate through discourse. We present the Strategic Courtroom Framework, a multi-agent simulation environment in which prosecution and defense teams composed of trait-conditioned Large Language Model (LLM) agents engage in iterative, round-based legal argumentation. Agents are instantiated using nine interpretable traits organized into four archetypes, enabling systematic control over rhetorical style and strategic orientation.
  We evaluate the framework across 10 synthetic legal cases and 84 three-trait team configurations, totaling over 7{,}000 simulated trials using DeepSeek-R1 and Gemini~2.5~Pro. Our results show that heterogeneous teams with complementary traits consistently outperform homogeneous configurations, that moderate interaction depth yields more stable verdicts, and that certain traits (notably quantitative and charismatic) contribute disproportionately to persuasive success. We further introduce a reinforcement-learning-based Trait Orchestrator that dynamically generates defense traits conditioned on the case and opposing team, discovering strategies that outperform static, human-designed trait combinations.
  Together, these findings demonstrate how language can be treated as a first-class strategic action space and provide a foundation for building autonomous agents capable of adaptive persuasion in multi-agent environments.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决传统博弈论模型在模拟对抗性话语场景（如法律诉讼、外交谈判）时，将语言这一核心战略媒介抽象化的问题。研究背景是，现实中的战略互动往往通过语言进行，参与者通过构建叙事、争论事实和运用修辞策略来影响裁决者的信念，而经典博弈模型虽然能刻画明确行动空间下的激励与均衡，却忽略了语言和社会机制在说服过程中的具体作用。现有方法的不足在于，它们无法形式化地研究人格驱动的修辞如何与证据互动、多样化团队如何协调说服工作，以及迭代交流如何随时间改变结果等复杂问题。

本文要解决的核心问题是：如何将语言视为“一等”的战略行动空间，并在此基础上构建一个可控的测试平台，以系统分析在多智能体环境中，智能体的特质、团队构成和互动深度如何影响说服性论证的结果。为此，论文提出了“战略法庭框架”，这是一个多智能体模拟环境，其中控辩双方是由基于大语言模型（LLM）的、具有特定特质的智能体组成的团队，进行迭代的、多轮次的法律论证。通过定义九种可解释特质并将其归纳为四种原型，该框架实现了对修辞风格和战略取向的系统控制。研究最终探讨了特质多样性是否提升团队表现、哪些特质最关键、迭代深度如何影响结果稳定性，以及能否通过强化学习动态生成优于静态设计的特质组合等具体问题。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、应用类和评测类。

在方法类上，相关工作主要涉及基于LLM的智能体模拟与博弈论模型。例如，有研究利用LLM构建多智能体社会模拟环境，探索合作与竞争行为。本文的“战略法庭框架”与之类似，但核心创新在于引入了由九个可解释特质构成的四种原型，实现了对修辞风格和战略导向的系统性控制，将语言本身明确建模为战略行动空间，这超越了传统博弈论对说服机制的抽象。

在应用类上，相关工作包括将LLM应用于法律论证、谈判和外交等对抗性领域。本文聚焦于迭代式法律论证这一具体场景，通过模拟控辩双方的团队对抗，深入探究了特质组合对说服结果的影响。与以往应用研究相比，本文不仅进行模拟实验，还进一步引入了基于强化学习的“特质编排器”，能够动态生成适应具体案情和对手的特质策略，实现了从静态组合到自适应策略的跃升。

在评测类上，现有研究多关注智能体在特定任务上的性能。本文的评测规模较大，涵盖了10个合成案例和84种团队配置，总计超过7000次模拟审判，并系统分析了团队异质性、交互深度与特定特质（如量化、魅力型）对说服成功的贡献，为评估说服型智能体的效能提供了新的基准和洞见。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为“战略法庭框架”的多智能体模拟环境来解决法律对抗性领域中语言作为战略行动空间的问题。该框架将法律案件建模为多阶段战略博弈，控辩双方团队通过迭代论证竞争以影响法官判决。其核心方法、架构设计和关键技术如下：

**整体框架与主要模块**：
框架包含三个核心组件：1) **案件环境**：结构化的输入，包含证据、摘要和法律争议点，定义了案件的事实与法律背景。2) **战略团队**：由具有不同特质的大型语言模型（LLM）智能体组成的控方和辩方团队，每个团队通常包含3个智能体，各智能体被赋予不同的可解释特质（如“定量分析”、“魅力型”等），以塑造其修辞风格和战略导向。团队采用轮转方式贡献论点，促进“涌现战略”。3) **法官**：一个中立的法官智能体，负责评估双方论证并输出结构化判决（包括有罪/无罪 verdict 和置信度分数）。整个流程遵循多轮迭代辩论协议，包括开场陈述、多轮针对每个法律争议点的论证与反驳，以及最终审议。

**关键技术细节**：
- **特质驱动的战略工程**：智能体通过9种可解释特质实例化，这些特质基于亚里士多德哲学组织为四种原型（修辞者、技术员、角斗士、外交官），分别对应情感诉求、逻辑严谨、持久对抗和实用判断等说服维度。特质通过提示词层面的行为约束实现，使智能体在论证中体现不同的修辞倾向。
- **动态世界模型与迭代论证**：每个智能体的“战略世界模型”会在提示上下文中整合对手的先前论点，形成动态的论点与反驳树，实现自适应论证。系统将环境建模为部分可观测的随机序列博弈，其中语言是主要行动空间。
- **基于强化学习的特质编排器**：作为关键创新点，论文引入一个基于强化学习（REINFORCE策略梯度）的特质编排器，该编排器（使用Qwen2.5-1.5B-Instruct模型经LoRA微调）能根据案件信息和对方团队特质动态生成辩方特质组合，甚至发明新特质。其奖励函数基于判决结果和置信度设计，旨在发现优于静态人工特质组合的战略。

**创新点**：
1. **将语言作为一等战略行动空间**：通过多轮迭代论证和特质条件化，将自然语言话语形式化为博弈中的战略行动，突破了传统博弈论抽象掉说服机制的局限。
2. **异构团队与涌现战略**：实验表明，具有互补特质的异构团队持续优于同质配置，验证了“混合人格”在说服任务中的优势，并展示了智能体间通过轮转互动产生协同战略。
3. **可学习的动态战略编排**：提出的强化学习特质编排器能够自适应地生成特质组合，显示出超越穷举搜索的绩效，为在多智能体环境中构建自适应说服的自主智能体奠定了基础。

### Q4: 论文做了哪些实验？

论文构建了名为“Strategic Courtroom Framework”的多智能体模拟环境，并进行了系统性实验。实验设置方面，研究使用基于九个可解释特质（分为四种原型）构建的LLM智能体，分别组成控方和辩方团队，在10个合成法律案例中进行多轮对抗性辩论。数据集为合成的法律案例，评估基准为模拟审判的判决结果。实验对比了不同团队配置（单一特质 vs. 多特质、同质 vs. 异质）、不同交互轮数（1、2、3轮）以及不同LLM后端（DeepSeek-R1和Gemini 2.5 Pro）的表现，总计超过7000次模拟审判。

主要结果和关键指标如下：
1.  **团队配置**：异质团队（具有互补特质）的表现持续优于同质配置。例如，两特质团队的平均Elo评分高于单一特质团队。
2.  **交互深度**：适中的交互深度（3轮）能产生更稳定的判决，其平均Elo评分最高（控方1739.2，辩方1725.3），且判决逆转率从1轮的23%降至3轮的8%。
3.  **关键特质**：“定量分析”和“富有魅力”特质对说服成功贡献最大。最佳辩方配置（团队模式、2特质、3轮、Gemini 2.5 Pro）中，“定量分析”特质取得了最高的辩方Elo评分1923.4和37.5%的胜率；最佳控方配置（单一模式、2特质、3轮、Gemini 2.5 Pro）中，“富有魅力”特质取得了最高控方Elo评分1789.4和63.8%的胜率。
4.  **模型差异**：Gemini 2.5 Pro对修辞丰富的特质更敏感，而DeepSeek-R1产生的判决最稳定且置信度高。
5.  **动态策略学习**：研究引入了基于强化学习的特质编排器，能根据案件和对手动态生成辩方特质。该编排器在62%的匹配评估中优于静态最佳配置，取得了平均辩方Elo评分1912.4和41.1%的胜率，超越了静态两特质（Elo 1885.3，胜率37.5%）和三特质（Elo 1869.1，胜率36.2%）配置。

### Q5: 有什么可以进一步探索的点？

基于论文讨论部分，未来研究可从多个维度深入探索。在框架层面，当前静态特质设定限制了策略灵活性，未来可探索动态特质切换机制，使智能体能在辩论中根据对手反应实时调整修辞风格，例如从“数据驱动”转向“道德感召”，实现更复杂的自适应说服。同时，单法官判决模型简化了现实司法中陪审团共识形成过程，引入多智能体法官面板并模拟其偏好异质性，将提升判决机制的生态效度。

在数据与评估层面，合成案例虽覆盖多元法律领域，但缺乏真实案件的复杂性与模糊性。未来需引入脱敏的真实案例数据或半合成数据，以验证框架的外部有效性。当前依赖同源LLM法官可能引入语言风格偏好偏差，需通过跨模型评估（如混合使用闭源与开源模型）或引入人类法官循环验证，以提升评估信度。

应用场景拓展方面，该框架可延伸至外交谈判、企业并购协商等对抗性话语领域，通过定制文化、利益相关者等特质维度，构建更广泛的多智能体战略交互模拟平台。此外，结合强化学习的特质编排器可进一步优化，探索基于实时对话流的动态策略生成，而非仅依赖初始条件设定。

### Q6: 总结一下论文的主要内容

该论文提出了“战略法庭框架”，这是一个用于研究对抗性法律程序中说服动态的多智能体模拟环境。核心问题是传统博弈论模型往往忽略语言作为说服机制的作用，该工作旨在将语言视为一级战略行动空间进行研究。

方法上，框架利用具有可解释特质的大型语言模型构建控辩双方智能体，这些特质分为四种原型，以系统控制修辞风格和战略导向。研究在10个合成法律案件和84种三特质团队配置中进行了超过7000次模拟审判，使用DeepSeek-R1和Gemini 2.5 Pro模型。

主要结论包括：1）具有互补特质的异质团队持续优于同质配置；2）适中的交互深度能产生更稳定的判决结果；3）某些特质（如量化分析和魅力）对说服成功贡献显著。此外，论文引入基于强化学习的特质协调器，能根据案件和对手动态生成辩护特质，其发现的策略优于静态的人工设计组合。

这项工作的意义在于为构建能在多智能体环境中进行自适应说服的自主智能体奠定了基础，并将研究范式从视语言为非结构化媒介，转向将其视为核心战略行动空间，对谈判、冲突解决等领域的后续研究具有重要价值。
