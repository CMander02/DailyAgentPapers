---
title: "Slm-mux: Orchestrating small language models for reasoning"
authors:
  - "Chenyu Wang"
  - "Zishen Wan"
  - "Hao Kang"
  - "Emma Chen"
  - "Zhiqiang Xie"
  - "Tushar Krishna"
  - "Vijay Janapa Reddi"
  - "Yilun Du"
date: "2025-10-06"
arxiv_id: "2510.05077"
arxiv_url: "https://arxiv.org/abs/2510.05077"
pdf_url: "https://arxiv.org/pdf/2510.05077v2"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent 架构"
  - "多智能体系统"
  - "模型编排"
  - "小语言模型"
  - "推理"
relevance_score: 9.0
---

# Slm-mux: Orchestrating small language models for reasoning

## 原始摘要

With the rapid development of language models, the number of small language models (SLMs) has grown significantly. Although they do not achieve state-of-the-art accuracy, they are more efficient and often excel at specific tasks. This raises a natural question: can multiple SLMs be orchestrated into a system where each contributes effectively, achieving higher accuracy than any individual model? Existing orchestration methods have primarily targeted frontier models (e.g., GPT-4) and perform suboptimally when applied to SLMs. To address this gap, we propose a three-stage approach for orchestrating SLMs. First, we introduce SLM-MUX, a multi-model architecture that effectively coordinates multiple SLMs. Building on this, we develop two optimization strategies: (i) a model selection search that identifies the most complementary SLMs from a given pool, and (ii) test-time scaling tailored to SLM-MUX. Our approach delivers strong results: Compared to existing orchestration methods, our approach achieves up to 13.4% improvement on MATH, 8.8% on GPQA, and 7.0% on GSM8K. With just two SLMs, SLM-MUX outperforms Qwen 2.5 72B on GPQA and GSM8K, and matches its performance on MATH. We further provide theoretical analyses to substantiate the advantages of our method. Additional experiments show that the core principle of SLM-MUX extends to open-ended generation tasks (e.g., HumanEval) and benefits other model classes, including frontier LLMs and domain-specific fine-tuned SLMs. In summary, we demonstrate that SLMs can be effectively orchestrated into more accurate and efficient systems through the proposed approach. The project page is available at https://slm-mux.github.io/.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决一个核心问题：如何有效地编排（orchestrate）多个小语言模型（SLMs），使它们协同工作，以超越单个模型（包括单个SLM和大型前沿模型）的性能。作者观察到，随着语言模型的快速发展，SLMs的数量显著增长。虽然它们在特定任务上表现出色且更高效，但单个SLM的准确率通常无法达到最先进的水平。现有的编排方法（如基于讨论的LLM-Debate、Mixture-of-Agents等）主要针对GPT-4等前沿大模型设计，当直接应用于SLMs时，性能反而会下降（甚至导致高达5.5%的准确率损失）。论文发现，SLMs在讨论中容易出现“群体思维”（groupthink），倾向于强化错误而非纠正错误。因此，本文的核心目标是填补这一空白，提出一种专门为SLMs设计的三阶段编排方法，以构建一个比任何单个模型都更准确、更高效的系统。

### Q2: 有哪些相关研究？

相关研究主要分为两类：一是针对大模型的智能体协作与编排方法，二是提升模型推理性能的集成技术。
1. **基于讨论的编排方法**：论文重点对比了三种方法：**LLM-Debate**（通过辩论提升事实性和推理）、**Mixture-of-Agents**（通过分层聚合多个智能体的响应来增强LLM）、以及**Multi-Agent Verification**（通过多智能体验证来扩展测试时计算）。这些方法在编排前沿LLM时有效，但论文发现它们不适用于SLMs，甚至会损害性能。
2. **集成与采样方法**：**Self-Consistency**（自洽性解码）通过对单个模型进行多次采样并投票来提升性能，本文将其作为重要基线（Single-Best-SC）。**Agent Forest** 是一种通过从多个模型中采样并构建决策森林的方法，论文将其作为计算扩展（增加每个模型的采样数）的对比基线。
3. **模型选择与集成学习**：传统集成学习（如模型平均、堆叠）和神经架构搜索中的模型选择思想为本文的模型选择搜索策略提供了背景。本文的工作与这些研究的区别在于，它首次系统性地研究了SLMs特有的编排挑战（如群体思维），并提出了一种专为SLMs设计的、结合了架构创新和优化策略的完整解决方案。

### Q3: 论文如何解决这个问题？

论文提出了一个名为 **SLM-MUX** 的三阶段方法，专门用于编排小语言模型以进行推理任务。

**第一阶段：核心架构 SLM-MUX**
这是方法的基础，一个多模型编排架构。其核心思想是避免SLMs之间直接的、可能导致群体思维的交互式讨论。具体操作如下：对于每个输入问题，让每个参与的SLM独立生成多轮答案（例如，温度=0.3下生成三轮）。然后，为每个模型计算一个置信度分数：统计其多轮生成中出现最频繁的答案的次数。每个模型的最终输出就选定为该最频繁答案（若出现平局，则选择在验证集上准确率最高的模型的答案）。最后，SLM-MUX从所有参与模型的这些“最终输出”中，通过多数投票或置信度加权的方式选出系统的最终答案。这种“先生成后聚合”的管道，避免了模型在生成过程中的相互影响，从而缓解了群体思维问题。

**第二阶段：模型选择搜索**
为了从候选模型池中选出最具互补性的SLMs子集进行编排，论文设计了一个基于验证集的搜索策略。搜索目标函数平衡了两个因素：1) **并集准确率**：即至少有一个模型能正确回答的问题比例，衡量模型的覆盖能力；2) **矛盾惩罚**：衡量不同模型对同一问题给出不同答案的程度，过高的矛盾可能意味着难以达成共识。目标函数为：并集准确率 - λ * 矛盾惩罚（λ为超参数）。通过优化此目标，可以为给定规模的编排（如K=2,3,4,5个模型）找到最优模型组合。

**第三阶段：面向SLM-MUX的测试时计算扩展**
论文探索了两种在推理时增加计算资源以提升性能的策略：1) **增加参与模型的类型**：即增加编排中模型的数量（K）。2) **增加每个模型的采样数**：即让每个模型生成更多独立样本，以提高其自身输出的置信度估计。论文通过实验分析了这两种策略在不同任务上的效果和最优资源分配方案。

总之，该方法通过一个避免直接讨论的聚合架构、一个数据高效的模型选择策略，以及针对性的计算扩展分析，系统地解决了SLMs的编排难题。

### Q4: 论文做了哪些实验？

论文在三个数学和科学推理基准测试（MATH, GPQA, GSM8K）上进行了系统性的实验，以验证SLM-MUX的有效性。

1. **现有方法在SLMs上的局限性验证**：首先，在SLMs（Llama 3.1 8B, Mistral 8×7B, Gemma 2 27B）和前沿LLMs（DeepSeek V3, Gemini 2.0 Flash, GPT-4o）上对比了三种基于讨论的编排方法。结果证实，这些方法对前沿LLMs有提升（最高+2%），但对SLMs则导致性能下降（最高-5.5%），并归因于SLMs的群体思维现象。

2. **SLM-MUX基础性能评估**：使用上述三个SLMs，将SLM-MUX与单个模型最佳性能、单个模型自洽性（Single-Best-SC）以及三种现有编排方法对比。结果显示，SLM-MUX显著优于其他编排方法，在MATH、GPQA、GSM8K上分别取得了最高13.4%、8.8%、7.0%的改进。输出归因分析表明，SLM-MUX成功利用了不同SLMs的互补优势。

3. **模型选择搜索效果评估**：从一个包含5个SLMs的候选池中，使用500个验证问题，搜索最优的2模型组合。在测试集上，搜索得到的最佳组合相比组合内最佳单模型，在三个基准上分别实现了4.5%、4.4%、4.3%的准确率提升，证明了搜索策略的有效性。

4. **计算扩展策略分析**：
   - **增加模型数量**：实验发现，性能提升因任务而异。在MATH上，增加模型数持续提升性能；在GPQA上，2个模型最佳，更多模型反而下降；在GSM8K上，2个模型后即饱和。这强调了模型互补性与矛盾之间的平衡。
   - **增加每个模型的采样数**：这是一个更稳健的策略，在所有基准上，随着采样数增加（2到9），SLM-MUX的性能持续提升，且 consistently 优于基线方法 Agent Forest。

5. **与大型模型的对比**：经过模型选择和采样扩展优化后，仅由两个SLMs组成的SLM-MUX系统，在GPQA和GSM8K上超越了庞大的Qwen 2.5 72B模型，在MATH上也能与之匹敌，凸显了其高效性。

### Q5: 有什么可以进一步探索的点？

论文的工作为SLM编排开辟了新的方向，但仍有一些局限性和未来探索空间：

1. **动态与自适应编排**：当前的模型选择和聚合策略是静态的。未来可以探索根据输入问题的类型或难度，动态选择参与模型或调整聚合权重，实现更精细化的资源分配。

2. **扩展到更复杂的任务和交互模式**：本文主要关注封闭式推理任务（数学、科学QA）。未来可以将SLM-MUX架构应用于更开放、多轮、需要工具使用的复杂Agent场景，研究其与规划、记忆等模块的整合。

3. **理论分析的深化**：论文虽然提供了理论分析来佐证方法的优势，但关于群体思维的产生机制、不同模型间矛盾与互补性的量化理论，以及最优编排规模的理论边界，仍有待进一步研究。

4. **成本与延迟的优化**：虽然SLMs本身比大模型高效，但编排多个模型会增加总计算成本。未来需要研究如何在性能、成本和推理延迟之间取得更好权衡，例如通过早停、异步生成或模型缓存等策略。

5. **更广泛的模型池与领域特异性**：实验使用了通用的开源SLMs。未来可以探索将领域微调的SLMs或不同模态的专家模型纳入编排池，构建面向垂直领域的超级“模型联盟”，并研究其协同效应。

### Q6: 总结一下论文的主要内容

这篇论文的核心贡献是提出了 **SLM-MUX**，一个专门为编排多个小语言模型（SLMs）而设计的三阶段框架，旨在解决现有基于讨论的编排方法在SLMs上失效的问题。论文首先通过实验揭示了SLMs在交互中容易陷入“群体思维”导致性能下降的缺陷。针对此，SLM-MUX采用了一种“先生成后聚合”的架构，让各SLM独立生成答案并基于置信度进行聚合，从而有效利用模型的多样性。在此基础上，论文进一步提出了一个数据高效的模型选择搜索策略，以从候选池中找出最具互补性的模型组合，以及系统分析了两种测试时计算扩展策略（增加模型数量 vs. 增加每个模型的采样数）的效果。实验表明，SLM-MUX在多个推理基准上显著优于现有编排方法和强基线，并且经过优化的、仅由两个SLMs组成的系统，其性能可以匹配甚至超越参数量大一个数量级的单体大模型（如Qwen 2.5 72B）。这项工作证明了通过智能编排，一群高效的“小模型”可以协同成为一个更强大、更准确的系统，为构建低成本、高性能的AI系统提供了新的思路。
