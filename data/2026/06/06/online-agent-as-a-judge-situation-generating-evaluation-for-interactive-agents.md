---
title: "Online Agent-as-a-Judge: Situation-Generating Evaluation for Interactive Agents"
authors:
  - "Hyogon Ryu"
  - "Jeonghwan Kim"
  - "Yewon Lim"
  - "Chaeun Lee"
  - "Jeongwook Kim"
  - "Donghoon Ham"
date: "2026-06-06"
arxiv_id: "2606.08200"
arxiv_url: "https://arxiv.org/abs/2606.08200"
pdf_url: "https://arxiv.org/pdf/2606.08200v1"
categories:
  - "cs.AI"
  - "cs.LG"
tags:
  - "Agent评估"
  - "多智能体交互"
  - "社会智能体"
  - "交互评估框架"
  - "LLM智能体"
  - "自动评估"
  - "情境生成"
relevance_score: 9.0
---

# Online Agent-as-a-Judge: Situation-Generating Evaluation for Interactive Agents

## 原始摘要

Evaluating LLM-powered interactive social agents is challenging because socially relevant behaviors depend not only on isolated outputs, but also on prior interactions, social roles, and downstream actions. Existing methods typically allow a target agent to act freely in an environment and then score the resulting trajectory. However, this passive setup can miss capabilities that only become observable under specific social circumstances; for example, conflict handling may remain untested if no disagreement arises. We propose Online Agent-as-a-Judge, a situation-generating evaluation framework for interactive social agents. Online Agent-as-a-Judge deploys an in-world evaluator agent that interacts with the target agent through the environment's native dialogue and action protocol, actively eliciting situations relevant to the evaluation criteria. The resulting trajectories provide evidence for assessing both immediate responses and subsequent behavior. In a life-simulation environment with $32$ designer-authored social criteria, Online Agent-as-a-Judge improves criteria coverage and agreement with human labels, yielding more reliable evidence-grounded evaluations of behaviors that passive methods can leave unobserved.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

本文试图解决LLM驱动的交互式社会智能体评估中的一个核心瓶颈：相关行为证据的可获得性问题。现有评估方法，如LLM-as-a-judge或离线Agent-as-a-judge，要么仅评估静态输出，要么只能检索已有的交互轨迹。然而，在持续性的社会环境中，许多关键能力（如冲突处理、情感支持）只有在特定的社会情境（如分歧、尴尬请求）下才能被触发。传统的被动评估范式无法主动创造这些情境，导致许多目标能力从未被测试到，评估证据链不完整。为此，论文提出Online Agent-as-a-Judge（在线智能体即法官）框架，核心创新在于引入一个在线的、具有社会角色的评估者智能体，它在评估过程中通过与目标智能体在同一环境中进行原生对话和行动交互，主动“生成”评估所需的社会情境，从而获取更可靠的、基于证据的评估结果。该方法旨在弥补现有被动范式的不足，提升评估的准则覆盖率和对人类标签的一致性。

### Q2: 有哪些相关研究？

相关工作可以从几个类别来理解。首先，**评估方法类**包括LLM-as-a-judge和Agent-as-a-judge。前者依赖另一个LLM对静态输出评分，无法主动触发特定行为；后者虽能检查环境状态，但仍是后验观察，无法主动构造所需的社会情境。本文提出的Online Agent-as-a-Judge则不同，它通过在线交互主动生成评估所需的社会情境，克服了被动方法的局限性。其次，**基准与测试类**包括ORAK、MineDojo、WebArena等游戏与工具代理基准，它们通常以任务完成率或奖励为指标，而本文聚焦于社会互动行为，这些行为往往没有单一任务目标，需要社会参与者诱导。再次，**生成式代理与社会模拟类**如Generative Agents和Social Simulacra，侧重可信度建模，但本文关注的是代理是否满足设计师定义的具体行为标准。最后，**过程感知与社会评估类**中，Concordia通过外部裁判生成情境，但本文的评估器直接与目标代理在线互动，针对的是游戏设计师为特定NPC编写的角色级行为标准，而非观察涌现现象本身。此外，M3-Bench、AgentRewardBench等也关注过程而非最终状态，但本文通过在线互动显著改变了哪些过程能被观测到。

### Q3: 论文如何解决这个问题？

论文提出了Online Agent-as-a-Judge框架，一种主动式情境生成评估方法。核心思想是让一个评估者智能体（Judge）以原生交互协议进入仿真世界，与目标智能体进行多轮对话和行动互动，主动诱发能够检验特定评估标准的社会情境，从而解决被动评估中关键行为因情境缺失而无法被观察的问题。

整体框架包含五个主要模块：Inspect模块通过只读工具获取当前世界状态、目标角色、附近人物和对话历史等评估上下文；Plan模块基于当前证据集和上下文，生成具体的探测计划，设计如何诱发目标情境；Elicit模块执行该计划，让Judge在与目标智能体的交互中主动构造关键情境；Observe模块记录目标智能体的即时回复和后续行为；Decide模块基于收集到的证据给出pass/fail/insufficient判定，若证据不足则返回Inspect进入新一轮迭代。

关键技术包括：采用闭环迭代机制，Judge可针对同一标准多次调整探测策略，直到获得充分证据；通过仿真协议的对话和行动接口进行交互，保证评估框架对世界更新的鲁棒性；Judge与目标共处同一世界，能观察行为后果而不仅是单轮回复。主要创新点在于从被动记录转向主动诱发，使评估者能够针对任何设计者指定的社会行为标准（如维持家庭角色、完成家务请求）生成相关情境，显著提高了标准覆盖率和与人类标签的一致性。

### Q4: 论文做了哪些实验？

论文在生命模拟沙盒环境中进行了实验，该环境包含一个五口之家（父母、孩子、兄弟姐妹、祖父母）。评估了三种目标智能体后端：随机规则选择、单次LLM提示和具有记忆与规划能力的观察-思考-行动循环，每种运行三次。使用32个人工策划的标准，涵盖对话/关系、家庭角色/人格、记忆/连续性等8个领域。对比方法包括离线LLM-as-a-Judge（读取预记录轨迹并评分）、离线Agent-as-a-Judge（可检索数据库但不能创建新情境）和提出的Online Agent-as-a-Judge（在线法官与目标交互生成相关情境）。关键指标：标准覆盖率（Online方法达0.92，远高于离线的0.56和0.54）和人类一致性（Online方法达0.70，显著优于离线的0.40和0.33）。在冲突/违规和情感/社会支持等罕见情境领域，覆盖率差距最大（冲突：1.00 vs 0.19/0.22；情感：0.89 vs 0.44/0.58）。一致性方面，Online方法在冲突领域达0.96，情感领域达0.82。鲁棒性分析显示，Online方法正确识别93/114个通过（82%）和87/144个失败（60%），而离线方法几乎无法识别失败。时间成本上，Online方法评估32个标准仅需约21分钟，远少于人工的60分钟。

### Q5: 有什么可以进一步探索的点？

论文提出的Online Agent-as-a-Judge框架尽管在主动诱发评估场景上具有创新性，但仍存在若干局限与未来探索空间。首先，主动探测可能无意中为智能体提供答案线索，例如评估者提问时暗示了预期行为或补充了缺失上下文，导致评估失真。未来可改进探测门控机制，通过更严格的语义过滤或对抗性验证来避免引导性偏差。其次，评估者判断继承了大语言模型的内在偏见，当前仅通过分段评分和共享评判策略块来缓解，但未能根本消除。可探索引入多模型投票或偏见过滤层，或使用更细粒度的行为分解来提升客观性。此外，该方法仅适用于需要诱发而非自发出现的行为，对于有明确量化终点的任务仍显多余。未来可尝试将主动评估与被动日志结合，形成混合框架：先用被动数据覆盖常规行为，再针对盲区进行主动诱发，从而提高整体覆盖率和评估效率。该方法在生命模拟、长期对话助手和角色扮演场景中具有广阔应用前景，但需进一步优化其通用性与鲁棒性。

### Q6: 总结一下论文的主要内容

这篇论文提出了一种名为“在线智能体即评委”（Online Agent-as-a-Judge）的互动社交智能体评估框架。现有被动评估方法无法测试特定社会情境下（如冲突处理）的能力，导致关键行为未被观察。该框架将一个评估智能体部署在目标智能体的环境中，利用环境的对话和行动协议主动生成与评估标准相关的情境，从而获取包含及时反应和后续行为的轨迹证据。在包含32个设计师编写的社会标准的生活模拟实验中，该方法实现了显著更高的标准覆盖率（0.92对比基线方法的0.56和0.54）以及与人类标签的一致性（0.70对比0.33和0.40），尤其在相关情境罕见出现的领域提升最大。结论表明，情境生成是评估社会情境化智能体的实用路径，并突出了主动式、环境内评估作为研究和验证互动社交智能体的方法论工具的重要性。
