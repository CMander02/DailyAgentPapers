---
title: "AgentHijack: Benchmarking Computer Use Agent Robustness to Common Environment Corruptions"
authors:
  - "Jingwei Sun"
  - "Jianing Zhu"
  - "Yuanyi Li"
  - "Tongliang Liu"
  - "Xia HU"
  - "Bo Han"
date: "2026-05-25"
arxiv_id: "2605.25707"
arxiv_url: "https://arxiv.org/abs/2605.25707"
pdf_url: "https://arxiv.org/pdf/2605.25707v1"
categories:
  - "cs.AI"
tags:
  - "MLLM Agent"
  - "Robustness"
  - "Benchmark"
  - "Computer Use Agent"
  - "Environment Corruption"
  - "Agent Safety"
relevance_score: 9.0
---

# AgentHijack: Benchmarking Computer Use Agent Robustness to Common Environment Corruptions

## 原始摘要

Autonomous computer use agents that powered by multimodal large language models (MLLMs) are emerging as capable assistants for completing complex digital workflows. However, real-world execution environments are far from ideal: pop-ups, resolution changes, and competing applications frequently interfere with agent perception and control. We introduce AgentHijack, a benchmark designed to evaluate the robustness of computer-use agents under common corruptions, where the uncertainties in dynamic environment disrupt the execution flow without direct adversarial intent. Specifically, AgentHijack introduces 9 configurable common corruptions to replicate realistic imperfect scenarios. We evaluate a variety of desktop tasks that utilize MLLM-based agents and discover that even minor instances of corruption can result in substantial performance degradation, which emphasizes the fragility of agents and underscores the necessity of robustness evaluation. Afterward, we propose AgentHijack-Agent, a framework that integrates an action generator with enhanced grounding capabilities and an onlooker responsible for behavior summarization and environment checking. Extensive experiments validate its effectiveness. Our code, environment, baseline models and data are publicly available at: https://AgentHijack.github.io.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多模态大语言模型（MLLM）驱动的计算机使用代理在实际动态环境中鲁棒性不足的问题。研究背景是：这类代理在完成复杂数字工作流方面展现出巨大潜力，现有基准如OSWorld、WebArena等主要关注其在干净环境下的任务成功率。然而，真实世界的执行环境充满不确定性，诸如弹窗、分辨率变化、网络错误等常见环境干扰会频繁影响代理的感知与控制。现有方法的不足之处有三：第一，多数研究仅在理想化干净环境中评估代理性能，忽略了真实场景的复杂性；第二，部分工作虽探索了异常环境下的鲁棒性，但主要聚焦于对抗性攻击，而非日常干扰；第三，少数关注常见干扰的研究采用问答式评估范式，缺乏真实的可执行环境和灵活的自定义配置支持。本文的核心问题是：建立首个系统评估MLLM计算机使用代理在常见环境干扰下鲁棒性的基准（AgentHijack），通过引入9种可配置的常见干扰类型，揭示当前代理在动态环境中的脆弱性，并提出增强鲁棒性的框架AgentHijack-Agent。

### Q2: 有哪些相关研究？

主要相关研究可分为三类。第一类是**计算机使用智能体框架**，如利用GPT-4o进行规划解决歧义的GTA1、基于Qwen-VL增强规划与定位能力的UI-TARS、以及通过稀疏奖励实现端到端优化的ARPO。这些工作聚焦于提升智能体在开放环境中的任务执行能力，而本文则关注它们在实际环境中的脆弱性。第二类是**任务性能基准**，包括模拟网页环境的Mind2Web和WebArena、覆盖日常与办公场景的OSWorld、以及针对移动端的AndroidWorld。本文与这些基准不同，它不评估理想条件下的任务完成度，而是系统性地测试环境扰动下的鲁棒性。第三类是**鲁棒性与安全评测**，如针对恶意指令的Injecagent、R-Judge、SafeArena，以及关注屏幕扰动的VisualWebArena-Adv和评估各类攻击的RiOSWorld。然而，现有工作大多聚焦于对抗性攻击，忽略了由弹窗、分辨率变化等常见环境扰动导致的非恶意故障。本文提出的AgentHijack专门填补了这一空白，通过9种可配置的常见扰动来模拟现实中的不完美场景，并揭示了即使轻微扰动也会导致性能大幅下降。相比而言，本文更关注环境本身的非对抗性噪声对智能体感知与控制的破坏。

### Q3: 论文如何解决这个问题？

论文提出了AgentHijack-Agent框架来解决GUI代理在常见环境干扰下的脆弱性问题。整体框架包含三大核心模块：增强定位能力的动作生成器、负责行为总结与环境监控的旁观者，以及数据增强群体相对策略优化（DA-GRPO）训练方法。

关键技术方面，首先通过DA-GRPO进行端到端优化，不同于传统GRPO仅在干净环境中采样，DA-GRPO从多种受干扰环境（如弹窗、分辨率变化、标记等9种干扰）中生成多样化响应轨迹，并采用经验回放缓冲池保留成功轨迹，解决稀疏奖励问题。其次，引入旁观者模块解决两个关键缺陷：一是持续捕获环境状态变化（包括意外操作如误触、应用最小化等），将环境变化总结为简短描述$d_t$融入上下文$\{o_1,d_1,...,o_k,d_k,...o_t,d_t\}$；二是在任务执行前进行初始环境检查，利用外部错误信息库验证网络连接、身份验证等环境状态，避免无效探索。

创新点主要体现在：1）首次系统评估GUI代理在9种实际环境干扰下的鲁棒性；2）DA-GRPO通过多干扰环境数据增强训练，显著提升泛化能力（在弹窗干扰下提升11.23%，验证环节提升9.67%）；3）旁观者模块的持续环境监控与行为总结机制，有效缓解了代理因意外操作导致的错误归因和注意力偏移问题。实验表明，该框架在平均性能上比顶级基线UI-TARS-1.5-7B提升4.15个百分点。

### Q4: 论文做了哪些实验？

论文围绕 AgentHijack 基准测试，系统评估了多模态大模型驱动的计算机使用智能体在常见环境扰动下的鲁棒性，并验证了所提 AgentHijack-Agent 框架的有效性。

实验设置方面，采用 1920×1080 分辨率的截图作为观测，最大历史图像 15 张，智能体最多执行 10 步。数据集为 AgentHijack 基准，包含 9 种可配置的常见环境扰动（如弹窗、分辨率变化、意外触摸等）。对比了 9 个代表性模型：Qwen2.5-VL-72B-Instruct、Llama-3.2-90B-Vision-Instruct、GLM-4.5V、Gemini-2.5-Pro、GPT-4o、Claude-3.7-Sonnet、UI-TARS-7B-DPO、UI-TARS-72B-DPO 和 UI-TARS-1.5-7B，统一设置温度 0.6、top-p 0.9、最大 token 1500。AgentHijack-Agent 基于 UI-TARS-1.5-7B 使用 VERL 框架微调，128 个任务训练 15 个 epoch。

主要结果：当前智能体在扰动下表现脆弱，如 UI-TARS-1.5-7B 在干净数据上成功率为 24.21%，受干扰后降至 18.74%。AgentHijack-Agent 将平均成功率提升 4.15%。消融实验表明：框架对扰动位置和内容鲁棒；各模块（强化学习、旁观者模块）均不可或缺；更强大的旁观者模型（如 Qwen3-VL-235B-A22B-Instruct）带来更大增益，但为平衡性能与计算开销，选用微调后的 UI-TARS-1.5-7B。案例分析显示，该框架能准确判断动作后果、适应意外操作并主动验证环境。

### Q5: 有什么可以进一步探索的点？

根据论文内容，未来可探索的方向包括：首先，论文仅关注单一任务中的瞬时扰动，可进一步研究多步任务中累积性、级联式环境干扰对决策链的影响。其次，当前9种扰动类型主要针对视觉感知层面（如弹窗、分辨率突变），可扩展至逻辑层攻击（如界面元素语义错位、API调用延迟模拟），以更贴近实际多Agent协作场景。此外，AgentHijack-Agent的"旁观者"模块在实时异常检测中依赖静态规则，可引入在线强化学习或差分注意力机制，使其能动态适应环境变化而非仅触发预设修复。最后，论文以成功率评估鲁棒性，但未量化扰动对执行路径合法性的影响（例如绕过安全校验的隐藏风险），建议建立包含安全性指标的多维度评估体系，并探索对抗训练与软动作约束的融合方法。

### Q6: 总结一下论文的主要内容

这篇论文提出了AgentHijack基准，旨在评估基于多模态大语言模型的计算机使用代理在真实动态环境中的鲁棒性。问题定义是：现实执行环境中常见的弹窗、分辨率变化和竞争应用等干扰（定义为9种可配置的“常见损坏”）会破坏代理的感知和控制流程，导致性能显著下降。方法上，论文构建了包含多种桌面任务的基准测试，并提出了AgentHijack-Agent框架，该框架集成一个具有增强基础能力的行为生成器和一个负责行为总结与环境检查的观察者。主要结论是：现有代理在面对微小环境干扰时表现出严重脆弱性，暴露出基础能力不足、易被意外操作干扰以及缺乏错误检测能力等问题。AgentHijack-Agent通过引入环境检查机制有效提升了鲁棒性。该研究的核心贡献是揭示了计算机使用代理在非理想环境下的脆弱性，并提供了一个可配置的鲁棒性评估基准与解决方案。其意义在于强调了鲁棒性评估的重要性，为开发更可靠的自主代理提供了方向。
