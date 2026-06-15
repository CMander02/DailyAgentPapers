---
title: "AgentCyberRange: Benchmarking Frontier AI Systems in Realistic Cyber Ranges"
authors:
  - "Fengyu Liu"
  - "Jiarun Dai"
  - "Yihe Fan"
  - "Wuyuao Mai"
  - "Ziao Li"
  - "Bofei Chen"
  - "Jie Zhang"
  - "Zheng Lou"
  - "Bocheng Xiang"
  - "Qiyi Zhang"
  - "Xudong Pan"
  - "Geng Hong"
  - "Yuan Zhang"
  - "Min Yang"
date: "2026-06-12"
arxiv_id: "2606.14295"
arxiv_url: "https://arxiv.org/abs/2606.14295"
pdf_url: "https://arxiv.org/pdf/2606.14295v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.LG"
tags:
  - "网络安全Agent"
  - "Agent基准测试"
  - "多主机渗透"
  - "工具使用"
  - "行动编排"
relevance_score: 8.5
---

# AgentCyberRange: Benchmarking Frontier AI Systems in Realistic Cyber Ranges

## 原始摘要

Frontier AI systems are increasingly capable of cybersecurity tasks, including codebase inspection, vulnerability detection, and exploitation. However, evaluating their offensive capabilities remains constrained by limited access to open, reproducible, multi-host cyber ranges. Existing public benchmarks capture isolated skills such as CTF solving, vulnerability reproduction, and exploit generation, but often abstract away realistic intrusion workflows: discovering exposed services, gaining a foothold, collecting internal information, and expanding compromise across hosts. This gap makes it difficult to observe emerging risks early, because frontier AI systems are rarely evaluated under realistic attack conditions.
  We introduce AgentCyberRange, the first open, multi-range infrastructure for measuring autonomous cyber attack capability in realistic cyber ranges. It combines 110 vulnerabilities across 15 real web applications and 8 enterprise-like cyber ranges with 156 internal hosts, plus Cage, a toolchain for execution, orchestration, result collection, and verification. The benchmark covers two core stages: web exploitation, where agents explore exposed applications and validate vulnerabilities, and post exploitation, where agents turn an initial foothold into broader internal compromise. We evaluate six frontier AI systems under matched prompts and budgets. GPT-5.5 with Codex performs best, solving 16.1% of web exploitation tasks and 31.7% of post-exploitation tasks; with more concrete hints, these rates increase to 33.0% and 46.3%. We also observe out-of-benchmark findings, including unknown vulnerabilities in popular projects, and payload mutation that bypasses host defenses. These results show that open cyber-range evaluation is necessary for observing emerging offensive capabilities under realistic and reproducible conditions.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前缺乏在真实、可复现的多主机网络靶场中评估前沿AI系统自主网络攻击能力的问题。现有方法主要基于CTF解题、漏洞复现或单点利用等孤立任务进行评测，这些基准虽然能衡量特定技能，但往往抽象掉了现实入侵的完整工作流，如发现暴露服务、获得立足点、收集内部信息以及跨主机横向移动等关键环节。这种评估上的空白导致难以在接近真实攻击的条件下早期观察和衡量前沿AI系统可能带来的新兴网络安全风险。因此，本文的核心目标是构建一个开放、多靶场的基础设施，用于在逼真且可复现的网络环境中，系统性地测量前沿AI系统自主完成从外部Web利用到内部后渗透的端到端攻击链的能力。

### Q2: 有哪些相关研究？

本文的相关研究可分为三类：方法类、应用类和评测类。方法类包括通用编程代理（如Codex、Claude Code、OpenHands、Qwen）和专用网络安全代理（如PentestGPT、Incalmo），前者虽针对软件工程但展现出非平凡的网络攻防能力，后者则集成渗透测试工具以支持更真实的攻击工作流。应用类研究聚焦具体任务，如漏洞复现（CyberGym）、漏洞利用（ExploitGym）和渗透测试（PentestGPT、XBOW），这些工作通常从已知漏洞或简化场景出发，忽略了真实入侵的多阶段特性。

评测类研究主要包括CTF基准（如Cybench）、真实世界基准（如CyberGym）和渗透测试基准（如AISI的The Last Ones，TLO）。CTF基准易于评分但缺乏真实性；真实世界基准虽使用真实软件漏洞，但侧重单步漏洞复现而非完整攻击链；TLO虽评估长程攻击，但为封闭测量研究。与这些工作不同，AgentCyberRange首次构建了开放、多靶场的真实网络靶场，涵盖110个漏洞和15个真实Web应用，同时评估Web利用（探索+利用隐藏端点）和后期利用（主机内提权、横向移动）两大核心阶段，支持零日漏洞发现，并提供了统一的Cage管道以支撑可复现的大规模评估。

### Q3: 论文如何解决这个问题？

AgentCyberRange通过构建一个开放、可复现的多靶场基准测试基础设施来解决现有评估缺乏真实攻击流程模拟的问题。核心方法包括两大任务轨道：Web利用轨（WebExploitBench）和后利用轨（PostExploitBench）。Web利用轨涵盖15个真实Web应用中的110个漏洞（含18个零日漏洞），要求智能体在无代码信息的黑盒条件下探索隐藏端点并构造利用载荷。创新点在于引入三种难度级别（仅给URL、额外给出漏洞URL、进一步给出漏洞类型），从而分离端点发现与漏洞利用能力评估。后利用轨包含8个企业级靶场和156个内部主机，模拟了DMZ服务、内部应用、多层网络拓扑和防御系统（如反病毒软件、监控操作员）等真实场景，覆盖横向移动、权限提升、凭证重用、持久化等12种后利用技术。关键技术还包括Cage工具链，提供代理适配器层（统一不同AI系统的调用接口）、运行管理器（隔离容器化执行并记录轨迹）、基准管理器（部署清理环境）和验证模块（通过检查随机标志文件确认利用效果）。设计上强调“可验证性”，Web任务需通过PoC触发可观测的随机金丝雀字符串，后利用任务通过/tmp和/root下的标记文件区分用户级与root级渗透进度。

### Q4: 论文做了哪些实验？

论文对六个前沿AI系统在现实网络靶场中的攻防能力进行了系统评估。**实验设置**方面，使用AgentCyberRange框架，包含15个真实Web应用和8个企业级网络靶场（156个内部主机），覆盖110个漏洞。任务分为Web利用（150步限制）和后渗透（500步限制），每种任务设置2小时超时。**对比方法**包括GPT-5.5+Codex、Claude-Opus-4.7+Claude Code、Qwen-3.7-Max+Qwen Code、Kimi-2.6+Kimi Code，以及使用Claude Code作为通用支架的DeepSeek-V4-Pro和GLM-5.1。**主要结果**：在Level-0设置下，GPT-5.5表现最佳，Pass@1达19.09%，Pass@3（Avg）16.06%，Pass@3（Max）28.18%，成功发现31个跨13类漏洞的独特漏洞。Claude-Opus-4.7和Qwen-3.7-Max为中等梯队（Pass@3 Avg约12-14%），其余模型表现较差（3-8%）。后渗透任务中GPT-5.5以31.7%的Pass@1领先，提供具体提示后Web利用和后渗透成功率分别提升至33.0%和46.3%。分析发现主要失败原因是攻击面探索不足，检测率随漏洞深度从35%（深度2）降至11%（深度6）。

### Q5: 有什么可以进一步探索的点？

AgentCyberRange在构建真实网络攻防场景上迈出了重要一步，但其局限性与未来方向值得关注。首先，当前基准仅覆盖Web利用与后渗透两阶段，未包含侦察、横向移动中的权限提升、数据外泄等完整攻击链环节。未来可扩展至多阶段连续任务，尤其需引入不可预测的防御方（如动态蜜罐、主动响应机制），以测度AI系统在对抗性环境下的适应性。其次，任务难度分级较粗，仅通过“具体提示”区分，建议引入自动化难度评估（如基于漏洞复杂度、网络拓扑熵值），并构建可配置的难度梯度。此外，当前仅评估单次成功率，缺乏对失败后策略调整、资源消耗、以及攻击行为隐蔽性（如规避日志审计）的量化。可借鉴强化学习中的“样本效率”指标，分析模型在不同探索预算下的表现。最后，未知漏洞发现与载荷变异的初步发现暗示模型存在“意外涌现能力”，需建立专门的鲁棒性测试集，并评估其生成代码的毒化风险——例如，是否可能自主构造零日漏洞利用链。建议联合红队推理框架，在受限沙箱中测试模型自动生成的多步攻击计划，以提前识别跨界安全风险。

### Q6: 总结一下论文的主要内容

这篇论文提出了AgentCyberRange，一个用于评估前沿AI系统在真实网络靶场中自主网络攻击能力的开源基准测试平台。现有基准测试多聚焦于CTF解题或单漏洞利用等孤立技能，缺乏对真实入侵流程（如服务发现、立足点建立、内部横向移动）的端到端评估。AgentCyberRange集成了15个真实Web应用和8个企业级网络靶场（包含156个内部主机）中的110个漏洞，并配套了Cage工具链。评估覆盖Web利用和后利用两个核心阶段。在六个前沿AI系统的测试中，GPT-5.5 + Codex表现最佳，在Web利用和后利用任务上分别完成16.1%和31.7%。研究还发现了系统发现未知漏洞和绕过防御的能力。结论表明，现有系统尚不可靠，但已展现出有意义的攻击能力，凸显了开放网络靶场评估的必要性。
