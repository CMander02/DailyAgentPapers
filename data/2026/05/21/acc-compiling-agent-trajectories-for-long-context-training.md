---
title: "ACC: Compiling Agent Trajectories for Long-Context Training"
authors:
  - "Qisheng Su"
  - "Zhen Fang"
  - "Shiting Huang"
  - "Yu Zeng"
  - "Yiming Zhao"
  - "Kou Shi"
  - "Ziao Zhang"
  - "Lin Chen"
  - "Zehui Chen"
  - "Lijun Wu"
  - "Feng Zhao"
date: "2026-05-21"
arxiv_id: "2605.21850"
arxiv_url: "https://arxiv.org/abs/2605.21850"
pdf_url: "https://arxiv.org/pdf/2605.21850v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent轨迹数据合成"
  - "长上下文训练"
  - "监督微调"
  - "Agent上下文编译"
  - "多步工具使用"
  - "远程依赖建模"
  - "MRCR"
  - "GraphWalks"
  - "Qwen"
relevance_score: 9.5
---

# ACC: Compiling Agent Trajectories for Long-Context Training

## 原始摘要

Recent development of agents has renewed demand for long-context reasoning capacity of LLMs. However, training LLMs for this capacity requires costly long-document curation or heuristic context synthesis. We observe that agents produce massive trajectories when solving problems, invoking tools and receiving environment observations across many turns. The evidence needed to answer the original question is thus scattered throughout these turns, requiring integration of distant context segments. Nevertheless, standard agent SFT masks tool responses and only trains turn-level tool selection, creating a supervision blind spot where these scattered signals go unused. We propose Agent Context Compilation (ACC), which converts trajectories from search, software engineering, and database querying agents into long-context QA pairs that combine the original question with tool responses and environment observations gathered across multiple turns, training the model to answer directly without tool use. This makes the dependencies between the question and the evidence explicit, enabling direct supervision of long-context reasoning over distant segments without additional annotation. ACC is a simple but effective approach that can be combined with any existing long-context extension or training method, providing scalable supervised fine-tuning data. We validate ACC on long-range dependency modeling tasks through MRCR and GraphWalks, challenging benchmarks requiring cross-turn coreference resolution and graph traversal over extended contexts. Training Qwen3-30B-A3B with ACC achieves 68.3 on MRCR (+18.1) and 77.5 on GraphWalks (+7.6), results comparable to Qwen3-235B-A22B, while preserving general capabilities on GPQA, MMLU-Pro, AIME, and IFEval. Further mechanism analysis reveals that the ACC-trained model exhibits task-adaptive attention restructuring and expert specialization.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）在长上下文推理能力训练中的数据瓶颈问题。研究背景是，随着智能体（Agent）应用的兴起，模型需要处理多轮工具调用产生的大量轨迹数据，其推理能力依赖于从分散在各轮次中的片段整合信息。然而，现有方法存在明显不足：一方面，传统的长文档标注成本高昂且需要精确的证据定位，人工构建的成本极高；另一方面，启发式上下文合成方法（如随机拼接文本）生成的数据缺乏真实问题解决场景中产生的复杂依赖关系，难以有效训练模型进行长跨度推理。此外，标准的智能体监督微调（SFT）只关注单轮工具选择，屏蔽了工具响应和环境反馈，导致散落在轨迹中的跨轮次证据信号被浪费，形成了监督盲区。为了解决这个问题，本文提出了一种名为“智能体上下文编译”（Agent Context Compilation, ACC）的方法。该方法将智能体执行搜索、软件工程、数据库查询等任务时产生的多轮轨迹，直接编译成包含原始问题、多轮工具响应和环境反馈的长上下文问答对，从而显式建立起问题与散落证据间的依赖关系。这使得模型可以直接在无需额外人工标注的情况下，对长距离片段间的推理进行监督训练，为长上下文能力提供了一种经济、可扩展且有效的监督微调数据源。

### Q2: 有哪些相关研究？

本文的相关研究可以从评测、训练方法和推理框架三类来组织：

**评测类相关工作**：早期长上下文评测如NIAH、RULER和LongBench主要测试局部检索或单轮推理，性能已趋于饱和。Musique和NarrativeQA进一步探索多跳推理和长文档理解。近期OpenAI提出的MRCR（多轮共指消解）和GraphWalks（图遍历）要求跨轮次依赖建模，成为当前主流模型的标准测试。本文在这些更难的基准上验证了方法的有效性，超越了仅测试表面检索的早期评测。

**训练方法类相关工作**：包括四类：  
1. 预训练方法：修改位置编码或注意力机制，如MrRoPe、ROPE++、Native Sparse Attention等，本文不改变架构。  
2. 高质量长文档构建：如Longwanjuan、LiteLong、Quest等，通过过滤或拼接合成长文本，而非像本文直接利用agent轨迹构建QA对。  
3. 后训练方法：longRLVR、LongPO、LoongRL等结合合成数据与强化学习，需要复杂的数据标注或RL管道；本文仅通过监督微调即可实现可扩展的长上下文训练。  
4. 推理时框架：如QwenLong-L1.5、MemAgent在推理时管理长上下文记忆，本文则预训练模型直接推理。

**本文的创新与区别**：不同于上述方法，本文首次利用agent轨迹作为长上下文推理的直接数据源，将多轮工具调用与环境观察编译为显示依赖的QA对，无需额外标注或架构修改，可与任何长上下文扩展方法兼容，在保留通用能力的同时显著提升长程依赖建模。

### Q3: 论文如何解决这个问题？

论文通过提出Agent Context Compilation (ACC)方法解决标准智能体SFT中存在的监督盲区问题。标准SFT仅监督每一步的工具选择和局部推理，忽略了多轮交互中散布在工具响应和环境观察里的证据，导致模型无法学习跨远距离位置的依赖推理。

ACC的核心方法是：将智能体轨迹（包括搜索、软件工程、数据库查询等场景）转化为长上下文问答对，使得问题和所有跨轮次收集的证据（工具响应、环境观察）同时出现在一个长上下文中，训练模型直接基于该长上下文回答原始问题，而不再依赖工具调用。具体架构如下：
1. **证据提取与上下文编译**：从每个轨迹中提取结构化证据片段（如搜索轨迹的访问页面全文、SWE轨迹的涉及文件、SQL轨迹的查询表内容），并加入未使用的干扰项（如未访问的搜索结果、调试时查看但未修改的文件等）以增加难度。
2. **随机打乱与长度约束**：对证据片段进行随机排列后拼接成编译上下文$C$，迫使模型通过语义关联而非位置信息定位相关证据，并限制总token数$B$。
3. **推理轨迹生成**：对答案已验证的轨迹，使用DeepSeek-V3.2-Thinking生成候选推理过程，仅保留能推导出正确答案的推理轨迹作为训练目标。

关键技术特点是：损失函数$\mathcal{L}_{ACC}$仅监督推理轨迹和最终答案，没有中间动作预测项，因此最终答案的监督信号能直接传递到每个证据token，避免了标准SFT中通过多层中间步骤衰减的梯度传播问题。该方法是一个简单但有效的数据编译框架，可与任何长上下文扩展或训练方法结合（如RoPE、FlashAttention等），提供可扩展的有监督微调数据，无需额外人工标注。

### Q4: 论文做了哪些实验？

论文实验基于Qwen3-30B-A3B作为基座模型，使用编译自搜索（3369条）、软件工程（4368条）和数据库查询（3065条）三类智能体轨迹的10802个长上下文QA对进行监督微调，序列长度为131072 token。评估基准包括长距离依赖建模基准MRCR（多轮共指消解，含2针和4针子任务）和GraphWalks（图遍历，含Parents和BFS子任务），以及通用能力基准GPQA-Diamond、MMLU-Pro、AIME和IFEval。对比方法包括Qwen3-235B-A22B、GPT-OSS-120B、DeepSeek-V3.2等强基线和QwenLong-L1.5、LongRLVR、LongPO等长上下文后训练方法。主要结果：ACC在MRCR上达到68.28（+18.09），其中2针76.90（+15.06）、4针59.57（+21.16）；在GraphWalks上达到77.51（+7.59），其中Parents 81.50（+10.31）、BFS 72.95（+4.48），性能与8倍参数量的Qwen3-235B-A22B相当。通用能力无负迁移，GPQA-Diamond提升2.49、MMLU-Pro提升1.50、AIME'25提升3.33。消融实验显示：全数据混合优于单智能体类型；去除干扰项（未访问结果/未打开文件）会降低MRCR性能（-3.34至-3.81）。机制分析表明ACC训练模型展现出任务自适应注意力重构和专家专业化。

### Q5: 有什么可以进一步探索的点？

ACC的局限性主要体现在三方面。首先，其验证仅覆盖三种智能体类型和单一模型，在更广泛的任务类别和百万级上下文扩展上缺乏实证，未来需要探索多模型架构（如MoE）下长程依赖的泛化能力。其次，推理合成依赖强教师模型（如Qwen3-235B），可能导致偏见或知识短板从教师到学生的级联传播，可尝试引入对抗训练或多教师蒸馏来缓解。最后，当前仅利用工具响应与环境观测，未建模智能体内部的思考链（如推理步骤中的隐含中间状态），这可能造成监督信号损失。未来方向包括：设计更细粒度的上下文压缩策略（如基于注意力熵的动态筛选），并将ACC与强化学习结合形成闭环优化（如利用DPO对编译后的QA对进行偏好对齐），以提升模型对噪声轨迹的鲁棒性。此外，可探索ACC在代码仓库级上下文（如跨文件依赖）中的自动证据追踪能力，这需引入图神经网络进行结构化信息提取。

### Q6: 总结一下论文的主要内容

该论文提出了Agent Context Compilation (ACC)方法，用于解决大型语言模型长上下文推理能力训练中数据获取成本高的问题。核心问题在于标准有监督微调忽略工具响应，导致跨轮次分散线索未被充分利用。ACC通过将搜索、软件工程和数据库查询等大规模多轮智能体轨迹转化为长上下文问答对，使模型能直接回答而不借助工具，显式建立了问题与远距离证据间的依赖关系，无需额外标注即可实现长距离监督。主要结论显示，在Qwen3-30B-A3B上应用ACC，在长距离依赖基准MRCR和GraphWalks上分别提升18.1%和7.6%，达到与Qwen3-235B-A22B相当的水平，同时保留通用能力。机制分析表明ACC训练后模型具有任务适应性的注意力重构和专家专业化。该方法作为一种可扩展的有监督微调数据方案，能无缝结合现有长上下文扩展技术。
