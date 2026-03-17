---
title: "$τ$-Voice: Benchmarking Full-Duplex Voice Agents on Real-World Domains"
authors:
  - "Soham Ray"
  - "Keshav Dhandhania"
  - "Victor Barres"
  - "Karthik Narasimhan"
date: "2026-03-14"
arxiv_id: "2603.13686"
arxiv_url: "https://arxiv.org/abs/2603.13686"
pdf_url: "https://arxiv.org/pdf/2603.13686v1"
categories:
  - "cs.SD"
  - "cs.AI"
tags:
  - "Agent Benchmark"
  - "Voice Agent"
  - "Full-Duplex Interaction"
  - "User Simulation"
  - "Task-Oriented Dialogue"
  - "Evaluation Framework"
relevance_score: 7.5
---

# $τ$-Voice: Benchmarking Full-Duplex Voice Agents on Real-World Domains

## 原始摘要

Full-duplex voice agents--systems that listen and speak simultaneously--are rapidly moving from research to production. However, existing evaluations address conversational dynamics and task completion in isolation. We introduce $τ$-voice, a benchmark for evaluating voice agents on grounded tasks with real-world complexity: agents must navigate complex multi-turn conversations, adhere to domain policies, and interact with the environment. The framework extends $τ^2$-bench into a novel voice agent benchmark combining verifiable completion of complex grounded tasks, full-duplex interaction, and realistic audio--enabling direct comparison between voice and text performance. A controllable and realistic voice user simulator provides diverse accents, realistic audio environments, and rich turn-taking dynamics; by decoupling simulation from wall-clock time, the user simulator can use the most capable LLM without real-time constraints. We evaluate task completion (pass@1) and voice interaction quality across 278 tasks: while GPT-5 (reasoning) achieves 85%, voice agents reach only 31--51% under clean conditions and 26--38% under realistic conditions with noise and diverse accents--retaining only 30--45% of text capability; qualitative analysis confirms 79--90% of failures stem from agent behavior, suggesting that observed failures primarily reflect agent behavior under our evaluation setup. $τ$-voice provides a reproducible testbed for measuring progress toward voice agents that are natural, conversational, and reliable.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决全双工语音智能体在现实复杂任务中缺乏综合性评估基准的问题。研究背景是，随着音频原生语言模型的发展，能够同时听说的全双工语音交互系统正从研究走向实际应用（如客户服务）。然而，现有评估方法存在明显不足：它们往往孤立地评估对话动态（如轮流发言、打断处理）或任务完成能力（如使用工具、修改数据库），且多在文本、回合制或合成任务中进行，未能涵盖语音交互在现实场景中面临的综合挑战。例如，语音缺乏标点、包含不流利表达、受背景噪音和口音影响，且实时对话动态要求智能体在连续时间内流畅响应，这些因素共同增加了任务难度，而现有基准无法捕捉这种多维度交织的失败（如因噪音听错信息导致后续工具调用错误）。

本文的核心问题是：如何系统评估全双工语音智能体在**接地气的复杂任务**中的综合性能，即同时衡量其在真实音频环境下的任务完成能力和对话管理能力。为此，论文提出了τ-Voice基准，首次将可验证的复杂任务完成、全双工交互和真实音频模拟三者结合，并支持语音与文本智能体的直接性能对比，以推动构建更自然、可靠且具有对话能力的语音智能体。

### Q2: 有哪些相关研究？

本文的相关研究可分为三大类：任务完成评测、全双工会话动态评测以及真实音频环境评测。  

在**任务完成评测**方面，τ-bench 和 τ²-bench 专注于基于文本的客服任务，通过可验证的数据库状态变化评估智能体完成任务的能力，但缺乏语音交互和实时性考量。  

在**全双工会话动态**方面，Full-Duplex-Bench 及其 V2 版本提出了自动评估指标，涵盖停顿处理、反馈信号、话轮转换和打断管理，但任务多为脚本化场景，未与真实工具调用和数据库操作结合。Talking Turns 则基于人类标注数据评估话轮转换，发现现有模型存在不当打断和缺乏反馈的问题。  

在**真实音频环境评测**方面，VoiceBench、VocalBench 和 Audio MultiChallenge 分别评估了自动语音识别（ASR）在多样化口音、噪声环境下的鲁棒性，以及语音对话的流畅度、记忆一致性等，但通常仅针对语音理解本身，未与复杂任务完成结合。  

本文提出的 τ-voice 首次将上述三个维度整合：既包含可验证的复杂任务完成，又支持全双工实时交互，同时引入包含多样口音、背景噪声的真实音频模拟环境。与现有工作相比，τ-voice 通过基于“时钟滴答”的协调机制，实现了更灵活的话轮行为配置，并在仿真中解耦了实时约束，从而能利用最强的大语言模型进行高效评估。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为τ-Voice的基准测试框架来解决全双工语音代理在真实世界复杂任务中的评估问题。其核心方法是对现有的τ²-bench文本基准进行扩展，引入了三个关键组件：一个支持全双工交互的可控协调器、一个高度逼真的语音用户模拟器，以及一套同时衡量任务完成度和交互质量的评估指标。

整体框架由协调器、用户模拟器和语音代理API适配器构成。协调器是核心控制模块，它管理着模拟器与语音代理之间的交互循环，负责音频交换、话轮转换事件和评估日志记录。其关键创新在于采用了**离散模拟时间**的设计，将连续的音频流离散化为固定时长（默认为200毫秒）的“滴答”。每个滴答内，双方交换固定时长的音频，实现了真正的全双工交互（允许同时说话）。更重要的是，该框架**将模拟时间与真实时钟时间解耦**。语音API（如OpenAI Realtime）基于音频时间戳而非实时处理音频，这使得协调器可以独立地推进模拟时间，从而允许用户模拟器使用最强大的LLM（无需考虑实时生成延迟）来生成高度可靠的指令和话轮决策，确保了评估的可复现性和对交互时序的精细控制。

用户模拟器是另一个核心模块，它通过一个多阶段流水线生成高度逼真的呼叫者音频。首先，**语音生成**模块利用LLM生成包含不流利词、口语化表达的自然口语文本，再通过配置了不同口音、风格和韵律的TTS语音角色进行合成。其次，**音频环境模拟**模块将合成语音与背景噪音（如交谈声、交通声）、突发噪音（如电话铃声）以及非话轮内语音（如“稍等”、咳嗽声）混合，并施加电话压缩、帧丢失等信号退化效果，以模拟真实通话条件。最后，**话轮转换策略**模块结合了可配置的基于阈值的规则（如静默等待时间）和LLM驱动的智能决策（如判断是否打断、是否给予反馈性应答），从而模拟丰富、动态的对话行为。

在评估方面，框架不仅继承了τ²-bench对**任务成功率**（pass@1）的验证（通过比对最终数据库状态与目标，并使用LLM评估代理沟通内容），还创新性地定义了**语音交互质量**的四维度指标：响应性、延迟、打断率和选择性。此外，通过详细的日志和可视化时间线，框架能够精确捕捉和量化交互中的复杂现象（如打断、非指向性语音、反馈性应答的处理等），从而系统性地分析失败原因。这种将可控、可复现的模拟环境与多维评估指标相结合的方法，为全面、深入地评测语音代理在复杂、真实场景下的能力提供了系统化的解决方案。

### Q4: 论文做了哪些实验？

论文在三个真实领域（零售、航空、电信）共278个任务上进行了实验，主要评估全双工语音代理的任务完成度和语音交互质量。

**实验设置与数据集**：实验基于τ²-bench扩展的τ-voice基准，包含零售（114任务）、航空（50任务）和电信（114任务）三个领域，其中零售领域因对槽填充要求高被设为主要评估域。评估了三个2025年末至2026年初发布的音频原生模型：OpenAI的gpt-realtime-1.5、Google的gemini-live-2.5-flash-native-audio和xAI的grok-voice-agent。实验设计了两种语音复杂度条件：Clean（清晰美式口音、无噪音或打断）和Realistic（多样口音、环境噪音、信道退化、自然轮流对话行为）。此外，还通过消融实验单独测试了噪音、口音和轮流对话各自的影响。

**对比方法与主要结果**：主要对比了语音代理与文本基线（GPT-5和GPT-4.1）的性能。关键指标为任务完成度（pass@1）和语音交互质量（包括响应性、延迟、打断率和选择性）。

**主要结果**：
1.  **任务完成度**：在Clean条件下，最佳语音代理（xAI）的pass@1为51%，较GPT-5的85%下降34个百分点；在Realistic条件下进一步降至38%，仅保留文本SOTA能力的30-45%。各领域表现差异显著，例如在零售领域，OpenAI在Clean条件下达到71%，但在Realistic条件下降至45%。
2.  **消融分析**：平均而言，口音对性能影响最大（导致平均下降10pp），其次是轮流对话（7pp）和噪音（4pp）。但影响因提供商而异，例如口音对xAI影响巨大（-18pp），而对Google几乎无影响。
3.  **语音交互质量**：在Realistic条件下，OpenAI在延迟（0.90秒）、响应性（100%）和打断率（14%）上表现最佳，但选择性最差（6%）；xAI选择性最好（57%），但打断率最高（84%；Google打断率最低（21%），但响应性最低（69%）。这表明当前系统在实时对话中存在可靠响应与适当克制之间的权衡。
4.  **错误分析**：定性分析显示，79-90%的失败源于代理行为而非模拟器伪影。常见错误包括逻辑错误、转录错误（尤其在身份验证时）、幻觉以及多步骤请求跟踪失败。

### Q5: 有什么可以进一步探索的点？

本文的局限性及未来研究方向可从多个维度展开。首先，评估范围有限，仅关注任务完成度和对话动态，未涉及语音生成质量（如语调自然度）、用户满意度或部分任务成功情况，未来可引入更全面的评价指标。其次，模拟器虽具可控性，但假设了用户完美记忆与无限耐心，且绕过ASR直接注入文本，未来需整合真实ASR模块并开展人类用户研究以验证模拟真实性。此外，当前仅支持英语且依赖TTS，后续可扩展至多语言及真实录音，以更准确评估口音与噪声的影响。从技术改进看，可探索级联ASR→LLM→TTS基线，以区分语音模态与架构选择带来的性能差距。最后，论文揭示的语音-文本性能差距（仅保留30–45%能力）及特定口音脆弱性，指向了亟待加强的公平性评估——需确保语音代理在不同口音、说话风格和声学环境中均能可靠服务，这亦是推动技术普惠的重要方向。

### Q6: 总结一下论文的主要内容

该论文提出了τ-Voice基准测试框架，旨在全面评估全双工语音代理在真实世界复杂任务中的表现。核心问题是现有评估方法仅孤立考察对话动态或任务完成能力，而语音代理需同时处理多轮对话、遵守领域策略并与环境交互，现有基准无法衡量这些综合能力。

τ-Voice通过三个主要贡献解决这一问题：首先，将τ²-bench扩展为首个结合复杂任务验证、全双工交互和真实音频的语音代理基准，支持语音与文本性能的直接对比；其次，设计了可控的真实语音用户模拟器，提供多样口音、真实音频环境和丰富对话轮转动态，并通过模拟时间与实时解耦确保使用最强LLM而无延迟约束；最后，通过278项任务的实证评估发现，即使在理想条件下语音代理任务完成率（31-51%）也大幅落后于文本模型GPT-5（85%），在包含噪音和口音的真实条件下进一步降至26-38%，仅保留文本能力的30-45%。定性分析表明79-90%的失败源于代理行为缺陷，揭示了语音代理在实时推理与流畅对话协同方面的核心挑战。该研究为构建自然、可靠的全双工语音代理提供了可复现的评估基础。
