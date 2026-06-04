---
title: "MIRAGE: Mobile Agents with Implicit Reasoning and Generative World Models"
authors:
  - "Zhichao Yang"
  - "Yuanze Hu"
  - "Haojie Hao"
  - "Longkun Hao"
  - "Dongshuo Huang"
  - "Hongyu Lin"
  - "Gen Li"
  - "Lanqing Hong"
  - "Yihang Lou"
  - "Yan Bai"
date: "2026-06-03"
arxiv_id: "2606.04627"
arxiv_url: "https://arxiv.org/abs/2606.04627"
pdf_url: "https://arxiv.org/pdf/2606.04627v1"
categories:
  - "cs.AI"
tags:
  - "mobile agent"
  - "latent reasoning"
  - "world model"
  - "implicit reasoning"
  - "GUI agent"
  - "screenshot-based control"
  - "efficient inference"
relevance_score: 9.5
---

# MIRAGE: Mobile Agents with Implicit Reasoning and Generative World Models

## 原始摘要

Mobile agents are increasingly expected to operate everyday applications from screenshots and language goals, where reliable control requires reasoning over screen affordances, multi-step navigation, and future state changes. However, many agents externalize this computation as long textual chains of thought, which slows interaction, increases supervision cost, and complicates deployment. We introduce MIRAGE, a framework that learns continuous latent reasoning representations from visible textual reasoning traces. MIRAGE transfers explicit reasoning into compact hidden states, enabling the agent to reason internally without decoding long rationales. It also incorporates a generative world-model objective: latent reasoning vectors are aligned with future screenshots, encouraging the agent to anticipate upcoming interface states before acting. This turns hidden computation into both a compressed thought representation and a forward-looking model of environment dynamics. At inference time, MIRAGE reasons in continuous latent space, reducing token generation while improving execution efficiency. On AndroidWorld, MIRAGE matches explicit chain-of-thought supervised fine-tuning in the 4B ablation with a 3-5x lower decoded-token budget and improves a comparable instruction-tuned baseline by 10.2 points; on AndroidControl, it improves action grounding while generating over 75% fewer tokens.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决移动GUI代理在视觉-语言模型应用中面临的核心困境：如何在不牺牲推理能力的前提下，降低交互延迟和部署成本。现有方法如UI-TARS、MAI-UI等通常依赖显式的思维链（CoT）进行导航推理，即通过冗长的文本Token序列来描述屏幕状态、操作理由和预期变化。虽然这种方式提升了决策可靠性，但也带来了严重问题：解码时间长、上下文预算消耗大、需要大量人工标注的中间推理轨迹，在实时交互场景中严重影响用户体验。

本文提出的MIRAGE框架旨在打破这一权衡。其核心创新在于将显式推理过程转化为连续的潜在空间表示，使代理能够“内部思考”而无需解码冗长的中间文本。具体来说，MIRAGE通过两阶段训练：先让模型学习显式推理轨迹，再通过近似并行潜在细化（APLR）技术将推理压缩至隐空间，并引入生成式世界模型（Q-Former）将隐状态与未来屏幕截图特征对齐。这样既保留了CoT的多步推理能力，又将解码Token量减少75%以上（如AndroidControl上），同时提升任务成功率——在AndroidWorld上4B模型相比指令微调基线提升10.2个百分点，且性能匹配显式CoT但推理成本降至1/3~1/5。

### Q2: 有哪些相关研究？

相关研究可分为三类：**移动和GUI智能体**方面，现有工作从网页交互演进到动态Android控制（如AndroidWorld、AndroidControl基准），通过VLM进行截图定位、GUI动作和移动设备操作。本文区别于这些方法的思路，不扩展定位或规划管线，而是用对未来GUI状态具有预测性的潜在槽替换可见推理轨迹来训练内部智能体状态。

**语言和视觉语言智能体中的推理**方面，可见的CoT和ReAct范式虽提升推理和行动能力，但产生冗长推理过程和上下文消耗。其他工作通过暂停令牌、私有思考、蒸馏或连续潜在CoT内化计算。本文创新地将隐式推理引入移动GUI控制，利用潜在思考支持动作选择和转换理解，并采用APLR在严格因果三角系统中近似序列潜在精炼（而非均衡模型）。

**世界模型和视觉特征预测**方面，世界模型从紧凑潜在模拟器到潜在想象智能体学习预测性动力学。联合嵌入视觉目标显示特征预测无需像素生成即可学习语义，Q-Former查询提供轻量跨注意力瓶颈。近期GUI世界模型预测未来屏幕、草图或语义状态。本文不同之处在于利用未来预测塑造潜在推理状态，在推理时无需生成像素或未来文本，而是鼓励由动作引发的转换表示。

### Q3: 论文如何解决这个问题？

MIRAGE提出了一种将显式推理隐式化的框架，核心思想是用连续隐变量替代文本推理链。整体框架包含两阶段训练：第一阶段使用结构化显式思维模板（包含观察、推理、预测三个字段）对VLM进行监督微调，让模型学会移动GUI任务中的推理模式；第二阶段将整个思维块替换为N个连续隐变量，通过近似并行潜变量细化（APLR）机制进行高效推理。关键创新点包括：1）APLR采用雅可比迭代风格代替传统串行隐变量更新，通过K轮并行细化（默认K=3）使前K个隐变量与串行解完全匹配，显著降低训练开销；2）引入生成式世界模型目标，使用Q-Former对齐器将隐变量状态与下一帧截图特征对齐，通过掩码余弦距离损失迫使隐向量编码环境动态信息；3）隐变量在推理时以连续隐藏状态存在，无需解码为文本token，可将解码token量减少75%以上。在AndroidWorld上，MIRAGE在保持与4B参数显式思维链模型相当性能的同时，将token预算降低3-5倍；在AndroidControl上提升动作定位准确率并减少75%以上token生成。

### Q4: 论文做了哪些实验？

论文在AndroidControl和AndroidWorld两个标准移动代理基准上进行了实验。实验设置包括微调Qwen3-VL-4B-Instruct（4B参数）和Qwen3-VL-8B-Instruct（8B参数）作为骨干网络。对比方法包括大小匹配的Qwen3-VL-4B/8B-Instruct基线、GPT-4o、GUI-R1、UI-R1、ShowUI、MAI-UI、UI-Venus-Navi、UI-TARS-7B-SFT和Ferret-UI Lite。主要结果如下：
- AndroidControl上，MIRAGE-4B在低层级将EM从68.48提升至77.59，动作准确率从75.15提升至91.09，令牌数从115.67降至18.92；高层级EM/动作准确率分别提升9.85/6.28个百分点，令牌减少82.23%。MIRAGE-8B在低层级EM从77.66升至83.75，动作准确率从82.54升至94.62，令牌降至18.01。
- AndroidWorld上，MIRAGE-4B将任务成功率从42.9%提升至52.6%，令牌从103.0降至31.0；MIRAGE-8B从47.6%提升至57.8%，令牌从108.0降至27.0。
消融实验显示，隐式CoT、APLR并行细化和Q-Former世界模型三个核心组件均有助于性能提升，而隐式推理匹配显式CoT性能，同时生成令牌减少75%以上。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在四个方面：一是当前训练完全依赖监督信号，尚未探索半监督或无监督学习范式来降低对标注数据的依赖；二是世界模型仅基于特征级别的未来帧对齐，缺乏像素级或高分辨率环境建模能力，可能遗漏细粒度界面变化；三是仅使用下一帧监督，对更长时域因果推理的支持不足；四是实际部署前需完善隐私保护和动作安全机制。未来研究方向包括：引入强化学习或自监督目标提升推理泛化性；将特征对齐升级为隐空间或像素级预测，构建更强世界模型；扩展多步未来预测以支持长期规划；探索压缩推理与外部知识库的结合，处理未见过的界面模式。此外，可设计更高效的隐式推理长度自适应机制，平衡推理质量与延迟，并考虑在移动端资源受限场景下的轻量化部署。

### Q6: 总结一下论文的主要内容

MIRAGE提出了一种让移动GUI智能体在连续隐空间中进行推理的方法，解决了传统显式思维链（CoT）推理因输出大量文本令牌而导致的交互延迟高、成本大的问题。其核心思想是将显式推理轨迹压缩为连续的隐变量，并通过一个生成式世界模型目标来对齐这些隐状态与未来截图特征，使智能体既能保持多步推理能力，又能预测界面状态变化。方法上，MIRAGE采用两阶段训练：先对显式思维链进行有监督微调，随后通过提出的近似并行隐精炼（APLR）在K轮雅可比迭代中将推理转移到隐空间。在AndroidWorld和AndroidControl基准上，MIRAGE在4B参数模型上匹配了显式CoT的成功率（52.6%），但解码令牌减少了3-5倍；在8B模型上取得了最佳任务成功率（57.8%），同时解码令牌减少75%以上。这表明隐空间推理与未来状态预测的耦合能有效替代显式推理，显著提升移动智能体的部署效率。
