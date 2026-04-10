---
title: "Structured Distillation of Web Agent Capabilities Enables Generalization"
authors:
  - "Xing Han Lù"
  - "Siva Reddy"
date: "2026-04-09"
arxiv_id: "2604.07776"
arxiv_url: "https://arxiv.org/abs/2604.07776"
pdf_url: "https://arxiv.org/pdf/2604.07776v1"
categories:
  - "cs.LG"
tags:
  - "Web Agent"
  - "Knowledge Distillation"
  - "Synthetic Data Generation"
  - "Agent Training"
  - "Tool Use"
  - "Agent Architecture"
  - "WebArena"
  - "Open-weight Model"
  - "Supervised Learning"
  - "Generalization"
relevance_score: 9.0
---

# Structured Distillation of Web Agent Capabilities Enables Generalization

## 原始摘要

Frontier LLMs can navigate complex websites, but their cost and reliance on third-party APIs make local deployment impractical. We introduce Agent-as-Annotators, a framework that structures synthetic trajectory generation for web agents by analogy to human annotation roles, replacing the Task Designer, Annotator, and Supervisor with modular LLM components. Using Gemini 3 Pro as teacher, we generate 3,000 trajectories across six web environments and fine-tune a 9B-parameter student with pure supervised learning on the 2,322 that pass quality filtering. The resulting model achieves 41.5% on WebArena, surpassing closed-source models such as Claude 3.5 Sonnet (36.0%) and GPT-4o (31.5%) under the same evaluation protocol, and nearly doubling the previous best open-weight result (Go-Browse, 21.7%). Capabilities transfer to unseen environments, with an 18.2 percentage point gain on WorkArena L1 (an enterprise platform never seen during training) and consistent improvements across three additional benchmarks. Ablations confirm that each pipeline component contributes meaningfully, with Judge filtering, evaluation hints, and reasoning traces each accounting for measurable gains. These results demonstrate that structured trajectory synthesis from a single frontier teacher is sufficient to produce competitive, locally deployable web agents. Project page: https://agent-as-annotators.github.io

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决如何将前沿大语言模型（LLM）强大的网页导航与交互能力，高效地蒸馏到参数规模更小、可本地部署的开放权重模型中的问题。

研究背景是，以GPT-4、Claude等为代表的“前沿模型”在网页任务上表现出色，但它们依赖昂贵的API调用，存在数据隐私风险，且无法离线部署。而参数约9B的“小模型”虽易于本地部署，但其网页代理能力与前沿模型存在巨大差距（在WebArena基准上落后超过22个百分点）。现有方法如InSTA和NNetNav等，虽然探索了利用前沿模型作为“教师”来生成训练轨迹以蒸馏“学生”模型，但这些方法的设计各异，缺乏一个统一、可系统化分析和比较的框架，使得难以厘清各组件的作用和最佳实践。

因此，本文的核心问题是：如何构建一个结构化、可解释的合成轨迹生成框架，以高效地从单一前沿教师模型中蒸馏出网页代理能力，从而训练出既具备强大泛化性能、又可本地部署的小型学生模型。为此，论文提出了“Agent-as-Annotators”框架，其创新之处在于借鉴人类标注员创建网页任务基准（如WebArena）时的三种角色（任务设计者、标注者、监督者），并分别用模块化的LLM组件来替代，从而系统化地生成高质量的训练数据。通过此框架，论文证明了仅使用一个前沿教师模型（Gemini 3 Pro）进行结构化轨迹合成，便足以训练出在多个基准上超越部分前沿闭源模型、且能泛化到未见过环境的竞争性本地网页代理。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为四类。

第一类是**网络智能体评测基准与架构**，如WebArena、VisualWebArena、WorkArena、OSWorld和BrowserGym等。这些研究构建了从模拟到真实环境的多样化评测平台。本文的框架设计直接受到了这些基准构建过程中“任务设计、标注、监督”等角色的启发，并将其模块化地融入了合成轨迹生成流程。

第二类是**网络智能体的合成轨迹生成方法**，旨在解决人工标注成本高的问题。相关工作包括InSTA的大规模网络任务生成与过滤、NNetNav的探索轨迹后验标注、AgentTrek基于网页教程的回放，以及Go-Browse基于URL图搜索的方法。本文提出的“Agent-as-Annotators”框架在结构上与这些方法不同，它明确类比人类标注角色，设计了模块化的LLM组件（任务设计器、标注器、监督器）来结构化地生成高质量轨迹，并通过严格的“法官”过滤来保证数据质量。

第三类是**知识蒸馏与合成数据**的研究，例如Self-Instruct、LIMA以及利用特权信息进行蒸馏的工作。本文继承了利用强模型（教师）训练弱模型（学生）的核心思想，并将其扩展至需要多步环境交互的智能体场景。本文的蒸馏过程同样利用了教师模型在生成时拥有的探索数据和评估提示等“特权信息”，而这些信息在推理时并不提供给学生模型。

第四类是**基于LLM的评估与自我改进**，包括将LLM作为评估器的普遍做法，以及AgentRewardBench等针对智能体评估的元评测研究。本文的“法官”模块增强了传统的LLM-as-judge方法，通过提供评估提示来提高可靠性。此外，本文的监督微调（SFT）管道也与DigiRL、Agent Q等强化学习方法形成互补。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为“Agent-as-Annotators”的结构化框架来解决低成本、可本地部署的网页智能体能力泛化问题。其核心方法是模仿人类标注流程，将合成轨迹生成过程分解为三个模块化的LLM组件角色，以结构化方式蒸馏前沿大模型（教师模型）的网页导航能力到一个更小的学生模型上。

整体框架包含三个主要模块，分别对应传统标注中的角色：1) **任务设计器（Task Designer）**：负责根据给定的网页环境（如购物网站、企业平台）生成多样且复杂的任务指令，确保覆盖广泛的用户意图和交互场景。2) **标注器（Annotator）**：作为核心执行组件，它接收任务指令和当前网页状态（如HTML），模拟教师模型（文中使用Gemini 3 Pro）的推理过程，逐步生成包含思维链（reasoning traces）的动作轨迹（如点击、输入）。3) **评判器（Judge）**：充当质量监督者，对生成的轨迹进行过滤和评分，只保留高质量、正确的轨迹用于后续训练。这种结构化设计将开放的轨迹生成过程转化为可控、可迭代的流水线。

关键技术包括：**结构化轨迹合成**，通过角色分离确保生成数据的多样性和质量；**质量过滤机制**，由评判器模块严格筛选轨迹（从3000条中筛选出2322条），有效提升了训练数据的信噪比；**纯监督学习微调**，直接使用筛选后的高质量轨迹（包含动作序列和推理过程）对一个90亿参数的学生模型进行微调，避免了复杂的强化学习或模仿学习框架。

创新点主要体现在：1) **模块化类比设计**，将合成数据生成流程结构化，提升了可控性和可扩展性；2) **能力的有效蒸馏**，仅使用单一前沿教师模型，通过合成数据就能让小模型获得超越许多闭源大模型的网页导航性能；3) **强大的泛化能力**，模型在训练未见的网页环境（如WorkArena企业平台）上表现出显著的性能提升，证明了其学到的能力是可迁移的。消融实验进一步证实了评判器过滤、评估提示和推理轨迹等关键组件都对最终性能有重要贡献。

### Q4: 论文做了哪些实验？

论文实验主要包括数据合成、模型训练和跨基准评估。实验设置上，研究者使用Agent-as-Annotators框架，以Gemini 3 Pro作为教师模型，在WebArena的六个自托管网络环境（Reddit、GitLab、电商网站、管理后台、Wikipedia、OpenStreetMap）上生成了3,000条轨迹。通过Judge模块（同样基于Gemini 3 Pro）进行质量过滤后，获得2,322条成功轨迹（共16,353个训练样本），并以此对Qwen3.5-9B学生模型进行纯监督微调，训练2个周期。

评估在五个基准测试上进行：WebArena（381个任务，同领域）、VisualWebArena（449个任务，视觉基础）、WorkArena L1（330个任务，企业平台，训练中未见）、WorkArena++ L2（185个任务）和MiniWoB（125种任务类型）。对比方法包括闭源模型（如GPT-4o、Claude 3.5 Sonnet、Gemini系列）和开源基础模型（Qwen家族不同规模模型），以及之前的开源最佳结果Go-Browse。

主要结果显示，微调后的A3-Qwen3.5-9B在WebArena上达到41.5%的成功率，超过了GPT-4o（31.5%）和Claude 3.5 Sonnet（36.0%），并将之前开源最佳结果（Go-Browse的21.7%）提升近一倍。关键指标包括：在完全未见的WorkArena L1上获得18.2个百分点的提升（从33.3%到51.5%）；在VisualWebArena上达到33.9%；在WorkArena++ L2上为9.7%。消融实验证实，Judge过滤贡献4.5个百分点提升，保留推理轨迹贡献7.9个百分点，且数据规模收益随数量增加而递减。

### Q5: 有什么可以进一步探索的点？

本文的局限性与未来研究方向可从数据、模型、评估和框架扩展性四个方面展开。首先，数据层面，虽然六个环境已覆盖核心交互原语，但进一步探索可测试“深度”（任务多样性）与“广度”（网站数量）的结合是否带来互补增益；同时，需开发新策略以突破当前数据规模下的收益递减，例如通过迭代自改进生成新轨迹。其次，模型层面，当前仅使用监督微调，结合强化学习进行策略优化是自然的下一步，而“自我思考轨迹再生”（用学生模型生成推理轨迹）可能提升推理连贯性。第三，评估方面，需对Judge模块的误判率进行人工验证，并扩展教师模型测试（如Claude、GPT-4）以验证方法的通用性。最后，框架的模块化设计允许灵活集成更强组件，未来可探索更高效的人设模块设计、跨领域适应性调整（如移动端或动态Web应用）以及开源轨迹数据的社区化评估与改进。这些方向有望进一步提升轻量级Web智能体的泛化能力和实用部署潜力。

### Q6: 总结一下论文的主要内容

该论文提出了一个名为“Agent-as-Annotators”的框架，旨在通过结构化知识蒸馏，将前沿大语言模型（如Gemini 3 Pro）的网页导航能力迁移到小型、可本地部署的模型中。其核心问题是解决前沿模型成本高、依赖API而难以本地实用化的问题。

方法上，该框架模拟人类标注流程，将任务设计、轨迹生成与质量监督分解为模块化的LLM组件，以此结构化地合成高质量的训练轨迹。研究者利用教师模型生成了3000条轨迹，经过严格的质量筛选后，使用2322条轨迹，通过纯监督学习微调了一个90亿参数的学生模型。

主要结论是，数据质量远重于数量：经过精心筛选的少量高质量轨迹足以训练出极具竞争力的模型。该学生模型在WebArena基准测试上达到41.5%的成功率，超越了GPT-4o和Claude 3.5 Sonnet等闭源模型，并将此前最佳开源结果的性能提升近一倍。更重要的是，模型展现出强大的泛化能力，在训练中从未见过的企业平台（WorkArena）等新环境中也取得了显著提升。这证明了结构化轨迹合成能够有效蒸馏网页智能体能力，为实现高性能、可本地部署的通用网页代理提供了可行路径。
