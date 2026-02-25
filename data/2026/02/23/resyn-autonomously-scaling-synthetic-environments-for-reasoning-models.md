---
title: "ReSyn: Autonomously Scaling Synthetic Environments for Reasoning Models"
authors:
  - "Andre He"
  - "Nathaniel Weir"
  - "Kaj Bostrom"
  - "Allen Nie"
  - "Darion Cassel"
  - "Sam Bayless"
  - "Huzefa Rangwala"
date: "2026-02-23"
arxiv_id: "2602.20117"
arxiv_url: "https://arxiv.org/abs/2602.20117"
pdf_url: "https://arxiv.org/pdf/2602.20117v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent 数据合成"
  - "Agentic 强化学习"
  - "推理模型"
  - "合成环境"
  - "可验证奖励"
  - "环境生成"
  - "强化学习"
  - "语言模型训练"
relevance_score: 9.0
---

# ReSyn: Autonomously Scaling Synthetic Environments for Reasoning Models

## 原始摘要

Reinforcement learning with verifiable rewards (RLVR) has emerged as a promising approach for training reasoning language models (RLMs) by leveraging supervision from verifiers. Although verifier implementation is easier than solution annotation for many tasks, existing synthetic data generation methods remain largely solution-centric, while verifier-based methods rely on a few hand-crafted procedural environments. In this work, we scale RLVR by introducing ReSyn, a pipeline that generates diverse reasoning environments equipped with instance generators and verifiers, covering tasks such as constraint satisfaction, algorithmic puzzles, and spatial reasoning. A Qwen2.5-7B-Instruct model trained with RL on ReSyn data achieves consistent gains across reasoning benchmarks and out-of-domain math benchmarks, including a 27\% relative improvement on the challenging BBEH benchmark. Ablations show that verifier-based supervision and increased task diversity both contribute significantly, providing empirical evidence that generating reasoning environments at scale can enhance reasoning abilities in RLMs

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决强化学习在训练推理语言模型（RLMs）时面临的数据多样性不足和人工依赖问题。研究背景是，近期工作（如OpenAI-o1和DeepSeek-R1）表明，通过强化学习在数学和代码数据上训练可以显著提升大语言模型的推理能力，并引发回溯、自我验证等涌现行为。然而，现有方法主要依赖已知标准答案的任务（如数学题），限制了问题多样性；而基于验证器的方法虽能利用更易验证的任务（如数独），但通常局限于少数手工设计的程序化环境，导致推理模式单一、泛化能力受限。

现有方法的不足在于：一方面，基于解决方案注释的方法需要人工标注，成本高且可扩展性差；另一方面，现有的合成数据生成方法虽能自动产生大量数据，但环境多样性受限于人工设计，无法自动创建多样化的任务，可能使模型陷入重复模式，难以培养通用推理技能。

本文的核心问题是：如何自动、大规模地生成多样化的推理环境，以突破人工设计的瓶颈，从而更有效地提升语言模型的推理能力。为此，论文提出了ReSyn方法，通过自动生成配备实例生成器和验证器的多样化推理环境（涵盖约束满足、算法谜题、空间推理等任务），将基于验证器的监督与任务多样性扩展相结合，为强化学习提供可靠且丰富的训练基础。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大类。

在方法类研究中，相关工作主要围绕如何为推理模型提供监督信号。早期研究（如OpenAI-o1和DeepSeek-R1）主要聚焦于数学和编程领域，利用参考答案或单元测试来提供明确的奖励信号，但其问题多样性受限于已知标准答案。另一类方法是基于验证器的强化学习（RLVR），它利用任务本身易于验证的特性（如数独规则检查）来提供监督，避免了需要完整解决方案标注的负担。然而，现有的RLVR方法依赖于少数手工设计的程序化环境，导致任务多样性和推理模式有限。此外，还有研究探索基于LLM的合成数据生成，但其通常以模型生成的推理链作为监督依据，在超出教师模型能力的问题上可靠性不足。

在应用类研究中，相关工作致力于构建用于训练推理语言模型（RLMs）的环境。已有研究开始探索基于代码的、类似谜题的推理环境，并证明其能提升下游推理基准的表现，并激发出与数学训练中观察到的类似行为（如回溯、自我验证）。但这些工作的环境集合规模小，且依赖人工设计，限制了任务多样性和可扩展性。

本文提出的ReSyn与这些工作的关系和区别在于：1）**与早期数学/代码RL方法的关系与区别**：共享了利用强化学习增强推理能力的核心思路，但ReSyn通过合成多样化的、配备验证器的环境，突破了依赖已知标准答案对问题多样性的限制。2）**与现有RLVR及程序化环境工作的关系与区别**：继承了利用验证器提供监督的思想，但通过自动化生成大量多样化的代码环境，显著扩展了环境规模和任务多样性，而非依赖少量手工设计。3）**与LLM合成数据生成方法的关系与区别**：都利用LLM生成内容，但ReSyn专注于合成代码化的环境生成器和验证器，从而能对超出教师模型解决能力的问题提供可靠、可扩展的监督，而非依赖模型生成的解决方案作为真值。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为ReSyn的自动化数据生成流水线来解决大规模、多样化推理环境生成的问题。其核心方法是利用大语言模型的代码生成能力，自动创建可编程的推理环境，而非单个的问答对。

整体框架是一个五阶段的流水线。首先，从现有基准中提取关键词作为种子主题。其次，针对每个关键词，提示LLM构思并实现一个相关的推理任务，生成包含实例生成函数ρ₀、观察函数O和奖励函数R的Python代码环境。第三，采用LLM作为评判员，对生成的代码环境进行两阶段评估，确保其满足“无参考验证”和“计算优势”等关键标准，并修正不合格的环境。第四，从通过评估的环境中，按不同难度等级程序化地生成大量问题实例，每个实例通过观察函数转化为自然语言问题Q，并与对应的验证函数V配对，形成用于训练的(Q, V)对。最后，通过LLM尝试解题并进行难度校准，利用统计检验筛选出难度参数有效的环境，确保数据集的多样性和可控的难度梯度。

关键技术在于将推理任务形式化为一个交互式学习问题T = (S, A, R, O, ρ₀)，其中S是实例参数空间，A是模型的语言动作空间，O将实例参数转化为问题，R验证答案的正确性，ρ₀控制实例的难度分布。这种设计使得单个环境可以生成无限多的问题变体，并复用同一套验证逻辑，极大地提升了数据生成的效率和规模。

主要创新点包括：1）从生成具体问答对转向生成可编程的“环境”，实现了数据的规模化、程序化生成。2）强调“无参考验证”，即验证函数R不依赖于标准答案，而是基于问题实例的内在逻辑进行程序化验证，这更符合许多推理问题的本质。3）通过LLM评判和难度校准机制，自动化地保证了生成环境的质量和难度有效性。4）最终构建的数据集支持基于可验证奖励的强化学习训练，实验证明其能有效提升推理模型的泛化能力。

### Q4: 论文做了哪些实验？

论文实验主要包括使用ReSyn生成的数据集对Qwen2.5-7B-Instruct模型进行强化学习训练，并在多个推理和数学基准上评估其性能。

**实验设置**：模型基于Qwen2.5-7B-Instruct初始化，使用DAPO强化学习算法进行训练。训练时，模型针对每个问题生成多个候选答案，由对应的验证器（Verifier）提供二元奖励信号（正确为1，错误为0），并结合格式奖励（要求输出符合指定的<think>和<answer>标签结构）来更新模型参数。标准训练步数为400步。

**数据集/基准测试**：使用ReSyn管道生成训练数据，从约100个关键词出发，最终生成418个不同的推理环境，并从中产生16K训练实例和500个验证实例，每个实例包含自然语言问题（Q）和代码实现的验证器（V）。评估基准包括：BBH（零样本）、BBEH、GSM8K-test和AIME 2024。

**对比方法**：主要对比了未经训练的Qwen2.5-7B-Instruct基础模型、使用SynLogic方法训练的模型（7B参数），以及外部模型如Llama-3.1-Instruct（8B）和Mistral-Instruct（7B）。

**主要结果与关键指标**：ReSyn训练的模型在所有基准上均取得显著提升。具体指标如下：在BBH上达到75.19（mean@4），相比基础模型（65.90）和SynLogic（66.50）有大幅提高；在更具挑战性的BBEH上达到14.29（mean@4），相比基础模型（11.22）有27%的相对提升；在GSM8K-test上达到91.36（mean@4），高于基础模型的82.34；在AIME 2024上达到13.96（mean@128），高于基础模型的9.77。消融实验表明，基于验证器的监督和增加任务多样性都对性能提升有重要贡献。

### Q5: 有什么可以进一步探索的点？

基于论文内容，ReSyn方法在利用验证器生成多样化推理环境方面取得了显著成效，但仍存在一些局限性和值得深入探索的方向。首先，论文提到验证器或代码生成的奖励信号可能存在错误，虽然验证器生成比答案生成更不易出错，但如何进一步降低验证器本身的错误率，或设计自修正机制来确保奖励信号的可靠性，是一个关键问题。其次，实验表明任务多样性（N）比每个环境的实例数量（M）对性能提升更重要，但论文未深入探讨如何系统性地衡量和优化任务多样性，例如引入更细粒度的任务分类或难度梯度，以避免生成冗余或无效的环境。此外，当前方法主要覆盖约束满足、算法谜题和空间推理等任务，未来可以扩展到更复杂的领域，如数学证明、多模态推理或现实世界问题，以测试其泛化能力。另一个方向是探索更高效的训练策略，例如结合课程学习，让模型从简单任务逐步过渡到复杂任务，或引入元学习来快速适应新环境。最后，论文未讨论计算成本问题，生成大量环境和验证器可能带来高昂开销，未来可以研究如何压缩或共享环境结构以提升效率。

### Q6: 总结一下论文的主要内容

该论文提出了ReSyn框架，旨在通过自主扩展合成环境来增强推理语言模型的训练。核心问题是现有基于验证器的强化学习方法依赖有限的手工环境，限制了任务多样性和模型泛化能力。ReSyn通过自动生成多样化的推理环境（如约束满足、算法谜题和空间推理）及其对应的实例生成器和验证器，实现了环境的规模化创建。方法上，它利用这些合成环境进行强化学习训练，特别强调验证器提供的可验证奖励信号。实验表明，使用ReSyn数据训练的Qwen2.5-7B-Instruct模型在多项推理和数学基准测试中均取得显著提升，其中在BBEH基准上相对改进达27%。主要结论是验证器监督和任务多样性的增加共同提升了推理模型的性能，证明规模化生成推理环境能有效增强模型的推理能力。
