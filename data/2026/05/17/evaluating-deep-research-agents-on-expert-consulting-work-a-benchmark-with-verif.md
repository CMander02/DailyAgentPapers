---
title: "Evaluating Deep Research Agents on Expert Consulting Work: A Benchmark with Verifiers, Rubrics, and Cognitive Traps"
authors:
  - "Tanmay Asthana"
  - "Aman Saksena"
  - "Divyansh Sahu"
date: "2026-05-17"
arxiv_id: "2605.17554"
arxiv_url: "https://arxiv.org/abs/2605.17554"
pdf_url: "https://arxiv.org/pdf/2605.17554v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "LLM Agent评估"
  - "深度研究Agent基准"
  - "认知陷阱"
  - "混合评估框架"
  - "管理咨询"
  - "人工验证"
  - "错误模式分析"
relevance_score: 9.5
---

# Evaluating Deep Research Agents on Expert Consulting Work: A Benchmark with Verifiers, Rubrics, and Cognitive Traps

## 原始摘要

Frontier deep research agents (DRAs) plan a research task, synthesize across documents, and return a structured deliverable on demand. They are being deployed in enterprise workflows faster than they are being evaluated. Existing benchmarks measure factual recall, single-hop QA, or generic agentic skill, missing the multi-document, decision-grade work DRAs are deployed to produce. We introduce a benchmark targeting the structured analytical deliverables that fill a management consultant's typical week.
  We grade three frontier agents, namely Claude Opus 4.6 with web search, OpenAI o3-deep-research, and Google Gemini 3.1 Pro deep-research, on 42 SME-authored prompts. Each of the 126 responses is scored on two layers: deterministic ground-truth verifiers (mean 13.8 per task) and a five-criterion 0-3 SME rubric, composed into a Verifier-Rubric Score (VRS) on 0-100. Most prompts embed cognitive traps that penalize surface-pattern matching. Acceptance under our joint threshold (rubric mean >= 2.5 and verifier rate >= 80%) is uniformly low: Gemini 21.4%, o3 9.5%, Claude 9.5%.
  Mean VRS scores agree with published rubric-based benchmarks (our top 62.6 vs. APEX-v1 64.2, ProfBench 65.9, ResearchRubrics < 68%), validating the rubric construct. ACCEPT rates sit below APEX-Agents' MC-segment Pass@1 band (12.3-22.7%) on dedicated DR agents; our floor is three points lower despite the harness advantage, opened by stricter conjunctive grading and trap design.
  Each agent fails distinctively. Claude produces the deliverable most reliably (4.5x the others' rate on file-required tasks) but carries the highest fabrication signature. o3 has the cleanest reasoning average yet drops required sections and propagates arithmetic errors. Gemini is bimodal, with the highest acceptance rate alongside the most zero-scored rubric cells.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

论文旨在填补前沿深度研究Agent（DRA）评估的空白。当前主流基准（如MMLU、TriviaQA、WebArena、GAIA）主要衡量事实回忆、单跳问答或通用Agent技能，无法评估DRA在企业场景中所需的、基于多文档的、决策级结构化交付物生成能力。具体问题包括：缺乏评估多文档综合、结构化输出、精确计算和领域专业性结合的基准；现有评估多依赖LLM作为裁判，存在长度偏好、谄媚和自我偏好等校准失效问题；缺少针对深度研究Agent特有的错误模式（如编造数据、级联数学错误、格式坍塌）的系统性评测。论文通过构建42个管理咨询领域专家级提示、双层评分系统（确定性验证器+5维度0-3专家评分量表）、刻意嵌入认知陷阱，以及三位前沿Agent（Claude Opus 4.6、o3-deep-research、Gemini 3.1 Pro）的126次响应评估，来解决这一评估鸿沟。

### Q2: 有哪些相关研究？

相关工作分为几个方向。通用Agent基准（GAIA、BrowseComp、WebArena、AgentBench、ToolBench）针对工具使用和浏览，但缺乏领域专家级研究评估。深度研究基准（DeepResearch Bench、ResearcherBench、SciAgent、SciBench）侧重科学QA，不测试企业交付物生产。领域特定基准（FinanceBench、FinQA、TAT-QA用于金融；MedQA、PubMedQA用于医学；LegalBench、CaseHOLD用于法律）是进步，但仍将评估框架为问答而非结构化交付物生产。最密切的方法论相关工作是APEX-v1（LLM评判的知识工作交付物二元量表）和APEX-Agents（LLM评判的多应用模拟环境状态捕捉二元标准），以及ResearchRubrics（专家量表框架）。但上述均未在同一个响应上结合确定性专家级验证器与独立的多标准序数量表，也未将认知陷阱作为设计选择。LLM-as-Judge范式（Zheng et al.、Li et al.）已知有校准失败，因此论文锚定专家注释并使用二元验证器（类似HELM风格混合评估）。幻觉研究（Ji et al.、Huang et al.、Zhang et al.）主要在QA设置中，本文的双层工具可在同一响应中观察编造和结构完成失败，将其扩展到结构化交付物场景。

### Q3: 论文如何解决这个问题？

论文设计了一个包含三个核心组件的基准：（1）提示语料库由42个管理咨询领域专家撰写提示组成，分为五类认知能力——约束研究提示（CRP，测试来源纪律）、相关性压缩提示（RCP，测试信号提取）、结构合规提示（SCP，测试算法服从性）、潜在分解提示（LDP，测试问题分解）、失败敏感提示（FSP，测试精度和准确性）。大多数提示刻意嵌入认知陷阱：人类误差模仿（如不一致单位、脚注矛盾、非标准日期格式）和确定性精度陷阱（如取第一个合理数字、不加权平均）。所有提示包由15年以上经验的管理咨询领域专家独立审核。（2）双层评分系统：第一层为任务特定二元验证器（平均每任务13.8个），提供自动化、客观的通过/失败门控；第二层为五位0-3序数专家量表（数据完整性DI、分析严谨度AR、相关性与聚焦RF、执行精度EP、格式与可交付性FD）。两层结合成验证器-量表分数VRS（0-100），其中严格变体在任一标准得零分时整体归零。接受标准ACCEPT定义为所有标准>0、推理均值≥2.5且验证器通过率≥80%。（3）评估基础设施：通过代理特定适配器（Claude用Anthropic Messages API、o3用OpenAI Responses API+Containers、Gemini用Google Interactions API）同时分发42个提示，文件格式规范化后运行。三位Agent在API表面、代码执行环境、工具可用性和文件处理能力上存在显著架构差异（见表5），但文件生成失败归因于模型代码质量而非基础设施不对称。评估后进行了独立质量控制（QC）第二轮审核。论文还采用Cohen's d效应量、麦克尼马尔检验、多重检验校正等统计方法进行Agent对比。

### Q4: 论文做了哪些实验？

实验对42个提示在3位Agent（Claude Opus 4.6、o3-deep-research、Gemini 3.1 Pro）上进行了共126次响应评估。主要结果：接受率（ACCEPT）方面，Gemini 21.4%、Claude和o3均为9.5%；严格VRS方面，o3 62.6、Gemini 56.9、Claude 42.0；推理均值方面，o3 1.97、Gemini 1.81、Claude 1.65；自动拒绝率（至少一个标准为零）方面，Claude 33.3%、Gemini 23.8%、o3 4.76%；输出文件产出率（10个要求文件任务）方面，Claude 90%、o3 30%、Gemini 10%。按提示类型分析：o3在FSP（VRS 76.93）和RCP（71.59）领先，Gemini在CRP（54.64）和FSP（77.20）领先，Claude在LDP（57.73）领先。Cohen's d效应量显示FSP上o3对Claude的d=-1.39（大规模优势），SCP上Claude对o3的d=-1.66。模型判别力分析显示仅33%提示能区分Agent（无提示全接受），但连续VRS显示有效能力分化（Gemini赢19提示、Claude赢13、o3赢10，90.5%与专家共识一致）。错误模式分析（基于LLM对专家自由文本的标记分类）：Claude以编造为特征（22编造标签、20文件未读取标签）；o3以崩溃为特征（22级联数学错误标签、8缺失部分标签）；Gemini以波动和系统崩溃为特征（8技术失败标签、41标准零分（Claude 30、o3 10）但19次VRS胜出）。内部结构分析显示标准间相关性均值约0.61（最高AR×EP=0.75最低DI×FD=0.38），验证器通过率与推理均值相关性0.78。量表验证显示所有标准与ACCEPT显著相关（范围ρ=0.31-0.55），无单一主导标准，且FD、DI、AR可独立导致边界拒绝。跨VRS权重敏感性分析显示结论稳健。

### Q5: 有什么可以进一步探索的点？

论文自身指出了若干局限性和未来方向。首先，样本量有限（42提示×3Agent=126响应），限制了提示类型内效应量的推断精度（如FSP每臂n=6），计划发布第二版增加更多领域和样本。其次，评分者间信度（IRR）未正式报告（当前仅单专家评分+QC确认），后续应进行两独立专家评分并计算Cohen's κ等。第三，标准间相关性（均值ρ≈0.61）表明量表可能测量2-3个潜在因子而非5个正交特质，需正式因子分析确定真实潜在结构。第四，ACCEPT阈值（推理均值≥2.5且验证器通过率≥80%）是任意设定的，未来应基于实际操作需求或领域标准进行校准研究。第五，认知陷阱的设计和难度校准需要更系统的实验来验证其有效性。第六，研究可扩展到更多Agent（如GPT-5、Claude下一代版本）和更多领域（如金融、法律、医疗）。第七，论文提出的错误模式分析（LLM标记分类）的精度/召回率未系统评估，可开发更严格的自动错误检测方法。第八，验证器覆盖范围有限（任务特定而非通用），未来可探索将结构化知识图谱或形式化推理作为部分验证器的方案。总之，这篇论文为深度研究Agent评估建立了新范式，为后续研究提供了丰富的实证基础和可扩展框架。

### Q6: 总结一下论文的主要内容

这篇论文提出了针对前沿深度研究Agent（DRA）的评估基准，聚焦管理咨询领域专家级结构化交付物生产。核心贡献包括：1) 42个专家撰写提示，分为五类认知能力测试，并刻意嵌入认知陷阱（如不一致单位、脚注矛盾、精度陷阱）以防止表面模式匹配。2) 双层评分系统：任务特定确定性验证器（平均每任务13.8个）+五维度0-3序数专家量表（数据完整性、分析严谨度、相关性、执行精度、格式与可交付性），组合成VRS分数。3) 对Claude Opus 4.6、o3-deep-research和Gemini 3.1 Pro三位Agent的126次响应系统评估。主要发现：接受率普遍低（Gemini 21.4%、Claude和o3均为9.5%）；每位Agent有独特的失败模式（Claude以编造为特征、o3以级联数学错误和缺失部分为特征、Gemini以高度波动和系统崩溃为特征）；量表证明有效且能区分Agent能力（90.5%与专家共识一致）。论文为DRA评估建立了新标准，凸显了现有前沿Agent在结构化、决策级知识工作中的显著差距。所有评估代码和提示语料库开源发布。
