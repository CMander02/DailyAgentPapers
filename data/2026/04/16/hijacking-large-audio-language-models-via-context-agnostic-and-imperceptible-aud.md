---
title: "Hijacking Large Audio-Language Models via Context-Agnostic and Imperceptible Auditory Prompt Injection"
authors:
  - "Meng Chen"
  - "Kun Wang"
  - "Li Lu"
  - "Jiaheng Zhang"
  - "Tianwei Zhang"
date: "2026-04-16"
arxiv_id: "2604.14604"
arxiv_url: "https://arxiv.org/abs/2604.14604"
pdf_url: "https://arxiv.org/pdf/2604.14604v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.SD"
tags:
  - "Agent Security"
  - "Adversarial Attack"
  - "Prompt Injection"
  - "Audio-Language Model"
  - "Multi-Modal Agent"
  - "Robustness"
relevance_score: 7.5
---

# Hijacking Large Audio-Language Models via Context-Agnostic and Imperceptible Auditory Prompt Injection

## 原始摘要

Modern Large audio-language models (LALMs) power intelligent voice interactions by tightly integrating audio and text. This integration, however, expands the attack surface beyond text and introduces vulnerabilities in the continuous, high-dimensional audio channel. While prior work studied audio jailbreaks, the security risks of malicious audio injection and downstream behavior manipulation remain underexamined. In this work, we reveal a previously overlooked threat, auditory prompt injection, under realistic constraints of audio data-only access and strong perceptual stealth. To systematically analyze this threat, we propose \textit{AudioHijack}, a general framework that generates context-agnostic and imperceptible adversarial audio to hijack LALMs. \textit{AudioHijack} employs sampling-based gradient estimation for end-to-end optimization across diverse models, bypassing non-differentiable audio tokenization. Through attention supervision and multi-context training, it steers model attention toward adversarial audio and generalizes to unseen user contexts. We also design a convolutional blending method that modulates perturbations into natural reverberation, making them highly imperceptible to users. Extensive experiments on 13 state-of-the-art LALMs show consistent hijacking across 6 misbehavior categories, achieving average success rates of 79\%-96\% on unseen user contexts with high acoustic fidelity. Real-world studies demonstrate that commercial voice agents from Mistral AI and Microsoft Azure can be induced to execute unauthorized actions on behalf of users. These findings expose critical vulnerabilities in LALMs and highlight the urgent need for dedicated defense.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在揭示并系统性地研究大型音频-语言模型（LALMs）中一种先前被忽视的安全威胁——听觉提示注入攻击，并在现实约束下（仅能访问音频数据且需具备强感知隐蔽性）实现对此类模型的高效劫持。

研究背景在于，随着语音接口与大型语言模型的深度融合，催生了新一代的LALMs，它们支持端到端的音频输入输出，实现了自然、低延迟的全双工语音交互，甚至具备调用外部工具和执行命令的自主能力。然而，这种强大的多模态感知与自主能力也扩展了攻击面。现有研究主要关注“音频越狱”攻击，即攻击者作为用户直接输入精心构造的恶意音频来触发有害响应。相比之下，更具主动性和隐蔽性的“听觉提示注入”攻击却研究不足。在这种威胁模型下，攻击者是第三方，只能在用户在场时向音频流中注入恶意内容，且只能访问音频数据，同时要求注入内容对人耳高度隐蔽（强感知隐蔽性）。现有唯一的相关探索性工作存在扰动不受限、隐蔽性差、泛化能力有限等问题。

因此，本文要解决的核心问题是：在“仅音频数据访问”和“强感知隐蔽性”的现实约束下，第三方攻击者能否成功劫持最先进的LALMs？这面临三大挑战：1）LALMs架构异构（离散令牌、连续、混合等），需要普适的攻击方法；2）攻击无法预知用户语音或文本指令（上下文未知），需要攻击能泛化到未见过的用户上下文；3）需在保持高度隐蔽的同时实现精确的行为控制，现有方法在隐蔽性或有效性上存在不足。

为此，本文提出了一个名为AudioHijack的通用攻击框架，旨在实现与上下文无关且难以察觉的听觉提示注入。该框架通过基于采样的梯度估计绕过不可微的音频令牌化过程，实现端到端优化；通过注意力监督与多上下文训练，使模型注意力聚焦于对抗性音频并泛化到未知上下文；并设计卷积混合方法将扰动调制为类似自然混响的效果，极大提升了隐蔽性。最终，论文通过广泛的实验验证了该威胁的严重性。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：针对大型音频-语言模型（LALMs）的攻击研究，以及更广泛的音频对抗样本研究。

在**针对LALMs的攻击研究**中，相关工作主要集中于直接提示注入（如越狱攻击）。例如，VoiceJailbreak、Ying等人、BoN-Jailbreak、JAB、AdvWave、SpeechGuard和AudioJailbreak等方法，均假设攻击者能完全控制用户的语音指令，通过合成或优化有害语音来绕过模型的安全对齐。这些方法属于直接攻击，攻击者即用户，对感知隐蔽性要求较低。另一项工作SSJ则在语音中嵌入字母拼写来隐藏恶意内容，但仍依赖伴随的文本指令。与这些工作不同，本文研究的**听觉提示注入**属于**间接提示注入**，攻击者是第三方，仅能操控音频数据部分，无需控制用户指令，这对攻击的上下文无关性和隐蔽性提出了极高要求。在此方向上，Bagdasaryan等人的研究是唯一的先例，但其仅在少数通用多模态模型上进行了概念验证，且扰动明显。本文则首次对最先进的专用LALMs进行了系统性的间接注入攻击研究，在仅访问音频数据的现实约束下，实现了对未见用户指令的泛化和高度不可感知的扰动。

在更广泛的**音频对抗样本（AEs）** 研究领域，传统方法主要针对语音识别、音频分类等判别式模型，目标是在完全控制输入的情况下引发错误分类。然而，本文攻击的目标是**大规模生成式LALMs**，目标转向在开放生成中操控模型行为；同时，攻击者面临**部分输入控制**的约束（只能操控复合提示中的音频数据部分）；这导致了独特的上下文依赖性和技术挑战。因此，本文的间接提示注入并非传统音频AEs的简单延伸，而是一个具有不同目标、约束和挑战的新问题。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为AudioHijack的通用框架来解决听觉提示注入问题，该框架旨在生成与上下文无关且难以察觉的对抗性音频，以劫持具有异构集成方案的大型音频-语言模型（LALMs）。其核心方法、架构设计和关键技术如下：

**整体框架与主要模块**：
AudioHijack框架包含三个关键组件，分别应对三个核心挑战（C1-C3）。

1.  **基于采样的梯度估计（应对C1：结构梯度阻塞）**：针对LALMs中音频标记化过程（特别是离散标记或混合方案）的非可微向量量化操作，该方法使用Gumbel-Softmax采样进行梯度估计。它将声学特征与码本向量之间的负距离视为分类logits，通过Gumbel-Softmax分布计算软权重，从而用可微的概率采样和矩阵乘法替代了硬标记选择和嵌入查找。结合直通估计器技巧，在前向传播中使用硬权重模拟真实推理，在反向传播中使用软权重实现梯度流动，从而实现了跨不同模型架构的端到端对抗优化。

2.  **注意力引导的上下文泛化（应对C2：上下文不透明与敏感性）**：为确保生成的对抗音频能泛化到未见过的用户上下文，该方法结合了隐式和显式注意力操纵。
    *   **隐式方法（基于转换的期望）**：利用一个辅助指令数据集，在优化对抗音频时，对多个用户指令计算期望损失，从而隐式地鼓励模型更多地关注对抗音频并抑制上下文影响。
    *   **显式方法（注意力监督）**：在优化目标中引入一个边际注意力损失项，该损失通过计算对抗音频令牌在模型所有层和注意力头中获得的平均注意力权重，并设定一个下界，从而显式地引导模型将注意力重新定向到对抗音频上。这种结合显著提升了攻击在不同上下文中的泛化能力。

3.  **卷积扰动混合（应对C3：感知隐形约束）**：为了在严格的扰动预算下实现高攻击成功率和听觉不可感知性，该方法摒弃了简单的加性扰动，采用了卷积扰动混合。
    *   具体操作是将良性载波音频分割成短帧，对每一帧应用一个短的、可学习的卷积核（初始化为房间脉冲响应信号）进行卷积操作。
    *   这种方法在时频域上重新分配扰动能量，模拟真实的混响效果，使得生成的对抗性音频听起来像经过自然混响处理，从而在极小的感知失真下实现高度隐形。

**创新点**：
*   **系统性威胁建模与框架**：首次系统性地形式化并研究了在仅音频数据访问和强感知隐形现实约束下的“听觉提示注入”威胁，并提出了一个通用攻击框架。
*   **可微的音频标记化攻击**：通过基于Gumbel-Softmax的梯度估计方法，成功绕过了LALMs中非可微音频标记化的障碍，实现了对采用离散或混合标记化方案的模型的端到端对抗优化。
*   **上下文无关的注意力操纵**：创新性地结合了基于多上下文训练的隐式泛化和基于注意力权重的显式监督，使攻击能够有效泛化到未知的用户指令，实现上下文无关的劫持。
*   **物理启发的隐形扰动**：提出的卷积混合方法将对抗扰动调制为类似自然混响的信号，显著提升了听觉上的不可感知性，超越了传统加性扰动的隐形能力。

通过这三项技术的协同工作，AudioHijack能够在保持高音频保真度的前提下，以高成功率劫持多种最先进的LALMs，并诱导其执行预定义的恶意行为。

### Q4: 论文做了哪些实验？

论文的实验设置围绕其提出的AudioHijack框架，在13个最先进的大型音频-语言模型（LALMs）上进行了广泛的评估。这些模型涵盖了离散、连续和混合三种集成方案，参数规模从2B到9B不等，能力包括音频分析、语音对话和工具使用。

实验使用了自构建的数据集和基准测试。核心是定义了六种不当行为类别（如泄露私人信息、生成有害内容、执行未经授权的工具调用等），用于评估劫持成功率。此外，通过人类听觉测试（MOS）和客观声学指标（如信噪比SNR、对数谱距离LSD）来评估对抗音频的感知不可察觉性和声学保真度。

对比方法方面，由于这是首个针对听觉提示注入的系统性研究，论文主要将AudioHijack与自身消融变体（如移除注意力监督、多上下文训练或卷积混合）进行对比，以验证各组件有效性。同时，也与基于梯度的基线方法进行了比较。

主要结果显示，AudioHijack在未见过的用户上下文上实现了高且一致的劫持成功率。在13个目标LALMs上，针对六类不当行为的平均成功率达到79%至96%。关键数据指标包括：平均劫持成功率超过90%，生成的对抗音频信噪比（SNR）高达38.57 dB，对数谱距离（LSD）低至0.65，并且在人类主观评分（MOS）中与干净音频无法区分（得分约4.5/5）。真实世界研究也成功演示了该方法可诱导Mistral AI和Microsoft Azure的商业语音代理执行未经授权的操作。

### Q5: 有什么可以进一步探索的点？

该论文揭示了音频提示注入攻击的有效性，但其局限性和未来探索方向值得深入。首先，研究主要针对已知模型结构进行优化，对黑盒或持续演进的商用系统（如实时更新的语音助手）的泛化能力尚未验证。防御方面仅提及需求，未提出具体方案，未来可探索基于音频特征过滤、对抗训练或异常检测的实时防护机制。其次，攻击依赖端到端梯度估计，计算成本较高，需研究更高效的轻量级生成方法。此外，实验集中于英语场景，多语言、多方言环境下的攻击鲁棒性仍是空白。结合AI安全趋势，可进一步探索：1）跨模态攻击的扩展，如结合视觉提示进行多模态劫持；2）攻击的可解释性分析，通过注意力机制解析模型被误导的决策路径；3）设计人类感知与模型感知差异更大的隐形扰动，以应对潜在的人类审核环节。这些方向将深化对LALMs安全边界的理解，推动更具韧性的语音交互系统发展。

### Q6: 总结一下论文的主要内容

该论文揭示了大型音频-语言模型（LALMs）中一种被忽视的安全威胁——听觉提示注入攻击。研究指出，LALMs 紧密集成音频与文本，虽提升了交互能力，但也扩展了攻击面，使连续高维音频通道成为潜在漏洞。现有工作多关注音频越狱，而对恶意音频注入及下游行为操控的风险研究不足。

论文核心贡献是提出了 **AudioHijack** 框架，用于生成与上下文无关且难以察觉的对抗性音频，以劫持 LALMs。该方法通过基于采样的梯度估计实现端到端优化，绕过不可微的音频分词器；结合注意力监督与多上下文训练，引导模型关注对抗音频并泛化至未见过的用户上下文；此外，设计卷积混合方法将扰动调制为自然混响，大幅提升听觉隐蔽性。

实验在 13 个先进 LALMs 上进行，结果显示在 6 类恶意行为中均能实现稳定劫持，在未见上下文中的平均成功率达 79%–96%，且音频保真度高。真实世界测试表明，Mistral AI 和 Microsoft Azure 的商业语音代理可被诱导执行未授权操作。这些发现暴露了 LALMs 的关键脆弱性，强调了开发针对性防御措施的紧迫性。
