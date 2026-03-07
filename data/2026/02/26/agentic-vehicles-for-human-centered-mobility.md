---
title: "Agentic Vehicles for Human-Centered Mobility"
authors:
  - "Jiangbo Yu"
  - "Raphael Frank"
  - "Luis Miranda-Moreno"
  - "Sasan Jafarnejad"
  - "Jonatas Augusto Manzolli"
date: "2025-07-07"
arxiv_id: "2507.04996"
arxiv_url: "https://arxiv.org/abs/2507.04996"
pdf_url: "https://arxiv.org/pdf/2507.04996v8"
categories:
  - "cs.CY"
  - "cs.CE"
  - "cs.CL"
  - "cs.HC"
  - "cs.RO"
tags:
  - "Reasoning & Planning"
  - "Human-Agent Interaction"
relevance_score: 3.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Human-Agent Interaction"
  domain: "Robotics & Embodied"
  research_type: "Survey/Position Paper"
attributes:
  base_model: "N/A"
  key_technique: "Agentic Vehicle (AgV) conceptual framework"
  primary_benchmark: "N/A"
---

# Agentic Vehicles for Human-Centered Mobility

## 原始摘要

Autonomy, from the Greek autos (self) and nomos (law), refers to the capacity to operate according to internal rules without external control. Autonomous vehicles (AuVs) are therefore understood as systems that perceive their environment and execute pre-programmed tasks independently of external input, consistent with the SAE levels of automated driving. Yet recent research and real-world deployments have begun to showcase vehicles that exhibit behaviors outside the scope of this definition. These include natural language interaction with humans, goal adaptation, contextual reasoning, external tool use, and the handling of unforeseen ethical dilemmas, enabled in part by multimodal large language models (LLMs). These developments highlight not only a gap between technical autonomy and the broader cognitive and social capacities required for human-centered mobility, but also the emergence of a form of vehicle intelligence that currently lacks a clear designation. To address this gap, the paper introduces the concept of agentic vehicles (AgVs): vehicles that integrate agentic AI systems to reason, adapt, and interact within complex environments. It synthesizes recent advances in agentic systems and suggests how AgVs can complement and even reshape conventional autonomy to ensure mobility services are aligned with user and societal needs. The paper concludes by outlining key challenges in the development and governance of AgVs and their potential role in shaping future agentic transportation systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前自动驾驶车辆（AuV）概念框架的局限性，并引入一个新的概念——“具身智能体车辆”（Agentic Vehicles, AgVs）。作者指出，传统的自动驾驶定义（如SAE标准）侧重于车辆在无外部控制下执行预编程任务的能力，即“自主性”（autonomy）。然而，随着多模态大语言模型（LLMs）等技术的发展，车辆开始展现出超越这一定义的行为，例如与人类进行自然语言交互、动态调整目标、进行上下文推理、使用外部工具以及处理未预见的伦理困境。这些能力体现了“能动性”（agency），即形成、协商和适应目标，并与环境动态交互的能力。论文认为，现有“自动驾驶”的范式无法充分捕捉和指导这些更高级的认知和社会交互能力的发展，这造成了技术能力与实现“以人为本的出行”所需更广泛智能之间的鸿沟。因此，本文的核心目标是提出并定义“具身智能体车辆”这一新概念，以填补这一概念空白，并探讨其如何补充甚至重塑传统的自动驾驶范式，确保未来的出行服务更好地与用户及社会需求对齐。

### Q2: 有哪些相关研究？

相关研究主要分为三个领域：1) **自动驾驶车辆（AuVs）**：这是本文的对比基线。大量研究聚焦于AuVs的感知、规划与控制技术，如LiDAR、计算机视觉、深度学习、传感器融合以及强化学习在驾驶决策中的应用。相关文献（如[10], [12], [13], [15]）综述了这些技术进展。同时，也有研究关注AuV的伦理、法规及人机交互（如与行人交互[22]），但批评者指出这些系统在复杂社会情境下的适应性、长期结果考量和规范性推理方面存在局限[20, 21]。2) **能动性、具身智能体AI与具身出行系统**：在哲学和认知科学中，关于“能动性”的讨论历史悠久[6,7,8]。在AI领域，近期研究（如[4,5]）开始探索具备长期规划、目标重排、道德敏感性和通信能力的“具身智能体AI”系统。LLMs与记忆、反思和工具使用能力的结合是这一演进的关键推动力[4]。在交通领域，已有研究开始应用LLMs于车辆感知、导航、地图解释以及与乘客/行人的对话中[24,25,26,27]，但这些应用通常仍被框定在自动驾驶范式内，而非作为根本性具身智能体系统的使能者。此外，具身智能体AI也被用于出行行为建模、参与式规划以及偏好获取[28,29,30]。3) **LLMs在交通系统中的应用**：包括事故预测[35]、旅行者心理状态推断[34]以及通过模块化AI框架模拟规划场景[29,30,36]。本文的工作旨在弥合“自主性”与“能动性”文献之间的概念鸿沟，将具身智能体AI系统地置于智能交通系统领域，从而为AgVs这一新兴类别奠定概念基础。

### Q3: 论文如何解决这个问题？

论文通过概念定义、能力对比、架构设想和发展路线图来系统性地提出和阐述“具身智能体车辆”这一解决方案。首先，**明确定义**：论文将AgV定义为一种集成了具身智能体AI系统的智能移动系统，其核心特征是“能动性”，具体表现为：目标适应、上下文与伦理推理、对话与交互、外部工具使用以及学习与自我反思。这与仅强调任务自动化的传统AuV形成鲜明对比。其次，**详细对比**：通过一个乘客突发心脏病的具体场景（图1）和详细的对比表格（表1），论文生动地展示了AuV（继续执行原定路线）与AgV（主动检测危机、重新规划路线至医院、通知急救服务、调整驾驶风格等）在行为上的根本差异，从而凸显了“能动性”的实践内涵。第三，**提出技术基础与多层架构**：论文指出，AgV的实现依赖于多项关键技术，包括生成式AI/LLMs（用于开放目标形成和交互）、强化学习（用于不确定性下的决策）、传感器融合以及V2X通信。论文还概念化了一个多层次的AgV架构（图3），包括：感知与传感层、认知层（规划、预测、伦理推理）、交互层（自然语言与多模态交换）、执行层（底层车辆控制）以及工具接口层（与API、基础设施集成）。这一架构旨在支持AgV的复杂推理和交互能力。最后，**构建发展框架与政策建议**：为了引导AgV的负责任发展，论文提出了一个初步的“具身智能体车辆发展等级”框架（表3，表4），从Level 0（非具身）到Level 4（伦理、社会、反思性具身），逐级描述了目标调整、自然语言使用、多模态交互、伦理推理和工具使用等能力的演进。这为评估AgV的进展提供了新维度。论文还讨论了AgV可能带来的社会、伦理、安全、治理等挑战，并提出了相应的政策建议和研究方向。

### Q4: 论文做了哪些实验？

这篇论文是一篇概念性、综述性和前瞻性的文章，并非一篇提出具体新算法或模型并进行实证验证的技术论文。因此，它没有进行传统意义上的“实验”。然而，论文通过以下方式进行了深入的论证和分析：1) **概念论证与场景分析**：论文的核心“实验”是构建并分析了一个详细的对比场景（图1和表1），即乘客突发心脏病的案例。通过这个思想实验，论文清晰地、令人信服地展示了AuV与AgV在行为模式和能力上的本质区别，从而有力地支撑了其核心论点。2) **文献综述与综合**：论文对自动驾驶、具身智能体AI、LLM在交通中的应用等相关领域的研究进行了系统的梳理和综合（见第II节及表2）。这种综述本身是一种研究方法，用于识别现有研究的局限和空白，并为新概念的提出建立理论基础。3) **框架与分类法构建**：论文提出了原创性的概念框架，包括AgV的核心能力总结（图3）以及一个五级的AgV发展等级分类法（表3, 表4）。这些框架的构建是基于对现有技术趋势和理论的理解进行的逻辑推演和系统化组织，可以视为一种概念建模工作。4) **影响分析与政策推导**：论文在第IV节深入分析了AgV可能带来的广泛社会、伦理、经济影响，并据此提出了发展挑战和政策建议。这部分工作是基于逻辑推理和跨学科知识进行的系统性前瞻分析。总之，论文的“贡献”在于提出了一个清晰、有说服力的新概念和分类框架，并通过严谨的论证和文献支撑，为未来在LLM/VLM驱动的具身智能体车辆领域的研究、开发和治理指明了方向。

### Q5: 有什么可以进一步探索的点？

论文在提出AgV概念的同时，也明确指出了多个有待深入探索的研究方向和挑战：1) **具体技术实现与集成**：论文勾勒了AgV的技术基础和架构，但如何具体设计并集成感知、认知（尤其是伦理推理模块）、交互、执行和工具接口等各层，确保其高效、安全、可靠地协同工作，是巨大的工程和科研挑战。例如，如何将LLM的推理能力与实时车辆控制系统（通常要求毫秒级响应和极高可靠性）安全结合。2) **评估基准与指标**：需要开发全新的评估框架和基准测试，以衡量AgV的“能动性”水平，而不仅仅是自动驾驶的SAE等级。这包括如何量化目标适应性、交互质量、伦理决策的合理性、工具使用的有效性等。3) **安全、可靠性与验证**：AgV的复杂性和开放性带来了前所未有的安全和验证难题。如何确保其目标调整和决策不会产生意外或有害后果？如何测试其在无限长尾场景中的表现？如何防御对抗性攻击或提示注入？4) **伦理、责任与治理**：当AgV做出具有伦理色彩的决策时（如经典的“电车难题”变体），责任应如何归属？需要建立怎样的伦理准则、透明度和问责机制？跨地域、跨文化的治理框架如何协调？5) **社会接受度与人机协作**：公众对具有高度自主决策能力的AgV的信任如何建立？AgV与人类驾驶员、行人、其他AgV以及交通基础设施之间的协作协议和通信标准应如何设计？6) **资源与部署**：尽管论文提到车辆是部署本地LLM/智能体的理想平台，但如何在资源受限的边缘设备上高效运行大型模型，平衡云端与车端的计算，仍需突破。未来研究可以沿着这些方向，从概念论证转向具体的技术原型开发、仿真测试、社会实验和政策设计。

### Q6: 总结一下论文的主要内容

本文是一篇开创性的概念论文，核心贡献是提出了“具身智能体车辆”这一新范式，以超越和补充传统的“自动驾驶车辆”。论文指出，当前基于SAE等级的自动驾驶定义侧重于技术上的“自主性”（无外部控制下的任务执行），但无法涵盖由LLMs等AI进步所催生的更高级能力，如目标动态调整、上下文与伦理推理、自然语言交互和外部工具使用等“能动性”特征。为此，论文明确定义了AgV为具备这些能动性特征的智能移动系统，并通过生动场景对比和详细表格阐明了其与AuV的本质区别。论文进一步综述了相关研究，勾勒了实现AgV所需的技术基础（LLMs、RL、传感器融合等）和多层架构，并原创性地提出了一个从Level 0到Level 4的AgV发展等级框架，为评估其演进提供了新维度。最后，论文前瞻性地分析了AgV将带来的社会、伦理、安全及治理挑战，并提出了相应的政策建议。总之，本文成功地将“具身智能体AI”的前沿思想引入交通领域，为未来以人为本、具备认知和社交能力的下一代出行系统奠定了重要的概念基础和研究议程。
