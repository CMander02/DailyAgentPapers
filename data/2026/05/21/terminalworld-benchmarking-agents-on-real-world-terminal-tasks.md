---
title: "TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks"
authors:
  - "Zhaoyang Chu"
  - "Jiarui Hu"
  - "Xingyu Jiang"
  - "Pengyu Zou"
  - "Han Li"
  - "Chao Peng"
  - "Peter O'Hearn"
  - "Earl T. Barr"
  - "Mark Harman"
  - "Federica Sarro"
  - "He Ye"
date: "2026-05-21"
arxiv_id: "2605.22535"
arxiv_url: "https://arxiv.org/abs/2605.22535"
pdf_url: "https://arxiv.org/pdf/2605.22535v1"
github_url: "https://github.com/EuniAI/TerminalWorld"
categories:
  - "cs.AI"
tags:
  - "Agent 评测基准"
  - "终端 Agent"
  - "可扩展数据引擎"
  - "任务反演"
  - "多智能体评估"
relevance_score: 9.0
---

# TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks

## 原始摘要

We introduce TerminalWorld, a scalable data engine that automatically reverse-engineers high-fidelity evaluation tasks from "in-the-wild" terminal recordings. Processing 80,870 terminal recordings, the engine yields a full benchmark of 1,530 validated tasks, spanning 18 real-world categories, ranging from short everyday operations to workflows exceeding 50 steps, and covering 1,280 unique commands. From these, we curate a Verified subset of 200 representative, manually reviewed tasks. Comprehensive benchmarking on TerminalWorld-Verified across eight frontier models and six agents reveals that current systems still struggle with authentic terminal workflows, achieving a maximum pass rate of only 62.5%. Moreover, TerminalWorld captures real-world terminal capabilities distinct from existing expert-curated benchmarks (e.g., Terminal-Bench), with only a weak correlation to their scores (Pearson r=0.20). The automated engine makes TerminalWorld authentic and scalable by construction, enabling it to evaluate agents in real-world terminal environments as developer practices evolve. Data and code are available at https://github.com/EuniAI/TerminalWorld.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前终端智能体评估中的一个核心矛盾：现有的基准测试无法同时满足真实性与可扩展性。研究背景是，终端环境已成为自主智能体（基于LLM）完成复杂软件任务的主要操作空间，但如何可靠地评估这些智能体在真实任务上的表现仍是一个开放问题。

现有方法的不足主要体现在两个方面：一是人工策划的基准（如Terminal-Bench）依赖领域专家手工构建任务，这些任务往往倾向于设计对抗性难题以人为增加难度，偏离了开发者日常的真实终端工作流；同时，这种劳动密集型过程难以随着终端工具的演进（如新命令、新框架的出现）和多样性的扩展而规模化，导致基准范围狭窄且更新滞后。二是最近的自动化合成方法主要用于训练，缺乏严格的验证来保证任务的真实性和质量。

因此，本文要解决的核心问题是：如何构建一个既真实（源于开发者自然操作）又可扩展（能随实践演进自动更新）的评估系统，来系统回答“终端智能体在随日常实践演变的真实任务上表现如何”。为此，论文提出了TerminalWorld，一个能从“野外”终端录制数据中自动逆向工程、生成高质量评估任务的数据引擎，并以此构建了一个包含1530个验证任务（含200个人工复核子集）的基准测试，全面覆盖18个真实类别和1280个独特命令。

### Q2: 有哪些相关研究？

相关工作主要分为终端Agent和终端Agent评测两大类。在终端Agent方面，早期框架如SWE-agent、OpenHands将shell命令封装为结构化工具API，让Agent通过受限动作模式执行任务；而新一代原生CLI助手（如Claude Code、Codex CLI、Gemini CLI）直接暴露原始shell接口，允许Agent调用任意命令并实时观察反馈，实现了更紧密的工具集成。此外，还有工作通过合成大规模环境和利用Agent轨迹进行训练来提升模型在CLI环境中的能力。在评测方面，早期基准如NL2Bash和InterCode聚焦于自然语言转shell命令或单步执行，而近年来的Terminal-Bench和LongCLI-Bench则在交互式shell沙箱中评估多步推理和工具使用。然而，这些现有基准均依赖人工构建，成本高昂且倾向于设计对抗性难题，与真实开发者工作流存在偏差。本文通过从真实终端记录中逆向工程自动构建评测任务，不仅保证了真实性和可扩展性（覆盖1,530个任务），还发现与Terminal-Bench的分数相关性很弱（皮尔逊r=0.20），说明TerminalWorld评估了现有基准未覆盖的独特终端能力。

### Q3: 论文如何解决这个问题？

TerminalWorld通过一个四阶段可扩展数据引擎自动从真实终端录制中逆向工程出高保真评估任务。首先，从asciinema平台收集80,870条人类终端录制，经过隐私过滤、排除TUI/GUI应用、剔除不可复现和环境依赖的录制后，保留9,492条高质量记录。其次，利用Claude Sonnet 4.6等LLM从清洗后的转录中提取开发者核心意图，生成面向结果的指令（仅描述最终状态而非实现路径），并提取干净的可执行bash脚本作为参考解决方案。第三，通过LLM代理（如Claude Code）合成Dockerfile并构建隔离容器环境，采用执行反馈循环不断修复依赖冲突，直到参考脚本能在容器中成功运行（退出码0），最终为5,035个任务生成可复现环境。最后，在容器内生成测试套件，通过三重试炼循环（参考方案全通过、空操作全失败、部分操作至少一个失败）消除误判，确保测试的判别力。经过这四步流水线，最终得到1,530个验证任务，覆盖18个真实世界类别和1,280个独特命令。该框架的核心创新在于完全自动化地从真实人类操作中合成可执行的终端评估任务，无需人工标注，保证了真实性和可扩展性，并通过严格的环境复现和测试校准流程确保了评估的可靠性和区分度。

### Q4: 论文做了哪些实验？

论文在TerminalWorld-Verified子集（200个手动审核任务）上开展了全面的实验评估。实验设置采用Harbor评估框架，使用8个前沿大语言模型（闭源：Claude Opus 4.7、GPT-5.5、Gemini 3.1 Pro；开源：DeepSeek-V4-Pro、Qwen3.6-Max-Preview、Kimi K2.6、GLM-5.1、MiniMax M2.7）和6个智能体框架（Terminus-2、Claude Code、Codex CLI、Gemini CLI、mini-SWE-agent、OpenHands）。主要结果包括：1）所有模型最高通过率仅62.5%，平均54.8%，其中Claude Opus 4.7表现最佳；2）开源模型（如Kimi K2.6的57.5%）与闭源模型差距不大，且成本效益高出4-8倍；3）智能体框架对能力上限影响有限，主要影响成本效益（Terminus-2每通过成本仅$0.51）；4）模型在性能优化（28.1%）、脚本自动化（39.1%）、调试测试（39.3%）等类别表现较差；5）与Terminal-Bench 2.0的分数相关性极弱（Pearson r=0.20），表明TerminalWorld评估了独特的真实终端能力。

### Q5: 有什么可以进一步探索的点？

论文的局限性首先在于数据来源的单一性：仅依赖asciinema格式的终端记录，可能遗漏其他终端环境（如tmux、screen）或工作流形态（如带图形界面的交互）。未来可拓展至多模态终端场景，例如结合日志文件、配置文件或网络状态进行复合任务推理。

其次，当前评估偏重“任务完成率”，缺乏对失败原因（如命令误解、权限错误）的细粒度分析。可考虑设计分层错误诊断框架，比如区分“策略错误”和“语法错误”，以指导模型针对性改进。

此外，手工验证仅覆盖200个任务，自动生成的1530个任务可能存在噪声（如无效步骤路径）。建议引入对抗性验证机制，通过生成任务-解法-变体的三角校验自动过滤低质量样本。

从方法看，终端任务本质是“工具使用+状态管理”的复合推理，可借鉴程序合成中的归纳逻辑编程（ILP）技术，让模型学习从成功轨迹中抽象出可复用的终端操作模式，而非仅依赖预训练知识。同时，结合RLHF对终端行为的安全性约束（如禁止rm -rf /）也是重要方向。

### Q6: 总结一下论文的主要内容

TerminalWorld 提出了一个可扩展的数据引擎，用于从野外终端记录中自动逆向工程高保真评估任务。该论文首先定义了现有基准测试缺乏真实性和可扩展性的问题，然后描述了从80,870条终端记录中提取出1,530个验证任务（其中200个经人工审查）的方法，涵盖18个真实类别和1,280条独特命令。主要结论是，对八个前沿模型和六个智能体在TerminalWorld-Verified上的基准测试显示，当前系统最高仅能通过62.5%的任务，且该基准与专家策划的Terminal-Bench得分相关性较弱（皮尔逊r=0.20）。核心贡献在于提供了一个真实、可扩展且能随开发者实践演进的终端任务测试平台，强调了超越静态专家基准、在动态真实环境中评估智能体的重要性。
