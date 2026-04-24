---
title: "When Agents Look the Same: Quantifying Distillation-Induced Similarity in Tool-Use Behaviors"
authors:
  - "Chenghao Yang"
  - "Yuning Zhang"
  - "Zhoufutu Wen"
  - "Tao Gong"
  - "Jiaheng Liu"
  - "Qi Chu"
  - "Nenghai Yu"
date: "2026-04-23"
arxiv_id: "2604.21255"
arxiv_url: "https://arxiv.org/abs/2604.21255"
pdf_url: "https://arxiv.org/pdf/2604.21255v1"
github_url: "https://github.com/Syuchin/AgentEcho"
categories:
  - "cs.CL"
tags:
  - "Agent行为分析"
  - "模型蒸馏"
  - "工具使用"
  - "行为相似性度量"
  - "评估基准"
  - "多智能体分析"
relevance_score: 9.2
---

# When Agents Look the Same: Quantifying Distillation-Induced Similarity in Tool-Use Behaviors

## 原始摘要

Model distillation is a primary driver behind the rapid progress of LLM agents, yet it often leads to behavioral homogenization. Many emerging agents share nearly identical reasoning steps and failure modes, suggesting they may be distilled echoes of a few dominant teachers. Existing metrics, however, fail to distinguish mandatory behaviors required for task success from non-mandatory patterns that reflect a model's autonomous preferences. We propose two complementary metrics to isolate non-mandatory behavioral patterns: \textbf{Response Pattern Similarity (RPS)} for verbal alignment and \textbf{Action Graph Similarity (AGS)} for tool-use habits modeled as directed graphs. Evaluating 18 models from 8 providers on $τ$-Bench and $τ^2$-Bench against Claude Sonnet 4.5 (thinking), we find that within-family model pairs score 5.9 pp higher in AGS than cross-family pairs, and that Kimi-K2 (thinking) reaches 82.6\% $S_{\text{node}}$ and 94.7\% $S_{\text{dep}}$, exceeding Anthropic's own Opus 4.1. A controlled distillation experiment further confirms that AGS distinguishes teacher-specific convergence from general improvement. RPS and AGS capture distinct behavioral dimensions (Pearson $r$ = 0.491), providing complementary diagnostic signals for behavioral convergence in the agent ecosystem. Our code is available at https://github.com/Syuchin/AgentEcho.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前LLM智能体生态系统中普遍存在的行为同质化问题。随着模型蒸馏技术的广泛使用，众多看似不同的智能体实际上表现出高度相似的行为模式，包括相同的推理步骤、工具调用习惯甚至失败模式。这种“蒸馏回响”现象导致智能体缺乏真正的多样性，无法为系统提供独立的验证，反而呈现集体性的相同缺陷。

然而，现有评估指标存在明显不足。它们主要关注静态对话中的响应级相似性，无法捕捉工具使用轨迹的动态特征；更关键的是，无法区分两类不同行为：一是任务成功必需的强制性行为（如取消航班必调用`cancel_reservation`），二是反映模型自主偏好的非强制性行为（如是否额外调用`get_reservation_details`确认）。由于无法隔离这些“行为自由度”，现有指标难以判断两个模型趋同是因为存在唯一正确路径，还是因为一个模型在盲目跟随另一个。

为填补这一空白，本文提出系统性框架来量化智能体蒸馏，核心贡献在于：首次在工具使用智能体场景中分离出非强制性行为，并引入两个互补指标——响应模式相似度（RPS）用于衡量语言对齐，动作图相似度（AGS）用于衡量工具使用习惯。通过这套新方法，论文得以揭示被任务要求掩盖的风格和结构上的趋同模式，为理解智能体生态系统的行为收敛提供了实证基础。

### Q2: 有哪些相关研究？

**相关研究主要分为三类：**

1. **知识蒸馏与同质化研究**。现有研究指出蒸馏会导致LLM同质化，但缺乏量化工具使用行为相似性的方法。本文首次提出RPS和AGS指标，专门针对蒸馏导致的非强制性行为趋同进行测量，与已有工作关注参数或输出层不同，本文聚焦于行为模式层面。

2. **数据污染检测**。数据污染会干扰模型评估，现有方法包括分布记忆检测和核散度评分等。本文提出的度量标准可间接用于检测污染：若模型与教师行为高度相似（如Kimi-K2在AGS上超过Anthropic自有模型），可能暗示训练数据存在重叠。

3. **工具使用基准测试**。相关基准包括API-Bank、ToolBench、BFCL和τ-Bench等，主要评估工具选择准确性。本文不同之处在于不衡量任务成功率，而是构建动作流图（AGS）分析工具调用的依赖模式，并利用τ-Bench的标准化场景设计RPS的提示模板，测量非任务必需的对话模式相似度。

### Q3: 论文如何解决这个问题？

该论文提出了两个互补的度量指标来量化蒸馏导致的行为同质化，分别聚焦于语言和工具使用两方面。整体框架包括轨迹采集、阶段标注和相似度计算三个步骤：首先在工具使用任务集上收集各模型的执行轨迹；然后定义认证、需求获取、执行、验证和通知五个标准阶段，利用LLM将轨迹中的每个响应和工具消息标注到对应阶段。

核心方法是响应模式相似度（RPS）和动作图相似度（AGS）。RPS通过比较共享阶段中模型的风格（措辞习惯）、结构（句型模板）和对齐（推理到行动的模式）三个维度来量化语言层面的相似性。AGS则直接对工具调用序列构建有向图，节点代表工具调用（含名称、参数和结果），边分为顺序边（时间相邻调用）和依赖边（参数值源于前序结果）。在此基础上，AGS定义三个子指标：可选工具一致性$S_{node}$通过排除所有成功模型的共同强制工具，只比较可选工具的使用一致性；顺序模式相似度$S_{seq}$提取写后验证、写前确认和错误重试三个特征向量计算余弦相似度；依赖模式相似度$S_{dep}$提取输出重用率、最长依赖链长度和输出扇出率三个特征。

创新点在于：1）提出阶段标注方法实现不同长度轨迹的语义对齐；2）通过自主行为隔离，即区分强制工具（任务必要的共同行为）和可选工具（反映模型自主偏好），避免基线方法因共同行为而高估相似度；3）控制蒸馏实验验证了AGS能区分教师特定收敛和通用改进，且RPS与AGS（Pearson r=0.491）捕获不同行为维度，为诊断智能体生态系统中的行为趋同提供了互补信号。

### Q4: 论文做了哪些实验？

论文进行了三类实验。**实验设置**：评估18个来自8家提供商的模型（包括Claude、GPT、DeepSeek、Kimi-K2等），均使用官方API和默认超参数，以Claude Sonnet 4.5 (thinking)为参考模型。**数据集/基准测试**：使用τ-Bench和τ^2-Bench，从航空、零售和电信三个领域各采样50个任务，涵盖身份验证、信息检索和订单修改等场景。**对比方法**：语义基线包括RSE、2-gram重叠比和BERTScore；图结构基线使用图编辑距离(GED)。**主要结果**：1）同家族模型对的AGS比跨家族模型对高5.9个百分点；2）Kimi-K2 (thinking)表现出异常高的相似性，$S_{node}$达82.6%，$S_{dep}$达94.7%，均超过Anthropic自家的Opus 4.1（分别为81.0%和93.7%）；3）Anthropic家族内部RPS得分均超过3.8，非家族模型至少低0.20；4）RPS和AGS呈中等相关（Pearson r=0.491），表明两者捕获不同的行为维度；5）受控蒸馏实验进一步证实AGS能区分教师特定收敛与通用改进。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向主要包括：一是当前研究仅聚焦于任务级别的行为模式（如工具调用和对话风格），未深入分析模型在底层推理链或知识表征层面的相似性，未来可结合思维链（CoT）分析或表示相似性度量（如CKA、SVCCA）来揭示更细粒度的蒸馏痕迹。二是RPS和AGS虽能区分强制与非强制行为，但依赖于轨迹和对话数据的可获取性，对仅输出结果的封闭模型不适用，可探索从最终输出反推行为模式的轻量级方法。三是实验仅验证了单轮蒸馏（从Claude到Qwen），未考察多代蒸馏（如学生模型再被蒸馏）中相似性的累积与稀释效应，未来可设计多轮蒸馏实验追踪行为漂移。四是当前指标在混合任务场景（both-correct/wrong/mixed）下区分度仍有限（如GED在控制实验中方向不一致），可改进为对任务约束更鲁棒的归一化度量，或引入因果干预（如删除强制步骤后重新计算相似性）以纯净提取非强制偏好。

### Q6: 总结一下论文的主要内容

论文提出了一种量化大语言模型代理行为同质化的方法。现有指标无法区分任务必需的强制性行为与反映模型自主偏好的非强制性模式。为此，作者设计了两个互补指标：响应模式相似度(RPS)衡量语言表达一致性，动作图相似度(AGS)将工具使用习惯建模为有向图进行比较。在τ-Bench和τ²-Bench上评估了8家供应商的18个模型，发现同家族模型对的AGS比跨家族对高5.9个百分点。特别地，Kimi-K2（思考版）的节点相似度达82.6%、依赖相似度达94.7%，超过Anthropic自家的Opus 4.1。控制蒸馏实验证实AGS能区分针对特定教师的收敛与通用提升，而传统GED指标无法区分。RPS与AGS呈中等相关(Pearson r=0.491)，表明它们捕捉了不同行为维度。该工作为评估代理生态中的行为趋同提供了诊断工具，揭示了蒸馏可能导致非强制性行为模式的复制与同质化。
