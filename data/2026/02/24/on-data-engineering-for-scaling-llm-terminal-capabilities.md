---
title: "On Data Engineering for Scaling LLM Terminal Capabilities"
authors:
  - "Renjie Pi"
  - "Grace Lam"
  - "Mohammad Shoeybi"
  - "Pooya Jannaty"
  - "Bryan Catanzaro"
  - "Wei Ping"
date: "2026-02-24"
arxiv_id: "2602.21193"
arxiv_url: "https://arxiv.org/abs/2602.21193"
pdf_url: "https://arxiv.org/pdf/2602.21193v1"
categories:
  - "cs.CL"
tags:
  - "Agent 数据合成"
  - "Agent 评测/基准"
  - "工具使用"
  - "LLM 应用于 Agent 场景"
  - "终端智能体"
relevance_score: 8.0
---

# On Data Engineering for Scaling LLM Terminal Capabilities

## 原始摘要

Despite rapid recent progress in the terminal capabilities of large language models, the training data strategies behind state-of-the-art terminal agents remain largely undisclosed. We address this gap through a systematic study of data engineering practices for terminal agents, making two key contributions: (1) Terminal-Task-Gen, a lightweight synthetic task generation pipeline that supports seed-based and skill-based task construction, and (2) a comprehensive analysis of data and training strategies, including filtering, curriculum learning, long context training, and scaling behavior. Our pipeline yields Terminal-Corpus, a large-scale open-source dataset for terminal tasks. Using this dataset, we train Nemotron-Terminal, a family of models initialized from Qwen3(8B, 14B, 32B) that achieve substantial gains on Terminal-Bench 2.0: Nemotron-Terminal-8B improves from 2.5% to 13.0% Nemotron-Terminal-14B improves from 4.0% to 20.2%, and Nemotron-Terminal-32B improves from 3.4% to 27.4%, matching the performance of significantly larger models. To accelerate research in this domain, we open-source our model checkpoints and most of our synthetic datasets at https://huggingface.co/collections/nvidia/nemotron-terminal.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在终端交互能力训练中面临的数据工程挑战。研究背景是，随着LLMs向实际软件工程应用迈进，终端交互已成为一项关键能力，前沿模型在相关基准测试中展现出潜力，但其背后训练数据的构建策略却鲜有公开。现有方法的不足主要体现在两个方面：一是缺乏透明、高效的数据生成框架。当前提升终端能力的方法主要依赖改进代理框架或直接优化底层模型，例如通过适配器将现有数据集包装成命令行接口形式，但这类方法受限于源数据集的结构假设，并非为顺序环境交互设计，效果可能受限；而基于多智能体框架的生成方法则计算复杂，难以扩展到大规模训练。二是数据生成本身存在瓶颈，包括基础资源（如多样化的任务提示、依赖文件、预配置环境）稀缺，以及轨迹收集在现实世界或通过LLM代理合成时都面临高昂的代价和复杂性。

因此，本文要解决的核心问题是：如何设计一个实用、高效且可扩展的数据工程框架，以系统性地生成高质量、大规模的终端任务训练数据，从而透明、经济地提升LLMs的终端能力，并填补该领域在有效数据设计方面的知识空白。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕智能体设计、数据集适配和合成任务生成三个类别展开。

在**智能体设计**方面，相关工作如Claude Code和Codex CLI通过复杂的智能体框架（scaffolding）显著提升了性能。然而，这些框架通常针对特定模型，且工程实现复杂。本文的研究重点与之不同，不探索智能体设计的变体，而是专注于通过有监督的微调来扩展基础模型的内在终端能力。

在**数据集适配**方面，Hugging Face等平台上的许多数据集通过将现有提示（如来自编程或数学领域）在终端环境中执行来收集智能体轨迹。这种方法能高效扩增数据，但缺乏对数据集适配器特性如何影响训练效果的正式分析。本文通过使用自定义数据集和适配器进行系统研究，深入探讨了这种方法的优缺点。

在**合成任务生成**方面，相关研究致力于为微调LLM有效生成合成数据。例如，Evol-Instruct通过迭代的深度和广度演化来自动扩展指令数据；Code Evol-Instruct将其成功应用于代码指令；AgentInstruct和LAB通过建议者-编辑者智能体对或分类驱动的生成从种子数据创建大规模数据集；MAGPIE则探索了无需种子数据、通过独特提示策略从对齐LLM中提取指令数据。近期也有工作尝试将多智能体系统用于扩展LLM的终端能力，但其过程耗时且成本高。本文提出的Terminal-Task-Gen管道对此进行了简化，消除了不必要的协调阶段并优化了环境验证，从而实现了更高效的扩展，并通过系统分析和消融实验提供了可操作的见解。

### Q3: 论文如何解决这个问题？

论文通过一个系统化的数据工程框架来解决终端智能体训练数据策略不透明的问题，其核心是“两阶段数据生成框架”和配套的训练策略。

**整体框架与主要模块**：
框架分为两个主要阶段：1）**数据集适配**：从现有高质量问题库（数学、代码、软件工程）中筛选和转换提示，将其统一包装成终端任务格式，以快速建立广泛的基础能力覆盖。2）**合成任务生成**：这是论文的核心创新模块，旨在生成可执行的、针对终端操作特性的任务。它包含两种互补的方法：
*   **基于种子的生成**：利用来自相邻领域（如科学计算）的结构化种子问题（包含问题描述、领域标签和参考解决方案），通过LLM将其适配为自包含的终端任务。适配过程会添加具体的软件工程要求（如安装包、文件I/O）、生成测试用例和输入数据文件。
*   **基于技能的生成**：从一个精心策划的**原始技能分类法**出发，涵盖算法、系统、数据处理、数学、测试、网络/安全等多个维度。LLM根据9个特定领域（如数据处理、数据科学、安全等）的提示，将多个原始技能（通常3-5个）以非平凡的方式组合，创造出新颖、多样化的任务场景。

**关键技术细节与创新点**：
1.  **标准化任务格式与解决方案隔离**：所有生成的任务都遵循统一格式（自然语言提示、pytest测试用例、输入文件、Docker环境）。一个关键设计原则是**严格隔离问题描述与解决方案信息**，确保LLM在生成任务时不会泄露算法或代码，迫使智能体进行真正的解决问题。
2.  **预构建的Docker镜像**：摒弃了为每个任务生成唯一Dockerfile的传统做法，转而使用**9个领域特定的预构建Docker镜像**。每个镜像预装了该领域的常用包。这极大地提升了生成管道的可扩展性，消除了Dockerfile验证开销，减少了资源占用，并将环境生成与任务生成解耦。
3.  **高质量数据筛选与轨迹处理**：在训练前，对监督微调数据集进行去污（移除与基准测试集重叠的提示）和质量过滤（如移除身份泄露、包含中文字符的响应）。此外，实验性地移除教师模型生成的不完整轨迹，或仅保留通过测试的轨迹，以防止模型变得冗长并鼓励正确的行为。
4.  **教师模型选择**：选用在终端基准上表现优异的DeepSeek-V3.2作为教师模型，用于生成合成任务和解决方案轨迹，确保了生成数据的质量起点。

通过这套方法，论文构建了大规模开源数据集Terminal-Corpus，并训练出Nemotron-Terminal模型系列，在终端基准上取得了显著性能提升，验证了其数据工程策略的有效性。

### Q4: 论文做了哪些实验？

本论文的实验主要围绕验证其提出的数据工程方法对提升大语言模型终端能力的有效性展开。

**实验设置与数据集**：研究基于Qwen3系列预训练模型（8B、14B、32B）进行微调实验。核心训练数据来源于作者提出的合成任务生成管道Terminal-Task-Gen所构建的大规模开源数据集Terminal-Corpus。训练采用标准监督微调，关键超参数包括学习率2e-5、权重衰减1e-4、2个训练周期、最大序列长度32,768 tokens，使用AdamW优化器和余弦学习率调度器。实验在分布式GPU集群上进行，并利用了Harbor、Daytona和veRL等基础设施框架进行数据生成、评估和训练。

**基准测试与对比方法**：核心评估基准是Terminal-Bench 2.0 (TB2.0)。对比方法分为三类：1) 闭源商业模型（如GPT-5系列、Claude系列、Gemini系列）；2) 开源基线模型（包括不同规模的原始Qwen3模型及其他大型开源模型如DeepSeek-V3.2）；3) 作者训练的Nemotron-Terminal模型家族（即\ourmodel）。

**主要结果与关键指标**：在TB2.0总体得分上，作者的方法带来了显著提升。关键数据指标如下：Nemotron-Terminal-8B得分从Qwen3-8B的2.47%提升至13.0%；14B模型从4.04%提升至20.2%；32B模型从3.37%提升至27.4%。这些经过数据工程优化的中等规模模型，其性能超越了参数量大得多的模型，例如Nemotron-Terminal-14B（20.2）超越了120B的GPT-OSS（18.7）和Gemini 2.5 Flash（16.9）；Nemotron-Terminal-32B（27.4）超越了480B的Qwen3-Coder（23.9）。

**分任务类别分析**：论文进一步提供了分任务类别的详细结果，显示模型在原始基模型得分为0的多个关键领域实现了从无到有的能力突破。例如，对于32B模型，在数据查询（Data Querying）任务上从0.0提升至60.0，在模型训练（Model Training）任务上从0.0提升至50.0。在安全（Security）、数据处理（Data Processing）、软件工程（Software Engineering）、系统管理（System Administration）和调试（Debugging）等类别上也观察到了类似的巨大性能飞跃，证明了所提数据工程策略在注入领域特定技能方面的有效性。

### Q5: 有什么可以进一步探索的点？

该论文在终端能力数据工程方面取得了显著进展，但仍存在一些局限性和值得探索的方向。首先，其任务生成管道（Terminal-Task-Gen）主要基于合成数据，虽然支持种子和技能构建，但可能无法完全覆盖真实世界终端使用中复杂、动态和多变的交互场景，存在分布偏差风险。未来可探索如何高效融入高质量的人类真实交互数据，或设计更强大的对抗性/演化式数据生成方法，以提升模型的泛化性和鲁棒性。

其次，论文侧重于单轮或有限轮次的终端任务，而对需要长期规划、多步骤执行、并能从错误中持续学习和自我修正的持久性终端代理（persistent agent）研究不足。这是一个关键方向，可结合强化学习、反思机制和环境反馈来构建更自主的代理。

此外，模型的安全性与可控性未深入讨论。终端代理拥有执行系统命令的强大能力，如何防止恶意指令、确保操作安全、并实现细粒度的权限控制，是走向实际应用必须解决的难题。未来需研究有效的对齐技术、沙箱机制和可解释性方法。

最后，论文的评估主要基于静态基准（Terminal-Bench 2.0），未来需要建立更动态、交互式的评估框架，以测试模型在开放环境中的实际效用、效率及与人协作的能力。模型架构与训练算法的协同优化（如针对终端序列的稀疏注意力）也是一个有潜力的改进点。

### Q6: 总结一下论文的主要内容

该论文聚焦于提升大语言模型在终端任务（如命令行操作）能力的数据工程策略。针对当前顶尖终端智能体训练数据细节不公开的现状，研究做出了两大核心贡献：一是提出了Terminal-Task-Gen，一个轻量级的合成任务生成流水线，支持基于种子和基于技能的任务构建，并由此创建了开源的大规模数据集Terminal-Corpus；二是对数据过滤、课程学习、长上下文训练及扩展规律等训练策略进行了全面分析。基于此数据集，研究团队从Qwen3系列模型初始化并训练了Nemotron-Terminal模型家族（8B、14B、32B）。实验结果表明，这些模型在Terminal-Bench 2.0基准测试上取得了显著提升，其中32B版本性能从3.4%提升至27.4%，达到了与更大规模模型相媲美的水平。该工作通过开源数据集、模型及大部分合成数据，旨在推动终端智能体领域的开放研究。
