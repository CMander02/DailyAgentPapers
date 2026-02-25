---
title: "Bagpiper: Solving Open-Ended Audio Tasks via Rich Captions"
authors:
  - "Jinchuan Tian"
  - "Haoran Wang"
  - "Bo-Hao Su"
  - "Chien-yu Huang"
  - "Qingzheng Wang"
  - "Jiatong Shi"
  - "William Chen"
  - "Xun Gong"
  - "Siddhant Arora"
  - "Chin-Jou Li"
  - "Masao Someki"
  - "Takashi Maekaku"
  - "Keita Goto"
  - "Yusuke Shinohara"
  - "Jin Sakuma"
  - "Chao-Han Huck Yang"
  - "Shinji Watanabe"
date: "2026-02-05"
arxiv_id: "2602.05220"
arxiv_url: "https://arxiv.org/abs/2602.05220"
pdf_url: "https://arxiv.org/pdf/2602.05220v2"
categories:
  - "cs.CL"
  - "cs.SD"
tags:
  - "音频基础模型"
  - "多模态理解与生成"
  - "任务无关推理"
  - "认知概念映射"
  - "统一模型"
relevance_score: 5.5
---

# Bagpiper: Solving Open-Ended Audio Tasks via Rich Captions

## 原始摘要

Current audio foundation models typically rely on rigid, task-specific supervision, addressing isolated factors of audio rather than the whole. In contrast, human intelligence processes audio holistically, seamlessly bridging physical signals with abstract cognitive concepts to execute complex tasks. Grounded in this philosophy, we introduce Bagpiper, an 8B audio foundation model that interprets physical audio via rich captions, i.e., comprehensive natural language descriptions that encapsulate the critical cognitive concepts inherent in the signal (e.g., transcription, audio events). By pre-training on a massive corpus of 600B tokens, the model establishes a robust bidirectional mapping between raw audio and this high-level conceptual space. During fine-tuning, Bagpiper adopts a caption-then-process workflow, simulating an intermediate cognitive reasoning step to solve diverse tasks without task-specific priors. Experimentally, Bagpiper outperforms Qwen-2.5-Omni on MMAU and AIRBench for audio understanding and surpasses CosyVoice3 and TangoFlux in generation quality, capable of synthesizing arbitrary compositions of speech, music, and sound effects. To the best of our knowledge, Bagpiper is among the first works that achieve unified understanding generation for general audio. Model, data, and code are available at Bagpiper Home Page.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前音频基础模型在处理开放式、综合性音频任务时存在的根本性瓶颈问题。研究背景是，现有音频模型大多采用多任务学习范式，每个任务仅针对音频的孤立方面（如语音识别、事件检测、音乐生成等）进行特定监督，且建模时通常将语音、音乐和音效等类别严格区分。这种任务和类别层面的割裂，导致模型难以灵活应对用户实际提出的、通常是组合性且不局限于预定义任务边界的开放式请求（例如“生成一段带有紧张背景音乐和急促脚步声的旁白”），其扩展性严重依赖不可持续的领域特定工程。

现有方法的不足在于缺乏一种统一的、整体性的建模哲学，无法像人类智能那样，将物理音频信号与抽象的认知概念（如文字转录、情感、韵律、声音事件、音乐风格等）无缝关联，从而进行全方面的理解和生成。本文的核心问题是：如何构建一个能够统一处理各类音频任务和类型的通用音频基础模型。为此，论文提出了Bagpiper模型，其核心思想是通过“丰富描述”作为桥梁，建立原始音频信号与高层认知概念空间之间的鲁棒双向映射。模型采用“先描述后处理”的工作流程，在预训练阶段学习音频与描述之间的转换，在微调阶段模拟基于认知概念的中间推理步骤，从而无需特定任务先验知识即可解决多样化的开放式音频理解和生成任务。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：开放任务解决、模态接口（丰富字幕）和通用音频处理。

在**开放任务解决**方面，文本领域已通过大规模多任务监督（如FLAN-T5枚举1800多个任务）实现零样本泛化。然而，音频领域因任务定义稀缺、标注成本极高而难以复制此策略，导致现有音频语言模型对训练分布外的组合指令泛化能力有限。本文的Bagpiper则绕过大规模任务枚举，通过建立“丰富字幕”作为通用语义代理，将开放推理负担卸载给LLM的文本能力，从而无需显式音频任务监督即可解决复杂任务。

在**丰富字幕作为模态接口**方面，近期研究已表明自动生成的详细字幕能提升特定下游能力（如音乐理解、语音合成、音频生成），但这些工作通常局限于特定任务、规模较小且是单向的。本文首次建立了自然语言与所有音频类别之间的通用双向映射，并以此为基础支持下游开放处理。

在**通用音频处理**方面，音频理解已取得显著进展，但生成领域仍高度碎片化，当前最优模型通常局限于语音、环境声或音乐等垂直领域，即使混合领域（如歌声合成）也受限于特定模态。虽有先驱工作尝试覆盖全听觉频谱，但依赖刚性的预定义控制令牌。相比之下，Bagpiper能在一个片段中合成包含任意重叠组合的语音、音乐和音效的集成声学场景。此外，近期工作虽尝试用文本转录（语音）或简短字幕（非语音）实现部分统一，但本文证明丰富字幕是更优的全方位语义接口。同时，其他研究（如专注于音频理解的通用推理、基于扩散模型的语音编辑、流式实时检索的通用音频处理）也考虑了丰富字幕，但本文首次实现了理解与生成的统一。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为Bagpiper的80亿参数音频基础模型来解决开放端音频任务，其核心方法是利用“丰富描述”作为连接原始音频信号与高层认知概念的通用语义接口，并采用“描述-处理”的工作流来模拟中间认知推理步骤。整体架构基于编码器-适配器-LLM的统一框架，主要模块包括预训练音频编码器、MLP适配器、以Qwen3-8B-Base初始化的仅解码器LLM主干，以及用于音频生成的多流音频编解码器令牌预测模块。关键技术体现在三个方面：首先，在预训练阶段，通过大规模学习（6000亿令牌）建立原始音频与丰富描述之间的鲁棒双向映射，并采用分层数据处理策略（基于文本的分类、分层过滤和重采样）来平衡语音、音乐和音效的数据分布，同时保留基础LLM的文本处理能力。其次，在监督微调阶段，创新性地采用“描述-处理”流程进行数据模拟，即无论理解还是生成任务，都强制模型以丰富描述为中介进行推理：对于音频理解，模板为[音频, 用户请求, 丰富描述, 思维链, 答案]；对于音频生成，模板为[用户请求, 思维链, 丰富描述, 音频]。最后，通过多样化的用户请求模拟（基于属性列表或人物角色）和严格的自动质量保证（基于LLM的法官评估），构建高质量的训练数据，使模型无需任务特定先验即可解决多样任务。这种将物理信号映射到认知概念空间，并通过自然语言描述进行中间推理的设计，是实现统一音频理解与生成的关键创新。

### Q4: 论文做了哪些实验？

论文实验主要分为预训练模型能力评估和微调后任务解决能力验证两部分。

**实验设置与数据集**：评估主要使用LibriSpeech Test-Clean（语音）和MMAU-Mini（覆盖语音、音乐、音效的通用音频基准）。对比方法包括：在理解任务上对比Qwen3-Captioner、AudioFlamingo3、Qwen-2.5-Omni等；在生成任务上对比OpusLM、CosyVoice3（TTS）以及TangoFlux、AudioLDM2-L（TTA）。评估指标涵盖词错误率（WER）、MMAU-Mini准确率、Fréchet Audio Distance（FAD）、CLAP相似度以及循环一致性测试中的音频/文本相似度。

**主要结果**：
1. **预训练模型能力**：Bagpiper-Base（8B）在音频理解上，通过生成描述文本后由外部LLM完成任务，WER达5.0%，MMAU-Mini准确率69.0%，与30B的Qwen3-Captioner性能相当。在音频生成上，仅基于描述文本合成音频，WER低至1.8%，FAD为2.98，CLAP相似度0.55，优于或媲美专用TTS/TTA模型。循环一致性测试中，音频相似度0.502、文本相似度0.840，显著高于组合基线模型。
2. **微调后任务解决**：在ASR任务上，WER为2.5%；引入思维链推理后，MMAU-Mini准确率提升至74.5%。在开放任务上，AIR-Bench聊天子集得分6.57，优于Qwen-2.5-Omni（6.30）；AudioBench开放QA子集平均得分70.39，与AudioFlamingo3（70.45）接近。生成方面，TTS任务WER为2.7%，优于CosyVoice3（2.9%）；在复杂音频合成的人工评估中，Bagpiper对TangoFlux等基线的胜率显著领先，尤其在语音与音效/音乐混合合成上表现突出。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在推理延迟和复杂组合指令处理能力上。未来研究可从以下方向深入：首先，优化推理效率，例如探索轻量级中间表示或知识蒸馏技术，在保持性能的同时降低计算开销。其次，提升模型对复杂组合指令的理解与执行能力，可引入分层推理机制或外部知识库来分解多约束任务。此外，可探索更动态的提示工程，使模型能自适应调整推理深度。从更宏观角度看，如何将这种“描述-推理”范式扩展到多模态场景，实现跨模态的联合理解与生成，也是一个值得探索的方向。最后，模型的可解释性仍有提升空间，未来可设计更透明的中间表示，以增强人类对模型决策过程的理解与信任。

### Q6: 总结一下论文的主要内容

本文提出Bagpiper，一个80亿参数的音频基础模型，旨在通过“丰富字幕”作为通用语义代理，统一音频的理解与生成任务。核心问题是解决现有音频模型通常依赖特定任务监督、处理孤立音频因素，而无法像人类一样整体处理音频并连接物理信号与抽象认知概念的局限。方法上，模型首先在6000亿token的大规模语料上进行预训练，建立原始音频与高层认知概念（如转录、音频事件）之间的鲁棒双向映射；在微调阶段，采用“先描述后处理”的工作流程，模拟中间认知推理步骤，从而无需任务先验即可解决多样化任务。主要结论显示，Bagpiper在音频理解基准（如MMAU和AIRBench）上超越Qwen-2.5-Omni，在生成质量上优于CosyVoice3和TangoFlux，能够合成语音、音乐和音效的任意组合，并展现出精确时间可控性、融合世界知识等涌现行为。其意义在于将音频处理重构为可扩展的文本推理问题，推动了灵活、通用的音频智能发展。
