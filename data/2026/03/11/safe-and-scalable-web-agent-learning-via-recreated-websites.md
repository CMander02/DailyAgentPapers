---
title: "Safe and Scalable Web Agent Learning via Recreated Websites"
authors:
  - "Hyungjoo Chae"
  - "Jungsoo Park"
  - "Alan Ritter"
date: "2026-03-11"
arxiv_id: "2603.10505"
arxiv_url: "https://arxiv.org/abs/2603.10505"
pdf_url: "https://arxiv.org/pdf/2603.10505v1"
github_url: "https://github.com/kyle8581/VeriEnv"
categories:
  - "cs.CL"
tags:
  - "Web Agent"
  - "Environment Synthesis"
  - "Self-Generated Tasks"
  - "Scalable Training"
  - "Autonomous Learning"
  - "Verifiable Reward"
  - "Generalization"
relevance_score: 8.0
---

# Safe and Scalable Web Agent Learning via Recreated Websites

## 原始摘要

Training autonomous web agents is fundamentally limited by the environments they learn from: real-world websites are unsafe to explore, hard to reset, and rarely provide verifiable feedback. We propose VeriEnv, a framework that treats language models as environment creators, automatically cloning real-world websites into fully executable, verifiable synthetic environments. By exposing controlled internal access via a Python SDK, VeriEnv enables agents to self-generate tasks with deterministic, programmatically verifiable rewards, eliminating reliance on heuristic or LLM-based judges. This design decouples agent learning from unsafe real-world interaction while enabling scalable self-evolution through environment expansion. Through experiments on web agent benchmarks, we show that agents trained with VeriEnv generalize to unseen websites, achieve site-specific mastery through self-evolving training, and benefit from scaling the number of training environments. Code and resources will be released at https://github.com/kyle8581/VeriEnv upon acceptance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自主网络智能体（Web Agent）在真实网站上进行强化学习训练时面临的安全性、可重置性和反馈可验证性等根本性限制问题。研究背景是，为了实现能够自主进化、协助人类完成复杂任务的通用智能体，网络环境因其真实性、多样性和长程交互特性而成为理想的训练场。然而，现有方法通常让智能体直接在真实网站上探索和学习，这存在显著不足：首先，这种探索不安全，可能干扰其他用户、违反平台政策或触发安全机制（如验证码）；其次，真实网站难以重置到特定状态以供重复训练；再者，现有方法（如基于LLM的评判器）为智能体自我生成的任务提供的奖励信号往往不可靠、易出错，缺乏确定性的验证机制，导致学习过程不稳定且低效。

因此，本文要解决的核心问题是：如何为自我进化的网络智能体创造一个既安全（可无风险探索）、又可扩展（能生成大量训练环境）、且能提供程序化可验证奖励信号的训练框架。论文提出的解决方案是VeriEnv框架，其核心思想是将大语言模型视为环境创建者，自动将真实网站克隆成完全可执行的合成环境。该框架通过Python SDK提供对克隆环境内部状态（前端、后端逻辑和数据库）的受控访问，使得智能体能够自我生成任务，并伴随可执行的验证程序，从而获得确定性的、可编程验证的奖励。这从根本上将智能体的学习过程与不安全的真实世界交互解耦，同时通过环境扩展支持智能体的规模化自我进化。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕三个方向展开。

在**具有可验证奖励的智能体学习**方面，现有研究强调在数学、编程等领域利用可验证的奖励进行强化学习，或将网络智能体的行动流程分解为提议、执行、评估以获取更清晰的奖励信号。本文的VeriEnv框架与这些工作的目标一致，即追求可靠的训练信号，但其核心创新在于解决了在无法直接探索或外部验证的现实网站上进行学习的难题。它通过克隆完整网站（含数据库）并启用受控的内部验证，为轨迹评估提供了确定性的奖励，从而区别于依赖启发式或基于LLM评判器的现有方法。

在**自我进化智能体**方面，相关研究致力于通过探索、课程学习和自动任务构建来减少对静态人工监督的依赖。例如，在Mind2Web等基准测试中，已有工作利用在线课程或探索驱动的任务生成来扩展覆盖范围。本文同样构建了一个自我进化的训练循环，但关键区别在于其任务生成和奖励验证的机制：它并非在真实网站上交互或生成不可验证的任务，而是基于克隆的、可执行的环境和数据库支持进行验证，从而确保了自我生成任务的有效性和奖励的完全可验证性，且不影响真实用户。

在**用于网络开发的编程智能体**方面，近期工作展示了智能体自主开发全栈网络应用的能力，并通过编译器输出、运行时日志等反馈进行迭代调试。然而，许多功能性和交互性错误仅在执行时才会暴露。本文借鉴了利用网络智能体和浏览器测试框架检测此类错误的思路，并进一步将编程智能体与自动化网络交互相结合，以迭代式地精炼克隆的网站，从而生成功能可靠、可用于智能体训练的合成环境。

### Q3: 论文如何解决这个问题？

论文通过提出VeriEnv框架来解决Web智能体训练环境不安全、难重置、反馈难验证的问题。其核心方法是利用大语言模型作为环境创建者，将真实网站克隆为可完全执行、可验证的合成环境，从而为智能体提供安全、可扩展的训练平台。

整体框架包含三个主要阶段：环境克隆、任务生成和智能体训练。在环境克隆阶段，框架利用一个编码智能体（如GPT-5.2），根据真实网站的截图，通过本地文件系统和终端访问权限，编写、执行并迭代优化代码，重构出目标网站的合成版本。合成环境被表示为三元组 \((\mathcal{C}, \mathcal{D}, \mathcal{P})\)，其中 \(\mathcal{C}\) 是可执行的应用代码，\(\mathcal{D}\) 是底层数据库状态，\(\mathcal{P}\) 是一个Python SDK，用于提供受控的内部访问以查询和验证环境状态。此外，编码智能体还会创建辅助脚本（如服务器启动和重置工具），并通过类似人类开发者的迭代流程（使用Playwright MCP进行交互测试和错误修复）来稳定环境，确保其功能可靠且可重置。

在任务生成阶段，框架利用大语言模型为每个合成环境自动生成可验证的任务。每个任务 \(\mathcal{T}\) 包含一个自然语言描述和一个使用Python SDK \(\mathcal{P}\) 编写的验证程序。该验证程序能检查任务的可执行性，并创建一个可验证的评判器，通过可执行的谓词对环境状态进行判断，在任务结束时确定性地评估最终状态并返回二元奖励（任务完成与否）。这种方法实现了无需人工标注的大规模任务生成，并保证了任务正确性可以通过可执行验证而非启发式或基于LLM的评判来确定性评估。

在智能体训练阶段，智能体在合成环境中通过自演化的学习循环进行训练。在每个迭代中，智能体与克隆网站交互以解决采样任务，产生包含浏览器动作和观察的轨迹。任务完成后，通过Python SDK执行任务特定的验证程序，确定性地查询底层数据库状态 \(\mathcal{D}\)，从而产生可重复的奖励信号。这些可验证的奖励被用于更新智能体（例如采用基于奖励的拒绝微调），支持稳定且可扩展的学习。新生成的任务和收集的轨迹被迭代纳入训练过程，使智能体能逐步适应更复杂的行为。

创新点主要体现在：1) 将LLM作为环境创建者，自动生成高质量、可执行的合成网站环境，解决了真实环境探索的安全性和可重置性问题；2) 通过可编程验证程序实现任务的确定性奖励评估，摆脱了对启发式或LLM评判器的依赖，提高了反馈的可靠性和可重复性；3) 框架支持通过环境扩展实现可扩展的自演化学习，智能体训练与真实世界交互解耦，同时能通过增加训练环境数量来提升性能。

### Q4: 论文做了哪些实验？

论文的实验分为两部分：跨领域泛化实验和站点特定精通实验。

在跨领域泛化实验中，实验设置如下：使用GPT-5.2作为骨干LLM，Cursor CLI作为环境构建的编码代理来实施VeriEnv框架。平均每个网站的克隆过程耗时83.5分钟，成本3.6美元。从Mind2Web获取目标网站列表和截图，并确保克隆和训练过程中排除与评估基准测试集重叠的网站。构建合成环境并生成可验证任务后，基于Qwen3-4B和LLaMA-3.2-3B-Instruct两个开源基础模型训练网页智能体。采用基于拒绝的微调策略，在97个网站上采样智能体轨迹，仅保留满足可执行验证标准的轨迹作为监督训练数据。

使用的数据集/基准测试包括：WebArena-Lite（在Docker中实现的5个真实网站）和Mind2Web-Online（100多个真实网站的300个任务，分为简单、中等、困难三个难度级别，实验中排除了阻止网页智能体的任务，最终使用220个任务）。评估使用原始论文中的WebJudge-7B模型。

对比方法分为两类：1) 专有LLM：GPT-4o-mini、GPT-4o和Claude-3.5-Sonnet；2) 开源网页智能体：使用现有数据集和训练协议训练的模型，特别是Synatra（从网站特定教程构建合成轨迹）和Agent Data Protocol（ADP，聚合多个智能体数据集并标准化动作表示）。

主要结果：在完全域外的WebArena设置中，VeriEnv在不同基础模型上均能持续提升性能。具体而言，与基线相比，在Qwen3-4B和LLaMA-3.2-3B-Instruct上分别获得了+6.06和+9.09分的提升。ADP的表现因基础模型而异，在LLaMA-3.2-3B-Instruct上带来明显性能增益，但在Qwen上可能降低性能。

在站点特定精通实验中，实验设置如下：从WebArena中选取网站克隆为合成环境，作为自我进化智能体的训练场。智能体仅在克隆环境中交互，而非原始WebArena实例。目标是评估在可验证合成环境中的自我进化训练能否在固定网站上带来强大的域内性能。对比方法为PAE，后者生成任务并使用视觉语言模型评估轨迹。

主要结果：在三个代表性网站类别中，使用VeriEnv训练的智能体性能随着从基础模型到后续自我进化阶段的训练而持续提升，表明该方法在站点特定精通方面的有效性。

### Q5: 有什么可以进一步探索的点？

该论文提出的VeriEnv框架虽在安全性和可扩展性上取得进展，但仍存在若干局限和可探索方向。首先，其环境复现依赖语言模型，可能无法完全捕捉动态网站（如依赖实时API或用户交互生成内容）的复杂行为，导致模拟环境与真实场景存在偏差。未来可研究结合静态分析与动态执行追踪，提升复现保真度。

其次，当前任务生成与验证机制虽避免启发式评判，但任务多样性可能受限于预设的Python SDK接口。可探索引入多模态信息（如图像、布局结构）增强环境表征，并设计元学习框架让Agent自主发现更复杂的跨网站任务模式。

此外，框架未充分解决长期决策中的部分可观测性问题。未来可集成记忆机制与探索策略，使Agent能处理多步骤任务中的状态不确定性。最后，将验证机制扩展到非确定性场景（如网络延迟、内容更新）也是一大挑战，需设计概率性验证方法以增强鲁棒性。

### Q6: 总结一下论文的主要内容

该论文提出VeriEnv框架，旨在解决自主网页智能体训练面临的环境限制问题。核心问题是：真实网站环境存在探索风险、难以重置且缺乏可验证反馈，阻碍了智能体的安全与规模化学习。

论文的核心贡献是设计了一种将大语言模型作为环境创建者的方法，自动将真实网站克隆为完全可执行、可验证的合成环境。该方法通过Python SDK提供受控的内部访问，使智能体能够自主生成任务，并获得确定性的、可通过程序验证的奖励，从而摆脱了对启发式或基于LLM的评判器的依赖。

主要结论表明，在网页智能体基准测试中，通过VeriEnv训练的智能体能够泛化到未见过的网站，通过自我演化的训练实现针对特定站点的精通，并且受益于训练环境数量的扩展。其意义在于将智能体学习与不安全的真实交互解耦，同时通过环境扩展实现了可规模化的自我进化。
