---
title: "D3-Gym: Constructing Real-World Verifiable Environments for Data-Driven Discovery"
authors:
  - "Hanane Nour Moussa"
  - "Yifei Li"
  - "Zhuoyang Li"
  - "Yankai Yang"
  - "Cheng Tang"
  - "Tianshu Zhang"
  - "Nesreen K. Ahmed"
  - "Ali Payani"
  - "Ziru Chen"
  - "Huan Sun"
date: "2026-04-30"
arxiv_id: "2604.27977"
arxiv_url: "https://arxiv.org/abs/2604.27977"
pdf_url: "https://arxiv.org/pdf/2604.27977v2"
github_url: "https://github.com/OSU-NLP-Group/D3-Gym"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "科学智能体"
  - "评测基准"
  - "数据驱动发现"
  - "环境构建"
  - "训练数据"
relevance_score: 9.0
---

# D3-Gym: Constructing Real-World Verifiable Environments for Data-Driven Discovery

## 原始摘要

Despite recent progress in language models and agents for scientific data-driven discovery, further advancing their capabilities is held back by the absence of verifiable environments representing real-world scientific tasks. To fill this gap, we introduce D3-Gym, the first automatically constructed dataset with verifiable environments for scientific Data-Driven Discovery. D3-Gym comprises (1) 565 tasks sourced from 239 real scientific repositories across four disciplines where (2) each task is equipped with a natural language instruction, an executable environment with pre-installed dependencies, input dataset and artifact previews, a reference code solution, and an automatically synthesized evaluation script. Rigorous evaluation of the quality of the verification signal in D3-Gym confirms that our evaluation scripts achieve 87.5% agreement with human-annotated gold standards and strong alignment in domain-specific evaluation logic, showing their scientific soundness. Further, training on trajectories sampled from D3-Gym yields consistent and substantial gains across Qwen3 models of varying sizes on ScienceAgentBench, boosting Qwen3-32B by 7.8 absolute points and substantially shrinking the gap with strong proprietary models. All D3-Gym artifacts (environments, creation workflow, trajectories, and models) can be found at https://github.com/OSU-NLP-Group/D3-Gym.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决在科学数据驱动发现中缺乏真实世界可验证环境的问题。研究背景是语言模型和智能体在科学发现中已展现出潜力，可通过编程测试假设并推导科学见解，但现有方法受限于基础设施不足。关键瓶颈在于：构建可验证环境（如AutoResearch中手动准备的任务指令、数据集、评估脚本等）需要大量人工投入，难以规模化扩展。现有的软件工程领域可直接复用仓库中的单元测试作为验证信号，但科学任务面临独特挑战——相关仓库几乎不包含预置评估脚本，且程序输出是领域特定的，无法用通用标准判断正确性。为此，本文提出D3-Gym，这是首个自动构建的包含可验证环境的数据集。其核心思路是：从大量候选任务出发（通过AutoSDT收集），设计严格的过滤步骤和执行验证流程，保留高质量实例；重点创新在于两阶段评估脚本合成方法——首先生成任务特定的详细评估计划，再将其转化为可执行脚本。最终产出包含565个任务（覆盖生物信息学、计算化学、地理信息科学、心理学与认知神经科学四个学科，源自239个真实仓库），每个任务配备自然语言指令、可执行环境、数据集预览、参考代码及自动评估脚本。实验显示评估脚本与人工标注的通过/失败判定有87.5%一致率，且通过该数据集训练可显著提升开源模型在科学智能体基准上的表现（如Qwen3-32B提升7.8个绝对百分点）。

### Q2: 有哪些相关研究？

在相关研究方面，本文主要涉及三类工作。**方法类**：AutoSDT 提供了候选任务收集的基础，而 AutoResearch 展示了手动创建可验证环境的价值，但受限于人工成本；本文的自动构建流程针对科学任务中缺乏现成单元测试的挑战，通过两阶段评估脚本合成（先写计划再转可执行脚本）实现了规模化。**评测类**：ScienceAgentBench 作为评测基准，本文通过在其上进行拒绝采样微调，验证了 D3-Gym 训练轨迹的有效性，且 32B 模型提升了 7.8 个绝对点，接近 OpenAI o1。**应用类**：与软件工程领域（如 SWE-bench）可直接复用仓库中的单元测试不同，科学数据驱动发现任务的输出具有领域特异性，无法用通用标准评估；本文通过严格的筛选和执行验证，保留了四大学科（生物信息学、计算化学、地理信息科学、心理学与认知神经科学）的 239 个仓库中的 565 个高质量任务。总体而言，本文填补了自动化构建科学领域可验证环境的数据集空白，与现有工作相比，其核心区别在于实现了从手动到自动的扩展，并通过合成评估脚本与人工标准的高一致性（87.5%）验证了其科学性。

### Q3: 论文如何解决这个问题？

D3-Gym通过一个四阶段自动构建流程来解决缺乏可验证真实科学环境的问题。首先，候选任务收集阶段利用AutoSDT从GitHub爬取科研仓库，经过多步过滤识别数据驱动的科学工作流，将其改编为参考代码方案并配以自然语言指令，同时提取依赖文件夹。其次，过滤与数据集预览创建阶段使用Claude Code验证文件依赖，仅保留基于真实数据文件的任务，并为每个输入数据文件生成结构化摘要作为数据预览。第三，执行与输出验证阶段在隔离环境中运行参考方案，通过pipreqs安装依赖，并采用多模态LLM裁判（GPT-5.2，与人类一致性92.31%）检查输出是否完整且有意义，剔除执行失败或退化的任务。核心创新在于第四阶段：将评估脚本生成分解为计划与编码两个连续阶段。在计划阶段，向Claude Sonnet 4.5提供任务指令、数据预览和已验证输出，利用其参数化科学知识生成详细评估计划，指定检查哪些输出工件、适用哪些科学指标以及接受标准（含容差阈值、精确或近似匹配、领域合理的性能边界）。在编码阶段，将计划传递给同一模型单独生成可执行评估脚本。该设计通过分离高层推理与实现细节提升了评估脚本质量。整体框架包含565个任务，覆盖四个学科239个真实仓库，每个任务配有指令、可执行环境、输入数据、参考方案和自动合成的评估脚本。经严格验证，银级评估脚本与人类标注金标准在通过/失败判定上达成87.5%一致性，并在指标选择、阈值设定和工件检查等评估逻辑上高度对齐。

### Q4: 论文做了哪些实验？

D3-Gym 论文针对科学数据驱动发现任务，构建了首个自动生成的可验证环境数据集，并设计了三类实验验证其有效性。

首先，**验证信号质量评估**实验：从239个真实科学仓库中筛选出565个任务，涵盖四个学科领域。每个任务包含自然语言指令、可执行环境（预装依赖）、输入数据集、代码参考方案及自动生成的评估脚本。评估结果显示，自动合成脚本与人工标注黄金标准的一致性达87.5%，且在领域特定评估逻辑上表现出强对齐，证明其科学合理性。

其次，**训练增强效果实验**：在不同规模（从小到32B）的Qwen3模型上，利用D3-Gym采样的轨迹进行微调。在ScienceAgentBench基准上，所有模型均获得一致且显著的性能提升，其中Qwen3-32B提升7.8个绝对百分点，大幅缩小了与强闭源模型（如GPT-4）的差距。

最后，**对比基线方法**：实验未显式提及其他对比方法，但通过消融研究（如训练前后对比）和跨模型规模验证，凸显了D3-Gym环境对智能体数据驱动发现能力的强化效果。所有数据、创建流程、轨迹及模型均已开源。

### Q5: 有什么可以进一步探索的点？

D3-Gym的局限性体现在任务来源和分析的广度上。尽管覆盖了4个学科，但主要集中在数据科学任务（如数据清洗、可视化），缺乏对需要复杂设备交互的物理实验或需要严格数学推导的理论任务的验证。未来可扩展至更多学科，例如材料科学中的自动化合成实验或量子化学模拟。其次，自动生成的评估脚本与人类标准有12.5%的不一致，在科学严谨性要求极高的领域（如药物发现）可能引入系统性偏差。改进方向包括引入人类专家校验流程，或利用语言模型的自我反思能力迭代优化评估脚本。此外，当前任务多为单步或固定流程的“执行型”任务，缺乏涉及长期规划、多智能体协作的“探索型”任务。未来可设计包含子目标分解和环境反馈的层级式任务，例如通过查询数据库、优化算法参数完成完整科学发现流程。最后，D3-Gym的代码环境和依赖固定，无法模拟真实科研中因硬件限制或API变动导致的失败模式，可加入随机故障或资源约束来增强鲁棒性训练。

### Q6: 总结一下论文的主要内容

D3-Gym论文针对科学数据驱动发现中缺乏可验证真实环境的问题，提出了首个自动构建的包含可验证环境的数据集。该数据集包含565个任务，源自生物信息学、计算化学等四个学科的239个真实科学代码仓库。每个任务配有自然语言指令、可执行环境、输入数据、参考代码和自动合成的评估脚本。方法上，论文设计了自动流水线，通过质量过滤、执行验证和两阶段（规划+编码）评估脚本生成来构建环境。实验表明，自动合成的评估脚本与人工标注的金标准在通过/失败判定上达到87.5%的一致性，且评估逻辑高度对齐。在ScienceAgentBench基准上，基于D3-Gym轨迹进行拒绝采样微调后，Qwen3-32B模型性能提升7.8个绝对百分点，显著缩小了与强闭源模型的差距。该工作为训练和评估科学数据驱动发现模型提供了可扩展的基础设施。
