---
title: "APT-Agent: Automated Penetration Testing using Large Language Models"
authors:
  - "William Guanting Li"
  - "Alsharif Abuadbba"
  - "Kristen Moore"
  - "Dan Dongseong Kim"
date: "2026-05-24"
arxiv_id: "2605.24949"
arxiv_url: "https://arxiv.org/abs/2605.24949"
pdf_url: "https://arxiv.org/pdf/2605.24949v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Cybersecurity Agent"
  - "Penetration Testing"
  - "Command Rectification"
  - "Memory Architecture"
  - "Automated Exploitation"
  - "Multi-step Planning"
relevance_score: 9.5
---

# APT-Agent: Automated Penetration Testing using Large Language Models

## 原始摘要

Penetration testing is essential to securing modern web infrastructures, yet traditional manual methods struggle to keep pace with their scale and complexity. Large Language Models (LLMs) offer new opportunities for automating these tasks, but existing approaches face two persistent challenges: hallucination of technical entities and insufficient long-term contextual memory. To address these issues, we present APT-Agent, a fully automated LLM-driven penetration testing framework that systematically orchestrates reconnaissance, exploitation, and exfiltration. APT-Agent introduces a hybrid rectification module to recover hallucinated commands and a command-specific memory architecture to preserve operational context across multi-step attack sequences. We evaluate our APT-Agent on Metasploitable 2 against seven vulnerable services spanning web, database, and network protocols. APT-Agent achieves an 84.29% end-to-end exploitation success rate, compared to 48.57% (Script Kiddie) and 18.57% (PentestGPT) under matched conditions. By reducing cognitive burden and minimizing reliance on human intervention, APT-Agent represents a step toward scalable, reliable, and cognitively efficient automation for penetration testing.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前渗透测试自动化中面临的两个核心问题：技术实体幻觉和长期上下文记忆不足。研究背景是，随着网络基础设施规模与复杂性的增长，传统的手工渗透测试面临可扩展性差、依赖稀缺专家经验、结果不一致等局限性。虽然大语言模型（LLM）为自动化渗透测试带来了新机遇，但现有方法（如PentestGPT等）存在两个关键不足：一是LLM经常“幻觉”出错误的技术实体，包括捏造或误写命令语法、Metasploit模块路径、平台名称或payload标识符。这种细微错误会直接破坏自动化流程，导致无意义的探测乃至安全风险。二是现有系统缺乏对多步攻击序列的长期上下文记忆，常常丢失或覆盖之前的状态和中间结果，导致重复失败命令或无法基于前期发现（如开放服务、凭证）调整后续策略，从而降低整体效率并需要频繁人工干预。为解决这些问题，本文提出了APT-Agent框架，通过引入混合校正模块（利用模糊字符串匹配和精确后缀匹配修复幻觉命令）以及命令特定的阶段感知上下文管理模块（持续跟踪操作状态和历史，将执行信息整合进后续提示），旨在实现无需人工干预、可靠且可扩展的全自动渗透测试。

### Q2: 有哪些相关研究？

相关研究主要分为基于强化学习（RL）和基于大语言模型（LLM）两类。RL方法将渗透测试建模为马尔可夫决策过程，通过奖励反馈学习最优攻击路径，代表工作包括Schwartz等人使用部分可观测MDP模拟防御措施对攻击者知识的影响、Chen等人提出的GAIL-PT结合专家演示与生成对抗模仿学习、Becker等人对多种RL算法的基准测试，以及Li等人引入的层次化深度强化学习框架。然而这些方法严重依赖模拟环境，难以泛化到真实场景。LLM方法利用模型推理能力实现自动化，包括PentestGPT通过攻击任务树分解子任务、AutoAttacker使用规划器-导航器-总结器流水线、Script Kiddie采用零样本提示链策略、PentestAgent引入多智能体协作与检索增强生成。本文的核心改进在于：针对RL方法需要大量专家工程且无法直接生成命令的问题，APT-Agent无需预配置环境和领域专家；针对现有LLM方法存在的幻觉命令和长程记忆不足，本文创新性地提出混合修正模块恢复幻指令，并设计命令特定记忆架构保持多步操作上下文，从而在实体修正、长期记忆、完全自动化和低专家配置四个维度上首次同时达到良好表现，以84.29%的端到端成功率显著优于Script Kiddie（48.57%）和PentestGPT（18.57%）。

### Q3: 论文如何解决这个问题？

APT-Agent通过一个由大语言模型驱动的全自动化渗透测试框架来解决传统方法中的幻觉和上下文记忆不足问题。其核心架构包括三个迭代运行的模块：战术选择模块、命令生成模块和输出翻译模块。战术选择模块基于MITRE ATT&CK框架和累积知识决定下一阶段（侦察、利用、窃取）；命令生成模块将战术决策转化为可执行命令（如Metasploit操作），并动态调整策略；输出翻译模块将原始工具输出压缩为结构化的成功/失败反馈，避免噪声误导。

创新点在于两个关键组件：一是修正模块，它通过构建包含3253个有效Metasploit模块的数据库，并采用混合模糊匹配（结合后缀提取、归一化Levenshtein模糊匹配和模块重构）纠正LLM产生的幻觉命令（如将无效模块映射为有效模块），同时自动注入缺失参数和验证负载架构。二是命令特定记忆模块，它以极简JSON格式记录每轮迭代的阶段编号、执行命令和二元结果（成功/失败），专为利用和窃取阶段维护日志，确保LLM不会重复失败命令并保留历史执行顺序。该模块还通过路由管理读写权限，直接注入记忆到命令生成模块。此外，框架集成了工具适配器、自动会话管理和暴力破解时间预算机制，实现从目标指定到文件窃取的全自动端到端操作。

### Q4: 论文做了哪些实验？

论文在Metasploitable 2靶机上进行了实验，该靶机包含vsftpd、OpenSSH、Telnet、Apache、UnrealIRCd、PostgreSQL和Samba等7种脆弱服务。实验设置包括：使用GPT-4o作为核心LLM，每服务运行10次独立测试，每阶段最多30次迭代，以获取敏感文件为目标。对比方法包括Script Kiddie和PentestGPT，均使用相同LLM配置。

主要结果：APT-Agent在70次测试中成功59次，端到端成功率84.29%，显著优于Script Kiddie（48.57%）和PentestGPT（18.57%）。各服务成功率从70%（Apache 2.2.8和UnrealIRCd）到100%（vsftpd）不等。消融实验显示，移除矫正模块和CMM内存模块后成功率分别降至71.43%和65.71%，两者都移除则仅54.29%。矫正模块成功恢复了62.5%的幻觉命令，CMM将UnrealIRCd的EXFILTRATE迭代次数从52次降至3次。在矫正方法对比中，混合方法（51.95%）优于模糊匹配（38.46%）、末部匹配（37.18%）和RAG（5.13%）。内存机制对比中，CMM达到最高成功率（100%）和最低重复率（16.67%）。

### Q5: 有什么可以进一步探索的点？

该论文在自动化渗透测试领域取得了显著进展，但仍存在一些值得深入探索的方向。首先，当前评估环境较为单一（仅Metasploitable 2），未来需在多主机、异构网络及跨机器攻击路径等复杂场景中验证其鲁棒性。其次，战术覆盖范围有限，论文仅实现了RECON、EXPLOIT和EXFILTRATE三个阶段，而ATT&CK框架中的横向移动、权限提升等关键阶段尚未集成，可通过扩展决策规则和命令模板实现更完整的攻击生命周期覆盖。此外，幻觉纠正模块虽然有效，但当前仅依赖固定的知识库回滚，未来可引入动态知识图谱或在线检索增强生成来提升自适应能力。最后，伦理与安全防护机制需进一步强化，包括建立标准化基准测试、沙箱隔离和人类监督流程，以防双用途技术被恶意利用。从更宏观视角看，LLM驱动的安全自动化不应仅局限于模拟攻击，还可探索将防御策略与攻击行为动态耦合，实现攻防一体的智能安全评估框架。

### Q6: 总结一下论文的主要内容

本文提出APT-Agent，一个基于大语言模型的自动化渗透测试框架，旨在解决传统手动测试难以应对现代Web基础设施规模与复杂性、以及现有LLM方法存在的技术实体幻觉和长期上下文记忆不足问题。该框架通过混合修正模块恢复幻觉命令，并引入命令专用记忆架构保留多步攻击序列的操作上下文，系统化地组织侦察、利用和数据窃取阶段。在Metasploitable 2上针对七种漏洞服务的评估显示，APT-Agent的端到端利用成功率达84.29%，显著优于Script Kiddie（48.57%）和PentestGPT（18.57%）。核心贡献在于通过减少认知负担和人为干预，实现了更可靠、可扩展的渗透测试自动化，为LLM驱动的网络安全自动化提供了有效方案。
