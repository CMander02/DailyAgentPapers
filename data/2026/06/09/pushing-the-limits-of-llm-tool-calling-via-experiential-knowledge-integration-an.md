---
title: "Pushing the Limits of LLM Tool Calling via Experiential Knowledge Integration and Activation"
authors:
  - "Yupu Hao"
  - "Zhuoran Jin"
  - "Huanxuan Liao"
  - "Kang Liu"
  - "Jun Zhao"
date: "2026-06-09"
arxiv_id: "2606.10875"
arxiv_url: "https://arxiv.org/abs/2606.10875"
pdf_url: "https://arxiv.org/pdf/2606.10875v1"
github_url: "https://github.com/hypasd-art/KATE"
categories:
  - "cs.CL"
tags:
  - "LLM工具调用"
  - "经验知识集成"
  - "推理宽度扩展"
  - "知识增强训练"
  - "工具执行框架"
  - "后训练对齐"
relevance_score: 8.5
---

# Pushing the Limits of LLM Tool Calling via Experiential Knowledge Integration and Activation

## 原始摘要

Large language models (LLMs) rely on tool use to act as autonomous agents, yet often fail in multi-step execution due to insufficient tool-related knowledge and ineffective knowledge activation. Therefore, we present a systematic study on how knowledge influences tool-use performance, covering the stages of knowledge acquisition, activation, and internalization. In the knowledge acquisition stage, we acquire and evaluate various forms of experiential knowledge, and our analysis shows that simple instance-level knowledge can already provide strong and reliable gains, while abstract intent-level knowledge offers limited benefits. At inference time, to activate knowledge, we find that prompting LLM to expand the depth of reasoning yields diminishing returns, whereas expanding the width of reasoning by parallel sampling with aggregation more effectively activates latent experiential knowledge. At training time, for knowledge internalization, post-training with knowledge-augmented data further improves performance, with reinforcement learning outperforming supervised fine-tuning. Based on these insights, we propose the Knowledge-Augmented Tool Execution (KATE), a knowledge-augmented tool execution framework that integrates experiential knowledge with reasoning-width-expanded inference and knowledge-aware training. Experiments on BFCL-V3 and AppWorld demonstrate consistent and substantial improvements over strong baselines across model scales. Our Code is available at https://github.com/hypasd-art/KATE.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文致力于解决大型语言模型（LLM）在工具调用（Tool Use）任务中因缺乏经验性知识（Experiential Knowledge）及知识激活不足而导致的失败问题。研究背景是，尽管LLM作为智能代理依赖工具调用执行复杂任务，但现有方法多将工具使用简化为提示工程（Prompt Design）或对齐（Alignment）问题，隐含假设模型已具备足够的工具执行经验。然而，实际失败往往源于缺乏具体可操作的知识，如参数约束、操作模式或错误恢复策略。现有研究对经验性知识在工具执行中的作用缺乏系统性探索，尤其是在知识形式、推理时激活机制以及训练时内化效果三个关键问题上存在空白。为此，本文首次系统地研究了经验性知识如何在工具执行中实现全流程的获取、激活与内化。核心目标是回答三个问题：哪种形式的经验性知识对工具使用最有效？如何有效激活系统中的知识？通过训练将知识内化到模型参数中能否带来额外收益？基于此，本文提出了KATE（知识增强工具执行）框架，通过整合实例级知识、扩展推理宽度（width-based parallel sampling）以及知识感知训练，显著提升了LLM在多步工具调用中的准确性和鲁棒性。

### Q2: 有哪些相关研究？

在工具学习方面，现有研究主要通过优化推理框架和微调模型参数来增强LLM的工具调用能力，如使用强化学习提升工具调用性能，但很少有工作强调知识在工具使用任务中的关键作用。本文则系统性地研究了知识在工具使用任务中的完整生命周期，包括知识获取、激活和内化阶段，填补了这一空白。

在经验知识方面，近期方法开始在推理和训练阶段利用程序性经验来增强模型能力，但未区分不同抽象层次知识的作用。本文在知识获取阶段引入并比较了实例级轨迹和意图级脚本等不同抽象层次的知识，分析了它们的不同效果，而先前工作往往只关注改进特定知识构建过程。在知识激活阶段，与先前设计细粒度检索机制来获取最有用知识不同，本文采用简单的top-k检索器，主要探究如何有效利用已有知识进行推理，发现扩展推理宽度（并行采样与聚合）比扩展推理深度更有效。

### Q3: 论文如何解决这个问题？

为解决LLM在工具调用中知识不足和激活失效的问题，论文提出了知识增强工具执行框架KATE，系统性地从知识获取、激活和内化三个阶段进行优化。

在知识获取阶段，论文构建了结构化知识库，采用实例级的场景轨迹知识，将用户查询编码为向量存储，并在推理时通过相似度匹配检索最相关的执行轨迹作为上下文增强。该方法优于意图级知识，因为轨迹级信息提供了可直接执行的细粒度指导。

在知识激活阶段，论文创新性地采用基于推理宽度扩展的并行采样策略。在每个交互步骤，模型基于当前对话历史并行生成多个候选动作，当所有候选一致时直接执行，否则通过LLM聚合函数选择最优动作。实验表明，这种方式比单纯增加推理深度的提示方法更有效，因为并行采样能更好地激发模型潜在的体验知识。

在知识内化阶段，论文通过后训练将知识内化到模型参数中。具体地，将检索到的体验知识预插入训练上下文作为引导信号，采用强化学习训练策略，提高正确推理路径的采样概率，从而获得比监督微调更稳健的性能提升。

整体框架由知识库、并行采样推理模块和后训练模块三部分组成，核心创新在于将实例级轨迹知识与推理宽度扩展策略结合，并通过知识增强训练进一步强化模型能力。

### Q4: 论文做了哪些实验？

论文在BFCL-V3和AppWorld两个基准上进行了实验。BFCL-V3是多步工具调用基准，涵盖Base、Miss Func、Miss Param和Long Context四个场景；AppWorld是交互式编码代理基准，使用Task Goal Completion (TGC)和Scenario Goal Completion (SGC)指标。对比方法包括默认函数调用(FC)、提示工程(Prompt)、Memp（静态过程记忆框架）以及ReAct/ReAct+ST（仅AppWorld）。主要模型为Qwen3-8B和Qwen3-32B，并报告了GPT-4.1和GPT-5作为参考。

实验结果显示，KATE在BFCL-V3上显著超越基线：Qwen3-8B上平均得分提升13.25（从32.75到46.00），Qwen3-32B上提升4.50（从46.00到50.50）。在AppWorld上，KATE在Test-N和Test-C场景下均优于ReAct和Memp，例如Qwen3-8B平均得分10.92 vs ReAct+ST的10.6。消融实验表明，取消平行采样（w/o PS）或经验知识（w/o Exp）均导致性能下降，且LLM聚合替换为自一致性（r PS-Con）在32B模型上表现稳健。后训练中，直接强化学习（RL，+15.50）优于监督微调（SFT，+13.00）及两者结合（+13.50）。错误分析显示，KATE显著减少了规划推理错误和过早终止错误。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面：首先，知识库规模较小，未探索大规模知识库的扩展性影响，未来可研究动态知识检索与规模化知识库的协同机制；其次，仅针对纯文本工具调用场景，未涉及多模态任务，可尝试将视觉、语音等模态信息融入工具执行框架；最后，当前知识激活方式中，宽度扩展的推理效率较低，可探索基于蒙特卡洛树搜索或对照解码的自适应采样策略。此外，知识内部化阶段仅对比了SFT与RL，可进一步研究离线强化学习（如DPO）或过程奖励模型对工具执行稳定性的提升，同时考虑知识遗忘对长序列任务的影响，设计记忆回放机制来维持知识激活的持续性。

### Q6: 总结一下论文的主要内容

这篇论文系统研究了如何通过经验知识提升大语言模型（LLM）在多步工具调用任务中的表现。问题定义是LLM作为自主智能体时常因工具相关知识不足和知识激活效率低而失败。方法上，作者提出了知识增强工具执行框架KATE，涵盖三个关键阶段：知识获取阶段，比较了实例级和意图级经验知识，发现简单实例级知识即可稳定提升性能；推理阶段，发现增加推理宽度（并行采样+聚合）比增加推理深度更能有效激活潜在经验知识；训练阶段，使用知识增强数据进行后训练（尤其是强化学习优于监督微调）能进一步内化知识。实验在BFCL-V3和AppWorld数据集上，跨不同模型规模均取得显著改进。核心贡献在于揭示了经验性知识如何系统性地增强工具执行能力，并提供了从知识构建到推理和训练集成的实用框架，对提升LLM作为自主智能体的可靠性有重要价值。
