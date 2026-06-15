---
title: "GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge"
authors:
  - "Pavan C Shekar"
  - "Abhishek H S"
  - "Aswanth Krishnan"
date: "2026-06-12"
arxiv_id: "2606.14470"
arxiv_url: "https://arxiv.org/abs/2606.14470"
pdf_url: "https://arxiv.org/pdf/2606.14470v1"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "Agent Memory"
  - "Reasoning Tree Version Control"
  - "LLM Agent Architecture"
  - "Agent Auditability"
  - "Memory Substrate Evaluation"
relevance_score: 8.5
---

# GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge

## 原始摘要

Large language model (LLM) reasoning is ephemeral: chains of thought vanish with the context window, pruned search branches leave no record, and memory buffers cannot be diffed, merged, or audited. Every other complex software process (code, infrastructure, data, experiments) is version-controlled; reasoning is not. We introduce GitOfThoughts, which stores an agent's reasoning tree as a git repository: every scored thought is a commit, scores are notes, outcomes are tags, and retrieval is "git log" over the agent's own history. This makes reasoning replayable, auditable, and mergeable across agents at near-zero engineering cost.
  We then ask the harder question: does memory, in any substrate, actually improve accuracy? Across five substrates (none, markdown, vector, graph, git), two benchmarks, two model scales, and pre-registered replications, the answer for novel problems is no. No memory format reliably helps, and a promising early result collapsed under its own pre-registered replication. Memory pays only above what we call the copyability threshold: when the retrieved case is a near-duplicate of the current problem (similarity >~ 0.8), accuracy jumps sharply; below it, nothing. The gain is answer retrieval, not method transfer: a 4.5x larger model doubles the near-duplicate payoff yet still cannot extract a transferable method from a worked example. The only general lever we find is test-time sampling. The case for git-as-substrate is therefore auditability, provenance, and mergeability at accuracy parity. We document a retracted result and a refuted hypothesis to model the evaluation standard we hold ourselves to.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大语言模型（LLM）推理过程的“短暂性”问题。当前，诸如思维链、思维树等推理过程会随上下文窗口消失，剪枝的搜索分支不留记录，记忆缓冲区无法进行对比（diff）、合并（merge）或审计。这严重阻碍了推理的可复现性、审计、记忆传递和事件审查。现有方法（如Markdown、向量数据库、图结构）虽然尝试存储记忆，但缺乏版本控制，无法实现像代码管理那样的完整操作。

核心问题在于两点：第一，能否构建一个类似git的版本控制推理系统，使得推理过程可重放、可审计、可合并，同时不牺牲准确性（H-substrate假设）。第二，跨问题记忆能否实际提升模型在新问题上的准确性（H-memory假设）。本文通过GitOfThoughts（将推理树存储为git仓库）作为实验工具，试图验证这两个假设，并最终发现：记忆在面临真正的新问题时无效，仅当检索到的案例是当前问题的近重复（相似度>0.8）时，准确性才有显著提升，且这种提升是答案检索而非方法迁移。因此，论文否定了记忆能普遍提升新问题准确性的观点，转而强调版本控制带来的审计、溯源和合并能力才是核心价值。

### Q2: 有哪些相关研究？

### 相关研究

本文的相关工作可归类为以下四类：

**方法类：迭代推理和树搜索研究**  
ReAct、Reflexion、Self-Refine 等通过单次查询内的推理轨迹增强思考，但内存结构是瞬时的，无法跨会话持久化。Tree-of-Thoughts、LATS、RAP 等树搜索方法虽引入分支和回溯，但树结构在进程结束时即被释放。GitOfThoughts 与它们的关键区别在于将推理树持久化为 git 仓库，实现版本化、可重放和可合并的推理过程。

**应用类：长期记忆系统**  
Voyager、Generative Agents、MemoryBank、MemGPT、ExpeL、CLIN、Mem0、A-MEM、TextGrad 等使用定制化的侧存储（如 markdown、向量、图结构）来管理智能体记忆。本文将这些方法映射到自己的 flat markdown、vector、graph 三类基座，并新增 git 基座作为版本控制系统。GitOfThoughts 的创新在于将推理 DAG 本身作为记忆基座，而非依赖外部存储。

**评测类：测试时扩展机制**  
Self-consistency、多智能体辩论、验证器引导的 best-of-N 等方法通过计算换取准确性。本文的发现与近期研究一致：辩论主要改善个体预测，而裁决（selector）是关键瓶颈。

**机制类：上下文学习原理**  
本文的“可复制性阈值”发现与 ICL 机制的已有证据相连——演示通常通过任务识别和表面格式起作用，而非方法内容。当检索案例与当前问题的相似度低于 0.8 时，记忆几乎无效。

### Q3: 论文如何解决这个问题？

GitOfThoughts将智能体的推理树直接映射为Git仓库，每个带评分的思考节点是一个Git提交，评分存入Git Notes，验证结果打为Git Tag，检索复用`git log --grep`和`git log -S`等原生工具。整体框架包括外层的树状搜索（深度1、分支因子4，对多选题以候选答案为根来扩展）和内层的ReAct循环（最多3步，集成计算器、SymPy和PuLP求解器）。评分机制采用局部分数和跨节点分数的加权组合（0.6:0.4），最佳子节点验证后标记并允许最多一次带失败上下文的重新扩展。每个问题运行在独立的临时仓库中，通过commit-on-score钩子写入thought.md、scores.json、trace.jsonl和metadata.json四个文件，附上评分笔记和结果标签。master分支积累会话推理树，长期memory分支存储跨问题洞见。创新点在于：1）零工程成本获得版本控制的所有操作属性——可重放（任何SHA可恢复完整推理状态）、可审计（`git diff success_X failed_Y -- thought.md`给出行级差异）、可合并（`git fetch && git merge`实现跨智能体记忆同步并暴露冲突）；2）通过`git log -S`进行公平性审计，确保实验无数据泄露；3）跨进程合并通过中央裸仓库端到端运行，矛盾教训显式作为合并冲突呈现。检索仅使用原生Git命令，按置信度加权分数排序（α=0.7, β=0.2, γ=0.1）。这一设计的关键洞见是：既然实验证明任何记忆格式都无法提升新问题的准确率，那么Git作为基底的操作优势（可审计、可复现、可合并）就成了决定性选择因素。

### Q4: 论文做了哪些实验？

论文进行了三组实验验证记忆对推理准确性的影响。实验设置包括五种记忆后端（无、markdown、git、向量、图）和两个基准（GPQA-Diamond、MATH-500），主模型为Qwen3.5-9B。在交叉问题实验中，n=40时所有后端的准确率变化置信区间均包含零（如MATH-500上git下降-5.0pp，CI[-12.5,0]），n=98时git仅+1.0pp（CI[-10.2,+11.2]），均未支持记忆有效的假设。在n=500的大规模实验中，自一致性（+3.4pp，CI[+0.6,+6.2]）是唯一显著提升准确率的方法，而所有记忆后端（如向量+1.6pp，CI[-1.4,+4.6]）和静态few-shot（+0.4pp）均不显著。相似度实验发现记忆仅在余弦相似度>0.85时有效（如7B模型+12.7pp，CI[+8.4,+17.3]），而方法迁移（余弦0.72）无效果（7B：-4.1pp；32B：-3.6pp），表明增益来自答案复制而非方法提取。系统对比显示GitOfThoughts（47.0%）比Vanilla（33.0%）高14pp，但主要归因于更大计算预算和MCQ-aware扩展。

### Q5: 有什么可以进一步探索的点？

论文的局限性首先在于其核心发现——在未见问题上，任何记忆格式都无法提升准确率，这强烈暗示了当前LLM推理的“复制性阈值”可能是一个根本性障碍。未来最直接的方向是完成预注册的合并记忆准确性实验，但考虑到该阈值，预期效果微弱。一个关键改进点是测试前沿模型与丰富情景记忆（完整推理链而非提炼教训）的组合，这最有可能降低阈值，实现方法迁移而非单纯答案检索。此外，应进行算力匹配的基线对比，确保自一致性采样等简单方法不被不公平地限制计算资源。更远期的探索包括跨episode迁移（非平坦agent）以及分布式持久化执行，以验证GitOfThoughts在更复杂生态下的可扩展性。最后，论文中撤稿和反驳假设的自我严谨态度值得推广，但这也提示研究社区需警惕类似“假阳性”结果在记忆增强领域的普遍存在。

### Q6: 总结一下论文的主要内容

论文提出GitOfThoughts，将大语言模型的推理树存储为git仓库，每个评分思考节点对应一次提交，评分作为注释，结果作为标签，检索通过“git log”实现，使推理过程可重放、可审计、可合并。核心贡献在于定义了一个新问题：LLM推理是最后一个非版本化的软件过程，并提供了零成本的版本控制解决方案。通过五个记忆基板（无、markdown、向量、图、git）和两个基准测试的系统实验，论文得出主要结论：对于新问题，任何记忆格式都不能可靠提升准确性。只有当检索到的案例与当前问题近乎重复（相似度>0.8）时，准确性才显著提升（7B模型+12-13.5pp，32B模型+22.5-28.5pp），且增益来自答案检索而非方法迁移。模型规模扩大4.5倍仅增强这种效应，未能实现抽象迁移。唯一的通用杠杆是测试时采样（+3.4pp）。因此，git作为基板的真正价值在于审计性、溯源性和可合并性，而非检索提升。
