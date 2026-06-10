---
title: "Assessing Automated Prompt Injection Attacks in Agentic Environments"
authors:
  - "David Hofer"
  - "Edoardo Debenedetti"
  - "Florian Tramèr"
date: "2026-06-09"
arxiv_id: "2606.10525"
arxiv_url: "https://arxiv.org/abs/2606.10525"
pdf_url: "https://arxiv.org/pdf/2606.10525v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "LLM Agent安全"
  - "提示注入攻击"
  - "黑盒攻击"
  - "白盒攻击"
  - "AgentDojo基准"
  - "多智能体系统"
relevance_score: 8.5
---

# Assessing Automated Prompt Injection Attacks in Agentic Environments

## 原始摘要

Indirect prompt injection poses a critical threat to LLM agents that interact with untrusted external data, yet automated attack methods--proven effective for jailbreaking--remain underexplored in realistic agentic settings. We present a comprehensive empirical evaluation of automated prompt injection attacks against LLM agents, adapting both white-box (GCG) and black-box (TAP) methods to the agentic setting within the AgentDojo framework. We evaluate across 80 task pairs spanning four domains and multiple models, and find that black-box optimization substantially outperforms gradient-based methods, a gap we attribute to GCG's optimization instability under reasonable compute budgets. We also find that TAP's effectiveness depends on the attacker model, as both general capability and safety tuning affect attack success--stronger models produce more effective injections, while safety-tuned attackers can refuse to generate adversarial prompts. Task-universal attacks transfer effectively to unseen tasks and out-of-distribution domains, but attacks optimized on smaller open-source models do not transfer to frontier models like GPT-5. These findings highlight automated prompt injection as a credible but model-dependent threat, with significant barriers remaining for model-agnostic exploitation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）智能体在自主环境中面临的间接提示注入攻击威胁，但自动化攻击方法尚未在现实智能体场景中得到充分评估的问题。研究背景是，LLM驱动的智能体能够与外部工具交互、执行代码并修改真实世界状态，这引入了严重的安全风险，其中最关键的是间接提示注入：攻击者将恶意指令嵌入到智能体正常操作中会检索的外部数据（如邮件或网页）中。现有方法的不足在于：对自动化提示注入攻击的研究仍不成熟，大多数工作依赖手动构造的攻击或简单启发式方法，且评估常局限于简化的单轮设定（如嵌入恶意指令的文本摘要），缺乏对状态化工具调用智能体的全面评估。这种场景更贴近真实部署，因为攻击需要引导模型进行多步推理和精确工具调用，与影响单一输出的挑战有本质区别。本文的核心问题是：如何将两种著名的越狱方法（白盒梯度优化GCG和黑盒搜索TAP）适配到智能体的提示注入场景，并在AgentDojo框架中对80个跨领域任务对进行实证评估，以系统性地量化自动化攻击的有效性、迁移性和模型依赖性。

### Q2: 有哪些相关研究？

相关工作主要分为三类：

1. **攻击方法类**：本文主要改编了两种代表性方法：GCG（白盒梯度优化攻击）和TAP（黑盒攻击框架，基于PAIR并引入分支与剪枝）。与这些方法的原始版本不同，本文将它们首次系统应用于Agent环境，且发现黑盒TAP显著优于白盒GCG，归因于GCG在合理计算预算下的优化不稳定性。

2. **攻击类型研究类**：本文聚焦间接提示注入（Indirect Prompt Injection），与常见的越狱攻击（Jailbreaking）形成对比。越狱攻击由用户直接操控输入以绕过安全对齐，而间接注入则利用Agent自主检索的外部数据（如邮件、文档）嵌入恶意指令。本文强调Agent化场景放大了此类风险，因为工具使用和多轮交互增加了攻击面。

3. **评测框架类**：本文基于AgentDojo平台，该平台提供动态、有状态的执行环境（覆盖工作区、银行、旅行、Slack四个领域），包含超过900个良性任务与恶意任务的组合，并通过确定性检查函数评估攻击成功性。与静态基准不同，AgentDojo模拟真实Agent交互，且注入点位于自然内容中（而非简单附加），使评估更贴近实际威胁。

### Q3: 论文如何解决这个问题？

论文通过将白盒（GCG）和黑盒（TAP）攻击方法适配到AgentDojo框架中，系统评估了自动化提示注入攻击在智能体环境中的有效性。整体框架包括三个核心组件：目标模型（被攻击的LLM Agent）、攻击模型（生成和优化注入候选）和评估模型（LLM判分员）。技术关键在于将攻击公式化为优化问题：白盒GCG利用梯度搜索修改对抗性前缀和后缀，使模型生成确认攻击目标的自然语言回复（而非脆弱的JSON工具调用）；黑盒TAP采用树搜索算法，攻击模型迭代生成候选注入，评估模型按1-10分对攻击效果打分，并通过分支因子和宽度参数进行剪枝。创新点包括：(1) 使用“解码-重编码”验证过滤器确保令牌序列在完整上下文中稳定，且限制ASCII可打印字符以通过JSON/YAML处理；(2) 引入通用优化，在多样任务批次上联合优化共享前缀/后缀，支持跨任务和跨域迁移；(3) 处理安全对齐模型的拒绝行为，如将攻击提示框定为防御性安全评估，并让评估器对拒绝响应打低分形成负反馈循环。此外，框架支持单任务（针对特定任务对生成定制注入）和任务通用（生成可复用组件）两种模式，并通过早停、可靠性重试和并行评估提升效率。核心评估指标包括攻击成功率、实用性和Success@N，其中黑盒TAP显著优于白盒GCG，后者因计算预算下的优化不稳定而表现不佳。

### Q4: 论文做了哪些实验？

在AgentDojo框架下，论文针对四个领域（Workspace、Banking、Travel、Slack）共80个任务对，系统评估了自动化提示注入攻击。实验设置使用NVIDIA H200 GPU，目标模型包括Gemma3-4B、Qwen3-4B和GPT-5。攻击方法对比了白盒方法GCG（30个对抗标记，800步优化，256候选/步）和黑盒方法TAP（GPT-5攻击者，3个根节点，分支因子3，最大宽度8，深度5），基线为直接指令和随机前缀-后缀。主要结果：TAP显著优于GCG，对Qwen3-4B单任务TAP的ASR达44.6%，通用版45.2%，而GCG仅为23.0%和24.1%。模型脆弱性差异显著：Qwen3-4B最脆弱，GPT-5最鲁棒（最佳TAP仅~4.5% ASR）。域间Slack最脆弱（单任务TAP ASR~67%），Workspace最鲁棒。通用攻击泛化良好，TAP在保留套件上仅轻微退化，GCG退化更严重。计算成本上，单任务TAP约0.6小时，GCG约1.5小时；通用TAP约2.4小时，GCG约21.9小时。此外，随机信号GCG表现与标准GCG相当，TAP评估器（GPT-5-mini）对Qwen召回率100%但精确率仅52.3%。跨模型迁移显示，小模型优化的攻击无法转移到GPT-5。

### Q5: 有什么可以进一步探索的点？

论文的局限包括：实验主要基于AgentDojo框架，任务类型和复杂度有限，未能覆盖多智能体协作、长周期任务等更现实的场景；GCG优化在有限算力下表现不稳定，未探索更高效的梯度引导攻击变体；TAP攻击者模型依赖性表明，安全对齐对攻击生成产生抑制作用，但未深入分析如何绕过这一限制。未来可探索：1) 设计针对Agentic环境的混合攻击，结合白盒梯度信息与黑盒搜索策略，提升攻击效率；2) 研究跨模型、跨任务的通用对抗后缀，利用元学习或强化学习生成在未见域中转移的提示注入；3) 开发防御机制，如基于任务关键性的动态输入过滤或行为隔离，应对自动化注入的威胁。此外，可改进评估基准，引入多步推理、工具调用交织等更复杂任务，以验证攻击的鲁棒性。

### Q6: 总结一下论文的主要内容

该论文研究了自治环境中针对大语言模型（LLM）自主Agent的自动提示注入攻击。问题定义在于，间接提示注入是Agent与不可信外部数据交互时面临的严重威胁，但现有自动攻击方法在真实Agent环境中的评估不足。方法上，论文扩展了AgentDojo框架，改编了白盒（GCG）和黑盒（TAP）两种攻击方法，在80个任务对（涵盖四个领域和多个模型）上进行了全面评估。主要结论显示：黑盒优化（TAP）显著优于梯度方法（GCG），后者在有限计算预算下优化不稳定；TAP的效果依赖于攻击者模型的能力和安全调优；任务通用攻击可有效迁移至未见任务和领域，但在小开源模型上优化的攻击无法迁移至GPT-5等前沿模型。该研究的核心贡献在于提供了自动化提示注入在Agent环境中的系统评估框架和实证结果，揭示了威胁的模型依赖性，对实际部署安全性具有重要意义。
