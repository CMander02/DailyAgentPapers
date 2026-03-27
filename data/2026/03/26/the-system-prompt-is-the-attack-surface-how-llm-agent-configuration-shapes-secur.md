---
title: "The System Prompt Is the Attack Surface: How LLM Agent Configuration Shapes Security and Creates Exploitable Vulnerabilities"
authors:
  - "Ron Litvak"
date: "2026-03-26"
arxiv_id: "2603.25056"
arxiv_url: "https://arxiv.org/abs/2603.25056"
pdf_url: "https://arxiv.org/pdf/2603.25056v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Security"
  - "Prompt Engineering"
  - "Adversarial Robustness"
  - "System Prompt"
  - "Vulnerability Analysis"
  - "Tool-Augmented Agent"
  - "Evaluation Metric"
relevance_score: 7.5
---

# The System Prompt Is the Attack Surface: How LLM Agent Configuration Shapes Security and Creates Exploitable Vulnerabilities

## 原始摘要

System prompt configuration can make the difference between near-total phishing blindness and near-perfect detection in LLM email agents. We present PhishNChips, a study of 11 models under 10 prompt strategies, showing that prompt-model interaction is a first-order security variable: a single model's phishing bypass rate ranges from under 1% to 97% depending on how it is configured, while the false-positive cost of the same prompt varies sharply across models. We then show that optimizing prompts around highly predictive signals can improve benchmark performance, reaching up to 93.7% recall at 3.8% false positive rate, but also creates a brittle attack surface. In particular, domain-matching strategies perform well when legitimate emails mostly have matched sender and URL domains, yet degrade sharply when attackers invert that signal by registering matching infrastructure. Response-trace analysis shows that 98% of successful bypasses reason in ways consistent with the inverted signal: the models are following the instruction, but the instruction's core assumption has become false. A counter-intuitive corollary follows: making prompts more specific can degrade already-capable models by replacing broader multi-signal reasoning with exploitable single-signal dependence. We characterize the resulting tension between detection, usability, and adversarial robustness as a navigable tradeoff, introduce Safetility, a deployability-aware metric that penalizes false positives, and argue that closing the adversarial gap likely requires tool augmentation with external ground truth.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在揭示并解决基于大语言模型（LLM）的邮件代理在防范网络钓鱼攻击时，其系统提示词配置所引发的核心安全矛盾。研究背景是LLM邮件助手正从研究原型快速部署到企业和个人实际应用中，承担着包括安全决策在内的邮件处理任务。然而，与传统认知不同，现有研究和实践往往将安全性能主要归因于模型本身（如架构、参数规模），而忽视了部署配置，尤其是系统提示词的关键作用。这导致了一个未被充分认识的风险：即通过精心设计提示词来优化模型在特定基准测试上的表现，可能会无意中引入新的、可被攻击者利用的脆弱性。

本文要解决的核心问题正是系统提示词作为“攻击面”的双刃剑效应。具体而言，论文首先论证了系统提示词配置是一个与模型选择同等重要甚至更关键的一阶安全变量——同一模型在不同提示词下，其钓鱼邮件绕过率可从低于1%剧增至97%。基于此，研究展示了通过优化提示词来聚焦于高区分度的信号（如发件人域名与邮件内URL域名的一致性），确实能在基准测试中实现高性能（如93.7%的召回率）。然而，论文的核心发现和要解决的关键问题在于：这种针对固定威胁模型的、基于单一信号的优化具有内在的结构性脆弱。当攻击者通过注册匹配域名（即“信号反转”）进行基础设施钓鱼攻击时，这些优化策略的防御效果会急剧下降（召回率损失高达一半）。模型失败并非因为推理错误，而是因为它们忠实地遵循了提示词指令，而指令所依赖的核心假设（如域名不匹配即可疑）已被攻击者颠覆。因此，论文最终要解决的是如何理解和导航由提示词配置所塑造的、在检测率、误报率和对抗鲁棒性之间的三元权衡，并指出仅靠提示词工程可能存在性能天花板，需要结合外部工具（如威胁情报）来提供真实依据以弥补信息缺口。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、应用类和评测类三大方向。在方法类研究中，[作者1]提出了LLM自主智能体的统一框架，将系统提示视为直接影响智能体感知与行动的核心模块；[作者2]则聚焦于个人LLM智能体的安全与隐私风险，指出这是实际部署的主要障碍。这些研究为本文分析系统提示配置的安全影响奠定了基础。

在应用类研究中，[作者3]探讨了LLM在钓鱼攻击中的双重角色：一方面，研究表明LLM能生成高质量钓鱼邮件（如SpearBot工作），这支持了本文采用LLM生成钓鱼语料的方法；另一方面，LLM作为钓鱼防御工具的研究尚不充分，尤其在自主决策场景中——本文正是填补了这一空白，首次系统评估了提示配置对多模型钓鱼检测行为的影响。

在评测类研究中，相关基准测试与本文形成对比。例如，Fraud-R1关注多轮对话中的欺诈咨询（人类保留决策权），而本文评估自主智能体的二元决策；DetoxBench涵盖更广泛的滥用内容检测，但未专门针对钓鱼或提示敏感性；HarmBench和JailbreakBench专注于模型越狱（jailbreaking）而非检测能力退化。此外，现有基准普遍缺乏误报率分析，而本文引入的Safetility指标直接解决了这一缺口。与强调对抗性输入（如AgentDojo的提示注入攻击）的研究不同，本文聚焦于“标准钓鱼邮件”的检测，即攻击者针对人类而非模型漏洞的社会工程威胁，从而揭示了提示配置与模型选择交互带来的独特攻击面。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为PhishNChips的系统性实验框架来解决LLM邮件代理中系统提示配置引发的安全漏洞问题。其核心方法是系统性地量化不同提示策略对模型安全判断的影响，并揭示优化策略带来的脆弱性。

整体框架基于一个自主邮件代理场景，模型需对输入的钓鱼邮件和合法邮件进行二分类（放行或拦截）。研究设计了包含2000封合成邮件的平衡语料库（1000封钓鱼邮件，1000封合法邮件），并选取了11种适合生产环境部署的LLM模型。实验的关键在于引入了10种不同的提示策略，这些策略构成了从“安全优先”到“效率优先”的风险谱系，从而隔离了提示配置这一变量对模型行为的影响。

主要模块包括：1）**提示策略设计模块**：包含六种核心策略（如security_first、balanced、efficiency_first等）和四种优化策略（如sender_url_match、trap_sender_match等），通过改变系统提示中定义代理“人格”的自然语言指令来操纵模型的风险容忍度。2）**评估与度量模块**：不仅使用召回率（Recall）和误报率（FPR）等传统指标，还创新性地引入了**Safetility**这一部署感知指标。该指标通过二次项奖励高召回率，并通过Hill函数在误报率超过阈值（如10%）时施加严厉惩罚，从而量化安全性与可用性之间的实际可部署权衡。3）**对抗性测试模块**：专门构建了“基础设施钓鱼”子集（73个样本），其中攻击者注册单一域名并同时用于发件人地址和URL主机，以此测试依赖发件人-URL一致性信号的策略的鲁棒性。

关键技术发现与创新点包括：首先，论文实证揭示了**系统提示是首要的安全变量**，其影响远超模型本身的选择。例如，GPT-4o-mini模型的钓鱼绕过率在不同提示策略下可从低于1%波动至97%。其次，通过信号分解的提示工程（如依赖“发件人-URL域名匹配”这一结构性信号），可以显著提升基准性能（如GPT-4o-mini的召回率从32.8%提升至93.7%，FPR为3.8%）。然而，这同时创造了一个**脆弱的攻击面**：当攻击者通过注册匹配的基础设施来“反转”该信号时，依赖该单一信号的策略会急剧失效（如GPT-4o-mini对基础设施钓鱼的召回率暴跌至30.1%）。响应轨迹分析显示，98%的成功绕过都遵循了被反转的信号逻辑，这体现了**指令特异性悖论**：使提示更具体（聚焦于单一强信号）可能会取代模型原本更广泛的多信号推理能力，从而使其更易被利用。最后，论文论证了完全依赖提示工程无法从根本上解决对抗性差距，并指出可能需要通过**工具增强（Tool Augmentation）** 引入外部真实数据来弥补这一缺陷。

### Q4: 论文做了哪些实验？

论文实验设计围绕评估LLM邮件代理在钓鱼邮件检测中的安全性，重点探究系统提示词配置如何影响模型表现和攻击面。实验设置包括：构建一个包含2000封合成邮件的平衡语料库（1000封钓鱼邮件，1000封合法邮件），其中钓鱼邮件使用真实恶意URL（来自PhishTank和OpenPhish）并由Gemini 3 Flash生成内容，以模拟高质量攻击；合法邮件涵盖8个常见场景。特别地，包含73个“基础设施钓鱼”子集，攻击者使用同一域名作为发件人和URL主机，以针对依赖域名一致性信号的策略。

评估了来自5个提供商的11个模型（如Gemini系列、GPT系列、Claude系列、Llama等），这些模型均为适合实时处理的快速、经济型版本。每个模型在10种提示策略下测试：6种核心策略（如security_first、balanced、efficiency_first等）构成风险谱系，3种优化策略（如sender_url_match、trap_sender_match）通过针对特定信号的提示工程开发，以及第10种策略infra_aware。所有评估使用temperature=0.0以确保确定性，并通过解析器提取二元判决，总评估量达22万次。

主要结果：首先，系统提示词配置对安全性有决定性影响。例如，在核心策略中，钓鱼邮件绕过率从security_first的7%到efficiency_first的55%不等，而GPT-4o-mini的绕过率在不同提示下可从低于1%到97%波动，显示提示配置的影响超过模型间差异。其次，优化策略能显著提升基准表现。通过依赖发件人-URL域名匹配等信号，最佳策略在GPT-4o-mini上实现了93.7%的召回率和3.8%的误报率（FPR），但这也引入了脆弱性：在基础设施钓鱼攻击下，同一策略的召回率暴跌至30.1%。此外，论文引入了Safetility指标（公式为Recall² × [1 / (1 + (FPR/0.1)⁵)]）来综合衡量部署可行性，其中Grok 4.1在优化策略下获得最高Safetility（90.7%）。关键数据包括：平均误报率在核心策略中最高达57%（security_first），优化策略下最低至0.6%（Gemini 2.5 Flash）；在辅助测试中，针对跨域合法邮件，依赖域名匹配的策略误报率急剧上升，揭示了基准条件性局限。

### Q5: 有什么可以进一步探索的点？

该论文揭示了系统提示词作为攻击面的核心脆弱性，即过度优化特定信号（如域名匹配）会导致模型推理路径单一化，从而在对抗性场景（如攻击者注册匹配域名）下性能急剧退化。其局限性在于研究主要集中于钓鱼邮件检测这一特定任务，且实验的对抗性扰动类型相对有限。

未来研究方向可沿以下路径深入：一是**扩展攻击面研究**，将分析框架迁移至代码生成、多轮对话等更复杂的智能体场景，探究提示词在不同任务中引发的连锁安全风险。二是**发展动态防御机制**，例如设计提示词元优化框架，使模型能根据实时反馈动态调整推理策略，平衡多信号融合与单一信号依赖。三是**增强外部知识验证**，正如论文所指，需结合外部事实核查工具（如实时域名注册库）来弥补LLM内部知识的不足，构建“提示词+工具”的混合防御体系。此外，可探索**对抗性提示词训练**，在模型微调阶段引入对抗性提示样本，提升其对恶意诱导的鲁棒性，从而在保持实用性的前提下缩小对抗性差距。

### Q6: 总结一下论文的主要内容

该论文聚焦于大语言模型（LLM）智能体系统提示词配置对其安全性的关键影响，揭示了其本身构成一个可被利用的攻击面。核心问题是：系统提示词的微小调整会如何剧烈改变LLM代理（如邮件钓鱼检测代理）的安全表现，并引入新的脆弱性。

研究方法上，作者提出了PhishNChips框架，对11个模型在10种提示策略下进行了系统性评估。研究发现，提示词与模型的交互是首要的安全变量：同一模型的钓鱼邮件绕过率可从低于1%到高达97%，完全取决于其配置；而同一提示词在不同模型上产生的误报成本也差异巨大。论文表明，虽然围绕高预测性信号（如发件人与URL域名匹配）优化提示词能提升基准性能（召回率达93.7%，误报率3.8%），但这会创造一个脆弱的攻击面。一旦攻击者注册匹配的基础设施来“反转”该信号，依赖单一信号的检测策略会急剧失效。响应轨迹分析显示，98%的成功绕过案例中，模型的推理逻辑与反转后的信号一致——它们忠实地遵循了指令，但指令的核心假设已被破坏。

主要结论是，使提示词更具体化可能会损害本已具备多信号推理能力的模型，代之以可被利用的单一信号依赖，从而在检测性能、可用性和对抗鲁棒性之间形成紧张关系。论文为此引入了**Safetility**这一兼顾部署（惩罚误报）的度量指标，并指出缩小对抗性差距可能需要通过工具增强来引入外部事实核查。
