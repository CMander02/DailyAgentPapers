---
title: "FedGUI: Benchmarking Federated GUI Agents across Heterogeneous Platforms, Devices, and Operating Systems"
authors:
  - "Wenhao Wang"
  - "Haoting Shi"
  - "Mengying Yuan"
  - "Yiquan Lin"
  - "Panrong Tong"
  - "Hanzhang Zhou"
  - "Guangyi Liu"
  - "Pengxiang Zhao"
  - "Yue Wang"
  - "Siheng Chen"
date: "2026-04-16"
arxiv_id: "2604.14956"
arxiv_url: "https://arxiv.org/abs/2604.14956"
pdf_url: "https://arxiv.org/pdf/2604.14956v1"
github_url: "https://github.com/wwh0411/FedGUI"
categories:
  - "cs.MA"
tags:
  - "GUI Agent"
  - "Federated Learning"
  - "Benchmark"
  - "Cross-Platform"
  - "Cross-Device"
  - "Cross-OS"
  - "Privacy"
  - "Evaluation"
relevance_score: 7.5
---

# FedGUI: Benchmarking Federated GUI Agents across Heterogeneous Platforms, Devices, and Operating Systems

## 原始摘要

Training GUI agents with traditional centralized methods faces significant cost and scalability challenges. Federated learning (FL) offers a promising solution, yet its potential is hindered by the lack of benchmarks that capture real-world, cross-platform heterogeneity. To bridge this gap, we introduce FedGUI, the first comprehensive benchmark for developing and evaluating federated GUI agents across mobile, web, and desktop platforms. FedGUI provides a suite of six curated datasets to systematically study four crucial types of heterogeneity: cross-platform, cross-device, cross-OS, and cross-source. Extensive experiments reveal several key insights: First, we show that cross-platform collaboration improves performance, extending prior mobile-only federated learning to diverse GUI environments; Second, we demonstrate the presence of distinct heterogeneity dimensions and identify platform and OS as the most influential factors. FedGUI provides a vital foundation for the community to build more scalable and privacy-preserving GUI agents for real-world deployment. Our code and data are publicly available at https://github.com/wwh0411/FedGUI..

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决图形用户界面（GUI）智能体在现实世界分布式训练中面临的关键挑战。传统GUI智能体训练依赖于集中式数据收集和人工标注，这种方法成本高昂且难以扩展。尽管用户日常使用各类GUI设备（如手机、网页、桌面应用）会自然产生大量交互数据，可作为低成本训练数据源，但由于隐私顾虑，这些数据无法被公开共享和集中利用。联邦学习（FL）作为一种隐私保护的分布式学习范式，为此提供了潜在解决方案，但现有研究缺乏能够系统反映真实世界跨平台、跨设备、跨操作系统等异构性的基准测试，限制了联邦学习在GUI智能体领域的有效发展和评估。

具体而言，现有方法如FedMABench仅支持移动端（Android）用户间的联邦协作，忽略了将网页和桌面环境用户纳入协作以进一步提升性能的潜力，同时也未考虑设备、操作系统、数据来源等多种异构性维度。这些不足导致两个核心问题未被充分探索：第一，如何实现跨平台（移动、网页、桌面）的GUI智能体联邦训练，以及这种扩展的协作是否真能提升性能；第二，如何量化表征和衡量跨越不同平台、操作系统、设备和数据源的现实异构性。

因此，本文的核心问题是构建一个全面的基准测试FedGUI，以支持在异构的真实世界环境中开发与评估联邦GUI智能体。FedGUI通过精心构建的六个数据集，系统研究跨平台、跨设备、跨操作系统和跨数据源四种关键异构性，旨在为社区提供一个基础，以构建更具可扩展性和隐私保护能力的实用化GUI智能体。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为四类：单平台GUI智能体、跨平台GUI智能体、联邦学习以及联邦GUI智能体。

**单平台GUI智能体**：早期研究专注于特定平台，如移动端（应用导航）、网页端（浏览器任务）和桌面端（工作流自动化）。这些方法在各自平台内表现良好，但因其能力高度专业化，难以有效迁移到其他界面模态，**跨平台泛化能力有限**。

**跨平台GUI智能体**：为克服泛化限制，近期研究转向开发能在移动、网页和桌面等多种界面环境中统一操作的智能体，涵盖了模型和评测基准。虽然这些方法展现了**跨平台统一推理的潜力**，但其依赖**集中式数据收集**，扩展成本高昂，且难以捕捉真实世界分布式场景中完整的数据多样性。

**联邦学习**：作为一种去中心化范式，联邦学习允许模型在不传输原始数据的情况下进行协同训练，通过本地优化和周期性服务器聚合，在保护隐私的同时实现大规模学习，并能**自然地捕捉用户特定行为**。

**联邦GUI智能体**：FedMABench是首个针对联邦移动智能体的评测基准。然而，其**范围仅限于移动设备用户间的协作**，忽略了不同平台用户可贡献于统一智能体系统的更广泛背景。相比之下，本文提出的FedGUI是**首个全面的联邦智能体评测基准**，其创新在于系统地涵盖了异构数据源、设备类型和操作系统，在更广泛的场景谱系中进行评测，从而弥补了现有工作的不足。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为FedGUI的综合性基准测试框架来解决联邦GUI智能体在异构平台、设备和操作系统上缺乏评估标准的问题。其核心方法、架构设计和关键技术如下：

**整体框架与主要模块：**
FedGUI遵循典型的联邦学习协议，构建了一个研究友好的基础设施。其整体架构基于ms-swift框架进行扩展，通过模块化核心流程无缝集成了联邦学习组件。主要模块包括：1) **数据集构建模块**：系统性地收集并整合了来自移动端（如AndroidControl、Android-in-the-Wild）、网页端（如Mind2Web、GUIAct）和桌面端（如OmniAct、AgentSynth）的七类现有GUI交互数据集，形成六个精心策划的基准数据集（FedGUI-Platform, -Device, -OS, -Mobile, -Web, -Full），涵盖29个子集。2) **异构性建模模块**：明确定义并构建了四种关键异构性维度——跨平台、跨设备、跨操作系统和跨数据源，并设计了从IID（独立同分布）到高度倾斜（Skew）等多种数据划分配置来模拟不同程度的非IID场景。3) **统一动作空间模块**：设计了一个跨移动、网页和桌面平台的统一动作空间，识别出六个基本共享动作（如点击、输入），并将平台特定动作映射到系统提示中定义的两个不同域，从而实现跨平台的一致策略学习和参数聚合。4) **模型与算法集成模块**：支持超过20种主流视觉语言模型（包括GPT系列、Qwen系列、Gemma等）和7种代表性联邦学习算法（如FedAvg、FedProx、SCAFFOLD），确保在相同配置下进行公平、可复现的比较。

**创新点：**
1.  **首个跨平台联邦GUI基准**：首次创建了一个全面评估联邦GUI智能体在移动、网页和桌面多平台环境下性能的基准，填补了该领域的空白。
2.  **系统性异构性刻画**：创新性地从四个维度（平台、设备、OS、数据源）对GUI交互数据中固有的复杂非IID模式进行系统性的分类、建模和控制研究，并构建了从均匀到极端倾斜的渐进式数据分区变体。
3.  **统一动作空间设计**：提出了跨平台的统一动作表示方法，解决了不同平台交互动作异构带来的模型聚合难题，是实现有效跨平台联邦学习的关键技术。
4.  **现实且可扩展的实验设置**：通过FedGUI-Full数据集整合了所有异构性维度，并模拟了不同客户端规模和分布偏斜的真实联邦场景，为社区提供了研究可扩展、隐私保护的GUI智能体的重要基础。实验验证了跨平台协作能提升性能，并识别出平台和操作系统是最具影响力的异构性因素。

### Q4: 论文做了哪些实验？

论文在FedGUI基准上进行了广泛的实验，以评估联邦GUI智能体在异构环境下的性能。实验设置方面，主要采用Qwen2-VL-7B作为基础模型，并应用LoRA进行高效适配。训练共进行30个联邦轮次，每轮均匀采样10%的训练数据，并随机选择3个客户端参与，以模拟真实的用户可用性和客户端退出场景。评估采用三个动作级指标：动作类型准确率（Type）、空间定位准确率（Ground）以及综合要求类型和内容定位都正确的成功率（SR）。

实验使用了FedGUI提供的六个数据集，包括FedGUI-Full、FedGUI-Platform、FedGUI-OS、FedGUI-Device、FedGUI-Web等，以系统研究跨平台、跨设备、跨操作系统和跨数据源四种异构性。对比方法包括集中式训练（Central）、仅本地训练（Local）以及多种联邦学习算法，如FedAvg、FedProx、SCAFFOLD、FedYogi、FedAdam、FedAvgM和FedAdagrad。

主要结果和关键指标如下：
1.  **跨平台协作的有效性**：实验证实跨平台联邦协作能显著提升性能。例如，在平台异构（非IID）设置下，联邦学习算法（如FedAdam）能将成功率从本地模型的极低水平（如在平台倾斜设置下，某些平台低至5.53%）显著恢复至可用的水平（如FedAdam在桌面平台达50.62%），证明了联邦学习对于弥合平台间领域隔离至关重要。
2.  **异构性维度的影响**：研究发现平台和操作系统是影响性能的最关键异构性因素。在平台倾斜分布下，性能相比IID设置下降明显；跨操作系统异构性导致的性能下降比跨设备或跨数据源更为严重。
3.  **算法性能比较**：在非IID设置下，基于自适应优化器的算法（如FedAdam、FedYogi）通常表现出更强的鲁棒性和更高的平均性能。例如，在平台倾斜设置下，FedAdam在桌面、网页和移动平台的平均成功率为42.95%，优于FedAvg的35.05%。
4.  **模型骨干分析**：对超过20个视觉语言模型的实验表明，经过联邦微调后，多个紧凑的开源模型性能可以超越大型专有模型，凸显了联邦微调的价值。
5.  **跨应用异构性**：在FedGUI-Web数据集上的实验显示，虽然应用类别的极端倾斜会影响性能（例如从App IID到App Skew，平均成功率从47.68%降至45.92%），但其影响远小于跨平台异构性带来的挑战。

这些实验系统地揭示了联邦GUI智能体在真实异构环境中的行为，为构建更可扩展、保护隐私的GUI智能体奠定了基础。

### Q5: 有什么可以进一步探索的点？

本文提出的FedGUI基准虽然系统性地定义了跨平台异构性，但其探索仍处于初步阶段。一个核心局限是实验主要验证了异构性的存在及其影响程度，但尚未深入探究其背后的根本成因（例如，是界面元素渲染差异、交互逻辑不同，还是底层系统API的多样性导致了性能波动）。未来研究可进一步拆解这些因素，并设计针对性的模型架构或训练策略来缓解特定类型的异构性。

此外，基准中的任务和数据集虽具代表性，但规模和复杂性可能仍与真实世界海量、动态变化的GUI环境有差距。未来的探索点可以包括：1）研究更高效的联邦学习算法，如在客户端选择、个性化模型或知识蒸馏方面进行优化，以降低异构性带来的收敛困难与通信开销；2）将研究扩展到更具挑战性的序列决策任务（如多步骤复杂工作流），并考虑动态环境（如GUI界面更新）下的持续学习能力；3）探索联邦GUI智能体与多模态基础模型（如具备屏幕理解的VLMs）的结合，利用其强大的泛化能力作为先验，或许能更优雅地处理跨平台差异。

### Q6: 总结一下论文的主要内容

该论文提出了FedGUI，这是首个用于在移动、网页和桌面平台上开发和评估联邦GUI智能体的综合性基准。其核心贡献在于解决了传统集中式训练GUI智能体面临的高成本和可扩展性挑战，并通过引入联邦学习（FL）来应对现实世界中跨平台的异构性问题。

论文首先定义了问题：现有研究缺乏能够捕捉真实、跨平台异构性的基准，这阻碍了联邦学习在GUI智能体领域的潜力。为此，FedGUI构建了一套包含六个数据集的基准，用于系统研究四种关键的异构性类型：跨平台、跨设备、跨操作系统和跨数据源。

方法上，FedGUI通过广泛的实验评估联邦GUI智能体。主要结论包括：首先，跨平台协作能提升性能，将先前仅限于移动设备的联邦学习扩展到了多样化的GUI环境；其次，研究证实了不同异构性维度的存在，并识别出平台和操作系统是最具影响力的因素。该工作为社区构建更具可扩展性和隐私保护的现实部署GUI智能体奠定了重要基础。
