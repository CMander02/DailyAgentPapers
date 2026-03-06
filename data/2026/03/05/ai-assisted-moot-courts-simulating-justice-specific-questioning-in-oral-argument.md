---
title: "AI-Assisted Moot Courts: Simulating Justice-Specific Questioning in Oral Arguments"
authors:
  - "Kylie Zhang"
  - "Nimra Nadeem"
  - "Lucia Zheng"
  - "Dominik Stammbach"
  - "Peter Henderson"
date: "2026-03-05"
arxiv_id: "2603.04718"
arxiv_url: "https://arxiv.org/abs/2603.04718"
pdf_url: "https://arxiv.org/pdf/2603.04718v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agentic Simulation"
  - "Agent Evaluation"
  - "Human-AI Interaction"
  - "Domain-Specific Agent"
  - "Prompt Engineering"
relevance_score: 7.5
---

# AI-Assisted Moot Courts: Simulating Justice-Specific Questioning in Oral Arguments

## 原始摘要

In oral arguments, judges probe attorneys with questions about the factual record, legal claims, and the strength of their arguments. To prepare for this questioning, both law schools and practicing attorneys rely on moot courts: practice simulations of appellate hearings. Leveraging a dataset of U.S. Supreme Court oral argument transcripts, we examine whether AI models can effectively simulate justice-specific questioning for moot court-style training. Evaluating oral argument simulation is challenging because there is no single correct question for any given turn. Instead, effective questioning should reflect a combination of desirable qualities, such as anticipating substantive legal issues, detecting logical weaknesses, and maintaining an appropriately adversarial tone. We introduce a two-layer evaluation framework that assesses both the realism and pedagogical usefulness of simulated questions using complementary proxy metrics. We construct and evaluate both prompt-based and agentic oral argument simulators. We find that simulated questions are often perceived as realistic by human annotators and achieve high recall of ground truth substantive legal issues. However, models still face substantial shortcomings, including low diversity in question types and sycophancy. Importantly, these shortcomings would remain undetected under naive evaluation approaches.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在探讨人工智能模型能否有效模拟美国最高法院口头辩论中法官的特定提问，以用于模拟法庭（moot court）式的律师培训。研究背景是，在司法实践中，口头辩论环节法官的提问对案件结果有重要影响，律师通常通过模拟法庭来准备，但高质量的模拟（如聘请前法官）成本高昂，而资源有限的律师往往只能采用简陋的自助方式（如抽卡片模拟）。现有基于AI的法律应用多集中于问答或文件分析，缺乏针对这种对抗性、对话式且具教学意义的模拟场景的研究。现有方法的不足主要体现在：一、模拟口头辩论需处理冗长复杂的法律文件并理解每位法官的偏好，技术难度高；二、评估生成问题质量非常困难，因为任何环节都可能存在多个合理问题，传统基于文本匹配或相似度的指标无法捕捉“好问题”的多维特质（如预见法律议题、检测逻辑漏洞、保持适当对抗性语气等）。本文要解决的核心问题是：如何构建并全面评估AI驱动的口头辩论模拟器，使其能生成既真实又具教学价值的法官式提问，从而帮助弥合律师资源差距，同时为前沿模型提供一个新颖的测试平台。为此，论文提出了一个双层评估框架，综合衡量问题的真实性（通过对抗性测试和人工判断）与教学有用性（如覆盖法律议题、问题类型多样性等），并构建了多种模拟器进行验证。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及法律自然语言处理、实证法律研究、法庭模拟以及人机协作系统四个领域。

在法律自然语言处理方面，已有大量研究评估和改进语言模型执行法律推理任务的能力，例如法律问答、判决预测、法规推理等。与这些专注于孤立、狭窄任务的研究不同，本文关注的是交互式、长上下文、开放式的口头辩论模拟，这促使作者提出了多层次的评估框架。

在实证法律研究方面，特别是对美国最高法院口头辩论的分析，已有学者研究了法官的提问风格、性别与资历效应等问题。这些研究为本文理解提问的“教学实用性”以及评估模拟问题的“真实性”提供了基础。

在法庭模拟方面，近期研究如AgentCourt和SimCourt尝试用智能体模拟完整的法庭程序，以预测最终判决或优化AI律师的知识。本文与之在范围和目标上均有区别，其核心是模拟法官提问，旨在帮助人类律师改进论点，而非模拟整个审判过程或追求AI代理的进化。

在人机协作系统方面，本文借鉴了将AI定位为“思维伙伴”以支持人类学习和技能发展的研究。同时，作者也关注到此类系统中存在的风险，例如模型可能出现的谄媚行为（即迎合用户已知观点而非进行批判性互动），这在需要挑战和批判的教学场景中尤为有害，因此本文专门测试了模拟器能否施加足够的对抗性压力。

### Q3: 论文如何解决这个问题？

论文通过构建一个包含任务设计、模拟器构建和双层评估框架的完整方法体系来解决AI模拟法庭口头辩论中法官特定提问的问题。

**核心方法与架构设计：**
研究构建了两类口头辩论模拟器：基于提示的模拟器和智能体模拟器。整体框架以美国最高法院口头辩论笔录为数据基础，每个任务样本包含案件事实、法律问题、多轮对话上下文以及即将发言的法官姓名。模拟器的目标是预测特定法官在给定上下文下的发言。

1.  **基于提示的模拟器**：使用多个开源和闭源大语言模型（如Llama-3.3-70B、GPT-4o等），并应用三种手动设计的提示策略：
    *   `SCOTUS_DEFAULT`：将模型置于最高法院场景并指示其扮演特定法官。
    *   `SCOTUS_PROFILE`：在默认提示基础上，加入手工编写的法官“档案”，描述其司法哲学和政治倾向。
    *   `MOOT_COURT`：将具有档案的法官角色设定为全国模拟法庭竞赛的评委，并明确指示其挑剔逻辑错误。

2.  **智能体模拟器**：使用更强的推理模型（如GPT-4o、Gemini-2.5-Pro）作为基础，赋予其访问工具的能力，并在每个生成步骤中允许其采取多种行动：
    *   `THINK`：进行内部推理和规划。
    *   `CLOSED_WORLD_SEARCH`：在案件卷宗文件上进行封闭搜索。
    *   `JUSTICE_PROFILE`：查询特定法官的历史投票模式和党派倾向。
    *   `PROVIDE_FINAL_RESPONSE`：输出最终的模拟法官回应。智能体最多可进行10步的探索和工具使用以生成回应。

**关键技术：双层评估框架**
由于不存在单一的“正确”问题，论文创新性地提出了一个双层评估框架，从“真实性”和“教学有用性”两个互补维度进行全面评估。

1.  **真实性层**：作为教学有效性的必要非充分条件，旨在过滤掉不符合基本法庭互动规范（如法庭礼仪、已知司法倾向）的模拟。包含两种方法：
    *   **对抗性测试**：构建半合成的对抗性基准测试，故意设置律师的回应违反法庭礼仪、引入与法官观点冲突的政治言论或突然转换立场为对方辩护，以测试模拟法官是否会如预期般指出或反驳这些不当行为，从而检测模型的“谄媚”倾向。
    *   **人工评估**：通过让标注者对模拟回应和真实回应进行两两偏好判断，计算胜率来评估感知真实性。

2.  **教学有用性层**：评估模拟器是否能在关键方面有效锻炼律师的思辨能力，为其真实辩论做准备。包含四个维度的评估：
    *   **法律问题覆盖率**：评估模拟问题是否涵盖了律师在真实辩论中预期会被法官提及的实质性法律议题。使用“狭义”和“广义”两种召回率指标进行衡量。
    *   **问题类型多样性**：使用三种不同的分类体系（Legalbench、Stetson、Metacog）对问题类型进行分类，并通过计算模拟问题与真实问题分布之间的Jensen-Shannon散度来评估多样性。
    *   **谬误检测能力**：构建一个涵盖十种逻辑谬误类型的半合成基准测试，评估模拟法官是否能如教学所期望的那样，识别并挑战律师论证中的这些缺陷。
    *   **提问语气**：通过`VALENCE`指标评估问题的对抗性或合作性程度。将问题分类为竞争性、中性或支持性，通过比较模拟与真实提问的语气分布，来检测模拟器是否过于合作（即存在谄媚行为）。

**创新点**：
1.  **任务与模拟器设计的针对性**：紧密结合最高法院辩论场景，设计了融合法官个性化档案和模拟法庭教学目标的提示策略，以及能够利用外部知识工具进行推理的智能体架构。
2.  **评估框架的系统性与创新性**：认识到单一指标的局限性，首创了“真实性”与“教学有用性”双层评估框架。该框架不仅包含传统的人工偏好评估，还创新性地引入了对抗性测试来暴露模型缺陷，并设计了一系列针对教学目标的代理指标（如覆盖率、多样性、谬误检测、语气分析），为评估复杂、开放的对话生成任务提供了可扩展的范例。
3.  **问题暴露的深度**：通过这一综合评估，论文不仅展示了AI模型在生成看似真实且能覆盖核心法律问题方面的潜力，更重要的是系统地揭示了其当前存在的显著短板，如问题类型多样性低、存在谄媚行为等，而这些在简单的评估方法下容易被忽视。

### Q4: 论文做了哪些实验？

论文实验旨在评估AI模型模拟最高法院口头辩论中法官提问的能力，重点关注模拟问题的真实性和教学实用性。实验设置包括构建基于提示（prompt-based）和智能体（agentic）两类口头辩论模拟器，使用了多种大语言模型，如Gemini-2.5-Pro、Llama-3.3-70B-Instruct、GPT-4o、GPT-OSS-120B和Qwen3-32B。

数据集基于美国最高法院口头辩论记录文本。评估采用一个双层框架：第一层评估真实性，包括对抗性测试（如DECORUM、Rage-Bait、Switching-Sides）和人工偏好评估；第二层评估教学有用性，包括法律问题覆盖率（Issue Coverage）、问题类型多样性（Question Type Diversity）和逻辑谬误检测（Fallacy Detection）。对比方法主要是在不同模型和模拟技术之间进行排名比较。

主要结果如下：在综合排名中，Gemini-2.5-Pro（PROMPT）总体表现最佳。具体指标上，在对抗性测试中，所有模拟器在应对挑衅性辩护行为时表现均不佳，最佳模型对DECORUM违规的检出率低于40%，对Rage-Bait和Switching-Sides的应对更差。人工评估中，Gemini-2.5-Pro（AGENT）的加权胜率最高（55.6%），部分模拟器的问题甚至比真实法官提问更受青睐。在法律问题覆盖率上，使用Issue-Broad指标时，8个模拟器中有5个能覆盖超过60%的真实议题；但使用要求更严格的Issue-Narrow指标时，最佳模型（GPT-OSS-120B）仅覆盖41%。问题类型多样性方面，所有模拟器生成的问题类型都显著少于真实法官，分布更集中。逻辑谬误检测能力因谬误类型而异，模型普遍难以检测Numbers和Sampling类谬误，但对Exclusivity等谬误检测率较高，最佳模型在十类谬误中的七类上检测率超过80%。此外，实验还发现模拟器存在过度合作（奉承）倾向、提问竞争性过强、以及某些模型会错误识别辩护方等问题。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从数据、评估和模型三个层面展开。首先，研究仅基于美国最高法院的庭审记录，其提问规范和互动模式与下级法院及模拟法庭存在差异，未来可扩展至不同司法管辖区和层级的法庭数据，以提升系统的泛化能力。其次，当前评估框架依赖代理指标和有限的人工标注，未能直接衡量模拟问题对律师实际辩论技能的提升效果，后续需开展长期实证研究，通过真实模拟法庭参与者的学习成果进行教学有效性验证。此外，评估流程中大量使用语言模型作为分类器，可能引入偏差，未来可结合更可靠的人工评估或多模型交叉验证以提高信度。从模型改进角度看，当前系统存在提问类型单一和谄媚性倾向等问题，可探索引入对抗性训练或多样性优化机制，增强问题的批判性和多维性。最后，可进一步探索AI模拟与人类教练的协同模式，例如通过动态难度调整或个性化反馈，构建更具适应性的法律训练生态系统。

### Q6: 总结一下论文的主要内容

该论文探讨了如何利用人工智能模拟最高法院口头辩论中法官的提问，以改进法律实践训练中的模拟法庭（moot court）。核心问题是评估AI模型能否生成既真实又具有教学价值的法官式提问，以帮助律师和学生更好地准备实际庭审。

论文提出了一种双层评估框架，从真实性和教学实用性两个维度评估模拟问题。方法上构建了基于提示的模拟器和智能体模拟器，利用美国最高法院口头辩论转录数据集进行训练和测试。主要结论显示，AI生成的问题在人类评估者看来通常较为真实，并能有效涵盖实质法律议题，但也存在明显缺陷，如问题类型多样性不足和过度迎合（奉承）倾向。这些缺点在简单的评估方法下容易被忽略，凸显了该论文所提评估框架的必要性。

这项工作的意义在于为法律教育提供了新的AI辅助训练工具，并强调了在开放域生成任务中采用多维、针对性评估的重要性，以避免模型缺陷被掩盖。
