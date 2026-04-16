---
title: "MM-Doc-R1: Training Agents for Long Document Visual Question Answering through Multi-turn Reinforcement Learning"
authors:
  - "Jiahang Lin"
  - "Kai Hu"
  - "Binghai Wang"
  - "Yuhao Zhou"
  - "Zhiheng Xi"
  - "Honglin Guo"
  - "Shichun Liu"
  - "Junzhe Wang"
  - "Shihan Dou"
  - "Enyu Zhou"
  - "Hang Yan"
  - "Zhenhua Han"
  - "Tao Gui"
  - "Qi Zhang"
  - "Xuanjing Huang"
date: "2026-04-15"
arxiv_id: "2604.13579"
arxiv_url: "https://arxiv.org/abs/2604.13579"
pdf_url: "https://arxiv.org/pdf/2604.13579v1"
categories:
  - "cs.CL"
tags:
  - "Agent Training"
  - "Multi-turn Reinforcement Learning"
  - "Visual Question Answering"
  - "Long Document Understanding"
  - "Retrieval-Augmented Generation"
  - "Policy Optimization"
  - "Vision-Language Agent"
relevance_score: 8.0
---

# MM-Doc-R1: Training Agents for Long Document Visual Question Answering through Multi-turn Reinforcement Learning

## 原始摘要

Conventional Retrieval-Augmented Generation (RAG) systems often struggle with complex multi-hop queries over long documents due to their single-pass retrieval. We introduce MM-Doc-R1, a novel framework that employs an agentic, vision-aware workflow to address long document visual question answering through iterative information discovery and synthesis. To incentivize the information seeking capabilities of our agents, we propose Similarity-based Policy Optimization (SPO), addressing baseline estimation bias in existing multi-turn reinforcement learning (RL) algorithms like GRPO. Our core insight is that in multi-turn RL, the more semantically similar two trajectories are, the more accurate their shared baseline estimation becomes. Leveraging this, SPO calculates a more precise baseline by similarity-weighted averaging of rewards across multiple trajectories, unlike GRPO which inappropriately applies the initial state's baseline to all intermediate states. This provides a more stable and accurate learning signal for our agents, leading to superior training performance that surpasses GRPO. Our experiments on the MMLongbench-Doc benchmark show that MM-Doc-R1 outperforms previous baselines by 10.4%. Furthermore, SPO demonstrates superior performance over GRPO, boosting results by 5.0% with Qwen3-8B and 6.1% with Qwen3-4B. These results highlight the effectiveness of our integrated framework and novel training algorithm in advancing the state-of-the-art for complex, long-document visual question answering.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决长文档视觉问答（Long Document Visual Question Answering）中的复杂多跳查询问题。研究背景是，随着文档长度和视觉内容的增加，传统方法难以有效定位和整合分散在多页文档中的关键信息。现有方法主要基于检索增强生成（RAG）系统，这些系统通常依赖单次检索，即仅根据初始查询一次性检索相关内容。然而，对于需要跨多个文档片段进行迭代信息收集的多跳问题，这种单次检索模式存在明显不足，因为它无法动态调整检索策略，容易遗漏关键信息，尤其是在涉及视觉元素（如图表、图像）时，处理能力更为有限。

本文的核心问题是：如何设计一个能够进行迭代信息发现与合成的智能体框架，以提升对长文档中复杂多跳视觉问题的回答能力。为此，论文提出了MM-Doc-R1框架，它通过多智能体协作（包括规划器、信息搜寻器和答案生成器）实现多轮工具调用（如搜索和视觉阅读），模拟人类逐步探索文档的过程。同时，为了更有效地训练这些智能体，论文指出了现有多轮强化学习算法（如GRPO）的不足：GRPO仅基于初始状态估计基线值，并将其错误地应用于所有中间状态，导致基线估计偏差，影响训练稳定性和性能。因此，本文进一步引入了相似性策略优化（SPO）算法，其核心思想是利用轨迹间的语义相似性来加权计算更精确的基线值，从而减少估计偏差，为智能体提供更稳定、准确的学习信号，最终提升其在复杂长文档视觉问答任务中的信息寻求能力和整体性能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：长文档视觉问答方法、检索增强生成框架以及用于语言模型训练的强化学习算法。

在**长文档视觉问答方法**方面，早期研究集中于从单一短文档中提取答案。随着大语言模型发展，出现了如MMLongbench-Doc等针对长文档的基准。现有方法主要分为两类：一是基于OCR和文本检索的方法，通过检索相关文档片段来回答问题；二是基于视觉编码器获取嵌入进行检索的方法，例如ColPALI。此外，多智能体系统如M3docrag和MDocagent被提出，通过协同视觉语言模型和大语言模型，结合文本与图像嵌入的RAG来处理DocVQA任务。然而，这些方法主要针对单跳问题，而本文则专注于解决需要多轮交互和生成子查询的多跳问题。

在**检索增强生成框架**方面，传统RAG系统使用BM25或BGE-M3等检索器，但在处理复杂多跳查询时存在局限。近期多模态扩展模型如ColQwen2.5引入了视觉特征以增强检索，但仍缺乏迭代优化能力。另一些方法如Search-R1和Deepreasearcher采用多步检索处理长文本问答，但仅关注文本模态并依赖通用网络搜索工具。本文的创新在于整合了专门的“视觉阅读”工具，结合视觉与文本模态，能够处理更广泛的视觉丰富问答问题。

在**强化学习训练算法**方面，早期广泛采用近端策略优化，其使用评论家模型估计基线。近期，随着DeepSeek-R1等模型发展，组相对策略优化因使用组平均奖励估计基线而无需单独评论家模型，节省了计算资源。其他方法如REINFORCE++使用批次平均奖励估计基线，VRPO则重新探索了在噪声监督下的价值建模。本文提出的相似性策略优化针对GRPO在多轮强化学习中基线估计偏差的问题，通过基于轨迹语义相似性的加权平均奖励来计算更精确的基线，从而提供更稳定准确的学习信号。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MM-Doc-R1的集成框架来解决长文档视觉问答中的复杂多跳查询问题，该框架结合了创新的智能体工作流程和一种新的强化学习训练算法。

**整体框架与核心方法**：MM-Doc-R1框架的核心是一个自主的、结构化的智能体工作流程，旨在迭代地处理多页文档。该工作流程包含五个阶段：1) 文档解析与预处理，使用OCR工具提取文本、表格和图像并转换为Markdown格式，同时生成文档目录(TOC)和按页分块；2) 规划，由规划智能体根据TOC和图表标题制定全局策略，将初始查询分解为细粒度子查询并规划所需工具；3) 迭代检索与推理，这是核心循环，由寻求智能体动态执行，它选择并调用两种专用工具（“阅读”和“搜索”）来获取信息；4) 答案生成，由答案智能体综合所有检索到的上下文，生成最终答案；5) 整个流程是顺序且可迭代的，赋予了模型动态规划和自我纠正能力。

**主要模块/组件**：
1.  **三个关键智能体**：规划智能体（负责策略分解）、寻求智能体（负责执行迭代检索）、答案智能体（负责综合生成）。
2.  **两种多模态工具**：“阅读”工具，接收页面ID和子查询，利用视觉语言模型(VLM)从指定页面提取和解读文本、图表及图像信息；“搜索”工具，使用BM25算法基于子查询进行快速关键词检索，返回最相关的文本片段。
3.  **训练算法——基于相似性的策略优化(SPO)**：这是论文的关键技术创新，用于从零开始训练上述智能体，优化其工具调用、子查询分解和工作流导航的策略。

**SPO算法的创新点**：论文指出，在多轮强化学习中，随着交互进行，即使从相同初始状态出发的轨迹也会迅速分化，导致其中间状态差异巨大。现有的GRPO算法使用所有轨迹在初始状态的奖励平均值作为共享基线，这会在优势估计中引入偏差。SPO的核心洞察是：语义越相似的轨迹，其共享的基线估计就越准确。因此，SPO不再使用统一的基线，而是为每个轨迹计算一个**基于语义相似性加权的奖励平均值**作为其基线。具体而言，它使用冻结的BGE-M3模型获取每个轨迹的嵌入表示，通过计算轨迹间的余弦相似度得到权重，进而计算加权平均奖励。优势函数则定义为当前轨迹奖励与其相似性加权基线之差。这种方法为智能体决策提供了更精确、更稳定的学习信号，有效减少了因轨迹发散导致的估计方差和偏差，从而在多轮、长视野的交互设置中实现了更优的训练性能。实验表明，SPO显著超越了GRPO，带来了明显的性能提升。

### Q4: 论文做了哪些实验？

论文在MMLongbench-Doc基准数据集上进行了全面的实验评估，该数据集包含1082个复杂的长文档视觉问答问题，涵盖文本、布局、图表、表格和图像等多种证据模态，以及单证据、多证据和不可回答问题类型。实验设置包括使用Qwen3-4B和Qwen3-8B作为基础模型，并对比了多种方法：传统的基于文本的RAG方法（BM25、BGE-M3）、多模态RAG（ColQwen2.5-7B）以及基于智能体的系统（Mdoc Agent、M3doc RAG）。主要评估指标为整体准确率（ACC）和F1分数，并按证据模态和数量进行了细分。

主要结果显示，未经训练的MM-Doc-R1（Qwen3-8B）整体准确率达到45.7%，已超越之前最佳基线10.4%。在单证据问题上领先5.7%，在多证据问题上领先10.0%。关键数据指标包括：在Qwen3-8B上，使用提出的SPO强化学习算法后，整体准确率提升至49.7%（比GRPO高5.0%），F1达到46.1%；在Qwen3-4B上，SPO将准确率从GRPO的39.9%提升至46.0%（提升6.1%）。此外，消融实验表明，移除目录、页面OCR阅读或VLM阅读模块均会导致性能下降，验证了各组件的重要性。在召回率方面，MM-Doc-R1(SPO)仅平均阅读3.35页就达到了66.3%的召回率，优于BM25（42.0%）、BGE-M3（51.3%）和Colqwen（65.4%）。这些结果证明了MM-Doc-R1框架及其SPO训练算法在复杂长文档视觉问答任务中的有效性。

### Q5: 有什么可以进一步探索的点？

该论文的局限性为未来研究提供了明确方向。首先，框架性能高度依赖文档预处理质量，未来可探索更鲁棒的文档解析方法，例如开发对低质量扫描或非标准格式具有更强容错能力的多模态理解模块，或引入自监督预训练来提升对噪声数据的适应性。其次，当前工作针对静态文档，未来需研究如何将智能体工作流扩展到动态或交互式文档环境，这可能涉及设计能感知并响应布局变化的在线学习机制，或构建包含动态内容的仿真环境进行训练。此外，SPO算法目前仅在英文基准上验证，其跨语言泛化能力有待检验，未来可研究多语言场景下的策略优化，或探索语言无关的语义相似性度量以提升算法普适性。从更广阔的视角看，可进一步探索将类似的多轮强化学习范式应用于更复杂的多模态推理任务，如涉及时序信息的视频文档问答，或研究如何降低智能体训练对大量标注数据的依赖，例如通过课程学习或元学习来提升样本效率。

### Q6: 总结一下论文的主要内容

这篇论文针对长文档视觉问答中传统检索增强生成系统单次检索难以处理复杂多跳查询的问题，提出了MM-Doc-R1框架。其核心贡献是设计了一个具备视觉感知能力的智能体工作流，通过多轮迭代进行信息发现与合成，以应对长文档的复杂性。方法上的关键创新是提出了基于相似性的策略优化算法，该算法通过计算多条轨迹的语义相似度，对奖励进行加权平均以获得更精确的基线估计，从而解决了如GRPO等多轮强化学习算法中存在的基线估计偏差问题，为智能体训练提供了更稳定、准确的学习信号。实验结果表明，该框架在MMLongbench-Doc基准上超越了先前基线方法10.4%，且SPO算法在不同规模的模型上都显著优于标准的GRPO。这验证了将视觉感知推理与基于轨迹的强化学习相结合，能有效推动复杂多模态信息发现任务的技术发展。
