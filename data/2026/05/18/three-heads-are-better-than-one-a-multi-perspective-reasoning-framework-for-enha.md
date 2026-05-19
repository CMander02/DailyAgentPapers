---
title: "Three Heads Are Better Than One: A Multi-perspective Reasoning Framework for Enhanced Vulnerability Detection"
authors:
  - "Xin Peng"
  - "Bo Lin"
  - "Jing Wang"
  - "Xiaoling Li"
  - "Jun Ma"
  - "Jie Yu"
  - "Xiaoguang Mao"
  - "Shangwen Wang"
date: "2026-05-18"
arxiv_id: "2605.18153"
arxiv_url: "https://arxiv.org/abs/2605.18153"
pdf_url: "https://arxiv.org/pdf/2605.18153v1"
categories:
  - "cs.SE"
tags:
  - "Multi-agent"
  - "Debate & Collaboration"
  - "Code Agent"
  - "Vulnerability Detection"
  - "LLM Agent"
relevance_score: 8.0
---

# Three Heads Are Better Than One: A Multi-perspective Reasoning Framework for Enhanced Vulnerability Detection

## 原始摘要

Automated vulnerability detection is crucial for enhancing software security by identifying potential flaws that attackers could exploit, thereby reducing the reliance on labor-intensive manual code audits. Recent advancements have shifted towards leveraging large language models (LLMs) for vulnerability detection, with techniques like Vul-RAG and VulnSage demonstrating progress through structured prompting and external knowledge integration. However, these approaches typically rely on a single reasoning paradigm, limiting their ability to address the complex and diverse nature of real-world vulnerabilities. To overcome these limitations, we propose ReasonVul, a novel multi-perspective reasoning framework that harnesses cognitive synergy among three specialized LLM agents, each embodying a distinct reasoning mode. The framework begins with independent analyses of the source code, followed by a structured debate mechanism to resolve conflicts through iterative rebuttal and revision, ultimately converging on a collaborative judgment. Evaluated on the PrimeVul dataset, ReasonVul achieves a PairAcc of 40.00% and an F1-score of 72.52%, surpassing the best baseline by 81.24% in PairAcc. Further tests on the JITVUL dataset confirm its generalizability, with a PairAcc of 28.67%. Additionally, we analyzed 542 conflict cases and found that 389 were correctly resolved, highlighting the framework's ability to uncover hidden vulnerabilities through the error-correction mechanism driven by the debate. This work emphasizes the importance of multi-perspective reasoning and collaborative validation in achieving robust and comprehensive vulnerability detection in real-world software systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有自动化漏洞检测方法中单一推理范式局限性导致检测能力不足的问题。研究背景是随着软件系统规模和复杂度的增加，手动代码审计成本高昂且不适用于快速开发周期，而现有方法如基于程序分析（静态分析、符号执行）的方法受限于路径爆炸和复杂控制流，深度学习方法则对训练数据质量高度敏感且泛化能力有限。近年来，大语言模型（LLM）因具备代码语义理解和上下文推理能力，被用于漏洞检测，并涌现了如Vul-RAG（归纳推理）和VulnSage（溯因推理）等方法。然而，这些方法通常只依赖单一推理模式（如演绎、归纳或溯因），而现实世界中的漏洞具有多样性和复杂性，单一范式无法覆盖所有漏洞类型，导致检测效果受限。核心问题是如何克服单一推理范式的局限，通过整合多种推理机制增强检测的鲁棒性和全面性。为此，论文提出ReasonVul框架，结合三种专用LLM智能体（分别模拟演绎、归纳和溯因推理），通过独立分析、结构化辩论和协作判断来解决冲突，从而更有效地检测复杂漏洞，提升对真实软件系统中隐藏漏洞的识别能力。

### Q2: 有哪些相关研究？

相关研究主要分为两类：一是基于深度学习的方法，包括图结构方法（如Devign通过抽象语法树、控制流图和数据流图构建代码属性图，利用门控图神经网络编码漏洞特征）和基于令牌的方法（如LineVul、VulBERT等使用CodeBERT提取语义特征，MoEVD通过专家混合模型针对特定CWE分解任务）。二是基于大语言模型的方法，包括利用结构化提示（如CoT引导推理）和外部知识增强（如Vul-RAG和VulnSage采用检索增强生成，VulTrial通过法庭角色扮演实现多智能体辩论）。与这些方法不同，ReasonVul的独特之处在于：1）它不采用传统角色扮演，而是让每个智能体体现一种核心认知推理模式（演绎、归纳或溯因），真正模拟人类专家的多维逻辑思考；2）通过结构化的辩论机制实现冲突消解和错误修正，而非简单的相互质疑；3）实验表明，其在PrimeVul和JITVUL数据集上显著优于现有方法，特别是通过辩论在542个冲突案例中正确纠正了389个，展示了多视角推理在复杂漏洞发现中的有效性。

### Q3: 论文如何解决这个问题？

ReasonVul提出了一种新颖的多视角推理框架来解决单范式推理的局限性。核心方法是构建一个由三个专业化LLM智能体组成的多智能体系统，每个智能体采用不同的推理模式：演绎、归纳和溯因。整体框架分为两个阶段。

第一阶段是多视角推理，三个智能体独立并行分析源码。演绎智能体模仿安全审计员，采用自上而下的方式，通过检索增强生成(RAG)机制从SEI CERT C编码标准知识库中检索最相关的安全规则，检查代码是否违规。归纳智能体模拟数据驱动的安全从业者，采用自底向上的模式匹配，通过RAG从ReposVul漏洞库中检索最相似的历史漏洞-修复案例作为上下文示例，推断代码风险。溯因智能体模仿渗透测试人员，不依赖外部知识库，而是利用LLM的内生知识进行结构化思维链(CoT)推理，从假设的负面结果逆向推导代码中的漏洞原因，并进行自我批判。每个智能体输出二分类漏洞判断和自然语言解释。

第二阶段是协作辩论。当三个智能体的初步判断不一致时，系统进入多轮次并行辩论。每轮中，每个智能体会审查同伴的推理链条，特别是与其判断相悖的部分，然后重新评估证据。如果同伴论点有说服力，则修正自身立场；否则，构建反驳来强化原观点。通过这种迭代式反驳和修正机制，智能体逐渐融合观点，最终达成共识。若达成一致则采纳统一判断，若达不成则默认判定为无漏洞。该方法的关键创新在于通过辩论实现认知协同，使系统能从冲突中学习并纠正错误，相比简单多数投票能更深入地整合不同视角。

### Q4: 论文做了哪些实验？

ReasonVul在PrimeVul和JITVUL两个数据集上进行了实验。PrimeVul是函数级基准测试集，包含435个脆弱/修复代码对，涵盖140个CWE类别；JITVUL是仓库级基准，包含1758个配对样本（879个脆弱版本和879个良性版本），涵盖91个CWE。实验对比了两类基线方法：基于学习的方法（CausalVul、DeepDFA、VulChecker、FVD-DPM、Coca、VulSim、LineVul、MoEVD）和基于LLM的方法（SAVul、Vul-RAG、VulnSage、GPTLens、VulTrial）。主要结果方面：在PrimeVul上，ReasonVul达到40.00%的PairAcc和72.52%的F1分数，PairAcc比最佳基线提升81.24%；在JITVUL上，PairAcc为28.67%，验证了泛化能力。此外，对542个冲突案例的分析显示，389个被正确解决（正确率达71.8%），表明辩论驱动的纠错机制能有效发现隐藏漏洞。

### Q5: 有什么可以进一步探索的点？

论文的主要局限性在于推理过程的计算开销较大：三个LLM agent的独立分析加辩论机制需要多次调用模型，可能影响实际部署效率。未来可探索轻量化协同策略，例如将辩论压缩为单轮或多阶段精简交互，或采用知识蒸馏技术将多agent能力迁移至更小的模型。其次，当前框架主要依赖自然语言理解进行辩论，缺乏对代码结构语义的显式建模。可考虑引入程序分析工具（如抽象语法树、数据流图）作为辅助信号，帮助agent在辩论中更精准定位漏洞模式。此外，辩论机制中冲突决议的规则较为固定，可设计自适应终止条件（如根据分歧程度动态调整辩论轮次），或引入强化学习训练agent学会更高效的协作策略。在数据集层面，当前评估仅覆盖PrimeVul和JITVUL，未来需在跨语言、跨项目场景及真实漏洞分布下验证鲁棒性。

### Q6: 总结一下论文的主要内容

ReasonVul提出了一种新颖的框架，旨在解决当前自动化漏洞检测方法仅依赖单一推理范式的局限性。该方法将漏洞检测视为推理过程，并定义了三类推理模式：演绎推理（依据安全规则）、归纳推理（从历史案例中学习模式）和溯因推理（从潜在攻击结果反推原因）。该框架通过三个分别模拟这三种推理模式的大模型智能体，首先对源代码进行独立分析，随后通过一个结构化的辩论机制，让智能体进行迭代的反驳与修正，最终达成协同判断。在PrimeVul数据集上的评估显示，ReasonVul在PairAcc和F1分数上分别达到40.00%和72.52%，显著超越最优基线（VulTrial）81.24%和29.09%。此外，对542个冲突案例的分析表明，辩论机制能正确解决其中72%的冲突，证明了其通过错误修正机制发现隐藏漏洞的能力。这项工作强调了多视角推理和协作验证对于实现更鲁棒、全面的漏洞检测的重要性。
