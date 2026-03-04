---
title: "Saarthi for AGI: Towards Domain-Specific General Intelligence for Formal Verification"
authors:
  - "Aman Kumar"
  - "Deepak Narayan Gadde"
  - "Luu Danh Minh"
  - "Vaisakh Naduvodi Viswambharan"
  - "Keerthan Kopparam Radhakrishna"
  - "Sivaram Pothireddypalli"
date: "2026-03-03"
arxiv_id: "2603.03175"
arxiv_url: "https://arxiv.org/abs/2603.03175"
pdf_url: "https://arxiv.org/pdf/2603.03175v1"
categories:
  - "cs.AI"
tags:
  - "Agent Framework"
  - "Multi-Agent Collaboration"
  - "Tool Use"
  - "Retrieval-Augmented Generation"
  - "Domain-Specific Application"
  - "Formal Verification"
relevance_score: 8.0
---

# Saarthi for AGI: Towards Domain-Specific General Intelligence for Formal Verification

## 原始摘要

Saarthi is an agentic AI framework that uses multi-agent collaboration to perform end-to-end formal verification. Even though the framework provides a complete flow from specification to coverage closure, with around 40% efficacy, there are several challenges that need to be addressed to make it more robust and reliable. Artificial General Intelligence (AGI) is still a distant goal, and current Large Language Model (LLM)-based agents are prone to hallucinations and making mistakes, especially when dealing with complex tasks such as formal verification. However, with the right enhancements and improvements, we believe that Saarthi can be a significant step towards achieving domain-specific general intelligence for formal verification. Especially for problems that require Short Term, Short Context (STSC) capabilities, such as formal verification, Saarthi can be a powerful tool to assist verification engineers in their work. In this paper, we present two key enhancements to the Saarthi framework: (1) a structured rulebook and specification grammar to improve the accuracy and controllability of SystemVerilog Assertion (SVA) generation, and (2) integration of advanced Retrieval Augmented Generation (RAG) techniques, such as GraphRAG, to provide agents with access to technical knowledge and best practices for iterative refinement and improvement of outputs. We also benchmark these enhancements for the overall Saarthi framework using challenging test cases from NVIDIA's CVDP benchmark targeting formal verification. Our benchmark results stand out with a 70% improvement in the accuracy of generated assertions, and a 50% reduction in the number of iterations required to achieve coverage closure.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决人工智能在形式验证领域应用时存在的可靠性、可控性和知识基础不足的问题，以推动该领域向“领域特定通用智能”迈进。研究背景是现代半导体设计日益复杂、可配置且安全关键，传统形式验证高度依赖专家工程师手动完成，从解读规范到编写断言、迭代闭合覆盖缺口，整个过程劳动密集、难以扩展。虽然大语言模型和智能体框架为自动化带来了希望，但现有方法存在明显不足：直接应用通用模型会导致句法不稳定、语义误解、幻觉以及浅层推理；多智能体协作虽能提升鲁棒性，但在断言生成的可控性、将智能体推理基于权威知识库以及自适应反馈机制方面仍存在缺口。

因此，本文的核心问题是：如何构建一个更稳健、可靠的AI驱动形式验证框架，以克服当前LLM智能体在复杂验证任务中的幻觉和错误倾向，并有效整合可控生成、结构化知识检索与经验学习。具体而言，论文通过增强Saarthi框架来解决三个关键挑战：一是通过引入结构化规则手册和规范语法，提升SystemVerilog断言生成的准确性和可控性，减少变异性和首次编译失败；二是集成先进的检索增强生成技术，特别是GraphRAG，使智能体能基于权威技术文献进行多跳推理，确保生成结果的可靠性和可追溯性；三是建立闭环的人类在环数据收集与自动化覆盖缺口填充机制，将人工干预转化为可重用的知识资产，加速验证收敛。最终目标是在形式验证这类需要“短期、短上下文”精确能力的任务中，实现更高程度的自动化辅助，缩小AI在工作流中的可靠性差距。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类。

在方法类研究中，相关工作包括：
1.  **基于大语言模型（LLM）的代码/断言生成**：先前研究已探索利用LLM生成硬件描述语言代码或形式验证断言，但普遍指出其输出存在幻觉和错误，尤其在复杂任务中可靠性不足。本文的Saarthi框架在此基础上，通过引入**结构化规则手册（rulebook）和规范语法**，旨在提升SystemVerilog断言生成的准确性和可控性，这是对现有LLM生成方法在精确度和可控性方面的重要改进。
2.  **检索增强生成（RAG）技术**：传统RAG通过检索外部知识库的文本来增强LLM的生成，以提高事实性和减少幻觉。本文不仅集成了基础的RAG流程，更进一步引入了**GraphRAG**这一高级技术。与仅依赖语义相似性的传统RAG不同，GraphRAG利用知识图谱的结构化关系进行多跳推理，能够更好地处理形式验证中需求、设计、测试、覆盖率之间的长程依赖关系，从而提供更具可追溯性和解释性的响应。

在应用类研究中，相关工作聚焦于：
**AI辅助的电子设计自动化（EDA）与验证**：已有研究尝试将AI应用于芯片设计和验证流程。本文的Saarthi框架是一个**多智能体协作**的端到端形式验证框架，其核心创新在于将上述方法类增强（结构化规则与GraphRAG）系统性地整合到一个支持迭代精炼和系统性反馈循环的智能体框架中。这与之前可能侧重于单一任务或缺乏深度知识集成与追溯能力的工作形成了区别。本文的目标是迈向**领域特定通用智能（DSGI）**，专门针对形式验证这类需要“短期、短上下文（STSC）”能力的复杂问题，提供更稳健、可靠的自动化解决方案。

### Q3: 论文如何解决这个问题？

论文通过引入三项核心增强技术来提升Saarthi框架在形式化验证任务中的准确性、可控性和效率。其核心方法是构建一个基于多智能体协作的、可迭代优化的自动化验证流程，并针对现有大语言模型智能体在复杂任务中易出现的幻觉和错误问题，设计了结构化的约束与知识增强机制。

整体框架建立在Microsoft AutoGen的多智能体编排能力之上，采用顺序执行的编排策略。主要模块包括：一个负责端到端验证计划管理的协调器/主导智能体、专门生成候选SystemVerilog断言（SVA）的属性生成智能体、用于检测和修复语法错误的语法纠错智能体（包含语法分析器、代码修复器和语法验证器三阶段管道）、以及执行覆盖率差距分析和策略性断言插入的覆盖率智能体。此外，一个代码提取器/管理器模块负责物化智能体生成的代码并将其集成到验证环境中。

论文的创新点主要体现在三个关键技术增强上：
1.  **结构化规则书与规范语法**：为了解决自然语言指令的模糊性导致断言生成不稳定的问题，论文提出将验证规范编码为一组简洁的关键词数组。这种结构化的“规则书”作为自然语言与机器可读格式之间的桥梁，创建了一个确定性的断言生成流水线。规则书还集成了最佳实践、常见错误案例及其修正方案，形成一个可供所有智能体学习的“错误缓存”，从而避免重复犯错，显著提高了生成的一致性和可调试性。
2.  **高级检索增强生成（RAG）技术集成**：为了给智能体提供更丰富的技术知识和迭代推理能力，论文集成了如GraphRAG等先进的RAG技术。这使得智能体能够访问外部的技术文档、最佳实践库和过往经验，从而在迭代过程中不断精炼和改进其输出，弥补了大语言模型自身知识的局限性。
3.  **自动化覆盖率空洞填补机制**：该机制旨在自动识别未验证的设计区域，并生成有针对性的断言来覆盖这些“空洞”。覆盖率智能体通过分析验证报告定位缺口，然后请求生成针对特定模块和信号的新属性，从而加速覆盖率收敛的进程。

这些增强措施通过一个包含“生成-批评-迭代”的闭环工作流协同作用。属性生成后由批评智能体评估并提供反馈，进行迭代优化，直至达到收敛阈值或触发人工干预（HIL）。在HIL阶段收集的已验证数据会被结构化记录，用于持续改进智能体的提示和模板，形成一个自我增强的反馈循环。最终，通过在NVIDIA CVDP基准测试上的验证，这些增强使得生成断言的准确率提升了70%，达成覆盖率闭合所需的迭代次数减少了50%。

### Q4: 论文做了哪些实验？

论文的实验设置基于增强后的Saarthi多智能体框架，该框架在Microsoft AutoGen上构建，采用顺序编排的智能体协作流程，包括属性生成、语法纠错、覆盖分析等专门智能体。实验使用了NVIDIA的全面Verilog设计问题（CVDP）基准测试数据集，该数据集包含针对形式验证的具有挑战性的测试用例。对比方法主要涉及增强前后的Saarthi框架性能，特别是引入结构化规则书/规范语法与高级检索增强生成（如GraphRAG）技术前后的效果。

主要结果通过关键数据指标体现：在断言生成准确性方面实现了70%的显著提升；在达到覆盖闭合所需的迭代次数上减少了50%。这些改进验证了所提出的结构化规则书和高级RAG技术能有效提高智能体生成SystemVerilog断言（SVA）的准确性和可控性，并利用技术知识库进行迭代优化，从而加速覆盖闭合过程，增强了框架在复杂形式验证任务中的鲁棒性和实用性。

### Q5: 有什么可以进一步探索的点？

该论文展示了Saarthi框架在形式验证领域的进展，但其局限性和未来探索方向仍较明显。首先，框架目前主要针对“短时短上下文”（STSC）问题，对于需要长期推理和复杂上下文理解的任务，其能力可能不足。其次，尽管引入了规则库和RAG技术，LLM固有的幻觉问题仍未根本解决，在高度专业的验证场景中可能导致错误累积。

未来研究方向可包括：一是增强代理的长期记忆与推理能力，通过改进架构使其能处理更复杂的多步骤验证任务；二是开发更动态的规则学习机制，让系统能从错误中自动调整规则库，而非完全依赖预设；三是探索跨领域知识迁移，将形式验证中习得的模式应用于其他硬件设计或软件验证场景，以提升通用性。此外，可考虑引入人类工程师的实时反馈循环，形成混合智能系统，进一步降低幻觉风险并提升可靠性。

### Q6: 总结一下论文的主要内容

该论文介绍了Saarthi框架，这是一个面向形式验证领域的多智能体协作AI系统，旨在推动该领域的特定领域通用智能（AGI）发展。核心问题是当前基于大语言模型（LLM）的智能体在处理形式验证等复杂任务时，存在幻觉和错误，导致框架的端到端验证流程虽完整但效能（约40%）有待提升。论文提出了两项关键增强方法：一是引入结构化的规则手册和规范语法，以提高系统验证断言（SVA）生成的准确性和可控性；二是集成先进的检索增强生成（RAG）技术（如GraphRAG），为智能体提供技术知识和最佳实践，以迭代优化输出。通过在NVIDIA CVDP基准测试中评估，这些改进使生成断言的准确率提升了70%，并减少了50%的覆盖闭合所需迭代次数。主要结论表明，Saarthi通过针对性增强，显著提升了形式验证任务的可靠性和效率，尤其在需要短时、短上下文（STSC）能力的场景中，成为辅助验证工程师的强大工具，是迈向领域特定通用智能的重要一步。
