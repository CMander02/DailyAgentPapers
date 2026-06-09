---
title: "The Consistency Illusion: How Multi-Agent Debate Hides Reasoning Misalignment"
authors:
  - "Xiaoyang Wang"
  - "Christopher C. Yang"
date: "2026-06-07"
arxiv_id: "2606.08457"
arxiv_url: "https://arxiv.org/abs/2606.08457"
pdf_url: "https://arxiv.org/pdf/2606.08457v1"
categories:
  - "cs.MA"
tags:
  - "Multi-Agent Debate"
  - "Reasoning Alignment"
  - "Medical QA"
  - "Consistency Evaluation"
  - "Multi-Agent Systems"
relevance_score: 8.5
---

# The Consistency Illusion: How Multi-Agent Debate Hides Reasoning Misalignment

## 原始摘要

Multi-agent LLM systems for medical question answering often treat consensus as a reliability signal: if multiple agents agree on an answer, it is presumed trustworthy. However, answer-level consensus does not entail reasoning-level alignment. We introduce CARA (Cross-Agent Reasoning Alignment), a family of automated metrics that measure whether agents who agree on an answer also agree on the reasoning. Applying CARA to a standard debate system on two medical QA benchmarks, MedQA-USMLE and MedThink-Bench, we identify the consistency illusion: a failure mode where debate reduces detectable contradictions between agents while simultaneously decreasing the semantic similarity of their reasoning chains; agents appear to agree more but reason less consistently. To improve this misalignment, we propose the Grounded Debate Protocol (GDP), a prompt-level intervention that requires agents to commit to named medical facts and take explicit stances on other agents' claims. GDP produces large, consistent alignment improvements, with Cohen's d ranging from +1.43 to +1.99, across two datasets and two backbone models, without adding LLM calls or modifying system architecture. Our results motivate cross-agent reasoning alignment as a quantity to audit alongside accuracy in safety-critical domains.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多智能体LLM系统在医疗问答中存在的“一致性幻觉”问题。研究背景是，当前多智能体医疗问答系统（如MedAgents、MDAgents等）普遍将智能体间的答案共识视为可靠性的信号——如果多个智能体独立得出相同答案，就认为该答案可信。然而，现有方法的不足在于，评估体系主要关注宏观答案准确性和多数投票下的答案一致性，完全忽略了推理层面的一致性。即使多个智能体对答案达成一致，它们的推理链可能基于互斥的医学机制（如对同一症状的治疗依据三种不同药理作用），这种“表面一致、推理矛盾”的模式被称为一致性幻觉。核心问题因此产生：在安全关键的医疗领域，如何检测和量化这种隐藏的推理错位？论文引入了CARA（跨智能体推理对齐）指标体系，通过NLI矛盾检测和嵌入相似度混合方法，专门测量达成答案共识的智能体之间推理链的对齐程度，并发现标准辩论系统在减少表面矛盾的同时，反而加剧了推理链的语义分歧。

### Q2: 有哪些相关研究？

相关研究可分为三类。第一类是医疗问答中的多智能体系统，如MedAgents、MDAgents、MCC、TeamMedAgents及Agent Hospital等，它们将多智能体答案层面的共识视为可靠推理的代理指标，但本文指出这些系统从未审计共享相同选项的智能体是否具有一致的底层推理逻辑。

第二类是对多智能体辩论的批判研究，部分工作从理论上证明辩论动态形成鞅结构，其增益归因于多数投票而非实质推理；还有研究记录特定故障模式，如答案抄袭、奉承性回答切换和多轮对话质量下降。与本文最相关的“问题漂移”文献关注辩论性能随轮次退化，而CARA提出互补问题：当共识达成时，底层推理是否对齐？前者攻击辩论过程，本文攻击对辩论结果的假设。

第三类是单智能体推理评估方法，如CoT截断、错误注入探针、ROSCOE、NLI忠实度检查和CC-SHAP等，它们用于验证单个模型输出的推理链，但均未测量共享答案的多个智能体之间的推理对齐程度。本文填补了这一空白，提出跨智能体推理对齐作为安全关键领域与准确性并行的审计指标。

### Q3: 论文如何解决这个问题？

论文通过提出CARA（跨主体推理对齐）度量框架和GDP（基于事实的辩论协议）干预方法，解决了多智能体辩论中表面答案一致但推理错位的问题。CARA的核心思想是衡量达成同样答案的智能体之间的推理链语义一致性，而非仅仅检查答案正确性。其架构包括：首先将每个智能体的推理链分割为步骤序列，然后构建对齐矩阵计算步骤对之间的NLI（自然语言推理）标签和余弦相似度，其中混合度量CARA_hyb采用“矛盾覆盖相似度”策略，即若NLI检测到矛盾则直接赋值-1，否则使用语义相似度。通过最佳匹配对齐和对称化平均处理长度不等的推理链，最终在问题级别和语料库级别聚合得分。CARA还引入矛盾率指标衡量推理链中矛盾步骤的比例，用于识别“一致性幻觉”——即辩论虽减少了表面矛盾但降低了推理相似度。

针对此问题，论文提出GDP协议干预。GDP要求每个智能体在独立轮次输出结构化字段：命名为“声明”（原子化的临床断言）和“依据”（具体医学事实或机制），在辩论轮次中增加“立场”（同意/反对/扩展），反对时必须提供反向依据。同时加入反谄媚规则，要求智能体仅在发现更有力的依据或自身错误时才能改变答案。GDP仅通过提示工程实现，不增加LLM调用次数或修改系统架构，仅增加约9%的token开销。实验表明GDP在两个医疗QA基准和两种骨干模型上，使用科恩d系数衡量均产生1.43到1.99的大幅一致性提升，且无需额外计算成本。

### Q4: 论文做了哪些实验？

论文在多智能体医疗问答系统中进行了一系列实验，探究“一致性幻觉”现象，并提出跨智能体推理对齐指标CARA和干预协议GDP。实验设置包括三种系统：M3（对称单轮辩论）、M4（无交流的独立投票对照组）和M3-GDP（在M3基础上采用GDP提示格式）。使用两个医疗QA基准数据集：MedQA-USMLE（500个四选一问题）和MedThink-Bench（499个多选问题，选项3-10个）。主要骨干模型为Qwen 2.5 72B Instruct，并在MedThink的100个样本上用Llama 3.3 70B Instruct进行跨骨干模型验证。

对比方法方面，CARA通过NLI硬过滤（DeBERTa-v3）和句子嵌入余弦相似度（Stella）测量推理对齐，包括HYB（综合对齐）、SIM（语义相似度）和CR（矛盾率）。主要结果：标准辩论（M3 r1）在辩论后出现一致性幻觉——矛盾率显著降低（如MedQA上CR从0.104降至0.035），但语义相似度也下降（SIM从0.801降至0.787），表明“看似更一致但推理更不一致”。相比之下，GDP协议（M3-GDP r1）产生真正的对齐提升：SIM显著上升（0.835→0.912）同时CR下降（0.117→0.098）。Cohen's d效应量分析显示GDP带来大规模对齐改进，范围从+1.43到+1.99（跨数据集和骨干模型）。在专家推理对齐（cara-GT）上，GDP使智能体向专家推理移动（d=+0.32），而标准辩论使其偏离（d=-0.21）。失败模式分析表明，GDP消除了严重模式（如互补推理、迎合性收敛）共34/50和33/50案例，将残余错位转移到轻度基线。

### Q5: 有什么可以进一步探索的点？

根据论文的分析，其局限性和未来探索方向主要体现在以下几个方面。首先，CARA指标的“一致性集合”定义依赖离散答案匹配，这限制了其在自由形式临床任务（如鉴别诊断）中的应用，未来需要扩展到非选择题场景。其次，研究仅使用了两种70B级开源模型，未验证GPT-4o等闭源模型，这关系到一致性幻觉的普遍性。第三，论文明确指出，所提出的GDP干预主要提升推理一致性而非答案准确性，这提示未来需探索对齐与准确率之间的权衡关系。最后，当前实验基于对称单轮辩论协议，未来有必要检验在其他拓扑结构（如非对称角色、多轮辩论）下一致性幻觉是否依旧存在，以及GDP的矫正效果是否稳定。从个人见解出发，可以尝试将CARA与思维链的可视化结合，开发出更直观的推理矛盾检测工具，或者设计自适应的GDP机制，根据代理间的实时对齐状态动态调整立场要求。

### Q6: 总结一下论文的主要内容

这篇论文揭示了多智能体LLM系统在医疗问答中的一个关键缺陷，即“一致性错觉”：当多个智能体在答案层面达成共识时，其背后的推理逻辑可能并不一致，甚至相互矛盾。作者指出，现有评估仅关注答案准确率，忽略了推理对齐性。为此，他们提出了CARA（跨智能体推理对齐）指标族，通过结合NLI矛盾检测和嵌入相似性，自动量化达成共识的智能体在推理步骤上的对齐程度。实验表明，在MedQA-USMLE和MedThink-Bench基准上，标准辩论流程虽减少了智能体间的显性矛盾，却降低了其推理链的语义相似性，即产生了“一致性错觉”。为缓解此问题，论文提出了“基于事实的辩论协议”（GDP），该轻量级提示干预要求智能体在每一步推理中明确引用医学事实并对他人主张表明立场。实验证明，GDP在无需额外LLM调用或修改架构的情况下，显著提升了跨智能体的推理对齐度（Cohen's d介于+1.43至+1.99）。该工作首次揭示了多智能体共识的可靠性假象，并提供了切实可行的审计与改进方案，对安全关键领域（如医疗）的AI系统评估具有重要意义。
