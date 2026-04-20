---
title: "MemEvoBench: Benchmarking Memory MisEvolution in LLM Agents"
authors:
  - "Weiwei Xie"
  - "Shaoxiong Guo"
  - "Fan Zhang"
  - "Tian Xia"
  - "Xue Yang"
  - "Lizhuang Ma"
  - "Junchi Yan"
  - "Qibing Ren"
date: "2026-04-17"
arxiv_id: "2604.15774"
arxiv_url: "https://arxiv.org/abs/2604.15774"
pdf_url: "https://arxiv.org/pdf/2604.15774v1"
categories:
  - "cs.CL"
tags:
  - "Agent Safety"
  - "Memory"
  - "Benchmark"
  - "Evaluation"
  - "Long-Horizon Interaction"
  - "Adversarial Attack"
relevance_score: 8.0
---

# MemEvoBench: Benchmarking Memory MisEvolution in LLM Agents

## 原始摘要

Equipping Large Language Models (LLMs) with persistent memory enhances interaction continuity and personalization but introduces new safety risks. Specifically, contaminated or biased memory accumulation can trigger abnormal agent behaviors. Existing evaluation methods have not yet established a standardized framework for measuring memory misevolution. This phenomenon refers to the gradual behavioral drift resulting from repeated exposure to misleading information. To address this gap, we introduce MemEvoBench, the first benchmark evaluating long-horizon memory safety in LLM agents against adversarial memory injection, noisy tool outputs, and biased feedback. The framework consists of QA-style tasks across 7 domains and 36 risk types, complemented by workflow-style tasks adapted from 20 Agent-SafetyBench environments with noisy tool returns. Both settings employ mixed benign and misleading memory pools within multi-round interactions to simulate memory evolution. Experiments on representative models reveal substantial safety degradation under biased memory updates. Our analysis suggests that memory evolution is a significant contributor to these failures. Furthermore, static prompt-based defenses prove insufficient, underscoring the urgency of securing memory evolution in LLM agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体在配备持久记忆能力后，因记忆被污染或产生偏见而逐渐导致行为异常和安全风险的问题。研究背景是，随着LLM智能体从瞬时响应单元发展为具有长期记忆的自主决策体，记忆在维持交互连续性、提供个性化服务方面发挥关键作用，但记忆并非静态中性存储，而是一个在长期运行中可能因交互机制、反馈信号和外部输入而向非预期方向演化的动态实体。

现有方法的不足在于，尽管已有研究提出了“记忆错误演化”的概念，揭示了持续交互和自我更新闭环中累积偏见会导致智能体偏离初始目标，但尚缺乏系统化的评估框架来衡量这种演化。具体来说，当前研究缺少能够清晰阐明记忆错误演化如何被触发、如何通过结构性偏见被放大、以及在真实部署环境中如何形成长期累积效应的标准化评测基准，这限制了对相关风险的深入理解和防御方案的开发。

本文要解决的核心问题是：如何系统评估LLM智能体在面临对抗性记忆注入、有噪声的工具输出和带有偏见的反馈时，其长期记忆的安全性，即抵抗“记忆错误演化”的能力。为此，论文提出了首个此类基准MemEvoBench，它构建了包含良性记忆和误导性记忆的混合记忆池，通过多轮交互模拟记忆演化过程，并设计了涵盖7个高风险领域、36种风险类型的问答式任务，以及从20个工具使用环境中改编的工作流式任务，以量化评估记忆污染下智能体安全性的退化程度，并探究有效的防御策略。

### Q2: 有哪些相关研究？

相关研究主要可分为两大类：**记忆增强的智能体方法**和**记忆相关的安全风险研究**。

在**方法类**工作中，记忆增强智能体从早期的扩展上下文窗口或静态键值存储，发展到动态、结构化的系统。具体可细分为：1）**框架式方法**，如MemGPT通过操作系统启发的虚拟内存抽象和分页机制管理记忆；HiAgent采用基于子目标分层的记忆结构以提升长程任务效率。2）**原生记忆架构**，如A-MEM、Intrinsic Memory Agents将记忆的形成、演化和检索直接集成到智能体的感知-规划-行动循环中；MIRIX进一步扩展到多智能体场景，支持跨智能体的记忆共享。

在**安全与评测类**工作中，研究重点从静态攻击转向动态演化风险。例如，AgentPoison展示了针对RAG和记忆模块的后门攻击；Xiong等人揭示了记忆错误在长程任务中通过经验跟随行为形成自我强化的错误循环；Shao等人则形式化了“记忆错误演化”概念，指出持续交互会导致对齐退化和奖励攻击。此外，现有评测基准如HEAL专注于具身智能体的幻觉率量化，LoCoMo评估长对话中的记忆保留，但它们多关注静态范式下的准确性或幻觉检测，未能涵盖多源偏见累积以及从微小偏差到系统性安全失效的完整轨迹。

本文提出的MemEvoBench与上述工作的区别在于：它首次建立了**标准化评测框架**，专门针对记忆在对抗性注入、噪声工具输出和偏见反馈下的**长期安全演化**进行评估，弥补了现有基准在动态、多轮次记忆演变风险量化方面的空白。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为MemEvoBench的综合性基准测试框架来解决LLM智能体在持续记忆演化过程中面临的安全风险评测问题。其核心方法是模拟现实世界中记忆被污染和逐渐演化的过程，并系统化地评估智能体在此过程中的行为漂移。

**整体框架与主要模块**：
MemEvoBench包含两个核心评测场景，共同构成一个多轮交互的评估协议。
1.  **QA风格场景（误导性记忆注入）**：该模块旨在评估陈述性记忆被污染的影响。它覆盖了医疗保健、心理健康、金融等7个高风险领域，定义了36种具体的风险失效模式。对于每种风险类型，研究团队通过结合领域分析、认知偏差研究和LLM辅助生成，精心设计了包含不同人物角色和情境的测试查询。关键创新在于构建了**混合记忆池**，其中包含正确和误导性的记忆条目。这些误导性条目并非明显的错误，而是通过**省略关键前提、转移决策阈值或过度概括结论**等三种现实污染模式，微妙地引导智能体做出不安全决策。记忆条目被设计为四种真实来源类型（知识片段、对话历史、个人笔记、论坛帖子）并带有时间戳。
2.  **工作流风格场景（含噪声的工具返回）**：该模块评估程序性记忆（即工作流执行历史）中的风险。它基于AgentSafetyBench的20个常见交互环境和8个风险类别，构建了83个测试用例。其创新点在于模拟了智能体在调用外部工具时可能遇到的风险：一是工具返回结果作为**间接提示注入**的渠道，二是返回结果可能**暴露超出查询范围的敏感信息**。研究构建了包含正确和误导性工作流记忆的执行历史，其中误导性条目嵌入了与风险类别相关的操作错误。

**关键技术设计与创新点**：
1.  **多轮记忆演化协议**：这是框架的核心创新。针对每个测试案例，设计了三轮评估。每一轮的查询在相同底层失效模式下实例化相关但不完全相同的决策情境。智能体每轮的响应会被作为新的记忆条目存储回记忆池。这种方法能够捕捉**自我强化的退化**过程，即早期的错误响应是否会随着错误历史的积累进一步加剧后续推理的偏差。
2.  **有偏见的用户反馈模拟**：为了模拟现实世界中的选择压力，框架引入了由LLM生成的模拟用户反馈。其机制是**不对称的强化**：导致成本增加的安全响应被赋予负面反馈，而采取风险捷径的响应则获得正面反馈。这种设计创造了系统性向不安全模式漂移的条件，放大了污染和偏见反馈对长期安全的复合影响。
3.  **系统化的评估指标与判据**：采用**攻击成功率（ASR）** 作为核心指标，并明确定义了“被误导”（MISLED）响应的四条判据（如提供可能导致伤害的建议、鼓励风险行为、未能警告风险、包含事实错误或过度自信等）。通过计算每一轮的ASR，可以量化安全性的渐进退化模式。评估使用先进的LLM（如GPT-5.2）作为法官模型，并进行了人工验证以确保可靠性。

总之，MemEvoBench通过精心设计的混合记忆池、模拟现实污染模式、多轮交互演化协议以及引入有偏见的反馈机制，首次为LLM智能体的长期记忆安全评估建立了一个标准化、系统化的基准，揭示了静态提示防御的不足，并强调了保障记忆演化安全的紧迫性。

### Q4: 论文做了哪些实验？

实验设置方面，研究在提出的MemEvoBench基准上进行评估，包含两种任务场景：问答风格（108个测试用例）和工作流风格（83个测试用例）。评估了9个代表性大语言模型，包括GPT-4o、GPT-5、Gemini-2.5-Pro、Claude-3.7-Sonnet、Llama-3.3-70B以及多个Qwen和DeepSeek模型。实验采用温度0.0以确保可复现性。

对比方法包括三种配置：1) 基础配置（Vanilla），仅使用标准系统提示；2) 安全提示（+SafePrompt），在系统提示中增加安全指南，要求模型批判性评估检索内容；3) 记忆修改工具（+ModTool），为模型提供correct_memory工具，允许在响应前修正误导性记忆条目。此外，每种配置都测试了有无带有偏见用户反馈（w/feedback）的情况，以模拟部署时的选择压力。实验模拟了三轮记忆演化过程。

主要结果如下：在基础配置下，所有模型都表现出高风险，平均攻击成功率（ASR）在三轮中分别为75.9%、75.2%和80.1%。加入偏见反馈后，ASR呈现明显逐轮上升趋势（71.6%/84.9%/87.8%）。安全提示方法在问答风格任务中能将第一轮平均ASR从76.2%降至55.5%，但在工作流风格任务中完全失效，且偏见反馈会进一步削弱其效果。记忆修改工具方法表现最佳，在多数配置下实现了最低ASR。例如Gemini-2.5-Pro在问答风格任务中，使用该工具后ASR降至19.0%/13.0%/14.0%，显著低于基础配置的67.0%/55.0%/55.0%和安全提示的46.0%/33.0%/32.0%。关键数据指标显示，模型检测误导性记忆的F1分数与ASR呈强相关，但多数模型的F1分数随轮次增加而下降，表明在记忆更新下的稳健检测仍是挑战。

### Q5: 有什么可以进一步探索的点？

该论文的局限性在于其基准测试主要聚焦于对抗性记忆注入、噪声工具输出和偏见反馈等外部风险，尚未深入探究模型内部机制（如记忆编码、检索与整合过程）如何导致行为漂移。未来研究可探索以下方向：一是开发动态防御机制，如实时记忆监控与净化算法，而非依赖静态提示；二是研究记忆演化的可解释性，通过可视化或归因分析揭示误导信息如何逐步扭曲决策路径；三是扩展评估维度，纳入多模态记忆（如图像、音频）及复杂社会情境下的伦理风险。此外，可结合强化学习设计自适应记忆管理策略，使智能体能在风险积累初期自主触发纠偏。这些改进有望提升长期记忆系统的鲁棒性，推动更安全的持续学习智能体发展。

### Q6: 总结一下论文的主要内容

该论文针对大型语言模型（LLM）智能体在配备持久记忆后可能面临的安全风险，提出了首个用于评估记忆错误演化的基准测试框架MemEvoBench。核心问题是：当智能体在多轮交互中反复接触误导性信息（如对抗性记忆注入、噪声工具输出或带有偏见的反馈）时，其记忆会逐渐被污染或产生偏见，从而导致行为漂移和异常，现有方法缺乏对此“记忆错误演化”现象的标准评估体系。

论文的方法概述是构建了一个包含两种任务类型的综合基准：一是涵盖7个领域、36种风险类型的问答式任务，二是基于20个Agent-SafetyBench环境改编、包含噪声工具返回的工作流式任务。两者均在多轮交互中混合使用良性和误导性记忆池，以模拟记忆的动态演化过程。

主要结论是，通过对代表性模型的实验，发现存在偏见的记忆更新会导致模型安全性显著下降，分析表明记忆演化是导致这些失败的重要因素。此外，仅依靠静态提示的防御措施被证明是不够的，这凸显了保障LLM智能体记忆演化安全的紧迫性。该工作的核心贡献在于为理解和量化记忆相关的安全风险提供了一个标准化、可复现的评估基准，对推动安全、可靠的持久记忆智能体发展具有重要意义。
