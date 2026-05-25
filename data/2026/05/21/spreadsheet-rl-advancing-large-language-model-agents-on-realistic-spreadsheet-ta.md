---
title: "Spreadsheet-RL: Advancing Large Language Model Agents on Realistic Spreadsheet Tasks via Reinforcement Learning"
authors:
  - "Banghao Chi"
  - "Yining Xie"
  - "Mingyuan Wu"
  - "Jingcheng Yang"
  - "Jize Jiang"
  - "Zhaoheng Li"
  - "Shengyi Qian"
  - "Minjia Zhang"
  - "Klara Nahrstedt"
  - "Rui Hou"
  - "Xiangjun Fan"
  - "Hanchao Yu"
date: "2026-05-21"
arxiv_id: "2605.22642"
arxiv_url: "https://arxiv.org/abs/2605.22642"
pdf_url: "https://arxiv.org/pdf/2605.22642v1"
categories:
  - "cs.AI"
tags:
  - "Spreadsheet Agent"
  - "Reinforcement Learning"
  - "LLM Fine-tuning"
  - "Tool Use"
  - "Multi-turn Interaction"
relevance_score: 7.5
---

# Spreadsheet-RL: Advancing Large Language Model Agents on Realistic Spreadsheet Tasks via Reinforcement Learning

## 原始摘要

Spreadsheet systems (e.g., Microsoft Excel, Google Sheets) play a central role in modern data-centric workflows. As AI agents grow increasingly capable of automating complex tasks, such as controlling computers and generating presentations, building an AI-driven spreadsheet agent has emerged as a promising research direction. Most existing spreadsheet agents rely on specialized prompting over general-purpose LLMs; while this design has potentials on simple spreadsheet operations, it struggles to manage the complex, multi-step workflows typical of real-world applications.
  We introduce Spreadsheet-RL, a reinforcement learning (RL) fine-tuning framework designed to train specialized spreadsheet agents within a realistic Microsoft Excel environment. Spreadsheet-RL features an automated pipeline for scalable collection of paired start-goal spreadsheets from online forums, as well as domain-specific evaluation tasks in areas such as finance and supply chain management, which we compile into the new Domain-Spreadsheet benchmark dataset. It also includes a Spreadsheet Gym environment designed for multi-turn RL: Spreadsheet Gym exposes extensive Excel functionality through a Python sandbox, along with a refined harness that incorporates a comprehensive tool set and carefully designed tool-routing rules for spreadsheet tasks. Through comprehensive experiments, we show that Spreadsheet-RL substantially enhances AI agent's performance on both general and domain-specific spreadsheet tasks: it improves Qwen3-4B-Thinking-2507's Pass@1 on SpreadsheetBench from 12.0% to 23.4%, and raises Pass@1 from 8.4% to 17.2% on our curated Domain-Spreadsheet dataset. These results highlight Spreadsheet-RL's strong potential for generalization and real-world adoption in spreadsheet automation, and broadly, its promise for advancing LLM-based interactions with data interfaces in everyday work.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有大语言模型（LLM）在电子表格任务中表现不佳的问题。研究背景是，电子表格系统（如Microsoft Excel）在现代数据工作流中至关重要，AI驱动的电子表格智能体具有广阔前景。然而，现有方法（如SheetCopilot、SheetAgent）主要依赖对通用大模型的特殊提示（prompting）策略，这种方式虽然能处理简单操作，但在面对真实世界中复杂的多步骤工作流时表现不佳。例如，ChatGPT Agent和Copilot在SpreadsheetBench上的准确率分别仅为45.5%和20.0%。该方法的根本局限在于其依赖通用LLM的能力提升而非针对电子表格任务的专门优化。论文要解决的核心问题是如何构建一个专门化的、开源的电子表格智能体，使其能够可靠地执行真实世界中复杂的多步骤电子表格操作。为此，论文提出Spreadsheet-RL框架，首次将强化学习（RL）微调方法应用于电子表格领域，通过自动化收集大规模起始-目标电子表格对、设计专门的Spreadsheet Gym交互环境以及基于GRPO的RL训练管线，显著提升了智能体在通用和领域特定电子表格任务上的表现。

### Q2: 有哪些相关研究？

相关研究主要分为方法类和评测类。在方法类中，早期工作如SheetCopilot和SheetAgent通过提示工程和推理时设计实现电子表格自动化，它们依赖通用LLM的专用提示，擅长简单操作，但面对复杂多步工作流时能力有限。本文Spreadsheet-RL与这些方法的关键区别在于，它首次采用强化学习微调进行模型端的智能体训练，而非仅关注推理策略，从而在复杂任务上实现显著性能提升。在评测类方面，SpreadsheetBench收集了912对经专家验证的初始-最终电子表格，SheetCopilot从28个工作簿合成任务，SheetAgent使用表格问答基准如WikiTableQuestions和TabFact进行评估，而OpenAI Agent则使用专有的投资银行电子表格数据集。相比之下，Spreadsheet-RL填补了缺乏专用开源框架的空白，创新性地引入全开源、自动化的大规模数据采集管道，能从网络论坛获取多样化领域的工作流数据，并建立了Domain-Spreadsheet基准，专门覆盖金融、供应链等实际领域，有效支持了基于RL的训练与评估。

### Q3: 论文如何解决这个问题？

Spreadsheet-RL 通过一个强化学习微调框架来解决大规模现实电子表格任务。核心方法包括三个部分：自动化数据生成、交互环境设计和异步RL训练。

首先，论文提出一个自动化流水线，从ExcelForum等在线论坛收集包含初始电子表格、用户任务描述及解决方案讨论的元数据种子。然后使用Claude Code等强编码智能体生成可执行的电子表格编辑脚本，在真实Excel环境中执行并得到Oracle最终电子表格，再通过规则过滤和验证确保质量。这一方法无需人工专家即可大规模构建任务数据。

其次，设计了一个名为Spreadsheet Gym的强化学习环境。该环境基于真实Microsoft Excel，支持FILTER、UNIQUE等现代高级函数，确保执行语义与真实工作流一致。环境通过文件系统隔离的工作空间支持安全的并行执行，与VeRL等异步训练框架兼容。在智能体工具接口上，Spreadsheet Gym定义了一套电子表格原生工具集（如find_cells、inspect_range、fill_formula、clear_range、delete_rows等），路由不同操作到专用工具，并实施并发只读、串行写入的安全调用规则。工具套件封装了电子表格的语义，减少了小中型LLM在索引偏移、公式翻译等低层次执行错误。

最后，采用GRPO策略优化策略模型，使用可验证的基于结果的奖励函数。智能体通过“检查-修改-验证”工作流与Spreadsheet Gym交互，在每一步交替输出推理和工具调用。轨迹结束时，通过与Oracle电子表格的单元格级匹配来计算奖励。整体框架不依赖SFT预热，直接从基础模型开始RL训练。在SpreadsheetBench和Domain-Spreadsheet基准上，Spreadsheet-RL将Pass@1分别从12.0%提升至23.4%和从8.4%提升至17.2%。

### Q4: 论文做了哪些实验？

论文在SpreadsheetBench和Domain-Spreadsheet两个数据集上进行实验。SpreadsheetBench包含912个独特任务，每个任务有3个不同但高度相似的测试用例；Domain-Spreadsheet包含1660个任务，涵盖金融、供应链、人力资源、销售和房地产五个领域。主要评价指标是精确匹配所有单元格的Pass@1。

对比方法包括GPT-4o、OpenAI o3、ChatGPT agent、Claude Files Opus 4.1、Copilot Agent Mode等闭源模型，以及Qwen3系列（4B、8B、14B、32B）开源模型。主要结果：在SpreadsheetBench上，Qwen3-4B-Thinking-2507基础模型Pass@1为12.0%；加入表格原生交互工具后提升至15.6%；增加全面工具访问后提升至19.3%；经过Spreadsheet-RL强化学习微调后达到23.4%，超越了OpenAI o3的23.3%基线。在Domain-Spreadsheet上，Spreadsheet-RL将整体Pass@1从8.4%提升至17.2%，其中金融领域提升最显著（从15.6%到29.3%），供应链、HR和销售领域也有提升，房地产领域保持1.1%不变。训练动态显示，经过60步RL训练，平均奖励从0.21升至0.33，平均响应长度从约16k降至约11k，平均交互轮次从约20降至约11。

### Q5: 有什么可以进一步探索的点？

论文在电子表格任务上取得了显著进展，但仍有几个值得深挖的局限性。首先，Spreadsheet-RL的奖励信号完全依赖最终结果的通过/失败，缺乏对中间步骤质量的细粒度评估，这可能导致模型学习到“运气好”的路径而非稳健的推理策略。未来可引入过程奖励模型，对每一步操作的正确性和效率给予部分信用。其次，当前环境仅模拟了Excel的部分功能（如公式、单元格操作），而真实场景中常涉及更复杂的宏录制、图表交互或跨应用数据联动（如从SQL数据库拉取数据）。扩展Gym环境以支持混合界面（如VBA脚本、外部API调用）将提升实用性。此外，强化学习训练依赖大量自动生成的初始-目标电子表格对，这些数据可能覆盖不到长尾但关键的业务场景（如税务计算中的异常值处理）。结合少量人类专家标注的“硬样本”进行在线微调，或引入课程学习渐进式增加任务难度，可能更符合真实落地的需求。最后，当前4B模型性能有限，探索更大规模模型（如14B）与RL训练的结合，并建模工具调用的时序依赖关系（如同步多区域操作），是提升电子表格智能体复杂任务成功率的可行方向。

### Q6: 总结一下论文的主要内容

该论文提出Spreadsheet-RL，一个通过强化学习微调专用于电子表格任务的AI智能体的框架。核心问题在于现有方法依赖通用大语言模型和专门提示，难以处理真实世界中复杂的多步骤电子表格工作流。方法上，Spreadsheet-RL包含三个关键组件：一个自动化的数据处理智能体，能从在线论坛大规模收集并构建初始-最终电子表格配对；一个专为多轮强化学习设计的真实Microsoft Excel交互环境；以及一个通过异步GRPO进行训练的精巧智能体工具集和路由规则。主要结论是，采用该微调方法的Qwen3-4B模型在通用基准SpreadsheetBench上的准确率从12.0%提升至23.4%，在涵盖金融、供应链等领域的领域专用数据集Domain-Spreadsheet上总体准确率从8.4%提升至17.2%。这项工作的意义在于，它首次将基于结果的强化学习确立为电子表格自动化的一种实用且有效的后训练范式，并提供了一个完整的开源基础平台。
