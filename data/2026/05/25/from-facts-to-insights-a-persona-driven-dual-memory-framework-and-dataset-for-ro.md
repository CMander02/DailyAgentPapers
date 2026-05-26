---
title: "From Facts to Insights: A Persona-Driven Dual Memory Framework and Dataset for Role-Playing Agents"
authors:
  - "Rongsheng Zhang"
  - "Ruofan Hu"
  - "Weijie Chen"
  - "Jiji Tang"
  - "Junnan Ren"
  - "Wanying Wu"
  - "Xunuoyan Chen"
  - "Tangjie Lv"
  - "Tao Jin"
  - "Zhou Zhao"
date: "2026-05-25"
arxiv_id: "2605.25693"
arxiv_url: "https://arxiv.org/abs/2605.25693"
pdf_url: "https://arxiv.org/pdf/2605.25693v1"
github_url: "https://github.com/role2026/rolememo"
categories:
  - "cs.CL"
  - "cs.DB"
  - "cs.MA"
tags:
  - "角色扮演Agent"
  - "长期记忆框架"
  - "基准数据集"
  - "微调/强化学习"
  - "个性化推理"
relevance_score: 9.0
---

# From Facts to Insights: A Persona-Driven Dual Memory Framework and Dataset for Role-Playing Agents

## 原始摘要

While role-playing agents excel in short-term interactions, long-term conversations overwhelm context windows, motivating external memory frameworks. Current systems typically rely on persona-agnostic summarization, which records facts without persona-specific interpretation, yielding generic responses that compromise persona fidelity. To bridge this gap, we introduce RoleMemo, a dataset featuring four reasoning tasks where the factual fragments must be interpreted through the persona to reach the correct answer. Evaluation on RoleMemo exposes critical limitations of persona-agnostic frameworks. We thus propose DualMem, which decouples memory into two streams: factual cognition and persona-conditioned insight. Trained through Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL), our framework with a 4B-parameter model outperforms zero-shot persona-agnostic frameworks powered by DeepSeek-V3.2 for sustained persona fidelity. Our resources are available at https://github.com/role2026/rolememo.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有角色扮演代理在长期对话中，由于依赖于无视人设的通用记忆框架（persona-agnostic summarization）而导致的人设一致性（persona fidelity）不足的问题。研究背景是，虽然当前的角色扮演代理在短时交互中表现出色，但长对话会超出上下文窗口的容量，因此需要引入外部记忆框架。现有方法通常使用一个无视人设的模型将历史对话总结为中性事实，然而，这种记忆方式与真实的人类认知过程相悖——人类的记忆是“重构性”的，即个体会根据自身人设对经历进行解读和存储，而非简单地记录客观事实。例如，对于“深夜玩游戏”这一事实，一个心理学家角色的记忆应将其解读为“行为性疲劳”，而非仅记录中性事件。现有方法的不足在于，它们在检索时仅能提供表面的事实，而缺乏基于人设的解释性洞察（insight），导致代理在推理时需从头进行不可靠的重建，最终产生违背人设的通用回答。同时，现有的评估基准多侧重于事实检索（如“大海捞针”式任务），无法暴露这一核心缺陷。因此，本文旨在解决的核心问题是：如何构建一种新的大规模数据集（RoleMemo）以评估长期对话中人设驱动的重构性记忆，并据此提出一种双流记忆框架（DualMem），将记忆解耦为事实认知与基于人设的洞察认知，从而提升代理在长期交互中的人设忠实度。

### Q2: 有哪些相关研究？

相关研究主要分为三类。第一类是**记忆框架方法**，早期采用检索增强生成（RAG）搜索未压缩对话历史，但存储开销大。近期研究转向智能体记忆框架，如使用与角色无关的模型迭代提取对话中的关键事实，并通过层次结构、轻量压缩和任务驱动预测建模更新记忆。本文指出，这些方法优先提取普遍显着的事实，忽略了角色特定的细微解释，导致响应缺乏角色保真度。第二类是**长时任务解决智能体**，如Reflexion通过反思执行轨迹构建高层记忆以抽象经验用于未来任务完成。这与角色扮演中角色条件化解释的记忆目标不同。第三类是**基准评测**，现有记忆基准通过“大海捞针”范式评估显式事实检索，强调查询与键的字面匹配，无法评估角色驱动的记忆推理；而角色扮演基准虽注重角色保真度，但将记忆评估局限于短对话窗口，无法衡量长上下文中的角色一致性。本文提出的RoleMemo数据集填补了这一空白，通过四项推理任务要求智能体基于角色解释事实碎片。

### Q3: 论文如何解决这个问题？

论文通过提出RoleMemo数据集和DualMem框架来解决长期对话中角色扮演代理的人物保真度问题。核心方法是构建一个双流记忆架构，将记忆解耦为事实认知和人物条件洞察两个部分。

RoleMemo数据集构建了四个推理任务，要求代理将分散的事实片段通过人物角色进行解释性理解，而非简单的表面检索。该数据集包含2052个角色和26636条洞察，每一对事实与洞察构成核心单元。对话历史规模从32k扩展到256k token，嵌入事实片段时确保其自然语境化且依赖周围的语句。

DualMem框架的核心组件包括两个互补的认知类型：事实认知捕捉对话中的客观事件和语义细节，保持现有方法的信息基础；洞察认知则从事实认知中推导出基于人物的解释，每个洞察引用其基础事实以保持可追溯性。记忆构建过程采用增量方式，将对话历史划分为固定大小的块并顺序处理。每一步，模型按顺序先提取事实认知，再基于事实和先前记忆通过人物角色构建洞察认知，最后将所有认知统一存储在记忆库中。当检索到洞察认知时，其关联的事实认知也被包含以提供证据支持。

技术创新点包括：(1) 双流记忆解耦机制；(2) 通过监督微调和强化学习进行训练，其中RL框架使用多轮对话轨迹，并通过格式合规和角色质量两个奖励函数优化；(3) 基于角色驱动的解释性推理，而非中性的事实记录。实验表明，4B参数的DualMem框架在持续人物保真度上超越了基于DeepSeek-V3.2的零样本基线。

### Q4: 论文做了哪些实验？

论文在RoleMemo数据集上进行了两项核心实验。首先是记忆构建质量评估，设置32k token对话历史，使用Recall@10指标，对比了NoMem和八种无个性化记忆框架（HiMem、O-Mem、Mirix、LightMem、SimpleMem、Mem0、PreMem、Memalpha），这些基线使用DeepSeek-V3.2（685B）作为记忆模型。结果是：在事实回忆方面，DualMem-RL和DualMem-SFT分别达到0.77和0.76，超越所有基线（最好为Mem0的0.74）；在洞察回忆方面，DualMem-RL达到0.73，DualMem-SFT达到0.65，而基线最好仅0.41，差距显著。其次是角色扮演质量评估，使用GPT-5.1在信息丰富度、逻辑质量、角色一致性、对话吸引力四个维度的5分制评分。DualMem-RL以4.16的平均得分全面超越基线（3.94-4.01），其中信息丰富度4.22，逻辑质量3.78。消融实验证明移除训练或任一记忆流都会导致性能下降。

### Q5: 有什么可以进一步探索的点？

该研究存在几个值得深入探索的局限性。首先，目前的评估仅覆盖256k token的历史对话，但真实场景中可能涉及数百万token的长期交互，需要更高效的增量处理机制。其次，尽管包含2052种人格，但面对现实中无限多样的人格特征，模型的泛化能力尚未在自然场景中得到验证。此外，数据集由单一LLM生成，可能编码了特定生成器的人格推理风格，导致评测结果部分反映了与生成器的对齐而非真正的人格驱动理解。未来的工作可以考虑：探索更高效的增量记忆更新机制；构建更大规模、更多样化的人格数据集；采用多模型协同生成数据以减少偏差；优化强化学习训练效率以降低计算成本；开展纵向用户研究验证长期角色一致性；以及扩展情感调节、多模态交互等更全面的陪伴能力评估。

### Q6: 总结一下论文的主要内容

角色扮演智能体在长期对话中面临语境窗口过载的问题，现有方法依赖角色无关的记忆框架，仅存储中性事实，导致智能体在推理时需重新解释，从而产生缺乏角色忠诚度的通用回复。针对此问题，论文提出了RoleMemo数据集，涵盖跨会话推理和深度角色解释等四项任务，要求智能体基于角色身份对历史事实进行解释性理解。评估显示角色无关框架在此类任务中存在结构性缺陷。由此，论文提出DualMem框架，将记忆解耦为事实认知和角色条件洞察两个流，通过监督微调和强化学习训练一个4B参数模型。实验表明，该模型在角色忠诚度上优于由DeepSeek-V3.2驱动的零样本角色无关框架。该工作首次构建了角色驱动重建记忆基准，并证明了通过专门训练分离记忆流能显著提升角色扮演质量。
