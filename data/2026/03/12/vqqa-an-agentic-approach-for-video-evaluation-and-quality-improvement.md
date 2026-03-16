---
title: "VQQA: An Agentic Approach for Video Evaluation and Quality Improvement"
authors:
  - "Yiwen Song"
  - "Tomas Pfister"
  - "Yale Song"
date: "2026-03-12"
arxiv_id: "2603.12310"
arxiv_url: "https://arxiv.org/abs/2603.12310"
pdf_url: "https://arxiv.org/pdf/2603.12310v1"
categories:
  - "cs.CV"
  - "cs.AI"
  - "cs.LG"
  - "cs.MA"
tags:
  - "Multi-Agent Framework"
  - "Prompt Optimization"
  - "Video Generation"
  - "Vision-Language Model"
  - "Evaluation"
  - "Black-Box Optimization"
  - "Semantic Feedback"
relevance_score: 7.5
---

# VQQA: An Agentic Approach for Video Evaluation and Quality Improvement

## 原始摘要

Despite rapid advancements in video generation models, aligning their outputs with complex user intent remains challenging. Existing test-time optimization methods are typically either computationally expensive or require white-box access to model internals. To address this, we present VQQA (Video Quality Question Answering), a unified, multi-agent framework generalizable across diverse input modalities and video generation tasks. By dynamically generating visual questions and using the resulting Vision-Language Model (VLM) critiques as semantic gradients, VQQA replaces traditional, passive evaluation metrics with human-interpretable, actionable feedback. This enables a highly efficient, closed-loop prompt optimization process via a black-box natural language interface. Extensive experiments demonstrate that VQQA effectively isolates and resolves visual artifacts, substantially improving generation quality in just a few refinement steps. Applicable to both text-to-video (T2V) and image-to-video (I2V) tasks, our method achieves absolute improvements of +11.57% on T2V-CompBench and +8.43% on VBench2 over vanilla generation, significantly outperforming state-of-the-art stochastic search and prompt optimization techniques.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决视频生成模型在复杂用户意图对齐方面的挑战，以及现有评估和优化方法的不足。研究背景是，尽管扩散模型和Transformer架构的突破推动了视觉生成模型的快速发展，使其能够生成高分辨率动态场景，但生成的视频仍经常出现构图错误、时间不一致和物理幻觉等问题，用户往往需要通过繁琐的试错式提示工程来调整。同时，现有的评估方法未能跟上模型发展的步伐：早期指标仅衡量基本的视觉分布，忽略了复杂的组合对齐；而全面的基准测试虽然能解决此问题，但通常需要大型、专门的模型集合，计算开销巨大。此外，基于回归器或视觉语言模型（VLM）的评分系统只能作为被动观察者，无法灵活适应新任务或提供可操作的反馈来纠正生成内容。

现有方法的不足主要体现在两个方面：一是现有的视频测试时优化方法通常要么计算成本高昂（例如依赖成对锦标赛的VISTA），要么需要白盒访问模型内部参数，限制了其适用性和效率；二是缺乏一个可解释的、闭环的系统，能够诊断视觉缺陷并通过黑盒自然语言接口迭代优化视频。

因此，本文要解决的核心问题是：如何构建一个统一、高效且可泛化的框架，能够主动评估视频质量，并提供可操作的反馈以迭代优化生成提示，从而显著提升视频生成模型与复杂用户意图的对齐能力，同时避免高计算成本和白盒访问需求。为此，论文提出了VQQA（Video Quality Question Answering）框架，这是一个多智能体系统，通过动态生成视觉问题并利用VLM的批判作为语义梯度，将被动评估转化为可解释的、可操作的反馈，实现基于黑盒自然语言接口的高效闭环提示优化。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：视频生成评估方法、提示词优化技术以及推理时计算扩展方法。

在**视频生成评估方法**方面，早期工作依赖基于参考的指标（如FVD、IS），但其与人类感知相关性弱且无法提供可操作的反馈。随后，研究转向基于视觉语言模型（VLM）的评估，例如CLIPScore、BLIP-Score（缺乏时序感知），以及更近的VQAScore、T2VQA和VideoScore2（引入思维链推理）。然而，这些方法多为静态、预定义维度的被动评估。本文的VQQA则是一个主动的、多智能体框架，能动态生成针对具体视频问题的视觉问答，提供可解释、可操作的反馈，从而直接支持下游优化。

在**提示词优化技术**方面，早期文本领域工作（如APE、Promptist）和视频领域工作（如Prompt-A-Video、VPO）通常基于数据集级先验进行“开环”优化，而非针对当前生成的具体视觉缺陷。大语言模型中的自我修正方法（如Self-Refine）在视频生成中探索较少，虽有VideoRepair等局部修复方法，但难以处理全局不一致问题。VQQA提出了一个“闭环”系统，基于细粒度视觉证据迭代更新整个提示词，以同时纠正局部和全局错误。

在**推理时计算扩展方法**方面，大语言模型中的思维树（ToT）等技术通过迭代推理提升性能。视频生成中则表现为拒绝采样、轨迹搜索（如Video-T1、VISTA）或直接对模型内部进行梯度更新（如Video-TTT、EvoSearch）。前者计算成本高昂，后者需要白盒模型访问权限。VQQA受TextGrad等文本优化工作启发，将VLM批评作为语义梯度，仅通过自然语言接口实现精确适配和错误纠正，避免了权重访问和大量采样，在效率和通用性上具有优势。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为VQQA的多智能体框架来解决视频生成模型输出与复杂用户意图对齐的挑战。其核心方法是用一个可解释的、基于反馈的闭环优化过程，替代传统计算昂贵或需要白盒模型访问的测试时优化方法。

整体框架包含三个核心智能体模块，形成一个迭代优化循环。首先，**问题生成（QG）智能体**会动态分析生成的视频、原始提示词和生成条件，并围绕“视频-提示词对齐”、“视觉质量”和“条件保真度”三个维度生成一系列具体的视觉问题。这确保了评估能系统性地覆盖关键缺陷模式。接着，**问题回答（QA）智能体**作为主要评估器，针对这些问题检查视频，为每个问题给出量化的分数（0-100）并生成详细的诊断报告，从而构建出一张缺陷语义地图。最后，**提示词优化（PR）智能体**扮演关键角色，它将QA智能体输出的低分项及其诊断（即“语义梯度”）进行综合处理，并生成一个经过修订的、旨在同时解决这些具体缺陷的新提示词，用于驱动下一轮视频生成。

该方法的创新点主要体现在三个方面：一是提出了“语义梯度”的概念，利用VLM生成的、人类可理解的文本批评作为优化信号，绕过了对离散文本进行传统梯度下降的难题，实现了通过黑盒自然语言接口进行高效优化。二是设计了**全局VLM评分器**和**收敛准则**作为保障机制。全局评分器在迭代结束后对所有候选视频进行整体评估，选择与原始意图最对齐的视频，防止迭代过程中的语义漂移；收敛准则则通过目标满足或性能饱和判断来平衡计算成本与质量提升。三是框架的通用性，它不依赖于特定生成模型的内部结构，可适用于文本到视频和图像到视频等多种任务和输入模态，通过多智能体分工协作将评估与优化统一在一个流程中。

### Q4: 论文做了哪些实验？

论文在文本到视频（T2V）和图像到视频（I2V）生成任务上进行了广泛的实验评估。实验设置方面，VQQA作为一个任务无关的优化器，使用相同的迭代优化流程处理两种任务，无需修改架构。主要对比方法包括：1）视频提示优化（VPO）；2）基于不同评分函数的Best-of-N（BoN）随机搜索策略，具体使用了VQAScore、VideoScore2和VLM-Rating（GPT-4o、Gemini-3-Pro等）作为评分机制。

实验使用了三个基准测试数据集：T2V-CompBench（包含1400个提示，评估七个组成类别）、VBench2（评估五个高级维度：人类保真度、可控性、创造力、物理、常识）和VBench-I2V（用于I2V任务，评估与参考图像的对齐度）。主要视频生成模型为CogVideoX-5B（及其I2V变体），并额外在Google Veo 3.1模型上进行了测试以验证方法的模型无关性。

主要结果如下：在T2V-CompBench上，使用Gemini-3-Pro的VQQA取得了53.46%的平均分，相比原始生成（41.89%）绝对提升了+11.57%，并超越了所有基线（最佳基线VQAScore为48.70%）。在VBench2上，VQQA（Gemini-3-Pro）总分为50.41%，相比原始生成（41.98%）提升+8.43%。在VBench-I2V上，VQQA（Gemini-3-Pro）平均分达到97.86%，相比原始生成（96.62%）提升+1.24%。此外，消融实验表明VQQA在视觉缺陷识别的端到端召回率（E2E-Recall）上达到82.08%，显著优于直接VLM分析基线（70.18%）。收敛性分析显示，算法通常在3.8到4.2次迭代内达到饱和，高效地捕获了主要性能增益。在Veo 3.1模型上的实验也证实了VQQA的有效性，其T2V-CompBench平均分达到61.81%，优于所有对比方法。

### Q5: 有什么可以进一步探索的点？

本文提出的VQQA框架虽在多模态视频生成优化上取得显著效果，但仍存在若干局限和可拓展方向。首先，其依赖的视觉语言模型（VLM）本身存在幻觉和语义理解偏差，可能影响生成反馈的准确性；未来可探索更鲁棒的VLM或引入多模型交叉验证机制。其次，当前方法主要针对视觉伪影和构图优化，对视频时序连贯性、物理合理性等动态特性的评估能力有限，需设计更具时序感知的问答策略。此外，框架的迭代优化效率虽高，但未考虑计算成本与质量提升的权衡，可引入自适应终止机制。从更广视角看，该智能体框架可扩展至多轮人机协作场景，允许用户介入反馈循环，或结合强化学习使智能体自主探索更优的提示策略。最后，将其应用于3D生成、跨模态编辑等新兴领域，也是值得探索的方向。

### Q6: 总结一下论文的主要内容

本文针对视频生成模型输出与复杂用户意图对齐的挑战，提出了一种名为VQQA的多智能体框架。该框架的核心贡献在于将传统的被动视频质量评估，转变为一种主动、闭环的提示词优化过程。其方法是通过动态生成视觉问题，并利用视觉语言模型（VLM）的评判作为“语义梯度”，来替代计算昂贵或需白盒模型访问的传统优化方法。VQQA通过黑盒的自然语言接口，提供人类可理解、可操作的反馈，从而高效地迭代优化生成提示。实验表明，该方法能有效定位并修复视觉瑕疵，在文本生成视频和图像生成视频任务上，仅需少量优化步骤即可显著提升生成质量，性能超越现有的随机搜索和提示优化技术。这为可控、可解释的AI内容生成提供了一种可扩展且与任务无关的解决方案。
