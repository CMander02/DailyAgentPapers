---
title: "AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents"
authors:
  - "Hailin Zhong"
  - "Shengxin Zhu"
date: "2026-05-13"
arxiv_id: "2605.13357"
arxiv_url: "https://arxiv.org/abs/2605.13357"
pdf_url: "https://arxiv.org/pdf/2605.13357v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Software Engineering Agent"
  - "Agent Runtime Architecture"
  - "AI Harness"
  - "Agent Evaluation Protocol"
  - "Foundation Model Agent"
relevance_score: 9.5
---

# AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents

## 原始摘要

Foundation models have transformed automated code generation, yet autonomous software-engineering agents remain unreliable in realistic development settings. The dominant explanation locates this gap in model capability. We propose a different locus: software-engineering capability emerges from a model-harness-environment system, in which a runtime substrate -- the harness -- mediates how a foundation-model agent observes a project, acts on it, receives feedback, and establishes that a change is complete. We formalize this substrate as an AI Harness Engineering and identify eleven component responsibilities: task specification, context selection, tool access, project memory, task state, observability, failure attribution, verification, permissions, entropy auditing, and intervention recording. We operationalize the harness through a four-level ladder (H0-H3) that progressively exposes runtime support to the agent, and we propose a trace-based evaluation protocol that converts each agent run into an auditable episode package. Applied to a controlled validation task, the framework yields episode packages whose evidence structure varies systematically with harness level: lower levels produce only a final patch, higher levels produce reproduction logs, failure attributions, deterministic requirement checks, and structured verification reports. The framework reframes the central question of autonomous software engineering from whether a foundation model can produce a patch to whether the model-harness-environment system can produce a verifiably correct, attributed, and maintainable change. We outline a research program for the runtime systems that foundation-model software agents will require.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前自主软件工程智能体在真实开发环境中不可靠的核心问题。研究背景是，尽管基础模型在代码生成方面取得了快速进展，但在需要长期规划、状态管理、工具使用和反馈驱动的完整软件工程任务中，这些智能体的表现却远低于预期。现有方法（主流观点）将这种差距归因于模型自身能力的不足，认为只要训练出更强的模型或更复杂的循环就能解决问题。

本文提出一个不同的观点：自主软件工程能力并非仅来自模型，而是源于“模型-支架-环境”这一整体系统。作者指出现有方法的不足在于忽视了运行时支架（Harness）的关键作用。在现有系统里，原本由人类开发者隐式提供的运行时支持（如上下文管理、项目记忆、工具接口、验证、权限等）对智能体而言往往是隐晦、不可访问或不稳定的，导致智能体频繁出现文件定位错误、测试误读、验证不足等问题。

因此，本文要解决的核心问题是：如何通过一个形式化定义的运行时支架系统（即AI Harness Engineering），来系统性弥合模型局部编码能力与完整软件工程能力之间的“自主性差距”，并使得这个支架的贡献可被分离、评估和优化。

### Q2: 有哪些相关研究？

根据论文内容，相关研究主要分为以下几类：

1. **模型能力提升类**：现有研究普遍将代码智能体失败归因于模型能力不足（如编码、推理、规划能力），主张通过训练更强模型或更复杂的智能体循环来解决问题。本文不否认模型能力的重要性，但认为该视角不完整，提出将软件工程能力视为模型-支架-环境系统的涌现属性，而非模型单点能力。

2. **智能体框架与接口类**：论文明确区分了其提出的“AI支架工程”与“智能体-计算机接口”、“智能体框架”和“智能体操作系统”等现有概念。这些相关工作侧重于智能体与环境的交互方式或通用框架设计，而本文聚焦于运行时中间件的具体组件职责（如任务规范、上下文选择、工具访问、项目记忆等11项），并提出了H0-H3分级支架梯度和基于轨迹的评估协议。

3. **工业实践与部署类**：OpenAI关于Codex的实践和微软关于智能体支架的报告已涉及上下文管理、仓库知识、可观测性等类似支架结构，但未将其作为独立研究对象，未定义组件、分级或规定轨迹证据结构。本文在此基础上系统化了该方向。

4. **评测基准与协议类**：现有基准（如SWE-bench）主要衡量最终补丁正确性，而本文提出更细粒度的评估协议（8类执行证据），按验证自主性而非单纯任务成功来评判智能体运行，将评估重心从“模型能否生成补丁”转向“系统能否生成可验证、可归因、可维护的变更”。

### Q3: 论文如何解决这个问题？

该论文提出了一种名为“AI Harness Engineering”的运行时基板方法，来解决基础模型在软件工程代理中表现不可靠的问题。核心方法将软件工程能力定位为“模型-约束-环境”系统的涌现属性，而非单一模型的编码能力。

整体框架是一个四层级的H0-H3递进约束阶梯。H0为最小基线，仅有任务描述和仓库文件；H1加入工具注册表、测试命令注册表和工具使用协议，使动作表面显式化；H2增加项目记忆、任务状态文件和上下文选择协议，管理认知资源；H3加入确定性检查、错误复现、失败归因和验证协议，使完成具备可验证证据。

关键技术包括十一项组件责任：任务接口、上下文管理器、工具注册表、项目记忆、任务状态、可观测层、失败归因、验证协议、权限边界、熵审计和干预记录器。这些组件管理类似操作系统的运行时资源，如上下文预算、工具预算、验证证据等。

创新点在于：提出基于痕迹的评估协议，将每次代理运行转化为可审计的“情节包”，包含八类痕迹（动作、工具、上下文、验证、失败归因、干预、熵审计、结果），并采用五标签结果分类法（自主验证成功、辅助验证成功、未验证成功、失败、不安全无效）。该方法从“模型能否生成补丁”转向“系统能否产生可验证、可归因、可维护的变更”，使运行支持的效果可分离、可消融、可比较。

### Q4: 论文做了哪些实验？

该论文在受控验证任务 repoA-T1 上进行了实验。实验设置包含一个登录应用，其缺陷为无法拒绝空密码。任务要求修改应用，使空密码返回包含"Password is required."的验证错误，同时保持其他行为不变。实验使用了四种对比方法，对应不同的 Harness 级别：H0、H1、H2 和 H3。主要结果如下：所有四个级别都产生了可工作的补丁，但生成的证据包在结构上存在系统性差异。H0 产生补丁、评估端确定性检查通过和完整回归成功；H1 产生补丁、工具跟踪、目标测试、lint，但完整回归超时；H2 在 H1 基础上增加了项目记忆的上下文跟踪和任务状态更新；H3 在 H2 基础上增加了 bug 复现日志、失败归因日志、确定性需求检查和结构化验证报告。H3 的独特之处在于其五步工作流：复现→归因→修复→验证→报告，能将任务完成转化为结构化的证据对象。关键数据指标显示，H1-H2 的结果被记录为“未验证成功”，而 H0 和 H3 为“自主验证成功”。

### Q5: 有什么可以进一步探索的点？

论文将自主软件工程的核心问题从“模型能否生成补丁”重新定义为“模型-工具-环境系统能否产生可验证、可归因、可维护的变更”，这一框架的局限性在于：**验证功能被完全内部化至工具层**，但当前的模型自身尚不具备完备的自我验证能力，H3级别要求模型再现失败、归因、检查需求并报告证据，这实际上对模型推理的理性程度和诚实性提出了过高要求。未来研究方向可包括：**构建混合验证架构**，将确定性检查（如形式化规约、回归测试）与模型驱动的启发式验证（如自然语言需求匹配）结合，降低对模型完全自证的依赖。  
**记忆的可审计性**（context trace）目前只记录了被查询的工件，但未解决“记忆污染”与“选择性遗忘”问题：当上下文窗口过长时，模型可能忽略关键记忆碎片。改进思路是引入**记忆重要性排序与衰减机制**，通过强化学习或注意力权重分析自动识别哪些记忆对当前决策有贡献。  
**熵审计**（entropy auditor）虽然识别了冗余代码、弱化测试等“残留物”，但**缺乏对熵积累速度的量化预警**。未来可结合代码库的静态分析指标（如圈复杂度、模块耦合度）与运行时变更日志，开发一个**熵预算控制器**，在代理每完成一个任务后自动计算“技术债务增量”，若超过阈值则触发重构要求。  
此外，**工具稳定性**（tool stability）在文中被定性为工具问题，但现实中**不稳定源于环境本身**（如网络延迟、随机化测试）。一个实际改进是设计**基于概率的决策后验检查**：当命令返回状态码成功但日志包含可疑模式时，工具层应自动重试或回滚，并将该事件作为稳定性证据记录到 episode package 中。最后，**从H0到H3的阶梯**目前是单向的，但更实用的系统可能需要**自适应等级切换**：在简单任务中降低验证开销，在关键变更中自动升级到H3。这要求未来研究开发一个**元工具**，根据任务复杂度、模型置信度和环境噪声动态选择工具等级。

### Q6: 总结一下论文的主要内容

本文定义了AI Harness Engineering，认为自主软件工程能力是模型-框架-环境系统的涌现属性，而非单纯模型能力。框架识别了11个组件责任（任务规范、上下文选择、工具访问、项目记忆、任务状态、可观测性、失败归因、验证、权限、熵审计和干预记录），并提出H0-H3四级框架梯，逐步暴露运行时支持给智能体。通过基于轨迹的评估协议，将每次运行转换为可审计的情节包。在验证任务上，框架梯级别越高产生的证据结构越系统：H0只产生最终补丁，而H3产生复现日志、失败归因、确定性需求检查和结构化验证报告。核心意义是重新框定核心问题从“模型能否产生补丁”变为“模型-框架-环境系统能否产生可验证、可归因、可维护的变更”。
