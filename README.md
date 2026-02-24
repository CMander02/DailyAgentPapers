# DailyAgentPapers

每日 Arxiv Agent 论文自动摘要 | Daily Arxiv Agent Paper Summaries

---

## 📋 最新论文 | 2026-02-23

共收录 **36** 篇 Agent 相关论文

### [OpenClaw, Moltbook, and ClawdLab: From Agent-Only Social Networks to Autonomous Scientific Research](https://arxiv.org/abs/2602.19810)

**评分: 9.5/10** | `多智能体系统` `自主科学研究` `Agent架构` `社会网络` `设计科学`

> 本论文首先对2026年初迅速崛起的开源Agent框架OpenClaw及其衍生的纯AI社交网络Moltbook生态系统进行了开创性的多声部文献综述，系统揭示了该生态在催生大规模AI-AI交互数据、涌现集体行为的同时，也暴露了严重的安全漏洞、不可靠的社交评估机制以及缺乏科学认知结构等五大架构失败模式。基于此分析，论文的核心贡献是提出了ClawdLab——一个作为“设计科学”响应的全新自主科学研究平台。...

📄 [详细解读](data/2026/02/23/openclaw-moltbook-and-clawdlab-from-agent-only-social-networks-to-autonomous-sci.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19810v1)

---

### [Agentic AI for Scalable and Robust Optical Systems Control](https://arxiv.org/abs/2602.20144)

**评分: 9.0/10** | `Agent 架构` `工具使用` `多智能体系统` `Agent 评测/基准` `自主控制`

> 这篇论文提出了一个名为AgentOptics的智能体AI框架，用于实现高保真、自主的光学系统控制。其核心贡献在于构建了一个基于模型上下文协议（MCP）的框架，通过结构化的工具抽象层，将自然语言任务解析并转换为对异构光学设备的标准化控制动作。研究团队为8种代表性光学设备实现了64个标准化MCP工具，并创建了一个包含410个任务的基准测试，以全面评估系统在指令理解、角色感知响应、多步协调、语言变化鲁棒...

📄 [详细解读](data/2026/02/23/agentic-ai-for-scalable-and-robust-optical-systems-control.md) | 📎 [PDF](https://arxiv.org/pdf/2602.20144v1)

---

### [Descent-Guided Policy Gradient for Scalable Cooperative Multi-Agent Learning](https://arxiv.org/abs/2602.20078)

**评分: 9.0/10** | `多智能体系统` `强化学习` `策略梯度` `可扩展性` `合作学习`

> 这篇论文针对大规模多智能体强化学习（MARL）中因智能体间动作相互干扰导致的梯度噪声和样本复杂度随智能体数量线性增长（O(N)）的核心问题，提出了“下降引导策略梯度”（DG-PG）框架。其核心贡献在于，利用许多实际系统（如云计算、交通）已有的可微分分析模型，为每个智能体构造出无噪声的“引导梯度”。这种方法将单个智能体的梯度估计与其他智能体的动作解耦，从而将梯度方差从Θ(N)降至O(1)，并实现了与...

📄 [详细解读](data/2026/02/23/descent-guided-policy-gradient-for-scalable-cooperative-multi-agent-learning.md) | 📎 [PDF](https://arxiv.org/pdf/2602.20078v1)

---

### [The LLMbda Calculus: AI Agents, Conversations, and Information Flow](https://arxiv.org/abs/2602.20064)

**评分: 9.0/10** | `Agent 架构` `Agent 安全` `形式化方法` `信息流控制` `编程语言理论`

> 这篇论文的核心贡献是提出了“LLMbda演算”——一个形式化的计算模型，用于为基于大语言模型（LLM）的AI智能体系统建立严格的理论基础。论文指出，当前AI智能体（如自动规划循环）将LLM调用、工具使用和代码执行紧密耦合，形成了一个新的、未被充分理解的安全攻击面（如提示注入攻击）。为了系统性地分析和保障这类系统的安全性，作者设计了一个未类型化、按值调用的λ演算，并扩展了动态信息流控制原语以及用于构...

📄 [详细解读](data/2026/02/23/the-llmbda-calculus-ai-agents-conversations-and-information-flow.md) | 📎 [PDF](https://arxiv.org/pdf/2602.20064v1)

---

### [CodeCompass: Navigating the Navigation Paradox in Agentic Code Intelligence](https://arxiv.org/abs/2602.20048)

**评分: 9.0/10** | `Agent 架构` `工具使用` `Agent 评测/基准` `代码智能体` `导航悖论`

> 这篇论文的核心贡献是提出了“导航悖论”，并开发了CodeCompass工具来解决智能代码代理在大型代码库中的导航问题。研究发现，随着LLM上下文窗口的扩大，代理的失败模式从检索容量不足转变为导航显著性不足。论文通过258次实验证明，基于图结构的导航工具在处理隐藏依赖任务时，能将任务完成率提升至99.4%，比传统代理和BM25检索分别高出23.2和21.2个百分点。然而，研究也揭示了一个关键瓶颈：代...

📄 [详细解读](data/2026/02/23/codecompass-navigating-the-navigation-paradox-in-agentic-code-intelligence.md) | 📎 [PDF](https://arxiv.org/pdf/2602.20048v1)

---

### [Agents of Chaos](https://arxiv.org/abs/2602.20021)

**评分: 9.0/10** | `Agent 安全` `Agent 评测/基准` `Agent 架构` `多智能体系统` `工具使用`

> 这篇论文通过一项为期两周的“红队”实验，实证研究了在接近真实部署环境中（具备持久记忆、邮件、Discord、文件系统和shell执行权限）的自主语言模型智能体所暴露出的安全与治理风险。核心贡献在于，它超越了传统孤立任务评估，首次系统性地揭示了当LLM与自主性、工具使用及多方通信结合时，在复杂社会技术环境中涌现的新型故障模式。论文通过11个代表性案例，具体记录了智能体出现的非所有者合规、敏感信息泄露...

📄 [详细解读](data/2026/02/23/agents-of-chaos.md) | 📎 [PDF](https://arxiv.org/pdf/2602.20021v1)

---

### [SkillOrchestra: Learning to Route Agents via Skill Transfer](https://arxiv.org/abs/2602.19672)

**评分: 9.0/10** | `Agent 架构` `多智能体系统` `Agent 规划/推理` `Agent 评测/基准` `强化学习`

> 这篇论文提出了SkillOrchestra框架，旨在解决复合AI系统中智能体协同调度的核心挑战。现有方法存在两大局限：一是基于输入的路由器仅做粗粒度的查询级决策，无法适应多轮交互中动态变化的任务需求；二是基于强化学习的调度器训练成本高昂且易陷入“路由崩溃”，即反复调用单一强大但昂贵的选项。

SkillOrchestra的核心贡献在于引入了“技能感知”的调度新范式。它不直接端到端学习路由策略，而是...

📄 [详细解读](data/2026/02/23/skillorchestra-learning-to-route-agents-via-skill-transfer.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19672v1)

---

### [Compositional Planning with Jumpy World Models](https://arxiv.org/abs/2602.19634)

**评分: 9.0/10** | `强化学习` `世界模型` `分层规划` `策略组合` `长时程预测`

> 这篇论文提出了一种名为“跳跃世界模型”的创新方法，用于实现智能体对预训练技能的策略组合规划，以解决复杂的长时程任务。其核心贡献在于：1) 提出学习能够预测预训练策略在多时间尺度上诱导的状态占用分布的生成模型；2) 引入了一个新颖的跨时间尺度一致性目标，显著提升了长时程动态预测的准确性和连贯性，这是实现可靠组合规划的关键；3) 展示了如何利用这些预测模型来估计任意策略序列的价值，从而支持零样本的组合...

📄 [详细解读](data/2026/02/23/compositional-planning-with-jumpy-world-models.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19634v1)

---

### [TAPE: Tool-Guided Adaptive Planning and Constrained Execution in Language Model Agents](https://arxiv.org/abs/2602.19633)

**评分: 9.0/10** | `Agent 架构` `工具使用` `规划` `约束执行` `自适应重规划`

> 这篇论文提出了TAPE框架，旨在解决语言模型智能体在严格约束环境中因规划不完善和执行随机性而容易失败的问题。其核心贡献在于通过工具引导的自适应规划和约束执行来提升智能体的鲁棒性。具体来说，TAPE首先通过聚合多个初始规划构建规划图，并利用外部求解器寻找可行路径，从而增强规划能力。在执行阶段，它采用约束解码来减少采样噪声，并在环境反馈偏离预期状态时进行自适应重规划。实验表明，TAPE在多个基准测试中...

📄 [详细解读](data/2026/02/23/tape-tool-guided-adaptive-planning-and-constrained-execution-in-language-model-a.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19633v1)

---

### [How to Train Your Deep Research Agent? Prompt, Reward, and Policy Optimization in Search-R1](https://arxiv.org/abs/2602.19526)

**评分: 9.0/10** | `Agent 架构` `Agentic 强化学习` `工具使用` `Agent 评测/基准` `多轮检索`

> 这篇论文对深度研究智能体（Deep Research Agent）中的强化学习应用进行了首次系统性研究。核心贡献在于从三个解耦维度（提示模板、奖励函数和策略优化方法）深入剖析了RL训练的关键设置如何影响智能体的性能、稳定性和推理成本。

研究发现：1）相比先前工作使用的“慢思考”模板，“快思考”模板能带来更好的稳定性和性能；2）基于F1的奖励函数会因答案回避导致训练崩溃，表现不如精确匹配奖励，但通...

📄 [详细解读](data/2026/02/23/how-to-train-your-deep-research-agent-prompt-reward-and-policy-optimization-in-s.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19526v1)

---

### [OptiRepair: Closed-Loop Diagnosis and Repair of Supply Chain Optimization Models with LLM Agents](https://arxiv.org/abs/2602.19439)

**评分: 9.0/10** | `Agent 架构` `工具使用` `规划与推理` `LLM 微调` `领域特定 Agent`

> OptiRepair 提出了一种由LLM智能体驱动的闭环诊断与修复框架，用于解决供应链优化模型因建模错误而导致的不可行问题。其核心贡献在于将复杂的修复任务分解为两个阶段：第一阶段是领域无关的可行性修复，利用迭代的不可行约束集（IIS）引导LLM修复任何线性规划模型；第二阶段是领域特定的验证，基于库存理论设计了五项可验证的合理性检查，确保修复方案在操作上合理。通过在一个包含976个多级供应链问题的测...

📄 [详细解读](data/2026/02/23/optirepair-closed-loop-diagnosis-and-repair-of-supply-chain-optimization-models.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19439v1)

---

### [To Move or Not to Move: Constraint-based Planning Enables Zero-Shot Generalization for Interactive Navigation](https://arxiv.org/abs/2602.20055)

**评分: 8.5/10** | `Agent 架构` `规划` `工具使用` `具身智能` `场景理解`

> 这篇论文提出了“终身交互式导航”新问题，解决传统视觉导航中因杂物堵塞而无可行路径的挑战。其核心贡献是设计了一个基于约束规划的LLM驱动框架，使机器人能主动移动障碍物、开辟路径以完成顺序物体放置任务。该框架的关键在于让大语言模型基于结构化场景图进行推理，动态决策移动哪个物体、放置何处以及下一步探查哪里，从而将高层任务规划与主动感知耦合，避免低效的全环境探索。论文在ProcTHOR-10k物理仿真器中...

📄 [详细解读](data/2026/02/23/to-move-or-not-to-move-constraint-based-planning-enables-zero-shot-generalizatio.md) | 📎 [PDF](https://arxiv.org/pdf/2602.20055v1)

---

### [Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks](https://arxiv.org/abs/2602.20156)

**评分: 8.0/10** | `Agent安全` `提示注入攻击` `Agent评测基准` `技能文件` `Agent供应链安全`

> 这篇论文的核心贡献是提出了Skill-Inject基准，用于系统评估LLM智能体对技能文件攻击的脆弱性。论文指出，随着智能体技能（Skill）的普及，第三方代码和指令的引入创造了新的攻击面，即“基于技能的提示注入攻击”。与传统的提示注入不同，这种攻击发生在完全由指令构成的技能文件中，使得区分恶意与合法指令变得极为困难，因为许多指令具有“双重用途”，其危害性高度依赖于任务上下文。

Skill-In...

📄 [详细解读](data/2026/02/23/skill-inject-measuring-agent-vulnerability-to-skill-file-attacks.md) | 📎 [PDF](https://arxiv.org/pdf/2602.20156v1)

---

### [Interaction Theater: A case of LLM Agents Interacting at Scale](https://arxiv.org/abs/2602.20059)

**评分: 8.0/10** | `多智能体系统` `Agent 评测/基准` `Agent 交互分析` `LLM-as-Judge` `大规模实证研究`

> 这篇论文通过分析AI社交平台Moltbook上大规模LLM智能体间的互动数据，揭示了当前多智能体交互存在的“表演性”问题。核心发现是：尽管智能体能生成多样且形式良好的文本，营造出活跃讨论的表象，但实质性的信息交换严重缺失。具体表现为，65%的评论与对应帖子缺乏独特的共享词汇，信息增益随评论数增加迅速衰减，且多数评论被判定为垃圾或无关内容。此外，智能体极少进行线程式对话（仅占5%），主要进行独立的并...

📄 [详细解读](data/2026/02/23/interaction-theater-a-case-of-llm-agents-interacting-at-scale.md) | 📎 [PDF](https://arxiv.org/pdf/2602.20059v1)

---

### [AgenticSum: An Agentic Inference-Time Framework for Faithful Clinical Text Summarization](https://arxiv.org/abs/2602.20040)

**评分: 8.0/10** | `Agent 架构` `工具使用` `Agentic 推理` `医疗应用` `文本摘要`

> 这篇论文提出了AgenticSum，一个用于临床文本摘要的智能体推理框架，旨在解决大语言模型在生成临床摘要时容易产生事实性错误（幻觉）的难题。其核心贡献在于将摘要任务分解为四个协调的智能体阶段：首先选择并压缩任务相关上下文，然后生成初始草稿，接着利用模型内部注意力信号识别草稿中证据薄弱的部分，最后在监督控制下有选择地修正这些被标记的内容。这种结构化的“选择-生成-验证-修正”流程，无需额外训练，仅...

📄 [详细解读](data/2026/02/23/agenticsum-an-agentic-inference-time-framework-for-faithful-clinical-text-summar.md) | 📎 [PDF](https://arxiv.org/pdf/2602.20040v1)

---

### [MAS-FIRE: Fault Injection and Reliability Evaluation for LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2602.19843)

**评分: 8.0/10** | `多智能体系统` `可靠性评估` `故障注入` `系统鲁棒性` `Agent评测`

> 这篇论文提出了MAS-FIRE框架，专门用于评估基于大语言模型的多智能体系统的可靠性。其核心贡献在于首次系统性地定义了多智能体系统中可能发生的15种故障类型（涵盖智能体内部认知错误和智能体间协调故障），并设计了三种非侵入式的故障注入方法（提示修改、响应重写和消息路由操控）来模拟这些故障。通过将该框架应用于三种典型的多智能体架构，研究发现系统的容错行为可分为机制、规则、提示和推理四个层级，这为细粒度...

📄 [详细解读](data/2026/02/23/mas-fire-fault-injection-and-reliability-evaluation-for-llm-based-multi-agent-sy.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19843v1)

---

### [Agentic AI as a Cybersecurity Attack Surface: Threats, Exploits, and Defenses in Runtime Supply Chains](https://arxiv.org/abs/2602.19555)

**评分: 8.0/10** | `Agent安全` `Agent架构` `Agent评测/基准` `工具使用` `多智能体系统`

> 这篇论文系统性地分析了基于大语言模型的智能体系统在运行时面临的新型网络安全威胁。核心贡献在于提出了“动态智能体运行时供应链”框架，将攻击面从传统的构建时依赖转移到运行时的数据与工具依赖。论文将威胁系统化分类为数据供应链攻击（如瞬时上下文注入和持久性记忆污染）和工具供应链攻击（涉及工具发现、实现和调用环节），并首次识别出“病毒式智能体循环”风险，即智能体可在无代码漏洞的情况下成为自我传播生成式蠕虫的...

📄 [详细解读](data/2026/02/23/agentic-ai-as-a-cybersecurity-attack-surface-threats-exploits-and-defenses-in-ru.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19555v1)

---

### [Human-Guided Agentic AI for Multimodal Clinical Prediction: Lessons from the AgentDS Healthcare Benchmark](https://arxiv.org/abs/2602.19502)

**评分: 8.0/10** | `Agentic AI` `多模态` `临床预测` `人机协作` `基准评测`

> 该论文的核心贡献在于提出并验证了一种“人机协同”的智能体AI工作流，用于解决多模态临床预测任务。研究通过在AgentDS医疗基准的三个挑战任务（30天再入院预测、急诊费用预测和出院准备评估）中引入人类专家的关键性指导，显著提升了模型性能。研究发现，人类在三个环节的介入至关重要：基于临床知识的跨模态特征工程、针对具体任务的数据整合策略选择，以及构建具有临床合理性的模型集成方案。消融实验表明，人类指导...

📄 [详细解读](data/2026/02/23/human-guided-agentic-ai-for-multimodal-clinical-prediction-lessons-from-the-agen.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19502v1)

---

### [Assessing Risks of Large Language Models in Mental Health Support: A Framework for Automated Clinical AI Red Teaming](https://arxiv.org/abs/2602.19948)

**评分: 7.5/10** | `Agent 评测/基准` `Agent 安全` `多智能体系统` `模拟环境` `AI 安全`

> 这篇论文提出了一个创新的评估框架，用于系统性检测大型语言模型在心理健康支持应用中潜在的、复杂的临床风险。其核心贡献在于构建了一个自动化“临床红队测试”系统，该系统通过让AI心理治疗师与配备动态认知情感模型的模拟患者智能体进行多轮对话，并在一个全面的护理质量与风险本体论下评估治疗会话。研究以酒精使用障碍为高影响力测试案例，评估了包括ChatGPT在内的六个AI代理，揭示了严重的安全漏洞，如可能加剧患...

📄 [详细解读](data/2026/02/23/assessing-risks-of-large-language-models-in-mental-health-support-a-framework-fo.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19948v1)

---

### [SAMAS: A Spectrum-Guided Multi-Agent System for Achieving Style Fidelity in Literary Translation](https://arxiv.org/abs/2602.19840)

**评分: 7.5/10** | `多智能体系统` `LLM应用` `Agent架构` `翻译` `风格控制`

> 这篇论文针对文学翻译中难以保持作者独特文风的难题，提出了一个创新框架SAMAS（风格自适应多智能体系统）。其核心贡献在于将风格保真度问题重新定义为信号处理任务：首先，利用小波包变换将文学风格量化为一个“风格特征谱”信号；然后，此信号作为动态控制信号，根据源文本的结构模式，实时组装并调度由多个专业化翻译智能体构成的定制化工作流程。实验表明，SAMAS在保持竞争力的语义准确度基础上，在风格保真度上显著...

📄 [详细解读](data/2026/02/23/samas-a-spectrum-guided-multi-agent-system-for-achieving-style-fidelity-in-liter.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19840v1)

---

### [Representation Stability in a Minimal Continual Learning Agent](https://arxiv.org/abs/2602.19655)

**评分: 7.5/10** | `Continual Learning` `Agent Architecture` `Representation Learning` `Stability-Plasticity Dilemma` `Minimal Agent`

> 这篇论文提出了一种极简的持续学习智能体，其核心贡献在于剥离了复杂的架构和优化目标，专注于研究内部表征随时间的动态演化。该智能体通过在多次执行中维护一个持久的状态向量，并随着新文本数据的引入进行增量更新，从而将学习过程本身视为一种状态积累与演化的现象。

研究通过量化连续归一化状态向量之间的余弦相似度，定义了表征稳定性指标。纵向实验表明，在一致的输入下，系统会从初始的“可塑性”阶段过渡到稳定的“表征...

📄 [详细解读](data/2026/02/23/representation-stability-in-a-minimal-continual-learning-agent.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19655v1)

---

### [ISO-Bench: Can Coding Agents Optimize Real-World Inference Workloads?](https://arxiv.org/abs/2602.19594)

**评分: 7.5/10** | `Agent Benchmark` `Coding Agent` `Inference Optimization` `LLM Serving` `Evaluation Metrics`

> 这篇论文提出了ISO-Bench，一个专门用于评估代码智能体在真实世界推理优化任务中能力的基准测试。其核心贡献在于填补了现有评测的空白，将评估场景从传统的算法题或代码补全，转向了从主流LLM服务框架（vLLM和SGLang）的实际合并请求中提取的、具有明确性能提升目标的复杂优化任务。论文强调，仅依赖运行时指标的评测可能被“欺骗”，因此创新性地结合了基于执行的“硬指标”和基于LLM评估的“软指标”，...

📄 [详细解读](data/2026/02/23/iso-bench-can-coding-agents-optimize-real-world-inference-workloads.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19594v1)

---

### [Cost-Aware Diffusion Active Search](https://arxiv.org/abs/2602.19538)

**评分: 7.5/10** | `主动搜索` `多智能体系统` `决策规划` `扩散模型` `强化学习`

> 这篇论文提出了一种名为“成本感知扩散主动搜索”（CDAS）的新方法，用于解决自主智能体在未知环境中进行主动搜索时的探索-利用权衡问题。核心贡献在于利用扩散模型的序列建模能力，直接生成前瞻性的动作序列，从而避免了传统树搜索算法（如蒙特卡洛树搜索）因构建和更新搜索树而带来的高昂计算成本。论文指出，此前基于扩散模型的强化学习方法在主动搜索场景中可能存在“乐观偏差”，并针对单智能体和多智能体团队提出了缓解...

📄 [详细解读](data/2026/02/23/cost-aware-diffusion-active-search.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19538v1)

---

### [Ada-RS: Adaptive Rejection Sampling for Selective Thinking](https://arxiv.org/abs/2602.19519)

**评分: 7.5/10** | `Agent 推理` `Agent 效率优化` `选择性思考` `工具使用` `拒绝采样`

> 这篇论文针对成本与延迟敏感场景下大语言模型（LLM）的推理效率问题，提出了**自适应拒绝采样（Ada-RS）**框架。其核心贡献在于，通过一种与具体优化算法无关的样本过滤机制，引导模型学会“选择性思考”——即仅在复杂任务上进行显式推理（如思维链），而对简单请求则直接输出答案，从而避免不必要的令牌消耗。

Ada-RS 的工作原理是：对于给定上下文，模型生成多个候选完成序列，并使用一个结合了效果与长...

📄 [详细解读](data/2026/02/23/ada-rs-adaptive-rejection-sampling-for-selective-thinking.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19519v1)

---

### [Pyramid MoA: A Probabilistic Framework for Cost-Optimized Anytime Inference](https://arxiv.org/abs/2602.19509)

**评分: 7.5/10** | `Agent 架构` `成本优化` `动态路由` `模型集成` `推理系统`

> 这篇论文提出了Pyramid MoA，一种用于大语言模型（LLM）成本优化推理的概率框架。其核心贡献在于设计了一个分层混合智能体架构，旨在以显著降低的计算成本逼近大型“Oracle”模型的性能。

该框架的核心是一个轻量级的路由器，它管理一组小型、成本效益高的模型（如8B参数）。路由器通过评估这些小型模型集合在特定查询上的语义一致性和校准后的置信度，来动态识别“困难”问题。只有当问题被判定为足够困...

📄 [详细解读](data/2026/02/23/pyramid-moa-a-probabilistic-framework-for-cost-optimized-anytime-inference.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19509v1)

---

### [ComplLLM: Fine-tuning LLMs to Discover Complementary Signals for Decision-making](https://arxiv.org/abs/2602.19458)

**评分: 7.5/10** | `多智能体系统` `LLM微调` `决策辅助` `决策理论` `奖励设计`

> 这篇论文提出了ComplLLM框架，旨在通过微调大语言模型（LLM）来发现决策中的互补信号。其核心贡献在于将决策理论融入LLM的后训练过程，将“互补性”本身作为一种奖励信号来优化模型。具体而言，它训练一个决策辅助LLM，使其输出的信号能够与现有智能体（如领域专家）的决策信息形成互补，从而为最终决策者提供独特且增量的信息支持。论文在合成任务和涉及领域专家的真实世界任务上验证了该框架的有效性，表明其不...

📄 [详细解读](data/2026/02/23/complllm-fine-tuning-llms-to-discover-complementary-signals-for-decision-making.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19458v1)

---

### [When AI Teammates Meet Code Review: Collaboration Signals Shaping the Integration of Agent-Authored Pull Requests](https://arxiv.org/abs/2602.19441)

**评分: 7.5/10** | `Agent 评测/基准` `Agent 协作` `软件工程` `实证研究` `代码审查`

> 这篇论文通过分析AIDev数据集中的AI代理提交的GitHub拉取请求，探讨了其在人类主导的代码审查工作流中的集成情况。研究发现，AI拉取请求的集成成功率不仅取决于代码质量，更关键的是其与现有协作规范的契合度。具体而言，审查者的积极参与（如提供可操作的反馈）能显著提升合并概率，而较大的代码变更规模或破坏协作稳定的行为（如强制推送）则会降低集成可能性。相比之下，单纯的迭代次数对集成结果解释力有限。论...

📄 [详细解读](data/2026/02/23/when-ai-teammates-meet-code-review-collaboration-signals-shaping-the-integration.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19441v1)

---

### [Multi-CoLoR: Context-Aware Localization and Reasoning across Multi-Language Codebases](https://arxiv.org/abs/2602.19407)

**评分: 7.5/10** | `Agent` `代码智能体` `代码定位` `多语言代码库` `图推理`

> 这篇论文提出了Multi-CoLoR框架，旨在解决大语言模型在复杂多语言代码库中定位相关代码的难题。其核心贡献在于将组织上下文知识与图结构推理相结合，实现了更精准的代码定位。具体而言，框架分为两个阶段：首先，相似问题上下文模块通过检索语义和组织结构上相关的历史问题来有效缩减搜索空间；其次，一个扩展的代码图遍历智能体在C++和QML等代码库中进行结构推理。该方法的创新点在于超越了现有方法仅关注单语言...

📄 [详细解读](data/2026/02/23/multi-color-context-aware-localization-and-reasoning-across-multi-language-codeb.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19407v1)

---

### [Meta-Learning and Meta-Reinforcement Learning - Tracing the Path towards DeepMind's Adaptive Agent](https://arxiv.org/abs/2602.19837)

**评分: 6.5/10** | `元学习` `元强化学习` `自适应智能体` `综述` `迁移学习`

> 这篇论文是一篇关于元学习和元强化学习的综述，其核心贡献在于提供了一个严谨的、基于任务的形式化框架，用以统一和梳理该领域的发展脉络。论文系统地比较了元学习与标准机器学习、元强化学习与标准强化学习，并明确定义了关键的性能度量指标，弥补了现有文献中数学形式化不足的缺陷。在此基础上，论文以该形式化框架为线索，按时间顺序回顾了从早期元学习算法到DeepMind自适应智能体（ADA）的里程碑式进展，特别是梯度...

📄 [详细解读](data/2026/02/23/meta-learning-and-meta-reinforcement-learning-tracing-the-path-towards-deepminds.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19837v1)

---

### [Botson: An Accessible and Low-Cost Platform for Social Robotics Research](https://arxiv.org/abs/2602.19491)

**评分: 6.5/10** | `Social Robotics` `LLM-Powered Agent` `Human-AI Interaction` `Embodied AI` `Trust in AI`

> Botson论文的核心贡献是设计并实现了一个低成本、易获取的仿人社交机器人平台，旨在推动社交机器人研究。该平台通过集成大语言模型，使机器人能够进行自然对话，并特别强调利用实体形态和拟人化设计来传达非语言社交线索，以解决当前AI（如语音助手）因缺乏实体表现而难以建立用户信任的关键问题。其意义在于降低了社交机器人研究的门槛，使更多研究者能够进行涉及人机交互、信任建立等领域的实验，为探索具身智能如何通过...

📄 [详细解读](data/2026/02/23/botson-an-accessible-and-low-cost-platform-for-social-robotics-research.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19491v1)

---

### [Advantage-based Temporal Attack in Reinforcement Learning](https://arxiv.org/abs/2602.19582)

**评分: 6.0/10** | `强化学习` `对抗攻击` `时序攻击` `Agent安全` `Transformer`

> 这篇论文提出了一种名为“基于优势的对抗性变换器”（AAT）的新方法，用于生成针对深度强化学习（DRL）智能体的时序相关对抗样本。其核心贡献在于解决了现有基于未来奖励的攻击方法在生成序列扰动时，难以捕捉不同时间步之间依赖关系、导致时序相关性弱的问题。AAT通过两个关键机制实现突破：一是采用多尺度因果自注意力（MSCSA）机制，动态建模历史信息与当前状态之间的依赖，从而增强当前扰动与先前扰动之间的相关...

📄 [详细解读](data/2026/02/23/advantage-based-temporal-attack-in-reinforcement-learning.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19582v1)

---

### [Recurrent Structural Policy Gradient for Partially Observable Mean Field Games](https://arxiv.org/abs/2602.20141)

**评分: 5.5/10** | `Mean Field Games` `强化学习` `部分可观测` `策略梯度` `多智能体系统`

> 这篇论文针对大规模多智能体系统中的部分可观测平均场博弈问题，提出了两项核心贡献。首先，作者引入了**循环结构策略梯度**算法，这是首个适用于具有公共信息（如共享观测历史）的部分可观测平均场博弈场景的混合结构方法。该算法通过利用已知的个体转移动力学，在策略优化中仅对公共噪声进行采样，从而大幅降低了方差，实现了比基于强化学习的方法快一个数量级的收敛速度，并首次解决了包含异质智能体、公共噪声和历史依赖策...

📄 [详细解读](data/2026/02/23/recurrent-structural-policy-gradient-for-partially-observable-mean-field-games.md) | 📎 [PDF](https://arxiv.org/pdf/2602.20141v1)

---

### [Unlocking Multimodal Document Intelligence: From Current Triumphs to Future Frontiers of Visual Document Retrieval](https://arxiv.org/abs/2602.19961)

**评分: 5.5/10** | `多模态大语言模型` `检索增强生成` `Agent系统` `文档智能` `视觉文档检索`

> 这篇论文是首篇针对视觉文档检索（VDR）领域的系统性综述，其核心贡献在于填补了现有研究的空白，首次从多模态大语言模型（MLLM）时代的视角，全面梳理和审视了VDR领域。论文首先明确了VDR与自然图像检索的根本区别，强调了视觉文档在信息模态密度、语义粒度和任务复杂性上的独特性。文章从基准评测和方法论演变两个维度展开分析，将现有技术归纳为三大范式：多模态嵌入模型、多模态重排序模型，以及结合检索增强生成...

📄 [详细解读](data/2026/02/23/unlocking-multimodal-document-intelligence-from-current-triumphs-to-future-front.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19961v1)

---

### [Beyond Mimicry: Toward Lifelong Adaptability in Imitation Learning](https://arxiv.org/abs/2602.19930)

**评分: 5.5/10** | `Imitation Learning` `Agent Adaptability` `Compositional Generalization` `Lifelong Learning` `Behavioral Primitives`

> 这篇论文的核心贡献是批判性地反思了模仿学习的根本局限，并提出了一个全新的研究方向。作者指出，当前模仿学习智能体本质上是“精密的记忆机器”，擅长复现训练数据，但缺乏在环境变化或目标演变时的适应能力。论文认为这一失败源于优化目标的偏差，因此主张将研究重心从追求“完美复现”转向培养“组合适应性”。

论文的意义在于为构建具有终身学习能力的智能体奠定了理论基础。它形式化了目标条件上下文MDP，提出了衡量组...

📄 [详细解读](data/2026/02/23/beyond-mimicry-toward-lifelong-adaptability-in-imitation-learning.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19930v1)

---

### [RAmmStein: Regime Adaptation in Mean-reverting Markets with Stein Thresholds -- Optimal Impulse Control in Concentrated AMMs](https://arxiv.org/abs/2602.19419)

**评分: 5.5/10** | `强化学习` `最优控制` `去中心化金融` `算法交易` `智能体决策`

> 这篇论文提出了一种名为RAmmStein的深度强化学习方法，用于解决去中心化交易所中集中流动性提供的最优控制问题。其核心贡献在于将流动性管理建模为一个脉冲控制问题，并推导出对应的哈密顿-雅可比-贝尔曼拟变分不等式（HJB-QVI）。该方法创新性地将奥恩斯坦-乌伦贝克过程的均值回归速度等市场动态特征作为模型输入，使智能体能够学习区分“行动”与“不行动”的状态空间区域。通过在包含超过680万笔交易的高...

📄 [详细解读](data/2026/02/23/rammstein-regime-adaptation-in-mean-reverting-markets-with-stein-thresholds-opti.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19419v1)

---

### [Effects of Property Recovery Incentives and Social Interaction on Self-Evacuation Decisions in Natural Disasters: An Agent-Based Modelling Approach](https://arxiv.org/abs/2602.19639)

**评分: 4.0/10** | `Agent-Based Modeling` `Multi-Agent Systems` `Evolutionary Game Theory` `Decision-Making` `Social Networks`

> 该论文采用基于智能体的建模（ABM）结合演化博弈论，研究了自然灾害中家庭智能体的自主疏散决策行为。核心贡献在于揭示了政府激励措施与社交网络结构对集体疏散率的复杂交互影响。研究发现，优先向社交连接度高的“社区影响者”提供财产恢复激励能显著提升整体疏散率，而优先连接度低的个体反而可能阻碍疏散进程。同时，激励效果存在阈值效应：超过一定水平后，增加资金或优先对象反而效果递减，且疏散率在特定优先值附近会出现...

📄 [详细解读](data/2026/02/23/effects-of-property-recovery-incentives-and-social-interaction-on-self-evacuatio.md) | 📎 [PDF](https://arxiv.org/pdf/2602.19639v1)

---

## 📅 历史归档

论文按日期归档在 `data/YYYY/MM/DD/` 目录下。

## 🔧 关于

本项目通过 GitHub Actions 每日自动运行，使用 arxiv API 获取论文，
LLM 进行智能筛选和中文摘要生成。

- 数据源: [arxiv.org](https://arxiv.org/)
- 关注领域: AI Agent, Multi-Agent Systems, LLM Agent, Tool Use, Planning, Reasoning
- 更新频率: 每日北京时间 07:00
