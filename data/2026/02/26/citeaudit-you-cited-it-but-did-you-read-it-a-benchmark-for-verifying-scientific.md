---
title: "CiteAudit: You Cited It, But Did You Read It? A Benchmark for Verifying Scientific References in the LLM Era"
authors:
  - "Zhengqing Yuan"
  - "Kaiwen Shi"
  - "Zheyuan Zhang"
  - "Lichao Sun"
  - "Nitesh V. Chawla"
  - "Yanfang Ye"
date: "2026-02-26"
arxiv_id: "2602.23452"
arxiv_url: "https://arxiv.org/abs/2602.23452"
pdf_url: "https://arxiv.org/pdf/2602.23452v1"
categories:
  - "cs.CL"
  - "cs.DL"
tags:
  - "多智能体系统"
  - "Agent评测/基准"
  - "工具使用"
  - "科学写作"
  - "幻觉检测"
  - "可信AI"
relevance_score: 7.5
---

# CiteAudit: You Cited It, But Did You Read It? A Benchmark for Verifying Scientific References in the LLM Era

## 原始摘要

Scientific research relies on accurate citation for attribution and integrity, yet large language models (LLMs) introduce a new risk: fabricated references that appear plausible but correspond to no real publications. Such hallucinated citations have already been observed in submissions and accepted papers at major machine learning venues, exposing vulnerabilities in peer review. Meanwhile, rapidly growing reference lists make manual verification impractical, and existing automated tools remain fragile to noisy and heterogeneous citation formats and lack standardized evaluation. We present the first comprehensive benchmark and detection framework for hallucinated citations in scientific writing. Our multi-agent verification pipeline decomposes citation checking into claim extraction, evidence retrieval, passage matching, reasoning, and calibrated judgment to assess whether a cited source truly supports its claim. We construct a large-scale human-validated dataset across domains and define unified metrics for citation faithfulness and evidence alignment. Experiments with state-of-the-art LLMs reveal substantial citation errors and show that our framework significantly outperforms prior methods in both accuracy and interpretability. This work provides the first scalable infrastructure for auditing citations in the LLM era and practical tools to improve the trustworthiness of scientific references.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大语言模型（LLM）时代下，学术写作中日益严重的“引用幻觉”问题，即模型可能生成看似合理但实际不存在的虚假参考文献。研究背景是科学研究的严谨性高度依赖准确引用，而LLM的广泛应用带来了全新的风险：它们能自动编造出格式规范、内容逼真却无对应真实出版物的参考文献。这种现象已在机器学习顶级会议的投稿甚至录用论文中被发现，严重损害了同行评审的可靠性和学术生态的诚信。

现有方法的不足主要体现在两个方面：首先，现有的自动化引用核查工具严重依赖外部信息检索，但现实世界中的引用格式嘈杂且异构，导致这些系统在面对非标准、有噪声的引用格式时表现脆弱，容易出错。其次，大多数现有系统是闭源的，既未公开其检测机制，也缺乏一个大规模、标准化且可复现的基准来系统评估引用幻觉检测的性能。

因此，本文要解决的核心问题是：如何构建一个全面、可靠的基准和检测框架，以应对真实学术环境中引用格式的噪声和多样性，并系统性地评估和提升对“引用幻觉”的检测能力。具体而言，论文提出了首个针对科学写作中幻觉引用的大规模基准（CiteAudit）和一个多智能体验证框架。该框架将引用核查分解为声明提取、证据检索、段落匹配、推理和校准判断等多个协作步骤，从而能够精细评估引用是否真正支持其关联的学术主张，旨在为研究者、评审人和出版商提供可扩展的实用工具，以提升科学引用的可信度。

### Q2: 有哪些相关研究？

相关研究主要可分为三类：**基于检索的引用验证方法**、**基于LLM的推理方法**以及**基于智能体（Agent）的检测框架**。

在**基于检索的引用验证方法**中，早期工作通过解析引用字符串并与外部书目数据库（如DOI、学术搜索引擎）进行精确匹配来审核参考文献。然而，这类方法对现实世界中噪声大、格式多变的引用十分脆弱，性能有限。后续研究采用了模糊匹配策略，通过词元级相似度比较字段，以检测变异或不完整的引用，但其本质仍是字段级相似度匹配，对于细微或残缺的引用扰动仍易失效。

**基于LLM的推理方法**是更近期的趋势，它们将LLM与检索结合进行引用验证。这些方法开始引入推理能力，但早期尝试依赖的外部数据库源往往过于有限和同质化，在实践中可能导致误报，且在需要从复杂多模态学术文档中提取和验证引用的真实场景中面临挑战。

**基于智能体的检测框架**代表了新的方向。智能体系统通过工具使用（如调用网络搜索）与外部环境交互，获取实时证据并执行操作，从而减少对参数化记忆的依赖。已有早期工作将网络搜索智能体应用于事实核查场景，证明了其在基于证据的错误信息检测中的有效性。这些进展为引用验证提供了新思路：利用更广泛的网络搜索智能体，可以访问更全面、多样化的来源，从而克服基于API的引用检查的覆盖范围限制，提升检测的鲁棒性。

本文提出的多智能体验证框架，正是在此基础上，系统性地将引用检查分解为声明提取、证据检索、段落匹配、推理和校准判断等多个步骤，构建了一个可扩展的基准和检测基础设施。与之前工作相比，本文方法不仅超越了单纯的字段匹配或有限的API检索，还通过智能体架构整合了更强大的证据获取与推理能力，并在标准化评估指标下实现了更高的准确性和可解释性。

### Q3: 论文如何解决这个问题？

论文通过构建一个去中心化的多智能体验证框架来解决科学文献中引用幻觉的检测问题。其核心方法是将引用验证分解为一个多阶段的证据核查流程，并采用分层标准化操作程序（SOP）进行协调。

整体框架是一个顺序与并行相结合的任务执行图。主要包含五个专门化的智能体模块：1）**提取智能体**：作为流程起点，它集成了高精度OCR工具，从PDF中解析文本和视觉坐标，并将非结构化引用字符串转换为结构化的元数据元组，确保捕获原始信息而无语义失真。2）**双端记忆智能体**：维护一个内部知识库，通过向量相似度计算进行语义查找。若置信度超过阈值，则通过“快速路径”立即验证，避免冗余的外部检索，从而优化延迟。3）**网络搜索智能体**：当内部缓存未命中时被触发，它通过搜索引擎API进行外部验证，并执行深度爬取协议获取Top-5结果URL的完整文本内容，为判断提供真实世界证据。4）**判断智能体**：作为核心决策引擎，它根据“严格一致性准则”评估提取的元数据与检索到的证据集之间的对齐程度。仅当所有字段（标题、作者、URL、出版场所）都严格匹配时，才判定引用为真实。5）**学者智能体**：作为真实性基准，在网络证据不足时被调用，对权威学术数据库进行低频、高精度的定向爬取，以获取规范记录。

创新点在于其分层级联的执行逻辑和资源优化策略。一个LLM控制器作为SOP执行器进行协调，通过规划模型将验证任务路由为：首先尝试高速内存查询；若不成功，则进行网络检索与一致性审计；若仍无法判定，最后才启动计算成本高的学者智能体进行最终验证。这种设计确保了计算昂贵的代理仅作为备用方案，遵循了最小资源消耗原则。整个流程不仅系统化地审计了引用的存在性和元数据完整性，还通过记忆池缓存已验证引用，显著提升了大规模验证的效率和可扩展性。

### Q4: 论文做了哪些实验？

论文实验主要包括系统性能评估、消融研究和案例分析。实验设置上，作者构建了一个多智能体验证框架，核心使用Qwen3-VL-235B模型进行推理和视觉解析，并部署在配备NVIDIA B200 GPU的高性能集群上。框架包含规划模型、提取、记忆、网络搜索、判断和学术数据库查询等多个智能体，采用多线程池实现并行处理。

数据集方面，使用了两个测试集：一个生成的基准测试集（包含3,586个真实引用和2,500个通过受控扰动生成的幻觉引用）和一个真实世界测试集（包含2,743个真实引用和467个从真实学术来源收集的自然产生的幻觉引用）。

对比方法包括多个先进的专有和开源大语言模型，如Mixtral-8x7B-Instruct、Llama-3.3-70B-Instruct、Qwen3-Next-80B-A3B、Gemini-3-Pro、GPT-5.2、GPTZero和Claude-Sonnet-4.5。

主要结果：在真实世界测试集上，本文提出的模型取得了最佳性能，准确率（Acc）为0.972，精确率（Prec）为0.823，召回率（Rec）为1.000，F1分数为0.903，显著优于所有对比模型。例如，第二佳的Gemini-3-Pro的F1分数为0.571。在效率方面，本文模型处理10个引用的平均时间为2.3秒，成本为0美元，在速度和成本上均优于其他商业模型。

消融研究验证了各组件的重要性：移除学术数据库查询智能体导致召回率从1.000降至0.684；移除基于LLM的判断智能体（改用严格字符串匹配）导致精确率从0.861暴跌至0.225，F1分数降至0.367；移除网络搜索智能体则使延迟增加约8倍至18.4秒。

案例分析进一步定性地展示了框架在检测细微引用不一致（如标题或作者不匹配）方面的有效性和可解释性。

### Q5: 有什么可以进一步探索的点？

该论文提出了一个创新的多智能体框架来检测科学文献中的幻觉引用，但其局限性和未来探索方向仍值得深入。首先，当前框架主要针对引用是否真实存在及其与主张的匹配度，但未深入评估引用质量，如来源的权威性、时效性或潜在偏见，这在实际科研中至关重要。其次，实验可能局限于特定领域或数据集，未来可扩展至更广泛的学科（如社会科学或医学），以测试框架的泛化能力。此外，依赖外部数据库进行证据检索可能受限于数据覆盖范围或更新延迟，未来可探索动态知识图谱或实时学术搜索引擎集成。从技术角度看，多智能体框架的计算开销较大，未来可优化其效率，例如通过轻量化模型或分布式处理。最后，论文未充分探讨如何将检测工具无缝整合到现有学术工作流（如投稿系统或审稿平台），这将是推动实际应用的关键。结合见解，未来可探索结合主动学习机制，让系统在检测中持续适应新的引用模式，或开发交互式工具，辅助研究者实时修正引用错误，从而提升科学写作的整体可信度。

### Q6: 总结一下论文的主要内容

该论文针对大语言模型（LLM）时代科学文献中日益严重的“幻觉引用”问题，提出了首个全面的基准测试与检测框架。核心问题是：LLM生成的文本可能包含看似合理但实际不存在的参考文献，或引用内容无法支持其声称的论点，这严重威胁了学术研究的可信度与同行评审的有效性。

论文的主要贡献是构建了一个名为CiteAudit的多智能体验证框架和大型人工验证数据集。该方法将引用核查分解为多个步骤：主张提取、证据检索、段落匹配、推理和校准判断，从而系统性地评估引用源是否真实存在并支持其相关主张。同时，论文定义了统一的评估指标，用于衡量引用的忠实性和证据对齐程度。

实验表明，当前先进的LLM存在大量引用错误，而CiteAudit框架在检测准确性和可解释性上均显著优于现有方法。这项工作的主要意义在于，为自动化、可扩展地审计科学引用提供了首个基础设施和实用工具，有助于在LLM辅助科研的背景下提升学术文献的可靠性与完整性。
