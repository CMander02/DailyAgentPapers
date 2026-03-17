---
title: "Lore: Repurposing Git Commit Messages as a Structured Knowledge Protocol for AI Coding Agents"
authors:
  - "Ivan Stetsenko"
date: "2026-03-16"
arxiv_id: "2603.15566"
arxiv_url: "https://arxiv.org/abs/2603.15566"
pdf_url: "https://arxiv.org/pdf/2603.15566v1"
categories:
  - "cs.SE"
  - "cs.AI"
  - "eess.SY"
tags:
  - "AI编程智能体"
  - "知识管理"
  - "软件开发"
  - "协议设计"
  - "Git"
relevance_score: 7.5
---

# Lore: Repurposing Git Commit Messages as a Structured Knowledge Protocol for AI Coding Agents

## 原始摘要

As AI coding agents become both primary producers and consumers of source code, the software industry faces an accelerating loss of institutional knowledge. Each commit captures a code diff but discards the reasoning behind it - the constraints, rejected alternatives, and forward-looking context that shaped the decision. I term this discarded reasoning the Decision Shadow. This paper proposes Lore, a lightweight protocol that restructures commit messages - using native git trailers - into self-contained decision records carrying constraints, rejected alternatives, agent directives, and verification metadata. Lore requires no infrastructure beyond git, is queryable via a standalone CLI tool, and is discoverable by any agent capable of running shell commands. The paper formalizes the protocol, compares it against five competing approaches, stress-tests it against its strongest objections, and outlines an empirical validation path.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决AI编程智能体（AI coding agents）在软件开发中日益普及所引发的一个关键问题：机构知识的加速流失。随着AI智能体成为源代码的主要生产者和消费者，传统的代码提交（commit）过程存在严重的信息缺失。每次提交虽然记录了代码差异（diff），但丢弃了变更背后的决策逻辑，包括约束条件、被拒绝的替代方案以及塑造决策的前瞻性上下文。作者将这种被丢弃的推理过程称为“决策阴影”（Decision Shadow）。这导致后续的AI智能体或人类开发者难以理解代码变更的“为什么”，从而可能做出冲突的决策、重复过去的错误或浪费精力探索已被否定的方案。因此，论文的核心问题是：如何以一种轻量级、可扩展且与现有工具链兼容的方式，捕获、结构化和复用软件开发中的决策知识，以增强AI编程智能体的上下文感知和决策能力。

### Q2: 有哪些相关研究？

相关工作主要围绕AI编程智能体的知识管理和软件开发中的决策记录。首先，是直接针对AI编程智能体的知识库研究，如Aider和Cursor等项目，它们尝试维护项目特定的知识库，但通常依赖非结构化的聊天历史或外部数据库，与版本控制系统（VCS）脱节。其次，是软件工程领域的“设计决策”和“架构决策”记录传统，如架构决策记录（ADR），但这些方法通常笨重、需要手动维护，且未针对AI智能体的消费进行优化。第三类是利用大型语言模型（LLM）从代码变更中生成解释或总结的研究，例如自动生成提交消息，但这通常是单向的、事后生成的，缺乏结构化、机器可读的决策元数据。第四类是在提交消息中使用约定（如Conventional Commits）或标签（如`Signed-off-by`），这提供了结构化的雏形，但未标准化用于承载丰富的决策知识。最后，是更广泛的AI智能体记忆和上下文管理研究，如向量数据库或提示工程，但它们往往引入复杂的基础设施。本文提出的Lore协议与这些工作的不同在于，它深度集成于Git这一核心工具中，将提交消息本身重新定义为结构化的知识协议，强调轻量级、无额外基础设施、机器可查询和人类可读的平衡。

### Q3: 论文如何解决这个问题？

论文提出了一个名为Lore的轻量级协议，其核心思想是重新利用Git提交消息（commit messages）作为AI编程智能体的结构化知识协议。Lore不引入任何Git之外的基础设施，而是巧妙地利用Git原生的“尾部”（trailers）机制（类似于电子邮件中的`Signed-off-by`）来嵌入结构化的决策记录。协议定义了一套标准化的尾部字段，将每个提交消息转化为一个自包含的“决策记录”。关键字段包括：`Decision`（核心决策描述）、`Constraints`（决策时的约束条件，如性能、安全、合规要求）、`Alternatives-Rejected`（被考虑但拒绝的替代方案及其原因）、`Agent-Directive`（给未来处理此代码的AI智能体的指令，例如“避免修改此模式”）、`Verified-By`（验证此决策的方法，如测试、审查）以及`Lore-Version`（协议版本）。这些结构化信息使得提交消息不仅是人类可读的变更描述，更是机器可查询的知识单元。论文还提供了一个独立的命令行界面（CLI）工具，使智能体能够通过执行Shell命令来查询和发现这些知识（例如，`lore find --constraint "performance"`）。整个方法的设计原则是极简主义、向后兼容（纯文本的Git尾部）、可发现性以及支持增量采用。

### Q4: 论文做了哪些实验？

论文并未报告在标准基准（如SWE-bench）上的大规模量化实验，而是采用了一种论证性和概念验证性的评估路径。作者首先对Lore协议进行了形式化定义，明确了其语法和语义。接着，论文将Lore与五种竞争性方法进行了系统比较，包括：1) 非结构化聊天历史（如Aider/Cursor），2) 外部知识库/向量数据库，3) 架构决策记录（ADR），4) 增强的代码注释，5) 专门的决策跟踪工具。比较的维度包括基础设施需求、与VCS的集成度、AI可消费性、人类可读性等，论证了Lore在轻量化和集成度上的优势。然后，论文对Lore可能面临的最强烈反对意见进行了“压力测试”，例如：增加了提交噪音、可能泄露敏感信息、依赖智能体遵守协议、以及初始采用成本。对于每个反对点，作者都给出了反驳和缓解策略。最后，论文概述了一个经验验证的路径，建议通过案例研究（在真实项目中应用Lore并观察对AI智能体任务完成效率和质量的影响）和受控实验（让智能体在有无Lore知识的情况下完成代码维护任务）来进行未来验证。因此，实验部分更侧重于理论论证、协议设计和可行性分析。

### Q5: 有什么可以进一步探索的点？

论文指出了多个未来可以探索的方向。首先，也是最迫切的，是需要进行前述的经验验证，通过案例研究和受控实验来量化Lore对AI编程智能体实际效能（如代码正确性、变更理解速度、决策一致性）的影响。其次，是协议本身的演化，包括定义更丰富的尾部字段类型、处理字段间的依赖关系或冲突，以及建立社区驱动的标准。第三，是开发更高级的智能体交互工具，例如IDE插件或智能体框架（如LangChain, LlamaIndex）的原生集成，使知识查询和注入更加无缝。第四，是探索知识的生命周期管理，例如如何对陈旧的决策进行标记、归档或重构，以及如何处理决策知识的版本冲突。第五，是安全性考量，需要研究如何在共享决策知识的同时保护知识产权或敏感信息，或许需要引入加密或权限模型。最后，可以探索Lore协议思想在其他领域的泛化，例如将其结构化的“决策记录”模式应用于非代码的创作或设计过程中，作为多轮次、多智能体协作的通用知识锚点。

### Q6: 总结一下论文的主要内容

本文提出并详细阐述了Lore协议，这是一个创新性的解决方案，旨在应对AI编程智能体普及导致的软件开发“决策阴影”问题——即代码变更背后推理知识的流失。Lore的核心贡献是重新定义了Git提交消息的角色，通过标准化使用Git尾部（trailers），将其从一个简单的文本描述转变为一个结构化的、机器可查询的决策知识记录。协议包含了决策、约束、被拒方案、智能体指令等关键字段，从而捕获了代码“为什么”这样修改的完整上下文。该方法的最大优势是轻量级、无需额外基础设施、与现有Git工作流完全兼容，并通过一个CLI工具提供可发现性。论文通过形式化协议、与多种替代方案的系统比较、以及对潜在质疑的压力测试，论证了Lore的可行性和优势。虽然缺乏大规模实验数据，但为AI编程智能体的知识管理和长期软件可维护性提供了一个极具潜力的实用化方向。其本质是为AI智能体在软件生命周期中建立一种共享的、结构化的“机构记忆”。
