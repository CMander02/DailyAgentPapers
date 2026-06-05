---
title: "DragOn: A Benchmark and Dataset for Drag-Based GUI Interactions"
authors:
  - "Nathan Bout"
  - "Maxime Langevin"
  - "Ronan Riochet"
date: "2026-06-04"
arxiv_id: "2606.06322"
arxiv_url: "https://arxiv.org/abs/2606.06322"
pdf_url: "https://arxiv.org/pdf/2606.06322v1"
categories:
  - "cs.AI"
tags:
  - "GUI Agent"
  - "Drag Grounding"
  - "Visual Language Model"
  - "Benchmark"
  - "Dataset"
  - "Agent Training"
  - "Human-Computer Interaction"
relevance_score: 9.5
---

# DragOn: A Benchmark and Dataset for Drag-Based GUI Interactions

## 原始摘要

GUI agents - vision-based models that control desktops, web browsers, and mobile devices through graphical user interfaces - promise to automate a wide range of digital tasks. While million-scale datasets have enabled substantial progress on click-grounding, drag grounding (e.g. drag-and-drop, swipe, highlight) data remains an order of magnitude smaller and current models fall short on complex drag-based interactions. We introduce DragOn, a drag grounding benchmark and training dataset covering four domains: text highlighting, cell selection, element resizing and slider manipulation. The dataset comprises 286K training screenshots and 3.5M training tasks, plus a 2000-example held-out evaluation suite. We evaluate proprietary (GPT, Claude) and open-weight (Qwen, Kimi, Holo) models, as well as a Qwen VLM fine-tuned on our training data. Results suggest that our dataset could improve performance of state-of-the-art models on downstream computer-use tasks.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决GUI智能体中拖拽动作的视觉定位（drag grounding）能力严重不足的问题。研究背景是，随着大型语言模型和视觉语言模型的发展，基于图形用户界面的自动化代理需求日益增长，而视觉定位（将自然语言指令映射到屏幕区域）是实现这一目标的核心。现有方法主要关注点击定位（click grounding），得益于百万级数据集（如OS-ATLAS、UGround），点击定位已取得显著进展。然而，对于拖拽定位（drag grounding，如拖放、滑动、高亮等操作），可用数据规模小了一个数量级，且主要局限于文本高亮任务。这种数据匮乏导致现有模型在复杂的拖拽交互任务上表现不佳。为此，本文提出了DragOn基准与数据集，通过“渲染即监督”原则，利用渲染器（PDF、XLSX等）的几何信息作为标注函数，低成本构建了包含28.6万张截图和350万任务的训练集，覆盖文本高亮、单元格选择、元素缩放和滑块操作四个领域。核心目标是提供一个大规模、多样化的拖拽定位基准，推动模型在该任务上的性能提升。实验表明，当前前沿模型（GPT、Claude等）在该基准上准确率均低于30%，凸显了拖拽定位的挑战性。

### Q2: 有哪些相关研究？

相关研究主要分为四类。首先是计算机使用智能体（Computer-Use Agents），如MAI-UI、Surfer 2和UI-TARS-2，它们构建通用GUI智能体，但本文认为这些端到端基准测试（如OSWorld、AndroidWorld、WebVoyager）仅衡量整体任务成功率，无法诊断具体感知与动作缺陷。本文通过分析发现OSWorld和AndroidWorld中分别有13.9%和82.8%的任务需要拖拽动作，凸显了拖拽接地研究的必要性。

其次是接地数据集（Grounding Datasets）研究，包括SeeClick、OS-ATLAS、UGround、ScreenSpot-Pro以及Aria-UI、GUI-Actor等。这些工作聚焦于点按操作接地，收集了百万级标注数据。本文指出它们几乎完全忽略了拖拽类连续交互，而DragOn专门填补这一空白，提供286K截图和350万训练任务，涵盖文本高亮、单元格选择、元素缩放和滑块操作四个领域。

第三类是程序化与合成监督（Programmatic and Synthetic Supervision），如DocBank和Donut利用渲染器作为精确标签源。本文借鉴其思路但不同之处在于，DragOn的标签映射是查询条件式的，同一截图对可支持任意粒度的子结构定位。

最后是两项专门的拖拽接地工作：GUI-Drag聚焦文本选择，本文将其扩展为四域之一并采用PDF坐标替代OCR实现像素级精度；ShowUI-π则采用流式生成模型预测连续拖拽轨迹。与之相比，DragOn数据集规模大1-2个数量级，并新增了单元格选择和滑块操作两个未探索领域。

### Q3: 论文如何解决这个问题？

论文通过“渲染即监督”（Rendering-as-Supervision）这一核心方法论，构建了DragOn数据集和基准。整体框架围绕四个拖拽交互领域（文本高亮、单元格选择、元素缩放、滑块操作）设计，每个领域均采用统一的(S, R, π)三元组——S为结构化源数据，R为确定性渲染器，π为标签映射函数。关键技术包含两种标签映射：解析式标签映射直接通过几何计算（如PDF文本坐标、PPTX的EMU单位转换）获取像素级边界框；探针式标签映射则通过扰动渲染（如用特征色填充单元格）再恢复定位，适用于无闭式解的渲染场景（如电子表格）。

架构上，每个领域有专属自动化流水线：文本高亮利用Wikipedia文章生成DOCX文档，通过LibreOffice转PDF后提取坐标；单元格选择基于Pandas生成XLSX文件，在Docker容器中运行LibreOffice Calc，通过颜色探针定位；元素缩放从Zenodo语料库解析PPTX的EMU几何数据；滑块操作则通过Playwright渲染HTML页面，从URL参数和轨迹几何计算位置。所有流水线输出包含截图、自然语言指令及拖拽起止框坐标，并应用图像增强（JPEG压缩、模糊、抖动等）提升鲁棒性。

创新点在于：1）首次系统解决拖拽交互的标注难题，生成286K截图和350万训练任务；2）通过渲染过程直接提取标注，避免人工标注成本；3）覆盖四种复杂拖拽类型，且指令模板融合文本内容、位置、语义角色等多维度信息；4）对旋转/缩放等连续动作定义了包含容错率的评估指标（acc@10%、acc@15%），更贴合实际应用场景。

### Q4: 论文做了哪些实验？

论文在DragOn基准上对多种模型进行了评估，包含闭源通用模型（通过公共API访问）和开源视觉语言模型（本地部署）。所有模型都使用结构化JSON输出四个拖拽坐标。实验设置上，研究人员基于Qwen3.5-VL-35B-A3B模型在训练集上进行微调，采用Adam优化器，学习率1e-6，序列长度20480，全局batch size为64，在32块Nvidia H100 GPU上训练了1000步（约2个epoch）。数据集包含28.6万张训练截图和350万个训练任务，以及2000个样本的测试集。对比方法包括Claude Sonnet 4.5、Claude Opus 4.7、GPT-5.4、Kimi-K2.5、Qwen3.5-VL系列（35B、122B、397B参数）以及Holo3-35B-A3B。主要结果以成功率（%）为指标：最佳模型（Our 35B-A3B）在总成功率达35.3%，显著优于其他模型。次优的Claude Opus 4.7为27.7%，GPT-5.4为25.7%。在四个子任务中，Our 35B-A3B在文本高亮（33.2%）、滑块操作（62.8%）和元素调整大小（32.0%）上领先，但在单元格选择（13.2%）上弱于Claude Opus 4.7（37.2%）。在容忍精度上，Our 35B-A3B在acc@10%和acc@15%上分别为46.8%和57.2%，显示大多数剩余误差为小幅偏移而非定性错误。

### Q5: 有什么可以进一步探索的点？

首先，当前DragOn数据集仅覆盖了文本高亮、单元格选择、元素拖拽和滑块操作这四个特定领域，远未涵盖GUI中所有拖拽交互类型，如文件拖拽到文件夹、画布上的自由绘制等。未来可以扩展更多元化的拖拽场景，并增加多步骤组合任务，以更贴近真实用户操作。

其次，论文虽展示了微调模型优于闭源模型，但未深入探讨模型泛化能力。例如，在未见过的GUI布局或屏幕分辨率上表现如何？建议引入领域泛化测试，并探索融合点击和拖拽的联合训练策略，使模型能同时处理多种交互。

此外，当前基准测试仅评估了拖拽定位精度，缺乏对下游任务完成率的衡量。可设计端到端任务（如用拖拽整理桌面文件）来评估实际效能。最后，可尝试引入多模态对齐技术，利用结构化元数据（如UI层级树）辅助训练，减少对大量标注数据的依赖，并提升模型的零样本迁移能力。

### Q6: 总结一下论文的主要内容

DragOn 基准与数据集专门针对 GUI 中的拖拽交互（如拖放、滑动、高亮）进行研究。当前视觉语言模型在点击定位上已有显著进步，但拖拽操作的数据量小一个数量级，导致性能不足。该工作构建了包含文本高亮、单元格选择、元素缩放和滑块操作四个领域的训练集，包含28.6万张截图和350万个任务，并附带2000个样本的评估集。通过评估GPT、Claude等闭源模型以及Qwen、Kimi等开源模型，并微调Qwen VLM，结果表明该数据集能有效提升模型在复杂拖拽任务上的表现，对推动GUI自动化操作具有重要意义。
