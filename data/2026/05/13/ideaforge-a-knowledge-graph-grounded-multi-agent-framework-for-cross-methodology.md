---
title: "IdeaForge: A Knowledge Graph-Grounded Multi-Agent Framework for Cross-Methodology Innovation Analysis and Patent Claim Generation"
authors:
  - "Joy Bose"
date: "2026-05-13"
arxiv_id: "2605.13311"
arxiv_url: "https://arxiv.org/abs/2605.13311"
pdf_url: "https://arxiv.org/pdf/2605.13311v1"
categories:
  - "cs.AI"
  - "cs.IR"
  - "cs.MA"
tags:
  - "多智能体系统"
  - "知识图谱"
  - "创新分析"
  - "专利生成"
  - "TRIZ"
  - "Design Thinking"
  - "SCAMPER"
  - "跨方法收敛"
  - "LLM Agent"
relevance_score: 9.5
---

# IdeaForge: A Knowledge Graph-Grounded Multi-Agent Framework for Cross-Methodology Innovation Analysis and Patent Claim Generation

## 原始摘要

Current AI-assisted innovation systems typically apply a single ideation methodology (such as TRIZ or Design Thinking) using sequential prompt-based workflows that do not preserve intermediate reasoning structure. As a result, insights generated across methodologies remain fragmented, limiting traceability, synthesis, and systematic evaluation of novelty. We present IdeaForge, a knowledge graph-grounded multi-agent framework for innovation analysis and patent claim generation. IdeaForge integrates multiple innovation methodologies (TRIZ, Design Thinking, and SCAMPER) through specialist agents operating over a persistent FalkorDB knowledge graph. Each agent contributes structured entities and relationships representing contradictions, inventive principles, user needs, transformations, analogies, and candidate claims. The central contribution of IdeaForge is a cross-methodology convergence mechanism implemented through graph-based claim linkage. Claims independently supported by multiple methodologies are connected using CONVERGENT relationships, enabling identification of high-confidence innovation candidates through graph traversal. A downstream patent drafting agent generates structured patent drafts grounded in convergent claim subgraphs, reducing reliance on unconstrained language model generation. An InnovationScore formula ranks claims by convergent support, methodology diversity, claim strength, and prior art challenge count. We describe the graph schema, agent architecture, convergence detection pipeline, and patent synthesis workflow. Experiments on a legal technology use case demonstrate that graph-grounded multi-methodology synthesis produces more diverse and traceable innovation candidates compared to single-methodology baselines. We discuss implications for computational creativity, explainable AI-assisted invention, and graph-native innovation systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

论文旨在解决当前AI辅助创新系统中普遍存在的结构性问题：多数系统仅应用单一创新方法论（如TRIZ、Design Thinking等），通过顺序提示词工作流运行，不保留中间推理状态，导致不同方法生成的洞察碎片化，缺乏可追溯性、合成能力和系统性新颖性评估。具体而言，现有方法缺乏三个关键能力：(1)跨方法流程的持久化创新图谱记忆；(2)异构创新方法论在统一框架内的集成；(3)基于跨方法收敛检测的原理性新颖性信号。IdeaForge通过构建一个知识图谱驱动的多智能体框架来应对这些挑战，该框架将TRIZ、Design Thinking和SCAMPER三种方法论作为异构推理算子作用于共享持久化知识图谱上，实现跨方法收敛检测，并据此生成可追溯、可排名的专利权利要求。

### Q2: 有哪些相关研究？

相关工作涵盖三个主要方向：(1) AI辅助创新与TRIZ系统：AutoTRIZ (2024)使用LLM自动化TRIZ推理但仅限单一方法；TRIZ Agents (Szczepanik and Chudziak, ICAART 2025)提出了多智能体TRIZ方法但缺乏持久化图记忆和跨方法合成；近期一个结合LLM和TRIZ的专利生成框架(2026)最接近IdeaForge，但同样局限于TRIZ且无知识图谱支持。(2) 知识图谱用于创意推理：GraphRAG等展示了图结构在查询摘要中的优势；Boden的创造力分类学（组合、探索、变换）正好对应SCAMPER、Design Thinking和TRIZ。但这些工作未使用持久化属性图，未与智能体系统集成。(3) 多智能体LLM系统：MetaGPT展示了角色分工协作的优势；MCP协议为工具暴露提供标准接口。IdeaForge的独特之处在于：首次将异构创新方法论集成在统一框架中，使用FalkorDB持久化知识图谱作为跨方法共享记忆，并引入基于嵌入的收敛检测机制。

### Q3: 论文如何解决这个问题？

IdeaForge采用八步流水线架构：第一步用户输入自然语言创意，在FalkorDB中创建Problem节点。第二步TRIZ智能体分析技术矛盾，识别改进/恶化参数，选择发明原理，生成Contradiction、Principle和Claim节点，并建立HAS_CONTRADICTION、RESOLVED_BY、SUPPORTS边。第三步Design Thinking智能体生成用户画像、工作任务、How-Might-We问题，创建UserNeed和Claim节点，使用MOTIVATES边连接。第四步SCAMPER智能体应用七种变换（替代、组合、适应等），生成Transformation和Claim节点，使用GENERATES边。第五步Prior Art智能体检索arXiv相关文献，创建PriorArt节点并用CHALLENGES边挑战相关权利要求。第六步嵌入合成智能体使用all-MiniLM-L6-v2计算所有跨方法权利要求对的余弦相似度，超过阈值(0.65)的创建CONVERGENT边。第七步InnovationScore模块使用加权公式（收敛计数0.4、方法多样性0.3、权利要求强度0.2、现有技术惩罚-0.1）对所有权利要求排序。第八步专利智能体从知识图谱检索最高排名权利要求及其支持子图，生成结构化专利草案。所有智能体采用模型无关设计，默认使用TinyLlama(1.1B参数)，包含JSON解析失败时的回退逻辑。核心创新在于CONVERGENT边和InnovationScore公式，将跨方法收敛作为新颖性信号。

### Q4: 论文做了哪些实验？

实验在代表性用例——印度农村印地语语音优先法律助手——上进行评估，使用TinyLlama(1.1B参数)通过Ollama运行，sentence-transformer嵌入使用all-MiniLM-L6-v2模型。知识图谱生成了16个节点和10条边，包括：1个Problem、1个Contradiction、2个Principles、1个UserNeed、3个Transformations、5个PriorArt和3个Claims。三个方法生成了语义不同的权利要求：TRIZ聚焦矛盾解决、Design Thinking关注用户画像、SCAMPER侧重跨域变换。收敛检测发现了3个收敛对，余弦相似度分别为0.837(TRIZ+DT)、0.817(TRIZ+SCAMPER)、0.819(DT+SCAMPER)。TRIZ权利要求获得最高InnovationScore(0.500)。与单一方法基线对比表明完整管线能产生更丰富且可追溯的候选。收敛阈值敏感性分析显示阈值为0.55-0.75时均产出3个收敛对。跨领域评估覆盖五个领域（法律科技、医疗AI、教育科技、精准农业、无障碍技术），四个领域实现完全收敛（3个收敛对），医疗用例仅1个收敛对，展示了框架的判别能力。

### Q5: 有什么可以进一步探索的点？

论文明确指出多个局限性和未来方向：(1) LLM质量依赖：TinyLlama频繁生成非标准JSON，需使用更大模型（如Llama 3或GPT-4）提升输出质量。(2) 收敛不等于新颖性：InnovationScore是启发式排名指标，非法律专利性评估，需整合人类专家评估。(3) 现有技术检索不完整：仅检索arXiv遗漏商业专利，需集成USPTO、EPO、Google Patents API。(4) 语义相似度限制：余弦相似度可能混淆词汇相似但语义不同的权利要求，需探索更精细的语义匹配。(5) 固定方法论集：当前仅支持TRIZ、Design Thinking、SCAMPER，未来可集成仿生学、类比推理、形态学分析。(6) 计算扩展性：当前O(n²)复杂度需使用FAISS等近似最近邻搜索优化。(7) 权重学习：InnovationScore的启发式权重可从专家标注数据学习。(8) 伦理法律考虑：生成的法律内容可能不准确，需专业审查和监管监督。

### Q6: 总结一下论文的主要内容

IdeaForge是一个知识图谱驱动的多智能体框架，用于创新分析和专利权利要求生成。其核心贡献在于将TRIZ、Design Thinking和SCAMPER三种异构创新方法论作为推理算子，作用于共享的FalkorDB持久化知识图谱，通过CONVERGENT边和基于嵌入的语义相似度实现跨方法收敛检测。框架包含八个专业智能体（TRIZ、Design Thinking、SCAMPER、Prior Art、Embedding Synthesis、InnovationScore、Patent Agent、MCP Server），采用模型无关设计，默认使用TinyLlama(1.1B参数)。InnovationScore加权公式结合收敛计数、方法多样性、权利要求强度和现有技术惩罚进行排序。实验在语音法律助手和跨五个领域（法律、医疗、教育、农业、无障碍）的评估中证明：图形驱动的多方法合成比单一方法基线产生更多样化、可追溯的候选创新。IdeaForge的核心理念是：独立推理方法对同一权利要求的收敛提供了一个原理性的新颖性信号，比单一方法支持的结果具有更高置信度。
