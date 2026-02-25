---
title: "When the Inference Meets the Explicitness or Why Multimodality Can Make Us Forget About the Perfect Predictor"
authors:
  - "J. E. Domínguez-Vidal"
  - "Alberto Sanfeliu"
date: "2026-02-21"
arxiv_id: "2602.18850"
arxiv_url: "https://arxiv.org/abs/2602.18850"
pdf_url: "https://arxiv.org/pdf/2602.18850v1"
categories:
  - "cs.RO"
  - "cs.AI"
tags:
  - "人机协作"
  - "意图预测"
  - "显式通信"
  - "机器人"
  - "多模态交互"
  - "人机交互"
  - "实验评估"
relevance_score: 7.0
---

# When the Inference Meets the Explicitness or Why Multimodality Can Make Us Forget About the Perfect Predictor

## 原始摘要

Although in the literature it is common to find predictors and inference systems that try to predict human intentions, the uncertainty of these models due to the randomness of human behavior has led some authors to start advocating the use of communication systems that explicitly elicit human intention. In this work, it is analyzed the use of four different communication systems with a human-robot collaborative object transportation task as experimental testbed: two intention predictors (one based on force prediction and another with an enhanced velocity prediction algorithm) and two explicit communication methods (a button interface and a voice-command recognition system). These systems were integrated into IVO, a custom mobile social robot equipped with force sensor to detect the force exchange between both agents and LiDAR to detect the environment. The collaborative task required transporting an object over a 5-7 meter distance with obstacles in the middle, demanding rapid decisions and precise physical coordination. 75 volunteers perform a total of 255 executions divided into three groups, testing inference systems in the first round, communication systems in the second, and the combined strategies in the third. The results show that, 1) once sufficient performance is achieved, the human no longer notices and positively assesses technical improvements; 2) the human prefers systems that are more natural to them even though they have higher failure rates; and 3) the preferred option is the right combination of both systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决人机协作中一个核心问题：如何让机器人更有效地理解人类意图。传统方法依赖于意图预测器，通过传感器数据推断人类意图，但其存在不可避免的错误率，部分源于人类行为固有的随机性和对环境理解的主观差异。这引发了一个根本性质疑：是否存在完美的意图预测器？因此，论文探讨了另一种思路——显式沟通系统（如按钮、语音），让人类直接表达意图。

本文具体的研究问题是：在需要快速决策和精确物理协调的协作任务（如协同搬运物体）中，比较并融合意图推断（隐式）与显式沟通两种策略，以确定何种方式更能被人类接受并提升协作效果。它延续了作者先前的工作，旨在验证几个关键假设：1）当预测器性能达到一定阈值后，进一步的技术改进是否会被人类察觉和重视？2）人类是否更偏好使用起来更“自然”的沟通方式，即使其技术指标（如失败率、延迟）更差？3）推断与显式沟通的结合是否会成为最优方案？论文通过三轮对照实验来回答这些问题，其贡献在于从人本角度评估了不同意图沟通机制的有效性与用户体验，而不仅仅是追求技术指标的提升。

### Q2: 有哪些相关研究？

相关研究主要分为两类：意图推断系统和显式通信系统。在意图推断方面，已有工作广泛使用高斯混合模型（GMM）或人工神经网络（ANN）来预测人类意图，例如轨迹、手部动作或下一个抓取对象。在协作搬运等物理接触任务中，常采用阻抗或导纳控制器使机器人适应人类意图，近期研究则进一步引入了对物体期望轨迹、速度剖面或短期作用力的预测器（如Alevizos等人2020年、Alyacoub等人2021年及Predictor_IROS2023的工作），但这些研究均未考虑通过人机通信来降低推断不确定性或解决推断错误。

在显式通信系统方面，相关研究较少。例如，ROMAN2021设计了一款支持远距离双向通信的智能手机应用，后被应用于协作搜索任务（Dalmasso等人2023）；Mullen等人（2021）通过增强现实（AR）系统让机器人在执行推断任务前寻求人类确认；Gildert等人（2022）则结合隐式力传递和显式无线消息交换来改进双机器人物体操控；Lorentz等人（2023）允许人类结合手势和语音命令指挥机器人。语音命令识别在机器人领域的早期研究有限，直到ANN发展和大型命令数据集出现后才取得进展（如Warden2018、Majumdar2020和Kim2021的工作）。

本文与这些研究的关系在于：首先，系统性地比较了两种推断方法（基于力和基于增强速度预测）与两种显式通信方法（按钮界面和语音命令），而以往研究多专注于单一策略；其次，本文首次在协作搬运任务中将两种策略结合使用，并验证了人类对系统的接受度，弥补了现有工作多假设人类愿意使用其系统的不足。

### Q3: 论文如何解决这个问题？

论文通过设计并比较四种不同的通信系统来解决人机协作中意图理解的不确定性问题，核心思路是结合隐式意图推断与显式意图通信。方法上构建了一个人机协作搬运物体的实验平台，机器人（IVO）配备力传感器和激光雷达，能感知交互力与环境。任务要求双方在5-7米距离内绕过障碍物搬运物体，需要快速决策和精确协调。

架构上，系统基于虚拟力模型进行运动控制：环境障碍产生排斥力，目标点产生吸引力，再与人类施加的力结合，输入控制器生成速度指令。关键创新在于将意图信息融入该框架。论文测试了两种隐式意图推断系统：一是基于历史力、速度、环境力和激光雷达数据的力预测器，预测未来1秒的人类施力，进而估计短期路径；二是改进的速度预测器，直接预测未来1秒的人机对速度，积分得到路径估计，将轨迹预测误差从0.199米降低至0.138米，提升了推断准确性。

同时，论文设计了两种显式意图通信系统：一是手柄按钮接口（三个按钮分别对应直行、左转、右转），无误识别且延迟可忽略；二是语音命令识别系统（识别“Go”、“Left”、“Right”），识别率94.75%，但可能受蓝牙延迟影响（0.2-1秒）。通过让75名志愿者进行255次实验，依次测试推断系统、通信系统及组合策略，发现人类更偏好自然交互方式（如语音）即使其故障率更高，而最优方案是隐式推断与显式通信的恰当结合。这验证了在协作任务中，单一完美预测器并非必需，多模态通信能平衡效率与用户体验。

### Q4: 论文做了哪些实验？

该论文设计了三轮实验，共招募75名志愿者，完成了255次人机协作物体搬运任务。实验使用定制移动社交机器人IVO，在室内预设起点和终点，通过动作捕捉系统记录数据。

**第一轮实验（22人）**：比较两种意图预测器（基于力的预测器和基于速度的预测器）。每位志愿者进行三次实验：一次无预测器（基线），以及分别使用两种预测器各一次。通过问卷（1-7分）和客观测量（持续时间、平均力、最大力）评估。结果显示，尽管速度预测器将轨迹估计平均误差降低了30.6%，但志愿者对两者的主观评价无显著偏好，验证了“一旦性能足够，用户不再感知技术改进”的假设。

**第二轮实验（23人）**：比较两种显式通信系统（按钮界面和语音命令识别）。每位志愿者进行三次实验：一次无通信系统（基线），以及分别使用两种系统各一次。结果显示，语音命令在“机器人贡献度”、“流畅性”、“舒适度”和“信任度”等多方面获得显著更高评分，尽管其错误率更高，86.9%的志愿者仍偏好语音命令，验证了“用户偏好更自然的系统”。

**第三轮实验（30人）**：结合前两轮中最佳系统（速度预测器和语音命令）。每位志愿者进行四次实验：基线、仅用预测器、仅用语音命令、两者结合。结果显示，结合系统在“舒适度”、“信任度”和“感知易用性”上获得最高评分，并且是大多数志愿者（56.7%）的首选，验证了“组合系统是最优选项”。

所有实验均采用随机顺序以消除统计偏差，并使用方差分析等统计方法检验显著性。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于实验场景相对单一（仅限物体搬运任务），且未深入探讨不同用户群体（如年龄、技术熟悉度）对交互方式的偏好差异。未来研究可从以下方向拓展：一是探索更复杂的协作任务（如多步骤操作、动态环境），验证多模态系统的泛化能力；二是结合个性化建模，使机器人能自适应调整推理与显式通信的平衡策略；三是研究非言语的隐式沟通方式（如手势、凝视），进一步逼近人类自然交互；四是量化“自然性”的具体维度（如认知负荷、情感体验），为设计提供更细致的指导。最终目标应是构建动态混合系统，能根据上下文不确定性、用户状态和任务需求，智能切换或融合多种交互模式。

### Q6: 总结一下论文的主要内容

这篇论文通过人机协作搬运物体的实验，对比了两种意图预测系统（基于力预测和增强速度预测）与两种显式通信系统（按钮界面和语音命令）在协作任务中的表现。核心贡献在于揭示了三个关键发现：首先，预测系统在达到足够性能后，进一步的技术改进可能不会被人类用户察觉或积极评价；其次，人类更偏好使用起来更自然的通信方式（如语音），即使其故障率更高；最后，将预测与显式通信系统恰当结合，能在任务流畅性、信任度和舒适度等方面实现最佳的人机交互效果。其意义在于挑战了单纯追求完美预测器的思路，论证了结合自然、显式通信（即使不完美）对于提升人机协作体验的重要性，为未来开发更自然人机交互系统提供了依据。
