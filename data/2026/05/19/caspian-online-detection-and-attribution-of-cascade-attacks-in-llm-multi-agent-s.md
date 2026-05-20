---
title: "CASPIAN: Online Detection and Attribution of Cascade Attacks in LLM Multi-Agent Systems via Cross-Channel Causal Monitoring"
authors:
  - "Kavana Venkatesh"
  - "Jafar Isbarov"
  - "Saad Amin"
  - "Murat Kantarcioglu"
  - "Jiaming Cui"
date: "2026-05-19"
arxiv_id: "2605.19240"
arxiv_url: "https://arxiv.org/abs/2605.19240"
pdf_url: "https://arxiv.org/pdf/2605.19240v1"
github_url: "https://github.com/caspian-detector/caspian"
categories:
  - "cs.MA"
tags:
  - "LLM多智能体系统安全"
  - "级联攻击检测"
  - "因果监控"
  - "跨通道分析"
  - "在线检测与归因"
relevance_score: 9.5
---

# CASPIAN: Online Detection and Attribution of Cascade Attacks in LLM Multi-Agent Systems via Cross-Channel Causal Monitoring

## 原始摘要

Cascade attacks in LLM multi-agent systems (MAS) arise when adversarial influence propagates across agents and leads to escalated system-level failures through complex agent interactions. Detecting such cascades is challenging, as their signals are distributed, tightly coupled across interaction channels, and often appear plausibly benign locally but may unfold quickly either within a single turn or gradually across multiple turns. Existing defenses, being largely local and text-centric, fail to capture such cross-channel, temporally coordinated dynamics of cascade propagation. Therefore, we propose CASPIAN, the first framework that provides a unified, cross-channel causal analysis of cascade behavior in LLM-MAS through online monitoring of dynamic influence propagation across agents. CASPIAN models multi-agent interactions using a unified, dynamic causal influence matrix across channels, estimated efficiently via a late-interaction conditional transfer entropy (LI-CTE) formulation, thereby enabling the detection of cascade onset from emergent system-level structure rather than isolated anomalies. It further performs online causal attribution, identifying the origin, bridge, and amplifier agents driving the cascade and reconstructing its principal propagation pathways, capabilities not supported by existing methods. Across diverse multi-agent frameworks and benchmarks, CASPIAN consistently outperforms semantic guardrails, LLM-based judges, and graph-based anomaly detectors in both detection accuracy and early cascade identification while operating with sub-1% relative overhead latency. These results demonstrate that unified cross-channel causal modeling is essential for reliably detecting and understanding cascade failures in LLM multi-agent systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型多智能体系统（LLM-MAS）中“级联攻击”的在线检测与归因问题。随着LLM被部署到协作式多智能体系统中，系统故障的本质发生了根本性转变：从单智能体系统中孤立的幻觉或提示注入攻击，演变为一种新型的“级联攻击”。在这种攻击中，恶意或错误的影响从一个智能体注入后，会通过智能体间的复杂交互在网络中传播、放大并自我强化，最终导致系统级的灾难性故障。现有防御方法（如语义护栏、基于LLM的裁判模型、图异常检测器）存在显著不足：它们主要局限于单一交互通道（如通信内容）的局部语义检查或静态图分析，无法捕捉级联攻击在多个通道（如通信、记忆、工具、执行）间联合传播的动态耦合特征，也忽视了其时间上的累积效应（可发生于单轮次内或逐步跨轮次）。因此，核心问题在于缺乏一种能够统一、在线地监测跨通道因果影响力传播，并实时检测和定位级联攻击源头、传播路径与关键节点的有效方法。

### Q2: 有哪些相关研究？

相关研究可分为方法类和评测类。评测类工作包括TAMAS、AgentLAB和ACIArena等基准，它们揭示了长程提示注入和级联代理妥协等漏洞，并指出记忆故障、自我复制攻击及跨通道传播是主要挑战。这些工作主要通过攻击结果或局部消息异常来表征级联问题，而CASPIAN则聚焦于在线执行过程中动态的跨通道传播建模。方法类工作涵盖三类防御：语义护栏（如PromptGuard 2、JailGuard）检测消息级恶意内容，困惑度方法识别词元异常；基于LLM的判断器扩展至交互窗口分析，但重心仍在文本；图检测器（如G-Safeguard、GUARDIAN）利用通信拓扑和表征空间信号检测异常。这些方法均局限于局部或文本中心视角。此外，故障归因依赖事后轨迹分析，治理框架仅提供整体监督。CASPIAN的独特贡献在于：首次将传输熵等因果影响估计方法引入LLM多智能体系统，通过跨通道（通信、记忆、工具、执行）统一因果影响矩阵实现在线级联检测与归因，超越了现有方法对静态结构或单通道分析的依赖，并能同时识别源头、桥梁和放大器智能体。

### Q3: 论文如何解决这个问题？

CASPIAN通过统一跨通道因果分析框架解决LLM多智能体系统中的级联攻击检测与归因问题。核心方法是构建一个动态因果影响张量\(\mathcal{A}_t \in \mathbb{R}^{N \times N \times |\mathcal{C}|}\)，该张量在四个交互通道（通信、记忆、工具、执行）上在线估计智能体间的定向因果影响。

关键技术包括：**晚期交互条件转移熵（LI-CTE）** 高效计算通道级影响，通过对源投影和目标投影的条件互信息进行解耦式分解，实现毫秒级开销。**统一因果影响矩阵**将通道级张量聚合并进行度感知归一化，得到\(\tilde{A}_t\)用于谱分析。

检测机制基于三个信号：**放大检测**通过主导谱能量\(E_t = \lambda_1 + \lambda_2\)的增长率\(A_t^{amp}\)识别影响力增长；**结构耦合**通过谱耦合比\(R_t\)和间隙收缩\(\Delta g_t\)区分良性活动与级联的传播结构变化；**跨通道传播**通过归一化熵\(H_t^{norm}\)量化影响力在通道间的分散程度。综合这些信号形成Watch条件，并分别处理**单回合级联**（瞬时检测）和**多回合级联**（基于逆谱间隙的自适应持久窗口）。

**归因模块**在检测触发后直接利用缓存的影响矩阵，无需额外计算。通过**出度最大**识别起源智能体，**出度/入度比最大**识别放大器，**出入度乘积最大**识别桥梁，并提取**拓扑瓶颈最优化**的传播骨干路径及主导通道。

创新点在于首次实现统一的跨通道因果建模，将级联检测从局部文本异常检测升级为全局谱结构分析，并支持在线归因识别三种关键角色与传播路径，同时保持亚1%的延迟开销。

### Q4: 论文做了哪些实验？

CASPIAN在两类基准测试（TAMAS和ACIArena）上进行了评估，涵盖727个场景（169个良性、558个攻击），生成2908条框架特定轨迹。攻击分为三类：意图操纵（语义漂移）、执行攻击（工具/内存传播）和协调攻击（多智能体同步失效）。实验在AutoGen、CrewAI、MetaGPT和LLM Debate四种MAS框架上进行，使用GPT-5.4作为基础模型。对比基线包括三类：语义护栏（PromptGuard 2等）、基于LLM的裁判（单轮/滑动窗口/全轨迹）和图检测器（G-Safeguard、BlindGuard、GUARDIAN）。关键指标：级联检测使用AUROC、TPR@5%FPR和EDR@5（5轮内早期检测率）；归因使用Acc@1、MRR等。主要结果：CASPIAN在所有设置中AUROC均超过0.9，在AutoGen上EDR@5最高达0.831。对比基线中，语义护栏性能最差（PromptGuard 2的TPR@5%仅0.284），LLM裁判滑动窗口（W=10）TPR@5%为0.612，图检测器BlindGuard最优（TPR@5%=0.645），而CASPIAN在AutoGen上TPR@5%达0.868、EDR@5=0.792、AUROC=0.942，显著优于所有基线。

### Q5: 有什么可以进一步探索的点？

基于论文，CASPIAN虽在在线监测方面表现优异，但其局限性与未来探索方向值得深入分析。**局限性**：首先，该框架依赖“条件转移熵”进行因果推断，但高维动态系统中可能存在长程依赖与非平稳性，导致因果估计偏差，尤其当桥接或放大智能体行为呈现“稀疏触发”特征时，在线监测可能遗漏慢传播或间歇性干扰的级联信号。其次，当前方法假设跨通道交互结构是时不变的，但真实多智能体系统中通信模式可能随任务或敌方诱导动态重构，导致因果矩阵更新滞后。**未来探索**：可引入**时序图注意力网络**或**元学习**，自动捕获跨信道交互的异构时变拓扑，以自适应识别新型攻击模式。同时，研究**对抗性因果混淆**：攻击者可设计局部良性但全局耦合的样本以绕过传递熵检测，需结合语义反常模式（如隐蔽编码）形成多模态因果图。最后，应探索**极低延迟因果图蒸馏**，使检测开销在100智能体以上场景仍保持亚毫秒级实时响应。

### Q6: 总结一下论文的主要内容

CASPIAN解决了LLM多智能体系统中级联攻击的在线检测与归因问题。级联攻击通过跨智能体的互动传播敌对影响，导致系统性故障，其信号分布且跨通道耦合，难以被局部检测。CASPIAN提出首个统一框架，通过在线监测跨通道（通信、记忆、工具和执行）的因果影响传播来检测级联。它利用延迟交互条件传递熵（LI-CTE）高效构建动态因果影响矩阵，通过频谱分析跟踪影响拓扑的演化（如放大、同步、跨通道传播和持久性），从而检测级联的起始，无需攻击模板或离线训练。检测后，它还能在线归因，识别出级联的起源、桥梁和放大器智能体，并重建主要传播路径。实验表明，CASPIAN在多种多智能体框架和基准上，在检测准确率和早期识别方面优于语义护栏、基于LLM的评判和图异常检测器，且相对延迟开销低于1%。核心贡献在于将级联检测从局部语义检查转向全局传播动力学建模，证明了跨通道因果建模对可靠检测和理解级联故障的必要性。
