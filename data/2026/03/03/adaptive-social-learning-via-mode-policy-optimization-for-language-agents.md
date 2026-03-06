---
title: "Adaptive Social Learning via Mode Policy Optimization for Language Agents"
authors:
  - "Minzheng Wang"
  - "Yongbin Li"
  - "Haobo Wang"
  - "Xinghua Zhang"
  - "Nan Xu"
  - "Bingli Wu"
  - "Fei Huang"
  - "Haiyang Yu"
  - "Wenji Mao"
date: "2025-05-04"
arxiv_id: "2505.02156"
arxiv_url: "https://arxiv.org/abs/2505.02156"
pdf_url: "https://arxiv.org/pdf/2505.02156v5"
github_url: "https://github.com/MozerWang/AMPO"
categories:
  - "cs.CL"
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent Architecture"
  - "Reasoning"
  - "Planning"
  - "Multi-Agent Systems"
  - "Social Intelligence"
  - "Adaptive Learning"
  - "Policy Optimization"
relevance_score: 9.0
---

# Adaptive Social Learning via Mode Policy Optimization for Language Agents

## 原始摘要

Effective social intelligence simulation requires language agents to dynamically adjust reasoning depth, a capability notably absent in current studies. Existing methods either lack explicit reasoning or employ lengthy Chain-of-Thought reasoning uniformly across all scenarios, resulting in excessive token usage and inflexible social behaviors in tasks such as negotiation or collaboration. To address this, we propose an $\textbf{A}$daptive $\textbf{S}$ocial $\textbf{L}$earning ($\textbf{ASL}$) framework in this paper, aiming to improve the adaptive reasoning ability of language agents in dynamic social interactions. To this end, we first identify the hierarchical reasoning modes under such context, ranging from intuitive response to deep deliberation based on the cognitive control theory. We then develop the $\textbf{A}$daptive $\textbf{M}$ode $\textbf{P}$olicy $\textbf{O}$ptimization ($\textbf{AMPO}$) algorithm to learn the context-aware mode adaptation and reasoning. Our framework advances existing research in three key aspects: (1) Multi-granular reasoning mode design, (2) Context-aware mode switching in rich social interaction, and (3) Token-efficient reasoning with depth adaptation. Extensive experiments on the benchmark social intelligence environment verify that ASL achieves 15.6% higher task performance than GPT-4o. Notably, our AMPO outperforms GRPO by 7.0% with 32.8% shorter thinking chains, demonstrating the advantages of our AMPO and the learned adaptive reasoning ability over GRPO's solution.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在动态、开放式社会交互场景中缺乏自适应推理能力的问题。研究背景是，尽管LLM在数学、代码等规则明确的静态领域展现出卓越的推理能力，但在涉及利益冲突、谈判协作等复杂社会互动中，其表现仍存在明显不足。现有方法主要有两种：一是端到端的目标导向训练，侧重于快速响应但缺乏显式的深度思考过程；二是集成外部规划模块，但这些方法通常采用统一的、冗长的思维链（Chain-of-Thought）推理模式，无论场景复杂度如何都进行深度推理。这导致了两大缺陷：一是令牌（token）使用效率低下，造成不必要的计算开销；二是社会行为僵化，无法灵活适应动态交互情境中瞬息万变的细微线索和长期目标。因此，本文的核心问题是：如何让基于LLM的语言智能体具备**根据社交情境动态自适应调整推理深度**的能力，从而在保证任务性能的同时，实现高效、灵活的社会智能模拟。为此，论文提出了自适应社交学习框架（ASL）及其核心算法——自适应模式策略优化（AMPO），旨在通过分层推理模式设计和上下文感知的模式切换机制，从根本上提升语言智能体在复杂社会互动中的适应性和推理效率。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类，围绕语言智能体的社会智能模拟展开。

在方法类研究中，现有工作主要遵循两条路径：一是端到端的面向目标训练，通过监督学习对LLM进行后训练；二是外部规划集成，为智能体添加即插即用的规划模块。这些方法大多属于“快速推理”范式，缺乏显式的深度思考过程。此外，虽然长思维链（Long-CoT）在数学、代码等静态领域被证明有效，但现有的大型推理模型（如OpenAI-o1、DeepSeek-R1）通常无论输入复杂度如何都进行穷举式推理，未能适应动态社交环境。

在应用类研究中，当前工作主要关注智能体在谈判、协作等社会互动任务中的行为模拟，但普遍存在推理深度僵化的问题——要么缺乏显式推理，要么在所有场景中统一采用冗长的思维链，导致令牌使用效率低下和社交行为不灵活。

本文提出的ASL框架与上述工作的关系和区别在于：1）它首次将层次化的推理模式（从直觉响应到深度思考）引入社会智能任务，超越了单一推理深度的设计；2）它通过AMPO算法实现了上下文感知的推理模式切换，与静态或穷举式推理方法形成鲜明对比；3）它强调在动态社交互动中学习自适应推理能力，通过强化学习优化令牌使用效率，这是对现有训练范式的显著推进。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为自适应社交学习（ASL）的框架来解决语言代理在动态社交互动中缺乏自适应推理能力的问题。该框架的核心是自适应模式策略优化（AMPO）算法，旨在让代理能够根据具体情境动态选择和调整其推理深度。

整体框架将社交智能任务建模为两个角色扮演代理之间的顺序对话交互，形式化为部分可观测马尔可夫决策过程（POMDP）。框架包含三个关键步骤：首先，基于分层认知控制理论（HCCT）设计了四种层次化的推理模式（Mode），从直觉响应到深度前瞻推演，每种模式对应不同的认知抽象层级和结构化推理动作序列。其次，通过模式行为克隆（Behavioral Cloning）对大型语言模型进行微调，使其能够准确遵循预定义的推理模式格式，为后续强化学习奠定基础。最后，也是最具创新性的部分，提出了AMPO算法进行自适应模式策略优化。

AMPO算法的核心创新在于引入了双层级优势估计，以克服现有方法（如GRPO）的“模式盲”问题。它包含两个关键组件：模式级优势（Mode-Level Advantage）和样本级优势（Sample-Level Advantage）。模式级优势通过比较不同模式在特定情境下的平均奖励和平均响应长度，引导模型在性能相近时选择更高效的推理模式，从而在任务表现和计算效率之间取得平衡。样本级优势则在选定模式内部，鼓励模型生成优于同组平均水平的推理轨迹，以优化具体内容生成。这两种优势被整合到一个PPO风格的优化目标函数中，共同指导模型学习动态、自适应的推理策略。

此外，论文还设计了精细的奖励函数，包含答案质量奖励、格式合规性奖励和答案长度奖励，以稳定训练并鼓励简洁有效的输出。通过这种架构，ASL框架实现了多粒度推理模式设计、丰富社交互动中的情境感知模式切换以及具有深度自适应的令牌高效推理，最终使代理能够根据社交情境的复杂性灵活调整其推理过程。

### Q4: 论文做了哪些实验？

论文在SOTOPIA和SOTOPIA-Hard两个基准测试环境中进行了广泛的实验，以评估所提出的自适应社交学习（ASL）框架及其核心算法AMPO的有效性。

**实验设置与数据集**：实验在SOTOPIA（面向目标的社交互动）和SOTOPIA-Hard（复杂战略推理任务）两个基准上进行。评估采用两种交互设置：智能体自我博弈（Self-Play）以及与GPT-4o作为伙伴交互（GPT-4o-as-Partner）。社交能力通过七个维度评估，其中核心指标是GOAL（0-10分，衡量目标达成度）和OVERALL（七个维度的平均分）。使用GPT-4o作为评估代理，其温度设为0以确保稳定性，而智能体温度设为0.7以鼓励响应多样性。

**对比方法**：实验对比了四大类基线模型：
1.  **专有大型语言模型**：如GPT-4o、Claude-3.5-Sonnet、DeepSeek-V3。
2.  **大型推理模型**：如OpenAI-o1、Gemini-2.5-Pro、DeepSeek-R1、QwQ-32B。
3.  **社交智能方法**：包括PPDPP、EPO、DAT、DSI等利用策略规划或注入的方法。
4.  **ASL框架变体**：包括行为克隆微调（BC）以及在ASL框架内使用GRPO进行强化学习（作为AMPO的主要对比对象）。

**主要结果与关键指标**：
1.  **整体性能**：在Llama骨干网络上，ASL框架（BC+AMPO）在SOTOPIA-Hard的GOAL指标上达到8.06分，比GPT-4o（6.97分）**提升15.6%**，在所有设置中达到SOTA性能。
2.  **与GRPO对比**：AMPO在实现更优性能的同时，显著缩短了推理链长度。以Llama骨干为例，AMPO平均每轮使用581个令牌，仅为GRPO（865个令牌）的**67.2%**，同时在SOTOPIA-Hard的OVERALL指标上以3.68分超越GRPO的3.44分，**提升7.0%**。这证明了AMPO在自适应推理和令牌效率上的优势。
3.  **消融研究**：
    *   **答案长度奖励**：移除该奖励（\(r^l\)）会导致响应长度大幅增加（例如从647令牌增至1617令牌），但目标分数下降（7.85→7.46），证实了简洁推理的有效性。
    *   **单一推理模式**：仅使用最深模式\(\mathcal{M}_4\)性能最佳但令牌消耗高（972令牌），而AMPO混合模式仅用647令牌即达到更优性能，凸显了自适应模式选择的必要性。
    *   **混合模式有效性**：在GRPO中使用显式设计的四种混合模式，相比无模式推理，在困难场景下OVERALL性能提升**8.0%**（3.16→3.41）。
4.  **自适应行为分析**：分析显示，AMPO能根据交互轮次和上下文动态调整推理模式。复杂模式（如\(\mathcal{M}_4\)）在早期和目标未达成时占主导，而简单模式（如\(\mathcal{M}_1\)）在后期或目标已达成时更频繁，验证了其上下文感知的深度适应能力。

### Q5: 有什么可以进一步探索的点？

本文提出的ASL框架在提升语言智能体社会交互适应性方面取得了显著进展，但其仍有进一步探索的空间。局限性在于：首先，其推理模式划分和切换策略主要基于认知控制理论，可能未完全覆盖复杂社会情境中更细微的认知状态（如情感影响下的直觉偏差）；其次，实验环境虽为基准测试，但与现实世界开放域、多轮次的社会动态相比仍显简化，泛化能力有待验证；此外，模式策略优化（AMPO）依赖于特定交互数据训练，在不同领域或文化背景的迁移上可能存在挑战。

未来研究方向可包括：1）**认知架构的扩展**，引入情感计算或元认知模块，使智能体不仅能调整推理深度，还能评估自身推理过程的可靠性；2）**多模态社会学习**，结合视觉、语音等线索，更全面地理解社交语境，实现更精准的模式切换；3）**轻量化与实时性优化**，在边缘设备上部署自适应推理机制，降低延迟；4）**跨领域泛化研究**，通过元学习或课程学习让智能体快速适应新社交场景。这些方向有望推动语言智能体从“适应已知”迈向“应对未知”的社会智能。

### Q6: 总结一下论文的主要内容

本文针对语言智能体在模拟社会智能时缺乏动态调整推理深度能力的问题，提出了一种自适应社会学习（ASL）框架。现有方法要么缺乏显式推理，要么在所有场景中统一采用冗长的思维链推理，导致在谈判或协作等任务中产生过高的计算开销和僵化的社会行为。

ASL框架的核心贡献是引入了自适应模式策略优化（AMPO）算法。该方法首先基于认知控制理论，定义了从直觉反应到深度思考的层次化推理模式。AMPO算法则通过学习上下文感知的模式切换策略，使智能体能够根据不同的社会互动情境，自适应地选择合适的推理深度进行决策。

实验结果表明，该框架在基准社会智能环境中取得了显著优于现有方法的表现：其任务性能比GPT-4o高出15.6%；其AMPO算法在比GRPO缩短32.8%思维链长度的同时，性能还提升了7.0%。这验证了该方法在实现高效、灵活的社会推理方面的有效性和优越性。
