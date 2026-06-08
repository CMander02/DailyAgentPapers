---
title: "Queen-Bee Agents: A BeeSpec-Centered Architecture for Governed Enterprise MCP Orchestration"
authors:
  - "Dutao Zhang"
  - "Liaotian"
date: "2026-06-04"
arxiv_id: "2606.06545"
arxiv_url: "https://arxiv.org/abs/2606.06545"
pdf_url: "https://arxiv.org/pdf/2606.06545v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "多智能体架构"
  - "企业Agent"
  - "MCP编排"
  - "治理与策略执行"
  - "工具使用"
  - "检索增强生成"
  - "审计回溯"
relevance_score: 8.5
---

# Queen-Bee Agents: A BeeSpec-Centered Architecture for Governed Enterprise MCP Orchestration

## 原始摘要

Enterprise agent systems increasingly need to connect large language models to private tools, internal knowledge, and Model Context Protocol (MCP) interfaces. In this setting, raw task capability is insufficient: organizations also require policy enforcement, tenant-scoped isolation, and execution that remains within explicit operational boundaries. We present Queen-Bee, a governed multi-agent architecture in which a Queen control plane retrieves capabilities, plans task-scoped execution, and compiles a structured BeeSpec that is executed by specialized Bee agents under constrained tool access. We implement a working prototype with tenant-scoped MCP connectors, audit-backed execution-time governance, retrieval-driven weak incubation, and multiple provisioning backends. We evaluate the system on 59 enterprise-style tasks spanning governance-sensitive requests, retrieval-driven provisioning, scoped local execution, and chemistry workflow integration. The retrieval-driven Queen-Bee variant achieves a task success rate of 0.964, zero governance failures, and substantially better scoped execution quality than both a static Queen-Bee baseline and a permissive single-agent baseline. We further show a multi-Bee chemistry workflow with explicit approval gating and a concrete top-3 shortlist grounded in real upstream evidence and screening artifacts. Additional comparisons with hybrid retrieval and LLM-guided provisioning show that richer provisioning backends are viable but do not outperform the lightweight structured retriever on the current small, highly structured capability registry. The results provide prototype-level systems evidence rather than a production deployment study, and suggest that enterprise agent platforms should be evaluated not only by capability, but also by governed provisioning, isolation behavior, scoped execution quality, and artifact-aware workflow coordination.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决企业级MCP（模型上下文协议）环境中大型语言模型代理系统的治理与安全执行问题。研究背景是，当前基于LLM的代理系统虽能调用工具、访问资源并执行工作流，但在企业私有MCP环境中存在根本性不足：现有方法（特别是单代理设计）将广泛能力与宽泛权限耦合，导致代理可能调用错误工具、跨越租户边界或违反审计要求，即使任务结果看似正确，在操作上也是不可接受的。研究指出现有方法的三点不足：1）单代理架构缺乏对部门边界、租户隔离、工具治理等企业约束的内生支持；2）现有多代理协调研究侧重能力分解而非执行边界控制；3）缺乏统一的规划与执行分离机制。本文要解决的核心问题是：如何设计一个受治理的多代理架构，使得系统在完成任务能力的同时，能够强制执行策略约束、实现租户范围隔离、确保执行始终在明确操作边界内运行。通过引入Queen控制平面和BeeSpec结构化中间表示，将能力检索、任务规划与受约束执行解耦，从而在保持高任务成功率的同时实现零治理失效。

### Q2: 有哪些相关研究？

根据论文相关章节，相关研究主要可分为方法类和应用类。在方法类中，**Toolformer**和**ReAct**展示了工具使用与推理-行动耦合的两种互补方向，而**ToolLLM**将这一趋势扩展到大型API生态，侧重于广泛的工具覆盖而非受控的企业执行。本文与这些工作的区别在于，Queen-Bee聚焦于有边界的、受治理的企业执行环境。在应用类中，**AutoGen**和**CAMEL**等框架展示了角色专业化代理可协调复杂任务，但它们未解决租户隔离、工具治理或显式执行边界编译问题。与之对比，本文更接近软件架构和访问控制传统，其治理层借鉴了基于角色的访问控制和可强制执行策略思想，而**BeeSpec**抽象明确分离了控制平面规划与执行平面行动。总体而言，相关研究侧重于能力扩展和开放协作，而本文的创新在于将治理、审计和工作流协调显式化与可检查化，目标不是最大化代理可触及的工具数量，而是实现可控的能力分配与分阶段执行。

### Q3: 论文如何解决这个问题？

Queen-Bee通过四层分离架构解决企业级MCP编排中的治理与隔离问题。核心思路是将控制与执行解耦，由Queen控制平面负责全局决策，通过BeeSpec中间层严格约束Bee Agent的执行边界。

**整体框架**包含四层：1) Queen控制平面，执行能力检索（从MCP和技能注册表获取可用工具）、蓝图规划（生成任务执行方案）、BeeSpec编译（生成结构化执行规范）及运行时治理（策略检查与审计日志）；2) BeeSpec中间层，定义每个Bee的执行边界，包含bee_id、角色、领域、租户域、内存域、附加技能、允许工具、策略配置及审批关卡等字段；3) Bee执行平面，每个Bee在BeeSpec约束下使用附加技能生成本地工具调用计划，仅调用被授权的MCP工具；4) 租户域MCP连接器层，将工具调用解析到当前租户作用域内。

**主要模块**：Queen作为非执行性控制器，专注于策略级决策；Bee作为领域化执行单元（原型中限定HR和IT域），在策略层授权后才能调用工具。**创新点**：1) BeeSpec作为规划与执行的硬边界，通过结构化记录永久解耦“谁允许做什么”与“实际做什么”，使路由、审计和策略强制可解释；2) 弱孵化机制通过检索驱动能力注册，实现轻量级工具搭配；3) 运行时审计回溯和多租户隔离，确保每次工具调用都经过策略检查并记录到审计日志；4) 审批关卡支持跨工作流人工审核（如化学工作流中的多步审批）。该系统在59个企业任务上达到0.964成功率与零治理失败。

### Q4: 论文做了哪些实验？

该论文在59个企业级任务上进行了实验，任务分为两个租户：24个常规HR和IT任务、16个治理敏感任务（财务敏感和跨租户）、16个限定执行任务（仅需部分本地工作流）和3个化学工作流任务。对比了七种系统：Queen-Bee静态版、检索版、压力检索版、混合检索版、LLM配置版、无策略版以及单智能体基线版。关键实验结果包括：检索驱动的Queen-Bee变体在治理指标上表现完美（财务防护栏拦截率、跨租户请求拦截率和租户范围准确率均为1.0），任务成功率达到0.964，错误工具调用仅1次，而静态版任务成功率为0.857，错误工具调用4次；无策略版和单智能体基线在治理敏感任务上完全失败（两项拦截率均为0.0），任务成功率仅0.571，错误工具调用达16次。在检索驱动配置中，检索工具覆盖率为1.000，精度达0.979，技能激活率为1.000。在限定执行方面，检索版Bee执行完成度达0.95，显著优于静态版的0.80。此外，在化学工作流中，检索版成功恢复预期工具链，而静态版过度执行。噪声扩展实验表明检索器鲁棒性良好。

### Q5: 有什么可以进一步探索的点？

基于论文的局限性和当前技术趋势，未来可从以下方向深入探索：首先，将合成任务集替换为真实企业生产环境数据，验证系统在动态业务流中的鲁棒性；其次，将本地演示MCP服务器升级为异构实时业务系统（如ERP、CRM），解决适配器层到商业系统的实际延迟与权限冲突问题；此外，当前基于规则的治理模型可引入动态策略学习，通过强化学习自动修正审批阈值，减少人工干预；针对注册表噪声，可设计对抗性能力进化测试，模拟开放世界中新工具、新权限的突发注册与冲突消解。结合自身的见解，一个关键改进点是构建“多层级隔离的沙箱执行框架”，让Bee代理在执行BeeSpec时能按工具敏感度分级回滚，避免单一工具级约束导致的流程死锁。同时，跨租户审计追踪的细粒度化（如工具调用链的因果溯源）可能成为从原型到生产部署的核心突破口。

### Q6: 总结一下论文的主要内容

这篇论文提出了Queen-Bee架构，一种以BeeSpec为中心的受治理企业MCP编排系统。核心问题在于企业级代理系统不仅需要原始任务能力，还必须满足策略执行、租户隔离和受限执行等治理需求。方法上，该系统设计了一个Queen控制平面，负责检索能力、规划任务并编译结构化的BeeSpec，然后由专门的Bee智能体在受限工具访问下执行该规范。原型系统实现了租户隔离的MCP连接器、审计执行时治理、检索驱动的弱孵化以及多种配置后端。在59项企业风格任务上的评估表明，基于检索的Queen-Bee变体在任务成功率（0.964）、零治理失败和更高范围的执行质量上，显著优于静态Queen-Bee基线和宽松的单智能体基线。研究还展示了多Bee化学工作流中带有明确审批门控的分阶段协作。主要结论是，企业代理平台不仅要评估任务能力，还应评估受治理的配置、隔离行为、限定执行质量和工件感知的流程协调，为系统设计提供了原型级的证据。
