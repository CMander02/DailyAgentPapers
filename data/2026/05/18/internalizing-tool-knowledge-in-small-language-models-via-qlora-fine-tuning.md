---
title: "Internalizing Tool Knowledge in Small Language Models via QLoRA Fine-Tuning"
authors:
  - "Yuval Shemla"
  - "Ayal Yakobe"
  - "Tanmay Agarwal"
date: "2026-05-18"
arxiv_id: "2605.17774"
arxiv_url: "https://arxiv.org/abs/2605.17774"
pdf_url: "https://arxiv.org/pdf/2605.17774v1"
categories:
  - "cs.CL"
tags:
  - "工具使用"
  - "小模型微调"
  - "QLoRA"
  - "参数高效微调"
  - "Agent规划"
  - "输入长度优化"
  - "灾难性遗忘"
relevance_score: 8.5
---

# Internalizing Tool Knowledge in Small Language Models via QLoRA Fine-Tuning

## 原始摘要

Large language models are increasingly used as planning components in agentic systems, but current tool-use pipelines often require full tool schemas to be included in every prompt, creating substantial token overhead and limiting the practicality of smaller models. This paper investigates whether tool-use knowledge can be internalized into small language models through parameter-efficient fine-tuning, enabling structured planning without explicit tool descriptions at inference time. Using AssetOpsBench as the primary benchmark, we fine-tune Gemma 4 E4B and Qwen3-4B with 8-bit QLoRA on approximately 1,700 tool-use examples spanning tool knowledge, question-to-plan mappings, and execution-style traces. We evaluate the resulting models under description-free inference, where the prompt omits the tool catalog entirely. The fine-tuned models outperform an informed unfine-tuned baseline that receives full tool descriptions, reducing input length by 82.6\% while improving structural and LLM-judge planning scores. In the best Gemma run, the model achieves an AT-F1 of 0.65 and an overall judge score of 3.88, compared with 0.47 and 2.88 for the informed baseline. Qwen3-4B achieves a strong overall judge score of 3.78 while using 62\% less memory and running 2.5$\times$ faster than Gemma, though it also exhibits greater catastrophic forgetting on general multiple-choice benchmarks. Additional ablations show that LoRA rank controls a quality--retention trade-off, with $r=32$ maximizing planning quality and smaller ranks preserving more general knowledge. These results suggest that, for fixed tool catalogs, QLoRA fine-tuning can shift tool knowledge from prompt context into model weights, substantially reducing inference overhead while maintaining or improving tool-planning quality.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型在工具使用代理系统中的两个关键效率问题。研究背景是，当前前沿模型常被用作代理系统的规划组件，但现有的工具使用流程要求每次推理时都在提示中附带完整的工具模式（包括名称、参数、描述等），这导致了巨大的token开销，并迫使开发者依赖昂贵的大模型。现有方法的不足主要体现在两方面：首先，小模型（如2B-5B参数规模）在没有详尽提示的情况下难以可靠地进行工具规划；其次，重复的工具上下文提示使每个查询的输入长度显著增加，造成高延迟和计算成本，在基准测试中工具描述可占输入token的82.6%。本文要解决的核心问题是：能否通过参数高效的微调方法，将工具使用知识内化到小型语言模型的权重中，从而实现在推理时无需提供显式工具描述的“无描述推理”模式。论文通过使用QLoRA对Gemma 4B和Qwen3-4B等小模型进行微调，旨在压缩输入长度（减少82.6%）、降低推理开销的同时，保持甚至提升工具规划的结构正确性和质量，为固定工具目录场景下的高效代理系统提供可行方案。

### Q2: 有哪些相关研究？

相关研究可分为三类：基准与框架类、方法类和应用类。在基准方面，IBM Research 提出的 AssetOpsBench 是本文的核心，它专门用于评估工业资产运维场景中 AI 代理的工具使用能力，包含152个人工生成的查询；本文以其作为训练数据生成和评估的主要基准，区别于其他通用工具使用benchmark。在方法上，本文基于参数高效微调技术，特别是 LoRA（低秩适应）及其量化版本 QLoRA，通过冻结预训练权重并注入可训练的低秩矩阵，在单张A100 GPU上对4-5B参数模型进行8位量化微调。与 Toolformer、Gorilla、ToolLLM 等将工具描述保留在提示词中的传统方法不同，本文通过微调将固定工具目录的知识内化到模型权重中，在推理时完全不需要工具描述，实现了更严格的工具知识内化，但牺牲了对未见工具的泛化能力。此外，本文与提示压缩（如 LLMLingua）和知识蒸馏方法有概念性联系：可被视为极端的提示压缩形式，将整个工具模式部分压缩进模型权重，且无需教师模型参与推理。

### Q3: 论文如何解决这个问题？

论文通过QLoRA微调将工具知识内化到小语言模型中，解决传统工具使用管道需要完整工具架构知识、造成大量token开销的问题。核心方法是在AssetOpsBench基准上，使用Gemini 2.5 Flash作为教师模型，构建约1,700个包含工具知识、问题到计划映射和执行追踪三类样本的训练数据。架构设计上，选取Gemma 4 E4B（约8B参数）和Qwen3-4B（4.0B参数）作为基座模型，采用8bit QLoRA进行参数高效微调，保持基座模型权重固定，仅训练少量适配器参数。关键技术包括：使用LoRA rank=32、alpha=64、dropout 0.05的参数配置，对所有线性层施加LoRA；在推理阶段采用无描述推理模式，将提示从约2,200 token压缩至128 token（降低82.6%）；评估采用结构指标（AT-F1和ArgKey-F1）与LLM评判（Gemini 2.5 Flash对六维度评分）相结合的双重评估体系。创新点体现在：验证了QLoRA微调可将工具知识从提示上下文转移到模型权重中，在无描述推理条件下，微调模型不提示工具描述即可生成结构化计划；发现LoRA rank控制质量与知识保留的权衡，r=32最大化计划质量，较小rank保留更多通用知识；相比传统方案，Qwen3-4B在内存使用减少62%、速度提升2.5倍的同时，LLM评判得分达3.78。

### Q4: 论文做了哪些实验？

实验基于AssetOpsBench基准，使用约1700个工具使用示例（涵盖工具知识、问题到计划映射和执行轨迹）微调Gemma 4 E4B和Qwen3-4B模型，采用8-bit QLoRA。对比方法包括：1）全工具架构信息的基线（约2400 tokens/查询）；2）无工具描述的基线（约128 tokens）。微调后模型在无描述推理（仅128 tokens输入）下评估，主要结果：最佳Gemma模型AT-F1达0.65，总体judge评分3.88（对比基线0.47和2.88）；Qwen3模型AT-F1为0.605，judge评分3.78，内存减少62%，推理速度提升2.5倍。输入长度减少82.6%。LoRA rank消融实验显示r=32时质量最佳（AT-F1 0.65，judge 3.88），r=64下降。遗忘测试中，Gemma在r=8和r=32分别保留82.1%和79.8%的MCQ准确率（基础84%），而Qwen3仅保留61.3%（基础75%→46%）。训练数据消融表明计划数据（AT-F1 0.65）优于工具定义数据（AT-F1 0.29），量化精度影响微小（8-bit vs 4-bit judge评分3.78 vs 3.74）。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面：第一，实验仅在 AssetOpsBench 单一基准上进行，未验证内化行为对其他工具目录的泛化能力；第二，评估集仅有 30 个保留场景，统计效力有限，且缺乏多随机种子的重复实验；第三，未对比在提示中包含工具描述时的表现，难以区分性能提升是源于内化本身还是释放了上下文窗口容量。

未来研究方向包括：在完整智能体循环中评估模型，测量任务成功率、延迟和鲁棒性；探索持续学习方法，如通过 VibrationAgent 保留实验测试增量学习新工具而避免遗忘旧知识；扩展基准范围至 162+ 场景和 9 类资产；改进推理效率，替换 MatMul8bitLt 为 GPTQ 或 AWQ 内核。此外，针对灾难性遗忘问题，可尝试降低 LoRA 秩、适配器合并或重放式持续学习，并在不同架构间系统分析预训练分布和指令微调历史的影响。

### Q6: 总结一下论文的主要内容

该论文研究是否可以通过参数高效微调将工具使用知识内化到小型语言模型中，使其在推理时无需显式工具描述即可进行结构化规划。问题定义在于当前工具使用流程需要在每个提示中包含完整工具架构，造成大量token开销，限制了小模型的实用性。方法上，使用AssetOpsBench作为基准，采用8位QLoRA微调Gemma 4 E4B和Qwen3-4B模型，在大约1700个工具使用示例上进行训练。主要结论是，微调后的模型在无描述推理场景下，不仅将输入长度减少了82.6%，还比接收完整工具描述但未微调的基线模型取得了更高的结构规划和LLM评判分。最佳Gemma运行的AT-F1达0.65，整体评分3.88，远超基线。Qwen3-4B在内存使用减少62%、推理速度快2.5倍的同时达到3.78高分。LoRA秩控制存在质量-保留权衡，r=32优化规划质量，更小秩保留更多通用知识。该研究证明QLoRA微调能有效将固定工具目录的知识从提示上下文转移到模型权重，大幅降低推理开销。
