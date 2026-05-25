---
title: "From Patches to Trajectories: Privileged Process Supervision for Software-Engineering Agents"
authors:
  - "Murong Ma"
  - "Tianyu Chen"
  - "Yun Lin"
  - "Shuai Lu"
  - "Qinglin Zhu"
  - "Yeyun Gong"
  - "Zhiyong Huang"
  - "Peng Cheng"
  - "Yan Lu"
  - "Jin Song Dong"
date: "2026-05-21"
arxiv_id: "2605.21996"
arxiv_url: "https://arxiv.org/abs/2605.21996"
pdf_url: "https://arxiv.org/pdf/2605.21996v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "SWE Agent"
  - "过程监督"
  - "微调数据合成"
  - "轨迹优化"
  - "代码生成Agent"
  - "工具使用Agent"
  - "教师-学生训练"
relevance_score: 9.5
---

# From Patches to Trajectories: Privileged Process Supervision for Software-Engineering Agents

## 原始摘要

Supervised fine-tuning (SFT) on long teacher trajectories is the dominant way to instill investigation and reasoning in open software-engineering (SWE) agents. Since every retained response becomes an imitation target, the student inherits the final outcome and intermediate flaws, including ungrounded leaps and redundant loops. High-quality training data must be effective(each step is grounded and narrows the agent's epistemic gap to the correct fix) and efficient(each step is information-bearing rather than redundant or looping). Existing recipes filter or relabel teacher rollouts using only a binary terminal verifier, which does not directly target these axes and provides no supervision on instances where the teacher fails.
  Most real issue includes a developer-authored reference patch, $p^\star$, revealing the file paths, runtime behaviors, and coding conventions presupposed by the correct fix, yet standard pipelines discard it. We propose Patches-to-Trajectories (P2T), which uses $p^\star$ as privileged information during curation and formulates trajectory construction as bi-objective optimization over per-step effectiveness and trajectory length. A reverse phase distills $p^\star$ into a latent process graph, $G^\star$, of contextual facts and solution milestones. A forward phase curates trajectories from blinded teacher continuations by scoring per-step progress against $G^\star$ under a leakage-blocking groundedness check and retaining the shortest effective segments.
  Using only 1.8k curated SWE-Gym instances, P2T improves effectiveness and efficiency over outcome-filtered SFT and its tool-error-masking variant. On SWE-bench Verified, it raises Pass@1 by up to 10.8 points while reducing per-instance inference cost by ~15%, with consistent gains on SWE-bench Lite. Size-matched ablations and qualitative analysis further isolate trajectory quality from data scale.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决软件工程（SWE）智能体在监督微调（SFT）过程中，因训练轨迹质量低下而导致模型学习效果不佳的核心问题。研究背景是，当前主流的训练方法是对强教师模型生成的长轨迹进行行为克隆，但这种方法存在根本缺陷：由于每个被保留的响应都成为模仿目标，学生不仅继承了最终结果，也继承了中间步骤中的瑕疵，如无根据的跳跃和冗余循环。现有方法仅依赖一个二元的最终验证器（是否通过测试）来筛选轨迹，这无法对中间推理步骤提供有效监督，且对教师模型失败的实例完全无法提供训练信号。

更关键的是，所有真实问题都附带一个开发者编写的参考补丁（p*），它蕴含了正确修复所需的文件路径、运行时行为和编码约定等关键先验信息，但现有标准流程却将其丢弃不用。本文要解决的核心问题正是：如何利用这个被忽略的“特权信息”p*，来构建同时满足有效性（每一步都基于事实并缩小与正确答案的认知差距）和高效性（每一步都承载新信息而非冗余循环）的高质量训练轨迹，从而从根本上提升SFT训练数据的质量，而非简单地增加数据量。

### Q2: 有哪些相关研究？

SWE智能体与基准方面：SWE-bench催生了一系列仓库级问题解决的推理系统，包括ReAct风格工具使用、SWE-agent的智能体-计算机接口、OpenHands平台、AutoCodeRover中的结构感知检索，以及Agentless的定位-修复-验证简化流水线。研究表明，当测试较弱或问题泄露解决方案时，终端通过/失败可能夸大正确性。本文的工作与这些框架正交，专注于改进训练智能体时SFT轨迹的每步质量。

开源SWE智能体的轨迹数据方面：现有方法通过可执行任务扩展并保留通过终端验证器的轨迹，如SWE-Gym处理真实Python问题、R2E-Gym采用程序化构建与混合验证器、SWE-smith通过测试破坏合成、Skywork-SWE进行大规模整理与轨迹缩放。这些方法都保留完整的成功轨迹，从而继承了其中的绕路、冗余观察和无根据推断。本文提出的P2T方法将参考补丁p*作为特权信息，蒸馏为G*以仅暴露修复所需的前提条件，且从不向学生模型展示p*。

LLM智能体的轨迹与上下文缩减方面：互补研究方向致力于降低长智能体历史的推理成本，如AgentDiet在运行时修剪编码智能体轨迹中的无用、冗余或过期条目，ACON学习压缩长时域智能体的观测与交互历史。这些方法保持底层策略不变而缩短其输入内容；P2T则是在训练时缩短生成的轨迹，使所得学生模型具有内在高效性，并能与这类推理时压缩器兼容。

### Q3: 论文如何解决这个问题？

P2T 通过一个两阶段流水线将开发者编写的参考补丁 $p^\star$ 转化为高质量的代理轨迹，核心是解决轨迹的有效性和效率问题。

**第一阶段：过程图蒸馏**。该阶段将 $p^\star$ 转化为一个隐式的有向无环图 $G^\star$，其节点代表中间上下文事实和解决方案里程碑，如代码定位、运行时行为、修复计划和代码编辑。边表示依赖关系。构建过程采用迭代的“提议者-评判者”机制：提议者添加逻辑上必要的节点以满足充分性，评判者则根据非泄露性原则剪除那些表述所依赖的事实尚未被发现的节点。$G^\star$ 定义了一个“进展分数” $Prog_t$，用于衡量每一步轨迹合法地覆盖了多少图节点，并惩罚那些在所需事实建立前就跳转到解决方案的“超前”行为。

**第二阶段：后退视界双目标轨迹实现**。该阶段通过滑动窗口逐步构建轨迹。在每个窗口内，算法采样多个候选片段（来自盲化求解器的种子），并允许对每个候选片段的最多一个步骤进行单次“突变”，使其朝向 $G^\star$ 中当前可达的节点。然后，算法计算每个候选片段的“有效性” $Eff_t$，该指标由窗口内的累积进展分数 $Prog_t$ 和一个“接地性门控” $Ground_t$ 共同组成。接地性门控通过符号检查（引用实体是否已在历史中出现）和LLM评判（推理是否被历史观察所支持）来防止信息泄露和不基于证据的跳跃。最后，算法在有效性超过局部阈值 $\eta_t$ 的候选片段中，选择长度最短的，从而实现有效性和效率的帕累托最优。整个轨迹通过半窗口步幅逐步扩展，避免了局部次优解。

### Q4: 论文做了哪些实验？

论文在SWE-bench Verified（500实例）和SWE-bench Lite（300实例）上评估了P2T方法。实验设置包括：从SWE-Gym的2438个实例中筛选出1800个具有工作Docker环境和参考补丁的实例用于P2T训练；使用Qwen3-Coder-480B-A35B-Instruct和GLM-5-FP8作为教师模型，在OpenHands框架下使用100次ReAct预算进行轨迹生成；对Qwen2.5-Coder-14B和32B两个学生模型进行微调。对比方法包括：测试通过拒绝采样（SWE-Gym基线）、SWE-Lego工具错误掩码基线、P2T大小匹配版本（随机子采样以控制数据规模）和P2T完整版本。

主要结果：P2T（完整版）在所有学生-教师-基准组合上同时提升了有效性和效率。在SWE-bench Verified上，使用Qwen3-C-480B教师和32B学生时，Pass@1提升高达10.8个百分点（从39.6%到50.4%），同时每实例推理成本降低约15%（从0.92美元降至0.78美元）。在SWE-bench Lite上也有类似增益（Pass@1提升7.3个百分点）。大小匹配版本已优于基线（+2.8 Pass@1），证明增益来自轨迹质量而非数据规模。消融实验证实：移除 groundedness 检查导致Pass@1下降7.2-8.2点；替换最短段选择规则使轨迹长度增加7.3%且Pass@1下降。

### Q5: 有什么可以进一步探索的点？

论文在验证P2T的通用性上存在局限。目前实验仅基于Qwen2.5-Coder系列和SWE-Gym数据，未来应探索其在不同基座模型（如Llama、DeepSeek-Coder）和不同SWE数据集上的迁移能力。此外，该方法依赖开发者提供的参考补丁作为特权信息，但在真实场景中，许多issue可能没有明确的参考补丁或补丁质量参差不齐，如何在没有完美补丁时构建有效的先验图是重要方向。

可以进一步研究将P2T与强化学习结合——当前SFT后，能否再用过程奖励模型对后续探索进行优化？同时，框架中的“泄露阻断检查”虽防止了轨迹过拟合补丁，但可能过于保守而错过高质量的中间步骤，未来可以设计更柔性的知识蒸馏机制，允许适度信息传递。最后，当前只关注了最长轨迹的缩减，但“最短”未必等于最优，需要平衡步长与任务完成可靠性之间的权衡，甚至引入主动学习来动态筛选对模型最具学习价值的子轨迹。

### Q6: 总结一下论文的主要内容

该论文旨在解决软件工程（SWE）智能体训练数据质量低的问题。现有方法基于二进制测试结果（是否通过）过滤教师模型轨迹进行监督微调（SFT），这忽略了轨迹中间步骤的有效性和效率，导致学生模型继承无关的循环或未验证的跳跃。作者提出Patches-to-Trajectories (P2T)方法，将开发者编写的参考补丁作为特权信息引入数据筛选过程。P2T包含两个阶段：首先，逆向阶段从参考补丁中提取一个潜在的过程图，包含上下文事实和解决里程碑；然后，正向阶段基于该图，对盲化的教师轨迹进行每步得分评估，同时进行抑制信息泄露的接地检查，并保留最短的有效轨迹片段。该方法将轨迹构建建模为每步有效性与轨迹长度双目标优化问题。实验表明，仅使用1.8k精心筛选的SWE-Gym实例，P2T在SWE-bench Verified上将Pass@1提升了最多10.8个点，同时将每次实例的推理成本降低了约15%。其核心贡献在于利用被丢弃的参考信息显著提升了训练轨迹的质量与效率。
