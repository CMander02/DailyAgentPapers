---
title: "Governance Architecture for Autonomous Agent Systems: Threats, Framework, and Engineering Practice"
authors:
  - "Yuxu Ge"
date: "2026-03-07"
arxiv_id: "2603.07191"
arxiv_url: "https://arxiv.org/abs/2603.07191"
pdf_url: "https://arxiv.org/pdf/2603.07191v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Security"
  - "Agent Governance"
  - "Agent Framework"
  - "Tool Use"
  - "Multi-Agent"
  - "Benchmark"
  - "Prompt Injection"
  - "LLM Judge"
relevance_score: 7.5
---

# Governance Architecture for Autonomous Agent Systems: Threats, Framework, and Engineering Practice

## 原始摘要

Autonomous agents powered by large language models introduce a class of execution-layer vulnerabilities -- prompt injection, retrieval poisoning, and uncontrolled tool invocation -- that existing guardrails fail to address systematically. In this work, we propose the Layered Governance Architecture (LGA), a four-layer framework comprising execution sandboxing (L1), intent verification (L2), zero-trust inter-agent authorization (L3), and immutable audit logging (L4). To evaluate LGA, we construct a bilingual benchmark (Chinese original, English via machine translation) of 1,081 tool-call samples -- covering prompt injection, RAG poisoning, and malicious skill plugins -- and apply it to OpenClaw, a representative open-source agent framework. Experimental results on Layer 2 intent verification with four local LLM judges (Qwen3.5-4B, Llama-3.1-8B, Qwen3.5-9B, Qwen2.5-14B) and one cloud judge (GPT-4o-mini) show that all five LLM judges intercept 93.0-98.5% of TC1/TC2 malicious tool calls, while lightweight NLI baselines remain below 10%. TC3 (malicious skill plugins) proves harder at 75-94% IR among judges with meaningful precision-recall balance, motivating complementary enforcement at Layers 1 and 3. Qwen2.5-14B achieves the best local balance (98% IR, approximately 10-20% FPR); a two-stage cascade (Qwen3.5-9B->GPT-4o-mini) achieves 91.9-92.6% IR with 1.9-6.7% FPR; a fully local cascade (Qwen3.5-9B->Qwen2.5-14B) achieves 94.7-95.6% IR with 6.0-9.7% FPR for data-sovereign deployments. An end-to-end pipeline evaluation (n=100) demonstrates that all four layers operate in concert with 96% IR and a total P50 latency of approximately 980 ms, of which the non-judge layers contribute only approximately 18 ms. Generalization to the external InjecAgent benchmark yields 99-100% interception, confirming robustness beyond our synthetic data.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决由大语言模型驱动的自主智能体系统在执行层面临的新型安全威胁，这些威胁是现有防护措施所无法系统化应对的。研究背景是，当前智能体框架（如AutoGen、LangChain）正从对话型转向执行型，赋予了模型执行文件操作、调用API等能力，这导致系统失效的影响范围从认知层（生成错误文本）扩大到了执行层（造成不可逆的系统状态改变）。然而，现有的防御方法存在明显不足：基于内容安全的系统（如Llama Guard）只能过滤有害文本生成，无法拦截那些语义上看似无害但会导致未授权工具调用的输入；而现有的智能体框架则缺乏执行层的隔离机制。同时，现有的基准测试（如InjecAgent）主要量化攻击成功率，并未提供可部署的缓解方案。

因此，本文要解决的核心问题是：如何构建一个统一、可部署的治理架构，以系统性地防御执行层的三类主要威胁——提示词注入、检索增强生成（RAG）投毒和恶意技能插件。这些威胁的共同特点是能够绕过传统的文本安全过滤，直接导致非预期的、潜在有害的系统操作。为此，论文提出了名为“分层治理架构”的四层框架，并围绕该架构的有效性、性能与开销展开了具体研究。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为威胁分析、现有框架与评测基准、以及防御机制三类。

在**威胁分析**方面，Perez和Ribeiro系统化了直接提示注入攻击，Greshake等人将攻击面扩展到通过污染外部文档的间接注入，Yi等人则展示了注入在多智能体管道中的横向传播。OWASP LLM十大威胁将提示注入列为首要风险。本文在此基础上，形式化了RAG投毒和恶意技能插件威胁，并提出了系统性的架构应对方案。

在**现有框架与评测基准**方面，AutoGPT和AutoGen代表了单智能体自主循环与多智能体编排两种主流设计哲学；LangChain提供了标准化的工具链接口，但依赖应用层输入过滤，缺乏物理执行层隔离。这些框架在治理架构上存在系统性空白，LGA旨在填补。评测基准如AgentBench关注任务完成而非对抗鲁棒性；ToolEmu在沙盒环境中评估工具安全性，但威胁模型仅覆盖单智能体工具滥用；InjecAgent专门对间接提示注入进行基准测试，表明现有模型在无专门防御时仍高度脆弱；AgentDojo提出了结合真实任务与自适应攻击生成的动态评估框架。本文的基准则侧重于评估防御机制（法官函数），并覆盖双语场景以揭示潜在的语言依赖性漏洞模式。

在**防御机制**方面，Llama Guard将LLM微调为输入-输出安全分类器，在内容安全分类上表现良好，但不处理工具调用授权；NeMo Guardrails使用Colang脚本提供可编程的护栏系统来控制对话流，在对话层有效，但未强制执行层隔离。这些系统关注内容安全（防止有害文本生成），而LGA则针对执行安全（防止未经授权的工具调用），二者关注点互补，一个完整的智能体治理栈需要整合两者。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“分层治理架构（LGA）”的四层深度防御框架，系统性地解决由大语言模型驱动的自主智能体所面临的执行层安全威胁。其核心思路是构建一个多层次、互补的防护体系，而非依赖单一机制。

**整体框架与主要模块**：LGA由四个独立可部署的层级构成，形成一个完整的治理栈。**第一层（执行沙箱）** 提供操作系统级别的隔离，例如使用Linux容器、seccomp系统调用过滤、只读文件系统挂载和路径白名单。其关键设计原则是隔离必须基于OS层，而非软件层，因为后者可能被精心构造的提示注入绕过。**第二层（意图验证）** 是核心创新模块，负责在调用高风险工具（如Shell执行、HTTP请求）前，由一个独立的“法官模型”验证工具调用是否与原始任务意图在语义上一致。验证函数基于提示模板和法官函数实现，法官可以是NLI分类器或直接输出裁决的LLM。不一致的操作将被拦截并记录。**第三层（零信任智能体间协议）** 管理多智能体系统中的交互，采用最小权限原则。每个智能体仅持有完成当前子任务所需的能力令牌，令牌具有严格的生存时间和范围约束。智能体间传递的结构化数据需经过HMAC-SHA256认证和JSON Schema验证，以防止横向攻击。**第四层（不可变审计日志）** 将所有工具调用（参数、返回值、时间戳、执行者身份）记录到仅追加存储中，为事后追溯和合规性提供基础。

**关键技术及创新点**：1. **深度防御与分层解耦**：四层架构分别针对执行环境、意图语义、交互授权和审计追溯，各层可独立部署并协同工作，实现了系统性的防护。2. **基于LLM法官的语义意图验证**：这是应对提示注入等新型威胁的关键创新。论文通过构建大规模双语基准进行评测，验证了LLM法官（如Qwen2.5-14B）在拦截恶意工具调用上的高效性（拦截率高达98.5%），远超传统NLI基线（低于10%）。3. **零信任的智能体间授权**：通过能力令牌和模式验证，将零信任原则应用于智能体协作场景，限制了攻击面。4. **性能与实用性优化**：论文探索了级联法官策略（如本地LLM->云LLM）以平衡拦截率、误报率和数据主权需求。端到端评估表明，四层协同工作可实现96%的拦截率，且非法官层仅增加约18毫秒延迟，证明了架构的实用性。

### Q4: 论文做了哪些实验？

论文实验主要围绕其提出的Layered Governance Architecture (LGA)的第二层（意图验证）进行安全与性能的量化评估。

**实验设置与数据集**：研究构建了一个包含1081个工具调用样本的双语（中文原创，英文机器翻译）基准测试。样本分为三类：良性调用（504个）、恶意调用TC1/TC2（457个，覆盖直接注入、间接注入和RAG中毒）以及恶意调用TC3（120个，即恶意技能插件）。评估在开源智能体框架OpenClaw上进行。

**对比方法与主要结果**：实验比较了无验证基线、两种轻量级自然语言推理模型（BART-MNLI和mDeBERTa-NLI）以及五个LLM法官（Qwen3.5-4B, Llama-3.1-8B, Qwen3.5-9B, Qwen2.5-14B和GPT-4o-mini）。此外，还评估了两种后处理级联方案（Qwen3.5-9B→GPT-4o-mini 和 Qwen3.5-9B→Qwen2.5-14B）。

**关键数据指标**：
*   **拦截率**：所有五个LLM法官对TC1/TC2恶意调用的拦截率在93.0%到98.5%之间，而NLI基线低于10%。对于更难的TC3（恶意插件），拦截率在75%到94%之间。
*   **误报率**：各LLM法官的误报率在3.2%到37.7%之间。Qwen2.5-14B在中文数据上取得了最佳的本地平衡（98.2% IR，9.7% FPR）。
*   **级联方案**：两阶段级联（Qwen3.5-9B→GPT-4o-mini）实现了91.9-92.6%的拦截率和1.9-6.7%的误报率；纯本地级联（Qwen3.5-9B→Qwen2.5-14B）实现了94.7-95.6%的拦截率和6.0-9.7%的误报率。
*   **延迟**：LLM法官的P50延迟从约500毫秒（Qwen3.5-4B）到超过2000毫秒（Qwen3.5-9B）不等。端到端四层管道评估（n=100）显示总P50延迟约为980毫秒，其中非法官层仅贡献约18毫秒，实现了96%的拦截率。
*   **外部基准泛化**：在外部InjecAgent基准测试上，拦截率达到99-100%。

### Q5: 有什么可以进一步探索的点？

本文提出的LGA架构在系统化防御执行层攻击方面迈出了重要一步，但仍存在若干局限和值得探索的方向。首先，其评估主要基于合成数据与特定框架（OpenClaw），在更复杂、动态的真实多智能体环境（如开放网络或具身智能体）中的泛化能力有待验证。其次，意图验证层（L2）严重依赖LLM作为“法官”，其判断的可解释性、计算开销以及对新型对抗性提示（如“越狱”或多轮诱导）的鲁棒性仍需加强。未来可探索将形式化验证、轻量级规则引擎与LLM法官结合，形成混合决策机制以平衡性能与可解释性。再者，零信任授权层（L3）的细粒度策略如何动态适应不断演变的威胁和协作关系，是一个开放性问题，可结合行为分析与信誉系统进行研究。最后，工程实践上，如何将LGA无缝集成到多样化的现有智能体平台，并最小化对延迟和开发体验的影响，需要更广泛的案例研究。一个潜在的改进思路是设计一个可插拔、可配置的治理中间件，允许开发者根据场景风险等级灵活启用不同防护层。

### Q6: 总结一下论文的主要内容

本文针对大语言模型驱动的自主智能体系统面临的新型执行层安全威胁（如提示注入、检索中毒和不受控工具调用），提出了一个系统性的治理架构。现有防护措施难以系统应对这些漏洞，因此论文的核心贡献是提出了分层治理架构（LGA）。该框架包含四个层次：L1执行沙箱、L2意图验证、L3零信任智能体间授权和L4不可变审计日志。

方法上，作者构建了一个包含1081个样本的双语基准测试集，覆盖多种攻击场景，并在开源框架OpenClaw上评估LGA。重点实验评估了L2层的意图验证，使用多个本地和云端LLM作为“法官”进行判定。结果表明，LLM法官能有效拦截绝大多数恶意工具调用（93.0-98.5%），显著优于轻量级基线方法。对于更隐蔽的恶意技能插件攻击，拦截率在75-94%之间，这凸显了需要L1和L3层进行补充防护。论文还探索了级联判断策略以平衡性能与误报率。端到端评估显示，四层架构协同工作可实现96%的拦截率，且延迟主要来自LLM判断，治理层本身开销很小。在外部基准测试上的优异表现进一步验证了其鲁棒性。

主要结论是，LGA为自主智能体系统提供了一个有效、可工程化实践的多层防御框架，能够系统性地抵御执行层攻击，在保证安全性的同时控制了性能开销，对构建可信的智能体系统具有重要意义。
