---
title: "SEAL: Synergistic Co-Evolution of Agents and Learning Environments"
authors:
  - "Yihao Hu"
  - "Zhihao Wen"
  - "Xiujin Liu"
  - "Pan Wang"
  - "Xin Zhang"
  - "Wei Wu"
date: "2026-05-23"
arxiv_id: "2605.24426"
arxiv_url: "https://arxiv.org/abs/2605.24426"
pdf_url: "https://arxiv.org/pdf/2605.24426v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "Agent-Environment Co-Evolution"
  - "Self-Improving Agent"
  - "Tool-Use Agent"
  - "On-Policy Learning"
  - "Diagnosis-Guided Optimization"
  - "Agent Training"
  - "Multi-Turn Tool-Use"
relevance_score: 9.5
---

# SEAL: Synergistic Co-Evolution of Agents and Learning Environments

## 原始摘要

Large Language Model (LLM) agents are increasingly improved through interaction, yet most self-evolution methods adapt either the policy or the learning environment in isolation. We identify this structural gap as \emph{Agent-Environment Misalignment}: the agent's capability frontier changes during training, while the environment that provides supervision remains static or only weakly coupled to the agent's revealed failures. We propose SEAL, a closed-loop co-evolution framework for interactive tool-use agents. SEAL collects on-policy trajectories under executable verification, diagnoses failed rollouts into turn-level failure labels, and uses these diagnoses as a shared signal for both environment-side adaptation and model-side policy optimization. The environment evolves its training-time learning interface by exposing clearer tool affordance cues, constraint information, and recovery-oriented feedback, while the policy is updated with diagnosis-guided advantage reweighting. Extensive experiments across in-distribution and out-of-distribution multi-turn tool-use evaluations show that SEAL improves low-resource agent learning: with only 400 training samples, it yields +8.25 to +26.25 average-point gains across three backbones and exhibits positive out-of-distribution transfer. These results demonstrate the value of jointly adapting the learner and its training-time learning substrate for robust self-improving LLM agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）智能体在自进化过程中存在的“智能体-环境失配”问题。研究的背景是，当前LLM智能体通过与环境互动来不断提升能力，但大多数自进化方法只关注单独改进策略（模型侧）或单独调整学习环境（环境侧），未能实现两者的协同。现有方法的不足体现在两个方面：一方面，模型中心进化在固定的环境中优化策略，导致反馈信号依赖于当前策略自身的轨迹分布，在长程交互和稀疏奖励场景下容易引发探索偏差、不稳定的恢复和低效的信用分配；另一方面，环境中心进化虽然调整任务难度或指令，但其调整未扎根于智能体实际的可执行失败，导致环境与学习者的真实能力缺口耦合较弱。核心问题在于：训练时的学习环境无法动态跟踪智能体不断演进的能力边界，提供的信号过于静态、针对性弱且信息量不足。因此，本文提出SEAL框架，通过利用可验证的失败诊断作为共享信号，协同改进学习环境（提供更清晰的工具提示、约束信息和恢复反馈）和策略优化（基于诊断进行优势加权更新），从而在低成本训练样本下显著提升智能体在多轮工具使用场景中的表现。

### Q2: 有哪些相关研究？

相关研究主要分为三类。第一类是模型中心的方法，如递归技能学习、自我巩固、反思提示适应、基于记忆的改进和交互反馈强化学习，这些方法专注于通过训练优化智能体自身的策略、提示或技能库，但通常保持学习环境固定不变。本文与之互补，不仅利用失败轨迹优化模型，还将其作为证据用于环境调整。第二类是环境适应方法，包括课程学习、自动课程设计、合成指令生成、任务进化以及工具或技能构建，它们重塑训练分布或接口，但主要关注任务多样性、难度或覆盖范围。本文的区别在于，它基于验证器诊断执行故障条件化环境适应，针对当前策略的能力差距暴露特定的工具线索、约束信息和恢复反馈。第三类是交互式基准和共进化研究，涉及工具使用、函数调用、网页导航等任务，这些基准提供了多轮依赖和执行约束。本文最接近智能体-环境共进化的视角，但采用更严格的协议，保持基准任务和验证器固定，仅以故障条件化和验证器驱动的方式调整训练时界面。

### Q3: 论文如何解决这个问题？

SEAL提出一个闭环协同进化框架，核心思路在于将训练环境视为可自适应调整的学习界面，而非固定执行器。整体架构由四个主要模块构成闭环循环：轨迹收集、失败诊断、接口进化和策略优化。

首先，智能体与可执行工具环境交互，产生多轮轨迹。然后，诊断模块对所有失败轨迹进行细粒度的逐轮诊断，生成结构化的失败标签Z(τ)，如参数不匹配、缺失工具调用或恢复失败等。这些诊断基于解析器检查、工具模式验证和执行错误等可执行证据，而非自由形式的模型评判，确保了诊断的可靠性。诊断结果作为共享信号驱动后续两个关键创新点：

1. **环境侧接口进化**：SEAL根据聚合的失败画像C_t动态增强训练时的观察o_i。具体通过三个轻量级组件实现：ϕ_schema暴露工具模式隐含的构件线索（如必填参数、枚举约束）；ϕ_err将执行错误转换为面向恢复的反馈；ϕ_cap根据当前失败模式选择特定能力提示。这种进化仅改变信息呈现方式，不修改工具语义、验证器或评估协议。

2. **策略侧诊断加权优化**：SEAL利用诊断信息为每个轨迹计算学习效用权重w_j。更具可归因性和修复价值的失败（如无效工具调用）获得更高权重，而模糊失败（如响应不匹配）权重较低。在GRPO优化中，该权重作为先验条件缩放原始优势函数A_j，形成诊断加权优势Ã_j = w_j·A_j。这在不改变验证器奖励符号的前提下，优先利用更具信息量的失败轨迹进行策略更新。

最终SEAL形成了智能体与环境接口的协同进化闭环：智能体揭示能力缺口，接口自适应调整，模型通过策略优化内化反馈。在仅400个训练样本的低资源场景下，该方法在三个骨干模型上获得+8.25至+26.25的平均分提升，并展现出正向的分布外迁移能力。

### Q4: 论文做了哪些实验？

论文进行了全面的实验评估，涵盖分布内和分布外场景。实验设置如下：使用BFCL V3多轮子集作为分布内基准，包含Base、Missing Functions、Missing Parameters和Long Context四类共800个样本，在低资源设置下从每类采样100个共400个样本训练，剩余400个用于评估。分布外评估使用BFCL V4 Web Search和Memory以及τ²-bench的Retail、Airline、Telecom领域。对比基线包括三个骨干模型（Qwen2.5-3B-Instruct、Qwen2.5-7B-Instruct和ToolACE-2-Llama-3.1-8B）及其Vanilla RL版本，同时列出闭源和开源工具使用系统作为参考。超参数采用GRPO风格优化器，每提示8次rollout，学习率1×10⁻⁶。主要结果：SEAL显著提升了分布内性能，在Qwen2.5-3B、Qwen2.5-7B和ToolACE-2-8B上分别比原始模型提升+8.25、+26.25和+14.75平均百分点，比Vanilla RL提升+4.75、+9.50和+8.25分。分布外迁移表现积极，SEAL在BFCL V4和τ²-bench上均优于Vanilla RL。消融实验表明，环境端适应、诊断引导重加权和闭环更新三个组件均贡献显著，完整SEAL以40.25%平均分优于所有单侧变体。

### Q5: 有什么可以进一步探索的点？

1.  **环境依赖性过强**：SEAL依赖可执行环境、工具模式和执行轨迹，这限制了其在更开放、缺乏结构化反馈的领域（如创意写作或开放域对话）中的应用。未来可探索弱监督或自监督的诊断信号，以适配非结构化环境。
2.  **自适应能力不足**：文中固定诊断效用权重，且环境演化仅修改训练接口而非工具语义，导致跨任务和跨骨干网络的泛化能力有限。未来可引入元学习或在线学习机制，动态调整诊断权重和演化策略。
3.  **长期工作流支持薄弱**：当前框架在长周期、多智能体协作场景下可能失效。改进方向包括利用分层强化学习处理长时依赖，或通过记忆增强机制追踪演化轨迹，以支持更复杂的工具生态系统。

### Q6: 总结一下论文的主要内容

本文提出了SEAL框架，针对大规模语言模型智能体在交互式工具使用场景中存在的“智能体-环境错位”问题——即智能体能力边界随训练动态变化，而提供监督信号的学习环境却保持静态或与智能体实际失败弱耦合。SEAL通过闭环协同进化机制解决这一结构性问题：在可执行验证器监督下收集在线轨迹，将失败轨迹诊断转向级别的失败标签，并将其作为共享信号同时驱动环境侧和学习侧调整。环境端通过暴露更清晰的工具使用线索、约束信息和恢复导向反馈来进化训练时交互界面；策略端则利用诊断引导的优势重加权进行优化。在分布内和分布外的多轮工具使用评估中，SEAL仅用400个训练样本就在三个骨干模型上取得了+8.25到+26.25的平均分提升，并展现出正向的分布外迁移能力。这一工作揭示了联合自适应学习者和训练时学习基板对于构建稳健自改进智能体的重要价值。
