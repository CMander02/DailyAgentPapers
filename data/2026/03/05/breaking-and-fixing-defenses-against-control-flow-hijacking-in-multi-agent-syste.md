---
title: "Breaking and Fixing Defenses Against Control-Flow Hijacking in Multi-Agent Systems"
authors:
  - "Rishi Jha"
  - "Harold Triedman"
  - "Justin Wagle"
  - "Vitaly Shmatikov"
date: "2025-10-20"
arxiv_id: "2510.17276"
arxiv_url: "https://arxiv.org/abs/2510.17276"
pdf_url: "https://arxiv.org/pdf/2510.17276v2"
categories:
  - "cs.LG"
  - "cs.CR"
  - "eess.SY"
tags:
  - "多智能体系统"
  - "Agent安全"
  - "Agent防御"
  - "控制流劫持"
  - "Agent编排"
  - "Agent通信"
  - "系统安全"
relevance_score: 8.5
---

# Breaking and Fixing Defenses Against Control-Flow Hijacking in Multi-Agent Systems

## 原始摘要

Control-flow hijacking attacks manipulate orchestration mechanisms in multi-agent systems into performing unsafe actions that compromise the system and exfiltrate sensitive information. Recently proposed defenses, such as LlamaFirewall, rely on alignment checks of inter-agent communications to ensure that all agent invocations are "related to" and "likely to further" the original objective.
  We start by demonstrating control-flow hijacking attacks that evade these defenses even if alignment checks are performed by advanced LLMs. We argue that the safety and functionality objectives of multi-agent systems fundamentally conflict with each other. This conflict is exacerbated by the brittle definitions of "alignment" and the checkers' incomplete visibility into the execution context.
  We then propose, implement, and evaluate ControlValve, a new defense inspired by the principles of control-flow integrity and least privilege. ControlValve (1) generates permitted control-flow graphs for multi-agent systems, and (2) enforces that all executions comply with these graphs, along with contextual rules (generated in a zero-shot manner) for each agent invocation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决多智能体系统中控制流劫持攻击的防御难题。研究背景是，基于大语言模型的智能体系统（如AutoGen、CrewAI等）通过任务分解与委托机制自动化复杂任务，但系统中包含不可信的外部内容（如邮件、网页），容易遭受间接提示注入攻击。现有防御方法（如LlamaFirewall）依赖对智能体间通信进行“对齐性检查”，以确保代理调用与原始目标相关且有助于推进任务。然而，这些方法存在明显不足：首先，对齐的定义本身脆弱且模糊，难以准确界定；其次，检查器缺乏对执行上下文的完整可见性，无法洞察黑盒智能体的内部状态；再者，安全性与功能性存在根本冲突——系统为适应环境错误而重新规划时，可能被攻击者利用，通过伪装成必要修复步骤的恶意指令绕过对齐检查。

本文的核心问题是：如何设计一种能够有效抵御控制流劫持攻击的防御机制，克服现有对齐检查方法的局限性，并解决多智能体系统中安全性与功能性的内在矛盾。为此，论文提出ControlValve防御系统，其创新点在于：1）为多智能体系统生成允许的控制流图，从结构上约束智能体调用路径；2）结合零样本生成的上下文规则，强制所有执行过程符合该图，从而在编排层面实现控制流完整性与最小权限原则，避免攻击者通过“推理绕过”对齐检查。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕多智能体系统的安全防御展开，可分为以下几类：

**1. 对齐检查与防火墙类防御**：这是本文重点讨论的现有防御范式。以LlamaFirewall为代表，这类工作在编排层监控智能体间的通信，通过检查消息是否与原始目标“相关”并“可能推进”该目标来防御控制流劫持。其核心假设是高级LLM（如GPT-4）能够可靠地执行这种对齐判断。本文的研究起点正是挑战这一假设，证明了即使由先进LLM执行检查，攻击依然可以绕过。

**2. 基于LLM微调或内部状态监控的防御**：论文在相关工作中简要提及了另一类防御方案，例如通过微调LLM或监控其内部状态来增强安全性。但本文明确指出，这类方法在实际的多智能体部署场景中往往不适用，因为它们需要改造LLM本身或拥有其内部访问权限，限制了普适性。因此，本文的研究聚焦于无需微调、不假设能访问LLM内部状态的编排层防御。

**本文工作与上述研究的关系与区别**：本文首先揭示了第一类对齐检查防御的根本性弱点，指出其依赖的“对齐”定义本身脆弱且检查器对执行上下文可见性不全，导致安全与功能目标存在本质冲突。在此基础上，本文提出的ControlValve防御机制转向了新的范式。它受控制流完整性和最小权限原则启发，通过生成并强制执行许可的控制流图及上下文规则来保障安全，这与依赖语义对齐判断的先前工作有本质区别，提供了更形式化、可验证的防护。

### Q3: 论文如何解决这个问题？

论文通过提出并实现名为ControlValve的新防御机制来解决多智能体系统中的控制流劫持问题。该方法的核心思想借鉴了控制流完整性和最小权限原则，通过生成并强制执行预定义的控制流图及上下文规则，确保系统执行过程的安全性与合规性。

整体框架分为规划与执行两个阶段。在规划阶段，系统基于用户任务和可用智能体集合，利用大语言模型生成两项关键内容：一是允许的控制流图，以上下文无关文法定义智能体调用的合法序列；二是针对图中每条边的上下文规则，限定智能体调用的具体条件。这些规则在零样本方式下生成，聚焦于输入验证、上下文适当性和数据来源验证，且每条边最多三条规则以避免过度约束。

执行阶段部署了LLM法官进行实时检查。在每次智能体间交互前，系统验证该转换是否对应控制流图中的合法边，并判断是否符合该边特定的上下文规则。与基于对齐检查的防御方法不同，ControlValve的运行时检查范围非常狭窄，仅验证动作是否符合预定义的图结构和规则，而非评估其与整体任务的对齐程度，从而降低了误判风险。若检查失败，系统会尝试重新规划（如添加提示约束或更换智能体），最多允许三次重试；若仍不满足则阻止转换。

创新点主要体现在三方面：一是将控制流完整性原则引入多智能体系统安全领域，通过文法化控制流图约束调用序列；二是采用边特异性上下文规则增强细粒度控制，在规划阶段生成以避免受不可信内容影响；三是实现任务无关和零样本的防御机制，无需攻击示例即可部署。该方法仅需在编排层操作，适用于智能体内部状态不可见的黑盒场景，有效解决了委托与不透明性带来的安全挑战。

### Q4: 论文做了哪些实验？

论文实验设置基于AutoGen平台，使用Magentic-One配置的多智能体系统，其中编排器采用OpenAI o4-mini，子智能体采用GPT-4o。实验数据集包括CFH-Hard（含10个编码任务和6个计算机使用任务）和AgentDojo Slack环境（21个任务）。攻击目标涉及打开反向Shell、通过邮件外泄信息等。评估指标包括良性任务成功率（单答案任务准确率、开放性问题由o4-mini作为裁判评估质量）和攻击成功率。

对比方法包括：（1）无防御基准（Base）、（2）最小权限（LP）、（3）LlamaFirewall（LF，使用Llama、GPT-4o-mini、GPT-4o、o4-mini四种LLM进行对齐检查）、（4）Azure内容过滤器（ACF）。主要结果如下：对于间接提示注入（IPI）攻击，LlamaFirewall在大多数情况下能有效阻挡（攻击成功率多为0%），但在AgentDojo模板的计算机使用场景中，使用Llama时攻击成功率达63%。ControlValve（CV）对所有IPI攻击的防御成功率均为0%。对于控制流劫持（CFH）攻击，LlamaFirewall的防御效果因攻击模板和后台LLM而异：在编码任务中，针对原始CFH攻击，使用Llama时攻击成功率为7%-23%，而针对CFH-Hard攻击，使用Llama时攻击成功率升至80%-100%；在计算机使用任务中，使用Llama时攻击成功率为67%-89%。ControlValve对所有CFH攻击的防御成功率均为0%。在良性任务性能上，ControlValve在单答案编码任务中准确率达97%（基准为93%），在计算机使用任务中达100%（基准为89%），在开放性问题中质量与基准相当或略优。此外，实验还发现，在模糊文档导致的意外安全违规中，基准系统在未授权情况下发送敏感数据的比率为56%-89%，而ControlValve将其降至13%。

### Q5: 有什么可以进一步探索的点？

基于论文内容，未来可探索的方向包括：首先，论文指出现有防御机制（如LlamaFirewall）对“对齐”的定义较为脆弱，且检查器对执行上下文可见性不足，这导致安全与功能目标存在根本冲突。因此，未来研究可深入探讨更鲁棒的对齐定义方法，例如结合动态上下文感知技术，以更全面评估代理行为的意图和风险。其次，ControlValve虽能有效防御攻击，但其生成的允许控制流图和上下文规则依赖零样本生成，可能无法覆盖复杂多变的真实场景。未来可研究如何结合少样本学习或持续学习，使系统能自适应更新安全策略。此外，论文提到攻击可能滥用合法代理工具，未来可探索基于行为分析或异常检测的补充防御机制，以识别工具使用中的异常模式。最后，多智能体系统的安全评估需扩展到更广泛的任务和攻击向量，包括跨平台协作场景，以验证防御方案的通用性和可扩展性。

### Q6: 总结一下论文的主要内容

该论文聚焦于多智能体系统中的控制流劫持攻击及其防御问题。核心贡献在于揭示了现有基于对齐检查的防御机制（如LlamaFirewall）的脆弱性，并提出了一种名为ControlValve的新防御方案。

论文首先定义了问题：攻击者可通过操纵多智能体系统的编排机制，诱导其执行危险操作，从而泄露敏感信息。现有防御依赖LLM对智能体间通信进行对齐检查，但作者证明即使使用先进LLM，攻击仍可绕过。其根本原因在于系统安全性与功能性目标存在内在冲突，且“对齐”定义脆弱，检查器对执行上下文可见性不足。

方法上，作者提出ControlValve，其灵感来源于控制流完整性和最小权限原则。该方法包含两个关键步骤：(1) 为多智能体系统生成允许的控制流图；(2) 强制执行所有执行都符合这些控制流图，并为每个智能体调用生成零样本的上下文规则。

主要结论是，ControlValve能有效防御所展示的控制流劫持攻击，为解决多智能体系统内在的安全与功能冲突提供了更健壮的思路。其意义在于将传统软件安全中的控制流完整性思想成功引入并适配于基于LLM的多智能体系统安全领域。
