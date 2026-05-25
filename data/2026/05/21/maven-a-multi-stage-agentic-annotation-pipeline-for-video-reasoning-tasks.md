---
title: "MAVEN: A Multi-stage Agentic Annotation Pipeline for Video Reasoning Tasks"
authors:
  - "Han Zhang"
  - "Wanting Jiang"
  - "Tomasz Kornuta"
  - "Tian Zheng"
  - "Vidya Murali"
date: "2026-05-21"
arxiv_id: "2605.21917"
arxiv_url: "https://arxiv.org/abs/2605.21917"
pdf_url: "https://arxiv.org/pdf/2605.21917v1"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Video Agent"
  - "多智能体流水线"
  - "数据标注"
  - "VLM微调"
  - "领域自适应"
  - "CoT推理"
relevance_score: 9.5
---

# MAVEN: A Multi-stage Agentic Annotation Pipeline for Video Reasoning Tasks

## 原始摘要

Training Vision Language Models (VLMs) for video event reasoning requires high-quality structured annotations capturing not only what happened, but when, where, why, and with what consequence, at a scale manual labelling cannot support. We present MAVEN (Multi-stage Agentic Video Event aNnotation), a multi-stage agentic pipeline that turns raw videos into multi-task training data with Chain-of-Thought (CoT) reasoning traces, organized around a designated Event of Focus. At its core, MAVEN synthesizes a Multi-Scale Spatio-Temporal Event Description (MSTED) from three complementary caption levels; this explicit intermediate serves as the sole input to downstream Q&A generation across multiple task formats. Crucially, MAVEN supports agent-driven domain adaptation: given a new video dataset and target question examples, the agent redesigns all prompts top-down without manual re-engineering. A hierarchical refinement loop further classifies annotation errors against a taxonomy, traces root causes to the originating pipeline stage, and applies targeted edits that rewrite prompts or modify the pipeline structure itself, iteratively improving data quality. We apply MAVEN to label over 5,300 traffic videos and fine-tune Cosmos-Reason2-8B on the resulting data. On a private CCTV evaluation set, fine-tuning surpasses both Gemini 2.5 Pro and 3.1 Flash, including a $+38.8$-point gain in MCQ accuracy over zero-shot. On AccidentBench, CCTV-only training lifts Cosmos-Reason2 by $+10.7$ MCQ points and matches Gemini 2.5 Pro despite seeing no dashcam videos; adding agent-adapted dashcam annotations narrows the gap to Gemini 3.1 Flash, and RL post-training pushes overall performance past both Gemini baselines. Qualitative results on warehouse surveillance and public safety videos further show the agentic workflow readily adapts the pipeline to new domains.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决视频事件推理任务中训练数据不足的问题。当前，视觉语言模型（VLM）需要进行结构化的因果推理（如理解事件中谁、何时、何地、为何发生以及后果），但高质量、结构化的链式思维（CoT）标注数据极其昂贵且难以规模化生产。现有自动标注方法存在明显不足：单次平面视频描述会永久丢失细粒度细节；固定分类或依赖特定领域传感器的方案则通用性差；并且没有一种方法能生成可复用的中间事件表示，以供多种下游任务格式使用。因此，本文核心问题是：如何设计一个自动化的、可扩展且通用的标注流程，以从原始视频中生成高质量、多任务的结构化训练数据（包括CoT推理轨迹），并支持高效地适应新领域，同时通过反馈机制持续迭代提升数据质量。

### Q2: 有哪些相关研究？

相关研究可分为以下几类：

1. **视频异常数据集**：UCF-Crime、CADP等传统数据集仅支持帧级或片段级分类，缺乏因果推理链。本文的MAVEN填补了这一空白，可生成包含因果推理的问答对。

2. **VLM推理基准**：AccidentBench提供约19,000个人工标注的推理问答对，SurveillanceVQA-589K展示AI辅助标注的规模。这些工作评估推理能力，但不生成训练数据，MAVEN则生成多样化的思维链问答。

3. **自动化数据生成方法**：Cosmos-Reason1将视频压缩为单一描述（有信息损失），VAD-Reasoning拼接帧级描述（遗漏帧间事件），Alpamayo-R1依赖封闭分类学和专有传感器数据。MAVEN的核心创新在于：a) 分层三级描述相互校正；b) 显式结构化中间表示（MSTED）作为验证检查点和问答生成的唯一输入，避免不可逆信息损失。

4. **基于智能体的方法**：推理时智能体（QVAD、PANDA）仅改进异常检测推理，不解决训练数据生成问题；Colon-Bench使用固定流水线。MAVEN的智能体作用于流水线设计时，可进行自顶向下的领域自适应，基于人类反馈修改流水线结构而非仅优化提示词。

### Q3: 论文如何解决这个问题？

MAVEN提出一个三阶段流水线架构,将原始视频自动转化为带链式推理轨迹的多任务训练数据。整体框架包含三个核心组件:自顶向下的代理辅助配置设计、标注流水线执行、以及带人工反馈的层级流水线精炼。

在标注流水线中,第一阶段使用视频VLM生成三个互补级别的视频描述:全局描述(场景布局、天气等上下文)、密集描述(带时间戳的事件级因果链)和片段描述(5-30秒细粒度细节)。第二阶段,LLM将三级描述整合为多尺度时空事件描述(MSTED),包含整体场景描述、时空定位和事件焦点描述三个部分。MSTED作为验证检查点,也是第三阶段问答生成的唯一输入,防止错误传播。第三阶段,另一LLM基于MSTED生成三类任务格式:多选题、二元验证和开放式问答,每类都包含明确推理轨迹。

关键技术方面,MAVEN具有代理驱动的领域自适应能力:给定新视频数据集和目标问题示例,代理通过反向推理自动重写所有提示词。层级精炼循环通过结构化错误分类、根因追溯和提示词/流水线编辑三个步骤迭代改进数据质量。该流水线在5300+交通视频上应用,生成约15000个带CoT的多任务训练样本,通过SFT+RL训练显著提升模型性能。

### Q4: 论文做了哪些实验？

论文在三个实验设置下评估了MAVEN管道生成的训练数据效果。首先，在私有CCTV评估集（80个视频）上，对Cosmos-Reason2-8B模型进行SFT微调（+CCTV SFT），在多项选择（MCQ）、验证和开放式任务上分别达到86.25%、85.00%和39.45%，相比零样本大幅提升+38.8、+35.0和+24.1个百分点，并超越了Gemini 2.5 Pro和3.1 Flash。加入汽车摄像头数据（+Dashcam SFT）后性能保持稳定，进一步RL训练将MCQ提升至88.75%。

其次，在AccidentBench基准测试（地面分割）上，仅使用CCTV数据训练的+CCTV SFT在整体MCQ准确率上达到40.6%，相比零样本提升+10.7点，并匹配Gemini 2.5 Pro（40.3%）。加入适配的汽车摄像头数据后，短视频准确率从42.4%提升至47.9%，超越两个Gemini基线。结合RL训练后整体准确率达到44.2%，同时超越Gemini 2.5 Pro（+3.9）和3.1 Flash（+1.4）。

最后，在消融实验中，对比使用单次全局字幕生成CoT的基线方法，MAVEN在CCTV评估集上分别获得+6.25 MC、+11.25验证和+3.50开放式的提升，证实了三层次字幕与MSTED结构化中间表示的关键作用。此外，在公共安全和仓库监控视频上的定性结果展示了管道通过智能体工作流适应新领域的能力。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于：1) 对open-ended评估仅依赖BertScore与管线生成答案的词汇重叠，缺乏真正的推理质量度量；2) 主要验证了交通和安防领域，通用视频推理的泛化性有待检验；3) 未充分探索MSTED中各层次caption的独立性贡献。

未来可探索：1) 引入人类专家标注或对抗性评估来替代BertScore，更准确衡量推理质量；2) 将MAVEN应用于更广泛的视频类型（如体育、新闻），测试其零样本适应能力；3) 设计自适应调度策略，根据视频复杂度动态调整三层次caption的权重，避免冗余计算；4) 探索将MSTED作为共享中间表示，与多模态大模型（如视觉-语言联合模型）端到端对齐，可能释放更强的跨域迁移能力；5) 在RL训练中引入开放任务的语义奖励函数，以平衡不同任务间的性能。

### Q6: 总结一下论文的主要内容

MAVEN提出了一种多阶段智能体标注流水线，用于为视频推理任务生成结构化训练数据。其核心创新在于先合成多尺度时空事件描述（MSTED），整合三个互补层次的视频描述，再基于此生成多种格式的问答对，避免了单遍自动标注的信息不可逆损失。该方法支持智能体驱动的领域自适应，无需人工重新设计即可自动调整整个流水线。通过层级化精炼循环，系统能按错误分类法定位问题根源并自动修改提示或流水线结构。MAVEN应用于5300+交通视频标注，微调后的Cosmos-Reason2-8B模型在私测CCTV集上准确率超越Gemini 2.5 Pro和3.1 Flash，提升38.8个MCQ点；在AccidentBench基准上仅凭CCTV数据即追平Gemini 2.5 Pro，加入领域自适应标注和RL后性能超越两个基线。该方法验证了跨领域推理能力的可迁移性，为大规模视频理解数据自动生成提供了有效方案。
