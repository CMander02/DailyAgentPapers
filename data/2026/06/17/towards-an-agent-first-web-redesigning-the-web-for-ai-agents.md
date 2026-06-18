---
title: "Towards an Agent-First Web: Redesigning the Web for AI Agents"
authors:
  - "Eranga Bandara"
  - "Ross Gore"
  - "Ravi Mukkamala"
  - "Asanga Gunaratna"
  - "Safdar H. Bouk"
  - "Xueping Liang"
  - "Peter Foytik"
  - "Abdul Rahman"
  - "Sachini Rajapakse"
  - "Isurunima Kularathna"
  - "Pramoda Karunarathna"
  - "Chalani Rajapakse"
  - "Ng Wee Keong"
  - "Kasun De Zoysa"
  - "Tharaka Hewa"
  - "Amin Hass"
  - "Wathsala Herath"
  - "Aruna Withanage"
  - "Nilaan Loganathan"
  - "Atmaram Yarlagadda"
date: "2026-06-17"
arxiv_id: "2606.19116"
arxiv_url: "https://arxiv.org/abs/2606.19116"
pdf_url: "https://arxiv.org/pdf/2606.19116v1"
categories:
  - "cs.AI"
  - "cs.CY"
tags:
  - "Agent-First Web"
  - "Web Agent"
  - "Agent Access"
  - "Agent Economy"
  - "Agent Content"
  - "ATML"
  - "Epistemic Recursion"
  - "Cryptographic Provenance"
  - "Multi-Agent Systems"
  - "Web Infrastructure"
relevance_score: 9.5
---

# Towards an Agent-First Web: Redesigning the Web for AI Agents

## 原始摘要

The World Wide Web was built on an assumption held for three decades: the primary consumer of web content is a human being. This permeates every layer; its access model presumes human visitors, its economics rest on human attention, and its content targets human perception. The rapid emergence of AI agents as intermediaries between humans and web content invalidates this assumption. Yet the web resists agents through blanket blocking, CAPTCHA-based exclusion, and economic models that treat agent access as extraction rather than legitimate interaction.
  This paper proposes a principled redesign across three layers. At the access layer, agents acting for humans should inherit equivalent access rights, governed by rate limiting and agent identification metadata in HTTP requests, analogous to browser headers, alongside a dual-layer architecture serving human-readable and agent-optimized content from the same domain. At the economic layer, we propose an intent-based tier framework grounded in the agent-as-human-proxy principle: an agent's economic obligation mirrors that of the human it represents. A token-based subscription model meters content in tokens rather than pageviews, alongside a commissioned content economy anchoring AI content production in human intentionality. At the content layer, we identify epistemic recursion, the self-referential loop in which AI-generated content is consumed by agents to produce further content, progressively detaching web knowledge from human ground truth. We propose the Agent Text Markup Language (ATML), a four-level human supervision tier model, and a cryptographic provenance chain to counter this threat.
  Together these constitute ten design principles for an agent-first internet, one in which agents are first-class citizens whose integration requires renegotiating the web's foundational social contract across access, economics, and content.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前万维网因AI代理（AI agents）作为人类与网页内容之间的新型中介而引发的系统性架构失效问题。研究背景指出，自1989年万维网诞生以来，其设计核心假设一直是人类是网页内容的唯一主要消费者。这种假设渗透至访问层（如验证码区分人机）、经济层（如基于注意力的广告模式）和内容层（如HTML为人类视觉呈现）。然而，大语言模型和自主AI代理的迅速崛起，使得代理能够代表人类端到端地完成任务（如订票、研究），而终端用户无需直接访问网页，这一根本性变化动摇了原有假设。

现有方法的不足表现为碎片化且被动的应对：基础设施商如Cloudflare默认封锁AI爬虫，采用按次付费的商业模型；经济层面，零点击搜索激增导致出版商流量暴跌70-80%；内容层面，AI代理消费AI生成内容再产生新内容，形成“认知递归”，使网页知识逐渐脱离人类事实基础。这些孤立方案（如协议标准、计费模型、内容溯源）未能从系统层面解决核心问题。

本文要解决的核心问题是：如何在保持网页开放性的前提下，对访问、经济和内容三层进行原则性协同重构，使代表人类行事的AI代理成为一等公民，享有与人类同等的访问权利并承担相应义务，从而修复网页因架构假设过时而破裂的社会契约。

### Q2: 有哪些相关研究？

相关研究可分为四类。第一类是AI智能体架构与网络交互，如WebShop、WebArena和Mind2Web等基准与数据集工作，它们将现有网络视为固定环境来提升智能体能力，而本文主张网络架构必须主动改变以适应智能体。第二类是智能体通信协议与基础设施，包括Anthropic的MCP、Google的A2A、IBM的ACP、微软的NLWeb及W3C Agent Web社区组等，这些工作仅解决访问和互操作问题，未涉及经济模型和认知递归后果，本文则综合了协议、经济与内容三层。第三类是网络经济学，研究如注意力经济模型、AI爬虫带来的点击率下降和付费爬取模式等，但这些应对措施是反应性的且不完整，本文提出基于“智能体作为人类代理”原则的意图分层经济模型作为系统性替代方案。第四类是内容溯源与认知完整性，包括C2PA标准、LLM文本水印、模型坍缩现象等，现有工作关注检测与归因，本文则提出ATML标记语言和加密溯源链等网络级标准以预防认知递归。综上，此前工作均孤立处理单维度问题，本文首次在同一框架内同时涵盖智能体访问模型、行为契约、经济框架、意图分层、认知递归和溯源架构六大维度。

### Q3: 论文如何解决这个问题？

论文提出了一种面向AI代理的Web三层重构方案，整体框架建立在"代理即人类代理"（agent-as-human-proxy）这一哲学锚点上，主张代表人类行事的AI代理应继承该人类同等的访问权利、经济义务与内容使用权限。

**访问层**的核心创新是**代理标识元数据**（agent identification metadata），即标准化HTTP请求头。借鉴浏览器User-Agent机制，新增Agent-Identity（代理身份与版本）、Agent-Represents（所代表用户类型：匿名/认证/订阅）、Agent-Intent（意图声明：个人使用/搜索/训练/商业/研究）、Agent-Auth（委托令牌，实现订阅继承）和Agent-Rate-Class（预期消费等级）五个头部。这些头部使服务器能区分个人助理、搜索引擎、训练爬虫与恶意机器人，从而实施逐步响应的速率限制而非一刀切封锁。此外，配套设计了**agents.txt**机器可读访问策略标准，取代依赖道德约束的robots.txt，支持基于意图的梯度访问声明。访问层还提出了**双层Web架构**，同一域名同时提供人类可读HTML内容和代理优化的结构化内容，支持渐进迁移。

**经济层**提出了**基于意图的层级框架**：代理的经济义务与其所代表人类的经济义务对等。核心是**基于Token的订阅模型**，用Token而非页面浏览量计量内容消费，直接兼容现有AI API定价体系。同时设计**委托内容经济**（commissioned content economy），由人类用户主动委托AI代理在特定来源购买专属内容片段，将AI内容生产锚定在人类意图上。此外设立基于速率限制的免费层。

**内容层**针对**认知递归**（epistemic recursion）问题——AI生成内容被AI消费再生成新内容，导致网络知识逐渐偏离人类真实——提出三项关键技术。首先是**代理文本标记语言（ATML）**，一种面向代理消费的语义内容格式，剥离HTML视觉渲染开销，实验表明可减少67.6%的Token消耗。其次是**四级人类监督层级模型**，将内容按人类监督程度分级（纯人工/人工审核AI/AI辅助人工/AI自主），使监督水平机器可读。最后是**加密溯源链**，通过密码学记录内容从人类原始产出到AI衍生各版本的完整派生链，使代理能验证内容的"人类真实性"。

三个层级的创新相互耦合：访问层的身份与意图声明为经济层的梯度计费提供技术基础，内容层的ATML格式与溯源链则依赖访问层传输代理身份信息，共同构成一个完整的十项设计原则框架，旨在重新谈判Web的基础社会契约。

### Q4: 论文做了哪些实验？

论文没有进行实证实验，而是通过概念分析和原则设计来论证一个面向AI代理的互联网架构。作者提出了三层设计原则：在访问层，代理应继承人类用户的等价访问权限，通过速率限制和HTTP元数据中的代理标识来实现；在经济层，基于"代理即人类代理"原则，提出意图导向的层级框架，采用基于Token的内容计量模式；在内容层，提出代理文本标记语言（ATML）作为人类监督层级模型。论文未使用具体数据集或基准测试，也未与现有方法进行定量比较，而是通过系统化的设计原则分析来论证其可行性，主要结果是一套包含十个设计原则的理论框架。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于预设了AI代理作为人类代理的良性角色，未充分探讨恶意代理（如自动化攻击、虚假信息传播）场景下的设计脆弱性。未来研究需构建对抗性信任模型：例如在访问层将速率限制与身份生命期绑定，防止代理身份伪造；在经济层引入惩罚性定价机制抑制非意图性内容抓取。更关键的是，ATML的四人级监督模型缺乏动态性——当人类监督者自身被AI生成内容污染时，层级标签将失效。可改进方向包括：建立图灵测试的机器化替代方案（如要求代理同步输出其推理链供验证），以及设计基于区块链的消费证明协议，使内容获取与人类意图的实时锚定成为经济交易的前提。此外，应探索DNS级代理身份注册制与Web3域名体系的融合，从网络架构层消灭匿名爬虫的生存空间。

### Q6: 总结一下论文的主要内容

这篇论文提出，万维网最初是为人类消费者设计的，但 AI 代理的兴起打破了这一基本假设，导致访问受限、经济模式失效和内容退化的三重危机。为此，论文提出了在访问、经济和内容三个层面进行重构的方案。访问层方面，通过标准化HTTP头部和“agents.txt”文件实现代理身份识别与意图声明，以速率限制取代全面封锁，并构建双内容层架构。经济层方面，基于“代理即人类代理”的原则，提出意图驱动的经济层级框架和基于代币的订阅模式，使代理的经济义务匹配其代表的人类。内容层方面，定义了“认知递归”问题，即AI生成内容被代理循环消费导致知识脱离人类真实；为此提出了代理文本标记语言、四级人工监督模型和加密溯源链。论文的核心贡献在于，将当前碎片化的应对策略统一为一个包含十项设计原则的“代理优先”互联网框架，旨在重新协商网络的社会契约，使AI代理成为网络的一等公民。
