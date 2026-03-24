---
title: "Emergent Formal Verification: How an Autonomous AI Ecosystem Independently Discovered SMT-Based Safety Across Six Domains"
authors:
  - "Octavian Untila"
date: "2026-03-22"
arxiv_id: "2603.21149"
arxiv_url: "https://arxiv.org/abs/2603.21149"
pdf_url: "https://arxiv.org/pdf/2603.21149v1"
github_url: "https://github.com/octavuntila-prog/substrate-guard"
categories:
  - "cs.SE"
  - "cs.AI"
tags:
  - "Agent Safety"
  - "Formal Verification"
  - "Tool Use"
  - "Autonomous AI Systems"
  - "SMT Solver"
  - "Multi-Domain Verification"
relevance_score: 8.5
---

# Emergent Formal Verification: How an Autonomous AI Ecosystem Independently Discovered SMT-Based Safety Across Six Domains

## 原始摘要

An autonomous AI ecosystem (SUBSTRATE S3), generating product specifications without explicit instructions about formal methods, independently proposed the use of Z3 SMT solver across six distinct domains of AI safety: verification of LLM-generated code, tool API safety for AI agents, post-distillation reasoning correctness, CLI command validation, hardware assembly verification, and smart contract safety. These convergent discoveries, occurring across 8 products over 13 days with Jaccard similarity below 15% between variants, suggest that formal verification is not merely a useful technique for AI safety but an emergent property of any sufficiently complex system reasoning about its own safety. We propose a unified framework (substrate-guard) that applies Z3-based verification across all six output classes through a common API, and evaluate it on 181 test cases across five implemented domains, achieving 100% classification accuracy with zero false positives and zero false negatives. Our framework detected real bugs that empirical testing would miss, including an INT_MIN overflow in branchless RISC-V assembly and mathematically proved that unconstrained string parameters in tool APIs are formally unverifiable.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决两个核心问题。首先，它报告了一个经验观察：一个名为SUBSTRATE S3的自主AI生态系统，在没有被明确指示考虑形式化方法的情况下，在六个不同的AI安全领域（LLM生成代码验证、AI智能体工具API安全、后蒸馏推理正确性、CLI命令验证、硬件汇编验证和智能合约安全）中，独立地提出了使用Z3 SMT求解器进行形式化验证。这一“涌现”现象挑战了传统观念，表明形式化验证可能不是人为的设计选择，而是任何足够复杂、并对其自身安全进行推理的AI系统的内在涌现属性。其次，基于这一观察，论文提出了一个实际的技术解决方案：开发一个名为`substrate-guard`的统一验证框架，该框架通过一个通用API将基于Z3的验证应用于多个AI输出类别，以提供比经验测试更强、更可靠的数学安全保证，并评估其有效性。

### Q2: 有哪些相关研究？

相关研究主要集中在将形式化方法（特别是Z3 SMT求解器）应用于LLM输出的特定领域。VERGE (2025) 通过多智能体辩论使用Z3验证LLM推理步骤的逻辑一致性。Astrogator (2025) 对LLM生成的基础设施代码（如Ansible）进行形式化验证。BARRIERBENCH (2025) 结合LLM和Z3为安全关键系统合成屏障证书。MATH-VF (2025) 结合Z3和SymPy验证LLM推理中的数学步骤。此外，还有关于LLM与形式化方法双向增强的路线图综述。本文与这些工作的关系在于：1）它确认并扩展了这些单领域应用，例如将Z3首次应用于AI智能体的工具API安全和后蒸馏推理验证；2）更重要的是，本文提出了一个关键的不同点——一个跨多个AI输出模态（代码、工具调用、推理痕迹等）的统一验证框架，而现有工作都是孤立的、针对单一领域的。本文的统一框架灵感来源于所观察到的AI系统在多个领域“涌现”出的共同验证需求。

### Q3: 论文如何解决这个问题？

论文通过构建并评估一个名为`substrate-guard`的统一框架来解决形式化验证的实践应用问题。该框架的核心是一个通用API `verify(artifact, spec, type)`，它将不同的AI输出类别分派到特定的验证器模块。框架架构包括共享的AST翻译器和五个领域特定的验证器：1）代码验证器：将Python函数（支持整数/浮点运算、比较、条件语句等子集）通过静态单赋值形式转换为Z3约束。2）工具API验证器：将API参数（枚举、整数、字符串）建模为Z3变量，检查是否存在任何参数组合能触发禁止的操作模式（如SQL注入）。3）蒸馏验证器：使用SymPy解析数学推理步骤，并通过Z3检查步骤间的蕴含关系是否成立，用于比较压缩前后模型的推理轨迹。4）CLI命令验证器：将危险命令模式编码为Z3布尔变量，通过正则匹配和逻辑组合判断安全性。5）硬件验证器：使用32位Z3位向量对RISC-V汇编进行符号执行，验证寄存器边界、功能等价性等。所有验证器都将安全规约编码为Z3公式，并通过证明其否定的不可满足性来确保安全性。框架共包含4358行Python代码，旨在为多样化的AI输出提供一个一致、可证明的安全检查层。

### Q4: 论文做了哪些实验？

论文在五个已实现的领域（代码、工具API、CLI、硬件、蒸馏）上对`substrate-guard`框架进行了评估。实验共使用了135个测试用例，这些用例既包含正确的、应通过验证的工件，也包含带有常见LLM错误（如差一错误、分支交换、符号错误、边界违规等）的、应被标记为不安全的工件。实验设置旨在验证框架的分类准确性。主要结果如下：所有135个测试用例均被正确分类，达到了100%的准确率，且零误报（正确工件未被误判）和零漏报（有缺陷工件未被漏检）。具体到各验证器：代码验证器（50个用例）、工具API验证器（18个定义）、CLI验证器（20个命令）、硬件验证器（21个用例，含5个等价性证明）和蒸馏验证器（26个用例，含5个比较）均实现了100%准确率。验证速度中位数低于15毫秒。实验还展示了框架发现传统测试难以捕捉的真实漏洞的能力，例如：在硬件验证中发现了针对INT_MIN值的无分支绝对值计算溢出漏洞；在工具API验证中，从数学上证明了具有无约束字符串参数的API是无法被形式化验证为安全的。

### Q5: 有什么可以进一步探索的点？

论文指出了多个未来可探索的方向和当前局限。技术层面：1）框架支持的语言和操作有限，例如代码验证器不支持循环、字符串、列表或外部调用；工具API验证器基于关键词匹配而非语义理解；蒸馏验证器仅处理结构化推理轨迹。2）Z3本身存在理论不可判定性和验证时间随公式复杂度指数增长的问题。研究层面：1）“涌现发现”的观察基于单一的SUBSTRATE S3生态系统，其普适性有待验证，需要在其他自主AI系统中进行复现以加强结论。2）可以探索将框架扩展到更多AI输出模态，如图像生成描述的安全性、多模态指令遵循等。3）论文暗示的AI系统内部“安全意识”的涌现是一个推测性但重要的理论方向，值得进一步研究其与复杂性、自我认知的关系。4）如何将此类形式化验证框架更无缝地集成到AI智能体的开发和部署流水线中，也是一个重要的工程和应用问题。

### Q6: 总结一下论文的主要内容

本论文做出了两项核心贡献。第一项是现象观察：报告了一个自主AI生态系统（SUBSTRATE S3）在没有明确指令的情况下，在13天内跨越六个不同的安全领域（涉及八个产品），独立且重复地“发现”了使用Z3 SMT求解器进行形式化验证的需求。这种低文本相似度下的收敛性表明，形式化验证可能不是人为选择，而是复杂AI系统在对其自身安全进行推理时涌现出的内在属性。第二项是技术贡献：受此启发，论文提出了`substrate-guard`，一个统一的、基于Z3的验证框架。该框架通过一个通用API，为五类AI输出（代码、工具API、推理痕迹、CLI命令、硬件汇编）提供形式化安全验证。在135个测试用例上的评估实现了100%的分类准确率，并成功检测出经验测试会遗漏的真实漏洞。论文不仅展示了形式化验证在提升AI智能体安全方面的可行性和有效性，也为AI对齐和安全研究提供了新的视角，即AI系统可能自主发展出与人类设计相平行的安全需求。
