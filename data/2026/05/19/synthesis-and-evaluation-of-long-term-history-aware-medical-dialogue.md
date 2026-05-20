---
title: "Synthesis and Evaluation of Long-term History-aware Medical Dialogue"
authors:
  - "Hebin Hu"
  - "Renke Dai"
  - "Ah-Hwee Tan"
  - "Yilin Kang"
date: "2026-05-19"
arxiv_id: "2605.19766"
arxiv_url: "https://arxiv.org/abs/2605.19766"
pdf_url: "https://arxiv.org/pdf/2605.19766v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Medical Agent"
  - "Agent Benchmark"
  - "Long-Term Memory"
  - "Multi-Turn Dialogue"
  - "Data Synthesis"
  - "LLM Evaluation"
relevance_score: 8.0
---

# Synthesis and Evaluation of Long-term History-aware Medical Dialogue

## 原始摘要

An effective healthcare agent must be able to recall and reason over a patient's longitudinal medical history. However, the absence of datasets with realistic long-term dialogue timelines limits systematic evaluation. Real clinical text is constrained by privacy and ethics, while existing benchmarks focus on isolated interactions, failing to capture cross-session reasoning. We introduce a framework for synthesizing high-quality, long-term medical dialogues with LLMs. Our approach entails a knowledge-guided decomposition into three stages: constructing synthetic patient profiles with diverse disease and complication trajectories, generating multi-turn dialogues per encounter, and integrating them into a coherent longitudinal history dataset, MediLongChat. We establish three benchmark tasks-In-dialogue Reasoning, Cross-dialogue Reasoning, and Synthesis Reasoning-to evaluate the memory capabilities of healthcare agents. To assess data quality, we introduce a multi-dimensional evaluation framework combining vector-based metrics with LLM-as-a-judge assessments. Specifically, we define automatic measures-Faithfulness, Coherence, and Diversity-together with two LLM-based evaluations: Correctness and Realism. Benchmark experiments show that even state-of-the-art LLMs struggle with MediLongChat. These findings highlight the benchmark's applicability and underscore the need for tailored methods to advance healthcare agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有医疗对话系统缺乏长程历史感知能力的问题。在现实临床场景中，医生需要综合患者数月甚至数年的病史（如既往症状、诊断和治疗）进行推理，而现有的大语言模型（LLM）驱动的医疗助手往往只关注当前交互，忽视了跨会话的纵向推理，可能导致诊断失误。当前研究面临三大瓶颈：一是现有数据集（如通用对话语料或医疗QA基准）多为独立对话，缺乏连贯的病历叙事，无法评估跨会话推理能力；二是真实临床数据受隐私和伦理限制，获取困难且脱敏成本高；三是合成数据方法存在质量不稳定（如LLM生成长对话时易出现幻觉和矛盾）、上下文窗口限制（难以覆盖完整病史）以及缺乏标准化评估体系等问题。为此，本文提出一个系统性框架，通过知识引导的任务分解，分三步构建高质量的长程医学对话数据集MediLongChat：首先生成包含多样疾病轨迹的合成患者档案，然后生成每次就诊的多轮对话，最后整合为连贯的纵向历史。并设计三维基准任务（对话内推理、跨对话推理、综合推理）和综合评价指标（忠实性、连贯性、正确性、多样性、真实性），以系统评估医疗助手的记忆与推理能力。

### Q2: 有哪些相关研究？

相关的代表性研究可从方法类、评测类和数据集类三个角度归纳。

**方法类**：与本文密切相关的数据集生成方法包括：NoteChat利用多智能体框架从临床笔记生成医患对话；SynDial基于MTS-Dialogue和MIMIC数据集通过零样本提示生成对话并引入反馈循环；SynSUM结合贝叶斯网络与LLM生成结构化变量与临床文本对；Holysz等提出多阶段框架先生成患者档案和病例背景再生成对话。这些方法都能产生高质量单次对话，但本文指出它们普遍缺乏跨轮次和跨对话推理能力，而本文首次系统性地构建了融合长时间轴的多会话纵向病史数据集MediLongChat。

**评测类**：现有对话质量评估方法分为三类：人工评估（金标准但昂贵低效）、传统词汇和向量指标（如BLEU、ROUGE、嵌入余弦相似度，难以评估跨会话连贯性和事实一致性）、以及LLM-as-a-Judge方法（快速灵活但存在位置偏差等局限）。本文提出了一套多维度评估框架，融合自动指标（忠实度、连贯性、多样性）与LLM评判（正确性、真实性），专门针对长期历史感知任务设计。

**数据集类**：现有医疗对话基准聚焦于单次问诊或会话内部对话-笔记对齐，缺乏覆盖同一患者多次就诊的纵向记录或对话历史，这是本文与它们的关键区别和主要贡献。

### Q3: 论文如何解决这个问题？

该论文通过一个三阶段知识引导的合成框架构建了长程医疗对话数据集MediLongChat，并设计了分层评估基准。核心方法如下：

1. **知识引导的医疗记录生成**：首先构造虚构但真实的患者档案（包含人口统计学、生活习惯、病史等），并通过人工审核确认疾病-并发症关联、时间顺序和事件间隔的临床合理性。基于审核后的疾病案例与患者画像融合，生成按时间排序的关键医疗事件时间线，作为对话生成的叙事骨干。

2. **多轮对话生成的任务分解**：为避免长上下文幻觉，将“生成完整对话历史”分解为三个子步骤：①从时间线中提取独立医疗事件（时间、疾病、治疗方法）；②对每个事件构建自包含的提示，仅包含患者画像和事件局部事实；③模型生成涵盖主诉、病史采集、检查建议、诊断和治疗方案的医患对话。每段对话约50轮交互（3000 tokens），完整患者历史包含15-20段对话（约5万tokens）。通过引入医生角色多样性、风格控制和温度随机性避免风格单一化。

3. **基准任务设计**：构建三个递进式推理任务：①**对话内推理**：从单次对话中提取关键事实（如就诊日期、诊断、用药）；②**跨对话推理**：关联多次就诊信息（如疾病复发判断、治疗变化追踪）；③**综合推理**：根据完整病史推断并发症或新疾病。并设计包含忠实度、连贯性、多样性、正确性和真实性的多维评估框架。

创新点在于：通过知识引导分解规避隐私问题并保证医学合理性；采用任务分解策略突破长上下文生成瓶颈；建立分层推理基准系统评估长期记忆和跨时间推理能力。

### Q4: 论文做了哪些实验？

论文围绕生成的医疗长对话数据集MediLongChat开展了三组实验。首先，**实验设置**上，对比了MSC、CC、LoCoMo（开放域）和NoteChat（医疗域）四个长对话数据集。**数据集/基准测试**包括MediLongChat的自动评估（忠实性、连贯性、多样性）和基于LLM的多评委G-Eval评分（多样性、连贯性、正确性、真实性）。**对比方法**包括GPT-4o mini、DeepSeek-R1、Qwen3和ERNIE-4.5等通用大模型。

**主要结果**分为三部分：(1) **质量评估**：MediLongChat在多样性(0.5447)和连贯性(0.925)上表现优异，G-Eval ensemble评分下多样性(4.858)、连贯性(4.838)、真实性(4.505)均显著高于基线，正确性(4.545)也具有竞争力。(2) **基准测试**：在对话内推理(IDR)、跨对话推理(CDR)和综合推理(SR)三个任务上，所有模型表现有限。IDR F1最高为DeepSeek-R1(33.49)，CDR F1最高为GPT-4o mini(24.25)，SR准确率最高为GPT-4.1 mini(83.75%)，表明模型在长程跨会话推理上存在困难。(3) **消融实验**：去除知识引导（Stage-1）使忠实性从0.6353降至0.4415，真实性从0.720降至0.540；去除任务分解（Stage-2）使连贯性从0.924降至0.8689，多样性从0.5447降至0.4590；去除多样性设置则使多样性大幅降至0.3134，证实了各组件对生成质量的关键贡献。

### Q5: 有什么可以进一步探索的点？

该框架存在几个值得探索的方向。首先，合成数据与真实临床分布的偏差是核心局限，尤其在罕见病、复杂合并症及行为健康因素的覆盖上，未来可引入真实结构化EHR数据作为种子，或采用对抗生成与领域专家校验混合策略，提升数据真实性。其次，LLM-as-judge评估的可靠性依赖提示设计和模型鲁棒性，可与临床专家标注结合建立层次化评估体系，开发细粒度的事实一致性检测模块。此外，当前仅支持文本模态，扩展集成医学影像、实验室曲线和结构化记录的多模态对话是重要方向。在模型能力上，可探索检索增强生成、动态情景记忆和分层记忆网络，以强化跨会话推理并缓解长文本幻觉。最后，针对诊疗连续性，可设计随时间演进的疾病进展预测任务，推动智能体从静态记忆向动态知识更新演变。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种生成长期历史感知医疗对话的系统性框架，以解决现有基准缺乏跨会话推理能力的数据稀缺问题。核心方法采用知识引导的任务分解：首先构建包含多样疾病及并发症轨迹的合成患者档案，接着为每次就诊生成多轮对话，最终整合成连贯的长期病史数据集MediLongChat。为评估医疗代理的记忆能力，论文建立了三项基准任务：会话内推理、跨会话推理和综合推理。同时，提出结合向量指标与LLM评判的多维评估框架，衡量数据的忠实度、连贯性、正确性、多样性和真实性。实验表明，即使最先进的LLMs在MediLongChat上表现不佳，凸显了该基准的挑战性及开发专门方法的必要性。该工作为推进安全、可靠的长期健康护理代理提供了关键数据资源和评估标准。
