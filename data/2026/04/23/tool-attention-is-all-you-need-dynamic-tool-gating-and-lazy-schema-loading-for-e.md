---
title: "Tool Attention Is All You Need: Dynamic Tool Gating and Lazy Schema Loading for Eliminating the MCP/Tools Tax in Scalable Agentic Workflows"
authors:
  - "Anuj Sadani"
  - "Deepak Kumar"
date: "2026-04-23"
arxiv_id: "2604.21816"
arxiv_url: "https://arxiv.org/abs/2604.21816"
pdf_url: "https://arxiv.org/pdf/2604.21816v1"
github_url: "https://github.com/asadani/tool-attention"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Tool Use"
  - "Efficient Inference"
  - "Context Reduction"
  - "Middleware"
  - "MCP"
relevance_score: 8.5
---

# Tool Attention Is All You Need: Dynamic Tool Gating and Lazy Schema Loading for Eliminating the MCP/Tools Tax in Scalable Agentic Workflows

## 原始摘要

The Model Context Protocol (MCP) has become a common interface for connecting large language model (LLM) agents to external tools, but its reliance on stateless, eager schema injection imposes a hidden per-turn overhead the MCP Tax or Tools Tax that practitioner reports place between roughly 10k and 60k tokens in typical multi-server deployments. This payload inflates the key-value cache, is associated with reasoning degradation as context utilization approaches published fracture points around 70%, and turns token budgets into a recurring operational cost. We introduce Tool Attention, a middleware-layer mechanism that generalizes the "Attention Is All You Need" paradigm from self-attention over tokens to gated attention over tools. Tool Attention combines (i) an Intent Schema Overlap (ISO) score from sentence embeddings, (ii) a state-aware gating function enforcing preconditions and access scopes, and (iii) a two-phase lazy schema loader that keeps a compact summary pool in context and promotes full JSON schemas only for top-k gated tools. We evaluate on a simulated 120-tool, six-server benchmark whose per-server token counts are calibrated to public audits of real MCP deployments. In this simulation, Tool Attention directly reduces measured per-turn tool tokens by 95.0% (47.3k -> 2.4k) and raises effective context utilization (a token-ratio quantity) from 24% to 91%. End-to-end figures for task success, latency, cost, and reasoning quality are reported as projections derived from the measured token counts combined with published deployment telemetry; they are not measured on live LLM agents, and we mark projected values explicitly throughout. Taken together, the results support a simple thesis: protocol-level efficiency, not raw context length, is a binding constraint on scalable gentic systems. The code for this work is accessible at https://github.com/asadani/tool-attention

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）智能体在使用模型上下文协议（MCP）时面临的一个核心效率与成本问题——即“工具税”（Tools Tax）。研究背景是，MCP作为连接LLM智能体与外部工具的标准接口，其设计为了互操作性而采用无状态、急切式（eager）的架构，导致在每个对话轮次中都必须重新序列化并注入所有工具的全部JSON架构。现有方法的不足体现在：这种模式每轮次会消耗约1万到6万token（在典型的多服务器部署中），这首先造成了显著的经济成本，因为所有token都按量计费；其次，这种开销挤占了有限的上下文窗口，当上下文利用率接近70%的认知“断裂点”时，LLM的推理能力会急剧下降，出现参数幻觉、工具混淆和任务记忆丢失；再者，大量冗余的架构文本也扩大了攻击面，使得恶意工具描述可以通过“工具投毒攻击”劫持智能体控制流。现有的缓解方案，如静态剪枝或手动范围限定，要么牺牲灵活性，要么需要大量工程改造，无法实现通用且无损的部署。为此，本文提出了Tool Attention，一个位于中间件层的注意力机制，旨在通过动态工具门控和惰性架构加载，从根源上消除MCP/工具税，在保持MCP协议语义不变的前提下，实现可扩展的智能体工作流。

### Q2: 有哪些相关研究？

相关工作可分为以下几类：

1. **协议与基础设施类**：MCP规范本身是本文的直接基础，其因无状态设计导致每次注入完整schema的“工具税”开销。后续MOQT草案和IETF代理通信草案提出传输层改进，而本文的Tool Attention则在应用中间件层提供可立即部署的互补方案。

2. **检索增强与工具检索类**：RAG、Toolformer、ReAct等方法将工具集固定注入prompt，无法规避规模膨胀。语义路由网关（如Cloudflare Code Mode）虽执行类似工具检索，但缺少形式化理论支撑和状态感知门控，而本文提出了基于ISO分数和状态门控的两阶段加载机制。

3. **注意力效率优化类**：注意力稀疏化、FlashAttention、KV缓存量化等工作仅优化注意力计算方式，无法减少协议强制注入的token数量。本文方法正交且可组合，通过减少prompt中的schema token直接降低KV缓存规模。

4. **中间件编排类**：LangChain、LangGraph、Semantic Kernel等框架暴露模型前后钩子，本文方法原生适配这些中间件架构的`before_model`阶段。

5. **安全防御类**：MindGuard的决策依赖图（DDG）和总注意力能量（TAE）指标用于检测工具中毒攻击，本文借用TAE直觉进行防御性门控。

6. **混合执行类**：Anthropic的代码执行模式通过优化工具输出来减少token，而本文优化工具定义阶段，两者可组合实现全栈优化。

关键区别在于：现有工作或仅关注传输层改进、或缺乏状态感知、或未减少协议强制的冗余token，而Tool Attention通过意图-模式重叠分数、状态化门控与懒惰加载机制，将每轮工具token削减95.0%，将上下文利用率从24%提升至91%，并直接解决了可扩展智能体系统的协议级效率瓶颈。

### Q3: 论文如何解决这个问题？

Tool Attention通过一个三层机制将传统的全量工具注入问题转化为可优化的动态选择问题。核心设计包括：(i) **Intent-Schema Overlap (ISO) 评分**：使用sentence-transformers/all-MiniLM-L6-v2将用户查询和工具摘要（名称+简短自然语言描述，≤60 tokens）编码为384维向量，通过余弦相似度计算语义匹配分数；(ii) **状态感知门控函数**：在ISO评分基础上叠加预定义前提条件（如认证状态、工作流里程碑）的确定性过滤，仅保留同时满足语义阈值θ和状态约束的工具；(iii) **两阶段惰性Schema加载**：阶段1将全部N个工具的紧凑摘要（~40 tokens/个）常驻上下文作为稳定摘要池，支持prompt缓存；阶段2仅在每轮从注册表中动态加载top-k门控工具的完整JSON schema。整体架构由四个协作模块组成：IntentRouter（FAISS索引+编码器）、ToolVectorStore（持久化索引）、LazySchemaLoader（LRU缓存按需加载schema）、ToolAttention（中间件编排器）。创新点在于将Transformer的自注意力范式推广到工具层面——用廉价嵌入空间代理估计工具在即将进行的前向传播中的期望总注意力能量（TAE），仅注入TAE超过阈值θ的工具，从而将每轮工具令牌从47.3k削减至2.4k（减少95%），有效上下文利用率从24%提升至91%。此外，after_model钩子还实现了幻觉拒绝门控，当模型调用未激活工具时返回结构化错误，确保激进门控的安全性。

### Q4: 论文做了哪些实验？

该论文的实验是在模拟环境中进行的，而非实时的端到端代理评估。主要实验设置如下：

- **实验设置**：构建了一个包含120个工具、6个服务器的合成MCP测试平台，模拟真实MCP部署的工具足迹。
- **数据集/基准测试**：采样了500个合成任务，包括单步、多步和长周期工作流，每个任务有人工标注的所需工具集作为真实值。对比方法包括：B1全架构（注入所有120个工具）、B2静态剪枝（人工选择30个工具）、B3简单检索（top-k=10余弦检索）、B4 CLI懒加载（mcp2cli模式）和作者提出的Tool Attention。
- **主要结果**：
  - **直接测量**：Tool Attention将每轮工具令牌从47,312个降至2,368个（减少95.0%），有效上下文利用率从24%提升至91%。
  - **投影结果**：任务成功率约为94%，P50延迟约2.0秒，每任务成本约0.03美元，均优于所有基线。
  - **推理质量**：投影LLM裁判评分4.43，87.6%评分≥4，远高于其他方法。
  - **消融实验**：懒加载是最大贡献（+10.3%成功率），前置条件贡献+3.6%，语义匹配优于词法匹配（TF-IDF导致-8.1%）。

### Q5: 有什么可以进一步探索的点？

## 局限性与未来研究方向

**核心局限**：论文主要基于仿真环境评估，缺乏真实MCP工作负载和端到端LLM agent的实测数据；工具摘要质量对检索精度高度敏感；缺乏社区标准基准。

**关键未来方向**：
1. **对抗性鲁棒性**：攻击者可构造语义接近的恶意工具描述绕过门控，需集成运行时监控（如TAE异常检测）。
2. **跨回合状态感知**：当前仅使用单轮用户查询嵌入，可引入任务状态编码器捕获中间工具输出与演化计划，初步实验显示多跳任务成功率+1.7pp。
3. **可学习门控**：用轻量MLP分类器替代阈值门控（查询-工具匹配度评分），预计额外提升1-3pp成功率且延迟<1ms。
4. **与代码执行融合**：将Tool Attention的输入侧门控与Anthropic输出侧代码执行结合，可再降一个数量级上下文消耗。
5. **协议层收敛**：MCP-over-MOQT可部分替代惰性加载，但意图门控仍需持续存在以塑造模型注意力。

**个人见解**：动态工具门控与主动遗忘机制结合可能是突破方向——当工具被门控排除后，其KV缓存应被显式压缩或移除，而非仅保留摘要，可进一步突破70%上下文利用率断裂点。

### Q6: 总结一下论文的主要内容

《MCP/Tools Tax》是协议设计缺陷（将所有工具视为常驻上下文），线性扩大目录时导致有效上下文窗口缩减、推理降级和成本上升。为解决该问题，论文提出Tool Attention中间件，将“Attention Is All You Need”自注意力泛化为对工具的注意力门控，结合意图模式重叠分数、状态感知门控和两阶段懒加载机制。在模拟120工具/6服务器的基准中，该方法每轮工具令牌减少95.0%（47.3k→2.4k），有效上下文利用率从24%提升至91%。主要结论为：协议级效率（而非原始上下文长度）才是可扩展智能体系统的关键约束。
