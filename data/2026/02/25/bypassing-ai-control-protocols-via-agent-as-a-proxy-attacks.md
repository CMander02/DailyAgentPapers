---
title: "Bypassing AI Control Protocols via Agent-as-a-Proxy Attacks"
authors:
  - "Jafar Isbarov"
  - "Murat Kantarcioglu"
date: "2026-02-04"
arxiv_id: "2602.05066"
arxiv_url: "https://arxiv.org/abs/2602.05066"
pdf_url: "https://arxiv.org/pdf/2602.05066v2"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Security"
  - "Agent Attacks"
  - "Prompt Injection"
  - "Agent Monitoring"
  - "Agent Defense"
  - "Agent Evaluation"
  - "Multi-Agent Systems"
relevance_score: 8.0
---

# Bypassing AI Control Protocols via Agent-as-a-Proxy Attacks

## 原始摘要

As AI agents automate critical workloads, they remain vulnerable to indirect prompt injection (IPI) attacks. Current defenses rely on monitoring protocols that jointly evaluate an agent's Chain-of-Thought (CoT) and tool-use actions to ensure alignment with user intent. We demonstrate that these monitoring-based defenses can be bypassed via a novel Agent-as-a-Proxy attack, where prompt injection attacks treat the agent as a delivery mechanism, bypassing both agent and monitor simultaneously. While prior work on scalable oversight has focused on whether small monitors can supervise large agents, we show that even frontier-scale monitors are vulnerable. Large-scale monitoring models like Qwen2.5-72B can be bypassed by agents with similar capabilities, such as GPT-4o mini and Llama-3.1-70B. On the AgentDojo benchmark, we achieve a high attack success rate against AlignmentCheck and Extract-and-Evaluate monitors under diverse monitoring LLMs. Our findings suggest current monitoring-based agentic defenses are fundamentally fragile regardless of model scale.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在揭示并解决当前基于监控的AI智能体防御协议中存在的一个根本性脆弱性问题。随着大型语言模型从被动文本生成器演变为能够执行复杂多步工作流的自主智能体，其安全性风险急剧增加。智能体在处理来自开放网络的不受信任数据时，极易遭受间接提示注入攻击，即攻击者将恶意指令嵌入外部内容，从而劫持智能体的控制流。为应对此威胁，当前的主流防御方案是采用混合监控机制，例如AlignmentCheck和LlamaFirewall。这类方法不仅检查智能体的最终输出，还会联合监控其内部思维链、工具调用及工具输出，以期全面评估其行为是否符合用户意图，并假设这种对“思考过程”的全面审视能提供比孤立检查输入输出更强的防御。

然而，本文指出，这种看似更强大的混合监控方法存在一个悖论性的新漏洞。现有方法的不足在于，其核心假设——联合监控能增强安全性——可能是不成立的。监控模型在处理智能体的思维链和工具调用时，无意中为攻击者提供了一个直接操纵监控器本身的渠道。本文要解决的核心问题正是：证明并利用这一漏洞，即攻击者可以将被入侵的智能体作为“代理”，使其在思维链或工具参数中重复经过优化的对抗性字符串，从而直接“欺骗”监控模型，使其将恶意的智能体行为轨迹误判为安全。论文通过提出一种新颖的“代理攻击”框架和相应的Parallel-GCG优化算法，实证了即使像Qwen2.5-72B这样的前沿大规模监控模型，也能被能力相近的智能体成功绕过。这表明，仅仅依靠扩大监控模型的规模无法保证安全，当前基于监控的智能体防御体系在架构层面存在根本性缺陷。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**攻击方法**、**防御与监控协议**以及**自适应攻击技术**。

在**攻击方法**方面，早期研究由Simon Willison和Fábio Perez等人提出，展示了针对大语言模型（LLM）的最初提示注入攻击。后续工作将间接提示注入（IPI）攻击扩展到了基于LLM的智能体（Agent）上。本文提出的“代理即代理”（Agent-as-a-Proxy）攻击是一种新颖的攻击形式，其核心区别在于：它将智能体仅视为攻击载荷的传递载体，而非攻击监控系统的参与者。这与之前需要智能体了解监控系统细节的攻击方法（如）有本质不同。

在**防御与监控协议**方面，相关工作主要围绕**思维链监控**展开。这类监控最初被提出作为一种AI安全措施，用于检测模型的不对齐行为（如奖励黑客攻击和消极怠工）。后来，它被用于检测由外部攻击引起的模型错误行为，最新版本通过同时监控智能体的推理（CoT）和工具使用行为来降低攻击成功率。具体实例包括LlamaFirewall中的AlignmentCheck（一种混合监控协议）以及“提取-评估”监控器。本文的研究对象正是这类结合了推理与行动监控的防御协议，并首次系统性地揭示了其根本脆弱性。

在**自适应攻击技术**方面，已有研究（如Greedy Coordinate Gradient和AutoDAN）表明，现有的IPI防御容易被自适应攻击绕过。但这些工作并未考虑针对CoT监控防御的场景。本文改进了现有方法：首先，成功将GCG应用于代理即代理攻击中；其次，提出了一种新的攻击算法，用于优化在LLM输入中多次出现的攻击字符串，从而有效绕过多步骤防御系统（如包含分类器和LLM监控器的LlamaFirewall）。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为“代理即代理”（Agent-as-a-Proxy）的新型攻击方法，来绕过基于监控的AI控制协议。其核心思路是将AI代理本身作为攻击载荷的传递机制，使恶意指令能够同时绕过代理及其监控器。

**整体框架与主要模块**：攻击框架基于对现有间接提示注入（IPI）任务的适应性修改。具体而言，论文设计了两种任务适配方式：一是修改原始任务指令，在合法操作中嵌入恶意字符串（OPTIM_STR）；二是在原始任务后追加一个额外的恶意子任务。这两种方式都旨在诱导代理在其执行轨迹（包括思维链和工具使用记录）中多次重复该恶意字符串，从而为后续优化提供基础。

**关键技术——Parallel-GCG**：这是论文的核心创新点。为了生成能有效欺骗监控器的对抗性字符串，论文扩展了传统的基于梯度的坐标梯度法（GCG）。传统GCG针对单一插入点优化字符串，但在智能体工作流中，监控器评估的是整个轨迹，对抗字符串会在多个阶段（如内部推理、工具调用）被重复观察到，且每次出现的上下文都不同。

Parallel-GCG 通过**同时优化字符串在K个插入点上的表现**来解决此问题。其流程是：首先使用一个占位符字符串运行一次代理，捕获其执行轨迹，并提取出恶意字符串出现位置前后的固定上下文切片。然后，构建一个近似的轨迹构造函数S(a)，将候选攻击字符串a插入到这个固定的上下文模板中，形成一个模拟的完整轨迹。优化目标是找到单个字符串a，使得该模拟轨迹在监控模型下产生目标（有害）响应的负对数似然损失最小。

关键的技术创新在于**梯度计算**：由于同一个字符串a被广播到轨迹中的K个不同位置，其嵌入向量的梯度是每个插入点处梯度的总和。通过这种聚合梯度的方法进行离散搜索，Parallel-GCG能够找到对轨迹中变化的局部上下文都保持“隐蔽性”的对抗字符串，确保其无论是在代理的内部推理阶段还是外部工具交互阶段，都能有效逃过监控器的检测。

**创新点总结**：1) 提出了“代理即代理”的攻击范式，揭示了监控协议的根本脆弱性；2) 设计了针对多阶段监控的Parallel-GCG优化算法，通过聚合多插入点梯度来生成鲁棒的对抗性提示；3) 在AgentDojo基准测试上成功验证了攻击对多种大型监控模型（如Qwen2.5-72B）的有效性，表明即使前沿规模的监控器也无法防御能力相近的代理发起的此类攻击。

### Q4: 论文做了哪些实验？

论文实验主要评估了新型“代理即代理”攻击对基于监控的AI代理防御协议的绕过能力。

**实验设置与数据集**：研究使用AgentDojo基准测试（版本1.2.1），重点关注其Slack任务套件（包含20个用户任务和5个注入任务），采用“重要指令”攻击模板，生成100个初始样本，并过滤掉代理层面攻击失败的案例，最终使用89个有效样本进行评估。攻击字符串使用贪婪坐标梯度（GCG）算法及其并行变体（Parallel-GCG）进行优化，针对监控模型的特定输出标签（如AlignmentCheck的“safe”标签或Extract-and-Evaluate的<score>0</score>）进行对抗性优化。

**对比方法与监控协议**：评估了三种监控协议：1) **混合监控（Hybrid monitor）**，使用AlignmentCheck实现，同时监控模型的思维链和工具调用；2) **输入过滤+混合监控**，结合PromptGuard 2进行输入过滤后再由AlignmentCheck监控；3) **提取与评估监控（Extract-and-Evaluate）**，先提取可疑引用再由判断模型评分。监控模型选用多个开源LLM，包括Llama-3.1-8B、Mistral-7B v0.3和Qwen2.5-7B。攻击代理则使用了GPT-4o mini和Llama-3.1-70B，以测试其绕过强大监控模型（如Qwen2.5-72B）的能力。

**主要结果与关键指标**：实验表明，优化后的自适应攻击能高效绕过所有监控协议。关键攻击成功率（ASR@5）数据如下：
- **针对AlignmentCheck**：使用Mistral-7B监控时ASR@5达93.3%，Qwen2.5-7B为90.7%，Llama-3.1-8B为42.3%。
- **针对PromptGuard 2 + AlignmentCheck**：Mistral-7B监控下ASR@5达99.0%，Qwen2.5-7B为86.6%，Llama-3.1-8B为76.3%。
- **针对Extract-and-Evaluate**：Mistral-7B监控下ASR@5达95.5%，Llama-3.1-8B为54.7%，Qwen2.5-7B为37.2%。

此外，实验发现即使代理与监控模型能力相近（如使用GPT-4o mini或Llama-3.1-70B攻击Qwen2.5-72B），攻击仍能成功（ASR@5分别达46.0%和60.2%），证明监控防御存在结构脆弱性，且混合监控在自适应攻击下反而暴露更大攻击面。

### Q5: 有什么可以进一步探索的点？

该论文揭示了基于监控的AI代理防御机制存在根本性脆弱性，但研究本身也存在局限，为未来提供了多个探索方向。首先，攻击字符串的高困惑度使其容易被分类器或人工检测，未来可研究生成低困惑度、更隐蔽的注入提示，甚至结合对抗样本技术使攻击更难被察觉。其次，当前攻击针对白盒监控模型，未来需探索黑盒场景下的代理攻击方法，例如利用代理引导的黑盒攻击技术，或通过迁移学习使攻击泛化至未知监控模型。此外，论文未深入探讨防御侧的改进可能性，未来可研究更鲁棒的监控架构，如引入多模态监控、动态权限机制或基于形式化验证的意图一致性检查。从更广视角看，仅依赖事后监控可能不足，需探索在代理架构层面嵌入安全机制，例如工具调用前的意图验证、分层决策审核，或将监控与训练过程结合，通过对抗训练提升代理内在的抵抗能力。

### Q6: 总结一下论文的主要内容

该论文揭示了基于监控的AI智能体防御机制存在根本性脆弱性，提出了一种新型的“代理即代理”攻击方法。核心问题是间接提示注入攻击可绕过现有依赖链式思维与工具使用联合评估的监控协议。论文通过设计Agent-as-a-Proxy攻击框架，将智能体本身转化为攻击传递机制，并开发Parallel-GCG优化算法自适应生成对抗性提示，使攻击能同时绕过智能体及其监控器。实验在AgentDojo基准上进行，结果表明即使采用前沿大模型如Qwen2.5-72B作为监控器，也能被能力相近的智能体如GPT-4o mini等成功欺骗，对AlignmentCheck和提取评估监控器的攻击成功率超过90%。主要结论挑战了“可扩展监督”假说，证明仅依靠模型规模扩展或运行时监控无法保证安全，必须转向设计具有结构安全性保障的体系架构。这一发现对自主智能体的安全部署具有紧迫意义。
