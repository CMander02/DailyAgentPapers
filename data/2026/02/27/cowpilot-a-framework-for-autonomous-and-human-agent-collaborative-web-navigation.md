---
title: "CowPilot: A Framework for Autonomous and Human-Agent Collaborative Web Navigation"
authors:
  - "Faria Huq"
  - "Zora Zhiruo Wang"
  - "Frank F. Xu"
  - "Tianyue Ou"
  - "Shuyan Zhou"
date: "2025-01-28"
arxiv_id: "2501.16609"
arxiv_url: "https://arxiv.org/abs/2501.16609"
pdf_url: "https://arxiv.org/pdf/2501.16609v4"
categories:
  - "cs.AI"
  - "cs.CL"
  - "cs.HC"
tags:
  - "Human-Agent Interaction"
  - "Web & Browser Automation"
relevance_score: 7.5
taxonomy:
  capability:
    - "Human-Agent Interaction"
    - "Web & Browser Automation"
  domain: "General Purpose"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "CowPilot framework for human-agent collaborative web navigation"
  primary_benchmark: "N/A"
---

# CowPilot: A Framework for Autonomous and Human-Agent Collaborative Web Navigation

## 原始摘要

While much work on web agents emphasizes the promise of autonomously performing tasks on behalf of users, in reality, agents often fall short on complex tasks in real-world contexts and modeling user preference. This presents an opportunity for humans to collaborate with the agent and leverage the agent's capabilities effectively. We propose CowPilot, a framework supporting autonomous as well as human-agent collaborative web navigation, and evaluation across task success and task efficiency. CowPilot reduces the number of steps humans need to perform by allowing agents to propose next steps, while users are able to pause, reject, or take alternative actions. During execution, users can interleave their actions with the agent by overriding suggestions or resuming agent control when needed. We conducted case studies on five common websites and found that the human-agent collaborative mode achieves the highest success rate of 95% while requiring humans to perform only 15.2% of the total steps. Even with human interventions during task execution, the agent successfully drives up to half of task success on its own. CowPilot can serve as a useful tool for data collection and agent evaluation across websites, which we believe will enable research in how users and agents can work together. Video demonstrations are available at https://oaishi.github.io/cowpilot.html

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前基于大语言模型（LLM）的网页导航智能体（agent）在复杂现实任务中表现不足，以及现有评估方法难以有效衡量人机协作效果的问题。研究背景是，尽管LLM在自动化数字任务方面展现出强大潜力，但智能体在实际复杂的网页导航任务中，常因无法准确理解用户偏好或处理动态环境而失败。现有方法主要侧重于评估智能体的自主任务成功率或效率，要么只支持用户通过自然语言反馈与智能体单向通信，要么仅记录人类用户单独的操作，缺乏对“动态人机协作”的支持——即在一个任务会话中，人类和智能体能够交替执行动作、共同解决问题的框架。

因此，本文的核心问题是：如何设计一个支持自主与协作两种模式的框架，以实现并系统评估人机协作的网页导航？具体而言，论文试图解决三个子问题：1）如何改进人机协作在网页导航任务中的评估方法；2）哪些因素促成了协作的成功或失败；3）用户的干预如何影响系统的整体效能。为此，作者提出了CowPilot框架，它允许智能体建议下一步动作，同时用户可暂停、拒绝建议或采取替代行动，并能随时恢复智能体控制，从而实现动态的人机交替协作。该框架不仅旨在提升复杂任务的成功率与效率，也作为一个工具，为未来研究人机如何有效协同工作提供了数据收集和系统评估的基础。

### Q2: 有哪些相关研究？

相关研究主要分为三类：工具与框架、基于LLM的智能体与评测基准、以及人机协作方法。

在工具与框架方面，现有工作主要提供网页自动化的开源工具包，形式包括API、模拟环境和Chrome扩展。例如，MultiOn和Anthropic提供API但设置复杂；BrowserGym、AgentLab、WebArena使用独立的浏览器实例，限制了多标签页导航和实际工作流。而Chrome扩展（如WebCanvas、WebOlympus、OpenWebAgent、Taxy）更轻量易用，能集成到标准浏览环境。本文提出的CowPilot也采用扩展形式，但关键区别在于**强化了人机协作功能**，支持建议-执行、暂停、覆盖等实时交互，而现有工具缺乏此类协作设计。

在基于LLM的智能体与评测基准方面，早期系统依赖HTML结构，后续视觉增强系统（如SeeACT、VisualWebArena、WebGUM）融入了空间与视觉理解。评测基准如MiniWoB、WebShop、WebLINX等专注于复杂多步骤任务。然而，这些研究**主要追求完全自主执行**，对人机协同循环的支持有限。CowPilot则填补了这一空白，强调动态人机协作，并支持在任务执行中进行交互式评估。

总体而言，CowPilot与相关工作的核心关系是继承并拓展了轻量级扩展的易用性，同时通过引入灵活的人机协同机制，在自主性与实用性之间取得了新的平衡。

### Q3: 论文如何解决这个问题？

论文通过提出CowPilot框架来解决自主智能体在复杂网页任务中表现不足的问题，其核心是支持自主与人类-智能体协作的混合导航模式。整体框架基于一个共享环境状态，其中LLM智能体（πℒ）和人类智能体（πΩ）交替或协同生成动作序列以完成自然语言描述的目标。

框架的主要模块包括：1）**建议-执行与人类监督机制**：LLM智能体在每个步骤生成建议动作（如点击、输入），并高亮显示目标元素和推理文本；用户有短暂时间（如5秒）审查，可选择批准（自动执行）、拒绝或暂停。2）**暂停与人类动作提取模块**：当用户暂停智能体时，系统通过HTML事件监听器捕获用户在网页上的原始交互（如点击、输入），并利用一个现成的LLM（如GPT-4o）将这些原始动作清洗并映射到智能体的标准化动作空间（如`type(elem, text)`），同时添加文本描述以便智能体理解上下文。3）**恢复与动作预测模块**：用户可随时恢复智能体控制；此时智能体基于完整的动作历史（包括自身和人类执行的动作）生成后续动作，从而避免重复错误并延续修正后的路径。

关键技术包括：**动态控制权转移**，允许用户在任务执行中无限次介入和交还控制；**动作空间对齐**，通过LLM将人类原始动作实时转化为智能体可解释的格式；以及**上下文感知的历史集成**，确保智能体在恢复后能基于人类修正进行决策。创新点在于平衡了自主性与人类监督：既通过智能体建议减少了用户操作负担（案例中人类仅需执行15.2%的步骤），又通过用户干预机制纠正智能体错误，最终实现95%的高任务成功率。此外，框架设计了协作质量评估指标（如人类干预次数、智能体驱动完成率），以量化人机协作效率。

### Q4: 论文做了哪些实验？

论文在WebArena基准测试的子集上进行了实验，该子集包含27个任务，按难度分为简单、中等和困难三个级别。实验设置包括两种模式：完全自主模式和Copilot（人机协作）模式，并使用了GPT-4o-2024-08-06和Llama-3.1-8B-Instruct作为LLM智能体的骨干模型。三名作者作为人类代理独立执行任务，结果取平均值。此外，还设置了仅由人类执行任务的无智能体参与基线作为对比。

主要结果如下：在Copilot模式下，使用GPT-4o的智能体实现了95%的任务准确率，显著高于自主模式的48%（相对提升97.9%），甚至超过了人类单独执行的准确率（相对提升6.7%）。然而，使用较小的Llama 8B模型的Copilot模式并未带来类似的准确率提升，反而使任务准确率略微下降了8%。在任务效率方面，基于GPT-4o的智能体在Copilot模式下平均仅需人类执行1.1步操作，占整个轨迹的15.2%，而智能体执行了84.8%的步骤。相比之下，使用Llama模型时，人类需执行4.77步，智能体执行4.15步，人类参与度翻倍。关键数据指标包括：Copilot模式（GPT-4o）任务准确率95%，人类步骤占比15.2%；自主模式任务准确率48%；智能体驱动完成的任务成功率占比最高达52%。这些结果表明，与强大的基于LLM的智能体协作能有效提升任务成功率和效率。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在需要人类持续观察任务执行，这限制了其规模化应用。未来研究可探索基于关键步骤检测的智能干预机制，仅在人机协作的关键决策点请求人类输入，从而降低人力成本。此外，论文提到可能存在的顺序偏差和用户行为差异，未来可通过更大规模、多样化的用户研究来验证泛化性。

结合个人见解，可能的改进方向包括：1）引入多智能体模拟框架，用第二个LLM代理模拟用户决策，实现自动化评估与主动学习；2）开发自适应协作策略，根据任务复杂度动态调整人机控制权分配；3）扩展至跨平台、跨场景的通用协作框架，并探索非视觉交互模式（如语音指令）以提升易用性。这些方向有望推动人机协作从“监督式”向“半自主协同”演进。

### Q6: 总结一下论文的主要内容

该论文提出了CowPilot框架，旨在解决现有网页代理在复杂任务和用户偏好建模方面的不足，通过支持自主与人类-代理协作的网页导航来提升任务执行效果。核心贡献在于设计了一个允许人类与代理动态交互的协作系统：代理可建议下一步操作，而用户可暂停、拒绝或采取替代行动，在执行中还能覆盖建议或恢复代理控制，从而平衡自动化与人工干预。

方法上，CowPilot框架整合了代理自主导航与用户协作机制，通过案例研究在五个常见网站评估任务成功率和效率。主要结论显示，人机协作模式达到95%的最高成功率，且人类仅需执行总步骤的15.2%；即使存在人工干预，代理仍能独立贡献约一半的任务成功。该框架可作为跨网站数据收集和代理评估的工具，推动用户与代理协同工作的研究发展。
