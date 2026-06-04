---
title: "Benchmarking Living-Screen-Native GUI Agents on Short-Video Platforms"
authors:
  - "Jiashu Yao"
  - "Heyan Huang"
  - "Daiqing Wu"
  - "Wangke Chen"
  - "Huaxi Ai"
  - "Haoyu Wen"
  - "Zeming Liu"
  - "Yuhang Guo"
date: "2026-06-03"
arxiv_id: "2606.04701"
arxiv_url: "https://arxiv.org/abs/2606.04701"
pdf_url: "https://arxiv.org/pdf/2606.04701v1"
github_url: "https://github.com/BITHLP/LivingScreen"
categories:
  - "cs.CV"
  - "cs.CL"
tags:
  - "GUI Agent"
  - "Benchmark"
  - "Observation Control"
  - "Short-Video Platform"
  - "Agent Evaluation"
relevance_score: 8.5
---

# Benchmarking Living-Screen-Native GUI Agents on Short-Video Platforms

## 原始摘要

GUI agents today assume a static screen, where the world is frozen between two actions. However, real interfaces such as short-video applications violate this assumption, as their content keeps playing, and a competent user must decide what to watch and for how long. We formalize this task as Living-Screen-Native GUI agents and introduce LivingScreen, the first benchmark instantiating it on short-video platforms, with a faithful browser-based environment, a three-tier task suite, and metrics that jointly score accuracy and information efficiency. Evaluating extensive frontier models, we find that none reaches the human cost-accuracy performance, and that their dominant failure mode is over- and under-observation, pointing to observation control as a missing capability axis for future GUI agents. All data and code will be available at https://github.com/BITHLP/LivingScreen.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决现有GUI代理在面对动态、连续演变的屏幕内容（如短视频平台）时的能力缺失问题。当前的研究背景是，多模态大语言模型已发展为通用GUI代理，能处理静态界面上的点击和操作。然而，现有基准测试存在明显不足：它们要么像视频问答那样剥离GUI界面直接输入视频文件，要么像传统GUI代理基准那样忽略视频内容的动态播放。这种将动态视频内容与操作环境割裂的做法，忽略了短视频等平台上屏幕内容持续播放、用户需主动决定观看内容和时长的真实交互场景。

本文要解决的核心问题是：如何建立并评估能够原生操作“活屏幕”（Living Screen）的GUI代理。这类代理需要在一个连续演变的屏幕上自主决定观察什么（是单张截图还是多秒视频片段）以及观察多久，同时与点赞、评论等静态UI元素交互。为此，论文提出了LivingScreen基准，通过高保真浏览器环境、三层任务体系和联合评估准确度与信息效率的指标，首次系统性地量化了这一能力。实验表明，现有最先进的模型因存在“过度观察”和“观察不足”的缺陷，均无法达到人类的经济性-准确性表现，揭示了观察控制作为GUI代理未来关键能力的缺失。

### Q2: 有哪些相关研究？

相关研究可分为三类。第一类是视频理解评测，如LiViBench等，它们采用被动消费协议，将固定片段和问题输入模型，模型既不选择观看内容也不控制时长；而本文提出动态屏幕环境，将信息选择本身纳入任务。第二类是GUI智能体，从端到端架构到Web/移动/桌面控制评测，但都视屏幕为离散截图序列；本文首次引入持续播放内容，将“观看时长与粒度”提升为一级决策维度。第三类是主动视频问答，如Video-Browser等，通过特权工具调用（搜索、缩放）探索离线视频；这些工作虽共享“应决定观看哪些帧”的核心动机，但动作空间是人为设计的特权API，而本文要求通过像素级GUI交互（滑动、进度条、评论）在自动播放的实时内容中操作，且评测处于连续时间状态而非离散的检索-回答循环。与这些工作相比，本文首次结合了主动视频探索的灵活性与GUI智能体的接地负担。

### Q3: 论文如何解决这个问题？

论文通过构建LivingScreen基准，提出了“活屏原生GUI代理”概念，并设计了评估框架。核心方法是对标准POMDP进行两项关键修改：**连续时间状态演化**（Δ₁）和**代理主动观测控制**（Δ₂）。在连续时间状态演化中，状态在决策间隔内由自主流Φ驱动（如视频播放头前进），而非仅由代理动作触发，这模拟了短视频平台内容持续变化的特点。代理主动观测控制则允许代理通过动作参数化观测窗口W(aₖ)，决定观测单帧截图还是视频片段，而非被动接收固定观测。

整体框架基于Playwright构建浏览器环境，模拟真实短视频应用，提供像素级操作API。任务体系分三层：**L1原子GUI动作**（点赞、滑动等）、**L2跨源理解**（关联视频与评论、特征分析等）、**L3闭环应用**（事实核查、内容审核等）。视频数据来自真实公开数据集，并辅以少量合成内容扩展长尾场景。技术关键包括通过聚类构建带主题一致性的工作流，并采用三级质量控制流程（校准、捷径过滤、交叉审核）确保任务质量。评估指标包含成功率（SR）和效率指标（步骤数NS、观看率WR），共同衡量准确性与信息获取成本。

### Q4: 论文做了哪些实验？

论文在LivingScreen基准上评估了主流多模态模型，包括原生视频模型（如Gemini-3.5-Flash、Doubao-Seed-2.0-Pro、Qwen-3.6-Plus、GLM-5V-Turbo、Kimi-K2.5等）和图像模型（如Claude-Opus-4.6、GPT-5.5等），所有模型基于统一单智能体架构，步骤上限为30步，温度0.6，采用“思考-工具调用”格式。

实验主要结果：LivingScreen对现有模型极具挑战性，所有模型在成功率（SR）上均低于人类水平，主要失败模式是过度观察（高Watch率）或观察不足（低Watch率）。例如，Kimi-K2.5偏好探索型策略（高导航步数NS），Doubao-Seed-1.8偏好观察型策略（高Watch率WR），而Doubao-Seed-1.6则保守地依赖最少信息。

通过消融实验验证了智能体设计非瓶颈：以Doubao-Seed-1.8为例，默认设置（最大步骤30、保留1步历史、使用推理）的SR为65.6%；增大步骤上限至40步或历史保留至5步时SR不变；减少步骤至20步时SR降至58.2%；减小历史保留至2步或3步时SR分别为61.1%和64.9%；移除推理时SR降至58.8%。这表明模型底层能力是性能瓶颈。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于其测试环境是短视频平台的高保真复刻版，而非真实部署平台，因此无法模拟推荐引擎、账户个性化或社交图等真实动态因素，可能低估了实际场景中智能体的挑战。未来研究方向包括：将环境从静态复刻扩展至真实社交网络平台，以捕捉更复杂的视频流变化和用户交互模式。此外，该基准仅覆盖中文视频和单一产品生态，语言和文化偏差可能高估或低估观察现象，需要跨语言、跨平台的验证。基于观察控制这一缺失能力轴，可以进一步设计自适应观察策略，例如引入强化学习来动态调整视频观看时长，或结合用户行为模型预测关键信息出现时机。另外，当前任务数量（499个）虽中等，但可结合更细粒度的注意力机制和时序建模，提升智能体在动态屏幕下的信息效率。

### Q6: 总结一下论文的主要内容

本文提出了“动态屏幕原生GUI智能体”这一新问题，针对短视频平台等屏幕内容持续演变的界面，传统静态屏幕假设不再适用。作者构建了首个基准测试LivingScreen，包含基于浏览器的忠实环境、三层任务体系，以及联合评估准确性和信息效率的指标。测试了多个前沿模型后，发现所有模型均未达到人类的成本-准确率性能，主要失败模式为过度观察或观察不足，表明观察控制是当前GUI智能体缺失的关键能力维度。该研究首次将时间维度引入GUI智能体评估，为未来动态界面智能体的发展奠定了基础。
