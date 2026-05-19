---
title: "SkillsVote: Lifecycle Governance of Agent Skills from Collection, Recommendation to Evolution"
authors:
  - "Hongyi Liu"
  - "Haoyan Yang"
  - "Tao Jiang"
  - "Bo Tang"
  - "Feiyu Xiong"
  - "Zhiyu Li"
date: "2026-05-18"
arxiv_id: "2605.18401"
arxiv_url: "https://arxiv.org/abs/2605.18401"
pdf_url: "https://arxiv.org/pdf/2605.18401v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent技能生命周期治理"
  - "技能库管理"
  - "经验重用"
  - "可验证技能"
  - "离线演化"
  - "在线演化"
  - "Agent认知架构"
  - "轨迹分解与归因"
relevance_score: 9.2
---

# SkillsVote: Lifecycle Governance of Agent Skills from Collection, Recommendation to Evolution

## 原始摘要

Long-horizon LLM agents leave traces that could become reusable experience, but raw trajectories are noisy and hard to govern. We treat Agent Skills as an experience schema that couples executable scripts, with non-executable guidance on procedures. Yet open skill ecosystems contain redundant, uneven, environment-sensitive artifacts, and indiscriminate updates can pollute future context. We present SkillsVote, a lifecycle-governance framework for Agent Skills from collection and recommendation to evolution. SkillsVote profiles a million-scale open-source corpus for environment requirements, quality, and verifiability, then synthesizes tasks for verifiable skills. Before execution, SkillsVote performs agentic library search over structured skill library to expose instructional skill context. After execution, it decomposes trajectories into skill-linked subtasks, attributes outcomes to skill use, agent exploration, environment, and result signals, and admits only successful reusable discoveries to evidence-gated updates. In our evaluation, offline evolution improves GPT-5.2 on Terminal-Bench 2.0 by up to 7.9 pp, while online evolution improves SWE-Bench Pro by up to 2.6 pp. Overall, governed external skill libraries can improve frozen agents without model updates when systems control exposure, credit, and preservation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决的是大规模智能体技能生态系统中技能生命周期治理的核心问题。研究背景在于，随着LLM智能体在长期任务中的广泛应用，其执行轨迹中蕴含了大量可重用的经验，但原始轨迹过长、噪声大且与环境紧密耦合，不适合直接作为知识复用。为此，现有工作提出了智能体技能（Agent Skill）这一结构化经验模式，它将可执行脚本与过程性指导打包，但开放式的技能生态面临冗余、质量不均、与环境敏感等挑战，不加区分地更新技能会导致库污染，恶化未来任务的上下文。

现有方法的不足主要体现在：技能库规模增长后，检索空间变大，低质量或不相关技能会降低智能体性能；现有技能演化工作直接使用执行证据进行更新，缺乏归因控制，容易将环境干扰或评估信号本身导致的失败误认为是技能问题，从而引入脏数据。

论文提出的SkillsVote框架旨在解决上述问题，核心是通过闭环治理机制实现技能从收集、推荐到演化的全生命周期管理。具体而言，它在执行前通过智能体库搜索进行结构化推荐，过滤出相关且低冗余的技能；执行后则通过轨迹归因，将结果信号与技能使用、智能体探索、环境及评估信号分离，只允许可复用的成功经验进入演化库，从而避免无差别更新带来的库污染问题，实现对外部技能生态的可控利用。

### Q2: 有哪些相关研究？

相关研究按类别可组织为：**方法类**包括早期记忆方法（存储非结构化案例和示例）、工作流方法（将轨迹抽象为半结构化工作流和SOP）、策略级方法（将经验压缩为原则和策略）、以及近期的工具、MCP和技能学习方法（将经验附加到可调用接口和依赖边界）。**评测与生态类**包括AgentSkillOS和SkillNet（将技能组织为生态对象）、SkillsBench、SkillCraft、SkVM和SkCC（评估技能效用、组合性、可移植性、安全性、依赖和兼容性）。**技能选择与路由类**包括SkillRouter（学习基于完整技能体的路由而非仅名称或描述）、DCI（用直接语料库交互替代嵌入检索）。**技能学习与进化类**包括训练策略以决定何时检索技能、如何使用技能、何时将行为蒸馏进模型或修改库的方法，以及保持基模型固定、利用会话级或轨迹级证据结合验证器或环境反馈生成可复用技能制品的方法。本文与这些工作的区别在于：1) 首次提出覆盖技能收集、推荐到进化的全生命周期治理框架；2) 对百万级开放技能语料进行格式、依赖、质量和可验证性画像；3) 在执行前通过结构化技能库的智能代理搜索暴露指令性技能上下文；4) 在执行后将轨迹分解为技能关联的子任务，归因结果至技能使用、代理探索、环境和结果信号，仅允许成功且可复用的发现进入证据门控的库更新。

### Q3: 论文如何解决这个问题？

SkillsVote通过一个完整的生命周期治理框架来解决开放技能生态中的冗余、质量不均和环境敏感问题。整体框架包括三个核心阶段：技能档案构建、执行前推荐和执行后归因演化。

在技能档案构建阶段，SkillsVote对GitHub上的百万级SKILL.md开源语料库进行三维度剖析：运行时需求档案评估操作系统假设、权限、API密钥等环境要求；质量档案衡量技能的一致性、完整性和任务导向性；可验证性档案判断低歧义成功条件、可复现沙箱环境和任务实例构建成本。对于通过可验证性筛选的技能，系统基于Harbor任务格式从技能自身合成包含清晰指令、可复现环境和可执行验证器的测试任务，通过实际智能体-模型组合运行记录成功率、成本和跟踪轨迹。

在执行前阶段，SkillsVote采用任务条件化的曝光控制层。该系统在求解智能体启动前运行独立推荐阶段，搜索本地技能库，选择性读取候选SKILL.md及相关资源，挑选出覆盖任务、适配目标环境并提供互补指导的技能，输出紧凑的曝光技能集及简短使用指南。

在执行后阶段，SkillsVote引入子任务级归因层解决信用分配粒度问题。子任务具有独立目标、单一评估信号和至多一个关联技能上下文。归因沿三个维度压缩执行证据：结果证据区分客观环境反馈、人类偏好或缺失明确信号；责任分配将最终状态及其主要原因（技能引导、独立探索或无关技能探索）关联；可复用增量定位实际影响执行的技能部分，仅提取缺失流程、先决条件或恢复模式等可复用发现。通过证据门控更新机制，仅成功的可复用子任务才能触发技能编辑或创建新技能，且更新前需聚合支持同一可复用过程的证据，确保演化保守且可追溯。

### Q4: 论文做了哪些实验？

SkillsVote在Terminal-Bench 2.0（89个困难终端任务）和SWE-Bench Pro public（731个来自11个仓库的软件工程任务）上进行了实验。实验设置包括无技能基线和在线进化（从空库开始，每任务推荐进化）。离线设置仅用于Terminal-Bench 2.0：先从48个Terminal-Bench Pro历史任务构建库，每4个任务触发一次进化，然后冻结库仅用于推荐。使用Codex（GPT-5.2 Medium和GPT-5.4 mini）作为主干模型。主要结果：离线设置中，SkillsVote在Terminal-Bench 2.0上将GPT-5.2的avg@5准确率从51.0提升至58.9（+7.9 pp），GPT-5.4 mini从51.7提升至57.5（+5.8 pp）。在线设置中，Terminal-Bench 2.0准确率提升GDP+2.7 pp（GPT-5.2）和+1.1 pp（GPT-5.4 mini）；SWE-Bench Pro上avg@1解决率提升+2.6 pp（GPT-5.2，从47.6到50.2）和+2.1 pp（GPT-5.4 mini，从46.9到49.0）。推荐消融实验表明，推荐主要过滤噪声，改善正负贡献平衡。

### Q5: 有什么可以进一步探索的点？

从论文的局限性和未来研究方向来看，SkillsVote在环境依赖处理上仍有不足——当前仅对技能进行静态的质量和可验证性分析，但实际环境中系统状态、API版本和工具链的动态变化会影响技能的可迁移性，未来可引入实时环境感知和自适应技能微调机制。其次，证据门控的更新策略虽然保守，但可能过于严格，导致一些潜在有价值但置信度不高的经验被丢弃，可探索概率性更新或混合记忆机制来平衡探索与利用。此外，当前的结构化技能库搜索依赖预定义分类，难以覆盖细粒度任务需求，改进方向包括结合语义embedding和动态聚类实现更灵活的技能检索。最后，跨域迁移和少样本场景下的鲁棒性验证不足，可参考元学习或强化学习中的经验回放机制，设计分层或图结构的技能依赖关系来提升长尾技能的泛化能力。

### Q6: 总结一下论文的主要内容

SkillsVote提出了一个面向Agent技能的完整生命周期治理框架，解决了LLM Agent在执行长周期任务时，原始轨迹噪声大、难以复用的问题。该工作将Agent Skill定义为耦合可执行脚本与不可执行流程指导的经验模式，并针对现有开源技能生态中冗余、质量不均、环境敏感等挑战，设计了从收集、推荐到演化的全流程管理方案。方法上，SkillsVote首先对百万级开源语料库进行环境需求、质量和可验证性画像，并合成任务验证技能；执行前，通过结构化技能库的Agnetic搜索提供指令性上下文；执行后，将轨迹分解为与技能关联的子任务，将结果归因于技能使用、Agent探索、环境和结果信号，仅将成功且可复用的发现纳入基于证据的更新。实验表明，离线演化在Terminal-Bench 2.0上使GPT-5.2提升最多7.9个百分点，在线演化在SWE-Bench Pro上提升最多2.6个百分点。其核心贡献是证明了在无需更新模型参数的情况下，通过受控的外部技能库管理（包括曝光控制、信用归属和持久化），能有效提升冻结Agent的性能，为可扩展的Agent经验复用提供了实用基础。
