---
title: "CyberGym-E2E: Scalable Real-World Benchmark for AI Agents' End-to-End Cybersecurity Capabilities"
authors:
  - "Tianneng Shi"
  - "Robin Rheem"
  - "Dongwei Jiang"
  - "Mona Wang"
  - "Francisco De La Riega"
  - "Zhun Wang"
  - "Jingzhi Jiang"
  - "Alexander Cheung"
  - "Sean Tai"
  - "Jonah Cha"
  - "Jianhong Tu"
  - "Gabriel Han"
  - "Chenguang Wang"
  - "Jingxuan He"
  - "Wenbo Guo"
  - "Dawn Song"
date: "2026-06-03"
arxiv_id: "2606.04460"
arxiv_url: "https://arxiv.org/abs/2606.04460"
pdf_url: "https://arxiv.org/pdf/2606.04460v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.LG"
tags:
  - "网络安全Agent"
  - "端到端评测基准"
  - "漏洞发现与修复"
  - "真实世界评估"
  - "智能体能力评估"
relevance_score: 9.5
---

# CyberGym-E2E: Scalable Real-World Benchmark for AI Agents' End-to-End Cybersecurity Capabilities

## 原始摘要

AI has the potential to transform cybersecurity by enabling systems that can autonomously detect, analyze, and remediate software vulnerabilities. However, existing cybersecurity evaluations of AI systems are limited in scale or scope, and fail to capture the end-to-end lifecycle of real-world software vulnerability discovery and remediation. To address this gap, we propose CyberGym-E2E, a large-scale and realistic end-to-end cybersecurity benchmark that comprehensively evaluates AI agents' abilities across the full lifecycle of vulnerability discovery, PoC generation, and patch generation. CyberGym-E2E is comprehensive and scalable, as we build an automated, agent-enhanced pipeline for transforming open-source vulnerability data into realistic evaluation environments. Currently, the benchmark consists of 920 real-world vulnerabilities across 139 different open-source projects.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

该论文旨在解决现有网络安全评估基准在规模、真实性及端到端覆盖上的不足。研究背景是：AI（尤其是大语言模型）在自主检测、分析和修复软件漏洞方面潜力巨大，但现有基准存在几个关键问题：一是任务范围狭窄（如仅关注漏洞检测而忽略修复，或仅针对安全代码生成），未能涵盖从漏洞发现、攻击验证（PoC生成）到补丁生成的完整生命周期；二是数据规模有限或依赖合成数据，缺乏真实世界的多样性；三是缺乏对代理运行环境的模拟，以及补丁后代码功能性的验证。为此，论文提出了CyberGym-E2E，一个大规模、真实的端到端网络安全基准。其核心创新是构建了一个自动化、代理增强的管道，能将开源漏洞数据（如来自OSS-Fuzz）高效转化为逼真的评估环境，涵盖920个真实漏洞和139个开源项目。该基准同时测试漏洞检测、PoC生成和补丁生成三个阶段，并包含补丁后功能测试，旨在全面评估AI代理在真实网络安全场景中的端到端能力，填补现有评估体系在全面性、可扩展性和真实性上的空白。

### Q2: 有哪些相关研究？

### 主要相关工作

本文对比了多类相关工作，主要分为以下几类：

**1. 端到端评估基准**  
- **BountyBench**：最接近本文工作，同样评估真实漏洞的端到端能力（发现→PoC→修复），但仅包含40个任务，依赖人工构建，规模受限。  
- **SecureAgentBench / SecRepoBench**：仅部分覆盖端到端流程，且规模较小。本文通过自动化流水线将真实漏洞转化为920个任务，大幅提升可扩展性。

**2. 单一阶段评估基准**  
- **进攻性基准**：PrimeVul、CVE-bench、CyberGym等聚焦漏洞检测与PoC生成，未覆盖修复环节。  
- **防御性基准**：SeCodePLT、SEC-bench虽包含攻防任务，但未连续评估完整生命周期，且缺乏后补丁功能测试（如SEC-bench无功能测试，SeCodePLT仅用非崩溃模糊测试输入验证C/C++任务，不够全面）。  
- **AutoPatchBench**：依赖LLDB对比函数状态差异，易产生假阳性/假阴性（如等价但不同的补丁可能被误判）。

**3. 环境真实性与规模**  
- 多数基准（如SeCodePLT、BountyBench）仅提供代码库的只读访问，缺乏构建环境，不贴近实际部署。本文直接让智能体在沙箱化构建环境中操作，禁止作弊行为，更符合真实场景。  
- 规模问题：现有基准（如SecureAgentBench）规模小，而本文通过自动化流水线实现139个项目、920个漏洞的高扩展性。

**总结**：本文通过端到端评估、真实环境模拟、大规模自动化构建及严格功能测试，解决了现有工作在范围、真实性、规模与有效性上的不足。

### Q3: 论文如何解决这个问题？

CyberGym-E2E通过构建自动化Agent增强管道，将开源漏洞数据转化为可扩展的现实基准环境。核心方法分为四个步骤：首先从OSS-Fuzz等历史数据源中识别干净补丁，通过二分搜索定位漏洞修复提交，过滤信息不足或涉及多问题的提交；其次准备可重现的Docker构建环境，验证漏洞版本和补丁版本中利用证明（PoC）与预期行为一致，并迁移历史漏洞到支持现代Agent工具链的新系统环境；第三，利用代码Agent自动识别、构建和运行项目开发者的功能测试套件，确保补丁不破坏原有功能；最后由专家验证测试脚本的正确性和覆盖率，过滤低质量任务。

技术创新体现在三个层面：1）端到端评估设计，要求Agent在仅提供代码库和构建环境的场景下独立完成漏洞发现、PoC生成和补丁生成全生命周期任务；2）可扩展的自动化管道，支持从OSS-Fuzz持续注入新漏洞，当前已覆盖920个真实漏洞和139个开源项目；3）四阶段验证体系，包括检查PoC触发未修补二进制漏洞、验证补丁消除崩溃、确认功能测试通过，以及诊断补丁是否修复目标漏洞。通过patch-only（提供真实PoC和崩溃日志）和端到端两种评估设置，系统性地衡量Agent的溯源分析和独立发现能力。

### Q4: 论文做了哪些实验？

论文在CyberGym-E2E基准上评估了AI智能体在漏洞发现、PoC生成和补丁生成全生命周期中的能力。实验设置包括统一框架下的多个智能体工具（Claude Code、OpenHands、Codex、Gemini CLI），初始使用615个任务，扩展后包含920个真实世界漏洞，涉及139个开源项目。主要结果分阶段（S1-S4）报告：在初始615任务上，GPT-5.2-Codex在S1（生成PoC触发崩溃）达30.2%，Gemini 3 Pro在S2（补丁消除PoC崩溃）达23.6%，Claude Opus 4.5在S3（通过测试）达19.2%，但S4（与真实漏洞匹配）最高仅7.6%。补丁-仅模式（P-O）成功率更高（Opus 4.5达82.3%），突显漏洞发现是瓶颈。扩展后新模型性能提升：GPT-5.4在S3达65.9%，S4达22.2%。消融实验表明，时间预算从30分钟增至90分钟、成本从$1增至$10均有收益提升但边际递减。跨运行反馈使S3成功率提升4.8-7.1个百分点。记忆化分析显示，知识截止日期前后的性能差异无统计学显著性（p>0.1）。

### Q5: 有什么可以进一步探索的点？

该工作虽具开创性，但存在显著局限：仅覆盖C/C++内存安全漏洞，且依赖sanitizer崩溃作为验证依据。未来可从以下方向拓展：1) 扩展漏洞类型至逻辑漏洞、Web安全、AI系统自身漏洞（如提示注入），需设计更复杂的或acles（如语义分析、渗透测试验证）；2) 提升任务复杂度，引入多步骤攻击链或带有缓解措施的漏洞环境，模拟真实攻防博弈；3) 改进评估指标，除成功率外纳入效率、资源消耗、隐蔽性（如补丁是否改变软件行为）；4) 增强环境多样性，支持不同编程语言、依赖管理及云原生场景。此外，当前agent-enhanced pipeline注入的“先验知识”可能造成评估偏差，未来应探索更公平的零样本或领域自适应设定。从反馈循环来看，可让agent自主提出新测试用例或绕过验证机制，推动安全评估向对抗性演进。

### Q6: 总结一下论文的主要内容

CyberGym-E2E 旨在解决现有AI网络安全评估在规模、范围和真实性上的不足，特别是缺乏覆盖漏洞从发现到修复的完整生命周期评估。论文提出了一个可扩展的基准构建方法，通过自动化、智能体增强的流程，将真实世界的开源漏洞数据转化为逼真的评估环境。该基准包含来自139个不同开源项目的920个真实世界漏洞，全面评估AI智能体在漏洞发现、概念验证生成和补丁生成三个核心阶段的能力。主要结论是，虽然现有AI系统在生成安全补丁方面表现良好，但在漏洞检测和概念验证生成上仍面临挑战，这显著制约了其端到端的性能。该工作的核心贡献在于首次提出了一个可扩展的、端到端的网络安全基准构建方法论，并进行了大规模评估，对于推动AI在网络安全领域的实际应用和安全部署具有重要意义。
