---
title: "VANGUARD: Vehicle-Anchored Ground Sample Distance Estimation for UAVs in GPS-Denied Environments"
authors:
  - "Yifei Chen"
  - "Xupeng Chen"
  - "Feng Wang"
  - "Niangang Jiao"
  - "Jiayin Liu"
date: "2026-03-04"
arxiv_id: "2603.04277"
arxiv_url: "https://arxiv.org/abs/2603.04277"
pdf_url: "https://arxiv.org/pdf/2603.04277v1"
categories:
  - "cs.RO"
  - "cs.AI"
tags:
  - "Tool Use & API Interaction"
  - "Perception & Multimodal"
relevance_score: 5.5
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Perception & Multimodal"
  domain: "Robotics & Embodied"
  research_type: "New Method/Model"
attributes:
  base_model: "N/A"
  key_technique: "VANGUARD (Vehicle-Anchored Ground Sample Distance Estimation)"
  primary_benchmark: "DOTA v1.5"
---

# VANGUARD: Vehicle-Anchored Ground Sample Distance Estimation for UAVs in GPS-Denied Environments

## 原始摘要

Autonomous aerial robots operating in GPS-denied or communication-degraded environments frequently lose access to camera metadata and telemetry, leaving onboard perception systems unable to recover the absolute metric scale of the scene. As LLM/VLM-based planners are increasingly adopted as high-level agents for embodied systems, their ability to reason about physical dimensions becomes safety-critical -- yet our experiments show that five state-of-the-art VLMs suffer from spatial scale hallucinations, with median area estimation errors exceeding 50%. We propose VANGUARD, a lightweight, deterministic Geometric Perception Skill designed as a callable tool that any LLM-based agent can invoke to recover Ground Sample Distance (GSD) from ubiquitous environmental anchors: small vehicles detected via oriented bounding boxes, whose modal pixel length is robustly estimated through kernel density estimation and converted to GSD using a pre-calibrated reference length. The tool returns both a GSD estimate and a composite confidence score, enabling the calling agent to autonomously decide whether to trust the measurement or fall back to alternative strategies. On the DOTA~v1.5 benchmark, VANGUARD achieves 6.87% median GSD error on 306~images. Integrated with SAM-based segmentation for downstream area measurement, the pipeline yields 19.7% median error on a 100-entry benchmark -- with 2.6x lower category dependence and 4x fewer catastrophic failures than the best VLM baseline -- demonstrating that equipping agents with deterministic geometric tools is essential for safe autonomous spatial reasoning.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决无人机在GPS拒止或通信受限环境中无法获取绝对度量尺度信息的问题。研究背景是无人机在灾害评估、基础设施巡检等自主任务中，常因无法获得相机元数据和遥测数据，导致单目视觉系统无法恢复场景的绝对物理尺度，从而影响下游空间推理的可靠性。随着基于大语言模型和视觉语言模型的高层规划器在具身系统中的广泛应用，这些模型对物理尺度的推理能力变得至关重要，但现有方法存在明显不足：论文实验表明，五种先进的视觉语言模型在仅凭航空图像估计物理面积时，会出现严重的“空间尺度幻觉”问题，中位面积估计误差超过50%，且常出现数量级偏差，这给自主无人机操作带来了直接安全风险。

本文要解决的核心问题是：在缺乏GPS和元数据的情况下，如何为基于大语言模型的规划器提供一种可靠、确定性的方法来从单目航空图像中恢复地面采样距离，从而支持安全的度量空间推理。为此，论文提出了VANGUARD方法，利用环境中普遍存在的小型车辆作为几何锚点，通过定向边界框检测、核密度估计模态像素长度，并结合预校准的参考长度来估算地面采样距离，最终以轻量级可调用工具的形式，为智能体提供确定性的几何感知技能。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为两类：**地面采样距离（GSD）与尺度估计方法**和**视觉语言模型（VLM）的空间推理研究**。

在**GSD与尺度估计**方面，传统方法依赖于传感器参数、飞行高度和相机标定等元数据。当元数据缺失时，现有研究尝试从图像内容推断尺度，例如基于阴影的方法、单目深度估计以及回归卷积神经网络。然而，这些方法要么需要带有GSD标签的有监督训练，要么只能恢复相对深度。Wang和Wang提出了一种基于GPT的视觉智能体系统，通过选择参考物体来估计尺度，但其对专有模型的依赖限制了可复现性。本文提出的VANGUARD方法针对这些不足，专注于利用“小型车辆”这一特征明确的参考物类别，并采用核密度估计进行稳健的模态值计算，从而在无需元数据或大量标注训练的情况下实现绝对度量尺度的恢复。

在**VLM空间推理缺陷**方面，尽管视觉语言模型在遥感等领域进展迅速，但其空间推理能力存在根本性局限。相关研究（如Liu等人、Chen等人和Liao等人的工作）表明，VLMs在空间关系理解、3D距离与尺寸估计、以及即使提供参考物体情况下的定量空间推理等方面，仍存在巨大困难或“幻觉”问题。这些发现正是本文研究动机的来源：与其依赖VLMs进行度量尺度的推理，本文选择为具身智能体提供一个可调用的、确定性的几何感知工具（VANGUARD），以夯实其空间理解的基础，确保安全可靠的空间推理。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为VANGUARD的轻量级、确定性几何感知技能来解决无人机在GPS拒止环境下无法恢复场景绝对度量尺度的问题。其核心方法是将地面采样距离（GSD）的估计问题，转化为利用环境中普遍存在的“锚点”——小型车辆——的像素长度进行推算的过程。

整体框架是一个五阶段的处理流水线，被封装为一个无状态、确定性的API，可供LLM/VLM等高级规划智能体调用。输入单目航拍图像，输出GSD估计值和一个复合置信度分数。主要模块包括：
1.  **车辆检测**：使用YOLO11-l模型进行有向边界框（OBB）检测，以精确获取车辆的长边像素长度P_i和置信度C_i。对于大图像，采用分块检测与合并策略。
2.  **异常值过滤**：采用基于中位数的简单过滤器，移除像素长度大于中位数α倍（α=1.5）的检测结果，以滤除大型车辆（如卡车、巴士）或误检目标。
3.  **模态像素长度估计**：对过滤后的像素长度集合，使用核密度估计（KDE）来寻找其分布的模式值P_mode，而非简单地使用均值或中位数。这种方法对由误检或尺寸异常车辆造成的偏态分布更具鲁棒性。
4.  **GSD计算**：利用一个预校准的参考物理长度L_ref（通过分析DOTA v1.5数据集中大量带标注的小型车辆实例，经KDE确定其最常见长度为5.045米），通过公式GSD_pred = L_ref / P_mode 计算出GSD。
5.  **多维置信度评估**：生成一个复合置信度分数C，综合了样本充足性、分布集中度、检测质量和异常检测四个维度，并引入一个硬性的“分辨率守卫”机制。当估计的像素长度P_mode过小（对应GSD过粗）时，会强制降低置信度，以防止在低分辨率下出现系统性误差却仍报告高置信度的情况。

创新点在于：首先，提出了“车辆锚定”的概念，利用环境中高频率出现、尺寸相对标准的小型车辆作为天然的尺度参考物，无需依赖GPS或相机元数据。其次，整个流程设计为确定性的、可解释的几何技能，与容易产生空间尺度幻觉的黑盒VLM形成鲜明对比，为自主系统提供了安全可靠的度量感知基础。最后，通过输出结构化结果（GSD估计值+置信度），使调用该技能的智能体能够根据置信度自主决策是否信任该测量或启用备用策略，实现了安全闭环的自主决策。

### Q4: 论文做了哪些实验？

论文在DOTA v1.5数据集和RS-GSD Benchmark v5.0上进行了实验。实验设置方面，使用DOTA v1.5的1411张训练图像（85%用于训练，15%用于开发集调参）和458张验证图像（其中450张包含GSD元数据用于测试）来评估GSD估计。对于下游面积测量，构建了RS-GSD Benchmark v5.0，包含100个条目（64张图像，8个类别）。对比方法包括：1）使用真实标注（GT Baseline）作为上界；2）多个先进VLM（Qwen2.5-VL-72B、Claude Opus 4.6、Qwen-VL-Max、Qwen-VL-Plus、GPT-4o）在零样本和提供车辆长度提示（“汽车≈5米”）两种设置下的面积估计；3）不同聚合方法（KDE、中位数、均值）和参数（参考长度、离群因子）的消融实验。

主要结果如下：在GSD估计上，使用YOLOv8m-OBB检测器的端到端VANGUARD管道在306张图像上取得了6.87%的中位数误差，66.0%的图像误差<10%，83.3%的图像误差<20%。与使用真实标注的基线（6.88%中位数误差）相比，性能接近。在面积估计上，零样本VLMs的中位数误差在38.3%至51.9%之间，显示严重的空间尺度幻觉；即使提供车辆长度提示，最佳VLM（Claude Opus 4.6）的中位数误差为17.1%。而集成了SAM分割的VANGUARD管道在RS-GSD基准测试中取得了19.7%的中位数误差（均值误差29.2%），性能优于大多数VLM，且类别依赖性降低了2.6倍，灾难性故障（误差≥100%）减少了4倍。消融实验表明，KDE模态估计优于均值聚合（中位数误差6.87% vs. 8.27%），参考长度是最敏感的参数（±0.5米偏差会使中位数误差翻倍），且性能随车辆数量增加而提升（≥20辆车时误差6.12%，<5辆车时13.47%），在粗分辨率（>0.7米/像素）下性能急剧下降。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要在于其应用场景的特定性：方法依赖于场景中存在小型车辆（在DOTA数据集中有33%的图像不满足），且要求图像地面采样距离（GSD）优于0.3米/像素，这限制了其在无车辆环境或低分辨率图像中的适用性。此外，其参考长度基于中国城市车队校准，跨地域部署需重新标定，且未建模倾斜或离天底点成像带来的透视畸变。

未来研究可从以下几个方向深入探索：
1.  **扩展环境锚点类别**：如论文所述，可纳入车道宽度、集装箱等具有标准尺寸的物体作为参考，以提升方法在无车辆场景（如工业园区、港口、高速公路）的覆盖率和鲁棒性。
2.  **处理复杂成像几何**：开发能够补偿透视畸变的模型扩展，例如通过估计相机姿态或利用场景几何先验，使方法适用于倾斜摄影等更广泛的航拍数据。
3.  **动态参考与在线学习**：探索在线校准或自适应参考长度估计机制，使系统能适应不同区域、不同车辆型号的变化，减少对固定先验的依赖。
4.  **与学习方法的深度融合**：虽然论文强调了确定性工具的优势，但未来可研究如何将此类几何技能与VLM的语义理解能力更紧密地耦合，例如让VLM主动指导锚点选择或解释置信度分数，形成更智能的协同决策循环。
5.  **端到端系统集成验证**：在更复杂的具身智能体闭环中进行测试，评估其在动态规划、避障等任务中实际提升安全性与可靠性的效果。

### Q6: 总结一下论文的主要内容

该论文针对无人机在GPS拒止或通信降级环境中，因无法获取相机元数据和遥测信息而导致场景绝对度量尺度丢失的问题，提出了一种轻量级、确定性的几何感知技能VANGUARD。其核心贡献是设计了一种可被基于LLM的智能体调用的工具，通过检测图像中普遍存在的小型车辆作为环境锚点，利用核密度估计稳健地估算其模态像素长度，并结合预校准的参考长度来恢复地面采样距离（GSD），从而解决现有视觉语言模型在空间尺度估计上存在的严重幻觉问题。方法上，VANGUARD不仅输出GSD估计值，还提供一个复合置信度分数，使调用智能体能自主决定是否信任该测量或转而采用备用策略。实验表明，在DOTA v1.5基准测试中，该方法取得了6.87%的中位GSD误差；与SAM分割结合进行下游面积测量时，在100条目的基准上中位误差为19.7%，其类别依赖性比最佳VLM基线低2.6倍，且灾难性故障大幅减少。结论指出，为智能体配备此类确定性几何工具对于实现安全的自主空间推理至关重要，并展望了未来扩展到多类别参考物体、在更多地理区域验证以及集成到闭环无人机规划系统中的方向。
