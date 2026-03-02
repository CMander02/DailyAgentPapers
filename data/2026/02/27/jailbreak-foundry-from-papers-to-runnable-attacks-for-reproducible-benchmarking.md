---
title: "Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking"
authors:
  - "Zhicheng Fang"
  - "Jingjie Zheng"
  - "Chenxu Fu"
  - "Wei Xu"
date: "2026-02-27"
arxiv_id: "2602.24009"
arxiv_url: "https://arxiv.org/abs/2602.24009"
pdf_url: "https://arxiv.org/pdf/2602.24009v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "Agent 评测/基准"
  - "多智能体系统"
  - "Agent 工作流"
  - "LLM 安全"
  - "可复现性"
relevance_score: 7.5
---

# Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking

## 原始摘要

Jailbreak techniques for large language models (LLMs) evolve faster than benchmarks, making robustness estimates stale and difficult to compare across papers due to drift in datasets, harnesses, and judging protocols. We introduce JAILBREAK FOUNDRY (JBF), a system that addresses this gap via a multi-agent workflow to translate jailbreak papers into executable modules for immediate evaluation within a unified harness. JBF features three core components: (i) JBF-LIB for shared contracts and reusable utilities; (ii) JBF-FORGE for the multi-agent paper-to-module translation; and (iii) JBF-EVAL for standardizing evaluations. Across 30 reproduced attacks, JBF achieves high fidelity with a mean (reproduced-reported) attack success rate (ASR) deviation of +0.26 percentage points. By leveraging shared infrastructure, JBF reduces attack-specific implementation code by nearly half relative to original repositories and achieves an 82.5% mean reused-code ratio. This system enables a standardized AdvBench evaluation of all 30 attacks across 10 victim models using a consistent GPT-4o judge. By automating both attack integration and standardized evaluation, JBF offers a scalable solution for creating living benchmarks that keep pace with the rapidly shifting security landscape.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）越狱攻击领域的一个核心痛点：攻击技术快速演进与评估基准相对静态之间的矛盾，导致模型鲁棒性评估过时且难以在不同研究间进行公平比较。

研究背景是，尽管经过安全训练和策略过滤，LLM仍然容易受到诱导其产生违规行为的越狱攻击。现有评估方法主要依赖人工集成：每篇新论文提出的攻击都需要工程师手动理解细节、适配框架接口并验证复现结果。这种模式存在严重不足：首先，集成严重滞后，新攻击在发表后数周甚至数月才能被纳入评估；其次，集成质量高度依赖工程师的个人理解，容易产生偏差；最后，维护复现保真度需要反复审计，成本高昂。这导致维护一个最新、可执行的评估套件成为纵向研究的重大瓶颈。

因此，本文要解决的核心问题是：如何自动化、标准化地将快速发表的越狱攻击论文转化为可立即执行的攻击模块，并在统一的评估框架下进行复现和评测，从而构建一个能够跟上安全形势快速变化的、可复现的“活”基准。论文提出的Jailbreak Foundry系统正是为了填补这一空白，通过多智能体工作流将论文转化为可执行模块，并实现标准化的评估，以支持跨攻击、跨模型的可比性分析。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：方法类、评测与框架类以及代码生成类。

在**方法类**研究中，论文梳理了越狱攻击的演进脉络，将其划分为搜索策略和载体策略两个正交维度。搜索策略包括单次生成、随机采样、无反馈的状态选择以及基于受害者反馈的优化等方法；载体策略则涵盖语言重构、上下文包装、结构化格式包装、混淆与重建以及多策略组合等。这些工作为理解攻击机制提供了基础，而本文的JBF系统旨在将这些多样化的攻击方法统一转化为可执行模块。

在**评测与框架类**方面，已有多个基准和框架致力于标准化评估。例如，AdvBench和HarmBench推动了大规模有害指令测试与自动化红队评估；GuidedBench强调基于准则的评判以减少不一致性；JailbreakBench则注重可执行构件和固定测试环境。同时，EasyJailbreak、TeleAI-Safety和OpenRT等框架提供了模块化抽象以提升可复现性。然而，这些工作普遍存在覆盖新鲜度不足的问题，即新攻击的集成往往依赖手动且设置差异大，难以进行纵向比较。本文的JBF系统直接针对这一缺口，通过自动化流程将论文转化为统一评估的可执行攻击，实现了“活”的基准。

在**代码生成类**研究中，论文提及了从论文到代码的智能体技术，这类工作旨在根据论文描述自动生成实现代码。但在快速演进的越狱领域，通用代码生成智能体往往难以同时保证可执行性和高保真复现。本文的JBF系统通过提取越狱攻击中共用的推理与评判循环脚手架，并专注于实现各论文特有的攻击组件，从而在复用基础设施的基础上，显著提升了复现的保真度和效率。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为JAILBREAK FOUNDRY（JBF）的系统来解决大语言模型越狱攻击评估中存在的基准滞后与结果不可比问题。其核心方法是一个多智能体工作流，将学术论文自动转化为可在统一评估框架中执行的模块，从而实现标准化、可复现的基准测试。

整体框架由三个核心组件构成：JBF-LIB、JBF-FORGE和JBF-EVAL。JBF-LIB作为共享框架核心，定义了模块契约C，包括基类接口、输入输出模式和类型化参数钩子，并提供了可复用的工具集（如提示格式化、请求响应归一化、缓存和日志）。这一设计确保了所有攻击模块遵循统一接口，支持配置驱动的实例化和一致的尝试处理，是实现自动化和可比性的基础。

JBF-FORGE是实现“从论文到可运行模块”转化的关键创新模块。它采用一个规划器-编码器-审计器（Planner-Coder-Auditor）的多智能体流水线。具体流程是：首先，规划器（π）阅读论文（及官方代码仓库R，如果存在），生成一个结构化计划（s_p），详细说明攻击算法、控制流、提示模板和参数化方案，并将其映射到契约C上。接着，编码器（κ）根据该计划实现具体的Python模块（m_p），确保暴露类型化参数并避免混入评估逻辑。然后，审计器（α）对生成的模块进行静态、逐行引用的审计，检查其与计划s_p和契约C的一致性，并生成修订报告。这个过程在一个有界循环中迭代，直至审计通过或达到迭代上限。当复现的攻击成功率（ASR）与论文报告值偏差较大时（Δ < -10.0），系统会触发一个增强的精炼环节，使用更强大的智能体进行深度代码级差距分析和针对性修补。

JBF-EVAL是标准化的评估层。它建立在JBF-LIB之上，通过分离数据集、执行和评判环节来确保结果可比性。它提供统一的数据集加载接口、可替换的评判器（将尝试记录映射为布尔成功标签）以及一个配置驱动的运行器。该运行器能够从注册表中实例化攻击，在一致的测试环境下运行，并报告ASR等标准指标，支持可恢复的大规模运行和批量扫描。

该系统的核心创新点在于：1）**自动化与保真度**：通过多智能体协作，将非结构化的论文描述自动转化为高质量、符合契约的可执行代码，平均ASR偏差仅为+0.26个百分点，实现了高保真复现。2）**代码复用与效率**：共享的基础设施使攻击特定实现代码量相比原始仓库减少了近一半，平均代码复用率达到82.5%。3）**标准化评估**：提供了一个统一的评估套件，能够对所有复现的攻击和多个受害者模型使用一致的评判标准（如GPT-4o）进行测试，从而消除了因数据集、测试工具和评判协议差异导致的评估漂移，创造了一个能够跟上快速演进的越狱攻击的“活”基准。

### Q4: 论文做了哪些实验？

论文通过构建JAILBREAK FOUNDRY系统，进行了三大类实验以验证其核心目标：将越狱论文转化为高保真、可复现的攻击实现，并支持系统化分析。

**实验设置与数据集**：实验复现了30种越狱攻击（其中22个有官方实现，8个仅依据论文文本）。评估主要在AdvBench或JailbreakBench数据集上进行，优先使用AdvBench以保证与JBF基准的可比性。实验采用多智能体工作流（JBF-FORGE）进行论文到模块的转换，其中规划、编码和审计分别由Gemini-3-pro、Claude-4.5-sonnet和GPT-5.1 Codex等LLM负责，并辅以长运行的Claude Code智能体进行深度优化。评估阶段（JBF-EVAL）使用统一的测试框架和GPT-4o作为评判模型，对10个受害者模型进行了标准化评估。

**对比方法与主要结果**：
1.  **复现保真度**：在论文匹配的设置下，复现攻击的成功率与原始报告结果高度一致，平均攻击成功率偏差仅为+0.26个百分点，范围在-16.0%到+20.0%之间。这表明JBF能够高保真地复现现有攻击。
2.  **代码效率与复用**：通过共享基础设施（JBF-LIB），集成的攻击模块代码量相比原始仓库减少了近一半（压缩比ρ=0.42）。在集成代码库中，平均有82.5%的代码是共享的框架代码，仅17.5%是攻击特定逻辑，体现了高度的可维护性和复用性。
3.  **标准化跨模型评估**：在统一的评估框架下，所有30种复现攻击在10个受害者模型上进行了测试。关键指标显示：20/30的攻击在至少6个模型上达到了≥50%的ASR；13/30的攻击在至少6个模型上达到了≥70%的ASR。最强的复现攻击在多达8/10的模型上取得了超过90%的ASR，证明了其在多样化模型上的广泛有效性。
4.  **消融实验**：通过对比“有代码仓库”和“无代码仓库”两种复现方式，发现官方可运行仓库能显著提升复现效果（平均ASR从66.5%提升至86.3%），尤其对于脚手架复杂的方法增益巨大（如GTA提升+48.6%）。增强的精炼流程（enhanced refinement pass）能将平均复现差距从-16.2%改善至-7.6%，有效弥补了实现驱动的性能不足。

### Q5: 有什么可以进一步探索的点？

该论文提出的Jailbreak Foundry系统在自动化复现和评估越狱攻击方面取得了显著进展，但其局限性和未来探索空间仍值得关注。首先，系统目前主要聚焦于论文描述的“白盒”攻击，对于依赖复杂外部工具或动态交互的“灰盒/黑盒”攻击（如多轮对话诱导、工具使用攻击）的自动化转换能力可能有限。其次，其评估依赖统一的GPT-4o作为评判器，可能存在评判偏差或无法捕捉人类评估中细微的越狱成功迹象，未来需探索更鲁棒的多评判器协议或人类评估集成。

未来研究方向可沿以下路径拓展：一是构建动态攻防交互评估框架，不仅自动化集成新攻击，也自动化集成防御策略（如输入过滤、后处理机制），从而生成攻防热力图，系统性分析不同防御对各类攻击的脆弱性模式。二是增强系统的时序与版本管理能力，建立攻击模块的版本化数据库与回归测试套件，以追踪攻击演化和模型安全性的长期趋势。三是探索跨模态越狱攻击的复现，如图文多模态模型的安全评估。改进思路上，可引入更细粒度的语义约束检查与仿真测试环境，提升复杂攻击场景下代码生成的正确性；同时，设计开源、可配置的评判框架，支持社区自定义评估标准，以增强基准的适应性和公正性。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型越狱攻击技术发展快于评估基准的问题，提出了JAILBREAK FOUNDRY系统，旨在实现可复现的标准化评测。核心问题是现有攻击方法在论文、数据集、评估框架和判断协议上存在差异，导致鲁棒性评估结果过时且难以横向比较。方法上，JBF设计了一个多智能体工作流，包含三个组件：JBF-LIB提供共享接口和可复用工具；JBF-FORGE通过多智能体将论文自动转化为可执行模块；JBF-EVAL统一评估流程。主要结论显示，系统成功复现了30种攻击，其攻击成功率与原始报告的平均偏差仅为+0.26个百分点，且通过共享基础设施将攻击特定代码减少近一半，代码复用率达82.5%。该系统实现了对10个受害模型使用一致GPT-4o评判器的标准化评估，为构建能跟上安全形势快速变化的动态基准提供了可扩展的自动化解决方案。
