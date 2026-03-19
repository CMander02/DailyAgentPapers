---
title: "CodeScout: An Effective Recipe for Reinforcement Learning of Code Search Agents"
authors:
  - "Lintang Sutawika"
  - "Aditya Bharat Soni"
  - "Bharath Sriraam R R"
  - "Apurva Gandhi"
  - "Taha Yassine"
  - "Sanidhya Vijayvargiya"
  - "Yuchen Li"
  - "Xuhui Zhou"
  - "Yilin Zhang"
  - "Leander Melroy Maben"
  - "Graham Neubig"
date: "2026-03-18"
arxiv_id: "2603.17829"
arxiv_url: "https://arxiv.org/abs/2603.17829"
pdf_url: "https://arxiv.org/pdf/2603.17829v1"
categories:
  - "cs.SE"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Code Agent"
  - "Reinforcement Learning"
  - "Tool Use"
  - "Code Search"
  - "SWE-bench"
  - "Agent Training"
  - "Reward Design"
relevance_score: 8.0
---

# CodeScout: An Effective Recipe for Reinforcement Learning of Code Search Agents

## 原始摘要

A prerequisite for coding agents to perform tasks on large repositories is code localization - the identification of relevant files, classes, and functions to work on. While repository-level code localization has been performed using embedding-based retrieval approaches such as vector search, recent work has focused on developing agents to localize relevant code either as a standalone precursor to or interleaved with performing actual work. Most prior methods on agentic code search equip the agent with complex, specialized tools, such as repository graphs derived from static analysis. In this paper, we demonstrate that, with an effective reinforcement learning recipe, a coding agent equipped with nothing more than a standard Unix terminal can be trained to achieve strong results. Our experiments on three benchmarks (SWE-Bench Verified, Pro, and Lite) reveal that our models consistently achieve superior or competitive performance over 2-18x larger base and post-trained LLMs and sometimes approach performance provided by closed models like Claude Sonnet, even when using specialized scaffolds. Our work particularly focuses on techniques for re-purposing existing coding agent environments for code search, reward design, and RL optimization. We release the resulting model family, CodeScout, along with all our code and data for the community to build upon.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型代码仓库中代码定位（code localization）的效率和泛化性问题。研究背景是，在执行如SWE-Bench等仓库级编码任务时，智能体（agent）必须首先从庞大且结构复杂的代码库中精准定位到需要修改的相关文件、类或函数。传统方法主要依赖基于嵌入的向量检索，而近期研究则转向使用智能体进行迭代式代码搜索，但现有方法大多存在明显不足：它们通常需要为智能体配备复杂、专用的工具（如基于静态分析生成的仓库依赖图），这些工具往往针对特定编程语言设计，不仅增加了部署的复杂性和成本，也限制了智能体在不同编程场景下的泛化能力。同时，尽管业界有传闻称强化学习能提升定位效率，但缺乏公开、系统且可复现的训练方案。

因此，本文的核心问题是：能否设计一套有效的强化学习训练方法，使得一个仅配备标准Unix终端（一种通用、语言无关的简单工具）的代码智能体，无需依赖任何专用工具，就能在代码定位任务上达到甚至超越那些使用复杂专用工具的智能体的性能？论文通过提出名为CodeScout的模型家族及一套完整的训练方案（包括环境构建、奖励函数设计和优化算法），成功验证了这一可能性，在多个基准测试中取得了优越或具有竞争力的结果，并为社区提供了可复现的强基线。

### Q2: 有哪些相关研究？

本文的相关研究主要集中在代码定位领域，可分为方法类和应用类。

在方法类研究中，先前工作主要依赖特定语言的静态分析工具来构建专门的智能体框架。例如，LocAgent和OraLoca使用基于AST的解析器构建代码图来捕获层次化的仓库依赖关系，这需要昂贵的预索引。CoSIL和RepoSearcher则动态构建模块调用图或引入专门的检索工具（如提取文件导入或搜索类内函数），但仍依赖于语言特定的静态分析。这些方法通常局限于单一语言（如Python），且工程开销较大。

在应用类研究中，一些工作（如CoSIL、OraLoca）未使用其提出的框架训练LLM，而另一些（如LocAgent、RepoSearcher）则依赖从闭源模型通过监督蒸馏进行微调。

本文的方法CodeScout与这些工作的主要区别在于：1）**工具通用性**：仅使用标准Unix终端作为智能体支架，无需语言特定的静态分析工具，因此天生支持多语言且工程更简单；2）**训练方法**：直接使用强化学习对LLM进行后训练，无需依赖闭源模型进行数据整理；3）**框架简洁性**：动作空间仅包含1个工具（终端），而先前方法使用3-5个专用工具，显著降低了复杂性。

### Q3: 论文如何解决这个问题？

论文通过设计一套有效的强化学习配方来解决代码定位问题，其核心是训练一个仅配备标准Unix终端的智能体，使其能够高效地在大型代码库中搜索相关代码。该方法摒弃了以往依赖复杂专用工具（如静态分析生成的仓库图）的思路，转而采用轻量级、通用的终端工具，并通过精心设计的奖励机制和RL优化策略实现高性能。

整体框架基于一个标准的软件智能体脚手架（OpenHands-Bash），其主要模块包括：1）一个支持标准Unix命令（如`rg`、`find`、`grep`）的终端工具，用于在代码库中进行递归搜索；2）一个结构化输出工具（LocalizationFinish），用于提交预测的文件、模块和函数列表，这避免了早期基于字符串输出格式的解析脆弱性问题，提升了奖励信号的可靠性。环境构建方面，论文通过克隆问题对应的代码仓库预提交状态来创建RL环境，由于定位任务无需执行代码，因此无需安装依赖或进行沙箱隔离，显著降低了环境开销。

关键技术体现在以下几个方面：首先，在奖励设计上，论文基于预测结果与真实修改之间的F1分数来构建奖励函数，具体计算文件、模块和函数三个粒度上的F1值并求和。针对训练中出现的智能体耗尽步数而不提交预测的崩溃问题，论文引入了一个辅助的二元奖励，仅在智能体恰好在步数限制内终止时给予奖励，从而鼓励及时提交。其次，在RL优化方面，论文采用Group Sequence Policy Optimization（GSPO）算法进行训练，并利用SkyRL框架实现异步并行化，以提高GPU利用率。GSPO损失函数基于序列级的重要性采样比，并去除了KL正则项和优势计算中的标准差，同时禁用了熵损失和对于未调用结束工具的轨迹的掩码损失。此外，论文还通过提示工程鼓励智能体使用并行工具调用以提升效率。

创新点主要包括：1）证明了仅使用标准Unix终端作为工具，通过有效的RL训练即可实现强大的代码定位能力，无需复杂的基础设施；2）设计了多粒度F1奖励与及时终止奖励相结合的奖励函数，有效稳定了训练过程；3）通过重用现有的代码修复任务数据来构建RL环境，为代码搜索任务提供了高质量的训练实例。实验结果表明，该方法在不同规模的模型（1.7B、4B、14B）上均在SWE-Bench多个基准测试中达到了开源模型的最先进水平，其性能甚至可与更大规模的基础模型或闭源模型相竞争。

### Q4: 论文做了哪些实验？

论文在三个基准测试（SWE-Bench Verified、Pro 和 Lite）上进行了实验，评估其提出的 CodeScout 模型在代码搜索任务上的性能。

**实验设置**：模型基于 Qwen3 系列（1.7B、4B、14B）进行训练。对于 1.7B 模型，先使用从 CodeScout-14B 采样的成功轨迹进行拒绝采样微调（RFT），再进行强化学习（RL）训练；4B 和 14B 模型则直接使用改进的 GSPO 算法进行 RL 训练。训练时使用了修改后的聊天模板以保留轨迹标记，并掩码非模型生成的令牌损失。关键训练参数包括：最大上下文长度（32K-50K 令牌）、每回合最大步数（4-6 步）、批量大小（8-32）以及恒定学习率（1e-6）。评估时使用温度采样等解码超参数，最大上下文长度为 132K 令牌。

**数据集/基准测试**：使用 SWE-Bench 的三个子集：Verified（500 个实例）、Lite（300 个实例）和 Pro 的 Python 子集（266 个实例）。这些数据集经过处理，提取了文件、模块和函数级别的真实位置作为评估依据。

**对比方法**：与多种基线方法比较，包括使用开源和闭源大语言模型（LLM）的框架：RepoNavigator、RepoSearcher、LocAgent、OrcaLoca、CoSIL 和 Agentless。闭源模型对比了 GPT-5 和 Claude-Sonnet-4.5（均使用 OpenHands-Bash 脚手架，部分添加了提交提醒）。还比较了不同规模的 Qwen 基础模型及其指令微调版本。

**主要结果与关键指标**：主要评估指标是文件、模块和函数三个粒度上的 F1 分数（同时报告精确率和召回率）。实验结果表明：
1.  CodeScout 模型在 OpenHands-Bash（仅 Bash 终端）脚手架下，性能显著优于其对应基础模型。例如，CodeScout-1.7B 在文件级 F1 上比基础模型提升 40-54 个百分点。
2.  CodeScout 展现出卓越的参数效率，小模型常优于大得多的基础模型。例如，CodeScout-4B 在三个基准测试的所有粒度上均优于 8 倍大的 Qwen3-32B（F1 绝对提升：文件 5-8%，模块 11-16%，函数 13-17%）。
3.  与使用复杂专用脚手架（如 RepoNavigator）的更大规模基础或后训练模型相比，CodeScout 表现具有竞争力或更优。例如，在 SWE-Bench Verified 上，CodeScout-4B 和 14B 在函数级 F1 上超过了使用 RepoNavigator 的 Qwen2.5-32B 模型 3-6%。
4.  与闭源模型相比，CodeScout 缩小了性能差距。在 SWE-Bench Verified 上，CodeScout-4B 和 14B 在函数级 F1 上超过了使用 RepoNavigator 的 Claude-3.7-Sonnet（提升 5-8%）。但添加了提醒的 GPT-5 和 Claude-Sonnet-4.5 在使用相同 Bash 脚手架时仍优于 CodeScout。

### Q5: 有什么可以进一步探索的点？

该论文展示了基于强化学习的终端代码搜索代理的有效性，但其方法仍存在一些局限性。首先，完全依赖终端命令进行导航和搜索，在处理高度结构化或依赖复杂静态分析（如类型关系、调用图）的代码库时可能效率不足，未来可探索将轻量级静态分析工具作为辅助感知模块，以提升对代码语义的理解。其次，训练依赖于特定基准（如SWE-Bench），其任务场景可能未覆盖真实开发中更模糊或跨模块的查询需求，需构建更多样化的代码搜索环境以增强泛化能力。此外，奖励函数设计较为直接，未来可引入分层奖励或基于代码变更最终正确性的稀疏奖励，以更好地引导长期决策。最后，模型目前主要针对本地仓库，可扩展至云端或分布式代码库的搜索场景，并探索多智能体协作进行跨仓库代码定位。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为CodeScout的强化学习方法，用于训练代码搜索智能体。核心问题是代码定位，即在大规模代码库中准确找到与任务相关的文件、类或函数。传统方法依赖基于嵌入的检索或复杂的专用工具（如静态分析生成的仓库图），而本文证明，仅配备标准Unix终端的智能体通过有效的强化学习配方即可实现强大性能。

方法上，论文专注于改造现有编码智能体环境以适用于代码搜索，并设计了专门的奖励函数和强化学习优化技术。通过这一配方，智能体能够学习在终端中高效导航和搜索代码库。

实验在SWE-Bench的Verified、Pro和Lite三个基准上进行。结果表明，CodeScout模型性能优于或媲美比其大2-18倍的基础及后训练大语言模型，有时甚至接近Claude Sonnet等闭源模型的表现，即使后者使用了专用框架。论文的核心贡献在于展示了一种简单而有效的强化学习方案，使轻量级智能体仅凭终端就能完成复杂代码搜索任务，为社区提供了可复现的模型家族、代码和数据。
