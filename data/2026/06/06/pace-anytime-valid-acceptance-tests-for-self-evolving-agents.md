---
title: "PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents"
authors:
  - "Zayx Shawn"
date: "2026-06-06"
arxiv_id: "2606.08106"
arxiv_url: "https://arxiv.org/abs/2606.08106"
pdf_url: "https://arxiv.org/pdf/2606.08106v1"
categories:
  - "cs.AI"
  - "cs.MA"
tags:
  - "self-evolving agent"
  - "commit gate"
  - "sequential hypothesis test"
  - "agent reliability"
  - "prompt-level evolution"
relevance_score: 9.2
---

# PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents

## 原始摘要

Self-evolving agents improve by repeatedly proposing changes to their own prompts, skills, or workflows and keeping those that score higher on a small held-out set. Almost all effort has gone into the proposer that generates candidates; we argue the weak point is the acceptor, the rule that decides whether to commit a change. Applied hundreds of times against the same noisy dev estimate, the ubiquitous "keep it if the score went up" rule is uncontrolled adaptive multiple testing: the agent effectively p-hacks itself, accumulating false commits that make it churn and drift rather than improve.
  We recast committing as a sequential hypothesis test and propose PACE (Paired Anytime-valid Commit Evaluation), a training-free, anytime-valid commit gate. Each candidate is compared to the incumbent on identical instances and committed only when a testing-by-betting e-process accumulates decisive evidence, stopping early to save evaluations and controlling each candidate's false-commit probability at a user-set level even under optional stopping (a per-decision guarantee).
  On Qwen2.5 agents (0.5B-3B) self-evolving at the prompt level on GSM8K, SVAMP, and ARC-Challenge, greedy acceptance commits 30-42% false and 10-33% harmful edits when a genuine improvement is hidden among noisy proposals, while PACE commits the real one and essentially nothing else, matching greedy's held-out accuracy at sharply lower variance and about 18% lower evaluation cost. With no real gain available, greedy commits 13-21 spurious self-modifications per run (72-100% false) and degrades the most fragile agent by 4.9 points, while PACE holds at baseline. Reliability of self-evolution depends on the acceptor, not only on the proposer.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文聚焦于自我进化智能体（Self-Evolving Agents）的可靠性问题。现有方法几乎将所有努力投入到“提议者”（proposer）上，即生成修改候选的机制，而对于决定是否采纳修改的“接受者”（acceptor），普遍采用一个未经检验的简单启发式规则：只要候选在小规模开发集上的分数上升，就采纳该修改。论文指出，这种“贪婪接受”规则在数百次迭代中重复使用同一份有噪声的评估数据，本质上是无控制的适应性多重假设检验，会导致智能体像研究者“p-hacking”一样积累大量虚假提交——那些对真实性能无益甚至有害的修改。这造成智能体不断波动、性能漂移，最终退化。核心问题在于，当前自我进化循环中关键的“接受”步骤缺乏严格的统计控制。为此，本文提出PACE（Paired Anytime-valid Commit Evaluation），将提交决策重新定义为序列假设检验，通过一种无训练、任意有效的成对测试（基于赌博的e-process），在有限的评估成本内，为用户设定的每个候选修改的虚假提交概率提供严格的上界，从而在保留真实增益的同时，几乎完全消除虚假和有害的修改。

### Q2: 有哪些相关研究？

相关研究可分为四类：  
1. **自我进化智能体**：如ADAS、Gödel Agent、Darwin Gödel Machine、Voyager、Agent Workflow Memory等，通过实证分数选择修改。本文指出现有方法均将接受视为统计决策问题（即缺乏对假阳性提交的控制），而本文首次从统计角度填补该空白。  
2. **提示词与工作流优化**：DSPy、TextGrad、OPRO、GEPA、Promptbreeder、EvoPrompt、AFlow等，在固定开发集上优化标量适应度，已知会过拟合。本文区分了“是否应提交候选”这一正交问题，而非关注生成候选本身。  
3. **自我改进及其病理**：STaR、Reflexion、Self-Refine、Self-Rewarding LMs等，其局限性在于自我评估可靠性。这些研究分析自我改进的信号质量，而本文关注消耗该信号的决策规则（即提交阈值）。  
4. **序列与随时有效检验**：PACE借鉴了安全、随时有效的推断方法（如e-processes、testing-by-betting以及Ville's不等式），以及流式测试的在线误差控制。本文首次将这些统计工具引入智能体自我进化循环，此前决策仅依赖未受保护的点估计。

### Q3: 论文如何解决这个问题？

PACE通过将候选改进的接受过程重新定义为序列假设检验，并引入一种名为“成对随时有效提交门控”的训练无关方法。核心架构围绕一个配对评估与赌博式测试机制展开。在每一轮自我进化中，当前智能体配置（现任）和候选改进配置被应用于相同的测试实例，并记录两者答案正确性的分歧模式：仅当候选正确而现任错误时记为一次“胜”（win），反之则记为“负”（loss），平局（两者都对或都错）则被丢弃，这构成了一个类似McNemar检验的配对比较。基于此，后续关键技术是“通过赌博进行检验”。该方法将假设检验转化为一个财富赌博游戏：初始财富为1，每遇到一个胜/负分歧对，就以固定比例（如0.5）的当前财富下注于“胜”这一结果，财富更新公式为E = E * (1 + λ(2w-1))。在原假设（候选不优于现任）下，胜败几率均等，赌注是公平的，财富预期保持为1左右；若候选真正更优，胜多负少，财富会累积增长。关键在于，这一财富过程是一个关于原假设的非负鞅。根据Ville不等式，财富首次超过预设阈值（如1/α，α=0.05）的时刻，其发生概率在控制水平α内。因此，一旦财富达到阈值，PACE就立刻接受该候选改进，这保证了每个候选的误提交概率被严格控制在α以下，且检验可在任何时刻停止（随时有效）。整体框架通过迭代上述过程：如果财富在耗尽评估预算前达到阈值则提交；否则拒绝该候选，继续探索下一个提案。该方法的创新点在于：(1) 无需额外训练，(2) 提供了对单个候选误提交概率的严格、随时有效的控制，有效抑制了贪婪接受规则下因噪声导致的非改进提交累积问题，(3) 通过动态适配证据强度来决定评估实例数量，比固定样本量检验更高效，通常消耗更少的评估资源。

### Q4: 论文做了哪些实验？

实验在Qwen2.5 agents（0.5B, 1.5B, 3B）上，通过提示级别自演化进行。使用GSM8K、SVAMP和ARC-Challenge三个数据集，采用独立的dev集（n=40）和审计池（n=120）。对比方法包括贪婪接受、固定样本配对检验和PACE门控方法。

在受控实验中（存在一个已知的真实改进），1.5B模型上贪婪接受提交了3.4次/运行，其中42%为误提交、33%为有害提交；而PACE仅提交了真实的改进，误提交和有害提交均为0%，最终准确率提升（Δ=+0.57）与贪婪接受相同，但评估成本降低约18%（1712 vs 2080个配对问题）。3B模型上，贪婪接受Δ=+0.54±0.30（高方差），PACE Δ=+0.74±0.04（低方差，且0%误提交）。

在随机实验（无已知改进，温度0.7采样）中，贪婪接受提交了13-21次/运行（72-100%为误提交），导致最脆弱的0.5B agent性能下降4.9分；而PACE提交少于1次/运行，性能保持基线水平。所有统计门控方法（PACE、固定配对检验、在线FDR）均能有效拒绝噪声，仅贪婪接受出现大量误提交。实验在SVAMP和ARC-Challenge上验证了相同模式，表明结果具有跨任务和领域的稳健性。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面：第一，PACE的验证仅在作者自建的prompt进化循环中进行，未在DSPy、ADAS等第三方系统中验证，跨系统的泛化性有待证实；第二，实验仅使用了Qwen2.5单一模型家族和一种proposer设计，虽然接口层面宣称proposer无关，但缺乏实证支持；第三，PACE在增益极小时会牺牲召回率，过于微小的真改进可能被拒绝。未来研究方向包括：在更广泛的Agent架构（如工具使用、多步骤推理）上验证PACE的有效性；探索动态调整α或自适应阈值的方法，在保守性和召回率之间取得更好平衡；将PACE与更先进的proposer（如LLM-based生成器）结合，形成完整的"检测-生成-验证"闭环；拓展到"弱到强"泛化场景，研究当前置Agent较弱时如何设计更鲁棒的接受规则。此外，开发可证明的族级错误率控制方法（如FWER或FDR）也是一个重要方向。

### Q6: 总结一下论文的主要内容

这篇论文针对自主进化智能体在自我改进时普遍存在的一个被忽视的关键问题——接受器（acceptor）的缺陷。作者将问题定义为一个失控的自适应多重测试：智能体反复在同一个含噪的开发集上执行“分数提高就保留”的贪婪规则，导致大量错误提交（p-hacking），造成性能漂移和退化。作为核心贡献，论文提出了一种免训练、任意有效的验收方法PACE（配对任意有效提交评估）。该方法将提交过程重构为顺序假设检验，利用“测试-下注”的e值过程，在同一实例上对比候选方案与现有方案，仅当累积到决定性证据时才提交，从而在用户设定的水平上控制每个候选的误提交概率，并能提前停止以节省评估成本。主要结论表明，在Qwen2.5智能体上，贪婪规则会提交大量虚假和有害的修改，而PACE在几乎不损失真正增益的情况下，显著降低了方差和评估成本，证明了智能体自我进化的可靠性关键不在于生成器，而在于接受器。
