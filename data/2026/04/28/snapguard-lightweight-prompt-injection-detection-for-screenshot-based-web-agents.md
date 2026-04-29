---
title: "SnapGuard: Lightweight Prompt Injection Detection for Screenshot-Based Web Agents"
authors:
  - "Mengyao Du"
  - "Han Fang"
  - "Haokai Ma"
  - "Jiahao Chen"
  - "Kai Xu"
  - "Quanjun Yin"
  - "Ee-Chien Chang"
date: "2026-04-28"
arxiv_id: "2604.25562"
arxiv_url: "https://arxiv.org/abs/2604.25562"
pdf_url: "https://arxiv.org/pdf/2604.25562v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Web Agent安全"
  - "提示注入检测"
  - "轻量级防御"
  - "多模态Agent"
  - "对抗攻击防御"
relevance_score: 8.5
---

# SnapGuard: Lightweight Prompt Injection Detection for Screenshot-Based Web Agents

## 原始摘要

Web agents have emerged as an effective paradigm for automating interactions with complex web environments, yet remain vulnerable to prompt injection attacks that embed malicious instructions into webpage content to induce unintended actions. This threat is further amplified for screenshot-based web agents, which operate on rendered visual webpages rather than structured textual representations, making predominant text-centric defenses ineffective. Although multimodal detection methods have been explored, they often rely on large vision-language models (VLMs), incurring significant computational overhead. The bottleneck lies in the complexity of modern webpages: VLMs must comprehend the global semantics of an entire page, resulting in substantial inference time and GPU memory usage. This raises a critical question: can we detect prompt injection attacks from screenshots in a lightweight manner? In this paper, we observe that injected webpages exhibit distinct characteristics compared to benign ones from both visual and textual perspectives. Building on this insight, we propose SnapGuard, a lightweight yet accurate method that reformulates prompt injection detection as multimodal representation analysis over webpage screenshots. SnapGuard leverages two complementary signals: a visual stability indicator that identifies abnormally smooth gradient distributions induced by malicious content, and action-oriented textual signals recovered via contrast-polarity reversal. Extensive evaluations across eight attacks and two benign settings demonstrate that SnapGuard achieves an F1 score of 0.75, outperforming GPT-4o-prompt while being 8x faster (1.81s vs. 14.50s) and introducing no additional memory overhead.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决**基于截图的Web代理面临的新型提示注入攻击威胁**。研究背景是：Web代理利用大模型自动执行网页操作，但攻击者可将恶意指令嵌入网页内容，诱导代理执行危险操作。现有防御方法主要依赖文本特征（如HTML/DOM），对直接处理渲染后截图而非结构化文本的截图型代理（如Anthropic的CUA、OpenAI的BUA等）完全失效。虽然存在多模态检测方法，但它们依赖大视觉语言模型（VLM）进行全页面全局语义理解，导致推理时间长达数秒、GPU内存消耗巨大，无法满足实时交互需求（用户可容忍延迟<4秒）。核心挑战在于：恶意内容可能仅占据页面极小区域甚至视觉上不可见，且代理运行有严格效率约束。本文提出的核心问题是：**能否从截图中以轻量级方式检测提示注入攻击？** 作者基于“被注入页面在视觉和文本上均存在异常特征”的观察，设计了一种无需VLM全页理解的快速检测方法。

### Q2: 有哪些相关研究？

相关研究主要分为攻击与防御两大类。在攻击方面，许多工作聚焦于操纵网页视觉内容诱导代理行为，如VWA-Adv通过商品图像扰动，WASP利用用户发布内容隐式注入指令，WebInject和经典弹窗攻击通过像素级扰动或恶意弹窗实施攻击。另一类攻击侧重指令注入，例如EIA通过隐藏HTML元素窃取信息，VPI-Bench和REDTEAM-CUA分别展示了对UI元素和操作系统界面的注入攻击。这些研究揭示了攻击面的广泛性与演化趋势。

在防御方面，现有方法多基于文本中心范式。早期Known-Answer Detection通过检测响应偏差识别恶意提示，后续方法利用LLM、嵌入分类器或训练模型区分恶意与良性文本。其他防御包括博弈论检测、自适应提示框架（如对抗性结构化越狱防御）、多模态模型微调（如Web防御框架的语义一致性分析）以及护栏机制（如规则检查、形式验证、安全-效用优化）。这些方法依赖于结构化或自由形式的文本表示，不适用于直接基于截图决策的Web代理。

本文SnapGuard与上述工作关键区别在于：针对截图型代理的独特性，将检测重构为多模态表示分析，利用视觉稳定性（识别恶意内容导致的异常梯度分布）和动作导向文本信号（通过对比极性反转恢复），无需依赖大规模VLM或文本表示。相较于基于VLM的多模态检测方法，SnapGuard在计算效率上显著提升（8倍加速且无额外内存开销），在涵盖八种攻击和两种良性设置的评估中F1达0.75，优于GPT-4o-prompt。

### Q3: 论文如何解决这个问题？

SnapGuard通过将提示注入检测重构为多模态表示分析，采用轻量级双分支架构解决截图型Web代理的防御问题。整体框架包含两个并行模块：视觉稳定性指示器（VSI）和文本信号提取分支，二者联合输出统一风险评分拦截恶意输入。

**视觉稳定性指示器（VSI）** 基于关键观察：恶意注入内容会引入空间弥散扰动，抑制局部结构变化，导致梯度分布异常平滑。该模块对输入截图计算灰度图后，统计所有像素点梯度幅值的方差\(\phi(x)\)，量化图像结构异质性。良性页面因具有多样局部结构而呈现高方差，恶意页面则因梯度均匀化而方差偏低。检测阈值\(\tau\)通过预设定假阳性率\(\alpha\)在良性数据集上标定，实现无参数、\(\mathcal{O}(HW)\)复杂度的轻量级检测。

**文本信号提取分支** 通过对比极性反转（Contrast-Polarity Reversal）增强弱对比度文本区域的可见性：对灰度强度>240的像素执行颜色反转（\(x \rightarrow 255-x\)），使原本与背景融合的浅色文字变为深色高对比度状态。随后对原始图和反转图分别执行OCR提取文本，再通过基于行为意图的分类体系（包括交互触发词、凭据请求、链接邀请、控制覆盖指令四类）进行模式匹配。该分类体系无需语义理解，每个检测决策可追溯至具体匹配模式，兼具可解释性与扩展性。

**创新点**在于：1）首次从视觉统计特征（梯度方差）检测注入攻击，避免VLM的全局语义计算开销；2）对比极性反转+OCR的轻量文本提取方案，无需大模型即可定位恶意文本指令。实验表明，SnapGuard在F1=0.75的同时，推理速度仅为GPT-4o的1/8（1.81s vs 14.50s），且无额外显存消耗。

### Q4: 论文做了哪些实验？

论文进行了全面的实验评估，使用WAInjectBench基准测试，包含948个良性样本（分嵌入式图像和截图两类）和2185个恶意样本（涵盖EIA、WebInject、Pop-up、WASP、VWA-emb/VWA-shot、VPI-BU/VPI-CU共八种攻击）。实验对比了五类图像检测方法和五类文本检测方法基线。主要结果如下：在图像检测方法中，SnapGuard以F1分数0.75、平均TPR 0.66、平均FPR 0.09全面领先，相比之下GPT-4o-prompt的F1为0.71但时间成本高达14.50秒，Embedding-I的F1仅0.52。在文本检测方法中，SnapGuard同样表现最优（所有基线F1均低于0.45）。关键成本指标显示SnapGuard推理仅需1.81秒且无额外内存消耗，而GPT-4o-prompt需14.50秒，文本方法需额外OCR时间（平均78.69秒）和GPU内存（7.9GB）。ROC分析显示SnapGuard的AUC达0.742（Embedding-I为0.652），在低FPR区域表现优异。鲁棒性实验表明SnapGuard在噪声扰动下仍保持约0.8的F1，并在不同文本提取接口下表现稳定（F1约0.76），而OCR接口时间成本仅1.8秒，远低于VLM接口（15-16秒）。消融实验验证了视觉稳定性指标、对比极性反转和行动导向模式检测三个组件的贡献。

### Q5: 有什么可以进一步探索的点？

SnapGuard在轻量级检测上表现出色，但未来仍有多个探索方向：首先，其检测基于视觉平滑度与行动文本特征，可能对刻意伪装成高文本密度或复杂布局的攻击失效，需研究更鲁棒的视觉-文本联合特征。其次，当前仅验证了8种攻击场景，实际攻击方式可能更隐蔽（如动态注入或跨层隐藏），需构建更大规模对抗性测试集。第三，模型依赖截图中的文字OCR结果，嘈杂或低分辨率情况下，行动文本提取的正负极性反转可能产生误判，可引入多视角截图融合或时序信息辅助。更根本上，能否将检测与防御结合，如动态重渲染页面以消除注入痕迹，或设计端到端的轻量CNN-Transformer混合架构，在保持速度优势的同时提升对未知攻击的泛化能力。

### Q6: 总结一下论文的主要内容

SnapGuard针对基于截图的网页代理面临的提示注入攻击威胁，提出了一种轻量级的检测方法。问题定义为从网页截图中检测恶意指令的嵌入，这些指令会诱导代理执行非预期操作。该方法核心创新在于将提示注入检测重构为多模态表示分析，利用两个互补信号：视觉稳定性指标，用于识别由恶意内容引起的异常平滑梯度分布；以及通过对比度极性反转从渲染页面恢复的面向动作的文本线索。主要结论是，在包含八种攻击和两种良性设置的全面评估中，SnapGuard取得了0.75的F1分数，优于GPT-4o-prompt的0.71，同时速度提升8倍（1.81秒对比14.50秒），且无额外内存开销。其核心贡献是提出一种无需大型视觉语言模型进行全局语义理解的轻量级方案，实现了准确性与效率的平衡，适合实时网页代理部署。
