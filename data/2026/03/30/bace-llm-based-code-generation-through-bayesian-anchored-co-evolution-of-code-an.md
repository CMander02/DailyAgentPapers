---
title: "BACE: LLM-based Code Generation through Bayesian Anchored Co-Evolution of Code and Test Populations"
authors:
  - "Kaushitha Silva"
  - "Srinath Perera"
date: "2026-03-30"
arxiv_id: "2603.28653"
arxiv_url: "https://arxiv.org/abs/2603.28653"
pdf_url: "https://arxiv.org/pdf/2603.28653v1"
categories:
  - "cs.NE"
  - "cs.SE"
tags:
  - "代码智能体"
  - "多智能体框架"
  - "测试生成"
  - "贝叶斯方法"
  - "协同进化"
  - "代码生成"
  - "自我改进"
  - "评估基准"
relevance_score: 7.5
---

# BACE: LLM-based Code Generation through Bayesian Anchored Co-Evolution of Code and Test Populations

## 原始摘要

Large Language Models (LLMs) have demonstrated impressive capabilities in code generation. While an interactive feedback loop can improve performance, writing effective tests is a non-trivial task. Early multi-agent frameworks, such as AgentCoder, automated this process but relied on generated tests as absolute ground truth. This approach is fragile: incorrect code frequently passes faulty or trivial tests, while valid solutions are often degraded to satisfy incorrect assertions. Addressing this limitation, newer methods have largely abandoned test generation in favor of planning and reasoning based on examples. We argue, however, that generated tests remain a valuable signal if we model them as noisy sensors guided by bayesian updates. To this end, we introduce BACE (Bayesian Anchored Co-Evolution), a framework that reformulates synthesis as a Bayesian co-evolutionary process where code and test populations are evolved, guided by belief distributions that are reciprocally updated based on noisy interaction evidence. By anchoring this search on minimal public examples, BACE prevents the co-evolutionary drift typical of self-validating loops. Extensive evaluations on LiveCodeBench v6 (post-March 2025) reveal that BACE achieves superior performance across both proprietary models and open-weight small language models.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型在代码生成任务中，因依赖自动生成的、不可靠的测试用例进行反馈和修复，而导致的合成系统脆弱性问题。研究背景是，尽管LLM在代码生成上取得了显著进展，但生成的代码常包含逻辑错误。为此，以AgentCoder为代表的早期多智能体框架引入了“开发者-测试者”的交互式闭环，通过执行生成的测试来迭代修复代码，提升了性能。然而，现有方法存在根本不足：它们将生成的测试视为绝对正确的“金标准”，这在实际中非常脆弱。一方面，错误的代码可能通过有缺陷或过于简单的测试（假阳性）；另一方面，正确的逻辑方案可能因测试断言错误而被错误拒绝，并在后续修复中被降级为错误代码（假阴性）。这种对不可靠测试的确定性依赖，导致一些最新的先进框架（如MapCoder、CodeSIM）完全放弃了测试生成，转而依赖纯粹的规划和推理。

本文要解决的核心问题是：当作为衡量工具的测试套件本身是不可靠的真相来源时，如何构建一个代码合成系统，使其能够收敛到正确的解决方案？换言之，论文挑战了“生成的测试毫无价值”的过早结论，认为问题在于缺乏一种在测试非绝对正确时有效利用它们的方法。为此，论文提出了BACE框架，将代码合成重新定义为一个贝叶斯协同进化过程。其核心思路是同时维护代码和测试两个种群，并将测试执行结果视为噪声信号而非二元判断，通过贝叶斯更新来迭代调整对每个代码和测试个体正确性的“信念”分布。同时，为了防止整个系统在协同进化中漂移到自我验证的错误循环中，BACE引入“锚定”机制，利用问题描述中提供的少量高可信度公开输入输出示例，来约束信念更新，确保搜索过程与基本事实保持一致。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三大类：基于搜索的合成方法、基于LLM的代码生成与反馈方法，以及多智能体协作框架。

在**基于搜索的合成方法**中，遗传编程（GP）将合成视为优化问题，而Hillis和Arcuri等人的“宿主-寄生虫”协同进化方法通过共同进化程序和对抗性测试来避免局部最优。本文的BACE框架继承了协同进化思想，但关键区别在于：它利用LLM初始化候选代码，将进化重点放在“优化”而非“从零发现”上，并引入贝叶斯框架处理测试噪声。

在**基于LLM的代码生成与反馈方法**中，早期“开环”方法（如CoT、SCoT）依赖思维链推理，后续“闭环”方法（如Reflexion、Self-Debugging）则引入执行反馈。本文工作属于闭环范式，但与许多依赖生成测试进行验证的方法（如AgentCoder、DebateCoder）不同，BACE不将生成的测试视为绝对真值，而是将其建模为“有噪声的传感器”，通过贝叶斯更新来管理其不确定性，从而避免有效解决方案因错误断言而退化。

在**多智能体与验证策略**方面，一些近期研究（如MapCoder、CodeSIM）因测试生成不可靠而完全放弃测试生成，转而专注于基于输入/输出示例的推理。另一些方法（如CodeT）则通过代码与测试的双重执行一致性来筛选方案。本文的BACE框架与这些方法都不同：它通过“锚定”在少量公开示例上，引导协同进化搜索，从而既能安全利用生成测试中的高价值信号，又能避免典型自验证循环中的协同进化漂移。与同样采用协同进化的CoCoEvo相比，由于后者缺乏标准基准结果和开源代码，本文无法直接比较，但BACE在贝叶斯信念更新和行为多样性保持机制上具有独特性。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为BACE（贝叶斯锚定协同进化）的框架来解决LLM代码生成中测试作为“噪声传感器”的不可靠性问题。其核心方法是将代码生成重新构建为一个贝叶斯协同进化过程，其中代码种群和测试种群并行进化，并通过基于交互证据的信念分布进行相互指导。

整体框架是一个迭代的协同进化算法。主要组件包括：1）**代码种群**和**测试种群**，分别代表候选解决方案和测试用例；2）**锚定集**，由问题描述中提供的公开输入/输出示例构成，其信念值固定为接近1，作为进化过程不可动摇的参照点；3）**信念分布**，为每个代码和测试个体关联一个后验正确概率；4）**观察矩阵**，记录代码与测试之间所有执行通过/失败的结果。

其关键技术在于**概率化建模代码-测试交互**。BACE不将测试结果视为绝对真理，而是建模为受三个噪声超参数（α, β, γ）影响的“噪声传感器”观测值。基于贝叶斯更新规则，在log-odds空间中对个体信念进行迭代更新。更新机制具有一个关键特性：只有当交互方的信念超过一个由噪声模型定义的**可信度阈值**时，“通过”结果才会正向提升被评估方的信念；否则更新逻辑会反转，从而惩罚那些通过低信念（可能错误）代码的测试，增强了系统的鲁棒性。

创新点主要体现在三个方面：首先，**贝叶斯锚定更新顺序**，在每一代中严格按顺序执行：先基于锚定集更新代码信念，再基于已锚定的代码种群更新测试信念，最后基于测试的先验信念进一步更新代码。这种顺序防止了不稳定的反馈循环。其次，**交替进化策略**，在偶数代进化测试种群而冻结代码种群，在奇数代则相反，以此稳定学习信号，避免“红皇后”动态。最后，**基于功能等价性的多样性保持精英选择**。对于代码，精英集不仅选择信念最高的个体，还从每个功能等价组（在观察矩阵中行为向量完全相同的代码）中选择最高信念代表，以保持策略多样性。对于测试，则消除功能冗余的测试（诱导相同行为向量的测试），仅保留信念最高的代表，形成一个高效且正交的“传感器”集合。

### Q4: 论文做了哪些实验？

实验设置方面，论文在LiveCodeBench v6（2025年3月后版本）数据集上进行评估，该基准包含多种编程问题。对比方法包括早期多智能体框架AgentCoder以及较新的基于规划和示例推理的方法。BACE框架的核心是贝叶斯协同进化过程，其中代码种群和测试种群并行演化，并通过基于噪声交互证据的贝叶斯更新来引导。

主要结果显示，BACE在专有模型和开源小语言模型上均实现了优越性能。具体关键数据指标表明，BACE在整体代码生成准确率上显著超越了基线方法，特别是在处理复杂或易产生误导性测试的问题时，其通过锚定最小公共示例有效避免了协同进化漂移，从而提升了生成代码的鲁棒性和正确性。

### Q5: 有什么可以进一步探索的点？

该论文提出的BACE框架虽然通过贝叶斯协同进化改进了代码生成与测试验证的循环，但仍存在一些局限性和值得探索的方向。首先，其“锚定”机制依赖于少量公开示例，这可能导致对特定问题类型的过拟合，未来可研究如何动态选择或生成更通用的锚点，或引入领域自适应技术以提升泛化能力。其次，框架中测试生成仍被视为“带噪声的传感器”，但噪声模型较为简单；未来可结合更精细的测试质量评估（如基于语义的覆盖度分析）来优化贝叶斯更新过程，减少误判。此外，协同进化过程计算开销较大，可探索轻量化进化策略或提前终止机制以提升效率。从更广视角看，该方法尚未充分探索多模态反馈（如编译器错误信息或运行时性能数据）的融合，未来可将其纳入信念更新以增强鲁棒性。最后，当前评估集中于基准数据集，实际复杂项目中的长周期代码生成与测试维护仍是挑战，需进一步研究如何将框架扩展到迭代开发场景中。

### Q6: 总结一下论文的主要内容

该论文针对LLM代码生成中测试反馈不可靠的问题，提出了BACE框架。核心问题是：当生成的测试本身存在错误时，如何利用其作为噪声信号来引导代码合成？传统方法将生成测试视为绝对真值，导致错误代码通过有缺陷的测试（假阳性），或有效方案为满足错误断言而被降级（假阴性）。

BACE将合成重新定义为贝叶斯协同进化过程。方法上，同时维护代码和测试两个种群，并引入贝叶斯信念分布来建模个体正确性。执行结果被视为噪声观测，用于交互更新两个种群的信念。为防止协同进化漂移，框架使用问题描述中提供的少量公共输入输出示例作为“锚点”，约束信念更新。此外，通过基于行为向量的精英策略和差分测试来保持种群多样性。

实验表明，在LiveCodeBench v6上，BACE在GPT-5-Mini和Qwen2.5-Coder-7b等模型上均优于现有多智能体框架。主要贡献在于提出了贝叶斯协同进化框架、信念锚定机制以及行为多样性保持策略，证明了在妥善处理噪声的情况下，生成的测试仍能有效提升代码合成性能。
