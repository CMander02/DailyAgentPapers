---
title: "EmoMAS: Emotion-Aware Multi-Agent System for High-Stakes Edge-Deployable Negotiation with Bayesian Orchestration"
authors:
  - "Yunbo Long"
  - "Yunhan Liu"
  - "Liming Xu"
date: "2026-04-08"
arxiv_id: "2604.07003"
arxiv_url: "https://arxiv.org/abs/2604.07003"
pdf_url: "https://arxiv.org/pdf/2604.07003v1"
categories:
  - "cs.AI"
tags:
  - "Multi-Agent System"
  - "Negotiation"
  - "Emotion Modeling"
  - "Bayesian Methods"
  - "Edge Computing"
  - "Benchmark"
  - "Small Language Models (SLMs)"
relevance_score: 8.0
---

# EmoMAS: Emotion-Aware Multi-Agent System for High-Stakes Edge-Deployable Negotiation with Bayesian Orchestration

## 原始摘要

Large language models (LLMs) has been widely used for automated negotiation, but their high computational cost and privacy risks limit deployment in privacy-sensitive, on-device settings such as mobile assistants or rescue robots. Small language models (SLMs) offer a viable alternative, yet struggle with the complex emotional dynamics of high-stakes negotiation. We introduces EmoMAS, a Bayesian multi-agent framework that transforms emotional decision-making from reactive to strategic. EmoMAS leverages a Bayesian orchestrator to coordinate three specialized agents: game-theoretic, reinforcement learning, and psychological coherence models. The system fuses their real-time insights to optimize emotional state transitions while continuously updating agent reliability based on negotiation feedback. This mixture-of-agents architecture enables online strategy learning without pre-training. We further introduce four high-stakes, edge-deployable negotiation benchmarks across debt, healthcare, emergency response, and educational domains. Through extensive agent-to-agent simulations across all benchmarks, both SLMs and LLMs equipped with EmoMAS consistently surpass all baseline models in negotiation performance while balancing ethical behavior. These results show that strategic emotional intelligence is also the key driver of negotiation success. By treating emotional expression as a strategic variable within a Bayesian multi-agent optimization framework, EmoMAS establishes a new paradigm for effective, private, and adaptive negotiation AI suitable for high-stakes edge deployment.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决高风险、隐私敏感的边缘设备（如移动助手或救援机器人）上部署自动谈判系统时面临的挑战。当前，大型语言模型（LLM）虽广泛用于自动谈判，但其计算成本高且存在隐私风险，难以在边缘设备本地运行。小型语言模型（SLM）虽能提供隐私保护的本地化替代方案，却受限于其情感动态处理能力不足，尤其在复杂的高风险谈判中容易受到情感操纵。现有方法，包括基于LLM的情感优化方法，通常需要大量预训练（如强化学习），这过程耗时且数据需求大；而混合代理（MoA）或混合专家（MoE）等框架虽能协调多个模型，但往往依赖静态问答，无法在持续交互中动态适应，且策略容易过拟合，难以泛化到新对手或新情境，导致每次遇到新情况都需重新训练。

因此，本文的核心问题是：如何设计一个能够在边缘设备上运行、无需预训练即可在线学习，并能动态优化情感策略以适应高风险谈判的智能谈判系统。为此，论文提出了EmoMAS框架，通过贝叶斯编排器协调三个专门代理（博弈论、强化学习和心理一致性模型），实时融合其见解并更新代理可靠性，从而将情感决策从被动反应转变为战略规划，实现隐私保护、自适应的高风险边缘谈判。

### Q2: 有哪些相关研究？

相关研究主要可分为三类：基于LLM的谈判代理、边缘部署的轻量级模型，以及多智能体协作架构。

在**基于LLM的谈判代理**方面，已有工作将大型语言模型应用于卡牌游戏、交易和债务催收等角色扮演场景，模拟谈判方。然而，这些方法通常依赖云端LLM，需在谈判中直接访问银行、医院或个人设备等敏感信息，忽视了提示信息传输带来的隐私和安全风险，且严重依赖持续网络连接，在时延和可靠性上存在不足。本文的EmoMAS则针对隐私敏感的高风险边缘场景（如移动助手、救援机器人）设计，强调离线部署与数据主权。

在**边缘部署的轻量级模型**方面，小型语言模型因低延迟、低成本及易定制性受到关注，但已知其在数学和常识推理上存在性能差距，且在谈判等社会情感互动中的情绪智能（如情感角色适应、实时策略调整）尚未被充分探索。本文工作聚焦于SLMs在这一空白领域的潜力，并通过EmoMAS框架提升其在高风险谈判中的表现。

在**多智能体协作架构**方面，混合专家（MoE）或混合智能体（MoA）方法已用于提升复杂推理任务（如数学、开放生成）的答案质量，但其通常采用静态聚合（如固定平均或投票），假设各智能体的置信度和可靠性恒定。此外，现有方法多在固定问题上通过预训练学习智能体权重，难以适应长周期、情绪动态变化的谈判场景。本文提出的EmoMAS引入贝叶斯编排器，能够根据谈判反馈实时更新各专门智能体（博弈论、强化学习、心理一致性模型）的可靠性权重，实现在线策略学习，从而将情绪决策从反应式转变为战略式。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为EmoMAS的贝叶斯多智能体系统框架来解决高风险边缘可部署谈判中复杂情感动态的挑战。其核心方法是将情感表达从被动反应转变为战略变量，通过一个混合智能体架构进行在线策略学习，无需预训练。

整体框架包含一个贝叶斯协调器和三个专门化的智能体。主要模块包括：1）博弈论智能体，采用带有情感加权的“赢则保持，输则转变”策略，基于支付矩阵优化情感选择以最大化收益；2）强化学习智能体，采用Q学习方法进行在线自适应学习，其状态定义为谈判上下文（如双方情感、谈判阶段、差距大小）的离散表示，通过Q表更新和softmax选择来学习最优情感策略；3）心理一致性智能体，利用大语言模型进行心理推理，评估每种情感在给定上下文下的 plausibility、appropriateness 和 strategic value，并输出一个评估矩阵，通过加权聚合生成选择概率。

创新点在于贝叶斯协调器的设计。它作为元推理器，动态整合三个专家智能体的概率预测。协调器为每个智能体维护一个实时更新的可靠性分布，通过贝叶斯推理进行宏微观两级更新：宏观层面基于完整谈判轨迹的收集效率更新，微观层面基于实时预测与选定情感的一致性调整。最终情感选择通过加权求和每个智能体对情感的置信度与当前可靠度得分来决定，且严格限制在智能体推荐情感的并集中选择，确保了可解释性并尊重了各智能体的专业领域。

此外，系统通过上下文学习进行情感识别，无需任务特定的微调。整个框架通过自动化多智能体模拟系统运行，包含对手、谈判者和法官三个角色，实现了在单个谈判内的实时学习和跨场景的累积改进。这种将情感决策置于贝叶斯多智能体优化框架中的范式，使得系统能够在保护隐私的边缘设备上实现有效、自适应的高风险谈判。

### Q4: 论文做了哪些实验？

论文实验主要包括四部分。实验设置上，研究者构建了一个贝叶斯多智能体框架（EmoMAS），包含博弈论、强化学习和心理一致性三个专门代理，并由贝叶斯协调器进行实时协调与可靠性更新。系统在四个高风险、可边缘部署的谈判基准数据集上进行评估：债务谈判的CRAD、医疗手术调度的SSD、紧急救援的DESRD以及教育场景的SSAD。对比方法涵盖了五种基线系统：无情感指导的单一智能体、提示引导情感策略的智能体、基于博弈论的智能体、在线强化学习智能体、心理一致性智能体，以及两种混合智能体系统（EmoMAS-LLM和EmoMAS-Bayes）。对手策略则包括基础情感基线及三种高级策略（施压战术、扮演受害者和威胁策略）。

主要结果方面，EmoMAS在多个指标上表现优异。在基础对手策略下，EmoMAS-Bayes在多个场景中取得了最高的成功率（例如在CRAD债务场景中，使用Qwen-7B时成功率达90%），并在谈判结果（如SSD医疗场景中，使用GPT-4o-mini时谈判结果达86.4%）和谈判轮次上取得平衡。关键数据指标包括成功率（%）、谈判结果（%）和谈判轮次（数值越低越好）。在面对高级对手策略的鲁棒性测试中，EmoMAS-Bayes在施压、扮演受害者和威胁策略下均保持了最高的成功率（例如在医疗场景面对施压策略时成功率为50%）和谈判结果。模型规模分析表明，即使使用小型语言模型（如Qwen-1.5B），EmoMAS也能保持有效性能，在SLM对SLM的紧急场景交互中，EmoMAS-LLM和EmoMAS-Bayes均表现出色（如EmoMAS-Bayes对Qwen-1.5B对手成功率高达100%）。行为评估还显示，EmoMAS在情感一致性、遵循指令准确性和操纵行为率等伦理维度上优于单一智能体基线，实现了性能与伦理的较好平衡。

### Q5: 有什么可以进一步探索的点？

论文的局限性为未来研究提供了明确方向。首先，系统可解释性有待提升，贝叶斯编排器虽能动态加权各智能体输出，但情感状态转换的具体逻辑及其对谈判成功的直接影响仍部分处于“黑箱”状态，未来可探索更具透明度的决策路径可视化或引入可解释AI技术。其次，情感建模粒度较粗，当前七种离散情感状态难以捕捉真实谈判中微妙或混合的情感表达，未来可探索连续情感空间建模或引入多模态信号（如语音语调、面部表情）以更细腻地感知和生成情感。再者，文化普适性尚未验证，实验仅基于英语语境，而情感表达与谈判策略存在显著文化差异，未来需在跨文化谈判基准上进行测试，并可能引入文化适配模块。最后，实际部署经验缺失，系统仅在智能体间模拟环境中测试，未来需在真实高风险边缘场景中与人类进行交互验证，并解决实时性、隐私保护与计算资源约束等实际挑战。此外，论文提及但未深入探索的具身多智能体、多模态谈判等方向，也为情感智能在更复杂环境中的应用开辟了道路。

### Q6: 总结一下论文的主要内容

论文针对高风险边缘部署场景下的自动谈判问题，提出了一种情感感知的多智能体系统EmoMAS。核心问题是现有小型语言模型在复杂情感动态谈判中能力不足，而大型语言模型则存在计算成本高和隐私风险。EmoMAS的核心贡献在于将情感决策从被动反应转变为主动战略，通过一个贝叶斯编排器协调三个专门智能体（博弈论、强化学习和心理一致性模型），实时融合其见解以优化情感状态转换，并基于谈判反馈持续更新各智能体的可靠性。该方法无需预训练即可实现在线策略学习。论文还构建了债务、医疗、应急响应和教育四个高风险领域的边缘可部署谈判基准。实验表明，配备EmoMAS的模型在谈判性能和伦理行为平衡上均超越基线模型，证实了战略情商是谈判成功的关键驱动因素。这为高效、私密且自适应的边缘AI谈判建立了新范式。
