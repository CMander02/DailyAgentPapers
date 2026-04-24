---
title: "Transient Turn Injection: Exposing Stateless Multi-Turn Vulnerabilities in Large Language Models"
authors:
  - "Naheed Rayhan"
  - "Sohely Jahan"
date: "2026-04-23"
arxiv_id: "2604.21860"
arxiv_url: "https://arxiv.org/abs/2604.21860"
pdf_url: "https://arxiv.org/pdf/2604.21860v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "多轮攻击"
  - "对抗鲁棒性"
  - "安全评估"
  - "自动攻击智能体"
  - "对话安全"
relevance_score: 9.0
---

# Transient Turn Injection: Exposing Stateless Multi-Turn Vulnerabilities in Large Language Models

## 原始摘要

Large language models (LLMs) are increasingly integrated into sensitive workflows, raising the stakes for adversarial robustness and safety. This paper introduces Transient Turn Injection(TTI), a new multi-turn attack technique that systematically exploits stateless moderation by distributing adversarial intent across isolated interactions. TTI leverages automated attacker agents powered by large language models to iteratively test and evade policy enforcement in both commercial and open-source LLMs, marking a departure from conventional jailbreak approaches that typically depend on maintaining persistent conversational context. Our extensive evaluation across state-of-the-art models-including those from OpenAI, Anthropic, Google Gemini, Meta, and prominent open-source alternatives-uncovers significant variations in resilience to TTI attacks, with only select architectures exhibiting substantial inherent robustness. Our automated blackbox evaluation framework also uncovers previously unknown model specific vulnerabilities and attack surface patterns, especially within medical and high stakes domains. We further compare TTI against established adversarial prompting methods and detail practical mitigation strategies, such as session level context aggregation and deep alignment approaches. Our study underscores the urgent need for holistic, context aware defenses and continuous adversarial testing to future proof LLM deployments against evolving multi-turn threats.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）在安全部署中面临的一种新型多轮攻击威胁。随着LLM被广泛应用于医疗、教育等高风险领域，其安全性至关重要。现有方法通过RLHF等对齐技术提升模型安全，并采用逐轮内容审核来拦截恶意请求。然而，这些方法存在不足：传统单轮越狱攻击容易被检测，而多轮攻击通常依赖维持对话上下文。本文要解决的核心问题是：攻击者能否通过在相互独立的、无状态的多轮交互中分布恶意意图，从而绕过每轮独立的审核机制。作者形式化提出了“瞬时轮次注入”（TTI）攻击，这是一种新颖的多轮攻击方法，攻击者利用辅助LLM作为生成器，仅基于上一轮的响应（而非完整对话历史）迭代地构造看似无害的提示，逐步诱导目标模型泄露敏感信息。该攻击不依赖持续的对话记忆，因此对采用无状态API或受限上下文的系统尤为致命。论文通过自动化黑盒评估，系统地揭示了当前商业及开源LLM在应对这种分布式、无状态的对抗性攻击时的脆弱性，为构建更鲁棒的安全框架提供了重要警示。

### Q2: 有哪些相关研究？

相关研究可以归纳为以下类别：

1. **LLM安全评测与基准类**：如TrustLLM框架，通过结构化分类体系评估多个模型在安全、鲁棒性等方面的表现，揭示了开源与闭源系统在对抗性攻击下的脆弱性差距。本文在此基础上引入瞬态交互这一新维度进行评测。

2. **传统越狱与对抗性提示类**：研究包括MasterKey等通过持续对话上下文的迭代探查诱导有害输出的方法，以及OpenAI、Anthropic等行业领先者的红队测试实践。不同于这些依赖持久上下文的方法，本文提出的瞬态轮注入(TTI)利用**独立的短暂交互**，攻破防御时无需保留对话历史。

3. **对齐技术类**：包括OpenAI的RLHF和安全奖励建模、Anthropic的Constitutional AI、Google DeepMind的Sparrow规则分类器、Meta LLaMA-2的迭代红队测试等。这些方法主要针对持续上下文攻击设计，而TTI利用其忽视**无状态交互**的盲点，揭示了这些对齐策略在瞬态攻击下的局限性。

本文的关键创新在于将攻击维度从持久上下文转向**无状态的多轮瞬态交互**，通过攻击者LLM自适应地基于防守方单次响应生成后续提示，暴露了现有对齐防御在无记忆策略下的脆弱性。

### Q3: 论文如何解决这个问题？

论文提出了一种名为"瞬态轮次注入"(Transient Turn Injection, TTI)的新型多轮攻击方法，通过系统性地利用大语言模型的无状态审核机制来暴露安全漏洞。核心方法是将恶意意图分布在多个独立的交互轮次中，避免在单一轮次触发安全过滤器。

整体框架采用三阶段流水线架构：第一阶段是攻击准备，攻击者提交一个初始的良性种子提示(p0)，确保获得安全的非敏感响应，从而建立对话基础。第二阶段是多轮交互，利用辅助的大语言模型作为攻击提示生成器(A)，根据累积的对话上下文(c_i)自动生成下一个提示(p_i)，形成一个反馈驱动的循环。每个轮次都确保响应被安全函数(S)标记为安全。第三阶段是漏洞利用，当模型在某些轮次无意中泄露敏感内容(k)时，攻击成功，同时所有轮次都通过了安全检查。

关键技术包括：(1) 基于大语言模型的自动攻击智能体，能根据上下文迭代优化攻击提示；(2) 黑盒查询访问，无需模型内部参数；(3) 自适应策略，根据每个新响应微调后续提示。创新点在于：TTI与传统越狱攻击不同，不依赖保持持久对话上下文，而是通过分布式会话实现攻击；该方法能发现模型特定的漏洞和攻击面模式，尤其在医疗等高危领域；论文还提出了会话级上下文聚合和深度对齐等实用缓解策略。

### Q4: 论文做了哪些实验？

论文进行了一系列实验，评估了13个主流LLM在Transient Turn Injection (TTI)攻击下的安全性。实验设置包括：使用Google Colab (Python 3.10, NVIDIA T4 GPU)，依赖pandas、openai等库，通过OpenRouter API和Gemini API调用模型。攻击者提示由gemini-2.0-flash合成，目标模型生成响应。基准测试使用ModifiedMasterKeyJailbreakQuestions.csv，每个提示进行1次种子轮和9次对抗轮。主要评估指标包括：安全/不安全提示和响应的数量和百分比、漏洞类别、TTI和PAIR攻击的命中次数，以及API成本和token使用。对比方法包括PAIR (Prompt Automatic Iterative Refinement)。主要结果：1）在安全响应率方面，Anthropic Claude 3.5 Haiku最高（98%），OpenAI GPT-4.1 Mini和GPT-4o系列为92%，而Gemini系列最低（60-66%）。2）漏洞类别分析显示，几乎所有模型在Adult、Harmful、Medical、Unauthorized Practice和Unlawful类别上存在漏洞，但Political、Government和Misleading类别未发现漏洞。3）TTI可比PAIR揭示更多漏洞：TTI命中数（2-40）远超PAIR（0-8），其中Gemini系列TTI命中数最高（34-40），而Claude 3.5 Haiku的TTI命中数仅为2。实验还提供了详细的API使用成本分析，总成本约5.38美元。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于其黑盒攻击框架未深入探究模型内部注意力机制如何导致跨轮次语义重组，且实验仅覆盖文本模态。未来可从三方面深化：**多模态攻击扩展**，将瞬态注入与视觉、音频模态的跨轮次分片结合，探索多模态语义断层；**防御机制优化**，研究基于因果推断的上下文聚合策略，通过建立跨轮次语义图谱检测隐藏的对抗链；**动态攻击范式**，结合强化学习让攻击Agent自动进化注入策略，突破当前静态模板的局限。此外，可开发**红队自动化工具**量化模型在医疗、金融等高危场景的瞬态脆弱性阈值，并探索联邦学习环境下多轮攻击的分布式特征。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为“瞬态轮次注入”的新型多轮攻击方法，系统性地利用大语言模型在单次交互中的无状态审核机制，通过将恶意意图分散到多个看似孤立的交互中，逐步绕过安全策略。与依赖于维持对话上下文的传统越狱攻击不同，TTI 攻击中的攻击者代理大模型仅基于目标模型的立即前一次响应来生成后续提示，模拟一系列无状态的独立请求。论文对包括 OpenAI、Anthropic、Google Gemini、Meta 在内的商业及开源模型进行了广泛评估，发现不同模型对 TTI 攻击的抵抗力存在显著差异，仅少数架构展现出实质性鲁棒性。该研究揭示了特别是在医疗等高风险领域存在的模型特定漏洞和攻击面模式，并提出了会话级上下文聚合和深度对齐等缓解策略。其核心贡献在于定义并实证了一种新型多轮攻击范式，强调了为抵御此类演变威胁而构建整体性、上下文感知防御及进行持续对抗测试的紧迫性。
