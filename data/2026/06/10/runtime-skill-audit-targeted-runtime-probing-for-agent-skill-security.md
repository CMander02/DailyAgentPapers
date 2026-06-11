---
title: "Runtime Skill Audit: Targeted Runtime Probing for Agent Skill Security"
authors:
  - "Tu Lan"
  - "Chaowei Xiao"
date: "2026-06-10"
arxiv_id: "2606.11671"
arxiv_url: "https://arxiv.org/abs/2606.11671"
pdf_url: "https://arxiv.org/pdf/2606.11671v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "LLM Agent 安全"
  - "Agent 技能审计"
  - "动态分析"
  - "Agent 安全评测"
  - "运行时监测"
relevance_score: 8.5
---

# Runtime Skill Audit: Targeted Runtime Probing for Agent Skill Security

## 原始摘要

Agent skills let LLM agents reuse instructions, resources, tools, and workflows, but they also create a new place for malicious behavior to hide. A skill may look benign in its documentation or code while becoming harmful only when it is invoked with particular user requests, local assets, persistent state, or multi-step tool interactions. This makes purely static vetting brittle. We present Runtime Skill Audit (RSA), a dynamic analysis method that audits skills by asking what the skill-mediated agent actually does under targeted runtime conditions. Instead of testing every skill with the same generic tasks, RSA profiles risk-relevant interfaces, prepares the execution context needed to exercise them, and assigns security labels from the resulting trace evidence. We instantiate RSA on OpenClaw and evaluate it on 100 skills against representative static baselines. RSA achieves 90.0\% accuracy with an 88.0\% true positive rate and an 8.0\% false positive rate, improving accuracy by 13.0 percentage points over the best static baseline. Under self-evolving attacks, static detectors collapse after one or two rounds, while RSA continues to detect 19--20 out of 20 malicious skills across rounds.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决LLM代理技能安全评估中的核心问题：现有静态分析方法无法有效检测依赖于运行时上下文的恶意行为。研究背景是，随着OpenClaw、Claude Code等高自主性LLM代理的普及，代理技能作为能力扩展机制被广泛采用，但也引入了新的安全风险。恶意技能可能在其文档和代码中表现正常，仅在特定用户请求、本地资产、持久状态或多步工具交互等特定执行条件下才暴露有害行为。

现有方法如基于模式的匹配和LLM指令评判存在明显不足：它们依赖于对技能工件的静态分析，无法判断规则是否实际执行、访问了哪些文件，或者良性工作流在运行时上下文中是否变得有害。例如，一个文件整理技能可能包含一个看似无害的“选择.json文件并发送审查”的规则，但只有在其运行环境中存在敏感文件（如auth.json）时，恶意行为才会显现。

本文提出的Runtime Skill Audit（RSA）是一种动态分析方法，通过风险导向的概要分析、上下文感知的运行时执行和轨迹证据判断，在目标运行时条件下审计技能的实际行为。核心思路是将技能审查从工件级检查转变为行为级审计，从而解决静态分析在检测隐藏、上下文依赖或自适应重写攻击时的脆弱性。

### Q2: 有哪些相关研究？

相关研究主要分为三类。首先是**预执行检测方法**，包括基于规则或形式化分析的方法，通过检查技能定义、依赖和组合约束来在部署前发现潜在不安全组合；以及基于大模型的审查方法，如结合工件分析与语义安全评估的生态级方法，或多智能体审计方法，它们检查语义-行为对齐性。这些方法对表面信号有效，但受限于工件级证据，无法捕获仅在运行时上下文（如特定用户请求、持久状态）下触发的恶意行为。

其次是**运行时痕迹分析方法**，相关工作将痕迹抽象为结构化执行单元并检查行为约束，或建模依赖关系以检测工具使用和元数据污染传播。本文方法与这些工作接近，均视运行时行为为核心证据，但区别在于前者侧重于对痕迹的异常检测，而本文通过生成针对性的运行时探针，在真实任务上下文中主动判断技能是否表现出恶意行为，实现主动审计。

此外，相关工作还揭示了恶意技能的已有攻击模式，如通过持久化代理状态（知识与记忆）嵌入恶意行为，或在看似正常的技能文件中注入依赖上下文的攻击，这进一步印证了静态审查的局限性，凸显了本文动态分析方法的必要性。

### Q3: 论文如何解决这个问题？

RSA通过动态分析方法审计技能安全，核心方法分为三个阶段。首先，风险引导任务生成阶段：系统使用LLM将原始技能工件转换为结构化安全画像，通过分析技能可能调用的平台工具，将其映射到文件访问、shell执行、Web交互、内存访问和会话控制等安全相关能力组。画像记录技能的良性目的、工具界面、敏感资源和攻击模式，为后续测试提供针对性接口而非通用任务列表。

其次，沙盒执行与痕迹收集阶段：RSA为每个生成的任务准备包含相关文件、目录、模拟凭证和持久状态的运行时上下文，在隔离的OpenClaw环境中执行。系统记录完整的代理动作、工具调用和可观察副作用的结构化轨迹。通过自修复循环处理因任务准备不完全导致的执行失败，并针对沙盒无法直接支持的外部应用使用确定性虚假应用垫片（如模拟Gmail命令）来保留行为证据。

最后，轨迹驱动评估阶段：评估器基于执行轨迹而非工件本身分配安全标签，检查良性目标是否完成、风险表面是否被触及以及观察到的动作是否显示安全相关误用。系统使用四种判定结果：良性执行、有害被阻断、有害执行和不确定。支持组件包括知识库（含工具分类学、风险映射和攻击模式模板）和记忆模块（存储有效触发器、假阳性和遗漏恶意行为的摘要）。创新点在于动态上下文感知测试，能发现仅在特定用户请求、本地资产或持续状态下显现的恶意行为，相较静态基线在自进化攻击下保持90%准确率，而静态检测器在一两轮后即失效。

### Q4: 论文做了哪些实验？

论文在OpenClaw平台上进行了三项实验。首先，在包含50个恶意和50个良性技能的100技能数据集上，对比了Aguara、通用/定制Semgrep规则、ClawScan、OpenClaw Skill Scanner及其LLM变体等静态基线方法。RSA取得了90.0%的准确率，真阳性率（TPR）为88.0%，假阳性率（FPR）为8.0%，相比最佳静态基线（SkillScanner的77.0%准确率）提升13个百分点。其次，在自进化攻击实验中，从20个恶意种子技能出发，通过多轮变异规避检测，静态检测器（如Skill Scanner与Aguara）在1-2轮后性能崩溃（降至0%），而RSA稳定保持检测19-20个恶意技能。最后，消融实验评估知识引导组件：完整RSA相比无知识版本，TPR从82.0%提升至88.0%，FPR从16.0%降至8.0%，准确率从83.0%升至90.0%。

### Q5: 有什么可以进一步探索的点？

首先，RSA的实验验证仅基于100个OpenClaw技能，样本覆盖了多种良性类别与攻击模式，但未充分代表所有智能体技能生态系统或高自主性平台。未来的研究应扩展到更多样化的技能库，例如真实世界攻击案例，以验证方法的泛化能力。其次，RSA依赖LLM进行子任务生成、执行上下文准备和痕迹判断，因此其质量受限于模型能力、提示设计和评估者一致性。可探索更鲁棒的LLM基于判定机制或结合静态分析来减少误报。此外，动态评估的非穷举性是核心局限：一个在当前生成任务下显得安全的技能，可能在未测试的输入、外部状态或长程交互中触发恶意行为。未来工作可引入更系统的探索策略，如基于梯度或模糊测试的输入变异，以提高覆盖率和检测隐蔽的时序触发功能。最后，可将RSA与静态审计持续集成，构建多层防御体系。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种针对大语言模型代理技能安全的动态分析方法——运行时技能审计（RSA）。问题定义在于，代理技能看似无害的文档或代码可能在特定用户请求、本地资源、持久状态或多步骤工具交互下才暴露恶意行为，使静态审查方法失效。方法上，RSA通过剖析技能的风险相关接口，准备必要的执行上下文，生成针对性运行时任务，在沙盒化环境中执行技能，并从执行痕迹中分配安全标签，而非对所有技能使用相同的通用测试。主要实验表明，RSA在100个技能上达到90.0%的准确率，真阳性率88.0%，假阳性率8.0%，比最佳静态基线提高13.0个百分点。在自适应进化攻击下，静态检测器一两轮后即失效，而RSA每轮仍能检测出19-20个恶意技能。该工作的核心贡献是提供了一个可复现的动态审计框架，用于研究恶意技能行为并评估防御措施，对保障技能增强型代理的安全性有重要意义。
