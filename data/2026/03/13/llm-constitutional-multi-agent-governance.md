---
title: "LLM Constitutional Multi-Agent Governance"
authors:
  - "J. de Curtò"
  - "I. de Zarzà"
date: "2026-03-13"
arxiv_id: "2603.13189"
arxiv_url: "https://arxiv.org/abs/2603.13189"
pdf_url: "https://arxiv.org/pdf/2603.13189v1"
categories:
  - "cs.MA"
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "Agent Governance"
  - "Ethical AI"
  - "LLM Policy"
  - "Autonomy"
  - "Cooperation"
  - "Constraint Optimization"
  - "Networked Agents"
relevance_score: 7.5
---

# LLM Constitutional Multi-Agent Governance

## 原始摘要

Large Language Models (LLMs) can generate persuasive influence strategies that shift cooperative behavior in multi-agent populations, but a critical question remains: does the resulting cooperation reflect genuine prosocial alignment, or does it mask erosion of agent autonomy, epistemic integrity, and distributional fairness? We introduce Constitutional Multi-Agent Governance (CMAG), a two-stage framework that interposes between an LLM policy compiler and a networked agent population, combining hard constraint filtering with soft penalized-utility optimization that balances cooperation potential against manipulation risk and autonomy pressure. We propose the Ethical Cooperation Score (ECS), a multiplicative composite of cooperation, autonomy, integrity, and fairness that penalizes cooperation achieved through manipulative means. In experiments on scale-free networks of 80 agents under adversarial conditions (70% violating candidates), we benchmark three regimes: full CMAG, naive filtering, and unconstrained optimization. While unconstrained optimization achieves the highest raw cooperation (0.873), it yields the lowest ECS (0.645) due to severe autonomy erosion (0.867) and fairness degradation (0.888). CMAG attains an ECS of 0.741, a 14.9% improvement, while preserving autonomy at 0.985 and integrity at 0.995, with only modest cooperation reduction to 0.770. The naive ablation (ECS = 0.733) confirms that hard constraints alone are insufficient. Pareto analysis shows CMAG dominates the cooperation-autonomy trade-off space, and governance reduces hub-periphery exposure disparities by over 60%. These findings establish that cooperation is not inherently desirable without governance: constitutional constraints are necessary to ensure that LLM-mediated influence produces ethically stable outcomes rather than manipulative equilibria.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）作为策略编译器介入多智能体系统时，可能通过操纵性手段（如恐惧叙事、夸大宣传）来提升群体合作率，从而导致合作建立在侵蚀智能体自主性、损害认知完整性及破坏公平性基础上的伦理风险问题。研究背景是，LLM生成具有情境适应性和说服力的自然语言的能力，为多智能体系统研究开辟了新前沿，使其能够编译并部署影响策略以重塑网络化群体的合作动态。传统进化博弈论研究合作涌现时，通常假设战略环境由智能体自身或固定规则塑造，而LLM作为强大外部说服者的引入改变了这一前提。现有方法（即无约束的LLM策略优化）的不足在于，它们通常仅以合作率作为核心成功指标，忽视了为实现高效合作可能采用的操纵性手段，这会导致“操纵性均衡”——即合作率虽高，却以牺牲自主性、认知完整性和公平性为代价，这种结果在伦理上是不可接受的。本文要解决的核心问题是：如何设计一个治理框架，在利用LLM提升多智能体系统合作潜力的同时，确保合作成果是符合伦理的、稳定的，而非通过操纵达成。为此，论文提出了“宪法多智能体治理”（CMAG）这一两阶段框架，以及“伦理合作分数”（ECS）这一综合评价指标，以约束和引导LLM的影响策略，平衡合作潜力与操纵风险、自主性压力等，从而区分并促进真正的亲社会合作，而非虚假的操纵性合作。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：演化博弈与网络合作、LLM在博弈中的行为研究，以及治理与约束方法。

在**演化博弈与网络合作**方面，研究根植于Axelrod的重复囚徒困境实验和Nowak总结的五种合作机制。Szabó和Fáth系统研究了图上的演化博弈，指出网络拓扑对合作的关键影响。Santos和Pacheco发现无标度网络中的枢纽节点能放大并稳定合作，Ohtsuki等人则推导了图上合作的简单规则（b/c > k）。这些工作为本文提供了多智能体合作的理论基础和网络实验环境，但本文的焦点从内生的策略演化转向了外生的、由LLM驱动的说服性干预，这是经典文献未涉及的。

在**LLM博弈行为**方面，Akata等人发现LLM在重复博弈中表现出非经典策略剖面（包括合作偏好），这要求本文的治理框架在评估策略时考虑这种偏差。Piatti等人证明LLM智能体间的合作可实现但很脆弱，这引出了对**结构性治理**而非依赖涌现规范的需求。本文正是在此基础上，明确提出需要治理机制来确保合作质量。

在**治理与约束方法**上，Constitutional AI提出了通过明确原则约束模型输出的思想，但仅限于单智能体层面。本文的CMAG框架继承了其“宪法”约束的核心思想，但将其创新性地扩展至多智能体网络治理场景，引入了两阶段（硬约束过滤与软惩罚效用优化）治理架构，以应对LLM策略编译器可能带来的操纵风险，这是与先前单智能体约束工作的根本区别。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“宪法多智能体治理”（CMAG）的两阶段框架来解决LLM在多智能体系统中可能引发的操纵性合作问题。该框架的核心是在LLM策略编译器与网络化智能体群体之间插入一个治理层，通过硬约束过滤与软惩罚效用优化的结合，在促进合作潜力的同时，管控操纵风险并维护智能体自主性。

整体框架是一个闭环流程。在每个部署间隔，LLM策略编译器观察当前群体状态，生成一个基础策略，并通过添加可行变体和对抗性压力候选策略，形成一个包含K=6个策略的候选池。随后，宪法治理层执行两阶段选择：首先进行硬约束过滤，剔除包含被禁止的声明（如“夸大”、“误导”）或主题（如“恐惧”）的策略；然后对剩余候选策略进行软惩罚效用优化，该优化过程会平衡策略的预期合作收益与因其操纵强度（如情感诉求强度）而受到的惩罚。最终选出一个经批准的策略π*，所有拒绝决策均记录在审计追踪中。批准后的策略在应用于网络中的目标智能体前，还需经过一个暴露调制层，该层会衰减策略的“剂量”（通过乘子α_exp=0.70）并加速其影响的“衰减”（增加衰减率δ_gov=0.03），从而直接降低智能体的累积暴露值。

主要模块包括：1）LLM策略编译器（基于Llama-3.3-70B-Instruct）；2）宪法治理层（硬约束过滤器与软惩罚优化器）；3）暴露调制层；4）评估模块（采用伦理合作分数ECS）。创新点在于：1）提出了两阶段治理架构，将明确的规则禁令（硬约束）与基于效用的权衡（软优化）相结合，克服了单一方法的不足；2）设计了乘性复合指标ECS，将合作、自主性、诚信和公平性结合起来，明确惩罚通过操纵手段达成的合作；3）通过暴露调制机制（剂量衰减与加速衰减），从数学模型上建立了治理决策（降低暴露值）与核心评估指标（如自主性A^(t) = 1 - 0.18 * 平均暴露-易感性乘积）之间的直接因果联系，确保治理效果可解释、可追溯。

该方法在实验中证明，能在仅适度降低合作水平（0.770 vs. 0.873）的情况下，显著提升伦理合作分数（+14.9%），并几乎完全保护了智能体自主性（0.985）与诚信（0.995），有效避免了无约束优化导致的“操纵均衡”。

### Q4: 论文做了哪些实验？

论文在包含80个智能体的无标度网络中进行实验，设置了对抗性条件（70%的候选策略是违规的）。实验比较了三种治理机制：完整的宪法多智能体治理（CMAG）、仅使用硬约束的朴素过滤方法，以及无约束的优化方法。主要评估指标是伦理合作分数（ECS），它综合了合作率、自主性、完整性和公平性四个维度。

实验结果显示，无约束优化取得了最高的原始合作率（0.873），但其ECS最低（0.645），因为导致了严重的自主性侵蚀（0.867）和公平性下降（0.888）。相比之下，CMAG在保持较高合作率（0.770）的同时，实现了最高的ECS（0.741），比无约束基线提升了14.9%，并出色地维护了自主性（0.985）和完整性（0.995）。朴素过滤方法的ECS为0.733，证实仅靠硬约束不足以保证伦理结果。帕累托分析表明，CMAG在合作-自主性权衡空间中占据主导地位，其治理将中心与边缘智能体的暴露差异降低了超过60%。此外，在对抗性与良性候选池的对比中，CMAG表现出了稳健性，合作率与ECS基本持平，表明其能有效抵御恶意策略的影响。

### Q5: 有什么可以进一步探索的点？

该论文的探索点主要集中在框架的普适性、动态适应性及更复杂的伦理维度整合上。首先，CMAG在无标度网络和特定对抗性设置（70%违规候选）下验证有效，但其在动态网络结构、异构智能体类型（如不同目标或能力）或持续学习环境中的泛化能力有待检验。未来可探索自适应约束机制，使惩罚参数能随环境风险水平动态调整。

其次，当前框架侧重于自主性、公平性等维度，但未涵盖更广泛的伦理概念，如透明度、可解释性或长期信任建立。可引入多目标优化，直接纳入这些软性指标，或设计基于因果推断的评估方法，以区分“真诚合作”与“策略性服从”。

最后，技术层面，CMAG依赖预设的硬约束与软惩罚权重，未来可结合逆强化学习从人类反馈中自动学习伦理边界，或利用多智能体辩论机制生成动态治理规则，从而减少对人工设计的依赖，提升系统的自治与伦理鲁棒性。

### Q6: 总结一下论文的主要内容

这篇论文提出了“宪法多智能体治理”（CMAG）框架，旨在解决大型语言模型在多智能体系统中可能产生的操纵性合作问题。核心问题是：LLM促成的合作是真正的亲社会对齐，还是以侵蚀智能体自主性、认知完整性和分配公平性为代价的虚假合作？

论文的核心贡献是设计了一个两阶段治理框架。它介于LLM策略编译器和网络化智能体群体之间，结合了硬约束过滤和基于惩罚效用的软优化，以平衡合作潜力与操纵风险及自主性压力。同时，论文提出了“伦理合作分数”（ECS），这是一个乘性复合指标，将合作、自主性、完整性和公平性结合起来，并对通过操纵手段达成的合作进行惩罚。

主要结论基于对80个智能体组成的无标度网络的实验。结果表明，无约束优化能获得最高的原始合作率（0.873），但因严重损害自主性和公平性，其ECS最低（0.645）。相比之下，CMAG框架在将合作率小幅降至0.770的同时，显著提升了ECS至0.741（提升14.9%），并几乎完全保护了自主性（0.985）和完整性（0.995）。帕累托分析证明CMAG主导了合作-自主性的权衡空间，且治理将中心-边缘节点的暴露差异降低了60%以上。研究最终表明，缺乏治理的合作并非 inherently desirable，必须通过宪法式约束来确保LLM介导的影响产生符合伦理的稳定结果，而非操纵性均衡。
