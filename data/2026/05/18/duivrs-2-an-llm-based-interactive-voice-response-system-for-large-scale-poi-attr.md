---
title: "DuIVRS-2: An LLM-based Interactive Voice Response System for Large-scale POI Attribute Acquisition"
authors:
  - "Le Zhang"
  - "Shengming Zhang"
  - "Rui Zha"
  - "Yunpeng Wu"
  - "Jingbo Zhou"
  - "Jizhou Huang"
date: "2026-05-18"
arxiv_id: "2605.17900"
arxiv_url: "https://arxiv.org/abs/2605.17900"
pdf_url: "https://arxiv.org/pdf/2605.17900v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Conversational Agent"
  - "Interactive Voice Response"
  - "Data Augmentation"
  - "Chain-of-Thought"
  - "Industrial Deployment"
  - "Task-Oriented Dialogue"
relevance_score: 8.5
---

# DuIVRS-2: An LLM-based Interactive Voice Response System for Large-scale POI Attribute Acquisition

## 原始摘要

Accurate Point of Interest (POI) attribute acquisition is essential for location-based services, yet traditional modular Interactive Voice Response (IVR) systems suffer from error accumulation and high maintenance overhead. We present DuIVRS-2, a large language model (LLM)-based end-to-end framework designed for large-scale POI attribute acquisition at Baidu Maps. To address the long-tail distribution of real-world interactions, our methodology first employs a finite state machine (FSM)-guided data augmentation strategy to synthesize a balanced and diverse training dataset. We then streamline dialogue management via a selective generation scheme combined with a Chain-of-Thought (CoT) mechanism, which ensures output stability and effectively eliminates hallucinations in industrial settings. To facilitate continuous policy refinement with minimal manual effort, we design a cooperative iterative learning framework that leverages a dual-evaluator voting system. Deployed in production for two months, DuIVRS-2 processed 0.4 million calls daily and achieved a 83.9\% Task Success Rate (TSR), outperforming its predecessor by 4 percentage points while maintaining a low reaction time of 130ms. This work provides a production-proven reference for developing robust, cost-effective LLM agents for large-scale industrial dialogue applications.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在大规模商业地图应用中，通过交互式语音应答（IVR）系统自动获取POI（兴趣点）属性时面临的核心挑战。研究背景是地图服务需要海量、动态更新的POI属性（如名称、地址），但手动采集不现实。现有方法包括非交互式采集（如从网页、街景提取）和传统的模块化IVR系统。非交互式方法存在数据覆盖有限、易过时、从非结构化数据中提取困难以及后期人工处理成本高等不足。而作为前身的模块化IVR系统（DuIVRS-1）虽能主动致电收集信息，但其顺序模块化设计（NLU、DM、NLG）会导致错误逐级累积，且维护复杂。因此，本文要解决的核心问题是：如何在大规模工业场景中，利用大语言模型（LLM）构建一个端到端的IVR系统，以克服模块化系统的错误累积和运维开销，同时解决LLM在工业部署中面临的高成本、慢推理速度和输出不稳定性等难题，从而高效、准确且稳定地完成POI属性的大规模自动采集。

### Q2: 有哪些相关研究？

相关研究主要分为POI属性获取方法和任务型对话系统两大类。在POI属性获取方面，现有方法包括街景、网页、用户生成内容和IVRS四种主要来源。街景法仅能获取名称和位置等基础信息；网页法通过NLP解析非结构化内容，但覆盖率不足30%；用户生成内容（如Google本地导览系统）覆盖率低于10%且存在时效性问题。DuIVRS-2继承了IVRS方法的优势，通过电话交互获取POI属性，该方法已在大规模部署中验证其有效性。本文基于DuIVRS升级，从传统模块化架构转向端到端设计。在任务型对话系统方面，传统管道结构包含NLU、DST、POL、NLG四个模块，近年研究倾向于用神经网络模型统一处理子任务。大语言模型的发展推动了端到端对话系统的兴起，相关工作包括使用LLM提示词管理多参与者对话、开发慢性病支持隐私保护聊天机器人等。但现有方法受限于工业部署的稳定性、延迟和成本要求。DuIVRS-2的创新在于将LLM创新性地集成到IVRS系统中，在保持130ms低响应速度的同时实现了83.9%的任务成功率，比前代提升4个百分点，为大规摸工业对话应用提供了可参考的解决方案。

### Q3: 论文如何解决这个问题？

DuIVRS-2通过端到端的大语言模型(LLM)框架解决大规模POI属性获取问题。核心方法包括三个方面：

1. **FSM引导的数据增强策略**：针对真实对话日志的长尾分布问题，先从传统规则系统中提取有限状态机(FSM)结构，将固定回复模板映射为状态(S)，用户回复映射为转移(Σ)。通过历史日志提取经验性转移模式后，采用路径采样(按长度均匀分布)和转移采样(在状态间均匀选择用户回复变体)两种策略，将训练数据从长尾分布转换为均匀分布，有效解决罕见对话状态的冷启动问题。

2. **选择性生成与CoT机制**：在工业部署的延迟约束下，使用小型高效LLM(LLM-S)。输入包含对话历史和FSM转移生成的有效回复选项集，输出格式化为CoT推理步骤后选择最合适选项。这种方式将输出限制在预定义选项集合内，通过显式的用户意图分类保证输出稳定性和可解释性，从根本上消除幻觉。

3. **双评估器协同迭代学习框架**：构建双评估器系统——LLM-L从生成视角(条件似然)和判别视角(二元分类)评估LLM-S输出；独立黑盒LLM(如ERNIE 4.0)通过上下文学习提供无偏评判。训练过程交替进行Grow步骤(用当前策略采样新对话，高置信度样本自动加入训练集)和Improve步骤(在清洗后的增强数据集上微调模型)，形成数据飞轮效应，逐步消除历史日志噪声并适应复杂场景。

### Q4: 论文做了哪些实验？

论文进行了系统性的离线与在线实验。**离线实验**在三个来源于DuIVRS-1日志的测试集（D_effect、D_general、D_robust）上评估，以一致性率（CR）为指标。主要对比方法包括前代系统DuIVRS-1、通用大模型GPT-4o和DeepSeek-V3，以及基于Qwen2.5系列的混合模型HybridLLMs。结果显示，DuIVRS-2平均CR达77.18%，优于DuIVRS-1（68.08%）和GPT-4o（66.68%），而HybridLLMs达到77.03%，证明框架与模型无关。消融实验表明，移除CoT机制（w/o-CoT）导致CR骤降至39.00%，验证了推理过程的关键作用。**在线实验**进行了为期两个月的A/B测试，将DuIVRS-2与人类操作员和DuIVRS-1对比，以任务成功率（TSR）为核心指标。DuIVRS-2的TSR为83.9%，比DuIVRS-1（79.9%）高4个百分点，达到人类水平（89.6%）的93.64%。系统日处理40万通电话，单次通话成本低于¥0.2，平均响应时间仅130ms。此外，通过迭代学习实验发现，经过3-4次迭代后性能趋于稳定，且双评估器投票机制有效降低了人工判断比例和评估错误率。

### Q5: 有什么可以进一步探索的点？

基于该论文，未来可从以下方向深入探索：首先，论文采用FSM引导的数据增强虽缓解了长尾分布问题，但对极端罕见场景的覆盖仍有限，可探索基于对抗生成网络或扩散模型的动态数据合成方法，主动挖掘系统薄弱环节。其次，当前双评估器投票机制依赖人类标注反馈，效率仍有提升空间，可引入主动学习策略，利用模型不确定性采样高价值样本进行人工校正。第三，130ms的响应延迟虽符合实时要求，但端到端LLM在更复杂任务（如多轮情感检测）中的延迟问题尚未解决，可研究混合架构（如将简单对话流交由轻量模型处理，复杂场景才触发大模型）。此外，系统的跨领域泛化能力未验证，例如迁移至餐饮或医疗POI采集时的适配成本。最后，当前仅报告任务成功率，未分析用户长期满意度，后续可建立包含对话流畅度、修复成功率的综合评估矩阵，并探索基于强化学习的离线策略预训练以降低在线部署风险。

### Q6: 总结一下论文的主要内容

本文提出了DuIVRS-2，一个基于大语言模型（LLM）的端到端交互式语音响应（IVR）系统，旨在解决百度地图大规模POI属性采集中传统模块化IVR系统的错误累积和维护成本高的问题。该方法首先采用有限状态机（FSM）引导的数据增强策略，生成平衡且多样化的训练数据集以应对长尾分布；然后通过结合选择性生成方案和思维链（CoT）机制优化对话管理，确保输出稳定性并消除幻觉；最后设计了协同迭代学习框架，利用双评估器投票系统实现最小人工干预下的持续策略优化。生产部署两个月间，系统日均处理40万通电话，任务成功率（TSR）达83.9%，相比前代系统提升4个百分点，且反应时间低至130毫秒。该工作为开发工业级稳健、低成本的LLM对话体统提供了生产验证的参考。
