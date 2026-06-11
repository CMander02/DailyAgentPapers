---
title: "Exploration Structure in LLM Agents for Multi-File Change Localization"
authors:
  - "Akeela Darryl Fattha"
  - "Kia Ying Chua"
  - "Lingxiao Jiang"
  - "Laura Wynter"
date: "2026-06-10"
arxiv_id: "2606.11976"
arxiv_url: "https://arxiv.org/abs/2606.11976"
pdf_url: "https://arxiv.org/pdf/2606.11976v1"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Code Agent"
  - "Multi-Agent"
  - "Software Engineering Agent"
  - "File Localization"
  - "SWE-bench"
  - "Agent Architecture"
relevance_score: 9.5
---

# Exploration Structure in LLM Agents for Multi-File Change Localization

## 原始摘要

Software engineering tools increasingly rely on LLM based agents to localize files to change to resolve a software issue. Most AI agents explore repositories linearly, that is, visiting one directory or file per step. We postulate that this is a structural mismatch for changes that span several subsystems. We compare linear sequential exploration against non-linear, domain-scoped parallel agentic exploration. Using SWE Bench Pro as initial benchmark, we focus on ansible as an exemplar. We construct an approach for persistent-session evaluation of GitHub issues anchored at a single base commit. We compare our non-linear domain-agent file traversal system against a base LLM without direct repository access, a single agent Recursive Language Model (RLM) baseline with a persistent Python REPL and an external CLI baseline using Codex 5.5 High. Domain scoped parallel agent spawning with a small Haiku-class model achieves the highest micro F1 among Haiku class models by a large margin. Domain-agents is the second highest behind only the much larger Codex 5.5 High on our own expanded benchmark including over more recent PRs from 2025 and 2026. On the original, curated, 2020 SWE-bench Pro benchmark, a larger Sonnet plain LLM baseline attains higher micro F1 by predicting few files, leading to higher precision, but at significantly lower all gold recall. We also present three additional findings. First, documentation evolution is a latent dependency unresolved by any approach. Second, naive file system access can degrade localization driven by test-file over prediction. Lastly, forced multi-agent consultation does not measurably help and raises token cost substantially.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于 LLM 的智能体在进行多文件变更定位时存在的结构性探索缺陷问题。当前主流方法（如 SWE-agent、AutoCodeRover）普遍采用线性顺序探索模式，即智能体逐步骤访问单个目录或文件。对于横跨多个子系统的软件变更，这种线性策略存在根本性不足：智能体必须预先猜测起始点，且其步骤或令牌预算往往在探索第一个子系统时即被耗尽，导致后续包含关键文件的子系统完全未被触及。研究试图通过引入非线性、领域限定的并行智能体探索结构来克服这一限制。具体而言，论文提出了三个核心待解决问题：(1) 线性探索结构是否本质上限制了多文件变更的定位能力，抑或更强的模型能弥补这一缺陷；(2) 赋予智能体原始文件系统访问权限是否总能可靠地提升定位性能，还是反而可能因导航错误和过度预测（如误入大型测试目录）而损害准确性；(3) 强制多个智能体协作是否真的能提升召回率，还是仅仅因引入无关子系统的噪声而降低整体性能。通过控制实验，论文旨在证明探索结构本身是影响多文件变更定位效果的关键二阶因素。

### Q2: 有哪些相关研究？

根据论文背景部分，相关研究可分为以下几类：

1. **基于信息检索的文件定位方法**：如BugLocator、BLUiR、AmaLgam及BugScout等主题模型变体，通过文本相似度对文件排序。本文采用BM25作为基线，但指出这些方法在处理用户视角的问题描述时存在弱点，且本文在更难的基准（多文件修改率达80%）上评估。

2. **基于学习的定位与程序修复**：包括DeepLocator等神经排序方法，以及Genprog、TBar、SequenceR等自动修复系统。本文与这些工作的区别在于专注纯文件定位评估，排除补丁质量和测试执行干扰。

3. **基于LLM的软件工程智能体**：包括SWE-bench系列、Agentless、SWE-agent、OpenHands、AutoCodeRover、MAGIS、SWE-Search等。本文的核心区别在于：①在隔离环境中评估文件定位，解耦探索策略与补丁质量；②采用基于仓库子系统而非任务角色的并行多智能体分解。

4. **递归语言模型（PLM）**：通过持久Python REPL增强长上下文推理。本文的单智能体RLM基线直接应用该范式，但发现其优势无法迁移到结构化多文件仓库。

5. **共变与逻辑耦合**：相关工作揭示了文档与源文件的协同演化关系，这与本文发现的文档演化潜在依赖问题一致。

6. **长上下文代码理解**：LongBench-v2等基准测试长上下文推理。本文将此方向从单文档扩展至多文档磁盘仓库场景。

### Q3: 论文如何解决这个问题？

论文提出了一种基于领域限定并行智能体的非线性文件定位方法，以解决传统线性探索与多文件变更需求之间的结构性不匹配。整体框架包含三个核心组件：根协调器、持久化领域智能体和受限仓库I/O层。初始化阶段，根协调器首先对仓库进行轻量探索，识别出如ansible项目中的lib/ansible/cli/等独立维护区域，为每个区域创建专门领域智能体并生成区域摘要，该知识可跨查询复用。查询时，根协调器读取智能体注册表，判断相关领域后并行派发多个领域智能体进行探索，每个智能体负责分析其指定区域并返回候选文件及理由，最后由协调器合并过滤得到最终预测。

关键技术方面，论文提出了三方面创新：一是仓库结构化上下文管理，包括有界文件读取（只暴露压缩预览和检索片段）、句柄式大文件访问（通过字典句柄在程序环境中处理）和紧凑相对树形目录展示（相比逐行全路径节省40.8%输入token）。二是最小化提示工程，采用简洁工具描述替代大量少样本示例。三是受限递归机制，仅在环境内允许本地总结调用，避免完整协调器循环复制。该方法使用Haiku小模型实现，在SWE Bench Pro基准测试中，其微F1值远超同等规模模型，仅略低于体积大得多的Codex 5.5 High。消融实验显示，并行领域派发是性能提升的关键，而强制多智能体协商反而无益且增加token成本。

### Q4: 论文做了哪些实验？

论文在SWE-Bench Pro Ansible基准测试及其扩展的PR基准测试上进行了实验，涵盖19个GitHub issue。对比方法包括：Plain LLM（Haiku/Sonnet，无仓库访问）、Single-agent RLM（Sonnet/Haiku，有REPL访问）、Domain agents（自适应/无生成/提示变体，Haiku模型）、Codex 5.5 High和BM25基线。主要结果：在原始基准上，Plain LLM Sonnet取得最高微F1（0.467±0.028），但以低召回为代价（全金4.0/19）；在扩展PR基准上，Codex 5.5 High最优（微F1 0.523±0.071，全金9.2±0.6），Domain agents自适应变体（Haiku）位列第二（微F1 0.408±0.018，全金6.4±0.7），且显著优于所有Haiku类方法（Plain LLM仅0.184，RLM仅0.147）。BM25最佳F1仅约0.24。此外，文档检索极差（仅Codex找回3.2/9文件），强制多agent协商无帮助且增加token成本（从16.1M升至25.1M）。

### Q5: 有什么可以进一步探索的点？

论文提出了一种非线性的域范围并行智能体探索结构，但在局限性和未来方向上仍有几个值得探索的点。首先，文档演变作为潜在依赖未被解决，未来可研究动态知识库或增量更新机制，以缓解文档过时对定位的负面影响。其次，朴素文件系统访问因过度预测测试文件而降低定位精度，建议引入测试文件与源文件的关联推理或依赖图剪枝策略。第三，强制多智能体协作未提升效果且增加token成本，这表明需要更高效的任务分配或选择性协作机制，如基于置信度的门控调用。此外，当前基准聚焦于Ansible和SWE-bench，扩展到其他领域（如Web应用或嵌入式系统）可验证通用性。最后，利用小模型（如Haiku类）通过域并行取得较好F1，显示资源效率与性能的平衡潜力，未来可探索自适应模型选择（根据任务复杂度动态切换模型大小），或结合检索增强生成进一步优化探索路径的广度与深度。

### Q6: 总结一下论文的主要内容

这篇论文研究了LLM Agent在代码仓库中定位多文件变更时的探索结构问题。作者指出，现有方法多采用线性探索模式（每次访问一个目录或文件），这可能导致在处理跨多子系统的变更时，因步骤或token预算耗尽而遗漏后续子系统中的目标文件。为此，论文提出了一种领域限定的并行多Agent探索系统，使用小模型（Haiku-class）并行派生子Agent进行非线性、领域限定的探索。在基于SWE-Bench Pro和自定义扩展基准的实验表明，该方法在Haiku-class模型中取得了最高的Micro F1值，性能仅次于使用更大模型（Codex 5.5 High）的CLI基线。主要结论包括：1）文档协同演化是现有方法无法解决的潜在依赖；2）原始文件系统访问可能因过度预测测试文件而降低定位精度；3）强制多Agent协商无益且显著增加token开销。论文的核心贡献在于揭示了探索结构是影响多文件变更定位的第二阶因素，并验证了并行探索策略在提升小模型性能方面的有效性。
