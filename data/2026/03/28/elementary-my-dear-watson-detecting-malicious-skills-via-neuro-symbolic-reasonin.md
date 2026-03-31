---
title: "\"Elementary, My Dear Watson.\" Detecting Malicious Skills via Neuro-Symbolic Reasoning across Heterogeneous Artifacts"
authors:
  - "Shenao Wang"
  - "Junjie He"
  - "Yanjie Zhao"
  - "Yayi Wang"
  - "Kan Yu"
  - "Haoyu Wang"
date: "2026-03-28"
arxiv_id: "2603.27204"
arxiv_url: "https://arxiv.org/abs/2603.27204"
pdf_url: "https://arxiv.org/pdf/2603.27204v1"
categories:
  - "cs.CR"
  - "cs.SE"
tags:
  - "Agent Security"
  - "Malicious Skill Detection"
  - "Neuro-Symbolic Reasoning"
  - "Agent Supply Chain"
  - "Tool-Augmented Agent"
  - "Static Analysis"
  - "Benchmark Evaluation"
relevance_score: 7.5
---

# "Elementary, My Dear Watson." Detecting Malicious Skills via Neuro-Symbolic Reasoning across Heterogeneous Artifacts

## 原始摘要

Skills are increasingly used to extend LLM agents by packaging prompts, code, and configurations into reusable modules. As public registries and marketplaces expand, they form an emerging agentic supply chain, but also introduce a new attack surface for malicious skills. Detecting malicious skills is challenging because relevant evidence is often distributed across heterogeneous artifacts and must be reasoned in context. Existing static, LLM-based, and dynamic approaches each capture only part of this problem, making them insufficient for robust real-world detection. In this paper, we present MalSkills, a neuro-symbolic framework for malicious skills detection. MalSkills first extracts security-sensitive operations from heterogeneous artifacts through a combination of symbolic parsing and LLM-assisted semantic analysis. It then constructs the skill dependency graph that links artifacts, operations, operands, and value flows across the skill. On top of this graph, MalSkills performs neuro-symbolic reasoning to infer malicious patterns or previously unseen suspicious workflows. We evaluate MalSkills on a benchmark of 200 real-world skills against 5 state-of-the-art baselines. MalSkills achieves 93% F1, outperforming the baselines by 5~87 percentage points. We further apply MalSkills to analyze 150,108 skills collected from 7 public registries, revealing 620 malicious skills. As for now, we have finished reviewing 100 of them and identified 76 previously unknown malicious skills, all of which were responsibly reported and are currently awaiting confirmation from the platforms and maintainers. These results demonstrate the potential of MalSkills in securing the agentic supply chain.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决LLM智能体生态系统中，由第三方技能（skills）构成的“智能体供应链”所面临的新型安全威胁问题。随着技能（将提示词、代码和配置打包成可重用模块）的普及，公共注册中心和市场不断扩张，这为恶意技能提供了新的攻击面，可能导致凭证窃取、远程代码执行和智能体劫持等风险。

现有检测方法存在明显不足，主要分为三类：1) 基于静态规则的方法，虽然高效、可扩展且易于审计，但严重依赖对已知敏感行为的预定义启发式规则，难以应对通过变体重写、无文件攻击、第三方库API或自然语言提示表达的恶意逻辑；2) 基于LLM的语义分析方法，虽能提供更强的语义泛化能力，但容易被嵌入的提示词或看似良性的描述误导；3) 基于动态沙箱或运行时监控的方法，其有效性依赖于执行覆盖率，可能漏检未触发的潜在行为，且可能被环境感知或沙箱敏感的样本规避，甚至遭受沙箱逃逸攻击。

因此，本文的核心问题是：如何设计一种鲁棒且有效的检测框架，以应对恶意技能检测中证据分散于异构工件（如提示词、代码、清单）、威胁模型具有对抗性、以及风险高度依赖上下文这三大挑战。论文提出的MalSkills框架通过神经符号推理，整合跨工件的证据提取、技能依赖图建模和上下文推理，旨在实现对已知和未知恶意行为模式的精准检测。

### Q2: 有哪些相关研究？

本文的相关研究主要分为三类检测方法，它们各自存在局限性，而本文提出的MalSkills框架则通过神经符号推理整合了它们的优势。

**1. 静态检测方法**：这类方法（如Skill-Sec-Scan）通过预定义的规则、签名或模式匹配来扫描技能构件（如代码、提示词），以识别可疑内容。其优点是高效、可扩展，但缺点是容易被绕过，例如当恶意行为通过逻辑重写、看似良性的API或跨构件组合来表达时。

**2. 基于LLM的语义分析方法**：这类方法（如Skill Scanner、Nova-Proximity）利用大语言模型来解释提示词、脚本和文档，以检测可疑意图或隐藏的恶意行为。其优势在于能超越手工规则进行泛化，但缺点是大模型可能被提示词注入、混淆描述或对抗性构造的上下文所误导。

**3. 动态分析与沙箱监控**：这类方法（如MASB）在受控环境中执行技能，并通过观察运行时行为来检测恶意性。其优势在于能揭示具体的攻击动作，但效果受限于执行覆盖范围，并且可能被环境敏感或沙箱感知的样本所规避。

**本文工作与上述研究的关系与区别**：现有方法各自只解决了问题的一部分（如表格所示，它们在“跨构件”推理方面支持有限或不支持），且均未系统性地对跨异构构件（如提示、代码、配置）的分布式证据进行上下文关联推理。本文提出的MalSkills是一个**神经符号框架**，它首先通过符号解析和LLM辅助的语义分析从异构构件中提取安全敏感操作，然后构建连接这些操作的技能依赖图，最后在该图上进行神经符号推理以推断恶意模式或先前未知的可疑工作流。这种方法整合了静态分析的精确性、LLM的语义理解能力，并引入了跨构件的显式关系推理，从而实现了更鲁棒和全面的检测。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MalSkills的神经符号推理框架来解决恶意技能检测问题。该框架的核心方法分为三个阶段：安全敏感操作（SSO）提取、技能依赖图（SDG）生成以及神经符号推理。

首先，在SSO提取阶段，框架采用**混合提取策略**。一方面，使用基于解析的符号提取器，通过预定义的启发式规则（如识别`subprocess.run`、`requests.get`等API调用）从源代码、配置等异构工件中提取显式的安全敏感操作。另一方面，针对规则难以覆盖的隐式操作（如通过第三方库、自然语言提示隐含的恶意行为），引入了**LLM辅助的神经提取器**。该组件通过精心设计的提示模板，引导LLM从非结构化文本中提取结构化证据，并将其映射到固定的SSO分类中。此外，框架还设计了**神经到符号的反馈循环**，将LLM稳定发现的模式（如特定包装器调用）抽象为新的符号规则，从而持续增强符号规则库。

其次，在SDG生成阶段，框架将分散的SSO记录组织成一个统一的、操作数中心的**技能依赖图**。该图包含四种节点（工件、SSO、操作数、值）和三种边（包含、拥有操作数、值流）。构建过程结合了**符号操作数解析**（利用静态指向分析追踪操作数的显式数据流）和**LLM辅助的操作数推断**（用于归一化语义等价的操作数并推断静态分析无法恢复的隐式值流）。SDG有效地连接了跨工件的证据，刻画了安全敏感操作之间的依赖关系和数据传播路径，为后续推理提供了结构化上下文。

最后，在神经符号推理阶段，框架在SDG之上进行恶意行为检测。**基于模式的符号推理**部分使用预定义的恶意模式（如信息窃取链、命令与控制活动），这些模式要求参与的操作在SDG中通过操作数依赖或值流边语义关联，从而检测已知威胁。更重要的是，框架引入了**基于学习的神经推理**来发现先前未知的可疑工作流。它通过图神经网络（GNN）等模型学习SDG的表示，并利用异常检测或分类器来识别偏离正常模式或表现出可疑语义结构的子图。符号与神经组件协同工作：符号推理提供可解释的已知模式匹配，而神经推理扩展了对新型和复杂攻击的检测能力。

整体而言，MalSkills的创新点在于：1) **异构证据的融合提取**，结合符号规则与LLM语义分析，全面覆盖显式与隐式安全操作；2) **操作数中心的价值依赖图构建**，通过混合解析与推断，重建跨工件的语义链接；3) **神经符号协同推理架构**，既利用符号规则实现可解释的已知模式检测，又借助神经模型发现未知可疑工作流，二者通过反馈循环持续优化。该框架通过这种多层次、混合方法，有效应对了恶意技能检测中证据分散、语境依赖的挑战。

### Q4: 论文做了哪些实验？

论文进行了全面的实验评估，主要围绕四个研究问题展开。实验设置方面，作者在配备256 CPU、1TB内存和NVIDIA RTX 4090 GPU的Ubuntu服务器上，使用Python实现了MalSkills原型（约7.9K行代码），并集成了Semgrep（含2,665条多语言规则）和YASA静态分析器。默认使用gpt-5.3-codex-medium作为LLM模型。

数据集包括：1) **MalSkillsBench**：包含200个真实技能（100个恶意技能+100个良性技能），恶意样本从ClawHub历史提交中收集并去重，良性样本选自热门技能，保留了原始异构工件结构；2) **Wild-Skills-150K**：从7个公共注册表收集的150,108个去重后技能，用于大规模扫描。

对比方法涵盖了当前社区代表性的恶意技能检测工具，包括静态分析、LLM分析和动态分析三类，具体为**Skill Scanner**、**Nova-Proximity**、**Skill-Sec-Scan**、**Caterpillar**和**MASB**。所有基线均使用相同LLM模型并在相同环境下运行。

主要结果如下：在MalSkillsBench上，MalSkills的**F1分数达到93%**，显著优于基线（超出5~87个百分点）。具体指标显示，其精确度（Precision）和召回率（Recall）均保持高水平。在大规模扫描中，MalSkills在150,108个技能中识别出**620个恶意技能**；对其中100个已完成人工审核，确认了**76个此前未知的恶意技能**，并已报告给相关平台。这些结果验证了MalSkills在检测效果和实际应用中的优势。

### Q5: 有什么可以进一步探索的点？

该论文提出的神经符号框架在恶意技能检测上取得了显著效果，但其局限性和未来探索方向仍值得深入。首先，框架高度依赖对异构工件的解析和语义分析，其准确性受限于LLM的理解能力和符号解析规则的完备性，可能无法覆盖所有新型或高度混淆的攻击模式。其次，当前评估主要基于已知数据集，在真实世界大规模、动态演化的技能生态中，其泛化能力和持续检测效率有待验证。

未来研究方向可考虑：一、增强框架的适应性，引入在线学习和增量更新机制，使系统能自动识别新型攻击模式并更新规则库。二、探索跨技能关联分析，当前检测主要针对单个技能，未来可研究技能组合使用时可能产生的协同攻击风险。三、提升解释性，虽然采用了神经符号方法，但如何向安全分析师提供更直观、可操作的推理过程仍需改进。四、考虑隐私保护，在分析技能时如何平衡深度检测与用户数据隐私，特别是在处理涉及敏感信息的技能时。这些方向将有助于构建更健壮、可扩展的智能体供应链安全体系。

### Q6: 总结一下论文的主要内容

该论文提出了一个名为MalSkills的神经符号推理框架，用于检测LLM智能体生态中恶意技能（malicious skills）的安全威胁。核心问题是：随着技能（打包了提示词、代码和配置的可重用模块）在公共注册表中广泛传播，形成了新兴的智能体供应链，但也引入了新的攻击面，而现有静态、LLM或动态检测方法各自仅能捕捉部分证据，难以实现鲁棒检测。

方法上，MalSkills采用三阶段设计：首先，通过符号解析与LLM辅助语义分析相结合，从异构工件（如代码、提示、清单）中提取安全敏感操作；其次，构建技能依赖图，关联跨工件的操作、操作数和值流；最后，在该图上进行神经符号推理，以识别恶意模式或先前未见的可疑工作流。

主要结论显示，在包含200个真实技能的基准测试中，MalSkills的F1分数达到93%，优于5个先进基线5~87个百分点。进一步对7个公共注册表的150,108个技能进行分析，发现了620个恶意技能，其中随机审查的100个里确认了76个先前未知的恶意案例。这表明MalSkills能有效保障智能体供应链安全，其结合符号精确性与LLM语义泛化的方法，为跨工件上下文推理提供了新思路。
