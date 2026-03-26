---
title: "UI-Voyager: A Self-Evolving GUI Agent Learning via Failed Experience"
authors:
  - "Zichuan Lin"
  - "Feiyu Liu"
  - "Yijun Yang"
  - "Jiafei Lyu"
  - "Yiming Gao"
  - "Yicheng Liu"
  - "Zhicong Lu"
  - "Yangbin Yu"
  - "Mingyu Yang"
  - "Junyou Li"
  - "Deheng Ye"
  - "Jie Jiang"
date: "2026-03-25"
arxiv_id: "2603.24533"
arxiv_url: "https://arxiv.org/abs/2603.24533"
pdf_url: "https://arxiv.org/pdf/2603.24533v1"
github_url: "https://github.com/ui-voyager/UI-Voyager"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.CV"
tags:
  - "GUI Agent"
  - "Self-Evolving"
  - "Mobile Automation"
  - "Reinforcement Learning"
  - "Fine-Tuning"
  - "Knowledge Distillation"
  - "AndroidWorld"
  - "Multimodal LLM"
relevance_score: 8.5
---

# UI-Voyager: A Self-Evolving GUI Agent Learning via Failed Experience

## 原始摘要

Autonomous mobile GUI agents have attracted increasing attention along with the advancement of Multimodal Large Language Models (MLLMs). However, existing methods still suffer from inefficient learning from failed trajectories and ambiguous credit assignment under sparse rewards for long-horizon GUI tasks. To that end, we propose UI-Voyager, a novel two-stage self-evolving mobile GUI agent. In the first stage, we employ Rejection Fine-Tuning (RFT), which enables the continuous co-evolution of data and models in a fully autonomous loop. The second stage introduces Group Relative Self-Distillation (GRSD), which identifies critical fork points in group rollouts and constructs dense step-level supervision from successful trajectories to correct failed ones. Extensive experiments on AndroidWorld show that our 4B model achieves an 81.0% Pass@1 success rate, outperforming numerous recent baselines and exceeding human-level performance. Ablation and case studies further verify the effectiveness of GRSD. Our method represents a significant leap toward efficient, self-evolving, and high-performance mobile GUI automation without expensive manual data annotation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决移动图形用户界面（GUI）智能体在自主执行长周期、复杂任务时面临的两个核心挑战：一是从失败轨迹中学习效率低下，二是在稀疏奖励场景下的信用分配模糊问题。

研究背景方面，随着多模态大语言模型（MLLMs）的快速发展，构建能够感知、理解并自主操作GUI的通用智能体成为前沿方向。移动GUI环境因其布局多样、交互丰富、视觉上下文有限且状态动态变化，成为一个极具代表性且富有挑战的研究领域。尽管已有工作将强大MLLMs集成到手机中以构建GUI代理，并出现了一些实际应用，但现有方法仍存在明显不足。

现有方法的不足主要体现在两点：首先，在移动交互中，失败轨迹占据了智能体经验（尤其是在困难任务上）的很大一部分，但传统训练流程通常未能充分利用这些失败经验，导致数据效率低下。其次，现有强化学习方法依赖于从GUI交互中获得的粗粒度、轨迹级别的稀疏奖励（成功/失败），这使得智能体难以准确识别导致任务失败的具体步骤，从而阻碍了策略的稳定优化。

因此，本文的核心问题是：如何设计一种高效、自演进的移动GUI智能体，使其能够充分利用失败经验进行学习，并克服稀疏奖励下的信用分配难题。为此，论文提出了UI-Voyager，一个新颖的两阶段自演进GUI代理框架。第一阶段采用拒绝微调策略，实现数据与模型在全自动循环中的协同进化；第二阶段引入组相对自蒸馏方法，通过识别组间轨迹的关键分叉点，从成功轨迹中构建密集的步骤级监督信号来修正失败轨迹，从而将稀疏的轨迹级奖励替换为精确的自蒸馏学习信号。

### Q2: 有哪些相关研究？

相关研究主要可分为**方法类**和**评测环境类**两大类。

在**方法类**研究中，一类工作利用大规模静态数据集训练GUI代理，以学习动作定位、图标功能等通用知识，但难以处理动态交互和从试错中学习。另一类研究则在交互式环境中训练和评估代理，通过环境反馈（如任务完成奖励）优化策略。早期方法多采用强化学习或行为克隆。随着基础模型（如ChatGPT、Gemini等）的发展，现有研究广泛利用大型语言模型或视觉语言模型进行任务规划或微调，以构建GUI代理。

在**评测环境类**方面，已有许多针对网页（如WebShop、WebArena）、桌面操作系统（如OSWorld、WindowsAgentArena）和移动端（如Mobile-Env、MobileWorld）的交互式基准测试平台。本文专注于AndroidWorld这一移动端环境。

**本文与这些工作的关系和区别**在于：1）**方法上**，不同于依赖静态数据集或外部模型合成纠正轨迹的先前方法（如EvoCUA），本文提出了一个两阶段自进化框架。第一阶段通过拒绝微调实现数据与模型的自主协同进化；第二阶段引入组内相对自蒸馏机制，通过轻量级方法定位关键决策点，并将成功轨迹中的动作知识蒸馏到失败轨迹中，从而在稀疏奖励下实现高效学习和明确的信用分配。2）**目标上**，本文旨在构建一个无需昂贵人工标注、能在复杂长视野任务中高效运行的高性能开源移动GUI代理，并在AndroidWorld上取得了超越现有基线和人类水平的性能。

### Q3: 论文如何解决这个问题？

论文通过一个名为UI-Voyager的两阶段自进化框架来解决移动GUI智能体从失败轨迹中学习效率低下、以及在稀疏奖励下长视野任务中信用分配模糊的问题。其核心方法包括拒绝微调（RFT）和组相对自蒸馏（GRSD）两个迭代阶段，整体形成一个数据与模型协同进化的闭环。

在第一阶段，RFT旨在构建高质量的训练数据集。其架构包含轨迹生成和拒绝采样两个主要模块。首先，通过一个种子任务生成器，通过扰动原始任务模板的关键参数（如时间约束、数量、文件实体）来合成多样化的新任务，从而自动化产生大量交互轨迹。随后，利用一个基于规则的验证器对轨迹进行过滤，仅保留那些成功达成目标或通过任务完成验证的“成功”轨迹，形成高质量的监督微调（SFT）数据集。该过程迭代进行，上一轮训练好的模型被用作新一轮的轨迹生成智能体，确保了数据和模型能力的共同提升。

第二阶段，GRSD是关键创新点，旨在解决稀疏轨迹级奖励下的信用分配难题。其核心思想是：对同一任务进行多次 rollout 形成轨迹组，其中成功和失败的轨迹往往在某个步骤前访问相同的屏幕状态，之后因不同动作选择而分叉。GRSD通过“分叉点检测”机制来识别这些关键决策点。具体技术包括：1）**跨轨迹状态匹配**：使用结构相似性指数（SSIM）比较预处理后的屏幕截图，判断观察状态是否等价。2）**过渡对齐**：检查连续步骤的观察是否都匹配，以跳过已对齐的步骤。3）**教师步骤选择**：为失败轨迹的每个步骤，在满足观察等价且后续状态发生分叉的成功轨迹步骤中，选择SSIM最高的作为“教师”步骤。检测到的每个分叉点都构成一个训练样本：保留失败轨迹到该步骤的上下文提示，但将响应替换为对应教师步骤的成功动作。

最终，通过混合使用RFT收集的SFT数据和GRSD构建的纠正数据进行训练，模型能将稀疏的轨迹级反馈转化为密集的步骤级监督，实现精准的自我纠正。这种方法无需昂贵的人工标注，实现了高效、自进化的高性能移动GUI自动化。

### Q4: 论文做了哪些实验？

论文在AndroidWorld基准测试上进行了广泛的实验。实验设置方面，以Qwen3-VL-4B-Instruct为骨干模型，在包含116个多样化真实世界移动应用任务的AndroidWorld数据集上进行评估。该数据集通过随机化初始化参数，可生成大量可验证奖励的训练任务。训练使用了来自AndroidWorld的超过7000个任务的数据集。

对比方法涵盖了开源和闭源的多种基线模型与智能体，包括通用视觉语言模型（如Qwen3-VL系列）、专用GUI智能体（如UI-Tars、GUI-Owl、Step-GUI、MAI-UI、UI-Venus）以及大规模专有模型（如Gemini-2.5-Pro、Seed1.8）。主要性能指标为Pass@1成功率。

主要结果显示，UI-Voyager（4B参数）取得了81.0%的成功率，超越了所有基线方法，并超过了报告中80.0%的人类水平性能。关键数据指标包括：UI-Voyager (4B) 81.0%，而参数量大得多的MAI-UI-235B-A22B为76.7%，UI-Tars-2为73.3%。在同等规模模型中，UI-Voyager显著优于Step-GUI-4B（63.9%）和Qwen3-VL-4B（45.3%）。为确保可复现性，论文报告了在64个随机种子上的平均成功率。

此外，消融和案例分析验证了所提方法组件的有效性。拒绝微调（RFT）实验显示，经过四轮迭代，模型性能持续稳定提升，第三轮迭代的检查点达到73.2%的Pass@1成功率，被用作后续训练的基础。与直接从基础模型应用GRPO和PPO等强化学习方法相比，RFT作为初始化策略效率更高。分组相对自蒸馏（GRSD）中的关键分叉点检测机制也在案例（如BrowserMaze任务）中得到了直观展示，证明了其通过成功轨迹的密集步骤级监督来纠正失败轨迹的有效性。

### Q5: 有什么可以进一步探索的点？

本文提出的UI-Voyager在自主学习和失败经验利用上取得了显著进展，但仍存在一些局限性和值得深入探索的方向。首先，其训练和演化完全依赖模拟环境（AndroidWorld），在真实设备、复杂网络条件或多样化的第三方应用界面上的泛化能力尚未验证，未来需在更开放的真实世界场景中测试。其次，方法依赖于初始任务的成功轨迹来启动自演化循环，对于完全未知或高度动态的任务，如何冷启动仍是一个挑战；可探索结合课程学习或主动探索策略来引导初始数据收集。此外，当前的关键分叉点识别和密集监督构建可能对任务分解的粒度敏感，未来可研究更细粒度或层次化的动作表示与信用分配机制，以处理更复杂的多步骤任务。最后，模型完全基于视觉，未整合系统级API或辅助传感器信息，融合多模态信号（如文本描述、布局树、可访问性节点）可能进一步提升鲁棒性和效率。

### Q6: 总结一下论文的主要内容

本文提出UI-Voyager，一种自演进的移动图形用户界面（GUI）智能体，旨在解决现有方法在长程GUI任务中学习效率低、稀疏奖励下信用分配模糊的问题。其核心贡献在于一个两阶段自演进框架：第一阶段采用拒绝微调（RFT），通过完全自主的循环实现数据与模型的持续协同进化；第二阶段引入组相对自蒸馏（GRSD），通过分析群体轨迹中的关键分叉点，从成功轨迹构建密集的步级监督来修正失败轨迹。实验表明，该方法的40亿参数模型在AndroidWorld基准上取得了81.0%的Pass@1成功率，超越了现有基线及人类水平，且无需昂贵的人工标注。这标志着向高效、自演进、高性能的移动GUI自动化迈出了重要一步。
