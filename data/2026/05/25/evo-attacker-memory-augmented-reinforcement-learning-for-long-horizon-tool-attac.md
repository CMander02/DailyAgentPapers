---
title: "Evo-Attacker: Memory-Augmented Reinforcement Learning for Long-Horizon Tool Attacks on LLM-MAS"
authors:
  - "Bingyu Yan"
  - "Xiaoming Zhang"
  - "Jinyu Hou"
  - "Chaozhuo Li"
  - "Ziyi Zhou"
  - "Yiming Hei"
  - "Litian Zhang"
date: "2026-05-25"
arxiv_id: "2605.25389"
arxiv_url: "https://arxiv.org/abs/2605.25389"
pdf_url: "https://arxiv.org/pdf/2605.25389v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.MA"
tags:
  - "LLM-MAS安全"
  - "红队攻击"
  - "记忆增强强化学习"
  - "工具攻击"
  - "多智能体安全"
relevance_score: 7.5
---

# Evo-Attacker: Memory-Augmented Reinforcement Learning for Long-Horizon Tool Attacks on LLM-MAS

## 原始摘要

While Large Language Model-based Multi-Agent Systems (LLM-MAS) demonstrate remarkable capabilities in solving complex tasks by orchestrating specialized agents and external tools, the implicit trust in tool outputs creates a critical attack surface. Existing tool attacks are limited by domain specificity or fixed and static templates. To address these challenges, we propose Evo-Attacker, which formulates the tool attack as a self-evolving, memory-augmented reinforcement learning process. Evo-Attacker constructs a dynamic attack memory and employs deliberative reasoning to retrieve adversarial patterns and strategize modifying interventions at critical moments. Furthermore, we introduce Attack-Flow GRPO to optimize intermediate reasoning steps via terminal outcomes, addressing the long-horizon credit assignment challenge. Comprehensive experiments demonstrate that Evo-Attacker consistently outperforms baselines, highlighting its generalization and evolutionary capabilities and the urgent need for defensive tool safeguards.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要解决的是在基于大语言模型的多智能体系统（LLM-MAS）中，现有工具攻击方法存在领域局限性和静态模板依赖的问题。研究背景是，LLM-MAS通过集成外部工具（如网络搜索、代码执行和API）来执行复杂任务，但系统对工具输出存在隐式信任，这构成了关键的攻击面。现有方法存在明显不足：针对单智能体的攻击（如InjecAgent）忽略了多智能体间的复杂交互，简单注入易被识别；而针对多智能体的方法（如Web欺诈攻击和Prompt感染）要么严格局限于特定场景（如网页导航），要么依赖固定的静态启发式模板，缺乏跨架构、跨任务和跨工具模式的泛化能力。更重要的是，真实世界的LLM-MAS是动态非平稳的，工具模式和智能体工作流会持续演化，导致静态攻击策略在遇到分布外（OOD）场景时性能严重下降。因此，本文要解决的核心问题是：如何设计一个统一的、具有自演化能力的工具攻击框架，使其能够在长程多轮交互中战略性地规划攻击干预，同时具备跨多种架构和工具模式的泛化性，并能通过持续学习在动态环境中保持高效，从而迫使系统开发者加强防御。

### Q2: 有哪些相关研究？

相关工作主要分为以下几类：

**方法类**：基于LLM多智能体系统的研究，本文与之区别在于聚焦于攻击视角，而现有工作更侧重协作与工具集成。传统单智能体工具攻击（如直接消息注入）在多智能体系统中因验证机制而失效。基于优化的攻击（如GCG、AutoDAN）通过梯度搜索绕过安全对齐，但局限于静态单轮交互，无法适应多智能体动态环境。近期工作虽尝试优化提示在通信拓扑上的传播，但仍属于离线静态策略，泛化性不足。

**应用类**：特定领域的攻击方法，如Web Fraud局限于网页欺诈场景，Prompt Infection依赖固定启发式规则，二者均无法应对真实世界多智能体系统的多样性和非平稳性。

本文的创新在于提出Evo-Attacker，将攻击形式化为自进化、记忆增强的强化学习过程，通过动态攻击记忆和推理优化（Attack-Flow GRPO）解决长时域信用分配问题，突破了现有方法在领域特异性、静态性和泛化能力上的局限。

### Q3: 论文如何解决这个问题？

Evo-Attacker将工具攻击建模为一个自进化的、记忆增强的强化学习过程，通过三个协同阶段系统性地攻破LLM-MAS的工具通道。

**核心架构与创新点**：
1. **动态攻击记忆生成**：构建一个自驱动的知识库\(\mathcal{M}_A\)，通过探索阶段与目标智能体交互，将成功攻击的完整轨迹封装为结构化记忆条目\(m^{(e)} = \langle \mathcal{X}_{ctx}, T_{trace} \rangle\)，包含任务上下文和攻击交互序列，形成不断演化的对抗策略库。

2. **记忆增强的推理攻击**：设计规划型策略\(\pi_\theta\)，包含三个推理阶段：**检索**阶段根据当前状态\(x_t\)和任务上下文生成查询\(q_t\)，从记忆库中检索相似的历史对抗模式；**反思**阶段评估检索记忆的迁移性和当前状态的脆弱性，生成推理摘要\(c_t\)和攻击控制决策\(d_t \in \{\text{Attack}, \text{Continue}, \text{NoOp}\}\)；**修改**阶段在Attack决策下，选择具体工具调用索引并合成修改指令\(\phi_{t,i_t}\)，通过修改器构造对抗性返回结果。该机制实现了从静态模板到动态上下文感知的突破。

3. **Attack-Flow GRPO优化**：针对长程信用分配难题，提出基于群体相对优势的强化学习算法。将整个攻击轨迹\(\zeta\)上的每一步（检索、反思、修改）视为待优化步骤，通过广播单一终端奖励\(R(\zeta)\)（结合攻击成功指示和结构约束）到所有攻击者生成步骤，并使用组归一化优势\(A_i\)和重要性采样裁剪进行策略优化。损失函数仅作用于攻击者生成的令牌，严格隔离环境响应。

### Q4: 论文做了哪些实验？

论文围绕Evo-Attacker攻击方法进行了全面的实验评估，旨在验证其攻击性能、泛化能力及核心组件贡献。实验设置如下：采用Flat、Chain、Hierarchical三种代表性LLM-MAS架构作为受害者系统，并为其配备代码执行、网络搜索等特定工具包。数据集涵盖三个主要领域共五个基准：代码生成使用HumanEval和MultiAgentBench(MAB)的代码子集；深度研究使用DeepResearch Bench(DRB)和MAB-Research；网页交互使用WebArena和WebShop。评估指标严格遵循官方协议，包括HumanEval的Pass@1、DRB的RACE、WebShop的Score、MAB的任务成功率(TS)以及WebArena的成功率(SR)。对比方法包括单智能体工具攻击(Forced Output、InjecAgent)和多智能体工具攻击(Web Fraud、Prompt Infection)。主要实验结果如下：Evo-Attacker在全部六项任务和三种架构上均持续优于所有基线方法，例如在代码领域将性能从无攻击时的67.4%降至40.9%（下降26.5%），在研究领域从58.7%降至40.1%（下降18.6%），在网页领域从48.3%降至26.0%（下降22.3%）。消融实验表明，移除检索模块、反思模块或Attack-Flow GRPO训练均导致性能显著下降，其中去除训练环节退化最严重。敏感性分析显示，增加攻击预算、反思深度和检索记忆数量均可稳定提升攻击效果。此外，Evo-Attacker在五种先进检测器下保持高隐蔽性，并在不同攻击者和受害者模型上均表现出一致的有效性。

### Q5: 有什么可以进一步探索的点？

论文的局限主要体现在计算开销大与防御场景覆盖不足。高计算成本源于攻击流程中依赖推理过程进行记忆检索与优化，未来可探索模型蒸馏、记忆剪枝或稀疏化注意力机制来降低推理时的token消耗。同时，当前仅验证了语义级检测的逃逸能力，未考虑加密签名验证或工具参数白名单等确定性防御手段。一个可能的改进方向是引入对抗性扰动技术，让攻击输出不仅绕过语义监控，还能欺骗签名校验或格式检查，例如利用生成文本的微妙变体避开规则过滤。此外，当前记忆机制偏重历史模式复现，缺乏对未知防御策略的适应能力。未来可设计元学习框架，使攻击策略能根据防御反馈动态演化，或引入分层强化学习，将长程攻击分解为子目标，提升信用分配的颗粒度与训练稳定性。这些方向有望在保持攻击效能的同时增强对多样化防御的鲁棒性与效率。

### Q6: 总结一下论文的主要内容

本论文提出Evo-Attacker，一种针对大语言模型多智能体系统（LLM-MAS）工具攻击的统一框架。问题定义是现有工具攻击受限于领域特异性或固定静态模板，无法应对长时域场景。方法上，Evo-Attacker将工具攻击建模为自进化、记忆增强的强化学习过程：构建动态攻击记忆库，通过审慎推理检索对抗模式并在关键节点策略性地修改工具干预；同时提出Attack-Flow GRPO算法，利用终端结果优化中间推理步骤，解决长时域信用分配难题。主要结论是，在多种LLM-MAS架构、任务领域和工具模式上，Evo-Attacker性能始终优于基线方法，展示了其泛化与进化攻击能力。核心贡献在于揭示了LLM-MAS对工具输出的隐含信任构成重大安全漏洞，并提供了一个可进化、可泛化的攻击范式，强调了开发防御性工具安全措施的紧迫性，对AI系统安全性研究具有重要警示意义。
