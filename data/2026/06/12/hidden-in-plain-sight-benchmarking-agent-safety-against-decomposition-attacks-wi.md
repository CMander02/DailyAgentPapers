---
title: "Hidden in Plain Sight: Benchmarking Agent Safety Against Decomposition Attacks with DECOMPBENCH"
authors:
  - "Vikhyath Kothamasu"
  - "Virginia Smith"
  - "Chhavi Yadav"
date: "2026-06-12"
arxiv_id: "2606.13994"
arxiv_url: "https://arxiv.org/abs/2606.13994"
pdf_url: "https://arxiv.org/pdf/2606.13994v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent安全"
  - "对抗攻击"
  - "基准测试"
  - "任务分解"
  - "安全评估"
relevance_score: 8.5
---

# Hidden in Plain Sight: Benchmarking Agent Safety Against Decomposition Attacks with DECOMPBENCH

## 原始摘要

LLM-based Agents are becoming increasingly capable and widely deployed, creating growing incentives for adversarial misuse in the real-world. A key emerging threat is Decomposition Attacks \cite{glukhov2024breach, jones2024adversaries} in which a harmful task is broken into simpler, benign subtasks that evade safety mechanisms when executed separately but cumulatively fulfill the malicious intent. Although recent benchmarks assess agent safety in multi-turn and multi-tool-use settings, they do not explicitly capture this form of decompositional misuse and may not represent realistic adversarial execution flows. To this end, we introduce DeCompBench, a benchmark designed specifically to evaluate agentic safety under decomposition attacks. DeCompBench is created with a decomposition-by-design principle using a graphical framework and enables harmful task decomposition into individually benign and executable subtasks with realistic workflows. Our experiments using a custom decomposer show that state-of-the-art agents exhibit high refusal rates on monolithic harmful tasks, but significantly lower refusal rates on their decomposed variants, while often inadvertently fulfilling the adversarial objectives. These findings underscore the need for safety evaluations against decomposition attacks and corresponding defenses. Our dataset is publicly available and can be found at https://huggingface.co/datasets/decompositionbench/DeCompBench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大语言模型（LLM）智能体在面对分解攻击（Decomposition Attacks）时的安全性评估问题。研究背景是，随着LLM智能体能力日益增强并被广泛部署，它们成为对抗性滥用的目标。现有方法虽已关注多轮、多工具场景下的智能体安全基准测试，但并未专门针对分解攻击进行设计。分解攻击的核心威胁在于，攻击者将一个有害任务拆解为一系列看似无害的子任务，每个子任务单独执行时能绕过安全机制，但累积起来却实现了恶意意图。现有安全基准的不足在于：其任务并非为分解攻击量身定制，导致子任务可能仍暴露有害意图、需要不自然的转换，且无法反映攻击者在真实世界中采用的执行流程，从而可能得出误导性的安全性评估。为解决这一核心问题，本文提出了DeCompBench——一个专门评估智能体在分解攻击下安全性的基准测试框架。该基准采用“分解优先设计”原则，利用图形化框架确保有害任务能够被分解为相互依赖、单独无害且可执行的子任务，并涵盖多种真实世界系统（如版本控制、数据库等）中的8类危害场景。通过实验，作者发现当前最先进的LLM智能体对单一有害任务的拒绝率很高，但对其分解变体的拒绝率显著降低，且经常无意中完成攻击目标，这揭示了现有安全防护的局限性。

### Q2: 有哪些相关研究？

与本文最相关的研究可从三类工作理解。**方法类**中，Glukhov等和Jones等首次验证了LLM的分解攻击可行性，但仅聚焦于语言模型本身。本文扩展至具有工具调用能力的智能体，强调现实工作流中的分解风险。**评测类**中，OpenAgentSafety（OAS）和MT-AgentRisk是最接近的基准：OAS虽涵盖多轮多工具场景，但未专门设计分解攻击测试，且恶意任务仅99个；MT-AgentRisk通过转换算子将单轮任务转化为多轮攻击，但其子任务需保留对话历史，而本文的子任务独立、无需上下文继承，更贴近真实攻击执行流程。此外，OAS和MT-AgentRisk的任务来源并非天然可分解，本文通过图框架构建的250个恶意任务则天生具有可分解性，且单体任务拒绝率更高。**防御类**工作如状态缓冲和ToolShield尝试缓解分解攻击，但本研究明确将防御留作未来工作，专注于构建衡量此类攻击易感性的真实基准。

### Q3: 论文如何解决这个问题？

该论文提出DeCompBench基准来评估LLM代理在面对分解攻击时的安全性。核心方法是“分解即设计”原则，通过图形框架确保有害任务能被分解为一系列单独良性的子任务。

整体框架包含四个阶段的构建流程：第一阶段创建能力目录，从服务环境中枚举335个原子能力，并标注角色标签；第二阶段手动策划101个种子任务，覆盖8种攻击类别，每个种子任务包含手工设计的DAG模板；第三阶段将种子DAG实例化为具体能力图，通过拓扑排序分配能力，并自动插入桥接能力以处理类型不兼容，同时设置多样性过滤和LLM真实性检查；第四阶段使用GPT-4o生成自然语言任务描述，确保描述只表述最终目标而非步骤指令。

关键技术方面，论文设计了专门的任务分解器，采用两种核心转换：中间间接法将有害值与操作分离，通过中间文件传递；逐步包装法将有害操作隐藏在中性产物中。实验表明，当前最先进的代理对单一有害任务的拒绝率很高，但对分解后的变体拒绝率显著降低，往往无意中完成了对抗目标。该基准包含250个任务，平均每个任务分解为5.98个子任务，涵盖8种攻击类型，涉及平均2.64个服务，有效模拟了现实场景。

### Q4: 论文做了哪些实验？

论文使用DeCompBench基准测试评估了分解攻击对LLM智能体的影响。实验设置：通过OpenHands框架部署了GPT-5-mini、Claude Haiku 4.5和Qwen3-Coder三个智能体，在默认安全配置下测试。数据集为作者构建的DeCompBench，包含经分解设计的恶意任务及其无害子任务。对比方法包括：整体任务（将原始恶意任务作为单次提示）vs. 分解任务（顺序独立提交无害子任务，清除历史记录）。主要结果：1）分解显著降低拒绝率——Qwen3-Coder从21%降至0%，Claude Haiku从90%降至2.5%，GPT-5-mini从约90%降至6%；2）分解提升攻击成功率——Qwen3-Coder从17%升至36%，Claude Haiku和GPT-5-mini均从0%升至约70%；3）检查点通过率相应提升约29%、81%和74%；4）分解后失败任务中安全拒绝占比极低（GPT-5-mini约19%、Claude Haiku约8%、Qwen3-Coder为0%），主要归因于能力限制。此外，消除安全对齐的弱模型（Llama3.1-8B-Instruct）在整体任务上攻击成功率为0%，验证了执行难度标准。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向主要体现在：当前DECOMPBENCH主要针对LLM-based agents，未覆盖其他类型智能体（如多模态、具身智能体）的安全评估；测试场景有限，未考虑动态环境下的实时分解攻击。未来可探索更全面的防御机制，例如设计能够推理跨子任务累积意图的安全协议，或通过意图检测、任务图状态监控来识别分解模式。改进思路包括：引入对抗性训练增强模型对分解攻击的鲁棒性；开发自适应的安全层，在子任务执行前进行上下文关联分析；以及构建更复杂的攻击图（如包含循环、条件分支），以模拟真实攻击流程。此外，可借鉴图神经网络技术构建任务依赖关系推理模块，提升智能体对隐性目标的感知能力。

### Q6: 总结一下论文的主要内容

这篇论文介绍了DECOMPBENCH，一个专门评估LLM智能体在分解攻击下安全性的基准。问题定义是：攻击者将有害任务分解成多个看似良性的子任务，这些子任务单独执行时能绕过安全机制，但累积起来实现恶意目标。现有基准未能明确捕捉这种攻击。方法上，论文采用“分解即设计”原则，通过图形框架将有害任务分解为可执行的、单独无害的子任务，并遵循固有恶意性、固有可分解性、良性子任务隔离和执行难度四项标准。实验发现，最先进的智能体对完整有害任务的拒绝率很高，但对其分解变体的拒绝率显著降低，且常无意中完成对抗目标。主要结论是当前安全机制无法可靠地推理跨多个子任务的累积意图，揭示了分解攻击的严重威胁，强调了针对性防御和严格安全评估的必要性。该基准包含8个危害类别、250个任务，平均使用2.64个工具。
