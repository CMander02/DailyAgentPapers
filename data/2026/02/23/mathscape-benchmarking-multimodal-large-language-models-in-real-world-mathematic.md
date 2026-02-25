---
title: "MathScape: Benchmarking Multimodal Large Language Models in Real-World Mathematical Contexts"
authors:
  - "Hao Liang"
  - "Linzhuang Sun"
  - "Minxuan Zhou"
  - "Zirong Chen"
  - "Meiyi Qiang"
  - "Mingan Lin"
  - "Tianpeng Li"
  - "Fan Yang"
  - "Zenan Zhou"
  - "Wentao Zhang"
date: "2024-08-14"
arxiv_id: "2408.07543"
arxiv_url: "https://arxiv.org/abs/2408.07543"
pdf_url: "https://arxiv.org/pdf/2408.07543v6"
categories:
  - "cs.CV"
  - "cs.CL"
tags:
  - "Agent Benchmarking"
  - "Multimodal Reasoning"
  - "Mathematical Reasoning"
  - "Real-World Scenarios"
  - "MLLM Evaluation"
relevance_score: 7.5
---

# MathScape: Benchmarking Multimodal Large Language Models in Real-World Mathematical Contexts

## 原始摘要

With the rapid progress of Multimodal LLMs, evaluating their mathematical reasoning capabilities has become an increasingly important research direction. In particular, visual-textual mathematical reasoning serves as a key indicator of an MLLM's ability to comprehend and solve complex, multi-step quantitative problems. While existing benchmarks such as MathVista and MathVerse have advanced the evaluation of multimodal math proficiency, they primarily rely on digitally rendered content and fall short in capturing the complexity of real-world scenarios. To bridge this gap, we introduce MathScape, a novel benchmark focused on assessing MLLMs' reasoning ability in realistic mathematical contexts. MathScape comprises 1,369 high-quality math problems paired with human-captured real-world images, closely reflecting the challenges encountered in practical educational settings. We conduct a thorough multi-dimensional evaluation across nine leading closed-source MLLMs, three open-source MLLMs with over 20 billion parameters, and seven smaller-scale MLLMs. Our results show that even state-of-the-art models struggle with real-world math tasks, lagging behind human performance, highlighting critical limitations in current model capabilities. Moreover, we find that strong performance on synthetic or digitally rendered images does not guarantee similar effectiveness on real-world tasks. This underscores the necessity of MathScape in the next stage of multimodal mathematical reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前多模态大语言模型在真实世界数学推理场景中评估不足的问题。随着多模态大语言模型的快速发展，评估其数学推理能力已成为重要研究方向。现有基准如MathVista和MathVerse主要依赖数字渲染内容，虽然推动了多模态数学能力评估，但未能充分捕捉真实场景的复杂性。这些合成数据无法反映实际应用中用户常基于打印文档或屏幕照片提问的情况，忽略了图像质量变化、上下文模糊性等现实挑战，导致模型在合成数据上的强表现未必能迁移到真实任务。

因此，本文的核心问题是：如何构建一个更贴近实际教育场景的基准，以全面评估MLLMs在真实世界数学上下文中的推理能力。为此，作者提出了MathScape基准，包含1,369个与真人拍摄的真实世界图像配对的高质量数学问题，模拟实际学习环境中的挑战。通过系统评估多个领先模型，研究发现即使最先进的模型在真实数学任务上也表现不佳，落后于人类水平，且合成图像上的优势不能保证现实有效性，凸显了当前模型能力的局限性和开发此类基准的必要性。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕多模态数学推理评测基准展开，可分为以下几类：

**现有评测基准**：MathVista 专注于视觉数学问答，涵盖算术、代数等多个领域；MATH-V 主要采用数学竞赛题目评估多模态数学理解；MathVerse 通过链式思维（CoT）推理评估模型对视觉图表的理解能力；CMMU 则是大规模中文多学科多模态理解基准，题目来源于大学考试和教材。

**本文与现有工作的关系与区别**：上述基准均推动了多模态数学能力评测的发展，但它们的共同局限是主要依赖数字渲染或合成图像，未能充分反映真实世界场景的复杂性。MathScape 与这些工作一脉相承，都旨在评估MLLMs的数学推理能力，但其核心区别在于**专注于真实世界语境**。它通过使用人工拍摄的真实世界图像构建问题，更贴近实际教育环境中的挑战，从而弥补了现有基准在现实复杂性捕捉上的不足。实验也证实，在合成图像上表现优异的模型，在MathScape的真实任务上可能表现不佳，这凸显了该新基准的必要性和独特性。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为MathScape的新型基准测试来解决评估多模态大语言模型在真实世界数学场景中推理能力不足的问题。其核心方法围绕一个高质量、多维度评估数据集的创建与一套精细化的自动评估流程展开。

整体框架分为数据准备、多维分类和评估方法三个主要部分。首先，在数据准备阶段，研究团队从中国中小学教育题库中收集了1,369道数学题，涵盖小学到高中，并标注了难易度。关键创新在于对视觉数据的模拟：他们将题目文档转为PDF后，并非使用数字渲染图像，而是通过拍摄打印稿和屏幕显示的方式来获取图像，从而最大程度地模拟了现实世界中（如试卷、作业本）遇到的复杂、非理想的视觉条件。随后，通过雇佣数学专业研究生进行人工验证，确保了数据和答案的高质量。

其次，论文设计了一个多维度的分类体系来结构化评估。主要模块包括按**问题类型**（选择题、填空题/解答题、证明题）、**数学知识领域**（代数、几何、概率统计等）以及**教育阶段**进行划分。这种分类由多名标注者独立完成并通过仲裁达成一致，确保了评估能够细致地分析模型在不同结构、不同领域、不同复杂度问题上的表现。

最后，在评估技术上，论文提出了一种针对长答案（如解答题）的两步自动评分法，这是一个重要的创新点。第一步是**答案分割**：提示LLM将复杂的多步解答分解为多个专注于特定方面的子答案。第二步是**子答案评分**：使用特定的提示词自动对每个子答案进行独立评分。这种方法实现了对模型推理过程更细粒度的分析，而非仅仅判断最终答案对错。该自动评估方法的有效性得到了人工验证，与人类判断的一致性超过97%，证明了其可靠性。

### Q4: 论文做了哪些实验？

论文在MathScape基准上进行了全面的实验评估。实验设置采用零样本推理，配置包括最大token数2048、top-k为5、温度0.3和重复惩罚1.05，所有实验在NVIDIA H100 GPU上运行。

使用的数据集是论文提出的MathScape基准，包含1,369道与现实世界图像配对的高质量数学题，涵盖选择题、解答题和证明题等类型，以及代数、几何、方程、函数、概率统计等知识领域，并按小学、初中、高中教育阶段划分难度。

评估了19个多模态大语言模型（MLLM），包括9个闭源模型（如GPT-4V、GPT-4o、Claude-3-Opus等）、3个超过200亿参数的开源大模型（如Qwen2-VL-72B、Yi-VL-34B）和7个小规模开源模型（如Qwen2-VL-7B、DeepSeek-VL2-4.5B）。作为对比，还设置了随机猜测和频率基线，并引入了人类表现（76.96%准确率）。

主要结果显示：1）所有模型在MathScape上表现均远低于人类，最优模型GPT-4o平均准确率为42.47%，GPT-4o（PDF版）为43.89%，开源最佳模型Qwen2-VL-72B为38.67%，凸显了基准的挑战性。2）模型在现实世界图像上表现显著差于纯净PDF输入，例如LLaVA-OneVision-72B在PDF上准确率从8.31%提升至30.56%，表明合成数据性能不能迁移到真实场景。3）模型预测稳定性不足，在300道题的五次重复测试中，仅约25%的问题能全部答对。关键指标上，模型在证明题上表现相对较好（如GPT-4o达66.79%），但在解答题上较弱；代数题表现最佳（GPT-4o达50.58%），几何题较差；且性能随教育阶段升高而下降，例如GPT-4o在小学、初中、高中阶段平均准确率分别为49.22%、45.56%、35.73%。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其基准数据集规模相对有限（1,369个问题），且主要聚焦于静态图像与文本结合的数学问题，未涵盖动态、交互式或视频形式的多模态数学场景。未来研究方向可首先扩展数据集的多样性和规模，纳入更多元化的现实世界数学应用场景，如工程图纸、科学图表或日常生活中的动态问题（如物体运动轨迹计算）。其次，可探索模型在数学推理中的可解释性，例如要求模型输出中间推理步骤或可视化思维链，以增强其可靠性和教育应用价值。此外，结合领域自适应技术，使模型能更好地处理不同文化背景或教育体系下的数学表述差异，也是一个值得深入的方向。最后，可研究如何将符号计算系统与MLLMs结合，以弥补当前模型在精确符号推理方面的不足，提升解决复杂数学问题的准确性。

### Q6: 总结一下论文的主要内容

该论文针对现有多模态大语言模型数学推理评估主要依赖数字渲染内容、难以反映真实世界复杂性的局限，提出了MathScape基准。其核心贡献是构建了一个包含1,369道高质量数学问题与真实拍摄图像配对的数据集，紧密贴合实际教育场景中的挑战，旨在评估模型在真实数学情境下的推理能力。

研究方法上，论文对九种领先的闭源MLLM、三种参数量超过200亿的开源MLLM以及七种较小规模的MLLM进行了全面的多维度评估。主要结论表明，即使是当前最先进的模型在真实世界数学任务上也表现挣扎，显著落后于人类水平，这揭示了现有模型能力的严重不足。此外，研究发现模型在合成或数字渲染图像上的强劲表现并不能保证其在真实任务上的同等有效性。

该工作的意义在于凸显了现有评估范式的不足，并证明了MathScape对于推动多模态数学推理迈向下一发展阶段、促进模型处理真实世界复杂问题的必要性。
