---
title: "FastKernels: Benchmarking GPU Kernel Generation in Production"
authors:
  - "Gabriele Oliaro"
  - "Yichao Fu"
  - "May Jiang"
  - "Owen Lu"
  - "Junli Wang"
  - "Zhihao Jia"
  - "Hao Zhang"
  - "Samyam Rajbhandari"
date: "2026-05-22"
arxiv_id: "2605.23215"
arxiv_url: "https://arxiv.org/abs/2605.23215"
pdf_url: "https://arxiv.org/pdf/2605.23215v1"
github_url: "https://github.com/Snowflake-AI-Research/fastkernels"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CL"
tags:
  - "GPU kernel generation"
  - "agent benchmark"
  - "production alignment"
  - "code agent"
  - "LLM-based code generation"
relevance_score: 9.5
---

# FastKernels: Benchmarking GPU Kernel Generation in Production

## 原始摘要

LLM-based agents for GPU kernel generation are advancing rapidly, yet their progress is fundamentally constrained by the benchmarks they optimize against. Existing benchmarks are poorly aligned with production inference frameworks: they evaluate kernels on a single GPU with synthetic inputs, ignore the surrounding compilation stack, and reward replicating known optimizations rather than discovering new ones. The resulting reward signals are misleading: agents learn to generate kernels that score well in sandboxes but introduce interface incompatibilities, compilation-stack conflicts, and silent correctness degradation when integrated into real systems. We introduce FastKernels, a kernel benchmark built around a minimal set of 46 representative architectures spanning 8 categories, whose kernels collectively subsume those of 96.2% (409/425) of HuggingFace Transformers architectures. FastKernels doubles as a minimalistic, production-grade inference framework that runs at parity with hardened systems such as vLLM and SGLang on mainstream LLM serving and substantially exceeds upstream references on under-served architectures; each task's interface mirrors the corresponding module in the state-of-the-art library for its architecture family, enabling direct deployment of optimized kernels into production codebases. Evaluating state-of-the-art kernel agents on FastKernels, we find that even the strongest agent achieves only 0.94$\times$ aggregate speedup over production baselines, with weaker agents at $0.78\times$ and $0.53\times$ -- confirming that benchmark-production misalignment is a critical bottleneck for the field. We release FastKernels as a stepping stone toward kernel agents whose benchmark gains translate directly into production throughput improvements. Code is available at https://github.com/Snowflake-AI-Research/fastkernels

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型的GPU内核生成代理在生产部署中面临的基准测试与实际生产环境严重脱节的问题。当前研究背景是，这类代理在孤立基准测试（如单GPU、合成输入）上表现优异，但将其生成的内核集成到vLLM、SGLang等实际推理框架时，性能提升往往无法有效迁移。现有方法的不足主要体现在三方面：第一，基准测试依赖合成输入和孤立内核，忽略了真实编译栈、模型级工作负载及多GPU通信模式的影响；第二，任务层级相互独立，无法复用低层优化结果，导致重复优化；第三，评估标准聚焦于孤立性能，未考虑接口兼容性、编译栈冲突或下游正确性退化。本文核心问题是消除基准-生产对齐鸿沟，提出FastKernels——一个兼具生产级推理框架功能的核基准测试。它通过覆盖46种真实架构的层级化、可组合任务（从原语到完整模型），匹配生产模块接口，并利用捕获的真实张量和并行模式进行评估，确保优化内核能直接产出生产吞吐量提升，从而解决代理生成的内核难以在真实系统中生效的瓶颈。

### Q2: 有哪些相关研究？

在GPU kernel生成领域，相关研究可分为方法类和评测类。评测类工作包括：KernelBench开创了LLM生成GPU kernel的评测，但基于AlexNet、VGG等早期架构；robust-kbench修复了KernelBench的数值不稳定和奖励黑客问题；SOL-ExecBench使用B200光速界限而非软件基线评分；FlashInfer-Bench集成推理引擎但限于FlashInfer LLM算子；CUDABench和TritonBench则孤立评估算子。这些工作均存在与生产环境脱节的问题。本文FastKernels填补了四个关键空白：首次包含多GPU通信kernel（覆盖张量并行和专家并行模式），将任务组织为从原语到完整模型的分层结构（模拟生产组装），使用真实推理框架中的实际kernel而非PyTorch参考实现或理论界限作为基线，并确保接口与vLLM、SGLang等SOTA框架的生产模块一致，支持直接复制部署。方法类工作开发了结合LLM推理与profiler反馈或进化搜索的推理时agent。这些系统通常基于算子级评测开发，FastKernels为这些进展提供了与生产对齐的评估平台。

### Q3: 论文如何解决这个问题？

FastKernels通过一套严格对齐生产环境的基准设计来解决现有基准与真实推理框架的严重脱节问题。核心方法是自上而下的任务构建：直接从46个代表性模型架构（覆盖HuggingFace 96.2%的架构）的推理路径中递归分解出所有计算内核，确保每个内核都能追踪到特定模型的特定层，而非合成或子图提取。架构设计分为四个层级：Level 1基础算子（如GQA注意力、RMSNorm）、Level 2融合算子（如残差+归一化+量化）、Level 3完整模块（如Transformer解码层、MoE层）、Level 4端到端模型推理。创新点包括：1）接口兼容性设计，每个任务的接口严格匹配vLLM、SGLang等生产库中对应模块的构造函数和forward方法签名，优化后的内核可直接复制部署，无需重构；2）首次将多GPU通信内核（如张量并行all-reduce、专家并行all-to-all）作为一等公民任务，因为单GPU加速可能破坏通信调度反而降低整体吞吐；3）三层基准栈（Tier 1内核级、Tier 2端到端、Tier 3标准化评测）确保从孤立算子优化到全模型推理的闭环验证，使用生产派生的输入形状和真实捕获的张量进行正确性与性能测量。整体框架本身即为一个最小化的生产级推理引擎，能独立运行并产生与vLLM相当的效率，同时内建NVIDIA Nsight profiling集成和MLflow跟踪链路。

### Q4: 论文做了哪些实验？

论文针对FastKernels基准进行了两项实验。**实验一：基准自身性能评估**。在46个代表性架构上，以各架构族最强的生产推理框架（如LLM用vLLM/SGLang、SDXL用diffusers、线性注意力用FLA）为基准，测量端到端吞吐量和数值正确性。结果显示，FastKernels平均吞吐量达1.24倍（中位数1.04倍），但分布呈双峰：主流LLM服务与vLLM等持平（如Llama-3.1为1.04×），而缺乏优化参考的架构（如Pi0 3.48×、ColBERTv2 3.08×）提升显著。**实验二：评估现有核生成Agent**。测试Dr. Kernel、KernelAgent和OpenAI Codex三个Agent在FastKernels L1（48个任务）和L2（40个任务）上的性能。关键结果：Codex以0.943×的几何平均加速比领先，KernelAgent为0.777×，Dr. Kernel仅0.527×，均低于1×。Agent在L2任务上表现更差（如KernelAgent正确率从26/40降至2/36，加速比从0.79×降至0.629×）。失败主要源于：生产级别参考（如cuBLAS）而非PyTorch eager导致增益消失（如linear仅0.56×），以及Agent无法满足生产级复合模块的契约（如attention、fused_experts）。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于基准测试的覆盖范围与评估粒度的平衡。首先，L1/L2层级的任务设计可能过于聚焦已知模式优化，未能充分挖掘agent在新型算子发现上的潜力；未来可增设L3/L4任务，测试agent在完全未见过架构上的零样本生成能力。其次，评估体系依赖人工验证的架构映射，存在覆盖边界模糊问题，建议引入自动化的等价性验证流程，如利用形式化方法检测输出精度退化。性能评估仅基于H100 GPU，在AMD MI300X或消费级GPU上的行为差异未被考虑，未来需构建跨硬件平台的验证管道。此外，MacroEval的等权重加权结合可能掩盖长尾架构的实际收益，可尝试基于生产实际请求频率的加权方案。最后，当前任务镜像生产接口但未完全捕捉动态张量形状和运行时调度冲突，建议引入实时编译器（如Triton IR）的冲突检测器作为奖励信号的一部分，使agent在生成时主动规避编译栈干扰。

### Q6: 总结一下论文的主要内容

FastKernels论文针对GPU内核生成领域基准测试与生产环境严重脱节的问题，提出了一个创新解决方案。问题在于现有基准测试依赖单GPU和合成输入，忽略编译栈影响，且奖励已知优化而非新发现，导致智能体生成的核在沙箱中表现优异，但集成到实际推理系统时会引发接口不兼容、编译冲突和正确性退化。FastKernels构建了一个由8大类46个代表性模型架构组成的基准测试，覆盖96.2%的HuggingFace Transformers架构。它同时作为一个最小化生产级推理框架，性能与vLLM和SGLang相当，并采用组合式任务层次（从基础算子到融合算子、层、完整模型）支持动态规划优化。评估显示，最强内核智能体仅达到生产基线0.94倍加速，较弱者更差，证实了基准-生产对齐是核心瓶颈。该研究的核心贡献是提供了一个基准即框架的设计，确保优化的内核能直接部署到生产代码中，为将基准测试收益转化为实际吞吐量提升铺平了道路。
