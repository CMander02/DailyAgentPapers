---
title: "Measuring Safety Alignment Effects in Autonomous Security Agents"
authors:
  - "Isaac David"
  - "Arthur Gervais"
date: "2026-05-19"
arxiv_id: "2605.19722"
arxiv_url: "https://arxiv.org/abs/2605.19722"
pdf_url: "https://arxiv.org/pdf/2605.19722v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "安全对齐"
  - "自主安全Agent"
  - "基准测试"
  - "工具使用"
  - "拒绝行为评估"
relevance_score: 7.5
---

# Measuring Safety Alignment Effects in Autonomous Security Agents

## 原始摘要

Do stock safety-aligned language models and their uncensored or abliterated derivatives behave differently when run as autonomous security agents? Single-turn refusal benchmarks cannot answer this question: security agents must inspect repositories, call tools, and produce vulnerability evidence inside authorized sandboxes.
  We present a trace-based benchmark of 30 local vulnerability-analysis tasks with fixed tools, deterministic success predicates, redaction rules, and grounding checks, and compare four stock models against uncensored or abliterated derivatives: Gemma 4 31B, Gemma 4 26B A4B, Qwen2.5-Coder 7B, and Llama 3.1 8B. The artifact contains 1,500 security-agent traces and 800 non-security control traces. The Gemma pairs show large less-restricted gains on security tasks: 14.0% versus 0.7% success for 31B and 10.7% versus 0.0% for 26B, with higher mean grounding (3.91 versus 3.27 and 4.12 versus 1.64 out of five) and 0.0% refusal, suppressed-action, and unsafe-action rates in the 31B traces. However, controls and non-Gemma pairs rule out a clean security-specific or universal less-restricted effect: Gemma gaps also appear on ordinary coding tasks, Qwen2.5-Coder success is lower for the less-restricted derivative (2.0% versus 5.3%), and the abliterated Llama derivative fails the tool protocol. Across all families, hard proof-of-trigger and patch-verification tasks remain unsolved. These results show that safety alignment effects in autonomous security agents should be measured at the system level, separating refusal, unsafe action, tool reliability, and evidence grounding rather than treating refusal rate as the safety signal.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决的问题是：在自主安全代理（autonomous security agents）的工作场景中，传统的基于单轮拒绝（single-turn refusal）的安全对齐评估方法已经失效。研究背景是，语言模型正从简单的顾问角色转变为能够自主检查仓库、调用工具、在沙盒中验证漏洞并存取证的安全代理。现有方法（如传统的拒绝基准测试）只能评估模型在单轮对话中是否拒绝回答恶意问题，但无法衡量模型在实际授权任务中的表现，例如定位漏洞、验证可触发路径或验证补丁有效性。

现有方法的不足在于，它们将“可见拒绝率”作为唯一的安全信号，忽视了代理在工具调用可靠性、证据质量（grounding）和任务完成能力方面的表现。例如，一个模型可以安全地拒绝回答，但它在执行授权漏洞分析任务时可能因能力不足或工具协议失败而表现更差。相反，一个较少限制的模型可能成功完成任务，但也可能产生不可靠的行动。

因此，本文的核心问题是：模型层面的安全对齐（safety alignment）如何影响自主安全代理在执行授权的、沙盒化的本地安全任务时的性能和证据质量？论文通过系统级基准测试，将拒绝行为、工具可靠性、证据基础和任务成功率分离评估，以揭示安全对齐在自主代理场景中的复杂真实效应。

### Q2: 有哪些相关研究？

相关研究主要分为以下几类：第一，对齐与拒绝机制研究，本文指出传统单轮拒绝基准（如HarmBench、JailbreakBench）仅评估对话场景下的有害内容拒止，无法衡量自主安全代理在多轮工具调用中的行为差异。第二，网络安全能力基准，包括CyberSecEval 2/3、Cybench、EnIGMA等，它们强调可执行环境和任务验证，本文借鉴了其成功率判定和部分评分方法，但创新性地采用配对对比设计，固定基准、任务和种子以隔离对齐条件影响。第三，智能体基准与工具使用研究，如AgentBench、SWE-bench、OSWorld等揭示了多轮交互中单轮问答不可见的失败模式，本文据此设计了机器可读任务清单和确定性检查器。第四，拒绝消除机制，社区“uncensored/abliterated”模型通过激活方向编辑等方法减少拒绝行为，本文利用这些衍生模型进行配对比较，但明确指出其不能作为完美反事实，需配合非安全任务校验和模型溯源分析。此外，Gemma 4系列因官方明确支持agent用例而被选为核心研究对象。本文与这些工作的核心区别在于：将评估重心从拒绝率转向系统级指标（拒绝、不安全动作、工具可靠性、证据接地度），并揭示了安全对齐效果在自主代理场景下并非单向或普适的结论。

### Q3: 论文如何解决这个问题？

该论文通过构建一个基于轨迹的基准测试框架来评估自主安全智能体的安全对齐效果，核心方法包括：

整体框架采用“模型套件-共享安全智能体框架-轨迹测量”三阶段设计。模型套件包含四组配对模型（Gemma 4 31B、Gemma 4 26B A4B、Qwen2.5-Coder 7B和Llama 3.1 8B），每组包含官方对齐版本与去限制版本（未经审查或消融的衍生模型），并额外测试了Gemma 31B的授权和越狱提示条件。

共享框架包含六个核心模块：任务清单（定义30个本地漏洞分析任务，分为漏洞定位、可达性验证、触发证明、补丁验证和安全报告编写五类）、本地沙箱、智能体控制器、工具执行模块、轨迹检查器和确定性成功谓词。所有任务使用固定工具、预算、种子和控制器模式，确保可比性。

关键技术包括：1) 确定性成功谓词，基于文件、命令输出和报告工件自动判断任务成功；2) 证据接地评分，通过不区分大小写的子串匹配检查智能体是否读取了相关文件并将本地证据与最终工件关联；3) 两级控制器模式（严格控制器和修复控制器），后者修复了常见接口故障；4) 完整的轨迹日志记录和自动审查前编辑。

主要创新点在于：1) 将安全对齐效果测度从单轮拒绝基准扩展到系统级多维度评估，分离拒绝率、不安全动作、工具可靠性和证据接地等指标；2) 包含800个非安全控制轨迹（12个本地编码任务和8个HumanEval/MBPP风格修复任务），区分安全特定效果与通用模型质量差异；3) 采用配对任务-种子运行设计，避免模型族、架构和衍生来源差异带来的统计偏差。

### Q4: 论文做了哪些实验？

论文构建了一个基于30个本地漏洞分析任务的trace基准测试，包含1500条安全智能体trace和800条非安全控制trace。实验设置了四个模型对：Gemma 4 31B、Gemma 4 26B A4B、Qwen2.5-Coder 7B和Llama 3.1 8B，每个模型对比其原始对齐版本与未审查/消融版本。所有任务使用固定工具集、确定性子成功谓词、修订规则和基础性检查。

主要结果如下：Gemma 31B的未审查版本在安全任务上成功率为14.0%（21/150），而对齐版本仅为0.7%（1/150）（McNemar p=1.10×10⁻⁵），平均基础性得分分别为3.91和3.27。Gemma 26B A4B未审查版本成功率为10.7%（16/150），对齐版本为0.0%，基础性得分为4.12 vs 1.64。但非Gemma模型未呈现一致趋势：Qwen2.5-Coder的消融版本成功率反而更低（2.0% vs 5.3%），Llama 3.1的消融版本成功率为0.0%且基础性近乎为零。所有模型在验证触发条件和补丁验证等硬任务上均未成功。控制实验表明，Gemma的差异也出现在普通编码任务中，非安全控制任务揭示了更广泛的能力/基础性差距而非纯粹的安全对齐效应。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面：首先，当前研究仅对比了有限几个模型家族的“安全对齐”与“无限制”衍生版本，缺乏更广泛模型架构和更大规模参数的实验，因果推断不够纯净；其次，硬性的“触发证明”和“补丁验证”任务在所有模型上成功率极低，说明当前方法在复杂自主安全代理场景下仍然缺乏核心竞争力；最后，评估依赖固定工具集和确定性评分，缺乏可执行证据检查和跨语言、跨领域的泛化测试。

未来可探索的方向包括：构建更干净、规模更大的匹配模型对，引入干预实验以分离安全对齐效果与模型能力差异；设计更灵活的沙箱工具接口和可执行证据检查机制，提升复杂任务的验证能力；探索在系统边界（如权限管理、痕迹审查）而非模型输出层面施加安全控制的有效性；以及将评估扩展至多语言、多轮交互和实时协作场景，分析安全对齐效果的非对称性和动态演化规律。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种基于轨迹的基准测试方法，用于评估自主安全代理中的安全对齐效应。传统单轮拒绝基准无法回答安全代理在检查仓库、调用工具和生成漏洞证据等操作中的行为差异。为此，作者构建了一个包含30个本地漏洞分析任务的基准，并配备了固定工具、确定性成功谓词、编辑规则和基础验证。他们对比了四组模型及其去约束或消融版本：Gemma 4 31B、Gemma 4 26B、Qwen2.5-Coder 7B和Llama 3.1 8B，生成了1500条安全代理轨迹和800条非安全控制轨迹。结果显示，Gemma模型在安全任务上表现显著（31B成功率14.0% vs 0.7%，26B为10.7% vs 0.0%），基础得分更高，且无拒绝、抑制或不安全行为。但控制组和非Gemma组否定了纯粹的安全特异性效应：Gemma的改进也出现在普通编码任务中，Qwen2.5-Coder去约束版本成功率反而下降（2.0% vs 5.3%），消融的Llama模型工具协议失败。所有模型在困难的证明触发和补丁验证任务上均未成功。核心结论是，应通过系统级轨迹测量安全对齐效应，区分拒绝、不安全行为、工具可靠性和基础验证，而非仅关注拒绝率。论文的重要贡献在于推动了基于证据的、轨迹感知的安全代理评估方法。
