---
title: "WindowsWorld: A Process-Centric Benchmark of Autonomous GUI Agents in Professional Cross-Application Environments"
authors:
  - "Jinchao Li"
  - "Yunxin Li"
  - "Chenrui Zhao"
  - "Zhenran Xu"
  - "Baotian Hu"
  - "Min Zhang"
date: "2026-04-30"
arxiv_id: "2604.27776"
arxiv_url: "https://arxiv.org/abs/2604.27776"
pdf_url: "https://arxiv.org/pdf/2604.27776v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "GUI Agent"
  - "Benchmark"
  - "Cross-Application Agent"
  - "Multi-Agent Framework"
  - "Autonomous Agent"
  - "Evaluation"
relevance_score: 9.0
---

# WindowsWorld: A Process-Centric Benchmark of Autonomous GUI Agents in Professional Cross-Application Environments

## 原始摘要

While GUI agents have shown impressive capabilities in common computer-use tasks such as OSWorld, current benchmarks mainly focus on isolated and single-application tasks. This overlooks a critical real-world requirement of coordinating across multiple applications to accomplish complex profession-specific workflows. To bridge this gap, we present a computer-use benchmark in cross-application workflows, named WindowsWorld, designed to systematically assess GUI Agents on complex multi-step tasks that mirror real-world professional activities. Our methodology uses a multi-agent framework steered by 16 occupations to generate four difficulty-level tasks with intermediate inspection, which are then refined by human review and executed in a simulated environment. The resulting benchmark contains 181 tasks with an average of 5.0 sub-goals across 17 common desktop applications, of which 78% are inherently multi-application. Experimental results of leading large models and agents show that: 1) All computer-use agents perform poorly on multi-application tasks (< 21% success rate), far below the performance of simple single-app tasks; 2) They largely fail at tasks requiring conditional judgment and reasoning across $\geq$ 3 applications, stalling at early sub-goals; 3) Low execution efficiency, where tasks often fail despite far exceeding human step limits. Code, benchmark data, and evaluation resources are available at github.com/HITsz-TMG/WindowsWorld.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前GUI代理基准测试在评估专业级跨应用工作流方面的严重不足。研究背景是，尽管现有基准如OSWorld已能评估代理在通用计算机使用任务上的能力，但它们主要聚焦于孤立、单一应用的任务。这种设计忽略了现实世界中完成复杂专业工作流所必需的多应用协调需求。现有方法的不足主要体现在三点：首先，跨应用任务严重匮乏（如AndroidWorld中多应用任务仅占9.50%），导致对代理真实能力的评估存在巨大偏差；其次，采用“全有或全无”的评分范式，无法为长时、高难度任务提供细粒度的进度诊断，使得大量部分成功的模型无法被有效区分；最后，基准构建依赖劳动密集型的人工筛选或重复的模板替换，难以规模化且缺乏专业背景的真实感。因此，本文的核心问题是构建一个名为WindowsWorld的过程导向型基准，以系统性地评估GUI代理在需要协调多个桌面应用（平均2.4个/任务，78%为多应用任务）的专业级、多步骤工作流上的表现，并引入中间检查点机制来奖励部分进展，从而实现更精细、更具诊断性的评估。

### Q2: 有哪些相关研究？

相关研究可分为以下几类：

1. **桌面环境基准**：早期工作如MiniWoB、MiniWoB++、WebShop、Mind2Web、WebArena和VisualWebArena聚焦于单步准确率或简单任务。OSWorld引入首个可扩展的执行评估环境，支持Ubuntu、Windows和macOS；Windows Agent Arena专注于Windows和云并行测试；OSUniverse提出渐进难度任务。本文基于OSWorld基础设施，但将任务复杂度推至跨应用多步流程的新高度。

2. **GUI Agent评估方法**：传统方法依赖最终状态匹配或成功率，但难以定位失败原因。ProBench通过“过程提供者”捕获中间信息；SPA-Bench和A3实现了步骤级验证但依赖固定轨迹或LLM分解。本文创新性地引入基于检查点的灵活评分系统，允许替代合法路径，同时通过关键流程节点确保功能正确性。

本文的核心区别在于：将基准从单应用任务扩展到多应用协同的专业工作流（78%的任务涉及多应用），并采用16种职业角色驱动的多智能体生成方法，结合人工审核与中间检查点，系统评估复杂条件推理与执行效率瓶颈。

### Q3: 论文如何解决这个问题？

WindowsWorld通过一个半自动化的多智能体流水线来解决跨应用GUI代理基准测试的构建问题，该流水线结合了LLM生成、系统验证和人工审核。整体框架分为四个阶段：首先，**Generator**利用DeepSeek-V3.2作为LLM，基于16种职业角色的日常工作流程和应用依赖关系生成候选任务，并引用真实开放的互联网资源（如GitHub、Wikipedia）确保生态有效性。其次，**Refiner**通过自动化的四节点管道进行质量控制：语义去重器剔除相似度>0.85的冗余任务；有效性审核器异步验证URL和文件的可访问性；依赖推理器将程序性前提转化为确定性环境状态；指标精炼器标准化评估标准，确保中间检查点明确可验证。随后，**Human Reviewer**由四名人工标注员执行最终审核，筛除指令模糊、依赖主观判断或需要不可用软件/服务的任务。最后，**Environment Generator**利用LLM自动合成任务所需的环境文件（如.xlsx、.docx），并通过智能文件合并策略为相同职业创建一致的数据资源。该流水线最终产出了包含181个任务的基准，其中77.9%为跨应用任务，平均每个任务包含5.0个子目标。

在架构上，该基准将GUI交互形式化为部分可观测马尔可夫决策过程（POMDP），并引入过程感知评估协议，通过自动化裁判（Qwen3-VL-Plus）在中间检查点上打分，实现细粒度的部分进度评估。创新点包括：1）提出一种融合LLM生成、自动化验证和人工审核的半自动任务生成流水线，大幅降低构建成本并保证任务多样性；2）设计基于职业角色和难度等级（L1-L4）的双轴任务组织体系，特别是L4级别的不可达任务用于测试代理拒绝不合理目标的能力；3）引入过程感知评估机制，通过多个中间状态检查点（平均4.97个/任务）替代传统的二元结果评分，能够诊断长期推理中的具体瓶颈，且与人工评分相关性高达0.91。这一设计有效解决了现有基准在跨应用、长流程任务上评估粒度不足的问题。

### Q4: 论文做了哪些实验？

论文在WindowsWorld基准测试上评估了多种SOTA模型和专用GUI智能体。实验设置包括通用多模态模型（Gemini-3-flash/pro-preview、GPT-5.2、Claude-Sonnet 4.5、Qwen3-VL-Plus）和专用GUI智能体（Agent-S3、UiPath Screen Agent）。输入模态分为截图、截图+无障碍树（Hybrid）和Set-of-Marks（SoM）三种。任务分L1-L4四个难度等级，共181个任务，平均5.0个子目标，78%为多应用任务。主要结果表明：所有智能体在多应用任务上表现较差（成功率<21%），远低于单应用任务。Gemini-3-flash在Hybrid模式下表现最佳，中间进度得分$S_{int}$为50.32%，但最终完成得分$S_{final}$仅为20.44%，显示效率-完成度差距。随着难度从L1到L3，Gemini-3-flash的$S_{final}$从35.90%骤降至16.67%，表明跨应用协调和状态维护存在瓶颈。L4负约束处理中，最佳模型GPT-5.2 (SoM)成功率仅25%。错误分析显示，模型在跨应用任务中早期子目标即出现失败，如中文文件打开和跨应用信息传输。消融实验表明，英文指令优于中文指令。

### Q5: 有什么可以进一步探索的点？

根据论文及分析，WindowsWorld 的局限性及未来可探索点如下：首先，当前依赖全轨迹执行和人工校验的评分机制限制了规模化扩展，未来可探索自动化、可泛化的奖励函数设计，例如引入过程监督学习或基于逆强化学习的稀疏奖励塑造，以支持大规模在线强化学习。其次，环境仅针对单语言操作系统优化，无法评估非英语/中文UI元素的鲁棒性，后续可构建多语言UI适配层或借助视觉语言模型实现跨语言界面理解。此外，任务设计虽多步骤但当前缺乏对动态环境反馈和长程推理瓶颈的显式建模，可考虑引入在线适应机制（如失败时重规划）或基于子目标分解的层次化强化学习。最后，未纳入对MCP等工具调用协议的评估，未来可设计跨应用API交互的标准化评估，模拟真实专业场景中工具链的协作执行。这些方向将推动GUI代理从封闭式单应用任务向开放、动态的专业化工作流演进。

### Q6: 总结一下论文的主要内容

WindowsWorld提出了首个面向跨应用工作流的GUI智能体基准，聚焦专业级多步骤任务。当前基准多局限于单应用场景，而真实专业工作常需协调多个应用。论文通过16个职业驱动的多智能体框架，生成含4个难度等级、具有中间检查点的181个任务，平均5个子目标，覆盖17个桌面应用，其中78%任务天然跨应用。实验发现：1) 所有智能体在多应用任务中成功率低于21%，远低于单应用表现；2) 在需要条件判断和涉及3个以上应用的推理任务中，智能体普遍在早期子目标阶段失败；3) 执行效率低下，任务常因远超人类步骤限制而失败。该工作揭示了当前GUI智能体在复杂专业工作流中的重大局限，为构建更实用的自主系统提供了重要评测基准，推动领域从单应用对话向多应用协作业升级。
