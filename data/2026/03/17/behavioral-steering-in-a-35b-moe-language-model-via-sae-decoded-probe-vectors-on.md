---
title: "Behavioral Steering in a 35B MoE Language Model via SAE-Decoded Probe Vectors: One Agency Axis, Not Five Traits"
authors:
  - "Jia Qing Yap"
date: "2026-03-17"
arxiv_id: "2603.16335"
arxiv_url: "https://arxiv.org/abs/2603.16335"
pdf_url: "https://arxiv.org/pdf/2603.16335v1"
categories:
  - "cs.LG"
  - "cs.CL"
tags:
  - "Agent Steering"
  - "Sparse Autoencoders"
  - "Interpretability"
  - "Tool Use"
  - "Behavioral Control"
  - "Mixture-of-Experts"
  - "Decoding-Time Intervention"
relevance_score: 8.5
---

# Behavioral Steering in a 35B MoE Language Model via SAE-Decoded Probe Vectors: One Agency Axis, Not Five Traits

## 原始摘要

We train nine sparse autoencoders (SAEs) on the residual stream of Qwen 3.5-35B-A3B, a 35-billion-parameter Mixture-of-Experts model with a hybrid GatedDeltaNet/attention architecture, and use them to identify and steer five agentic behavioral traits. Our method trains linear probes on SAE latent activations, then projects the probe weights back through the SAE decoder to obtain continuous steering vectors in the model's native activation space. This bypasses the SAE's top-k discretization, enabling fine-grained behavioral intervention at inference time with no retraining. Across 1,800 agent rollouts (50 scenarios times 36 conditions), we find that autonomy steering at multiplier 2 achieves Cohen's d = 1.01 (p < 0.0001), shifting the model from asking the user for help 78% of the time to proactively executing code and searching the web. Cross-trait analysis, however, reveals that all five steering vectors primarily modulate a single dominant agency axis (the disposition to act independently versus defer to the user), with trait specific effects appearing only as secondary modulations in tool-type composition and dose-response shape. The tool-use vector steers behavior (d = 0.39); the risk-calibration vector produces only suppression. We additionally show that steering only during autoregressive decoding has zero effect (p > 0.35), providing causal evidence that behavioral commitments are computed during prefill in GatedDeltaNet architectures.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何对大规模、非标准架构的语言模型进行精细化的行为干预，并探究其内部行为表征的本质问题。研究背景是，虽然稀疏自编码器（SAE）和激活工程等技术已被用于理解和干预语言模型的行为，但现有方法主要在小规模（如7B参数）的标准Transformer模型上得到验证。这些方法能否扩展到生产级、采用混合架构（如混合专家模型MoE、线性循环层）的大模型上，仍是一个开放性问题。现有方法通常依赖于对SAE特征的离散化操作（如top-k激活），这会破坏潜在的连续方向信息，限制了精细行为调控的能力。

本文的核心问题是：第一，探索在35B参数的混合专家模型（Qwen 3.5-35B-A3B，采用GatedDeltaNet/注意力混合架构）上，能否通过一种新方法实现有效的、无需重新训练的行为干预；第二，深入理解模型中“智能体行为特质”（如自主性、工具使用倾向等）的内在表征结构，即这些特质是独立的还是共享一个更根本的维度。为此，论文提出了一种“SAE解码探针向量”方法：首先在模型残差流上训练SAE，然后在SAE的潜在激活上训练线性探针来预测特定行为特质，最后将探针权重通过SAE解码器投影回模型原生激活空间，得到连续的干预向量。这种方法绕过了SAE的离散化步骤，实现了推理时细粒度的行为调控。

研究发现，尽管针对五个不同特质训练了干预向量，但它们主要调控的是一个共享的、占主导地位的“能动性轴”（即独立行动 vs. 遵从用户），而特质特异性效应仅作为次要调制出现。这揭示了模型内部行为表征的一个关键结构。此外，论文还因果性地证明了在该混合架构中，行为决策主要在预填充阶段计算完成，并通过GatedDeltaNet的循环进行传播，因为在自回归解码阶段进行干预无效。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**稀疏自编码器（SAE）用于可解释性**：SAE通过训练带有稀疏性约束的过完备自编码器，将模型激活分解为稀疏、可解释的特征。例如，相关工作已将SAE扩展到Claude 3 Sonnet等模型，并证明单个特征对应人类可理解的概念。本文则将SAE训练扩展到混合GatedDeltaNet/注意力架构，并创新性地将SAE潜在表示用作构建转向向量的中间表征，而非直接钳制特征。

**激活转向技术**：已有研究通过在推理时向残差流添加方向向量来改变模型行为，例如激活加法、基于探针识别注意力头后进行激活偏移，以及对比激活加法（CAA）。本文提出的SAE解码探针方法不同于基于均值差的CAA，它利用SAE学习到的基础来识别更精准的方向，实现了更细粒度的行为干预。

**线性探针与因果干预**：线性探针广泛用于检测模型中特定信息的线性表征，但其仅衡量表征与标签的相关性，而非对行为的因果影响。先前研究通过零空间投影或遗忘反事实等方法探讨了探针准确性与因果相关性之间的差距。本文的风险校准解离案例实证了这种差距：一个高R²的探针识别出的方向在转向中因果效力为零，而同一SAE上另一相似R²的探针却成功转向了不同特质。

**混合与线性循环架构**：GatedDeltaNet结合门控线性注意力与delta规则更新，实现了次二次序列处理。Qwen 3.5采用了循环层与注意力层交替的混合配置。本文首次研究了线性循环与稀疏特征分解的交互，并通过发现行为承诺在预填充阶段计算并通过循环状态传播，为这些架构组件的计算角色提供了证据。

### Q3: 论文如何解决这个问题？

论文通过一个四阶段的“SAE解码探针向量”管道来解决对大型混合专家模型进行细粒度行为引导的问题。核心方法是将稀疏自编码器（SAE）与线性探针相结合，并将探针权重解码回模型原生激活空间，从而绕过SAE的离散化瓶颈，实现无需重新训练的连续行为干预。

**整体框架与主要模块**：
1.  **SAE训练**：在Qwen 3.5-35B-A3B模型的残差流上，于四个深度层级（早期、早中期、中期、晚期）的GatedDeltaNet和注意力子层处，共训练了9个top-k SAE。SAE架构为标准形式，包含编码器、top-k激活函数和解码器，并采用辅助的“死亡特征”损失进行训练。
2.  **对比性特征识别**：针对五个自主行为特质（自主性、工具使用积极性、持久性、风险校准、顺从性），构建了“高表达”与“低表达”的对比提示对。通过前向传播提取SAE潜在特征激活，并计算每个特征的“特质关联分数”（TAS），以选择对每个特质最敏感的SAE作为后续探针的“钩子点”。
3.  **探针到引导向量的投影**：这是方法的关键创新步骤，分为两步：
    *   **线性探针**：在选定的最佳SAE的潜在激活上，训练一个岭回归线性探针，以区分特质的高/低表达状态。探针权重定义了SAE潜在空间中的判别方向。
    *   **解码器投影**：将学习到的探针权重通过SAE的解码器权重矩阵进行投影，得到一个连续的引导向量，该向量位于模型原始的、连续的残差流激活空间中。这一步巧妙地绕过了SAE top-k激活函数的硬阈值和离散化问题，使得后续可以施加任意尺度的、平滑的行为干预。
4.  **行为评估**：在推理时，将生成的引导向量以标量乘子的形式，添加到残差流中对应的层。论文测试了三种应用模式：全程添加、仅在预填充阶段添加、仅在自回归解码阶段添加。通过50个ReAct式智能体场景进行大规模评估，从行为轨迹中提取代理指标（如是否询问用户、工具调用次数等），并使用效应量（Cohen‘s d）和统计检验来量化引导效果。

**核心创新点**：
1.  **解码投影绕过离散化**：最大的技术贡献在于通过SAE解码器将探针权重投影回连续激活空间，从而规避了直接在SAE离散的、稀疏的潜在空间中进行操作的限制，实现了对模型行为的**连续、细粒度**的引导。
2.  **在原生空间进行干预**：引导直接在模型原本的残差流激活上进行，无需修改SAE本身或重新训练模型，方法高效且具有可解释性。
3.  **因果性实验设计**：通过对比不同引导应用模式（特别是“仅预填充”与“仅解码”），论文提供了因果证据，表明在GatedDeltaNet架构中，行为倾向主要是在预填充阶段而非自回归解码阶段计算决定的。这一发现深化了对模型内部计算机制的理解。

最终，研究发现，尽管针对五个不同特质构建了引导向量，但它们主要调制的是一个主导的“自主性轴”（即独立行动与顺从用户之间的倾向），特质特异性效果仅作为次要调制出现。这揭示了底层行为表征的某种统一性。

### Q4: 论文做了哪些实验？

该论文进行了系统的行为引导实验，以验证其提出的基于稀疏自编码器（SAE）解码探针向量的方法在大型MoE模型中的有效性。

**实验设置与数据集**：研究在Qwen 3.5-35B-A3B模型（一个350亿参数的混合专家模型）的残差流上训练了九个SAE。实验核心是使用线性探针在SAE潜在激活上识别五个代理行为特质（自主性、工具使用、顺从性、持久性、风险校准），并将探针权重通过SAE解码器投影回模型原生激活空间，形成连续的引导向量。实验共执行了1800次智能体推演，涵盖50个场景和36种引导条件（包括不同引导强度乘数α和施加位置：全部、仅预填充、仅解码）。

**对比方法与主要结果**：实验评估了不同特质引导向量的效果，并与未引导的基线模型进行对比。关键结果如下：
1.  **自主性引导效果最强**：在α=2（全部位置施加）时，模型从78%的时间询问用户转变为主动执行工具调用。关键指标：询问用户调用从1.04±1.65降至0.12±0.33（Cohen‘s d = -0.76， p < 0.0001），主动工具调用从0.30±0.85升至2.10±2.14（d = +1.01， p < 0.0001）。
2.  **工具使用引导呈现相位转变**：在α=3时，模型行为模式突变，每个场景产生4.26次工具调用（基线为1.34），其中88%为网络搜索。
3.  **顺从性引导窗口狭窄**：仅在预填充阶段引导效果最佳（α=2时，d(pro) = +0.80）。
4.  **持久性与风险校准引导失败**：仅产生行为抑制，未能引发有效的主动行为重定向。
5.  **关键因果发现**：仅在解码阶段施加自主性引导向量完全无效（p > 0.35），证明行为决策主要在预填充阶段计算完成。
6.  **跨特质分析揭示主导轴**：所有五个引导向量主要调节一个共享的“代理轴”（独立行动 vs. 顺从用户），特质特异性效应仅作为工具类型构成和剂量反应曲线形状的次要调制出现。例如，自主性向量解锁了代码执行（工具调用占比从0%升至48%），而工具使用向量则导致强迫性网络搜索（占比88%）。

### Q5: 有什么可以进一步探索的点？

该论文的局限性为：样本量较小，仅能检测大效应；代理指标设计存在构造性负相关，可能混淆跨特质特异性分析；未与简单的均值差分导向方法进行对比，无法确认稀疏自编码器（SAE）是否带来性能提升；缺乏对最大激活输入的分析，限制了特征的可解释性；所有实验仅在单一混合架构模型上进行，泛化性未知。

未来可探索的方向包括：扩大评估集规模，以检测中等效应并验证结果的稳健性；设计更丰富、独立的评估指标（如基于LLM评判的多维度行为评分），以揭示潜在的、更细微的特质特异性；进行与均值差分导向的对比实验，明确SAE在行为导向中的实际贡献；开展最大激活示例分析，深入理解SAE所捕获特征的语义含义；将该方法应用于其他模型架构（如纯Transformer）和不同规模模型，验证其通用性。此外，可探索将多个SAE解码向量进行组合或正交化，以尝试分离出更独立的行为特质轴，而非单一的主导能动性轴。

### Q6: 总结一下论文的主要内容

该论文提出了一种基于稀疏自编码器（SAE）解码探针向量的方法，用于在大型混合专家（MoE）语言模型中实现行为干预。核心问题是：能否在不重新训练模型的情况下，通过干预激活空间来精细调控模型的“能动性”行为特质？作者在Qwen 3.5-35B-A3B模型的残差流上训练了九个SAE，并在其潜在激活上训练线性探针，然后将探针权重通过SAE解码器投影回模型的原始激活空间，从而获得连续的干预向量。这种方法绕过了SAE的top-k离散化，实现了推理时无需重训练的细粒度行为调控。

主要结论包括：1）该方法在规模化生产模型中有效，自主性干预效果显著（Cohen's d高达1.04），能将模型从频繁求助用户转变为主动执行代码和搜索；2）研究发现，五个预设的能动性特质（如自主性、工具使用等）实际上主要受一个单一的“能动性轴”主导（即独立行动与遵从用户之间的倾向），特质特异性效应仅作为次要调制出现在工具类型构成和剂量反应曲线中；3）预测准确性不等于因果证据：风险校准探针虽预测性能高（R²=0.795），但其对应干预向量仅产生抑制效应，表明存在预测行为但不引发行为的“附带现象表征”；4）行为承诺的计算发生在GatedDeltaNet架构的预填充阶段，仅在自回归解码阶段干预无效。

论文的意义在于提供了一种可扩展的行为干预方法，并揭示了大型语言模型中行为表征的复杂性——表面多元的特质可能收敛于少数核心维度，这对理解模型内部机制和实现安全、可控的AI系统具有重要价值。
