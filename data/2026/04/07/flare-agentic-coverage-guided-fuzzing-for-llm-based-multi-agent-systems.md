---
title: "FLARE: Agentic Coverage-Guided Fuzzing for LLM-Based Multi-Agent Systems"
authors:
  - "Mingxuan Hui"
  - "Xinyue Li"
  - "Lu Wang"
  - "Chengcheng Wan"
  - "Yifan Wang"
  - "Yimian Wang"
  - "Feiyue Song"
  - "Beining Shi"
  - "Yixi Li"
  - "Yaxiao Li"
date: "2026-04-07"
arxiv_id: "2604.05289"
arxiv_url: "https://arxiv.org/abs/2604.05289"
pdf_url: "https://arxiv.org/pdf/2604.05289v1"
categories:
  - "cs.SE"
tags:
  - "多智能体系统"
  - "测试与验证"
  - "鲁棒性与安全"
  - "工具使用"
  - "软件工程"
relevance_score: 7.5
---

# FLARE: Agentic Coverage-Guided Fuzzing for LLM-Based Multi-Agent Systems

## 原始摘要

Multi-Agent LLM Systems (MAS) have been adopted to automate complex human workflows by breaking down tasks into subtasks. However, due to the non-deterministic behavior of LLM agents and the intricate interactions between agents, MAS applications frequently encounter failures, including infinite loops and failed tool invocations. Traditional software testing techniques are ineffective in detecting such failures due to the lack of LLM agent specification, the large behavioral space of MAS, and semantic-based correctness judgment.
  This paper presents FLARE, a novel testing framework tailored for MAS. FLARE takes the source code of MAS as input and extracts specifications and behavioral spaces from agent definitions. Based on these specifications, FLARE builds test oracles and conducts coverage-guided fuzzing to expose failures. It then analyzes execution logs to judge whether each test has passed and generates failure reports. Our evaluation on 16 diverse open-source applications demonstrates that FLARE achieves 96.9% inter-agent coverage and 91.1% intra-agent coverage, outperforming baselines by 9.5% and 1.0%. FLARE also uncovers 56 previously unknown failures unique to MAS.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的多智能体系统（MAS）中存在的测试难题。研究背景是，MAS通过将复杂任务分解为子任务并由多个智能体协作执行，已广泛应用于自动化复杂工作流。然而，由于LLM智能体行为的非确定性以及智能体间交互的复杂性，MAS应用经常出现故障（如无限循环、工具调用失败），且现有方法难以有效检测。

现有方法的不足主要体现在三个方面：首先，缺乏对LLM智能体的形式化规约（Specification）。传统软件测试依赖明确的规约来定义预期行为，但MAS的智能体规约（如预期行为、交互规则）通常以非正式的文本形式分散在提示词、代码注释等各处，导致难以获得精确、机器可读的完整规约。现有针对非AI软件或传统AI软件的规约提取方法（如基于代码断言或手动枚举任务）无法适用于输出开放、支持上下文学习的LLM智能体。其次，MAS的行为空间（Behavioral Space）极其庞大且隐含。智能体的行为由提示词和外部工具调用隐式定义，智能体间的交互又进一步扩大了状态空间，其生成性和高层行为（如自我规划）使得难以静态建模所有可能动作。现有针对特定领域（如GUI应用）的行为空间建模方法无法直接应用于MAS。最后，正确性判断（Correctness Judgment）需要基于语义。MAS的故障多为非致命性功能错误，判断测试是否通过需关注功能语义和令牌传递的信息，而传统基于控制流或数据流覆盖率的判断方法无法反映智能体的实际功能。

因此，本文要解决的核心问题是：如何为基于LLM的多智能体系统构建一个有效的功能性测试框架，以自动提取其规约与行为空间，并基于覆盖引导的模糊测试（Fuzzing）及语义分析来暴露系统中的特定故障。论文提出的FLARE框架正是为了系统性地应对上述三大挑战。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**多智能体系统（MAS）开发框架**、**基于LLM的软件测试方法**以及**传统软件测试技术**。

在**MAS开发框架**方面，已有多个开源项目（如Microsoft AutoGen、CrewAI、Camel、Praison）提供了高级模块化抽象，方便开发者集成工具、管理记忆和定义交互拓扑。本文研究的MAS应用正是基于此类框架构建，但本文重点并非开发新框架，而是针对这些框架所构建系统的**可靠性测试**。

在**基于LLM的软件测试**领域，已有工作关注提示测试、越狱攻击或单智能体系统的评估。然而，这些方法通常**未专门针对MAS中智能体间复杂的交互模式和非确定性行为**进行设计。本文提出的FLARE框架则专门针对MAS，通过从智能体定义中提取规范和行为空间，构建测试预言并进行覆盖引导的模糊测试，以暴露MAS特有的故障（如无限循环、工具调用失败）。

在**传统软件测试技术**方面，如模糊测试（Fuzzing）和覆盖引导测试，虽在传统软件中有效，但**难以直接应用于MAS**。原因在于MAS缺乏明确的智能体规范、行为空间巨大，且正确性判断往往依赖于语义。FLARE的创新之处在于，它**适配了覆盖引导的模糊测试思想，使其能处理MAS的独特挑战**，例如从自然语言描述中推导出可测试的规范，并针对智能体内（intra-agent）和智能体间（inter-agent）的覆盖进行优化。

### Q3: 论文如何解决这个问题？

FLARE 通过一个三阶段的覆盖引导模糊测试框架来解决多智能体系统（MAS）测试难题。其核心思想是从MAS源代码中自动提取行为规范、构建行为空间，并以此为基础驱动智能化的测试生成与失败识别。

**整体框架与主要模块**：
框架包含三个阶段：1) **软件分析**：通过两个智能体模块处理SUT源代码和领域知识。**规范智能体** 利用思维链技术，从系统提示词、配置属性等中提取四类行为规范：智能体关系、系统终止模式、任务执行和工具调用。**空间智能体** 则构建两个互补的行为空间抽象：**智能体内行为空间**（通过解析提示模板和工具描述，将任务拆分为原子单元，并纳入三类异常行为）和**执行路径空间**（根据通信模式枚举所有有效的智能体交互序列）。2) **模糊测试循环**：采用覆盖引导的反馈机制。它初始化一个种子池，包含由辅助LLM生成的任务描述。通过**加权随机选择策略**动态选择种子，并应用**变异器**对种子进行突变，主要针对模型配置和智能体执行顺序，而保持系统输入不变以确保规范有效性。测试执行后，系统计算**智能体内覆盖**和**智能体间覆盖**指标，并将能提升覆盖率的种子优先加入后续测试。3) **失败识别**：基于提取的规范构建测试预言。采用**双智能体验证机制**：失败智能体首先扫描执行日志中潜在的规范违反，随后法官智能体进行二次审查以验证其有效性，从而减轻LLM幻觉导致的误报，最终生成失败报告。

**关键技术**：
1.  **基于规范与空间提取的测试基础构建**：创新性地从代码中自动推导出形式化的行为规范和行为空间，为测试提供了语义基础和覆盖分母。
2.  **覆盖引导的MAS特异性模糊测试**：设计了针对MAS特点的种子选择、突变策略和覆盖度量（区分智能体内和智能体间行为），引导测试探索复杂的状态空间。
3.  **双智能体验证机制**：在失败识别环节引入两级审查，显著提高了报告的可信度，有效应对了LLM输出不确定性的挑战。

总之，FLARE通过将传统的覆盖引导模糊测试与针对LLM智能体系统的自动化规范提取、空间建模及语义验证相结合，系统化地解决了MAS测试中缺乏规范、行为空间巨大和语义判断困难的核心挑战。

### Q4: 论文做了哪些实验？

论文在评估部分围绕三个研究问题设计了实验。实验设置以AutoGen这一主流多智能体框架为平台，构建了一个包含16个开源应用的基准测试集。这些应用通过GitHub搜索筛选，涵盖代码生成、视频制作、数据分析等多样化任务场景，代码规模在80至550行之间，具有代表性。对比方法包括三类基线：针对LLM安全的LLM-Fuzzer（通过种子选择与突变生成多样化初始查询）、传统覆盖引导模糊测试工具PythonFuzzer（基于AFL逻辑，进行字节级随机突变以最大化代码覆盖），以及另一传统覆盖测试工具（未在提供章节详述）。主要结果显示，FLARE在智能体间覆盖率达到96.9%，智能体内覆盖率达到91.1%，分别超出基线方法9.5%和1.0%。此外，FLARE成功发现了56个此前未知的、MAS特有的逻辑故障，证明了其在理解和触发深层智能体交互语义方面的有效性。

### Q5: 有什么可以进一步探索的点？

该论文提出的FLARE框架在基于覆盖引导的模糊测试方面取得了显著成效，但其局限性和未来探索方向仍值得深入。首先，当前方法严重依赖从代理定义中提取的显式规范，对于隐式、动态或上下文相关的交互逻辑可能捕捉不足。未来可探索结合运行时行为学习或形式化方法，以更全面地建模代理意图与约束。其次，测试预言（oracle）的构建仍基于相对简单的规则（如无限循环检测），对于更复杂的语义错误（如逻辑矛盾或目标偏离）识别能力有限。可引入神经符号方法，将LLM的语义理解与符号推理结合，实现更细粒度的正确性判断。此外，评估主要针对开源应用，在复杂商业场景中的泛化能力有待验证。未来可研究自适应模糊策略，根据系统反馈动态调整测试输入与代理调度。最后，当前工作侧重于失败检测，未能提供自动修复建议。结合因果分析与程序合成技术，实现从“测试”到“修复”的闭环，将是提升多智能体系统可靠性的关键方向。

### Q6: 总结一下论文的主要内容

该论文提出了FLARE框架，旨在解决基于大语言模型的多智能体系统（MAS）中因智能体行为不确定性和复杂交互而频繁出现的故障问题。传统软件测试方法因缺乏智能体规范、行为空间庞大以及语义正确性判断困难而难以有效检测此类故障。

FLARE的核心贡献在于首次为MAS设计了一个覆盖引导的模糊测试框架。其方法首先从MAS源代码中提取智能体规范和行为空间，并据此构建测试预言。随后，框架通过覆盖引导的模糊测试主动生成测试用例以暴露故障（如无限循环和工具调用失败），并分析执行日志进行结果判定与报告生成。

实验评估表明，FLARE在16个开源应用上实现了96.9%的智能体间覆盖率和91.1%的智能体内覆盖率，显著优于基线方法，并成功发现了56个此前未知的MAS特有故障。这项工作为MAS的可靠性保障提供了自动化、高效的新工具，对推动复杂AI系统的实际部署具有重要意义。
