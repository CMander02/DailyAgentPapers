---
title: "Heuristic Adaptation of Potentially Misspecified Domain Support for Likelihood-Free Inference in Stochastic Dynamical Systems"
authors:
  - "Georgios Kamaras"
  - "Craig Innes"
  - "Subramanian Ramamoorthy"
date: "2025-10-30"
arxiv_id: "2510.26656"
arxiv_url: "https://arxiv.org/abs/2510.26656"
pdf_url: "https://arxiv.org/pdf/2510.26656v3"
categories:
  - "cs.RO"
  - "cs.LG"
tags:
  - "Likelihood-Free Inference"
  - "Robotics"
  - "Policy Learning"
  - "Stochastic Dynamical Systems"
  - "Domain Adaptation"
  - "Simulation-based Learning"
relevance_score: 5.5
---

# Heuristic Adaptation of Potentially Misspecified Domain Support for Likelihood-Free Inference in Stochastic Dynamical Systems

## 原始摘要

In robotics, likelihood-free inference (LFI) can provide the domain distribution that adapts a learnt agent in a parametric set of deployment conditions. LFI assumes an arbitrary support for sampling, which remains constant as the initial generic prior is iteratively refined to more descriptive posteriors. However, a potentially misspecified support can lead to suboptimal, yet falsely certain, posteriors. To address this issue, we propose three heuristic LFI variants: EDGE, MODE, and CENTRE. Each interprets the posterior mode shift over inference steps in its own way and, when integrated into an LFI step, adapts the support alongside posterior inference. We first expose the support misspecification issue and evaluate our heuristics using stochastic dynamical benchmarks. We then evaluate the impact of heuristic support adaptation on parameter inference and policy learning for a dynamic deformable linear object (DLO) manipulation task. Inference results in a finer length and stiffness classification for a parametric set of DLOs. When the resulting posteriors are used as domain distributions for sim-based policy learning, they lead to more robust object-centric agent performance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决机器人领域中，基于仿真的无似然推断（LFI）方法在进行参数推断和策略学习时，由于先验定义域（support）可能设定错误而导致的性能下降问题。研究背景是，在机器人学中，为了弥合仿真与现实之间的“现实鸿沟”，常使用LFI（如BayesSim）来校准仿真器参数，并将推断得到的后验分布作为领域随机化（DR）中的领域分布，以训练能鲁棒迁移到现实世界的策略。现有方法通常假设一个固定的、均匀的先验定义域Θ，并在整个迭代推断过程中保持不变。然而，在实际应用中（例如操纵可变形线性物体DLO），由于缺乏对系统参数的先验知识，直观定义的定义域可能是不准确或“设定错误”的。这会导致两个主要不足：1）在参数推断中，即使后验概率密度在定义域边界处累积（表明真实参数可能在域外），LFI仍会产生看似确定但实际有偏的子优后验估计；2）在策略学习中，使用这种有偏的后验作为领域分布，会限制或误导策略的鲁棒性训练。此外，简单地使用尽可能宽的定义域虽能降低遗漏风险，但会引入仿真失效（如物理崩溃）和数据效率低下等问题。因此，本文要解决的核心问题是：如何在LFI的迭代过程中，动态地检测并调整可能设定错误的先验定义域，从而获得更准确的参数后验估计，并最终提升基于仿真的策略在现实世界中的对象中心化性能。为此，论文提出了三种启发式的LFI变体（EDGE, MODE, CENTRE），利用后验分布的模式移动或质量累积信息来启发式地调整定义域边界。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类和应用类两大类。

在方法类中，相关工作包括：
1.  **近似贝叶斯计算与无似然推断**：本文的LFI方法源于近似贝叶斯计算领域，旨在解决仿真器似然函数难以计算的问题。文中具体引用了BayesSim方法，它通过训练条件密度函数来近似后验分布，并支持迭代式的后验细化。
2.  **自适应贝叶斯实验设计**：文中提到了贝叶斯实验设计，它通过设计实验来最大化信息增益以改进参数估计。贝叶斯优化作为其特例，通过构建代理模型和采集函数来指导采样。

在应用类中，相关工作包括：
1.  **自适应域随机化**：已有研究通过动态调整域随机化的参数范围来训练更具鲁棒性的智能体，通常采用扩展支持域的策略以覆盖更广泛的部署条件。
2.  **Real2Sim与策略学习**：将推断得到的后验分布作为域分布用于基于仿真的策略学习，以弥合现实差距。

**本文与这些工作的关系和区别**：
本文的核心贡献在于首次在Real2Sim参数推断中提出了**支持域自适应**。现有LFI方法（如BayesSim）在迭代推断中通常**固定采样支持域**，这可能导致在支持域设定有误时，得到次优且虚假确定的后验。本文提出的三种启发式变体（EDGE, MODE, CENTRE）通过在推断步骤中解释后验众数的移动，**动态调整支持域**。这与传统的自适应域随机化工作不同，后者主要面向训练通用、鲁棒的智能体，而本文旨在通过高效、可解释的方式，为特定真实环境生成“专家型”智能体。本文方法将支持域自适应与后验推断相结合，从而在动态任务（如可变形线性物体操控）中实现了更精细的参数推断和更鲁棒的以物体为中心的智能体性能。

### Q3: 论文如何解决这个问题？

论文通过提出三种启发式的LFI变体——EDGE、MODE和CENTRE，来解决领域支持可能错误设定导致后验次优且虚假确定性的问题。核心方法是**在迭代推断过程中动态调整参数采样的支持域**，而非保持固定。

**整体框架**基于BayesSim算法，在每次LFI迭代中，除了更新后验分布，还根据当前后验的特征启发式地调整参数空间的支持边界Θ。主要模块包括：1) 模拟器，用于从当前支持域采样参数并生成仿真数据；2) 推理网络，训练以近似似然；3) 后验估计模块，计算当前迭代的后验；4) **支持域适应启发式模块**，这是核心创新组件。

**三种启发式变体的关键技术如下**：
- **EDGE**：检查后验概率质量在支持边界附近（定义为“边缘区域”）的累积情况。如果累积质量超过阈值τ，则按比例因子η将边界向外扩展，类似于探索边界外的概率质量。
- **MODE**：跟踪后验混合高斯（MoG）模式的位置。如果模式向某个边界移动并接近到一定程度，则将该边界向外扩展，以捕捉模式可能移出当前支持域的趋势。
- **CENTRE**：将后验MoG的加权均值视为理想支持域的中心，并据此重新调整支持边界，使其围绕该中心对称或合理定位。

**创新点**在于将支持域适应问题转化为基于后验特征的确定性启发式规则。这些启发式函数充当了**信息获取函数**，模仿了探索（扩大支持域以发现新区域）与利用（在当前支持域内细化后验）的平衡。它们避免了计算期望信息增益（EIG）的棘手问题，而是利用后验分布本身作为代理，通过简单规则（如质量累积、模式位置）来决策边界的扩展。此外，支持调整采用“窗口拉伸”而非“窗口滑动”，即不断累积新样本并扩展范围，而非平移固定窗口，从而能逐步覆盖更合理的参数空间。

在实现上，这些启发式模块被集成到LFI循环中，每次迭代后自动检查并可能调整支持域，确保后续采样在更合适的范围内进行，从而提升参数推断和政策学习的鲁棒性。

### Q4: 论文做了哪些实验？

论文实验分为两部分。首先，在随机动力学基准测试（Lotka-Volterra 模型和 M/G/1 队列模型）上验证了支持域误设定问题，并评估了三种启发式支持域自适应方法（EDGE、MODE、CENTRE）。实验设置包括：使用 MDNN 近似累积分布函数进行无似然推断；对于 Lotka-Volterra，参数空间设定为 OK（[-5,2]×4）、误设定（如 θ₁ 和 θ₂ 为[-3,2]和[-5,-1.5]）、宽（[-6,4]×4）等不同支持域；对于 M/G/1，参数空间包括 OK（[[0,10],[0,10],[0,0.35]]）、误设定（[[3.0,10.0],[0.0,7.0],[0,0.35]]）和宽（[[0,20],[0,20],[0,0.5]]）支持域。主要结果：误设定支持域导致推断失效（无法收敛到真实参数），而过宽支持域虽能包含真实值，但会降低模拟成功率（如 Lotka-Volterra 在最宽支持域[-7,7]×4下模拟失败累积增加），并阻碍可靠后验学习；启发式方法通过动态调整支持域改善了后验推断的准确性和数据效率。

其次，在动态可变形线性物体（DLO）操作任务中评估了支持域自适应对参数推断和策略学习的影响。实验设置：将学习到的后验作为域分布用于基于模拟的策略学习。主要结果：使用自适应支持域进行推断，能对 DLO 的长度和刚度参数实现更精细的分类；将此改进的后验用于策略训练，可得到更稳健的、以物体为中心的智能体性能。关键数据指标包括：Lotka-Volterra 模拟成功率随迭代次数变化（窄支持域下后期成功率提升）、每轮最大模拟次数（125次）、M/G/1 的观测数据为50个作业的离开间隔时间的5个百分位数（0、25、50、75、100）。

### Q5: 有什么可以进一步探索的点？

该论文提出的启发式支持域自适应方法虽能缓解支持域误设问题，但仍存在若干局限和可拓展方向。首先，三种启发式策略（EDGE、MODE、CENTRE）依赖于对后验模式偏移的直观解释，缺乏严格的理论保证，未来可结合贝叶斯优化或主动学习框架，理论化分析支持域自适应与后验收敛性的关系。其次，实验集中于随机动力学系统和特定柔性物体操控任务，泛化能力有待验证，可扩展至更复杂的多模态任务或高维参数空间。此外，当前方法仅调整采样支持域边界，未考虑域内概率密度重加权，可探索基于重要性采样或流模型的重参数化方法，实现支持域形状的连续自适应。最后，将学习到的域分布用于策略训练时，未显式考虑分布偏移下的策略泛化误差边界，未来可结合元学习或分布鲁棒优化，进一步提升跨域策略的稳定性。

### Q6: 总结一下论文的主要内容

该论文针对机器人学中基于仿真的参数推断与策略学习，提出了一种解决领域支持（domain support）可能设定错误的方法。核心问题是，在无似然推断（LFI）中，若用于采样的参数空间支持域Θ初始设定不当且固定不变，会导致后验分布虽看似确定、实则次优，进而影响后续基于域随机化的策略学习效果。

论文提出了三种启发式LFI变体（EDGE、MODE、CENTRE），通过在推断迭代中监测后验分布的模态偏移或边界概率质量累积，动态调整参数支持域Θ的边界。这些启发式方法利用标准贝叶斯推断步骤中已计算的信息，无需额外昂贵仿真。

研究首先在随机动力系统基准（Lotka-Volterra和M/G/1队列模型）上揭示了支持域设定错误的问题并验证了启发式方法的有效性。随后，论文将最鲁棒的变体集成到一个Real2Sim2Real框架中，应用于可变形线性物体（DLO）的动态操控任务。实验表明，支持域自适应能更精细地推断DLO的长度和刚度参数，且当将优化后的后验用作域分布进行策略学习时，能训练出更专注、鲁棒性更强的智能体，并在真实世界中展现出更优的任务性能。
