---
title: "ACIArena: Toward Unified Evaluation for Agent Cascading Injection"
authors:
  - "Hengyu An"
  - "Minxi Li"
  - "Jinghuai Zhang"
  - "Naen Xu"
  - "Chunyi Zhou"
  - "Changjiang Li"
  - "Xiaogang Xu"
  - "Tianyu Du"
  - "Shouling Ji"
date: "2026-04-09"
arxiv_id: "2604.07775"
arxiv_url: "https://arxiv.org/abs/2604.07775"
pdf_url: "https://arxiv.org/pdf/2604.07775v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.CR"
tags:
  - "多智能体系统"
  - "安全与对抗"
  - "评估基准"
  - "鲁棒性"
  - "Agent Cascading Injection"
relevance_score: 7.5
---

# ACIArena: Toward Unified Evaluation for Agent Cascading Injection

## 原始摘要

Collaboration and information sharing empower Multi-Agent Systems (MAS) but also introduce a critical security risk known as Agent Cascading Injection (ACI). In such attacks, a compromised agent exploits inter-agent trust to propagate malicious instructions, causing cascading failures across the system. However, existing studies consider only limited attack strategies and simplified MAS settings, limiting their generalizability and comprehensive evaluation. To bridge this gap, we introduce ACIArena, a unified framework for evaluating the robustness of MAS. ACIArena offers systematic evaluation suites spanning multiple attack surfaces (i.e., external inputs, agent profiles, inter-agent messages) and attack objectives (i.e., instruction hijacking, task disruption, information exfiltration). Specifically, ACIArena establishes a unified specification that jointly supports MAS construction and attack-defense modules. It covers six widely used MAS implementations and provides a benchmark of 1,356 test cases for systematically evaluating MAS robustness. Our benchmarking results show that evaluating MAS robustness solely through topology is insufficient; robust MAS require deliberate role design and controlled interaction patterns. Moreover, defenses developed in simplified environments often fail to transfer to real-world settings; narrowly scoped defenses may even introduce new vulnerabilities. ACIArena aims to provide a solid foundation for advancing deeper exploration of MAS design principles.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体系统（MAS）中一个新兴且关键的安全问题——智能体级联注入（ACI）攻击的全面评估与防御框架缺失问题。随着基于大语言模型的智能体协作系统在代码生成、数学推理乃至企业级应用中的快速部署，其通过信息共享和协作提升能力的同时，也引入了新的安全风险。攻击者可以通过外部输入、智能体配置文件或智能体间消息等多个攻击面，入侵单个智能体，并利用智能体间的信任关系，使恶意指令在整个系统中级联传播，导致系统故障甚至崩溃。

然而，现有研究存在明显不足：首先，威胁场景不完整，大多只考虑有限的攻击策略（如仅针对特定攻击面或目标）或简化的MAS设置，难以系统性地识别潜在漏洞；其次，缺乏标准化的评估环境，现有工作使用的MAS实现过于简化，与真实系统差异大，导致研究结论难以泛化；最后，现有代码库的扩展性有限，模块化设计不足，难以快速适配新的任务、系统或攻防模块。

因此，本文的核心问题是：如何建立一个统一、全面且可扩展的框架，以系统评估多智能体系统在面临多样化ACI攻击时的鲁棒性，并深入理解其脆弱性根源。为此，论文提出了ACIArena框架，旨在通过覆盖多攻击面、多攻击目标的系统性测试套件、统一的接口规范以及模块化设计，填补当前研究在全面基准测试和可扩展性方面的空白，为深入探索MAS设计原则和安全防御奠定基础。

### Q2: 有哪些相关研究？

本文的相关工作主要涉及三类研究：多智能体系统（MAS）的构建、针对MAS的级联注入攻击（ACI）以及智能体系统的安全评测。

在多智能体系统方面，已有研究探索了多种协作范式。例如，CAMEL和AutoGen专注于用户-助理角色扮演；MetaGPT和ChatDev在固定的软件开发流程中分配专业角色（如程序员、评审员）；而MAD和LLM-Debate等辩论式系统则让智能体提出并批判解决方案。近期研究还关注动态适应机制，使智能体能根据任务需求重新配置角色与通信策略。本文提出的ACIArena框架支持并集成了这些多样化的MAS实现，旨在提供一个统一的评估平台。

在攻击研究方面，已有工作揭示了ACI攻击的风险，即攻击者通过向关键组件或消息注入恶意提示来危害整个系统。例如，有研究通过配置文件注入引入恶意智能体；有工作针对多智能体辩论系统，利用从众偏见传播错误信息；还有研究向MAS注入递归和传染性提示以破坏协作。然而，这些研究通常只考虑有限的攻击策略和简化的MAS设置。本文的ACIArena则系统性地涵盖了多个攻击面（如外部输入、智能体档案、内部消息）和攻击目标（如指令劫持、任务破坏、信息窃取），从而提供了更全面和通用的评估。

在安全评测方面，现有的智能体安全基准（如AgentDojo、InjecAgent、Agent Security Bench）主要关注单智能体场景，对多智能体协作中产生的漏洞探索不足。虽然已有研究引入了针对MAS的ACI攻击，但缺乏一个全面的基准。本文的ACIArena正是为了填补这一空白，它作为首个专门为MAS设计的基准，提供了一个可动态扩展新系统及攻防模块的统一评测框架，并建立了包含1,356个测试用例的基准，以系统评估MAS的鲁棒性。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为ACIArena的统一评估框架来解决多智能体系统（MAS）在面临代理级联注入（ACI）攻击时的鲁棒性评估问题。其核心方法是提供一个系统化的评估套件，覆盖多种攻击面和攻击目标，并支持模块化扩展。

在整体架构设计上，ACIArena首先定义了统一的规范，以同时支持MAS的构建和攻防模块的集成。框架集成了六种广泛使用的MAS实现（如MetaGPT、AutoGen等），并将它们异构的代码库重构为统一的执行入口点，从而实现标准化评估。框架包含三个主要组件：1）**良性任务域**：选取数学推理、代码生成、科学和医学四个需要多步协作和结构化推理的领域，并采用自动化流程筛选高复杂性、高可分解性和低模糊性的任务，以确保能有效评估MAS的协作能力。2）**ACI攻击实例**：设计了针对劫持、破坏和信息窃取三大目标的28种攻击，攻击面覆盖外部输入、代理配置和代理间消息。攻击提示的生成采用一种无需梯度优化的自动化演化过程：从初始攻击目标出发，通过预定义的变异算子集生成变体，并基于LLM评判器根据隐蔽性（与良性提示的相似度）和危害性（响应与初始目标的匹配度）进行选择，迭代优化直至收敛。3）**评估套件**：将良性任务与攻击实例配对，构建了包含1356个测试用例的基准，并分为针对不同攻击目标的三个评估套件。

关键技术包括：1）**统一的评估接口**：通过标准化不同MAS的执行流程，实现了跨系统的公平比较。2）**攻击的自动化演化**：利用基于LLM的变异-选择循环，生成高效且隐蔽的攻击策略，避免了手工设计的局限性。3）**多维评估指标**：不仅采用良性效用（BU）、攻击成功率（ASR）和受攻击下效用（UA）来评估最终输出，还创新性地提出了传播脆弱性指数（PVI），该指数结合恶意代理到最终响应的最小拓扑距离和相应的攻击成功率，量化攻击在系统内的传播倾向，从而更深入地理解攻击机理。

创新点在于首次建立了系统化、可扩展的ACI评估基准，突破了以往研究仅考虑有限攻击策略和简化MAS设置的局限。ACIArena强调，仅通过拓扑结构评估MAS鲁棒性是不足的，需要精心设计角色并控制交互模式；同时揭示了在简化环境中开发的防御措施往往难以迁移到现实场景，甚至可能引入新漏洞。该框架为深入探索MAS设计原则奠定了坚实基础。

### Q4: 论文做了哪些实验？

论文构建了ACIArena统一评估框架，并基于此进行了系统性实验。实验设置上，研究覆盖了多个攻击面（外部输入、智能体档案、智能体间消息）和攻击目标（指令劫持、任务破坏、信息窃取），并假设系统中存在单个恶意智能体以模拟更现实的攻击条件。评估使用了三个不同规模的LLM：GPT-4o、GPT-4o-mini和Qwen2.5-7B-Instruct。

数据集与基准测试方面，ACIArena建立了一个包含1,356个测试用例的基准，涵盖了数学、代码、科学和医疗四个任务领域，并对六种广泛使用的多智能体系统（MAS）实现（如CAMEL、AutoGen、AgentVerse、MetaGPT、Self Consistency、LLM Debate）进行了评估。主要对比了这些系统在基准效用（BU）、攻击成功率（ASR）和效用保持率（UA）等关键指标上的表现。

主要结果包括：1）当前MAS普遍对ACI攻击高度脆弱，尤其在代码生成领域，某些系统在劫持或破坏攻击下的ASR高达90%-100%（如LLM Debate在劫持攻击下ASR达100.00%），而效用（UA）则大幅下降。2）仅从拓扑结构评估MAS鲁棒性是不充分的，例如AgentVerse和CAMEL具有相同智能体数量且非简单设计，但表现出截然不同的韧性水平。3）鲁棒性与效用之间存在权衡，例如CAMEL在多个领域和威胁场景下ASR最低（劫持套件下可达0.0），但这源于其效用降低，系统可能直接不执行注入指令而非成功抵抗。4）精心设计的角色和受控的交互模式对鲁棒性至关重要，例如包含关键审查角色（如AgentVerse和CAMEL中的批评者）的系统通常整体安全性更强，而关键角色若仅限于单向交互（如CAMEL）则能在保持鲁棒性的同时有效抑制恶意传播。5）在简化环境中开发的防御措施（如BERT检测器、分隔符、Sandwich、AGrail、G-Safeguard）往往难以迁移到真实场景，甚至可能引入新漏洞；而论文提出的ACI-Sentinel防御方法在降低ASR方面表现更优，例如在AutoGen上能将劫持攻击的ASR从92.78%降至8.06%。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其评估框架主要针对预设的攻击面和目标，可能无法覆盖未来更复杂或未知的攻击模式。未来研究可探索更具动态性和适应性的攻击策略，例如利用多模态信息或社交工程手段进行渗透。此外，当前防御机制在真实场景中的泛化能力不足，需开发更具鲁棒性的跨环境迁移方案。可能的改进方向包括引入强化学习让系统在对抗中自我进化，或设计基于因果推理的信任验证机制，以更精准地识别恶意指令传播。同时，可考虑将人类反馈纳入防御循环，增强系统对隐蔽攻击的感知能力。

### Q6: 总结一下论文的主要内容

该论文针对多智能体系统（MAS）中存在的Agent Cascading Injection（ACI）安全风险，提出了首个统一评估框架ACIArena。核心问题是现有研究攻击策略有限、评估环境简化，导致泛化性和全面性不足。ACIArena通过建立统一规范，支持构建MAS及攻防模块，覆盖六个常用MAS实现，并提供了包含1,356个测试用例的基准，系统评估了MAS在多种攻击面（外部输入、智能体档案、智能体间消息）和目标（指令劫持、任务破坏、信息窃取）下的鲁棒性。主要结论指出，仅通过拓扑结构评估MAS鲁棒性不足，需精心设计角色并控制交互模式；且在简化环境中开发的防御措施往往难以迁移到现实场景，甚至可能引入新漏洞。该框架为深入探索MAS设计原则奠定了坚实基础。
