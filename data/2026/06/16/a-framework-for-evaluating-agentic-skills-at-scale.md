---
title: "A Framework for Evaluating Agentic Skills at Scale"
authors:
  - "Maksim Shaposhnikov"
  - "Nicolas Fortuin"
  - "Simon Stipcich"
  - "Maria I. Gorinova"
  - "Amy Heineike"
  - "Rob Willoughby"
date: "2026-06-16"
arxiv_id: "2606.17819"
arxiv_url: "https://arxiv.org/abs/2606.17819"
pdf_url: "https://arxiv.org/pdf/2606.17819v1"
categories:
  - "cs.SE"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Agent技能评估"
  - "Agent评测基准"
  - "多模型对比"
  - "指令遵循"
  - "开源评估数据集"
  - "技能效用分析"
relevance_score: 9.5
---

# A Framework for Evaluating Agentic Skills at Scale

## 原始摘要

Agent skills -- structured, reusable knowledge artifacts that augment LLM agent capabilities -- have been rapidly adopted in industry, yet their cross-domain impact and use across commercial and open-source models remain under-studied, and no reusable methodology exists for evaluating an individual skill. In this work, we present an evaluation framework that lets a skill author construct realistic tasks to rigorously assess the aspects of a skill that matter most to them, and that estimates skill utility by solving those tasks. Further, we apply our evaluation approach at scale to 500 real-world skills, generating 1,000 tasks derived from the skills' content, along with instruction-following and goal-completion scoring rubrics. Using these metrics, we evaluate how 19 agent-model configurations, both proprietary and open-source, perform on the tasks. Our results show that models vary widely in how closely they adhere to the instructions encoded in skills, leading to substantial differences in their performance gains. Furthermore, we show that access to a skill significantly changes model behavior compared to the no-skill setup, providing an essential mechanism for encoding opinionated workflows into LLM agents. We release our evaluation dataset to support future work on agent skills.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大规模评估AI Agent技能效果的问题。研究背景是，LLM驱动的Agent通过“技能”（即结构化的可复用知识工件，如工作流、API模式、编码规范等）来扩展能力，这些技能已在工业界广泛应用。然而，现有评估方法存在明显不足：大多数Agent基准测试关注通用任务解决、工具使用或编程能力，并未专门评估技能如何改变Agent行为；少数涉及技能评估的工作依赖小规模、手工编写的固定任务集，领域覆盖有限，无法推广到社区注册表中多样化的真实世界技能。最关键的是，这些基准只针对自身固定任务集评分，无法回答技能作者面临的核心实践问题：给定一个新创建的技能，如何判断它是否真正改进了Agent在目标任务上的表现？具体而言，需要评估Agent是否遵循技能中的指令、技能是否提供了模型本身不具备的知识或工作流、技能是否提升了任务完成度，以及能否让小模型借助技能达到大模型的性能。因此，本文提出了一个可扩展的评估框架，能够自动生成与技能相关的真实任务和评分细则，从而量化技能对Agent行为的影响，填补了现有方法中无法按需评估单个技能的空白。

### Q2: 有哪些相关研究？

本文相关工作分为三类：1）**LLM智能体评测基准**，如AgentBench、WebArena、SWE-bench等，主要评测智能体在固定环境中的整体能力；本文不同在于提出**可复用评测方法**，允许技能作者自行构造任务和评分规则，而非依赖预定义基准。2）**智能体增强方法**，包括ReAct、ToT等推理框架，以及工具使用、函数调用、MCP等知识注入方式；本文聚焦于**技能（skill）**这类结构化可重用知识工件，研究其跨模型、跨域的影响，而非通用推理策略。3）**技能驱动的性能测量**，已有工作如OpenHands、LangChain评估技能效果，但多限于特定模型或领域；本文在**19种模型配置（商业+开源）**上对500个真实技能生成1000个任务，系统比较分数，发现技能显著改变模型行为，且模型对技能指令遵循度差异巨大。本文创新在于提供**端到端评测框架**，兼容量化任务达成与指令遵循双维度，并发布大规模评测数据集供后续研究。

### Q3: 论文如何解决这个问题？

该论文提出一个可扩展的智能体技能评估框架，核心方法是通过自动化流水线将技能转化为可执行的评估任务。整体框架包含四个主要模块：环境工程代理分析技能依赖（如CLI工具、API密钥、运行时环境等），任务生成代理根据技能内容或用户意图生成多样化任务提案并配备输入文件和环境，验证代理检查任务的可执行性、一致性和评分标准泄露问题，最后求解代理在有无技能两种条件下执行任务并交由LLM裁判评分。关键技术包括：自动生成两套评分标准（任务完成度和指令遵循度），每套100分，用于衡量技能对模型行为的影响；采用混合模式支持人工审查中间结果以保证任务质量；通过大规模实验（500个技能生成1000个任务，评估19个模型配置）验证框架有效性。创新点在于：首次提出可复用的技能评估方法论，能独立评估单个技能效用；设计带技能/无技能的对照实验分离技能影响；构建公开评估数据集支持后续研究。框架特别关注环境依赖分类和自动满足，并利用技能内容推断其实际使用场景，解决了真实用户输入难以获取的问题。

### Q4: 论文做了哪些实验？

论文在"with-skill"和"without-skill"两种条件下，使用19个 agent-模型配置（包括Anthropic、OpenAI、Google、DeepSeek、Kimi、GLM、Nemotron、MiniMax、Qwen等商业和开源模型）在500个真实技能上生成了1000个任务。使用指令遵循和任务完成两个评分标准，主要结果包括：（1）技能访问使所有模型的指令遵循分数和总体分数获得显著提升，相对提升范围为5.5-22分，其中Haiku 4.5提升19.7分、Sonnet 4.6提升22.1分；（2）不同模型受益程度差异大，Nemotron系列仅提升5.5-8.2分，Kimi K2.6仅提升7.1分；（3）技能使小模型接近大模型性能，如GPT-5.4 nano（81.9分）接近GPT-5.4（88.2分），GLM 5.1（91.1分）匹配Sonnet 4.6（91.5分）；（4）按技能领域分析，Media & File Processing领域提升最大（+38.1分），Testing, QA & Code Quality提升最小（+16.7分）；（5）对hf-cli技能的具体分析显示，技能将huggingface-cli使用降低为0，全部替换为hf命令。

### Q5: 有什么可以进一步探索的点？

从论文的讨论和局限性来看，未来探索方向主要包括：第一，研究技能选择机制，当前假设技能相关性对代理透明，实际部署中技能库的自动筛选能力需独立评估，可设计动态选择策略并分析其与任务绩效的关联；第二，解决LLM评判偏差，依赖单一评判模型（Sonnet 4.6）可能导致审美或风格性评分不公，可引入多评判模型集成、人类反馈微调或对评判标准进行对抗性校验；第三，拓展评估域覆盖，当前偏重软件工程场景，未来需将框架应用于医疗、法律、金融等技能稀疏领域，验证跨域泛化性；第四，处理依赖复杂环境的技能（如数据库、MCP服务器、多轮交互），可通过仿真环境抽象、状态压缩或部分可观测马尔可夫过程建模来降低重现成本；第五，长期方向是构建技能效用与成本（token/延迟/API费用）的联合优化函数，为生产环境中模型选择提供可操作的帕累托边界。

### Q6: 总结一下论文的主要内容

该论文提出了一个可扩展的智能体技能评估框架，解决了现有基准无法评估任意新技能实用性的问题。核心方法是从真实技能内容自动生成相关任务及指令遵循、目标完成评分标准，实现个体技能效果评估、多模型横向对比及技能弱点定位。在500个真实技能上生成约1000个任务，对19种模型配置（含闭源与开源）的实验表明：不同模型对技能指令的遵循程度差异显著，且技能访问权相比无技能设置能本质改变模型行为（尤其对编码工作流的一致性）。主要结论是技能可为小模型提供等效于大模型的能力，且框架能量化技能边际价值。该工作首次为技能作者提供了诊断技能弱点的工具，释放的评估数据集为后续研究奠定基础。
