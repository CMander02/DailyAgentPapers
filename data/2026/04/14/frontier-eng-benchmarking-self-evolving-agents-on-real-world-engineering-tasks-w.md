---
title: "Frontier-Eng: Benchmarking Self-Evolving Agents on Real-World Engineering Tasks with Generative Optimization"
authors:
  - "Yizhe Chi"
  - "Deyao Hong"
  - "Dapeng Jiang"
  - "Tianwei Luo"
  - "Kaisen Yang"
  - "Boshi Zhang"
  - "Zhe Cao"
  - "Xiaoyan Fan"
  - "Bingxiang He"
  - "Han Hao"
  - "Weiyang Jin"
  - "Dianqiao Lei"
  - "Qingle Liu"
  - "Houde Qian"
  - "Bowen Wang"
  - "Situ Wang"
  - "Youjie Zheng"
  - "Yifan Zhou"
  - "Calvin Xiao"
  - "Eren Cai"
date: "2026-04-14"
arxiv_id: "2604.12290"
arxiv_url: "https://arxiv.org/abs/2604.12290"
pdf_url: "https://arxiv.org/pdf/2604.12290v1"
categories:
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent Benchmark"
  - "Generative Optimization"
  - "Iterative Agent"
  - "Propose-Execute-Evaluate Loop"
  - "Engineering Agent"
  - "Continuous Feedback"
  - "Feasibility Constraints"
  - "Multi-Task Benchmark"
relevance_score: 9.0
---

# Frontier-Eng: Benchmarking Self-Evolving Agents on Real-World Engineering Tasks with Generative Optimization

## 原始摘要

Current LLM agent benchmarks, which predominantly focus on binary pass/fail tasks such as code generation or search-based question answering, often neglect the value of real-world engineering that is often captured through the iterative optimization of feasible designs. To this end, we introduce Frontier-Eng, a human-verified benchmark for generative optimization -- an iterative propose-execute-evaluate loop in which an agent generates candidate artifacts, receives executable verifier feedback, and revises them under a fixed interaction budget -- spanning $47$ tasks across five broad engineering categories. Unlike previous suites, Frontier-Eng tasks are grounded in industrial-grade simulators and verifiers that provide continuous reward signals and enforce hard feasibility constraints under constrained budgets. We evaluate eight frontier language models using representative search frameworks, finding that while Claude 4.6 Opus achieves the most robust performance, the benchmark remains challenging for all models. Our analysis suggests a dual power-law decay in improvement frequency ($\sim$ 1/iteration) and magnitude ($\sim$ 1/improvement count). We further show that although width improves parallelism and diversity, depth remains crucial for hard-won improvements under a fixed budget. Frontier-Eng establishes a new standard for assessing the capacity of AI agents to integrate domain knowledge with executable feedback to solve complex, open-ended engineering problems.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI智能体（Agent）评估体系中的一个关键缺陷：现有基准测试主要关注具有二元（通过/失败）结果的单次任务（如代码生成、基于搜索的问答），而忽视了现实世界工程实践中至关重要的“生成式优化”能力。研究背景是，工程领域的核心价值往往体现在对已有可行方案的持续迭代优化上（例如优化充电算法以缩短时间、改进结构设计以节省材料），这是一个在约束条件下不断改进、没有明确理论最优解的开放式过程。现有基于LLM的智能体基准无法有效评估这种需要整合领域知识、代码合成与可执行反馈的迭代优化能力。

现有方法的不足在于：1）主流智能体基准（如编程、问答）奖励信号是二元的，无法衡量持续改进的程度；2）已有的生成式优化研究多局限于狭窄领域（如数学发现、算法设计），缺乏覆盖多工程学科、使用工业级仿真器和验证器的综合评估平台；3）缺乏一个能防止“奖励黑客”行为、确保改进真实性的标准化测试环境。

因此，本文的核心问题是：如何系统性地评估AI智能体在真实世界、多学科工程任务中进行“生成式优化”的能力？具体而言，即智能体在固定的交互预算内，通过“生成-执行-评估”的循环，整合领域知识检索与代码编辑，根据可执行验证器的反馈持续改进初始可行方案，以在硬性可行性约束下实现性能提升。为此，论文提出了Frontier-Eng基准，包含47个跨越五大工程类别的任务，其特点是任务基于工业级仿真器、提供连续奖励信号、执行硬约束，并建立了防篡改的标准化评估流程，旨在为衡量智能体解决复杂、开放式工程问题的能力设立新标准。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**方法类、评测类和应用类**。

**方法类工作**聚焦于利用大语言模型进行迭代优化的范式。例如，FunSearch 利用LLM引导的程序搜索发现新的数学构造；AlphaEvolve 将基于自动评估的进化代码编辑范式扩展到更广泛的科学和算法发现；“Learning to Discover at Test Time” 展示了模型在固定发现问题上持续适应并取得新SOTA的能力；Self-Refine 则将迭代自我反馈形式化为一个通用的“提出-批评-修订”范式。这些工作共同构成了“生成式优化”这一方法家族。本文的 Frontier-Eng 基准正是为了系统评估这类方法在真实工程场景下的能力而构建的，其核心区别在于强调在**工业级仿真器和验证器**提供的连续奖励信号与硬性可行性约束下进行优化，而非在狭窄或合成的领域进行纯推理。

**评测类工作**主要指现有的智能体基准测试。当前主流基准（如代码生成或基于搜索的问答）大多关注具有二元通过/失败结果的“0到1”任务。本文明确指出，Frontier-Eng 与这些基准的根本区别在于评测范式的不同：它评估的是智能体在固定交互预算内，对**已有可行方案进行迭代优化**的能力，其奖励是连续且无理论上界的，更贴近真实工程中价值创造的核心过程。

**应用类工作**涉及将AI用于特定工程领域优化的探索，例如在数学、GPU内核工程或算法设计中的发现。本文的贡献在于将这些分散的应用整合到一个**跨学科、大规模**的基准中，涵盖了计算、运筹学、机器人、光学和物理科学等五大工程类别，从而提供了一个更全面、统一的评估平台，以检验智能体整合领域知识与可执行反馈解决复杂、开放式工程问题的综合能力。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为Frontier-Eng的基准测试套件来解决现有LLM智能体基准测试在真实世界工程任务评估上的不足。其核心方法是定义一个名为“生成式优化”的迭代框架，并基于此框架构建一个包含47个多样化任务的、经过严格质量控制的基准。

**核心方法与整体框架**：
论文将工程优化任务形式化为一个三元组 τ = (C, x₀, E)，其中C是任务上下文，x₀是初始可行解，E是评估器。生成式优化智能体A的目标是在固定的交互预算B内，通过迭代的“提出-执行-评估”循环，最大化找到的最佳可行解分数s*。在每个迭代步骤t，智能体基于任务上下文C和完整的历史尝试记录H_{t-1}提出一个新的候选解x_t，然后由评估器E返回可行性指标v_t和分数s_t。这个框架的关键在于智能体A是一个围绕大语言模型构建的生成器，它通过代码生成来产生候选解，而不是进行传统的梯度优化。

**主要模块/组件与架构设计**：
1.  **任务定义与来源**：基准包含47个任务，覆盖五大工程领域：计算与量子信息、运筹学与决策科学、机器人控制与能源系统、光学与通信系统、物理科学与工程设计。任务来源多样，包括工程竞赛、学术基准套件、经典课程项目、工业级仿真工具和领域专家的原创贡献。
2.  **评估器 (E)**：这是基准的核心组件。每个任务都配备一个工业级模拟器或验证器，提供连续的奖励信号，并在约束预算下强制执行严格的可行性约束。评估器返回二元可行性指标和标量分数。
3.  **智能体交互接口**：定义了智能体与任务环境的标准交互协议。智能体接收上下文和历史，输出候选解决方案（如代码、配置文件）。
4.  **质量与完整性保障机制**：
    *   **纳入标准**：任务必须满足四个要求：清晰自包含的规范、可编辑的初始工件、可运行的评估器、已验证的初始可行解。
    *   **质量控制**：采用两阶段评审流程（自动化代码检查与人工领域审核）。
    *   **评估完整性**：实施三层防护防止奖励黑客行为：**隔离**（评估器代码只读，解决方案在沙箱中运行）、**验证器解析评分**（分数直接从评估器输出日志中提取，防止智能体自报告）、**评估鲁棒性**（使用多随机种子、随机化输入、多场景平均以及正确性检查来确保改进的真实性）。

**关键技术点与创新点**：
1.  **生成式优化形式化**：将工程优化问题形式化为一个受预算约束的、基于LLM代码生成的迭代优化问题，强调了历史反馈的利用和搜索策略的作用。
2.  **真实性与工业级 grounding**：与以往基于合成或简化任务的基准不同，Frontier-Eng的任务根植于真实的工业级模拟器和验证器（如MuJoCo、PyBullet、OpenSSL、有限元求解器等），提供了连续、可执行的反馈并强制执行硬约束，更能反映真实工程挑战。
3.  **严格的防黑客设计**：通过隔离环境、验证器解析评分和鲁棒性评估等多重机制，确保评分反映的是解决方案在真实约束下的真实改进，而非利用评估漏洞。
4.  **广度与深度兼具的任务集**：涵盖从底层CUDA内核优化、量子电路编译，到高层机器人控制、库存管理、光学设计等跨学科任务，旨在全面评估智能体整合领域知识与可执行反馈解决复杂、开放式工程问题的能力。

总之，论文通过精心设计一个形式化框架、构建一个高质量且多样化的任务库、并实施严格的评估保障措施，建立了一个新的基准，旨在推动能够进行持续自我演进的AI智能体的发展。

### Q4: 论文做了哪些实验？

论文实验主要评估了多个前沿大语言模型在 Frontier-Eng 基准上的性能。实验设置方面，所有模型在固定的“openevolve”预算下运行100次迭代，使用相同的搜索框架、由贡献者提供的相同初始程序，并在声明的任务环境中由相同的冻结任务验证器进行评估。数据集/基准测试为 Frontier-Eng 基准，包含跨越五大工程类别（如空气动力学、密码学、机器人学等）的47个真实世界工程任务，这些任务基于工业级模拟器和验证器，提供连续奖励信号并强制执行严格的可行性约束。

对比方法涉及九种基础模型：claude-opus-4.6、qwen3-coder-next、seed-2.0-pro、gpt-5.4、gpt-oss-120b、glm-5、deepseek-v3.2、grok-4.20 和 gemini-3.1-pro-preview。

主要结果以跨任务平均排名（越低越好）为核心指标。Claude 4.6 Opus 取得了最佳平均排名（3.18），其次是 GLM-5（4.02）、DeepSeek-V3.2（4.41）和 GPT-OSS-120B（4.46）。性能概况图显示，Claude 4.6 Opus 在42.6%的任务上达到最优，在59.6%的任务上达到接近最优（与最优差距在10%以内），展现了最强的前沿性能和跨任务鲁棒性。胜率图则显示 GLM-5 和 GPT-OSS-120B 在超越基线方面最为可靠。分析还揭示了改进频率（约1/迭代）和幅度（约1/改进次数）呈现双重幂律衰减，并指出在固定预算下，搜索深度对于取得艰难改进至关重要。

### Q5: 有什么可以进一步探索的点？

本文提出的 Frontier-Eng 基准在评估智能体迭代优化能力方面迈出了重要一步，但仍存在一些局限性和可进一步探索的方向。首先，基准任务虽基于工业级模拟器，但本质上仍是在受控的仿真环境中进行，未能完全模拟真实工程中动态、多变的物理约束和人际协作复杂性。其次，当前评估主要依赖固定的交互预算和预定义的验证器，未来可探索更开放、自适应预算的优化过程，以及引入人类在环的混合评估机制，以更好地反映实际工程中资源权衡与专家干预。

从方法改进角度看，论文观察到改进频率与幅度的双幂律衰减，这提示智能体的搜索策略可能在后期陷入局部最优。未来可研究更高效的探索-利用平衡机制，例如引入元学习来自适应调整提议-修订策略，或结合符号推理与神经生成，以提升在硬约束下的深层优化能力。此外，当前基准未充分考虑多智能体协作场景，在复杂工程任务中，分布式智能体间的知识共享与分工优化是一个值得探索的方向，这可能更贴近真实工程团队的演进模式。

### Q6: 总结一下论文的主要内容

该论文针对现有LLM智能体基准测试过于侧重二元通过/失败任务（如代码生成）而忽视真实工程迭代优化的问题，提出了Frontier-Eng基准。其核心贡献是构建了一个覆盖五大工程领域、包含47项任务的人类验证基准，用于评估“生成式优化”能力，即智能体在固定交互预算内，通过“生成-执行-评估”循环，依据可执行的验证器反馈持续迭代改进候选方案。

方法上，该基准的关键创新在于其任务基于工业级模拟器和验证器，能提供连续奖励信号并强制执行严格的可行性约束，从而更贴近真实工程场景。论文评估了八个前沿语言模型，发现Claude 4.6 Opus表现最稳健，但所有模型在该基准上仍面临挑战。

主要结论包括：1）改进频率和幅度呈现双重幂律衰减规律；2）在固定预算下，搜索深度对于取得艰难改进至关重要，而宽度主要提升并行性和多样性。该研究为评估AI智能体整合领域知识与可执行反馈以解决复杂、开放式工程问题的能力设立了新标准。
