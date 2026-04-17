---
title: "RaTA-Tool: Retrieval-based Tool Selection with Multimodal Large Language Models"
authors:
  - "Gabriele Mattioli"
  - "Evelyn Turri"
  - "Sara Sarto"
  - "Lorenzo Baraldi"
  - "Marcella Cornia"
  - "Lorenzo Baraldi"
  - "Rita Cucchiara"
date: "2026-04-16"
arxiv_id: "2604.14951"
arxiv_url: "https://arxiv.org/abs/2604.14951"
pdf_url: "https://arxiv.org/pdf/2604.14951v1"
categories:
  - "cs.CV"
  - "cs.AI"
  - "cs.CL"
  - "cs.MM"
tags:
  - "工具学习"
  - "多模态大语言模型"
  - "检索增强"
  - "开放世界工具使用"
  - "偏好优化"
  - "数据集构建"
relevance_score: 7.5
---

# RaTA-Tool: Retrieval-based Tool Selection with Multimodal Large Language Models

## 原始摘要

Tool learning with foundation models aims to endow AI systems with the ability to invoke external resources -- such as APIs, computational utilities, and specialized models -- to solve complex tasks beyond the reach of standalone language generation. While recent advances in Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs) have expanded their reasoning and perception capabilities, existing tool-use methods are predominantly limited to text-only inputs and closed-world settings. Consequently, they struggle to interpret multimodal user instructions and cannot generalize to tools unseen during training. In this work, we introduce RaTA-Tool, a novel framework for open-world multimodal tool selection. Rather than learning direct mappings from user queries to fixed tool identifiers, our approach enables an MLLM to convert a multimodal query into a structured task description and subsequently retrieve the most appropriate tool by matching this representation against semantically rich, machine-readable tool descriptions. This retrieval-based formulation naturally supports extensibility to new tools without retraining. To further improve alignment between task descriptions and tool selection, we incorporate a preference-based optimization stage using Direct Preference Optimization (DPO). To support research in this setting, we also introduce the first dataset for open-world multimodal tool use, featuring standardized tool descriptions derived from Hugging Face model cards. Extensive experiments demonstrate that our approach significantly improves tool-selection performance, particularly in open-world, multimodal scenarios.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有工具学习框架在开放世界和跨模态场景下的局限性。研究背景是，随着基础模型的发展，AI系统开始具备调用外部工具（如API、计算工具、专用模型）的能力，以解决超越纯文本生成范围的复杂任务。尽管大型语言模型（LLM）和多模态大语言模型（MLLM）在推理和感知方面取得了进展，但现有方法存在两个主要不足：一是它们大多局限于文本输入，难以处理需要视觉或音频信息的多模态用户指令；二是它们通常采用封闭世界设定，将工具选择视为在训练期间见过的固定工具集上的监督分类问题，导致无法泛化到未见过的工具或新任务。

本文要解决的核心问题是：如何设计一个能够处理多模态输入、并能在开放世界中动态适应新工具的工具选择框架。为此，论文提出了RaTA-Tool，一个基于检索的新型框架。该框架的核心思想是避免学习从用户查询到固定工具标识的直接映射，而是让MLLM将多模态查询转换为结构化的任务描述，然后通过语义匹配从机器可读的工具描述库中检索最合适的工具。这种基于检索的表述自然支持扩展到新工具而无需重新训练。此外，论文还引入了基于直接偏好优化（DPO）的偏好对齐阶段，以提升任务描述与工具选择之间的匹配度。为了支持该方向的研究，作者还构建了首个开放世界多模态工具使用的数据集，为系统性评估提供了基础。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：多模态大语言模型（MLLMs）、基于语言模型的工具使用，以及多模态工具智能体。

在多模态大语言模型方面，代表性工作如LLaVA、BLIP和Flamingo，它们通过跨模态投影和指令微调，将预训练语言模型与特定模态编码器对齐，增强了模型的感知与推理能力。后续研究进一步扩展至音频、视频等模态，并探索统一架构或模态无关的表示。然而，这些模型主要聚焦于提升模型内部的感知能力，并未明确解决如何利用多模态输入来选择和调用外部工具的问题，也未考虑训练时未见工具的开放世界场景。

在基于语言模型的工具使用方面，Toolformer开创性地通过自监督标注教LLM决定何时及如何调用API。后续工作如Gorilla专注于机器学习工作流中的API选择，ToolLLM强调使用预定义工具库进行多步骤任务执行，而HuggingGPT等系统则将用户请求分解并路由至专用模型。这些方法虽然有效，但主要局限于文本输入，无法直接利用现实指令中常见的多模态线索。

在多模态工具智能体方面，MLLM-Tool等工作首次尝试让MLLM基于多模态查询选择工具。然而，现有方法大多依赖于从查询到预定义工具标识符的直接映射，属于封闭集合学习，难以泛化至未见过的工具。本文提出的RaTA-Tool与这些工作的核心区别在于：它采用基于检索的开放世界框架，将多模态查询转化为结构化任务描述，并通过语义匹配从丰富的机器可读工具描述中检索最合适的工具，从而支持无需重新训练即可扩展到新工具的能力。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为RaTA-Tool的创新框架来解决开放世界多模态工具选择问题。其核心思路是摒弃传统的、将用户查询直接映射到固定工具标识符的封闭式学习范式，转而采用一种基于检索的两阶段方法，使多模态大语言模型能够先将多模态查询转化为结构化的任务描述，再通过语义匹配从外部工具库中检索最合适的工具。

整体框架主要由两个核心组件构成：一个经过微调的多模态大语言模型和一个检索模块。主要工作流程如下：首先，**多模态集成与自回归生成模块**接收包含文本、图像或音频的多模态用户查询。通过监督微调，MLLM被训练为根据特定提示，将输入查询生成一个标准化的、结构化的JSON格式任务描述。该描述包含三个关键字段：工具所需的**输入**格式与模态、预期的**输出**类型与结构，以及工具功能的**过程**摘要。这一步骤将模糊的用户意图转化为机器可读的、语义丰富的表示。

随后，**工具集合检索模块**开始工作。外部工具库中的每个工具都拥有一个同样以标准化JSON格式描述的功能说明。检索时，使用预训练的嵌入模型分别对MLLM生成的任务描述和所有候选工具描述进行向量化。通过计算两者嵌入向量之间的内积来衡量语义相似度，最终选择相似度最高的工具作为输出。这种检索式设计是框架的关键创新，它使得系统能够无缝扩展到训练时未见的新工具，只需将新工具的描述加入检索库即可，无需重新训练模型。

为了进一步提升任务描述与工具选择之间的对齐质量，论文引入了**基于偏好的优化阶段**。具体而言，在监督微调之后，利用直接偏好优化方法对模型进行进一步对齐。首先，使用SFT模型为每个查询生成多个候选描述，然后根据每个描述在检索中为真实工具带来的排名（相似度排名）来构建偏好数据：使真实工具排名最佳的描述作为优选响应，随机选择一个其他描述作为非优选响应。通过DPO目标函数训练模型，使其更倾向于生成那些能通过检索更准确找到正确工具的描述，从而在语义层面优化了任务描述的生成质量。

此外，论文在方法准备阶段进行了重要的**数据集构建与工具表示标准化**工作。基于现有基准，通过程序化抓取Hugging Face模型卡片，并利用大语言模型将其转化为统一的三字段JSON结构，创建了首个支持开放世界多模态工具使用的数据集，为整个框架的训练与评估奠定了基础。

综上所述，RaTA-Tool通过“生成结构化任务描述”加“语义检索匹配”的范式，结合监督微调与直接偏好优化两阶段训练，有效解决了传统方法在多模态理解与开放世界泛化方面的局限性。

### Q4: 论文做了哪些实验？

论文的实验设置主要包括在提出的开放世界多模态工具选择数据集上进行训练和评估。数据集基于ToolMMBench构建，并进行了预处理和标准化。工具描述源自Hugging Face模型卡片，使用Qwen3-8B生成JSON格式的标注。数据集按工具级别划分：90%的工具（826个）用于训练，10%的工具（94个）用于测试，确保测试工具在训练中未见。查询根据关联工具分配到相应划分，并保持了输入模态（纯文本、文本-图像、文本-音频）的分布。整体包含14,924个唯一查询。对于DPO训练，构建了包含2,981个训练项和409个评估项的偏好数据集。

实验采用Qwen2.5-Omni-3B和7B作为底层MLLM进行结构化任务描述生成，使用LoRA进行微调。监督微调（SFT）进行4个周期，DPO训练进行8个周期。检索阶段使用Qwen3-Embedding-8B编码任务描述和工具描述。对比方法包括不同检索模型（Contriever与Qwen3-Embedding）、不同训练策略（零样本、少样本、SFT、DPO）以及不同工具描述格式（自然语言NL与结构化JSON）。

主要结果以准确率衡量。关键数据指标显示：在零样本设置下，使用Contriever时，3B和7B模型的加权平均准确率（Avg_m）分别低于21和17.6；换用Qwen3-Embedding后，Avg_m提升至约41.7。SFT后性能显著提升，例如3B模型使用Qwen3-Embedding时，Avg_m从58.2（Contriever）提升至69.7。进一步应用DPO后，最佳结果来自7B模型（Ours-7B），达到Avg_q=69.1和Avg_m=70.8，各模态准确率为文本71.6、图像57.1、音频83.7。消融实验表明，结构化JSON描述结合SFT始终优于自然语言格式，且少样本提示优于零样本。这些结果证实了强嵌入模型和基于偏好的对齐对提升工具选择性能的关键作用。

### Q5: 有什么可以进一步探索的点？

该论文的RaTA-Tool框架在开放世界多模态工具选择上取得了进展，但仍存在一些局限性和值得深入探索的方向。首先，其检索机制依赖于工具描述的语义相似度匹配，这可能无法充分捕捉复杂任务与工具功能之间更精细、隐式的关联，例如需要多步骤推理或动态组合的工具链场景。未来可探索引入图神经网络或知识图谱来建模工具间的依赖和组合关系，提升复杂任务下的工具规划能力。

其次，论文虽引入DPO进行偏好优化，但偏好数据可能局限于特定领域或模态组合。未来可研究更高效的无监督或自监督对齐方法，例如通过工具执行反馈自动生成偏好对，或利用多智能体协作模拟用户偏好，以增强系统的泛化能力和人机协作的自然性。

此外，当前工具描述标准化程度虽高，但现实世界中工具文档往往异构且不完整。可进一步探索如何从非结构化数据（如代码库、演示视频）自动提取或增强工具描述，并研究跨模态工具描述生成（如将视觉演示转化为文本规范），以应对更开放的环境。

最后，该工作主要关注工具选择，而未深入评估工具调用后的执行质量与错误恢复机制。未来可构建端到端的评估框架，集成工具选择、参数生成、执行监控与迭代修正，推动从静态选择到动态交互的完整工具学习系统发展。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为RaTA-Tool的新型框架，旨在解决开放世界多模态场景下的工具选择问题。核心问题是现有工具学习方法主要局限于纯文本输入和封闭世界设定，难以理解多模态用户指令，也无法泛化到训练时未见过的工具。

方法上，RaTA-Tool采用了一种基于检索的范式。其核心思路是让多模态大语言模型（MLLM）将用户的多模态查询（如图文指令）转换为结构化的任务描述，然后将此描述与一组语义丰富、机器可读的工具描述（基于Hugging Face模型卡片构建）进行匹配，从而检索出最合适的工具。这种设计无需学习从查询到固定工具ID的直接映射，因此无需重新训练即可扩展到新工具。为进一步提升任务描述与工具选择的对齐，论文还引入了一个基于直接偏好优化（DPO）的偏好优化阶段。

论文的主要贡献和意义在于：1）首次提出了一个针对开放世界多模态工具选择的检索式框架，有效提升了工具选择的性能，尤其是在开放世界和多模态场景下；2）引入了首个支持该研究方向的数据集；3）实验证明该方法显著优于现有基线。主要结论是，通过将工具选择转化为语义匹配问题，RaTA-Tool实现了对未知工具的可扩展支持和对多模态指令的更好理解。
