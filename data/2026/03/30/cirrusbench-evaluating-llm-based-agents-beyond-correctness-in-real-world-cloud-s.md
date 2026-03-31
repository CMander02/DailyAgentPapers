---
title: "CirrusBench: Evaluating LLM-based Agents Beyond Correctness in Real-World Cloud Service Environments"
authors:
  - "Yi Yu"
  - "Guangquan Hu"
  - "Chenghuang Shen"
  - "Xingyan Liu"
  - "Jing Gu"
  - "Hangyi Sun"
  - "Junzhuo Ma"
  - "Weiting Liu"
  - "Jianfeng Liu"
  - "Mingyue Pu"
  - "Yu Wang"
  - "Zhengdong Xiao"
  - "Rui Xie"
  - "Longjiu Luo"
  - "Qianrong Wang"
  - "Gurong Cui"
  - "Honglin Qiao"
  - "Wenlian Lu"
date: "2026-03-30"
arxiv_id: "2603.28569"
arxiv_url: "https://arxiv.org/abs/2603.28569"
pdf_url: "https://arxiv.org/pdf/2603.28569v1"
categories:
  - "cs.LG"
  - "cs.AI"
  - "cs.IR"
  - "cs.PF"
tags:
  - "Agent评测基准"
  - "真实世界评估"
  - "云服务Agent"
  - "多轮对话"
  - "工具使用"
  - "效率指标"
  - "客户满意度"
relevance_score: 8.0
---

# CirrusBench: Evaluating LLM-based Agents Beyond Correctness in Real-World Cloud Service Environments

## 原始摘要

The increasing agentic capabilities of Large Language Models (LLMs) have enabled their deployment in real-world applications, such as cloud services, where customer-assistant interactions exhibit high technical complexity and long-horizon dependencies, making robustness and resolution efficiency critical for customer satisfaction. However, existing benchmarks for LLM-based agents largely rely on synthetic environments that fail to capture the diversity and unpredictability of authentic customer inputs, often ignoring the resolution efficiency essential for real-world deployment. To bridge this gap, we introduce CirrusBench, a novel evaluation framework distinguished by its foundation in real-world data from authentic cloud service tickets. CirrusBench preserves the intricate multi-turn logical chains and realistic tool dependencies inherent to technical service environments. Moving beyond execution correctness, we introduce novel Customer-Centric metrics to define agent success, quantifying service quality through metrics such as the Normalized Efficiency Index and Multi-Turn Latency to explicitly measure resolution efficiency. Experiments utilizing our framework reveal that while state-of-the-art models demonstrate strong reasoning capabilities, they frequently struggle in complex, realistic multi-turn tasks and fail to meet the high-efficiency standards required for customer service, highlighting critical directions for the future development of LLM-based agents in practical technical service applications. CirrusBench evaluation framework is released at: https://github.com/CirrusAI

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型（LLM）的智能体在真实世界应用（特别是云服务这类复杂技术场景）中评估体系不足的问题。研究背景是，随着LLM智能体能力的增强，它们正被部署到云服务等技术复杂、交互链条长、依赖工具使用的现实场景中，其**鲁棒性和解决效率**直接关系到客户满意度。然而，现有评估基准存在两大不足：首先，它们大多依赖**合成环境或角色扮演模拟**，无法捕捉真实客户交互的多样性、不可预测性和“噪音”，导致对智能体在实际场景中的性能高估；其次，现有评估主要关注任务完成的**正确性**（如成功率），而普遍忽视了对于服务质量至关重要的**解决效率**。在真实的云服务中，一个正确但过程冗长、低效的解决方案，从客户角度看仍然是失败的。

因此，本文要解决的核心问题是：**如何构建一个基于真实世界数据、能够全面评估LLM智能体（不仅包括正确性，更包括解决效率和服务质量）的评估框架**，以弥合学术基准与现实应用需求之间的差距。为此，论文提出了CirrusBench，一个基于真实云服务工单数据构建的新型评估框架，其核心创新在于引入了以客户为中心的全新度量标准（如标准化效率指数、多轮次延迟等），旨在量化智能体的响应速度和解决效率，从而更真实地反映其在复杂、长程技术对话中的实际服务能力。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及三大类别：LLM智能体基准评测、多轮交互中的工具使用评估，以及面向客户满意度的评价指标。

在**智能体基准与真实性**方面，现有工作如Webshop、WebArena和SWE-bench构建了静态或特定领域（如软件工程）的测试环境；AgentBench则尝试在多个不同环境中评估智能体的通用能力。然而，这些基准大多依赖模板或LLM角色扮演生成的合成数据，缺乏真实人类交互的噪声、多样性和不可预测性。ABCD数据集虽采用了专家实时聊天记录，但未包含技术支持中至关重要的复杂工具使用。本文提出的CirrusBench则直接基于真实云服务工单数据构建，天然融合了真实的多轮对话与复杂的工具集成，显著提升了评测环境的真实性。

在**多轮交互中的工具利用**方面，ToolBench、Metatool和τ-bench系列等工作系统评估了工具选择与参数化能力；ToolSandbox引入了能动态改变世界状态的有状态环境。近期研究虽尝试在对话语境中嵌入工具使用，但通常基于模拟交互构建。相比之下，CirrusBench专注于评估智能体在真实、长程客户支持对话中，如何应对自然出现的复杂工具依赖关系。

在**评价指标与客户满意度**方面，早期方法侧重于执行准确性和关键词匹配。随后，研究者开始采用基于LLM的评判器进行更细致的评估。在客户服务领域，近期工作已着手形式化客户满意度指标，而云服务基准评测的基础研究也长期强调效率与延迟是关键性能指标。本文在此基础上，通过引入标准化效率指数（NEI）和多轮延迟（MTL）等客观、具体的指标，将客户满意度操作化，首次构建了能直接衡量LLM智能体在真实技术支持场景中解决效率的评估框架。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为CirrusBench的新型评估框架来解决现有基准测试在真实云服务环境中评估LLM智能体时的不足。该框架的核心在于其**基于真实世界数据**的构建方法、**多轮任务评估**的架构设计，以及超越单纯正确性、引入**以客户为中心的效率指标**的创新评估体系。

**整体框架与数据构建**：CirrusBench的基石是来自真实云服务工单的历史对话数据。其构建过程包含四个核心阶段：数据收集、预处理、知识增强标注和质量保证。通过这一流程，将原始工单转化为结构化的评估任务集，共包含1500个无需工具调用的任务和425个需要工具调用的任务，覆盖20个不同的服务类别。这种方法确保了评估场景的**真实性、复杂性和多样性**，保留了真实服务交互中固有的多轮逻辑链条和工具依赖关系。

**主要模块与关键技术**：
1.  **数据预处理与增强模块**：采用了包括**去敏感化（PII擦除）**、**去噪与话语修剪**、**工具模拟（Tool Mock）**、**对话规范化**和**翻译**在内的关键技术。其中，“工具模拟”通过记录并回放真实工具调用及其结果，构建了标准化的模拟实例，使得评估无需连接真实后端API即可复现，解决了使用历史数据进行工具调用评估的关键挑战。
2.  **评估方法论模块**：框架采用**分层评估**策略。基础是**单轮子任务评估**，精细评估智能体在三个维度的表现：
    *   **工具使用能力**：分解为工具调用意识（TIA）、工具选择准确性（TSA）和工具执行有效性（TEV）三个递进指标。
    *   **问题解决能力**：核心指标是回复可解决性（RR），判断回复是否包含解决当前步骤问题所需的关键信息。
    *   **服务资格（效率）**：引入**单轮延迟（STL）**，以输出令牌数来衡量响应效率。
3.  **多轮任务动态评估机制**：这是框架的创新核心。评估不是静态比较，而是一个**动态过程**。系统会沿着真实解决方案的检查点序列推进，但在每个检查点，智能体可以自由生成响应。评估器会计算单轮指标，并判断响应是否“可接受”。如果失败，一个**流畅性检查器（Fluency Checker）** 会判断后续的用户查询在智能体偏离的响应下是否仍然逻辑有效，从而决定是开启新的评估会话还是终止整个多轮任务评估。这种设计允许智能体展示比参考答案更高效的解决路径。

**创新点**：
1.  **生态效度优先的数据集**：完全基于真实、成功的云服务工单构建，而非合成数据，确保了评估环境与真实业务场景的高度一致。
2.  **超越正确性的客户中心指标**：论文最大的创新在于提出了量化**解决效率**的指标，包括**任务推进率（TPR）**、**逻辑跳跃（LJ）** 和**归一化效率指数（NEI）**。NEI尤其关键，它通过计算智能体跳过的必要子任务比例，来量化其通过更少步骤解决问题的“捷径”能力。此外，**多轮延迟（MTL）** 则从整体上衡量完成一个任务的平均响应长度。这些指标共同将评估重点从“是否做对”扩展到“是否高效、令人满意地解决”。
3.  **支持高效路径发现的动态评估**：通过结合历史解决方案路径和流畅性检查，评估框架不仅能检测错误，还能识别和奖励那些能通过更优推理逻辑缩短解决流程的智能体行为，引导模型向更高效的问题解决方向发展。

总之，CirrusBench通过其真实数据基础、精细化的单轮能力诊断、以及创新的多轮动态效率评估体系，系统地解决了在复杂、长视野的真实云服务环境中全面评估LLM智能体性能（包括正确性与效率）的问题。

### Q4: 论文做了哪些实验？

实验在CirrusBench框架上进行，该框架基于真实的云服务工单数据构建，旨在评估LLM智能体在复杂、多轮次技术客服场景中的表现。

**实验设置与数据集**：实验使用了CirrusBench数据集，该数据集包含需要调用工具的任务和无需调用工具的任务。评估通过API调用多个系列的先进LLM模型进行，包括Qwen系列、GPT系列和DeepSeek系列。评估中采用DeepSeek-V3.2作为基础模型的自动评估器（辅以精心设计的提示词），其在包含141个人工标注的验证集上准确率达到91.49%，确保了评估的可靠性。

**评估指标与对比方法**：实验超越了传统的执行正确性，引入了以客户为中心的新颖指标来综合定义智能体成功。主要评估指标包括：平均任务推进率（ATPR）、平均逻辑跳跃（ALJ）、平均归一化效率指数（ANEI）、平均多轮延迟（AMTL）以及成功率（SR，包括pass@1和pass@2）。实验对比了不同模型（包括具有显式思考能力的模型与标准模型）在有无工具调用需求场景下的表现，并分析了输入长度、检查点数量、服务类别和回复类型等因素对性能的影响。

**主要结果与关键指标**：
1.  **工具使用是挑战**：几乎所有模型在需要工具调用的任务上各项指标表现均差于无需工具调用的任务。
2.  **思考能力的权衡**：显式思考能力并非总是带来收益。例如，在工具使用场景下，DeepSeek-R1（思考模型）的pass@1 SR仅为7.9%，低于其非思考版本DeepSeek-V3.2的9.6%。Qwen2.5-72B-Thinking在工具场景的SR（11.0%）也未超越标准指令版本（11.0%），且在非工具场景表现更差（13.3% vs. 19.0%）。思考模型通常伴随更高的延迟（AMTL），如GPT-5-0807-Global的AMTL高达1583.0/2234.4个令牌。
3.  **性能与延迟的权衡**：像GPT-4o-0806这样的标准模型保持了极低的延迟（188.6/250.8令牌），但其绝对成功率（pass@1 SR 6.8%/7.0%）相比更大、计算更密集的模型较低。表现最佳的GPT-5-0807-Global在工具/非工具场景的pass@1 SR分别达到16.7%和23.8%。
4.  **上下文长度的影响**：与“中间迷失”现象相反，在CirrusBench上，输入上下文长度与解决成功率呈正相关。在超过16000个令牌的范围内，GPT-5模型达到最佳性能（pass@1 SR 44.8%， pass@2 SR 64.8%）。
5.  **多轮交互的挑战**：任务所需的检查点数量与成功率呈明显负相关。检查点为1时pass@1 SR可达45.8%，而检查点≥5时骤降至5.3%，表明模型在维持长程逻辑一致性和状态跟踪方面存在困难。
6.  **服务类别与回复类型的差异**：不同服务类别的性能差异显著（如Website类别pass@1 SR为36.8%，而Email类别为18.9%）。模型最擅长生成“解决方案”类回复，而在“询问”类回复上表现最弱，表明其存在跳过关键信息收集、过早提出解决方案的系统性倾向。

### Q5: 有什么可以进一步探索的点？

基于论文结论，未来研究可深入探索以下几个方向。首先，需解决工具集成瓶颈，当前模型在纯对话与工具调用间性能差距显著，未来可设计更高效的工具学习与调用机制，例如通过分层决策或工具抽象来降低复杂度。其次，需优化“思考”模型的效率权衡，显式推理常带来过高延迟却未提升解决率，未来可研究轻量化推理模块或动态推理终止策略，在效率与效果间取得平衡。再者，需增强长程交互的鲁棒性，当前模型在多次交互中错误累积、逻辑一致性下降，且倾向于过早闭合问题，未来应探索记忆增强、状态跟踪及主动询问机制，以提升多轮对话的稳定性。此外，知识嵌入对云服务任务至关重要，未来可结合领域知识图谱进行预训练或检索增强，以提升准确性。最后，评估体系需持续拓展，除论文中的效率指标外，可纳入用户体验、个性化适应等维度，推动智能体向更人性化、高效实用的方向发展。

### Q6: 总结一下论文的主要内容

该论文提出了CirrusBench，一个基于真实云服务工单数据构建的评估框架，旨在解决现有基于LLM的智能体评测基准的不足。核心问题是现有基准多依赖合成环境，无法捕捉真实客户交互的多样性和不可预测性，且普遍忽视对实际部署至关重要的解决效率。

论文的方法是从大量真实的云服务工单中构建评估数据集，保留了多轮对话的复杂逻辑链和真实的工具依赖关系。其核心贡献在于超越了传统的执行正确性指标（如成功率），引入了一套以客户为中心的新评价指标，包括标准化效率指数（NEI）和多轮延迟（MTL）等，以量化解决效率和响应性，从而更全面地衡量服务质量和客户满意度。

主要结论指出，实验分析揭示了最先进的LLM与真实云服务需求之间存在显著差距。模型在复杂的多轮任务中表现脆弱，错误会累积，且存在过早结束对话的倾向。此外，工具集成是当前的关键瓶颈，而“思考”模型往往会带来过高的延迟却未成比例地提升问题解决能力。因此，未来基于LLM的智能体发展必须超越孤立的准确性指标，优先考虑解决效率、多轮对话的鲁棒性以及响应式信息收集策略。
