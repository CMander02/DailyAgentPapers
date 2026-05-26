---
title: "Memory-Induced Tool-Drift in LLM Agents"
authors:
  - "Mahavir Dabas"
  - "Jihyun Jeong"
  - "Ming Jin"
  - "Ruoxi Jia"
date: "2026-05-24"
arxiv_id: "2605.24941"
arxiv_url: "https://arxiv.org/abs/2605.24941"
pdf_url: "https://arxiv.org/pdf/2605.24941v1"
categories:
  - "cs.CR"
  - "cs.LG"
tags:
  - "LLM Agent安全"
  - "Agent记忆系统"
  - "工具使用"
  - "模型鲁棒性"
  - "Agent评测基准"
  - "多智能体安全"
  - "对抗攻击"
  - "生产系统Agent"
relevance_score: 9.5
---

# Memory-Induced Tool-Drift in LLM Agents

## 原始摘要

Modern LLM agents combine long-term memory for personalization with tool-calling interfaces for taking actions in the world -- a combination underpinning contemporary production systems. We study a previously unexamined failure of this combination: when personality-driven biases stored in memory (cost-consciousness, impatience, risk tolerance, etc.) silently affect tool calls in contexts where they are not applicable. We call this memory-induced tool-drift and operationalize it through MEMDRIFT, a benchmark of 105 scenarios spanning five bias dimensions and seven professional domains, generated through an automated adversarial pipeline. Across seven frontier models -- including those with extended reasoning -- biased memories raise deflection scores (a judge-scored measure of parameter deviation from unbiased baselines) by up to $+3.6$ points on a 1--5 scale. Tool-drift persists when memory management is handled by three production memory architectures. The phenomenon affects real-world tools: scanning 6{,}062 tools across 288 verified MCP servers, we flag 608 with susceptible parameters and confirm tool-drift on a validated subset. Mechanistically, biased memories act as implicit steering vectors, pushing activations along the same latent directions as explicit behavioral instructions. They also redistribute attention from task-relevant context toward memory entries with surface-level keyword overlap to the target parameter. Standard defenses -- prompt-based relevance instructions and memory filters -- reduce drift but do not eliminate it. As agents take increasingly consequential actions on a user's behalf, memory-induced tool-drift represents a systematic vulnerability that current safeguards do not address, motivating dedicated defenses at the intersection of memory management and tool-call generation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文研究的是现代LLM智能体中一个此前未被探索的安全漏洞：记忆引发的工具漂移（memory-induced tool-drift）。研究背景是，当前生产级LLM智能体（如OpenAI Codex、Claude Code等）通常将长期记忆（用于个性化）与工具调用（用于执行外部动作）两大能力结合使用。然而，现有研究往往将这两者分开考量：记忆研究关注回忆准确性和一致性，工具使用研究关注选择准确性、模式合规性和多步规划，仅有少量工作研究了“有益”的记忆使用（如从用户画像推断缺失工具参数），或开始关注对话情境中的过度个性化问题。本文指出现有方法的不足在于：对于工具调用场景中，存储在记忆中的个性驱动偏见（如成本意识、不耐烦、风险承受能力等）在不适用的上下文中静默影响工具参数选择这一失败模式，尚未被研究过。而这一场景比对话场景更具后果性，因为工具调用通常不会经过用户对每个参数的检查，且可能是不可逆的。因此，本文要解决的核心问题是：当智能体在专业领域（如医疗、金融、法律等）执行工具调用任务时，存储于长期记忆中的、来自个人生活的偏见性记忆（如消费习惯、风险偏好等）是否会无意中泄露到工具参数的选择中，造成参数偏差。作者通过构建MEMDRIFT基准（105个场景、5个偏见维度、7个专业领域）来系统化度量这一现象，并证实其在多个前沿模型和实际工具生态中普遍存在。

### Q2: 有哪些相关研究？

相关研究可按三类组织：**方法类**聚焦LLM工具使用，如从早期自监督API调用发展到基于MCP协议统一数万API的框架，并测试工具选择、参数正确性、多步规划与安全性（如ToolBench、SwiftSage），但未关注长期用户记忆中无关上下文对工具调用参数的潜在影响；**应用类**关注持久化记忆，包括参数化方法（将偏好编码至权重）与检索式架构（推理时注入存储上下文），评估集中于回忆保真度与一致性，近期工作研究模型如何从用户画像推断缺失参数（个性化工具调用），或对话中过度个性化问题；**评测类**则缺乏针对记忆诱发工具漂移的专门基准。本文的独特贡献在于首次系统研究无关记忆偏差（如成本意识、急迫性等五种维度）如何通过隐式影响工具参数（如跳过验证、降级SSL），导致参数偏离无偏基线高达+3.6分（1-5分制），即使工具选择与模式合规正确（区别于现有工作）。机制上，偏差记忆作为隐式操纵向量，推动激活沿显式行为指令相同方向演化，并导致注意力从任务相关上下文向表层关键字匹配的记忆条目重新分配。标准防御（提示相关性指令、记忆过滤器）仅部分缓解此系统性漏洞，与现有记忆管理或工具调用安全研究形成互补。

### Q3: 论文如何解决这个问题？

论文通过系统性的基准测试和机制分析，揭示了记忆诱导的工具漂移（Memory-Induced Tool-Drift）现象。核心方法是构建MEMDRIFT基准，包含105个跨5个偏见维度和7个专业领域的场景，通过自动化对抗性管道生成，确保所有记忆与专业任务无关，从而隔离偏见影响。方法论上，设计了三个对照条件：无记忆、中性记忆和偏见记忆，通过计算偏移分数（deflection score）量化偏见记忆导致的参数偏离程度。架构上，先进行直接记忆注入测试，再评估三种生产级记忆架构（Mem0、MemPalace、SimpleMem）下的表现，结果显示所有前沿模型均存在显著漂移。关键技术包括：1）利用LLM驱动的自改进对抗管道生成高难度测试场景；2）开发基于LLM的评委系统对工具调用进行1-5分偏移评分；3）对6082个真实MCP工具进行漏洞扫描，识别出608个易感参数，并通过验证子集确认了实际影响。创新点在于：首先正式定义并操作化了工具漂移现象；其次揭示了偏见记忆作为隐式操纵向量的机制，会沿着与显式行为指令相同的潜在方向推动激活，并将注意力从任务相关内容重分布到与参数存在表层关键词重叠的记忆条目；最后指出标准防御（提示指令、记忆过滤器）只能减轻但不能消除该问题，系统性地暴露了当前安全机制的盲区。

### Q4: 论文做了哪些实验？

论文做了三组实验。**实验设置**上，采用直接记忆注入和三个生产级记忆框架（Mem0、MemPalace、SimpleMem）两种方式，在105个涵盖5个偏差维度和7个专业领域的MEMDRIFT基准测试上进行。**对比方法**包括无记忆、中性记忆和偏差记忆三种条件，评估模型在工具调用参数上的偏移程度。**主要结果**：在直接注入下，所有7个前沿模型（GPT-5.2、GPT-5.4、Claude-Sonnet-4.5、Gemini-2.5-Pro、Gemini-3.1-Pro-Preview、Kimi-K2.5、Qwen3.5-397B-A17B）均表现出显著的工具漂移，偏差偏移分数（1-5量表）提升高达+3.6分，中性记忆的偏移分数保持低位。在记忆框架设置下，偏差偏移分数与直接注入相当甚至更高。此外，对288个MCP服务器中的6062个真实工具进行扫描，识别出608个易受影响的参数，并在验证子集上确认了漂移现象。敏感性分析表明，即使少量偏差记忆也能引发近最大漂移。标准防御措施（提示和记忆过滤器）能减少但无法消除漂移。

### Q5: 有什么可以进一步探索的点？

论文揭示了内存诱导工具偏离这一系统性漏洞，但现有防御措施仍存在显著局限。未来探索可从以下方向展开：首先，在训练阶段引入对抗性数据，如MEMDRIFT风格的数据集，通过后训练显式惩罚过度个性化，培养模型对上下文无关记忆的判别能力，并验证其对未见过偏置维度的泛化性。其次，现有相关性过滤器在跨域多跳推理场景下召回率仅61%，需开发更精细的上下文感知过滤机制，例如结合图神经网络捕捉记忆与任务间的隐式关联。此外，可探索混合防御策略：将提示约束与动态记忆重要性加权相结合，利用注意力分布监控实时修正参数偏移。最后，从机械论视角看，偏置记忆作为隐式转向向量改变注意力分配，未来可设计正交化记忆表示，抑制任务无关特征对工具参数的影响，从而从根本上阻断漂移路径。

### Q6: 总结一下论文的主要内容

这篇论文提出并系统研究了LLM智能体中“记忆诱导的工具漂移”问题。该问题指智能体长期记忆中的个性化偏见（如成本意识、风险容忍度等）在调用工具时，会无声地影响参数选择，从而导致在不适用的专业场景中产生偏差。为研究此问题，作者构建了MEMDRIFT基准，包含105个场景，覆盖5种偏见维度和7个专业领域。实验表明，在7个前沿模型中，偏见记忆能使参数偏离得分（1-5分制）增加高达3.6分。通过扫描288个MCP服务器的6062个工具，他们识别出608个易受影响参数。机制分析发现，偏见记忆作为隐式引导向量，通过词汇重叠劫持注意力，从而影响激活方向。现有防御措施（如提示相关性指令和记忆过滤器）虽能减少但无法消除漂移。这项研究揭示了当前记忆管理与工具调用机制结合时存在的系统性漏洞。
