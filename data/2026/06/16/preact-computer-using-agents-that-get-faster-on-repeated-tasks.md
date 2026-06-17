---
title: "PreAct: Computer-Using Agents that Get Faster on Repeated Tasks"
authors:
  - "Bojie Li"
date: "2026-06-16"
arxiv_id: "2606.17929"
arxiv_url: "https://arxiv.org/abs/2606.17929"
pdf_url: "https://arxiv.org/pdf/2606.17929v1"
categories:
  - "cs.AI"
tags:
  - "Computer-Using Agent"
  - "Program Compilation"
  - "State Machine"
  - "Task Repetition"
  - "Inference Acceleration"
  - "GUI Agent"
  - "Mobile Agent"
  - "Web Agent"
  - "Desktop Agent"
  - "Replay Mechanism"
  - "Software Automation"
relevance_score: 9.0
---

# PreAct: Computer-Using Agents that Get Faster on Repeated Tasks

## 原始摘要

Computer-using agents drive real software through the screen -- clicking and typing -- but they solve every task from scratch: asked to repeat a task, an agent re-reads the screen, re-reasons every tap, and pays the full cost again. We present PreAct, which lets such an agent get faster on tasks it has done before. The first time it succeeds, PreAct compiles the run into a small state-machine program-states that check the screen, transitions that act-and on later runs replays it directly instead of invoking the agent 8.5-13x faster, with no per-step language-model calls. Replay is not blind: at each step PreAct checks that the screen matches what the program expects before acting, and hands control back to the agent the moment something is off.
  PreAct applies the same discipline when deciding what to keep: a freshly compiled program enters the store only if, re-run from a clean state, an independent evaluator confirms it solved the task-catching programs that replay to their last step yet leave the task undone. Across a mobile, a desktop, and a web benchmark, this store-time check separates repeated runs that improve from ones that degrade as faulty programs accumulate, worth 1.75-2.6 tasks per benchmark, the same direction on all three; a fallback that explores afresh when no program fits brings PreAct level with a strong record-and-replay baseline. We also report what did not matter: prompt wording, runtime guardrails, and whether a language model or a plain embedding retriever selects which program to reuse.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决计算机操作代理（Computer-using Agents）在重复执行相同任务时的效率低下问题。研究背景中，现有代理通过屏幕读取和点击操作完成任务，但每次执行任务时都从零开始，重复读取屏幕、重新推理每一步操作，导致巨大的计算成本浪费。现有方法的不足包括：技能库方法（如SAGE）虽保存行为参数，但运行时仍需语言模型参与，无法消除每步的推理成本；记录-回放系统缓存动作序列，但回放时盲目执行，无法验证每一步是否成功，缺乏分支处理能力，且无法自我改进。本文核心问题是：**如何让计算机操作代理在重复执行已成功完成的任务时，能够显著降低计算成本和延迟，同时保持对执行环境的验证能力，避免盲目回放导致失败**。具体地，PreAct提出将首次成功执行的任务编译为状态机程序，在后续任务中直接回放该程序，通过屏幕检查确保每一步正确，并在程序存储前进行独立验证，从而在8.5-13倍加速的同时，避免因错误程序积累导致的性能退化。

### Q2: 有哪些相关研究？

相关研究可分为以下几类：

1. **计算机使用智能体**：如SeeAct、CogAgent、UI-TARS等，通过屏幕像素和可访问性树操作软件。PreAct与这些智能体正交，可将其作为后备方案。

2. **技能库与经验记忆系统**：Voyager积累代码技能库、ExpeL蒸馏经验为规则、TroVE和LATM构建可复用工具箱。这些系统在运行时仍需LLM调用技能，而PreAct直接执行状态机，无需LLM介入。

3. **工作流编译与回放系统**：Muscle-Mem、AgentRR、Workflow-Use缓存线性动作序列并在缓存命中时直接回放。ActionEngine通过爬取构建状态机并生成扁平Python脚本。PreAct的关键区别在于：(1) 回放时逐状态验证屏幕是否匹配预期；(2) 通过"验证后存储"门控确保只有独立验证成功的程序才被加入库中；(3) 通过去重替换实现增量精炼而非仅追加。

4. **代码作为智能体表示**：PAL、CodeAct等方法用代码作为动作空间。但与PreAct不同，这些系统每次需由LLM重新生成和解释代码。

5. **内部化vs外部化世界模型**：PreAct可视为一种外部化世界模型——每个存储程序是任务动态的可验证模型，而非隐式编码在权重中，因此可检查、替换或修复而无需重新训练。

### Q3: 论文如何解决这个问题？

PreAct通过一种“先验证后执行”的编译-回放循环来解决重复任务效率低下的问题。其核心是将首次成功执行的任务轨迹编译成一个轻量级状态机程序，后续遇到相同任务时直接回放该程序，从而避免调用昂贵的语言模型。

整体框架包含四个主要模块：**程序选择器(Program Selector)**根据任务目标从语料库中检索匹配的状态机程序；**回放器(Replayer)**直接执行该程序，在每个状态转移前先通过验证谓词检查屏幕状态是否匹配，只有匹配时才执行预定义动作，否则将控制权交还给原始智能体；**回退机制(Fallback)**在无匹配程序或回放失败时，退回到完全智能体(CUA)执行任务；**编译与存储管道(Compile & Store)**在任务成功后，将轨迹编译为参数化的状态机，并通过“存储前验证门”(Verify-before-store Gate)确保新程序独立执行后仍能通过评估，才将其存入语料库。

关键技术包括：1) **状态机程序**：每个状态包含验证谓词和操作转移，支持参数绑定(如联系人姓名、电话)和分支处理，比扁平脚本更灵活可靠；2) **运行时验证**：每一步回放前都检查屏幕状态与预期是否一致，出错立即切换为智能体模式，防止盲目执行；3) **存储前验证门**：新程序需从干净的初始状态重新回放并通过独立评估者确认后才入库，防止“执行到最后但任务未完成”的劣质程序积累；4) **去重签名插入**：新程序替换同签名旧程序，使语料库在迭代中精炼而非简单堆积。

创新点在于将智能体执行模式转化为可信任的、无模型调用的状态机回放，同时通过运行时校验和存储前验证保证回放的可靠性和语料库质量，实现了8.5-13倍的速度提升。

### Q4: 论文做了哪些实验？

论文在三个基准测试上进行了实验：AndroidWorld "official-15"子集（15个任务，8个应用领域）、OSWorld "test_tiny"子集（6个任务，涉及Chrome、LibreOffice Calc和Writer）以及WebArena shopping_admin子集（12个字符串匹配任务，基于Magento电商管理面板）。对于AndroidWorld，使用Gemini 3 Flash作为CUA模型；OSWorld和WebArena使用Claude Sonnet 4.6。采用5个种子（42, 100, 1337, 2024, 7777）的多种子协议，从空语料库开始进行冷启动运行，然后复用冷启动构建的语料库进行热启动运行。

主要实验结果：
1. **冷热启动对比**：在AndroidWorld上，热启动的成功率平均提升1.33个任务（从9.33提升到10.67，共15个任务），且没有种子出现退化。热启动中大多数任务通过重放存储的程序完成，而非重新推导。
2. **加速效果**：重放程序无逐步骤语言模型调用，WebArena上热启动比冷启动快8.5-13倍，Android上命中语料库的热启动任务在数秒内完成。
3. **验证门控消融实验**：在所有三个平台上，开启验证门控（gate on）时热启动成功率改善或保持（Android +1.2±0.45，OSWorld +0.2±0.45，WebArena -4.0±2.94）；关闭门控（gate off）时所有平台均退化（Android -1.4±0.89，OSWorld -2.4±0.55，WebArena -5.75±1.71）。门控的边际价值为1.75-2.6个任务，方向一致。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个层面。第一，编译阶段依赖成功运行的完美记录，若初始执行存在微小错误（如点击偏移），生成的有限状态机可能固化低效路径，未来可引入在线学习机制，在重播时动态修正状态转移概率。第二，状态检查仅依赖屏幕像素匹配，对动态内容（如滚动列表、弹窗广告）敏感度不足，建议结合DOM树变化检测或差分注意力机制。第三，存储校验环节存在计算冗余——每次成功执行后需完整二次验证，可优化为蒙特卡洛采样验证或贝叶斯置信度评估。此外，程序检索的鲁棒性值得探索：当前使用固定嵌入模型，若任务描述语义变化（如“保存文件”vs“另存为”），可能出现类似错误匹配。未来可将有限状态机与神经流程图结合，允许在重播中自适应插入新子程序，形成增量式技能库。

### Q6: 总结一下论文的主要内容

PreAct针对计算机使用代理在重复任务上的效率问题，提出了一种让代理从经验中加速的机制。传统代理每次执行任务都需从头感知和推理，成本高昂。PreAct的核心贡献在于，首次成功完成任务后，会将执行过程编译成一个带屏幕状态检查的有限状态机程序。后续遇到相同任务时，直接重放该程序，无需调用语言模型，实现8.5-13倍的速度提升。重放并非盲目执行，每一步都会检查屏幕状态是否匹配预期，不匹配则回退给代理。为确保存储的程序可靠，PreAct在存入前会重置环境并重新运行程序，通过独立的评估器验证任务是否真正解决，避免错误程序累积导致性能恶化。在AndroidWorld、OSWorld和WebArena三个基准测试上，PreAct的验证机制使重复运行表现提升1.75-2.6个任务，而缺乏验证则会导致性能下降。其主要结论是，通过“存储你运行的程序，且只存储经过验证的程序”这一设计原则，代理能够像人类一样将熟练任务内化为自动化习惯，显著提升重复任务效率，而提示词、运行时防护栏和程序选择器等因素影响不大。
