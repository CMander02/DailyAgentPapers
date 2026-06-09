---
title: "SecureClaw: Clawing Back Control of LLM Agents"
authors:
  - "Yuhan Ma"
  - "Stefan Schmid"
date: "2026-06-08"
arxiv_id: "2606.09549"
arxiv_url: "https://arxiv.org/abs/2606.09549"
pdf_url: "https://arxiv.org/pdf/2606.09549v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent安全"
  - "双边界架构"
  - "授权机制"
  - "明文隔离"
  - "工具使用Agent"
relevance_score: 9.0
---

# SecureClaw: Clawing Back Control of LLM Agents

## 原始摘要

Tool-using large language model (LLM) agents face two distinct security failures: unauthorized external actions and exposure of sensitive plaintext inside the runtime before any final output check can intervene. Existing defenses usually protect one boundary, either the planner/runtime or the action sink, and therefore do not by themselves secure both surfaces. We present SecureClaw, a dual-boundary architecture that places authorization at the effect sink and plaintext confinement at the read boundary. Sensitive reads pass through a trusted gateway that replaces raw values with opaque handles and, in the evaluated deployment, bounded summaries as an explicit declassification interface. Writes that change external state follow a PREVIEW$\rightarrow$COMMIT protocol in which only a trusted executor may commit the exact canonical request authorized by policy. The runtime can still plan over summaries and symbolic references, but cannot directly dereference secrets or perform side effects. Across AgentDojo, AgentLeak, and Agent Security Bench (ASB), SecureClaw is the only defense we evaluate in a common harness that simultaneously retains usable task utility and achieves 0\% attack success rate (ASR) on ASB, 0.64\% ASR on AgentDojo, and 3.23\% overall leak on AgentLeak's attacked parity lane, which measures final-output and internal-relay leakage.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决工具使用型大语言模型（LLM）代理面临的两个关键安全问题：一是未经授权的外部操作，二是敏感明文在运行时环境中暴露，而现有的输出检查机制无法在操作发生前或内部通信中进行干预。当前研究背景显示，虽然已有针对提示注入、工具选择等攻击的防御方法，但这些方法通常只保护单一边界，例如规划器/运行时或动作接收端，无法同时应对上述两类威胁。现有防御的不足在于：若仅控制效果边界，运行时仍可能读取并泄漏敏感数据；若仅限制信息流，却无法阻止未被授权的操作被执行。因此，本文提出一种双边界架构SecureClaw，旨在同时解决这两个问题。核心思路是：在效果接收端实施基于请求的授权控制，在读取端通过可信网关将敏感数据替换为不透明句柄和受限摘要，从而彻底隔离敏感明文。该架构确保即使运行时被攻陷，也无法直接访问机密或执行未经授权的状态修改，从而在保持任务可用性的同时有效阻断攻击。

### Q2: 有哪些相关研究？

相关研究可分为三类。**基准与运行时防御**：如AgentDojo、ASB、AgentLeak、WASP等基准测试将评估从提示分类转向动态agent，而IPIGuard、DRIFT等运行时防御通过隔离注入指令或约束工具依赖来增强规划器鲁棒性。SecureClaw将此类方法作为基线，但核心区别在于其主张被注入或攻破的运行时不应作为外部效应或敏感明文的参考监视器。**执行控制与agent授权**：Faramesh、Progent、PCAS、AC4A将执行强制转向agent动作边界的策略或能力检查。SecureClaw与它们互补，但分离了两个常被混淆的问题：一是通过PREVIEW→COMMIT协议将策略决策绑定到后续执行的确切规范请求，消除规划器检查与工具调用间的TOCTOU间隙；二是仅靠动作端授权无法移除已存在于规划器状态中的秘密，因此需结合独立的读边界。**信息流、能力与策略表达性**：读路径借鉴了信息流控制、降级与能力系统，但LLM agent存在不透明隐藏状态和自然语言通道。SecureClaw通过不透明句柄使原始受保护值在运行时中不可表示，并将有界摘要视为显式降级而非无害预处理。句柄不具备模型的环境权限，解引用仅在经过调用者、会话、端点与策略检查后，在可信端点发生。

### Q3: 论文如何解决这个问题？

SecureClaw通过双边界架构解决LLM代理面临的两类安全失效:授权放置在效果边界,明文约束在读取边界。整体框架将规划与安全执行分离,运行时负责推理、搜索和编排工具调用,但不再受信任处理明文或执行外部效果。

核心设计包括两个主要模块。在读取路径上,可信网关(trusted gateway)作为中介,当工具返回敏感内容时,网关将明文存储在受保护的句柄表中,并返回不透明句柄(opaque handle)给运行时。句柄是基于HMAC-SHA256的高熵符号引用,关联调用者、会话、生存时间等元数据,运行时无法将其解析为明文。同时,网关会提供有界摘要(bounded summary)作为显式的解分类接口,使运行时仍能进行规划。

在写入路径上,采用PREVIEW→COMMIT协议。运行时仅能提议(propose)效应性动作,但无法直接提交。可信网关追加认证的调用者、会话和上下文信息后,对请求进行规范化并计算绑定摘要(binding digest)。策略引擎(policy engine)对精确的规范化请求进行授权。最终,可信执行器(executor)是唯一能接触效应性接收器的组件,它独立重新计算摘要、验证授权工件、检查新鲜度和重放状态,确认无误后才提交外部效果。

创新点在于:通过请求绑定授权完整性防止运行时篡改请求字段,通过句柄约束阻止内嵌明文泄露,并通过结构化的拒绝模板维持失败时的可用性。该方法在多个基准上实现了近乎零的攻击成功率。

### Q4: 论文做了哪些实验？

SecureClaw在三个基准测试（AgentDojo、AgentLeak、ASB）上进行了全面评估，使用gpt-4o-mini模型，温度设为0。实验比较了四个同框架基线方法：Plain、IPIGuard、DRIFT和Faramesh。主要结果如下：在ASB上，SecureClaw实现了0%的攻击成功率（ASR），同时保持了88.90%的实用性；在AgentDojo上ASR仅0.64%（4/629），攻击实用性56.60%，良性任务成功率60.82%；在AgentLeak的攻击并行通道上，总体泄露率降至3.23%（16/496），其中C2泄露0.20%，C5泄露0%。相比之下，其他基线方法无法同时达到这两个安全边界。机制消融实验表明，移除句柄机制会使C2泄露升至20.8%、C5升至8.3%，而移除执行边界不影响泄露率，验证了双边界架构的必要性。拒绝感知恢复实验显示，在保持0% ASR的前提下，可将ASB实用性从70%提升至86%。在29个对抗性绕过测试中，SecureClaw成功拒绝了所有25个对抗案例并接受了4个阳性控制。核心边界开销较小，执行器验证低于1毫秒，单服务授权约15毫秒。

### Q5: 有什么可以进一步探索的点？

SecureClaw的局限主要体现在三点：首先，它不保证策略允许动作内的语义正确性，这意味着即使行为被授权，其内容和影响可能仍存在安全隐患；其次，在AgentDojo上引入了良性效用损失，说明当前策略层对主体、客体和阶段的绑定不够严格；最后，部署风险在于虚假安全感——若保护字段被错误分类或副作用接收点未受管控，边界保证将失效。未来可探索更细粒度的策略建模，例如引入基于形式化验证的权限推理，确保授权动作的语义符合预期。针对效用损失，可尝试动态declassification策略，允许在可信环境下按需暴露最小必要信息。另一个方向是改进策略引擎的自动化审计：结合运行时监控与离线分析，自动识别未受管控的效应接收点。此外，目前的PREVIEW→COMMIT协议仅针对外部状态写入，可扩展至内部敏感操作（如模型状态修改），形成全方位的原子化控制流。跨代理协作场景中，分布式策略变体的非共谋假设也值得深入研究，以增强实际部署的鲁棒性。

### Q6: 总结一下论文的主要内容

SecureClaw提出了一种针对工具调用型大语言模型代理的安全架构，以解决现有防御仅保护单一边界（规划器/运行时或动作执行端）的不足。论文定义了两类安全失效：未经授权的对外部动作和运行时内部敏感明文泄露。该方法采用双边界架构：在效果执行端通过“预览→提交”协议，仅允许受信执行器提交符合策略的授权请求；在读取边界通过可信网关将敏感值替换为不透明句柄和有限摘要，使运行时只能基于符号化引用和摘要进行规划，无法直接解引用秘密或执行副作用。在AgentDojo、AgentLeak和Agent Security Bench（ASB）三个基准测试中，SecureClaw是唯一在保持可用任务效用的同时，实现ASB上0%攻击成功率、AgentDojo上0.64%攻击成功率、AgentLeak攻击平行通道上3.23%总体泄露的防御系统。结论表明，其结构性优势来自两种机制分别覆盖不同失效模式，高安全部署需两者结合。
