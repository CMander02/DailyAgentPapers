---
title: "Experience-Guided Self-Adaptive Cascaded Agents for Breast Cancer Screening and Diagnosis with Reduced Biopsy Referrals"
authors:
  - "Pramit Saha"
  - "Mohammad Alsharid"
  - "Joshua Strong"
  - "J. Alison Noble"
date: "2026-02-27"
arxiv_id: "2602.23899"
arxiv_url: "https://arxiv.org/abs/2602.23899"
pdf_url: "https://arxiv.org/pdf/2602.23899v1"
categories:
  - "cs.CV"
  - "cs.AI"
  - "cs.LG"
tags:
  - "多智能体系统"
  - "Agent 架构"
  - "记忆与检索"
  - "决策规划"
  - "医疗应用"
relevance_score: 7.5
---

# Experience-Guided Self-Adaptive Cascaded Agents for Breast Cancer Screening and Diagnosis with Reduced Biopsy Referrals

## 原始摘要

We propose an experience-guided cascaded multi-agent framework for Breast Ultrasound Screening and Diagnosis, called BUSD-Agent, that aims to reduce diagnostic escalation and unnecessary biopsy referrals. Our framework models screening and diagnosis as a two-stage, selective decision-making process. A lightweight `screening clinic' agent, restricted to classification models as tools, selectively filters out benign and normal cases from further diagnostic escalation when malignancy risk and uncertainty are estimated as low. Cases that have higher risks are escalated to the `diagnostic clinic' agent, which integrates richer perception and radiological description tools to make a secondary decision on biopsy referral. To improve agent performance, past records of pathology-confirmed outcomes along with image embeddings, model predictions, and historical agent actions are stored in a memory bank as structured decision trajectories. For each new case, BUSD-Agent retrieves similar past cases based on image, model response and confidence similarity to condition the agent's current decision policy. This enables retrieval-conditioned in-context adaptation that dynamically adjusts model trust and escalation thresholds from prior experiences without parameter updates. Evaluation across 10 breast ultrasound datasets shows that the proposed experience-guided workflow reduces diagnostic escalation in BUSD-Agent from 84.95% to 58.72% and overall biopsy referrals from 59.50% to 37.08%, compared to the same architecture without trajectory conditioning, while improving average screening specificity by 68.48% and diagnostic specificity by 6.33%.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决乳腺癌超声筛查和诊断过程中因特异性不足导致的过度诊断升级和不必要活检转诊问题。研究背景是乳腺癌作为全球女性最常见的癌症，超声因其在致密乳腺组织和资源有限环境中的适用性而被广泛用作一线筛查工具。然而，现有方法主要聚焦于开发分类或分割模型，缺乏智能化的分诊机制，导致大量低风险良性病例被过度升级至诊断环节，造成假阳性率高、活检转诊过多，从而增加了医疗系统负担、患者焦虑以及关键病例的诊疗延迟。

现有方法的不足在于传统系统通常依赖固定的决策逻辑，无法根据历史经验动态调整信任阈值，难以在保持高敏感性的同时有效提升特异性，从而无法缓解诊断拥堵和资源浪费。本文要解决的核心问题是设计一个能够模拟临床两级决策流程、并能利用历史经验进行自适应调整的智能体框架，以安全、选择性地过滤低风险病例，减少不必要的诊断升级和活检转诊。为此，论文提出了BUSD-Agent，一个经验引导的级联多智能体框架，通过轻量级筛查智能体初步筛选，高风险病例再升级至诊断智能体，并利用记忆库中病理确认的历史决策轨迹进行检索条件化的上下文适应，动态调整模型信任和升级阈值，实现无需参数更新的自我改进行为。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、应用类和评测类。

在**方法类**研究中，相关工作主要集中在开发用于乳腺超声的单一分类或分割模型，旨在提升诊断准确性。本文提出的BUSD-Agent框架与这些工作有显著区别：它并非一个单一的模型，而是一个**级联多智能体决策系统**，将筛查和诊断建模为一个两阶段的选择性决策过程。这超越了传统模型仅关注图像分析的模式，引入了基于风险评估的智能分流机制。

在**应用类**研究中，已有工作探索了AI在医学影像分析中的辅助诊断应用。本文的独特之处在于其**经验引导的自适应机制**。系统通过记忆库存储历史确诊案例的决策轨迹，并基于新案例的相似性进行检索，从而动态调整决策策略和信任阈值。这与大多数依赖固定规则或静态模型的应用不同，实现了无需参数更新的上下文自适应。

在**评测类**研究中，现有工作通常侧重于在单一或少数数据集上评估模型的分类性能（如准确率、AUC）。本文则在一个包含**10个不同乳腺超声数据集**的大规模集合上进行综合评估，不仅关注诊断准确性，更将**减少诊断升级和活检转诊率**作为核心评测指标，更贴合临床减少不必要医疗干预的实际需求。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为BUSD-Agent的经验引导级联多智能体框架来解决乳腺癌筛查与诊断中减少不必要活检转诊的问题。其核心方法是将临床工作流建模为一个两阶段、选择性的决策过程，并引入基于记忆的经验引导机制实现无需参数更新的上下文自适应。

整体框架采用级联设计，包含两个主要智能体模块。首先是“筛查诊所”智能体，它使用一组独立的乳腺癌分类模型作为工具，对输入的超声图像进行分析，并通过LLM协调层进行ReAct式多步推理，生成是否将病例升级到诊断阶段的二元决策。其目标是当恶性风险和不确定性估计较低时，筛选出良性和正常病例，避免不必要的升级。其次是“诊断诊所”智能体，它接收被升级的病例，并集成了更丰富的感知和放射学描述工具，包括多标签放射学特征预测器、微调的视觉语言模型（用于生成结构化文本报告）、基于边界框的病变定位模块、病变分割模块以及缩放叠加工具。LLM协调层整合这些诊断输出和筛查阶段的上下文，通过另一个ReAct循环进行结构化分析，最终做出活检转诊决策。

该框架的关键技术创新在于其“经验引导的上下文自适应”机制。系统维护一个记忆库，存储了具有病理确认结果的过往病例，每个病例被记录为包含图像嵌入、模型预测、智能体决策和最终活检确认标签的结构化决策轨迹。对于新病例，系统会从记忆库中检索最相似的过往案例。在筛查阶段，相似性基于图像嵌入和来自多个筛查分类器的恶性置信度向量的组合来计算。在诊断阶段，则在一个更丰富的联合特征空间中进行检索，该空间包含图像嵌入、多标签放射学特征预测和结构化放射学描述输出。检索到的相似轨迹被格式化为上下文示例集，提供给LLM作为先验知识，以影响当前决策。

这种方法使智能体能够动态调整对模型输出的信任度和升级阈值，识别历史上可靠或易错的工具输出模式，从而在没有参数更新的情况下，自适应地优化其升级策略和活检转诊政策。最终，该框架通过利用历史成功与失败的经验，显著减少了诊断升级率和总体活检转诊率，同时提高了筛查和诊断的特异性。

### Q4: 论文做了哪些实验？

实验在10个乳腺超声数据集上进行评估，包括BUET-BUSD、BUSBRA、BUS-UCLM等。实验设置采用GPT-4o作为编排模块，筛查阶段使用14个分类模型（如ConvNeXt、DeiT等），诊断阶段整合了微调的MedGemma-4B生成结构化报告，以及U-Net、YOLOv11和ResNet50多任务头进行病灶分割与属性识别。所有模型均在BUS-CoT数据集上预训练，超参数设为λ=0.5，K=10，并使用20%样本构建记忆库。

对比方法包括多个专有和开源视觉语言模型（VLMs），如GPT-4o、Gemini 2.5 Pro、Qwen 2.5 VL 32B等。主要结果显示，提出的经验引导框架（BUSD-Agent）在筛查阶段将诊断升级率从84.95%降至58.72%，总体活检转诊率从59.50%降至37.08%；筛查特异性平均提升68.48%，诊断特异性提升6.33%。在BUS-UCLM和BUS-BRA数据集上，筛查代理的平衡准确率分别达到78.29%和98.67%，诊断代理分别为71.58%和88.96%，均优于对比的VLMs。此外，消融实验表明，检索样本数K=10时性能最佳，且结合图像与置信度的检索策略比单一检索更有效。

### Q5: 有什么可以进一步探索的点？

本文提出的经验引导级联智能体框架在降低活检转诊率方面成效显著，但其局限性与未来探索方向值得深入探讨。首先，框架高度依赖历史决策轨迹的质量与规模，若记忆库中病例分布不均或存在偏差，可能影响检索条件化决策的泛化能力，未来需研究如何动态更新记忆库并引入去偏技术。其次，当前方法仅基于相似性检索调整模型信任阈值，未显式建模病例间的因果关联，可探索引入因果推理模块，使智能体更深入理解临床决策逻辑。此外，框架未整合多模态信息（如患者病史、基因组数据），未来可扩展为融合临床知识的跨模态决策系统，提升诊断全面性。从技术角度看，智能体工具链仍以传统影像分析模型为主，可探索集成大语言模型（LLM）增强报告解读与推理能力。最后，研究仅在超声数据集验证，需拓展至乳腺X线摄影、MRI等多模态筛查场景，并开展前瞻性临床试验以评估实际医疗环境中的效能与安全性。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为BUSD-Agent的经验引导级联多智能体框架，用于乳腺癌超声筛查与诊断，旨在减少诊断升级和不必要的活检转诊。核心问题在于传统筛查流程存在大量假阳性，导致过度诊断和活检转诊。方法上，框架模拟临床分流流程，分为两个阶段：轻量级“筛查诊所”智能体使用分类模型工具，在估计恶性风险和不确定性较低时筛选出良性/正常病例；高风险病例则升级至“诊断诊所”智能体，该智能体集成更丰富的感知和放射学描述工具进行二次决策。关键创新在于引入经验引导的策略自适应机制：将病理确认的过往病例（包括图像嵌入、模型预测、智能体行动）存储为结构化决策轨迹记忆库；针对新病例，基于图像、模型响应和置信度相似性检索相似历史案例，以此条件化当前决策策略，实现无需参数更新的动态模型信任度与升级阈值调整。主要结论显示，在10个乳腺超声数据集上的评估表明，相比无轨迹条件化的相同架构，该框架将诊断升级率从84.95%降至58.72%，总体活检转诊率从59.50%降至37.08%，同时筛查特异性平均提升68.48%，诊断特异性提升6.33%。该工作的意义在于通过经验引导的上下文自适应，显著优化了筛查与诊断的权衡，为临床决策支持系统提供了可减少不必要侵入性检查的高效AI解决方案。
