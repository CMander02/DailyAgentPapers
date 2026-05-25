---
title: "DART: Semantic Recoverability for Structured Tool Agents"
authors:
  - "Ke Yang"
  - "Panpan Li"
  - "Zonghan Wu"
  - "Kejin Xu"
  - "Huaxi Huang"
  - "Xiaoshui Huang"
date: "2026-05-22"
arxiv_id: "2605.23311"
arxiv_url: "https://arxiv.org/abs/2605.23311"
pdf_url: "https://arxiv.org/pdf/2605.23311v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Tool Use"
  - "Error Recovery"
  - "Runtime Framework"
  - "Semantic Correctness"
relevance_score: 8.5
---

# DART: Semantic Recoverability for Structured Tool Agents

## 原始摘要

When a structured tool agent fails mid-execution, the runtime faces a dilemma: replaying the entire task is safe but wasteful, while restoring from a local checkpoint is efficient but can leave committed downstream work tied to an upstream history that no longer exists. This tension is acute in commitment-sensitive settings, where rollback targets a single failed instance yet downstream consumers have already acted on its output. Existing recovery approaches provide mechanical rollback but no criterion for whether a local restore remains semantically valid after downstream commitment. We formalize this gap as semantic recoverability and address it in DART, a modular runtime that localizes the failed instance, certifies semantically recoverable boundaries of that instance, aligns checkpoints to those boundaries, and selects an admissible restore point that preserves committed downstream work under dependency and effect constraints-or blocks otherwise. Across three LLM-driven domains and external validation on a LangGraph-based substrate, DART correctly recovers all evaluated commitment-sensitive cases where baseline local recovery fails, and a five-domain safety audit finds no unsafe admitted rollbacks. These results show that controller legality does not imply semantic validity, and that sound local recovery requires an explicit admissibility check.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决结构化工具智能体在执行过程中发生故障时，现有恢复机制存在的语义有效性问题。在大型语言模型驱动的生产系统中，智能体常作为结构化工具使用，其执行流程由显式控制流、可观测动作边界和持久化轨迹组织。现有恢复方法（如工作流异常处理、事务快照、LangGraph等智能体运行时）主要提供机械化的回滚能力，但缺乏对“语义可恢复性”的判定标准，即恢复后的执行状态在考虑到下游已提交工作后是否依然语义有效。这导致了一个核心困境：全任务重放安全但低效，局部恢复高效但可能使已提交的下游任务（如已发送的日程邀请）基于一个不再存在的上游历史，从而产生语义无效的执行。现有方法认为“控制器合法”（即运行时能机械恢复状态）就足够，但本文指出这并不保证语义有效性。因此，本文的核心问题是：在结构化工具智能体中，如何判定一个局部回滚不仅是控制器合法的，而且是语义有效的？论文通过形式化语义可恢复性概念并设计DART运行时来解决此问题。

### Q2: 有哪些相关研究？

- **方法类**：经典工作流系统研究异常处理与作用域（如异常范围），运行时修复工作引入引导式、监控驱动的恢复机制，自愈流程修复扩展至自适应工作流修正。这些方法要求预先定义恢复单元（如活动或服务级区域），而本文DART需运行时动态识别失败语义实例，再决定本地恢复。
- **应用类**：分布式快照与回滚恢复协议、事务导向恢复及嵌套事务、Saga和幂等模式等处理跨边界一致性。它们预设回滚作用域（如事务或检查点级别），但未询问本地恢复在依赖与副作用约束下是否语义可接受；本文关注控制器合法恢复是否语义有效。
- **评测类**：LangGraph等现代图运行时提供持久化与中断原语，Step Functions和Ray提供重试容错，SagaLLM为多智能体规划添加事务保证。这些系统使结构化恢复更实用，但将正确性隐式视为可重试即可；DART隔离出缺失的语义层——判断控制器合法恢复点是否沿下游承诺与副作用边界仍可接受。

### Q3: 论文如何解决这个问题？

DART通过一个四层流水线解决结构化工具代理在失败时的语义可恢复性问题。整个框架围绕四个核心问题展开:失败实例定位、可恢复边界认证、实例对齐检查点和可接受回滚选择。

首先，在实例定位层，运行时通过解析有限状态机状态、工具参数和边车注册表，将观察到的失败映射到唯一的子任务实例(k,η,o)，若无法唯一确定则保守地回退到全局重跑。第二层是边界认证，基于预定义的"最小恢复契约"对候选生命周期的提交/退出状态进行四重验证:可判定性(实例仍唯一可识别)、封闭性(语义交接完整)、可分离性(重放局限于该实例)和可控性(效果策略允许回滚)，只有全部通过才认证为可恢复边界。第三层是检查点对齐，将认证的边界具体化为绑定到该实例的稳定检查点(入口、提交、退出三种类型)，确保后续恢复搜索局限于该实例的检查点集。最后一层是可接受选择，在依赖和效果约束下评估哪些稳定检查点是安全的:通过生产者-消费者关系判断不会破坏已提交的下游消费者，通过冻结的效果策略检查未跨越不可逆效果边界，然后选择最新的可接受检查点进行本地回滚，若无可接受点则拒绝本地恢复。

关键创新在于:首次形式化定义了语义可恢复性，将其与控制器合法性分离，并设计了一套守卫函数确保回滚不会在语义上破坏已提交的下游工作。

### Q4: 论文做了哪些实验？

论文在三个LLM驱动领域（导航、日程表单、诊断）和两个确定性领域（ETL流水线、旅行规划，见附录）上评估了DART。实验比较了四种恢复策略：全任务重跑（Retry-Only）、粗粒度状态恢复（Coarse-State-Retry）、仅失败实例入口点恢复（Comp-EntryOnly）以及DART的已审查可接收恢复（CompFrozen）。主要指标包括成功率、恢复观察率、失败到里程碑延迟、重放动作数、上游重放数和保留的已完成实例数。在承诺敏感场景中，Comp-EntryOnly在所有核心领域均失败：导航中出现合同违反（成功率为0.00），日程表单和诊断中未观察到本地恢复（成功率为0.00）。而DART在所有承诺敏感情况下均成功恢复（成功率1.00），且重放步数最少（1-2步），延迟最低（1141-2527毫秒）。在官方标头案例中，DART与基线性能相当，但显著减少上游重放。跨运行时的外部验证（LangGraph）显示，在日程表单的承诺敏感案例中，LangGraph恢复失败（成功率0.00），而DART成功（成功率1.00）。安全审计覆盖54个可比行和47个恢复事件，所有35个已批准恢复均语义安全，12个被阻止的恢复无假阳性，表明DART的语义可恢复性检查有效且保守。

### Q5: 有什么可以进一步探索的点？

论文的局限性在于其验证范围局限于显式状态机控制器和可观测错误恢复场景，尚未探索隐式控制流（如LLM自主调用工具）或非可观测错误（如数据污染）下的语义可恢复性。未来方向可拓展至：（1）将依赖抽象扩展至异步和分布式场景，处理跨进程的副作用一致性；（2）开发自动边界配置机制，避免人工审查的开销与主观误差；（3）研究适应性可恢复性策略，在完全重放与局部恢复间动态权衡，例如基于错误传播概率选择恢复粒度；（4）结合因果推断模型预测下游依赖的语义兼容性，突破当前严格的依赖约束限制。此外，可考虑引入概率性可恢复性认证，允许在低风险场景下放宽语义一致性条件以换取效率提升，但需配套安全审计框架。

### Q6: 总结一下论文的主要内容

论文解决了结构化工具智能体在部分执行失败后，如何在保留已提交下游工作的前提下进行语义有效恢复的问题。现有方法只提供机械回滚，但缺乏判断局部恢复是否仍具有语义正确性的标准。DART将这一差距形式化为语义可恢复性问题，并提出模块化运行时，通过失败实例定位、可恢复边界认证、实例对齐检查点和可接受回滚点选择四个步骤，在依赖和效果约束下选择既能保留下游工作、又语义正确的恢复点，否则阻止恢复。实验表明，在三种LLM驱动领域和基于LangGraph的外部验证中，DART在基准局部恢复失败的所有关键承诺敏感场景下都能正确恢复，且五领域安全审计未发现不安全的回滚。核心贡献在于揭示了控制器合法性不等于语义有效性，证明了可靠的局部恢复需要明确的可接受性检查。
