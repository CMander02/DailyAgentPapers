---
title: "An Empirical Study of Privacy Leakage Chains via Prompt Injection in Black-Box Chatbot Environments"
authors:
  - "Hongjang Yang"
  - "Hyunsik Na"
  - "Daeseon Choi"
date: "2026-05-18"
arxiv_id: "2605.18133"
arxiv_url: "https://arxiv.org/abs/2605.18133"
pdf_url: "https://arxiv.org/pdf/2605.18133v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.HC"
  - "cs.IR"
tags:
  - "LLM Agent安全"
  - "提示注入"
  - "隐私泄露"
  - "黑盒攻击"
  - "工具使用agent"
relevance_score: 8.0
---

# An Empirical Study of Privacy Leakage Chains via Prompt Injection in Black-Box Chatbot Environments

## 原始摘要

LLM-based chatbot agents increasingly process user requests by combining natural-language reasoning with external tools such as web browsing. These capabilities improve usability, but they also create attack surfaces when untrusted external content is processed as part of a user' s task. This paper studies a privacy-leakage attack chain based on indirect prompt injection in black-box chatbot environments, where the attacker has no access to model weights, system prompts, or agent implementation details including how a trajectory is actually managed during its processing for a query. We first analyze how an attacker can hijack an agent' s intended task by crafting external content that appears benign to the victim while inducing the agent to execute an attacker-defined objective. We then evaluate a new prompt-injection technique, called exemplification, which uses a bridge in the external content to reframe the user prompt and the benign beginning of the retrieved page as few-shot examples before appending the attacker' s objective. We compare its attack success rate with a prior fake-completion technique. Finally, we demonstrate a proof-of-concept data-exfiltration chain using fictitious personal information in a controlled setting. Our results suggest that prompt injection, jailbreak-style instruction steering, and web-tool invocation can be combined into a feasible privacy-leakage path in deployed chatbot agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于LLM的聊天机器人助手在处理用户请求时，因使用外部工具（如网页浏览）而引入的隐私泄露安全问题。研究背景是，这类智能体通过结合自然语言推理和外部工具调用提升了可用性，但也创造了攻击面：当不受信任的外部内容作为用户任务的一部分被处理时，可能被恶意利用。

现有方法的不足在于，虽然已有针对提示注入攻击的研究，但大多关注单次注入事件，缺乏对完整攻击链的深入分析；同时，在攻击者无法访问模型权重、系统提示或智能体实现细节的黑盒环境中，隐私泄露的风险尚未被充分评估。

本文的核心问题是：在黑盒聊天机器人环境中，仅控制外部内容的攻击者能否通过间接提示注入，诱导智能体偏离受害者目标，形成一条完整的隐私泄露攻击链？为此，论文提出了一种新的提示注入技术——示例化（exemplification），并验证了其与网络工具调用相结合，从外部内容欺骗、指令劫持到数据外泄的可行性。

### Q2: 有哪些相关研究？

与本文相关的研究主要可分为三类。**方法类**方面，本文提出了一种新的提示注入技术"exemplification"，与先前的"fake-completion"技术（如Kang等人在2023年的工作）形成对比。**应用类**方面，本文聚焦基于LLM的聊天机器人中的隐私泄露链，这与Petri等人在2024年研究的平台特定ChatGPT数据窃取、Yang等人对工具调用代理中个人数据泄露的基准测试，以及Oh等人在2024年提出的零点击或隐式出口攻击等生产环境攻击链互补。**评测类**方面，本文在黑盒环境中系统评估了攻击成功率，与Liu等人对NeurIPS 2023红队挑战中提示注入的评测类似。**核心关系与区别**：现有工作大多分别研究提示注入的某个环节（如指令-数据边界破坏、工具调用漏洞），而本文首次将间接提示注入、越狱式指令操控和网络工具调用整合成一条端到端的可行隐私泄露链，特别强调了在攻击者无法访问模型权重、系统提示或代理实现细节的黑盒环境中的实际威胁。此外，本文的"exemplification"技术通过将用户提示和网页内容重构为少样本示例来隐蔽地注入攻击目标，这是对传统提示注入方法的重要扩展。

### Q3: 论文如何解决这个问题？

本文通过提出一种名为"exemplification"的提示注入技术，结合越狱引导和网络工具调用，构建了一条完整的隐私泄露攻击链。核心方法包括三个关键步骤：首先，利用CSS样式隐藏等技术制造视觉欺骗，让受害者看到的网页内容看似安全无害，而智能体读取的HTML文本中已嵌入恶意指令，实现用户感知与代理处理内容之间的信息不对称；其次，实施任务劫持，通过精心设计的外部内容，将受害者原始目标重新定义为攻击者目标，其中关键创新是"exemplification"技术——在外部内容中构建"桥接结构"，将用户提示和检索页面的良性开头重新组织为少样本示例，随后附加攻击者的目标指令，相比以往的"fake-completion"技术可显著提升攻击成功率；最后，实施越狱辅助的隐私泄露子目标，因为直接要求通过URL泄露个人信息通常会被拒绝，攻击者通过中间外部内容引入越狱令牌，诱导智能体执行将私有信息编码到URL查询参数并调用网络工具的行为，使得攻击者服务器可通过日志记录获取泄露的数据。该方法具有模块化特性，注入技术可根据实际威胁模型灵活替换，实验在受限的黑盒环境下验证了该链路的可行性。

### Q4: 论文做了哪些实验？

论文进行了两个实验。第一个实验测量单次提示注入的攻击成功率，对比了所提“示范法”（exemplification）与先前的假完成（fake completion）技术。实验在基于ChatGPT 5.3的聊天机器人上进行，用户提示和注入片段使用韩语。假完成在136次尝试中成功4次（约3%），而示范法在168次尝试中成功121次（约72%），成功率约为前者的24倍。第二个实验评估完整的数据泄露链是否可应用于已部署的聊天机器人服务，在ChatGPT 5.2上进行概念验证。攻击链包括：1）攻击者控制页面嵌入隐藏指令；2）指令将代理重定向至包含越狱指令的中间资源（基于JailMine的token级操纵）；3）代理构造并访问包含虚构个人信息作为查询参数的URL。实验通过服务器日志确认了虚构信息可被嵌入URL请求参数并被观测到。该实验定性评估了三个标准：在当前环境中可复现、受害者可能暴露于攻击、具体私人信息可被泄露。结果表明提示注入可与工具调用结合形成实际数据泄露渠道。

### Q5: 有什么可以进一步探索的点？

基于论文的分析，未来研究可以从以下几个方向深入探索。首先，论文的局限性在于固定用户提示场景，未来应研究更动态、更复杂的用户意图下注入攻击的自适应性和成功率，例如结合多轮对话上下文推理。其次，可探索跨语言、跨模型的攻击泛化能力，当前韩语实验的结果可能受文化或语法特征影响，需在英语、中文等语言及开源模型中验证“范例化”技术的有效性。此外，攻击链中“越狱”原语的成功率是关键瓶颈，未来应尝试与高成功率的越狱方法耦合，如基于对抗性后缀或思维链的诱导，以实现端到端的数据泄露。在防御层面，可设计更鲁棒的内容与指令边界检测机制，例如利用形式化语法严格隔离外部内容中的示例；或者引入数据流追踪，仅在工具调用前对敏感信息进行匿名化处理。最后，可探索多代理系统中攻击的传播性，如一个被劫持的代理如何通过工具调用链感染其他代理，这对实际部署的鲁棒性至关重要。

### Q6: 总结一下论文的主要内容

这篇论文研究了黑盒聊天机器人环境中通过提示注入实现隐私泄露的攻击链。问题定义上，作者关注基于LLM的聊天代理在处理用户请求时集成外部工具（如网页浏览）所带来的安全风险，攻击者可通过操控外部内容实现隐私窃取。方法上，论文提出了一种名为"exemplification"的新提示注入技术，该技术通过外部内容中的桥接方式，将用户提示和检索页面的良性开头重构为少样本示例，再附加上攻击者目标，并与已有fake-completion技术进行攻击成功率对比。主要结论表明，在单一注入实验中，exemplification技术的攻击成功率显著高于fake-completion；进一步的PoC验证了通过提示注入、越狱式指令引导和网络工具调用组合形成的可行隐私泄露路径。该研究揭示了黑盒环境中隐私泄露链的可行性，强调了加强指令与数据分离、工具使用安全控制等防御措施的重要性。
