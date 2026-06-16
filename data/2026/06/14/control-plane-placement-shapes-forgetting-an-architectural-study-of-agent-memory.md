---
title: "Control-Plane Placement Shapes Forgetting: An Architectural Study of Agent Memory Across Thirteen System Configurations"
authors:
  - "Dongxu Yang"
date: "2026-06-14"
arxiv_id: "2606.15903"
arxiv_url: "https://arxiv.org/abs/2606.15903"
pdf_url: "https://arxiv.org/pdf/2606.15903v1"
github_url: "https://github.com/deeplethe/lethe"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent memory"
  - "Forgetting evaluation"
  - "Memory architecture"
  - "LLM agent pipeline"
  - "Adversarial evaluation"
relevance_score: 8.5
---

# Control-Plane Placement Shapes Forgetting: An Architectural Study of Agent Memory Across Thirteen System Configurations

## 原始摘要

Where an LLM sits in an agent memory pipeline -- between the recall plane that retrieves stored facts (extensively benchmarked) and the control plane that mutates them via supersede, release, purge (largely untested) -- shapes which forgetting failure modes the system recovers. Comparing thirteen system configurations on a 385-case adversarial surface, we observe three placement regimes with partly complementary coverage: deterministic primitives suffice for lexical/temporal categories but fail canonicalization (5% on identifier-obfuscation, 0% on cross-lingual); inscribe-time LLM recovers canonicalization (100%) but cannot help intent-aware deletion (0% on prefix-collision and compound-fact); a mutation-time hook recovers intent-aware deletion (78-85%) and brightens nearly all categories simultaneously (91.7-93.2% overall, $0.17 per 385-case run, 2.3s/case mutation latency vs. 64-191ms/case deterministic, recall path unchanged).
  We expose the trade-off via ForgetEval, a 1000-case templated suite plus a 385-case adversarial layer (132 hand-crafted + 253 LLM-drafted oracle-validated) scored by deterministic substring match, paired with a six-method Adapter Protocol with honest N/A scoring that lets heterogeneous memory stores enter in 130 lines. Admission is corroborated by 10-annotator IAA (Fleiss' kappa = 0.958) and a 77-case external-authored subset (four blind contributors) that replicates the canonicalization asymmetry and amplifies the joint-placement lift (+27.8 pt). Production failures are predominantly forgetting failures rather than recall failures, yet existing benchmarks measure only recall. ForgetEval and all adapters are released under MIT.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）智能体系统中被现有研究忽视的“遗忘”问题。当前研究背景是，几乎所有记忆框架和基准测试（如LongMemEval、MTEB、BEIR等）都聚焦于“回忆”平面——即从记忆中检索正确的事实，并追逐更高的召回率。然而在生产环境中，系统最常见的失败并非是回忆失败，而是遗忘失败：例如，用户三个月前轮换的密码仍被推荐，用户根据GDPR行使“被遗忘权”后数据仍出现在推荐候选池，或过期的验证码与长期偏好一起被永久保留。现有方法的不足在于：它们只测量“检索到正确事实”的能力，完全没有评估系统能否被命令去正确“遗忘”或“突变”记忆存储。

本文要解决的核心问题是：在智能体记忆流水线中，控制平面（负责突变存储，如替换、释放、清除）的设计与被遗忘能力之间的关系。具体而言，论文研究了LLM在记忆流水线中的“放置位置”（是在写入时、在突变时、还是仅靠确定性规则）如何系统性塑造不同类别的遗忘失败模式。其核心发现是，遗忘失败模式由LLM在记忆架构中的放置位置决定，而非仅仅是否使用LLM——通过对比13种系统配置，揭示了不同放置方案（如确定性原语、写入时LLM、突变时钩子）之间存在部分互补而非冗余的覆盖能力，从而暴露了各种遗忘类别（如规范化、意图感知删除、词法/时序正确性）之间的权衡。

### Q2: 有哪些相关研究？

根据论文和相关工作，相关研究可分为以下几类：

**方法类**：本文提出的ForgetEval定位于遗忘轴（forgetting axis）的存储层（memory-store）基准测试。最接近的工作是ICLR 2026的FactConsolidation任务，但本文有三点不同：粒度上，FactConsolidation仅测试单事实替换，而ForgetEval解构为5个原始家族和10个对抗类别（含遗忘、清除、衰减等）；评分上，ForgetEval使用确定性子串匹配以消除LLM评判的可复现性问题；适配器协议方面，ForgetEval提供了6方法协议和N/A评分，而FactConsolidation仅评估端到端代理。

**应用类**：记忆框架如MemGPT、Zep、HippoRAG等主要关注召回（recall），而本文关注的是存储层中控制平面（如替换、释放、清除操作）导致的遗忘故障模式。

**评测类**：LongMemEval、LOCOMO、AMA-Bench等现有基准主要评估对话召回或端到端代理行为，未专门测试遗忘原始操作。2026年4月的FAMA引入了单一聚合指标惩罚过时内存重用，但本文在粒度、对抗样本和确定性评分方面形成互补。此外，机器遗忘研究（如模型编辑、参数删除）针对的是权重层面，而非本文聚焦的存储层原始操作。

### Q3: 论文如何解决这个问题？

核心方法围绕控制平面在记忆管线中的放置位置展开，提出了三种架构配置：确定性原语、写入时LLM、变异时钩子。整体框架由ForgetEval评估套件和适配器协议组成。

ForgetEval包含1000个模板化案例和385个对抗性案例（132个人工编写+253个LLM生成并经预言机验证），覆盖取代、衰减、遗忘、清除、漂移五种记忆失效模式。每个案例包含设置事实、变异操作、最终查询和必须包含/不得包含的字符串，通过确定性子串匹配评分。适配器协议定义了六个方法的接口：三个强制召回平面原语（reset、inscribe、recall_texts）和三个可选控制平面变异（supersede、release、purge），使用诚实N/A评分，允许异构记忆存储用130行代码接入。

关键技术包括：
1. **两种LLM放置策略**：写入时LLM在事实写入时调用LLM解决正则化问题（如标识符混淆、跨语言）；变异时钩子在每次变异操作时调用LLM，针对意图感知删除（如前缀碰撞、复合事实）。
2. **分层评估**：模板套件具有平坦难度，对抗层扩展了10种攻击类别，通过两阶段准入协议（结构检查+独立LLM法官）确保质量，10位标注者的Fleiss kappa=0.958。
3. **消融实验**：在13种系统配置下评估，发现变异时钩子显著提升整体性能（91.7-93.2%准确率，但延迟为2.3秒/案例），而确定性方法在词法/时间类别上有效但正则化失败（0-5%）。写入时LLM恢复正则化（100%）但无法处理意图感知删除（0%）。

### Q4: 论文做了哪些实验？

论文在13种系统配置上进行了三类实验。首先是在1000个模板化案例（ForgetEval-Template）上测试基础召回，所有适配器使用all-MiniLM-L6-v2嵌入，对比Lethe v1 (99.30%)、LangMem (99.50%)、Mem0 (88.80%)和Palace (0.00%)。

核心实验是385个对抗性案例（ForgetEval-Adv），包含10个攻击类别（132个手工+253个LLM起草并经oracle验证），采用确定性子串匹配评分。结果显示：Lethe (63.4%)、Mem0 (68.3%)、LangGraph (62.9%) 三个确定性系统聚集在63-68%的通过带内，威尔逊区间重叠。而在具体类别上，Lethe在prefix_collision上82% vs Mem0的31%，但Mem0在cross_lingual_id上55% vs Lethe的0%。当在变异时间添加LLM钩子（DeepSeek-V3，每次运行约$0.17/385案例），Lethe+LLM达到91.7%，LangGraph+LLM达到93.2%，且2.3秒/案例的突变延迟。inscribe-time LLM（如Amem, Mem0+v3）能恢复规范化（100%）但无法处理意图感知删除。

最后在Memora-weekly基准测试（10个角色，150个问题）上，Palace (40%)从ForgetEval的0/385翻转到领先，而Lethe (31%) vs LangGraph (45%)的排名也发生反转，证明了两个基准测量互补的遗忘轴。10个标注者的Fleiss' kappa=0.958，外部77案例子集复现了规范化不对称性，联合放置提升27.8个百分点。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于语言和脚本覆盖的偏向性，特别是非拉丁语系（如韩语、阿拉伯语、印地语）样本量过少（1-3例），导致无法在统计上区分不同LLM挂载系统的优劣，未来需扩大长尾脚本的采样规模。此外，当前评估仅关注英文，构建多语言、多文化的遗忘基准是重要方向。其次，记忆系统的覆盖存在缺口：如MemGPT因无release原语导致大量N/A，Graphiti和HippoRAG这类知识图谱系统因抽象化而无法匹配子串评分。未来应设计支持软删除和语义级遗忘评估的元协议。从架构角度看，当前工作展示了控制面（如变异时挂载）和召回面（如向量）的互补性，但未深入探索将两者动态融合的混合策略，例如根据遗忘类别自动切换挂载位置。最后，成本与延迟权衡值得优化：变异时hook虽然效果好，但延迟高达2.3秒/例，是纯确定性的20倍以上，未来可通过缓存LLM输出或使用更轻量模型来降低开销，同时保持92-93%的召回率。

### Q6: 总结一下论文的主要内容

这篇论文系统研究了LLM在Agent记忆管线中的控制平面放置位置如何影响遗忘失败模式。现有基准仅评估召回能力，忽略了遗忘这一生产环境中的关键故障来源。作者定义了记忆控制平面中的遗忘问题，并设计了包含1385个案例的ForgetEval基准（含1000个模板案例和385个对抗案例），覆盖5种遗忘结构家族和10种攻击类别。通过在13种系统配置上的实验，识别出三种具有互补性的LLM放置模式：确定性原语处理词法/时间类别但规范化解题失败（标识符混淆5%、跨语言0%）；写入时LLM恢复规范化（100%）但无法处理意图感知删除（0%）；变异时钩子恢复意图感知删除（78-85%）并显著提升整体性能（91.7-93.2%），每次运行成本约0.17美元。研究表明遗忘失败比召回失败更普遍，而遗忘性能由LLM在架构中的放置位置决定，而非仅依赖其存在与否，为Agent记忆系统设计提供了新视角。
