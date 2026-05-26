---
title: "Peak-Then-Collapse and the Four Interface Channels of Knowledge-Graph Tool Use"
authors:
  - "Tianda Sun"
  - "Dimitar Kazakov"
date: "2026-05-25"
arxiv_id: "2605.26037"
arxiv_url: "https://arxiv.org/abs/2605.26037"
pdf_url: "https://arxiv.org/pdf/2605.26037v1"
categories:
  - "cs.CL"
tags:
  - "LLM Agent"
  - "工具使用"
  - "知识图谱"
  - "强化学习"
  - "RLVR"
  - "GRPO"
  - "反馈机制"
  - "智能体训练"
  - "检索增强"
  - "自蒸馏"
relevance_score: 8.0
---

# Peak-Then-Collapse and the Four Interface Channels of Knowledge-Graph Tool Use

## 原始摘要

We test the standard RLVR tool-use recipe -- GRPO on Qwen2.5-7B-Instruct -- on a deliberately minimal knowledge-graph tool API: four Freebase navigation verbs over Complex WebQuestions. Under a self-verifiable retrieval reward, the policy's tool-grounded answer rate climbs from $3.8\%$ to $9.6\%$ over 250 steps, then collapses to $0\%$ within a single 50-step window -- a \emph{peak-then-collapse} pattern replicated across four seeds. Across seven reward designs, we find four recurring failure modes: adding denser or more targeted proxy rewards shifts the failure mode rather than eliminating it. We argue that a key difference from Python interpreters, web search, and JSON APIs is interface feedback: their failures often leak natural-language signal the model saw in pretraining. A Python traceback names the failing line; an empty Freebase result \texttt{[]} does not. Stripping away that surface exposes a degradation regime that same-family reward redesigns do not fix. A direct oracle ablation rules out relation selection: injecting gold relations at every retrieval call lifts exact-match accuracy by only $+0.20$~pp, and $95.4\%$ of retrieval-dependent errors are retrieval-composition failures rather than answer-extraction failures. As a mitigation, one-iteration self-distillation reaches $40.0\%$ EM at 7B and is capacity-invariant: doubling capacity to 14B improves EM by only $0.25$~pp, and initialization barely matters -- the ceiling appears interface-bound within the 7B--14B range tested.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文探讨了在知识图谱工具使用场景中，标准强化学习与可验证奖励（RLVR）训练方法所面临的挑战。当前，将大语言模型训练为智能体的主流方法（如GRPO算法）在代码解释器、网页搜索等接口上表现良好，因为这些接口的失败反馈（如Python的traceback）包含丰富的自然语言信号，模型在预训练阶段已熟悉。然而，知识图谱接口（如Freebase）的失败反馈仅为空列表（`[]`），没有提供任何可理解的语义信息。这种“无信号”的接口导致了严重的训练失败。本文发现的核心问题是“先升后崩”现象：模型在使用工具的正确率从3.8%提升至9.6%后，会在极短的训练步骤内（50步）急剧崩溃至0%。论文通过系统对比七种奖励设计，揭示了四种机制各异的失败模式，并指出在知识图谱这种预训练对齐表面被剥离的接口上，同系列奖励设计的迭代优化无法从根本上解决问题。研究最终定位到模型在检索组合（retrieval composition）环节存在瓶颈，这一瓶颈占到了95.4%的检索相关错误。

### Q2: 有哪些相关研究？

相关工作分为三类：

1. **过程奖励RL与工具使用**：主流方法在具有预训练对齐表面的工具API（如Python解释器）上取得成功，而本文专门测试了剥离自然语言表面的最小知识图谱工具接口，发现相同配方失效。同期工作如GraphWalker（通过增加21K轨迹SFT+BM25+LLM重排序器达到79.6% EM）和Graph-RFT（通过网络回退解决40%知识图谱不完整性问题，达67.2% Hits@1）验证了界面丰富性而非模型容量才是关键差异轴——本文故意采用最小接口作为互补，隔离剥离式KG工具提供的梯度信号。

2. **冷启动SFT后接RL**：本文的自蒸馏方案属于该家族，但方法扩展在于SFT语料是来自自身RL检查点的严格过滤（EM正确∩工具有效∩格式有效）。无规则前缀变体证明仅从基座模型初始化（无需规则SFT或再蒸馏）即可达到40%天花板，验证了ReST-EM在不同任务族上的基座初始化原则。

3. **奖励黑客与智能体RL崩溃**：峰值-崩溃模式扩展了已知的奖励黑客模式。RLHF记录了学习奖励模型层面的代理过度优化；智能体RL诊断包括动作分布熵、奖励方差等。本文的独特贡献在于知识图谱工具智能体上工具调用量从3.0骤降至1.0的步级分辨率特征。

### Q3: 论文如何解决这个问题？

该论文通过一个精心设计的“奖励阶梯”(six-rung ladder)实验框架，系统性地诊断并尝试解决在最小知识图谱(KG)工具使用场景中出现的“先升后崩”(Peak-Then-Collapse)问题。核心方法是在Qwen2.5-7B-Instruct模型上应用GRPO强化学习算法，并让模型通过四个基本Freebase导航动词(get_tail_relations, get_head_relations, get_tail_entities, get_head_entities)访问KG，每次最多进行5次工具调用。

整体框架从最简化的“结果奖励”(R-binary)开始，逐步添加更密集的代理奖励。关键技术包括：R-binary仅基于最终答案的EM/F1给予奖励；R-stepwise增加了语法有效、路径奖励和连贯性奖励；R-toolverbs奖励所有四种动词的使用和结果非空；R-toolverbs·KL通过提高KL散度系数(从0.05升至0.25)来加强策略约束；R-selfV引入基于检索实体的奖励以提升工具使用率；self-distill则对成功轨迹进行自我蒸馏作为SFT预训练。

主要创新点在于：(1) 发现了四种反复出现的失败模式(Mode 1-4)——格式崩溃、仪式性调用、指向漂移和突然悬崖式下降；(2) 揭示了KG工具接口的关键缺陷：其反馈（如空结果`[]`）缺乏自然语言信号，与Python回溯或网页搜索不同，导致模型无法从失败中学习；(3) 证明单纯增加或优化代理奖励只会转移失败模式而非消除它；(4) 通过消融实验表明95.4%的检索依赖错误源于检索组合失败而非答案提取失败，插入金关系仅提升0.20个百分点。最终，单次自我蒸馏方法在保持容量不变性下达到40.0%的精确匹配率，表明在7B-14B容量范围内存在接口导致的性能天花板。

### Q4: 论文做了哪些实验？

论文在Complex WebQuestions（CWQ）数据集（N=3,531）上，使用Qwen2.5-7B-Instruct模型，通过GRPO算法测试了七种奖励设计在知识图谱工具使用上的效果。实验设置了多种对比方法：R-binary（稀疏结果奖励）和R-binary-SR（复现Search-R1配置）均导致格式完全崩溃（EM=0.000）。R-stepwise（分步可验证奖励）达到32.5%的精确匹配率（EM），但工具使用率极低（0.03%），工具调用仅为装饰性。R-toolverbs（工具动词奖励）在100步时短暂成功（EM=32.2%，工具有效调用率CvT=3.03%），随后因格式漂移崩溃。加入KL惩罚的R-toolverbs·KL将稳定窗口延长至400步（EM=38.4%，CvT=3.77%）。核心发现是R-selfV奖励（含自验证检索贡献项）下的“先峰后崩”模式：CvT从3.77%攀升至250步的峰值9.57%后，在50步内骤降至0%，EM同时从39.5%归零。该模式在4个随机种子中复现。作为缓解措施，一次迭代自蒸馏（self-distill）在500步达到40.0% EM（CvT=5.81%），且容量增大至14B仅提升0.25个百分点。Pass@16测试显示，R-toolverbs和R-toolverbs·KL具有11-14个百分点的真实工具增益，而R-stepwise的增益为零。

### Q5: 有什么可以进一步探索的点？

论文在六个方面存在局限：仅测试了Qwen2.5-7B单一家族和7B/14B规模，未探索更大模型（≥32B）或Llama系列；仅在Complex WebQuestions单一基准上训练验证；评估依赖测试集选择checkpoint，存在过拟合风险。未来研究可沿三条路径深入：一是设计能绕过接口僵化瓶颈的新型奖励函数，如将知识图谱查询的空结果转化为可学习的自然语言信号，或引入过程导向的搜索空间剪枝奖励，而非仅依赖结果惩罚；二是探索模型架构级修改，比如让模型在预训练中接触更多结构化查询轨迹，或像“思维树”那样显式建模多步检索组合路径；三是研究跨模型尺寸的缩放规律，目前7B到14B性能饱和表明21B/32B可能揭示新的适应相变。此外，需设计更鲁棒的早停策略防止峰值后崩塌，例如基于验证集熵值或工具调用模式的稳态检测。

### Q6: 总结一下论文的主要内容

本文研究了知识图谱工具使用中强化学习（RLVR）的标准流程，使用Qwen2.5-7B-Instruct模型和最小化Freebase导航API，在自验证检索奖励下训练GRPO。实验发现策略的工具接地回答率从3.8%上升到9.6%后，在50步内骤降至0%，呈现“先升后降”模式，并在四种随机种子中复现。通过七种奖励设计，识别出四种界面层级的失败模式（$L_{sig/lang/comp/prior}$），表明增加密集或更直接的代理奖励仅改变失败模式而非消除。与Python解释器、网络搜索等不同，知识图谱接口反馈缺乏自然语言信号（如空结果`[]`不提供错误信息），导致退化无法通过奖励重设计修复。实验证实95.4%的检索依赖错误源于检索组合失败，而非关系选择或答案提取。作为缓解方案，单次自蒸馏在7B模型上达到40.0%的精确匹配，将容量翻倍至14B仅提升0.25个百分点，表明性能上限受限于接口而非模型容量。该研究揭示了界面反馈设计在工具使用中的关键作用，为未来接口感知训练提供了重要启示。
