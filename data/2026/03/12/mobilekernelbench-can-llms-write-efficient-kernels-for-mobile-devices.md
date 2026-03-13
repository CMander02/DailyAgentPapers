---
title: "MobileKernelBench: Can LLMs Write Efficient Kernels for Mobile Devices?"
authors:
  - "Xingze Zou"
  - "Jing Wang"
  - "Yuhua Zheng"
  - "Xueyi Chen"
  - "Haolei Bai"
  - "Lingcheng Kong"
  - "Syed A. R. Abu-Bakar"
  - "Zhaode Wang"
  - "Chengfei Lv"
  - "Haoji Hu"
  - "Huan Wang"
date: "2026-03-12"
arxiv_id: "2603.11935"
arxiv_url: "https://arxiv.org/abs/2603.11935"
pdf_url: "https://arxiv.org/pdf/2603.11935v1"
categories:
  - "cs.LG"
  - "cs.AI"
tags:
  - "代码生成"
  - "多智能体系统"
  - "移动计算"
  - "基准测试"
  - "工具使用"
  - "规划与执行"
relevance_score: 7.5
---

# MobileKernelBench: Can LLMs Write Efficient Kernels for Mobile Devices?

## 原始摘要

Large language models (LLMs) have demonstrated remarkable capabilities in code generation, yet their potential for generating kernels specifically for mobile de- vices remains largely unexplored. In this work, we extend the scope of automated kernel generation to the mobile domain to investigate the central question: Can LLMs write efficient kernels for mobile devices? To enable systematic investigation, we introduce MobileKernelBench, a comprehensive evaluation framework comprising a benchmark prioritizing operator diversity and cross-framework interoperability, coupled with an automated pipeline that bridges the host-device gap for on-device verification. Leveraging this framework, we conduct extensive evaluation on the CPU backend of Mobile Neural Network (MNN), revealing that current LLMs struggle with the engineering complexity and data scarcity inher-ent to mobile frameworks; standard models and even fine-tuned variants exhibit high compilation failure rates (over 54%) and negligible performance gains due to hallucinations and a lack of domain-specific grounding. To overcome these limitations, we propose the Mobile K ernel A gent (MoKA), a multi-agent system equipped with repository-aware reasoning and a plan-and-execute paradigm.Validated on MobileKernelBench, MoKA achieves state-of-the-art performance, boosting compilation success to 93.7% and enabling 27.4% of generated kernelsto deliver measurable speedups over native libraries.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探索大型语言模型（LLM）在移动设备上自动生成高效计算内核（kernel）的能力，并解决该领域存在的核心挑战。研究背景是，尽管LLM在代码生成方面已取得显著成功，且在服务器级GPU的CUDA内核生成上展现出硬件感知能力，但随着移动AI应用的激增，在资源受限的移动设备上进行高效推理部署的需求日益迫切。然而，移动端内核开发具有独特性：优先考虑兼容性（需支持大量算子以确保模型迁移）、工程复杂度高（面临移动生态碎片化、异构后端和架构的挑战）以及数据稀缺（缺乏高质量参考实现），这使得现有面向服务器端的方法难以直接适用。

现有方法的不足主要体现在两方面：一是当前的基准测试通常关注内核的算法复杂度，而非移动兼容性所需的算子多样性；二是由于内核与特定框架紧密耦合，缺乏能够在移动设备上直接系统化评估LLM生成内核的自动化流程。因此，LLM在移动框架上面临工程复杂性和数据稀缺的内在困难，导致生成的内核编译失败率高、性能增益有限。

本文要解决的核心问题是：**LLM能否为移动设备编写高效的内核？** 为此，论文引入了MobileKernelBench这一综合评估框架（包括注重算子多样性的基准测试和实现设备端验证的自动化流水线），并基于此系统评估了当前LLM的局限性。进一步地，为克服这些限制，论文提出了MoKA（移动内核代理），一个具备仓库感知推理和规划-执行范式的多智能体系统，旨在提升编译成功率和生成内核的性能，从而推动移动端自动内核生成的前沿发展。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：代码生成与优化、专用基准评测以及移动端推理框架。

在**代码生成与优化方法**方面，相关工作主要集中于服务端高性能计算。一类研究（如KernelBench、MultiKernelBench、TritonBench）建立了评估LLM生成内核正确性与效率的基准。另一类研究通过强化学习或监督微调（如Kevin、AutoTriton、CUDA-L1/L2）来优化内核生成，或采用智能体协作框架（如Astra、EvoEngineer、CudaForge）来融入硬件知识进行推理。本文提出的MoKA系统也属于此类，但关键区别在于，上述工作主要针对CUDA和服务器GPU，而本文首次将焦点转向了资源受限、生态碎片化的移动设备。

在**评测基准与框架**方面，现有基准（如前述KernelBench系列）主要面向服务器环境。本文则针对移动设备的独特性，首次构建了MobileKernelBench，其特点是强调算子多样性和跨框架互操作性（基于ONNX标准），并提供了实现端侧验证的自动化流水线，填补了该领域的空白。

在**移动端应用与优化**方面，相关研究涉及移动推理引擎（如MNN、NCNN、TFLite）及其所需的底层硬件感知优化（如算法选择、内存布局）。本文的工作与这些引擎的目标一致，即追求高效的端侧执行，但本文的贡献在于首次系统地探索了使用LLM为这些轻量级引擎自动生成高效内核的可行性及挑战，并提出了针对性的解决方案。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MoKA（Mobile Kernel Agent）的多智能体系统来解决移动设备高效内核生成的问题。其核心方法是采用一个“规划-执行”的迭代范式，将复杂的算子实现、调试和优化任务分解给三个各司其职的智能体，并通过共享记忆和领域专用工具来克服现有LLMs在工程复杂性和领域知识匮乏方面的局限。

整体框架是一个自动化闭环流水线。系统首先由**Coder（编码器）** 根据任务描述生成初始的C++内核代码。生成的代码随后被送入评估流水线进行编译、正确性和性能测试。测试结果的结构化反馈（如编译错误、输出不符、性能指标）将触发相应的智能体介入，进行迭代优化。

主要模块包括三个协同工作的智能体：
1.  **Coder**：作为系统的唯一执行器，负责根据任务描述或来自其他智能体的高级策略，生成或修改具体的C++源代码。
2.  **Debugger（调试器）**：在流水线失败时被激活，处理两种错误模式。针对编译失败，它启动**编译诊断（修复计划）**；针对输出不正确，它启动**功能校正（校正计划）**。
3.  **Accelerator（加速器）**：在算子通过功能验证后启动，致力于性能优化。它分析性能剖析日志，提出**加速计划**以优化内存访问模式或计算逻辑。

关键技术创新点在于：
*   **多智能体分工与迭代规划**：将单一复杂任务分解为编码、调试、优化三个专业化角色，通过迭代反馈循环逐步收敛到高质量实现。
*   **反射记忆（Reflective memory）**：一个共享的历史记忆机制，记录过去的策略及其结果，使智能体能够进行自我反思，避免重复错误并剪枝无效的优化路径。
*   **领域专用工具集**：为解决LLMs缺乏对移动框架特定结构的认知问题，集成了两类工具。**仓库感知工具**（如仓库树构建器、错误提取器）帮助理解代码库结构和解析编译器日志，精准定位依赖和语法错误。**信息解析工具**（如模型解析器、性能解析器）将静态计算图模型和动态性能日志转化为结构化表示，为语义对齐和瓶颈分析提供依据。

通过这种架构设计，MoKA将智能体的推理过程“锚定”在具体的部署环境约束中，显著提升了编译成功率和生成内核的性能，从而有效回答了论文的核心问题。

### Q4: 论文做了哪些实验？

论文在MobileKernelBench框架下进行了系统实验，评估LLM为移动设备生成高效内核的能力。

**实验设置与数据集**：实验以MNN（v3.2.2）推理引擎的CPU后端为目标平台，在搭载骁龙8 Gen 2的小米13手机上进行。评估基准是MobileKernelBench，它强调算子多样性和跨框架互操作性。评估指标包括编译成功率（CSR）、功能正确率（FCR）以及相对于原生MNN实现达到特定加速比阈值（p）的任务比例（fast$_p$）。

**对比方法与主要结果**：
1.  **基线LLM评估**：测试了包括GPT-5、Claude-Sonnet-4.5、Gemini-2.5-Flash及多个开源模型在内的六种SOTA LLM。结果显示，即使表现最好的Claude-Sonnet-4.5，其CSR仅为46.3%，FCR为34.2%，fast$_{1.0}$（加速比≥1）仅为16.3%，fast$_{1.5}$（加速比≥1.5）低至4.7%。开源模型表现更差。
2.  **监督微调（SFT）**：使用LoRA对Qwen3-32B进行微调。相比基础模型（CSR 16.7%，FCR 13.9%），微调后CSR提升至25.0%，FCR提升至18.5%，但未能产生任何fast$_{1.5}$的加速。
3.  **强化学习（RL）**：使用GRPO对Qwen3-4B-Instruct进行训练。相比基础模型（CSR 10.0%，FCR 5.0%），训练后CSR提升至25.0%，但FCR仅微增至7.5%，fast$_{1.0}$维持在5.0%。
4.  **所提方法MoKA**：这是一个多智能体系统。以Claude-Sonnet-4.5为基础，经过10轮迭代，MoKA取得了显著优于所有基线方法的结果：CSR达到93.7%，FCR达到75.3%，fast$_{1.0}$达到46.8%，fast$_{1.5}$达到27.4%。其性能也大幅超过了同一模型的pass@10采样策略。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于主要聚焦于CPU后端和单一框架（MNN），且未深入探索低层优化技术。未来研究可从多维度拓展：一是技术深化，如支持多线程NEON、内联汇编等底层优化，并扩展至GPU、NPU等移动端硬件后端，以提升性能上限；二是框架泛化，将评估体系适配到TensorFlow Lite、PyTorch Mobile等更多框架，检验方法的跨平台鲁棒性；三是流程自动化，探索从算子生成到完整部署框架的端到端自动化，降低工程门槛。此外，可结合强化学习或代码检索增强，让Agent动态学习移动硬件的约束与优化模式，减少“幻觉”并提升生成代码的实用性。这些方向有望进一步释放LLM在边缘计算中的潜力。

### Q6: 总结一下论文的主要内容

该论文针对大型语言模型（LLM）能否为移动设备编写高效计算内核的问题展开研究。核心贡献是提出了一个系统性的评估框架 MobileKernelBench，它包含一个注重算子多样性和跨框架互操作性的基准测试，以及一个自动化流水线，用于实现主机-设备间的验证。研究发现，当前LLM（包括微调版本）因工程复杂性和移动框架数据稀缺，在移动设备内核生成上表现不佳，编译失败率高（超过54%），且性能提升微乎其微。为克服这些限制，论文提出了 Mobile Kernel Agent (MoKA)，这是一个具备仓库感知推理和“规划-执行”范式的多智能体系统。实验表明，MoKA 实现了最先进的性能，将编译成功率提升至93.7%，并使27.4%的生成内核相比原生库获得了可测量的加速。该工作揭示了LLM在移动端代码生成的挑战，并提供了一个有效的解决方案和评估基准。
