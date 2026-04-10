---
title: "ClawBench: Can AI Agents Complete Everyday Online Tasks?"
authors:
  - "Yuxuan Zhang"
  - "Yubo Wang"
  - "Yipeng Zhu"
  - "Penghui Du"
  - "Junwen Miao"
  - "Xuan Lu"
  - "Wendong Xu"
  - "Yunzhuo Hao"
  - "Songcheng Cai"
  - "Xiaochen Wang"
  - "Huaisong Zhang"
  - "Xian Wu"
  - "Yi Lu"
  - "Minyi Lei"
  - "Kai Zou"
  - "Huifeng Yin"
  - "Ping Nie"
  - "Liang Chen"
  - "Dongfu Jiang"
  - "Wenhu Chen"
date: "2026-04-09"
arxiv_id: "2604.08523"
arxiv_url: "https://arxiv.org/abs/2604.08523"
pdf_url: "https://arxiv.org/pdf/2604.08523v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "Agent评测基准"
  - "Web智能体"
  - "真实世界交互"
  - "多步任务"
  - "表单填写"
  - "动态环境"
  - "工具使用"
relevance_score: 9.0
---

# ClawBench: Can AI Agents Complete Everyday Online Tasks?

## 原始摘要

AI agents may be able to automate your inbox, but can they automate other routine aspects of your life? Everyday online tasks offer a realistic yet unsolved testbed for evaluating the next generation of AI agents. To this end, we introduce ClawBench, an evaluation framework of 153 simple tasks that people need to accomplish regularly in their lives and work, spanning 144 live platforms across 15 categories, from completing purchases and booking appointments to submitting job applications. These tasks require demanding capabilities beyond existing benchmarks, such as obtaining relevant information from user-provided documents, navigating multi-step workflows across diverse platforms, and write-heavy operations like filling in many detailed forms correctly. Unlike existing benchmarks that evaluate agents in offline sandboxes with static pages, ClawBench operates on production websites, preserving the full complexity, dynamic nature, and challenges of real-world web interaction. A lightweight interception layer captures and blocks only the final submission request, ensuring safe evaluation without real-world side effects. Our evaluations of 7 frontier models show that both proprietary and open-source models can complete only a small portion of these tasks. For example, Claude Sonnet 4.6 achieves only 33.3%. Progress on ClawBench brings us closer to AI agents that can function as reliable general-purpose assistants.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前AI智能体在真实网络环境中执行日常在线任务的能力评估不足的问题。研究背景是，尽管基于大语言模型的AI智能体（如OpenAI Operator、Anthropic Computer Use等）已能导航图形界面、填写表单和执行多步工作流，但它们能否作为真正的通用在线助手仍未知。现有评估方法存在明显局限：主流基准测试（如WebArena、OSWorld）多在离线沙盒中使用静态HTML页面进行评估，缺乏真实网站的动态性、身份验证流程和反爬虫机制；而少数在真实网站上运行的基准（如WebVoyager）又仅限于只读信息检索或使用模拟API测试简单写入操作，未能覆盖需要大量写入操作（如填写复杂表格）的任务。因此，现有方法无法有效评估智能体在真实生产网站上完成具有实际后果的日常任务（如购物、预约、求职申请）的能力。本文的核心问题是：如何构建一个既安全又生态有效的评估框架，以衡量AI智能体在真实、动态且复杂的生产网站上完成日常在线任务的实际性能，特别是那些涉及多步骤、重写入、需处理用户文档信息的关键任务。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为四类：网络智能体评测基准、基于大语言模型的网络智能体、智能体系统的评估方法，以及近期并发或互补的研究。

在网络智能体评测基准方面，早期工作如MiniWoB使用简化的合成界面和短动作序列。后续研究如WebArena、VisualWebArena和Mind2Web引入了更真实的自托管环境或大规模真实网站任务，但通常侧重于动作序列匹配或特定领域。OSWorld将范围扩展到操作系统任务。REAL Bench虽在真实网站上评估，但依赖人工评分。**ClawBench**与所有这些工作的核心区别在于：它在**144个真实在线平台**（而非自托管沙箱）上运行，专注于**写入密集型、改变状态的任务**，并通过一个智能体化评估器提供可追溯的、基于人类参考轨迹的比较性评估。

在基于大语言模型的网络智能体方面，WebGPT、WebAgent、SeeAct等系统展示了LLM执行多步浏览任务的能力，近期工作结合了视觉感知与结构化页面表示以提升准确性。AgentGPT、AutoGPT、OpenClaw等框架提供了标准化的智能体部署接口。**ClawBench**旨在评估任何能控制Chromium浏览器的智能体系统，独立于底层模型或框架。

在评估方法方面，先前工作使用了动作序列匹配、基于URL的成功检测、截图比较和人工判断等方法，但这些方法分别存在有效路径多样、确定性不足或成本高昂等问题。**ClawBench**通过结合**拦截最终提交请求的HTTP负载**与一个执行步骤级对齐的智能体化评估器，来规避这些问题，产生基于证据的二元判定。

近期并发或互补的工作包括：TheAgentCompany（自托管沙箱公司模拟）、EconWebArena（实时网络经济研究任务，侧重只读）、MCP-Bench（评估结构化API调用）、TrickyArena（研究黑暗模式）、AssistantBench（侧重信息检索的开放网络任务）以及WebCanvas（类似实时网络设置但无HTTP负载验证）。这些工作共同体现了**真实性与可复现性之间的权衡**。**ClawBench**明确选择了真实性，并通过基于人类参考的比较评估和全栈轨迹记录来缓解可复现性问题。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为ClawBench的评估框架来解决AI代理在真实网络环境中完成日常在线任务的能力评测问题。其核心方法、架构设计和关键技术如下：

**整体框架**：ClawBench采用三阶段架构：任务定义、代理执行（包含五层记录）以及通过“代理化评估器”进行的自动化评估。整个框架的核心设计理念是，评估代理在真实网站上的表现并不需要阻止它们与真实网站交互，而只需拦截最终提交请求。

**主要模块/组件**：
1.  **任务定义与收集**：通过人工标注，从144个真实在线平台中精心策划了153个日常在线任务。每个任务包含三个要素：自然语言用户指令、起始URL以及在HTTP请求级别指定的终端提交目标。任务涵盖8个高级类别（如日常、工作、金融、旅行等），重点是“写密集型”操作（如填写表单、完成购买、提交申请等会改变服务器状态的操作）。
2.  **轻量级拦截层**：这是实现安全评估的关键创新组件。通过一个Chrome扩展和CDP服务器，监控所有发出的HTTP请求。当代理的操作触发与人工标注的拦截规则（URL模式、HTTP方法）匹配的请求时，系统会捕获完整的请求载荷（包括表单字段、头部信息等），并阻止该请求发送到服务器，从而确保评估不会产生任何实际副作用（如下单、提交申请）。所有其他请求（如页面加载、动态内容请求）则正常通过，保证了代理体验与真实用户一致。
3.  **五层行为记录系统**：为了支持细粒度评估和深度诊断，框架在代理执行时同步记录五个层面的行为数据：
    *   **会话录制**：录制整个浏览器窗口的视频。
    *   **动作截图**：在每次代理操作（点击、输入、滚动）后立即截图。
    *   **HTTP流量**：记录所有HTTP请求，包括请求体和时间信息。
    *   **代理消息**：以结构化JSON格式记录代理的完整推理链、工具调用和中间输出。
    *   **浏览器动作**：捕获低级别的浏览器事件（如鼠标点击坐标、按键、滚动偏移）。
4.  **代理化评估器**：这是评估模块的核心。它利用上述五层记录，将代理的执行轨迹与人工标注的参考轨迹进行多模态、多层次的比对。评估器（通常由一个Claude Code子代理实现）根据固定的评估准则，对两条轨迹进行步骤对齐、差异检测，并检查代理是否完成了所有必要操作并达到了与人类参考等效的终端状态，从而判定任务成功与否。

**创新点**：
1.  **真实网络环境与安全评估的结合**：ClawBench是首个在真实生产网站（而非离线沙盒）上评估“写密集型”任务的基准测试。其创新的轻量级拦截机制，通过精准拦截最终提交请求，在保留真实网站全部复杂性和动态性的同时，实现了零副作用的评估安全性。
2.  **全面且可诊断的多层记录**：提出的五层同步记录系统远超现有基准（通常仅记录最终输出或截图），为每个代理运行提供了前所未有的丰富行为数据，支持从观察到思考、从操作到网络影响的全面分析和失败诊断。
3.  **基于人类参考轨迹的可靠评估**：每个任务都提供了由人工在相同框架下完成的完整参考轨迹（同样包含五层数据），使得评估器能够进行细致、客观的轨迹比对，避免了仅依赖脚本检查或LLM-as-judge可能带来的不可靠性问题。
4.  **聚焦高价值、高难度任务**：明确专注于对日常生活直接相关、且需要多步骤工作流、信息整合和准确表单填写能力的“写密集型”任务，填补了现有基准测试的空白，对AI代理提出了更高要求。

### Q4: 论文做了哪些实验？

论文在ClawBench框架上对7个前沿AI模型进行了实验评估。实验设置方面，每个模型通过OpenClaw代理框架控制一个Chromium浏览器实例，并在后台运行ClawBench Chrome扩展和CDP工具服务器来拦截HTTP请求和代理动作以进行事后评估。为确保可复现性，每个基准测试运行在封装容器中，并禁用Chrome的UI提示、同步和不相关扩展。

数据集/基准测试即论文提出的ClawBench，包含153个涵盖日常生活与工作的简单任务，涉及144个实时平台，分为15个类别（如购物、预约、求职等）。这些任务要求代理从用户文档获取信息、跨平台导航多步骤工作流以及正确填写详细表格等。

对比方法包括5个专有模型（Claude Sonnet 4.6、GPT-5.4、Gemini 3.1 Flash Lite、Claude Haiku 4.5和Gemini 3 Flash）和2个开源模型（GLM-5和Kimi K2.5）。主要结果以成功率（SR）作为核心指标。整体上，Claude Sonnet 4.6表现最佳，成功率为33.3%，其次是GLM-5的24.2%。模型在不同任务类别间表现差异显著：Claude Sonnet 4.6在Daily、Finance、Academic和Social类别领先，GLM-5在Work类别最优，Gemini 3 Flash在Travel类别领先，Claude Haiku 4.5在Dev类别领先。这些结果表明当前代理尚未展现跨领域的统一能力，且即使最佳类别结果也远未饱和，凸显了ClawBench的整体难度。

### Q5: 有什么可以进一步探索的点？

本文的局限性在于其任务范围虽广，但主要集中于信息填写和流程导航类操作，对于需要复杂推理、多轮对话协商（如客服沟通）或处理高度非结构化动态内容（如弹窗验证码）的任务覆盖不足。此外，评估主要依赖最终请求拦截的成功率，对任务执行过程的效率、鲁棒性及在模糊指令下的适应性缺乏细粒度度量。

未来研究可从以下方向深入：一是扩展任务类型，纳入需跨平台信息整合与决策的长期任务（如比价购物），并增强对多模态交互（如图片验证、语音指令）的评估。二是改进评估体系，开发过程性指标，如步骤合理性、错误恢复能力，并引入人类偏好评估以衡量用户体验。三是提升Agent能力，可探索将大型语言模型与专用工具（如文档解析器、工作流引擎）更深度结合，并研究在安全前提下进行持续在线学习，使Agent能自适应网站界面变化。这些探索将推动智能体从完成预设流程向真正理解用户意图、灵活处理复杂现实任务演进。

### Q6: 总结一下论文的主要内容

本文介绍了ClawBench评估框架，旨在测试AI智能体在真实在线任务中的执行能力。核心问题是现有基准测试通常在离线沙盒中使用静态页面，无法反映真实网络环境的动态复杂性，因此需要构建一个更贴近现实、能全面评估智能体实用性的评测体系。

论文的主要贡献是提出了ClawBench，一个包含153个日常在线任务的评估框架，涵盖15个类别、144个真实生产网站。这些任务模拟了人们工作和生活中的常规操作，如完成购买、预约、提交申请等，要求智能体具备从文档提取信息、跨平台多步骤导航以及正确填写大量表单等超越现有基准的复杂能力。方法上，ClawBench通过一个轻量级拦截层在真实网站上运行，仅阻止最终的提交请求，从而在确保评估安全无副作用的同时，完整保留了网络交互的动态性和挑战性。

主要结论是，对7个前沿模型的评估表明，无论是专有还是开源模型，目前都只能完成其中一小部分任务（例如表现最佳的Claude Sonnet 4.6成功率仅为33.3%）。这揭示了当前AI智能体作为通用助手在实际应用中的显著局限性，也说明ClawBench是一个具有挑战性的基准，其进展将推动开发更可靠、实用的AI助手。
