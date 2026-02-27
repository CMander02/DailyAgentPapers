---
title: "OmniGAIA: Towards Native Omni-Modal AI Agents"
authors:
  - "Xiaoxi Li"
  - "Wenxiang Jiao"
  - "Jiarui Jin"
  - "Shijian Wang"
  - "Guanting Dong"
  - "Jiajie Jin"
  - "Hao Wang"
  - "Yinuo Wang"
  - "Ji-Rong Wen"
  - "Yuan Lu"
  - "Zhicheng Dou"
date: "2026-02-26"
arxiv_id: "2602.22897"
arxiv_url: "https://arxiv.org/abs/2602.22897"
pdf_url: "https://arxiv.org/pdf/2602.22897v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.CV"
  - "cs.LG"
  - "cs.MM"
tags:
  - "Agent 架构"
  - "多模态 Agent"
  - "Agent 评测/基准"
  - "工具使用"
  - "推理"
  - "Agent 数据合成"
  - "Agent 训练"
relevance_score: 9.5
---

# OmniGAIA: Towards Native Omni-Modal AI Agents

## 原始摘要

Human intelligence naturally intertwines omni-modal perception -- spanning vision, audio, and language -- with complex reasoning and tool usage to interact with the world. However, current multi-modal LLMs are primarily confined to bi-modal interactions (e.g., vision-language), lacking the unified cognitive capabilities required for general AI assistants. To bridge this gap, we introduce OmniGAIA, a comprehensive benchmark designed to evaluate omni-modal agents on tasks necessitating deep reasoning and multi-turn tool execution across video, audio, and image modalities. Constructed via a novel omni-modal event graph approach, OmniGAIA synthesizes complex, multi-hop queries derived from real-world data that require cross-modal reasoning and external tool integration. Furthermore, we propose OmniAtlas, a native omni-modal foundation agent under tool-integrated reasoning paradigm with active omni-modal perception. Trained on trajectories synthesized via a hindsight-guided tree exploration strategy and OmniDPO for fine-grained error correction, OmniAtlas effectively enhances the tool-use capabilities of existing open-source models. This work marks a step towards next-generation native omni-modal AI assistants for real-world scenarios.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前多模态大语言模型（MLLMs）在迈向通用人工智能助手时面临的核心瓶颈：缺乏真正的全模态（Omni-Modal）感知与复杂推理、工具使用深度融合的能力。研究背景是，人类智能天然地融合了视觉、听觉、语言等多种模态的感知，并结合长程推理和工具使用来理解和改造世界。然而，现有的多模态研究大多局限于双模态交互（如视觉-语言或音频-语言），这限制了模型处理现实世界中交织在一起的多种信息源的能力。尽管已出现一些统一多种模态的基础模型，但它们主要侧重于感知能力，而将工具整合、主动式推理的智能体（Agent）能力探索不足。同时，现有的评测基准也大多是双模态、以感知为中心的，无法充分衡量需要跨模态多跳推理、多轮次调用外部工具并生成可验证开放答案的复杂任务。

因此，本文的核心问题是：如何推动AI智能体从双模态迈向真正的“原生全模态”智能体，即能够像人类一样，无缝整合视频、音频、图像等多种模态信息，进行深度推理，并主动使用工具来解决问题。为解决此问题，论文提出了两个主要贡献：一是构建了OmniGAIA评测基准，它通过一种新颖的全模态事件图方法，从真实世界数据中合成需要跨模态推理和工具整合的复杂多跳查询任务，以全面评估智能体的上述能力；二是提出了OmniAtlas，一个遵循工具集成推理范式的原生全模态基础智能体，它支持主动的全模态感知（有选择地关注长媒体中的片段），并通过后见之明引导的树探索和OmniDPO细粒度纠错等训练方法，有效提升了现有开源模型在复杂任务上的工具使用和推理能力。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**基础模型方法**、**评测基准**和**智能体范式**。

在**基础模型方法**方面，现有研究致力于将文本、视觉和音频统一到单一的大语言模型（LLM）主干中，主流方法是采用统一的标记化与投影接口，将异构的视觉和听觉输入映射到共享的标记空间。本文提出的OmniAtlas模型属于此类，但强调其是首个在工具集成推理范式下、具备主动全模态感知能力的“原生”全模态基础智能体，旨在原生融合音频、视觉和语言进行长程推理，这与之前主要关注双模态（如视觉-语言）或短序列感知的模型有显著区别。

在**评测基准**方面，已有工作如OmniBench、WorldSense等，但它们大多侧重于短音频/视频和以感知为中心的任务。本文构建的OmniGAIA基准则填补了空白，专注于评估需要**深度推理**和**多轮工具执行**的复杂、长视野任务，其查询通过全模态事件图方法合成，要求跨模态推理和外部工具集成。

在**智能体范式**方面，LLM驱动的自主智能体通过外部工具进行推理和行动，现有方法主要分为基于工作流的范式和原生智能体推理方法，且多在纯文本任务上表现良好。近期研究开始探索视觉-语言智能体。本文的工作属于智能体范式，但将范围扩展到了全模态（视频、音频、图像），并专注于解决长视野的智能体推理这一尚未充分探索的问题。

### Q3: 论文如何解决这个问题？

论文通过提出OmniAtlas这一原生全模态基础智能体来解决现有开源模型在全模态感知和工具集成推理方面的不足。其核心方法是一个集成了训练、优化和架构设计的完整方案。

整体框架上，OmniAtlas采用工具集成推理范式，将视觉、音频和语言感知与长程推理、自主工具使用统一起来。智能体的交互轨迹被形式化定义为一系列“思维-行动-观察”三元组。模型根据交互历史生成下一步的推理思维和行动（工具调用或最终响应）。当检测到工具调用令牌时，生成暂停，执行相应工具，并将返回的观察结果追加到上下文中，使模型能够继续推理。这种设计保留了中间推理状态，支持连贯的长程问题求解。

关键技术包括：1）**主动全模态感知**：为解决长视频或高分辨率图像直接输入带来的令牌爆炸和细节丢失问题，OmniAtlas支持智能体通过特定操作（如`read_video`、`read_audio`、`read_image`）主动请求所需的特定片段或区域，实现“按需查看”的感知，避免了粗暴的下采样。2）**高质量轨迹合成与训练**：通过两阶段流水线合成训练数据：首先使用Gemini-3-Flash将原始多模态输入转化为详细文本描述；然后采用**后见之明引导的树探索**策略，利用DeepSeek-V3.2生成工具增强的解决方案轨迹。该策略在每一步采样多个候选延续，并使用基于真实答案的验证器（Gemini-3-Flash）来剪除错误或冗余分支，仅保留成功的轨迹用于训练。3）**掩码监督微调**：在轨迹级监督微调中，采用掩码监督，仅对智能体生成的令牌（推理和工具调用令牌）计算损失，而屏蔽工具观察令牌，防止模型记忆环境反馈噪声，专注于学习如何思考和行动。4）**细粒度错误校正（OmniDPO）**：针对全模态任务中感知、推理、工具使用等多能力紧密耦合、SFT难以纠正细粒度错误的问题，提出OmniDPO。该方法在训练集上让SFT模型进行探索，对于每个失败轨迹，利用Gemini-3-Flash（可访问标注解法和答案）识别第一个错误步骤并生成纠正后的前缀，从而在每次优化中专注于纠正单个错误。优化时采用掩码DPO目标，且仅针对智能体生成的令牌计算概率，将校正聚焦于出现错误的特定模块。

创新点在于：提出了一个统一感知、推理与工具使用的原生全模态智能体架构；设计了主动感知机制以高效处理高负荷多模态输入；开发了后见之明引导的树探索策略来合成高质量的复杂任务解决轨迹；并引入了针对多模态智能体细粒度错误的OmniDPO优化方法，显著提升了现有开源模型在复杂全模态任务上的工具使用和推理能力。

### Q4: 论文做了哪些实验？

论文在OmniGAIA基准上进行了全面的实验评估。实验设置方面，采用基于DeepSeek-V3.2的LLM-as-a-Judge方法评估答案等价性，报告Pass@1指标，并为所有模型提供相同的外部工具（包括网络搜索、浏览器和代码执行器）。评估的数据集是论文提出的OmniGAIA基准，该基准包含需要跨视频、音频和图像模态进行深度推理和多轮工具执行的复杂任务。

对比方法包括专有模型（Gemini-2.5-[Flash-Lite, Pro]和Gemini-3-[Flash, Pro]）和开源模型（如Qwen2.5-Omni-[3B,7B]、Qwen3-Omni-30B-A3B-Thinking、Baichuan-Omni-1.5等）。论文提出的方法OmniAtlas（包含SFT和OmniDPO训练阶段）也在多个骨干模型上进行了评估。

主要结果和关键指标如下：
1.  **性能差距**：最优专有模型Gemini-3-Pro在OmniGAIA上达到62.5 Pass@1，而最强开源基线Qwen-3-Omni仅为13.3，存在约4.7倍的巨大差距。
2.  **模型规模局限性**：仅增加参数规模收益递减，例如560B的LongCat-Flash-Omni（11.1）性能低于30B的Qwen-3-Omni（13.3）。
3.  **OmniAtlas的有效性**：OmniAtlas显著提升了骨干模型的性能，例如将Qwen-3-Omni从13.3提升至20.8（+7.5）。在较小模型上提升更显著，如Qwen-2.5-Omni-7B从3.6提升至13.3（约3.7倍）。
4.  **任务难度影响**：所有模型在困难任务上性能均大幅下降，例如Gemini-3-Pro在简单、中等、困难任务上的Pass@1分别为78.7、未明确值、38.5。
5.  **错误分析**：工具使用无效和推理错误是主要失败模式（分别占35.3%–91.9%和15.8%–79.7%）。OmniAtlas有效降低了工具误用率（如Qwen-3-Omni-30B从81.1%降至59.4%）和推理错误率（从79.7%降至64.4%），但感知错误（视觉约30%，音频约31.9%）仍是瓶颈。
6.  **工具使用分析**：外部工具不可或缺，但过多工具调用（>10-20次）并不保证成功，可能伴随低效探索。OmniAtlas促使模型从工具调用不足转向更主动的使用。
7.  **原生感知与工具感知对比**：对于强模型（如Gemini-3-Flash），原生感知性能最优（平均51.7），且工具调用次数更少（4.4次）；使用感知工具会降低性能并增加调用成本。对于弱模型，感知工具有助于提升简单和中等任务性能，但会损害困难任务性能。
8.  **训练方法贡献**：OmniAtlas-SFT贡献了主要性能增益，OmniDPO则进一步带来全面提升（如Qwen-3-Omni-30B性能从13.3经SFT提升至18.9，再经DPO提升至20.8）。

### Q5: 有什么可以进一步探索的点？

基于论文内容，未来研究可从以下几个方向深入探索。首先，论文指出当前模型在长程推理和工具使用方面仍是瓶颈，而非单纯参数扩展。因此，可进一步研究如何通过**全模态智能体强化学习（Omni-modal Agentic RL）**，直接优化智能体在复杂多模态反馈下的长期决策策略，提升其主动感知与规划能力。其次，**全模态MCP服务（Omni-modal MCP Services）** 的构建值得关注，即开发可扩展的工具集以支持更广泛的全模态任务，例如动态集成视频、音频和图像处理工具，增强智能体的实际应用灵活性。最后，论文提到向**全模态具身智能体（Omni-modal Embodied Agents）** 发展，未来可创建物理世界中的基准与基础模型，使AI助手能更好地理解并操作真实环境，例如在机器人或交互系统中实现多模态感知与行动的统一。此外，结合个人见解，模型在跨模态证据对齐和错误修正方面仍有局限，未来可探索更高效的轨迹合成方法，或引入因果推理机制来减少多跳查询中的累积误差。

### Q6: 总结一下论文的主要内容

该论文针对当前多模态大语言模型局限于双模态交互（如视觉-语言）而缺乏统一认知能力的问题，提出了面向原生全模态AI智能体的研究框架。核心贡献包括：首先，构建了OmniGAIA基准，通过一种新颖的全模态事件图方法，基于真实世界数据合成需要跨模态推理和多轮工具执行的复杂任务，以评估智能体在视频、音频和图像模态上的深度推理与工具使用能力。其次，提出了OmniAtlas——一个在工具集成推理范式下具有主动全模态感知能力的原生全模态基础智能体。该方法采用后见之引导的树探索策略合成训练轨迹，并结合OmniDPO进行细粒度错误修正，有效提升了现有开源模型的工具使用性能。这项工作的意义在于推动了面向真实场景的下一代原生全模态AI助手的发展，为实现更接近人类智能的、融合感知、推理与工具使用的统一认知能力迈出了重要一步。
