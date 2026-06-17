---
title: "LegalHalluLens: Typed Hallucination Auditing and Calibrated Multi-Agent Debate for Trustworthy Legal AI"
authors:
  - "Lalit Yadav"
  - "Akshaj Gurugubelli"
date: "2026-06-16"
arxiv_id: "2606.18021"
arxiv_url: "https://arxiv.org/abs/2606.18021"
pdf_url: "https://arxiv.org/pdf/2606.18021v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
  - "cs.MA"
tags:
  - "Legal AI"
  - "Hallucination Detection"
  - "Multi-Agent Debate"
  - "Calibration"
  - "Typed Evaluation"
  - "Risk Assessment"
  - "Agent Auditing"
  - "CUAD Benchmark"
relevance_score: 9.5
---

# LegalHalluLens: Typed Hallucination Auditing and Calibrated Multi-Agent Debate for Trustworthy Legal AI

## 原始摘要

AI systems deployed in legal workflows hallucinate at rates that aggregate metrics report at ~52%, but this average conceals where errors concentrate and in which direction they run, leaving compliance officers without an actionable signal for trustworthy deployment. We present LegalHalluLens, an auditing framework with three components: typed hallucination profiles across four legally-motivated claim categories (numeric, temporal, obligation/entitlement, factual) over CUAD (Hendrycks et al., 2021); a Risk Direction Index (RDI) that reduces omission-versus-invention bias to a single deployment-comparable scalar; and a typed debate pipeline calibrated to both magnitudes and directions. Across 510 contracts and 249,252 clause-level instances we measure a within-model gap of approximately 38-40 pp between obligation/numeric and temporal claims that aggregate reporting hides, and show that two systems with matched 52% rates can carry opposite RDIs. The debate pipeline reduces fabricated detections by 45% with per-category gains tracking the diagnosis, matching commercial APIs with a substantially smaller backbone (4B active parameters). Typed profiles and RDI surface failure modes that aggregate metrics hide; we further show these diagnostics serve as calibration inputs for multi-agent debate pipelines, where Skeptic challenges and asymmetric gates targeted at measured failure modes outperform generically-tuned debate. The framework supports direction-aware procurement, accountability, and agent design for legal AI deployed in the wild.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决法律AI部署中的核心信任问题：虽然现有模型平均幻觉率约为52%，但这一聚合指标掩盖了错误的具体类型和方向，使合规官员难以获得有意义的行动信号。现有方法存在三大不足：一是仅报告平均幻觉率，无法揭示不同法律条款（如数字、义务、时间、事实）间的显著失败差异（模型内差距可达38-40个百分点）；二是缺乏区分错误方向（遗漏 vs 编造）的单一可部署指标；三是现有的通用多智能体辩论方法未针对法律领域的特定错误模式进行校准。

为此，本文提出了LegalHalluLens审计框架，核心解决三个问题：（1）是否不同法律声明的幻觉率存在系统差异，且模式跨架构一致？（2）能否通过单一标量指标（风险方向指数RDI）捕捉错误的方向性特征，以区分聚合指标无法区分的系统？（3）校准后的多智能体辩论管道能否针对最高失败类别产生显著增益，使小模型匹配甚至超越商业API性能？通过249,252个条款级实例的实证，论文证明类型化剖析和RDI能暴露聚合指标隐藏的失败模式，而针对这些诊断校准的辩论管道可将编造检测减少45%，显著提升法律AI的可信部署性。

### Q2: 有哪些相关研究？

在相关研究中，本文主要从三个类别进行对比。**法律幻觉与基准方面**：已有研究在法律领域构建了幻觉分类法（如联邦司法任务中58%-88%的幻觉率），但未关注合同提取任务，也未将幻觉方向性转化为可比较的标量。本文提出的四类分类法（数字、时间、义务/权利、事实）和风险方向指数（RDI）填补了这一空白。CUAD数据集被作为幻觉标注基准，但与本文按类别细分的漏洞不同。**通用幻觉基准与辩论式缓解**：FActScore、HaluBench等工具测量事实精度但缺乏类别分层；多智能体辩论已被研究作为事实性机制，但本文创新在于校准怀疑者挑战（Skeptic challenges）和不对称门控（asymmetric gates）以匹配实验1中每类别的失败模式，而非通用调优。**高风险部署中的智能体设计**：现有工作对怀疑者提示、门控阈值等采用通用调整，本文认为这在高风险场景中不合适——适当的怀疑者挑战应基于模型实际表现出的失败模式，门控不对称性应由检测方向风险画像决定。本文首次提出基于实测失败模式诊断（而非通用选择）校准多智能体提取管道组件。总体上，本文在合同提取场景下首次结合了细粒度幻觉分类、方向性指标与诊断校准的辩论管道。

### Q3: 论文如何解决这个问题？

该论文通过三个核心组件解决法律AI幻觉问题：类型化幻觉画像（Typed Hallucination Profile）、风险方向指数（RDI）和类型化辩论管道（Typed Debate Pipeline）。整体框架首先将模型输出按法律主张类别（数值、时间、义务/权利、事实）分层报告幻觉率，揭示聚合指标掩盖的类别间差异（如义务/数值与时间类间存在约38-40个百分点的差距）。RDI将遗漏与发明两种方向性偏差压缩为单个标量值（正数表示过度发明，负数表示过度省略），通过比较两个聚合幻觉率均为52%的系统却呈现相反RDI值的案例，证明其能区分方向性风险。类型化辩论管道采用六角色状态机设计：怀疑者（Skeptic）针对测量出的故障模式发起类型化质询问题（如数值类追问是否逐字引用、义务类检查情态动词和例外条款）；支持者（Supporter）仅使用合同原文辩护；重提取器（Re-extractor）在检测到结构错误时重新提取；仲裁者（Arbiter）在回合耗尽时保守解决僵局；验证者（Verifier）独立核查合同；法官（Judge）基于完整辩论记录做出绑定决策。三个创新设计包括：1）类型化怀疑问题精准匹配故障模式；2）重提取节点针对结构错误而非内容矛盾（覆盖62-71%的矛盾）；3）非对称结构门控（新增检测需双重确认，删除检测被验证者阻止），反映高风险类别高虚警率>低拒真率的风险偏好。该管道在仅4B参数的模型上实现虚造检测降低45%，匹配商业API性能。

### Q4: 论文做了哪些实验？

论文进行了两项主要实验。**实验1**构建了类型化幻觉基准测试，使用CUAD v1.0数据集（510份商业合同，249,252个条款级实例），将41种条款类型映射为四类（数字、时间、义务/权利、事实）。对比了四个模型（gemini-3-flash、gpt-5.2、qwen3-32b、llama-3.3-70b），每模型在510份合同上运行三次。结果显示，尽管聚合指标报告约52%的幻觉率，但类型化分析揭示了隐藏的巨大差异：在数字和义务条款上，所有模型的幻觉率（Hal_TP）高达64.8%-74.3%，而时间条款仅为29.0%-35.1%，模型的类型内差距约38-41个百分点。此外，两个聚合指标均为约52%的模型（qwen3-32b和gpt-5.2）展示了相反的误差方向（RDI指标分别为-0.202和+0.161），一个倾向于遗漏，另一个倾向于捏造。**实验2**使用gemma-4-26B-A4B（4B活跃参数）作为骨干模型，在120份合同的匹配子集上评估了类型化辩论流程。结果显示，该方法将错误检测减少了45%（FP从524降至287），在义务（ΔFAR下降8.2%）、事实（下降5.8%）和数字条款上取得了最大收益，使gemma-debate综合排名从基线最后一名（5.2）升至第一（2.4），甚至超越了商业API（gpt-5.2得分2.6）。同时，义务条款的RDI从-0.078纠正至-0.014，实现了方向校准。

### Q5: 有什么可以进一步探索的点？

主要局限性与未来研究方向包括：

1. **跨领域泛化性不足**：当前结论仅基于CUAD数据集中的美国商业合同，未能验证在其它司法管辖区域、非合同类法律文档（如判例、法规）中的表现。未来应构建多语言、多法系的法律审计基准，验证类型化幻觉模式的迁移性。

2. **上下文窗口限制**：所有实验均假设完整文档上下文；当合同超出模型窗口时，检索增强架构会引入新的正交失败模式。建议开发长文档专用的分块审计策略，或采用层级式RDI聚合。

3. **评估依赖单一法官**：所有指标通过单个LLM评估器执行，缺乏人工专家验证。后续可设计分层抽样下的专家注释验证流程，将RDI从方向性信号提升为量值化置信区间，并开发针对法官偏好的弱监督校准方法。

4. **辩论管道对比有限**：实验仅使用单一骨干模型（4B参数），未探索不同规模、架构下类型化辩论的效果边界。可扩展至混合专家系统，利用类别特异性布防策略（如对数值类事实增加统计分析入口），实现更精细的幻觉校正。

### Q6: 总结一下论文的主要内容

本文提出LegalHalluLens框架，旨在解决法律AI系统中幻觉率（约52%）被聚合指标掩盖的问题。核心贡献包括：基于四种法律相关声明类型（数值、时间、义务/权利、事实）在CUAD数据集上构建类型化幻觉画像；提出风险方向指数（RDI），将遗漏与捏造偏差简化为单一标量指标；以及一种校准到幻觉幅度和方向的多智能体辩论管道。在510份合同、249,252条款级实例上，发现聚合报告隐藏了约38-40个百分点的模型内差距（义务/数值与时间声明间），且两个具有相同52%幻觉率的系统可能具有相反的RDI。辩论管道将捏造检测减少45%，使用较小骨干网络（4B活跃参数）即达到商业API性能。主要结论是：法律AI的可信部署关键不在于聚合准确率，而在于识别其失败的具体声明类型及失败方向，类型化画像和RDI可作为校准多智能体辩论的输入。
