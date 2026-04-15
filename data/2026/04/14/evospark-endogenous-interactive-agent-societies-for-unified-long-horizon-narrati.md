---
title: "EvoSpark: Endogenous Interactive Agent Societies for Unified Long-Horizon Narrative Evolution"
authors:
  - "Shiyu He"
  - "Minchi Kuang"
  - "Mengxian Wang"
  - "Bin Hu"
  - "Tingxiang Gu"
date: "2026-04-14"
arxiv_id: "2604.12776"
arxiv_url: "https://arxiv.org/abs/2604.12776"
pdf_url: "https://arxiv.org/pdf/2604.12776v1"
categories:
  - "cs.CL"
tags:
  - "多智能体系统"
  - "叙事生成"
  - "长期模拟"
  - "社会记忆"
  - "一致性保持"
  - "框架设计"
relevance_score: 8.0
---

# EvoSpark: Endogenous Interactive Agent Societies for Unified Long-Horizon Narrative Evolution

## 原始摘要

Realizing endogenous narrative evolution in LLM-based multi-agent systems is hindered by the inherent stochasticity of generative emergence. In particular, long-horizon simulations suffer from social memory stacking, where conflicting relational states accumulate without resolution, and narrative-spatial dissonance, where spatial logic detaches from the evolving plot. To bridge this gap, we propose EvoSpark, a framework specifically designed to sustain logically coherent long-horizon narratives within Endogenous Interactive Agent Societies. To ensure consistency, the Stratified Narrative Memory employs a Role Socio-Evolutionary Base as living cognition, dynamically metabolizing experiences to resolve historical conflicts. Complementarily, Generative Mise-en-Scène mechanism enforces Role-Location-Plot alignment, synchronizing character presence with the narrative flow. Underpinning these is the Unified Narrative Operation Engine, which integrates an Emergent Character Grounding Protocol to transform stochastic sparking into persistent characters. This engine establishes a substrate that expands a minimal premise into an open-ended, evolving story world. Experiments demonstrate that EvoSpark significantly outperforms baselines across diverse paradigms, enabling the sustained generation of expressive and coherent narrative experiences.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型的多智能体系统在实现长周期、自洽的叙事演化时所面临的核心挑战。当前，这类系统在生成短期互动片段方面表现出色，但在构建能够从一个简单初始设定自主演化成无限、自持且逻辑一致的叙事生态系统的长周期模拟方面，仍存在显著不足。

研究背景在于，LLM与多智能体系统的结合虽革新了生成式叙事，但现有方法在长周期模拟中暴露出两大系统性缺陷。首先，现有架构普遍存在“社会记忆堆叠”问题，即采用简单的追加式记忆机制，导致相互矛盾的关系状态（如既为友又为敌的记忆）不断累积而无法消解，最终引发角色行为逻辑的混乱。其次，文本智能体面临“叙事-空间失调”，由于缺乏将叙事进展与空间状态同步的机制，智能体常产生脱离现实的交互，例如在关键情节转折时角色出现在不连贯的地点，这割裂了故事、角色与场景之间本应存在的逻辑联系。

此外，该领域在结构上还受限于一种范式分裂：传统的交互式叙事依赖僵化的脚本，保证了逻辑但牺牲了自主性；而近期基于LLM的模拟则往往优先追求开放式的涌现，结果导致不可控的混沌状态。尽管已有研究暗示了控制机制的必要性，但现有的碎片化架构无法支持从严格层级规划到开放式演化这一完整谱系的叙事控制需求。

因此，本文要解决的核心问题是：如何设计一个统一的框架，以克服社会记忆堆叠和叙事-空间失调，并弥合控制与涌现之间的范式鸿沟，从而在基于LLM的内生交互式智能体社会中，实现逻辑连贯的长周期叙事自主演化。论文提出的EvoSpark框架正是为了应对这一系列相互关联的挑战。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：内生多智能体系统、社会进化动力学与记忆、以及生成性场面调度。

在内生多智能体系统方面，早期研究如MetaGPT和Camel依赖固定的标准操作流程，限制了适应性。后续工作如CoMAS、AFlow和Darwin Gödel Machine转向通过交互奖励优化策略或允许智能体自我修改代码，以实现自我改进。社会模拟器如AgentSociety、OASIS和Generative Agents则通过扩展交互规模来观察涌现的规范。然而，本文指出，这些现有系统存在“目的论错配”，它们通常为指标收敛（如通过率）而优化，将叙事扩展所必需的随机性视为噪声，并且缺乏解决长期模拟中“社会记忆堆叠”问题的代谢机制。

在社会进化动力学与记忆方面，相关研究如ID-RAG、Open-Theatre和MemoryBank通过身份知识图谱或分层记忆存储来确保一致性，防止身份漂移。S3、AgentSociety和Generative Agents也利用记忆模块维持行为模式。但本文认为，这些方法通常将记忆视为累积日志，导致过时的关系状态持续存在并引发冲突。尽管G-Memory、MemEvolve和DOME等近期工作尝试优化记忆架构或追踪状态变化，但仍缺乏从根本上随时间转化智能体个性与关系的“社会进化代谢”能力。

在生成性场面调度方面，研究旨在解决叙事与空间环境的脱节问题。Generative Agents将行为锚定在沙盒中，AgentSociety通过兴趣区建模城市移动性，BookWorld引入了离散的地理空间追踪。NarrativeGenie、HAMLET、Open-Theatre和HoLLMwood则通过动态布置道具、裁定物理交互或定义场景边界来约束智能体位置。然而，本文指出这些框架往往缺乏维持情节、角色及其具体位置之间本质对齐的细粒度机制，且标准语义度量无法检测逻辑不一致。

### Q3: 论文如何解决这个问题？

论文通过提出EvoSpark框架来解决长时程叙事模拟中的社会记忆堆叠和叙事空间失调问题。其核心方法是一个整合了叙事操作引擎、分层叙事记忆和生成性场面调度机制的统一架构。

整体框架包含三个主要阶段：叙事构思与宏观规划、叙事操作化引擎、以及迭代模拟与演化。核心创新在于**统一叙事操作引擎**，它作为底层支撑，将静态蓝图转化为动态演化的故事世界。该引擎集成了**涌现角色锚定协议**，能够将LLM随机产生的“火花”（即未初始化实体的幻觉）通过实体解析和本体提升，转化为故事世界中持久且一致的角色，从而实现了角色的内生性涌现。

框架包含四个专门化的智能体协同工作：**Genesis Agent**负责根据用户前提生成叙事脊柱；**Architect Agent**执行世界地图与位置模块化，并协同处理ECGP协议；**Director Agent**作为模拟过程的指挥者，提供实时交互指导并执行动态空间对齐；**Role Agents**则基于其**角色社会演化基**进行去中心化交互，形成内生的社会图景。

关键技术之一是**分层叙事记忆**，它采用四层架构来避免记忆堆叠：临时性的情节演化缓冲区、存储全局事实的共享世界知识库、用于溯源的不可变角色情节基，以及核心的、可变的**角色社会演化基**。RSB通过事件驱动的**反思-合成-巩固机制**进行原地更新，主动对比新经验与旧状态，解析并覆盖过时的社会关系和性格向量，从而确保认知状态的一致性。

另一项关键技术是**生成性场面调度机制**，它通过Genesis与Director智能体之间的“计划-修正”协议，强制执行**角色-位置-情节对齐**。该机制包含离线规划对齐和动态空间对齐两个阶段。后者尤其关键，它作为一个“虚拟舞台监督”，通过实体解析步骤纠正LLM可能产生的身份幻觉，并将空间约束（如角色站位、视线方向）显式地注入到交互描述中，确保角色的物理行动与叙事意图在空间逻辑上保持一致，从而解决了叙事与空间的脱节问题。

### Q4: 论文做了哪些实验？

论文实验主要包括三部分：比较评估、长时程演化对齐分析和消融研究。实验设置上，使用涵盖神秘、科幻、史诗奇幻等六种类型的精选场景，主要评估具有挑战性的长时程设定，每次模拟包含15个连续重大事件（约45个场景），每次运行平均生成20万至25万词。使用的基线框架包括代表集中控制范式的Open-Theatre、高保真虚拟世界模拟框架BookWorld，以及模仿作家-编辑工作流的创意写作代理框架HoLLMwood。

评估采用全面的指标：通用指标包括角色表现（RP）和沉浸感（Im）；针对HDP和SNP范式的指标包括叙事共鸣（NR）和长时程一致性（LC）；针对自由EN范式的指标包括叙事健全性（NS）、创造力（Cr）和情节推进（PAC）。采用基于LLM-as-a-Judge的成对评估协议，使用Gemini-2.5-Pro（英文）和Deepseek-v3.2-Think（中文）模型，报告胜率和平均李克特分数（1-5分）。

主要结果显示，EvoSpark在大多数设置下显著优于基线，尤其在推理增强模型上，在角色表现、叙事共鸣和沉浸感等指标上取得主导性胜率和优势。关键数据包括：在推理模型上胜率显著更高；在自由EN模式下，由于框架干预最小，性能波动性增加。长时程演化对齐分析表明，随着事件数增加到5和10个，角色表现、长时程一致性和演化行动对齐的胜率显著提升，特别是在SNP和自由EN范式下。消融研究评估了四个变体：无RSB、无RSB关系演化、无GMS和无ECGP。结果显示，移除GMS导致角色表现、共鸣和沉浸感最严重下降；禁用ECGP显著损害沉浸感和创造力；而无RSB变体在短期评估中下降相对较小，其影响主要在长时程中显现。

### Q5: 有什么可以进一步探索的点？

本文提出的EvoSpark框架在维持长程叙事一致性方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。主要局限性包括：随着模拟时长增加，叙事历史和关系图的不断积累会导致显著的内存开销和推理延迟，限制了其在资源受限或严格实时环境中的应用效率；此外，当前评估侧重于自主智能体间的互动演化以验证内部一致性，对人类玩家交互的动态响应尚未充分量化。

未来研究方向可以从以下几个层面展开：在技术优化层面，可以探索更高效的内存管理策略，例如采用分层压缩、选择性遗忘或增量更新机制来减轻存储与计算负担；也可研究轻量化的关系图表示与推理方法，以提升系统实时性。在交互性拓展层面，亟需设计并评估系统对人类不可预测输入的鲁棒响应机制，这可能涉及引入适应性更强的叙事规划模块或建立玩家意图识别模型。在理论深化层面，可以进一步形式化“叙事-空间”对齐的度量标准，并探索不同叙事类型（如悬疑、浪漫）对演化机制的特殊要求。此外，将框架应用于更复杂的开放世界游戏或沉浸式叙事生成平台，进行大规模用户研究，也是验证其普适性与实用价值的重要步骤。

### Q6: 总结一下论文的主要内容

该论文针对基于大语言模型的多智能体系统中，内生叙事演化因生成涌现的固有随机性而受阻的问题，提出了EvoSpark框架。核心挑战在于长时程模拟中存在社会记忆堆叠（冲突关系状态累积无法解决）和叙事空间失调（空间逻辑与情节发展脱节）。为解决这些问题，EvoSpark的核心贡献在于设计了一个旨在维持内生交互智能体社会中逻辑连贯长时程叙事的统一框架。其方法主要包括：采用分层叙事记忆，以角色社会进化基础作为活体认知，动态代谢经验以解决历史冲突；辅以生成性场面调度机制，强制实现角色-地点-情节的对齐，使角色存在与叙事流同步；底层则由统一叙事操作引擎支撑，它集成了涌现角色锚定协议，将随机火花转化为持久角色，从而将最小前提扩展为一个开放、演化的故事世界。实验表明，EvoSpark在多种范式下显著优于基线方法，能够持续生成富有表现力且连贯的叙事体验。这项工作通过将随机幻觉转化为结构性叙事资产，为实现开放故事世界的无限扩展和自主叙事智能的进步铺平了道路。
