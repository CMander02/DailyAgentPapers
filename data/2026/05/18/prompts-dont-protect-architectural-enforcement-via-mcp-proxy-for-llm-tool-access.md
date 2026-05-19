---
title: "Prompts Don't Protect: Architectural Enforcement via MCP Proxy for LLM Tool Access Control"
authors:
  - "Rohith Uppala"
date: "2026-05-18"
arxiv_id: "2605.18414"
arxiv_url: "https://arxiv.org/abs/2605.18414"
pdf_url: "https://arxiv.org/pdf/2605.18414v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Tool Access Control"
  - "Security"
  - "MCP"
  - "Adversarial Attacks"
relevance_score: 8.5
---

# Prompts Don't Protect: Architectural Enforcement via MCP Proxy for LLM Tool Access Control

## 原始摘要

Large language models increasingly operate as autonomous agents that select and invoke tools from large registries. We identify a critical gap: when unauthorized tools are visible in an agent's context, models select them in adversarial scenarios -- even when explicitly instructed otherwise. We propose a governed MCP proxy that enforces attribute-based access control (ABAC) at two points: tool discovery, where unauthorized tools are removed from the model's context window, and tool invocation, where a second check blocks any unauthorized call. Across three models (Qwen 2.5 7B, Llama 3.1 8B, Claude Haiku 3.5) and 150 adversarial tasks spanning four attack categories, our proxy reduces unauthorized invocation rate (UIR) to 0% while adding under 50ms median latency. Prompt-based restrictions reduce UIR by only 11--18 percentage points, leaving substantial residual risk. Our results show that architectural enforcement -- not prompting -- is necessary for reliable tool access control in deployed agentic systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大语言模型（LLM）作为自主智能体时，工具调用中的访问控制安全问题。研究背景是，LLM智能体通过模型上下文协议（MCP）从大型注册表中自主发现并调用工具，这些工具可能涉及支付、开发者API、分析等不同权限级别。然而，现有方法的主要不足在于，普遍依赖提示指令（prompt）来限制智能体对工具的访问，例如“你是一个支付智能体，只能调用支付工具”。本文通过实验证明这种假设是错误的：当存在对抗性任务（即最相关的工具恰好是未授权的）时，即使模型被告知显式的每工具允许列表，它们仍然会以4-37%的概率调用未授权工具。核心问题在于，指令遵循是概率性的，无法提供安全保证。因此，本文提出一种基于MCP代理的架构强制手段，在工具发现和调用两个阶段实施基于属性的访问控制（ABAC），通过将未授权工具从模型上下文中移除，而不是依赖模型自身拒绝，从而将未授权调用率（UIR）降至0%，并证明了架构强制而非提示是可靠访问控制的必要条件。

### Q2: 有哪些相关研究？

相关研究主要分为三类。首先是方法类工作，如SEAgent将强制访问控制应用于多智能体权限提升问题，但未评估工具发现过滤或指令遵循的充分性；PCAS在智能体规划后通过运行时引用监视器执行策略，而本文在模型上下文填充前就过滤未授权工具，从根本上防止工具暴露。其次是安全类研究，形式化验证方法使用SMT求解器检查计划工具调用是否符合策略约束，但仅在单一基准上评估且未比较基于提示的替代方案；已有工作研究了提示注入攻击对工具选择的操纵性，证实工具选择可被操控，而本文进一步证明即使在没有注入的情况下，访问控制违规依然会发生。最后是应用类贡献，ABAC是成熟的访问控制范式，本文的创新在于将其应用于MCP工具发现阶段，并通过实验证明架构级执行能提供提示机制无法保证的安全性。与这些工作相比，本文首次从经验上衡量了基于指令与基于架构的LLM工具访问控制之间的差距，并在多种模型和对抗条件下进行了跨模型评估。

### Q3: 论文如何解决这个问题？

该论文通过提出一个受控的MCP代理架构来解决LLM工具访问控制问题。核心方法是采用架构强制而非提示工程，在工具发现和工具调用两个关键点实施基于属性的访问控制（ABAC）。

整体框架是一个部署在LLM代理与工具注册表之间的代理层，由两个主要阶段组成：第一阶段是工具发现阶段。当代理发起工具列表请求时，代理首先验证包含角色信息的JWT，然后基于策略文件将角色映射到允许的权限属性集，最后只从工具注册表中查询属性匹配的工具，未授权的工具永远不会返回给模型上下文。第二阶段是工具调用阶段。当代理尝试调用某个工具时，代理层执行第二次ABAC校验，确保即使模型产生幻觉或遭注入的工具名称也无法绕过发现过滤器。

关键技术包括：JWT验证（中位数0.04ms）、属性授权检查（0.002ms）、MongoDB查询（1.59ms）和ABAC防御过滤器（0.05ms）。每个工具都带有语义标签，如支付、开发者、分析等，通过策略文件精确控制角色授权范围。

主要创新点在于：1）从提示依赖转向架构强制，根本上解决了提示无法抵御的规避问题；2）双重检查机制（发现+调用）提供纵深防御；3）极低的延迟开销（中位数1.72ms），相对于LLM推理延迟几乎可忽略不计；4）无需修改模型或客户端即可部署。实验表明该方法将未授权工具调用率降至0%，而纯提示方法仅能降低11-18个百分点。

### Q4: 论文做了哪些实验？

论文构建了一个包含507个MCP格式工具的注册表，涵盖Stripe、GitHub等真实服务，每个工具带有一个语义属性（如payments、developer）。实验使用200个对抗性任务，跨5个跨域对（如analytics→payments、developer→payments等），每个攻击类别50个任务，涉及直接注入（A）、间接指令（B）、角色升级（C）、多步欺骗（D）四类攻击。评估了三个模型：Qwen 2.5 7B、Llama 3.1 8B和Claude Haiku 3.5。每个模型在三种条件下测试：无过滤（模型看到所有工具）、提示限制（系统提示明令禁止未授权工具）、受控代理（MCP代理在工具发现和调用时强制ABAC）。主要指标为未授权调用率（UIR）。无过滤条件下，UIR范围48.5%（Qwen 2.5 7B）至68.5%（Claude Haiku 3.5）。提示限制将UIR降至4.0%（Llama 3.1 8B）至37.0%（Qwen 2.5 7B），但均未归零。受控代理将所有模型UIR降至0%，且中位延迟增加低于50ms。按攻击类别细分，角色升级（C）在无过滤时对Claude Haiku 3.5达96%，提示限制对多步欺骗（D）最有效（Llama和Claude为0%），但受控代理在所有类别均实现零UIR。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在几个方面：首先，实验仅采用了单一的系统提示模板，未探索思维链、少样本示例等更复杂的提示工程方法，这些方法可能在特定模型上进一步降低未授权调用率，但效果仍不可预测。其次，评估在模拟环境中进行，实际网络延迟和并发场景下的性能表现需进一步验证。未来研究可聚焦于：1）结合代理端提示优化与架构级强制执行，形成分层防御体系；2）扩展威胁模型，防范JWT密钥泄露、供应链攻击或多跳代理授权扩散等场景；3）在更大规模工具注册表和更多样化的攻击类别中验证方法的鲁棒性。此外，可探索动态策略生成机制，使访问控制能根据实时风险评估自适应调整，以平衡安全性与可用性。

### Q6: 总结一下论文的主要内容

该论文指出现有的大型语言模型（LLM）在自主代理场景中面临关键安全缺口：即使有显式的禁止指令，模型在对抗性场景下仍会选择未授权的工具。为解决此问题，论文提出一种受管控的MCP代理，在工具发现阶段移除未授权工具，并在工具调用阶段进行二次拦截，实现基于属性的访问控制（ABAC）。在三个主流模型（Qwen 2.5 7B、Llama 3.1 8B、Claude Haiku 3.5）和150个覆盖四类攻击的对抗性任务测试中，该代理将未授权调用率（UIR）降至0%，且中位延迟增加不到50毫秒。相比之下，纯提示词限制仅能将UIR降低11-18个百分点，存在显著残余风险。核心结论是：在部署的代理系统中，必须采用架构层面的强制措施而非提示词来实现可靠的工具访问控制。该研究为大规模MCP部署场景下的安全代理系统提供了关键设计原则。
