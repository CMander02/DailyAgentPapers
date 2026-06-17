---
title: "Scaling Enterprise Agent Routing: Degradation, Diagnosis, and Recovery"
authors:
  - "Kellen Gillespie"
  - "Robyn Perry"
date: "2026-06-16"
arxiv_id: "2606.17519"
arxiv_url: "https://arxiv.org/abs/2606.17519"
pdf_url: "https://arxiv.org/pdf/2606.17519v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent Routing"
  - "Multi-Agent Systems"
  - "Tool Selection"
  - "Enterprise Assistant"
  - "Routing Degradation"
  - "Retrieval-Augmented Routing"
  - "Production Agent"
  - "Scalability"
  - "Embedding-based Shortlisting"
relevance_score: 8.5
---

# Scaling Enterprise Agent Routing: Degradation, Diagnosis, and Recovery

## 原始摘要

Production LLM assistants route user requests to growing libraries of specialized tools, but how does routing accuracy degrade as the catalog scales? We study single-step routing on a 110-agent, 584-tool catalog from a deployed enterprise productivity assistant, evaluating three frontier models from 10 to 110 agents. Routing F1 on under-specified requests drops 16--23 percentage points across models. An oracle analysis decomposes the degradation into a \emph{retrieval} gap (the model cannot surface the right tool) and a \emph{confusion} gap (even with perfect retrieval, the oracle ceiling drops 10pp). Embedding-based shortlisting recovers +10--11pp F1 at full scale across all three models and two providers. A production annotation study (1,435 human-labeled utterances, three annotators) confirms the recovery on real traffic at +10--17pp despite 10--15pp lower absolute performance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决企业级LLM助手在扩展专用工具库时面临的路由准确性退化问题。研究背景是，生产环境中的LLM助手需要将用户请求路由到日益庞大的专业化工具库（如电子邮件、项目管理、日程安排等）中，同时OpenAI、Anthropic等平台已开始引入工具搜索机制以应对规模挑战。现有方法存在明显不足：虽然已有研究指出工具调用性能会随目录规模扩大而下降，且检索错误是主要失败原因，但退化机制（具体哪些环节出问题、在何种规模下发生、有哪些干预杠杆）尚未得到系统刻画。论文核心要解决三个具体问题：一是量化路由准确性随工具目录从10个扩展到110个时的退化程度，实验显示三个前沿模型的F1分数下降16–23个百分点；二是通过oracle分析分解退化根源，发现存在“检索缺口”（模型无法定位正确工具）和“混淆缺口”（即使完美检索，oracle上限也从79%降至69%），后者在企业场景中因语义相似工具（如Gmail/Outlook、改进/改写/校对、Jira/Asana）的自然增长而加剧；三是验证嵌入基召回（embedding-based shortlisting）作为干预手段的有效性，能在全规模下恢复10–11个百分点的F1分数，并在1435条人工标注生产数据上获得10–17个百分点的恢复效果。

### Q2: 有哪些相关研究？

相关研究可按类别组织如下:

**工具数量扩展类研究**: LiveMCPBench在527个工具上发现检索错误占代理失败的~50%;Toolshed、ScaleMCP、MonoScale和RAG-MCP均报告了工具和代理池增长时的性能崩塌。本文通过引入精确率/召回率分解和受控缓解措施,在上述研究基础上新增了细粒度分析。

**工具检索与选择类研究**:Toolformer教会语言模型在生成过程中插入工具调用;检索-路由方法涵盖了API目录的文档检索、微调检索器、重排序与查询重写、token级工具编码等;ToolScope通过合并相似工具解决语义重叠问题。本文证明密集嵌入检索在无大模型调用情况下,性能优于平台方案和微调检索器。

**代理系统扩展类研究**:AgentArch在固定工具集上变化代理架构;HuggingGPT和AnyTool分别通过层级调度进行模型和API层级路由;ScaleCall评估了企业工具选择中的混合检索方法。本文保持架构不变、变化目录规模,系统比较了层级调度与平面嵌入检索的差异。

### Q3: 论文如何解决这个问题？

论文通过提出嵌入短列表（embedding-based shortlisting）方法来解决多智能体路由准确率随工具目录规模增加而退化的问题。核心方法：使用预训练的文本嵌入模型（text-embedding-3-large）将每个工具映射为向量，对用户查询进行相同的嵌入编码，通过语义相似度检索出最相关的k个候选工具（固定k=20），再将这些候选工具送入路由器进行最终选择。架构设计上采用两阶段流水线：第一阶段是检索器，从584个工具的完整目录中快速生成20个候选工具；第二阶段是路由器，在缩减后的候选集上进行精细路由决策。关键技术包括：1）工具级检索优于智能体包级检索（pack-level），因为包级扩展会引入无关的兄弟工具，导致2-4pp的性能损失；2）大规模稠密检索器（text-embedding-3-large）优于词法匹配（BM25）和微调检索器（ToolRet-e5），BM25在共享词汇的企业生产力工具中完全失效，而微调模型因领域偏移表现不佳；3）检索器利用路由器的位置偏差（primacy bias）获得约2pp的额外精度提升。实验表明，该方案在三个前沿模型（GPT-5.4、GPT-5.1、Sonnet 4.5）上均能稳定恢复+10-11pp的F1分数，在1,435条人工标注的生产数据中恢复+10-17pp。创新点在于：首次量化了路由退化的两个独立来源——检索差距（16pp）和混淆差距（10pp），并通过短列表方法有效弥补了检索差距，同时将混淆差距作为系统固有瓶颈暴露出来。

### Q4: 论文做了哪些实验？

论文设计了三个主要实验：1) 在110个智能体、584个工具的部署企业生产力助手目录上，测试三种前沿模型（GPT-5.4, GPT-5.1, Sonnet 4.5）从10到110个智能体的单步路由性能。实验使用人工标注的1435条生产语句和合成查询，以F1分数为指标。结果显示，在未明确指代查询上，路由F1下降16-23个百分点。2) 基于嵌入的候选集预筛选（text-embedding-3-large, k=20）对比扁平路由和平台工具搜索。在584个工具规模下，嵌入候选集F1达52.5%，显著优于扁平路由的42.1%（+10.4pp）和工具搜索的50.3%。跨模型验证显示，GPT-5.4、GPT-5.1和Sonnet 4.5的F1提升分别为+10.4pp、+11.3pp和+10.0pp。3) 1435条人工注释生产语句验证实验。生产流量上，扁平路由F1仅28-36%，但嵌入候选集使所有模型F1提升至44-46%（+10-17pp）。Oracle分析将性能下降分解为检索差距（模型无法找到正确工具）和混淆差距（即使完美检索，oracle上限也下降10pp）。总体而言，嵌入候选集有效恢复了因规模扩展造成的路由性能下降。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面：一是合成查询与真实用户请求存在10-15pp的性能差距，说明合成数据无法完全覆盖真实场景中模糊意图的多样性；二是仅针对单一企业生产力目录，工具间语义高度重叠，结论向功能差异更大的领域迁移时需要重新校准；三是跨模型比较时混合了模型能力与接口差异（如OpenAI function calling vs. Anthropic native tool use），尽管验证了接口影响小于1pp但仍需谨慎。未来可探索的方向包括：1）设计动态工具排除机制，在路由时基于历史交互或上下文主动移除冗余工具以降低混淆；2）引入多轮澄清对话，让语言模型主动向用户询问歧义参数，替代单步推理的猜测；3）开发去重后的智能描述生成方法，通过自动合并相似工具定义来压缩候选集；4）研究渐进式扩展策略，结合检索增强与分类器级联，在数百工具规模下保持路由精度。

### Q6: 总结一下论文的主要内容

这篇论文研究了企业级LLM助手在路由请求到不断扩大的工具库时，路由精度如何随着目录规模扩大而下降。问题定义为单步路由在包含110个智能体、584个工具的部署型企业生产力助手上的表现。方法上，研究人员评估了三种前沿模型在10到110个智能体范围内的表现，发现路由F1值在请求不明确的情况下平均下降16-23个百分点。通过oracle分析，将退化分解为检索差距（模型无法找到正确工具）和混淆差距（即使完美检索，oracle上限也下降10个百分点）。嵌入排序法可在全规模下恢复10-11个F1点。主要结论是，退化主要由召回驱动，嵌入短排序能有效弥补检索差距，但无法消除混淆差距。生产环境标注研究（1435个语音）证实了这些发现，恢复幅度为10-17个百分点，尽管绝对表现低10-15个百分点。该研究揭示了工具库扩展时路由退化的根本原因，并提出了一种实用恢复方法。
