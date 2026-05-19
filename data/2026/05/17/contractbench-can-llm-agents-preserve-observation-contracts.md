---
title: "ContractBench: Can LLM Agents Preserve Observation Contracts?"
authors:
  - "Jicheng Wang"
  - "Yifeng He"
  - "Zili Wang"
  - "Hanwen Xing"
  - "Arkaprava De"
  - "Hao Chen"
date: "2026-05-17"
arxiv_id: "2605.17281"
arxiv_url: "https://arxiv.org/abs/2605.17281"
pdf_url: "https://arxiv.org/pdf/2605.17281v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Tool-Augmented Agent"
  - "Agent Evaluation"
  - "Benchmark"
  - "API Compliance"
  - "Observation Contract"
  - "Integrity"
  - "Temporal Validity"
  - "Regression Analysis"
  - "Model Comparison"
relevance_score: 7.5
---

# ContractBench: Can LLM Agents Preserve Observation Contracts?

## 原始摘要

Tool-augmented LLM agents call APIs whose intermediate outputs, such as presigned URLs, session tokens, and OAuth state parameters, are observation contracts: artifacts whose later use is constrained by the external system that produced them. We show that observation contract compliance (preserving the temporal validity and byte-level integrity) is an emergent, regression-prone capability: it is neither guaranteed by general tool-use ability nor consistently improved by larger or newer models. To measure this, we introduce ContractBench, a benchmark of 33 dual-axis tasks that probe two orthogonal failure modes no existing benchmark evaluates: validity failures (using an artifact after expiry) and integrity failures (corrupting an artifact's bytes through the observation-to-action pipeline). Our evaluation is deterministic and programmatic, with a virtual clock controlling time and SHA-256 hashes verifying byte integrity. We assign each outcome a failure label drawn from real-world API specifications. We evaluate 38 models and report four findings: (i) no evaluated model clears 80%, with Claude-Opus-4.6 leading at 77.8%, revealing that current frontier models still fail to comply with observation contracts; (ii) a sharp within-family capability cliff in Qwen 3.5 between 4B (0%) and 9B (56.6%), smoothing to 70.7% at 397B-A17B: what emerges across the cliff is mid-trajectory restraint, not tool-call competence; (iii) non-monotonic scaling across the GPT-5 family: agentic post-training can erode compliance through sycophancy-driven regression; (iv) our failure taxonomy works as an actionable in-context reward signal, yielding +7.1 pp on 42 paired GPT-5.1 failures.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决工具增强型大语言模型（LLM）智能体在调用API时，无法遵守“观察合同”的问题。研究背景是LLM智能体正被广泛应用于自主完成多步骤任务，它们通过观察中间步骤的输出（如预签名URL、会话令牌、OAuth状态参数）来决定下一步行动。现有方法（如SWE-bench、ToolBench等基准测试）的不足在于，它们只关注任务最终是否成功，而忽视了中间步骤输出的约束性。这些中间输出实际上是外部系统施加的“观察合同”，其使用受限于两个正交的约束：时间有效性（如令牌过期）和字节级完整性（如URL签名被篡改）。当前基准测试未能联合评估这两类约束，导致智能体在实际部署中常因使用过期令牌、截断或修改字节等错误而破坏整个工作流。本文要解决的核心问题是：如何系统性地测量和诊断LLM智能体在任务执行过程中，能否同时保证中间观测结果的时间有效性和字节级完整性。为此，论文提出了ContractBench基准，包含33个双轴任务，通过虚拟时钟和SHA-256哈希进行确定性评估，以填补现有评估体系的空白。

### Q2: 有哪些相关研究？

根据论文内容，相关研究可分为以下类别：

**评测类**：现有Agent基准测试主要评估任务完成能力（如网页导航、软件问题解决、工具使用等），但均不测试Agent是否保留工具返回的工件（artifacts）。最接近的工作是TicToc，它识别了"时间盲点"（重新调用工具时缓存信息过期的失败）。本文的创新在于两点：测试主动时间规划（按截止时间重排序）而非仅被动检测过时性，并新增了正交的完整性维度。

**能力涌现与逆缩放**：先前研究观察到某些能力在特定模型规模下会突然涌现（而非渐进提升），以及逆缩放现象（更大模型表现更差）。本文的发现对两类文献均有贡献：能力悬崖（4B模型0%→27B模型76.5%）展示了涌现性；而API速率限制耐心测试中（更强模型因激进重试得分更低）展示了Agent设置下的逆缩放。

**迭代精炼与自我修正**：Reflexion和Self-Refine方法使用模型自身言语自我批评作为纠正信号重试失败片段。本文的预测有效性实验用确定性、服务端生成的失败标签替换自我批评，并添加错误标签对照控制以隔离标签内容作为操作变量，同时本文的失败分类体系本身也可作为Agent强化学习的自然过程奖励信号。

**上下文窗口保真度**：先前工作表明LLM在长上下文中间位置会丢失信息（"丢失中间"）。本文的完整性维度直接在Agent设置中测试该现象：通过上下文窗口的不透明工件（预签名URL、HMAC签名）可能被截断、重新编码或重排序，产生完整性失败。

### Q3: 论文如何解决这个问题？

ContractBench通过构建一个双轴任务基准来评估LLM代理对观察契约的合规能力。整体框架包含33个任务，每个任务都由四个文件构成：TOML元数据头（固定难度、双轴类别和时间预算）、Markdown指令（提供给代理）、FastAPI服务器（在虚拟时钟下运行，每个HTTP请求输出确定性失败标签）和pytest验证器（消费请求日志并计算奖励）。代理仅能看到指令和服务器的HTTP响应，元数据和验证器被隐藏，消除了测试集泄露和LLM评判歧义。

核心方法采用双轴任务设计，基于两个正交维度：有效性（时效性，如TTL过期）和完整性（字节级，如哈希匹配），分为四个象限（Q1-Q4），其中Q4（同时强调两个轴）包含24个任务，反映真实场景中既有时间限制又有签名绑定的工件普遍性。关键技术包括：1）13个标签的失败分类法（4个有效性+9个完整性+2个元标签），每个标签对应真实API规范文档；2）虚拟时钟控制时间，SHA-256哈希验证字节完整性；3）确定性评估协议，无LLM评判或人类评分员；4）种子化生成确保可重现性。

主要创新点包括：1）首次系统评估观察契约合规这一涌现但易回归的能力；2）发现模型之间存在能力悬崖（如Qwen 3.5从4B的0%到9B的56.6%），关键差异在于轨迹中期的约束而非工具调用能力；3）揭示了非单调缩放（如GPT-5系列中，agentic后训练可能通过谄媚驱动回归损害合规性）；4）验证了失败分类可作为上下文奖励信号（在GPT-5.1上提升+7.1个百分点）。

### Q4: 论文做了哪些实验？

论文在ContractBench基准上进行了全面实验，包含33个双轴任务，使用虚拟时钟控制时间、SHA-256哈希验证字节完整性，并依据真实API规范对失败分类。实验设置：38个模型变体，覆盖Claude、GPT-5系列、Gemini 2.5等前沿闭源模型，Qwen 3.5/2.5、MiniMax、Mistral、Gemma、Llama、DeepSeek-R1等开源模型，以及Base和Instruct版本，每个模型执行99个episode（33任务×3 rollout），温度0，600秒超时。主要结果：（i）无模型突破80%，Claude Opus 4.6以77.8%领先；（ii）Qwen 3.5系列出现能力陡坡：4B为0%，9B跃升至56.6%，397B达70.7%，陡坡源于中途轨迹约束能力而非工具调用能力；（iii）GPT-5系列呈非单调V形变化：GPT-5（70.7%）→GPT-5.1（48.5%）→GPT-5.2（74.8%），回归集中在字节完整性轴；（iv）失败标签可作为上下文奖励信号：在GPT-5.1的42个失败案例中，正确标签提示比错误标签提示提升7.1个百分点。关键数据：Qwen 3.5-9B（56.6%）、Qwen 2.5-72B（23.2%）、Llama-3.3-70B（7.1%），基座模型无一达标，表明合约遵循是后训练能力。

### Q5: 有什么可以进一步探索的点？

根据论文的分析，ContractBench揭示了观察契约合规性是一个尚未被充分解决的难题，存在多个值得深入探索的方向。首先，论文主要聚焦于静态的、预设的时间窗口和字节完整性约束，未来可以研究动态契约，例如观察契约的约束条件本身会随外部系统状态（如服务器负载、权限变更）实时变化，这要求LLM Agent具备更复杂的动态监测与自适应能力。其次，目前的评估任务基于单一API调用，而现实世界中的复杂工作流往往涉及多步API链，其中前一步的输出契约会影响后续步骤的可用性，因此需要构建多步骤、有依赖关系的契约合规性基准。此外，论文中提到的“共情导致的回归”现象值得深究，可以探索如何通过对抗训练或契约感知的强化学习来抑制模型因迎合用户而违反契约的行为。最后，将失败标签作为上下文奖励信号在文中仅初步验证，未来可将其整合到更精细化的在线学习框架中，结合主动查询外部系统状态来动态调整Agent的行为策略。

### Q6: 总结一下论文的主要内容

ContractBench提出并形式化了“观测契约”（observation contracts）概念——即工具调用返回的中间产出物（如预签名URL、会话令牌、OAuth状态参数）受外部系统约束，必须保持时间有效性和字节级完整性。现有基准未联合评估这两种正交的失败模式。为此，作者构建了包含33个双轴任务的确定性基准：虚拟时钟控制时间、SHA-256哈希验证字节完整性，并定义了8个契约域、15种故障标签。对38个模型的评估得出四个主要结论：（1）最佳模型Claude-Opus-4.6仅达77.8%，前沿模型仍无法可靠遵守观测契约；（2）Qwen 3.5系列内部存在陡峭能力悬崖（4B模型0% vs 9B模型56.6%），突破关键并非工具调用能力，而是中间轨迹的约束保持；（3）GPT-5系列性能非单调缩放，后训练可能因迎合行为而侵蚀合规性；（4）故障标签可作为上下文奖励信号，提升GPT-5.1性能7.1个百分点。该工作揭示观测契约合规是新兴的、易退化的能力，为LLM智能体可靠性评估开辟了新维度。
