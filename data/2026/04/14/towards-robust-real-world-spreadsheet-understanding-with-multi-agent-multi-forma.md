---
title: "Towards Robust Real-World Spreadsheet Understanding with Multi-Agent Multi-Format Reasoning"
authors:
  - "Houxing Ren"
  - "Mingjie Zhan"
  - "Zimu Lu"
  - "Ke Wang"
  - "Yunqiao Yang"
  - "Haotian Hou"
  - "Hongsheng Li"
date: "2026-04-14"
arxiv_id: "2604.12282"
arxiv_url: "https://arxiv.org/abs/2604.12282"
pdf_url: "https://arxiv.org/pdf/2604.12282v1"
github_url: "https://github.com/renhouxing/SpreadsheetAgent"
categories:
  - "cs.CL"
tags:
  - "Multi-Agent"
  - "Tool Use"
  - "Reasoning"
  - "Multi-Modal"
  - "Real-World Application"
  - "Benchmark Evaluation"
  - "Code Execution"
  - "Verification"
relevance_score: 7.5
---

# Towards Robust Real-World Spreadsheet Understanding with Multi-Agent Multi-Format Reasoning

## 原始摘要

Spreadsheets are central to real-world applications such as enterprise reporting, auditing, and scientific data management. Despite their ubiquity, existing large language model based approaches typically treat tables as plain text, overlooking critical layout cues and visual semantics. Moreover, real-world spreadsheets are often massive in scale, exceeding the input length that LLMs can efficiently process. To address these challenges, we propose SpreadsheetAgent, a two-stage multi-agent framework for spreadsheet understanding that adopts a step-by-step reading and reasoning paradigm. Instead of loading the entire spreadsheet at once, SpreadsheetAgent incrementally interprets localized regions through multiple modalities, including code execution results, images, and LaTeX tables. The method first constructs a structural sketch and row/column summaries, and then performs task-driven reasoning over this intermediate representation in the Solving Stage. To further enhance reliability, we design a verification module that validates extracted structures via targeted inspections, reducing error propagation and ensuring trustworthy inputs for downstream reasoning. Extensive experiments on two spreadsheet datasets demonstrate the effectiveness of our approach. With GPT-OSS-120B, SpreadsheetAgent achieves 38.16% on Spreadsheet Bench, outperforming the ChatGPT Agent baseline (35.27%) by 2.89 absolute points. These results highlight the potential of SpreadsheetAgent to advance robust and scalable spreadsheet understanding in real-world applications. Code is available at https://github.com/renhouxing/SpreadsheetAgent.git.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现实世界中大规模、结构复杂的电子表格（Spreadsheet）自动理解与推理问题。研究背景在于，电子表格在企业报表、财务审计和科学数据管理等场景中应用广泛，但现有基于大语言模型（LLM）的方法通常将表格视为纯文本（如Markdown、HTML或LaTeX格式），忽略了关键的布局线索和视觉语义信息，例如分层表头、合并单元格、字体颜色和边框等样式元素。此外，实际电子表格往往规模庞大，行数和列数远超当前LLM能高效处理的输入长度限制，导致现有方法难以同时应对结构复杂性和数据规模的双重挑战。

现有方法的不足主要体现在两方面：一是文本化表示丢失了视觉布局所蕴含的语义信息，限制了模型对表格结构的深层理解；二是无法有效处理超长表格，直接输入整个表格会超出LLM的上下文窗口，而简单截断又会损失重要内容。

本文要解决的核心问题是：如何设计一个既能捕捉电子表格丰富视觉与结构语义，又能适应其大规模特性的鲁棒性理解框架。为此，论文提出了SpreadsheetAgent，一个两阶段多智能体框架，采用渐进式读取与推理范式。该方法不一次性加载整个表格，而是通过多个智能体协作，以代码执行结果、图像和LaTeX表格等多种模态增量解读局部区域，先构建结构草图和行列摘要作为中间表示，再基于该表示进行任务驱动的推理。此外，框架还设计了验证模块，通过针对性检查来验证提取的结构，减少错误传播，从而提升现实场景下电子表格理解的可靠性和可扩展性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、应用类和评测类三大方向。

在方法类研究中，相关工作主要聚焦于提升语言模型对表格的理解与推理能力。例如，Chain-of-Table通过逐步生成操作来构建中间表示链，实现查询的系统性分解；TaPERA则将组合查询分解为子问题，通过执行Python程序来检索事实。本文提出的SpreadsheetAgent与这些方法的核心区别在于其采用了多智能体、多模态的增量式解读范式，并引入了结构草图与行列摘要等中间表示，而非一次性处理整个表格或仅依赖符号推理。

在应用类研究中，已有工作如SheetMind和SheetAgent设计了基于LLM的多智能体框架，用于电子表格的自动化操作。ReAcTable则通过外部工具增强和投票机制提升鲁棒性。本文的SpreadsheetAgent与这些框架类似，都采用了多智能体架构，但本文的创新点在于明确设计了包含结构构建与任务驱动求解的两阶段推理流程，并专门集成了代码执行、图像和LaTeX表格等多模态信息，以更好地捕捉真实电子表格中的布局线索和视觉语义。

在评测与模型适应方向，TableGPT等研究通过指令微调提升模型在表格任务上的泛化能力，后续工作如TableGPT2和Table-LLaVA进一步扩展到多模态理解。近期，受DeepSeek-R1启发，强化学习（RL）也被应用于表格推理，以提升小模型或特定场景下的性能。本文虽未直接采用RL，但其设计的验证模块通过针对性检查来验证提取的结构，旨在减少错误传播，这与RL方法追求鲁棒性和一致性的目标有相通之处。总体而言，本文在现有表格理解研究的基础上，针对真实世界电子表格规模庞大、富含视觉布局信息的特点，提出了一个更为综合和稳健的解决方案。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为SpreadsheetAgent的两阶段多智能体框架来解决现实世界中电子表格理解所面临的挑战，其核心是采用逐步阅读与推理的范式。该框架的整体架构分为两个主要阶段：提取阶段和解决阶段，并创新性地集成了一个验证模块以增强可靠性。

在整体框架上，系统首先通过一个**提取智能体**增量式地解析电子表格，而非一次性加载整个可能规模巨大的表格。该智能体利用多种模态工具来理解局部区域：**代码执行工具**用于精确计算和验证原始值；**视觉范围描述工具**将选定区域转为图像，借助视觉语言模型提取颜色、边框等视觉语义；**LaTeX范围描述工具**则将区域转为LaTeX表格，供语言模型恢复层次化表头、合并单元格等结构信息。提取过程采用提示驱动，引导大语言模型识别并输出一个规范化的、保留布局与语义的**YAML格式中间表示**（结构草图与行列摘要），这种结构化输出减少了歧义，便于下游解析。

为确保提取结果的可靠性，论文设计了**验证模块**，包含视觉验证智能体和LaTeX验证智能体。该模块不会重新处理整个表格，而是针对提取的YAML表示，选择性地对不确定或结构复杂的区域进行针对性检查。验证智能体可以调用相应的工具（生成图像或LaTeX），交叉比对原始表格与提取结果，检测不一致之处（如缺失的合并单元格、误解的颜色等）并生成修正建议。

提取与验证模块并非独立运行，而是通过一个**迭代的提取-验证循环**紧密耦合。算法会循环进行：提取生成YAML表示，验证模块对其进行检查，若未通过则将修正反馈给提取过程进行更新，直至表示达到足够的保真度。这种渐进式的“读取-检查”范式，结合了自适应区域选择，使得系统能够在有限的上下文预算下处理大规模表格，同时通过验证减少错误传播。

最终，经过验证的、富含语义的结构化表示被注入到**解决阶段**，用于支持下游任务驱动的推理。该方法的核心创新点在于：1) **多智能体、多格式、多工具的增量式理解框架**，有效突破了LLM的输入长度限制并利用了视觉与结构线索；2) **提取与验证的迭代闭环设计**，显著提升了表示的准确性与可靠性；3) **结构化YAML中间表示与针对性工具辅助检查的结合**，在保持语义保真度的同时实现了高效处理。

### Q4: 论文做了哪些实验？

论文在SpreadsheetBench和RealHiTBench两个真实世界电子表格数据集上进行了实验。SpreadsheetBench包含来自Excel用户论坛的912个问题及原始表格文件，涵盖多表、非标准关系结构、合并单元格等复杂场景；RealHiTBench则专注于评估分层表头处理能力。实验设置采用GLM-4.5V作为视觉语言模型，Qwen3-Coder-480B作为主要语言模型，使用vLLM进行推理加速，最大上下文长度为4K token，最多允许20轮工具调用。

对比方法包括通用大模型（GPT-3.5、GPT-4o、Llama-3等）、专用表格系统（SheetCopilot、Copilot in Excel、ChatGPT Agent）以及近期强基线TreeThinker。主要结果如下：在SpreadsheetBench的Soft Restriction设置下，本文方法（SpreadsheetAgent）使用GPT-OSS-120B达到38.16%的整体准确率，超越ChatGPT Agent基线（35.27%）2.89个百分点；使用Qwen3-Coder-480B时达到41.67%，创下新state-of-the-art。在Hard Restriction设置下，GPT-OSS-120B版本达到31.47%，Qwen3-Coder-480B版本达到34.65%。关键指标显示，本文方法在不同模型规模上均一致优于TreeThinker，例如在Qwen3-30B上提升近6个百分点，在Qwen3-Coder-480B上提升超11个百分点。

消融实验验证了各组件贡献：移除验证模块（w/o Verify）导致准确率下降；移除结构化草图（w/o Structure）严重损害性能；移除多格式工具（如视觉或LaTeX工具）均降低准确性；移除所有组件（w/o All）时性能暴跌至16.41%/12.83%，比完整模型低近10个百分点。此外，提取器强度实验表明，强推理模型搭配强提取器效果最佳（如GPT-OSS-20B搭配Qwen3-480B提取器达到32.16%/29.25%），而弱推理模型可通过强提取器获得显著提升（如Qwen3-30B搭配480B提取器提升约6个百分点）。效率方面，平均每表格处理耗时97.49秒，进行19.54次智能体调用，最大内存占用21GB。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在两方面：一是框架高度依赖同时支持多模态输入和函数调用的强大基础模型（如GLM-4.5V），这类模型在开源社区中仍较稀缺，限制了方法的可复现性和广泛适用性；二是未探索模型蒸馏，缺乏大规模、真实的电子表格数据集来支持将大模型的推理能力迁移至小模型。

未来研究方向包括：1）框架适配性优化，研究如何将多智能体设计适配到更易获取或更专精的开源模型上，例如通过模块化设计分离视觉解析与逻辑推理，或利用轻量级模型协同完成特定子任务；2）构建高质量蒸馏数据集，可考虑利用合成数据生成技术或众包标注，创建包含复杂布局与公式的大规模电子表格语料库，以系统评估小模型的推理继承效果；3）扩展任务范畴，当前工作聚焦于理解与问答，未来可探索电子表格的自动修改、错误检测乃至基于表格的预测与决策生成等更动态的任务，进一步提升智能体在实际工作流中的实用性。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为SpreadsheetAgent的两阶段多代理框架，旨在解决现实世界中大规模电子表格理解的关键挑战。现有基于大语言模型的方法通常将表格视为纯文本，忽略了布局线索和视觉语义，且难以处理超出模型输入长度限制的大型表格。

该框架的核心方法分为两个阶段：首先通过逐步读取局部区域（包括代码执行结果、图像和LaTeX表格等多模态信息）构建结构草图及行列摘要，形成中间表示；随后在解决阶段基于此表示进行任务驱动的推理。为提升可靠性，框架还设计了验证模块，通过针对性检查验证提取的结构，减少错误传播。

实验表明，在SpreadsheetBench数据集上，使用GPT-OSS-120B的SpreadsheetAgent达到了38.16%的准确率，较ChatGPT Agent基线提升2.89个百分点，验证了其在保持布局语义、克服上下文长度限制以及整合多格式工具方面的有效性。该研究为推进现实应用中鲁棒且可扩展的电子表格理解提供了潜在方向。
