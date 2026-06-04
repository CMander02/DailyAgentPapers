---
title: "Evaluating Large Language Models in Dynamic Clinical Decision-Making with Standardized Patient Cases"
authors:
  - "Cheng Liang"
  - "Pengcheng Qiu"
  - "Ya Zhang"
  - "Yanfeng Wang"
  - "Chaoyi Wu"
  - "Weidi Xie"
date: "2026-06-03"
arxiv_id: "2606.05112"
arxiv_url: "https://arxiv.org/abs/2606.05112"
pdf_url: "https://arxiv.org/pdf/2606.05112v1"
categories:
  - "cs.CL"
tags:
  - "临床Agent"
  - "评测基准"
  - "动态决策"
  - "标准化病人"
  - "多轮交互"
  - "LLM代理"
  - "医疗AI"
relevance_score: 9.0
---

# Evaluating Large Language Models in Dynamic Clinical Decision-Making with Standardized Patient Cases

## 原始摘要

Large language models (LLMs) are increasingly proposed as clinical agents, yet static, single-turn benchmarks cannot capture how a model dynamically delivers care across an encounter: gathering information, planning treatment, and adapting longitudinal management across successive patient states. Medical education has long addressed an analogous challenge through standardized patients (SPs): trained actors who consistently portray clinical cases, enabling realistic practice and objective, scripted assessment. Here we introduce MedSP1000, an SP-derived interactive benchmark for clinical-agent evaluation, including 1,638 SP cases with 24,602 trajectory-level peer-reviewed rubrics. MedSP1000 converts peer-reviewed SP teaching cases into executable scenarios with defined SP case scripts, clinical environment contexts, and human-validated structured rubric. In each simulation evaluation run, a clinical agent interacts in closed loop with a patient agent and an environment controller, and its behaviour is scored throughout the encounter against expert criteria specified in the original materials. Applying MedSP1000 to a range of general-purpose and medically specialized LLMs, we find that performance on static benchmarks does not reliably translate to such educational scenarios. The best-performing model, GPT-5.5, completes only 60.4% of expert-defined rubric items, whereas the strongest medically specialized model reaches 40.0%; increasing test-time compute produces no measurable gain. These results suggest that current LLMs, including agentic systems tuned for medicine, are not yet reliable enough to be safely integrated into actual clinical practice. More broadly, MedSP1000 shows how process-level, SP-style evaluation can reveal clinically relevant failure modes that single-turn benchmarks miss.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前大型语言模型（LLM）在动态临床决策能力评估上的缺失。研究背景指出，虽然LLM在静态医学考试和问答基准上表现出色，但现实临床实践是一个需要交互、序贯决策的动态过程，包括收集信息、制定检查、调整治疗方案等。现有评估方法主要依赖单轮问答，无法捕捉模型在完整诊疗过程中信息获取、治疗规划及长期管理的动态能力。为此，论文引入了基于标准化病人（SP）的教育评估框架，构建了MedSP1000基准。该基准包含1,638个经过同行评审的SP病例和24,602个轨迹级评分标准，通过封闭式多智能体系统模拟临床互动，对模型行为进行过程级评分。核心问题在于：现有LLM（包括医学专用模型）是否具备安全进行动态交互式临床实践的能力？评估发现，最佳模型GPT-5.5仅完成60.4%的评分项，而医学专用模型最高仅达40.0%，且增加测试时计算量无明显提升。这表明，当前LLM在动态临床场景中表现仍不可靠，静态知识优势无法转化为可靠的交互式临床行动能力。

### Q2: 有哪些相关研究？

根据论文，相关研究主要分为两类：

**方法类**：现有的大语言模型（LLM）临床评估方法大多依赖静态、单轮问答基准，如医学考试和临床决策支持基准。这些方法无法评估模型在交互式临床场景中的表现，例如信息收集、治疗计划制定和纵向管理。本文提出的MedSP1000则采用标准化病人（SP）案例，构建了交互式、多轮、闭环的评估框架，填补了静态基准的空白。与之前的交互式方法（如诊断病史采集或在线咨询）相比，MedSP1000更全面地涵盖了干预决策、纵向治疗规划和并发症监测等临床行为，并基于专家定义的评分标准进行过程级评估。

**应用类**：医学教育中广泛使用的标准化病人（SP）和客观结构化临床考试（OSCE）是本文工作的基础。这些方法通过训练有素的演员模拟临床案例，并对学习者进行客观评估。本文首次将这一成熟框架系统地应用于LLM临床智能体的评估，将经过同行评审的SP教学案例转化为可执行的基准测试，并实现了自动化的多智能体评估流程。与以往侧重最终答案正确性的单轮基准不同，MedSP1000揭示了模型在临床过程中遗漏关键步骤、时机不当等静态基准无法捕捉的失败模式。

### Q3: 论文如何解决这个问题？

MedSP1000通过构建一个动态、多智能体的标准化病人(SP)交互评估框架来解决对大型语言模型(LLM)在动态临床决策中的评估问题。核心方法是将经过同行评审的SP教学案例转化为可执行的闭环模拟场景。整体框架包含四个角色特定的信息包:场景初始化(仅提供就诊背景和主诉)、患者脚本(指导患者智能体如何回应)、环境控制材料(控制临床环境状态变化)和评分标准。评估运行时,待评估模型扮演临床医生,与患者智能体和环境控制器进行闭环交互,逐轮获取信息、做出决策,最终由评估智能体根据完整对话轨迹对每项评分标准进行二元判断。架构设计上,该框架将原始分散的教学材料重新组织为结构化、可执行的素材,支持有效的多智能体SP模拟。关键技术包括:从MedEdPORTAL教育资源中自动提取、过滤和构建1638个可执行案例;采用基于ACGME六大核心能力的评分标准;通过12名临床医生验证数据构建质量和运行时模拟保真度。创新点在于:首次系统性地利用医学教育中的SP案例资源构建LLM评估基准;从仅评估结果转向过程级评估,考察模型在什么时机获取正确信息、如何随患者状态更新判断以及执行适时的干预措施;揭示了静态基准测试表现好并不等同于动态临床实践能力可靠的关键发现。

### Q4: 论文做了哪些实验？

论文构建了MedSP1000基准，包含1,638个标准化病人案例及24,602个专家审核的评分细则。实验设置中，将LLM作为临床医生与病人智能体和环境控制器进行闭环交互，评估其在动态临床决策中的表现。测试了7个模型：闭源前沿模型（GPT-5.5、Claude-Opus-4.7、Gemini-3.1-Pro）、开源通用模型（DeepSeek-V4-Pro、Qwen-3.5）和医学专用模型（Baichuan-M3、MedGemma）。主要结果以案例级评分项目完成率（Rubric Completion Rate）为指标，采用确定性解码（temperature=0）。最佳模型GPT-5.5完成60.4%的评分项目（微平均），宏观平均为54.4%；最强医学模型Baichuan-M3仅达40.0%（微平均），宏观平均34.9%。所有模型在实践导向学习与改进（PBLI）能力上表现最差（如GPT-5.5仅25.8%），而在患者关怀（PC）方面相对最好（GPT-5.5达67.7%）。额外分析发现，增加测试时计算量未见可测量收益，且静态基准性能无法可靠迁移至此类交互场景。临床医生验证了数据构建（平均评分4.66-4.85）和运行时模拟（97.7%评分在4-5分）的高质量。研究表明当前LLM在动态临床决策中可靠性不足。

### Q5: 有什么可以进一步探索的点？

基于MedSP1000的评估结果，当前LLMs在动态临床决策中存在几个关键局限与未来探索点。首先，模型在信息主动获取、时序推理和适时干预等过程性环节表现薄弱，这提示未来需突破现有单轮问答评估框架，开发更精细的交互式训练范式，例如引入强化学习让模型在模拟环境中通过试错学习完整的临床信息采集与决策链条。其次，最佳模型GPT-5.5仅完成60.4%的评分项，且增加测试时计算量无显著提升，表明单纯扩大模型规模或推理深度存在天花板，未来应探索模块化认知架构（如分离诊断推理与行动规划模块），或结合知识图谱增强状态追踪与约束满足能力。此外，当前SP案例涵盖17个专科，但缺乏对罕见病、多病共存及跨文化语境的覆盖，未来需扩展案例库的多样性与临床现实复杂度。更前瞻的改进方向是将LLM与外部工具（如电子病历系统、临床决策支持API）深度集成，通过tool-use学习实现信息查询、结果解释与医嘱执行的全流程自动化。最后，由于静态指标无法可靠预测交互性能，学术界亟需建立像MedSP1000这样的过程性基准作为LLM临床评估的必要标准，并推动开源的交互式测试平台建设，以加速可安全部署的临床智能体研发。

### Q6: 总结一下论文的主要内容

论文提出了MedSP1000基准，用于评估大语言模型在动态临床决策中的表现。现有静态基准无法评测模型在完整诊疗过程中的信息收集、治疗规划和长期管理能力。受医学教育中标准化病人方法的启发，作者从同行评审的教育材料中构建了包含1638个交互式病例和24602个专家评分标准的基准。评估框架采用多智能体闭环系统，让被测试模型与患者智能体和环境控制器交互，并按专家标准逐项评分。对多种通用和医学专用LLM的评估显示，最佳模型GPT-5.5仅完成60.4%的专家定义项，医学专用模型最高仅达40.0%，增加测试时计算量未显著提升性能。结果表明，当前LLM在交互式临床场景中远未达到安全应用的可靠性要求。该研究首次将教育性SP案例系统转化为LLM评估资源，揭示了静态基准无法发现的临床相关失败模式。
