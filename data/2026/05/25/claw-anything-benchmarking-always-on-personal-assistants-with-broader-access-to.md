---
title: "Claw-Anything: Benchmarking Always-On Personal Assistants with Broader Access to User's Digital World"
authors:
  - "Yusong Lin"
  - "Xinyuan Liang"
  - "Haiyang Wang"
  - "Qipeng Gu"
  - "Siqi Cheng"
  - "Jiangui Chen"
  - "Shuzhe Wu"
  - "Feiyang Pan"
  - "Lue Fan"
  - "Sanyuan Zhao"
  - "Dandan Tu"
date: "2026-05-25"
arxiv_id: "2605.26086"
arxiv_url: "https://arxiv.org/abs/2605.26086"
pdf_url: "https://arxiv.org/pdf/2605.26086v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent Benchmark"
  - "Always-On Personal Assistant"
  - "Multi-Device Interaction"
  - "Proactive Assistance"
  - "Data Synthesis Pipeline"
  - "Long-Horizon Context"
  - "GUI/CLI Agent"
  - "Realistic Noise Robustness"
relevance_score: 9.5
---

# Claw-Anything: Benchmarking Always-On Personal Assistants with Broader Access to User's Digital World

## 原始摘要

Large language model agents are increasingly envisioned as always-on personal assistants with access to anything relevant in the user's digital world. Yet current systems operate over only narrow slices of that world, limiting context-sensitive reasoning and effective assistance. Existing benchmarks similarly provide only partial user state and therefore fail to capture performance in such a broad, always-on setting. To address this gap, we introduce Claw-Anything, a benchmark that expands agent context along three dimensions: long-horizon activity histories, interdependent backend services, and integrated GUI and CLI interaction across multiple devices. To instantiate this setting, we simulate months of user activity through multi-round event injection, producing complex world states and realistic noise, including irrelevant events and conflicting signals. Agents must reason over rich contextual environments while remaining robust to such noise. This expanded scope also enables the evaluation of proactive assistance, requiring agents to anticipate user needs and deliver timely recommendations. Experiments show that GPT-5.5 achieves only 34.5% pass@1, substantially below prior benchmarks, underscoring a gap between current agent capabilities and the demands of always-on personal assistance. Alongside the benchmark, we release an automated data-generation pipeline that yields 2,000 training environments and improves the base model by 23.7%, demonstrating its utility of scalable data infrastructure.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前个人助理智能体（AI Agent）在“始终在线”场景下因操作范围狭窄而导致的性能不足问题。研究背景是，前沿智能体系统正从一次性任务解决转向持续性的个人助理模式，期望能长期、上下文敏感地支持用户。然而，现有方法存在根本性局限：首先，现有系统和基准测试仅能访问用户数字世界中极其狭窄、静态的片段，例如只暴露单一命令行界面或少量服务，忽略了用户活动在时间、服务和设备上的分布式特性；其次，因此，现有基准无法评估智能体在需要整合长期活动历史、跨服务依赖以及多设备（图形界面与命令行界面）交互的复杂场景下的推理与行动能力。本文要解决的核心问题是：当智能体被赋予更宽泛的访问权限（即能观测和操作更全面的数字世界状态）时，其性能会面临怎样的挑战？为此，论文提出了Claw-Anything基准，通过沿三个维度（长期事件流、互联后台服务、多设备GUI/CLI接口）扩展智能体上下文，并引入对主动辅助能力的评估，旨在揭示当前模型与现实全访问个人助理需求之间的巨大差距。实验表明，即使在最先进的模型上，其成功率也远低于以往基准，这凸显了现有评估范式的不足和对更全面测试环境的迫切需求。

### Q2: 有哪些相关研究？

在相关研究中，**评测类工作**主要包括ClawBench、WildClawBench、PinchBench、ClawMark、QwenClawBench和Claw-Eval等。这些基准主要将智能体定位为执行局部任务的工具，专注于规划、工具使用和有限环境中的交互，通常限于孤立、短周期且较为干净的场景。本文与它们的关键区别在于，Claw-Anything将评估扩展至三大维度：长周期活动历史、相互依赖的后台服务以及集成GUI与CLI的多设备交互，从而测试智能体在噪声事件流、跨系统协调和主动辅助能力上的表现，填补了“始终在线”个人助理评测的空白。

**方法/环境类工作**方面，相关研究包括SWE-smith、SWE-Gym（代码中心场景）以及CLI-Gym、TermiGen（终端中心场景）。这些工作侧重于构建可扩展的训练环境以支持智能体发展，但在个人助理场景中，可验证环境的构建仍依赖人工，限制了现实性和可扩展性。本文提出了一个结合多轮事件注入、模拟人物设定和历史、跨服务状态联合模拟的自动化数据生成流水线，能够产生2000个训练环境，使基础模型性能提升23.7%，显著推进了个人助理领域环境可扩展性的发展。

### Q3: 论文如何解决这个问题？

Claw-Anything通过构建一个三维扩展的数字化环境基准来解决现有系统在上下文感知和主动辅助能力上的不足。核心方法包括：1) 环境构建：基于用户画像、多设备(CLI和GUI)、超过40个后端服务、以及三个月活动日志的流式事件流，创建丰富的上下文和噪声背景；2) 任务生成：自动化流水线通过多轮事件注入逐步演化世界状态，在快照点生成任务查询、参考答案和可执行验证器；3) 评估机制：结合规则检查和LLM判断的结果导向评估，支持多路径解决方案。

架构设计包含三个主要模块：数字环境生成器、任务与验证器生成器、自动过滤与人工验证模块。关键技术包括：迭代式环境合成，从初始种子画像通过LLM模拟器逐步构建连贯的数字世界；自适应事件生成，将任务/噪声模板适应当前环境状态并更新事件流；自动质量控制，结合规则检查和LLM过滤去除无效实例；以及执行支持的人工验证，确保任务的可解性。

创新点主要体现在：首次将长时活动历史、多服务依赖、多设备异构接口集成到统一基准中；实现了主动辅助能力的评估；提供了可扩展的自动化数据生成基础设施，产生2000个训练环境并将基础模型提升23.7%。

### Q4: 论文做了哪些实验？

论文进行了三组主要实验。首先，基准测试评估了多种前沿LLM（包括Qwen系列、Minimax 2.7、GLM 5.1、Kimi 2.6等开源模型，以及Claude Opus 4.7和GPT-5.5等闭源模型）在Claw-Anything上的表现，使用Claude Sonnet 4.5作为评判模型，主要指标为Pass@1、Pass@3和Pass^3。结果显示，最强闭源模型GPT-5.5仅达到34.5%的Pass@1和20.0%的Pass^3，显著低于此前基准。

其次，消融实验验证了扩展上下文维度的必要性。移除事件流后成功率从21.0%降至0.0%；移除跨服务工具后从24.0%降至0.0%；限制CLI-GUI协同访问后从16.0%降至2.0%。主动式任务（Pass@1=6.7%）远难于被动式任务（25.9%）。上下文规模消融显示，历史越长、服务越多成功率越低。

第三，数据生成管线实验表明，使用2000个训练任务中收集的1500条成功轨迹微调Qwen3.5-27B，其Pass@1提高23.7%，超过所有开源模型。噪声注入比例越高、模拟轮次越多、服务冲突越大，任务成功率越低。懒加载技能策略相比全加载显著降低性能（如Minimax 2.7的Pass@1从22.7%降至10.0%）。

### Q5: 有什么可以进一步探索的点？

从论文的局限性和未来方向来看，Claw-Anything在以下方面值得深入探索。首先，当前模拟的用户活动基于事件注入，与真实用户行为的随机性和深层意图仍有差距，未来可引入更真实的行为模型或从实际日志中提取模式以提高生态效度。其次，代理在长上下文推理和抗噪声（如无关事件和冲突信号）中表现较差，尤其是主动预测任务（如按时间建议）准确率极低，这提示需要改进因果推理与时间序列建模能力，例如结合强化学习或专门的状态跟踪器。第三，基准测试仅覆盖了有限的后端服务（如邮箱、日历、文件存储），扩展至更多跨平台API（如社交媒体、支付系统）将增强现实适用性。此外，自动化数据生成管道虽提升了模型性能，但其生成的样本多样性（如训练环境）可能仍不足，通过引入对抗性生成或元学习可进一步提升鲁棒性。最后，当前缺乏对代理安全性与隐私保护的考量，未来需评估在广泛接入用户数据时如何平衡效用与风险。

### Q6: 总结一下论文的主要内容

论文提出“Claw-Anything”基准测试，用于评估在用户数字世界中拥有广泛访问权限的始终在线个人助手。现有系统因仅访问用户数字世界的狭窄切片，限制了上下文感知推理和有效辅助，而现有基准也仅提供部分用户状态，无法评估这种广泛、始终在线场景的性能。为此，Claw-Anything从三个维度扩展智能体上下文：长周期活动历史、相互依赖的后端服务、以及跨多个设备的GUI和CLI集成交互。通过多轮事件注入模拟数月的用户活动，产生复杂的世界状态和现实噪声。实验表明，最强模型GPT-5.5的pass@1仅为34.5%，远超低于先前基准，揭示了当前智能体能力与始终在线个人助手需求之间的差距。此外，论文还发布了一个自动化数据生成流程，产出2000个训练环境，使基础模型性能提升23.7%，证明了其可扩展数据基础设施的实用性。核心贡献在于定义了更广泛的智能体操作范围这一核心挑战，并构建了相应的评估基准与数据生成基础设施，为未来研究奠定基础。
