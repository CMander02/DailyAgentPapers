---
title: "Efficient Agent Training for Computer Use"
authors:
  - "Yanheng He"
  - "Jiahe Jin"
  - "Pengfei Liu"
date: "2025-05-20"
arxiv_id: "2505.13909"
arxiv_url: "https://arxiv.org/abs/2505.13909"
pdf_url: "https://arxiv.org/pdf/2505.13909v2"
github_url: "https://github.com/GAIR-NLP/PC-Agent-E"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "Tool Use & API Interaction"
  - "Learning & Optimization"
relevance_score: 8.0
taxonomy:
  capability:
    - "Tool Use & API Interaction"
    - "Learning & Optimization"
  domain: "General Purpose"
  research_type: "New Method/Model"
attributes:
  base_model: "Claude 3.7 Sonnet"
  key_technique: "PC Agent-E (efficient agent training framework with AI-synthesized trajectory augmentation)"
  primary_benchmark: "WindowsAgentArena-V2"
---

# Efficient Agent Training for Computer Use

## 原始摘要

Scaling up high-quality trajectory data has long been a critical bottleneck for developing human-like computer use agents. We introduce PC Agent-E, an efficient agent training framework that significantly reduces reliance on large-scale human demonstrations. Starting with just 312 human-annotated computer use trajectories, we further augment them by synthesizing diverse alternative action decisions with Claude 3.7 Sonnet. Trained on these enriched trajectories, our PC Agent-E model achieved a remarkable 141 relative improvement, and even surpassed the Claude 3.7 Sonnet by 10% in relative terms on WindowsAgentArena-V2, an improved benchmark we also released. By integrating robust human computer use skills with automated AI data synthesis capabilities, our method not only brought substantial improvements over training on human trajectories alone, but also significantly surpassed direct distillation from Claude 3.7 Sonnet. Code, data and models are available at https://github.com/GAIR-NLP/PC-Agent-E

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决训练高性能计算机使用智能体（Agent）时面临的高质量轨迹数据极度稀缺这一核心瓶颈问题。研究背景是，开发能够像人类一样操作计算机的自主智能体是人工智能领域的重要目标，这类智能体有望自动化大量数字任务。然而，当前模型，特别是开源模型，其性能与顶尖的专有系统（如Claude 3.7 Sonnet）相比存在显著差距。

现有方法的不足主要体现在两个方面：首先，获取大规模、高质量的人类演示轨迹数据成本高昂、过程繁琐，成为制约模型能力提升的关键瓶颈；其次，直接依赖有限的人类轨迹数据进行训练，或者直接从强大教师模型进行知识蒸馏，其数据利用效率和最终性能都存在局限。

因此，本文要解决的核心问题是：如何以极高的数据效率，训练出性能强大、甚至能超越专有模型的计算机使用智能体。为此，论文提出了PC Agent-E这一高效智能体训练框架。其核心思路是，从一个极小规模（仅312条）的人类标注轨迹出发，通过创新的“轨迹增强”方法，利用前沿的Claude 3.7 Sonnet模型为每个轨迹步骤合成多样化的、合理的替代性动作决策，从而极大地丰富和扩展了训练数据。这种方法将人类专家的计算机使用技能与AI的自动化数据合成能力相结合，旨在用最少的人工标注成本，突破数据瓶颈，赋能开源模型达到并超越前沿专有模型的性能水平。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类（计算机使用智能体的架构范式）和数据类（利用大模型进行数据合成）两大方向。

在方法类研究中，现有计算机使用智能体主要分为两种范式：模块化智能体工作流和原生智能体模型。模块化方法依赖人工定义的专业模块和多智能体协作，虽能降低任务复杂度，但因其强依赖人工先验知识，限制了其在新领域的适应性和端到端优化能力。相比之下，原生智能体模型依赖单一模型根据历史和当前状态逐步行动，具有更好的灵活性、泛化能力，并能通过监督微调（SFT）或强化学习（RL）持续提升性能。本文的研究聚焦于通过SFT对原生智能体模型进行高效训练，属于这一主流范式。

在数据类研究中，利用强大LLM合成数据已成为常见做法，主要包括蒸馏法和自改进法。具体到计算机使用领域，数据合成研究又可细分为三类：用于构建基础GUI理解的大规模数据集（如截图描述或问答）、单步视觉定位（如在GUI特定位置合成鼠标点击任务），以及多步轨迹合成（如利用网络教程引导轨迹生成或从智能体自身探索记录中反向合成任务）。本文的工作与这些研究均有所不同：它基于真实世界的人类演示轨迹来合成高质量的多步轨迹，并且特别强调数据效率，即用极少量的人类标注数据（仅312条）作为起点，通过AI（Claude 3.7 Sonnet）合成多样化的替代决策来扩充数据，从而显著减少对大规模人类演示数据的依赖。

### Q3: 论文如何解决这个问题？

论文通过提出PC Agent-E这一高效智能体训练框架来解决高质量轨迹数据稀缺的问题。其核心方法是结合少量真实人类轨迹与AI驱动的数据增强，以生成丰富且高质量的训练数据，从而显著降低对人类演示的依赖。

整体框架包含四个主要步骤：首先，收集312条经过筛选的人类计算机使用轨迹，记录每一步的屏幕状态和操作动作。其次，通过迭代提示Claude 3.7 Sonnet模型，为每个动作重建其背后隐含的人类思考过程，形成带有显式推理的轨迹。接着，采用创新的Trajectory Boost方法进行数据增强：以人类轨迹中每一步的环境快照（包括任务描述、当前屏幕截图和历史上下文）作为输入，利用Claude 3.7 Sonnet并行采样生成多个合理的替代动作决策（包括思考过程和具体动作），从而构建一个以原始人类轨迹为主干、分支节点为合成动作的“轨迹树”。最后，基于这些增强后的轨迹数据，使用一个简洁的端到端架构训练PC Agent-E模型。该架构采用ReAct范式，输入为当前屏幕截图、任务描述和文本形式的历史动作与思考记录，输出为下一步的思考与动作。

关键技术包括：1）**轨迹增强（Trajectory Boost）**：利用前沿大模型的规划与推理能力，在人类轨迹的环境快照上合成多样化的替代决策，极大提升了数据的多样性和信息量，最终从312条原始轨迹扩展出2.7万个训练样本。2）**思考过程重建**：将人类动作背后的隐式决策逻辑显式化，为智能体提供可学习的推理模式。3）**统一动作空间与简易脚手架**：设计了一个涵盖点击、拖拽、输入等操作的统一动作空间，并采用简单一致的训练与推理架构，确保方法聚焦于数据有效性而非工程优化。

创新点在于：通过“人类真实性”与“AI多样性”的有机结合，以极低的人工标注成本（仅312条轨迹）生成了大规模高质量训练数据；提出的Trajectory Boost方法能有效捕捉任务解决路径的多样性；最终训练的模型在性能上不仅大幅超越仅基于人类轨迹训练的基线，甚至超过了直接蒸馏Claude 3.7 Sonnet的效果。

### Q4: 论文做了哪些实验？

论文实验主要包括以下几个方面：

**实验设置**：采用纯截图观察模式，屏幕分辨率统一为1280×720。默认最大步数设为30步，并研究了步数限制对性能的影响。训练基于Qwen2.5-VL-72B骨干模型，图像分辨率1280×720，上下文长度8192个token。

**数据集/基准测试**：主要使用自行发布的改进基准WindowsAgentArena-V2（包含141个任务，涵盖LibreOffice、Chrome、Edge、系统操作、VS Code、VLC等7个类别）进行评估。同时使用OSWorld基准测试跨操作系统（Linux）的泛化能力。

**对比方法**：
- **模型对比**：与领先的专有模型（Claude 3.7 Sonnet及其扩展思考版本、GPT-4o）和开源模型（UI-TARS系列、Qwen2.5-VL-72B）进行比较。
- **方法对比**：将提出的Trajectory Boost方法与两种训练方法对比：（1）在312条人工标注轨迹上进行标准行为克隆；（2）从Claude 3.7 Sonnet进行直接蒸馏（采样3120条轨迹）。

**主要结果与关键指标**：
1. **主实验结果**：PC Agent-E在WindowsAgentArena-V2上取得36.0%的总成功率，相比基础模型Qwen2.5-VL-72B（14.9%）实现141%的相对提升，甚至超过教师模型Claude 3.7 Sonnet（32.6%）10%。在具体应用上，Chrome任务达到64.1%成功率，VS Code任务57.9%，VLC任务35.7%。

2. **数据扩展分析**：定义数据扩展因子s（训练使用总动作数/原始人工轨迹动作数）。仅使用人工轨迹（s=1）性能从14.9%提升至17.2%；Trajectory Boost方法（s=10）将性能提升至36.0%，显著优于单纯使用人工演示。

3. **与蒸馏对比**：Trajectory Boost在多数数据规模下显著优于直接蒸馏基线。效率方面，收集3120条轨迹数据时，蒸馏基线需约900小时，而Trajectory Boost仅需3小时，加速300倍。

4. **测试时扩展**：当步数限制从15步增加到30步时，PC Agent-E能有效利用额外计算，与基础模型的性能差距随步数增加而扩大。

5. **跨平台泛化**：在OSWorld基准上，尽管仅在Windows数据上训练，PC Agent-E在Linux系统上仍实现34%的相对提升（从11.1%到14.9%），验证了方法的泛化能力。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其数据合成过程高度依赖Claude 3.7 Sonnet，这可能导致合成轨迹的多样性和质量受限于该特定模型的认知边界与潜在偏见。此外，实验主要集中于Windows环境下的特定任务，其方法的通用性在不同操作系统（如macOS、Linux）或更复杂的跨应用工作流中尚未得到验证。

未来研究可从以下几个方向深入：首先，探索更廉价或开源的基础模型进行数据合成，以降低对专有模型的依赖并提升方法的可复现性。其次，将框架扩展至更广泛的数字环境（如移动端、网页自动化）和长周期、多模态任务，以测试其泛化能力。再者，研究如何引入强化学习或课程学习，使智能体能在合成数据的基础上通过自主交互持续优化，形成“合成-学习-交互”的闭环。最后，对合成数据的质量进行更细致的评估与控制机制，例如通过对抗性过滤或可信度评分，可能进一步提升训练效率与最终性能。

### Q6: 总结一下论文的主要内容

本文提出了一种高效的计算机使用智能体训练框架PC Agent-E，旨在解决高质量轨迹数据稀缺这一长期瓶颈。其核心贡献在于显著降低了对大规模人工演示数据的依赖。方法上，仅从312条人工标注的计算机使用轨迹出发，利用Claude 3.7 Sonnet合成多样化的替代动作决策以增强数据，并在此基础上训练模型。主要结论显示，在作者发布的新基准WindowsAgentArena-V2上，PC Agent-E模型取得了141%的相对性能提升，甚至以10%的相对优势超越了Claude 3.7 Sonnet本身。该方法通过结合可靠的人类计算机使用技能与自动化AI数据合成能力，不仅显著优于仅使用人工轨迹的训练，也超越了直接从Claude 3.7 Sonnet进行知识蒸馏的效果，为高效训练类人计算机使用智能体提供了新路径。
