---
title: "Recursive Agent Harnesses"
authors:
  - "Elias Lumer"
  - "Sahil Sen"
  - "Kevin Paul"
  - "Vamse Kumar Subbiah"
date: "2026-06-11"
arxiv_id: "2606.13643"
arxiv_url: "https://arxiv.org/abs/2606.13643"
pdf_url: "https://arxiv.org/pdf/2606.13643v1"
categories:
  - "cs.CL"
tags:
  - "多智能体协作"
  - "递归Agent"
  - "长上下文推理"
  - "代码Agent"
  - "Agent架构"
relevance_score: 9.5
---

# Recursive Agent Harnesses

## 原始摘要

Recursive language models (RLMs) showed that recursion over model calls is an effective strategy for long-context reasoning, and production coding agents have begun to write code that spawns subagents at scale, most recently in Anthropic's dynamic workflows. We name and study the pattern between these two lines of work, where the recursive unit is a full agent harness with filesystem tools, code execution, and planning rather than a model call with no tools. We call this the Recursive Agent Harness (RAH) and frame it as harness recursion, the code-first extension to the model recursion of RLMs. A parent agent generates and runs an executable script that spawns subagent harnesses in parallel for fine-grained workloads and uses structured function calls for small subtasks. We provide a controlled evaluation on long-context reasoning. With the backbone held fixed at GPT-5 to match the published Codex and RLM baselines, RAH improves the Codex coding-agent baseline from 71.75% to 81.36% on Oolong-Synthetic (199 samples, 13 context-length buckets up to 4M tokens), a gain attributable to the harness rather than the model. With a stronger backbone, Claude Sonnet 4.5, the same design reaches 89.77%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有长上下文推理方法在处理细粒度、多条目任务时的局限性。研究背景中，现有的编码型代理（coding agents）虽然具备文件系统访问和代码执行等工具，但面对需要逐条进行LLM推理的独立条目（如Oolong基准测试中数千个键值对）时，它们只能退化为基于正则表达式的启发式方法，无法为每个条目调用LLM，导致推理质量低下。另一方面，递归语言模型（RLMs）虽然通过递归划分上下文来实现细粒度推理，但它们缺乏工具访问能力，无法执行文件操作或子代理生成。现有工作（如Anthropic的动态工作流）虽已开始在生产中通过代码生成子代理，但并未系统性地研究将完整代理框架（包括工具、文件系统、上下文工程等）作为递归单元的模式。

本文核心问题是：当代理在长上下文任务中进行递归时，递归单元应该是一个无工具的模型调用（如RLM），还是一个具备完整工具集的代理框架？为此，论文定义并研究了递归代理框架（Recursive Agent Harness, RAH），其中父代理生成可执行代码，为每个条目并行生成独立子代理框架，每个子代理拥有独立的上下文窗口、文件系统和LLM调用，从而实现代码优先的框架递归。通过控制模型主干（GPT-5）的实验，RAH将编码型代理基线从71.75%提升至81.36%，证明了框架而非模型本身带来的性能改进。

### Q2: 有哪些相关研究？

相关工作主要分为几类。**方法类**中，Zhang等人提出的递归语言模型(RLM)通过模型递归实现长上下文推理，在Oolong-Synthetic上达到64.38%；本文的递归Agent框架(RAH)将其扩展为带工具的完整Agent递归，证明了将递归单元从纯模型调用升级为完整Agent框架能带来显著提升（从71.75%到81.36%）。**应用类**方面，Anthropic动态工作流已在大规模生产中使用代码生成子Agent，与RAH的代码优先生成模式一致，但RAH将其置于递归语言模型的理论框架下，并提供了受控评估；Minions等编排框架使用多工作模型，CodeAct强调代码作为有效交互方式，RAH将这些结合用于长上下文推理。**系统类**中，Lambda-RLM使用固定结构静态管道分解任务，而RAH通过执行脚本动态适配；AGENTHIVE将子Agent生成定义为Schema原语，RAH则直接嵌入可执行代码，支持并发和参数化。并行函数调用和记忆管理相关工作分别从不同角度处理资源限制，RAH通过分配独立子Agent避免了共享状态，与MemGPT的页面交换策略形成对比。

### Q3: 论文如何解决这个问题？

RAH的核心方法是将整个代理框架（而非单纯的模型调用）作为递归单元。在架构上，父代理接收完整任务后，通过两种方式生成子代理：标准JSON工具调用路径受限于每轮工具调用预算，而代码执行路径是RAH的关键创新——父代理通过shell工具编写并执行Python脚本，利用asyncio.gather并行实例化数千个子代理框架，绕过API的调用限制。每个子代理都是完整的代理框架，配备read_file、write_file、grep、execute等文件系统工具、代码执行和规划能力，并能像父代理一样递归生成孙代理，递归深度默认可配置为3层。对于小规模任务（1-5条），父代理直接使用结构化函数调用；超过阈值则自动切换至脚本路径。子代理在隔离工作空间中独立运行，通过共享输出文件聚合结果，无进程间通信开销。创新点包括：将代码视为一等行动而非固定工具模式，通过生成脚本实现与模型无关的并行扩展，以及使完整代理框架而非模型调用成为递归单元。实验固定GPT-5骨干网络，RAH将Codex编码代理基线从71.75%提升至81.36%，使用Claude Sonnet 4.5时更达89.77%。

### Q4: 论文做了哪些实验？

论文在长上下文推理基准测试 Oolong-Synthetic 上评估了递归智能体框架（RAH）。实验设置使用 199 个样本，覆盖从 1K 到 4M tokens 的 13 个上下文长度桶（平均 629K tokens/实例）。对比方法包括全上下文基线（59.22%）、模型递归 RLM（64.38%）和 Codex 编码智能体（71.75%），所有基线均使用 GPT-5 骨干网络。RAH 在相同骨干网络下将 Oolong Score 从 71.75% 提升至 81.36%（95% CI [76.0, 86.5]），增益归因于框架架构而非模型。使用更强的 Claude Sonnet 4.5 骨干网络时，RAH 达到 89.77%。按答案类型分析，USER、COMPARISON 和 LABEL 语义类型得分均超过 86%，NUMERIC 类型为 69.33%，DATE 类型由于样本量小（n=5）为 60.00%。按上下文长度分析，Sonnet 4.5 在 524K tokens 以内保持 86% 以上，在 4M tokens 时仍有 76.7%；GPT-5 在大多数桶中超越 Codex 基线。主要发现是，将递归单元从模型调用扩展为完整智能体框架，显著提升了长上下文推理性能。

### Q5: 有什么可以进一步探索的点？

当前RAH仅在Oolong-Synthetic数据集上验证，泛化到Oolong-Real及证据更模糊的场景仍是开放问题。其失败模式包括父代理在超长上下文跳过子代理生成，以及NUMERIC评分机制低估连续量推理质量。未来可从三方面改进：一是系统分析递归深度、每子代理处理条目数、代码执行与工具调用路径等设计选择的独立贡献；二是解决父代理生成脚本的语法可靠性与长上下文稳定性；三是将RAH扩展到多文档问答、大型文档集审查等可分解为独立子任务的场景，同时建立成本-质量权衡的量化表征。此外，可探索动态递归策略（根据上下文复杂度自适应调整递归深度）和混合推理模式（在代码执行和工具调用间动态切换）。RAH的代码优先特性也暗示可将其与检索增强生成结合，通过子代理的代码执行能力实现更灵活的证据定位与交叉验证。

### Q6: 总结一下论文的主要内容

这篇论文定义并评估了"递归代理框架"（RAH）这一新范式。问题在于，现有的长文本推理方法存在盲区：编码型智能体将逐项推理简化为正则启发式，而递归语言模型缺乏工具访问权限。RAH的核心贡献在于，将完整的代理框架（包含文件系统工具、代码执行和规划能力）而非裸模型调用作为递归单元。方法上，父代代理通过编写可执行脚本并行生成子代理框架，绕过单次工具调用限制，支持大规模并行处理。主要结论：在GPT-5骨干网络固定的受控实验下，RAH在Oolong-Synthetic基准上将Codex编码智能体基线从71.75%提升至81.36%，证明增益来自框架而非模型；使用更强骨干网络时可达89.77%。该模式已在生产系统（如动态工作流）中出现，为长文本分解任务提供了可扩展的解决方案。
