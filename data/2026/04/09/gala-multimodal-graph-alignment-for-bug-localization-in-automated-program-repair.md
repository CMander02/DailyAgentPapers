---
title: "GALA: Multimodal Graph Alignment for Bug Localization in Automated Program Repair"
authors:
  - "Zhuoyao Liu"
  - "Zhengran Zeng"
  - "Shu-Dong Huang"
  - "Yang Liu"
  - "Shikun Zhang"
  - "Wei Ye"
date: "2026-04-09"
arxiv_id: "2604.08089"
arxiv_url: "https://arxiv.org/abs/2604.08089"
pdf_url: "https://arxiv.org/pdf/2604.08089v1"
github_url: "https://github.com/lzyyyyy666/GALA"
categories:
  - "cs.SE"
tags:
  - "Multimodal Agent"
  - "GUI Agent"
  - "Automated Program Repair"
  - "Tool Use"
  - "Graph Alignment"
  - "SWE-bench"
relevance_score: 7.5
---

# GALA: Multimodal Graph Alignment for Bug Localization in Automated Program Repair

## 原始摘要

Large Language Model (LLM)-based Automated Program Repair (APR) has shown strong potential on textual benchmarks, yet struggles in multimodal scenarios where bugs are reported with GUI screenshots. Existing methods typically convert images into plain text, which discards critical spatial relationships and causes a severe disconnect between visual observations and code components, leading localization to degrade into imprecise keyword matching. To bridge this gap, we propose GALA (Graph Alignment for Localization in APR), a framework that shifts multimodal APR from implicit semantic guessing to explicit structural reasoning. GALA operates in four stages: it first constructs an Image UI Graph to capture visual elements and their structural relationships; then performs file-level alignment by cross-referencing this UI graph with repository-level structures (e.g., file references) to locate candidate files; next conducts function-level alignment by reasoning over fine-grained code dependencies (e.g., call graphs) to precisely ground visual elements to corresponding code components; and finally performs patch generation within the grounded code context based on the aligned files and functions. By systematically enforcing both semantic and relational consistency across modalities, GALA establishes a highly accurate visual-to-code mapping. Evaluations on the SWE-bench Multimodal benchmark demonstrate that GALA achieves state-of-the-art performance, highlighting the effectiveness of hierarchical structural alignment.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的自动程序修复（APR）在处理多模态场景（即包含GUI截图的错误报告）时的定位难题。研究背景是，现代软件开发，尤其是前端系统中，错误报告常包含截图，这些视觉信息承载了文本无法完全捕捉的布局、渲染和交互问题。现有方法通常利用视觉大语言模型（vLLM）将图像转换为纯文本描述，然后将其作为补充上下文注入传统的单模态故障定位和修复流程。这种范式存在两个根本不足：一是丢失了视觉结构关系，例如UI元素间的空间和交互关系（如重叠）在文本描述中被舍弃；二是由于视觉与代码之间存在割裂，定位退化为不精确的语义关键词匹配，导致模型可能检索到语义相似但不相关的代码文件，而非真正导致错误的布局组件。

因此，本文要解决的核心问题是：如何克服现有方法因忽略视觉结构信息和依赖隐式语义匹配而导致的定位不准确问题。为此，论文提出了GALA框架，其核心是将多模态错误定位重新定义为一种结构化的跨模态对齐问题。GALA通过构建图像UI图来显式保留视觉结构，并设计分层图对齐机制，依次在文件级和函数级将视觉元素与代码库的结构（如文件引用关系、函数调用图）进行对齐，从而在语义和关系上建立一致、精确的视觉到代码的映射，将多模态APR从隐式的语义猜测转变为显式的结构推理。

### Q2: 有哪些相关研究？

相关研究主要可分为方法类、应用类与评测类。在方法类中，训练式方法（如DNNLOC、FBL-BERT、BLAZE）通过监督学习对齐错误报告与代码，依赖任务特定训练且难以适应代码库演化；提示式方法则利用LLM的推理能力，通过检索与结构化推理（如迭代推理、基于智能体的框架）进行定位，并引入代码图等结构表示以约束搜索空间，但这些方法均为单模态，无法处理视觉语义。在应用类中，自动程序修复（APR）研究早期聚焦函数级修复，近期转向仓库级问题解决（如SWE-agent），但同样缺乏视觉整合机制；多模态APR工作（如GUIRepair、SVRepair）开始融入视觉输入，但多依赖隐式或弱结构化的视觉表示，未能显式建模细粒度UI元素及其关系。评测类方面，SWE-bench Multimodal等新兴基准推动了多模态软件推理场景的发展。本文提出的GALA与上述工作的核心区别在于，它通过构建显式的图像UI图来捕获视觉元素的结构关系，并执行分层图对齐（文件级与函数级），实现跨模态的结构化推理，从而弥补了现有方法在视觉语义丢失和关系依赖性建模不足的缺陷。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为GALA的基于图结构的框架来解决多模态Bug定位问题。该框架的核心思想是将多模态APR从隐式的语义猜测转变为显式的结构推理，通过层次化的图对齐来桥接视觉症状与代码语义。其整体框架分为四个阶段，每个阶段都通过简化的提示词进行实例化。

首先，**构建图像UI图**：GALA不是简单地将图像转换为纯文本，而是构建一个以问题为中心的结构化图像图。该图通过类型识别、根对象选择、支持节点扩展和关系构建四个子步骤，仅保留与问题相关的视觉元素及其结构关系，形成一个稀疏但信息丰富的局部子结构，避免了全局视觉解析引入的无关噪声。

其次，**文件级对齐**：此阶段旨在在仓库级别进行粗粒度的跨模态定位。方法结合了仓库结构、视觉语义和文件间依赖关系。具体包括：1）构建过滤后的仓库目录树；2）基于问题描述和图像图摘要，进行视觉语义引导的候选文件检索；3）通过构建候选文件依赖图，进行结构感知的细化，最终输出一个依赖一致且语义相关的种子文件集合，大幅缩小了搜索空间。

接着，**函数级对齐**：在选定的种子文件内，GALA构建一个面向UI的封闭域函数图，其中节点是函数或组件级单元，边编码UI相关的交互（如渲染、状态更新）。随后，进行跨模态图对齐：模型基于问题描述、图像图和函数图，将图像节点与候选函数节点进行对齐，但仅保留那些语义兼容且**关系一致的邻域证据**所支持的对应关系。这通过结合实体定位和关系感知验证，过滤了结构不一致的匹配。

最后，**基于图引导的补丁生成**：在已对齐的子图基础上，模型识别出具体的编辑目标函数，并将修复过程约束在已对齐的图结构上下文中，从而生成有针对性和可靠的代码修改。

**创新点**在于：1）**问题中心的层次化图对齐**：从图像到代码，通过文件级和函数级两个层次的图结构进行对齐，系统性强制了跨模态的语义和关系一致性。2）**结构感知的推理**：在文件级利用依赖图进行细化，在函数级要求视觉关系与代码交互模式兼容，超越了单纯的语义匹配。3）**高效的图构建与表示**：图像图仅保留问题相关子结构，代码图聚焦UI相关交互，并通过摘要形式输入LLM，降低了计算开销。

### Q4: 论文做了哪些实验？

论文在SWE-Bench Multimodal基准测试上进行了全面的实验评估。实验设置方面，GALA使用Qwen3.5系列大语言模型（包括35B和122B参数版本）作为基础模型，负责视觉理解、代码定位和补丁生成全流程。模型在推理时温度设为0.0以确保输出确定性，并在配备NVIDIA A800 GPU的多GPU服务器上运行。

数据集采用SWE-Bench Multimodal，该基准包含来自17个JavaScript仓库的517个测试任务，每个任务都包含自然语言描述和视觉输入（如截图），要求模型进行多模态推理和跨语言代码修改。

对比方法包括多个先进的多模态程序修复方法：SWE-Agent Multimodal、Agentless Lite、Zencoder、OpenHands-Versa、GUIRepair和SVRepair。为公平比较，论文使用相同的基础模型重新实现了GUIRepair和SVRepair。

主要结果如下：在端到端修复性能上，GALA（使用Qwen3.5-122B-A10B）取得了35.40%的解决率（Pass@1），优于GUIRepair（34.82%）、OpenHands-Versa（34.43%）和SVRepair（33.66%）。在定位性能上，GALA在文件级和函数级召回率上均表现最佳：使用122B模型时，文件级召回率为29.22%，函数级为17.14%；使用35B模型时，文件级为28.22%，函数级为15.88%，均超过基线方法。

消融实验表明，引入图像图可将性能从33.66%提升至34.43%，而同时启用图像图、代码图和对齐机制后，性能达到最高的35.40%。代码图粒度分析显示，结合文件级和函数级图能获得最佳性能（35.40%），优于仅使用文件级图（34.62%）或无结构化图（34.43%）的设置。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要在于受限于当前大语言模型的上下文容量，难以实现视觉元素与代码行级别的细粒度对齐，因此采用了从文件到函数的层次化对齐策略。这导致方法对代码库的组织结构较为敏感，在命名模糊或模块化程度高的场景下性能可能下降。此外，框架依赖外部结构化中间表示作为推理支架，未来随着大语言模型和智能体系统的发展，这种结构可能被内化，实现更直接的端到端推理。

未来可探索的方向包括：1）结合代码语义嵌入与视觉特征，设计更精细的跨模态对齐机制，以突破当前行级对齐的瓶颈；2）引入动态推理机制，使模型能自适应不同代码库结构和命名规范，减少对预设结构的依赖；3）探索将结构化对齐过程逐步融入大语言模型预训练或微调中，实现显式引导与隐式推理的更好平衡；4）扩展框架以支持更多模态（如操作日志、用户反馈），构建更全面的程序理解与修复系统。

### Q6: 总结一下论文的主要内容

本文提出GALA框架，将多模态自动程序修复中的缺陷定位问题转化为层次化的跨模态图对齐任务。核心贡献在于通过结构化建模与对齐，解决现有方法因将图像简单转为文本而丢失空间关系、导致视觉观察与代码组件脱节的问题。方法上，GALA首先构建图像UI图以捕捉视觉元素及其结构关系，随后进行文件级对齐（通过交叉引用UI图与仓库级结构定位候选文件）和函数级对齐（通过细粒度代码依赖推理将视觉元素精确映射到代码组件），最后在已对齐的代码上下文中生成补丁。实验表明，GALA在SWE-bench Multimodal基准上取得了最先进的性能，验证了结构感知对齐在多模态程序修复中的有效性，并为基于图的多模态软件工程开辟了新方向。
