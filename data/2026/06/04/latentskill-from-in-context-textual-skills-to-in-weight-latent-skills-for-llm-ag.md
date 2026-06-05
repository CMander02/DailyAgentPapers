---
title: "LatentSkill: From In-Context Textual Skills to In-Weight Latent Skills for LLM Agents"
authors:
  - "Aofan Yu"
  - "Chenyu Zhou"
  - "Tianyi Xu"
  - "Zihan Guo"
  - "Rong Shan"
  - "Zhihui Fu"
  - "Jun Wang"
  - "Weiwen Liu"
  - "Yong Yu"
  - "Weinan Zhang"
  - "Jianghao Lin"
date: "2026-06-04"
arxiv_id: "2606.06087"
arxiv_url: "https://arxiv.org/abs/2606.06087"
pdf_url: "https://arxiv.org/pdf/2606.06087v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent架构"
  - "技能学习"
  - "LoRA适配器"
  - "模块化Agent"
  - "上下文压缩"
  - "Agent效率"
  - "知识注入"
relevance_score: 9.0
---

# LatentSkill: From In-Context Textual Skills to In-Weight Latent Skills for LLM Agents

## 原始摘要

Agent systems increasingly use textual skills to encode reusable task procedures, but injecting these skills into the prompt at every step incurs substantial context overhead and exposes skill content as plaintext. We present LatentSkill, a framework that converts textual skills into plug-and-play LoRA adapters through a pretrained hypernetwork. LatentSkill stores skill knowledge in weight space rather than context space, removing per-step skill tokens while preserving modular loading, scaling, and composition. On ALFWorld and Search-QA, LatentSkill outperforms the corresponding in-context skill baseline while using substantially fewer prefill tokens: it improves ALFWorld success by 21.4 and 13.4 points on the seen and unseen splits with 64.1% fewer prefill tokens, and improves Search-QA exact match by 3.0 points with 72.2% lower skill-token overhead. Further analysis shows that generated skill LoRAs form a structured semantic geometry, can be precisely controlled via the LoRA scaling coefficient, and can be composed through parameter-space arithmetic when skill components are aligned. These findings suggest that weight-space skills provide an efficient, modular, and less exposed substrate for extending LLM agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文针对大型语言模型（LLM）智能体系统中，将可复用的过程性知识以文本技能形式注入提示（prompt）所带来的两大核心问题：显著的计算开销和隐私暴露风险。现有方法通常将技能文本直接插入每一决策步的提示中，这导致预填充（prefill）token数随交互步数线性增长，极大增加了推理成本，同时技能作为明文暴露在提示中，可能泄露专有知识。虽然参数化方法（如微调）可避免文本注入，但其将多个技能融合到模型参数中，导致技能难以被单独更新、移除或组合，失去了模块性。因此，现有方法面临一个“三难困境”：如何在不重复注入技能文本的前提下，依然保持技能的模块化加载与灵活组合能力。本文提出的LatentSkill框架旨在解决这一困境。其核心思想是通过一个预训练的超网络，将文本技能描述转换为即插即用的LoRA适配器，从而将技能知识从上下文空间迁移到权重空间。这样，在推理时提示中不再包含技能文本token，大幅降低预填充开销和隐私暴露，同时生成的LoRA适配器保持了模块化特性，支持独立加载、缩放和组合，实现了在避免重复文本开销的同时，维持技能的模块性与可组合性。

### Q2: 有哪些相关研究？

主要相关研究包括以下几个类别：

1. **基于上下文的技能方法**：早期工作如存储原始轨迹或反思摘要到外部记忆库，在推理时检索到上下文中。后续工作将技能作为核心抽象，包括为具身代理构建可执行技能库、通过递归强化学习形成分层SkillBank，以及将交互经验提炼为可复用的战略原则。工业界如Anthropic的Agent Skills规范被Claude Code、Cursor等采用。以上方法都将技能作为自然语言文本注入上下文窗口，本文的核心区别在于将技能编码为LoRA模块，消除了上下文开销。

2. **参数内化技能方法**：部分工作通过训练时课程逐步撤销技能上下文，使模型在推理时无需技能文本即可执行。但技能被不可逆地融合进主干模型，失去了模块化灵活性。本文通过将技能编码为独立于主干的LoRA适配器，同时实现了零上下文开销和即插即用的灵活性。

3. **超网络生成LoRA方法**：超网络通过单独学习的网络为目标网络生成权重。Text-to-LoRA用小型MLP逐层生成权重片段但缺乏跨层依赖；Generative Adapter利用主干隐藏状态产生LoRA权重但参数开销限制覆盖范围；ICAE压缩上下文为紧凑令牌再生成LoRA但受信息瓶颈限制；SHINE提取每层记忆状态但未分析生成LoRA权重的内在结构；Doc-to-LoRA通过感知器编码器生成适配器。本文首次系统性地揭示了超网络生成的LoRA权重空间具有结构性、可控性和可组合性，是首个针对代理技能编码场景进行这些性质分析的工作。

### Q3: 论文如何解决这个问题？

LatentSkill通过超网络将文本技能转换为可插拔的LoRA适配器，实现技能知识从上下文空间到权重空间的迁移。整体框架分为四个部分：首先是**潜在技能定义**，使用技能编译器Gφ将文本技能文档s映射为LoRA更新集Δ_s，每个目标模块m的更新遵循标准LoRA形式ΔW_s^{(m)}=B_s^{(m)}A_s^{(m)}，通过缩放因子α控制注入强度，使得冻结的骨干LLM仅依赖任务历史进行预测。

其次是**文档级预训练**，在包含N个技能文档的语料库D_pre上训练编译器。设计两种预训练任务：重构任务中编译器读取完整文档，适配后骨干网络需重建原文；补全任务中使用截断前缀，迫使适配器编码完整技能信息。预训练目标为生成适配器下输出z_i的负对数似然，仅更新编译器参数φ，确保信息通过适配器传递而非直接输入。

然后是**轨迹监督微调**，使用教师代理轨迹集D_sft={（s_i,τ_i）}监督训练。编译器为每个技能文档生成单独适配器Δ_i^{sft}，并贯穿整个轨迹共享使用。微调目标为预测教师输出y_{i,t}^*的负对数似然，鼓励适配器捕获跨步骤一致的技能级策略信息，而非单步适应。

最后是**推理时控制与组合**，技能编译与代理执行分离：预先编译技能库并缓存适配器。运行时通过选择器选择相关技能，支持两种组合方式：参数空间算术直接叠加多技能适配器，以及组件级组合将技能分解为语义组件后独立编译并加权组合。创新点在于将技能知识压缩为权重空间的低秩更新，消除每步提示中的技能令牌开销，同时保持模块化加载、缩放和组合能力，形成结构化语义几何结构并支持精确控制。

### Q4: 论文做了哪些实验？

论文在 ALFWorld 和 Search-QA 两个基准上评估了 LatentSkill。实验设置采用 Qwen3-8B 作为冻结骨干模型，技能编译器基于 Transformer 超网络，预训练阶段使用约 171K GitHub 技能文档（约 300M tokens），SFT 阶段使用 5 个 ALFWorld 技能和 3 个 Search-QA 技能。对比方法包括 Vanilla、Few-shot、Reflexion、AdaPlanner、RAG、In-context Skill 等。主要结果：在 ALFWorld 上，LatentSkill 在 seen 和 unseen 分片上分别达到 74.3% 和 69.4% 的平均成功率，比 In-context Skill 提升 21.4 和 13.4 个百分点，同时预填充 token 减少 64.1%；在 Search-QA 上，平均精确匹配（EM）达到 35.6，比 In-context Skill 提升 3.0 分，技能 token 开销降低 72.2%。此外，还进行了技能 LoRA 权重的 MDS 结构分析、注入系数 α（0-1.2）的可控性实验（呈倒 U 形曲线），以及通过 Component Merging 进行技能组合（在 Seen 和 Unseen 分片分别达到 84.6% 和 77.8%）。

### Q5: 有什么可以进一步探索的点？

论文在ALFWorld和Search-QA上的评估覆盖了具身交互和搜索增强问答，但未涉及网页浏览、软件工程、多智能体协作等更广泛的Agent部署场景，框架的通用性和可扩展性有待验证。所有实验均基于Qwen3-8B固定骨干模型和单一LoRA配置，未探索不同模型家族、模型规模或适配器配置对技能编译器行为及生成的隐式技能属性的影响。未来可沿三个方向深入：一是扩展至更多任务类型和动态环境，检验隐式技能的跨任务迁移与泛化能力；二是研究如何实现技能LoRA的自动化组合与冲突消解，以支持复杂任务分解；三是探索技能空间的语义可解释性，例如通过可视化或干预手段理解隐式技能的内在逻辑，并开发相应的安全对齐机制，防止技能泄露或误用。

### Q6: 总结一下论文的主要内容

LatentSkill提出了一种将文本技能转化为LoRA适配器的框架，通过预训练的超网络将技能知识从上下文空间转移到权重空间。该方法解决了现有智能体系统将技能文本注入提示时带来的大量上下文开销和内容暴露问题。在ALFWorld和Search-QA两个基准上，LatentSkill相比基线方法显著提升了任务性能：在ALFWorld的未见和已见分割上分别提升21.4和13.4个成功率点，同时节省64.1%的前置填充令牌；在Search-QA上实现了3.0个精确匹配点提升，降低了72.2%的技能令牌开销。进一步分析表明，生成的技能LoRA具有结构化语义几何特性，可通过缩放系数精确控制，并能在技能组件对齐时通过参数空间算术进行组合。该工作证明了权重空间技能是一种高效、模块化且暴露度更低的LLM智能体扩展方式。
