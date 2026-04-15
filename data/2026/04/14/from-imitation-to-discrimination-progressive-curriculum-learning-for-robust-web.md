---
title: "From Imitation to Discrimination: Progressive Curriculum Learning for Robust Web Navigation"
authors:
  - "Chuang Peng"
  - "Wei Zhang"
  - "Renshuai Tao"
  - "Xinhao Zhang"
  - "Jian Yang"
date: "2026-04-14"
arxiv_id: "2604.12666"
arxiv_url: "https://arxiv.org/abs/2604.12666"
pdf_url: "https://arxiv.org/pdf/2604.12666v1"
categories:
  - "cs.LG"
  - "cs.CL"
  - "cs.HC"
tags:
  - "Web Agent"
  - "Curriculum Learning"
  - "Preference Optimization"
  - "Data Synthesis"
  - "Agent Training"
  - "HTML Understanding"
  - "Navigation"
relevance_score: 8.5
---

# From Imitation to Discrimination: Progressive Curriculum Learning for Robust Web Navigation

## 原始摘要

Text-based web agents offer computational efficiency for autonomous web navigation, yet developing robust agents remains challenging due to the noisy and heterogeneous nature of real-world HTML. Standard Supervised Fine-Tuning (SFT) approaches fail in two critical dimensions: they lack discrimination capabilities to reject plausible but incorrect elements in densely populated pages, and exhibit limited generalization to unseen website layouts. To address these challenges, we introduce the Triton dataset (590k instances) and a progressive training curriculum. Triton is constructed via Structural-Semantic Hard Negative Mining, which explicitly mines topologically similar distractors, and a Dual-Agent Consensus pipeline that synthesizes diverse cross-domain tasks with strict verification. Building upon this foundation, our progressive curriculum produces three models: Triton-SFT-32B for basic imitation, Triton-ORPO-32B for robust discrimination via Odds Ratio Preference Optimization, and Triton-GRPO-32B for long-horizon consistency through Group Relative Policy Optimization. Empirical evaluation on Mind2Web demonstrates that Triton-GRPO-32B achieves state-of-the-art performance among open-source models with 58.7% Step Success Rate, surpassing GPT-4.5 (42.4%) and Claude-4.5 (41.4%) by over 16%, validating that specialized data curriculum outweighs raw parameter scale for web navigation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于文本的网页导航智能体在现实复杂环境中鲁棒性不足的核心问题。研究背景是，虽然纯文本网页智能体相比多模态方案具有计算效率优势，但真实网页的HTML结构通常噪声大且异构性强，给自主导航带来了巨大挑战。

现有方法，特别是标准的监督微调（SFT），存在两大关键不足：首先，它们缺乏“辨别能力”，模型只学会了“应该点击什么”，却没有学会“不应该点击什么”。这导致在元素密集的页面中，模型容易产生“幻觉”，选择那些看似合理但实际错误的元素（例如，在购买iPhone 16 Pro的指令下，却选择了结构相似的iPhone 17 Pro选项）。其次，现有方法的泛化能力有限，过度依赖特定领域的训练数据，使得智能体难以适应未见过的网站布局和多样化的文档对象模型（DOM）结构。

因此，本文要解决的核心问题是如何构建一个既具备精细辨别力，又能广泛泛化到新网页环境的鲁棒网页导航智能体。为此，论文提出了系统性的解决方案：一是构建一个名为Triton的大规模高质量数据集（59万实例），通过挖掘结构相似的“困难负样本”和合成跨领域任务来针对性解决辨别与泛化难题；二是设计一个渐进式课程学习框架，引导模型从基础的模仿学习（SFT）阶段，进阶到通过优化技术（ORPO）强化辨别能力，最终通过群体策略优化（GRPO）确保多步长任务执行的一致性。该研究验证了针对性的数据课程和训练方法，比单纯增加模型参数量更能有效提升网页导航的性能。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：基于大语言模型的网页智能体、面向代码和网页的数据合成方法，以及偏好对齐与策略优化技术。

在**基于大语言模型的网页智能体**方面，研究已从模拟环境转向真实网页导航。现有方法主要分为多模态智能体（如SeeAct、CogAgent）和基于文本的智能体。前者利用视觉语言模型处理截图，精度高但延迟大；后者基于HTML DOM树，效率更高。先前工作多集中于改进推理提示策略（如思维链、树搜索）或修改模型架构，而本文则强调数据课程和判别式训练对提升鲁棒性的关键作用，弥补了该领域的空白。

在**数据合成**领域，合成数据已成为扩展指令微调的重要范式。代码领域有Magicoder等方法合成编程问题。网页领域则有WebSight数据集（用于设计转代码）和Auto-UI（为移动UI生成指令）等工作。本文提出的“双智能体共识”流程对此进行了延伸，确保合成的网页导航数据不仅多样，而且经过严格验证，解决了朴素合成中常见的幻觉问题。

在**偏好对齐与策略优化**方面，超越监督微调的方法对减少错误至关重要。主流技术包括需要复杂奖励建模的RLHF，以及更简化的DPO。近期出现的ORPO将偏好对齐直接融入SFT，而GRPO则通过优化输出组来增强推理一致性。本文首次系统地将ORPO和GRPO这两种先进对齐技术整合到一个统一的课程学习中，专门用于解决噪声HTML判别和长程一致性的挑战。

### Q3: 论文如何解决这个问题？

论文通过一个渐进式课程学习框架来解决基于文本的网页智能体在噪声和异构HTML环境中导航时存在的辨别力不足和泛化能力有限的问题。其核心方法分为三个阶段，依次构建了三个模型：Triton-SFT-32B、Triton-ORPO-32B和Triton-GRPO-32B。

整体框架建立在高质量数据集Triton（约59万实例）之上，该数据集通过“结构-语义硬负例挖掘”和“双智能体共识”流程构建，确保了数据的多样性和挑战性。训练课程的核心是分阶段、有侧重地利用这些数据。

第一阶段是基础模仿，采用标准的监督微调。模型在完整数据集上进行训练，目标是最大化给定HTML观察下生成真实动作序列的可能性。此阶段旨在让智能体掌握HTML语法和多样化的任务意图格式，完成基本的知识注入。

第二阶段聚焦于提升辨别能力，采用几率比偏好优化。其创新点在于动态生成偏好对：利用第一阶段训练好的SFT模型在训练集上进行策略采样，为每个指令生成多个输出，并将真实轨迹作为正例，模型自身生成的错误轨迹作为负例，从而构建一个反映模型当前“盲点”的判别子集。ORPO目标函数在SFT损失基础上，增加了对正负例几率比的对数进行优化的项，迫使模型学会区分与目标语义相似但错误的“硬负例”，将学习目标从纯粹模仿转向辨别。

第三阶段旨在增强复杂长视野任务下的稳定性和动作精度，采用分组相对策略优化。该阶段在一个精选的8万个复杂实例子集上进行。关键技术是设计了一个分层的奖励函数，以提供密集、精细的监督。该奖励包括：格式正确性奖励、选项匹配指示器（作为后续奖励的门控）、选择正确元素的主要奖励、预测动作与真实动作在词元级别的F1分数（提供稠密反馈），以及完美匹配的额外奖励。在训练时，对每个输入采样一组输出，并优化策略以最大化相对于该组基线奖励的期望奖励。GRPO无需额外的评论家模型，通过组内优势归一化来鼓励模型收敛到最精确、一致的动作执行路径。

这一渐进式课程的主要创新在于，它不是一次性训练，而是通过SFT、ORPO、GRPO三个连续阶段，分别解决基础指令遵循、对抗硬负例的决策边界锐化，以及复杂场景下的长程一致性优化问题。最终模型Triton-GRPO-32B在Mind2Web基准测试中取得了最先进的步骤成功率，显著超越了包括GPT-4.5在内的众多大参数规模模型，验证了专业化数据课程相对于单纯参数规模的优势。

### Q4: 论文做了哪些实验？

实验基于构建的Triton数据集（约59万实例）和渐进式课程学习框架，在Mind2Web基准上进行评估。实验设置以Qwen2.5-Coder-32B-Instruct为基座模型，使用Llama Factory和VERL进行监督/偏好对齐与强化学习训练。训练课程分为三步：SFT（3轮，学习率5e-5）、ORPO（学习率5e-6）和GRPO（学习率1e-6，组大小G=5）。评估指标包括元素准确率（Ele. Acc）、操作F1（Op. F1）、步骤成功率（Step SR）以及综合得分（Composite Score）。

主要对比方法包括开源模型（如Qwen、DeepSeek、Llama系列）和闭源模型（如GPT-4.5、Claude-4.5、Gemini 2.5）。在Mind2Web的三个泛化分割（Cross-Task、Cross-Website、Cross-Domain）上，论文通过消融实验验证了各组件效果：仅使用原始训练数据（Mind）步骤成功率为36.3%，加入判别性轨迹挖掘数据（Dis）提升至42.0%，结合合成视觉结构数据（Vis）后达47.6%。进一步应用ORPO和GRPO优化后，最终模型Triton-GRPO-32B达到58.7%的步骤成功率，在整体和跨域分割上分别获得70.1和69.9的综合得分。

关键结果显示：Triton-GRPO-32B显著超越闭源基线，步骤成功率比GPT-4.5（42.4%）和Claude-4.5（41.4%）高出16%以上；在最具挑战的Cross-Domain分割上，将基线模型的15.5%提升至58.2%。实验还分析了超参数敏感性（如负样本池大小K=20、拒绝量G=10时最优）和合成数据缩放规律（数据量增加持续提升性能，跨域步骤成功率提升3.3%），证实了课程学习中SFT基础的关键作用及后续对齐阶段的增量收益。

### Q5: 有什么可以进一步探索的点？

该论文的局限性为未来研究提供了几个明确的探索方向。首先，模型仅依赖HTML文本，缺乏视觉感知能力。未来的工作可以探索多模态模型，集成视觉编码器以理解颜色、图标、布局等像素级信息，这对于识别状态指示器或处理动态UI元素至关重要。其次，评估基于静态基准（Mind2Web），未能涵盖真实网络环境的动态性。一个重要的方向是开发能处理实时交互（如弹窗、网络延迟、验证码）的仿真环境或评估协议，以测试代理的鲁棒性。再者，GRPO等方法计算开销较大。未来可研究更高效的强化学习算法或离线优化技术，以降低训练成本。此外，论文展示了课程学习和专业数据的重要性，但数据合成管道（如双智能体共识）的泛化能力仍有提升空间。可进一步探索自动化、可扩展的数据生成方法，以覆盖更广泛的网站布局和任务类型。最后，当前模型规模较大（32B），研究如何通过知识蒸馏或架构优化，在保持性能的同时减小模型尺寸，对实际部署具有重要意义。

### Q6: 总结一下论文的主要内容

本文针对基于文本的网络智能体在真实世界异构HTML环境中导航鲁棒性不足的问题，提出了一种渐进式课程学习框架。核心贡献在于构建了大规模的Triton数据集（59万实例）并设计了分阶段的训练课程。方法上，首先通过“结构-语义硬负例挖掘”技术构建包含拓扑相似干扰项的数据，并利用“双智能体共识”流程合成经过严格验证的跨领域任务。在此基础上，训练流程分为三步：先进行基础模仿学习得到Triton-SFT-32B模型；接着通过几率比偏好优化提升模型在密集页面中拒绝错误元素的分辨能力，得到Triton-ORPO-32B；最后通过组相对策略优化确保长程任务的一致性，得到最终模型Triton-GRPO-32B。主要结论是，在Mind2Web基准测试中，Triton-GRPO-32B以58.7%的步骤成功率取得了开源模型中的最优性能，显著超越GPT-4.5和Claude-4.5等大型闭源模型超过16%。这验证了针对性的高质量数据课程与策略对齐的协同作用，其效能超越了单纯的参数规模扩展，为训练鲁棒的网络导航智能体提供了新范式。
