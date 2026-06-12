---
title: "HyperTool: Beyond Step-Wise Tool Calls for Tool-Augmented Agents"
authors:
  - "Yaxin Du"
  - "Yifan Zhou"
  - "Yujie Ge"
  - "Jiajun Wang"
  - "Xianghe Pang"
  - "Shuo Tang"
  - "Tuney Zheng"
  - "Bryan Dai"
  - "Jian Yang"
  - "Siheng Chen"
date: "2026-06-11"
arxiv_id: "2606.13663"
arxiv_url: "https://arxiv.org/abs/2606.13663"
pdf_url: "https://arxiv.org/pdf/2606.13663v1"
categories:
  - "cs.CL"
tags:
  - "Agent规划与推理"
  - "工具调用优化"
  - "LLM Agent架构"
  - "MCP接口"
  - "多步工具使用"
relevance_score: 9.5
---

# HyperTool: Beyond Step-Wise Tool Calls for Tool-Augmented Agents

## 原始摘要

Tool-augmented LLM agents commonly rely on step-wise atomic tool calls, where each invocation, observation, and value transfer is exposed in the main reasoning trace. This creates an \emph{execution-granularity mismatch}: locally deterministic tool workflows are unfolded into repeated model-visible decisions, consuming context and forcing the model to manage low-level dataflow in the trace. We introduce \textbf{HyperTool}, a unified executable MCP-style tool interface that changes the model-visible unit of tool execution. A model invokes HyperTool with a code block that can call existing tools through their original schemas, manipulate returned values, and pass intermediate results locally, folding deterministic tool subroutines into a single outer call. To train models to use this interface, we synthesize HyperTool-format trajectories from cross-tool compositional tasks and verify them in real MCP environments. On MCP-Universe, HyperTool improves average accuracy from 15.69\% to 35.29\% on Qwen3-32B and from 9.93\% to 33.33\% on Qwen3-8B, and surpass GPT-OSS and Kimi-k2.5 on average accuracy, showing that our HyperTool can substantially improve multi-step tool use.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决当前工具增强型LLM代理中一个核心矛盾：工具调用的执行粒度与任务推理需求不匹配。现有方法普遍采用逐步的原子化工具调用范式，即每次调用、观察结果和数据传递都在主推理轨迹中显式展开。这种设计带来了两个主要问题：一是上下文膨胀，大量中间过程的工具返回结果（如地理位置编码后的坐标）在轨迹中累积，即便只有少数字段是下游任务真正需要的；二是推理碎片化，模型不得不在高级任务推理和低级数据流管理之间频繁切换，增加了认知负担。虽然已有一些后处理式的轨迹压缩或子代理方法，但它们要么依赖特定任务假设，要么降低了透明度和可控性，并未从根本上改变工具的执行粒度。为此，本文提出 **HyperTool**，一种统一的、兼容MCP协议的可执行工具接口。它将原有的原子调用模式升级为代码块格式，允许模型在一个外部调用内部通过原始模式组合多个工具、处理中间值、传递局部结果，从而将确定性的工具子序列折叠为一个单一的操作。核心目标是：从根本上改变工具执行的模型可见粒度，从“事后压缩”转向“执行时控制”，在保持紧凑的高层推理轨迹的同时，提升多步工具组合的易用性和表达能力。

### Q2: 有哪些相关研究？

相关研究主要分为三类。第一类是工具增强型代理的基础工作，研究原子化、逐步的API式工具调用，通过推理与动作交错、自监督学习、指令微调等方式让模型调用外部工具。HyperTool并非替代此接口，而是将其封装为MCP风格的工具，通过代码块将确定性工具子流程折叠为单次外层调用，改变执行粒度而非工具规范方式。

第二类是程序化代理方法，将代码作为统一动作表示，允许模型在可执行程序中结合计算、控制流与环境交互。HyperTool与这类方法的区别在于，它不将代码视为通用动作语言，而是作为包装已有工具调用的外壳，保持工具显式性。

第三类是执行抽象方法，包括工作流级方法（如预编译依赖图或蓝图减少重复模型调用）和轨迹级上下文管理方法（如剪枝、压缩、摘要减少历史上下文）。这些方法在逐步执行暴露中间观测后管理轨迹。HyperTool在不同层级操作，将局部确定性工具链折叠为可执行块，从根源上改变模型可见的执行单元。在MCP-Universe基准上，HyperTool在Qwen3-32B上平均准确率从15.69%提升至35.29%，超越了GPT-OSS和Kimi-k2.5。

### Q3: 论文如何解决这个问题？

HyperTool通过一种统一的可执行工具接口解决了细粒度执行不匹配问题。核心创新在于改变了模型可见的原子工具调用单元：将原本需要在主推理轨迹中逐步骤暴露的局部确定性工作流，折叠为单个名为Block(S_t)的外层调用。

整体框架包含三个主要部分：**HyperTool接口**、**轨迹合成流水线**和**验证机制**。

1.  **HyperTool接口（核心设计）**：代理模型不是逐个调用MCP工具，而是编写一段可执行代码块（Block）。代码块内可以按原始Schema调用现有工具、存储返回值为局部变量、解析过滤结果、执行轻量计算、定义临时辅助函数以及直接在调用间传递中间值。只有块级最终观测结果返回给主推理轨迹。若块内仅含单个工具调用，则退化为标准接口；若含多个依赖调用，则表述为单个可执行子程序。设计理念是保留需要任务级推理的观测到主轨迹，将局部数据流内化在块中。

2.  **三阶段轨迹合成流水线**：为训练模型使用该接口，研究者构建了合成数据流程：**阶段一，组合式任务构建**——让教师模型与真实MCP环境交互，基于多工具收集的事实属性归纳出跨工具、跨数据维度的约束条件，确保答案必须通过跨源组合、本地过滤、比较或聚合才能确定。**阶段二，HyperTool轨迹滚动**——通过三种互补机制生成边界感知的演示：上下文压缩（用语言模型将旧工具响应摘要为关键信息）、失败块的局部修复（记录错误并构建修复提示，确保修复后的代码仍针对相同资源和操作）、以及轨迹级压缩。生成遵循三条规则：推理优先于工具调用、确定性工具调用组合成块、块内自包含且最终结果赋给`result`变量。**阶段三，执行与证据验证**——通过执行正确性过滤（移除结构或运行时缺陷）和证据一致性验证（LLM评判器多次投票检查最终答案是否由工具证据支持、中间结果是否正确解释等），保留通过验证的轨迹。

3.  **关键技术实现**：训练时对保留轨迹应用监督微调（SFT），损失施加于模型生成的推理文本和HyperTool代码块，工具观测视为环境输出不参与预测。这教会模型在复杂的多步骤工具使用任务中，学会何时发起块调用、如何实现内部工具组合、以及何时应将中间观测返回主推理轨迹。实验表明，在MCP-Universe基准上，HyperTool在Qwen3-32B上将平均准确率从15.69%提升至35.29%，在Qwen3-8B上从9.93%提升至33.33%，超越了GPT-OSS和Kimi-k2.5等强基线模型。

### Q4: 论文做了哪些实验？

论文在MCP-Universe基准上进行了实验，涵盖网络搜索、金融分析、位置导航和仓库管理四个领域。基线方法包括ReAct（逐步原子工具调用）、CodeAct和ReCode（代码生成）、BrowseMaster（编程化网页浏览）及AgentFold（长时程执行管理）。主要实验基于Qwen3-8B和32B模型，设置最大工具调用50次、上下文128k tokens。结果：HyperTool在8B上平均准确率从ReAct的20.92%提升至33.33%，32B上从24.18%提升至35.29%，平均分数分别达48.42和53.18。金融分析领域增益最大，两规模均达62.50%准确率。消融实验显示，全HyperTool接口优于Atomic+HyperTool混合（33.33% vs 26.85%）；移除执行或证据过滤将平均准确率从33.33%降至18.06%和21.05%。HyperTool减少了全局平均token消耗（816k vs 955k），在金融分析中仅用199k tokens即达62.50%准确率，而ReAct需916k tokens仅32.5%。

### Q5: 有什么可以进一步探索的点？

论文的局限在于当前 HyperTool 主要适用于局部确定性工具子程序（如检索、过滤、计算、聚合），对于需要频繁模型级干预的开放式、不确定或多模态交互场景（如涉及动态外部 API 返回、需要模型实时决策是否终止或切换工具）表现可能不佳。未来可探索将 HyperTool 与自适应调度机制结合，例如让模型在 block 内部插入“决策点”以动态判断是否跳出 block 进行模型级推理。另外，训练数据的多样性和规模限制了下游泛化能力，可借助更丰富的工具生态系统（如云服务、机器人控制）自监督生成更大规模的轨迹，并引入强化学习优化模型对 block 边界的划分，使模型学会在信息增益与上下文消耗间权衡。

### Q6: 总结一下论文的主要内容

论文针对当前工具增强型智能体在执行多步工具调用时存在的“执行粒度不匹配”问题，即原子化的逐步工具调用将局部确定性的工具流程暴露在主推理轨迹中，导致上下文膨胀和推理碎片化。为此，作者提出HyperTool，一种统一的可执行MCP风格工具接口。模型通过调用一个代码块来执行，该代码块内部可使用原有模式调用工具、操作返回值及传递中间结果，将多步工具子程序折叠为单个外部调用。为了训练模型使用该接口，作者从跨工具组合任务中合成了HyperTool格式的轨迹，并在真实MCP环境中验证。在MCP-Universe基准上，Qwen3-8B和Qwen3-32B模型微调后平均准确率分别从9.93%和15.69%提升至33.33%和35.29%，并超越GPT-OSS和Kimi-k2.5等近期模型。主要结论是，HyperTool通过改变工具执行的模型可见粒度，显著提升了多步工具使用的效率和准确性。
