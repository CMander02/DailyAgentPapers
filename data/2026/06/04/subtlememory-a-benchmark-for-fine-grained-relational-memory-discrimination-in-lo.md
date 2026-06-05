---
title: "SubtleMemory: A Benchmark for Fine-Grained Relational Memory Discrimination in Long-Horizon AI Agents"
authors:
  - "Wenxuan Wang"
  - "Haoyu Sun"
  - "Fukuan Hou"
  - "Mingyang Song"
  - "Weinan Zhang"
  - "Yu Cheng"
  - "Yang Yang"
date: "2026-06-04"
arxiv_id: "2606.05761"
arxiv_url: "https://arxiv.org/abs/2606.05761"
pdf_url: "https://arxiv.org/pdf/2606.05761v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "长期记忆"
  - "关系记忆"
  - "基准测试"
  - "AI Agent"
  - "LLM Agent"
  - "精细记忆区分"
  - "下游推理"
relevance_score: 9.0
---

# SubtleMemory: A Benchmark for Fine-Grained Relational Memory Discrimination in Long-Horizon AI Agents

## 原始摘要

Persistent AI assistants, such as OpenClaw, accumulate large collections of related memories over long-term interactions. As these memories grow, they may reinforce one another, diverge across contexts, or directly conflict, making correct assistance depend on memory relations rather than isolated recall. Existing long-term memory benchmarks rarely probe how agents preserve and utilize such relations during downstream tasks. To address this gap, we introduce SubtleMemory, a benchmark for fine-grained relational memory discrimination in long-running AI agents. SubtleMemory constructs relation-controlled latent semantic artifacts whose variants instantiate complementary, nuanced, or contradictory relations, and embeds them into realistic user-agent histories, requiring agents to recover distributed relational structures during later queries and instructions. The benchmark contains 1,522 evaluation instances over 10 long histories, grounded in 1,090 relation-controlled memory-variant sets and spanning user-related and non-user-related queries. Evaluating six standalone memory systems, two Claw-style agents with native memory modules, and three Claw-style agents with plugin memory modules, we find that current systems remain weak on fine-grained relational memory discrimination. We further introduce diagnostic protocols that reveal distinct capability profiles across memory preservation, retrieval, and downstream reasoning stages.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决长期AI助手在处理细微关系性记忆区分方面的不足。研究背景在于，持久性AI助手（如OpenClaw）在与用户长期交互中会积累大量相关记忆，这些记忆可能相互增强、在不同上下文中产生分歧或直接冲突，正确的辅助行为依赖于记忆间的相互关系，而非孤立的回忆。现有长期记忆基准大多评估系统能否检索或操作单个记忆，鲜少测试系统在后续任务中保留和利用多个相关记忆间细微关系的能力。针对这一空白，论文提出了SubtleMemory基准，通过构建关系控制的语义变体，嵌入到逼真的多轮交互历史中，要求代理在查询和指令执行时恢复并正确推理分布于历史中的分布式关系结构。核心问题在于当前AI系统对细微关系性记忆的区分能力薄弱，尤其在面对矛盾记忆时，即便使用最强模型和优化提示策略，系统仍难以恰当识别未解决的冲突，导致错误聚合或过度泛化。

### Q2: 有哪些相关研究？

相关研究可分为方法与应用类、评测类。方法类方面，早期工作如Reflexion、MemWalker等探索了外部记忆辅助agent进行反思与任务延续；近期系统如MemGPT、Memit、Agentic Note Networks等将记忆管理明确为设计问题，通过虚拟上下文管理器、层次化记忆、时序知识图谱等机制优化记忆的写入、压缩与检索。本文指出现有方法在记忆检索依赖隐含的关系分数或摘要链接，未明确验证模型能否在需要时精细区分相似记忆间的细微关系。

应用类方面，Claw类智能体通过原生记忆模块或插件记忆模块维持运行时上下文，本文测试了包括ClawArena风格在内的两类agent。评测类方面，LoCoMo、LongMemEval、PersonaMem-v2、Mem2ActBench等是代表性长期记忆基准，分别侧重多会话回顾、QA与遗忘、偏好推断、工具操作等。ClawArena关注多源冲突与信念修正，但均将记忆使用视为检索、更新或应用单一相关信息，而未构建以目标为条件的多组相关记忆并控制其互补、细微或矛盾关系。SubtleMemory通过精确控制目标相关的语义变体集、明确的关系分类法以及保存→检索→推理的分阶段诊断协议，填补了现有基准在精细关系记忆判别上的空白。

### Q3: 论文如何解决这个问题？

SubtleMemory通过构建精细的关系记忆判别基准来解决现有基准无法评估智能体在长程交互中关系记忆推理能力的问题。其核心方法是构造“潜在语义工件”——一组语义变体（种子事实的互补、细微区分或矛盾版本），并将其嵌入长时间的用户-智能体交互历史中，要求智能体在后续查询时恢复并推理这些分布式关系结构。

整体框架包含五个阶段：1）从开源基准中提取语义种子（用户偏好或知识事实）；2）通过细节丰富、掩码或语义近邻搜索生成变体，并定义互补、细微和矛盾三种关系；3）将每个变体实例化为多轮会话（逐步隐含地揭示事实）；4）生成查询及参考答案（要求关系推理）；5）将相关会话与非相关会话交错组装成长历史。关键技术包括：关系控制变体生成、延迟分布嵌入（相关记忆分散在无关会话之间）、以及LLM-as-Judge的正确性评估协议。创新点在于：首次明确定义了三种记忆关系（互补/细微/矛盾），并设计了对应的评估实例；将关系推理分解为记忆保存、检索和下游推理三个阶段进行诊断；构建了包含1522个评估实例、1090个变体集的基准。

### Q4: 论文做了哪些实验？

论文进行了以下实验：实验设置包括三种部署场景：6个独立记忆系统（Mem0、MemOS、EverMemOS、MIRIX、A-Mem、MemoBase）、2个Claw风格原生记忆Agent（OpenClaw、MetaClaw），以及OpenClaw集成3个插件记忆模块（Mem0、MemOS、EverMemOS）。使用Gemini 3.1 Pro Preview Thinking作为LLM评审，其与人工标注的Cohen's κ达0.963。主要采用gpt-5.4和gpt-oss-120b两个答案生成模型，并设置了Oracle和Perfect Retrieval两个对照条件。数据集包含1,522个评估实例，覆盖10段长历史记录，基于1,090个关系控制记忆变体集。主要结果显示：最强独立系统（GPT-5.4下A-Mem 70.0%、Mem0 69.0%、EverMemOS 68.1%）仍远低于Oracle（85.4%），差距在互补、细微和矛盾关系上分别达18.0%、10.0%和18.3%；矛盾关系最具挑战性，Oracle仅达68.7%而A-Mem仅50.4%；原生OpenClaw仅62.5%，集成Mem0后提升至71.3%；诊断水分析揭示了记忆保存、检索和下游推理阶段的能力差异。

### Q5: 有什么可以进一步探索的点？

本工作主要在文本型长期助手记忆上评估，未覆盖多模态、多语言或强领域特化场景，未来可扩展至视觉与语音混合的记忆形式，并引入人工校验以克服大模型判断偏差。诊断协议虽定位了保存、检索与推理阶段的瓶颈，但三个阶段紧密耦合，现有指标只能给出条件成功率，难以独立测量每种能力的上限。可设计更细粒度的控制实验，例如在保存阶段直接注入干扰记忆，或在检索阶段固定检索器参数以独立测试推理能力。矛盾关系记忆的保存与检索均显著弱于互补关系，这可能源于内存内事实冲突导致的表示干扰。一种改进思路是引入冲突感知的写作策略，当写入新记忆与现有记录矛盾时，主动标记冲突并触发专家模型裁决或重写历史。此外，当前基准仅包含10条长历史、1522个实例，规模偏小，且全部来自合成变体，缺乏真实用户交互中的噪点记忆和语境漂移。未来可构建更大规模、带人工标注的长期办公或生活助手日志，并将关系记忆推理任务嵌入实际工具调用与决策链中，以检验细粒度关系记忆在端到端任务中的真正价值。

### Q6: 总结一下论文的主要内容

针对长期交互AI助手在记忆规模增长时难以区分细粒度关系的问题，本文提出SubtleMemory基准。该基准通过构建受控于关系的潜在语义变体（如互补、细微或矛盾关系），将其嵌入长达10轮的用户-代理历史中，要求代理在后续查询中恢复分布式关系结构。核心贡献在于首次系统评估了代理对多段记忆间关系的精细辨别能力，而非简单记忆检索。实验涉及6个独立记忆系统、2个原生记忆模块Claw代理及3个插件记忆模块Claw代理，共1522个评估实例。主要结论显示现有系统在关系记忆保持、检索和下游推理阶段均表现薄弱：不仅会遗漏相关记忆，更会丢失关键关系细节、检索不完整证据，且难以在答案生成中正确利用关联记忆。该工作揭示了当前代理在长程交互中维持记忆分辨能力的根本瓶颈，为构建能处理微妙记忆冲突的AI系统提供了评估框架。
