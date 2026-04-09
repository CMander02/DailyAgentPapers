---
title: "SkillTrojan: Backdoor Attacks on Skill-Based Agent Systems"
authors:
  - "Yunhao Feng"
  - "Yifan Ding"
  - "Yingshui Tan"
  - "Boren Zheng"
  - "Yanming Guo"
  - "Xiaolong Li"
  - "Kun Zhai"
  - "Yishan Li"
  - "Wenke Huang"
date: "2026-04-08"
arxiv_id: "2604.06811"
arxiv_url: "https://arxiv.org/abs/2604.06811"
pdf_url: "https://arxiv.org/pdf/2604.06811v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Security"
  - "Backdoor Attack"
  - "Skill-Based Agent"
  - "Compositional Reasoning"
  - "Adversarial Robustness"
  - "Code Agent"
  - "Security Evaluation"
relevance_score: 8.0
---

# SkillTrojan: Backdoor Attacks on Skill-Based Agent Systems

## 原始摘要

Skill-based agent systems tackle complex tasks by composing reusable skills, improving modularity and scalability while introducing a largely unexamined security attack surface. We propose SkillTrojan, a backdoor attack that targets skill implementations rather than model parameters or training data. SkillTrojan embeds malicious logic inside otherwise plausible skills and leverages standard skill composition to reconstruct and execute an attacker-specified payload. The attack partitions an encrypted payload across multiple benign-looking skill invocations and activates only under a predefined trigger. SkillTrojan also supports automated synthesis of backdoored skills from arbitrary skill templates, enabling scalable propagation across skill-based agent ecosystems. To enable systematic evaluation, we release a dataset of 3,000+ curated backdoored skills spanning diverse skill patterns and trigger-payload configurations. We instantiate SkillTrojan in a representative code-based agent setting and evaluate both clean-task utility and attack success rate. Our results show that skill-level backdoors can be highly effective with minimal degradation of benign behavior, exposing a critical blind spot in current skill-based agent architectures and motivating defenses that explicitly reason about skill composition and execution. Concretely, on EHR SQL, SkillTrojan attains up to 97.2% ASR while maintaining 89.3% clean ACC on GPT-5.2-1211-Global.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在揭示并系统化研究基于技能的智能体系统中一个尚未被充分审视的安全漏洞：针对可复用技能实现的后门攻击。研究背景是，当前基于技能的智能体架构已成为主流设计范式，智能体通过组合封装了过程逻辑、工具调用和执行工作流的可复用技能来完成任务，这提高了模块化和可扩展性，并催生了广泛的智能体框架和技能市场。然而，现有安全研究主要集中在传统的后门攻击向量上，例如通过污染数据或修改参数来操控模型本身，或者通过提示词、规划上下文以及工具/内存接口等控制信道来诱导恶意行为。这些方法的评估和防御大多仍孤立地关注模型的可观测行为或特定交互界面。

现有方法的不足在于，它们普遍忽视了一个独特且未被充分检查的控制点：即那些封装了可执行逻辑、并能在不同任务、用户和部署中持久存在的可复用技能实现。由于技能作为被信任的模块化组件，其内部行为很少受到与模型输出同等程度的审计，这就在当前智能体安全假设中留下了一个关键盲区。攻击者可以通过在看似良性的技能中嵌入恶意逻辑，并利用标准的技能组合来重构和执行攻击载荷，从而创建一个新的、隐蔽的后门攻击向量。

因此，本文要解决的核心问题是：如何系统性地在基于技能的智能体系统中，针对技能抽象层（而非模型参数或训练数据）实施和评估后门攻击。具体而言，论文提出了SkillTrojan攻击范式，它将攻击者指定的有效载荷嵌入到技能中，并将其分割为加密片段分散在多个看似良性的技能调用里，仅在满足预定义触发条件时才重构并执行恶意载荷。论文旨在证明这种技能层后门攻击在保持良性任务性能的同时，可以达到很高的攻击成功率，从而暴露当前技能型智能体架构中的一个关键安全盲点，并推动需要显式考虑技能组合与执行的防御机制的发展。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大方向。

在方法类研究中，传统机器学习后门攻击主要针对模型本身，通过污染训练数据、操纵参数或植入触发输入来诱导恶意行为。近期研究将此类攻击扩展至智能体系统，出现了提示注入、恶意工具描述、记忆污染和智能体控制逻辑操纵等方法。这些方法大多作用于瞬态交互层面，如单次对话中的提示或工具调用。

在应用类研究中，基于技能的智能体系统研究主要聚焦于提升智能体能力、规划效率和组合泛化性，通常将可执行技能视为可信组件，仅关注功能正确性而缺乏安全审计。现有安全分析多集中于模型输出、提示或高层规划行为，对持久化、可重用执行抽象层引入的风险关注不足。

本文与这些工作的核心区别在于攻击面不同。SkillTrojan 直接针对智能体的执行层，将后门嵌入可重用的可执行技能内部，而非操纵模型行为或单次工具调用。这使得恶意逻辑能通过正常的技能组合在常规执行中激活，并持久存在于不同任务和部署中，超越了现有主要监控模型输入输出或孤立交互通道的防御机制范围，揭示了当前智能体执行流水线安全分析的根本性空白。

### Q3: 论文如何解决这个问题？

SkillTrojan通过一种分层的、隐蔽的后门攻击方法来解决针对技能型智能体系统的安全问题。其核心思想不是直接篡改模型参数或训练数据，而是在技能的实现层面嵌入恶意逻辑，并利用系统固有的技能组合机制来重构和执行攻击者指定的恶意负载。

整体框架分为三个关键阶段：负载准备与隐藏、技能规范修改与执行时触发、以及负载重构与执行。首先，攻击者指定的任意可执行负载程序P会使用密钥k进行对称加密，生成密文C。接着，该密文被编码并分割成N个片段{c1, ..., cN}，每个片段包含一个索引标识和一段加密的负载数据。这种分片设计是关键技术之一，它使得负载的重构不依赖于智能体规划器的调用顺序或控制流，从而增强了隐蔽性。

在技能层面，攻击方法修改了原始技能模板s=(m, A)。对于自然语言规范m，通过注入由触发谓词Trig_τ(q)参数化的条件控制逻辑，将其修改为˜m。在非触发查询下，˜m与m语义等价，保证正常功能。在触发查询下，˜m会轻微地引导智能体产生包含特定动作子集{a_i1, ..., a_iN}的执行轨迹，但这些修改完全在智能体正常的规划和分解机制内进行，不包含显式的恶意指令。

在执行层面，可执行组件A被植入代码，修改为˜A。每个被选定的动作˜a_ij在正常执行其原有功能的同时，当查询被触发时，会额外将对应的负载片段c_j写入技能执行上下文的中间存储中。这些片段被巧妙地隐藏在工具输出的良性字段里，成为智能体工具调用轨迹的一部分，从而避免引起怀疑。一个专门设计的验证动作会监控执行状态，检查是否所有N个片段都已收集完毕。由于每个片段带有索引，验证仅依赖于集合包含关系，无需考虑执行顺序。一旦集齐所有片段，系统便按索引拼接片段、解密并最终执行恢复出的负载P。整个恶意行为是正常任务完成的副作用，智能体仍为用户查询生成正确且良性的输出，这极大地增加了检测难度。

该方法的创新点在于：1）攻击面从模型/数据转移到了技能实现层，利用了技能组合这一系统设计特性；2）提出了“分片-隐蔽传输-条件重构”的执行流程，将恶意负载的激活与常规工作流的完成对齐，而非依赖单个异常动作；3）支持从任意技能模板自动合成后门技能，实现了攻击在技能生态中的可扩展传播。实验结果表明，该方法在保持高良性任务准确率（如在GPT-5.2上ACC为89.3%）的同时，能实现极高的攻击成功率（ASR达97.2%），验证了其有效性和隐蔽性。

### Q4: 论文做了哪些实验？

论文在基于代码的技能执行环境中评估了SkillTrojan。实验设置中，技能以包含自然语言规范文件和可执行工具脚本的包形式分发。攻击通过毒化部分工具实现，使其仅在触发谓词成立时输出加密的有效载荷片段，随后由指定的验证工具收集、重构并执行。默认参数包括毒化比例ρ=0.2、片段数量N=3，并使用Xor+Base64进行轻量级加密编码。

主要数据集和基准测试包括：1）EHR SQL任务，要求智能体根据临床查询生成并执行SQL，通过LLM作为评判者比较执行结果来评估清洁任务准确率（ACC）和攻击成功率（ASR）；2）SWE-Bench Verified软件工程基准（附录中详述），用于验证攻击在非SQL任务上的泛化性。评估模型涵盖开源模型（如GLM-4.7、Qwen3-Coder）和闭源模型（如GPT-4o-Mini、Claude-Sonnet4.5、GPT-5.2-1211-Global），所有模型均作为智能体的规划与工具选择策略模型。

对比方法包括适应到技能型智能体环境的现有攻击基线：GCG、AutoDAN、CPA、BadChain和AgentPoison，这些方法在相同触发插入过程、毒化比例和工具环境下进行评估。

主要结果显示：SkillTrojan在保持高清洁任务性能的同时实现了高攻击成功率。例如在GPT-5.2-1211-Global上，ASR达97.2%，ACC为89.3%（非攻击条件下ACC为73.0%）；在Qwen3-Max上ASR为74.7%，ACC为86.6%。与基线相比，SkillTrojan在ACC-ASR权衡上表现更优：例如在GPT-5.2-1211-Global上，最强基线AgentPoison的ASR最高仅58.3%，且部分基线（如CPA、AutoDAN）在提升ASR时显著降低了ACC。消融实验表明，片段数量N=3时ASR最高，加密方案切换对ACC和ASR影响微小（差异<0.3%），但能显著降低基于Base64的启发式检测器的标志率（从78%降至21%）。

### Q5: 有什么可以进一步探索的点？

本文揭示了技能层后门攻击的有效性，但其局限性与未来研究方向仍值得深入探索。首先，当前研究主要在代码型智能体（如SQL生成）中进行验证，未来需拓展至更广泛的技能类型（如API调用、工具使用）和智能体框架（如AutoGPT、CrewAI），以评估攻击的普适性。其次，防御机制仅被简要提及，亟需开发系统性的防护方案，例如动态沙箱执行、技能来源认证、异常行为检测等，并量化这些措施对正常任务性能（ACC）与攻击成功率（ASR）的权衡影响。此外，攻击假设技能可被恶意修改，但实际技能生态中可能存在代码审查或安全扫描，未来可研究更隐蔽的触发机制（如基于时序或外部信号的触发）以提升攻击的隐蔽性。最后，论文提出的数据集和框架为后续研究奠定了基础，可进一步探索自动化防御生成、多智能体协作场景下的攻击传播，以及从形式化验证角度对技能组合进行安全约束，从而构建更鲁棒的技能基智能体系统。

### Q6: 总结一下论文的主要内容

这篇论文提出了SkillTrojan，一种针对基于技能的智能体系统的新型后门攻击方法。其核心问题是：当前基于技能的智能体系统通过组合可复用技能来处理复杂任务，虽然提升了模块化和可扩展性，但也引入了一个尚未被充分审视的安全攻击面。SkillTrojan的创新之处在于，它不攻击模型参数或训练数据，而是直接针对技能实现本身进行攻击。

该方法的核心思想是：将恶意逻辑嵌入到看似正常的技能中，并利用标准的技能组合机制来重构和执行攻击者指定的恶意载荷。具体而言，攻击将一个加密的载荷分割到多个看似良性的技能调用中，并且仅在满足预定义触发条件时才被激活。此外，SkillTrojan支持从任意技能模板自动合成被植入后门的技能，这使得攻击能够在基于技能的智能体生态系统中大规模传播。

论文的主要结论是，技能层面的后门攻击非常有效，能在几乎不影响正常任务性能（在GPT-5.2-1211-Global上保持89.3%的清洁任务准确率）的同时，实现极高的攻击成功率（在EHR SQL任务上达到97.2%）。这揭示了当前基于技能的智能体架构中存在一个关键的安全盲点，并强调了未来防御机制需要明确地对技能组合与执行过程进行安全推理。
