---
title: "VisualClaw: A Real-Time, Personalized Agent for the Physical World"
authors:
  - "Haoqin Tu"
  - "Jianwen Chen"
  - "Zijun Wang"
  - "Siwei Han"
  - "Juncheng Wu"
  - "Hardy Chen"
  - "Haonian Ji"
  - "Kaiwen Xiong"
  - "Jiaqi Liu"
  - "Peng Xia"
  - "Jieru Mei"
  - "Hongliang Fei"
  - "Jason Eshraghian"
  - "Zeyu Zheng"
  - "Yuyin Zhou"
  - "Huaxiu Yao"
  - "Cihang Xie"
date: "2026-06-15"
arxiv_id: "2606.16295"
arxiv_url: "https://arxiv.org/abs/2606.16295"
pdf_url: "https://arxiv.org/pdf/2606.16295v1"
categories:
  - "cs.CV"
  - "cs.CL"
tags:
  - "Agent架构"
  - "多模态Agent"
  - "实时Agent"
  - "视频理解Agent"
  - "Agent自我进化"
  - "工具使用Agent"
  - "Agent基准测试"
  - "成本优化"
relevance_score: 8.5
---

# VisualClaw: A Real-Time, Personalized Agent for the Physical World

## 原始摘要

Vision language models are serving as general-purpose interfaces for complex multimodal tasks. However, deployment still faces three gaps: VLMs typically incur high latency and cost when processing dense video frames and long prompts, the agent scaffold remains static after deployment, and standard video-QA benchmarks do not test whether agents can use visual evidence inside tool-using workspaces. We present VisualClaw, a self-evolving multimodal agent built around two principles. First, hybrid encoding reduces deployment cost by filtering less informative streaming frames with a cascaded gate and compressing the text skill bank through hot/cold top-k injection. Second, skill evolution lets the agent learn from failures: retrieved memories condition an evolver as direct concatenated context or as guided evidence, producing skill-bank updates that help future questions. Across 4 video-QA benchmarks with 2 VLMs, VisualClaw cuts per-question API cost by an average -98% versus full-frame upload and by -25.9% over the offline uniform 8 frame baseline, while boosting accuracy in most settings, e.g., an average +3.85% and a peak +15.80% on EgoSchema with Gemini 3 Flash. To address the gap, we curate VisualClawArena, a 200-scenario multimodal agentic benchmark built through a strict five-stage pipeline; models must use video evidence, documents, dynamic updates, and executable checks inside a workspace. On VisualClawArena, the same framework with computer-use agent backends improves macro accuracy by +2.9% for Codex (GPT-5.5) and +3.2% for Claude Code (Sonnet 4.6) over no-evolution baselines, with a -9.5% cost reduction compared to the uniform-sampled baseline. These properties make VisualClaw a natural fit for edge applications, where the cascade reduces a 1-hour streaming session from ~3,600 API uploads down to only 5-20 calls and the self-evolution makes it a perfect personalized assistant.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决将视觉语言模型（VLM）部署为实际物理世界智能体时存在的三大核心差距。首先，现有VLMs在部署时面临高昂的延迟和成本，因为处理密集的视频帧流和不断增长的提示词（如技能库）会消耗大量计算资源。其次，当前智能体的框架在部署后是静态的，无法从自身的失败中学习并自我进化，缺乏持续适应和个性化的能力。最后，现有的标准视频问答（Video-QA）基准测试主要评估静态视频中的一次性回答，无法衡量智能体在需要使用工具的复杂工作区（如文件操作、视频证据与文档核对、执行检查）中利用视觉证据的能力。针对这些不足，本文提出了VisualClaw，一个围绕两个核心原则构建的自我进化多模态智能体：一是通过混合编码降低部署成本，利用级联门控过滤非信息性帧并压缩技能库；二是通过从失败中学习来实现技能进化，更新技能库以提升未来问题的处理能力。核心问题是实现一个实时、个性化且能适应物理世界工具使用场景的视觉智能体。

### Q2: 有哪些相关研究？

### 相关研究

本文的相关工作可归为以下几类：

1. **基于技能与记忆增强的智能体**：如Reflexion、Voyager、ExpeL、Agent-KB等，通过可复用技能库或外部记忆提升性能，但技能库是静态的。本文的VisualClaw通过技能演化和热/冷注入实现动态维护，并冻结模型权重，区别于MetaClaw结合RL训练的方式。

2. **持续学习与元学习**：如RL²、PEARL、ProMP等，关注快速适应新任务，但通常用于低维动作空间。VisualClaw将元学习思想引入LLM智能体，通过支持/查询分离和版本控制协议处理视频QA失败蒸馏，类似MetaClaw的结构但用于视频任务。

3. **高效视频VLM**：多数方法如LLoVi、MovieChat、VideoAgent等依赖LLM选择帧或离线访问完整视频。VisualClaw的级联门控选择器是唯一在边缘设备上逐帧实时决定、且不依赖LLM的选择方法，同时支持技能库演变。

4. **视频QA基准**：包括EgoSchema、EgoPlan-Bench、Video-MME等。VisualClaw提出VisualClawArena，专门测试智能体在工作空间中利用视频证据、文档、动态更新和可执行检查的能力。

### Q3: 论文如何解决这个问题？

VisualClaw通过三时间尺度协同设计解决部署中的高延迟、高成本和静态架构问题。其核心是混合编码与元进化两大原则。整体框架包含三个主要模块：

**1. 边缘端级联视觉门控（G）**：对每帧进行O(1)复杂度处理，无需GPU。首先通过感知哈希去重，再用轻量128维编码器（HSV直方图、亮度、边缘密度等）生成场景向量，最后通过自适应变化门输出major（上传）、minor（更新参考但不上传）、skip三档判定。这使1小时流媒体从约3600次API调用降至5-20次。

**2. 热/冷技能注入器（S）**：技能库以Markdown卡片形式存储程序化规则和反模式。对于每个问题，通过句子嵌入检索，将top-k个技能热注入到系统提示中（作为主体），其余技能以名称-描述对的冷目录形式附上（按需获取）。这使单次查询成本与技能库规模解耦。

**3. 记忆增强的进化器（E）**：每次会话中，当累积N_evo个失败时，进化器从置信度门控的片段记忆库M_v检索相关成功案例。提供两种注入方式：直接拼接（Cat.）将记忆作为额外上下文；引导式（Guide）添加前缀指示进化器提取可复用技能。新技能经过token-Jaccard去重和效用追踪器过滤后加入技能库。

创新点包括：三时间尺度协同（帧级/问题级/会话级）实现自进化；将记忆增强应用于低频率的进化过程而非高频推理；以及设计专用基准VisualClawArena验证工具使用场景中的视觉证据利用能力。

### Q4: 论文做了哪些实验？

论文进行了一系列实验评估VisualClaw框架。实验设置分为静态视频问答和多模态智能体基准测试（VisualClawArena）两类任务。静态视频问答使用Gemini 3 Flash和GPT-5.2作为冻结骨干模型，在EgoSchema（500实例，平均3分钟片段）、EgoPlan-Bench（923条目）、Video-MME long（900实例，30分钟以上视频）和NextQA（1000实例，约30秒视频）四个基准上测试。对比方法包括Plain（均匀采样8帧）、Seed、+Evolve、+SkillMemCat以及两种完整记忆演化变体（Cat.和Guide）。主要结果显示，Cascade编码中Guide变体平均比Plain基线提升3.85%，在EgoSchema上Gemini 3 Flash达到峰值提升15.80%（从52.60%到68.40%）。将完整演化应用于离线均匀8帧基线，额外带来3.50%到13.00%的提升，EgoSchema上达到73.60%。在VisualClawArena（200个场景，共3106轮指令）上，使用Codex和Claude Code作为工具使用后端，对比有无演化（Cat./Guide）和均匀8帧基线。Codex后端中Cascade (Cat.) 宏准确率54.27%，比无演化基线提升2.9%，Claude Code后端提升3.2%，同时成本比均匀采样降低9.5%。Cascade-fill实验表明在匹配8帧预算下，场景变化关键帧比均匀采样帧携带更多信号。

### Q5: 有什么可以进一步探索的点？

1.  **任务复杂度扩展**：当前系统主要基于视频QA进行演变，未来可探索支持多模态工具调用、动态工作流编排和跨会话长期记忆，以处理更复杂的真实世界任务。

2.  **演进机制深度**：目前的“skill evolution”依赖检索到的记忆，未来可引入强化学习主动探索失败案例，或采用协作式多智能体框架，让不同Agent分工改进技能库。

3.  **效率与保真度平衡**：级联门控虽大幅降低API调用，但在高动态场景（如快速动作）可能丢失关键帧，可尝试自适应采样策略（如基于光流或注意力）与轻量级帧插值重建。

4.  **安全与公平性**：自演进可能导致技能库偏差累积，需加入用户监督回滚机制、遗忘功能，并设计对抗性测试确保不学习有害行为。

5.  **边缘部署优化**：当前侧重API成本，未来可探索端侧VLM蒸馏、离线缓存热技能及隐私保护下的边缘-云端联合推理方案。

### Q6: 总结一下论文的主要内容

VisualClaw 提出了一种自演进的实时多模态智能体框架，旨在解决视觉语言模型（VLM）在部署中遇到的三个核心痛点：高延迟/成本、静态智能体架构无法适应失败、以及缺乏评估工具使用场景的基准。该方法采用混合编码策略，通过级联门控过滤低信息帧并将技能库分为“热/冷”两层注入，大幅降低了 API 成本（相比全帧上传降低约 98%）。同时，智能体利用记忆增强的演进器从失败中学习，动态更新技能库。在 4 个视频问答基准上，该方法平均提升准确率 3.85%，最高达 15.80%。此外，作者构建了包含 200 个场景的多模态智能体基准 VisualClawArena，在该基准上两个代理后端在技能演进后宏平均准确率分别提升 2.9% 和 3.2%，且成本降低 9.5%。实验表明，该混合编码与自演进机制不仅提升了静态视频问答性能，也增强了工作空间式智能体的工具使用能力，且兼容冻结的 VLM 骨干，适合边缘设备上的个性化实时部署。
