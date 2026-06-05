---
title: "TAPO: Tool-Aware Policy Optimization via Credit Transfer for Multimodal Search Agents"
authors:
  - "Chengqi Dong"
  - "Chuhuai Yue"
  - "Hang He"
  - "yandong liu"
  - "Fenghe Tang"
  - "S Kevin Zhou"
  - "Xiaohan Wang"
  - "Jiajun Chai"
  - "Guojun Yin"
date: "2026-06-04"
arxiv_id: "2606.05784"
arxiv_url: "https://arxiv.org/abs/2606.05784"
pdf_url: "https://arxiv.org/pdf/2606.05784v1"
categories:
  - "cs.AI"
tags:
  - "工具增强型Agent"
  - "多模态搜索Agent"
  - "Agent训练方法"
  - "GRPO改进"
  - "信用分配"
  - "强化学习"
relevance_score: 9.5
---

# TAPO: Tool-Aware Policy Optimization via Credit Transfer for Multimodal Search Agents

## 原始摘要

We identify and formally characterize credit misassignment as a systematic failure mode of GRPO in tool-augmented multimodal search agents: its uniform broadcast of trajectory-level advantages to all tokens causes valuable tool-use steps in failing trajectories to be penalized no differently from valueless ones. We further empirically quantify the scale of this phenomenon. Over half of failing trajectories and failing tool-use actions exhibit correctable credit misassignment, demonstrating that the wasted training signal is both substantial and structurally exploitable. Building on this insight, we propose Tool-Aware Policy Optimization (TAPO), which exploits the parameter-determinism property of information-acquisition tools: similar call parameters define equivalent information-acquisition actions and should therefore share comparable action credit. TAPO constructs counterfactual witnesses within the current training batch and compensates misassigned negative credit via confidence-gated conservative advantage correction. It requires no additional annotation, models, or sampling, and introduces negligible computational overhead. Across multiple multimodal search benchmarks, TAPO delivers consistent, plug-and-play improvements over strong baselines for three mainstream RL algorithms (GRPO, GSPO, and SAPO). Our code and models will be publicly released upon acceptance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于组的强化学习算法（如GRPO）在训练工具增强型多模态搜索智能体时的信用错误分配问题。研究背景是，智能体强化学习已成为训练能迭代调用外部工具（如图像搜索、文本搜索等）的多模态智能体的主流范式，其中GRPO因省略价值网络而在结果监督任务上表现优异。然而，现有方法的不足在于，GRPO将轨迹级别的优势值均匀地广播到所有令牌（token），这隐式假设每个生成步骤的贡献相等，但在需要多步工具调用的场景中，不同工具调用具有不同的信息价值，导致该假设系统性失效。具体表现为，在相同训练步内，具有相同参数的工具调用在成功和失败轨迹中分别获得正负相反的优势信号，产生相互矛盾的优化。论文通过实证量化发现，超过一半的失败轨迹及失败工具调用步骤存在可纠正的信用错误分配，表明浪费的训练信号不仅规模巨大，且具有结构性可挖掘性。核心问题是，如何在不引入额外标注、模型或采样成本的前提下，纠正这种信用错误分配，从而提升工具增强型搜索智能体的训练效率和性能。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及两类工作。第一类是**多模态搜索智能体**，包括MMSearch-R1、WebWatcher、DeepEyesV2、SenseNova-MARS、Vision-DeepSearch和MTA-Agent等。这些方法通过设计图像搜索/文本搜索工具或图像处理工具构建多步骤推理系统，但仅关注整体性能提升，忽视了多步工具使用中固有的信用分配问题。本文与它们的区别在于，首次识别并形式化了信用错误分配这一系统性问题，并提出针对性解决方案。第二类是**智能体强化学习中的细粒度信用分配**，包括基于PRM的方法、步骤级采样方法（成本高且精度无法保证），以及更轻量的替代方案如GiGPO（通过状态分组构建步骤奖励）、HCAPO和Belief-RL（分别通过事后概率偏移和信念估计评估步骤质量）。然而，这些方法主要针对文本领域的工具集成推理，且都将工具使用步骤视为普通生成步骤。本文的关键区别在于，利用信息获取工具的**参数确定性**特性，提出TAPO方法，通过构建反事实样本并进行置信度门控的保守优势校正，在不增加额外标注、模型或采样开销的情况下，解决了多模态搜索智能体中的信用错误分配问题。

### Q3: 论文如何解决这个问题？

TAPO针对GRPO在工具增强的多模态搜索智能体中存在的信用错配问题，提出了一种基于参数确定性假设的信用转移机制。其核心方法如下：首先，TAPO利用信息获取工具的“参数确定性”特性，即相似调用参数定义等价的信息获取动作，应共享相近的动作信用。基于此，TAPO在当前训练批次内构建“反事实见证”：将成功轨迹中相同工具类型且参数等价的工具使用步骤聚类成参考组，并计算每个组的参考优势（基于GRPO标准化的优势聚合）。然后，对于失败轨迹中的每个工具使用步骤，TAPO通过最大参数相似度匹配到最相似的参考组。若匹配度超过阈值θ，则进行信用转移。信用转移函数结合了参数匹配度、参考组覆盖率（成功轨迹中包含该组的比例）以及参考优势。通过置信度门控（α_min和θ两级过滤），只有高置信度的转移才被应用。最终，对失败步骤的负优势进行保守校正：将原始负优势加上一个受限的正向转移信号（由系数β控制），并截断至0，以保留整体优化方向。TAPO无需额外标注、模型或采样，计算开销极小，可作为GRPO、GSPO和SAPO等算法的即插即用模块，显著提升多模态搜索性能。

### Q4: 论文做了哪些实验？

论文在多个多模态搜索基准上进行了全面实验。实验设置：使用 VeRL 框架，不经过 SFT 预热，全局批量大小为 128，学习率 1×10⁻⁶，每个问题生成 8 条轨迹，约 4K 训练样本。工具设置包括图像搜索、文本搜索和区域放大三种类型。数据集：在 MMSearch、HR-MMSearch、FVQA-test、InfoSeek、SimpleVQA、LiveVQA 和 MAT-Search 七个基准上评估。对比方法：包括闭源模型 (GPT-5、Gemini 3)、开源模型 (Qwen3-VL) 和搜索代理 (DeepEyesV2、WebWatcher、SenseNova-MARS) 以及 GRPO、GSPO、SAPO 等强化学习基线。主要结果：TAPO 在所有基准上持续提升，例如在 Qwen3-VL-4B 基础上，TAPO (β=0.8) 平均准确率从 49.06% 提升至 61.18%，相对 GRPO 提升 8.74%。转移系数 β 消融实验显示 TAPO 在 β=0.8 时最优，且对所有 β 值均优于 GRPO。组件消融表明移除支持因子 (w/o sup.) 导致平均准确率下降 4.71%，移除保守裁剪 (w/o clip.) 导致训练不稳定。TAPO 还缓解了熵坍塌，维持了探索行为，并逆转了响应长度和工具调用频率的下降趋势。计算开销极小，仅占训练总时间的 0.06%（每步不到 1 秒）。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于其核心假设——工具调用参数决定信息获取动作——可能不适用于非参数确定性工具（如生成式工具或参数模糊的工具）。未来可探索：1) 将TAPO扩展到更复杂的组合工具链场景，其中多个工具的交互会导致信用归属更模糊；2) 研究动态β调整机制，避免固定的门限在训练后期造成过校正；3) 改进反事实构造策略，当前仅依赖同批次样本，可引入跨批次或缓存的历史轨迹来增强反事实多样性；4) 将信用转移与状态价值函数结合，对长序列中中间工具调用的信用进行更细粒度的时序分解。此外，可考虑用在线探索策略主动生成高信息量的反事实轨迹，从而进一步提升劣势轨迹中的可用信号利用率。

### Q6: 总结一下论文的主要内容

这篇论文针对工具增强的多模态搜索代理中GRPO算法的信用错误分配问题，即GRPO将所有token平等对待，导致失败轨迹中有价值的工具使用步骤也受到惩罚。作者发现，超过一半的失败轨迹中存在可纠正的信用错误分配，且参数相似的步骤在成功轨迹中可作为可靠的反事实参考信号。基于此，论文提出TAPO方法，利用信息获取工具的“参数确定性”特性，通过构建批次内成功轨迹的反事实参考库，评估参数相似性和覆盖度作为置信度，保守地修正被错误分配的负优势。TAPO无需额外标注、模型或采样，可作为插件式替换模块。在多个多模态搜索基准测试中，TAPO为GRPO、GSPO和SAPO三种主流强化学习算法带来一致且稳定的提升，且计算开销可忽略不计。
