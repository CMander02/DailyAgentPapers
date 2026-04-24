---
title: "CI-Work: Benchmarking Contextual Integrity in Enterprise LLM Agents"
authors:
  - "Wenjie Fu"
  - "Xiaoting Qin"
  - "Jue Zhang"
  - "Qingwei Lin"
  - "Lukas Wutschitz"
  - "Robert Sim"
  - "Saravan Rajmohan"
  - "Dongmei Zhang"
date: "2026-04-23"
arxiv_id: "2604.21308"
arxiv_url: "https://arxiv.org/abs/2604.21308"
pdf_url: "https://arxiv.org/pdf/2604.21308v1"
categories:
  - "cs.CR"
  - "cs.CL"
tags:
  - "LLM Agent安全"
  - "企业Agent基准测试"
  - "上下文完整性"
  - "隐私泄露"
  - "信息流评估"
relevance_score: 8.5
---

# CI-Work: Benchmarking Contextual Integrity in Enterprise LLM Agents

## 原始摘要

Enterprise LLM agents can dramatically improve workplace productivity, but their core capability, retrieving and using internal context to act on a user's behalf, also creates new risks for sensitive information leakage. We introduce CI-Work, a Contextual Integrity (CI)-grounded benchmark that simulates enterprise workflows across five information-flow directions and evaluates whether agents can convey essential content while withholding sensitive context in dense retrieval settings. Our evaluation of frontier models reveals that privacy failures are prevalent (violation rates range from 15.8%-50.9%, with leakage reaching up to 26.7%) and uncovers a counterintuitive trade-off critical for industrial deployment: higher task utility often correlates with increased privacy violations. Moreover, the massive scale of enterprise data and potential user behavior further amplify this vulnerability. Simply increasing model size or reasoning depth fails to address the problem. We conclude that safeguarding enterprise workflows requires a paradigm shift, moving beyond model-centric scaling toward context-centric architectures.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决企业级LLM代理在信息检索和任务执行过程中面临的敏感信息泄露问题。研究背景是，LLM已从静态文本生成器发展为能调用外部工具的动态代理，在企业工作流程中可检索和操作海量内部数据（如邮件、会议记录等）以代表用户执行复杂任务。然而，现有方法存在明显不足：第一，当前评估通常隔离单一信息流，忽视了企业环境中多个信息流同时交织的真实情况；第二，已有的隐私效用评估受限于简单、孤立的上下文，主要衡量任务完成程度而非区分关键信息与敏感信息的上下文精度；第三，现有研究依赖简化场景或短属性，无法复现真实企业数据的大规模和密度，代理需在“企业数据干草堆”中辨别敏感的“针”。因此，本文的核心问题是：如何构建一个基于上下文完整性（Contextual Integrity, CI）理论的高保真基准，系统评估LLM代理在企业工作流中能否在传递必要内容的同时抑制敏感上下文，并揭示任务效用与隐私保护之间的权衡。

### Q2: 有哪些相关研究？

相关研究主要分为两类。第一类是**情境隐私基准**，如ConfAide、CI-Bench评估静态隐私推理，PrivacyLens和CIMemories则关注动态代理轨迹中的隐私泄露。这些工作聚焦日常生活场景，基于法庭案例或物联网视角，而本文专门针对企业环境，隐私规范受复杂的组织层级和工作流约束。第二类是**企业代理评估**，如Workbench、OfficeBench、WorkArena等基准评估代理的任务执行效用，TheAgentCompany和CRMArena则聚焦软件工程或客服等特定领域。这些工作主要关注任务成功率和实用性，忽视了隐私泄露风险。本文的创新在于填补了这一空白，在评估企业LLM代理时同时衡量任务效用和情境隐私保护，揭示了二者间的权衡关系，并强调需要从模型中心转向情境中心架构来解决企业数据泄露问题。

### Q3: 论文如何解决这个问题？

CI-Work 通过构建一个基于上下文完整性（CI）理论的基准测试框架来评估企业级 LLM 智能体的隐私风险。其核心方法包括四个阶段：**任务导向种子生成**、**上下文条目生成**、**案例情节生成**和**轨迹模拟与评估**。首先，它基于标准组织沟通分类法，手动生成覆盖五种信息流方向（下行、上行、横向、对角、外部）的高质量种子，并采用人类在环的迭代生成范式确保场景的真实性和结构多样性。其次，采用 LLM 驱动的模板化方法，为每个种子同时生成严格不相交的**必要条目**（完成任务所需）和**敏感条目**（泄露隐私违规），并通过自迭代精炼机制（LLM 盲分类+自动修订循环）纠正生成偏差，使标签与人类隐私规范达到 82.5%-95.0% 一致。接着，为每个种子生成详细的案例情节，包括发送者、接收者、环境和指令，作为语义蓝图。最后，基于 ToolEmu 和 PrivacyLens 构建工具中心模拟环境，允许 LLM 模拟多种企业工具（如邮件、会议）的观察结果，并支持同时实例化多个语义相关的条目，真实反映企业数据的混合性。评估采用 LLM-as-a-Judge 框架，定义泄露率（Leakage）、违规率（Violation）和传递率（Conveyance）三个指标，严格量化隐私与效用的权衡。创新点在于：首次将 CI 理论引入企业工作流基准，揭示了任务效用与隐私违规之间的反直觉权衡，并强调需要从模型中心转向上下文中心架构。

### Q4: 论文做了哪些实验？

论文基于CI-Work基准，在模拟企业工作流的五个信息流方向（向上、向下、横向、斜向、外部）上评估了前沿大语言模型。实验设置包括：使用GPT-4o、GPT-4.1、o3、GPT-5、Grok-3、Qwen-2.5 32B、Kimi-K2、DeepSeek-V3和DeepSeek-R1等模型，测试其能否在传递必要内容的同时避免敏感信息泄露。

主要结果：所有模型的违反率在15.8%-50.9%之间，泄露率最高达26.7%。例如，DeepSeek-R1违反率最低（15.8%），Grok-3最高（50.9%）。研究发现更高的任务效用与隐私违反呈正相关（Pearson r=0.40, p<0.05）。向上交互泄露率和违反率显著高于向下交互（VR: p=0.006; LR: p=0.009）。实验还探究了数据类型、条目数量/长度的影响：增加条目数量会提高违反率但降低泄露率（稀释效应）；增加条目长度同时提升泄露率、违反率和传达率。用户行为压力测试显示，显式指令使违反率几近翻倍。此外，增大模型规模出现“逆缩放”现象（更大模型泄露更多），增强推理努力效果微弱，CI-CoT防御策略虽能平衡隐私-效用权衡，违反率仍超20%。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要在于其基准测试仅覆盖五类信息流方向和有限的任务场景，未能涵盖企业环境中更复杂的跨部门协作动态和隐性隐私规范。未来研究方向可从三方面展开：首先，构建动态化的隐私规范更新机制，引入用户实时反馈或组织政策演化来模拟上下文完整性（CI）的适应性调整；其次，设计基于图神经网络的上下文感知架构，通过显式建模信息实体间的隐私标签传播路径来替代当前单纯依赖模型规模扩展的方案；此外，探索对抗性攻击与防御的博弈框架，例如在密集检索阶段嵌入可学习的隐私约束控制器，平衡效用与泄漏风险。当前模型在长尾隐私违规案例中表现尤为脆弱，可能需要引入因果推理方法来识别敏感上下文中的关键干预点。

### Q6: 总结一下论文的主要内容

该论文提出了CI-Work基准，用于评估企业LLM智能体在遵循情境完整性（CI）原则下的隐私保护能力。核心问题在于，智能体在检索企业内上下文信息并代表用户执行任务时，可能无意泄露敏感信息。CI-Work模拟了五种企业信息流方向，在密集检索中测试智能体能否在传递必要内容的同时屏蔽敏感上下文。基于前沿模型的评估显示，隐私违规率高达15.8%-50.9%，信息泄露率达26.7%。研究发现了一个反直觉的权衡：任务效用越高，隐私泄露风险越大，而单纯增加模型规模或推理深度无法解决此问题。论文结论指出，保障企业工作流安全需从模型中心转向上下文中心架构，这对于工业部署具有重要指导意义。
