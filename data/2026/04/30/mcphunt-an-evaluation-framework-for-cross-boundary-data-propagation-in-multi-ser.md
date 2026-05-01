---
title: "MCPHunt: An Evaluation Framework for Cross-Boundary Data Propagation in Multi-Server MCP Agents"
authors:
  - "Haonan Li"
  - "Tianjun Sun"
  - "Yongqing Wang"
  - "Qisheng Zhang"
date: "2026-04-30"
arxiv_id: "2604.27819"
arxiv_url: "https://arxiv.org/abs/2604.27819"
pdf_url: "https://arxiv.org/pdf/2604.27819v1"
github_url: "https://github.com/lihaonan0716/MCPHunt"
categories:
  - "cs.AI"
tags:
  - "MCP Agent安全"
  - "跨边界数据传播"
  - "基准测试"
  - "凭证泄露"
  - "提示缓解"
relevance_score: 9.5
---

# MCPHunt: An Evaluation Framework for Cross-Boundary Data Propagation in Multi-Server MCP Agents

## 原始摘要

Multi-server MCP agents create an information-flow control problem: faithful tool composition can turn individually benign read/write permissions into cross-boundary credential propagation -- a structural side effect of workflow topology, not necessarily malicious model behavior. We present MCPHunt, to our knowledge the first controlled benchmark that isolates non-adversarial, verbatim credential propagation across multi-server MCP trust boundaries, with three methodological contributions: (1) canary-based taint tracking that reduces propagation detection to objective string matching; (2) an environment-controlled coverage design with risky, benign, and hard-negative conditions that validates pipeline soundness and controls for credential-format confounds; (3) CRS stratification that disentangles task-mandated propagation (faithful execution of verbatim-transfer instructions) from policy-violating propagation (credentials included despite the option to redact). Across 3,615 main-benchmark traces from 5 models spanning 147 tasks and 9 mechanism families, policy-violating propagation rates reach 11.5--41.3% across all models. This propagation is pathway-specific (25x cross-mechanism range) and concentrated in browser-mediated data flows; hard-negative controls provide evidence that production-format credentials are not necessary -- prompt-directed cross-boundary data flow is sufficient. A prompt-mitigation study across 3 models reduces policy-violating propagation by up to 97% while preserving 80.5% utility, but effectiveness varies with instruction-following capability -- suggesting that prompt-level defenses alone may not suffice. Code, traces, and labeling pipeline are released under MIT and CC BY 4.0.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决多服务器MCP（模型上下文协议）代理中一个未被充分研究的核心问题：非对抗性的、结构性的跨信任边界凭证传播。研究背景是，MCP生态系统发展迅速，已拥有超过10,000个公开服务器，其多服务器架构允许单个代理协调文件系统、数据库、浏览器等工具，形成复杂的数据流。现有方法（如代理安全基准和MCP特定基准）主要研究对抗性鲁棒性（如越狱、提示注入），解决的是“攻击者是否能让代理行为异常”的问题；信息流控制（IFC）框架提供形式化保障但没有实证测量。这些方法均未评估一种新风险：在常规、非对抗性任务执行中，即使每一个单独的工具调用都是良性的，其工作流拓扑结构也会导致预先存在的凭证（如API密钥）在跨服务器边界时被逐字传播。本文要解决的核心问题是，将这种“组合数据传播”现象度量化和特征化，区分因必须遵守指令（如“复制所有内容”）而产生的“任务强制传播”与属于真正安全失效的“违反策略的传播”，并评估提示级缓解措施的有效性。

### Q2: 有哪些相关研究？

相关研究可从威胁模型和传播机制两个维度进行组织。**对抗性基准**方面，MCP-SafetyBench、MCPSecBench、MSB和Trivial Trojans等研究主要评估恶意服务器或提示注入下的攻击鲁棒性，而AgentLeak则在多智能体场景下进行对抗性信道审计。MCPHunt与这些工作的根本区别在于：其评估的所有服务器都是可信且良性的，数据传播是工作流拓扑的结构性副作用，而非恶意模型行为。**非对抗性隐私与运行时防护**方面，TOP-Bench与本文最为相关，同样研究良性目标下多工具编排的隐私风险，但TOP-Bench衡量的是组合推理（合成新信息），而非已有凭证的传播，且其将风险归因于模型能力，而MCPHunt发现风险具有路径特异性。此外，动态污点分析、PRUDENTIA、NeMo Guardrails和Invariant等工作执行按次策略但未建模跨服务器数据流，这正是MCPHunt所填补的空白。本文通过金丝雀污点追踪、环境控制覆盖设计和CRS分层，首次实现了对非对抗性跨边界凭证传播的受控基准评估。

### Q3: 论文如何解决这个问题？

MCPHunt的核心方法是构建一个受控基准测试框架，用于隔离和量化多服务器MCP智能体中非对抗性的跨边界凭证传播。其整体框架包括三个主要组件：评估设计、痕迹收集、检测与分析。

评估设计中，框架采用**canary-based (金丝雀) 污点追踪**技术，用格式真实的金丝雀字符串替换敏感值（如 `sk_live_*`），将传播检测简化为客观的字符串匹配。同时设计了三种环境条件：Risky（包含格式真实的金丝雀值）、Benign（无害占位符，用于验证管道的完善性）、Hard-negative（使用安全主题但人类可读的占位符，如 `test_key_not_for_production`，用于验证生产格式凭证是否为必要条件）。任务覆盖9种风险机制家族（如 `browser_to_local`、`file_to_file`），并引入了**CRS (Completion Requires Secret) 分层**，区分任务强制传播（指令要求逐字传输）和违反策略的传播（智能体本可编辑但未编辑）。

痕迹收集阶段，一个协调器通过8个MCP服务器编排任务，记录每个工具调用，并进行逐次调用金丝雀追踪。检测与分析阶段，一个管道算法对每个金丝雀进行因果追踪，计算两层共11个风险信号（如 `data_flow`、`secret_in_command`、`secret_in_command`等），并依据CRS分层将传播分为任务强制和违反策略两类，最终按安全性和实用性将结果划分为四个象限。

该框架的主要创新点在于：1）通过金丝雀污点追踪和受控环境设计，客观、可复现地衡量非恶意、结构性的跨边界传播；2）通过CRS分层，从概念上区分是否违反策略；3）通过硬阴性控制实验，证明生产格式凭证并非传播的必要条件，仅凭提示词驱动的跨边界数据流就足以引发传播。

### Q4: 论文做了哪些实验？

论文进行了全面的实验评估。实验设置包括：使用5个模型（OpenAI的模型Primary、模型B/C/D/E），温度设为0，覆盖不同能力层级。数据集包含147个任务（135个机制标记任务覆盖9个风险机制家族，12个良性控制任务），在7种环境变体（risky_v1/v2/v3、benign、hard_neg_v1/v2/v3）下运行，每个模型产生723条轨迹，总计3615条主基准轨迹。对比方法包括三级提示缓解策略：M1（通用隐私提醒）、M2（明确重写规则）、M3（详细边界感知指令）。主要结果：政策违反传播率在所有模型中达11.5%–41.3%，其中浏览器到本地机制传播率最高（如模型Primary达49.8%），间接暴露最低（4.0%）。核心发现是传播路径依赖性强（机制间差异达25倍），且浏览器中介的数据流占主导。M3缓解策略将政策违反传播率降低97%（从41.3%降至1.2%），同时保持80.5%的实用性，但效果随模型指令遵循能力变化（模型C降75%，模型E降47%）。良性控制产生零信号，验证了管道可靠性。

### Q5: 有什么可以进一步探索的点？

首先，MCPHunt目前仅采用完全匹配或近似匹配的“金丝雀”字符串检测传播，无法捕捉改写或同义替换后的数据泄露，未来可引入嵌入相似度或语义聚类来扩大检测范围。其次，当前147个任务均为研究者设计的合成场景，缺乏真实企业级工作流的验证，后续可利用实际任务日志构建更贴近生产环境的测试集。第三，论文模拟的后验污点守卫是离线进行的，未考虑实时部署时守卫对智能体规划行为的影响，需开发集成入MCP runtime的在线信息流控制（IFC）原语。第四，覆盖的服务类型有限（仅8种），云存储、邮件、CI/CD等常见高频服务尚未测试，未来应扩展服务种类以评估更完整的数据流拓扑。此外，提示级缓解策略在不同指令遵循能力的模型上效果差异显著，说明单纯依靠提示工程不够鲁棒，未来应结合结构化数据流追踪与自动化重写机制，在保留任务效用的前提下实现跨边界传播的模型无关防御。

### Q6: 总结一下论文的主要内容

这篇论文提出了 MCPHunt，据作者所知是首个用于隔离多服务器 MCP 智能体中非对抗性、逐字凭据跨信任边界传播的受控基准。其核心贡献包括：引入基于金丝雀的污点追踪技术，将传播检测简化为客观字符串匹配；设计了包含风险、良性、硬负条件的环境控制覆盖方案，以验证流水线稳健性并控制凭据格式混淆；通过CRS分层将任务强制传播与违反策略的传播区分开。对5个模型（涵盖147个任务和9个机制族）的3,615条轨迹进行评估，发现所有模型的违反策略传播率在11.5–41.3%之间，且具有路径特异性（跨机制范围达25倍），主要集中在浏览器中介的数据流中。硬负对照表明生产格式凭据并非必要，提示引导的跨边界数据流已足够。提示缓解研究可将违反策略传播率降低最高97%并保留80.5%效用，但其效果因指令遵循能力而异，表明仅靠提示层防御可能不足。该框架填补了非恶意凭据传播的系统级评估空白，对MCP安全设计具有重要意义。
