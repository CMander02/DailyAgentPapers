---
title: "APEX: Adaptive Principle EXtraction A Three-Layer Self-Evolution Framework for Production AI Agents"
authors:
  - "Ya-Chuan Chen"
  - "Tien-Jen Lai"
  - "Hsiang-Wei Hu"
date: "2026-06-13"
arxiv_id: "2606.15363"
arxiv_url: "https://arxiv.org/abs/2606.15363"
pdf_url: "https://arxiv.org/pdf/2606.15363v1"
categories:
  - "cs.AI"
tags:
  - "多智能体协作"
  - "Agent架构"
  - "Agent训练方法"
  - "自我进化"
  - "生产环境Agent"
  - "行为原则提取"
  - "工作流拓扑优化"
relevance_score: 9.0
---

# APEX: Adaptive Principle EXtraction A Three-Layer Self-Evolution Framework for Production AI Agents

## 原始摘要

Self-improvement in AI agents has emerged as a key research frontier: systems that modify their own prompts, workflows, and decision rules based on accumulated operational experience. The state-of-the-art Self-Harness framework [1] achieves 14--21% improvement on Terminal-Bench-2.0 by mining failure clusters and patching the agent harness. However, Self-Harness optimises only one dimension -- the prompt harness -- leaving behavioural principles and workflow topology unchanged. We propose APEX (Adaptive Principle EXtraction), a three-layer co-evolution framework that simultaneously evolves: (L1) the harness via failure-mode patching, (L2) behavioural principles via success-trace distillation [2], and (L3) the agent workflow topology via structural fitness-based selection [6]. We implement APEX on Joe [13], a production-grade super AI Agent built on NVIDIA Nemotron and designed as an Edge AI Agent Factory for the NVIDIA Agent Challenge 2026, managing a 15-node compute fleet using 114 real task traces collected over 18 days. APEX achieves an APEX Health Score of 0.570 (+90% vs. baseline 0.300) in a single evolutionary run, distilling 6 novel reusable principles and selecting a research-first workflow topology scoring 0.900 (+20%). Our results demonstrate that multi-dimensional co-evolution substantially outperforms single-axis harness optimisation, at a cost of only 4 LLM calls (~270 s) on a local qwen2.5-coder:32b instance.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决生产环境中AI代理面临的配置僵化问题。研究背景是，现代AI代理在部署后，其初始配置（包括系统提示、工作流程结构和决策规则）会随着环境、用户需求和任务分布的变化而逐渐失效。传统方法依赖于缓慢、昂贵且与生产实际脱节的人工提示工程循环。

现有方法如Self-Harness、EvolveR、EvoAgentX和Reflexion等虽实现了自动自我改进，但它们的不足在于都只针对单一维度进行优化（例如，Self-Harness仅优化提示词，而工作流拓扑和行为原则保持不变），忽略了其他重要维度。这导致即使一个维度完美，其他维度的次优状态仍会造成系统性失败。

本文提出的核心问题是：如何让生产级AI代理能够沿着多个关键维度（即提示词、行为原则、工作流拓扑结构）同时进行协同自我进化，以克服单一维度优化的局限性，实现更全面、更鲁棒的性能提升。为此，论文提出了APEX（自适应原则提取）框架，这是一个三层次共同进化框架。

### Q2: 有哪些相关研究？

### 相关研究

本文的相关工作可按以下类别组织：

**1. 方法类（优化维度）**
- **Harness优化**：Ye等人的Self-Harness框架通过故障挖掘与补丁生成实现14-21%提升，但仅优化prompt层，忽略行为原则与工作流拓扑。
- **原则提炼**：Li等人从成功轨迹中离线蒸馏原则，强调“从成功中学习”优于仅修复失败，但未涉及harness修改或拓扑搜索。
- **工作流拓扑搜索**：Zhang等人用蒙特卡洛树搜索优化LLM调用DAG，Wang等人结合TextGrad/AFlow/MIPRO，但均依赖人工基准，未利用生产轨迹信号。

**2. 应用类（学习范式）**
- **语言强化学习**：ReAct/Reflexion通过反思实现单轮自适应，APEX将其扩展为批处理版本，系统化提取补丁与原则。
- **持续适应**：Gao等人的LoRA微调与在线无梯度自适应方法可作为未来权重级进化补充，但当前APEX专注prompt/原则/拓扑协同进化。

**3. 评测缺口**  
现有研究均未实现从共享生产轨迹池中同时进化三个维度（harness、原则、拓扑），APEX填补这一空白，无需合成基准与外部API即可实现多维度协同优化。

### Q3: 论文如何解决这个问题？

APEX通过一个三层协同进化框架来解决AI智能体自我改进的问题，克服了现有方法仅优化单一维度（如提示词）的局限性。核心架构包含三个并行运行的层，均从共享的生产环境追踪数据库中提取信息。

**第一层（L1：Harness补丁）**：聚焦于故障模式识别。它通过关键词（如error, fail）从追踪库中筛选出失败轨迹，并将最近的30条失败轨迹提交给本地LLM（qwen2.5-coder:32b），要求识别出前3个系统性故障模式及其根本原因和具体的禁止规则。这些规则被转化为显式的提示词规则块，注入到下一代智能体的系统提示中，用于预防类似错误。

**第二层（L2：行为原则提炼）**：专注于从成功经验中学习。它使用多因子质量评分公式，综合评估任务轨迹中的教训长度、动作数量、文件修改情况等，筛选出高质量的成功轨迹。这些轨迹被提交给LLM，要求提取6个可复用的行为原则。每个候选原则会通过余弦相似度进行新颖性评估，只有新颖性得分≥0.3的原则才会被采纳，确保提炼出的原则是全新的、可执行的。

**第三层（L3：工作流拓扑进化）**：对智能体的工作流拓扑（有向无环图DAG）进行结构优化。它定义了一组标准节点（如research, plan, code, review, verify），并使用结构适应度函数对每个拓扑进行评分。该函数奖励包含review、verify、research等关键环节以及循环回溯路由的结构，同时惩罚节点数过多的复杂拓扑。通过变异操作（如添加research节点、插入verify阶段）生成新的拓扑候选，经过多代选择，找到最优工作流结构。

三个层的输出（补丁规则、行为原则、最优拓扑）最终通过一个健康分数（APEX Health Score）进行聚合，综合评估智能体的整体改进效果。该框架的创新点在于实现了多维度的共同进化，而非单一维度优化。通过分别处理失败模式、成功经验和全局工作流结构，APEX能够从不同角度全面提升智能体性能，且仅需4次LLM调用（约270秒），计算成本低廉。

### Q4: 论文做了哪些实验？

论文在Joe智能体上进行了实验，该智能体基于NVIDIA Nemotron，管理15节点计算集群（192.168.1.x子网）。实验使用114条真实任务执行轨迹（18天收集），涵盖AI/ML部署（32%）、系统管理（28%）、前端/Web开发（22%）、网络（12%）和安全加固（6%）五个领域。所有LLM调用通过Ollama使用qwen2.5-coder:32b，无外部API依赖。

主要实验对比了三种配置：基线（无进化）、Self-Harness（仅L1）和APEX。APEX Health Score H从基线0.300提升至0.570（+90%），Self-Harness为0.380（+27%）。APEX提取了6个新型原则，探索了10种拓扑结构，最佳工作流分数0.900（+20%），每次演进仅需4次LLM调用（约270秒）。

消融实验显示：仅L1（Self-Harness）得0.380（+26.7%），仅L3得0.270（-10%），L1+L2得0.500（+66.7%），L1+L3与完整APEX均得0.570（+90%）。结果表明：L1+L3组合优于L1+L2（0.570 vs 0.500），工作流拓扑优化贡献（+0.190）超过原则丰富度（+0.120）；L3单独优化需以L1为基础。APEX完整版因L2原则尚未注入工作流，性能与L1+L3相同，预计注入后H可达0.65-0.70。

### Q5: 有什么可以进一步探索的点？

论文的局限性与未来探索方向主要集中在以下几点: (1) L3的结构评分目前依赖手工启发式规则而非实际任务完成率，未来应基于保留轨迹进行评估，使拓扑选择更贴合真实性能；(2) L2提取的原则已正确存储但尚未在装配时注入，完成注入预计可将Health Score提升至0.65-0.70；(3) 当前仅优化提示和工作流层面，引入Online-LoRA作为第4层权重进化，有望从生产数据中学习参数，带来额外10-20%改进；(4) 仅针对单智能体，扩展到多智能体团队拓扑演化，并实现跨智能体的原则共享，是重要方向。此外，我认为可探索自适应的L3评估权重，根据当前轨迹分布动态调整结构评分，避免手动启发式的偏差；同时尝试将L1失败模式与L2成功原则进行交叉验证，形成更鲁棒的闭环修正机制，进一步提升多维协同进化的稳定性。

### Q6: 总结一下论文的主要内容

APEX提出三层次协同进化框架，用于AI代理的自我完善。问题在于现有方法如Self-Harness仅优化单一维度（提示框架），忽略了行为原则和工作流拓扑。该方法包括：L1通过失败模式修补框架、L2从成功轨迹提炼可复用的行为原则、L3基于结构适应度选择优化工作流拓扑。在管理15节点计算集群的生产级代理Joe上，使用114条真实任务轨迹进行单次进化实验，实现了0.570的健康得分，相比基线的0.300提升90%，并蒸馏出6条新颖原则，工作流拓扑得分提升20%。总成本仅需4次LLM调用（约270秒）在本地qwen2.5-coder:32b实例上。核心贡献是证明多维协同进化显著优于单轴优化，且发现L3拓扑进化需要L1框架基础才能发挥正面作用，这种非加性交互是单轴框架无法捕捉的。
