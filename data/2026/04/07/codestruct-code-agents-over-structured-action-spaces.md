---
title: "CODESTRUCT: Code Agents over Structured Action Spaces"
authors:
  - "Myeongsoo Kim"
  - "Joe Hsu"
  - "Dingmin Wang"
  - "Shweta Garg"
  - "Varun Kumar"
  - "Murali Krishna Ramanathan"
date: "2026-04-07"
arxiv_id: "2604.05407"
arxiv_url: "https://arxiv.org/abs/2604.05407"
pdf_url: "https://arxiv.org/pdf/2604.05407v1"
categories:
  - "cs.AI"
  - "cs.SE"
tags:
  - "Code Agent"
  - "Agent Architecture"
  - "Tool Use"
  - "Structured Action Space"
  - "Abstract Syntax Tree (AST)"
  - "SWE-Bench"
  - "CodeAssistBench"
  - "Synthesis"
  - "Evaluation"
relevance_score: 9.0
---

# CODESTRUCT: Code Agents over Structured Action Spaces

## 原始摘要

LLM-based code agents treat repositories as unstructured text, applying edits through brittle string matching that frequently fails due to formatting drift or ambiguous patterns. We propose reframing the codebase as a structured action space where agents operate on named AST entities rather than text spans. Our framework, CODESTRUCT, provides readCode for retrieving complete syntactic units and editCode for applying syntax-validated transformations to semantic program elements. Evaluated on SWE-Bench Verified across six LLMs, CODESTRUCT improves Pass@1 accuracy by 1.2-5.0% while reducing token consumption by 12-38% for most models. Models that frequently fail to produce valid patches under text-based interfaces benefit most: GPT-5-nano improves by 20.8% as empty-patch failures drop from 46.6% to 7.2%. On CodeAssistBench, we observe consistent accuracy gains (+0.8-4.4%) with cost reductions up to 33%. Our results show that structure-aware interfaces offer a more reliable foundation for code agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型的代码智能体在处理软件工程任务时，因将代码库视为非结构化文本而导致的效率低下和可靠性差的核心问题。研究背景是，随着大语言模型能力的提升，代码智能体已能处理仓库级的bug修复和功能实现等复杂任务，但当前主流方法（如SWE-Bench中所示）存在根本的抽象失配：它们将程序当作纯文本来交互，通过行号或字符串模式进行读取和编辑，完全忽略了代码固有的语法和语义结构。

现有方法（即基于文本的交互范式）存在显著不足。在读取代码时，智能体要么需要读入整个文件（引入大量无关上下文干扰推理），要么选择行范围（常导致函数被不完整截断）。在修改代码时，基于字符串的替换方式尤其浪费且脆弱：即使是微小编辑，模型也不得不重新生成大量原有代码；同时，该方法极易因代码格式漂移而遭遇“未找到匹配”错误，或因目标模式在代码库中重复出现而引发“多匹配”错误。这些系统性缺陷迫使智能体陷入高成本的试错循环。尽管近期一些系统尝试通过引入仓库地图、符号索引等结构性摘要来缓解问题，但这些改进主要引导智能体“查看何处”，其底层的读写操作本质上仍是文本式的，依然继承了原有的脆弱性和低效性。

因此，本文要解决的核心问题是：如何为LLM代码智能体设计一个更可靠、更高效的代码交互基础。具体而言，论文提出了CODESTRUCT框架，其核心思想是将代码库重构为一个结构化的动作空间，使智能体能够直接基于命名的抽象语法树实体（如file.py::ClassName::method）进行操作，而非文本片段。该框架提供了`readCode`（用于检索完整的语法单元）和`editCode`（用于应用经过语法验证的转换）两个结构感知原语，从而消除字符串匹配的脆弱性，避免冗余代码再生，并将删除、复制等操作转化为原子动作，最终为代码智能体建立一个高效且基于结构的读写范式。

### Q2: 有哪些相关研究？

本文的相关工作主要可分为三类：代码智能体系统、代码结构表示与学习，以及结构化代码转换方法。

在**代码智能体系统**方面，SWE-Agent和Agentless等系统为智能体提供了基于文本的文件读取和编辑工具，通过多步骤方式操作仓库。近期工作通过文件映射或符号索引等机制增强了代码定位与检索，但仍未定义可执行的结构化修改原语，读写操作本质上仍是基于文本的。本文的CODESTRUCT框架则向前迈进了一步，将代码库重构为结构化动作空间，使智能体能直接对命名的AST实体进行操作，而非间接处理非结构化文本。

在**代码结构表示与学习**方面，Code2Vec、PSCS等基于路径的模型利用AST路径序列表示代码，实现比基于令牌的方法更具语义的检索。ASTNN及其后续工作将抽象语法树分解为语句级子树以进行神经表示学习。然而，这些方法仅将结构信息作为编码层的输入特征，用于单次预测任务，并未将其暴露为智能体在多轮工作流中可操纵的、可执行的动作空间。本文工作则旨在创建这样一个可执行的动作空间。

在**结构化代码转换方法**方面，程序修复系统（如DeepFix、DrRepair）和语法约束解码器利用AST或编译器反馈来减少语法错误。树差分算法（如GumTree）和基于规则的转换工具（如Comby、Semgrep）能够生成细粒度的AST编辑脚本或进行语义感知的重写。但前者主要用于离线差分或进化搜索，后者则需要预先指定转换模式，均不适合开放式的、多步的智能体问题求解。本文的CODESTRUCT框架区别于它们，将语义程序实体作为智能体在决策时可动态构建和调用的首要动作，适用于多步骤的交互式问题解决。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为CODESTRUCT的结构化接口来解决传统基于文本的代码代理在处理代码库时存在的脆弱性问题。其核心方法是将代码库重构为一个结构化的动作空间，使代理能够直接操作从抽象语法树（AST）派生的命名程序实体，而非脆弱的文本片段。

整体框架以AST作为环境状态的核心表示。系统将源代码解析为AST，使得文件、类、函数、方法等程序实体成为显式且可寻址的对象。代理通过两个核心工具与该结构化环境交互：`readCode`（结构感知的代码检索）和`editCode`（结构感知的代码修改）。这两个工具共同定义了代理可用的基本操作。

主要模块与组件包括：
1.  **结构感知的代码检索（readCode）**：该模块支持从粗到细的工作流。当输入为目录时，返回文件列表以供浏览；当输入为文件且无选择器时，根据文件大小自适应返回完整内容或仅包含类/函数签名的结构摘要；当提供文件路径和选择器时，则通过确定性名称匹配（支持模糊匹配）定位到具体的AST节点，并返回该节点对应完整语法单元（如整个函数）的源代码。这避免了基于行号的检索，并减少了无关上下文。
2.  **结构感知的代码修改（editCode）**：该模块允许代理通过指定操作类型（插入、替换、删除）和目标实体选择器来执行编辑。在定位到目标AST节点后，工具会在该节点的语法作用域内应用转换，自动保留缩进格式，并在提交更改前验证修改后的AST的语法正确性。任何会导致语法错误的编辑都会被拒绝，从而在构造上保证了修改后的代码语法有效。
3.  **标准化代理接口**：上述两个核心工具通过模型上下文协议（MCP）等标准化工具接口暴露，使得CODESTRUCT能够无缝集成到现有的LLM代理框架中，无需修改代理自身的规划或执行逻辑。

关键技术及创新点在于：
*   **结构化动作空间**：将代码交互重新定义为在命名程序实体（而非匿名文本跨度）上的操作，使代理的动作空间与人类开发者使用的抽象概念对齐。
*   **语义意图与文本实现的分离**：代理通过选择器指定“修改什么”（语义意图），而工具负责“如何实现”文本更改，消除了对易漂移的行号或字符串匹配的脆弱依赖。
*   **语法有效性保证**：所有编辑均在AST级别进行，并通过验证确保每次修改都产出语法有效的AST，从根本上避免了基于文本的编辑可能产生的畸形代码。
*   **可分析的明确轨迹**：每一次`editCode`调用都产生一次明确的状态转换，使得多步编辑过程成为一系列结构化动作的轨迹，便于对代理行为进行超越最终补丁正确性的细粒度分析。

### Q4: 论文做了哪些实验？

论文在SWE-Bench Verified和CodeAssistBench两个基准上进行了实验。实验设置方面，作者将CODESTRUCT（一种基于结构化AST操作空间的代码代理框架）与主流的文本交互基线（如SWE-Agent和OpenHands）进行对比。基线方法通过读取文件或行范围并以字符串替换方式修改代码，而CODESTRUCT则通过`readCode`和`editCode`工具，允许代理基于命名的AST实体（如函数、类）进行语法验证的检索和转换。实验使用了六种大语言模型，包括GPT-5系列（GPT-5、GPT-5-mini、GPT-5-nano）和Qwen系列（Qwen3-Coder、Qwen3-32B、Qwen3-8B），并固定了任务交互预算（大型模型5美元，中型3美元，小型1美元）。评估指标包括Pass@1准确率、输入/输出令牌消耗、LLM调用次数和成本。

在SWE-Bench Verified上，CODESTRUCT显著提升了大多数模型的性能：Pass@1准确率提高了1.2%至5.0%（例如GPT-5从66.0%提升至67.2%，Qwen3-Coder从61.2%提升至66.2%），其中GPT-5-nano提升最大（+20.8%，从19.6%到40.4%）。同时，令牌消耗减少了12-38%（如GPT-5-mini输入令牌减少31.9%，输出令牌减少72.4%），成本降低最高达32.6%。但GPT-5-nano和Qwen3-Coder在令牌使用上有所增加，这与其探索深度提升相关。在CodeAssistBench上，CODESTRUCT也带来了一致的准确率提升（+0.8%至+4.4%），并降低了成本（最高达33.3%）。错误分析显示，结构化操作将高级模型的编辑错误减少了76-88%，并大幅减少了空补丁情况（如GPT-5-nano从46.6%降至7.2%）。消融实验证实了`readCode`和`editCode`的互补作用，移除任一组件都会导致性能下降或成本上升。

### Q5: 有什么可以进一步探索的点？

该论文的局限性及未来研究方向可从多个维度拓展。首先，语言覆盖范围有限，当前评估主要集中于Python，未来需扩展至更多具有不同语法特性的语言（如静态类型语言、复杂泛型），以验证框架的普适性。其次，对语法错误的鲁棒性不足，CODESTRUCT依赖语法有效的源文件进行AST解析，无法处理已存在语法错误的代码，未来可探索结合部分解析或错误恢复机制。再者，任务覆盖较窄，目前仅针对缺陷修复和代码辅助，未来可应用于代码审查、测试生成等更广泛场景。

结合个人见解，可能的改进思路包括：1）设计混合动作空间，结合结构化操作与文本补丁，以处理边缘情况（如格式混乱的代码片段）；2）引入增量解析技术，提升对大型代码库的实时响应能力；3）探索多模态代码表示，将AST与自然语言注释、执行轨迹结合，增强语义理解。此外，可研究如何将结构化操作泛化至非代码任务（如配置文件编辑），进一步拓展智能体应用边界。

### Q6: 总结一下论文的主要内容

论文《CODESTRUCT: Code Agents over Structured Action Spaces》针对当前基于大语言模型（LLM）的代码代理在处理代码仓库时，将其视为非结构化文本、依赖脆弱的字符串匹配进行编辑所导致的格式漂移和模式模糊等问题，提出了一种结构化行动空间的新框架。核心贡献是将代码库重构为结构化行动空间，使代理能够基于抽象语法树（AST）命名的程序实体进行操作，而非文本片段。方法上，CODESTRUCT 框架提供了 readCode 和 editCode 两个关键操作：前者用于检索完整的语法单元，后者则对语义程序元素应用经过语法验证的转换，从而确保编辑的语法有效性。主要结论显示，在 SWE-Bench Verified 和 CodeAssistBench 等基准测试中，CODESTRUCT 显著提升了多种 LLM 的 Pass@1 准确率（提升 1.2%-5.0%，部分模型如 GPT-5-nano 甚至提升 20.8%），同时降低了令牌消耗（最高减少 38%），并有效减少了因文本接口脆弱性导致的无效补丁生成。这表明结构化感知接口为代码代理提供了更可靠的基础，能更好地协调代码的结构化本质与代理操作，提升代码推理与修改的效率和鲁棒性。
