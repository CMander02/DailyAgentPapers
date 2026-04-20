---
title: "Benchmarks for Trajectory Safety Evaluation and Diagnosis in OpenClaw and Codex: ATBench-Claw and ATBench-CodeX"
authors:
  - "Zhonghao Yang"
  - "Yu Li"
  - "Yanxu Zhu"
  - "Tianyi Zhou"
  - "Yuejin Xie"
  - "Haoyu Luo"
  - "Jing Shao"
  - "Xia Hu"
  - "Dongrui Liu"
date: "2026-04-16"
arxiv_id: "2604.14858"
arxiv_url: "https://arxiv.org/abs/2604.14858"
pdf_url: "https://arxiv.org/pdf/2604.14858v1"
categories:
  - "cs.AI"
  - "cs.SE"
tags:
  - "Agent Safety"
  - "Benchmark"
  - "Trajectory Evaluation"
  - "Tool Use"
  - "Code Agent"
  - "Risk Taxonomy"
  - "Diagnosis"
relevance_score: 7.5
---

# Benchmarks for Trajectory Safety Evaluation and Diagnosis in OpenClaw and Codex: ATBench-Claw and ATBench-CodeX

## 原始摘要

As agent systems move into increasingly diverse execution settings, trajectory-level safety evaluation and diagnosis require benchmarks that evolve with them. ATBench is a diverse and realistic agent trajectory benchmark for safety evaluation and diagnosis. This report presents ATBench-Claw and ATBench-CodeX, two domain-customized extensions that carry ATBench into the OpenClaw and OpenAI Codex / Codex-runtime settings. The key adaptation mechanism is to analyze each new setting, customize the three-dimensional Safety Taxonomy over risk source, failure mode, and real-world harm, and then use that customized taxonomy to define the benchmark specification consumed by the shared ATBench construction pipeline. This extensibility matters because agent frameworks remain relatively stable at the architectural level even as their concrete execution settings, tool ecosystems, and product capabilities evolve quickly. Concretely, ATBench-Claw targets OpenClaw-sensitive execution chains over tools, skills, sessions, and external actions, while ATBench-CodeX targets trajectories in the OpenAI Codex / Codex-runtime setting over repositories, shells, patches, dependencies, approvals, and runtime policy boundaries. Our emphasis therefore falls on taxonomy customization, domain-specific risk coverage, and benchmark design under a shared ATBench generation framework.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决随着智能体系统进入日益多样化的执行环境，其轨迹层面的安全性评估与诊断缺乏相应演进的基准测试工具的问题。研究背景是，当前智能体系统在保持高层架构相对稳定的同时，其具体的执行环境、工具生态和产品能力却在快速演变，这暴露出新的风险区域。现有的基准测试（如WebArena、OSWorld等）虽与特定执行环境绑定，但在轨迹安全性评估领域，缺乏一种能够灵活适应新环境、系统化覆盖新风险的基准构建方法。

现有方法的不足在于，大多数安全性基准是静态的，或仅针对特定固定场景设计，难以快速适配到如OpenClaw（涉及工具、技能、会话和外部服务链）或OpenAI Codex/Codex运行时（涉及代码仓库、shell、补丁、依赖与审批流程）这类新兴且风险模式迥异的执行环境中。这导致评估滞后于部署，无法有效诊断新环境下的具体安全失效模式与危害。

因此，本文要解决的核心问题是：如何构建一个可扩展的基准框架，使其能通过系统化的定制机制，快速生成适用于不同智能体执行环境的、面向轨迹安全评估与诊断的专用基准。具体而言，论文以ATBench为基础，通过分析新环境、定制涵盖风险来源、失效模式和现实危害的三维安全分类法，并利用共享的基准构建流水线，实例化了ATBench-Claw和ATBench-CodeX两个领域定制化扩展，从而验证其框架在覆盖领域特定风险、保持评估一致性方面的可行性与重要性。

### Q2: 有哪些相关研究？

本文的相关研究主要围绕智能体轨迹安全评估与诊断的基准测试展开，可分为方法类和应用类。

在方法类研究中，本文的核心基础是AgentDoG框架及其基准组件ATBench。AgentDoG是一个更广泛的护栏框架，专注于轨迹级智能体安全诊断，而ATBench则是其公开的基准测试组件，旨在为长视野智能体交互提供多样且真实的轨迹安全评估与诊断基准。本文的工作（ATBench-Claw和ATBench-CodeX）是ATBench的领域定制化扩展，而非一个全新的独立基准。其关键创新在于通过一个统一且可扩展的三维安全分类法（涵盖风险来源、故障模式和现实危害）作为控制支架，使基准能够适应新的执行环境，而无需重新设计整个数据生成流水线。

在应用类研究中，相关工作涉及特定领域的智能体系统安全评估。本文与这些工作的区别在于其系统化的扩展方法论。本文没有为OpenClaw或Codex环境从头创建孤立的基准，而是将ATBench框架定制化到这两个具体领域：ATBench-Claw针对OpenClaw环境中涉及工具、技能、会话和外部操作的执行链；ATBench-CodeX则针对OpenAI Codex/Codex-runtime环境中涉及代码仓库、shell、补丁、依赖、审批和运行时策略边界的轨迹。这种基于共享分类法和生成框架的扩展方式，使得在不同领域构建的基准保持了任务、诊断框架和数据生成引擎的共通性，从而支持跨领域的比较与分析。

### Q3: 论文如何解决这个问题？

论文通过一个名为ATBench的可扩展基准框架来解决不同智能体执行环境下的轨迹安全评估与诊断问题。其核心方法是基于一个统一的三维安全分类法，通过定制化该分类法来适配特定领域，并利用共享的数据生成引擎来构建具体的基准测试集。

整体框架由两个核心部分组成：一是统一的三维安全分类法，它定义了需要覆盖的智能体风险类型，涵盖了风险来源、故障模式和现实危害三个维度；二是数据生成引擎，它集成了基于分类法的风险采样、异构工具源、基于规划器的轨迹合成以及延迟触发的长上下文构建等技术。这两个部分紧密耦合：分类法规定了基准需要覆盖的风险范围，而数据生成引擎则根据这一规定生成具体的轨迹数据。

论文的创新点在于其可扩展性。面对快速演进的智能体执行环境（如OpenClaw和CodeX），论文并非为每个环境从头构建独立的基准，而是展示了如何通过定制化统一的三维分类法，将ATBench框架适配到新的领域。具体操作是：首先分析新执行环境（如OpenClaw的工具、技能、会话和外部服务，或CodeX的代码仓库、shell命令、补丁、依赖和MCP服务器），然后针对其特有的高风险区域（如OpenClaw中的状态执行、审批和跨工具协调，或CodeX中的仓库中心执行、破坏性变更和策略约束的运行时动作），对原有分类法进行定制化。这种定制化主要通过两种方式实现：1）在原有分类法未充分覆盖重要领域风险时引入新的类别；2）对继承的原有类别进行领域特定的操作化解释和强化。

主要模块/组件体现在两个定制化基准中：
*   **ATBench-Claw**：主要为OpenClaw环境引入了大量新的风险类别，以显式捕捉其特有的执行时风险，如身份模糊、会话状态污染、技能供应链攻击、审批绕过等。同时新增了“合规、法律与可审计性危害”这一危害类别。
*   **ATBench-CodeX**：则采用了混合策略，仅新增了少量类别（如仓库工件注入、依赖/MCP供应链攻击等），其重点在于对继承的原有类别（如提示注入、工具反馈、权限过高等）进行强化和重新解释，使其在仓库和运行时策略约束下具有特定含义。

尽管两个基准的分类法定制方式不同，但它们共享相同的底层ATBench数据生成引擎、轨迹级任务定义和诊断原语，从而保证了基准间的可比性。这种架构设计使得基准能够随着智能体执行环境的演变而灵活扩展，无需重构整个框架，实现了稳定架构与快速变化环境之间的解耦。

### Q4: 论文做了哪些实验？

实验设置方面，论文采用统一的评估框架对 ATBench-Claw 和 ATBench-CodeX 两个定制化基准进行联合分析。核心任务是轨迹级别的安全/不安全二分类。评估指标包括准确率（Acc）、F1 分数和召回率（Recall）。此外，研究利用细粒度安全分类法进行诊断性切片分析：针对每个基准中每个不安全的细分类别（叶子节点），计算模型在该类别的不安全轨迹上进行粗粒度安全判断的准确率，以定位分类难点。

使用的数据集/基准测试即为论文提出的 ATBench-Claw（针对 OpenClaw 环境）和 ATBench-CodeX（针对 OpenAI Codex/Codex-runtime 环境）。

对比方法涵盖三类模型：1) 专用防护模型，包括 Qwen3Guard-Gen-4B/8B、Llama-Guard-3-8B、Llama-Guard-4-12B 和 ShieldAgent；2) 开源通用指令微调模型，包括 Qwen3.5-4B/9B/397B-A17B、Llama-3.1-8B-Instruct 和 Llama-3.3-70B-Instruct；3) 基于 AgentDoG 框架的系统配置 AgentDoG-Qwen3-4B。

主要结果如下：在 ATBench-Claw 上，AgentDoG-Qwen3-4B 取得最佳性能，准确率 0.8720，F1 0.8958，召回率 0.9291。通用模型中 Qwen3.5-397B-A17B 表现最好（Acc 0.8380，F1 0.8648，Recall 0.8750），多数通用模型优于专用防护模型。在 ATBench-CodeX 上，整体指标普遍低于 ATBench-Claw，尤其是专用防护模型性能下降明显。AgentDoG-Qwen3-4B 依然领先（Acc 0.8220，F1 0.8379，Recall 0.9200）。Qwen3.5-397B-A17B 在通用模型中保持较好的准确率与 F1 平衡（Acc 0.7660，F1 0.7710）。细粒度诊断分析表明，两个基准的难度差异主要集中在与仓库原生执行、输出验证、依赖链危害等相关的分类叶子上，在这些长尾难点上，AgentDoG-Qwen3-4B 的优势尤为明显。

### Q5: 有什么可以进一步探索的点？

本文提出的ATBench框架及其在OpenClaw和Codex环境下的扩展，展示了通过定制化安全分类法来适配新领域的思路，但其局限性和未来探索方向仍值得深入。首先，当前工作主要关注特定执行链（如工具、技能、会话）和代码环境（如仓库、补丁、依赖）中的风险，但尚未覆盖更广泛的动态、开放世界场景（如多智能体协作、对抗性环境或持续学习中的安全演化）。其次，安全分类法的定制依赖人工分析新领域，这可能导致扩展效率较低，未来可探索自动化或半自动化的分类法生成方法，例如利用大语言模型对领域文档进行风险挖掘。此外，基准的评估目前侧重于轨迹层面的诊断，未来可结合实时监控与干预机制，构建“评估-诊断-修复”的闭环系统。最后，基准的多样性和真实性仍有提升空间，例如引入更多边缘案例或对抗性测试数据，以增强智能体在复杂、不可预测环境中的鲁棒性。这些方向将推动智能体安全评估向更自适应、全面和实用的方向发展。

### Q6: 总结一下论文的主要内容

该论文提出了ATBench-Claw和ATBench-CodeX两个新的基准测试，作为ATBench在特定领域的扩展，旨在对智能体轨迹进行安全评估与诊断。核心问题是随着智能体系统执行环境日益多样化，需要能随之演进的轨迹级安全评估基准。论文的方法论关键在于其可扩展性：针对每个新领域（如OpenClaw和OpenAI Codex/Codex-runtime环境），首先分析其特点，然后定制一个三维安全分类法（涵盖风险来源、失效模式和现实危害），再利用此定制化的分类法来定义基准规范，最后通过共享的ATBench构建流水线生成具体基准。ATBench-Claw专注于评估OpenClaw环境中涉及工具、技能、会话和外部动作的执行链安全；ATBench-CodeX则针对Codex环境中的仓库、shell、补丁、依赖、审批和运行时策略边界等场景的轨迹。主要结论是，这种基于可定制分类法的框架能有效适应不同且快速演进的智能体执行环境与工具生态，为领域特定的风险覆盖和基准设计提供了系统化方法，对推动智能体系统安全性的标准化评估具有重要意义。
