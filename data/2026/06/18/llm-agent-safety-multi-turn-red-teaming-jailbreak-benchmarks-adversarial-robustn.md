---
title: "LLM agent safety, multi-turn red-teaming, jailbreak benchmarks, adversarial robustness, safety-critical systems"
authors:
  - "Hanwool Lee"
  - "Dasol Choi"
  - "Bokyeong Kim"
  - "Seung Geun Kim"
  - "Haon Park"
date: "2026-06-18"
arxiv_id: "2606.20408"
arxiv_url: "https://arxiv.org/abs/2606.20408"
pdf_url: "https://arxiv.org/pdf/2606.20408v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "agent safety"
  - "multi-turn red-teaming"
  - "jailbreak benchmark"
  - "adversarial robustness"
  - "safety-critical systems"
  - "LLM agent security"
  - "attack-replay evaluation"
  - "defense evaluation"
relevance_score: 9.5
---

# LLM agent safety, multi-turn red-teaming, jailbreak benchmarks, adversarial robustness, safety-critical systems

## 原始摘要

Large language model (LLM) agents are increasingly proposed as supervisory components for safety-critical systems, yet their robustness under sustained, adaptive adversarial pressure remains poorly characterized. We present NRT-Bench, a benchmark for multi-turn red-teaming of LLM agents acting as operators of a safety-critical system, instantiated in a simulated nuclear power plant control room. A five-role operator team, each backed by a configurable LLM, runs a plant governed by six critical safety functions (CSFs), while adversaries inject messages over four channels in bounded multi-turn sessions with per-turn feedback. Harm is an objective signal rather than LLM-judged text: a run terminates the moment any CSF is lost, attributed to the causing message. Evaluating four frontier operator models under a fixed-attack paired-replay protocol, we find that adaptive multi-turn attacks reliably push the operator team past a safety limit: across the four models, between 8.7% and 12.1% of attack sessions end with the plant losing a critical safety function. Although the four models look almost equally robust by this aggregate rate, their failures barely overlap: of $149$ sessions, none defeat all four models while a third defeat at least one, so vulnerabilities are nearly disjoint across models rather than nested. The effect of added defences is strongly model-dependent: the same guardrail stack or safety-advisor agent that lowers attack success for one model can raise it for another. We release the simulation venue, attack dataset, and replay tooling for reproducible safety evaluation of LLM agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前LLM智能体安全评估中的一个核心问题: 现有红队测试基准无法有效评估多智能体系统在持续、自适应对抗攻击下的物理安全性。研究背景是LLM智能体正被提出用于工业、能源等安全关键系统的决策支持和监督组件,这些场景中错误操作可能导致不可逆的物理损害。现有方法的不足主要体现在三方面:第一,主流基准是单轮越狱测试,而真实攻击者是自适应、多轮次的,会利用会话积累的上下文。第二,伤害通常定义为由另一个LLM判定的违反策略的文本,缺乏对物理后果的客观衡量。第三,几乎所有基准都孤立评估单个模型,而高风险操作场景通常由多个角色分工、具有明确权限层级的团队构成,攻击通过操纵整个团队走向不安全轨迹,而非仅越狱单个模型。因此,本文要解决的核心问题是:能否通过自适应、多轮次的对抗攻击,驱动一个负责安全关键系统操作的多智能体团队(模拟核电站控制室)达到物理不安全状态,并为此建立一个具有客观物理伤害信号(关键安全功能丧失)的基准测试平台NRT-Bench。

### Q2: 有哪些相关研究？

1.  **方法类相关工作**：现有越狱评测从单轮提示向多轮对话演进。前期工作如规范越狱评测通常使用分类器或LLM法官评分单次提示；近期研究揭示多轮逐步升级、人工多轮红队攻击能在单一回合ASR个位数时令防御系统ASR超过70%。**本文NRT-Bench**与之共享多轮、基于反馈的攻击设定，但将LLM评判的有害文本替换为客观的安全功能转换信号，且攻击目标从单一模型扩展至团队。

2. **应用与评测类相关工作**：在智能体与多智能体安全领域，AgentDojo通过正式状态检查效用函数而非LLM法官来评估提示注入鲁棒性。**本文**采用了相同的防攻击标准，但将其具体化为物理信号（核电站安全功能）。现有研究虽表明单条注入消息可在智能体间级联传播，但主要衡量任务失败、数据泄露等抽象危害，鲜少针对角色结构化操作团队进行持续自适应压力测试，而**本文**填补了这一空白。

3. **特定领域相关工作**：在LLM用于安全关键控制领域（如核电与工业），现有基准主要评估LLM的网络安全建议知识或独立能力。**本文**首次将自适应多轮攻击、角色专业化团队、客观非LLM评判的危害信号以及安全关键物理领域结合到可复现的基准中，聚焦于操作团队向物理不安全状态演进的对抗鲁棒性。

### Q3: 论文如何解决这个问题？

该论文通过构建 NRT-Bench 基准框架，系统性地解决了LLM智能体在安全关键系统中的多轮对抗鲁棒性评估问题。核心方法采用**固定攻击-配对回放协议**，在模拟核电站控制室环境中，通过可复现的对抗交互来量化安全失效风险。

**整体框架**由三个核心组件构成：1）**状态化仿真环境**（nuclear-redteam-sim），包含六个关键安全函数（CSF）的抽象核电站模型，可确定性模拟正常运行、异常和紧急三种状态，任何CSF转为lost即触发客观安全指标；2）**五角色操作员团队**，包括高级反应堆操作员（SRO，最终决策权）、反应堆操作员（RO）、涡轮操作员（TO）、外场操作员（AO）和安全技术顾问（STA），通过类型化消息总线协作，每个角色可由不同LLM驱动；3）**四通道攻击接口**（CH-A外部监管通知、CH-B内部冒充、CH-C供应链篡改、CH-D辅助代理入侵），支持最多10轮的多轮对话，每轮返回状态摘要。

**关键技术**包括：确定性动作权限分类器，根据动作类型、子系统等级和电厂模式自动分配从L1到DENY的权限等级，防止攻击者绕过权限审批；**人类审批抽象层**，高影响动作需通过规则化模拟控制台批准；**完整踪迹捕获系统**，记录每一步交互并生成SHA-256校验清单，确保攻击可回放、可归因。创新点在于使用**客观环境状态**（而非LLM评判）作为主要安全指标，并通过**配对回放协议**消除攻击随机性，使不同防御者间的比较公平可靠。实验发现四个前沿模型（GPT-5.4-mini、Claude-Haiku-4-5、Gemma-4-26B、Qwen3.5-35B）的安全漏洞几乎不重叠，且同一防御措施对不同模型效果截然相反。

### Q4: 论文做了哪些实验？

论文在NRT-Bench基准上进行了一系列实验，模拟核电站控制室中LLM智能体操作员团队在多轮对抗攻击下的安全性。实验包含三名操作员角色，每位由可配置LLM支持，管理由六个关键安全功能（CSF）控制的电站。攻击者在有限回合中通过四个通道注入消息，每次回合有反馈，一旦CSF丢失即停止，视为安全事件。评估了四个前沿操作模型：gpt-5.4-mini、claude-haiku-4-5（云API），以及gemma-4-26B-A4B-it和Qwen3.5-35B-A3B（开源模型），在固定攻击重放协议下进行。主要结果：自适应多轮攻击可靠地将操作团队推过安全极限，各模型导致CSF丢失的攻击会话比例为8.7%至12.1%。但失败几乎没有重叠：149个会话中，无一个同时击败所有四个模型，三分之一至少击败一个，表明漏洞几乎互斥而非嵌套。防御效果高度依赖模型：相同防护栏或安全顾问对某模型降低攻击成功率，却可能提升另一模型的攻击成功率。关键数据指标：攻击成功率为8.7%-12.1%。

### Q5: 有什么可以进一步探索的点？

基于NRT-Bench的研究，未来可探索的方向包括：首先，当前攻击仅基于固定策略的配对回放协议，未来应研究完全自适应、动态演化的多轮攻击算法，以更真实模拟持续对抗压力。其次，论文发现不同模型的脆弱性几乎不重叠，这表明可探索模型集成或动态切换策略来提升鲁棒性，例如在运行中根据攻击模式选择最稳健的模型。此外，防御措施效果高度模型依赖，甚至可能适得其反，因此需设计个性化、上下文感知的守卫机制，而非通用堆叠。最后，当前任务局限于核电站模拟场景，可扩展到自动驾驶、医疗诊断等更多安全关键领域，并评估攻击对核心安全功能的多维度影响，如时序延迟或连锁故障。改进思路包括引入基于对抗训练的元学习框架，使代理在训练中暴露于跨模型的多样攻击模式，以增强泛化防御能力。

### Q6: 总结一下论文的主要内容

LLM智能体越来越多地被用作安全关键系统的监督组件，但其在持续对抗性压力下的鲁棒性尚未得到充分评估。本文提出NRT-Bench，一个针对安全关键系统中LLM智能体操作员的多轮红队测试基准。该基准在模拟核电站控制室中实现，由五名角色专业化操作员组成的团队运行基于六项关键安全功能（CSF）的设施，同时对手通过四个渠道在有限的多轮会话中注入消息，每轮提供反馈。危害被定义为客观信号而非LLM判断的文本：一旦任何CSF丢失，运行立即终止，并归因于导致该结果的消息。采用固定攻击配对回放协议评估四个前沿操作模型后发现，自适应多轮攻击能可靠地将操作团队推至安全极限：四个模型中，8.7%至12.1%的攻击会话导致工厂丧失关键安全功能。尽管各模型的总体脆弱率相似，但故障几乎不重叠：149个会话中，没有一次能攻破所有四个模型，而三分之一能攻破至少一个，表明漏洞在不同模型间几乎独立。防御措施的效果高度依赖模型：对某个模型降低攻击成功率的同一防护栏或安全顾问，可能反而增加另一模型的风险。本文开源了模拟平台、攻击数据集和回放工具，用于LLM智能体的可复现安全评估。
