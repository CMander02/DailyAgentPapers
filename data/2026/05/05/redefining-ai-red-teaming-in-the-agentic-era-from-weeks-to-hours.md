---
title: "Redefining AI Red Teaming in the Agentic Era: From Weeks to Hours"
authors:
  - "Raja Sekhar Rao Dheekonda"
  - "Will Pearce"
  - "Nick Landers"
date: "2026-05-05"
arxiv_id: "2605.04019"
arxiv_url: "https://arxiv.org/abs/2605.04019"
pdf_url: "https://arxiv.org/pdf/2605.04019v1"
categories:
  - "cs.AI"
  - "cs.CR"
tags:
  - "Agent安全/红队"
  - "Agent工具使用"
  - "Agent工作流"
  - "单Agent系统"
  - "Agent评估"
relevance_score: 7.5
---

# Redefining AI Red Teaming in the Agentic Era: From Weeks to Hours

## 原始摘要

AI systems are entering critical domains like healthcare, finance, and defense, yet remain vulnerable to adversarial attacks. While AI red teaming is a primary defense, current approaches force operators into manual, library-specific workflows. Operators spend weeks hand-crafting workflows - assembling attacks, transforms, and scorers. When results fall short, workflows must be rebuilt. As a result, operators spend more time constructing workflows than probing targets for security and safety vulnerabilities.
  We introduce an AI red teaming agent built on the open-source Dreadnode SDK. The agent creates workflows grounded in 45+ adversarial attacks, 450+ transforms, and 130+ scorers. Operators can probe multi-agent systems, multilingual, and multimodal targets, focusing on what to probe rather than how to implement it.
  We make three contributions: 1. Agentic interface. Operators describe goals in natural language via the Dreadnode TUI (Terminal User Interface). The agent handles attack selection, transform composition, execution, and reporting, letting operators focus on red teaming. Weeks compress to hours. 2. Unified framework. A single framework for probing traditional ML models (adversarial examples) and generative AI systems (jailbreaks), removing the need for separate libraries. 3. Llama Scout case study. We red team Meta Llama Scout and achieve an 85% attack success rate with severity up to 1.0, using zero human-developed code

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前AI红队测试中低效且高度依赖人工的问题，其核心目标是实现从库中心到意图驱动的范式转变。随着LLM、多模态模型和AI代理进入医疗、金融、国防等关键领域，红队测试作为确保模型鲁棒性的主要方法变得至关重要。然而，现有方法（如PyRIT、Garak、Promptfoo）虽已扩展攻击技术库，却要求操作员手工编写代码、配置参数并解析输出，形成了“库中心”工作流。这导致操作员需要掌握深度技术专长，并花费数周时间手工构建集攻击、转换和评分于一体的工作流。更严重的是，当评估结果不理想时，工作流必须重建，使得操作员将大部分时间消耗在技术编排上，而非实际安全探测。

本文引入的AI红队测试代理逆转了这一关系，既解决了技术门槛高、工作流手动编排耗时的问题，又通过统一框架消除了传统ML模型与生成式AI系统需要不同工具库的割裂现状。其核心创新在于让操作员只需用自然语言描述目标（探测什么、为何探测、激进程度），系统便自动处理攻击选择、转换组合、执行与报告，将周级耗时压缩至小时级，真正实现了从“如何实现”到“探测什么”的焦点转移。

### Q2: 有哪些相关研究？

相关研究可分为以下几类：**方法类**包括开放盒攻击（如梯度优化的对抗后缀、多轮多模态扩展）和封闭盒攻击（如PAIR、TAP、Crescendo等迭代优化与树搜索方法），以及针对传统ML模型的梯度攻击（FGSM、PGD）和决策边界攻击（HopSkipJump）。**框架工具类**涵盖PyRIT、Garak、Promptfoo等生成式AI红队工具，以及Counterfit、ART、TextAttack等传统ML安全框架，它们均为库导向，要求用户手动配置工作流。**评测类**包括HarmBench、AIRTBench等标准化基准，用于评估攻击和防御效果。**自动化红队研究**如Rainbow Teaming、AutoRedTeamer通过质量-多样性搜索或双智能体系统实现攻击生成自动化，但未覆盖从目标定义到合规报告的完整流程。本文与上述工作的核心区别在于交互范式：现有框架要求用户学习API、手动组合攻击-变换-评分器，而本文提出的基于Dreadnode SDK的智能体通过自然语言接口（TUI）自动管理攻击选择、变换组合、执行与报告，将数周工作压缩至数小时。在攻击覆盖上，本文集成了45+攻击、450+变换和130+评分器，并通过Llama Scout案例验证了零代码实现85%攻击成功率的有效性。

### Q3: 论文如何解决这个问题？

论文通过引入一个基于Dreadnode开源SDK的AI红队智能体（Agent）来解决传统红队工作耗时、手动且碎片化的问题。其核心方法是将操作员从繁琐的“如何实现”中解放出来，专注于“探测什么”。整体架构分为两层：交互层和攻击层。交互层通过Dreadnode终端用户界面提供一个智能体接口，操作员用自然语言描述目标，智能体自动处理攻击选择、转换组合、执行和报告，将数周的工作缩短至数小时。攻击层包含三大核心组件：超过45种攻击策略、450+转换器以及130+评分器。智能体通过循环机制运行：收集上下文 → 调用底层模型推理攻击策略 → 派遣工具生成和执行攻击 → 收集结果进行分析。关键技术包括：1) 统一的框架，可以同时探测传统机器学习模型（如对抗样本）和生成式AI系统（如越狱），无需切换不同的库；2) 丰富的转换器库（包括确定性转换如Base64编码和LLM驱动的转换如语言翻译），用于系统性地探测模型安全对齐的薄弱点；3) 自动化的评分器，通过评估目标响应来判断攻击是否成功。创新点在于提供了一个统一的、智能体驱动的界面和生命周期（定义目标、执行攻击、分析结果、审查报告、迭代强化），使操作员无需编写任何代码即可完成复杂的红队任务。案例研究中，该方法在Meta Llama Scout上实现了85%的攻击成功率，严重性最高达1.0。

### Q4: 论文做了哪些实验？

论文通过两个核心实验验证了AI Red Teaming Agent的有效性。实验一：针对Meta Llama Scout模型的全自动红队测试。采用45+攻击模板、450+变换和130+评分器的组合，在零人工代码干预下，实现了85%的攻击成功率（ASR），最高严重性评分达1.0。通过Tree of Attacks with Pruning（TAP）和Prompt Automatic Iterative Refinement（PAIR）等策略，单次攻击仅需自然语言指令即可执行完整工作流（生成脚本→执行→收集结果→注册评估）。实验二：多模态/多语言目标探测。在医疗、金融等关键领域（非公开数据集）中，验证了同一框架对传统ML对抗样本和生成式AI越狱的统一处理能力。对比基线为传统的库导向工作流（需手动编写代码、配置参数、解析输出），新方法将数周操作压缩至数小时。关键发现：针对推理模型（如o1、DeepSeek-R1）推荐CoT Jailbreak策略，而Agentic系统（多智能体系统）需采用工具滥用攻击和MCP服务器毒化。所有操作通过Dreadnode TUI终端界面、CLI和SDK三通道提供一致输出（发现项、追踪迹、合规标签）。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三方面：一是当前45种攻击和130种评分器覆盖的攻击面仍有限，对多步跨域组合攻击（如结合语音伪造与视觉混淆）的支持不足；二是自动化流程可能遗漏人类专家能发现的隐晦漏洞（如逻辑链后门）。未来可探索的方向包括：引入基于强化学习的攻击策略自适应进化，让agent自动发现攻击序列的依赖关系；构建开放式攻击知识图谱，允许社区持续贡献新型攻击模式；结合因果推断技术识别模型脆弱性的深层原因。此外，建议将agent的反思能力增强为记忆回放机制，使其能从历史攻防案例中提炼可迁移的对抗模式。可改进的思路包括设计分层架构，上层用大语言模型进行战略性攻击规划，下层用规则引擎确保战术执行的规范性。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种基于智能体的AI红队测试系统，旨在将当前耗时数周的手动工作流压缩至数小时。核心问题是现有红队测试工具（如PyRIT、Garak）要求操作者手动编写代码、组合攻击库，导致大量时间耗费在工作流构建而非实际测试上。论文基于开源Dreadnode SDK构建了一个智能体，该智能体集成了45+攻击策略、450+转换器和130+评分器，能够通过自然语言描述目标，自动完成攻击选择、执行、分析和报告生成。其主要贡献包括：1）智能体化界面，显著降低操作门槛；2）统一框架，支持同时测试传统ML模型（对抗样本）和生成式AI系统（越狱攻击）；3）对Meta Llama Scout的案例研究实现了85%的攻击成功率，且无需人工编码。研究意义在于，通过自动化将操作者从繁琐的库特定流程中解放出来，使得AI红队测试能够更高效、更全面地覆盖多模态、多智能体等新型攻击面，为大规模AI系统安全评估提供了可行方案。
