---
title: "See and Fix the Flaws: Enabling VLMs and Diffusion Models to Comprehend Visual Artifacts via Agentic Data Synthesis"
authors:
  - "Jaehyun Park"
  - "Minyoung Ahn"
  - "Minkyu Kim"
  - "Jonghyun Lee"
  - "Jae-Gil Lee"
  - "Dongmin Park"
date: "2026-02-24"
arxiv_id: "2602.20951"
arxiv_url: "https://arxiv.org/abs/2602.20951"
pdf_url: "https://arxiv.org/pdf/2602.20951v1"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Agent 架构"
  - "多智能体系统"
  - "Agent 数据合成"
  - "视觉语言模型"
  - "扩散模型"
  - "视觉伪影"
  - "自动化标注"
  - "工具使用"
relevance_score: 8.5
---

# See and Fix the Flaws: Enabling VLMs and Diffusion Models to Comprehend Visual Artifacts via Agentic Data Synthesis

## 原始摘要

Despite recent advances in diffusion models, AI generated images still often contain visual artifacts that compromise realism. Although more thorough pre-training and bigger models might reduce artifacts, there is no assurance that they can be completely eliminated, which makes artifact mitigation a highly crucial area of study. Previous artifact-aware methodologies depend on human-labeled artifact datasets, which are costly and difficult to scale, underscoring the need for an automated approach to reliably acquire artifact-annotated datasets. In this paper, we propose ArtiAgent, which efficiently creates pairs of real and artifact-injected images. It comprises three agents: a perception agent that recognizes and grounds entities and subentities from real images, a synthesis agent that introduces artifacts via artifact injection tools through novel patch-wise embedding manipulation within a diffusion transformer, and a curation agent that filters the synthesized artifacts and generates both local and global explanations for each instance. Using ArtiAgent, we synthesize 100K images with rich artifact annotations and demonstrate both efficacy and versatility across diverse applications. Code is available at link.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决AI生成图像中普遍存在的视觉伪影问题，以及现有视觉语言模型在理解和处理这些伪影方面的能力不足。研究背景是，尽管扩散模型在生成高真实感图像方面取得了显著进展，但生成的图像仍常包含如多指、实体融合等不自然的视觉伪影，降低了图像的实用性和用户满意度，尤其在医疗、自动驾驶等高可靠性要求的领域，这一问题更为关键。同时，现有的视觉语言模型在视觉问答等任务中表现出色，但在面对AI生成图像中的伪影时，却难以有效检测、定位或解释，几乎等同于随机猜测，限制了其作为自动化系统的可靠性。

现有方法存在两大不足：一是主要针对早期扩散模型中常见的简单伪影类型（如高斯噪声、模糊），而现代模型产生的伪影更倾向于物理上合理的复杂扭曲，现有方法覆盖不足；二是严重依赖人工标注的伪影数据集，成本高昂且难以扩展，无法捕捉现代扩散模型生成伪影的多样性和规模。

因此，本文的核心问题是：如何以可扩展、无需人工标注的方式，生成大量多样且真实的视觉伪影数据，并利用这些数据提升视觉语言模型对伪影的理解能力，进而改善图像生成和编辑流程。为此，论文提出了ArtiAgent框架，通过智能体协同自动合成带有丰富注释的伪影图像，以支持对伪影的检测、定位和推理研究，并应用于下游任务。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：视觉伪影数据集和视觉伪影处理方法。

在**视觉伪影数据集**方面，已有工作如PAL、SynthScars和DiffDoctor，它们通过人工标注或半监督扩展，提供了像素级掩码或文本解释，用于训练和评估模型对伪影的感知、定位和解释能力。评估基准如RichHF-18K和LOKI则提供了带标注的区域或自然语言解释。然而，这些数据集严重依赖成本高昂且难以扩展的人工标注，且大多基于早期扩散模型的伪影，对现代生成系统更丰富多样的失败模式覆盖有限。本文提出的ArtiAgent通过智能体自动合成伪影数据，旨在克服这些限制，实现低成本、可扩展且更贴近当前模型缺陷的数据生成。

在**视觉伪影处理**方法上，研究如PAL、RichHF-18K、LEGION和DiffDoctor利用上述数据集训练分割、多模态或统一模型，以检测、定位伪影并通过修复、偏好学习或微调扩散模型来减轻伪影。这些方法强调了伪影检测与推理的价值，但同样受限于人工标注数据的规模。本文的ArtiAgent则专注于数据合成的自动化，通过感知、合成和策展三个智能体生成高质量的伪影标注数据，为后续处理模型提供更丰富、可靠的训练基础，从而在根本上减少对人工标注的依赖。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ArtiAgent的自动化智能体流水线来解决视觉伪影数据合成问题。该流水线由三个协同工作的智能体构成：感知智能体、合成智能体和策展智能体，旨在无需人工标注的情况下，高效生成带有丰富注释的伪影-真实图像对。

**整体框架与核心方法**：
1.  **感知智能体**：首先分析真实图像，利用视觉语言模型（VLM）将图像分解为实体（如“狗”）和子实体（如“鼻子”）的层次化词汇表。然后，使用Grounded-SAM模型对这些语义单元进行视觉定位和分割，并通过计算重叠率将子实体与其父实体关联起来，从而确定适合注入伪影的候选区域。
2.  **合成智能体**：这是方法的核心创新模块，负责将伪影注入图像。它包含两个关键组件：
    *   **工具箱**：根据感知结果，使用四种工具（添加、移除、扭曲、融合）生成“目标-参考”图像块映射关系。例如，“添加”工具会为子实体区域（参考块）在周围寻找合适的目标位置。
    *   **反转-注入模块**：这是一个基于扩散Transformer（DiT）的创新性结构伪影合成方法。它扩展了图像编辑中的反转-恢复范式，分为两个阶段：
        *   **反转阶段**：将输入图像编码到其对应的噪声潜在表示，并缓存每一Transformer层的值嵌入（Value Embeddings）。
        *   **注入阶段**：在去噪过程中，利用工具箱提供的映射关系，通过**位置嵌入注入**和**值嵌入注入**来操纵DiT自注意力层中的空间信息。具体而言，对于目标图像块，将其位置嵌入替换为其对应参考块的位置，并将其值嵌入替换为反转阶段缓存的参考块的值嵌入。这使得目标区域能从参考区域“借用”空间语义和内容，从而合成出结构上逼真的伪影，同时保持背景区域的原始内容不变。
3.  **策展智能体**：作为质量控制和数据增强环节。首先进行数据过滤：对于扭曲类伪影，使用LPIPS指标确保变化既明显又合理；对于添加、移除、融合类伪影，则使用VLM进行三元组对比判断，验证修改是否可感知且位于指定区域。随后，该智能体利用VLM为每个伪影区域生成**局部解释**（描述该区域的具体变化），并汇总所有局部解释为整张图像生成**全局解释**（说明为何这是一张有伪影的图像）。

**创新点**：
*   **全自动的智能体流水线**：首次构建了一个端到端的自动化系统，将视觉理解、伪影合成与数据策展流程化，摆脱了对昂贵人工标注的依赖。
*   **基于DiT的补丁级结构伪影合成**：提出的“反转-注入”范式，特别是**位置嵌入注入**与值注入的结合，是图像编辑领域的新方法，能够精确控制空间语义的转移，从而生成高质量的结构性伪影（如多余或缺失的肢体）。
*   **双重验证与解释生成**：结合感知指标（LPIPS）和语义理解（VLM）进行数据过滤，确保了合成数据的质量。同时，自动生成局部和全局文本解释，为下游任务提供了丰富的监督信号。
*   **多样化的伪影工具箱**：定义了四种基础的伪影操作，能够系统性地模拟多种常见视觉缺陷，增强了合成数据集的多样性和实用性。

### Q4: 论文做了哪些实验？

论文实验主要围绕评估ArtiAgent生成的数据在提升视觉语言模型（VLM）对AI生成图像中视觉伪影的理解能力，以及利用该能力进行图像生成引导和修复。实验设置包括三个核心任务：伪影检测、定位和解释。评估使用的基准测试是ArtifactBench，并采用了多个指标：检测任务使用准确率和F1分数，定位任务使用mIoU和F1分数，解释任务使用ROUGE和CSS分数。

对比方法包括三类基线：1）伪影分割算法（PAL、DiffDoctor、LEGION）；2）专有VLM（GPT-4o、Gemini-2.5-Pro、GPT-5）。作者使用ArtiAgent合成的10万张图像训练集，对开源VLM（Qwen2.5-VL-7B和InternVL3.5-8B）进行微调。

主要结果如下：在检测任务中，ArtiAgent将InternVL3.5-8B的准确率提升了26.5%，微调后的模型性能超越原始版本，并匹配或超过了GPT-5等专有系统。在定位任务中，ArtiAgent增强了VLM的空间 grounding 能力，尽管DiffDoctor在旧基准LOKI上表现良好，但在ArtifactBench上泛化不佳，凸显了新基准的挑战性。在解释任务中，微调模型在ROUGE和CSS指标上均有显著提升。数据规模实验显示，性能随训练数据量增加而持续提升，即使仅使用1K样本，在定位和解释任务上已超越GPT-5，体现了高效样本利用率。此外，实验还展示了两个应用：1）使用基于ArtiAgent数据训练的奖励模型（以CLIP为骨干）引导FLUX-schnell扩散模型在测试时生成更少伪影的图像，奖励值随搜索轮次稳步提升；2）利用训练好的VLM检测并定位伪影区域，引导FLUX修复模型进行迭代修复，直至VLM确认伪影消除，定性结果显示了有效的定位和修复能力。

### Q5: 有什么可以进一步探索的点？

该论文提出的ArtiAgent框架在自动化生成视觉伪影数据集方面取得了显著进展，但其局限性和未来探索方向仍值得深入。首先，框架依赖扩散模型生成伪影，其注入的伪影类型和分布可能受限于基础模型的生成能力，未能覆盖真实场景中所有复杂伪影（如跨物体边界的结构扭曲）。未来可探索更广泛的伪影模拟方法，例如结合物理渲染引擎或对抗性攻击，以生成更贴近实际错误的样本。其次，当前方法侧重于静态图像伪影，而视频生成中的时序伪影（如闪烁、抖动）同样关键，未来可将代理框架扩展至视频领域，引入时间维度分析。此外，伪影修复部分仅初步验证了引导扩散采样，尚未实现端到端的自动修正系统；未来可集成强化学习代理，动态迭代修复过程，并评估修复后图像的视觉保真度。最后，框架的评估主要基于合成数据，在真实用户生成内容上的泛化能力有待验证；未来需构建跨域基准测试，并探索少样本适应策略，以提升实用性和鲁棒性。

### Q6: 总结一下论文的主要内容

本文提出了一种名为ArtiAgent的自动化框架，旨在解决AI生成图像中视觉伪影的识别与修复问题。核心贡献在于通过多智能体协作，无需依赖昂贵的人工标注，自动合成大规模、高质量且带有详细注释的伪影图像数据集。

具体方法上，ArtiAgent包含三个智能体：感知智能体从真实图像中识别并定位实体与子实体；合成智能体通过创新的基于扩散变换器的分块嵌入操作，利用伪影注入工具向图像中引入伪影；策展智能体则对合成结果进行过滤，并为每个实例生成局部和全局的伪影解释。该方法高效生成了10万张带有丰富注释的伪影图像对。

主要结论表明，该方法合成的数据集在多种下游应用中均展现出有效性和通用性，为视觉伪影的自动化检测与缓解研究提供了可扩展的数据基础，推动了生成模型在提升图像真实感方面的进展。
