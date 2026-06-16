---
title: "On-Policy Distillation with Curriculum Turn-level Guidance for Multi-turn Agents"
authors:
  - "Gengsheng Li"
  - "Mao Zheng"
  - "Mingyang Song"
  - "Ruiqi Liu"
  - "Tianyu Yang"
  - "Jie Sun"
  - "Qiyong Zhong"
  - "Haiyun Guo"
  - "Junfeng Fang"
  - "Dan Zhang"
  - "Jinqiao Wang"
date: "2026-06-14"
arxiv_id: "2606.15912"
arxiv_url: "https://arxiv.org/abs/2606.15912"
pdf_url: "https://arxiv.org/pdf/2606.15912v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "多智能体蒸馏"
  - "课程学习"
  - "策略蒸馏"
  - "工具使用"
  - "环境交互"
relevance_score: 8.5
---

# On-Policy Distillation with Curriculum Turn-level Guidance for Multi-turn Agents

## 原始摘要

Multi-turn agents that plan, invoke tools, and interact with environments offer a promising paradigm for solving complex tasks, yet their capabilities typically rely on very large models whose inference cost is prohibitive in practice.On-Policy Distillation (OPD) is a natural recipe for transferring such capabilities to smaller students, but we find that it suffers a characteristic failure mode in this setting: small student errors compound across turns and push the trajectory out of the teacher's familiar state distribution, so the teacher's supervision becomes least reliable precisely where the student needs it most.We propose Guided On-Policy Distillation (Guided-OPD), a simple yet effective algorithm that mixes teacher- and student-generated turns within each rollout and schedules the teacher's intervention probability along a curriculum that decays to zero.Strong guidance keeps early trajectories close to the teacher distribution and is then gradually withdrawn to recover the purely on-policy regime used at inference.On ALFWorld, ScienceWorld, and WebShop, distilling Qwen3 students from a Qwen3-30B-A3B teacher, Guided-OPD improves Score by 21.1\% and Success Rate by 25.5\% over vanilla OPD on average, with larger gains on smaller students.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在多轮交互智能体（multi-turn agents）中，使用在线策略蒸馏（On-Policy Distillation, OPD）将大型教师模型的能力迁移至小型学生模型时面临的独特挑战。研究背景是，多轮智能体通过规划、调用工具并与环境交互来执行复杂任务，但其能力通常依赖于参数巨大的模型，导致推理成本高昂。OPD 是迁移这类能力的自然方法，它通过在学生自身采样的轨迹上对齐教师分布，兼具在线学习的训练-推理一致性和词级蒸馏的密集监督优势。然而，现有方法在处理静态推理任务时已显示出不稳定性，而多轮交互的动态特性会放大这些问题。本文识别出 OPD 在多轮场景中的一个关键失败模式：学生模型的微小错误会随着交互轮次累积和放大，导致轨迹偏离教师模型熟悉的状态分布。当学生最需要可靠监督时（即偏离最严重时），教师模型反而因其自身不确定性而提供最不可靠的蒸馏目标，且该问题无法通过延长训练自然缓解。因此，核心问题是：如何克服这种因轨迹分布漂移导致的监督失效，实现从大型教师到小型学生的稳定知识迁移。为此，论文提出了引导式在线策略蒸馏（Guided-OPD）算法。

### Q2: 有哪些相关研究？

在多轮智能代理的蒸馏研究中，现有工作可分为几类：**方法类**方面，标准On-Policy Distillation（OPD）在单轮推理中表现优异，但多轮场景下学生错误会随轮次累积，使轨迹偏离教师分布，导致监督信号不可靠。近期改进包括引入奖励对齐信号增强token级KL散度，但这依赖可靠验证器并削弱蒸馏纯正性；或通过时间课程调度轨迹深度，但仅在宏观层面操作，未能修复学生已进入的状态分布。本文提出的Guided-OPD则直接在rollout中注入显式教师指导，将状态分布拉回教师熟悉区域，无需额外奖励或批评器。**教师指导类**工作中，现有方法存在两极分化：token级双向切换会产生嵌合轨迹，而序列尾部单次接管则阻止学生从局部错误恢复，且两者均导致训练-推理不匹配。Guided-OPD在轮次级别干预（与环境状态转换粒度对齐），并通过课程衰减至零，最终阶段回归纯OPD，消除不匹配。在ALFWorld、ScienceWorld和WebShop上，从Qwen3-30B-A3B教师蒸馏学生，Guided-OPD平均比标准OPD提升21.1%分数和25.5%成功率，小模型增益更大。

### Q3: 论文如何解决这个问题？

Guided-OPD (Guided On-Policy Distillation) 的核心创新在于通过**逐轮（turn-level）的教师引导**和**课程式退火调度**解决多轮智能体蒸馏中的轨迹漂移问题。整体框架保持标准的在线策略蒸馏范式，但关键改进在于混合生成轨迹的方式：在训练过程中，每轮交互（agent的一个完整思考加动作）独立地以概率β由教师模型生成，或以(1-β)由学生模型生成。β从一个较高的初始值（如1.0）沿着预设的余弦曲线平滑衰减至0。当β较高时，大部分轮次由教师主导，确保早期轨迹锚定在教师熟悉的状态分布中；随着β衰减，学生轮次占比逐渐增加，最终β=0时完全过渡到与学生推理一致的标准在线策略蒸馏。方法包含两个互补组件：**逐轮引导**和**课程引导**。在逐轮引导中，不同角色产生的轮次分配不同的KL散度损失：对于学生产生的轮次，使用**反向KL**，聚焦于使学生采样的动作落在教师高概率区域（模式寻找）；对于教师产生的轮次，使用**前向KL**，强制学生覆盖教师演示的多样化行为（质量覆盖）。这种非对称设计使训练信号与角色功能对齐。课程引导则通过衰减β实现从强引导到纯策略蒸馏的平滑过渡，默认采用余弦调度。最终目标函数是两种损失的加权平均：\( \mathcal{L} = (1-\beta_t)\mathcal{J}_{rKL}^{\pi_\theta} + \beta_t \mathcal{J}_{fKL}^{\pi_\phi} \)。该方法在ALFWorld、ScienceWorld和WebShop上，将平均Score提升21.1%，成功率提升25.5%。

### Q4: 论文做了哪些实验？

论文在三个多轮智能体基准（ALFWorld、ScienceWorld、WebShop）上进行了实验。实验设置包括从Qwen3-30B-A3B教师蒸馏三个Qwen3学生模型（0.6B、1.7B、4B），在8× NVIDIA H20 GPU上使用Trinity-RFT框架实现。对比方法包括：Zero-shot（未训练学生）、Vanilla OPD（标准在策略蒸馏）、AdaSwitch（自适应阈值切换教师生成）、TCOD（线性增加KL计算中参与轮次k的课程方法）。主要指标有Score（0-100连续任务分数，ALFWorld不可用）、Success Rate（SR，二进制完成率）和Round（平均交互步数）。主要结果显示，Guided-OPD在所有学生规模上的平均Score和SR均严格优于所有基线，对0.6B、1.7B、4B学生，相比Vanilla OPD分别提升Score 35.3%、17.6%、10.3%，提升SR 32.8%、23.7%、20.1%，同时减少Round 7.9%、7.3%、2.8%。值得注意的是，4B学生在平均Score（42.64 vs 41.40）上甚至超越了7.5倍大的教师模型。消融实验证实了不对称KL损失设计和余弦课程调度的必要性。训练时间效率分析显示，Guided-OPD在匹配性能下实现了约4倍加速。

### Q5: 有什么可以进一步探索的点？

论文的局限性可从四个方向进一步探索。首先，当前仅验证文本离散动作环境，未来可扩展至工具调用、软件工程、GUI 截图理解及连续物理空间等更复杂的观察与动作空间，检验 Guided-OPD 的泛化能力。其次，所有实验均在同一模型家族内进行，跨家族蒸馏（如 Qwen→Llama）可能因分词器不匹配放大分布漂移，需结合跨分词器蒸馏技术或自适应调整课程策略。第三，课程超参数（初始混合概率、衰减形状等）为全局固定，可设计基于教师困惑度或学生置信度的自适应调度，消除手动调参并提升收益。最后，实验限于单节点 8 GPU 及小规模学生，需在更大规模师生模型及更长任务上验证趋势，尤其针对长程轨迹中漂移加剧的场景。此外，可探索将课程视为在线强化学习中的探索-利用权衡，结合奖励信号动态调节教师干预，或引入对抗训练增强学生对漂移状态的鲁棒性。

### Q6: 总结一下论文的主要内容

论文研究了多轮智能体中在线策略蒸馏（OPD）的失效模式：学生模型的微小错误在轮次间累积，导致轨迹偏离教师模型熟悉的分布，使得教师在学生最需要时提供的监督最不可靠。为解决此问题，提出引导式在线策略蒸馏（Guided-OPD），该方法在每次展开中混合教师与学生生成的轮次，并通过课程学习逐步将教师干预概率衰减至零。在ALFWorld、ScienceWorld和WebShop三个基准上，将Qwen3-30B-A3B蒸馏至0.6B、1.7B和4B学生模型，Guided-OPD平均提升Score 21.1%、Success Rate 25.5%，并减少6.0%交互轮次，且较小学生模型获益更大。核心贡献在于揭示了多轮设定的分布漂移瓶颈，并提供了简单有效的解决方案。
