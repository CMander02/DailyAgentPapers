---
title: "CodeHacker: Automated Test Case Generation for Detecting Vulnerabilities in Competitive Programming Solutions"
authors:
  - "Jingwei Shi"
  - "Xinxiang Yin"
  - "Jing Huang"
  - "Jinman Zhao"
  - "Shengyu Tao"
date: "2026-02-23"
arxiv_id: "2602.20213"
arxiv_url: "https://arxiv.org/abs/2602.20213"
pdf_url: "https://arxiv.org/pdf/2602.20213v1"
categories:
  - "cs.SE"
  - "cs.AI"
  - "cs.CR"
tags:
  - "Agent 架构"
  - "自动化测试"
  - "代码生成"
  - "LLM 评测"
  - "对抗性测试"
  - "多策略规划"
  - "自我校准"
relevance_score: 7.5
---

# CodeHacker: Automated Test Case Generation for Detecting Vulnerabilities in Competitive Programming Solutions

## 原始摘要

The evaluation of Large Language Models (LLMs) for code generation relies heavily on the quality and robustness of test cases. However, existing benchmarks often lack coverage for subtle corner cases, allowing incorrect solutions to pass. To bridge this gap, we propose CodeHacker, an automated agent framework dedicated to generating targeted adversarial test cases that expose latent vulnerabilities in program submissions. Mimicking the hack mechanism in competitive programming, CodeHacker employs a multi-strategy approach, including stress testing, anti-hash attacks, and logic-specific targeting to break specific code submissions. To ensure the validity and reliability of these attacks, we introduce a Calibration Phase, where the agent iteratively refines its own Validator and Checker via self-generated adversarial probes before evaluating contestant code.Experiments demonstrate that CodeHacker significantly improves the True Negative Rate (TNR) of existing datasets, effectively filtering out incorrect solutions that were previously accepted. Furthermore, generated adversarial cases prove to be superior training data, boosting the performance of RL-trained models on benchmarks like LiveCodeBench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）代码生成评估中，因测试用例质量不足而导致评估结果不可靠的核心问题。研究背景是，当前LLM在代码生成和程序推理方面应用广泛，其性能评估高度依赖于测试用例的质量和覆盖度。然而，现有的主流方法存在明显不足：一方面，许多基准测试（如LiveCodeBench、CodeContests）虽然通过扩大规模或提高难度来构建更严格的测试集，但它们本质上仍依赖静态的、预先设计好的测试用例，难以全面覆盖程序实现中各种微妙的逻辑漏洞和边界情况，导致许多错误的解决方案也能侥幸通过测试。另一方面，现有的自动化测试生成方法（如基于输入变异或规则构造的方法）大多属于“黑盒模糊测试”，它们通过概率性地探索输入空间来寻找错误，侧重于统计覆盖率，而非针对特定代码实现的逻辑弱点进行精准打击。这种方法缺乏对程序语义和约束结构的深度理解，生成测试用例的针对性和有效性有限，评估结果的可靠性依然不足。

因此，本文要解决的核心问题是：**如何自动化地生成具有高度针对性、能够精准暴露程序潜在漏洞的对抗性测试用例**，从而更可靠地评估LLM的代码生成与程序推理能力。受竞技编程中“黑客”机制的启发，本文提出了CodeHacker框架。该框架将“成功黑掉一个程序”（即构造出使其失败的反例）形式化为一项对抗性测试生成任务。其核心思想是采用一种**代码感知的对抗性视角**，将待评估的具体程序作为首要分析对象，通过多策略方法（如压力测试、反哈希攻击、逻辑特定目标攻击）系统性地搜索能导致其失败的输入反例。这克服了现有方法在针对性（无法深入理解程序逻辑弱点）和可扩展性（依赖人工专家）两方面的局限，旨在实现接近专家水平的自动化“黑客”能力，为代码生成评估提供更强区分度的信号。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：代码基准测试、竞争编程中的对抗数据，以及强化学习优化方法。

在**代码基准测试**方面，现有工作主要采用三种范式：一是人工设计的测试用例（如MBPP、HumanEval、LiveCodeBench），其质量高但成本昂贵、难以自动化扩展；二是基于变异的生成方法（如在CodeContests中应用），通过重组或变异现有输入来提高覆盖率，但可能违反复杂约束，产生无效测试；三是基于LLM的生成方法（如Taco、EvalPlus、HardTests等），根据问题描述生成测试，但受限于上下文长度和输出可靠性，难以处理大型或高度结构化的实例。本文提出的CodeHacker与这些工作的核心区别在于，它模拟竞争编程中的“黑客”机制，采用多策略（如压力测试、反哈希攻击）主动生成**针对性**的对抗测试用例，以暴露提交代码中的潜在漏洞，而非被动地依赖人工设计、随机变异或条件生成。

在**竞争编程对抗数据**方面，相关工作如Codehacks数据集通过挖掘历史黑客记录构建，但由于无法通过公开API获取原始受害提交，其构建依赖于对执行失败的事后匹配。而CodeHacker作为一个自动化智能体框架，能够主动发起具有对抗意图的攻击，并引入了校准阶段来迭代优化验证器，确保攻击的有效性和可靠性，这比单纯的数据收集或随机生成方法更具针对性和系统性。

在**强化学习优化方法**方面，相关研究包括标准的PPO、去除显式价值函数的GRPO及其改进工作，以及近期将强化学习与可验证奖励（RLVR）结合用于代码生成的方法。本文虽未直接贡献于RL算法本身，但生成的对抗性测试用例被证明可作为优质的训练数据，能够提升基于RL训练的模型在LiveCodeBench等基准上的性能，从而与这类研究形成了互补关系。

### Q3: 论文如何解决这个问题？

论文通过设计一个名为CodeHacker的自动化智能体框架来解决现有基准测试中测试用例覆盖不足、无法有效检测代码提交中潜在漏洞的问题。其核心方法是模拟竞争编程中的“黑客”机制，生成针对特定提交的对抗性测试用例，以暴露隐藏的逻辑错误。

**整体框架与主要模块**：
CodeHacker框架分为两个主要阶段：
1.  **评估工具校准阶段**：在攻击参赛者提交之前，框架首先确保其“弹药”（测试用例）符合问题约束，且“判决”（检查器）准确无误。这是一个迭代精炼过程，包含两个核心组件：
    *   **验证器精炼**：智能体通过两种攻击方式主动测试验证器（负责检查输入是否满足题目约束）：a) **绕过攻击**：生成明显无效的输入，若验证器接受则暴露其“假阳性”漏洞（过于宽松）；b) **拒绝攻击**：生成有效但棘手的输入（如边界情况），若验证器拒绝则暴露其“假阴性”漏洞（过于严格）。发现漏洞后即对验证器进行修补。
    *   **检查器精炼**：类似地，智能体攻击检查器（负责验证程序输出的正确性）：a) **欺骗攻击**：构造格式正确但内容错误的输出，测试检查器是否过于宽松；b) **拒绝攻击**：识别一个有效的输出（可能是标准答案之外的另一种正确解），测试检查器是否因过于严格而误判。为防止LLM在生成正确输出时产生幻觉，引入了**抗幻觉管道**，包括限制输入规模、要求逐步推理链以及独立的LLM交叉验证。

2.  **对抗性用例生成阶段**：利用校准后的工具，生成旨在触发目标提交非AC判定的测试输入。此阶段的核心是**代码分析师**模块，它通过**双执行接口**进行混合分析：一方面通过C++沙箱对目标提交进行黑盒行为探测以验证漏洞假设；另一方面利用Python解释器进行精确计算（如复杂度验证、边界检查）。基于分析结果，框架采用三种互补的生成策略：
    *   **压力测试生成**：系统性地探索输入空间的边界，生成最大规模或特定结构模式的输入，主要暴露运行时错误、整数溢出等问题。
    *   **LLM生成**：由代码分析师的计划指导，LLM合成具有特定语义的针对性测试用例，能够针对所有类型的错误判定（WA, RE, TLE, MLE）进行设计。
    *   **反哈希生成**：专门针对使用哈希算法的提交。对于固定参数的滚动哈希，将碰撞搜索建模为最短向量问题并应用格基约减算法；对于其他情况，则采用生日攻击策略。

**创新点**：
1.  **先校准后攻击的可靠框架**：独创性地在生成攻击用例前，引入一个校准阶段，通过自我对抗的方式迭代精炼验证器和检查器，确保了后续攻击所依赖的评判基础设施的可靠性，这是生成有效且合法测试用例的基础。
2.  **混合分析与多策略生成**：代码分析师结合黑盒行为探测和白盒数学计算进行漏洞分析，提高了漏洞识别的准确性。随后集成了语义（LLM）、边界（压力测试）和算法特定（反哈希）三种生成策略，形成了多层次、针对性的攻击面。
3.  **抗幻觉与专家干预机制**：在检查器更新流程中设计了严格的多步验证管道，有效遏制了LLM幻觉。同时，对于少数验证逻辑极其复杂的难题（约5%），承认当前LLM的局限，引入有限的人工专家干预来确保评判工具的绝对正确，平衡了自动化与可靠性。
4.  **级联执行与泛化利用**：采用LLM生成为主、压力测试为后备的级联执行机制，兼顾了

### Q4: 论文做了哪些实验？

论文的实验设置主要包括：从CodeContest+数据集中随机选取2000个问题（1000个传统判题和1000个特殊判题），并聚焦于C++代码。实验使用了LiveCodeBench（包含287个AtCoder问题）进行强化学习评估。对比方法涉及不同数据集（如CodeContests、HardTests、TACO、CodeContest+）和不同模型（包括DeepSeek V3.2、GPT-5-Mini、Gemini-3.0等）。主要结果包括：1）CodeHacker生成的对抗性测试用例显著提升了真负例率（TNR），例如在特殊判题问题上达到96.05%，而基线数据集如CodeContest+的TNR为84.04%。2）在模型攻击成功率（HSR）方面，DeepSeek V3.2最高（64.83%），且推理模式相比非推理模式性能大幅下降（如DeepSeek V3.2从64.83%降至23.76%），验证了攻击是推理任务。3）对抗性数据纠正了评估指标的膨胀：在CodeHackerBench上，模型的Pass@1分数普遍下降（如Gemini-3.0-Flash从78.6%降至76.5%），表明原有测试覆盖不足。4）使用对抗性数据训练的强化学习模型在LiveCodeBench上表现更优，例如在困难问题上Pass@5准确率从25.00%提升至27.63%。消融实验显示，迭代优化循环对攻击成功率最关键（移除后从51.40%降至46.60%），而对抗性用例的添加使TNR从84.04%大幅提升至96.05%。

### Q5: 有什么可以进一步探索的点？

本文的局限性主要体现在测试用例生成的完备性、性能缺陷检测能力以及评估范围的广度上。未来研究可首先探索如何结合形式化验证或符号执行等技术，以系统性地覆盖更复杂的逻辑边界和算法漏洞，特别是涉及并发、资源竞争或特定领域语义的深层缺陷。其次，可增强对性能瓶颈（如时间复杂度、内存泄漏）的针对性测试生成，并引入动态分析或性能剖析来指导攻击策略。此外，将框架扩展到更多编程语言（如 Rust、Go）和多样化问题领域（如系统编程、机器学习代码），能进一步提升其通用性。从方法改进看，可考虑引入多智能体协作机制，让不同专长的代理分别负责逻辑攻击、性能压力测试和语义验证，并通过强化学习优化策略选择。最后，构建一个持续更新的漏洞模式库，并利用生成的对抗案例进行迭代式模型微调，有望形成更强大的代码安全评估与修复闭环。

### Q6: 总结一下论文的主要内容

本文提出CodeHacker框架，旨在通过自动生成针对性对抗测试用例来检测竞争编程解决方案中的潜在漏洞，以弥补现有基准测试在覆盖边角案例方面的不足。核心贡献在于设计了一个模拟竞争编程中“黑客”机制的多策略代理，包括压力测试、反哈希攻击和逻辑针对性攻击，并引入校准阶段，使代理能通过自生成的对抗性探针迭代优化验证器和检查器，确保攻击的有效性和可靠性。实验表明，CodeHacker显著提高了现有数据集的真阴性率，有效过滤了先前被错误接受的解决方案，且生成的对抗案例作为训练数据能提升强化学习模型在LiveCodeBench等基准上的性能。该工作将对抗生成确立为评估算法智能的关键方面，并有望应用于更广泛的软件工程任务以提升评估严谨性。
