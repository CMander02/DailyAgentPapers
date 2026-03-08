---
title: "AWE: Adaptive Agents for Dynamic Web Penetration Testing"
authors:
  - "Akshat Singh Jaswal"
  - "Ashish Baghel"
date: "2026-03-01"
arxiv_id: "2603.00960"
arxiv_url: "https://arxiv.org/abs/2603.00960"
pdf_url: "https://arxiv.org/pdf/2603.00960v1"
github_url: "https://github.com/stuxlabs/AWE"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Multi-Agent Systems"
  - "Tool Use & API Interaction"
relevance_score: 7.5
taxonomy:
  capability:
    - "Multi-Agent Systems"
    - "Tool Use & API Interaction"
  domain: "Cybersecurity"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "Claude Sonnet 4"
  key_technique: "AWE (memory-augmented multi-agent framework with structured, vulnerability-specific analysis pipelines)"
  primary_benchmark: "XBOW"
---

# AWE: Adaptive Agents for Dynamic Web Penetration Testing

## 原始摘要

Modern web applications are increasingly produced through AI-assisted development and rapid no-code deployment pipelines, widening the gap between accelerating software velocity and the limited adaptability of existing security tooling. Pattern-driven scanners fail to reason about novel contexts, while emerging LLM-based penetration testers rely on unconstrained exploration, yielding high cost, unstable behavior, and poor reproducibility.
  We introduce AWE, a memory-augmented multi-agent framework for autonomous web penetration testing that embeds structured, vulnerability-specific analysis pipelines within a lightweight LLM orchestration layer. Unlike general-purpose agents, AWE couples context aware payload mutations and generations with persistent memory and browser-backed verification to produce deterministic, exploitation-driven results.
  Evaluated on the 104-challenge XBOW benchmark, AWE achieves substantial gains on injection-class vulnerabilities - 87% XSS success (+30.5% over MAPTA) and 66.7% blind SQL injection success (+33.3%) - while being much faster, cheaper, and more token-efficient than MAPTA, despite using a midtier model (Claude Sonnet 4) versus MAPTA's GPT-5. MAPTA retains higher overall coverage due to broader exploratory capabilities, underscoring the complementary strengths of specialized and general-purpose architectures. Our results demonstrate that architecture matters as much as model reasoning capabilities: integrating LLMs into principled, vulnerability-aware pipelines yields substantial gains in accuracy, efficiency, and determinism for injection-class exploits. The source code for AWE is available at: https://github.com/stuxlabs/AWE

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现代Web应用安全评估中传统工具与快速发展的开发模式之间的脱节问题。研究背景是，随着AI辅助开发、无代码平台和快速部署流程的普及，Web应用的开发速度大幅提升，但大量开发者缺乏安全专业知识，导致攻击面显著扩大。然而，现有的安全工具（如基于模式的扫描器）缺乏真正的推理能力，无法适应新颖的上下文；而新兴的基于大语言模型（LLM）的渗透测试方法虽然具备一定的探索能力，但往往依赖无约束的探索，导致成本高、行为不稳定、可复现性差。

现有方法的不足主要体现在两方面：一是传统模式驱动扫描器无法理解动态上下文，难以检测逻辑漏洞或新出现的攻击模式；二是通用LLM智能体在渗透测试中盲目探索，效率低下且结果不可靠。本文要解决的核心问题是：如何构建一个既能像人类测试者一样进行智能推理，又能保持高效、稳定和可解释性的自动化Web渗透测试框架。为此，论文提出了AWE（自适应Web利用框架），这是一个记忆增强的多智能体系统，它将结构化的、针对特定漏洞的分析流程嵌入轻量级LLM编排层，通过上下文感知的负载变异与生成、持久记忆以及基于浏览器的验证，实现确定性的、以利用为导向的安全测试，从而在准确率、效率和确定性方面取得显著提升。

### Q2: 有哪些相关研究？

相关研究主要可分为三类：传统扫描工具、基于LLM的辅助系统以及自主多智能体框架。

**传统动态应用安全测试工具**：如Burp Suite、OWASP ZAP、Nuclei和sqlmap等，它们依赖签名驱动的有效载荷库和启发式模式匹配。这些工具在检测已知注入漏洞时表现优异，但本质上是静态的，无法针对非标准的输入处理或防御机制合成新的有效载荷或调整攻击策略，且在多步骤探测或需要上下文推理的场景中容易出现误报和漏报。本文的AWE框架旨在克服这种僵化性，通过LLM驱动实现动态、自适应的攻击推理。

**基于LLM的辅助渗透测试系统**：以PentestGPT为代表，它证明了LLM可以辅助人类测试者构建工作流、建议侦察策略和制定利用逻辑。然而，这类系统本质上是辅助工具，人类仍需负责记忆、验证和执行关键操作。AWE则追求完全自主的端到端操作。

**自主多智能体渗透测试框架**：如AutoPT、AutoAttacker、CAI以及更先进的MAPTA。它们通过多智能体编排实现了一定程度的自动化，但通常依赖通用推理模型，缺乏用于跟踪认证状态、过滤器行为或历史有效载荷的**持久化记忆**，而这些对于复杂的注入攻击至关重要。MAPTA是该领域的重要进展，它采用三角色多智能体架构，结合了工具编排和证据门控的验证。AWE与MAPTA的关键区别在于：AWE并非通用探索型架构，而是将轻量级LLM编排层与**结构化的、针对特定漏洞的分析管道**深度耦合，并集成了上下文感知的有效载荷变异、生成以及浏览器验证的持久化记忆。这使得AWE在注入类漏洞上实现了更高的成功率、确定性和效率，而MAPTA则在更广泛的探索性测试中保有更高的整体覆盖率，两者体现了专用架构与通用架构的互补优势。

### Q3: 论文如何解决这个问题？

论文通过设计一个记忆增强的多智能体框架AWE来解决动态Web渗透测试中的适应性问题。其核心方法是将结构化的、针对特定漏洞的分析流程嵌入轻量级的LLM编排层，从而在加速的软件开发和有限的安全工具适应性之间架起桥梁。

整体框架分为三层：编排层、专用智能体层和基础层。编排层负责管理全局状态、协调智能体并执行预算约束，其核心是智能编排器，它收集侦察结果，评估不同漏洞类的可行性，并选择适当的智能体调用。专用智能体层包含针对不同漏洞类（如XSS、SQL注入、SSTI等）的独立利用模块，每个智能体将应用行为转化为漏洞特定的假设，并使用结构化流程进行测试。基础层提供共享基础设施，包括持久内存系统、浏览器验证引擎以及端点发现和参数提取等服务。

关键技术包括：1）上下文感知的负载突变和生成，结合持久内存和基于浏览器的验证，以产生确定性的、利用驱动的结果；2）智能体编码专家方法论到操作流程中，例如XSS智能体通过多阶段分析（包括并行探测注入、DOM上下文区分和服务器端过滤策略推断）来确保可预测和可重复的行为；3）持久内存系统结合短期扫描状态和长期跨目标学习，防止重复尝试并积累知识；4）浏览器验证引擎通过受控浏览器环境执行负载，观察脚本执行等具体信号，消除误报。

创新点在于：1）专业化而非通用推理，将细粒度利用实现为专用的状态机和推理流程；2）有状态和内存驱动的操作，维护跨多个请求的上下文；3）验证而非推测，每个发现都必须有具体证据支持。这些设计原则使AWE能够以高精度发现复杂Web漏洞，同时提高效率、降低成本和增强确定性。

### Q4: 论文做了哪些实验？

论文实验主要包括两部分：在DVWA上的受控模型对比实验和在XBOW基准上的大规模性能评估。实验设置上，AWE采用激进配置，每个挑战给予10分钟时间预算，使用Claude Sonnet 4作为底层模型，在隔离环境中运行并进行浏览器验证。对比方法为当前最强的公开自主渗透测试框架MAPTA（使用GPT-5）。

在DVWA数据集上，针对反射型XSS、存储型XSS、DOM型XSS、错误型SQL注入和时间型盲SQL注入五类漏洞，对比了Claude Sonnet 4、GPT-4o和Gemini 2.0 Flash三种模型。关键结果显示，Claude Sonnet 4在需要复杂推理的漏洞上表现最佳，例如在盲SQL注入上达到70%成功率（GPT-4o为60%，Gemini为55%），且收敛所需payload尝试次数最少（10-40次），比GPT-4o少约20%，比Gemini少约40%。

在包含104个挑战的XBOW基准测试中，AWE整体解决率为51.9%（54/104），虽低于MAPTA的76.9%（80/104），但在针对的注入类漏洞上优势明显：XSS成功率达87%（20/23），比MAPTA（57%）高30.5个百分点；盲SQL注入成功率达66.7%（2/3），比MAPTA（33.3%）高33.3个百分点。效率方面，AWE平均解决时间53.1秒，远快于MAPTA的190.8秒；总token消耗仅1.12M，比MAPTA的54.9M减少98%；总API成本为7.73美元，低于MAPTA的21.38美元。这些结果表明，即使使用中等模型，专业化架构在特定漏洞类别上能实现更高的准确性、效率和成本效益。

### Q5: 有什么可以进一步探索的点？

基于论文所述，AWE的局限性为未来研究提供了明确方向。首先，**扩展漏洞覆盖范围**是首要方向。当前系统专注于注入类漏洞，未来可探索如何将类似的“管道化”架构应用于业务逻辑漏洞、复杂身份验证流程或协议级攻击（如请求走私）。这可能需要设计新的、能够理解应用状态和会话上下文的智能体模块。

其次，**增强多步骤与协同攻击能力**是关键。AWE目前缺乏智能体间的协调以执行链式攻击（如发现默认凭证→利用IDOR→提权）。未来研究可以探索在轻量级编排层之上，引入更高层次的“战略规划”智能体，负责分解复杂任务并在专用智能体间传递上下文，从而平衡专业化与任务连贯性。

再者，**降低对启发式抽象和特定LLM的依赖**值得深入。论文指出其上下文和过滤器模型基于特定假设，可能无法适应高度定制或混淆的框架。未来可研究更自适应、基于少量示例或实时反馈就能学习应用特定模式的机制。同时，需构建更鲁棒的智能体架构，减少对单一模型版本或供应商的敏感度，例如通过抽象层或集成多模型来确保长期稳定性和成本可控。

最后，**验证与评估体系的拓展**也至关重要。需要在更复杂、动态的真实世界Web应用（而不仅是基准挑战）中测试此类系统，并建立包含攻击链成功率、资源消耗和可重复性的综合评估标准。

### Q6: 总结一下论文的主要内容

本文针对现代Web应用安全测试中传统模式扫描器适应性差、新兴LLM渗透测试工具成本高且行为不稳定的问题，提出了AWE框架。其核心贡献是设计了一个记忆增强的多智能体系统，将结构化的、针对特定漏洞的分析流程嵌入轻量级LLM编排层，而非依赖LLM进行无约束探索。方法上，AWE结合了上下文感知的载荷变异与生成、持久化记忆以及基于浏览器的验证，以实现确定性的漏洞利用。在XBOW基准测试中，AWE在注入类漏洞（如XSS和盲SQL注入）上取得了显著高于通用系统MAPTA的成功率，同时速度更快、成本更低、令牌使用更高效。主要结论表明，将LLM集成到有原则的、感知漏洞的专用流程中，其架构设计与模型推理能力同等重要，能在准确性、效率和确定性上带来巨大提升，为自动化Web安全分析迈向实用化提供了新方向。
