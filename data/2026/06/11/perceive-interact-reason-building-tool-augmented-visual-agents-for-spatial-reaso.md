---
title: "Perceive, Interact, Reason: Building Tool-Augmented Visual Agents for Spatial Reasoning"
authors:
  - "Changye Li"
  - "Meng Lu"
  - "Yi Wu"
  - "Ligeng Zhu"
date: "2026-06-11"
arxiv_id: "2606.12830"
arxiv_url: "https://arxiv.org/abs/2606.12830"
pdf_url: "https://arxiv.org/pdf/2606.12830v1"
categories:
  - "cs.CV"
  - "cs.AI"
tags:
  - "Tool-Augmented Agent"
  - "Visual Agent"
  - "Spatial Reasoning"
  - "Multi-step Reasoning"
  - "Reinforcement Learning"
  - "Agent Benchmark"
relevance_score: 9
---

# Perceive, Interact, Reason: Building Tool-Augmented Visual Agents for Spatial Reasoning

## 原始摘要

While recent vision-language models (VLMs) demonstrate strong multimodal understanding, they remain limited in spatial reasoning tasks that require active evidence acquisition and multi-step visual interaction. This limitation suggests that relying solely on implicit visual representations from vision encoders is insufficient for recovering fine-grained spatial evidence. We introduce PERception-Interaction-reason Agent (PERIA), a tool-augmented visual agent for spatial reasoning tasks across map reasoning, visual probing, and vision reconstruction. PERIA uses two lightweight tool families: vision perception tools for exposing textual, symbolic, and spatial evidence, and vision interaction tools for manipulating visual context, tracing paths, and verifying spatial relations. To train PERIA, we develop a unified recipe that combines supervised tool-use trajectory synthesis, composite rewards, and Observation-Relaxed Group-in-Group Policy Optimization (OR-GIGPO) for effective multi-tool behavior. Experiments on 13 benchmarks from 8 datasets show that PERIA-8B improves over the Qwen3-8B backbone by 10.0% on in-distribution benchmarks and 4.4% on out-of-distribution benchmarks, while outperforming previous state-of-the-art baselines of similar size by 7.0%-14.8%. It also achieves performance comparable to much larger models such as Qwen3-VL-235B-A22B-Thinking and GPT-5, demonstrating the effectiveness of PERIA in enhancing spatial reasoning capabilities.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前视觉-语言模型（VLM）在空间推理任务中表现不足的问题。研究背景是，虽然现有VLM在理解多模态内容和推理上能力较强，但在需要主动获取证据、进行多步视觉交互的空间推理任务（如地图推理、视觉探测、视觉重建）中，其效果有限。现有方法的不足主要体现在两方面：1）单纯依赖视觉编码器产生的隐式视觉表征不足以恢复细粒度的空间证据；2）虽然已有研究尝试使用外部视觉工具辅助推理，但这些工具（如OCR、裁剪）通常只读取局部信息或聚焦特定区域，无法构建或更新跨区域的连贯空间状态，导致工具的使用与空间推理需求不匹配。此外，仅仅是让模型访问工具并不足以提升性能——实验表明，开源VLM（如Qwen3）在没有专门工具使用训练的情况下，工具访问反而会导致性能下降，主要失败原因包括工具调用遗漏和工具输出误导。因此，本文要解决的核心问题是：如何训练视觉代理（agent）在统一的推理过程中，有效协调感知工具（提取文本、符号、空间证据）和交互工具（操作视觉上下文、追踪路径、验证空间关系），从而提升多步空间推理的能力。

### Q2: 有哪些相关研究？

- **工具增强视觉推理类**：相关工作包括ReAct、DeepEyes系列、Mini-o3和Think3D。ReAct通过交织推理轨迹与外部动作实现多步推理，但未聚焦空间推理；DeepEyes和Mini-o3展示了多轮图像裁剪等交互工具的有效性，但工具集较小或任务范围窄；Think3D研究3D操作工具。本文与它们的区别在于，本文统一训练感知和交互工具（如视觉感知工具用于提取文本、符号和空间证据，视觉交互工具用于操作视觉上下文、追踪路径和验证空间关系），面向通用空间推理任务，覆盖地图推理、视觉探测和视觉重建等多类任务。

- **VLM空间推理能力研究类**：相关工作涉及3D空间理解、地图地理空间推理、杂乱图像中的视觉搜索探测，以及共享空间技能、低级视觉基元、模拟和重建等。这些研究表明空间推理需要全局-局部对齐、路径追踪、关系验证和多步规划，直接促使本文设计结合视觉证据获取与显式视觉交互的感知-交互工具架构，以弥补纯视觉表示难以恢复细粒度空间证据的缺陷。

- **工具智能体强化学习方法类**：相关工作包括PPO、GRPO、DAPO、RAGEN和GIGPO。PPO提供通用策略优化框架，GRPO从采样组估计相对优势，DAPO通过解耦裁剪和动态采样改进大规模RL，RAGEN处理多轮智能体RL中的稀疏奖励问题，GIGPO为完整轨迹和中间状态分配学习信号。本文在此基础上提出OR-GIGPO，针对工具智能体输出带来的视觉观测变异性，采用观测松弛策略优化替代精确状态匹配，从而更有效协调多工具行为。

### Q3: 论文如何解决这个问题？

论文提出 PERIA（Perception-Interaction-reason Agent）架构来解决空间推理中的视觉证据获取不足和多步交互问题。**核心方法**是将视觉任务建模为部分可观测马尔可夫决策过程（POMDP），通过工具增强的视觉智能体实现主动感知与交互推理。

**整体框架**包含三个关键组件：1）**工具沙箱**（Tool Sandbox）：集成18种视觉工具，划分为感知工具（如文本识别、坐标提取、目标分割）和交互工具（如路径绘制、边界框标注、图像裁剪），通过函数化工具和轻量级工具代理暴露细粒度空间证据；2）**监督微调轨迹合成**：使用GPT-5进行探索-利用采样，在有限交互步数内生成有效工具调用轨迹，并用Qwen3-VL-235B混合推理风格多样性；3）**OR-GIGPO强化学习**：创新性地提出观测松弛组内组策略优化，通过松弛观测匹配（使用文本序列相似度而非精确状态匹配）实现跨时间步的信用分配，结合轨迹级和步骤级优势函数优化多工具协同行为。

**关键技术**包括：复合奖励设计（重复惩罚+格式规范+正确性奖励），以及通过裁剪重要性采样比率稳定训练。实验表明，PERIA-8B在分布内和分布外基准上分别提升10.0%和4.4%，性能媲美GPT-5等大模型。

### Q4: 论文做了哪些实验？

论文在13个基准测试（来自8个数据集）上进行了全面评估。实验设置分为分布内和分布外两个场景：分布内任务包括MapTrace、ReasonMap、ReasonMap-Plus和Visual Probing（Easy/Medium/Hard）四个任务族；分布外任务涵盖Ball Tracking、Paper Folding、Cube Three-View Reasoning、Real-world Spatial Reasoning、V*、MapEval和BabyVision。所有任务均以准确率作为统一指标，其中MapTrace采用NDTW距离<1.0作为成功标准。对比方法包括三组：商业模型（GPT-5、Gemini-2.5-Flash/Pro）、开源VLM（Qwen3-VL系列、InternVL3.5系列）和工具/推理增强模型（VTool-R1、R1-OneVision-7B、Mini-o3）。基线采用Qwen3-VL-Thinking骨干网络（2B/4B/8B）。主要结果：PERIA-8B相比Qwen3-8B骨干在分布内任务平均提升10.0%（从44.1%到54.1%），在分布外任务平均提升4.4%（从31.7%到36.1%），总体平均提升7.0%（从37.4%到44.4%）。PERIA-8B在总体平均准确率上超越所有同规模基线（领先7.0%-14.8%），性能接近Qwen3-235B（44.3%）和GPT-5（46.8%）。消融实验显示：OR-GIGPO相比GRPO平均提升2.4%，相比DAPO提升11.1%；去除工具使用导致平均分降至37.6%；感知工具和交互工具均不可或缺。

### Q5: 有什么可以进一步探索的点？

尽管PERIA在空间推理任务上表现出色，但仍存在若干可进一步探索的方向。首先，当前工具沙箱设计为固定集合，未来可研究动态工具生成与自适应工具选择，使模型能根据任务需求实时构建专用工具。其次，OR-GIGPO算法中的观测放松策略虽提升了训练效率，但可能引入噪声，可探索更精细的置信度校准机制来平衡探索与利用。此外，PERIA在理解抽象空间关系（如拓扑结构）时仍显薄弱，可结合神经符号方法强化符号推理能力。另一个重要方向是跨模态工具融合，例如将物理仿真引擎（如3D物理模拟器）作为交互工具，以处理动态空间变化。最后，当前依赖大规模合成轨迹训练，可探索小样本或零样本工具使用范式，结合基础模型的涌现能力，减少对昂贵合成数据的依赖，从而提升泛化性和部署效率。

### Q6: 总结一下论文的主要内容

这篇论文提出了 PERIA（Perception-Interaction-Reason Agent），一个增强工具的视觉智能体框架，旨在解决现有视觉语言模型在空间推理任务中难以获取细粒度空间证据和进行多步视觉交互的问题。核心贡献在于：首先，设计了包括视觉感知工具（提取文本、符号和空间证据）和视觉交互工具（操作视觉上下文、追踪路径和验证空间关系）的两类轻量级工具族；其次，提出了统一的训练方案，包括监督式工具使用轨迹合成、复合奖励，以及核心优化方法 Observation-Relaxed Group-in-Group Policy Optimization (OR-GIGPO)，以实现有效的多工具行为。通过在8个数据集的13个基准测试上实验，PERIA-8B 相比 Qwen3-8B 基座模型在分布内和分布外基准上分别提升10.0%和4.4%，并超越同等规模的最先进基线7.0%-14.8%，性能媲美 Qwen3-VL-235B-A22B-Thinking 和 GPT-5 等更大模型。该工作证明了训练有素的视觉工具使用是构建更强空间推理智能体的有效方向。
