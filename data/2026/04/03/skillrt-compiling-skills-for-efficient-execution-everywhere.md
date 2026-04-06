---
title: "SkillRT: Compiling Skills for Efficient Execution Everywhere"
authors:
  - "Le Chen"
  - "Erhu Feng"
  - "Yubin Xia"
  - "Haibo Chen"
date: "2026-04-03"
arxiv_id: "2604.03088"
arxiv_url: "https://arxiv.org/abs/2604.03088"
pdf_url: "https://arxiv.org/pdf/2604.03088v1"
categories:
  - "cs.SE"
  - "cs.LG"
tags:
  - "Agent 系统"
  - "技能编译"
  - "执行效率"
  - "可移植性"
  - "基准评测"
  - "运行时优化"
relevance_score: 8.5
---

# SkillRT: Compiling Skills for Efficient Execution Everywhere

## 原始摘要

LLM agents increasingly adopt skills as a reusable unit of composition. While skills are shared across diverse agent platforms, current systems treat them as raw context, causing the same skill to behave inconsistently for different agents. This fragility undermines skill portability and execution efficiency.
  To address this challenge, we analyze 118,000 skills and draw inspiration from traditional compiler design. We treat skills as code and LLMs as heterogeneous processors. To make portability actionable, we decompose a skill's requirements into a set of primitive capabilities, and measure how well each model-harness pair supports them. Based on these capability profiles, we propose SkillRT, a compilation and runtime system designed for portable and efficient skill execution. At compile time, SkillRT performs capability-based compilation, environment binding, and concurrency extraction. At runtime, SkillRT applies JIT code solidification and adaptive recompilation for performance optimization.
  We evaluate SkillRT across eight LLMs of varying scales and three agent harnesses, covering SkillsBench and representative skill tasks. Results demonstrate that SkillRT significantly improves task completion rates across different models and environments while reducing token consumption by up to 40%. In terms of performance, SkillRT achieves up to 3.2x speedup with enhanced parallelism, and 19-50x latency reduction through code solidification.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大语言模型（LLM）智能体中“技能”（Skills）的移植性和执行效率低下问题。研究背景是，随着基于LLM的智能体日益普及，技能作为一种可复用的功能单元被广泛共享和使用，形成了一个包含超过十万个技能的生态系统。然而，现有方法将技能简单地视为原始的自然语言上下文，直接传递给模型执行。这种做法存在严重不足：首先，由于不同LLM模型和不同智能体运行框架（Harness）在能力、工具支持上存在巨大差异，同一技能在不同目标上表现不一致甚至失效，严重破坏了技能的移植性承诺。其次，技能中常见的半结构化代码片段和工作流描述会导致显著的令牌开销和执行延迟，效率低下。

本文的核心问题是：如何让技能能够像传统软件一样，在各种异构的“处理器”（即不同的LLM模型）和“运行环境”（即不同的智能体框架与用户环境）上实现高效、可靠且一致的执行。论文将这个问题类比为传统计算中的代码移植问题：技能是代码，LLM是异构处理器，但目前缺乏一个类似编译器和运行时的系统来弥合静态技能与动态多变的目标平台之间的鸿沟。因此，本文提出了SkillRT系统，旨在通过编译和运行时技术来解决技能与目标平台之间的能力不匹配、环境依赖不满足以及并行机会未被利用等核心挑战，从而实现技能的便携化和高效执行。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：技能/Agent框架、LLM编译/优化技术，以及能力评估与基准测试。

在**技能与Agent框架**方面，相关工作包括Claude Code、OpenCode、OpenClaw等Agent运行时框架，它们提供了技能加载和执行的基础设施。此外，像clawhub.ai和skills.sh这样的技能分发平台，构成了大规模技能生态系统的基石。本文与这些工作的关系是，SkillRT并非替代现有框架，而是构建于其上，旨在解决现有系统将技能视为原始上下文（raw context）所导致的**可移植性差和执行效率低下**的核心问题。区别在于，现有工作缺乏对技能在不同模型、框架和环境下的适配与优化，而SkillRT首次将编译器设计思想系统性地引入该领域。

在**LLM编译与优化技术**方面，相关工作包括针对提示（prompt）的压缩、缓存和JIT优化等技术。本文受传统编译器设计的启发，提出了创新的“能力编译”范式。其核心区别在于，SkillRT将技能视为“代码”，将不同的LLM和Agent框架视为“异构处理器”，通过将技能需求分解为**原始能力**并进行量化评估，实现了基于能力画像的针对性编译和运行时优化（如JIT代码固化、自适应重编译），这是对现有通用提示优化方法的重要深化和专门化。

在**能力评估与基准测试**方面，本文构建了大规模的技能分析（基于超11万个技能）和实验评估体系。相关工作包括各类Agent评测基准。本文的区别在于，它不仅关注任务完成率，更深入揭示了**模型不匹配、框架不匹配和环境不匹配**这三类可移植性问题的具体表现和影响，并以此作为驱动系统设计的核心依据。本文使用的SkillsBench和代表性技能任务，为评估技能执行的**可移植性和效率**提供了新的维度。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SkillRT的编译与运行时系统来解决技能在不同LLM代理平台间行为不一致、可移植性差和执行效率低的问题。其核心思想是将技能视为代码，将不同的LLM及代理框架视为异构处理器，借鉴传统编译器设计，通过静态编译和动态优化来确保技能的可移植性与高效执行。

**整体框架与主要模块：**
SkillRT系统由两部分组成：**提前（AOT）编译器**和**运行时（含即时JIT优化器）**。
1.  **AOT编译器**：在技能安装时，针对特定的目标环境（模型、代理框架、主机环境）对原始技能进行分析和优化，生成一个或多个优化后的技能变体。它包含三个核心编译阶段：
    *   **基于能力的编译**：这是核心创新点。系统引入了一套**原始能力**的抽象词汇表，用于描述技能所需和LLM目标所能提供的基本能力。通过离线微基准测试对目标进行能力画像，并与技能分解出的能力需求进行比对。根据差距，编译器应用两种转换策略：**补偿**（通过提供示例、明确指令等方式降低技能对能力等级的要求）或**替代**（切换到使用目标支持的其他能力实现的等效路径）。
    *   **环境绑定**：解决技能依赖的环境（如库、工具）与主机环境不匹配的问题。编译器提取依赖清单，检查并生成幂等的环境绑定脚本，确保执行前依赖已满足。
    *   **并发提取**：分析技能中隐含的并行性。通过LLM辅助分析将顺序工作流分解为步骤并构建有向无环图，识别数据级、指令级和线程级并行机会，并重写技能或添加注解，以便运行时利用目标框架的并发原语。

2.  **运行时与JIT优化器**：在执行时，运行时加载为当前目标编译的技能变体，并在此基础上进行动态优化：
    *   **自适应重编译**：监控技能执行结果。如果发现因静态画像未捕捉的能力差距导致的系统性失败，会触发重编译，利用失败日志进行针对性优化。
    *   **代码固化**：针对技能中结构固定、仅参数变化的代码模式（如重复的脚本），AOT编译器会生成包含代码签名和模板的JIT候选。运行时监控多次调用，确认模式一致后，将模板实例化为可执行函数，后续调用直接执行该函数而无需LLM推理，大幅降低延迟和令牌消耗。
    *   **资源感知调度器**：根据运行时资源状况（如CPU、内存、API速率限制）动态调整并发执行。它通过节流新子代理的启动或暂停现有子代理来避免资源竞争，实现编译时并行机会与运行时资源可用性的桥接。

**创新点：**
1.  **能力驱动的编译模型**：首创性地将技能可移植性问题形式化为LLM“能力”与技能“需求”的匹配问题，并通过定义可组合、通用、语义独立的“原始能力”层级体系，为跨异构目标的技能适配提供了可操作的抽象基础和自动化优化基础。
2.  **静动结合的优化体系**：结合了AOT编译的针对性优化与JIT运行时的适应性优化。AOT解决可移植性，JIT（特别是代码固化）提升效率，两者互补。
3.  **并发提取与资源感知调度**：系统性地挖掘并利用技能描述中隐含的并行性，并通过运行时调度解决并行执行与资源约束的矛盾，实现了性能加速。
4.  **端到端的技能生命周期管理**：从技能安装时的编译、环境准备，到运行时的变体选择、性能监控、优化与回滚，提供了一个完整的系统解决方案，显著提升了任务完成率、降低了令牌消耗并加快了执行速度。

### Q4: 论文做了哪些实验？

该论文在实验部分进行了全面的评估，以验证SkillRT系统的有效性。实验设置方面，研究在配备16GB内存的Mac Mini M4平台上进行，采用自动化评估套件（包括静态分析和基于LLM的评估）来衡量任务完成率、令牌消耗和端到端执行延迟。每个任务生成五个不同的输入实例进行平均测量。

数据集与基准测试主要基于SkillsBench和PinchBench，并进行了扩展，覆盖了代码生成、数据分析和系统管理等多样化的智能体任务。任务技能来源于Anthropic-skills、OpenClaw skills和skills.sh等主流技能库。

对比方法包括三个基线：1) **无技能**：智能体不加载任何技能执行；2) **原始技能**：使用原始未优化的技能；3) **Skill-Creator**：使用Anthropic的Skill-Creator（基于claude-opus-4.6）优化的技能。评估模型涵盖八个不同规模的LLM，分为三个能力层级：SOTA级（claude-opus-4.6, deepseek-v3.2）、中层级（gemini-3-flash, qwen3.5-397b等）和小型模型（qwen3-30b, devstral-small）。测试环境包括三个开源智能体框架：BareAgent、OpenCode和OpenClaw。

主要结果显示，SkillRT在所有模型和环境中均显著提升了任务完成率，尤其对较弱模型和在OpenClaw框架上提升幅度最大。在性能指标上，SkillRT将令牌消耗降低了**高达40%**；通过增强并行性实现了**最高3.2倍的加速**；并通过代码固化使延迟降低了**19至50倍**。此外，分阶段优化实验表明，经过AOT编译和三轮JIT优化后，技能在14个类别上的得分持续提升，验证了编译优化策略的有效性。

### Q5: 有什么可以进一步探索的点？

该论文提出的SkillRT系统在技能可移植性和执行效率方面取得了显著进展，但其局限性和未来探索方向仍值得深入。首先，系统依赖于对技能需求的“原始能力”分解和模型能力画像，这种静态映射可能无法充分捕捉LLM在动态上下文中的涌现能力或特定任务的细微需求，未来可引入更动态、在线学习的能力评估机制。其次，当前编译优化主要针对单技能，而复杂任务往往涉及多技能协作与状态管理，未来可探索跨技能的全局优化、依赖分析及并发调度策略。此外，SkillRT的评估集中于已知技能库和标准任务，对于开放域、长周期或需实时环境交互的agent任务，其适应性和鲁棒性有待验证。从系统角度看，可考虑将编译与运行时优化扩展到分布式多agent场景，支持技能在异构agent间的安全共享与协同。最后，结合神经符号方法，将部分技能编译为确定性代码或符号规则，可能进一步减少对LLM的依赖，提升执行效率与可靠性。

### Q6: 总结一下论文的主要内容

这篇论文提出了SkillRT，一个用于大语言模型（LLM）智能体技能的编译与运行时系统，旨在解决技能在不同智能体平台间执行不一致、效率低下的可移植性问题。其核心贡献是将传统编译器设计思想引入技能执行领域，将技能视为代码，将LLM视为异构处理器，从而系统性地优化技能的执行。

论文首先定义了问题：当前智能体系统将技能作为原始上下文直接传递给模型，忽略了不同模型和运行环境在能力上的巨大差异，导致技能执行脆弱、效率低下且不可靠。为解决此问题，SkillRT的方法借鉴了编译器设计，主要包括：1）**提前编译（AOT）**：在技能安装时，通过能力分析、环境绑定和并发提取三个步骤，针对特定目标（模型、运行框架、环境）生成优化的技能变体。能力分析通过定义26种原子能力及其熟练度等级，量化技能需求与模型能力之间的差距，并应用补偿或替换策略进行适配。2）**即时编译与运行时优化（JIT）**：在技能执行时，系统进行自适应重编译以弥补静态分析未发现的能力差距，并通过代码固化将高频出现的参数化代码模板转化为可执行函数，绕过LLM推理以降低延迟和token消耗。运行时还包含资源感知调度器，管理并行子任务的执行。

主要结论是，SkillRT在涵盖8个不同规模LLM和3种智能体框架的评估中，显著提升了任务完成率（平均提升15.3%），并将token消耗降低了最高40%。在性能方面，通过细粒度并行化和代码固化，实现了最高3.2倍的加速和19-50倍的延迟降低。这证明了SkillRT能够有效实现技能的高效、可移植执行，为构建更可靠的智能体生态系统提供了基础支持。
