---
title: "LABSHIELD: A Multimodal Benchmark for Safety-Critical Reasoning and Planning in Scientific Laboratories"
authors:
  - "Qianpu Sun"
  - "Xiaowei Chi"
  - "Yuhan Rui"
  - "Ying Li"
  - "Kuangzhi Ge"
  - "Jiajun Li"
  - "Sirui Han"
  - "Shanghang Zhang"
date: "2026-03-12"
arxiv_id: "2603.11987"
arxiv_url: "https://arxiv.org/abs/2603.11987"
pdf_url: "https://arxiv.org/pdf/2603.11987v1"
categories:
  - "cs.AI"
tags:
  - "安全评估"
  - "多模态Agent"
  - "基准测试"
  - "实验室自动化"
  - "安全关键推理"
  - "规划"
relevance_score: 7.5
---

# LABSHIELD: A Multimodal Benchmark for Safety-Critical Reasoning and Planning in Scientific Laboratories

## 原始摘要

Artificial intelligence is increasingly catalyzing scientific automation, with multimodal large language model (MLLM) agents evolving from lab assistants into self-driving lab operators. This transition imposes stringent safety requirements on laboratory environments, where fragile glassware, hazardous substances, and high-precision laboratory equipment render planning errors or misinterpreted risks potentially irreversible. However, the safety awareness and decision-making reliability of embodied agents in such high-stakes settings remain insufficiently defined and evaluated. To bridge this gap, we introduce LABSHIELD, a realistic multi-view benchmark designed to assess MLLMs in hazard identification and safety-critical reasoning. Grounded in U.S. Occupational Safety and Health Administration (OSHA) standards and the Globally Harmonized System (GHS), LABSHIELD establishes a rigorous safety taxonomy spanning 164 operational tasks with diverse manipulation complexities and risk profiles. We evaluate 20 proprietary models, 9 open-source models, and 3 embodied models under a dual-track evaluation framework. Our results reveal a systematic gap between general-domain MCQ accuracy and Semi-open QA safety performance, with models exhibiting an average drop of 32.0% in professional laboratory scenarios, particularly in hazard interpretation and safety-aware planning. These findings underscore the urgent necessity for safety-centric reasoning frameworks to ensure reliable autonomous scientific experimentation in embodied laboratory contexts. The full dataset will be released soon.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决人工智能体在自主科学实验室环境中的安全关键推理与规划能力评估缺失的问题。研究背景是，随着多模态大语言模型（MLLMs）和具身智能的发展，AI智能体正从实验室助手演变为能够自主操作的“自动驾驶实验室”的决策者。然而，实验室环境充满易碎玻璃器皿、危险化学品和高精度设备，任何规划错误或风险误判都可能导致不可逆的严重后果。

现有方法存在明显不足。当前的评估范式是割裂的：要么将安全视为语言对齐问题（关注有害文本生成），要么视为低层级的运动规划问题（关注无碰撞轨迹）。这些方法未能捕捉实验室环境中特有的语义与物理交互的复杂性，即需要将化学专业知识与细粒度感知（如识别全球化学品统一分类和标签制度符号、透明玻璃器皿）紧密结合，并在多步骤、长时程的工作流程中保持稳健的抑制控制能力。这种评估空白使得在赋予智能体物理操作权限前，难以验证其在高风险场景下的安全关键可靠性。

因此，本文要解决的核心问题是：如何在一个高风险、多模态的自主机器人实验室环境中，正式地定义、建模和评估实验安全性。为此，论文引入了LABSHIELD基准，它基于美国职业安全与健康管理局标准和全球化学品统一分类和标签制度，建立了一个涵盖164项操作任务的严格安全分类体系，旨在系统评估MLLMs在危险识别和安全关键推理方面的能力，弥补现有评估在语义-物理交织风险层面的不足。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两大类，但均未能全面解决实验室环境中的具身智能体安全问题。

**第一类是通用操作与导航基准**。这类工作（如各类机器人操作与移动基准）侧重于评估机械运动的精确性和任务完成度，但通常对科学实验室中复杂的语义风险（如化学品不相容性）视而不见。它们将安全简化为碰撞避免，忽略了基于GHS等标准的化学处理规程。

**第二类是符号推理与化学程序知识评估**。这类研究关注文本层面的规则和流程知识，但评估往往脱离具体的感知与运动执行环境，导致“纸上安全”与物理实践之间的鸿沟。智能体可能熟记文本规则，却在面对视觉和空间复杂的真实场景时无法可靠应用。

此外，当前关于自动化实验室系统和异常检测的研究，主要聚焦于事后偏差检测，而非主动评估具身智能体在实时物理交互中基于安全约束进行推理和规划的能力。

**本文与这些工作的关系与区别**在于：LABSHIELD 弥合了上述割裂的范式，首次提出了一个**面向具身智能体在自主科学发现中安全推理的统一评估框架**。它将严格的OSHA与GHS安全标准融入多视角、多任务的基准构建中，要求模型在逼真的实验室场景下同时进行危险识别与安全关键规划，从而系统性地评估其安全意识和决策可靠性。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为LABSHIELD的多模态基准测试框架来解决实验室环境中安全关键推理与规划的评估问题。其核心方法是建立一个基于现实实验室场景、严格遵循安全标准（如OSHA和GHS）、并具有层次化结构的评估体系。

整体框架基于经典的感知-推理-规划（PRP）架构，并将其专门化以适应非结构化的科学实验室环境。该框架包含四个主要构建阶段：数据采集、任务构建、多项选择题（MCQ）生成和半开放式问答（QA）标注。数据采集使用Astribot机器人平台，在三个代表性实验室区域（工作台、通风橱、水槽）通过头、躯干和手腕摄像头收集同步多视角视觉数据。任务构建则依据一个双轴分类法：在操作维度上，定义了从原子动作到移动操纵的四个复杂度层级；在安全维度上，定义了从无害操作到高风险违规的四个风险等级。基于此分类法，利用大语言模型生成候选任务，并最终筛选出164个任务以确保多样性和平衡性。

关键技术包括：1）**安全感知评估**：专注于识别安全关键异常（如GHS象形图、透明玻璃器皿），而非泛泛的对象检测，并利用多视角观测来缓解空间遮挡问题。2）**安全基础推理评估**：要求模型综合多视角感知输入与结构化安全知识（如试剂不相容性），进行因果推理以预测潜在风险。3）**安全设计规划评估**：评估模型在严格安全约束下生成可执行动作序列的能力，特别是其优先考虑安全协议、甚至主动拒绝危险指令的能力。

创新点主要体现在：1）**系统化的双轴分类法**，将任务的操作复杂性与安全风险等级明确关联，实现了对智能体能力的细粒度量化。2）**解耦的PRP评估维度**，允许对安全失误进行模块化归因分析，精确定位是感知、推理还是规划环节的缺陷。3）**双轨评估框架**，结合了封闭式的MCQ和开放式的半开放QA，揭示了模型在一般领域知识测试与专业安全场景性能之间存在显著差距（平均下降32.0%），突显了安全中心推理框架的紧迫必要性。

### Q4: 论文做了哪些实验？

论文在LABSHIELD基准上对33个多模态大语言模型进行了系统评估，涵盖闭源、开源和具身模型三类。实验在零样本设置下进行，解码温度固定为0.7。评估采用双轨框架：多选题（MCQ）和半开放式问答（Semi-open QA）。半开放式评估采用基于GPT-4o的标准化LLM-as-a-Judge协议，并将所有指标归一化到0-100分。同时，论文还报告了经过领域训练的标注者提供的人类基线作为上限参考。

主要对比了25个代表性模型，并进行了全面的消融研究。关键数据指标包括：模型在专业实验室场景下的平均性能下降达32.0%；在高风险场景（Safety L23）中，模型普遍低估风险；尽管GPT-4o和Claude-4 Sonnet在MCQ上准确率相同（73.2%），但安全得分差异显著（Claude为51.2 vs. GPT-4o的41.7）；人类专家在计划得分和对齐通过率上表现一致（88.4% vs. 85.4%），而GPT-4o则存在巨大差距（78.4% vs. 32.9%），揭示了“幻觉成功”。

主要结果发现：1）MCQ高准确率不能可靠迁移到需要安全基础决策的半开放环境，存在系统性差距；2）具有显式推理机制的模型表现出更稳定的安全行为和更低的风险低估倾向，但在高风险场景中依然脆弱；3）安全性能与危险感知能力（如不安全Jaccard和危险Jaccard）呈线性相关；4）具身模型相比通用多模态模型并未带来显著安全优势；5）消融研究表明，明确的安全约束、多视角集成（特别是腕部视角提供的近距离语义）以及高视觉分辨率对安全性能至关重要；6）模型普遍存在对透明器物的“感知盲区”，这直接破坏了安全感知推理的完整性。

### Q5: 有什么可以进一步探索的点？

基于论文内容，其局限性及未来研究方向可从多个维度进一步探索。首先，论文揭示了MLLM在抽象安全知识与具身物理推理之间存在显著脱节，这提示未来需开发更紧密融合视觉感知与物理常识的推理框架，例如通过增强对透明器皿、液体状态等细微视觉特征的 grounding 能力。其次，当前基准主要基于静态任务评估，未来可引入动态、交互式仿真环境，以测试智能体在连续决策和意外事件中的实时安全规划能力。此外，论文依赖现有安全标准（如OSHA），但实验室风险常具领域特异性，因此可探索自适应安全规范的学习机制，使智能体能够根据新设备或新物质动态更新风险知识。最后，评估聚焦于模型性能，未来可研究将安全约束形式化为可微目标或强化学习奖励，从而在训练中直接优化安全对齐，而不仅限于事后评估。

### Q6: 总结一下论文的主要内容

该论文提出了LABSHIELD基准，旨在评估多模态大语言模型在科学实验室这一高风险环境中的安全关键推理与规划能力。核心问题是当前AI代理在向自主实验室操作员演进时，其安全意识和决策可靠性缺乏明确的定义与评估，而实验室中易碎器皿、危险物质和高精度设备使得规划错误或风险误判可能造成不可逆后果。

论文的主要贡献是构建了一个基于美国职业安全与健康管理局标准和全球化学品统一分类标签制度的、现实的多视角基准。它建立了一个严谨的安全分类体系，涵盖164个具有不同操作复杂性和风险特征的任务。方法上，论文采用双轨评估框架，对20个专有模型、9个开源模型和3个具身模型进行了系统评估。

主要结论揭示了一个系统性差距：模型在通用领域多项选择题的准确性与在半开放问答中体现的安全性能之间存在显著落差，在专业实验室场景中平均下降32.0%，尤其在危险识别和安全意识规划方面表现薄弱。这凸显了开发以安全为中心的推理框架的紧迫性，以确保具身实验室环境中自主科学实验的可靠性。
