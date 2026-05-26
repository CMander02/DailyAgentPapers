---
title: "Reflect-Guard: Enhancing LLM Safeguards against Adversarial Prompts via Logical Self-Reflection"
authors:
  - "Lixing Lin"
  - "Juli You"
  - "Yue Li"
  - "Luyun Lin"
  - "Yiqing Wang"
  - "Zhen Zhang"
  - "Moxuan Zheng"
date: "2026-05-24"
arxiv_id: "2605.24834"
arxiv_url: "https://arxiv.org/abs/2605.24834"
pdf_url: "https://arxiv.org/pdf/2605.24834v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "LLM安全"
  - "对抗性提示"
  - "自我反思"
  - "参数高效微调"
  - "安全分类器"
  - "链式思维推理"
relevance_score: 7.5
---

# Reflect-Guard: Enhancing LLM Safeguards against Adversarial Prompts via Logical Self-Reflection

## 原始摘要

Large language model (LLM) safety classifiers such as Llama Guard are effective at detecting overtly harmful prompts but remain vulnerable to adversarial jailbreak attacks that disguise malicious intent through role-play scenarios, fictional framing, and indirect requests. We present Reflect-Guard, a method that augments LLM-based safety classifiers with chain-of-thought self-reflection capabilities through parameter-efficient fine-tuning. Our approach distills analytical reasoning from GPT-4o-mini into structured reflection annotations, then trains Llama-Guard-3-8B via QLoRA to generate logical self-reflections before issuing safety verdicts. Using only 1000 training examples and updating just 0.5% of model parameters (~42M), Reflect-Guard achieves substantial improvements on two challenging benchmarks. On WildGuardTest, F1 score improves from 0.770 to 0.842 (+7.2 pp), with recall on adversarial prompts increasing from 0.513 to 0.921 (+40.8 pp). On JailbreakBench, the attack success rate drops from 10.3% to 1.8%, representing an 82.5% relative reduction. These gains are especially pronounced on adversarial inputs, where the explicit reasoning step enables the model to see through obfuscation techniques that defeat standard pattern-matching approaches. Our results demonstrate that teaching safety classifiers to reason about adversarial intent, rather than simply classify surface patterns, is a promising direction for robust LLM safety.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）安全分类器在面对对抗性越狱攻击时表现脆弱的问题。当前的安全分类器，如Meta的Llama Guard系列，在检测直接有害的提示（prompt）方面表现良好，但容易被对抗性越狱攻击绕过。这些攻击通过将恶意请求包装在看似无害的上下文中，如虚构故事、角色扮演场景、假设性研究问题或教育性框架，来掩盖其真实意图，从而规避依赖表面语义匹配的安全过滤器。现有方法的根本不足在于其缺乏对对抗性意图的显式推理能力，只能进行基于模式匹配的二元分类，导致在检测精心伪装的提示时效果不佳。例如，Llama-Guard-3-8B在WildGuardTest数据集上对抗性子集的召回率仅为51.3%，几乎漏掉了一半的伪装有害提示。本文提出的核心解决方案是Reflect-Guard，一种通过知识蒸馏和参数高效微调，赋予安全分类器链式思维（CoT）自反思能力的方法。该方法通过让模型在输出安全判定前，先进行结构化逻辑反思，分析对抗性技术和危害指标，从而识破那些欺骗标准模式匹配方法的混淆技术，显著提升对对抗性提示的检测性能。

### Q2: 有哪些相关研究？

相关研究可分为四类：

1. **LLM安全分类器**：包括Llama Guard系列（版本1-3，利用可定制分类法进行内容审核）、WildGuard（通过对抗样本训练提升鲁棒性）、PromptGuard（注入检测）、ShieldGemma以及面向智能体的AgentAuditor。本文与之区别在于，现有分类器均未在分类前显式推理对抗意图，而Reflect-Guard通过自反思引入推理步骤。

2. **越狱攻击方法**：包括梯度方法GCG、语义方法PAIR/TAP（用LLM迭代优化提示）、混合方法AutoDAN、模板攻击（角色扮演/虚构框架）以及JailbreakBench标准化框架。本文专注于防御这类攻击，通过逻辑自反思看穿伪装手法。

3. **思维链推理用于安全**：前人工作将CoT用于内容审核、有害内容检测（如deliberative alignment）、宪法AI的自我批评。本文区别在于将结构化的安全反思蒸馏为轻量LoRA适配器，无需多轮提示或大型教师模型，实现高效部署。

4. **知识蒸馏用于安全**：有工作从大模型蒸馏安全行为。本文特化于蒸馏分析推理模式而非输出分布，教导学生模型推理对抗技术，而非简单匹配表面模式。

### Q3: 论文如何解决这个问题？

Reflect-Guard 通过引入逻辑自反思机制来增强LLM安全分类器的对抗性鲁棒性。核心方法是将分类过程分解为两步：首先生成结构化反思分析，然后基于反思输出安全裁决。整体框架包含训练和推理两个阶段。

训练阶段：使用GPT-4o-mini作为教师模型，从WildGuardMix和AdvBench中精选1000个标注样本，生成2-4句结构化反思注释，识别对抗技巧（如角色扮演、虚构场景）、判断意图并列出关键指标。每条训练数据按Llama Guard 3模板格式化为对话，包含安全指令、用户提示、反思标签和裁决。使用QLoRA在4-bit NF4量化下对Llama-Guard-3-8B进行参数高效微调，仅更新42M参数（0.5%）。LoRA适配器应用于所有线性投影层，秩r=16，使用paged AdamW优化器，学习率2e-4，训练3个epoch，约1小时完成。

推理阶段：微调模型接收相同格式的提示，自回归生成：先输出<reflection>标签内的反思分析，再输出安全裁决（safe/unsafe）及违禁类别。采用贪心解码，最大150 tokens，无需外部API调用，反思能力完全内化在LoRA适配器中，仅增加约50-100 tokens的生成开销。

关键技术在于将安全分类分解为条件概率pθ(r|x)pθ(y|x,r)，使反思成为模型生成的潜在推理过程，显式指导下游决策，让模型能够穿透对抗性混淆技术。在WildGuardTest上F1提升7.2个百分点，对抗性提示召回率从0.513提升至0.921；在JailbreakBench上攻击成功率从10.3%降至1.8%。

### Q4: 论文做了哪些实验？

论文在WildGuardTest和JailbreakBench两个基准上评估了Reflect-Guard。WildGuardTest包含1,699条提示（754条有害，945条无害），其中796条为对抗性提示。Llama-Guard-3-8B作为基线进行对比。主要结果：在WildGuardTest上，F1分数从0.770提升至0.842（+7.2pp），召回率从0.663提升至0.863（+20.0pp）。在对抗性子集上，召回率从0.513大幅提升至0.921（+40.8pp），F1从0.639提升至0.802。在JailbreakBench上，该基准包含282条由GCG、JBC和PAIR三种攻击生成的对抗提示，Reflect-Guard将总体攻击成功率从10.3%降至1.8%（相对降低82.5%）。具体来说，PAIR攻击的检测率从75.6%提升至95.1%（+19.5pp），GCG攻击从93%提升至99%，JBC攻击达到100%。实验还分析了三类案例：反射机制成功捕捉而SFT失败的29例（其中27例为对抗性）、反射机制导致的109例误报（多为角色扮演形式），以及所有方法均失败的78例（集中在隐私和社会刻板印象类别，表明训练数据覆盖不足）。这些结果表明，通过逻辑自反思精调，模型在对抗性提示上的检测能力获得显著提升。

### Q5: 有什么可以进一步探索的点？

论文存在几个值得深入探索的方向。首先，模型在安全相关但无害的提示上产生了大量误报（109个新误报），可以采用置信度阈值判断、级联二次分类器或人工审核边界案例来缓解。其次，训练数据仅覆盖1000个示例，未能涵盖新颖的对抗攻击变体，未来应构建更全面、多样化的对抗样本训练集。第三，反射注释由GPT-4o-mini生成，存在教师偏差转移风险，可以比较不同教师模型（如GPT-4、Claude-3）并测试方法的通用性。最关键的是多语言和跨文化泛化问题：当前仅处理英语，而非英语的对抗模式、文化特定伤害类别（如政治言论、宗教批判）和跨语言攻击技术（如代码切换）都未被覆盖。未来应使用多语言教师生成反射训练数据，扩展安全分类法，并在多语言基准上评估。此外，可以通过探索更高效的推理路径（如压缩反射长度）或动态学习是否生成反射来降低推理开销。

### Q6: 总结一下论文的主要内容

Reflect-Guard是一种增强LLM安全分类器的方法，针对对抗性越狱攻击（如角色扮演、虚构框架和间接请求）伪装恶意意图的问题。该方法通过参数高效微调，将GPT-4o-mini的分析推理能力蒸馏到Llama-Guard-3-8B模型中，使其在给出安全判定前先生成逻辑自反思。仅用1000个训练样本和更新0.5%的模型参数（约42M），Reflect-Guard在两个基准测试上取得显著提升：WildGuardTest的F1分数从0.770提升至0.842，对抗性输入的召回率从0.513提升至0.921；JailbreakBench的攻击成功率从10.3%降至1.8%。消融实验表明，反思训练能专门将性能分配到对抗性输入上。核心贡献在于教会安全分类器推理对抗意图而非简单匹配表面模式，为鲁棒且可解释的LLM安全分类提供了新范式。
