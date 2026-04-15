---
title: "Every Picture Tells a Dangerous Story: Memory-Augmented Multi-Agent Jailbreak Attacks on VLMs"
authors:
  - "Jianhao Chen"
  - "Haoyang Chen"
  - "Hanjie Zhao"
  - "Haozhe Liang"
  - "Tieyun Qian"
date: "2026-04-14"
arxiv_id: "2604.12616"
arxiv_url: "https://arxiv.org/abs/2604.12616"
pdf_url: "https://arxiv.org/pdf/2604.12616v1"
categories:
  - "cs.AI"
  - "cs.MM"
tags:
  - "多智能体"
  - "对抗攻击"
  - "越狱攻击"
  - "视觉语言模型"
  - "记忆机制"
  - "安全与对齐"
  - "评测基准"
relevance_score: 7.5
---

# Every Picture Tells a Dangerous Story: Memory-Augmented Multi-Agent Jailbreak Attacks on VLMs

## 原始摘要

The rapid evolution of Vision-Language Models (VLMs) has catalyzed unprecedented capabilities in artificial intelligence; however, this continuous modal expansion has inadvertently exposed a vastly broadened and unconstrained adversarial attack surface. Current multimodal jailbreak strategies primarily focus on surface-level pixel perturbations and typographic attacks or harmful images; however, they fail to engage with the complex semantic structures intrinsic to visual data. This leaves the vast semantic attack surface of original, natural images largely unscrutinized. Driven by the need to expose these deep-seated semantic vulnerabilities, we introduce \textbf{MemJack}, a \textbf{MEM}ory-augmented multi-agent \textbf{JA}ilbreak atta\textbf{CK} framework that explicitly leverages visual semantics to orchestrate automated jailbreak attacks. MemJack employs coordinated multi-agent cooperation to dynamically map visual entities to malicious intents, generate adversarial prompts via multi-angle visual-semantic camouflage, and utilize an Iterative Nullspace Projection (INLP) geometric filter to bypass premature latent space refusals. By accumulating and transferring successful strategies through a persistent Multimodal Experience Memory, MemJack maintains highly coherent extended multi-turn jailbreak attack interactions across different images, thereby improving the attack success rate (ASR) on new images. Extensive empirical evaluations across full, unmodified COCO val2017 images demonstrate that MemJack achieves a 71.48\% ASR against Qwen3-VL-Plus, scaling to 90\% under extended budgets. Furthermore, to catalyze future defensive alignment research, we will release \textbf{MemJack-Bench}, a comprehensive dataset comprising over 113,000 interactive multimodal jailbreak attack trajectories, establishing a vital foundation for developing inherently robust VLMs.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前多模态大语言模型（VLMs）安全防御中存在的深层语义漏洞问题，以及现有越狱攻击方法的局限性。研究背景是，随着VLMs的快速发展，其融合视觉与语言的能力极大地扩展了人工智能的应用范围，但也同时暴露了更广阔、更不受约束的攻击面。现有的安全对齐技术通常在单模态环境下有效，但难以泛化到多模态接口，视觉感知与文本生成之间的语义鸿沟成为了一个不受约束的通道，使得良性的视觉元素可能被武器化。

现有方法的不足主要体现在三个方面：首先，现有攻击方法（如文本操纵、像素扰动、排版攻击或有害图像）多停留在表面，依赖于静态启发式规则或固定模板，未能深入利用视觉数据内在的复杂语义结构，因此无法有效测试模型的深层推理能力，也容易被更新的安全护栏所缓解。其次，这些框架通常是“无状态”的单轮执行，缺乏持久记忆或分层策略探索，无法迭代优化攻击、从失败中学习或在不同的视觉上下文间迁移成功经验。最后，传统的对抗性提示生成忽略了模型内部的安全潜在空间，容易触发模型的过早拒绝响应，导致查询浪费，尤其难以应对具有几何防御（如激活导向）的模型。

本文要解决的核心问题是：如何系统性地暴露和利用VLMs在视觉语义层面的根本性安全漏洞。为此，论文提出了MemJack框架，旨在通过记忆增强的多智能体协作，克服上述不足。具体而言，它通过动态的视觉语义伪装来克服静态启发式方法的局限，通过持久的多模态经验记忆实现跨图像、多轮次的连贯攻击以克服无状态执行的缺陷，并利用迭代零空间投影几何过滤器来绕过模型在潜在空间的过早拒绝，从而实现对原始自然图像的高效、自动化越狱攻击。最终目标是揭示这些深层次的语义脆弱性，并为构建本质上更鲁棒的VLMs提供研究基础和数据支持。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为以下几类：

**1. 文本攻击方法迁移类**：这类方法不真正利用图像，而是将针对大语言模型（LLM）的文本越狱策略（如GCG、AutoDAN）直接迁移到VLM的文本通道。它们在多模态安全对齐较强的模型上性能会显著下降。

**2. 像素空间对抗扰动类**：这类方法直接在像素空间构建对抗性扰动（如Visual Adversarial Examples、AnyAttack、BAP），揭示了视觉编码空间的安全漏洞，但通常依赖于对图像的细粒度修改，且易受压缩和预处理的影响。

**3. 构造新攻击图像类**：这类方法不直接修改原图，而是构造新的攻击图像（如FigStep、HADES），证明图像本身可作为攻击锚点。但它们通常依赖于偏离原始图像分布的人工构造视觉内容，或对图像进行大幅修改。

**4. 自动化红队代理类**：这类方法（如PAIR、TAP）通过迭代重写攻击提示或结合树搜索剪枝，将攻击构建为多轮对话，减少了对手工制作的依赖，提高了可扩展性，但将每次攻击视为独立事件。AutoDAN-Turbo更进一步，通过维护终身策略库来跨模型发现、存储和重用有效策略，证明了持久记忆对攻击泛化的关键作用。更广泛的智能体记忆研究（如Reflexion、Voyager、HippoRAG）也证实了经验反思、策略巩固和结构化检索对长视野任务的价值。

**5. 跨模态交互漏洞探索类**：近期研究（如Cross-Modal Entanglement、SI-Attack、HIMRD、CS-DJ、JailBound）从输入重组、风险语义分解、干扰效应、跨模态纠缠和内部安全边界等角度，揭示了VLM在模态交互中的漏洞。而IDEATOR、MML、SSA等则引入了自生成攻击样本、跨模态联动、多轮代理交互等机制，推动了多模态越狱从静态构造向更复杂的自动化攻击发展。

**本文与这些工作的关系和区别**：
MemJack属于自动化红队代理的范畴，但与现有工作有显著区别。现有攻击记忆系统（如AutoDAN-Turbo）仅在纯文本策略空间运行，没有融入视觉语义线索、攻击目标映射或用于跨图像策略转移的成功/失败反馈。MemJack填补了这一空白，首次系统性地探索了未经修改的良性图像是否可作为可重用的攻击锚点，以及显式的多模态记忆是否能促进跨不同视觉上下文的策略转移。它通过引入一个**有状态的、记忆增强的范式**，利用视觉语义来协调自动化越狱攻击，并通过持久的多模态经验记忆实现跨图像的高度连贯的多轮攻击交互。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为MemJack的记忆增强多智能体越狱攻击框架来解决利用视觉语义进行自动化、高效越狱攻击的问题。其核心方法是构建一个由三个智能体阶段驱动的闭环“规划-攻击-反思”流程，并辅以跨图像持久记忆模块，从而系统性地挖掘和利用视觉语言模型（VLM）的深层语义漏洞。

**整体框架与主要模块**：
MemJack的架构包含一个迭代的三阶段攻击流水线和两个支撑性的记忆模块。
1.  **三阶段攻击流水线**：
    *   **阶段一：战略规划**。由战略规划智能体执行，其核心是脆弱性规划器。它分析输入图像，识别可被利用的“视觉锚点”（如实体、场景、关系），并将其映射到与受害者模型安全策略对齐的攻击目标上，输出按置信度排序的漏洞描述符。规划过程遵循四个优先级（直接威胁、基于场景的威胁、社会/心理威胁、关系威胁）并受真实性约束。
    *   **阶段二：迭代攻击**。由迭代攻击智能体执行。它基于选定的视觉锚点和攻击目标，通过六种互补的攻击角度生成对抗性提示。这六个角度（如视觉直觉关联、场景故事扩展、第一人称角色视角等）旨在将恶意意图伪装成合法的视觉分析。在将提示发送给受害者模型前，会使用基于迭代零空间投影（INLP）的几何过滤器进行预筛选，以降低因潜在表示过于接近“拒绝方向”而导致的早期拒绝概率。
    *   **阶段三：评估与反馈**。由评估与反馈智能体执行。它使用安全守卫对受害者模型的响应进行连续风险评分。若攻击失败（评分低于阈值），反思模块会诊断防御模式（如直接拒绝、说教、良性重构等），推荐下一个攻击角度并生成战术建议，甚至直接生成修正后的提示。当某个锚点下的所有角度均耗尽或达到预算时，控制流返回阶段一进行重新规划。

2.  **两个持久记忆模块**：
    *   **多模态经验记忆**：这是一个跨图像运作的模块，通过FAISS索引存储和检索成功的攻击策略。它维护视觉、目标和策略三个嵌入空间，支持基于嵌入相似性和效用值（Q值）的跨图像策略迁移与重用。策略的效用值通过时序差分学习进行更新。
    *   **越狱知识图谱**：以结构化图的形式捕获攻击要素（锚点、目标、策略）与防御模式之间的因果关系。边权重根据历史成功/失败计数动态更新。该图谱能为后续攻击提供绕过特定防御的建议，并指导提示生成（如作为蒙特卡洛树搜索的先验）。

**关键技术及创新点**：
1.  **语义驱动的多智能体协同**：将复杂的越狱攻击任务分解为由专门智能体负责的规划、攻击、评估子任务，通过闭环协作系统性地探索视觉语义与恶意意图的映射。
2.  **多角度视觉语义伪装**：定义了六种基于社会工程学的攻击角度，从不同认知层面构造对抗提示，深度利用视觉内容的语义结构进行伪装，超越了表面级的像素扰动。
3.  **INLP几何过滤**：创新性地将迭代零空间投影应用于对抗提示的预筛选，主动将提示的潜在表示投影到模型“拒绝方向”的零空间，以绕过潜在的早期语义拒绝机制。
4.  **跨图像经验积累与迁移**：通过多模态经验记忆和知识图谱，使框架能够积累攻击经验，形成结构化知识，从而在面对新图像时能更快速、更有效地发起攻击，实现了攻击能力的持续进化。
5.  **细粒度反思与动态重规划**：基于连续风险评分的反馈机制，以及针对不同防御模式的反思诊断，使得攻击能够动态调整策略，显著提升了在多轮交互中达成越狱的连贯性和成功率。

### Q4: 论文做了哪些实验？

论文实验主要包括以下几个方面：

**实验设置**：MemJack框架使用Qwen3-VL-8B-Instruct作为漏洞规划器和攻击代理的主干模型，Qwen3-VL-Embedding-8B用于INLP过滤器。默认每张图像的最大攻击轮次预算R=20。关键参数包括角度切换阈值τ=2、进化优化种群大小N=4、代数G=2、交叉/变异率0.4、拒绝残差阈值ε=0.15等。

**数据集与基准测试**：
- 主要评估使用完整的、未经修改的COCO val2017数据集（5000张自然图像，15个场景类别）。
- 使用COCO train2017的150张分层子集（15个类别×10张）进行跨模型和消融实验。
- 为评估跨分布泛化能力，额外在多个基准上测试：AdvBench-M (N=729)、MM-SafetyBench (N=260)、SIUO (N=167)、FigStep (N=500)、VLBreakBench (N=916)、JailbreakV-RedTeam2K (N=2000)和MMBench-en (N=1164)。

**评估模型**：评估了11个VLM，涵盖商业API和开源模型。商业API模型包括Qwen3-VL-Plus、Gemini-3-Flash、GPT-5-Mini等；开源模型包括Qwen3-VL-8B-Instruct、Llama-3.2-11B-Vision-Instruct等。攻击成功率由自动化安全评估器Qwen3Guard-Gen-8B判定。

**对比方法**：与两类基线方法比较：(i) 纯文本攻击：GCG和AutoDAN-Turbo；(ii) 多模态攻击：Visual-Adv、FigStep、HADES和QR-Attack。白盒方法在Qwen3-VL-8B-Instruct上评估，黑盒方法在Qwen3-VL-Plus上评估。

**主要结果与关键指标**：
1. **有效性**：在COCO val2017上对Qwen3-VL-Plus攻击，MemJack达到71.48%的总体攻击成功率，平均仅需5.18轮成功。其中68.3%的成功攻击在前6轮内完成，89.1%在10轮内完成。
2. **泛化性**：在多个不同分布的数据集上，ASR保持在62%-91%之间（如FigStep上达91%）。当轮次预算增至R=100时，在COCO子集上ASR可达90%。
3. **跨模型评估**：所有测试模型均表现出不同程度脆弱性，ASR范围从Gemini-3-Flash的35%到Mistral-Medium-3的82%。
4. **基线对比**：MemJack黑盒设置ASR达72%，白盒设置达53%，显著优于所有基线（最佳基线AutoDAN-turbo为30%，多模态基线最高为17%）。
5. **消融研究**：移除记忆模块使ASR从72%降至38%，平均轮次从5.38增至9.11；移除反思或重规划模块也使性能下降。
6. **记忆机制分析**：视觉索引增长至65,973条，策略索引至22,521条，重用比达6.2倍，证实了跨图像策略迁移的有效性。
7. **攻击模式**：视觉直观关联、实践知识和假设推理是最主要的三种攻击角度，共占尝试的74%以上。直接伪装成功占72.6%，反思模块挽救占27.4%。

### Q5: 有什么可以进一步探索的点？

该论文提出的MemJack框架虽然在多模态越狱攻击上取得了显著效果，但仍存在一些局限性，为未来研究提供了多个探索方向。首先，其攻击依赖于对目标模型（如Qwen-VL）内部拒绝机制的逆向工程与几何过滤，这种“白盒”或“灰盒”假设在现实黑盒场景中可能不适用，未来可探索更普适、无需模型内部信息的黑盒攻击方法。其次，框架的效能严重依赖于多智能体协作与经验记忆的构建，计算开销和复杂度较高，如何设计更轻量、高效的攻击策略是一个重要方向。

从防御角度看，论文释放的基准数据集MemJack-Bench为开发鲁棒对齐技术奠定了基础，但当前的防御研究可能仍滞后于此类复杂的语义攻击。未来可探索更具前瞻性的防御机制，例如在训练中主动注入类似的复杂多轮对抗样本，或构建能够实时检测并中断“视觉-语义伪装”模式的监控模块。此外，攻击目前主要针对静态图像，未来可扩展到视频、音频等多模态时序数据，研究其在动态上下文中的攻击与防御。最后，该工作揭示了VLMs深层的语义脆弱性，这促使我们反思当前对齐技术的本质——或许需要超越指令微调和RLHF，从模型架构层面（如改进跨模态融合机制）设计更根本的安全解决方案。

### Q6: 总结一下论文的主要内容

该论文针对视觉语言模型（VLMs）的安全漏洞，提出了一种新型的多模态越狱攻击框架MemJack。核心问题是现有攻击方法（如像素扰动或有害图像）未能深入利用视觉数据内在的复杂语义结构，导致大量自然图像的语义攻击面未被充分探测。

论文的核心贡献是设计了MemJack框架，它通过记忆增强的多智能体协作来发起自动化语义越狱攻击。方法上，首先通过多智能体动态地将图像中的视觉实体映射到恶意意图；然后生成多角度的视觉-语义伪装对抗提示；并利用迭代零空间投影（INLP）几何过滤器来规避模型的早期拒绝。关键创新在于引入了一个持久的多模态经验记忆库，用于积累和迁移成功的攻击策略，从而在不同图像间维持连贯的多轮次攻击，提升对新图像的攻击成功率。

主要结论显示，MemJack在未经修改的COCO val2017数据集上对Qwen3-VL-Plus模型的攻击成功率（ASR）达到71.48%，在扩展预算下可提升至90%。其意义在于首次系统性地利用深层语义结构进行攻击，暴露了VLMs的严重安全风险。同时，论文将发布包含超过11.3万条交互轨迹的MemJack-Bench数据集，为未来开发具有内在鲁棒性的VLMs提供了重要的研究基础。
