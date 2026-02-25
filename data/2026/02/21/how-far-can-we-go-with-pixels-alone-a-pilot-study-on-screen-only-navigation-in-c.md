---
title: "How Far Can We Go with Pixels Alone? A Pilot Study on Screen-Only Navigation in Commercial 3D ARPGs"
authors:
  - "Kaijie Xu"
  - "Mustafa Bugti"
  - "Clark Verbrugge"
date: "2026-02-21"
arxiv_id: "2602.18981"
arxiv_url: "https://arxiv.org/abs/2602.18981"
pdf_url: "https://arxiv.org/pdf/2602.18981v1"
categories:
  - "cs.AI"
tags:
  - "视觉导航"
  - "游戏智能体"
  - "视觉感知"
  - "环境理解"
  - "基准测试"
  - "有限状态机"
relevance_score: 7.5
---

# How Far Can We Go with Pixels Alone? A Pilot Study on Screen-Only Navigation in Commercial 3D ARPGs

## 原始摘要

Modern 3D game levels rely heavily on visual guidance, yet the navigability of level layouts remains difficult to quantify. Prior work either simulates play in simplified environments or analyzes static screenshots for visual affordances, but neither setting faithfully captures how players explore complex, real-world game levels. In this paper, we build on an existing open-source visual affordance detector and instantiate a screen-only exploration and navigation agent that operates purely from visual affordances. Our agent consumes live game frames, identifies salient interest points, and drives a simple finite-state controller over a minimal action space to explore Dark Souls-style linear levels and attempt to reach expected goal regions. Pilot experiments show that the agent can traverse most required segments and exhibits meaningful visual navigation behavior, but also highlight that limitations of the underlying visual model prevent truly comprehensive and reliable auto-navigation. We argue that this system provides a concrete, shared baseline and evaluation protocol for visual navigation in complex games, and we call for more attention to this necessary task. Our results suggest that purely vision-based sense-making models, with discrete single-modality inputs and without explicit reasoning, can effectively support navigation and environment understanding in idealized settings, but are unlikely to be a general solution on their own.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决一个核心问题：在复杂的商业3D动作角色扮演游戏（ARPG）中，能否仅依靠屏幕像素信息（即纯粹的视觉感知），而不依赖游戏内部状态（如坐标、引擎API或网格数据），实现自主的探索与导航。具体而言，研究旨在量化游戏关卡布局的“可导航性”，并建立一个完全基于视觉的智能体基线。

现有研究存在局限：一方面，导航智能体通常在简化模拟器（如AI2-THOR、Habitat）中训练，依赖结构化任务和干净传感器数据，与商业游戏混乱、视觉信息过载的真实环境差异巨大；另一方面，针对游戏视觉引导的定性研究或辅助工具（如视觉导航助手）多服务于人类玩家，并非自主智能体，且缺乏时序推理能力。

因此，本文基于已有的视觉可供性检测器（能识别空间过渡点STP和主空间过渡点MSTP），构建了一个仅依赖屏幕帧、使用离散动作的有限状态控制器智能体。它试图在《黑暗之魂》风格的线性关卡中，仅凭视觉线索探索并抵达目标区域。同时，论文提出了一种基于视觉里程碑的评估协议，仅通过图像匹配来评分，无需游戏引擎支持。

通过试点实验，论文验证了纯视觉导航在理想片段中的可行性，但也揭示了当前单帧视觉模型的根本局限（如在视觉模糊或极端视角下容易失败），表明仅靠此类模型无法构成通用解决方案。最终，研究为复杂游戏中的纯视觉导航提供了一个具体的、可复用的基线和评估方法，呼吁更多研究关注视觉可供性、关卡设计与具身智能体的交叉领域。

### Q2: 有哪些相关研究？

相关研究主要分为两大类：导航智能体和游戏视觉研究。

在导航智能体方面，早期工作如Zhu等人的目标驱动视觉导航和Mirowski等在3D迷宫中的强化学习研究，利用AI2-THOR等仿真环境进行训练。后续研究增强了空间记忆与规划能力，例如Cognitive Mapping and Planning（CMP）学习俯视图进行规划，Active Neural SLAM结合SLAM模块与规划器。评估标准也趋于统一，如Habitat采用的PointGoal任务和SPL指标。此外，Go-Explore等硬探索方法通过存档和重置机制解决稀疏奖励问题，其思想与本研究中利用里程碑存档重启类似。这些工作共同将魂类游戏视为仅依赖视觉输入和小动作空间的具身导航问题。

在游戏视觉研究方面，ViZDoom和Minecraft（Malmo）常作为强化学习测试平台，其中 curiosity-driven 方法鼓励探索。近期，Video Pre-Training通过人类游戏视频训练模型在Minecraft中导航。同时，游戏设计领域分析了视觉如何引导玩家，如Guo对开放世界视觉引导的系统化，以及Milam等人的“推拉”框架。特别是Xu等人针对魂类游戏开发了视觉空间转换点（STP）检测器，能从静态截图识别设计者预期的路径。本研究直接扩展了此项工作：不仅检测视觉线索，还构建了完全基于屏幕输入、使用有限按键的自动导航智能体，将视觉引导作为唯一感知模态，从而在复杂3D游戏世界中测试纯视觉线索的导航极限。

### Q3: 论文如何解决这个问题？

该论文通过构建一个纯视觉的探索与导航智能体来解决复杂3D游戏中的屏幕导航问题。其核心方法基于一个固定的视觉感知模型（STP/MSTP检测器），并在此基础上设计了控制与记忆层，将单帧的视觉显著性预测转化为连续的导航行为。

**核心架构与流程**：
智能体采用分层架构。底层是**视觉感知模型**，它通过两阶段处理检测空间过渡点（STP）并选择主空间过渡点（MSTP），即当前帧中最有希望的“前进方向”在屏幕上的位置。智能体仅以当前帧图像和MSTP作为输入，不依赖任何游戏内部状态。

中层是一个**有限状态机（FSM）控制器**，它管理高层行为状态（如扫描、对齐、前进、恢复等）。控制器循环执行：1) 捕获屏幕并运行感知模型获得MSTP；2) 计算基于帧差、结构相似性和光流的进展信号；3) 根据当前状态、MSTP和进展信号更新FSM状态；4) 执行低层控制。

**关键技术细节**：
1.  **脉冲式低级控制**：将MSTP中心与屏幕中心的像素误差，通过施密特触发器风格的死区处理，转化为离散的相机方向键脉冲（上/下/左/右）和前进键（W）的开关控制。这模拟了一个比例控制器，避免了抖动。
2.  **视觉记忆银行**：这是一个可选模块，用于减少重复失败。它存储历史帧的嵌入向量、感知哈希、当时选择的移动方向（扇形区）以及该选择的结果（好/坏/未知）。决策时，系统会查询记忆银行，对与过去“坏结果”相似的视觉场景中的相同移动方向施加惩罚分数，从而引导智能体尝试其他方向。这引入了基于经验的简单规避学习。
3.  **纯视觉约束下的进展判断**：由于无法获取坐标信息，智能体通过比较连续帧的MSTP框面积、结构相似性指数和光流幅度等视觉特征来推断自身是否在有效前进，并据此触发状态转换或恢复行为。

总之，该方法通过结合**固定的视觉显著性检测**、**基于规则的状态机**、**脉冲式伺服控制**以及**基于视觉相似性的经验记忆**，构建了一个完全依赖像素输入、能在复杂3D游戏环境中进行基本探索和导航的智能体系统。

### Q4: 论文做了哪些实验？

论文实验旨在评估纯视觉驱动的导航智能体在商业3D动作角色扮演游戏（ARPG）中的表现。实验设置基于“视觉里程碑”评估协议：在多个游戏（《黑暗之魂I/III》、《艾尔登法环》、《黑神话：悟空》）中，每条测试路线被分解为6个有序的视觉里程碑，智能体需从游戏实时画面中识别显著兴趣点，并驱动一个有限状态控制器，在仅使用基本行走控制的简化环境中（敌人被禁用）尝试依次到达这些里程碑。每个里程碑段设有固定时间预算，超时则视为失败并自动重置到下一个里程碑起点。

基准测试比较了三种智能体配置：1) **Naive**：直接朝向视觉可通行性预测点移动；2) **FSM-only**：启用完整的有限状态控制器（含扫描、对齐、前进、恢复等状态）；3) **Full**：在FSM基础上增加视觉记忆库。每种配置在每条路线上进行10次完整运行，记录里程碑成功率（MS）、路线完整成功率（RS）、段耗时等指标。

主要结果显示：在核心游戏《黑暗之魂III》中，FSM-only智能体在Grand Archives路线上表现最佳，路线成功率（RS）达50%，平均里程碑成功率为88.3%，且段耗时和前进时间均低于Naive版本。在《黑暗之魂I》中，所有智能体表现均较差（路线成功率最高仅10%），表明基础视觉模型在该游戏中的局限性。在跨游戏迁移测试中，《黑神话：悟空》上FSM-only智能体取得了40%的路线成功率和83.3%的平均里程碑成功率，显著优于Naive版本；而在《艾尔登法环》中，所有智能体均未能完成完整路线（RS=0），但Full版本将平均里程碑成功率提升至52.0%。实验表明，纯视觉智能体在理想化设置下能支持部分导航，但其性能严重依赖底层视觉模型的质量，且难以处理复杂空间转换。

### Q5: 有什么可以进一步探索的点？

该研究的局限性在于其视觉模型对复杂、动态游戏环境的理解能力有限，仅依赖离散的视觉输入且缺乏显式推理机制，导致导航行为在非理想化场景中不够全面可靠。未来可探索的方向包括：结合多模态输入（如音频、文本提示）增强环境感知；引入强化学习或世界模型进行序列决策优化，以处理更开放的非线性关卡；开发更强大的视觉基础模型，提升对游戏内动态物体、光影变化及视觉误导的鲁棒性；构建大规模游戏导航基准测试，推动智能体在复杂商业游戏中的泛化能力研究。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种仅依赖屏幕像素信息进行3D动作角色扮演游戏（ARPG）导航的智能体框架。研究团队基于现有的视觉可供性检测器，构建了一个纯视觉驱动的探索与导航智能体，该智能体通过实时游戏画面识别显著兴趣点，并驱动一个有限状态控制器在最小化动作空间中进行操作，以探索《黑暗之魂》风格的线性关卡并尝试抵达目标区域。

其核心贡献在于，首次在复杂的商业3D游戏环境中实例化并评估了一个“仅屏幕”导航智能体，为复杂游戏的视觉导航研究提供了一个具体、可共享的基准和评估协议。实验表明，该智能体能够穿越大部分必要路段，并展现出有意义的视觉导航行为，这证明了纯视觉感知模型在理想化设置下支持导航和环境理解的潜力。

然而，研究也明确指出，底层视觉模型的局限性阻碍了真正全面可靠的自动导航。论文的意义在于，它揭示了仅依赖离散单模态（视觉）输入、缺乏显式推理的纯视觉模型，虽然有效，但本身不太可能成为通用解决方案，从而呼吁研究社区更多地关注这一必要任务，并推动向更鲁棒、多模态或具推理能力的导航系统发展。
