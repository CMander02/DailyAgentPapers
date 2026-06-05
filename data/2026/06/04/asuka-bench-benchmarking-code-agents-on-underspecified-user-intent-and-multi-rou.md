---
title: "Asuka-Bench: Benchmarking Code Agents on Underspecified User Intent and Multi-Round Refinement"
authors:
  - "Xin Wang"
  - "Liangtai Sun"
  - "Yaoming Zhu"
  - "Shuang Zhou"
  - "Jiaxing Liu"
  - "Fengjiao Chen"
  - "Lin Qiu"
  - "Xuezhi Cao"
  - "Xunliang Cai"
  - "Licheng Zhang"
  - "Zhendong Mao"
date: "2026-06-04"
arxiv_id: "2606.05920"
arxiv_url: "https://arxiv.org/abs/2606.05920"
pdf_url: "https://arxiv.org/pdf/2606.05920v1"
categories:
  - "cs.SE"
  - "cs.CL"
tags:
  - "Code Agent"
  - "Benchmark"
  - "Multi-Round Refinement"
  - "User Intent"
  - "Web Development"
relevance_score: 8.5
---

# Asuka-Bench: Benchmarking Code Agents on Underspecified User Intent and Multi-Round Refinement

## 原始摘要

Existing code-generation benchmarks score a single mapping from a complete prompt to a one-shot output. However, real web development is different. Users seldom write a full spec at the start; many requirements only become clear once they look at an intermediate result and react to it. We present Asuka-Bench, a benchmark that pairs underspecified user intent with multi-round refinement, grounded in browser-rendered behavior. Each task is resolved through a closed loop: a Code Agent generates a web project, a UI Agent executes test cases on the deployed site, and a User LLM turns evaluation outcomes into natural-language feedback for the next round. The benchmark comprises 50 web tasks with 784 evaluation criteria and 2402 expected outcomes. We benchmark 8 LLMs across 2 agent frameworks. The results separate models clearly: weighted Task Pass Rate varies by 38 percentage points and models also differ substantially in their ability to repair from feedback. Asuka-Bench is also far from saturated: even the strongest model completes only 52% of projects after three rounds.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

现有代码生成基准测试采用"完整提示→一次输出"的静态评估范式，输入为清晰明确的完整规范，仅评价单次生成结果。然而，真实web开发场景中用户很少一开始就写出完整需求规格，许多需求只有看到中间结果并通过交互反馈才能明确。这种范式忽视了开发过程中关键的迭代反馈机制，无法评估代码智能体利用运行时反馈进行渐进式改进的能力。本文提出Asuka-Bench，一个将未明确的用户意图与多轮迭代改进相结合的基准测试，基于浏览器渲染行为进行评估。每个任务通过闭环流程解决：代码智能体生成web项目，UI智能体在部署站点上执行测试用例，用户LLM将评估结果转化为自然语言反馈供下一轮改进。基准包括50个web任务、784项评估标准和2402个预期结果。实验表明，加权任务通过率在不同模型间差异达38个百分点，模型在利用反馈修复错误的能力上也存在显著差异，即使最强模型三轮后仅完成52%的项目，表明基准尚未饱和。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及三个类别的工作。第一类是代码生成基准测试，如HumanEval、MBPP等函数级基准，以及SWE-Bench、Web-Bench和WebMMMU等仓库级基准。这些基准均假设任务说明完整明确，要求模型一次生成正确输出，而Asuka-Bench聚焦于用户意图不明确且需多轮迭代的真实场景。第二类是迭代代码生成研究，利用自我或环境反馈进行改进，但Asuka-Bench的创新在于将改进过程基于模拟用户反馈，源自浏览器渲染行为。第三类是文本到网页生成基准，如FrontendBench和WebGen-Bench，它们使用单一、完全指定的指令进行一次性评估，而Asuka-Bench针对初始需求不明确且通过对话逐步明确意图的真实开发流程进行评测。本文与这些工作的核心区别在于：首次结合了不明确的用户意图与多轮细化反馈，并利用浏览器渲染行为进行闭环评估，更贴近真实世界的网络开发实践。

### Q3: 论文如何解决这个问题？

Asuka-Bench通过构建一个从模糊用户意图出发、经过多轮迭代精化的闭环评估框架来解决实际Web开发中的需求不明确问题。核心方法是“用户意图欠指定+迭代反馈修正”，框架由四部分组成：任务规范阶段，将用户模糊查询（如“创建一个购物网站”）与其内部使用的Clarified PRD（含层次化功能模块、容错规则及784条评估标准）分离，仅向代码Agent暴露初始模糊查询；代码Agent阶段，基于LLM和Agent框架，首先生成初始Web项目，并在后续轮次接收自然语言反馈修改代码；自动化评估阶段，一个UI Agent在浏览器中执行预定义的DAG化测试用例（含存在性、功能性和鲁棒性三类任务），按拓扑顺序运行，失败任务才会生成带自然语言解释的反馈；迭代精化阶段，User LLM汇总各条失败评估结果，综合为结构化自然语言反馈返回给代码Agent，重复该闭环直到所有标准满足或达最大轮次。关键技术包括：基于有向无环图（DAG）的依赖驱动态评估协议（跳过因上游失败导致的不可达任务，聚焦根因）、三源查询收集（线上用户数据/GitHub仓库/现有网站）确保多样性、以及模拟数据生成实现无后端纯前端执行。这种设计不仅衡量初始生成质量，更评测Agent从模糊反馈中修复错误的能力。

### Q4: 论文做了哪些实验？

论文对8个大语言模型（GPT-5.4、Gemini-3.1-Pro、Claude-4.6-Sonnet、GLM-5、Kimi-K2.6、Seed-2.0-Pro、MiniMax-M2.7、Qwen3.5-Plus）在两个智能体框架（OpenHands和Claude Code）下进行了评估。基准测试包含50个网页开发任务，涉及784条评估标准和2402个预期结果。实验设置最大3轮优化回合，UI智能体每任务最多100步浏览器交互，采用DAG感知协议和软满足阈值T=0.5。报告三个指标：项目完成率(PCR)、加权任务通过率(累计加权)、加权标准通过率(累计加权)。主要结果：13种(模型,框架)配置在3轮后的加权任务通过率范围为51.8%-90.1%，差距达38个百分点，且最高与最低的95%置信区间不重叠。最强配置的任务通过率约90%，但项目完成率仅46-52%，说明完整可用网页应用要求所有子任务通过。迭代反馈的增益主要来自第2轮(约25个绝对百分点)，第3轮增加7-13个百分点。饱和实验表明，将Claude-4.6-Sonnet扩展至8轮后，项目完成率和加权任务通过率均收敛至100%，确认所有任务可解且反馈机制持续有效。

### Q5: 有什么可以进一步探索的点？

根据论文的局限性和结论，未来探索点主要包括：1) 扩展领域覆盖，增加3D、实时协作和实时后端场景，这需要改造数据管道和部署工具链；2) 研究评估器依赖问题，可以尝试用不同的UI Agent和User LLM组合来验证结果的鲁棒性，并开发多标注者的自动化评估方案；3) 解决基准污染问题，构建动态任务池或引入对抗性生成技术定期更新测试集；4) 论文发现修复能力与首轮生成能力解耦，可深入探索是否需要专门训练反馈理解与迭代改进的模型模块，或者设计强化学习框架来优化多轮交互策略；5) 目前的基准仅3轮，可研究更长的迭代周期是否能进一步缩小性能差距，以及如何定义“收敛”标准；6) 结合人类反馈的主动学习机制，让Agent学会在模糊意图下主动提问而非被动等待反馈。

### Q6: 总结一下论文的主要内容

Asuka-Bench是一个评估代码智能体在未明确用户意图和多次迭代细化条件下能力的基准测试。该基准定义了一个闭环流程：代码智能体生成网页项目，UI智能体在部署网站上执行测试用例，用户大语言模型将评估结果转化为自然语言反馈以供下一轮使用。基准包含50个网页任务，784个评估标准和2402个预期结果。通过在两个智能体框架上评估8个大型语言模型，得出三个主要结论：意图模糊性会造成显著的性能差距，但三轮内的迭代反馈可以有效弥合；反馈修复能力与首轮生成质量在很大程度上是解耦的，揭示了现有单次基准无法测出的能力轴；基于有向无环图的评估协议提供了可靠的自动化判断。该基准远未饱和，最强模型在三轮后也仅完成52%的项目，表明现有模型仍有很大提升空间。Asuka-Bench推动代码生成评估从静态、单次向反映真实开发迭代本质的方向发展。
