---
title: "Two-Stage Active Distribution Network Voltage Control via LLM-RL Collaboration: A Hybrid Knowledge-Data-Driven Approach"
authors:
  - "Xu Yang"
  - "Chenhui Lin"
  - "Xiang Ma"
  - "Dong Liu"
  - "Ran Zheng"
  - "Haotian Liu"
  - "Wenchuan Wu"
date: "2026-02-25"
arxiv_id: "2602.21715"
arxiv_url: "https://arxiv.org/abs/2602.21715"
pdf_url: "https://arxiv.org/pdf/2602.21715v1"
categories:
  - "eess.SY"
  - "cs.AI"
tags:
  - "Agent 架构"
  - "多智能体系统"
  - "工具使用"
  - "知识-数据驱动"
  - "强化学习"
  - "LLM Agent"
  - "电力系统"
relevance_score: 8.5
---

# Two-Stage Active Distribution Network Voltage Control via LLM-RL Collaboration: A Hybrid Knowledge-Data-Driven Approach

## 原始摘要

The growing integration of distributed photovoltaics (PVs) into active distribution networks (ADNs) has exacerbated operational challenges, making it imperative to coordinate diverse equipment to mitigate voltage violations and enhance power quality. Although existing data-driven approaches have demonstrated effectiveness in the voltage control problem, they often require extensive trial-and-error exploration and struggle to incorporate heterogeneous information, such as day-ahead forecasts and semantic-based grid codes. Considering the operational scenarios and requirements in real-world ADNs, in this paper, we propose a hybrid knowledge-data-driven approach that leverages dynamic collaboration between a large language model (LLM) agent and a reinforcement learning (RL) agent to achieve two-stage voltage control. In the day-ahead stage, the LLM agent receives coarse region-level forecasts and generates scheduling strategies for on-load tap changer (OLTC) and shunt capacitors (SCs) to regulate the overall voltage profile. Then in the intra-day stage, based on accurate node-level measurements, the RL agent refines terminal voltages by deriving reactive power generation strategies for PV inverters. On top of the LLM-RL collaboration framework, we further propose a self-evolution mechanism for the LLM agent and a pretrain-finetune pipeline for the RL agent, effectively enhancing and coordinating the policies for both agents. The proposed approach not only aligns more closely with practical operational characteristics but also effectively utilizes the inherent knowledge and reasoning capabilities of the LLM agent, significantly improving training efficiency and voltage control performance. Comprehensive comparisons and ablation studies demonstrate the effectiveness of the proposed method.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决主动配电网（ADN）中因分布式光伏（PV）高渗透率而加剧的电压控制难题。传统的数据驱动方法（如深度强化学习）虽然有效，但在实际应用中面临四大挑战：1）信息不完整且异构：日前阶段只能获得粗粒度的区域级预测，难以整合历史记录、电压报告等非结构化信息；2）基于语义的运行约束：机械资产（如有载调压变压器OLTC、并联电容器SCs）的调度需遵循自然语言描述的电网规程（如“OLTC每日调整次数上限”），现有RL方法难以有效融入此类约束；3）适应长尾需求的指令：电网运营商可能发布自然语言指令（如设备故障、维护），RL智能体无法理解并适应；4）策略改进方向模糊：RL仅依赖标量奖励信号，信息有限，导致探索效率低、性能提升慢。为此，论文提出一种混合知识-数据驱动方法，通过大语言模型（LLM）智能体与强化学习（RL）智能体的动态协作，实现两阶段电压控制，以更贴合实际运营场景的方式提升训练效率和电压控制性能。

### Q2: 有哪些相关研究？

相关研究主要分为三类：1）基于RL的电压控制方法：早期工作[5]-[7]利用RL优化ADN内部分布式能源以改善电压；多智能体RL方法[8]-[11]将不同区域或资源集群分配给多个RL智能体进行协作；分层电压调节方法[12]-[14]协调不同时间尺度的设备。这些方法虽有效，但面临上述四大挑战。2）LLM在电力系统中的应用：现有研究多将LLM用于仿真设置[31,32]、文档分析[33]、场景生成[34]等辅助任务，或作为代码编程/函数合成的自然语言接口[19]-[21]，尚未充分挖掘LLM作为决策模型的潜力。3）LLM辅助RL训练：一些研究探索LLM如何辅助RL智能体训练[22]-[24]，例如通过代码生成或函数合成，但LLM通常不直接参与策略制定。本文与现有工作的主要区别在于：首次提出LLM与RL的协作框架，将LLM作为核心决策智能体处理日前调度，并引入自进化机制；同时，将RL定位为LLM可调用的专用工具进行日内精细控制，形成一种深度融合的混合知识-数据驱动范式。

### Q3: 论文如何解决这个问题？

论文提出一个LLM-RL协作框架，分为日前和日内两阶段：日前阶段，LLM智能体接收粗粒度区域级预测（如净负荷），生成符合电网规程的OLTC和SCs调度策略；日内阶段，RL智能体基于精确节点级测量，调整PV逆变器的无功功率以精细化终端电压。核心方法包括：1）LLM智能体定制：通过精心设计的提示词（环境任务描述、输出格式、思维链指导、少样本示例）将通用LLM适配为领域专用决策模型。少样本示例来自一个不断更新的知识库，其中存储历史日的预测数据、动作及反馈结果。2）LLM策略自进化机制：基于Reflexion范式，LLM智能体通过与环境交互获得反馈（总奖励、电压曲线），进行多轮自我反思以优化策略。知识库更新设有阈值：若新场景与历史场景相似度低，则直接存入；若相似度高，则比较奖励，保留更优策略对应的场景。3）RL智能体预训练-微调管道：RL智能体首先在OLTC和SCs动作随机分配的环境中进行预训练，学习通用的PV逆变器控制策略；随后在由LLM策略定义的环境中进行微调，快速适应LLM的日前调度。RL采用PPO算法，其状态空间包含实时测量和LLM的日前动作（经one-hot编码），动作空间为PV逆变器无功出力，奖励函数与电压偏差最小化目标一致。该框架本质上是知识驱动（LLM的先验知识与推理）与数据驱动（RL的精确计算与快速响应）的协同，LLM作为环境的一部分为RL简化问题并缩小探索空间，RL则作为LLM的可调用工具扩展其能力边界。

### Q4: 论文做了哪些实验？

实验在IEEE 33节点和141节点配电系统上进行，使用一年的PV和负荷数据模拟潮流。日前预测添加5%白噪声以模拟误差，日内控制间隔为15分钟。LLM采用Qwen-Plus，RL采用PPO算法。实验分为离线训练和在线执行两个阶段。训练阶段比较了四种方法：1）Proposed（本文方法）；2）Pure-RL（用两个独立RL智能体分别处理日前和日内，并采用惩罚机制和动作掩码处理约束）；3）No-PT（RL智能体未经预训练直接微调）；4）No-Reflexion（LLM智能体省略Reflexion过程）。训练曲线显示，Proposed的LLM策略通过自进化稳定提升，RL预训练后能快速适应并进一步优化性能；Pure-RL即使经过训练，其日前策略仍远逊于LLM初始策略，验证了LLM在知识嵌入、语义理解和策略改进方面的优势；No-PT收敛更慢且在141节点系统陷入次优解；No-Reflexion改进速率显著较低。在线执行阶段，使用75个测试情景评估收敛策略的性能指标（平均节点电压偏差及电压越限率）。对比基线还包括：Original（无主动控制）、No-LLM（禁用机械资产）、No-RL（禁用PV无功）。结果表明，Proposed在两种测试系统上均取得最佳性能（电压偏差最小，越限率极低），显著优于所有基线。Pure-RL表现最差，甚至在某些场景差于Original；No-PT和No-Reflexion性能均次于Proposed，验证了预训练管道和Reflexion机制的有效性。

### Q5: 有什么可以进一步探索的点？

论文的局限性及未来方向包括：1）扩展性与泛化性：当前方法在特定拓扑和分区下验证，未来需测试更复杂、动态变化的网络拓扑及分区策略，并探索LLM-RL框架在其他电网优化问题（如经济调度、恢复控制）的泛化能力。2）LLM的可靠性与安全性：LLM可能存在幻觉或生成不符合物理规律的策略，需设计更严格的验证机制和安全护栏；同时，如何防御针对LLM提示词的对抗性攻击也是重要课题。3）多模态信息融合：目前LLM主要处理文本和数值预测，未来可整合卫星图像、天气图等多模态数据，提升日前预测的准确性。4）在线学习与持续适应：当前LLM知识库和RL策略在离线训练后冻结，未来可研究安全的在线学习机制，使智能体能持续适应电网运行模式的变化和新出现的指令。5）协作机制的深化：本文LLM与RL的协作相对松散，未来可探索更紧密的联合训练框架，例如让LLM为RL提供课程学习指导或内在奖励，实现更高效的协同进化。

### Q6: 总结一下论文的主要内容

本文提出了一种创新的混合知识-数据驱动方法，通过LLM智能体与RL智能体的协作解决主动配电网的两阶段电压控制问题。核心贡献在于：1）构建了贴合实际运营的两阶段问题形式化，明确区分了日前粗粒度预测与日内精确测量的信息差异；2）设计了LLM-RL协作框架，LLM负责日前调度机械资产（OLTC、SCs），利用其自然语言理解、知识整合与推理能力处理异构信息和语义约束；RL负责日内控制PV逆变器无功，发挥其精确计算与快速响应优势；3）提出了针对性的策略改进机制：为LLM智能体设计了基于Reflexion的自进化方法，通过交互反馈和知识库迭代更新优化策略；为RL智能体设计了预训练-微调管道，使其能快速适应LLM策略并实现高效协同。实验在IEEE标准系统上验证了所提方法的优越性，在训练效率和最终控制性能上均显著优于纯RL等基线方法。该工作为将LLM深度融入复杂决策任务提供了范例，推动了知识驱动与数据驱动智能体的融合，在电力系统及其他需要处理语义约束与异构信息的领域具有广泛的应用前景。
