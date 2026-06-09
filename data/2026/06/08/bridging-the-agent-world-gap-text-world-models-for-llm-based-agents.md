---
title: "Bridging the Agent-World Gap: Text World Models for LLM-based Agents"
authors:
  - "Yixia Li"
  - "Hongru Wang"
  - "Peng Lai"
  - "Zhiwen Ruan"
  - "He Zhu"
  - "Youxin Zhu"
  - "Ganlong Zhao"
  - "Minda Hu"
  - "Yun Chen"
  - "Sibei Yang"
  - "Peng Li"
  - "Jeff Z. Pan"
  - "Jia Pan"
  - "Guanhua Chen"
  - "Yang Liu"
  - "Guanbin Li"
date: "2026-06-08"
arxiv_id: "2606.09032"
arxiv_url: "https://arxiv.org/abs/2606.09032"
pdf_url: "https://arxiv.org/pdf/2606.09032v1"
github_url: "https://github.com/sustech-nlp/awesome-text-world-models"
categories:
  - "cs.CL"
tags:
  - "LLM-based Agent"
  - "Text World Model"
  - "World Model Construction"
  - "Planning with World Model"
  - "Agent Training Data Synthesis"
  - "Agent Evaluation"
  - "Code-as-WM"
  - "LLM-as-WM"
relevance_score: 9.5
---

# Bridging the Agent-World Gap: Text World Models for LLM-based Agents

## 原始摘要

Large language model (LLM)-based agents are increasingly used in interactive textual environments, from web navigation and code editing to tool use and long-horizon dialogue. Yet many remain largely reactive, mapping observations to actions without an explicit model of how these environments are structured and evolve. This motivates text world models (TWMs): transition models over textual states that, given a state and a candidate action, predict the resulting webpage, terminal output, API response, or user reply, thereby supporting planning, efficient learning, and principled evaluation. We systematically review text world models for LLM-based agents, organized around a formal framework and the agent lifecycle: (1) Foundations, defining text world models and characterizing them by state representation and grounding domain; (2) Construction, taxonomizing LLM-as-WM and code-as-WM paradigms and reviewing methods for building them; (3) Application, examining how world models support agents at training time through experience synthesis and at inference time through planning, verification, and adaptation; and (4) Evaluation, covering both evaluation of the world model itself and its use as an evaluation environment for agents. We aim to consolidate this rapidly developing area, clarify its design space, and highlight open challenges for future research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决基于大语言模型的智能体在交互式文本环境中缺乏显式的环境结构化与演化模型的核心问题。研究背景是，当前许多LLM智能体主要采用“反应式”架构，即将观测直接映射到动作，在网页导航、代码编辑、工具使用和长程对话等任务中表现出色。然而，现有方法的不足在于：智能体无法显式理解并预测环境的状态演化——网页代理可能在不理解页面任务跨点击如何变化的情况下选择链接；代码代理可能在不模拟源码变更对运行时行为的影响下直接修改文件；对话代理可能无法维持对用户动态目标的稳定模型。这种“智能体-世界鸿沟”限制了规划、高效学习和原则性评估能力。因此，本文要解决的核心问题是：如何系统性地构建、使用和评估“文本世界模型”（TWM），即一种能够根据当前状态和候选动作预测下一文本状态（如网页、终端输出、API响应或用户回复）的转移模型，从而为LLM智能体提供显式的世界理解与前瞻能力，填补这一方法论空白并梳理碎片化的研究领域。

### Q2: 有哪些相关研究？

本文的相关研究可以从方法、应用和评测三个类别进行梳理。

**方法类**：核心工作包括“LLM-as-World Model”范式（如使用语言模型直接预测环境状态变化）和“Code-as-World Model”范式（如用可执行程序表示环境动态）。本文与这些工作的关系在于，它提出了一个统一框架（状态表示与接地域），将分散的模型构建方法（如Fine-grained vs. Coarse-grained state）系统化，并明确了二者的互补性，而非停留在个别案例。

**应用类**：相关研究集中在规划（如Tree-of-Thought、ReAct）、经验合成（如Sim-to-Real）、验证与适应性（如自我纠错）。本文区别于这些应用研究，不是仅仅展示世界模型的某项能力，而是从训练阶段（通过合成经验提升样本效率）到推理阶段（规划、验证、适应）进行了全生命周期梳理，揭示了世界模型作为核心模块如何串联起多种代理能力。

**评测类**：已有工作包括对世界模型本身准确性的评估（如状态预测正确率）以及将其作为评估环境（如构建模拟器测试代理策略）。本文的贡献在于将两类评估并列，并指出了当前评测中缺乏对“泛化到未见环境”能力的系统衡量，明确呼吁更原则性的评估框架。

### Q3: 论文如何解决这个问题？

该论文的核心方法是提出“文本世界模型”(Text World Models, TWM)的概念框架,即一种在文本层面显式建模环境动态的系统。整体架构围绕一个形式化的转移函数定义：给定智能体可见状态\(s_t\)和候选动作\(a_t\),TWM输出后继状态的文本渲染\(\hat{s}_{t+1}\),其形式可以是自然语言描述、结构化记录或代码片段。这一设计的关键在于,与预测像素或潜变量的经典世界模型不同,TWM的输出是可读、可编辑、可验证的文本,可直接回送给LLM智能体用于规划。

论文构建了一个二维分类法来组织现有工作：一条轴是**状态表示**,涵盖自然语言(如Dyna-Mind, LLM-MCTS)、结构化记录(如JSON、代码片段)等形式；另一条轴是**基础领域**,分为物理环境(如机器人控制)、数字环境(如网页、软件仓库)、社会环境(如用户对话)和抽象环境(如数学推理)。这两个维度交叉定义出不同的TWM变体。

在具体实现上,论文归纳出两大技术范式：**LLM-as-World-Model**,即通过提示(prompting)从冻结的LLM中激发转移预测能力；**Code-as-World-Model**,即将环境动态编码为可执行的程序逻辑。这些模型既可以在训练时通过生成合成经验来辅助学习,也可以推理时用于规划、验证和自适应,从而弥补LLM智能体对环境结构缺乏显式理解的“智能体-世界鸿沟”。

### Q4: 论文做了哪些实验？

根据您提供的论文信息，这篇论文是一篇关于文本世界模型（TWM）的综述，因此它本身并未进行新的实验。相反，该论文系统性地回顾和分析了现有研究中关于TWM的实验。论文的核心贡献在于提出了一个统一的框架和分类法，将已有工作按“构建、应用、评估”的生命周期以及“状态表示”和“基础领域”两个维度进行归类。

因此，针对“论文做了哪些实验”这一问题，答案是基于综述内容整合的现有实验范式，而非新实验。综述覆盖的实验设置主要包括：在环境建模中针对网页导航、代码编辑、工具使用和软件仓库等数字领域；在用户建模中针对对话历史中的偏好、意图和任务进展。对比方法通常涉及“LLM-as-WM”和“code-as-WM”两种范式，以及将TWM作为规划、验证和适应模块集成到现有LLM智能体框架中（如Dyna-Mind, LLM-MCTS, MINDSTORES）。主要结果体现在：TWM在训练阶段能通过经验合成提升样本效率，在推理阶段通过前瞻规划提升任务成功率，并支持对智能体行为的可解释评估。论文未提供统一实验的具体数值指标，其关键发现是指出TWM在多种交互场景下作为过渡预测模型的有效性，并强调了其与隐空间世界模型和通用语言模型的区别优势。

### Q5: 有什么可以进一步探索的点？

未来可围绕以下方向展开：当前TWM在环境建模的因果性和泛化性上存在局限，尤其在处理未见过的状态转移或跨领域迁移时表现不佳。可探索将符号化因果图或概率图模型与LLM结合，提升对长尾情境的系统推演能力。在构建阶段，现有“LLM即世界模型”与“代码即世界模型”范式在计算效率和状态覆盖完整性上存在两难，未来可研究混合架构，如利用神经符号方法将LLM的常识推理能力与程序化环境约束进行协同，降低模拟幻觉。在应用层面，当前TWM主要支持任务搜索和回溯验证，但缺乏对专家示范或基于价值的学习的利用，可结合离线强化学习或逆强化学习来自适应优化探索策略。此外，TWM作为评估环境时，其自身的模拟保真度和覆盖度缺乏标准化基准，未来需构建跨领域的多任务评估套件，并推动对模型幻觉的鲁棒性测试与可解释性研究。

### Q6: 总结一下论文的主要内容

这篇论文是首篇系统综述文本世界模型（TWM）的论文，旨在解决基于大语言模型的智能体在交互式文本环境中缺乏结构化环境模型的问题。TWM被定义为预测文本状态转换的模型，给定当前状态和动作，输出结果状态。论文构建了一个包含四个阶段的智能体生命周期框架：基础（形式化定义、状态表示与领域表征）、构建（将方法分为学习型、提示型和编程型三大范式）、应用（训练时用于经验合成，推理时用于规划、验证与适应）、评估（涵盖单步精度、多步一致性、行为保持与下游效用）。主要结论是，TWM能支持规划、高效学习和可解释评估，但面临状态开放词汇、动态依赖知识、正确性主观等挑战。该综述整合了Web、代码、工具和对话等碎片化领域的研究，为未来研究提供了统一的设计空间和分类体系。
