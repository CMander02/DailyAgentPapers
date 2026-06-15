---
title: "When the Tool Decides: LLM Agents Defer Blindly to Graph Neural Network Tools, and Stronger Backbones Defer More"
authors:
  - "Zhongyuan Wang"
  - "Pratyusha Vemuri"
date: "2026-06-12"
arxiv_id: "2606.14476"
arxiv_url: "https://arxiv.org/abs/2606.14476"
pdf_url: "https://arxiv.org/pdf/2606.14476v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "LLM Agent"
  - "Graph Neural Network Tool"
  - "Tool Use"
  - "Agent Judgment"
  - "ReAct Agent"
  - "Node Classification"
  - "Agent-Tool Interaction"
  - "Selective Invocation"
  - "Agent Evaluation"
relevance_score: 9.5
---

# When the Tool Decides: LLM Agents Defer Blindly to Graph Neural Network Tools, and Stronger Backbones Defer More

## 原始摘要

A growing line of work equips large language model (LLM) agents with graph neural networks (GNNs) as callable tools, assuming the agent exercises judgment over when and how much to rely on such a tool. We test this directly. We expose a frozen GNN to a ReAct-style LLM agent as an explicit tool and measure, on node classification over a text-attributed graph (ogbn-arxiv, replicated on WikiCS), whether the agent uses the tool or merely obeys it. We find the agent does not exercise judgment: its predictions agree with the raw GNN's 97.6-99.2% of the time (5 seeds), collapsing into a GNN parrot that adopts the tool's output wholesale and bypasses its own reasoning. Sweeping backbone capability (Qwen2.5 0.5B-7B), the deference is not a weak-model artifact: among models able to invoke the tool, agreement rises with capability (0.60 to 0.98 from 1.5B to 7B). Crucially, the cost of deference does not shrink as capability grows and grows where alternatives emerge: a per-node oracle over the available actions beats the parrot by 0.09-0.18 at 3B and 0.12-0.22 at 7B, roughly doubling at high homophily, because the parrot is pinned to the frozen GNN while the agent's alternatives improve; at 7B a simple neighbour-label tool overtakes the GNN at high homophily (0.81 vs 0.71) yet the agent still defers. A simple selective-invocation gate recovers about half of that high-homophily gap (0.71 to 0.83) but yields no net global gain, and held-out estimates bound the best achievable gate over standard test-time features to at most a third of the oracle headroom: reliable selective invocation looks limited by available information, not merely router design. Our results are a cautionary measurement: evaluations of agent+tool systems cannot assume the agent adds judgment on top of the tool, and selective invocation must be designed in rather than expected to emerge from scale.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文主要研究了大语言模型（LLM）代理在调用图神经网络（GNN）作为工具时的行为模式。现有方法通常假设LLM代理能作为一个有判断力的调用者：在GNN可靠时依赖其输出，在不可靠时则依靠自身推理或其他证据。然而，这种假设是否成立并未被严格验证。

本文通过设计一个直接的实验发现：当给LLM代理提供冻结的GNN工具时，代理并不会进行独立判断，而是在97.6%-99.2%的情况下直接采纳GNN的输出，完全放弃自身的推理能力，沦为“GNN复读机”。更令人警惕的是，这种盲从行为并非弱模型的缺陷——随着骨干模型能力从1.5B提升到7B，代理对GNN的遵从度反而从0.60上升到0.98。同时，代理能力越强，其替代方案（如邻居标签工具）的表现越好，但代理却固执地坚守GNN，导致性能差距在高同质性图上加倍扩大（Oracle差距从0.09增长到0.22）。

核心问题在于：在LLM代理+GNN工具的系统中，代理是否真的起到了“判断者”的作用？论文提供的证据表明，即使最简单的选择性调用门控也只能恢复一半的高同质性性能差距，且无法实现全局收益，表明问题的根源在于可用信息的不足，而非路由设计。这提醒研究者：不能默认LLM代理能在工具调用中展现独立判断力，选择性调用必须被刻意设计，而非指望随模型规模自然涌现。

### Q2: 有哪些相关研究？

根据论文内容，相关研究可分为以下几类：

**方法类**：近期工作为LLM Agent提供图结构文本操作（如邻居查找、k跳检索）以提升性能。本文区别在于首次将冻结的图神经网络（GNN）作为显式工具暴露给Agent，而非仅提供文本接口。论文的对比基准“邻居标签查找”受这些图原生操作启发，但采用最小化设计。

**评测类**：有工作表明在非Agent场景下，LLM从结构编码中获益有限。本文关注不同问题——Agent在工具调用预算下是否会盲目服从结构工具（而非结构本身是否帮助LLM输入）。此外，并发工作研究了工具过信任现象，如工具-记忆冲突、工具使用税（增强推理反而加剧工具幻觉）。本文独特贡献在于：在Agent循环中暴露冻结的预测模型作为工具，测量预测层面的服从行为及其随骨干能力的缩放规律，填补了该领域的空白。

**应用类**：“GNN-as-Judge”虽同名，但实际是用GNN反馈过滤伪标签用于LLM微调（训练时协作），而非本文研究的推理时工具调用。另一方向学习何时从GNN侧调用LLM，本文研究镜像问题（Agent何时不应信任GNN），发现Agent无法自主实现选择性调用。

### Q3: 论文如何解决这个问题？

该论文通过设计GNN-as-tool实验框架来实证检验LLM智能体对图神经网络工具的依赖行为。核心方法是将预训练的GCN作为可调用工具，暴露给ReAct风格的LLM智能体（使用Qwen2.5系列0.5B-7B），并比较四种设置：A1（智能体+GNN工具）、A2（智能体+图导航工具，可访问邻居标签和度）、A3（独立GNN）、A4（仅文本的智能体）。

架构设计上，实验采用固定预算的ReAct循环（5000令牌+6次工具调用），在ogbn-arxiv文本属性图上按局部同质性分层测试。关键技术包括：（1）使用提示词鼓励工具调用，但专注测量智能体如何处理工具输出（采纳vs.权衡）；（2）通过一致性指标（A1与A3预测一致率）量化盲从程度，并分离选择性调用问题；（3）引入Oracle Gap（最佳动作选择器与A1的精度差）衡量盲从损失。

主要创新点：（1）发现LLM智能体在97.6-99.2%情况下盲从GNN输出，沦为"GNN鹦鹉"；（2）揭示更强的骨干网络（7B vs 1.5B）反而导致更高的一致性（0.98 vs 0.60）和更大损失（Oracle Gap 0.12-0.22）；（3）设计简易选择性调用门控可恢复一半高同质性差距，但信息瓶颈使得最优门控最多缩小1/3的Oracle差距。最终结论：评估agent+tool系统时不能假设智能体能对工具输出进行理性判断，选择性调用需要显式设计而非依赖规模涌现。

### Q4: 论文做了哪些实验？

论文在ogbn-arxiv（主实验）和WikiCS（复现）两个文本属性图数据集上进行了节点分类实验。实验设置中，将冻结的GNN作为ReAct风格LLM agent的可调用工具，测量agent是自主判断使用工具还是盲目服从。对比方法包括：A1（agent+GNN工具）、A2（邻居标签工具）、A3（原始GNN）、A4（无工具agent）以及per-node oracle（每个节点选择最佳动作的理想策略）。主要结果如下：1）鹦鹉效应：在7B模型上，A1与A3的预测一致性高达97.6%-99.2%，且agent仅调用一次工具就完全采纳其输出，完全绕过自身推理。2）能力越强服从越深：从1.5B到7B，agent与GNN的一致性从0.60升至0.98，更强能力带来更完全的服从。3）服从代价随能力增长：在7B高同质性区域，oracle比鹦鹉高0.22，且邻居标签工具（0.81）已超越GNN（0.71），但agent仍盲目服从。4）选择性调用门控：简单门控在高同质性区域恢复约一半差距（0.71→0.83），但全局无净收益（0.481→0.475）。基于标准不确定性指标的学习路由器仅能恢复oracle潜力空间的1/6至1/3，表明可靠的选择性调用受限于可用信息而非路由器设计。在WikiCS上复现了所有定性结论。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来研究方向：首先，研究仅在ogbn-arxiv和WikiCS两个节点分类任务上使用Qwen2.5系列和单一GCN工具，结论的泛化性需在其他架构（如GAT、GraphSAGE）及更大规模模型（>7B）上验证。其次，未探究盲从行为的底层机制（如GNN输出在上下文中的支配效应），未来可通过注意力权重分析或消融实验分离原因。改进思路包括：设计动态门控机制，利用工具输出的置信度或不确定性作为调节信号，而非固定阈值；或在训练中引入对抗性工具输出，迫使模型发展评判能力。跨家族实验显示Qwen的极端盲从具有模型特异性，启示研究者需关注基础模型训练数据分布（如代码/数学推理比例）对工具服从性的影响。最后，异配图上弱GNN可能放大盲从成本，可探索让LLM在调用工具前先进行图结构感知的预分析，或构建可学习的自适应路由策略，结合节点级同配性特征动态决策是否依赖工具。

### Q6: 总结一下论文的主要内容

该论文研究了LLM代理在使用图神经网络(GNN)工具时是否存在独立判断。通过将冻结的GNN作为工具提供给ReAct风格的LLM代理，并在文本属性图节点分类任务(ogbn-arxiv和WikiCS)上进行测试，发现代理并未行使判断权：其预测结果与原始GNN的吻合度高达97.6-99.2%，完全沦为GNN的"鹦鹉"，放弃了自身推理能力。更令人惊讶的是，随着骨干模型能力增强(Qwen2.5从1.5B到7B)，这种盲从程度反而上升(从0.60到0.98)，且代价不会缩小——在7B规模下，简单的邻居标签工具在高同质性场景中已超越GNN(0.81 vs 0.71)，但代理仍然选择盲从。虽然选择性调用门控能恢复约一半的性能差距，但整体效果有限。核心贡献在于警示：评估代理+工具系统时，不能默认代理会进行独立判断，选择性调用需要工程化设计而非期待从规模中涌现。
