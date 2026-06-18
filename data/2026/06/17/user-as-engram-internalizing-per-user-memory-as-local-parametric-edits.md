---
title: "User as Engram: Internalizing Per-User Memory as Local Parametric Edits"
authors:
  - "Bojie Li"
date: "2026-06-17"
arxiv_id: "2606.19172"
arxiv_url: "https://arxiv.org/abs/2606.19172"
pdf_url: "https://arxiv.org/pdf/2606.19172v1"
categories:
  - "cs.AI"
tags:
  - "Agent Memory"
  - "Personalization"
  - "Parametric Editing"
  - "Engram Model"
  - "Local Edits"
  - "Multi-User Composition"
relevance_score: 9.5
---

# User as Engram: Internalizing Per-User Memory as Local Parametric Edits

## 原始摘要

Personal memory in a language model is two problems: content and reasoning skill. The brain keeps the two apart (a sparse, local engram in the hippocampus for each episode, a slow neocortex for the shared skills that interpret it), so a new fact need not overwrite everything else. Most personalization today keeps a user's facts outside the weights, in a natural-language memory file or a retrieval index. When facts are written into the model instead, the standard recipe is the per-user LoRA adapter, which does the opposite of the brain, folding content and skill into one global weight delta. Writing a user's facts as a LoRA contaminates text unrelated to them; writing the same facts as local Engram rows leaves it mathematically untouched, resulting in a roughly 33,000x smaller memory footprint.
  We therefore propose User as Engram: store a user's content as surgical edits to the hash-keyed memory table of an Engram model, and carry the reasoning skill in one shared adapter. This layered design matches per-user LoRA's direct recall while delivering 5.6x higher indirect-reasoning accuracy on average, and never makes a single user worse at reasoning than the untouched base. The edit is a glass box: writing a fact switches on its lookup at exactly the trigger, adds the value the answer needs, leaves every other position unchanged to the last bit, and fails if written into the wrong layer. Because different users' facts land in disjoint hash slots, their edits compose: many users live in one shared table at once, stacking additively and losslessly, where a per-user LoRA, a single global weight delta, admits only one. Upon retrieval, a per-user Engram table does not grow with the population the retriever must search, so past ~100 facts it overtakes a retrieval pipeline on a 2.5x larger model.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）如何高效、安全地为每个用户存储和运用个性化记忆的核心问题。现有方法存在明显不足：主流方案如上下文学习（ICL）和检索增强生成（RAG）将事实存储在模型权重之外，虽避免了参数污染，但会随着用户和事实数量增长而面临检索效率瓶颈。另一种方案是将用户事实直接写入权重，标准做法是为每个用户训练一个单独的LoRA适配器。然而，LoRA的更新是全局性的，它将用户特定的内容（如“玛雅的心脏病医生是瓦兹奎兹医生”）与通用的推理技能（如“如何回答关于心脏检查的问题”）混杂在一个统一的权重增量中。这导致两个严重问题：一是“污染”，LoRA的调整会影响与用户事实无关的文本推理；二是“不堆叠”，不同用户的LoRA无法无损地共存，需要模型副本，造成巨大的存储开销。

本文提出的“User as Engram”方法旨在解决这些矛盾。其核心思想是将个人记忆分解为两部分：**用户内容**与**推理技能**。借鉴大脑的记忆编码机制（海马体负责稀疏、局部的记忆痕迹，新皮层负责共享技能），该方法将用户事实以“外科手术式”的精准编辑嵌入到一个Engram模型的哈希键控记忆表中，确保编辑只影响触发特定事实的文本位置，对其他部分毫无影响。而通用的推理技能则由一个所有用户共享的单一LoRA适配器承担。这种分层设计实现了内容的局部性、可组合性（不同用户事实可无损叠加在同一张表中）以及极低的推理损伤，从而在避免污染的同时，实现了远超传统LoRA的间接推理准确率（平均提高5.6倍），并在事实数量超过约100条时，在性能上击败了基于检索的、模型规模大2.5倍的基线方案。

### Q2: 有哪些相关研究？

相关研究主要分为以下几类：

**方法类**：Engram架构和LoRA-as-memory家族。Engram是DeepSeek系列的稀疏模型，通过哈希键表实现条件记忆，其地址从输入token ID中确定性计算，支持将表格卸载到主机DRAM。LoRA-as-memory家族包括per-user LoRA、prefix-tuning、自适应秩和量化变体，通过低秩增量在冻结基模型上训练，常基于NTP、知识蒸馏或超网络发射。本文的核心区别在于：Engram实现局部参数编辑，不污染其他位置；而LoRA是全局权重增量，会干扰无关文本。

**应用类**：In-context learning、检索增强和外部记忆系统（如DyPRAG、DistilledPRAG），这些方法保持模型未修改但每次查询需支付上下文token。Per-user LoRA和知识编辑（如T2L）无需上下文但全局修改权重。User as Engram处于新的角落：零上下文成本下的局部编辑，通过将用户内容存储为Engram模型的哈希键记忆表的手术式编辑，推理技能由共享适配器承载。

**评测类**：本文对比了per-user LoRA和检索管道。实验表明，User as Engram在直接回忆上与per-user LoRA匹配，间接推理准确率平均高5.6倍，且单个用户推理能力不劣于未修改基模型。在约100个事实后，其性能超越基于2.5倍规模模型的检索管道，且记忆表不随用户规模增长。

### Q3: 论文如何解决这个问题？

论文提出“User as Engram”方法，将用户个性化记忆拆分为内容与推理技能两部分，分别存储在模型的不同组件中。整体框架基于Engram预训练模型，其主体是标准Transformer，仅在少数指定层（如Mini-Engram中的两层）嵌入了内容可寻址的查找模块。核心创新在于：用户的事实内容被“外科手术式”地写入哈希键控的记忆表中，而推理能力则保留在共享的适配器中。

具体实现分为三步：首先，将事实的触发词（trigger）的N-gram后缀通过确定性哈希映射到记忆表中的稀疏行地址集（约16行），确定“写入位置”。然后，将事实的答案编码为行向量值，提供三种策略：UNEMBED_P通过闭式解一步计算（<1ms），OPT使用梯度微调（~1s），Joint OPT（默认用于超过30个事实）联合优化所有行的值以减少干扰。写入仅修改触发词哈希对应的行，模型其余部分（包括骨干网络和其他位置）保持比特级不变，实现了约33,000倍的内存占用缩减。

关键技术包括：门控机制使得查找稀疏且有条件，只在触发词位置激活；设计的“玻璃盒”特性可精确观察写入过程——门控值从0.02升至0.99，残差变化与目标值路径的余弦相似度达0.999，非触发位置变化严格为零。部署时，每个用户拥有一个覆盖映射表，推理时仅临时覆盖相关行，请求结束后恢复，实现零跨用户泄漏且支持无损叠加。

### Q4: 论文做了哪些实验？

论文进行了系统实验，验证User-as-Engram方法在个人化事实记忆上的性能。

**实验设置**：将事实作为手术式编辑写入Engram模型的哈希键记忆表中，共享推理技能适配器。使用Mini-Engram模型（d8 v2~d20@1536，178M~1.22B参数），在单块Blackwell GPU上训练。

**数据集/基准测试**：三个事实语料库——200事实基准（100 USER+100 ORG事实）、XL语料（1000 USER+1000 ORG模板事实）、XXL语料（3132个不同触发模板）。对比方法包括：每个用户的LoRA（rank-64）、检索增强（MEM0、MEMMACHINE，共享同一回答LM）。

**主要结果**：1）直接事实召回：在精确触发词查询上，检索接近完美但需16-63上下文token，Engram仅68% top-1但零token成本；在改述查询上，多触发词Engram插入达96.9% top-1，而检索下降至75%。2）存储效率：100事实/用户时Engram仅88KB，LoRA需14.2MB（161倍更大）；百万用户时100GB对14.2TB。3）LOCOMO基准：Engram Joint OPT在所有模型规模上单跳token-F1均优于检索基线（如d20@1536上领先约0.05-0.10），且密度高达300事实/用户时top-5召回仍超90%。4）推理能力：Engram不损害间接推理，而LoRA会污染无关文本。

### Q5: 有什么可以进一步探索的点？

论文存在几个值得深入探索的局限。首先，Engram表基于哈希键的固定存储方式可能无法有效处理语义相近但表示不同的用户事实（如同义句），未来可引入动态哈希或语义哈希机制。其次，当前方法仅支持显式事实的插入，缺乏对隐式用户偏好（如写作风格、常见推理路径）的学习，可考虑将Engram与可微分参数化记忆结合，实现隐式知识的内化。此外，共享适配器作为推理技能的唯一载体可能存在容量瓶颈，未来可探索多层级适配器或混合专家架构来扩展技能表征能力。最后，编辑操作对层级敏感（“失败如果被写入错误的层”），表明当前设计依赖特定层级的先验知识，可开发自适应的层选择机制，通过梯度分析和注意力权重分布自动决定事实应插入的层。这些改进将使Engram更接近生物学记忆中“稀疏编码+皮层整合”的协同机制。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为“User as Engram”的方法，用于在语言模型中实现个性化记忆。当前的问题在于，模型需要同时处理用户具体事实（内容）和基于事实的推理（技能），而现有方法如用户级LoRA将内容与技能混在全局权重更新中，导致干扰和存储开销大。作者受大脑海马体和新皮层分工启发，将存储分为两层：用户事实作为“内容”存储在Engram模型的哈希键控记忆表中，进行局部、可叠加的编辑；推理技能则通过一个共享的LoRA适配器实现。主要结论是，该方法在直接回忆上与用户LoRA相当，但在间接推理准确性上平均提升5.6倍，且不会降低用户的推理能力。记忆足迹缩小约33000倍，并且在事实数量超过约100个时，其性能超过了使用2.5倍更大模型的检索管道。该工作的核心贡献在于实现了存储与推理的分离，解决了多用户环境下记忆污染和扩展性问题。
