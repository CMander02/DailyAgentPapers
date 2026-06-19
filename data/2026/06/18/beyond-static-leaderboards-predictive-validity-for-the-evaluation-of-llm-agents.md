---
title: "Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents"
authors:
  - "Dhaval C. Patel"
  - "Kaoutar El Maghraoui"
  - "Shuxin Lin"
  - "Yusheng Li"
  - "Tianjun Feng"
  - "Chun-Yi Tsai"
  - "Yihan Sun"
  - "Wei Alexander Xin"
  - "Akshat Bhandari"
  - "Tanisha Rathod"
  - "Aaron Fan"
  - "Sanskruti Vijay Shejwal"
  - "Tomas Pasiecznik"
  - "Sagar Chethan Kumar"
  - "Tanmay Agarwal"
  - "Rohith Kanathur"
  - "Sam Colman"
  - "Amaan Sheikh"
  - "Dev Bahl"
  - "Ann Li"
date: "2026-06-18"
arxiv_id: "2606.19704"
arxiv_url: "https://arxiv.org/abs/2606.19704"
pdf_url: "https://arxiv.org/pdf/2606.19704v1"
categories:
  - "cs.AI"
tags:
  - "Agent评估"
  - "预测效度"
  - "基准设计"
  - "分布外泛化"
  - "多维度评估"
relevance_score: 9.0
---

# Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents

## 原始摘要

Agent benchmarks are growing fast, but no single benchmark touches more than four or five of the dimensions that deployment exposes. This paper aggregates the largest coordinated deep-dive of one MCP-based industrial-agent benchmark to date: fourteen parallel implementation studies covering new asset classes (including a multi-modal visual extension), alternative orchestrations, retrieval strategies, reasoning modes, infrastructure optimizations, and evaluation-methodology probes. Consolidating those studies with seven prior agent benchmarks, we argue that aggregate-score leaderboards systematically underspecify deployed-agent evaluation. Rankings derived from aggregate scores do not transfer to out-of-distribution settings; recent public-to-hidden competition retrospectives provide direct empirical evidence of this rank instability. We propose ranking configurations by predictive validity, the correlation between in-sample and out-of-sample rank, rather than in-sample mean, and report a twelve-tier measurement apparatus that exposes the deployment-relevant dimensions HELM and its agent-era successors collapse. The position is operationalized through three falsifiable out-of-distribution criteria with explicit thresholds; existing evidence partly supports it but is too thin to confirm. We close with a pre-registered pilot design and a field-level vision for what the next generation of agentic benchmarks should report.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前LLM智能体评估中存在的根本性问题：现有的排行榜和基准测试无法有效预测智能体在实际部署中的表现。研究背景是，LLM智能体已具备规划、调用工具、跨轮次复用工件及多智能体协作等复杂能力，但评估仍沿用传统单次基准测试的聚合评分排行榜。现有方法的不足包括两点：第一，聚合评分排行榜存在严重的排名不稳定性——在近期149支团队参与的智能体竞赛中，执行任务的公开榜排名与隐藏评估排名的斯皮尔曼相关系数仅为-0.13，表明排行榜排名无法迁移到分布外场景；第二，虽然HELM等框架扩展了单次模型的测量维度，但智能体引入了编排策略、多轮工件复用、工具调用规范性等正交维度，现有评估体系完全未涉及这些关键因素。本文要解决的核心问题是：提出以预测效度（即样本内排名与样本外排名之间的相关性）替代样本内均值作为排名标准，并建立包含十二个测量层级的评估架构，从而系统性地揭示被聚合评分排行榜掩盖的部署相关评估维度。

### Q2: 有哪些相关研究？

1. **评测类研究**：现有工作如HELM扩展了单次模型的评估维度，但未覆盖智能体特有的编排、工具调用等正交维度；多维度框架和行为测试虽提出结构变化，但未提供排名标准。本文则提出预测有效性作为新的排名标准。

2. **基准测试类研究**：近年来涌现的智能体基准（如AssetOpsBench、MCP-Bench等）各自关注轨迹级评估的不同方面，但仍使用聚合分数排名。本文通过整合7个前沿基准和14个并行实现研究，发现了聚合分数排名无法替代部署表现。

3. **方法类研究**：针对工业资产生命周期管理领域，14个并行实现研究揭示了不同架构选择下出现互补性失败模式。与这些研究的关系在于，本文将其发现系统化，提出12层测量框架，而非仅关注单一架构的排名。

4. **实践验证类**：最近的149支团队竞赛显示公开与隐藏排名的斯皮尔曼相关系数极低（执行轨迹ρ=-0.13），直接验证了排名不稳定性。本文提出三个可证伪的预测有效性标准（留出、跨子集、对抗），而现有实践仅依赖样本内均值排名。

### Q3: 论文如何解决这个问题？

论文提出用预测有效性（predictive validity）替代均值聚合分数作为排名标准，核心方法如下：

**整体框架**：放弃单一聚合分数排名，构建基于分布外（OOD）稳定性的评估体系。核心是测量配置在样本内排名与样本外排名之间的斯皮尔曼相关性，而非样本内均值。

**主要组件**：1）**十二层测量装置**：分为核心能力层（T1-T7：通过率、工具合规、规划质量、能力轴、成本效率、失败模式、可复现性）和部署扩展层（T8-T12：部署基础设施、多轮对话、推理模式自适应、知识增强、证据锚定）。这是对七个现有基准和十四个实现研究维度的聚合，每个维度正交或近似正交。2）**三个可证伪的OOD标准**：A. 保持场景分割（轻度偏移）；B. 跨子集迁移（中度偏移，如不同资产类间的排名稳定性）；C. 对抗性扰动（强偏移，如语义等价改写、标识符重命名等）。3）**复合排名分数**：PV(c)=α·Ȳc - β·σOOD - γ·IQR，组合样本内均值与跨OOD标准的排名稳定性。

**创新点**：1）识别并量化聚合分数隐藏的行为差异（如推理模式在清晰度上差异31pp、多轮延迟差异4.2倍、检索策略的token膨胀10倍）；2）引入判断无关组件解决LLM-as-judge偏差问题（如CAR从0.68提升至0.91）；3）基于CODS-2025挑战赛数据（执行跟踪public-private ρ=-0.13）证明当前排名不稳定，并提出四个实证条件（如ρ<0.85、Jaccard重叠<0.85）来验证该方法的有效性。

### Q4: 论文做了哪些实验？

论文围绕MCP工业级智能体基准展开14项平行实现研究。实验设置包括：启用深思推理（Gemma-4-26B规划器，AssetOpsBench 40个多智能体场景）、技能知识插件（Llama-4-Maverick-17B与Granite-3-8B在不同RAG策略下对比）、PHMForge基准（99个专家编写场景，39个MCP工具）。主要数据集包括AssetOpsBench、PHMForge（8类工业资产）、ARE/Gaia2（450条人工标注轨迹）、以及智能电网/风电场等垂直领域。对比方法涉及单程RAG vs. 多跳知识插件、ReAct vs. plan-execute基座、不同骨干模型及推理模式。关键结果：启用周密推理使规划延迟增加41.9%（15.08s→18.32s），但清晰度提升31个百分点（61%→92%）、幻觉降低7个百分点；知识插件以4.5-10倍token膨胀实现约90%准确率；PHMForge在轴承-电机跨设备转移中掉41个百分点（84.1%→42.7%），模糊查询从80.6%降至48.6%；LLM评判者间信度Krippendorff α=0.61（低于人工的0.74-0.82）。所有实验暴露出静态榜单无法捕捉鲁棒性、信任度、泛化性及纵向漂移四个维度。

### Q5: 有什么可以进一步探索的点？

基于论文的核心论点——聚合分数排名无法有效泛化到分布外场景，结合其提出的预测效度框架，未来研究可从以下方向深入：

首先，论文提出的三项可证伪条件（如排名相关性ρ<0.85、前3名在分布外的稳定性等）仍需通过大规模受控实验验证。可进一步设计跨多个市场环境（如金融交易、医疗诊断）的测试集，系统测量预测效度指标的鲁棒性。

其次，当前MCP基准仅覆盖工业场景，缺乏对开放域交互的刻画。建议构建混合研究框架，整合Agent在对话、代码生成和机器人控制中的跨维度表现。具体可参考HELM多轴评价经验，但需引入动态难度调节机制——允许测试案例根据Agent实时表现自适应调整，以暴露过度拟合问题。

另外，第5组实验显示知识库插件虽提高2.2倍准确率但引发4.5-10倍令牌消耗，揭示效率与性能的帕累托边界。未来需开发基于信息论的多目标优化算法，在保持预测效度前提下权衡延迟、计算成本和准确性。最后，预注册的试点设计应考虑因果推理校验，例如通过反事实生成验证排名转移是否源于偶然相关性。

### Q6: 总结一下论文的主要内容

该论文指出当前LLM Agent基准测试存在根本性缺陷：单一基准无法覆盖实际部署场景的所有维度，而基于聚合得分的排行榜系统性地低估了Agent评估的复杂性。核心贡献在于提出超越静态排行榜的预测有效性（Predictive Validity）评估框架，即用样本内与样本外排名相关性替代平均得分作为评估标准。方法上，论文汇总了基于MCP工业Agent基准的14项并行研究（涵盖多模态扩展、编排方式、检索策略、推理模式等12个评估层级），结合7个现有基准分析，论证了聚合分数排名在分布外场景中具有不稳定性。主要结论包括：现有基准无法满足部署需求，公共与私有竞赛数据直接证明排名的不稳定性；明确提出了三个可证伪的分布外判据及阈值，并给出预注册实验设计方案。该工作推动Agent评估从静态得分向动态预测有效性转变，对构建更可靠的AI系统评估体系具有重要方法论意义。
