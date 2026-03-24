---
title: "SkillProbe: Security Auditing for Emerging Agent Skill Marketplaces via Multi-Agent Collaboration"
authors:
  - "Zihan Guo"
  - "Zhiyu Chen"
  - "Xiaohang Nie"
  - "Jianghao Lin"
  - "Yuanjian Zhou"
  - "Weinan Zhang"
date: "2026-03-22"
arxiv_id: "2603.21019"
arxiv_url: "https://arxiv.org/abs/2603.21019"
pdf_url: "https://arxiv.org/pdf/2603.21019v1"
categories:
  - "cs.CR"
  - "cs.SE"
tags:
  - "Agent Security"
  - "Multi-Agent Collaboration"
  - "Skill Marketplace"
  - "Security Auditing"
  - "Risk Assessment"
  - "Agent Governance"
relevance_score: 7.5
---

# SkillProbe: Security Auditing for Emerging Agent Skill Marketplaces via Multi-Agent Collaboration

## 原始摘要

With the rapid evolution of Large Language Model (LLM) agent ecosystems, centralized skill marketplaces have emerged as pivotal infrastructure for augmenting agent capabilities. However, these marketplaces face unprecedented security challenges, primarily stemming from semantic-behavioral inconsistency and inter-skill combinatorial risks, where individually benign skills induce malicious behaviors during collaborative invocation. To address these vulnerabilities, we propose SkillProbe, a multi-stage security auditing framework driven by multi-agent collaboration. SkillProbe introduces a "Skills-for-Skills" design paradigm, encapsulating auditing processes into standardized skill modules to drive specialized agents through a rigorous pipeline, including admission filtering, semantic-behavioral alignment detection, and combinatorial risk simulation. We conducted a large-scale evaluation using 8 mainstream LLM series across 2,500 real-world skills from ClawHub. Our results reveal a striking popularity-security paradox, where download volume is not a reliable proxy for security quality, as over 90% of high-popularity skills failed to pass rigorous auditing. Crucially, we discovered that high-risk skills form a single giant connected component within the risk-link dimension, demonstrating that cascaded risks are systemic rather than isolated occurrences. We hope that SkillProbe will inspire researchers to provide a scalable governance infrastructure for constructing a trustworthy Agentic Web. SkillProbe is accessible for public experience at skillhub.holosai.io.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体生态系统中，新兴的集中式技能市场所面临的新型安全威胁。随着OpenClaw等系统的发展，智能体通过封装了领域知识和执行逻辑的“技能”来增强能力，技能市场（如ClawHub）成为关键基础设施。然而，当前的安全防护机制存在明显不足。现有方法主要分为两类：一是侧重于实时干预的“智能体中心运行时治理”，例如通过提示工程进行防御，但难以应对深藏在技能逻辑内部的隐秘攻击；二是侧重于“技能中心静态分析”，例如大规模漏洞特征刻画，但通常局限于离散的代码模式或供应链完整性检查，无法有效应对智能体生态所特有的、横跨语义层与执行层的复合型威胁。

具体而言，本文要解决的核心问题是现有方法难以应对的两种新型安全挑战：1. **语义-行为不一致**：由于智能体严重依赖自然语言描述来检索和调用技能，恶意开发者可以发布语义描述合规但底层实现有害的技能，造成文档声明的“安全”属性与实际执行逻辑（如未授权访问、数据窃取）之间的严重脱节，这种偏差对用户和智能体而言几乎是不可见的。2. **技能间组合风险**：在智能体协作或并行调用多个技能的动态场景中，单独审计时良性的技能，在特定执行链中组合时可能诱发突发的协同攻击（例如，上游技能的误导性输出触发下游技能的高危行为）。这种由组合爆炸导致的动态关联风险，使得传统的原子级技能审计方法失效。为此，论文提出了SkillProbe框架，通过多智能体协作的多阶段安全审计，系统性地应对这些新兴漏洞。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及方法类、应用类和评测类等多个方面。在方法类中，早期研究包括对工具描述与代码一致性的检测，例如基于神经网络的即时注释一致性检查，以及近期基于LLM的代码分类和过滤方法。在API契约挖掘领域，DAInfer通过神经符号优化从文档推断API别名规范，DocFlow从自然语言文档提取污点规范，而RESTSpecIT利用LLM辅助的请求变异自动化RESTful API文档推断和黑盒测试。然而，这些方法均假设文档是善意编写的，目标在于保持代码与文档一致，而本文则关注文档本身作为攻击向量的逆向威胁模型。

在应用类研究中，针对技能市场的安全审计工作已有初步探索。例如，对31,132项技能的实证研究发现26.1%存在漏洞，后续对98,380项技能的行为验证确认了数据窃贼和代理劫持者两种攻击模式。ClawHub作为主要技能注册中心，部署了结合VirusTotal签名匹配和LLM辅助代码分析器的扫描管道，但该方法仅在代码层面进行事后反应式检测，无法验证技能文档是否真实反映其可执行行为，也无法模拟多技能组合时出现的风险。此外，间接提示注入研究（如InjecAgent和Skill-Inject）表明技能文件是有效的注入表面，而运行时防御（如高亮显示和输出过滤）虽能部分缓解，但存在固有的TOCTOU问题。

在评测类方面，现有基准如AgentDojo提供了组合攻击的红队评估，但仅适用于部署后场景，缺乏市场层面的准入控制。同时，多智能体系统（如AutoGen、MetaGPT和LangGraph）在安全任务中展现出角色专业化和并行任务分解的优势，但将其应用于技能市场审计会引入信任边界问题。本文提出的SkillProbe框架与这些工作的区别在于，它专注于在技能注册前检测语义行为不一致性和跨技能组合攻击链，并采用多智能体协作的“技能驱动技能”设计范式，通过标准化技能模块封装审计流程，从而系统性应对现有方法未能解决的组合风险和语义欺骗问题。

### Q3: 论文如何解决这个问题？

SkillProbe通过一个分层、模块化的多智能体协作安全审计框架来解决技能市场中的安全挑战。其核心方法是“以技能审计技能”（Skills-for-Skills）的设计范式，将审计过程封装为标准化的技能模块，驱动专门的智能体执行严格的安全检查流程。

**整体框架与主要模块：**
系统架构分为五层：
1.  **输入层**：负责接收和预处理审计目标，兼容本地目录、压缩包和远程URL等多种格式。
2.  **编排层**：作为中央调度枢纽，由专门的“安全审计员”智能体作为主导协调者，维护审计状态、分发任务，并按阶段顺序调度底层执行器。
3.  **技能层**：核心功能域，基于“以技能审计技能”范式集成了三个主要审计模块：
    *   **Gatekeeper（守门员）**：负责准入过滤，并行检查合规性、恶意代码模式、危险依赖（如含已知CVE的包）和权限声明的合理性。它采用“解耦检查、集中聚合”的架构，将现有安全工具封装为自治的“门执行器”进行并行审查，并遵循保守原则（任一环节“阻止”即全局阻止）。
    *   **Alignment Detector（一致性检测器）**：检测语义行为一致性。通过文档提取器和代码提取器并行工作，分别从自然语言文档和实际代码中提取能力声明集（D(s)）与实现能力集（C(s)），然后由标记代理进行语义归一化映射。最终通过一个四类对齐矩阵（匹配、过度声明、声明不足、混合偏差）来分类风险状态，识别影子功能和权限偏差。
    *   **Flow Simulator（流模拟器）**：分析组合风险。采用风险指纹标记方法，将搜索复杂度从指数级降至线性级。首先由风险分析代理推断输出风险标签和输入敏感度标签，然后通过双重预过滤机制（资源类型验证和结构约束）收敛搜索空间，最后基于风险链接策略执行批量攻击路径模拟（如命令注入、间接提示注入、数据窃取）。为确保真实性，引入了证据强制执行机制，要求智能体为每个发现的漏洞引用原始代码或文档片段。
4.  **输出层**：将审计结果合成为结构化安全报告，并生成多维安全记分卡。
5.  **基础设施层**：提供基础原子能力，包括工具注册表、用于存储审计指纹的持久化数据库和专用的智能体循环运行时环境。

**关键技术设计与创新点：**
1.  **“规范即代码”的模块化抽象**：将每个审计阶段抽象为标准化的技能包，包含自然语言规范、机器可读的工作流配置、系统提示和操作脚本。这使得审计过程被表示为基于有向无环图（DAG）的智能体协作流，实现了审计逻辑与核心框架引擎的解耦，显著增强了系统的可扩展性。
2.  **动态、自适应的执行编排**：安全审计员驱动多个通用智能体，支持三种自适应执行模式：标准串行处理、动态并发（用于实时扩展和对比任务）以及预计算并行（用于高吞吐量多处理）。这种设计将执行拓扑与任务逻辑解耦，通过通用原子能力和按需工具加载确保了高代码复用性和接口一致性。
3.  **双模式操作平衡效率与深度**：提供“快速模式”（串行执行Gatekeeper和Alignment Detector，用于高频初步筛查）和“标准模式”（所有阶段完全并行化，用于深度系统级安全评估），以平衡吞吐量和分析深度。
4.  **多维安全记分卡与严格裁决策略**：通过记分卡从三个关键维度（恶意模式、语义一致性、组合安全性）评估技能，并遵循严格的“一票否决”裁决策略，将技能分类为“拒绝”、“有条件通过”或“批准”。
5.  **面向大规模部署的实用化平台与工具**：开发了包含高性能后端、响应式Web界面、命令行界面和LLM集成插件的Holos-SkillHub平台。特别是引入了“对话即审计”范式的OpenClaw插件，允许用户在LLM环境中异步触发审计工作流，显著降低了智能体安全治理的入门门槛。

### Q4: 论文做了哪些实验？

论文实验主要包括三个部分：跨模型审计一致性评估、大规模技能安全审计以及风险链网络分析。

**实验设置与数据集**：实验基于真实世界技能平台ClawHub（数据截至2026年3月16日）的技能数据。评估使用了8个主流大语言模型系列作为推理引擎，包括高性能/代码专用模型（如Claude Sonnet 4.6、GPT-5.2-Codex）和高效/轻量模型（如Claude Haiku 4.5、GPT-5 mini）。SkillProbe采用标准模式运行，并定义了9种核心风险链路策略（如命令注入、间接提示注入、数据泄露等）来检测组合攻击。

**对比方法与主要结果**：
1.  **跨模型审计评估**：使用下载量前20的技能作为基准，在8个模型上进行审计（共160个样本）。结果显示模型间存在显著异质性：执行时间差异巨大（Gemini 3.1 Flash-Lite仅需18.5秒，Nex-N1.1需282.0秒）；安全阈值不同，Claude Sonnet 4.6的“有条件通过”率高达45%，是最严格的审计器，而GPT-5.2-Codex则更宽松（95%通过率）。热力图分析表明，对于高质量技能（如find-skills），模型间存在稳健共识；但对于某些技能（如nano-banana-pro），所有模型一致给出“有条件通过”判决，证实了系统性风险的可复现性。

2.  **大规模安全审计**：对ClawHub下载量前2500的技能进行深度扫描（主要使用Nex-N1模型）。结果揭示了严峻的安全现状：仅9.9%（247个）技能完全“清洁”（无任何发现）；59.8%通过基线审计但存在小缺陷；30.4%（759个）因违反安全规则被标记为“有条件通过”。这意味着超过90%的高人气技能未能通过严格的安全准入标准。关键发现是，风险比例在不同下载量层级间保持稳定（20%-35%），直接反驳了“流行度等于安全性”的直觉假设。

3.  **风险链网络分析**：针对499个确认存在至少一条风险链路的技能构建关联网络。网络包含75,373条风险边，其中数据窃取（32,328边）和事实污染（28,441边）占主导（共80%）。最关键的结构性发现是：所有高风险技能在风险维度上形成了一个**单一的完全连通组件**。这意味着攻击面具有乘数效应，一旦任意两个高风险技能在复杂任务中被组合调用，就可能通过共享的危险能力模式触发级联攻击，这证明了SkillProbe跨技能组合模拟阶段的必要性。

### Q5: 有什么可以进一步探索的点？

本文揭示了当前技能市场在安全审计上的多个关键局限，为未来研究指明了方向。首先，检测深度受限于基础大模型的理解能力，对于高度混淆的代码或黑盒API，现有方法可能失效，未来需探索结合符号执行或形式化验证的混合增强方案。其次，当前组合风险模拟依赖预定义策略，对未知的零日攻击模式存在盲区，可研究引入对抗性学习或异常检测，让审计框架能动态演化以识别新型威胁。再者，面对海量技能瞬时提交的场景，计算开销与审计严格性之间的平衡是一大挑战，未来需设计更高效的并行化算法或分层抽样审计机制。从更宏观的视角看，论文强调应从原子检测转向组合防御，这启示我们需构建能模拟复杂技能链交互的动态沙箱环境，并建立跨技能的风险传播图谱。此外，语义与行为的一致性审计尚处早期，如何量化“意图对齐”并建立标准化评估基准，是推动该领域发展的关键。最终，这些探索应汇聚于为智能体生态构建一个可扩展、自动化且多层次的治理基础设施。

### Q6: 总结一下论文的主要内容

本文针对大型语言模型（LLM）智能体生态中新兴的集中式技能市场，提出了其面临的两大核心安全挑战：语义-行为不一致性以及技能间组合风险（即单个良性技能在协同调用时可能引发恶意行为）。为应对这些漏洞，论文提出了SkillProbe，一个基于多智能体协作的多阶段安全审计框架。其核心贡献在于引入了“技能审计技能”的设计范式，将审计流程封装为标准化的技能模块，驱动专用智能体执行严格的审计流水线，包括准入筛选、语义-行为一致性检测和组合风险模拟。通过对ClawHub平台上2500个真实世界技能、横跨8个主流LLM系列的大规模评估，论文得出了两个关键结论：一是发现了流行度与安全性之间的显著悖论，超过90%的高流行度技能未能通过严格审计；二是揭示了高风险技能在风险链接维度上形成了一个单一的巨型连通分量，表明级联风险是系统性而非孤立现象。该研究的意义在于为构建可信的智能体网络提供了一个可扩展的治理基础设施原型。
