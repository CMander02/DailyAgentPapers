---
title: "TeleSWEBench: A Commit-Driven Benchmark for Evaluating LLM-Powered Software Engineering in Telecommunications"
authors:
  - "Pranshav Gajjar"
  - "Ali Mamaghani"
  - "Dinesh Bharadia"
  - "Vijay K Shah"
date: "2026-06-03"
arxiv_id: "2606.05001"
arxiv_url: "https://arxiv.org/abs/2606.05001"
pdf_url: "https://arxiv.org/pdf/2606.05001v1"
categories:
  - "cs.SE"
tags:
  - "LLM驱动的SWE Agent"
  - "代码基准测试"
  - "领域特定Agent评估"
  - "5G/电信领域"
  - "LLM作为评判者"
relevance_score: 8.5
---

# TeleSWEBench: A Commit-Driven Benchmark for Evaluating LLM-Powered Software Engineering in Telecommunications

## 原始摘要

With the telecommunications field embracing zero touch management alongside novel O-RAN and AI-RAN frameworks, contemporary telecom networks now function as immensely intricate and heavily softwareized codebases. While automated software engineering (ASE) tools and Software Engineering (SWE) Agents hold the potential to alleviate the critical code generation bottleneck in this domain, their ability to navigate and modify specialized, mathematically rigorous wireless stacks like srsRAN 5G remains unverified. General-purpose coding benchmarks fail to capture the stateful logic and strict requirements of telecommunications, leaving a critical evaluation gap. In this paper, we introduce TeleSWEBench, the first commit-driven benchmark specifically designed to measure an agent's performance in the telecom domain. We mine real developer commits from the srsRAN 5G repository and distill them into structured test cases across three difficulty tiers (Easy, Medium, and Difficult). Our benchmark consists of 734 questions that are accompanied by executable unit tests. To avoid the rigidity of test cases, we further propose a hierarchical LLM as a Judge framework called TeleJudge that scores agent outputs at the file level and aggregates verdicts holistically. This follows an evaluation based on context and semantic similarity in parallel to a standard unit test-based evaluation. Using this benchmark, we evaluate AIDER, OpenHands, and the ClaudeCode frameworks, powered by state-of-the-art reasoning LLMs, including Qwen3, GPT OSS, Gemma 4, Kimi, and Qwencoder 2.5. Our two-stage evaluation reveals that models suffer from a lack of both localization accuracy and functional correctness, with the strongest ASE tools achieving up to 25% of shippable changes.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在电信软件工程领域缺乏专门评估框架的问题。随着电信行业向零接触管理和O-RAN、AI-RAN等新架构演进，现代电信网络成为高度复杂且软化的代码库。虽然自动化软件工程工具和SWE Agent有潜力缓解该领域的代码生成瓶颈，但它们在处理专业化、数学严谨的无线协议栈（如srsRAN 5G）方面的能力尚未得到验证。现有通用编码基准（如SWE Bench、MBPP和HumanEval）主要评估通用开发任务，未能捕捉电信领域特有的有状态逻辑、严格的异步时序要求、复杂状态机管理和对3GPP标准的刚性遵守，形成了关键的评估鸿沟。因此，本文提出TeleSWEBench，这是首个专门针对电信领域设计的提交驱动基准，通过从开源srsRAN 5G代码库中挖掘真实开发者提交，将其转化为三个难度等级的734个可执行单元测试问题，并引入分层LLM作为评判框架TeleJudge进行文件级别评估，以填补现有评估方法的空白。

### Q2: 有哪些相关研究？

相关研究可分为三类。首先是通用软件工程评估基准，如HumanEval（单函数生成）、SWE-bench（多文件GitHub问题修复）及其验证集SWE-Bench-Verified，还有RepoBench和ExecRepoBench等仓库级代码补全与执行评估。这些基准广泛使用Python/Java，缺乏电信领域硬件关联、状态化且数学复杂的C++范式，而本文专为电信域设计，填补了这一空白。其次是电信领域评估框架，如ORANBench、TeleQnA和GSMA套件，均基于多选问答（MCQA）测试模型对3GPP文档的理解与摘要能力；srsRANBench虽聚焦代码库理解，但仅限于静态代码理解，无端到端代码生成评估。本文TeleSWEBench是首个面向电信的提交驱动基准，评估代理在多文件修改和跨层编译上的表现。第三是领域适配模型，如TelecomGPT和ORANSight，后者将srsRAN代码纳入预训练，但仅测试代码理解或单函数生成。本文则通过734个附带单元测试的问题及TeleJudge分层评估框架，系统衡量代理在电信软件工程中的定位准确性和功能正确性。

### Q3: 论文如何解决这个问题？

为了解决TeleSWEBench中评估LLM在电信软件工程领域表现的问题，论文设计了一套从基准构建到两阶段评估的完整方法。核心方法包括：**基于真实开发者提交（commit）的基准构建**、**三级难度任务分类**、以及**两阶段评估与分级裁判机制**。

**整体框架**分为基准创建和评估两大部分。基准创建阶段，从srsRAN 5G开源仓库挖掘2023-2025年间的15k+个提交，平均每个提交修改5.57个文件，体现了电信软件的高耦合性。从这些提交中提炼出734个附带可执行单元测试的问题，并按难度分为Easy、Medium、Difficult三级：Easy任务给出精确文件路径和行级编辑指令；Medium任务说明改动原因和涉及文件但省略精确行级编辑；Difficult任务仅提供高层目标和最少提示，要求模型自主定位和规划修改。

**关键技术**包括：1）**层级生成与验证流水线**：生成时按难度顺序（Difficult→Medium→Easy），仅当高难度任务生成成功后才尝试下一难度，并采用模型级联（从小模型到大模型）以控制成本。验证阶段使用LLM检查问题是否无歧义、信息密度匹配难度、忠实于原始提交，并以0.9的信度阈值过滤。2）**两阶段评估**：第一阶段评估**定位准确性**，将模型修改的文件集与真实文件集对比，分为完全匹配、部分匹配、过度修改、无匹配、无修改五类。第二阶段仅对完全匹配的候选方案评估**功能正确性**，通过编译执行单元测试套件进行测试。为避免刚性单元测试惩罚正确但结构不同的方案，提出**TeleJudge**框架，先逐文件评估差异，再聚合为整体普适评价。两个评估集分别为1500题的扩展集和140题的验证集。

### Q4: 论文做了哪些实验？

实验基于srsRAN 5G仓库的734个真实commit任务，分为Easy、Medium、Difficult三级，并配有可执行单元测试。实验用AIDER框架评估Qwen3、Qwen3-small、Kimi-K2.5、Gemma4、GPT-OSS、QwenCoder-2.5、GLM-4.7等模型，并替换OpenHands和ClaudeCode框架进行消融。实验分两阶段：阶段一测量文件定位准确率（Exact Match, EM），阶段二在EM子集上评估代码生成，指标包括单元测试接受率（UAR）、TeleJudge语义接受率（TAR）和端到端可交付率（SRP）。主要结果：QwenCoder-2.5在Easy任务中EM达37.8%，但Difficult任务EM跌至5.3%；GLM-4.7因过度谨慎NC率达92.2%，但SRP达25.0%为最高；QwenCoder-2.5虽UAR达57.7%，TAR为0%，SRP为0%；框架对比中，ClaudeCode比AIDER表现更优。整体最强模型SRP仅25%，揭示电信领域的巨大挑战。

### Q5: 有什么可以进一步探索的点？

基于TeleSWEBench的研究，未来可从以下几个方面深入探索：

1. **基准扩展与泛化性**：当前仅基于srsRAN 5G单一项目，未来可引入更多电信开源项目（如O-RAN、OpenAirInterface）和网络协议栈，增强领域覆盖度和任务多样性。同时应考虑跨运营商、跨版本的代码变更场景。

2. **评估框架优化**：TeleJudge虽缓解了测试用例刚性，但语义相似度评判仍依赖LLM判断力，可能引入偏差。可探索结合静态分析工具、形式化验证或仿真环境的混合评估策略，提升评分客观性。

3. **代理能力提升**：当前最佳代理仅达25%可交付率，主要瓶颈在定位准确性与功能正确性。可研究**多层级上下文检索**（如结合AST解析与符号表）、**增量式验证**（边修边测）、或**领域知识注入**（如协议规范嵌入）来增强代理对电信领域状态逻辑的理解。

4. **动态难度机制**：现有三档难度为静态划分，未来可设计自适应难度调整机制，根据代理历史表现动态生成中间难度任务，更精细刻画能力边界。

总体而言，TeleSWEBench为领域评估奠定基础，但向实际工程化应用仍需在泛化性、评估客观性及代理智能上取得突破。

### Q6: 总结一下论文的主要内容

TeleSWEBench是首个专门评估大语言模型驱动的软件工程智能体在电信领域性能的基准测试。针对通用编程基准无法捕捉5G网络栈状态逻辑和严格约束的问题，论文通过挖掘srsRAN 5G仓库的真实开发者提交记录，构建了734个包含可执行单元测试的结构化问题，并按难度分为三个层级。方法上，论文提出两阶段评估流程，分别解耦智能体的仓库定位能力与逻辑正确性，同时设计了层级化LLM评判框架TeleJudge，基于上下文和语义相似性对多文件补丁进行评分。实验评估了AIDER、OpenHands和ClaudeCode框架搭配的先进推理模型，结果显示最强工具的可交付修改成功率仅达25%，揭示了模型在定位准确性和功能正确性上的显著不足。该基准为发展电信原生的软件工程智能体提供了关键评估基础。
