---
title: "Agentic Framework for Deep Learning workload migration via In-Context Learning"
authors:
  - "Qiyue Liang"
  - "Steven Ingram"
  - "George Vanica"
  - "Andi Gavrilescu"
  - "Newfel Harrat"
  - "Hassan Sipra"
  - "Sethuraman Sankaran"
date: "2026-06-14"
arxiv_id: "2606.15994"
arxiv_url: "https://arxiv.org/abs/2606.15994"
pdf_url: "https://arxiv.org/pdf/2606.15994v1"
github_url: "https://github.com/AI-Hypercomputer/accelerator-agents"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "LLM Agent"
  - "In-Context Learning"
  - "Self-Debugging"
  - "Code Migration"
  - "Autonomous Agent"
  - "Deep Learning Workload Migration"
relevance_score: 8.5
---

# Agentic Framework for Deep Learning workload migration via In-Context Learning

## 原始摘要

Translating deep learning models from PyTorch's flexible, object-oriented design to JAX's functional, stateless setup is usually a manual and error-prone task. Automated migration is challenging because Large Language Models (LLMs) struggle with strict and dynamic API alignment and are prone to mistakes for exacting operations. We propose a fully autonomous system that combines In-Context Learning (ICL) with oracle-driven self-debugging. First, we curated an ICL context that serves as a strict reference for idiomatic JAX styling and test case generation. Second, instead of depending on the LLM to deduce mathematical outputs, we run the source PyTorch modules to get their actual dynamic tensor states. This creates an unchangeable execution oracle. We then use an autonomous agentic loop to synthesize tests based on the oracle data. The test cases are executed repeatedly, and the traceback is sent back to the LLM for self-correction. Ablations show that combining ICL references with oracle grounding and self-debugging greatly outperforms pure instructional and basic agentic baselines. This improvement does not add an excessive computational overhead. Our lightweight pipeline achieves 91% numerical equivalence (compared to baseline: 9%, instruction + self-debugging: 27%) on neural modules, providing a highly reliable, scalable blueprint for cross-framework migration. This has been validated across several state-of-the-art models including SAM (segment anything), T5, Code Whisper amongst others showing high numerical equivalency. Code: https://github.com/AI-Hypercomputer/accelerator-agents/tree/main/MaxCode

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决将深度学习模型从PyTorch框架迁移到JAX框架时面临的自动化难题。研究背景是，PyTorch采用面向对象、动态执行的设计，而JAX基于函数式、无状态编程并依赖JIT编译，两者在API范式、张量布局（如NCHW vs NHWC）、默认精度（fp32 vs bfloat16）及控制流结构（如jax.lax.scan替代Python原生循环）上存在根本差异，导致手动迁移极易出错且成本高昂。现有自动迁移方法依赖大型语言模型（LLM），但LLM在处理严格动态API对齐时表现不佳，容易在高维张量运算中产生数学幻觉，且缺乏可靠验证机制。核心问题在于：如何设计一个全自动系统，让LLM不仅能生成符合JAX函数式风格的代码，还能确保迁移后的模型在数学上精确等价于原始PyTorch模型。为此，论文提出结合上下文学习（ICL）的结构锚定与基于动态执行Oracle的自调试循环，以克服LLM的算术局限，实现高数值等价性的跨框架迁移。

### Q2: 有哪些相关研究？

在跨框架深度学习模型迁移领域，相关研究主要可分为三类：自动化迁移方法、大语言模型（LLM）代码生成与修复，以及基于oracle的验证技术。

**1. 自动化迁移方法类**：现有工作包括基于规则或模板的PyTorch-to-JAX转换器，以及尝试使用RAG（检索增强生成）引用MaxText等代码库的方法。本文指出，RAG方法因引入分布式计算等噪音，加剧了API幻觉（“Lost in the Middle”现象）。与之不同，本文采用**受控的上下文学习（ICL）**，仅提供紧凑的语法锚点（源模块、惯用JAX翻译、测试用例），避免上下文污染，显著提升对齐准确性。

**2. LLM代码生成与自调试类**：典型基线包括纯指令提示、指令加自调试循环。本文通过消融实验证明，纯指令下数值等价性仅9%-18%，引入自调试后提升至27%-89%，但仍有局限。本文创新性地结合**ICL锚点 + oracle驱动的自调试**，通过将实际PyTorch执行状态（权重、输入、激活）序列化为不可变oracle，使LLM依据真实计算而非数学推理进行修复，相比纯自调试，数值等价性从27%跃升至91%。

**3. oracel与验证技术类**：传统方法依赖启发式规则或LLM数学预测，易产生隐性错误。本文提出“Silver”测试用例，通过动态执行提取oracle，并采用严格的`numpy.allclose(绝对误差≤1e-7)`进行分层评估（编译→形状→数值），确保验证的可靠性。同时，将ICL示例与评测集严格分离，防止奖励黑客行为，保证泛化能力。

综上，本文通过ICL锚定语法、oracle提供真实计算锚点、自调试修正错误，三者协同，解决了现有方法依赖静态指令或噪声检索、数学推理脆弱等核心瓶颈。

### Q3: 论文如何解决这个问题？

该论文提出一个结合上下文学习与Oracle驱动自调试的完全自主化系统。核心架构分为四个自动化阶段：首先构建受控的ICL上下文，包含源PyTorch模块、惯用JAX翻译和测试用例的紧密参考集，作为功能框架的结构锚点，避免传统RAG方法引入的分布式计算噪声。其次，通过动态执行源PyTorch模块创建不可变Oracle产物——包含初始化权重、输入张量和输出激活值的序列化状态，从而绕过LLM在高维张量运算中的数学推理缺陷。第三阶段基于Oracle数据和ICL示例生成自适应测试框架（Silver测试用例），实现编译检查、形状一致性验证（含NCHW到NHWC的布局映射）和数值等价性检验（绝对误差容限10⁻⁷）。最后，当生成的JAX模块未通过Oracle条件测试时，将堆栈跟踪、精确数值差异等执行反馈馈入LLM上下文，结合ICL模板进行迭代自调试。

关键技术突破在于三个创新点：一是用密集ICL参考替代稀疏检索，消除API幻觉和上下文窗口过载；二是以动态执行获取真实张量状态作为不可变Oracle，替代LLM数学推演；三是建立防奖励破解的分离评估机制——自调试能力与最终评估基准分离，ICL示例不出现在测试集中。消融实验显示，结合ICL锚定、Oracle基准和自调试的全流水线在神经模块上达到91%数值等价性，远超纯指令基线（9%）和指令+自调试基线（27%），且计算开销可控。该系统已在SAM、T5、Code Whisper等主流模型上验证跨框架迁移的可靠性和可扩展性。

### Q4: 论文做了哪些实验？

论文进行了三组实验，涵盖从基础算子到完整代码仓库的迁移测试。实验设置包括三个难度层级：Level 1包含9个基础数学与训练操作（如数据混合、梯度裁剪、各类损失函数等）；Level 2包含11个神经网络模块（MLP、VAE、GAN、GRU、LSTM、注意力机制、Transformer编码器、图卷积、ResNet块等）；Level 3包含10个完整代码仓库（如Code Whisper、T5、SAM、DETR等）。对比方法包括：基线（简单提示）、仅指令提示、指令+自调试循环，以及本文完整流水线。主要结果表明：在Level 1上，本文方法达到100%数值等价（对比基线9%、指令+自调试27%）；在Level 2上达到91%形状和数值等价（对比仅指令18%、指令+自调试89%）。Level 3人类评估显示，完整流水线在绝大多数仓库上完成度100%，其中4个仓库达到100%数值等价，但SAM（80%）和DETR（57%）表现较差。研究还分类了三种典型失败模式：语法幻觉、API签名不匹配、状态映射差异。

### Q5: 有什么可以进一步探索的点？

该工作的局限性主要体现在两个方面：一是未扩展到完整的仓库级迁移，当前仅处理独立模块，而真实场景中模型涉及跨文件依赖、动态图控制流和复杂数据增强流水线，这些需要结构化的依赖管理。二是未系统研究ICL示例选择对结果的影响，不同架构（如Transformer vs CNN）可能对参考样例的敏感度不同，存在过拟合风险。

未来可从三个方向改进：引入图级别的依赖解析器，自动构建模块间的拓扑顺序，将迁移范围扩展至完整仓库；探索动态ICL示例检索机制，基于目标代码的AST特征自动匹配最相关的迁移范例；结合差分测试技术，验证迁移后模型的数值稳定性与梯度行为，超越简单的逐模块数值等价比较。此外，可考虑将日志驱动的调试循环升级为需求驱动的验证器，自动推断未被当前测试覆盖的边界条件。

### Q6: 总结一下论文的主要内容

将PyTorch模型迁移到JAX通常是手动且易错的工作，因为大语言模型(LLM)难以处理严格的API对齐和精确操作。本文提出了一个全自主的深度学习工作负载迁移框架，结合上下文学习(ICL)和基于oracle的自调试。核心贡献包括：1) 构建ICL上下文作为JAX样式和测试用例生成的严格参考；2) 运行源PyTorch模块获取真实张量状态作为不可变执行oracle，而非依赖LLM推导数学输出；3) 基于oracle数据自动合成测试并通过自主循环执行，将回溯反馈给LLM进行自我修正。实验表明，ICL参考结合oracle基础化和自调试显著优于纯指令和基本自主基线，在神经模块上实现了91%的数值等价性（基线9%，指令+自调试27%），且未增加过多计算开销，并在SAM、T5、CodeWhisper等先进模型上验证了高数值等价性。该框架为跨框架迁移提供了可靠、可扩展的蓝图，但尚未扩展到完整仓库级别迁移。
