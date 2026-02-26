---
title: "BRIDGE: Building Representations In Domain Guided Program Synthesis"
authors:
  - "Robert Joseph George"
  - "Carson Eisenach"
  - "Udaya Ghai"
  - "Dominique Perrault-Joncas"
  - "Anima Anandkumar"
  - "Dean Foster"
date: "2025-11-26"
arxiv_id: "2511.21104"
arxiv_url: "https://arxiv.org/abs/2511.21104"
pdf_url: "https://arxiv.org/pdf/2511.21104v2"
categories:
  - "cs.LG"
  - "cs.PL"
tags:
  - "程序合成"
  - "形式化验证"
  - "结构化提示"
  - "代码生成"
  - "LLM推理"
  - "领域特定表示"
relevance_score: 5.5
---

# BRIDGE: Building Representations In Domain Guided Program Synthesis

## 原始摘要

Large language models (LLMs) are good at generating code, but remain brittle for formal verification in systems like Lean4. A core scalability challenge is that verified synthesis requires consistent outputs across multiple artifacts: executable code, precise specifications, theorem statements, and ultimately proofs. Existing approaches rarely treat these as a unified pipeline. We present BRIDGE, a structured prompting framework that decomposes verification into three interconnected domains: Code (implementations), Specifications (formal intent), and Theorem Statements (constructive correctness claims), and elicits domain-specific intermediate reasoning to connect them. In Lean4, BRIDGE often adopts a code-first workflow, using the generated implementation as a semantic anchor for downstream specification and theorem statement generation. Across 178 algorithmic problems and five LLMs, BRIDGE improves Lean executable correctness by nearly 1.5x (pass at 5) over direct baselines and can be 2x more sample-efficient at inference time, requiring fewer samples per verified solution at comparable generation lengths. We further find that specification-driven prompting improves Python pass rates by up to 17.5 percent. Beyond inference-time prompting, supervised fine-tuning on BRIDGE-style reasoning traces yields nearly 1.5x higher Lean pass success than code-only SFT, indicating that these intermediate representations are learnable. BRIDGE provides a practical foundation for scaling verified synthesis and motivates future work on expert iteration and full proof generation.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）在形式化验证（特别是在Lean4这类系统中）生成可验证代码时面临的**可扩展性挑战**。研究背景是，虽然LLM擅长生成代码，但要实现形式化验证，需要确保多个产出物（可执行代码、精确的规范、定理陈述以及最终的证明）之间保持语义一致性，而现有方法很少将它们视为一个统一的流程进行处理。现有方法的不足在于，它们通常直接让模型从自然语言问题描述生成完整的验证工件，这导致模型在生成与证明相关的工件或实现端到端验证时表现不佳，尤其是在需要严格形式化保证的场景下。

因此，本文要解决的核心问题是：**如何通过结构化的方法，引导LLM在代码、规范和定理陈述这三个相互关联的领域中进行领域特定的中间推理，从而系统地提升可验证程序合成的成功率与效率**。论文提出的BRIDGE框架将验证过程分解为上述三个领域，并支持灵活的推理顺序（例如在Lean中常采用“代码优先”的工作流，即以生成的实现作为语义锚点来推导下游的规范和定理），旨在通过领域特定的提示策略，引导模型生成语义一致的中间表示，从而弥合自然语言问题描述与最终可验证工件之间的鸿沟。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为方法类、评测类和系统/理论类。在方法类中，现有工作如CoT、PAL、ReAct等主要关注代码生成或通用推理，而Clover和AutoSpec则分别引入了代码-文档闭环检查或专注于形式化规约合成。本文提出的BRIDGE框架与这些方法的关键区别在于，它首次将代码、规约和定理陈述这三个验证领域的中间表示统一处理，并通过领域特定的结构化推理（Domain-specific CoT）将它们组合起来，旨在解决跨工件的一致性挑战。

在评测类方面，现有基准如DafnyBench、VERINA、CLEVER等分别评估了规约生成、代码+规约+证明等不同方面，但大多未系统性地要求组合多个工件。BRIDGE则在一个框架内同时处理代码生成、规约生成和定理陈述生成，并强调它们之间的组合与连贯性。

从系统与理论背景看，程序验证领域有从Hoare逻辑到依赖类型系统（如Lean）的丰富传统。近期研究指出，LLM在交互式定理证明（如Lean4）中因严格的证明构造要求而表现脆弱。与仅针对孤立任务进行领域微调（如TheoremLlama）的工作不同，BRIDGE直接针对编程范式（如函数式与命令式）带来的可验证性差距，设计了多阶段、领域感知的提示框架，以代码为语义锚点来引导下游规约和定理生成，从而支撑端到端的可验证综合。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为BRIDGE的结构化提示框架来解决大型语言模型在形式化验证（如Lean4中）时输出不一致和脆弱的挑战。其核心方法是将验证过程分解为三个相互关联的领域：代码（实现）、规范（形式化意图）和定理陈述（正确性声明），并通过领域特定的中间推理来连接它们。

整体框架采用一种分步的推理流程。在Lean4的上下文中，BRIDGE通常采用“代码优先”的工作流：首先生成可执行的代码实现，以此作为语义锚点，再引导模型生成下游的精确规范和定理陈述。框架也支持变体，例如首先生成Python中间解决方案并通过测试，再翻译为Lean代码。

主要模块/组件对应于三个领域：
1.  **代码域**：专注于生成能通过编译、终止性检查并提供测试套件的Lean可执行函数。成功标准是代码能具体化（elaborate）、类型检查并通过测试。
2.  **规范域**：引导模型生成形式化规约（如前置/后置条件），作为连接问题描述和可证明实现的桥梁。这些规范需要在Lean中语法有效、非空泛，并且实现能通过测试。
3.  **定理陈述域**：将定理发现作为一个显式的推理步骤，引导模型提出有实质意义的性质（如边界、不变量、单调性），形成类型检查正确的定理陈述，为最终证明奠定基础。

关键技术在于**领域特定提示**。BRIDGE不是直接生成最终产物，而是通过精心设计的提示模板，引导模型为每个领域产出结构化的中间推理表示。这些表示充当了检查点，使得可以通过跨领域的一致性（而非孤立的准确性）来评估和精炼输出。例如，在生成代码前先推理函数契约，或在实现后推理需要证明的数学性质。

创新点主要体现在：
1.  **统一管道**：将代码、规范和定理陈述的生成视为一个整体推理过程，而非孤立任务，强调它们之间的语义一致性。
2.  **中间表示作为语义桥梁**：提出并利用领域特定的中间推理表示（如功能式推理、规约导向推理、定理驱动推理）来对齐LLM的内部知识结构与证明助理所期望的逻辑抽象。
3.  **灵活的工作流与评估**：支持以代码或规范为起点的不同工作流，并为每个领域定义了明确的、可度量的成功标准。
4.  **可学习性验证**：实验表明，基于BRIDGE风格推理轨迹进行监督微调，其效果显著优于仅基于代码的微调，证明了这些中间表示可以被模型有效学习。

### Q4: 论文做了哪些实验？

论文在178个算法问题上进行了实验，这些问题来自LeetCode和各类编程竞赛，涵盖数组、字符串、图、动态规划、数值算法和树等多种类型。实验设置包括使用五个先进的大语言模型（Claude Sonnet 4、DeepSeek Coder V2、DeepSeek R1、Llama-3.1-70B和Qwen2.5 Coder），解码参数统一为温度0.7和最大输出token数4096。评估时，每个任务生成k个独立样本，若至少有一个样本能通过100个测试用例的Lean代码功能正确性验证，则记为pass@k成功。此外，实验还设置了最多3轮的修复机制。

对比方法主要围绕BRIDGE框架的三个领域展开：在代码领域，比较了直接生成Lean代码与使用不同编程范式（如函数式语言Haskell/OCaml和命令式语言Python/C++/Java）作为中间推理策略的效果；在规约领域，探索了多种框架（如契约设计、基于属性的测试等）来生成Lean规约；在定理陈述领域，则评估了生成语义合理定理语句的能力。

主要结果如下：函数式推理范式在生成正确Lean代码方面显著优于命令式方法和直接生成。例如，Claude Sonnet 4使用函数式提示的pass@5成功率达到48.9%，而命令式提示为44.9%，直接生成加3轮修复和API辅助为42.1%。函数式推理的样本效率最高可达2倍，即在相同生成长度下，获得一个正确Lean解决方案所需的生成样本数约为直接基线的一半。关键数据指标包括：函数式提示将语法错误从45%降至12%，终止失败从15%降至8%。在监督微调实验中，使用BRIDGE风格推理轨迹进行微调，其Lean通过率（8.5%）比仅使用代码微调（5.6%）高出近1.5倍。此外，规约驱动的提示也提升了Python代码生成通过率，其中DeepSeek-R1提升最大，达17.5个百分点（从57.9%到68.0%）。

### Q5: 有什么可以进一步探索的点？

该论文的BRIDGE框架虽在提升形式化验证成功率上表现显著，但仍存在若干局限与可拓展方向。首先，其当前工作流主要基于“代码优先”模式，这可能导致当初始代码存在语义偏差时，后续规范与定理生成累积错误。未来可探索“规范优先”或动态自适应的工作流，根据问题类型选择最优路径。其次，BRIDGE依赖人工设计的领域划分（代码、规范、定理），未来可研究如何让模型自动学习或优化领域结构，甚至引入更多中间表示（如测试用例、不变量）。此外，框架目前侧重于生成定理陈述，而非完整证明；结合专家迭代（expert iteration）或交互式证明助理进行闭环反馈，将是实现端到端验证合成的关键。从学习角度看，论文已证明基于BRIDGE轨迹的监督微调有效，但可进一步探索强化学习或课程学习，使模型能自主优化推理链。最后，将BRIDGE扩展到更复杂的验证场景（如并发程序、硬件设计）及更多形式化系统（如Coq、Isabelle），是验证其通用性的重要步骤。

### Q6: 总结一下论文的主要内容

这篇论文提出了BRIDGE框架，旨在解决大语言模型在形式化验证系统（如Lean4）中生成可验证代码的难题。核心问题是，可验证的合成需要确保代码、规范、定理陈述和证明等多个输出的一致性，而现有方法很少将其视为统一流程。BRIDGE通过结构化提示，将验证分解为三个相互关联的领域：代码（实现）、规范（形式化意图）和定理陈述（构造性正确性声明），并引导模型进行领域特定的中间推理来连接它们。在Lean4中，该方法常采用“代码优先”工作流，以生成的实现作为语义锚点，驱动后续规范和定理陈述的生成。实验表明，在178个算法问题和五个大语言模型上，BRIDGE将Lean可执行代码的正确率提升了近1.5倍，且在推理时样本效率可提高2倍。此外，规范驱动的提示也将Python通过率提升高达17.5%。监督微调实验进一步证明，基于BRIDGE推理轨迹的训练比仅基于代码的训练效果提升近1.5倍，说明这些中间表示是可学习的。BRIDGE为扩展可验证合成提供了实用基础，并推动了在专家迭代和完整证明生成方面的未来工作。
