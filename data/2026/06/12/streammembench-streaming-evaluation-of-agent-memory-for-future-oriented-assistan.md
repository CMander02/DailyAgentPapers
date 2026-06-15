---
title: "StreamMemBench: Streaming Evaluation of Agent Memory for Future-Oriented Assistance"
authors:
  - "Guanming Liu"
  - "Yuqi Ren"
  - "Hansu Gu"
  - "Peng Zhang"
  - "Weihang Wang"
  - "Jiahao Liu"
  - "Ning Gu"
  - "Tun Lu"
date: "2026-06-12"
arxiv_id: "2606.14571"
arxiv_url: "https://arxiv.org/abs/2606.14571"
pdf_url: "https://arxiv.org/pdf/2606.14571v1"
github_url: "https://github.com/landian60/StreamMemBench"
categories:
  - "cs.AI"
tags:
  - "Agent记忆"
  - "评测基准"
  - "个人Agent"
  - "流式处理"
  - "未来导向协助"
  - "反馈利用"
  - "长上下文"
relevance_score: 9.0
---

# StreamMemBench: Streaming Evaluation of Agent Memory for Future-Oriented Assistance

## 原始摘要

A central role of personal-agent memory is to turn stored information and prior interactions into future-oriented assistance. In daily use, useful cues come from what the agent observes and how the user interacts with the agent, and the agent must carry them forward from the current request to similar future tasks. Existing memory benchmarks usually test dialogue recall or task improvement in isolation, leaving the trajectory from streaming observations to later assistance largely untested. We introduce StreamMemBench, a streaming benchmark that constructs a two-step task sequence around each evidence anchor from EgoLife egocentric streams. The initial task tests evidence use, while the follow-up task tests whether feedback and interaction experience are reused. Four metrics diagnose evidence recall, initial evidence use, feedback incorporation, and follow-up reuse. Experiments with eight memory systems across two backbones show that current systems often fail to use observed evidence or turn feedback into reliable follow-up behavior, even when evidence is stored or feedback is incorporated locally. StreamMemBench is publicly available at https://github.com/landian60/StreamMemBench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文《StreamMemBench: Streaming Evaluation of Agent Memory for Future-Oriented Assistance》试图解决个人智能体记忆系统在流式场景下无法有效支持面向未来辅助的核心问题。研究背景是，个人智能体（如基于大型语言模型的助手）需要从持续的流式观察（如第一人称视角的日常记录）和用户交互中识别并存储关键信息，以便在当前任务中利用这些证据，并在后续的相似任务中复用从用户反馈中获得的经验。然而，现有记忆评估基准大多存在不足：它们通常使用脚本化对话或合成聊天记录，测试侧重对话回忆或孤立的任务改进，忽略了从流式观测到后期辅助的完整轨迹。具体不足包括：无法评估从非结构化流中提取并利用证据的能力（证据使用），缺乏真实的用户反馈来驱动经验复用，且难以追溯信息是否真正来源于观测。因此，本文提出StreamMemBench，一个流式基准，通过围绕来自EgoLife自我中心视频流的“证据锚点”构建两步任务序列（初始任务测试证据使用，后续任务测试反馈与交互经验的复用），并设计四项指标（Fidelity、Feedback Incorporation、Initial Evidence Use、Follow-up Reuse）来诊断记忆系统在面向未来辅助中的成败，从而系统地填补现有评估空白。

### Q2: 有哪些相关研究？

相关研究可分为三类：1) **记忆系统方法类**，如基于检索的MemoryBank和通用RAG管道、主动管理记忆的Mem0/EverMemOS（事实级提取）、A-Mem（块级链接）、MemOS/MemoryOS（层级整合），以及过程性记忆的MemSkill/IntPro/MemP（重用技能和模式）。本文与这些系统的区别在于不提出新方法，而是系统评估它们。2) **个人记忆评测类**，如LoCoMo和PersonaMem（对话回忆和动态用户画像）、LongMemEval和EverMemBench（长上下文与多方交互）、EgoLife和LifeDialBench（流式第一人称观察流）——后者最接近流式场景但未联合测试观察证据与交互反馈。本文通过构造“初试-后续”两阶段任务序列弥补这一空白。3) **智能体记忆基准类**，如MemoryAgentBench（增量交互与用户反馈）、MemoryBench和MemoryArena（持续学习与多会话任务）——它们测试行为改进但反馈通常不与同一流中可验证的观察证据绑定。StreamMemBench的核心区别在于每条轨迹都锚定自EgoLife第一人称日志的证据，同时追踪对观察证据的使用和交互反馈的巩固，并用四个分离指标诊断回忆、初始使用、反馈整合和后续重用的失败模式。

### Q3: 论文如何解决这个问题？

论文提出StreamMemBench，一个流式基准测试，用于评估代理记忆从流式观测到未来任务协助的能力。核心方法是构建一个两阶段流程：构造阶段和评估阶段。

在构造阶段，首先使用证据锚点代理 \(A_{anchor}\) 处理EgoLife的片段，提取用户特定证据并构建候选三元组，包含一个证据锚点 \(a_k\)（记录如长期偏好、计划、承诺或能力等未来可用的证据）和两个任务查询（初始任务 \(T_1\) 和后续任务 \(T_2\)）。两个查询都依赖于同一证据但场景不同，且查询文本不直接泄露该证据。随后，审查代理 \(A_{review}\) 检查每个候选三元组，确保证据支持、不会泄露证据、必须依赖证据才能正确回答，以及两个查询都自然且真实。

在评估阶段，代理记忆系统 \(M\) 按时间顺序摄取流数据。随后执行一个标准化的任务序列：先接受初始任务 \(T_1\) 生成回答 \(R_1\)，然后由用户代理 \(A_{user}\) 模拟反馈（确认或纠正，并提供缺失证据），\(M\) 据此生成反馈后响应 \(R_F\)；完成初始交互后，该交互被提交至记忆；接着接受后续任务 \(T_2\) 生成回答 \(R_2\)。系统使用四个指标进行诊断：保真度（Fidelity）测试证据是否被存储；初始证据使用（IEU）测试初始响应；反馈整合（FI）测试纠正后的响应；后续重用（FUR）测试后续任务是否复用经验。评估采用黑盒方式，仅依赖文本响应。创新点在于设计了双任务序列，清晰分离了证据使用与经验重用，并通过严格的审查和语义匹配确保测试的有效性。

### Q4: 论文做了哪些实验？

论文在StreamMemBench基准上进行了实验。实验数据基于EgoLife数据集，包含6名参与者的7天连续自我中心记录，划分为3,347个5分钟流片段和8,107个证据锚点，每个锚点生成两个任务查询共16,214个查询。评估了两种检索基线（RAG_raw和RAG_ext）和六种记忆系统（Mem0、EverMemOS、A-Mem、MemOS、MemoryOS和MemSkill），并在DeepSeek-V4-Flash和Gemini-3-Flash两个骨干网络上运行。

四个关键指标包括：保真度（证据存储检查）、初始证据使用（IEU）、反馈整合（FI）和后续重用（FUR）。主要结果显示，即使保真度很高（如RAG_raw和A-Mem为100%），IEU和FUR仍可能较低（例如RAG_raw在DeepSeek上IEU仅27.95%）。A-Mem在FUR上表现最佳（64.98%），而MemOS的IEU和FUR极低（分别为2.94%和3.96%）。实验还分析了随流长度的时间漂移和反馈效果，发现系统普遍存在从证据存储到任务使用的鸿沟，并且生命周期故障模式分析显示，故障多发生在初始使用或后续重用阶段，而非证据形成阶段。

### Q5: 有什么可以进一步探索的点？

论文的核心局限在于基准测试覆盖了有限的内存系统和检索基线，未来可以扩展到更长流媒体、更广泛的系统家族（如多代理协作框架）。当前的两步任务序列虽能测试记忆重用，但真实场景中用户行为存在长期依赖和意图漂移，可探索多步骤、跨会话的连续任务链。此外，当前指标仅关注证据召回和使用正确性，缺乏对记忆优先级排序、时间效率及用户隐私风险的量化评估（如系统是否会过度存储敏感信息）。改进方向包括：设计自适应记忆压缩机制（如基于 importance sampling 的动态过期策略）；引入对抗性用户反馈测试系统对误导性修正的鲁棒性；将隐私关切融入评估（如用户可编辑记忆后可预测性指标）。最后，可结合多模态联合推理（如视觉+交互日志）来弥补当前仅依赖文本指令的局限，使系统能更自然地处理流媒体中的弱监督信号。

### Q6: 总结一下论文的主要内容

StreamMemBench是一个用于评估智能体记忆在面向未来辅助中流式能力的基准。现有基准通常孤立测试对话回忆或任务改进，而忽略了从流式观察到后续协助的轨迹。该基准围绕EgoLife自我中心流中的每个证据锚点构建两步任务序列：初始任务测试证据使用，后续任务测试反馈和交互经验的复用。通过四项指标分别诊断证据回忆、初始证据使用、反馈整合和后续复用。在两种骨干网络上的八个记忆系统实验表明，当前系统即使能够存储证据或局部整合反馈，也往往无法利用观察到的证据或将反馈转化为可靠的后续行为。StreamMemBench的核心贡献在于提出了将记忆视为面向未来辅助能力而非单纯信息存储的评价原则，强调记忆应通过是否支持有用的未来行为来评判。
