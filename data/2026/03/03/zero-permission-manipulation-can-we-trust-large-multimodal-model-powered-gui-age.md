---
title: "Zero-Permission Manipulation: Can We Trust Large Multimodal Model Powered GUI Agents?"
authors:
  - "Yi Qian"
  - "Kunwei Qian"
  - "Xingbang He"
  - "Ligeng Chen"
  - "Jikang Zhang"
date: "2026-01-18"
arxiv_id: "2601.12349"
arxiv_url: "https://arxiv.org/abs/2601.12349"
pdf_url: "https://arxiv.org/pdf/2601.12349v2"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.SE"
tags:
  - "Safety & Alignment"
  - "Human-Agent Interaction"
relevance_score: 8.0
taxonomy:
  capability:
    - "Safety & Alignment"
    - "Human-Agent Interaction"
  domain: "Cybersecurity"
  research_type: "Empirical Study/Analysis"
attributes:
  base_model: "N/A"
  key_technique: "Action Rebinding, Intent Alignment Strategy (IAS)"
  primary_benchmark: "N/A"
---

# Zero-Permission Manipulation: Can We Trust Large Multimodal Model Powered GUI Agents?

## 原始摘要

Large multimodal model powered GUI agents are emerging as high-privilege operators on mobile platforms, entrusted with perceiving screen content and injecting inputs. However, their design operates under the implicit assumption of Visual Atomicity: that the UI state remains invariant between observation and action. We demonstrate that this assumption is fundamentally invalid in Android, creating a critical attack surface.
  We present Action Rebinding, a novel attack that allows a seemingly-benign app with zero dangerous permissions to rebind an agent's execution. By exploiting the inevitable observation-to-action gap inherent in the agent's reasoning pipeline, the attacker triggers foreground transitions to rebind the agent's planned action toward the target app. We weaponize the agent's task-recovery logic and Android's UI state preservation to orchestrate programmable, multi-step attack chains. Furthermore, we introduce an Intent Alignment Strategy (IAS) that manipulates the agent's reasoning process to rationalize UI states, enabling it to bypass verification gates (e.g., confirmation dialogs) that would otherwise be rejected.
  We evaluate Action Rebinding Attacks on six widely-used Android GUI agents across 15 tasks. Our results demonstrate a 100% success rate for atomic action rebinding and the ability to reliably orchestrate multi-step attack chains. With IAS, the success rate in bypassing verification gates increases (from 0% to up to 100%). Notably, the attacker application requires no sensitive permissions and contains no privileged API calls, achieving a 0% detection rate across malware scanners (e.g., VirusTotal). Our findings reveal a fundamental architectural flaw in current agent-OS integration and provide critical insights for the secure design of future agent systems. To access experimental logs and demonstration videos, please contact yi_qian@smail.nju.edu.cn.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在揭示并解决由大型多模态模型驱动的GUI智能体在移动平台上存在的严重安全漏洞。研究背景是，随着大型多模态模型被集成到移动操作系统中，能够感知屏幕并执行输入的自主GUI智能体正成为一种新兴的高权限操作者，它们作为用户与操作系统之间的新控制平面，执行跨应用的复杂任务。现有方法（即当前GUI智能体的设计）基于一个隐含的“视觉原子性”假设：即从智能体观察界面到执行动作期间，UI状态保持不变。然而，论文指出这一假设在Android这类事件驱动的环境中根本不成立，因为应用的有意行为（如主动前台切换）或异步系统事件（如来电）都可能导致UI状态在观察与执行动作的间隙发生不可预测的变化。

现有方法的不足正在于盲目依赖这一无效的“视觉原子性”假设，从而在智能体的“观察-推理-执行”流水线中引入了一个固有的、可被利用的“观察到动作的间隙”。这导致现有基于恶意代码分析、UI覆盖检测或语义对齐检查的安全机制完全失效，因为攻击意图既不体现在智能体的推理过程中，也不存在于攻击者应用的显式代码逻辑里。

因此，本文要解决的核心问题是：如何形式化地揭示这一由“观察到动作的间隙”构成的新型攻击面，并设计出一种名为“动作重绑定”的具体攻击方法，以证明当前GUI智能体与操作系统集成中存在根本性的架构缺陷。论文通过构建无需任何危险权限的恶意应用，利用Android系统的无限制前台切换和UI状态保持特性，在智能体推理间隙触发前台过渡，将其计划动作重绑定到目标应用，甚至组合成多步攻击链。此外，论文还引入了意图对齐策略来操纵智能体的推理过程，使其绕过验证关卡。最终，论文通过实证评估验证了攻击的可行性、有效性和隐蔽性，旨在为未来智能体系统的安全设计提供关键见解。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：GUI代理安全、Android系统交互漏洞，以及多模态模型的安全风险。

在**GUI代理安全**方面，已有工作关注基于规则的自动化工具（如UI Automator）的权限滥用问题，但本文聚焦于新兴的、基于大语言模型（LMM）的智能GUI代理。这些现代代理（如本文评估的六种）利用LMM进行泛化理解，无需应用特定脚本，但其“观察-推理-执行”的闭环流程引入了新的攻击面。本文的核心贡献在于首次揭示了这类代理所隐含的“视觉原子性”假设（即UI状态在观察与行动间保持不变）在Android动态环境中根本不成立，从而系统性地提出了“动作重绑定”攻击。

在**Android系统交互漏洞**领域，已有研究指出了Android任务栈管理和UI状态持久化机制可能被利用，例如任务欺骗（task-spoofing）和UI重定向（UI redressing）。本文与这些工作的关系在于，它直接利用了Android为保持用户体验而设计的“状态持久化”特性（即后台任务的Activity栈和瞬时UI状态会被冻结保存），并将其武器化，作为构建多步攻击链的基础。本文的独特之处在于，首次将这种系统特性与GUI代理的推理延迟和任务恢复逻辑相结合，实现了无需任何敏感权限的、可编程的攻击。

在**多模态模型安全风险**方面，现有研究多集中于提示注入或对抗性样本对模型本身的误导。本文则开辟了一个新方向：关注LMM作为**系统代理**在真实操作系统环境中运行时，其工作流程（而不仅仅是模型本身）存在的根本性架构缺陷。本文提出的“意图对齐策略”（IAS）通过操纵代理的推理过程来合理化异常的UI状态，从而绕过验证关卡，这区别于传统的模型对抗攻击，是一种针对“代理-操作系统”集成层面的新型攻击。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为“动作重绑定”的新型攻击方法，来揭示并利用基于大语言模型的GUI代理在Android平台上存在的根本性安全漏洞。该方法的核心思想是，利用代理从观察屏幕到执行动作之间必然存在的时间差，通过操纵UI状态，将代理原本针对良性诱饵应用的操作，重定向到敏感的目标应用上，从而在无需任何危险权限的情况下，实施高权限攻击。

整体攻击框架分为五个阶段，并依赖于两个关键的时间窗口：启动到观察窗口和观察到动作窗口。攻击流程如下：首先，用户指示代理在攻击者应用内执行任务；在启动到观察窗口内，攻击者应用渲染一个“上下文载体”，即一个包含标准交互元素的良性UI，旨在诱导代理产生特定的、可预测的操作。其次，代理在观察时刻捕获此良性UI状态并进入推理阶段。随后，在关键的观察到动作窗口内，攻击者应用利用标准的Android Intent机制，触发前台应用切换到目标应用。此时，代理的推理引擎正在处理模型推断，对此切换毫不知情。最后，代理按计划注入动作，但由于前台已变为目标应用，该动作被重绑定到目标应用的敏感组件上，从而执行了恶意操作。攻击后，代理的任务恢复逻辑通常会尝试重新启动原始应用，这无意中重置了攻击环境，使得攻击者可以编排多步骤的攻击链。

该方法包含三个关键技术组件：原子动作重绑定、多步骤编排和意图对齐策略。原子动作重绑定是基础，通过离线分析目标应用的UI布局，精心构造上下文载体，使其交互组件的位置与目标应用中目标组件的屏幕坐标对齐，然后在观察到动作窗口内触发前台切换，实现单次动作的劫持。多步骤编排则利用了代理的任务恢复逻辑，通过代理自主恢复或利用通知覆盖“返回”按钮等方式，诱使代理反复回到攻击者应用，从而将多个原子重绑定串联成可编程的攻击序列。意图对齐策略是针对验证关卡设计的创新技术，它通过精心设计上下文载体的文本内容，为代理建立一个“UI状态桥梁”，使其将后续在目标应用中出现的验证对话框合理化，从而自愿授权敏感操作，显著提高了攻击成功率。

该方法的创新点在于其攻击的隐蔽性和对现有防御体系的全面绕过。它将恶意意图、执行权限和操作能力三者解耦：攻击者应用代码完全良性，仅触发标准UI切换；代理的推理过程语义正确，未被污染；最终的高权限操作由拥有系统权限的代理合法执行。这使得它能够规避基于代码的静态分析、基于UI的点击劫持防护以及基于代理的提示词监控等现有防御机制，揭示了当前代理-操作系统集成架构中的根本性缺陷。

### Q4: 论文做了哪些实验？

论文实验评估了所提出的“动作重绑定”攻击方法对六款主流Android GUI智能体的有效性。实验设置方面，攻击者应用（$App_{atk}$）基于一个随机选择的开源应用进行修改，集成了攻击逻辑但保留了原有功能和用户体验。实验在运行Android 15的Pixel 14设备上进行。对于支持模型替换的智能体，使用qwen3-vl-plus作为推理模型；对于AutoGLM，则使用其平台唯一支持的AutoGLM-Phone-9B-Multilingual模型。

数据集/基准测试涉及15个具有代表性的攻击任务，涵盖了系统主权、身份、隐私、财务和数据完整性等多个安全领域。这些任务包括“开启勿扰模式”、“请求相册访问权限”、“安装应用”、“发送短信”、“在线购买”等。实验对比了六款广泛使用的开源Android GUI智能体：Mobile-Agent-v3, Droidrun, mobile-use, AppAgent, mobiagent, 和 AutoGLM。

主要结果如下：对于原子动作重绑定攻击，成功率达到100%。在端到端攻击测试中，Mobile-Agent-v3和Droidrun在全部15个任务上均成功；其他智能体在部分任务上失败，例如AppAgent在5个多步骤任务上失败，AutoGLM在2个需要验证关卡的任务上失败。关键数据指标显示，在引入意图对齐策略（IAS）后，绕过验证关卡（如确认对话框）的成功率从0%提升至最高100%。此外，攻击者应用无需任何敏感权限，也未调用特权API，在VirusTotal等恶意软件扫描器上的检测率为0%。这些结果证实了攻击的普遍有效性和隐蔽性。

### Q5: 有什么可以进一步探索的点？

该论文揭示了基于视觉原子性假设的GUI代理存在根本性安全缺陷，但仍有多方面值得深入探索。首先，研究主要针对Android平台，未来可扩展至iOS、桌面或Web环境，验证攻击的普适性。其次，当前攻击依赖特定UI状态转换，可探索更隐蔽的触发机制，如利用异步网络加载或动态内容更新制造观察-行动间隙。此外，论文的防御方案较为初步，未来需系统设计端到端的安全架构，例如在操作系统层面引入“代理感知”的权限沙箱，或让代理具备时序一致性验证能力，主动检测UI状态突变。从Agent设计角度，可探索将环境动态建模纳入推理过程，使代理能对预期外的界面变化进行质疑和重新规划，而非盲目执行原计划。最后，攻击目前针对已知任务，未来可研究如何让恶意应用诱导代理执行开放式的有害操作，这对评估代理的鲁棒性提出了更高要求。

### Q6: 总结一下论文的主要内容

该论文揭示了由大型多模态模型驱动的GUI代理在Android平台上存在严重安全漏洞。核心问题是这些代理设计基于“视觉原子性”的错误假设，即认为UI状态在观察与执行动作之间保持不变。论文提出了一种名为“动作重绑定”的新型攻击方法，允许一个看似无害、无需危险权限的恶意应用，通过利用代理推理流程中固有的观察-动作间隙，触发前台界面切换，从而将代理计划的操作重定向到目标应用。

论文的核心贡献在于：首先，形式化了这一攻击面，并展示了如何利用代理的任务恢复逻辑和Android的UI状态保持机制，编排可编程的多步骤攻击链。其次，引入了“意图对齐策略”，通过操纵代理的推理过程使其合理化被篡改的UI状态，从而能够绕过原本会拒绝操作的验证关卡（如确认对话框）。

实验评估了六款广泛使用的Android GUI代理在15个任务上的表现，结果显示原子动作重绑定攻击成功率达100%，并能可靠编排多步攻击链。结合意图对齐策略后，绕过验证关卡的成功率从0%大幅提升至最高100%。值得注意的是，攻击应用无需敏感权限且不含特权API调用，在所有恶意软件扫描器中检测率为0%。主要结论指出，当前代理与操作系统集成存在根本性的架构缺陷，为未来代理系统的安全设计提供了关键见解。
