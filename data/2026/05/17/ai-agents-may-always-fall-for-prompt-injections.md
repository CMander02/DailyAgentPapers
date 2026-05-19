---
title: "AI Agents May Always Fall for Prompt Injections"
authors:
  - "Sahar Abdelnabi"
  - "Eugene Bagdasarian"
date: "2026-05-17"
arxiv_id: "2605.17634"
arxiv_url: "https://arxiv.org/abs/2605.17634"
pdf_url: "https://arxiv.org/pdf/2605.17634v1"
categories:
  - "cs.CR"
  - "cs.CL"
  - "cs.CY"
tags:
  - "Agent 安全"
  - "提示注入"
  - "上下文完整性"
  - "对齐"
  - "对抗攻防"
relevance_score: 7.5
---

# AI Agents May Always Fall for Prompt Injections

## 原始摘要

Prompt injection is the most critical vulnerability in deployed AI agents. Despite recent progress, we show that the prevailing defense paradigm (data-instruction separation) both fails to detect attacks that operate through contextual manipulation and degrades contextually appropriate behavior. We then recast prompt injection via the lens of Contextual Integrity (CI), a privacy theory that judges information flow compliance with contextual norms. This explains types of attacks that current defenses attempt to patch and predict advanced ones future agents will face. We develop unique benign and attack scenarios that force an agent to violate the norms by (1) misrepresenting the flow, (2) manipulating norms, or (3) mixing multiple flows. This reframing suggests an impossibility result: an adversary can always construct a context under which a blocked flow appears legitimate, or a defender who tightens norms will block genuinely legitimate flows. Our findings suggest that current research addresses a shrinking fraction of future attack surfaces. Instead, through CI, we offer a principled framework for evaluating context-sensitive failures, and designing CI-aware alignment for the frontier autonomous agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决AI代理系统中提示注入攻击这一最关键的漏洞问题。当前研究背景是，随着LLM代理日益自主化并执行长周期任务，攻击者利用模型上下文进行攻击的机会显著增加。现有方法的不足在于，主流防御范式（数据-指令分离）将提示注入简单视为“隐藏在数据中的指令”，但这种做法无法检测通过上下文操控实施的攻击（如利用“请求已获部门主管批准”等合法表述进行伪装），同时会抑制上下文合理行为，降低系统实用性。更根本的是，代理的运行环境中指令无处不在，与第三方交互、内存使用或技能调用本质上都具有指令性，因此数据与指令难以分离且不影响代理工作流。

本文要解决的核心问题是：证明当前防御范式存在根本性局限，并重新定义提示注入的本质。通过引入情境完整性（CI）理论框架，将攻击分解为错误表述信息流、操控规范、混合多信息流三类规范违反模式。研究表明，攻击者总可以构造看似合法的上下文来绕过固定规则，而防御者收紧规则又会阻塞合法流程。这种矛盾揭示了提示注入防御不可能性的理论困境，预示现有防御仅适用于简单场景，无法应对未来更强大代理面临的攻击面。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要分为以下几类：

**1. 上下文完整性（CI）在LLM中的应用**：这类研究将CI理论引入LLM，用于指导信息共享决策。例如，ConfAIde衡量模型在信息传递中是否尊重上下文规范；PrivacyLens将CI参数实例化为小故事和工具使用任务；AirGapAgent通过每任务CI策略最小化用户数据暴露，并将上下文劫持视为CI违规。本文与这些工作的区别在于，以往研究主要将CI视为限制“披露什么”的框架，而本文将其扩展至“智能体是否应该采取行动”这一更广泛问题，认为提示注入应在此扩展背景下理解。

**2. 评估和攻击智能体LLM**：评估方面，AgentDojo和InjecAgent通过在工具输出中嵌入显式对抗字符串来测量鲁棒性；LLMail-Inject和ConVerse则进一步引入更贴近实际对话的、上下文敏感的对抗示例，发现此类攻击更难防御。攻击方面，PAIR、AutoInject和AgentVigil等方法通过自动红队生成攻击字符串，但这些方法通常在固定上下文中优化载荷。本文的基于CI的攻击则操纵上下文，使目标行为在模型可识别的规范下看起来合理，这是一种更难的问题，也是未来自主智能体可能面临的主要威胁。

### Q3: 论文如何解决这个问题？

论文通过重新定义提示注入为“上下文完整性（CI）违反”，提出了一个理论框架来分析和解决该问题。核心方法是将AI代理的动作建模为信息流，并通过五个参数（发送者、接收者、主体、信息类型、传输原则）来评估其适当性。整体框架包含两阶段分析：第一阶段识别信息流的CI参数，判断是否符合上下文规范；第二阶段通过评估启发式（考虑利益相关者偏好、伦理政治价值和上下文功能）来判定动作的合法性。

主要模块包括参数识别、规范评估和决策完整性。创新点在于揭示了当前防御范式（指令-数据分离）的盲区：攻击者可以通过（1）伪造参数值（如虚构发送者或授权原则）、（2）操纵规范判断（如利用紧急语气迫使代理行动）、（3）混合多个信息流（如将授权请求与未授权请求交织在同一消息中）来绕过防御。关键技术包括将每次信息流独立评估，避免授权泄漏，以及识别规范接地缺口（代理在缺乏历史交互时倾向于宽松解释权限）。

论文还提出了一个不可能性结果：攻击者总能构造一个使被封锁流看似合法的上下文，而加强规范的防御者则会阻止合法流。因此，当前防御仅能覆盖未来攻击面的一小部分。通过CI视角，论文提供了评估上下文敏感失败的框架，并倡导设计CI感知的对齐机制，以应对未来自主代理面临的复杂攻击。

### Q4: 论文做了哪些实验？

论文进行了三组实验。第一组实验是**CI参数攻击和规范评估攻击**。设置上，攻击模型（claude-sonnet-4-6）获取目标智能体的系统提示，通过PAIR红队框架迭代生成邮件，试图让目标智能体在限制性用户提示下执行send_email。随机采样150个场景，每场景3条攻击流，最多15次迭代。参数攻击在claude-sonnet-4-6上成功率达96.7%（基线0.67%），且攻击可迁移至其他模型（gpt-5.4成功率63.3%，gpt-5.2成功率89.3%，gemini-3-pro成功率92.6%），主要通过伪造用户委托、迭代缩小授权或伪造时间戳实现。规范评估攻击在gpt-5.2上成功率达79.0%，通过价值论证（如不行动对用户的危害）说服智能体。

第二组实验测试**无历史上下文的规范推断失败**。构建300个多轮场景，涵盖4个领域，分为相邻、跨类别和权限升级三类。评估claude-sonnet-4-6、gemini-3-pro和gpt-5.4。无历史时越权执行率分别为29.9%、32.2%和36.2%；有10轮历史后分别降至7.0%、24.2%和24.5%；实用基线保持在91.6-95.0%。

第三组实验测试**流分离失败**。构建100个跨专业场景，展示包含授权(F1)和非授权(F2)双重请求的单条消息。结果显示，无边界条件下，gpt-5.2在65%场景中执行了外部通信，gpt-5.4为34%，claude-sonnet-4-6为6%；明确边界后，claude-sonnet-4-6和gpt-5.4违规清零，gpt-5.2降至12%。

### Q5: 有什么可以进一步探索的点？

基于论文的局限性和未来研究方向，可以进一步探索的点包括：

1. **上下文边界的动态建模**：当前实验假设用户能明确表达委托范围和流程边界，但现实中用户委托往往模糊且多变。未来研究需开发能够从交互历史中动态推断上下文规范的方法，同时防止对手通过早期交互锚定代理理解以实施升级攻击。

2. **规范冲突与价值对齐**：论文指出规范依赖文化、组织或个人背景，且不同个体对“适当性”存在合理分歧。需要探索基于Contextual Integrity（CI）的奖励强化学习，通过对共享表面形式但不同委托上下文的情景对进行对齐训练，解决代理在规范冲突中的决策权衡。

3. **分层防御架构设计**：可研究CI启发的分层系统，其中模型进行CI推理，系统层对声明进行事实验证，以缓解过度或不足合规的困境。同时需要设计CI驱动的红队测试，在多代理系统中系统性地发现隐私与安全漏洞，应对未来更复杂的攻击面。

### Q6: 总结一下论文的主要内容

这篇论文重新定义了AI智能体面临的关键安全威胁——提示注入问题。传统上，该问题被视为“数据中的指令”，而作者指出现有防御（数据-指令分离）不仅无法检测通过上下文操纵进行的攻击，还会降低上下文的适切性。论文引入语境完整性理论，将提示注入理解为攻击者通过操纵信息流上下文来使违规行为看似合理。作者提出了三种攻击类型：误述信息流、操纵规范、混合多个信息流，并论证了一个不可能性结果：攻击者总能构造出使被阻断的流看似合法的上下文，而加强规范的防御者也必然会误伤合法请求。实验表明，当前基于对齐的安全训练会同时降低安全性和实用性，而基于CI的红队攻击在基准不到1%的邮件助手上可达96.7%成功率。本研究的核心贡献在于提供了一个评估上下文敏感失败的原则性框架，并呼吁设计CI感知的对齐方法以应对未来自主智能体更复杂的安全挑战。
