---
title: "From Runnable to Shippable: Multi-Agent Test-Driven Development for Generating Full-Stack Web Applications from Requirements"
authors:
  - "Yuxuan Wan"
  - "Tingshuo Liang"
  - "Jiakai Xu"
  - "Jingyu Xiao"
  - "Yintong Huo"
  - "Michael R Lyu"
date: "2026-05-17"
arxiv_id: "2605.17242"
arxiv_url: "https://arxiv.org/abs/2605.17242"
pdf_url: "https://arxiv.org/pdf/2605.17242v1"
categories:
  - "cs.SE"
tags:
  - "Multi-Agent Systems"
  - "Software Engineering Agent"
  - "Test-Driven Development"
  - "Code Generation Agent"
  - "Autonomous Web Development"
relevance_score: 8.5
---

# From Runnable to Shippable: Multi-Agent Test-Driven Development for Generating Full-Stack Web Applications from Requirements

## 原始摘要

Coding agents can generate web applications from natural-language descriptions, yet a recent benchmark study shows that generated applications fail to meet functional requirements in over 70% of cases. The core difficulty is that web correctness cannot be assessed from source files or terminal output: the application must be deployed, exercised through simulated browser interactions, and failures must be translated into actionable repair signals -- steps that current agents cannot perform without human mediation.
  We present TDDev, a framework that automates this closed loop through three stages: (1) converting high-level requirements into structured acceptance tests before any code is written, (2) deploying the application and validating it through browser-based interaction simulation, and (3) translating browser-observed failures into structured repair reports for the coding agent. Enabled by TDDev, we conduct the first controlled empirical study of Test-driven development (TDD) strategies for web application generation, comparing four development protocols across two coding agents, two backbone models, and two benchmarks. TDD infrastructure consistently improves generation quality by 34--48 percentage points over a no-TDD baseline. The central finding is that the optimal protocol depends on the model's generation style: models that build applications holistically benefit most from agentic enforcement, while models that extend code conservatively benefit from incremental enforcement. Mismatching protocol to generation style eliminates the TDD benefit entirely while multiplying token cost up to 25-fold. A user study confirms that TDDev reduces manual developer intervention to zero, shifting the workload from continuous prompt engineering to autonomous, feedback-driven refinement.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决编码代理生成的Web应用程序在功能需求上失败率超过70%的核心问题。研究背景是，虽然现有编码代理能从自然语言描述生成可运行的代码原型，但这些代码远未达到可交付的标准。现有方法的不足在于，Web应用程序的正确性无法像传统软件那样通过检查源文件或终端输出来评估，必须经过部署、在浏览器中模拟用户交互才能验证，并且浏览器中观察到的失败信息必须被转化为代理能理解的修复信号。然而，当前代理无法自动完成这一闭环，每个步骤都高度依赖人工干预，导致测试驱动开发（TDD）流程无法自动化。因此，本文要解决的核心问题是：如何构建一个自动化的TDD闭环框架，使编码代理能够在最少人工干预下，自主地从需求出发生成功能完整的全栈Web应用程序，并系统性地研究不同TDD策略对生成质量的影响。

### Q2: 有哪些相关研究？

相关研究可归纳为以下几类：

1. **UI代码生成类**：如基于CNN原型和MLLM的前端代码生成方法，它们主要关注前端视觉外观而非全栈功能。本文通过WebGenBench证明了此类方法在功能需求上存在70%以上的失败率，这正是TDDev要解决的核心问题。

2. **编码智能体类**：如AutoCodeRover、D4C等代理在仓库级软件工程任务中表现优异，但均依赖"直接可访问的执行环境"（终端输出/编译器反馈）。本文指出Web开发打破了这一假设——正确性取决于浏览器渲染和用户交互模拟，这是传统编码代理无法自行完成的。

3. **GUI测试类**：包括记录回放、随机测试（Monkey）、模型测试和强化学习测试方法。这些方法虽重视UI观察，但要么成本高、覆盖率有限，要么缺乏语义理解。最新MLLM方法具有视觉语义能力，但主要用于探索性测试而非功能验证和修复反馈。

4. **测试驱动开发（TDD）类**：如TiCoder利用LLM生成用户确认的测试用例提升46%通过率，ConTested利用测试套件一致性筛选高质量代码。但这些方法均假设测试已存在或验证反馈可直接获取。本文创新在于：针对Web应用构建了从需求到测试生成、自动部署、浏览器模拟验证、结构化修复报告的全闭环TDD框架，首次在受控实验中比较了四种TDD协议，并发现协议与模型生成风格匹配的关键作用。

### Q3: 论文如何解决这个问题？

TDDev 通过一个闭环的测试驱动开发框架解决全栈 Web 应用生成中功能不达标的问题。整体框架分为三个核心阶段:

1. **验收测试生成**: 在编写任何代码前,先用 LLM 从自然语言需求中生成可执行的验收测试。它通过“肥皂剧测试”思路,先让 LLM 想象具体的用户角色和目标,从而获得多样且贴合实际的需求;再为每个需求生成包含功能描述、交互步骤和预期结果的测试用例,确保测试可执行、可评判。

2. **部署与浏览器验证**: 将生成的应用部署到本地 URL,使用 Playwright 打开浏览器。设计了一个轻量级的 LLM 驱动的测试代理,它观察页面的可访问性树,结合测试上下文(功能、步骤、预期结果和历史轨迹),决定执行下一步 Playwright 操作或给出通过/失败/部分通过的判决。这种方式无需预知应用结构,能适应不同实现。

3. **失败翻译**: 当测试未通过时,将测试代理的交互轨迹和自然语言理由转换为结构化修复报告,记录尝试的操作、失败位置和观察结果,为编码代理提供具体的修复起点。

研究还定义了四种开发协议(增量式、全项目、自主式、无TDD基线)作为实验变量,通过对比隔离了TDD基础设施、外部强制程度和增量粒度的效果。核心创新在于将可运行的端到端TDD闭环自动化,使浏览器层面观察到的失败能转化为可操作的修复信号,从而将人工干预降为零。

### Q4: 论文做了哪些实验？

论文进行了四个研究问题（RQ1-RQ4）的实验。实验设置了四种开发协议（Whole-Project、Incremental、Agentic-TDD、Non-TDD），在两种编码代理（ClaudeSDK、OpenCode）、两种骨干模型（Claude Sonnet 4.6、Qwen-3.5-397B-A17B）和两个基准（WebGen-Bench、ArtifactsBench）上交叉评估，共四个实验组合。WebGen-Bench为主要基准，含101个任务（主实验随机抽50个），ArtifactsBench用于跨数据集泛化评估（随机抽100个）。RQ1评估模块可靠性：测试生成覆盖率达语义匹配准确性，测试代理准确率在标准夹具应用上衡量。RQ2衡量TDD收益：与Non-TDD基线相比，TDD基础设施稳定提升生成质量34-48个百分点。RQ3比较不同强制执行水平：最优协议依赖模型生成风格——整体构建型模型受益于代理强制执行，而保守扩展型模型受益于增量强制执行；错误匹配会消除TDD优势并将代币成本提升最多25倍。RQ4分析反馈轮次影响，通过acc@k（k=1...5）曲线展示准确率随反馈轮次增加的变化。主要指标是acc@K（最终准确率），同时记录代币消耗作为成本指标。用户研究证实TDDev可将手动开发干预降至零。

### Q5: 有什么可以进一步探索的点？

这篇论文的核心贡献在于自动化了Web应用测试驱动开发的闭环流程，但其局限性和未来探索方向同样清晰。首先，**协议与模型风格的强依赖关系是双刃剑**：当前结论基于Claude Sonnet和Llama 3.1两类模型，未来需验证在其他模型（如GPT-4o、Gemini）上是否成立，并探索能否在运行时**动态识别**模型生成风格并自适应切换协议，而非人工预设。其次，**修复报告的质量和粒度**是关键瓶颈：论文中修复报告由失败trace直接转化，但复杂交互失败（如异步状态、DOM竞态）的归因仍可能不精确。可以探索引入**多模态信号**（如截图对比、渲染树diff）来增强报告的可操作性，甚至让智能体自我生成修复补丁并验证。再者，**基准测试的局限性**：当前基于标准Web应用组件，但真实需求往往模糊、多轮迭代，且涉及第三方API交互。未来可研究**自然语言需求与测试用例的自动生成对齐**，减少人工提炼测试时引入的语义偏移。最后，**成本效益分析**：尽管文中提到25倍token成本，但未考虑因减少人工调试而节省的整体时间。一个关键改进是——将失败修复视为强化学习过程，让模型在每次修复后自动生成并执行一个新的最小化测试，形成**测试覆盖率的渐进增长**，避免无效的全局重试。

### Q6: 总结一下论文的主要内容

论文提出并解决了测试驱动开发（TDD）在生成全栈Web应用中的自动化问题，核心挑战在于Web应用的正确性无法通过源码或终端输出评估，必须通过模拟浏览器交互来验证。为此，作者提出了TDDev框架，自动完成三个环节：将高层需求转化为结构化验收测试、部署应用并通过浏览器交互模拟验证、将浏览器观测到的失败转化为可执行的修复报告。基于该框架，论文首次开展了关于Web应用生成中TDD策略的受控实证研究，比较了四种开发协议，涉及两个编码智能体、两个骨干模型和两个基准。主要结论是：TDD基础设施使生成质量比无TDD基线提升34至48个百分点；最优协议依赖模型的生成风格——整体构建型模型受益于智能体强制执行，保守扩展型模型受益于增量式强制执行；策略与风格不匹配会完全消除TDD优势，并将令牌成本提高25倍。用户研究证实TDDev将人工干预降至零，实现了从持续提示工程到自动化、反馈驱动精化的转变。该工作首次系统性地将TDD自动化应用于Web应用生成，为提升生成代码的可交付性提供了方法论和实证基础。
