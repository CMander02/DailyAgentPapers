---
title: "Trust No Tool: Evaluating and Defending LLM Agents under Untrusted Tool Feedback"
authors:
  - "Lecheng Yan"
  - "Ruizhe Li"
  - "Xicheng Han"
  - "Wenxi Li"
  - "Binwu Wang"
  - "Longyue Wang"
  - "Chenyang Lyu"
  - "Guanhua Chen"
date: "2026-05-17"
arxiv_id: "2605.17453"
arxiv_url: "https://arxiv.org/abs/2605.17453"
pdf_url: "https://arxiv.org/pdf/2605.17453v1"
categories:
  - "cs.CR"
  - "cs.CL"
tags:
  - "LLM Agent安全"
  - "工具使用Agent"
  - "认知中毒攻击"
  - "Agent安全基准"
  - "最终动作风险评估"
  - "Trust-Bench"
  - "VISTA-Guard"
  - "多步工具交互"
  - "黑盒工具生态"
relevance_score: 8.5
---

# Trust No Tool: Evaluating and Defending LLM Agents under Untrusted Tool Feedback

## 原始摘要

Tool-using LLM agents increasingly rely on external tools to make consequential decisions, yet most existing agent-security benchmarks and defenses implicitly assume that tool feedback is trustworthy once a tool has been selected. We study a different failure mode, cognitive poisoning, in which a malicious tool behaves plausibly during exploration, accumulates trust through benign-looking feedback, and becomes harmful only when hidden state conditions align with the final executable action. To study this setting, we construct TRUST-Bench, a task-conditioned benchmark of 1,970 hidden-trigger tool-compromise episodes with matched safe controls, introduce an asymmetric penalty metric, GuardedJoint, to better reflect real deployment risk, and present VISTA-Guard, a backbone-agnostic framework for final-action risk scoring. The core idea is to abstract multi-step tool interaction into structured environment variables that encode trust-formation dynamics and then score the risk of the final executable action from this trajectory-conditioned representation. Experiments show that prompt-centric heuristics, scalarized features, and zero-shot judges fail in this regime, whereas trajectory-aware final-action scoring yields strong in-domain discrimination and remains effective under balanced out-of-distribution transfer. Under GuardedJoint, VISTA-Guard reaches $84.2$ in-domain and $56.9$ on balanced out-of-distribution evaluation, while methods that optimize only one side of the safety--utility tradeoff collapse to zero. These findings support a broader view of agent security in black-box tool ecosystems: the decisive defense target is not local prompt text or tool descriptors alone, but the way trust is formed across the interaction trajectory and committed through the final action.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决LLM Agent在使用外部工具时面临的一种新型安全威胁——“认知投毒”（cognitive poisoning）。研究背景是，现有工具型LLM Agent的安全评测与防御方法普遍隐含一个假设：一旦工具被选中，其反馈就是可信的，恶意行为在局部文本、工具描述或明显不安全的输出中就能被检测到。

现有方法的不足在于，它们忽略了黑盒工具生态系统中“工具泛化安全”的问题：Agent无法直接验证外部工具的可靠性，只能通过反复交互推断信任。这造成了一个独特的攻击面——恶意工具在探索阶段表现得与良性工具无异，通过看似无害的反馈积累Agent的信任，只有当最终可执行动作满足隐藏的状态条件（如特定参数组合）时才会变得有害。

本文要解决的核心问题是：如何防御这种状态条件触发的、跨多步交互的隐蔽投毒攻击。该攻击并非通过单一恶意消息，而是通过塑造Agent在整个交互轨迹中的信任先验来实现攻击，使得最终危险动作看似平常。为此，论文构建了TRUST-Bench基准，并提出了VISTA-Guard框架，通过轨迹条件化的最终动作风险评分来应对这一挑战。

### Q2: 有哪些相关研究？

相关工作可分为三类。**评测类**方面，ToolEmu、InjecAgent、AgentDojo等基准研究间接提示注入和不安全工具使用，但本文指出这些工作的恶意性局限于单次提示或显式不安全调用，而本文研究的“认知中毒”攻击中，恶意行为仅在轨迹状态与最终动作对齐时才显现，因此本文构建的TRUST-Bench基准专门捕捉这种隐式威胁。**应用类**方面，ToolSandbox、StableToolBench、Toolathlon关注工具泛化与状态交互，近期MCP研究分析了元数据投毒、隐式工具投毒及自适应信任校准；本文在此基础上进一步探究代理在探索性交互中如何建立信任并安全泛化。**防御类**方面，Task Shield、CaMeL、ToolSafe等运行时防御及世界模型推理方法主要针对通用恶意文本，而本文提出的VISTA-Guard框架则聚焦于探索性信任形成下的最终动作风险评分，其核心创新在于将多步工具交互抽象为结构化环境变量，编码信任动态，而非仅依赖局部提示或工具描述。

### Q3: 论文如何解决这个问题？

论文通过设计VISTA-Guard框架解决不可信工具反馈下的LLM Agent安全问题。核心创新在于将多步工具交互抽象为结构化环境变量，编码信任形成动态，再对最终可执行动作进行风险评分。

整体框架包含三个模块：1) **轨迹状态视图**将每次探索回合转换为可审计的状态信号，统计触发阶段次数、探针检测、不匹配、标识符漂移和警告等计数，并计算辅助的state_risk标量；2) **最终动作参数视图**从提议的最终工具调用中提取工具名称、载荷键/令牌数以及高影响、绕过和安全提示的紧凑标记计数；3) **双分支风险评分**将轨迹状态和动作参数序列化为输入，通过微调LLM骨干网络学习low_risk/high_risk分类，最终使用校准阈值决定执行或拒绝。

关键技术包括：采用GuardiedJoint不对称惩罚指标反映真实部署风险；使用Mistral-7B等六个LLM骨干网络展示架构无关性；通过5折交叉验证校准拒绝阈值以平衡安全性与实用性。实验表明，纯提示启发式、标量化特征和零样本判断方法在此场景失效，而轨迹感知的最终动作评分在域内达到84.2 GuardiedJoint分数，在域外转移下仍保持56.9有效性能。

### Q4: 论文做了哪些实验？

论文在TRUST-Bench数据集（1970个隐藏触发工具妥协任务及匹配的安全对照组）上进行了多组实验。实验采用分组5折交叉验证，使用GuardedJoint（ρ=1.5）作为主要评估指标，对比了VISTA-Guard、TF-IDF+逻辑回归、TF-IDF+SVM、TF-IDF+MLP、BERT-base、GB（10-feat）和ToolShield等基线方法。

主要结果：VISTA-Guard在域内评估中表现最佳（Mistral骨干达到84.2分），是所有方法中唯一能同时保持低误警率（AMR）和低漏报率（RNR）并获得正GuardedJoint分数的方法族。在平衡的域外迁移测试（来自ToolEmu和SafeToolBench的9,216个样本）中，VISTA-Guard依然领先（56.9分），优于TF-IDF+逻辑回归（50.3分）、TF-IDF+SVM（43.6分）和ToolShield（43.3分）。消融实验证实：完整结构化三元组表示（62.6分）优于原始轨迹文本（50.7分），移除自适应状态证据会降低性能（42.1分），而仅依赖参数信息退化为0分。基于提示词、启发式规则或标量特征的基准方法在不对称指标下均失效。

### Q5: 有什么可以进一步探索的点？

首先，当前研究依赖于构造的基准测试TRUST-Bench，其“三步探索+二值动作”的设置简化了现实场景。未来可探索更长交互链、自适应攻击者以及多步修复策略，以更贴近生产环境。其次，论文揭示了轨迹信任形成与最终动作风险的关联，但VISTA-Guard仅处理最终动作评分。一个改进方向是引入动态防御机制，在交互过程中实时检测信任异常并干预，而非仅在终点做决策。此外，当前工作假设工具反馈是唯一威胁源，但现实攻击可能结合提示注入或旁路操纵。未来可构建统一框架，将本地提示、工具状态与轨迹特征联合建模，例如利用图神经网络编码工具调用间的依赖关系。最后，论文在OOD迁移中性能显著下降（56.9 vs 84.2），表明对未见过的工具生态泛化能力薄弱。可尝试基于元学习或因果干预的方法，提取跨场景不变的信任形成模式，而非依赖表面统计特征。这些扩展将推动从“静态基准”向“鲁棒部署”的跃迁。

### Q6: 总结一下论文的主要内容

论文针对LLM代理使用工具时面临的新型安全威胁——“认知投毒”——进行了系统研究。问题定义：恶意工具在探索阶段表现正常，通过良性反馈积累信任，仅在隐藏状态条件与最终可执行动作对齐时才触发危害，传统安全评测与防御隐含假设工具反馈可靠。方法概述：构建了TRUST-Bench基准，包含1970个隐藏触发工具妥协场景及匹配安全对照；提出非对称安全-效用度量指标GuardedJoint；开发VISTA-Guard框架，将多步工具交互抽象为结构化环境变量编码信任形成动态，进而对最终可执行动作进行风险评分。主要结论：提示启发式、标量特征和零样本法官在此场景下失效，而轨迹感知的最终动作评分在域内表现优异（GuardedJoint得分84.2），并在平衡分布外迁移中保持有效（56.9），仅优化安全或效用单一指标的方法得分归零。核心贡献在于揭示防御关键不是局部提示文本或工具描述，而是交互轨迹中的信任形成与最终执行动作的承诺。该工作拓展了黑盒工具生态下代理安全防御的视野。
