---
title: "DryRUN: On the Role of Public Tests in LLM-Driven Code Generation"
authors:
  - "Kaushitha Silva"
  - "Srinath Perera"
date: "2026-04-23"
arxiv_id: "2604.21598"
arxiv_url: "https://arxiv.org/abs/2604.21598"
pdf_url: "https://arxiv.org/pdf/2604.21598v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "LLM驱动的代码生成"
  - "多智能体框架"
  - "自生成测试输入"
  - "算法过度自信缓解"
  - "模拟驱动调试"
relevance_score: 8.5
---

# DryRUN: On the Role of Public Tests in LLM-Driven Code Generation

## 原始摘要

Multi-agent frameworks are widely used in autonomous code generation and have applications in complex algorithmic problem-solving. Recent work has addressed the challenge of generating functionally correct code by incorporating simulation-driven planning and debugging, where language models trace execution steps to verify logic. However, these approaches depend on human-provided public test cases to ground the debugging and simulation loop. Manually authoring comprehensive input-output examples is a labor-intensive bottleneck in the software development lifecycle. Because ground-truth input-output examples are rarely available prior to implementation in real-world software engineering, this dependency restricts methods to curated competitive programming benchmarks. Furthermore, we identify that reliance on these public tests induces an ``overconfidence gap,'' causing frameworks to overfit to simplistic examples and fail on hidden evaluations. In contrast, we observe that external sample inputs are not strictly necessary for code generation. We demonstrate that large language models can autonomously generate valid inputs and simulate execution traces to self-correct. Consequently, we develop DryRUN, a framework that eliminates the need for ground-truth samples by allowing the LLM to iteratively plan, autonomously generate its own inputs and simulate execution, mitigating algorithmic overconfidence. Evaluations on the LiveCodeBench v6 dataset (post-March 2025) demonstrate that DryRUN matches performance against CodeSIM, a state-of-the-art and public-test-dependent framework, while operating entirely without public test cases or external execution feedback while reducing output token consumption.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前基于大语言模型（LLM）的多智能体代码生成框架对人工提供的公共测试用例（public test cases）的深度依赖问题。现有方法，如CodeSIM等，在代码生成的预推理和事后调试阶段，都明确依赖这些标有输入-输出示例的公共测试来驱动逻辑验证和缺陷修复。然而，在真实的软件工程场景中，地面真值（ground-truth）的输入-输出示例在代码实现前几乎不可用，这种依赖导致方法被局限在特定编程竞赛基准上。更重要的是，论文识别出一个“过度自信差距”（Overconfidence Gap）：由于标准基准中的公共测试通常过于简化，模型在这些测试上通过后，容易对隐藏的复杂边缘案例掉以轻心，导致最终失败。人工编写全面覆盖边界情况的测试用例又极为耗时。因此，本文要解决的核心问题是：能否在不依赖任何外部公共测试或执行反馈的前提下，让LLM自主生成有效输入并模拟执行轨迹来自我纠正逻辑错误，从而消除对公共测试的依赖并缓解过度自信问题。为此，作者提出了DryRUN框架。

### Q2: 有哪些相关研究？

相关研究可按评测、方法、闭环调试三类组织。在评测类中，早期基准如HumanEval、MBPP因数据污染已不再可靠，LiveCodeBench、SWE-Bench-Live等新基准使用训练截止后的问题进行无污染评估，并依赖少量人工撰写的公共测试用例。本文指出这种依赖在实践中不可扩展，且易导致模型过拟合。

在方法类中，早期工作如Chain-of-Thought、结构化CoT等专注于通过提示策略提升零样本生成质量，但不利用执行反馈。随后闭环调试方法利用执行反馈迭代修复，包括早期自调试（如AgentCoder、Reflexion）和生成自主测试集的框架（如CodeT、S*）。但这些LLM生成的测试常不可靠。AlphaCodium通过锚定人工样本I/O解决此问题。最新框架如MapCoder和CodeSIM则完全放弃自主测试生成，转而严格依赖公共测试用例进行模拟执行调试。本文与这些方法的关键区别在于：DryRUN完全消除对人工公共测试的依赖，通过让LLM自主合成输入并模拟执行轨迹来驱动自纠正，避免了人工编写测试的瓶颈和公共测试导致的“过度自信”问题。

在应用评估中，本文在LiveCodeBench v6（2025年3月后）上与依赖公共测试的SOTA框架CodeSIM进行对比，在无公共测试且节省输出token的情况下达到了同等性能。

### Q3: 论文如何解决这个问题？

DryRUN框架通过一个多阶段循环过程解决对公开测试用例的依赖问题，核心设计围绕“自主生成输入”和“心理模拟执行”展开。整体框架包含四个主要阶段：初始规划、迭代计划优化、代码生成与痕迹驱动的自我修正、以及最终代码润色。

首先，框架基于问题定义P，提示LLM生成一个逐步实现计划，随后进入N\_plan轮次的无外部反馈自主优化循环。在这一阶段，LLM自行识别并消除初步的逻辑疏忽，通过提示优化计划细节、添加更多边缘情况，从而独立提升计划质量。

在计划优化后，框架生成初始代码草稿，并启动核心模拟循环（N\_sim轮次）。每轮循环中，LLM根据问题约束自主合成一个非平凡的合法输入样例，然后逐行模拟当前代码对该输入的执行过程，追踪变量状态以暴露隐藏的逻辑缺陷。生成的执行痕迹被反馈给计划模块，显式更新实现计划以修复所发现的错误，随后重新生成代码。这一过程完全依赖LLM自身的能力，不使用任何人工编写或沙盒执行的输入输出示例。

最后，框架执行最终润色阶段：LLM回顾最终计划及最新代码，修复潜在的语法异常、提升代码风格清晰度，并确保代码与计划完全对齐，从而补偿因缺乏外部执行而可能引入的误差。

关键技术包括：自主样例输入生成、心理模拟执行追踪、无外部反馈的计划优化循环，以及最终润色机制。创新点在于完全消除对公开测试用例或外部执行反馈的依赖，同时通过模拟执行有效缓解了算法自信度过拟合问题，在LiveCodeBench v6数据集上达到了与依赖公开测试用例的CodeSIM框架相当的性能，并减少了输出token消耗。

### Q4: 论文做了哪些实验？

论文在LiveCodeBench V6数据集上进行实验，该数据集仅包含2025年3月后发布的80个问题（37个困难、25个中等、18个简单），以确保无数据污染。实验使用gpt-5-mini和gemini-3-flash两个大模型，温度默认或设为1.0，DryRUN配置为N_plan=2和N_sim=2。对比方法包括直接生成（带/不带公共测试）、以及使用公共测试的最先进模拟框架CodeSIM。

主要结果如下：在gpt-5-mini上，DryRUN总体Pass@1达67.5±2.5%，CodeSIM为64.2±7.5%，DryRUN高出3.3%；在gemini-3-flash上，CodeSIM为74.6±1.9%，DryRUN为69.6±3.1%，CodeSIM高出5.0%，但标准差重叠表明性能相当。值得注意的是，直接生成（不带公共测试）在部分子集上反而优于带公共测试版本，说明公共测试并非必需。在困难子集上，DryRUN的Pass@1最佳达53.15±5.63%，远超零样本的27.93%。此外，DryRUN平均消耗28,567个token（输出10,670），仅为CodeSIM（40,976 token，输出22,054）的70%，效率显著更高。消融实验表明，每个组件（计划、细化、模拟、精修）均逐步提升性能，最终完整框架达最优。

### Q5: 有什么可以进一步探索的点？

论文展示了DryRUN在消除对公开测试依赖方面的优势，但仍有进一步探索的空间。首先，其无条件规划与模拟策略虽然避免了过拟合，但可能因缺乏外部信号而无法纠正某些隐蔽错误，未来可研究动态调整模拟轮数（如基于自评估置信度）的理论依据。其次，实验显示DryRUN在困难问题上表现略逊于CodeSIM，这暗示自主生成的输入可能仍不够复杂或覆盖不全，改进方向包括引入多样性约束或进化搜索策略以生成更具挑战性的测试输入。此外，论文主要关注竞争性编程任务，未来应验证该方法在更实际的软件工程场景（如API调用、多文件项目）中的可扩展性。最后，当前框架依赖LLM的思维链模拟，当代码涉及复杂数值计算或长序列时可能准确率下降，可探索结合符号执行或轻量级可微验证器（如差分测试）来增强模拟可靠性，从而平衡自足性与执行准确性。

### Q6: 总结一下论文的主要内容

本文研究了LLM驱动代码生成中公共测试用例的作用，发现现有方法依赖人工编写的输入输出样例进行推理和调试，但这在真实开发中不可行，且导致模型过度拟合简单样例而无法通过隐藏测试的“过度自信差距”。为解决此问题，论文提出DryRUN框架，其核心创新在于让LLM自主生成有效输入并模拟执行轨迹进行自我修正，完全摆脱对公共测试用例和外部执行反馈的依赖。在LiveCodeBench v6最新数据集上的实验表明，DryRUN在不使用任何人类标注样例的条件下，性能与依赖公共测试的先进方法CodeSIM持平，同时减少了输出token消耗，有效缓解了过拟合问题。该工作质疑了公共测试的必需性，为自动化代码生成提供了新范式。
