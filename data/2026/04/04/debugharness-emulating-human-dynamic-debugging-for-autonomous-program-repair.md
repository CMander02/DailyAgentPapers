---
title: "DebugHarness: Emulating Human Dynamic Debugging for Autonomous Program Repair"
authors:
  - "Maolin Sun"
  - "Yibiao Yang"
  - "Xuanlin Liu"
  - "Yuming Zhou"
  - "Baowen Xu"
date: "2026-04-04"
arxiv_id: "2604.03610"
arxiv_url: "https://arxiv.org/abs/2604.03610"
pdf_url: "https://arxiv.org/pdf/2604.03610v1"
categories:
  - "cs.SE"
tags:
  - "Autonomous Agent"
  - "Program Repair"
  - "Debugging"
  - "Tool Use"
  - "Reasoning"
  - "LLM Agent"
  - "Software Engineering"
  - "Dynamic Analysis"
  - "Closed-loop Validation"
relevance_score: 8.5
---

# DebugHarness: Emulating Human Dynamic Debugging for Autonomous Program Repair

## 原始摘要

Patching severe security flaws in complex software remains a major challenge. While automated tools like fuzzers efficiently discover bugs, fixing deep-rooted low-level faults (e.g., use-after-free and memory corruption) still requires labor-intensive manual analysis by experts. Emerging Large Language Model (LLM) agents attempt to automate this pipeline, but they typically treat bug fixing as a purely static code-generation task. Relying solely on static artifacts, these methods miss the dynamic execution context strictly necessary for diagnosing intricate memory safety violations. To overcome these limitations, we introduce DebugHarness, an autonomous LLM-powered debugging agent harness that resolves complex vulnerabilities by emulating the interactive debugging practices of human systems engineers. Instead of merely examining static code, DebugHarness actively queries the live runtime environment. Driven by a reproducible crash, it utilizes a pattern-guided investigation strategy to formulate hypotheses, interactively probes program memory states and execution paths, and synthesizes patches via a closed-loop validation cycle. We evaluate DebugHarness on SEC-bench, a rigorous dataset of real-world C/C++ security vulnerabilities. DebugHarness successfully patches approximately 90% of the evaluated bugs. This yields a relative improvement of over 30% compared to state-of-the-art baselines, demonstrating that dynamic debugging significantly enhances LLM diagnostic capabilities. Overall, DebugHarness establishes a novel paradigm for automated program repair, bridging the gap between static LLM reasoning and the dynamic intricacies of low-level systems programming.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决复杂软件中严重安全漏洞（尤其是内存安全违规类漏洞）的自动化修复难题。研究背景是，尽管模糊测试等自动化漏洞发现技术已能高效识别大量缺陷，但后续的修复环节仍严重依赖专家手动调试，成为安全风险和维护成本的主要瓶颈。现有基于大语言模型（LLM）的自动程序修复方法通常将漏洞修复视为静态代码生成任务，仅依赖问题报告、堆栈跟踪和源代码等静态信息，缺乏对程序动态执行状态（如内存布局、运行时值）的推理。这种静态方法在处理高级语言中的简单错误时可能有效，但在诊断复杂的底层内存安全漏洞（如释放后使用、内存损坏）时存在严重不足，因为它无法捕捉到漏洞触发所需的动态上下文，与人类专家实际使用的交互式、动态调试实践脱节。

因此，本文的核心问题是：如何让LLM驱动的自动化修复系统能够像人类系统工程师一样，进行动态、交互式的调试，以理解和修复那些需要深入理解程序运行时状态的复杂安全漏洞。为此，论文提出了DebugHarness系统，通过模拟人类的动态调试实践，让LLM代理能够主动查询实时运行时环境，在可复现的崩溃驱动下，利用模式引导的调查策略形成假设，交互式探查程序内存状态和执行路径，并通过闭环验证循环合成补丁，从而弥合静态LLM推理与底层系统编程动态复杂性之间的差距。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：传统自动程序修复（APR）方法、基于大语言模型（LLM）的静态修复方法，以及试图模拟人类调试过程的LLM智能体方法。

在**传统APR方法**方面，工作通常围绕故障定位、补丁生成和补丁验证三个阶段展开。例如，基于符号执行或频谱分析的故障定位技术计算开销大，而基于搜索、约束或模式的补丁生成方法则在表达能力和搜索空间之间权衡。像ExtractFix这样的端到端解决方案尝试串联这些阶段，但面临路径爆炸问题，难以修复复杂的内存安全违规（如释放后使用）。

**基于LLM的静态修复方法**利用LLM的代码理解和生成能力，但大多只针对修复流程的单一阶段。例如，有些系统使用多轮LLM交互进行故障定位（可能引入人工反馈），另一些则专注于在给定验证反馈后迭代改进候选补丁。即使整合了生成与验证的系统，也常假设故障位置已知，从而回避了最具挑战性的环节。近期，像Agentless这样的工作尝试用单一LLM统一整个流程，并在Python问题的SWE-bench基准上取得了显著成果。

**模拟人类调试的LLM智能体方法**是更接近本文的研究方向。例如，PatchAgent被设计为通过查询语言服务器进行静态代码导航来模仿人类调试工作流。然而，它仍将漏洞修复视为纯静态问题，仅能分析崩溃报告、堆栈跟踪和源代码等静态工件，而无法访问动态执行上下文。这导致其在处理需要追踪运行时状态（如缓存失效）的复杂漏洞（如文中的CVE-2022-1286案例）时失败。

**本文与这些工作的关系和区别**在于：DebugHarness同样旨在模拟人类工程师的交互式调试实践，但其核心创新在于突破了纯静态分析的局限。与PatchAgent等仅依赖静态导航的方法不同，DebugHarness让LLM智能体能够主动查询**实时运行时环境**，利用模式引导的调查策略、交互式探测程序内存状态和执行路径，并通过闭环验证循环合成补丁。这填补了静态LLM推理与底层系统编程动态复杂性之间的鸿沟，从而在修复复杂安全漏洞（尤其是内存安全违规）方面实现了显著超越现有最佳基线的性能提升。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为DebugHarness的自主调试代理系统来解决复杂内存安全漏洞的自动修复问题。其核心方法是模拟人类系统工程师的交互式调试实践，将动态执行上下文引入到基于大语言模型（LLM）的自动程序修复流程中，而非仅依赖静态代码分析。

**整体框架与工作流程**：系统采用一个结构化的闭环调试工作流，主要分为三个阶段。首先，在**签名驱动的初始化**阶段，系统解析可重现的崩溃报告（如由消毒剂提供的PoC输入），识别漏洞类型和关键上下文。其次，进入**模式引导的调查**阶段，这是核心创新所在。LLM代理在此阶段扮演“调查员”角色，它基于初始信息形成假设，并主动与**动态系统工具**（如调试器GDB、内存检查工具Valgrind、进程检查工具/proc）进行交互式查询，以探查程序运行时的内存状态和执行路径，动态收集证据。最后，在**闭环验证与合成**阶段，LLM代理综合调查结果，生成补丁代码，然后系统自动编译、运行测试（包括回归测试和模糊测试）来验证补丁的有效性。如果验证失败，工作流会反馈信息并引导代理重新进入调查循环，直至问题解决或超时。

**主要模块/组件**：
1.  **LLM驱动的自主代理**：作为系统的“大脑”，负责规划调试策略、生成查询、分析动态反馈并合成补丁。
2.  **动态执行环境接口**：这是关键组件，封装了对GDB等底层调试工具和系统运行时信息的访问，使LLM能够以编程方式“观察”和“询问”运行中的程序状态。
3.  **模式引导的调查策略**：指导代理如何系统性地提出假设并设计动态查询来验证或推翻它们，模仿了人类的调试启发式方法。
4.  **闭环验证引擎**：负责自动构建、测试生成的补丁，确保修复不仅解决了崩溃，还保持了功能正确性。

**创新点**：
1.  **动态调试范式**：最大的创新是将LLM的静态代码推理能力与程序的**动态运行时上下文**深度融合，通过主动查询实时运行环境来诊断需要动态观察的复杂内存违规问题（如use-after-free）。
2.  **仿生交互式工作流**：设计了一个模拟人类专家调试习惯的、交互式、假设驱动的工作流，使LLM代理能够进行有导向的深入调查，而非一次性代码生成。
3.  **闭环自主修复**：将动态诊断、补丁生成和自动化验证集成在一个闭环中，实现了从崩溃触发到验证修复的端到端自动化，显著提升了修复成功率和可靠性。

### Q4: 论文做了哪些实验？

论文的实验设置围绕评估DebugHarness在真实安全漏洞修复上的有效性。实验使用了SEC-bench数据集，这是一个包含真实世界C/C++安全漏洞的严格基准，涵盖了如释放后使用、内存损坏等深层低级故障。对比方法包括最先进的静态代码生成式LLM修复基线（如直接使用大型语言模型进行静态补丁生成的方法）。主要结果方面，DebugHarness成功修复了约90%的评估漏洞。与基线相比，这带来了超过30%的相对性能提升（例如，若基线修复率为约60%，则相对提升为(90%-60%)/60%=50%，但摘要中表述为“over 30%”）。关键数据指标包括：修复成功率约90%，以及相对于现有最佳方法的相对改进超过30%。这些结果证明了动态调试能显著增强LLM的诊断能力。

### Q5: 有什么可以进一步探索的点？

本文提出的DebugHarness系统在动态调试方面取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其当前评估主要集中于C/C++内存安全漏洞，未来可扩展至其他类型漏洞（如逻辑错误、并发缺陷）及更多编程语言（如Rust、Go），以验证范式的通用性。其次，系统依赖预定义的调试模式与启发式策略，可能难以覆盖所有复杂的交互场景；可探索引入强化学习或元推理机制，使代理能自主演化调试策略，适应更广泛、未知的故障类型。此外，动态执行与查询可能引入性能开销，在大型或分布式系统中需优化交互效率，例如通过选择性插桩或增量状态追踪来平衡深度与速度。最后，如何将动态信息更有效地融入LLM的推理过程（如设计专用的记忆模块或注意力机制）也是一个关键方向，以进一步提升诊断与修复的精准度。

### Q6: 总结一下论文的主要内容

这篇论文提出了DebugHarness，一个模拟人类动态调试过程的自主LLM驱动调试代理系统，用于自动修复复杂软件中的安全漏洞。核心问题是现有基于LLM的自动程序修复方法主要依赖静态代码分析，难以诊断和修复需要理解动态执行状态（如内存损坏、释放后使用）的低级安全漏洞。

方法上，DebugHarness将漏洞修复构建为一个动态交互式调试任务。系统以可复现的崩溃为起点，采用签名驱动的调查策略来指导LLM代理。它允许代理主动查询运行时环境，通过集成GDB、pwndbg、rr等工具来交互式探查程序内存状态和执行路径，从而形成并验证关于根本原因的假设。随后，系统会合成补丁并通过一个闭环验证周期（包括重新编译和测试）进行确认，若失败则迭代优化。

主要结论是，在包含200个真实C/C++安全漏洞的SEC-bench数据集上评估，DebugHarness成功修复了约90%的漏洞，相比最先进的静态基线方法（如PatchAgent和VulnResolver）取得了超过30%的相对提升。这证明了动态调试信息能显著增强LLM的诊断能力。该工作为自动程序修复建立了新范式，弥合了静态LLM推理与低级系统编程动态复杂性之间的鸿沟。
