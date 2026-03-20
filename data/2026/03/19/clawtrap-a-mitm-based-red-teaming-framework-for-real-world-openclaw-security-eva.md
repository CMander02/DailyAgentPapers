---
title: "ClawTrap: A MITM-Based Red-Teaming Framework for Real-World OpenClaw Security Evaluation"
authors:
  - "Haochen Zhao"
  - "Shaoyang Cui"
date: "2026-03-19"
arxiv_id: "2603.18762"
arxiv_url: "https://arxiv.org/abs/2603.18762"
pdf_url: "https://arxiv.org/pdf/2603.18762v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Web Agent"
  - "Security"
  - "Red Teaming"
  - "Evaluation"
  - "Network-layer Attack"
  - "MITM"
  - "Agent Robustness"
relevance_score: 7.5
---

# ClawTrap: A MITM-Based Red-Teaming Framework for Real-World OpenClaw Security Evaluation

## 原始摘要

Autonomous web agents such as \textbf{OpenClaw} are rapidly moving into high-impact real-world workflows, but their security robustness under live network threats remains insufficiently evaluated. Existing benchmarks mainly focus on static sandbox settings and content-level prompt attacks, which leaves a practical gap for network-layer security testing. In this paper, we present \textbf{ClawTrap}, a \textbf{MITM-based red-teaming framework for real-world OpenClaw security evaluation}. ClawTrap supports diverse and customizable attack forms, including \textit{Static HTML Replacement}, \textit{Iframe Popup Injection}, and \textit{Dynamic Content Modification}, and provides a reproducible pipeline for rule-driven interception, transformation, and auditing. This design lays the foundation for future research to construct richer, customizable MITM attacks and to perform systematic security testing across agent frameworks and model backbones. Our empirical study shows clear model stratification: weaker models are more likely to trust tampered observations and produce unsafe outputs, while stronger models demonstrate better anomaly attribution and safer fallback strategies. These findings indicate that reliable OpenClaw security evaluation should explicitly incorporate dynamic real-world MITM conditions rather than relying only on static sandbox protocols.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决自主网络代理（特别是OpenClaw）在真实网络环境中面临的安全评估不足问题。随着以OpenClaw为代表的大规模自主网络代理平台被广泛部署到高影响力的现实工作流中，其安全鲁棒性已成为实际应用的关键前提。然而，现有研究存在明显局限：当前的安全评估基准（如Zhan、Evtimov、Wu等人的工作）主要集中于静态沙箱环境，威胁模型也大多局限于内容层的提示注入攻击（如间接提示注入、恶意UI或提示词攻击）。这种方法论上的局限导致了一个关键的评估盲区——它无法有效模拟和测试代理在动态、真实的网络层所面临的威胁，尤其是中间人攻击这类能够实时篡改网络流量和观测信息的主动攻击。

因此，本文的核心问题是：如何对OpenClaw这类依赖实时网络观测的自主代理，进行更贴近真实部署场景的动态网络安全评估？为填补这一空白，论文提出了ClawTrap框架，这是一个专门为OpenClaw设计的、基于中间人攻击的红队测试框架。它通过构建一个可复现的、规则驱动的网络流量拦截、篡改与审计管道，在实时浏览环境中实现多样化的攻击形式（如静态HTML替换、Iframe弹窗注入、动态内容修改），从而揭示在静态沙箱测试中无法暴露的安全漏洞，对代理的鲁棒性提供更真实、更严格的评估。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 代理能力与安全性基准测试**：InjecAgent、AgentDojo和ASB等研究专注于评估提示注入（IPI）威胁下的工具使用工作流。AgentBench、ToolLLM、GAIA和SWE-bench等通用代理基准则评估规划、工具使用和长程任务执行能力。HAICOSYSTEM和OpenAgentSafety等生态系统进一步扩展了风险评估范围。这些工作奠定了重要基础，但**本文指出**，它们大多未直接评估实时浏览过程中的网络层对抗性操纵。

**2. 面向网络代理的现实环境与安全评估**：WebArena、Mind2Web、WebShop等环境实现了与部署相关的评估。基于此的安全评估工作，如WASP、WebTrap Park、DoomArena和WAREX等，表明自主浏览器在对抗性网络条件下依然脆弱。**本文的工作（ClawTrap）与这些研究密切相关**，均关注网络代理在真实或仿真环境中的安全风险。

**3. 视觉/用户界面层面的攻击研究**：EIA、Pop-up Attacks、WebInject、AdvAgent、SecureWebArena和TRAP等工作证明，被操纵的界面信号能显著改变代理决策。**本文与这类研究的区别在于**，它聚焦于网络流量层（MITM）的攻击，而非内容或UI层面的直接篡改。

**4. 中间人（MITM）攻击相关研究**：现有代理系统中的MITM研究主要针对代理间的通信信道攻击，或研究对抗性记忆/事实操纵。**本文明确指出，ClawTrap与这些工作的核心区别在于**：它专注于对实时网络流量的端到端拦截与重写，以填补当前基准测试与真实部署条件（流量可在传输中被拦截和篡改）之间的空白。因此，ClawTrap旨在通过动态的MITM评估，衡量网络层攻击下的任务结果和信任校准，从而补充现有研究体系。

### Q3: 论文如何解决这个问题？

论文通过设计并实现一个名为ClawTrap的中间人攻击框架来解决对OpenClaw等自主网络代理在真实网络威胁下安全鲁棒性评估不足的问题。其核心方法是采用“本地捕获-云端诱导”的架构，将代理执行环境保持在云端，而将审计逻辑集中在研究者控制的本地节点上，从而在动态、真实的网络条件下进行安全测试。

整体框架由四个紧密耦合的层组成：第一层是云端被代理适配器包装的OpenClaw目标实例；第二层是用于透明流量转发的私有Tailscale点对点隧道集群；第三层是构建在mitmdump上的本地拦截引擎，包含作为调度器的`interceptor.py`、作为规则评估器的`matcher.py`以及执行攻击模式的`transformer.py`；第四层是辅助服务，包括有效负载片段、基于FastAPI的蜜罐服务器以及用于遥测检查的研究者仪表板/CLI。

关键技术流程分为三个阶段：首先进行初始化与环境同步，研究者配置本地设置并同步脚本到云端实例，激活流量接管，将代理的出站请求路由至私有隧道。其次是请求路径拦截与规则决策，当代理发出请求时，流量被隧道传至本地代理端口并被拦截器捕获；匹配器先检查检测规则（如对可疑元数据接口的访问），匹配事件会异步报告给蜜罐服务器；随后检查针对受保护域的模拟规则，若匹配则转换器直接提供本地伪造内容，请求不会到达公共互联网。最后是响应路径转换与返回，对于非模拟流量，请求被转发至真实网络，返回的响应会根据激活的攻击模式在流中进行重写。

该框架的主要创新点在于形式化了一个三元攻击模式分类法，并通过其MITM管道原生支持这三种形式：1) **静态HTML替换**：完全用伪造但看似合理的页面替换原始响应体，毒化代理的主要证据源；2) **Iframe弹窗注入**：通过注入的iframe容器在合法页面上叠加欺骗性高优先级界面元素，实现钓鱼式指令劫持；3) **动态内容修改**：在内容渲染时对选定的DOM片段或文本字段进行细粒度的流内重写，用于隐秘操纵关键信息。这种设计有意识地弥合了静态沙盒内容攻击与部署时风险之间的差距，为系统性评估真实流量条件下的安全鲁棒性提供了统一且可复现的基础。

### Q4: 论文做了哪些实验？

实验在动态的真实世界浏览循环中进行：OpenClaw 发出实时网络请求，ClawTrap 在响应渲染给智能体之前执行实时中间人（MITM）重写，直接针对智能体的观察通道进行安全测试。实验评估了两种代表性的 MITM 注入模式：攻击 A 将返回页面替换为伪造的新闻内容；攻击 B 保留真实网页但注入一个高紧急性的虚假警告覆盖层。这两种攻击覆盖了实时流量下的全内容毒化和局部 UI 信号操纵。

实验设置了两个演示案例。案例一（攻击 A）的任务是“告诉我 bbc.com 上有什么”，拦截器将返回页面重写为伪造内容。案例二（攻击 B）的任务是“访问 google.com 并告诉我上面有什么”，并在真实页面上注入虚假警告。实验主要对比了不同规模模型（如 GPT-5-mini、GPT-5.4、GPT-5-nano、GLM-5、Qwen3.5-397b-a17b）的行为。

关键结果显示了清晰的模型分层现象：较弱模型（如 GPT-5-mini、GPT-5-nano）倾向于信任被篡改的观察内容，产生自信但不安全的输出（例如总结伪造新闻或忽略虚假警告）。而较强模型（如 GPT-5.4、GLM-5）则表现出更好的异常归因能力和更安全的回退策略，例如检测到页面不一致、归因于网络拦截/代理重写，并建议验证网络状况或警告真实性。这些发现表明，可靠的 OpenClaw 安全评估必须纳入动态的真实世界 MITM 条件，而不仅仅是静态沙箱协议。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其局限性主要体现在当前框架仍属初步概念验证，评估以定性案例分析为主，缺乏大规模、系统化的定量基准测试。未来研究可沿三个方向深入：一是**规模化定量评估**，构建更广泛的任务集（如信息检索、表单提交、多步骤事务），系统测量攻击成功率、任务完成率及信任误判率等指标；二是**扩展任务覆盖范围**，将评估场景从新闻阅读等延伸至凭据处理、电商交易、API集成管道等高安全敏感度领域；三是**发展更先进的动态MITM攻击方法**，如会话持久化注入、跨链式代理调用的多跳流量篡改、基于时序的攻击等，以模拟更真实复杂的对抗网络环境。

结合个人见解，还可探索以下方向：首先，可研究**攻击检测与防御机制的协同设计**，在评估框架中集成轻量级异常检测模块，以促进主动防御策略的开发；其次，考虑**多模态与跨平台安全评估**，将MITM攻击扩展至图像、音频等交互场景，并测试不同代理框架与模型骨干的泛化脆弱性；最后，引入**人类-AI协同安全评估**，探究在部分观测被篡改时，人类监督或干预能否提升代理的鲁棒性，这有助于推动安全人机协作范式的发展。

### Q6: 总结一下论文的主要内容

该论文提出了ClawTrap，一个基于中间人攻击的红队测试框架，用于评估真实网络环境中OpenClaw等自主网络代理的安全性。其核心问题是现有评测主要关注静态沙盒环境和内容层面的提示攻击，而忽略了动态网络层威胁，导致安全评估存在实践缺口。

方法上，ClawTrap构建了一个可复现的流水线，支持规则驱动的网络拦截、响应篡改和审计，并实现了多种可定制的攻击形式，如静态HTML替换、iframe弹窗注入和动态内容修改。这为系统化测试任务完整性、代理行为完整性和用户级安全性提供了统一框架。

主要结论显示，模型在遭受MITM攻击时表现出明显的分层现象：较弱模型更容易信任被篡改的观察结果并产生不安全输出，而较强模型则展现出更好的异常归因能力和更安全的回退策略。因此，可靠的OpenClaw安全评估必须纳入动态的真实网络条件，而非仅依赖静态协议。该框架的贡献在于将评估标准从“代理能否完成任务”转向“代理能否在对抗性网络条件下安全完成任务”，为构建来源感知防御和改进安全设计实践奠定了基础。
