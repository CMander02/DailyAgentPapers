---
title: "NovaPlan: Zero-Shot Long-Horizon Manipulation via Closed-Loop Video Language Planning"
authors:
  - "Jiahui Fu"
  - "Junyu Nan"
  - "Lingfeng Sun"
  - "Hongyu Li"
  - "Jianing Qian"
  - "Jennifer L. Barry"
  - "Kris Kitani"
  - "George Konidaris"
date: "2026-02-23"
arxiv_id: "2602.20119"
arxiv_url: "https://arxiv.org/abs/2602.20119"
pdf_url: "https://arxiv.org/pdf/2602.20119v1"
categories:
  - "cs.RO"
  - "cs.AI"
  - "cs.CV"
tags:
  - "Agent 架构"
  - "规划"
  - "工具使用"
  - "机器人"
  - "视觉语言模型"
  - "分层规划"
  - "零样本学习"
  - "长视野任务"
  - "闭环控制"
relevance_score: 9.0
---

# NovaPlan: Zero-Shot Long-Horizon Manipulation via Closed-Loop Video Language Planning

## 原始摘要

Solving long-horizon tasks requires robots to integrate high-level semantic reasoning with low-level physical interaction. While vision-language models (VLMs) and video generation models can decompose tasks and imagine outcomes, they often lack the physical grounding necessary for real-world execution. We introduce NovaPlan, a hierarchical framework that unifies closed-loop VLM and video planning with geometrically grounded robot execution for zero-shot long-horizon manipulation. At the high level, a VLM planner decomposes tasks into sub-goals and monitors robot execution in a closed loop, enabling the system to recover from single-step failures through autonomous re-planning. To compute low-level robot actions, we extract and utilize both task-relevant object keypoints and human hand poses as kinematic priors from the generated videos, and employ a switching mechanism to choose the better one as a reference for robot actions, maintaining stable execution even under heavy occlusion or depth inaccuracy. We demonstrate the effectiveness of NovaPlan on three long-horizon tasks and the Functional Manipulation Benchmark (FMB). Our results show that NovaPlan can perform complex assembly tasks and exhibit dexterous error recovery behaviors without any prior demonstrations or training. Project page: https://nova-plan.github.io/

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决机器人在零样本（无需任务特定演示或训练）条件下执行长时程、复杂操作任务时，如何将高层语义推理与低层物理执行有效结合的难题。

研究背景在于，尽管视觉语言模型（VLMs）和视频生成模型能够进行任务分解和结果想象，但它们通常缺乏物理世界的“接地性”，难以直接转化为精确、可执行的机器人动作。现有方法主要存在三大不足：第一，视频模型可能存在时序不一致和“幻觉”问题，导致长期规划性能下降；第二，当生成的视频因遮挡、深度估计不准或几何扭曲导致机器人无法准确跟踪视觉计划时，现实执行容易失败；第三，僵化的规划策略难以同时兼顾装配任务所需的战略性前瞻和探索性搜索所需的反应能力。

因此，本文的核心问题是：如何构建一个闭环框架，将高层视频语言规划与几何接地的机器人执行统一起来，以实现零样本、长时程的鲁棒操作。具体而言，论文提出的NovaPlan系统试图通过一个包含VLM规划器、视频生成、混合轨迹提取（在物体关键点与人类手部姿态间动态切换）以及VLM监控与重规划的闭环架构，来弥合“想象”与“执行”之间的鸿沟，使机器人能够处理复杂装配任务，并在单步失败时自主恢复。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类：零样本操作策略与视频驱动规划。

在零样本操作策略方面，一类主流方法是训练视觉-语言-动作模型，通过大量真实机器人轨迹数据学习通用控制策略，但其扩展受限于高质量物理交互数据的高昂成本。另一类研究方向则利用视觉语言模型的高层推理能力生成符号或空间规划，而非直接输出电机动作，这类方法在任务分解上表现出潜力，但通常缺乏非结构化环境中精确操作所需的细粒度3D空间感知和动态推理能力。

在视频驱动规划方面，研究主要集中于图像到视频生成模型，其通过初始观察和语言描述预测未来帧，为动态推理提供丰富表示。先前工作尝试使用逆动力学模型或模仿学习策略将生成视频转化为机器人动作，但通常需要大量任务特定演示来训练下游动作预测器。近期研究尝试利用现成感知模型从视频中提取6D姿态估计或光流跟踪等控制信号，但这些方法仍易受感知误差和跟踪漂移影响，且大多以开环方式运行，难以处理长视野任务或从执行错误中恢复。

与上述工作相比，本文提出的NovaPlan框架将高层VLM验证与混合手-物体跟踪机制在闭环框架中统一，实现了零样本设置下鲁棒的长视野操作和自主错误恢复能力，弥补了现有方法在物理基础、闭环纠错和动态推理方面的不足。

### Q3: 论文如何解决这个问题？

NovaPlan通过一个分层闭环框架来解决零样本长视野操作任务，核心思想是将高层语义规划与低层几何执行紧密结合。其整体架构分为高层视频语言规划和低层执行两个主要模块，通过闭环验证与恢复机制实现鲁棒操作。

在高层规划中，系统采用生成-验证树搜索方法。首先，视觉语言模型（VLM）将任务分解为多个子目标候选；接着，视频生成模型为每个候选生成多条视觉推演，模拟物理结果；然后，VLM通过四个指标（目标、物理、运动、结果）评估推演的物理合理性和语义一致性，筛选最优候选并递归扩展直至形成完整计划；最后，在执行过程中，VLM实时监控状态，一旦检测到失败（如抓取滑动），即触发恢复机制：分析失败模式并生成纠正动作，使场景从当前状态回归目标状态，实现自主错误恢复。规划视野（贪婪模式或战略模式）由VLM根据任务语义理解和几何依赖自主选择，以平衡计算开销与长期策略需求。

在低层执行中，系统从生成的视频中提取两种互补的3D运动表征——物体流和手部流，并通过自适应切换机制选择更优参考。物体流通过跟踪目标物体的3D关键点序列，利用Kabsch算法计算相邻帧间的刚体变换，得到6自由度轨迹。手部流则使用HaMeR估计人手姿态序列，并通过双锚点校准流程（检测交互区间、恢复度量尺度、补偿投影漂移）解决生成视频的几何失真问题，将其转换为准确的SE(3)轨迹。切换逻辑基于轨迹平滑性：当相邻帧间旋转角度超过阈值（表明物体可能被严重遮挡或发生大旋转）时，系统自动切换至手部流。

创新点主要体现在三方面：一是闭环视频语言规划框架，通过模拟验证与实时监控实现零样本长视野任务分解与错误恢复；二是混合流机制，结合物体与手部运动先验，提升在遮挡或深度不准确情况下的执行稳定性；三是执行重接地技术，每一步都基于最新观测重新生成视频参考，确保轨迹几何接地于实际工作空间。最终，物体流通过静态变换映射为机器人末端执行器轨迹，手部流则直接映射，两者均通过抓取提议网络确定初始抓取配置，从而将视觉计划转化为可执行的机器人动作。

### Q4: 论文做了哪些实验？

论文实验主要围绕验证NovaPlan在零样本长视野操作任务中的有效性展开。实验设置方面，硬件使用Franka Research 3机械臂和Robotiq 2F-85夹爪，感知由RealSense D455相机完成，关键模块（如视频生成、深度估计）部署在NVIDIA H100等GPU上。整个流程端到端耗时约40秒。

数据集与基准测试包括：1）三个自定义长视野任务（四层积木堆叠、颜色分类、隐藏物体搜索），用于评估推理、任务分解和错误恢复能力；2）单步任务（如Block Insertion）用于对比混合流程效果；3）功能操作基准（FMB）的装配任务，用于测试零样本能力边界。

对比方法包括三种零样本方法：NovaFlow（基于视频规划）、π₀.₅（VLA模型）和MOKA（基于VLM的规划）。为公平比较，假设基线方法具备“先知任务分解模块”提供子任务指令。

主要结果与关键指标如下：
- 长视野任务中，NovaPlan在四层积木堆叠任务上成功率达70%（10次尝试成功7次），显著优于基线（NovaFlow第四层成功率仅30%，π₀.₅仅能堆叠两层）。颜色分类任务中，所有方法在容差低的黄色积木上性能均下降，NovaPlan的失败主要源于深度估计误差。隐藏物体搜索任务中，NovaPlan与NovaFlow均实现100%成功率。
- 单步任务对比显示，NovaPlan通过混合对象关键点与手部姿态流程，成功率全面高于纯对象中心的NovaFlow，验证了手部流程提升执行稳定性的假设。
- FMB装配任务中，所有基线方法均无法完成单步，而NovaPlan在零样本设置下能部分完成，但面临视频生成物理合理性不足、不规则物体处理困难、恢复动作微小导致跟踪噪声等瓶颈。实验表明，使用Veo 3.1视频生成模型并启用非抓取恢复模式（如指尖推动）可提升恢复能力。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要在于其性能高度依赖于各子模块（如视频生成、深度估计、关键点跟踪等）的现有能力。例如，当前视频生成模型难以针对复杂失败场景生成可行的恢复计划，抓取网络对不规则物体的处理也不稳定，这限制了系统在重定向任务和特定失败模式下的恢复能力。

未来研究方向可从以下方面探索：一是提升基础模型的物理接地性，通过多模态训练融入更精确的几何与动力学约束，使视频生成能更贴合真实物理规律；二是增强系统的自适应能力，例如引入在线学习机制，让机器人能从少量实时交互中动态优化关键点提取或动作规划策略；三是扩展任务泛化性，探索如何将框架迁移到动态环境或非结构化场景中。此外，可考虑融合仿真与真实世界数据，构建更鲁棒的失败恢复知识库，以突破当前视频生成模型的瓶颈。

### Q6: 总结一下论文的主要内容

该论文提出了NovaPlan框架，旨在解决机器人零样本长时程操作任务中高层语义推理与低层物理交互的整合难题。核心贡献在于构建了一个分层系统，将闭环视觉语言规划与几何基础执行相结合，实现了无需任务特定演示或训练的长时程操作。

问题定义聚焦于如何让机器人在复杂长时程任务中自主分解目标、规划步骤并应对执行过程中的失败。方法上，高层采用视觉语言模型进行任务分解与闭环监控，支持自主重规划以恢复单步失败；低层则从生成视频中提取物体关键点和人手姿态作为运动学先验，通过切换机制选择更优参考以生成机器人动作，从而在严重遮挡或深度误差下保持稳定执行。

主要结论显示，NovaPlan在三个长时程任务和功能操作基准测试中表现出色，能够完成复杂装配任务并展示灵活的错误恢复能力。该框架为通用机器人操作提供了一条可扩展的路径，随着基础模型的进步，有望进一步推动机器人自主操作的发展。
