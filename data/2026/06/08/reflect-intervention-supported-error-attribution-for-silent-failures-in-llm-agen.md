---
title: "REFLECT: Intervention-Supported Error Attribution for Silent Failures in LLM Agent Traces"
authors:
  - "Xiaofeng Lin"
  - "Yingxu Wang"
  - "Tung Sum Thomas Kwok"
  - "Daniel Guo"
  - "Sahil Arun Nale"
  - "Charles Fleming"
  - "Guang Cheng"
date: "2026-06-08"
arxiv_id: "2606.09071"
arxiv_url: "https://arxiv.org/abs/2606.09071"
pdf_url: "https://arxiv.org/pdf/2606.09071v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "错误归因"
  - "静默失败"
  - "痕迹定位"
  - "对比证据"
relevance_score: 9.0
---

# REFLECT: Intervention-Supported Error Attribution for Silent Failures in LLM Agent Traces

## 原始摘要

Large language model (LLM) agents now solve complex tasks through long plan-and-execution traces, yet the ability to locate errors in a completed traces still lags far behind, especially in the \emph{silent failure} regime. Existing approaches predict suspect steps via classifiers or LLM judges, or recover correct answers via retry, but none feed the intervention outcome back to \emph{refine the attribution itself}. We propose \methodname, a method that closes this gap by diagnosing a candidate error step, testing it through controlled replay with a diagnosis-specific patch, and using the verified outcome flip as contrastive evidence to refine the final attribution. Across four localization benchmarks spanning multi-hop reasoning across domains, \methodname achieves the highest localization accuracy among same-auditor methods across all four benchmarks, with the largest gains on structured tool-use traces, while providing actionable localization even when ground-truth answers are unavailable.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）智能体在执行复杂任务时，其长规划与执行轨迹中“静默失败”的错误定位问题。静默失败是指智能体完成操作且无任何运行时异常（如工具崩溃、格式错误），但最终答案却是错误的情况。随着智能体能力增强，这种失败模式成为主流，错误仅体现在语义层面。

现有方法存在三个主要不足：一是通过分类器或LLM裁判预测可疑步骤，但缺乏执行验证，容易产生错误归因；二是重试或回溯虽能恢复正确答案，但无法指出原始轨迹中导致失败的关键步骤，将修正而非归因作为目标；三是约束与异常检测虽能标记异常步骤，但无法验证修复该步骤后是否真正改变结果。这些问题根源在于归因假设被提出但未经过测试。

因此，本文提出REFLECT方法，旨在通过干预支持的错误归因，弥补“修正-归因”鸿沟。其核心是诊断候选错误步骤，通过特定诊断补丁进行受控重放以测试假设，并利用验证后的结果翻转作为对比证据，细化最终归因。该方法要求在推理时对测试轨迹进行基于执行结果、保留前缀、目标明确干预的可验证归因，而非基于预训练分类器的预测。

### Q2: 有哪些相关研究？

根据论文内容，相关研究可分为以下几类：**推断时纠正方法**（如Reflection、self-consistency、self-debug等）通过反思或重新尝试提升任务准确率，但不诊断原始轨迹的失败原因，其批判附加于新尝试而非已归因的原始步；**无执行验证的定位方法**（如TRAIL、AgenTracer、TrajAD、ThinkPRM）依赖LLM评判、预训练分类器或过程奖励模型，但缺乏执行验证或因果测试，违反执行归因和推理时计算原则；**信号检查无因果测试**（如AgentRx）审计每一步但未验证修复是否改变结果；**无归因耦合的纠正方法**（如Reflexion、ICS、DoVer、LDB）虽涉及干预或回放，但干预结果未用于优化归因本身，如DoVer仅用验证结果评估纠正但不更新定位。本文提出的REFLECT通过将干预结果反馈到步骤级重新定位，首次统一具备执行验证、前缀保留回放、目标干预和推理时计算四大属性，与所有基线形成本质区别。

### Q3: 论文如何解决这个问题？

REFLECT 的核心创新在于将“干预验证”闭环引入错误归因流程。传统方法仅基于静态特征怀疑某步骤出错，但无法确认该错误是否真正导致最终答案失败。REFLECT 设计了“归因-干预-验证-修正”的四阶段架构。

首先，**候选错误步骤定位器**利用 LLM 作为审计者，分析完整工具调用痕迹，识别出最可能包含静默错误的节点（如错误参数或逻辑跳转）。然后，**诊断性干预模块**针对该候选步骤自动生成一个“修复补丁”（patch），例如修正函数参数、补充遗漏的中间推理或重新调用 API。接着，**受控重放机制**将补丁注入原始痕迹，从该步骤起重新执行后续所有操作，保留错误步骤之前的上下文不变。重放结果会输出一个新的最终答案。最后，**对比性归因精炼器**比较原始输出与重放输出的差异：若重放成功修复了答案错误，则确认原步骤确为根因，并利用该“成功翻转”作为正样本证据，反向指导归因模型更新其置信度；若重放未改善，则保留原归因。

关键技术包括：（1）**诊断性补丁生成**，需保证补丁最小化且不引入新错误；（2）**对比验证信号**，将干预结果作为强监督信号，而非单纯依赖静态评分。这一方法的关键创新在于，它让审计者从“观察者”变为“实验者”——通过主动试错获取因果证据来修正自身判断。实验表明，该方法在结构化工具使用痕迹上的归因准确率提升最大，且无需真实答案即可实现可操作的错误定位。

### Q4: 论文做了哪些实验？

论文在四个基准测试上进行了实验：WTQ（表格问答）、GAIA（多跳推理）、BBM（思维链验证）和SWE-bench（软件工程）。实验设置使用gpt-5.2作为审计器和代理，并采用确定性验证（字符串匹配、特定任务提取或测试套件）。对比方法包括八种基线，涵盖提示型（AAO、SBS、BS）、修正型（ICS、Reflexion）、评分型（AgentRx、ThinkPRM）和修正验证型（DoVer）。

主要结果如下：在定位准确率（Exact Match）上，REFLECT在所有四个基准上均取得最高分：WTQ达76.3%（远超AAO的55.5%），GAIA为39.0%（远超Reflexion+GT的16.2%），BBM为34.5%（与Reflexion+GT的34.0%持平），SWE-bench达70.0%（远超Reflexion+GT的45.2%）。在修正-定位耦合实验中，REFLECT修正后的解释相似度（Sim-c）为0.48-0.61，远高于修正失败的0.23-0.32，差距Δ达+0.25至+0.29，而ICS和Reflexion的Δ均≤+0.05。在受控干预实验中，注入正确提示比无提示提升42个百分点（78.7% vs 35.6%），证实目标干预的有效性。在代理设置下，REFLECT仍保持大部分性能（WTQ：62.2%，SWE-bench：66.1%），且优于多数基线。消融实验显示，诊断器对修正贡献最大（平均+27.8个百分点），后修正再定位提升EM达10.6个百分点。

### Q5: 有什么可以进一步探索的点？

REFLECT的核心局限在于其干预机制对纯思维链（CoT）轨迹的效果较弱，因为此类场景缺乏结构化工具调用产生的明确中间变量（如API返回值、数据库查询结果），导致“诊断-补丁-验证”的因果信号模糊。未来可探索以下方向：1）为CoT轨迹引入更细粒度的“心理模拟”干预——通过让LLM生成候选步骤的替代推理路径（如“如果第k步选择不同假设，后续逻辑会如何变化”），对比结果向量差异来近似干预信号；2）构建无oracle的验证器，例如利用LLM自身对干预前后整体轨迹的一致性评分（如“修复后轨迹是否更自洽”）替代真实答案的翻转检测；3）改进replay策略，对工具调用类错误可冻结下游上下文仅重放目标步骤，而对隐式错误需设计逐步回溯式replay（如从失败点反向删除证据链），以增强非结构化场景下的归因信噪比。

### Q6: 总结一下论文的主要内容

该论文针对大型语言模型智能体在“静默故障”场景下难以定位错误步骤的问题，提出了REFLECT方法。静默故障指智能体执行轨迹无异常信号但最终答案错误。现有方法要么仅预测错误步骤而无法验证，要么通过重试获得正确结果却未归因于原始错误。REFLECT的核心贡献是实现闭环的、基于因果验证的错误归因。其方法分为三步：首先诊断候选错误步骤并生成修复方案；然后通过受控回放注入针对性补丁，保持轨迹前缀不变以验证修复是否改变最终结果；最后利用原始与修正轨迹的对比证据精炼归因。在四个涉及多跳推理、结构化工具使用的基准上，REFLECT在同类审计方法中达到了最高定位准确率，尤其在结构化工具轨迹上提升显著，且即使无真实答案仍能提供有效定位。这项工作弥合了“纠正”与“归因”的差距，通过实验验证而非仅凭推理来定位错误，显著提升了LLM智能体在复杂任务中的可调试性和可靠性。
