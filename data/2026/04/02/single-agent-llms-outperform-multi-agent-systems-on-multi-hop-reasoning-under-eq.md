---
title: "Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets"
authors:
  - "Dat Tran"
  - "Douwe Kiela"
date: "2026-04-02"
arxiv_id: "2604.02460"
arxiv_url: "https://arxiv.org/abs/2604.02460"
pdf_url: "https://arxiv.org/pdf/2604.02460v1"
categories:
  - "cs.CL"
  - "cs.MA"
tags:
  - "多智能体系统"
  - "单智能体系统"
  - "计算效率"
  - "推理效率"
  - "信息论分析"
  - "多跳推理"
  - "基准评测"
  - "实验验证"
relevance_score: 8.5
---

# Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets

## 原始摘要

Recent work reports strong performance from multi-agent LLM systems (MAS), but these gains are often confounded by increased test-time computation. When computation is normalized, single-agent systems (SAS) can match or outperform MAS, yet the theoretical basis and evaluation methodology behind this comparison remain unclear. We present an information-theoretic argument, grounded in the Data Processing Inequality, suggesting that under a fixed reasoning-token budget and with perfect context utilization, single-agent systems are more information-efficient. This perspective further predicts that multi-agent systems become competitive when a single agent's effective context utilization is degraded, or when more compute is expended. We test these predictions in a controlled empirical study across three model families (Qwen3, DeepSeek-R1-Distill-Llama, and Gemini 2.5), comparing SAS with multiple MAS architectures under matched budgets. We find that SAS consistently match or outperform MAS on multi-hop reasoning tasks when reasoning tokens are held constant. Beyond aggregate performance, we conduct a detailed diagnostic analysis of system behavior and evaluation methodology. We identify significant artifacts in API-based budget control (particularly in Gemini 2.5) and in standard benchmarks, both of which can inflate apparent gains from MAS. Overall, our results suggest that, for multi-hop reasoning tasks, many reported advantages of multi-agent systems are better explained by unaccounted computation and context effects rather than inherent architectural benefits, and highlight the importance of understanding and explicitly controlling the trade-offs between compute, context, and coordination in agentic systems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在澄清多智能体大语言模型系统（MAS）与单智能体系统（SAS）在性能比较中的根本问题。研究背景是，近期许多工作显示MAS在各类任务上表现强劲，但这些提升往往与测试时计算量的增加相混淆。现有方法的不足在于，大多数比较没有在相等的计算资源（特别是“思考令牌”预算）下进行，导致无法区分性能增益是源于MAS的架构优势，还是仅仅因为它消耗了更多计算资源。

本文要解决的核心问题是：在严格限定用于中间推理的令牌预算（即“思考令牌”）的前提下，对于多跳推理任务，单智能体系统是否能够比多智能体系统更有效？论文从信息论（数据处理不等式）的角度论证，在固定令牌预算且上下文利用完美的条件下，单智能体系统因其避免了智能体间通信带来的信息瓶颈而更具信息效率。同时，研究也旨在明确MAS在何种情况下会变得有竞争力（例如，当单智能体上下文利用效率下降，或MAS获得额外未计入的计算时），并探讨如何进行可靠、受控的比较评估。

为此，论文通过跨多个模型系列的对照实验，比较了在匹配思考令牌预算下SAS与多种MAS架构的性能，并进行了详细的诊断分析，揭示了评估方法中可能夸大MAS优势的潜在缺陷。

### Q2: 有哪些相关研究？

本文的相关工作主要围绕预算控制评估、多智能体系统（MAS）的效用条件、单智能体与多智能体系统比较、多智能体协作机制以及上下文利用等类别展开。

在**预算控制评估**方面，近期研究强调评估时应控制测试时计算量，否则比较会被混淆。本文与此方向一致，但区别在于：本文仅将“思考令牌”作为受控资源，并专注于比较单智能体（SAS）与多智能体（MAS）架构，而非单一架构内的预算分配。

关于**MAS何时及为何有效**，并发研究指出MAS的增益取决于具体场景和实现。有研究认为MAS的明显优势常源于更多计算；另有研究表明，一旦计算归一化，智能体优势往往集中在较弱模型或困难任务中，并随基础模型能力增强而减弱甚至逆转，突显了协调开销的制约。还有工作通过多智能体追踪和故障分类，解释了编排如何导致信息漂移、损失或由评估伪影带来的虚假提升。这些发现与本文观察到的过度探索、聚合错误和不透明的API计量等问题相符。此外，有研究强调改进依赖于任务结构和验证协议，而非MAS普遍优越。这些成果共同促成了本文的核心设计：严格控制思考令牌预算、诊断协调与通信如何影响准确性，并界定MAS或混合设计具有竞争力的具体场景（如上下文利用退化时）。

在**SAS与MAS比较**方面，经验证据表明，随着前沿模型进步，编排的收益递减，SAS可匹配或超越MAS。例如在教育分析中，采用少量示例提示的SAS在反思评估上优于MAS；协作智能体基准也揭示MAS优势是任务特定的。本文在更严格的计算控制下补充了这些发现。

关于**多智能体协作机制**，先前研究提出了多种结构化协作方式（如辩论、角色专精、集成/自洽、反思）。本文并未将MAS视为单一设计，而是在统一预算匹配框架下评估了几种代表性机制，从而区分架构本身带来的增益与单纯增加计算带来的增益。

最后，在**上下文长度与利用**方面，研究表明现代LLM无法完美利用长上下文，存在注意力稀释、噪声敏感、上下文混淆和位置偏差等问题，导致推理退化。本文通过显式建模有效上下文退化，并将此与SAS-versus-MAS问题关联，测试了当单智能体上下文利用恶化时，结构化多智能体流程何时变得具有竞争力。

### Q3: 论文如何解决这个问题？

论文通过理论分析与实证研究相结合的方式，系统性地探讨了在固定思考令牌预算下，单智能体系统（SAS）与多智能体系统（MAS）在多跳推理任务上的性能比较问题。其核心解决思路是：首先基于信息论提出理论框架，论证在理想条件下SAS的信息效率优势；随后设计严格控制变量的实验进行验证，并深入分析评估过程中可能存在的偏差。

在理论部分，论文基于数据处理不等式（DPI）构建了形式化论证。将正确答案记为 \(Y\)，单智能体可访问的完整上下文（包括先验推理和中间状态）记为 \(C\)，而多智能体系统中传递的消息或摘要记为 \(M = g(C)\)。由于 \(M\) 是 \(C\) 的函数，形成马尔可夫链 \(Y \leftrightarrow C \leftrightarrow M\)。根据DPI，有 \(I(Y;C) \ge I(Y;M)\)，即单智能体系统与正确答案的互信息不低于多智能体系统。结合法诺不等式，这从理论上保证了在完美利用上下文且预算固定的情况下，SAS的误差概率下限不高于MAS。然而，论文进一步指出，实际LLM可能无法同等有效地利用所有上下文信息。因此引入有效上下文退化模型 \(\tilde{C}_{\alpha} = T_{\alpha}(C)\)，其中 \(\alpha\) 表示退化程度。理论预测，当单智能体的有效上下文利用率降低到一定程度时，设计良好的MAS可能通过其结构化的信息处理流程（如分解、过滤、验证）更可靠地恢复任务相关信息，从而变得有竞争力。

在实证方法部分，论文在FRAMES和MuSiQue（仅使用4跳问题）两个多跳知识问答数据集上进行了严格对比。核心是确保SAS与各种MAS架构在完全相同的全局思考令牌预算 \(B\) 下运行。

**整体框架与主要模块：**
1.  **单智能体系统（SAS）**：采用单一、直接的推理过程。模型接收包含“逐步思考然后回答”指令的系统提示，并在一次调用中被分配全部预算 \(B\) 进行内部推理，最后提取答案。
2.  **单智能体长思考变体（SAS-L）**：针对某些模型（如Gemini）在单次调用中产生的可见思考文本可能低于请求预算的现象，SAS-L在保持相同预算和单次调用的前提下，通过在用户消息中添加一个简短的结构化预回答分析支架（如要求模型识别歧义、提出解释、评估并选择），鼓励模型产生更长的内部推理。
3.  **多智能体系统（MAS）**：设计了五种架构，均在相同总预算 \(B\) 下运行，并尽量保持规划器和聚合器的预算中性。
    *   **顺序式（Sequential）**：作为与SAS对比的主要基线。规划器将问题分解为有序步骤，预算平均分配给顺序执行的多个工作器，聚合器综合中间输出。其本质是将SAS的潜在连续推理轨迹外部化为步骤间传递的显式消息。
    *   **子任务并行式（Subtask-parallel）**：规划器提出近似独立的子任务集，工作器并行解决（预算均分），聚合器合并结果。
    *   **并行角色式（Parallel-roles）**：将问题同时发送给具有不同角色（如求解器、事实提取器、怀疑者、第二求解器）的专门工作器，预算均分，聚合器综合输出。
    *   **辩论式（Debate）**：两个辩论者独立回答并相互批评，预算均分，聚合器根据候选答案和批评给出最终答案。
    *   **集成式（Ensemble）**：多个工作器在较高采样温度下独立回答（预算均分），由一个评判者选择最佳候选答案。

**关键技术：**
*   **严格的预算控制**：所有对比均在匹配的思考令牌预算下进行，这是比较公平性的基石。
*   **LLM即评判员评估**：使用一个独立的评估模型，根据固定的自然语言评分标准（检查真实答案是否出现或语义存在）对所有系统的输出进行评分，确保评估一致性。
*   **详细的诊断分析**：不仅比较聚合性能，还深入分析了系统行为（如Gemini API的预算控制伪影）和基准测试本身可能存在的偏差，这些因素可能夸大MAS的表面收益。

**创新点：**
1.  **理论创新**：首次从信息论（DPI）角度形式化地论证了在固定推理预算和完美上下文利用下，SAS相对于MAS的信息效率优势，并提出了一个解释MAS何时可能具有竞争力的有效上下文退化模型。
2.  **方法创新**：设计了在严格等预算条件下对比SAS与多种MAS架构的实证框架，并引入了SAS-L变体以控制某些模型特有的输出长度差异。
3.  **洞察创新**：通过大量实验发现，在思考令牌恒定的情况下，SAS在多跳推理任务上始终匹配或优于MAS。研究指出，许多文献中报道的MAS优势可能源于未计入的计算量增加和上下文效应，而非其架构固有的益处，强调了在智能体系统中理解并显式权衡计算、上下文和协调的重要性。

### Q4: 论文做了哪些实验？

论文在三个模型系列（Qwen3、DeepSeek-R1-Distill-Llama和Gemini 2.5）上进行了对照实验，比较单智能体系统（SAS）与多种多智能体系统架构（MAS）在匹配的“思考令牌”预算下的性能。实验设置严格控制计算量，确保SAS与MAS消耗的推理令牌总数相等。使用的数据集是多跳推理基准测试，主要包括FRAMES和MuSiQue 4-hop。对比方法包括标准的SAS、SAS-L（一种变体）以及多种MAS架构，如Sequential（顺序式）、Debate（辩论式）、Parallel-roles（并行角色）和Ensemble（集成式）。

主要结果显示，在匹配的思考令牌预算下（除极低的100令牌预算外，该预算下模型无法产生有效推理），SAS在多跳推理任务上始终匹配或优于MAS。具体数据指标上，在MuSiQue 4-hop任务中，SAS通常达到最高准确率或与最佳MAS统计上无差异；例如，在Gemini-2.5-Pro上，SAS-L在较高令牌预算下表现更强。MAS中，Debate是最稳定的变体，而Ensemble在高预算下（如5000和10000令牌）在FRAMES任务中可能表现最佳。实验还发现，性能随令牌预算增加而提升，但在1000/2000令牌后收益递减，模型趋于饱和。此外，通过上下文降解实验（如随机删除、掩码、替换令牌或添加干扰句）发现，当单智能体上下文有效利用率下降时（如替换降解α=0.7），MAS（如Sequential）变得更具竞争力，这验证了理论预测。论文还指出，API预算控制和基准测试中的伪影可能夸大MAS的增益，强调在评估时需明确控制计算、上下文和协调之间的权衡。

### Q5: 有什么可以进一步探索的点？

该论文指出在固定推理token预算下，单智能体系统（SAS）通常优于多智能体系统（MAS），但其结论本身也揭示了若干值得深入探索的方向。首先，研究仅在多跳推理任务上验证，未来可扩展到规划、创作、工具调用等更复杂的任务场景，以检验结论的普适性。其次，论文发现当单智能体上下文利用率下降时，MAS会变得有竞争力，这提示未来可系统研究上下文退化（如信息过载、干扰噪声）的阈值条件与缓解机制。此外，实验依赖API进行预算控制，存在潜在偏差，未来需设计更精细的底层推理过程监控方法。从改进思路看，可探索混合架构——例如在任务不同阶段动态切换单/多智能体模式，或设计轻量级协调机制来降低MAS的通信开销。最后，当前评估集中于最终答案准确性，未来应引入效率、鲁棒性、可解释性等多维度指标，以全面衡量智能体系统的实际效用。

### Q6: 总结一下论文的主要内容

本文针对多智能体系统（MAS）在推理任务中表现优于单智能体系统（SAS）的常见结论提出质疑，指出以往比较往往忽略了计算量的不对等。论文的核心贡献在于，在严格控制“思考令牌”预算的条件下，系统比较了SAS与多种MAS架构的性能。研究基于信息论的数据处理不等式论证，在固定令牌预算且上下文利用完美时，单智能体系统理论上信息效率更高；只有当单智能体上下文利用受损或计算量增加时，多智能体系统才具有竞争力。

方法上，作者在三个模型系列和两个多跳推理数据集上进行了受控实验，比较了SAS与五种MAS架构在等量推理令牌下的表现。主要结论表明，当计算量归一化后，SAS在多跳推理任务上一致达到或超越MAS的性能。此外，诊断分析揭示了API预算控制中的伪影以及基准测试本身的问题，这些都可能夸大MAS的表面优势。因此，论文认为许多已报道的MAS优势实际上源于未被计入的计算量差异和上下文效应，而非其架构的固有优势，并强调了在智能体系统设计中明确权衡计算、上下文与协调的重要性。
