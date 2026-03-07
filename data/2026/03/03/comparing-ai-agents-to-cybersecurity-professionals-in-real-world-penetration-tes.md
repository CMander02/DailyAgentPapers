---
title: "Comparing AI Agents to Cybersecurity Professionals in Real-World Penetration Testing"
authors:
  - "Justin W. Lin"
  - "Eliot Krzysztof Jones"
  - "Donovan Julian Jasper"
  - "Ethan Jun-shen Ho"
  - "Anna Wu"
date: "2025-12-10"
arxiv_id: "2512.09882"
arxiv_url: "https://arxiv.org/abs/2512.09882"
pdf_url: "https://arxiv.org/pdf/2512.09882v2"
categories:
  - "cs.AI"
  - "cs.CR"
  - "cs.CY"
tags:
  - "Multi-Agent Systems"
  - "Tool Use & API Interaction"
relevance_score: 7.5
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Tool Use & API Interaction"
  domain: "Cybersecurity"
  research_type: "Empirical Study/Analysis"
attributes:
  base_model: "N/A"
  key_technique: "ARTEMIS (multi-agent framework with dynamic prompt generation, arbitrary sub-agents, automatic vulnerability triaging)"
  primary_benchmark: "N/A"
---

# Comparing AI Agents to Cybersecurity Professionals in Real-World Penetration Testing

## 原始摘要

We present the first comprehensive evaluation of AI agents against human cybersecurity professionals in a live enterprise environment. We evaluate ten cybersecurity professionals alongside six existing AI agents and ARTEMIS, our new agent scaffold, on a large university network consisting of ~8,000 hosts across 12 subnets. ARTEMIS is a multi-agent framework featuring dynamic prompt generation, arbitrary sub-agents, and automatic vulnerability triaging. In our comparative study, ARTEMIS placed second overall, discovering 9 valid vulnerabilities with an 82% valid submission rate and outperforming 9 of 10 human participants. While existing scaffolds such as Codex and CyAgent underperformed relative to most human participants, ARTEMIS demonstrated technical sophistication and submission quality comparable to the strongest participants. We observe that AI agents offer advantages in systematic enumeration, parallel exploitation, and cost -- certain ARTEMIS variants cost $18/hour versus $60/hour for professional penetration testers. We also identify key capability gaps: AI agents exhibit higher false-positive rates and struggle with GUI-based tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI网络安全风险评估与现实环境脱节的问题。随着AI能力快速提升并被恶意行为者用于网络攻击，准确评估AI在真实网络环境中的攻防能力变得至关重要。然而，现有评估方法存在明显不足：许多基准测试仅关注问答表现或静态漏洞检测，而模拟夺旗挑战或复现已知漏洞的测试又缺乏真实环境的复杂性、交互性和噪声。这些抽象化的测试忽略了现实攻击中的关键环节，例如利用窃取的凭证、组合配置错误、钓鱼攻击和利用未修补漏洞等，导致评估结果无法准确反映AI在实际网络环境中的真实风险和能力。

因此，本文的核心问题是：在真实的、大规模的企业网络环境中，AI智能体与人类网络安全专业人员在渗透测试任务上的实际表现究竟如何？为了回答这个问题，研究团队首次在一个包含约8000台主机、12个子网的大学真实网络环境中，对10名网络安全专业人员和6个现有AI智能体（以及他们新提出的ARTEMIS智能体框架）进行了全面的对比评估。通过这项研究，论文试图弥合现有评估与现实风险之间的差距，为理解AI在真实网络安全攻防中的实际能力和局限性提供实证依据。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：代理风险评估基准和代理架构发展。

在**代理风险评估基准**方面，现有研究主要通过问答任务、代码片段漏洞检测、CTF竞赛或复现公开漏洞（CVE）来评估AI代理在攻击性网络安全中的表现。代表性基准包括Cybench、CVEBench和BountyBench的“检测”任务。尽管有证据表明威胁行为体已成功将AI用于实际攻击，但领先的基础模型在这些基准上的得分仍普遍低于50%。此外，一些基准（如Cybench、NYU CTF Bench和BountyBench）尝试通过解题时间、团队得分或漏洞赏金金额来建立人类基线，甚至直接在实时攻防竞赛中对比AI与人类。然而，本文指出这些基准忽略了真实生产环境的复杂性，且未能捕捉自主AI系统带来的核心风险——即其前所未有的速度和横向扩展效率。

在**代理架构发展**方面，相关研究从早期的单循环代理，迅速发展到能够协同工作的多代理团队，这些团队可执行多主机网络攻击、利用零日漏洞，甚至包含能发现、利用和修补CVE的复杂AI模糊测试器。另有研究专注于开发辅助人类研究人员的半自主代理工具，但其尚未实现完全自主的攻击性安全操作。与本文工作最为相关的是自主框架MAPTA，但它尚未经过全面评估。本文提出的ARTEMIS正是在此基础上发展出的一个多代理框架，并首次在真实生产环境（大型大学网络）中进行了全面评估，直接对比了AI代理与人类网络安全专家的表现，弥补了现有研究缺乏真实环境综合评估的空白。

### Q3: 论文如何解决这个问题？

论文通过设计并应用一个名为ARTEMIS的新型多智能体框架来解决在真实企业环境中进行渗透测试的挑战。该框架的核心目标是克服现有AI智能体在复杂、长周期网络安全任务中的局限性，如上下文管理能力弱、子智能体灵活性不足以及缺乏专业网络安全知识集成。

**整体框架与主要模块**：ARTEMIS是一个三层架构的多智能体系统。其核心包括：1）一个高层**监督器（supervisor）**，负责管理整体工作流程和任务规划；2）一个可动态创建的**任意子智能体群（swarm of arbitrary sub-agents）**，每个子智能体在执行特定任务时，会由专门的提示生成模块为其动态生成包含专家知识的系统提示，以确保使用正确的工具和流程；3）一个**漏洞分类验证模块（triager）**，用于自动验证提交漏洞的相关性和可复现性，旨在减少误报和重复提交。

**关键技术设计与创新点**：首先，ARTEMIS引入了**动态提示生成**技术，能够为每个具体任务定制专家级系统提示，从而提升子智能体执行的专业性和准确性。其次，框架采用了**任务列表、笔记系统和智能摘要**机制，使其能够将工作拆分为多个会话，在长时间运行中通过总结进展、清空上下文并从中断处恢复，从而实现了**远超现有智能体的长周期任务执行能力**。此外，其**自动漏洞分类验证**模块直接针对AI智能体误报率高的问题，通过技术验证提升提交质量。与Codex、CyAgent等现有单智能体或架构僵化的框架相比，ARTEMIS的**多智能体协同和灵活扩展能力**是其关键创新。值得注意的是，论文强调ARTEMIS并非旨在提升模型固有的网络安全知识（因此在Cybench等单机CTF挑战中未显示出显著优势），而是通过优化**复杂生产环境中的执行流程、规划和长期任务管理**来提升整体表现，这使其在真实异构网络（约8000台主机）的测试中，在发现有效漏洞数量和技术复杂度上能够媲美顶尖人类专家。

### Q4: 论文做了哪些实验？

该研究在真实企业环境中进行了首次AI代理与人类网络安全专家的渗透测试对比实验。实验设置方面，研究在一个包含约8000台主机、12个子网的大型大学网络中进行，评估了10名网络安全专业人员、6个现有AI代理（包括Codex、Claude Code、CyAgent、Incalmo和MAPTA）以及新提出的多代理框架ARTEMIS。ARTEMIS采用动态提示生成、任意子代理和自动漏洞分类机制，测试了两种配置：A₁使用GPT-5作为监督器和子代理模型，A₂采用多模型集成（Claude Sonnet 4、OpenAI o3等）作为监督器，子代理使用Claude Sonnet 4。所有代理在与人类相同的虚拟机环境中运行，ARTEMIS执行16小时，但仅评估前10小时以保证与人类（10小时测试时间）的可比性；其他代理因无法持续工作10小时以上而运行至完成。

主要结果方面，参与者共发现49个已验证的独特漏洞，每人发现数量在3至13个之间。ARTEMIS总体排名第二，发现了9个有效漏洞，有效提交率达82%，超过了10名人类参与者中的9名。关键数据指标显示：ARTEMIS的并行子代理峰值达8个，平均每轮迭代有2.82个并发子代理；其成本优势显著，某些变体每小时成本约18美元，而专业渗透测试员成本为60美元。相比之下，现有代理表现较差：Claude Code和MAPTA直接拒绝任务，Incalmo因僵化的任务图在早期侦察阶段停滞，三者均未发现漏洞；Codex和CyAgent虽能运行但表现不佳，例如Codex在20分钟内即提前结束。实验还揭示了AI代理的局限性：其误报率高于人类，且在基于GUI的任务上存在困难。ARTEMIS的技术复杂性和提交质量与最强人类参与者相当，但模型能力差异显著影响结果——使用GPT-5的A₁优于50%的人类，而使用Claude Sonnet 4的A₂表现较弱，凸显了模型性能与框架设计的共同作用。

### Q5: 有什么可以进一步探索的点？

该论文展示了AI在渗透测试领域的潜力，但也揭示了明显的局限性。首先，AI代理的误报率较高，且难以处理基于图形用户界面（GUI）的复杂任务，这限制了其在真实场景中的全面应用。其次，ARTEMIS在缺乏提示的情况下可能错过某些漏洞，表明其在自主识别漏洞模式方面存在瓶颈，而非技术执行能力不足。

未来研究方向可围绕以下几点展开：一是提升AI的上下文理解与推理能力，通过引入更强大的基础模型或改进提示工程，使其能更准确地筛选自动化工具输出，降低误报。二是开发多模态能力，结合计算机视觉技术处理GUI任务，扩展AI在图形化环境中的操作范围。三是优化成本效益，进一步降低API调用开销，例如通过模型蒸馏或本地化部署。此外，可探索人机协同模式，将AI的系统化枚举与人类的创造性思维结合，形成互补优势。最后，需在更复杂、动态的网络环境中进行长期评估，以验证AI代理的鲁棒性和适应性。

### Q6: 总结一下论文的主要内容

该论文首次在真实企业环境中对AI智能体与人类网络安全专家进行了全面的渗透测试对比评估。研究引入了一个名为ARTEMIS的新型多智能体框架，其具备动态提示生成、任意子智能体调用和自动漏洞分级能力。在包含约8000台主机的大学网络测试中，ARTEMIS总体表现排名第二，发现了9个有效漏洞，提交有效率达82%，超过了10位人类参与者中的9位。研究表明，AI智能体在系统枚举、并行利用和成本方面具有优势（ARTEMIS变体成本约18美元/小时，远低于专业渗透测试员的60美元/小时），但也存在误报率较高、难以处理基于GUI的任务等能力差距。论文通过分析双方战术、技术和程序，为现实的AI网络安全评估奠定了基础，并开源了ARTEMIS框架以促进防御工具普及。
