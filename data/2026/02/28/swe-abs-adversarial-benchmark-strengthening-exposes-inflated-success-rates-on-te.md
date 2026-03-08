---
title: "SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark"
authors:
  - "Boxi Yu"
  - "Yang Cao"
  - "Yuzhong Zhang"
  - "Liting Lin"
  - "Junjielong Xu"
date: "2026-02-28"
arxiv_id: "2603.00520"
arxiv_url: "https://arxiv.org/abs/2603.00520"
pdf_url: "https://arxiv.org/pdf/2603.00520v1"
categories:
  - "cs.SE"
tags:
  - "Code & Software Engineering"
relevance_score: 8.0
taxonomy:
  capability:
    - "Code & Software Engineering"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "SWE-ABS (Adversarial Benchmark Strengthening), coverage-driven augmentation, mutation-driven adversarial testing"
  primary_benchmark: "SWE-Bench Verified"
---

# SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark

## 原始摘要

The SWE-Bench Verified leaderboard is approaching saturation, with the top system achieving 78.80%. However, we show that this performance is inflated. Our re-evaluation reveals that one in five "solved" patches from the top-30 agents are semantically incorrect, passing only because weak test suites fail to expose their errors. We present SWE-ABS, an adversarial framework that strengthens test suites through a two-stage pipeline: (1) coverage-driven augmentation using program slicing to target untested code regions, and (2) mutation-driven adversarial testing that synthesizes plausible but incorrect patches to expose semantic blind spots. On SWE-Bench Verified (500 instances), SWE-ABS strengthens 50.2% of instances, a 25.1x improvement over prior work, and rejects 19.71% of previously passing patches. As a result, the top agent's score decreases from 78.80% to 62.20%, leading to significant leaderboard reshuffling, with the previous top-ranked agent dropping to fifth place.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在揭示并解决当前基于测试的AI代码生成基准评测中存在的一个关键问题：由于测试用例的判别力不足，导致大量语义错误的代码补丁被误判为“通过”，从而严重夸大了AI智能体（尤其是基于大语言模型的软件工程智能体）的实际性能表现，并可能误导对技术进展的评估。

研究背景是，以SWE-Bench为代表的代码生成基准测试被广泛用于评估和比较AI编程智能体的能力，其排行榜成绩被视为衡量进展的重要指标。例如，SWE-Bench Verified榜单的顶级系统声称达到了78.80%的解决率，接近“饱和”，这暗示了AI能力的成熟。然而，现有方法（即基准测试中自带的原始测试套件）存在根本性不足。这些测试套件通常直接来源于真实项目的拉取请求（PR），其设计初衷是验证特定补丁是否符合要求，而非用于区分所有潜在的正确与错误解决方案。这导致了两个系统性弱点：一是**覆盖范围缺口**，即测试未能覆盖补丁影响到的所有代码区域；二是**语义盲点**，即测试仅验证了表面行为，未能触及深层的语义约束（例如，要求环境变量必须是字符串类型）。这些弱点使得许多看似合理、能通过原始测试但实际语义错误的补丁得以蒙混过关。

本文要解决的核心问题正是这种“评测危机”。作者指出，现有基准测试的判别力严重不足，使得排行榜成绩虚高，无法真实反映AI智能体的代码生成质量。为此，论文提出了SWE-ABS框架，其核心目标是通过对抗性方法**强化基准测试套件**，主动暴露并修补测试中的弱点，从而提供一个更严格、更可靠的评估环境，挤掉性能“水分”，还原AI智能体的真实能力排名。这项工作不仅旨在纠正当前SWE-Bench榜单的虚高现象，更对如何构建具有高判别力的AI评测基准提出了方法论上的重要贡献。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：代码生成评测基准、测试增强方法和变异测试。

在**代码生成评测基准**方面，研究从HumanEval、MBPP等函数级基准，演进到SWE-Bench及其系列变体（如SWE-Bench Verified、SWE-Bench Pro）。这些基准聚焦于仓库级任务，并逐步提升了测试有效性、语言覆盖度和任务难度。然而，本文指出，所有这些变体都依赖为验证特定补丁而设计的测试套件，而非用于区分不同解决方案，因此存在覆盖空白和语义盲点，导致错误补丁也能通过测试。本文选取SWE-Bench Verified和SWE-Bench Pro作为评估基准，以检验所提方法在成熟和多语言场景下的效果。

在**测试增强**方面，相关工作旨在解决测试套件不足导致错误补丁通过的问题。例如，EvalPlus通过在HumanEval和MBPP上大量增加测试来暴露问题；UTBoost则专门针对SWE-Bench进行测试增强，发现了大量此前未检测出的错误补丁。本文认为，这些方法在生成测试时未能显式分析补丁相关代码区域或针对语义正确性，因此难以系统性地同时暴露覆盖空白和语义盲点。本文提出的SWE-ABS框架通过两阶段流程（覆盖驱动增强和变异驱动的对抗测试）直接针对这些弱点，实现了比UTBoost高25.1倍的实例增强率。

在**变异测试**方面，传统方法使用语法操作符（如替换运算符）引入人工故障以评估测试质量。近期研究开始利用LLM生成更真实的变异体。本文的SWE-ABS扩展了这一范式，它利用LLM合成代表“看似合理但实际错误”的语义变异（即能通过现有测试但违反实际需求的补丁），并据此生成测试来暴露这些语义盲点，从而更系统地评估和强化测试套件。

### Q3: 论文如何解决这个问题？

论文通过一个名为SWE-ABS的两阶段对抗性强化框架来解决测试套件不足导致性能评估虚高的问题。该框架的核心目标是增强现有测试套件，使其不仅能检测代码覆盖的缺失，还能暴露语义层面的盲点，从而更准确地评估补丁的正确性。

整体框架分为两个主要阶段。第一阶段针对覆盖缺口，通过程序切片识别与补丁相关的代码区域，并生成测试以覆盖这些区域。具体步骤包括：1）初始测试生成：利用大语言模型（LLM）根据问题描述、黄金补丁和现有测试生成多样化的初始测试；2）测试解耦：通过LLM检测并修正那些过度依赖黄金补丁具体实现的测试，避免其排斥其他正确实现；3）程序切片：构建程序依赖图，计算补丁相关代码行，捕获数据和控制依赖；4）覆盖引导增强：使用代码覆盖工具分析未覆盖的补丁相关行，并提示LLM生成针对这些行的测试，最终得到覆盖增强的测试套件 \( T_{cov} \)。

第二阶段针对语义盲点，通过突变驱动的对抗测试来强化测试套件。该阶段首先生成突变补丁：利用LLM基于黄金补丁合成看似合理但语义错误的突变补丁，并通过过滤模块（基于多LLM多数投票）确保突变与问题相关且语义不等价。接着，利用这些突变补丁暴露测试套件的弱点：将能通过当前测试的非等价突变归类为假阳性（揭示语义盲点），而将未能通过的等价突变归类为假阴性（表明测试过于严格）。针对假阴性，使用LLM修复过度严格的测试，使其泛化；针对假阳性，使用LLM生成新的对抗性测试来拒绝错误补丁。最终，通过替换修复的测试并添加新测试，构建出增强的测试套件 \( T_{aug} \)。

该方法的创新点在于：1）将覆盖驱动和突变驱动的对抗性测试相结合，系统性应对测试不足的两大根源；2）引入程序切片精准定位补丁相关代码，提升测试生成的针对性；3）利用LLM进行测试解耦、突变生成和修复，实现自动化强化；4）通过多LLM过滤确保突变的相关性和语义差异性，提高对抗测试的有效性。实验表明，SWE-ABS能显著增强测试套件，降低性能虚高，导致排行榜重排。

### Q4: 论文做了哪些实验？

论文在SWE-Bench Verified（500个Python实例）和SWE-Bench Pro（多语言实例）两个基准上进行了实验。实验设置使用GPT-5作为默认基础模型，并对比了开源模型GLM-4.7以验证泛化性。主要对比方法是先前的测试增强工作UTBoost。

实验结果显示，SWE-ABS在SWE-Bench Verified上显著增强了测试套件的判别能力：它强化了251/500个实例（50.2%），而UTBoost仅强化了10个（2%）；SWE-ABS拒绝了2184个先前通过的补丁（占总补丁11041的19.78%）。这导致顶级代理的解决率从78.80%下降至62.20%，并引发排行榜显著重排（Spearman秩相关系数从UTBoost的0.98降至0.82）。在SWE-Bench Pro上，SWE-ABS同样诱导了16.46个百分点的平均解决率下降，证明了其跨基准泛化能力。

消融研究表明，覆盖驱动增强阶段单独将强化实例数从190提升至198，平均解决率下降从10.34个百分点提升至11.30个百分点；结合突变驱动对抗阶段后，强化实例数增至251，平均解决率下降显著提升至14.56个百分点，证明两阶段具有互补性。此外，对错误类型的分析显示，被拒绝补丁中逻辑错误占47%，不完整修复占35%，表明当前AI代码生成存在语义推理弱点。

### Q5: 有什么可以进一步探索的点？

该论文揭示了当前基于测试的代码生成基准存在性能虚高问题，并提出了对抗性增强框架。其局限性主要包括：1）测试增强可能过拟合于“黄金补丁”，导致10.6%的假阴性率；2）分析范围限于过程内切片，可能忽略跨模块依赖；3）依赖参考实现，限制了在无参考场景的应用。

未来可探索的方向包括：首先，可研究如何减少对黄金补丁的依赖，例如通过合成语义等价的变体或利用形式化规范来生成测试，以降低过拟合风险。其次，可扩展跨过程与跨文件的程序分析技术，以捕捉更复杂的依赖关系，提升测试增强的完备性。此外，将SWE-ABS集成到持续的基准共进化流程中，实现测试套件的动态强化，能更持久地反映智能体真实能力。最后，将框架扩展到更多编程语言（如Java、C++）并探索其在其他需可执行验证的领域（如硬件设计或数学证明）的应用，也是富有潜力的方向。这些改进有望推动构建更鲁棒、更可靠的评估基准。

### Q6: 总结一下论文的主要内容

该论文指出当前SWE-Bench Verified排行榜的性能评估存在虚高问题，其核心贡献是提出了一个名为SWE-ABS的对抗性基准强化框架。研究问题在于现有测试套件不够严格，导致许多语义错误的代码补丁被误判为成功，从而夸大了AI代理的实际性能。

方法上，SWE-ABS采用两阶段流程：首先通过程序切片进行覆盖率驱动的测试增强，针对未测试的代码区域；其次进行突变驱动的对抗性测试，合成看似合理但实际错误的补丁，以暴露测试套件的语义盲区。

主要结论显示，在SWE-Bench Verified的500个实例中，SWE-ABS成功强化了50.2%的实例，性能比先前工作提升25.1倍，并拒绝了19.71%原本通过的补丁。这导致顶级代理的得分从78.80%显著下降至62.20%，排行榜发生重大重排，原排名第一的代理降至第五位。该研究意义在于揭示了现有基准的局限性，并为构建更鲁棒、可靠的AI编程评估体系提供了有效工具。
