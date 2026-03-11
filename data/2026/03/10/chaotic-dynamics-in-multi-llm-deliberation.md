---
title: "Chaotic Dynamics in Multi-LLM Deliberation"
authors:
  - "Hajime Shimao"
  - "Warut Khern-am-nuai"
  - "Sung Joo Kim"
date: "2026-03-10"
arxiv_id: "2603.09127"
arxiv_url: "https://arxiv.org/abs/2603.09127"
pdf_url: "https://arxiv.org/pdf/2603.09127v1"
categories:
  - "cs.AI"
  - "cs.MA"
tags:
  - "多智能体系统"
  - "多LLM审议"
  - "系统稳定性"
  - "混沌动力学"
  - "智能体委员会"
  - "经验性李雅普诺夫指数"
  - "治理系统"
relevance_score: 7.5
---

# Chaotic Dynamics in Multi-LLM Deliberation

## 原始摘要

Collective AI systems increasingly rely on multi-LLM deliberation, but their stability under repeated execution remains poorly characterized. We model five-agent LLM committees as random dynamical systems and quantify inter-run sensitivity using an empirical Lyapunov exponent ($\hatλ$) derived from trajectory divergence in committee mean preferences. Across 12 policy scenarios, a factorial design at $T=0$ identifies two independent routes to instability: role differentiation in homogeneous committees and model heterogeneity in no-role committees. Critically, these effects appear even in the $T=0$ regime where practitioners often expect deterministic behavior. In the HL-01 benchmark, both routes produce elevated divergence ($\hatλ=0.0541$ and $0.0947$, respectively), while homogeneous no-role committees also remain in a positive-divergence regime ($\hatλ=0.0221$). The combined mixed+roles condition is less unstable than mixed+no-role ($\hatλ=0.0519$ vs $0.0947$), showing non-additive interaction. Mechanistically, Chair-role ablation reduces $\hatλ$ most strongly, and targeted protocol variants that shorten memory windows further attenuate divergence. These results support stability auditing as a core design requirement for multi-LLM governance systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探究多LLM（大语言模型）审议系统中的混沌动力学问题，即多个AI代理在集体决策过程中，即使在没有随机性噪声（如温度参数T=0）的“确定性”设定下，其反复运行也可能产生不可预测的分歧和不稳定行为。研究背景是，随着AI系统从单代理使用转向委员会式部署，多个代理通过交换论点进行审议并投票或合成决策，系统的可重复性成为关键治理属性，而不仅仅是工程便利。现有方法通常关注单次模型评估，但未能充分刻画多代理系统在重复执行下的稳定性；先前工作虽已指出提示层面的LLM输出不稳定性，但缺乏对多LLM审议架构如何引发或放大分歧的实验性设计分析。本文的核心问题是：在多LLM审议系统中，哪些设计选择（如角色结构和模型异质性）会导致、加剧或减弱轨迹敏感性分歧，从而影响系统稳定性。论文通过将五代理LLM委员会建模为随机动力系统，并基于经验李雅普诺夫指数量化不稳定性，揭示了即使在T=0条件下，结构性的不可预测性依然存在，填补了多LLM不稳定性的设计图谱空白。

### Q2: 有哪些相关研究？

本文的相关研究主要可归纳为方法类和应用/评测类。在方法类上，先前研究已证实单一LLM在提示层面的输出具有不稳定性，这为本文研究多LLM系统的不稳定性奠定了基础。同时，社会科学文献指出群体决策结果对成员构成和框架设定敏感，这启发了本文对委员会组成和角色结构的实验设计。在应用/评测类方面，近期关于智能体安全的研究在更宽泛的描述性意义上使用“混沌”一词来指代自主系统的部署故障；与之不同，本文的研究范畴更窄且更侧重于动力学，即通过经验性的李雅普诺夫指数估计量来量化轨迹敏感的发散。

本文与这些工作的关系和区别在于：它填补了现有研究的空白，首次通过实验系统地识别并绘制了导致多LLM审议不稳定的设计因素图谱。具体而言，本文没有停留在描述现象或宽泛的安全担忧上，而是将多LLM委员会建模为随机动力系统，通过受控实验（交叉角色结构和模型同质性/异质性）来分解不稳定的产生路径，并量化其影响。这超越了先前关于单一模型不稳定或群体决策敏感性的孤立观察，提供了对多智能体系统结构不稳定性的机制性理解和可量化的审计方法。

### Q3: 论文如何解决这个问题？

论文通过将多智能体LLM委员会建模为随机动力系统，并采用经验李雅普诺夫指数（$\hat{\lambda}$）量化轨迹分歧，系统性地研究了多LLM审议中的不稳定性问题。核心方法是设计一个包含五个智能体的委员会进行20轮审议，每轮每个智能体输出论点及结构化偏好状态 $\mathbf{s}^{(i)}_t=(p_A,p_B,p_C,conf)$。通过计算委员会平均轨迹 $\overline{\mathbf{p}}^{(r)}_t$ 并分析不同重复运行间的轨迹差异 $D(t)$，估计 $\hat{\lambda}$ 作为 $\log D(t)$ 在3-20轮间的斜率，正值表示轨迹呈指数发散。

整体框架基于一个2×2因子设计，考察两个关键变量：角色分配（有角色 vs. 无角色）和模型组成（同质 vs. 异质）。主要模块包括智能体交互协议、轨迹记录与分歧计算模块，以及用于机制分析的干预测试模块。创新点在于首次在 $T=0$ 条件下量化了多LLM审议的不稳定性，并识别出两条独立的失稳路径：路径A（同质委员会中的角色分化）和路径B（无角色委员会中的模型异质性）。实验发现，即使在没有随机采样的 $T=0$ 条件下，系统仍表现出正的李雅普诺夫指数，表明不稳定性是结构性的而非仅由随机性引起。

关键技术包括角色消融实验和协议变体测试。机制分析显示，主席角色的消融能最大程度降低 $\hat{\lambda}$，表明其合成行为是重要的放大渠道。此外，通过缩短论点记忆窗口（如从 $k=15$ 减至 $k=3$ 或 $k=1$）的干预措施，能有效减弱轨迹分歧，验证了早期回合反馈记忆对不稳定性的贡献。这些发现为非加性相互作用提供了证据，例如异质无角色委员会的 $\hat{\lambda}=0.0947$ 高于异质有角色委员会的 $0.0519$，说明同时增加多样性和角色分配不会单调增加不稳定性。最终，论文提出稳定性审计应作为多LLM治理系统的核心设计需求，并为通过协议调整缓解不稳定性提供了实证依据。

### Q4: 论文做了哪些实验？

论文在五个智能体组成的LLM委员会中进行了多组实验，以探究多LLM审议中的混沌动力学。实验设置上，每个委员会运行20轮，每轮每个智能体输出论点及结构化偏好状态。通过计算委员会平均轨迹，并基于轨迹间的欧氏距离定义重复运行间的分歧度D(t)，进而估计经验李雅普诺夫指数(\(\hat{\lambda}\))，其正值表示轨迹呈指数发散。主要实验在温度T=0下进行，以隔离采样噪声，并设置了目标重复次数R=20。

实验使用了包含12个政策场景的基准测试，其中HL-01作为典型场景被深入分析。对比方法上，论文采用因子设计，考察了两个关键设计选择的影响：一是同质委员会中是否引入角色分化（如主席等制度性角色），二是委员会中是否混合不同模型家族（即模型异质性）。此外，还通过角色消融实验（特别是主席角色）和协议变体（如将论点记忆窗口从k=15缩短至k=3或k=1）来探究机制和干预效果。

主要结果显示：在同质无角色委员会中，尽管分歧较低，但仍存在正发散（\(\hat{\lambda}=0.0221\)）。引入角色分化会显著增加不稳定性（\(\hat{\lambda}=0.0541\)），而模型异质性（无角色时）导致更高的发散（\(\hat{\lambda}=0.0947\)）。这两种效应并非简单叠加：混合模型加角色的条件（\(\hat{\lambda}=0.0519\)）反而比混合模型无角色（\(\hat{\lambda}=0.0947\)）更稳定，表明存在非加性交互作用。机制上，主席角色的消融最能降低\(\hat{\lambda}\)，缩短记忆窗口也能进一步减弱分歧。这些结果证实了即使在T=0下，多LLM系统也可能出现不稳定的混沌动力学，强调了稳定性审计的重要性。

### Q5: 有什么可以进一步探索的点？

本文揭示了多智能体LLM审议系统存在混沌动力学的风险，但研究仍存在局限。首先，实验主要在T=0的确定性采样设置下进行，未来需探索不同温度参数对稳定性的影响。其次，研究聚焦于偏好轨迹的散度，但未直接关联到外部任务质量（如决策准确性或校准度），后续应评估混沌动态是否损害实际决策效能。此外，干预措施（如缩短记忆窗口）虽能降低不稳定性，但可能简化审议过程，需平衡稳定性与审议深度。

未来研究方向包括：1）将稳定性审计扩展到更复杂的协议和现实任务场景，验证结论的普适性；2）设计更精细的干预机制，例如动态角色分配或自适应记忆管理，以在保持审议质量的同时抑制混沌；3）探索系统初始条件敏感性，研究如何通过初始化控制提升可预测性；4）结合理论动力学模型，深入解析不稳定性产生的内在机制，为系统设计提供理论指导。这些探索将助力构建更稳健、可控的多LLM治理系统。

### Q6: 总结一下论文的主要内容

该论文研究了多LLM集体审议系统中的稳定性问题，发现即使在温度T=0的确定性设定下，相同的AI委员会在重复运行中也可能产生显著不同的集体决策轨迹。核心贡献在于将多智能体委员会建模为随机动力系统，并通过经验李雅普诺夫指数量化了轨迹分歧程度，揭示了导致不稳定的两条独立路径：同质委员会中的角色分化和无角色委员会中的模型异构性。方法上，论文设计了五智能体委员会进行20轮审议，通过计算委员会平均偏好轨迹的差异来估计不稳定性。主要结论包括：角色指派和模型混合均会加剧不稳定性，但两者存在非加性交互作用；主席角色的移除能显著降低不稳定性；通过缩短记忆窗口等协议修改可有效减弱轨迹分歧。这些发现强调了稳定性审计应成为多LLM治理系统的核心设计需求，挑战了实践中对T=0下确定性行为的普遍预期。
