---
title: "VehicleMemBench: An Executable Benchmark for Multi-User Long-Term Memory in In-Vehicle Agents"
authors:
  - "Yuhao Chen"
  - "Yi Xu"
  - "Xinyun Ding"
  - "Xiang Fang"
  - "Shuochen Liu"
  - "Luxi Lin"
  - "Qingyu Zhang"
  - "Ya Li"
  - "Quan Liu"
  - "Tong Xu"
date: "2026-03-25"
arxiv_id: "2603.23840"
arxiv_url: "https://arxiv.org/abs/2603.23840"
pdf_url: "https://arxiv.org/pdf/2603.23840v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent Benchmark"
  - "Long-Term Memory"
  - "Multi-User Interaction"
  - "Tool Use"
  - "In-Vehicle Agent"
  - "Simulation Environment"
  - "Memory Evolution"
  - "Preference Modeling"
relevance_score: 7.5
---

# VehicleMemBench: An Executable Benchmark for Multi-User Long-Term Memory in In-Vehicle Agents

## 原始摘要

With the growing demand for intelligent in-vehicle experiences, vehicle-based agents are evolving from simple assistants to long-term companions. This evolution requires agents to continuously model multi-user preferences and make reliable decisions in the face of inter-user preference conflicts and changing habits over time. However, existing benchmarks are largely limited to single-user, static question-answer settings, failing to capture the temporal evolution of preferences and the multi-user, tool-interactive nature of real vehicle environments. To address this gap, we introduce VehicleMemBench, a multi-user long-context memory benchmark built on an executable in-vehicle simulation environment. The benchmark evaluates tool use and memory by comparing the post-action environment state with a predefined target state, enabling objective and reproducible evaluation without LLM-based or human scoring. VehicleMemBench includes 23 tool modules, and each sample contains over 80 historical memory events. Experiments show that powerful models perform well on direct instruction tasks but struggle in scenarios involving memory evolution, particularly when user preferences change dynamically. Even advanced memory systems struggle to handle domain-specific memory requirements in this environment. These findings highlight the need for more robust and specialized memory management mechanisms to support long-term adaptive decision-making in real-world in-vehicle systems. To facilitate future research, we release the data and code.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决车载智能体在真实、动态的多用户环境中，如何进行有效的长期记忆建模和决策评估的基准缺失问题。随着大语言模型的发展，车载智能体正从简单助手演变为需长期陪伴的“伴侣”，其核心任务是在车辆这一特定场景中，通过工具操作来服务用户，并持续学习、适应多用户（如驾驶员和乘客）的偏好。然而，现有评估基准存在明显不足：专注于记忆的基准大多局限于单用户、静态的问答形式，无法捕捉偏好随时间演变的动态性；而工具使用基准则侧重于短期的指令跟随，缺乏对长期、演化中用户偏好的考量。这种差距导致现有方法难以真实评估智能体在面临用户间偏好冲突、习惯随时间变化等复杂情况下的可靠决策能力。

因此，本文的核心问题是：如何构建一个可执行的、能客观评估车载智能体在多用户长期记忆场景下综合性能的基准。具体而言，该基准需要模拟真实车载环境的多用户交互历史（包含偏好冲突与演化），整合可执行的车载工具接口，并以达成最终正确系统状态（而非依赖LLM或人工评分）作为客观评价标准，从而推动更鲁棒、专用于车载系统的记忆管理机制的研究与发展。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：工具使用与交互环境评测、长期记忆评测，以及个性化与偏好建模。

在**工具使用与交互环境评测**方面，早期研究关注静态API调用的正确性。后续工作引入了可执行反馈和闭环决策，强调在交互环境中进行多步感知与行动，如VehicleWorld构建了具状态反馈的车载环境，GAIA关注开放领域的多步问题解决。然而，这些基准主要聚焦任务完成，对跨时域用户建模和偏好演化关注有限。

在**长期记忆评测**方面，早期工作通过长上下文理解评估信息保留能力，如LongBench和L-Eval。近期研究开始强调跨会话信息整合与长期记忆保持，评估会话间的一致性与追踪能力，PerLTQA进一步纳入个性化与偏好驱动的记忆使用。但这些基准多为离线或非可执行设置，难以评估记忆对实际决策和环境状态的影响。

在**个性化与偏好建模**方面，研究认识到长期数字陪伴需基于持续交互形成的用户偏好，但现有工作较少在可执行环境中联合考虑多用户场景与动态变化的偏好。

**本文与这些工作的关系和区别在于**：VehicleMemBench整合了上述方向，构建了一个**可执行、多用户、长周期交互**的车载模拟基准。它区别于现有工具评测基准，专注于**偏好演化建模**；区别于静态记忆评测，通过**执行后环境状态与目标状态的比对**来客观评估记忆对决策的实际影响；并首次在可执行环境中系统性地考察**多用户偏好冲突与动态变化**这一现实挑战。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为VehicleMemBench的可执行基准测试来解决多用户长时记忆评估问题。其核心方法是一个多阶段的流水线框架，将用户画像转化为时序演化的交互历史与可执行的评估目标，并集成到一个模拟车载环境中进行状态驱动的客观评估。

整体框架包含五个主要阶段：首先，从高质量数据集中生成包含丰富属性和偏好描述的多用户画像组，确保人物多样性和交互一致性。其次，为每个用户组构建事件链，作为历史记忆的基本单元，覆盖偏好冲突、指代消解、条件约束、状态转移和错误修正等五种动态类型，以模拟偏好的时序演化。第三，采用时间交错策略，将不同事件链中的事件按统一时间线合并排序，以反映真实场景中多偏好线程的并发演进。第四，基于时序事件序列生成对话历史，利用大语言模型将结构化事件转化为乘员与车载系统的自然交互，确保对话反映历史上下文和用户偏好的动态更新。第五，针对与车载功能相关的事件链生成查询和答案，通过大语言模型生成可执行的参考工具调用，并在模拟环境中验证，形成每个测试实例的自然语言查询和已验证的目标状态。

关键技术方面，论文构建了一个基于VehicleWorld的可执行模拟环境，重组了车载交互框架，覆盖23类车载设备，封装了111个可执行工具，每个设备都有结构化状态表示、可执行动作和参数约束，使智能体工具调用能产生明确的环境状态转移。同时，引入统一的内存API支持集成各类定制和通用内存系统，提供标准化函数调用规范。评估协议结合了离线记忆摄取和在线交互执行：内存系统先摄取时序对话历史构建长时记忆表示；评估时，智能体接收新查询和初始环境状态，通过调用车载工具和内存检索操作与环境迭代交互，直至终止产生预测状态；最终通过执行参考工具序列得到目标状态，与预测状态进行比较（采用模糊匹配或精确匹配），实现无需人工或大语言模型评分的客观、可重复评估。

创新点主要体现在：1）首次构建了面向多用户、长上下文、可执行的车载记忆基准，突破了现有基准单用户、静态设置的局限；2）通过事件链设计和时间交错策略，真实建模了偏好冲突和动态演化等复杂记忆挑战；3）采用状态比对而非主观评分，实现了记忆检索与工具执行的联合客观评估；4）提供了统一的模拟环境和内存API，支持系统化、可扩展的评估与未来研究。

### Q4: 论文做了哪些实验？

论文在自建的VehicleMemBench基准上进行了系统实验。实验设置方面，评估了七类具备工具调用能力的主流大模型（包括Gemini-3-Pro-Preview、GPT-5、Doubao-Seed-1.6、MiniMax、GLM、Kimi和Qwen家族）以及五种代表性记忆系统（如MemOS、Mem0、LightMem等），并以Gemini-3-Pro-Preview和Qwen3-Max为骨干模型进行记忆增强测试。评估采用基于状态转移的客观指标，包括精确状态匹配（ESM）、字段级与值级的精确率/召回率/F1分数（F-F1, V-F1），以及效率指标（平均工具调用次数Calls和平均记忆检索令牌数MemToken）。实验围绕三个核心能力维度展开：整体任务性能、纯工具使用能力（提供Gold Memory）和记忆能力（对比自主记忆与Gold Memory）。

主要结果发现：1）在提供Gold Memory时，模型纯工具能力差异显著，最佳模型Gemini-3-Pro-Preview的ESM达90.60，而GLM-4.7-Flash仅为55.40，差距超35点。2）一旦需要自主记忆检索（如Recursive Summarization设置），所有模型性能大幅下降，Gemini-3-Pro-Preview的ESM从90.60降至64.80，表明记忆构建与检索是主要误差源。3）自主记忆下字段级与值级F1差距扩大（最高近10点），说明记忆常仅保留粗粒度偏好。4）现有通用记忆系统在车载场景下表现不佳，甚至不如简单的领域定制基线（如Recursive Summarization），其中条件约束（Conditional Constraint）是最难类别，而偏好冲突（Preference Conflict）相对容易。5）记忆错误是主要失败模式，占总错误的63.9%。效率方面，Supermemory虽准确但检索成本高（MemToken达960.79），而Key Value Store高效但准确性低，现有系统难以兼顾精度与效率。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在评估模型范围有限，仅测试了代表性模型而未覆盖全部方法，且场景复杂度有待提升，未来可设计更长交互周期的任务。未来研究方向可从三方面展开：一是扩展评估体系，纳入更多样化的模型和记忆机制进行横向对比；二是增强环境动态性，引入更复杂的用户习惯变迁模式和突发冲突场景，以考验记忆系统的鲁棒性；三是探索专业化记忆架构，可结合车辆场景的时空特性设计记忆压缩、偏好融合等机制，提升对多用户长期偏好演化的建模能力。此外，可考虑将基准与真实车载数据结合，进一步验证其在现实系统中的适应性。

### Q6: 总结一下论文的主要内容

该论文针对车载智能体从短期助手向长期伴侣演进的需求，提出了一个名为VehicleMemBench的可执行基准测试，旨在评估多用户长期记忆能力。核心问题是现有基准多为单用户、静态问答设置，无法捕捉真实车载环境中偏好随时间演变、多用户交互及工具使用的复杂性。

论文的主要贡献是构建了一个基于可执行车载模拟环境的基准，包含23个工具模块，每个测试样本涵盖超过80个历史记忆事件。该方法通过比较智能体执行操作后的环境状态与预设目标状态进行评估，无需依赖LLM或人工评分，实现了客观可复现的评估。实验发现，尽管强大模型在直接指令任务上表现良好，但在涉及记忆动态演化（特别是用户偏好随时间变化）的场景中表现不佳，现有通用记忆系统难以满足特定领域的记忆管理需求。

研究结论指出，记忆能力是现实世界智能体应用的主要瓶颈，凸显了开发更鲁棒、专业化记忆管理机制的必要性，以支持车载系统中长期自适应决策。论文开源了数据与代码以促进后续研究。
