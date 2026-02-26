---
title: "FewMMBench: A Benchmark for Multimodal Few-Shot Learning"
authors:
  - "Mustafa Dogan"
  - "Ilker Kesen"
  - "Iacer Calixto"
  - "Aykut Erdem"
  - "Erkut Erdem"
date: "2026-02-25"
arxiv_id: "2602.21854"
arxiv_url: "https://arxiv.org/abs/2602.21854"
pdf_url: "https://arxiv.org/pdf/2602.21854v1"
categories:
  - "cs.CL"
tags:
  - "多模态大语言模型"
  - "上下文学习"
  - "思维链"
  - "基准测试"
  - "少样本学习"
  - "模型评估"
relevance_score: 5.5
---

# FewMMBench: A Benchmark for Multimodal Few-Shot Learning

## 原始摘要

As multimodal large language models (MLLMs) advance in handling interleaved image-text data, assessing their few-shot learning capabilities remains an open challenge. In this paper, we introduce FewMMBench, a comprehensive benchmark designed to evaluate MLLMs under few-shot conditions, with a focus on In-Context Learning (ICL) and Chain-of-Thought (CoT) prompting. Covering a diverse suite of multimodal understanding tasks, from attribute recognition to temporal reasoning, FewMMBench enables systematic analysis across task types, model families, and prompting strategies. We evaluate 26 open-weight MLLMs from six model families across zero-shot, few-shot, and CoT-augmented few-shot settings. Our findings reveal that instruction-tuned models exhibit strong zero-shot performance but benefit minimally, or even regress, with additional demonstrations or CoT reasoning. Retrieval-based demonstrations and increased context size also yield limited gains. These results highlight FewMMBench as a rigorous testbed for diagnosing and advancing few-shot capabilities in multimodal LLMs. The data is available at: https://huggingface.co/datasets/mustafaa/FewMMBench

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前多模态大语言模型（MLLMs）评估中存在的关键缺口：缺乏一个系统、全面的基准来评测模型在少样本学习（few-shot learning）情境下的能力。随着MLLMs（如GPT-4V）的快速发展，它们不仅能处理交错的图像-文本输入，还展现出更强的通用多模态推理和指令遵循能力。然而，现有主流基准（如MMBench、SeedBench、MME）主要聚焦于零样本（zero-shot）评估或特定孤立能力（如视觉推理），未能系统化地测试模型在少样本情境学习（In-Context Learning, ICL）和思维链（Chain-of-Thought, CoT）提示下的表现。具体而言，现有方法不足在于：它们没有在交错多模态上下文中，对模型如何利用少量演示示例进行学习，以及如何通过生成中间推理步骤来提升性能，进行严谨、跨任务、跨模型家族的诊断分析。

因此，本文的核心问题是：如何构建一个专门的基准，以系统评估MLLMs在少样本条件（包括ICL和CoT提示）下的学习与推理能力，并诊断当前模型在此类设置中的局限性与提升潜力。为此，论文提出了FewMMBench基准，涵盖从属性识别到时序推理的九种多样化任务，并设计了随机与基于检索的演示示例选择策略，以及CoT增强的少样本设置。通过对六大模型家族、26个开源MLLMs的广泛评估，研究揭示了重要发现：例如，经过指令微调的模型在零样本下表现强劲，但增加演示示例或CoT推理往往带来有限增益甚至性能倒退。这些结果凸显了FewMMBench作为一个严谨测试平台的价值，用于诊断和推动多模态大语言模型少样本能力的发展。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：多模态大模型（MLLM）评测基准、少样本学习与思维链（CoT）研究，以及多模态推理评估方法。

在**评测基准**方面，已有工作如VHELM提供了涵盖感知、推理、公平性等多维度的标准化评估框架；MM-Vet v2和CURE则专注于评估组合推理或思维链一致性等特定能力。然而，这些基准大多未系统考察少样本情境下的学习能力。专门针对少样本的基准如VL-ICL Bench缺乏CoT示例，M³CoT虽提供CoT理由但演示样本随机选择，降低了上下文对齐性；VisualCoT则提供程序性指令而非推理轨迹。FewMMBench与这些工作的区别在于，它专门设计了一个统一的、基于语言现象分类的少样本评估框架，并提供了语义对齐的演示样本和明确的CoT理由，从而能系统分析模型如何从上下文中习得推理模式。

在**少样本与CoT研究**方面，先前研究发现，CoT示例相对于零样本CoT可能收益有限，多模态模型尽管经过混合模态预训练仍难以有效进行上下文学习（ICL），且微调可能损害推理行为的稳定性。FewMMBench直接针对这些开放性问题，通过提供结构化的演示和明确的CoT理由，在受控的少样本设置下进行诊断性评估。

在**评估方法**上，其他工作如Mementos关注序列图像推理，VisDialHallBench研究多轮视觉对话中的幻觉，MMIU和MIBench探究多图像协调与空间推理。这些基准与少样本推理评估正交，未提供结构化演示或分析模型如何学习推理模式。本文的独特贡献在于引入了基于图割（Graph Cut）的支撑集构建方法以确保多样性和代表性，并采用基于困惑度的准确率及不确定性量化来缓解ICL的顺序敏感性，从而实现了更稳定、更具诊断性的评估。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为FewMMBench的综合性基准测试来解决评估多模态大语言模型（MLLMs）在少样本学习（特别是上下文学习和思维链提示）中能力的问题。其核心方法、架构设计和关键技术如下：

**整体框架与主要模块**：
FewMMBench是一个系统化的评估基准，其整体框架围绕一个精心策划的数据集构建流程展开。该流程包含两个核心步骤：1）基于视觉-文本相似性指导，选择具有代表性和挑战性的样本；2）生成显式的思维链解释以指导模型推理。基准涵盖了九大任务类型，形成一个完整的评估套件，包括属性识别、物体识别、复数识别、物体计数、空间关系理解、动作识别、常识推理、时序推理和指代消解。每个任务都配备了查询集（供模型解答）和演示集（提供少样本示例以支持上下文学习）。

**关键技术细节与创新点**：
1.  **基于子模优化的示例选择策略**：这是核心创新之一。为了在演示集中最大化任务覆盖度并最小化冗余，论文摒弃了传统的聚类方法，采用了一种基于图割函数的子模选择策略。该策略通过平衡样本间的相似性，自动选择最具代表性和多样性的250个查询样本（每个任务）。随后，为每个查询检索其最相似的8个样本来构建演示集，确保了上下文的相关性，支持了少样本评估中的局部泛化。
2.  **高质量的思维链生成与校正**：为了研究逐步推理的效果，论文为少样本演示样本自动生成了思维链解释。由于源数据集缺乏此类标注，研究使用Qwen2.5-VL-7B-Instruct模型来生成答案和文本解释。关键创新在于一个迭代校正过程：如果预测答案错误或解释不完整，系统会注入正确答案并重新生成思维链。这一过程确保了最终的思维链示例忠实于真实情况，并保持了高质量的事实准确性，部分结果还经过了人工验证。
3.  **系统化的任务设计与数据整合**：FewMMBench的创新还体现在其广泛而系统的任务设计上。它并非创建全新数据，而是从MMBench、SeedBench、VALSE、ARO、MileBench等十余个现有权威数据集中，精心筛选和整合了特定维度的任务，构建了一个覆盖从低级感知到高级认知推理的多样化评估体系。这种整合方式既保证了基准的全面性和代表性，又使其建立在坚实的现有工作基础之上。

总之，论文通过设计一个结构严谨的基准构建流程，结合创新的子模优化示例选择方法和自动化的思维链生成与校正技术，系统化地解决了对MLLMs进行少样本能力评估的挑战。FewMMBench作为一个诊断工具，能够深入分析不同任务类型、模型家族和提示策略下的模型表现。

### Q4: 论文做了哪些实验？

论文在FewMMBench基准上进行了系统性实验，评估了26个开源多模态大语言模型（MLLMs）的少样本学习能力。实验设置方面，评估了来自六个模型家族（Qwen、InternVL、Idefics、Phi、LLaVA、xGen-MM）的模型，参数规模从0.5B到9B不等，包括指令微调和非指令微调变体。评估任务涵盖多模态理解任务（如属性识别、时序推理），采用多项选择题形式，主要评估指标为准确率（Accuracy）。实验对比了零样本、少样本（4-shot和8-shot）以及思维链（CoT）增强的少样本设置，并比较了随机选择示例与基于检索的相似示例两种演示构建方式。

主要结果发现：1）指令微调模型（如Qwen2.5-VL-7B）在零样本下表现强劲，但少样本演示带来的提升有限甚至出现性能下降；而非指令微调的基础模型则能从少样本示例中获得显著提升（部分达两位数百分比增长）。2）基于检索的演示相比随机选择未显示出明显优势，两者性能几乎相同。3）增加演示数量（从4-shot到8-shot）并未带来一致性能提升，有时甚至导致准确率下降。4）思维链提示在所有测试模型和任务类型中均导致性能下降，表明当前CoT技术与多模态推理需求存在不匹配。这些结果揭示了当前MLLMs在少样本学习中的局限性，为未来研究提供了重要诊断依据。

### Q5: 有什么可以进一步探索的点？

基于论文结论和摘要，该研究揭示了当前多模态大模型在少样本学习上的核心局限，未来可从多个维度深入探索。首先，论文指出指令微调模型在零样本表现良好，但增加示例或思维链提示后收益甚微甚至倒退，这暗示模型可能过度依赖预训练知识而难以动态适应新上下文。未来可研究更高效的示例选择与组织策略，例如引入元学习或动态示例加权机制，而非简单检索。其次，检索式示例选择效果有限，说明当前相似性度量可能无法捕捉任务本质，可探索基于任务感知的检索或生成式示例合成。此外，思维链在多模态场景中引发性能下降，需设计更适合跨模态推理的提示结构，如分步视觉-语言对齐机制。最后，基准任务虽覆盖多样，但未涉及复杂决策或交互式学习，未来可扩展至需多轮反馈的在线少样本学习场景，以更全面评估模型泛化能力。

### Q6: 总结一下论文的主要内容

该论文提出了FewMMBench基准，旨在系统评估多模态大语言模型（MLLMs）在少样本学习场景下的能力，尤其关注上下文学习（ICL）和思维链（CoT）提示的效果。核心问题是现有评估缺乏对MLLMs少样本性能的全面测试，该工作通过构建涵盖属性识别、时序推理等多种任务的数据集来填补这一空白。

方法上，FewMMBench设计了零样本、少样本及CoT增强少样本三种设置，并比较了不同任务类型、模型家族和提示策略的影响。作者评估了来自六个家族的26个开源MLLMs，发现指令微调模型在零样本下表现良好，但增加示例或CoT推理后提升有限甚至出现倒退，检索增强示例和扩大上下文窗口也收效甚微。

主要结论指出，当前MLLMs的少样本学习能力仍显不足，传统提升策略在多模态场景下效果不显著。该基准为诊断和推进MLLMs的少样本能力提供了严谨测试平台，有助于未来研究优化模型在有限示例下的泛化与推理性能。
