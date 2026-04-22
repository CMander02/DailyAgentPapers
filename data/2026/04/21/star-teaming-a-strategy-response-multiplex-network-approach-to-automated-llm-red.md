---
title: "STAR-Teaming: A Strategy-Response Multiplex Network Approach to Automated LLM Red Teaming"
authors:
  - "MinJae Jung"
  - "YongTaek Lim"
  - "Chaeyun Kim"
  - "Junghwan Kim"
  - "Kihyun Kim"
  - "Minwoo Kim"
date: "2026-04-21"
arxiv_id: "2604.18976"
arxiv_url: "https://arxiv.org/abs/2604.18976"
pdf_url: "https://arxiv.org/pdf/2604.18976v1"
github_url: "https://github.com/selectstar-ai/STAR-Teaming-paper"
categories:
  - "cs.CL"
tags:
  - "Red Teaming"
  - "Multi-Agent System"
  - "Jailbreak"
  - "Safety"
  - "Black-Box Attack"
  - "Network Optimization"
  - "Automated Testing"
  - "Interpretability"
relevance_score: 8.0
---

# STAR-Teaming: A Strategy-Response Multiplex Network Approach to Automated LLM Red Teaming

## 原始摘要

While Large Language Models (LLMs) are widely used, they remain susceptible to jailbreak prompts that can elicit harmful or inappropriate responses. This paper introduces STAR-Teaming, a novel black-box framework for automated red teaming that effectively generates such prompts. STAR-Teaming integrates a Multi-Agent System (MAS) with a Strategy-Response Multiplex Network and employs network-driven optimization to sample effective attack strategies. This network-based approach recasts the intractable high-dimensional embedding space into a tractable structure, yielding two key advantages: it enhances the interpretability of the LLM's strategic vulnerabilities, and it streamlines the search for effective strategies by organizing the search space into semantic communities, thereby preventing redundant exploration. Empirical results demonstrate that STAR-Teaming significantly surpasses existing methods, achieving a higher attack success rate (ASR) at a lower computational cost. Extensive experiments validate the effectiveness and explainability of the Multiplex Network. The code is available at https://github.com/selectstar-ai/STAR-Teaming-paper.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）自动化红队测试（Red Teaming）中存在的效率与可解释性不足的问题。研究背景是，随着LLM在安全关键领域的广泛应用，评估其对恶意或越狱（jailbreak）提示的抵抗能力变得至关重要。为此，研究者们从人工测试转向了自动化红队方法，以进行规模化、系统化的漏洞评估。现有方法主要分为基于优化的攻击和基于策略的攻击两类，但它们存在两大局限：首先，这些方法通常需要大量计算资源（如重复查询或基于强化学习的优化），限制了可扩展性；其次，基于策略的方法虽然引入了人工设计的攻击模式，但缺乏透明度，它们通常基于嵌入相似性进行采样，而未分析攻击成功背后的因果模式，导致难以精炼攻击策略或深入理解模型漏洞。

针对这些不足，本文提出的核心问题是：如何设计一种既高效（降低计算成本）又具备高可解释性的自动化红队框架，以更系统地生成有效的越狱提示并揭示LLM的策略性漏洞。为此，论文引入了STAR-Teaming框架，其核心创新在于构建了一个策略-响应复用网络（Multiplex Network），将高维且难以处理的嵌入空间重构为可管理的网络结构。该网络显式地捕获攻击策略与LLM响应之间的统计关系，将搜索空间组织成语义社区，从而避免冗余探索，并通过社区层面的概率采样来优化策略选择。这种方法不仅提升了攻击成功率（ASR），还通过映射矩阵直观展示了哪些策略类型在特定模型上下文中持续诱发有害行为，从而增强了漏洞的可解释性。

### Q2: 有哪些相关研究？

本文相关研究主要分为两大类：优化基方法和策略基方法。

在优化基方法中，研究者通常将大语言模型视为白盒系统，通过迭代查询、基于梯度的令牌更新或损失引导反馈等过程生成越狱提示。代表性工作包括GCG、AmpleGCG和COLD-Attack。AutoDAN使用遗传算法优化DAN风格提示。PAIR利用大语言模型的反馈进行迭代提示优化，而TAP通过增加剪枝和分支来加速搜索并提高成功率。这些方法通常计算成本较高，且依赖于模型内部信息。

在策略基方法中，研究者通过预定义或学习到的攻击模式生成提示，关注更高层次的语义变化。例如，PAP、DAN和Many-shot Jailbreaking使用固定模板，而Rainbow Teaming定义了包括情感或间接线索在内的八种策略类型。AutoDAN-Turbo采用多智能体循环，通过攻击-响应-评估周期迭代发现和优化新策略。这类方法提供了更好的语义多样性和可解释性，但通常涉及多个模块，导致计算开销大，且固定结构限制了在新场景中的适应性。此外，基于顺序或嵌入的策略选择常面临搜索效率低、语义相似性与攻击成功率对齐不佳的问题，导致攻击成功率较低。

本文提出的STAR-Teaming框架与上述工作密切相关，但做出了关键改进。它结合了策略基方法的语义多样性和网络化优化思路，通过引入策略-响应多重网络和网络驱动的优化采样，将高维嵌入空间重构为可处理的结构。这既增强了模型策略漏洞的可解释性，又通过将搜索空间组织成语义社区来简化有效策略的搜索，避免了冗余探索。因此，STAR-Teaming在继承策略基方法优势的同时，克服了其计算成本高、适应性有限和搜索效率低的缺点，实现了更高的攻击成功率和更低的时间成本。

### Q3: 论文如何解决这个问题？

论文通过整合多智能体系统（MAS）与策略-响应多重网络，并采用网络驱动的优化方法，解决了自动化红队测试中高效生成越狱提示的难题。其核心方法是将高维且难以处理的嵌入空间重构为可管理的网络结构，从而提升可解释性并优化策略搜索。

整体框架包含两个核心组件：多智能体系统（MAS）和策略-响应多重网络。MAS由三个基于LLM的智能体构成：攻击者、目标和评分器。它们在一个迭代循环中交互：攻击者根据给定种子和选定策略生成修改后的越狱提示；目标模型对此提示作出响应；评分器则根据提示和响应评估攻击是否成功。若评分未达预设阈值，攻击者会更新策略并重试，直至达到最大尝试次数。这一循环实现了对抗提示的自动化生成与评估，极大减少了人工干预。

关键技术在于构建并利用策略-响应多重网络来指导攻击者的策略选择。该网络从历史攻击日志中构建，包含两个层：响应网络和策略网络。构建过程是，首先使用基于LLM的策略提取器从原始日志中提取“（策略，响应）”对的结构化数据集。对于响应网络，计算所有目标响应文本嵌入的相似度矩阵，通过阈值化得到邻接矩阵，再应用Leiden算法识别出响应的语义社区。策略网络以相同方式处理策略名称和定义，识别策略社区。每个响应或策略都用一个社区成员向量（如one-hot编码）表示，从而将高维嵌入映射到离散的社区结构。

创新点体现在基于该多重网络的概率化策略采样机制。通过求解逆伊辛问题，学习一个耦合强度矩阵Z，该矩阵编码了响应社区与策略社区之间的统计关联。给定一个新的目标响应，先将其分配到最相似的响应社区，然后根据矩阵Z和玻尔兹曼分布，计算各策略社区被选中的概率，并据此采样策略。其中引入逆温度参数β来平衡探索与利用。此方法将参数空间大幅缩减至约O(10^3)量级，优化速度快，且能通过评分函数的梯度更新进行终身学习，从成功和失败中持续调整耦合强度。

总之，STAR-Teaming通过将MAS的交互循环与多重网络的社区发现、概率采样相结合，将策略搜索空间组织成语义社区，避免了冗余探索，从而以更低计算成本实现了更高的攻击成功率，并增强了模型脆弱性的可解释性。

### Q4: 论文做了哪些实验？

论文在HarmBench和StrongReject两个数据集上进行了广泛的实验评估。实验设置方面，采用黑盒攻击设定，攻击尝试由评判模型（如Llama-2-13b-cls或微调的Gemma-2b）评估，成功标准为攻击分数超过8.5或达到最大140次重复攻击。对比方法包括GCG、GCG-T、PAIR、TAP、PAP-top5、Rainbow Teaming和AutoDAN-Turbo等主流基线。

主要结果如下：在HarmBench的400个恶意请求上，STAR-Teaming在多个目标模型上取得了显著更高的攻击成功率（ASR）。关键数据指标显示，其平均ASR达到74.5%，优于次优基线AutoDAN-Turbo（61.0%）13.5个百分点。具体而言，在Llama-2-7b-chat上ASR为71.0%，在更具挑战性的Claude-3.5-Sonnet上达到12.0%，是唯一超过10%的方法。此外，实验还验证了复用网络（Multiplex Network）的有效性，其使用使ASR提升约6.0%（从65.0%到71.0%），并提高了攻击多样性（Self-BLEU从0.46降至0.25）。在StrongReject数据集上的实验进一步证实了其优势，平均得分0.52，远超基线TAP的0.11。动态网络扩展实验也显示，动态变体将ASR从71.0%提升至77.3%，同时将平均攻击尝试次数从61.1次降至52.4次，体现了更高的效率。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要在于对提示工程的高度依赖、长期部署中的社区漂移问题以及对单一评分智能体的依赖。未来研究可围绕以下方向展开：首先，可以探索更自动化的提示优化方法，例如利用强化学习或元学习来动态调整智能体的提示，减少人工干预。其次，针对社区漂移，可设计在线社区重检测算法，使网络能实时适应攻击防御格局的变化，而无需周期性重新初始化。此外，虽然集成多个评分智能体成本较高，但可以研究轻量级的校准机制，如定期引入人类反馈或构建更稳健的评估协议，以提升系统的可靠性。从更广泛的视角看，未来工作还可将此类多路网络结构应用于其他安全测试场景，例如对抗性图像生成或代码漏洞挖掘，以验证其通用性和可扩展性。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为STAR-Teaming的新型黑盒框架，用于自动化地对大语言模型进行红队测试，以生成有效的越狱提示。核心贡献在于将多智能体系统与策略-响应多重网络相结合，并利用网络驱动优化来采样高效攻击策略。该方法将原本难以处理的高维嵌入空间重构为可管理的网络结构，从而提升了模型策略漏洞的可解释性，并通过将搜索空间组织成语义社区来避免冗余探索，显著提高了搜索效率。实验结果表明，STAR-Teaming在较低计算成本下实现了更高的攻击成功率，其模块化引导的动态扩展机制使网络能随攻击过程演化，增强了适应性。该工作通过预先识别LLM潜在风险，为AI安全领域提供了有效的自动化评估工具。
