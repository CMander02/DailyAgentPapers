---
title: "From Chatbot to Digital Colleague: The Paradigm Shift Toward Persistent Autonomous AI"
authors:
  - "Yongheng Zhang"
  - "Ziang Liu"
  - "Jiaxuan Zhu"
  - "Shuai Wang"
  - "Xiangqi Chen"
  - "Haojing Huang"
  - "Jiayi Kuang"
  - "Siyu Chen"
  - "Ao Shen"
  - "Hao Wu"
  - "Qiufeng Wang"
  - "Qian-Wen Zhang"
  - "Junnan Dong"
  - "Wenhao Jiang"
  - "Ying Shen"
  - "Hai-Tao Zheng"
  - "Yinghui Li"
  - "Di Yin"
  - "Xing Sun"
  - "Philip S. Yu"
date: "2026-06-12"
arxiv_id: "2606.14502"
arxiv_url: "https://arxiv.org/abs/2606.14502"
pdf_url: "https://arxiv.org/pdf/2606.14502v1"
categories:
  - "cs.AI"
tags:
  - "Agent架构"
  - "Agent认知"
  - "Agent工具使用"
  - "Agent记忆"
  - "Agent技能"
  - "Agent评测"
  - "大型语言模型"
  - "自主智能体"
  - "持续学习"
  - "工作流"
relevance_score: 9.5
---

# From Chatbot to Digital Colleague: The Paradigm Shift Toward Persistent Autonomous AI

## 原始摘要

Large Language Models (LLMs) are undergoing a fundamental transformation from conversational generators into integrated AI systems capable of reasoning, action, memory, and self-improvement. We conceptualize this transition as a shift from Chatbot to Digital Colleague: from conversational answers to persistent work. We organize this transition along two tightly coupled dimensions. First, at the cognitive core level, LLMs are advancing from Chatbot-era "fast thinking" systems driven by next-token prediction toward Thinking LLMs that leverage inference-time computation, Chain-of-Thought reasoning, reflection, process supervision, and reinforcement learning to support more deliberate and reliable cognition. Second, at the tool-augmented task execution level, LLMs are progressing from tool-calling Agents that invoke external resources in an ad hoc manner toward OpenClaw-style workstation systems (OpenClaw) equipped with persistent Workspaces, skills, verification loops, and governance. The "Workspace + Skill" paradigm makes episodic tool use colleague-like via state persistence, reusable procedures, task closure, and experience reuse. We examine data construction shifts from instruction-response pairs to State-Action-Observation trajectories and evaluation from static benchmarks to sandboxed, auditable, self-evolving AI ecosystems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决的核心问题是：如何将大型语言模型（LLMs）从当前局限的、仅能进行“一问一答”的对话式聊天机器人，转变为能够自主、持续、可靠地在数字环境中完成复杂任务的“数字同事”。研究背景在于，LLMs已从统计语言生成发展成具备一定推理、行动和记忆能力的AI系统。然而，现有方法存在根本性不足：早期“聊天机器人”仅依赖“快思考”式的下一个词预测，缺乏深度推理与长程一致性；后续的“智能体”虽能调用工具，但执行过程脆弱、状态无持久性、错误易累积且无法恢复，本质上仍是临时性的、断裂的交互。因此，本文提出的核心转变是：从追求“生成更好的回答”转向“如何让AI系统可靠地将用户意图转化为完成的工作”。为实现这一目标，论文提出了一个二维转型框架：在认知核心层面，从“快思考”转向具备推理时计算、思维链等能力的“慢思考”LLM；在工具执行层面，从临时调用工具的“智能体”转向具备持久工作区和可复用技能的工作站系统，最终通过“工作区+技能”机制实现从偶发性的交互到持久、有状态、可自愈的数字同事工作的范式转变。

### Q2: 有哪些相关研究？

该论文的相关研究可归类如下：

**方法类**：与"思考型LLM"相关的研究包括**推理时计算**（如OpenAI o1）、**思维链推理**、**反思机制**、**过程监督**和**强化学习**（如DeepSeek-R1），这些方法推动了从快速直觉型回应到慢速审慎推理的转变。与"OpenClaw"相关的研究包括**持久化工作区**（如GitHub Copilot Workspace）、**技能复用**（如向量数据库存储技能）、**验证循环**和**治理机制**。

**应用类**：早期"智能体"研究（如AutoGPT、LangChain代理）展示了工具调用能力，但易出错且中断；新型"工作站"系统（如Codex CLI、Contextual AI）通过持久化状态和错误恢复实现了更可靠的任务执行。

**评测类**：传统**静态基准**（如MMLU、HumanEval）被取代为**沙盒化、可审计、自演化**的评估范式，核心指标从"答案正确性"转向"任务闭合度"，并采用状态-动作-观测轨迹作为训练数据。

**区别**：本文核心创新在于提出"WorkSpace + Skill"架构，将早期智能体的临时工具调用转变为持久化交互，并通过技能复用和状态管理实现从聊天机器人到数字同事的范式转型。

### Q3: 论文如何解决这个问题？

论文提出了一种从“聊天机器人”向“数字同事”转变的范式，核心在于将LLM从“快速响应”的下一代预测系统升级为具备持久工作能力的自主AI。这一转变沿着两个紧密耦合的维度展开：认知核心的进化和工具增强的任务执行进化。

在认知核心层面，论文提出了从“快思考”到“慢思考”的演进。传统聊天机器人（如ChatGPT时代）依赖单次自回归生成，本质上是“快速响应”系统，其能力源于缩放定律、参数知识压缩和指令对齐，但缺乏验证、搜索和长程推理能力。而“Thinking LLM”阶段引入了推理时计算、思维链、反思、过程监督和强化学习，使模型能够进行更审慎和可靠的System 2思考。这一进化是构建代理系统的基础，因为代理需要在行动前成为一个更强的生成器、推理者和决策者。

在工具增强的任务执行层面，论文提出了从“工具调用代理”向“OpenClaw式工作站系统”的转变。传统代理阶段，模型以临时、即席的方式调用外部工具（如API、数据库），缺乏状态持久性和可复用性。而OpenClaw式工作站系统通过引入“工作空间+技能”范式，实现了类似数字同事的持久化工作。该系统的关键组件包括：1）持久性工作空间，用于维护任务状态和上下文；2）可复用的技能，将常见的操作流程封装为标准化程序；3）验证循环，确保任务执行的正确性和可靠性；4）治理机制，保障安全和合规。这一范式将零散的工具使用升级为具有状态持久性、可复用流程、任务闭合和经验复用的类同事工作模式。

此外，论文还指出数据构建方式正从传统的“指令-响应”对转向“状态-动作-观察”轨迹，评估也从静态基准测试转向沙盒化、可审计、自我进化的AI生态系统。整体来看，该论文的核心创新在于系统性地定义了AI代理从“对话式应答”向“持久化工作”的范式转移，并给出了实现这一转移的认知核心和任务执行的双层架构蓝图。

### Q4: 论文做了哪些实验？

论文没有包含具体的实验部分。它是一篇概念性综述论文，主要探讨了大语言模型（LLM）从“聊天机器人”向“数字同事”的范式转变。论文不涉及实验设置、数据集、基准测试或对比方法与结果。相反，它从认知核心和工具增强任务执行两个维度，理论分析了从“快速思维”系统向“思考型LLM”的演进，以及从临时工具调用的代理向具备持久工作空间、技能、验证循环和治理的“OpenClaw”工作站系统的转变。论文还讨论了数据构建从指令-响应对向状态-动作-观测轨迹的转移，以及评估从静态基准向沙盒化、可审计、自进化的AI生态系统的转变。全文未提供任何关键数据指标，如准确率或性能数值，完全聚焦于概念框架和演进路径的理论阐述。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向可从几个关键角度探讨。首先，当前从“快思考”到“慢思考”的转变虽提升了推理深度，但“慢思考”本身引入的推理时计算开销和延迟仍是实际部署的瓶颈。未来可探索更高效的推理时计算策略，如动态分配计算资源，使模型在简单问题上快速响应，仅在复杂问题上启用在深度链式思考。其次，从“工具调用代理”到“数字同事”的“工作空间+技能”范式依赖状态持久化，但如何设计通用且安全的持久化机制以避免状态污染和错误累积是关键。未来可研究模块化的、可隔离的工作空间架构，并融入自我纠错和回滚机制。此外，当前的数据构建（从指令-响应对到状态-动作-观察轨迹）和评估（从静态基准到沙箱化自进化生态）仍不成熟，需要开发更鲁棒的、支持长程任务闭环验证的评估框架。最后，将认知核心的“思考”能力与“工作空间”的操作能力更紧密地耦合，实现思考即行动的统一推理-执行综合体，是提升AI代理自主性和可靠性的重要方向。

### Q6: 总结一下论文的主要内容

这篇论文提出并系统阐释了大语言模型从“聊天机器人”到“数字同事”的范式转变。核心问题是：AI系统如何从生成更好答案，转变为可靠地将用户意图转化为完成的工作？方法上，论文沿着两个紧密耦合的维度组织分析：一是认知核心从“快思考”的聊天机器人演进为具备推理、反思和强化学习能力的“思考型LLM”；二是工具增强的任务执行从脆弱的“智能体”进化为拥有持久工作空间、可复用技能、验证循环和治理机制的“OpenClaw式工作站系统”。论文的核心贡献在于提出了“工作空间+技能”范式，认为它能将临时性的工具调用转变为持久的同事式协作，并通过状态持久化、可复用程序和任务闭合机制实现。主要结论是，数据构建正从指令-响应对转向状态-动作-观测轨迹，评估也从静态基准转向可审计、可自我进化的AI生态系统，最终实现可靠、可持续的自主AI系统。
