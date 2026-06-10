---
title: "MemVenom: Triggered Poisoning of Multimodal Memories in Web Agents"
authors:
  - "Yv Zhang"
  - "Hao Sun"
  - "Hao Fang"
  - "Kuofeng Gao"
  - "Fan Mo"
  - "Bin Chen"
  - "Shu-Tao Xia"
  - "Yaowei Wang"
date: "2026-06-09"
arxiv_id: "2606.10742"
arxiv_url: "https://arxiv.org/abs/2606.10742"
pdf_url: "https://arxiv.org/pdf/2606.10742v1"
categories:
  - "cs.CR"
  - "cs.LG"
tags:
  - "Web Agent"
  - "安全攻击"
  - "记忆中毒"
  - "多模态"
  - "黑盒攻击"
  - "外部记忆"
relevance_score: 8.5
---

# MemVenom: Triggered Poisoning of Multimodal Memories in Web Agents

## 原始摘要

External memory has become a core component of modern web agents, enabling long-horizon reasoning through the retrieval of past experiences. However, this paradigm introduces a critical vulnerability: malicious content injected into memory can be persistently recalled and repeatedly influence agent behavior. In this work, we identify and systematically study multimodal memory poisoning, an overlooked yet practical attack surface in web-agent systems. We propose MemVenom, a unified black-box attack framework that poisons graph-structured external memory with coordinated text-image evidence. Our method consists of a two-stage design: (1) a trigger-conditioned retrieval attack that ensures high-probability recall of malicious memory, and (2) a post-retrieval attack induction that leverages adversarial perturbations and stealthy OCR injection to override the original user objective. Unlike prior attacks that operate on prompts or text-only memory, our approach enables persistent, reusable, and goal-agnostic attacks without modifying model parameters or re-optimizing malicious tasks. Experiments across multiple web-agent frameworks and vision-language models demonstrate that MemVenom achieves strong end-to-end attack success with minimal impact on benign performance, reaching up to 99.15% on GPT-5-family web agents, while transferring effectively across architectures and model scales.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多模态Web智能体外部记忆系统中存在的安全漏洞问题。研究背景是，现代Web智能体依赖外部记忆系统存储过往经验以支持长周期推理任务，但现有研究主要关注提示注入、越狱攻击或纯文本记忆投毒，忽视了多模态记忆（包含图像和文本证据）面临的安全威胁。当前方法的不足在于：记忆条目具有持久性，一旦写入可被反复检索并持续影响智能体决策，而现有攻击仅作用于临时输入上下文或假设纯文本记忆，无法有效应对真实场景中基于截图和图形化记忆的Web智能体。本文要解决的核心问题是：如何在黑盒条件下（无法修改模型参数或内部检索机制）实现多模态记忆投毒，通过注入带触发条件的恶意图文证据，使其在特定观测下被高概率检索，并在检索后诱导智能体以覆盖原始用户目标。具体而言，需要同时优化恶意记忆的召回概率和召回后的行为操控效果，且攻击需具有持久性、可复用性和模型无关性。

### Q2: 有哪些相关研究？

本文相关工作分为三类：**记忆增强型Web智能体**、**红队测试与攻击**、**检索与记忆投毒**。

1. **记忆增强型Web智能体**：现有工作（如使用LLM/VLM的智能体）通过外部记忆或检索模块存储观察、用户偏好与任务经验，以支持长程决策。本文指出，这些记忆并非被动存储，而是被整合到智能体的观察-推理-执行循环中，构成安全关键组件，从而识别了记忆投毒这一被忽视的攻击面。

2. **红队测试与攻击**：已有研究探索提示注入、越狱攻击、恶意工具调用和环境操纵等安全风险。这些攻击通常作用于当前输入上下文或即时环境，效果局限于特定交互实例。而本文提出的MemVenom是一种持久性记忆级攻击：投毒记忆在良性观察下保持静默，仅当触发载体出现时才激活恶意诱导，实现跨实例的复用性。

3. **检索与记忆投毒**：RAG系统和基于记忆的语言模型易受语料投毒、后门触发和恶意记忆注入攻击。但这些工作多针对纯文本RAG或语言模型。本文创新性在于：将其扩展至**多模态、记忆增强的Web智能体**，此场景下检索查询为截图等多模态观测，记忆包含视觉与文本证据，且攻击效果需体现为可执行的Web动作而非仅文本响应。因此，MemVenom需联合优化恶意检索与检索后操作诱导，填补了多模态记忆投毒的研究空白。

### Q3: 论文如何解决这个问题？

MemVenom提出了一种针对Web Agent多模态记忆体的黑盒投毒攻击框架,采用两阶段设计:第一阶段构建触发条件检索攻击,第二阶段构建检索后诱导攻击。在检索攻击阶段,首先在干净网页截图上叠加视觉触发,通过紧凑性损失(使触发样本在嵌入空间形成紧密聚类)、分离损失(将触发样本与干净样本在嵌入空间分开)和空间分离损失(减少与良性记忆空间的交叠)三个优化目标,获得最优触发和代表触发截图作为记忆节点。在检索后诱导阶段,通过桥接引导的对抗扰动在基图上叠加L∞受限的噪声,使其与优先级指令对齐;再通过隐写OCR注入将优先级指令文字嵌入图像,形成优先级提示组件。最后将这三个组件(检索组件、目标组件、优先级组件)组装成恶意记忆子图注入到原始记忆图中,其中目标组件可替换以实现不同恶意目标。该方法无需修改模型参数或重优化恶意任务,在GPT-5家族Web Agent上达到99.15%的攻击成功率。

### Q4: 论文做了哪些实验？

论文在三个多模态web-agent框架（SeeAct、LiteWebAgent和ReAct-WebAgent）上评估了MemVenom，使用多个VLM骨干（Qwen3-VL-4B/8B、Qwen3-VL-PLUS和GPT-5.4）。数据集采用SeeAct任务集，覆盖10类真实网站，每个良性任务配对四个OWASP类别的恶意子任务（钓鱼/重定向、隐私泄露、金融操作、数据破坏）。外部记忆实现为基于Qdrant和Kuzu的多模态图记忆。

主要实验结果：MemVenom在端到端攻击成功率（ASR-ra）上达到最高99.15%（GPT-5.4在SeeAct上的钓鱼任务）。对比方法中，Adapted AgentPoison在ASR-r上接近但ASR-ra较低（如Qwen3-VL-8B上74.28% vs 93.97%），CPA和BadChain表现更差。消融实验证实两阶段设计都必要：无检索组件时ASR-ra降至0，无优先级组件时ASR-a从97.65%降至76.47%。防御测试中，LlamaGuard将SeeAct的ASR-ra从93.97%降至75.89%，ReAct上从80.15%降至50.71%，但未消除威胁。跨检索器迁移显示良好转移性。良性任务效用（PU）与基线（BU）相当（如SeeAct上PU 11.76%-11.76% vs BU 11.76%-17.65%）。

### Q5: 有什么可以进一步探索的点？

首先，本文的攻击场景主要基于沙盒环境和截图检索的图结构记忆，未来可探索更真实的异构记忆管道，如工具特定记忆或用户画像记忆，这些系统的检索策略和约束条件可能改变攻击的生效条件。其次，当前防御评估仅涉及轻量级防护，需设计联合推理记忆来源、检索一致性与动作后果的强健防御机制，例如引入记忆溯源验证或任务对齐检查，以识别文本和图像的协调污染。此外，攻击依赖于预设计扰动和注入，可研究对抗性训练或自适应记忆筛选来提升模型鲁棒性。还可探索跨注意力层的记忆融合检测，或利用多模态一致性约束来瓦解恶意证据的协同效应。最后，考虑攻击的隐蔽性与时效性平衡，动态记忆更新可能降低持久性，未来可研究结合遗忘机制的自愈代理，以抵御此类污染威胁。

### Q6: 总结一下论文的主要内容

这篇论文聚焦于多模态记忆中毒攻击，针对现代网页代理中外部记忆组件的安全漏洞。问题定义为：攻击者可向外部记忆注入恶意内容，这些内容能被持续召回并反复影响代理行为。方法上，论文提出 MemVenom 框架，一种黑盒攻击方案，采用两阶段设计：首先通过触发条件检索攻击确保恶意记忆被高概率召回，随后利用对抗性扰动和隐蔽OCR注入诱导代理偏离原始用户目标。核心贡献在于揭示了外部记忆是安全关键组件，MemVenom 无需修改模型参数或重优化恶意任务即可实现持久、可复用且目标无关的攻击。主要结论表明，该攻击在多个网页代理框架和视觉语言模型上高效，在GPT-5系列代理上成功率高达99.15%，且具有良好的可迁移性和隐蔽性，对良性性能影响极小，为未来记忆感知防御研究提供了重要基础。
