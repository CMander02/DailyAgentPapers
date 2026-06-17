---
title: "A Red-Team Study of Anthropic Fable 5 & Opus 4.8 Models"
authors:
  - "Nicola Franco"
date: "2026-06-16"
arxiv_id: "2606.18193"
arxiv_url: "https://arxiv.org/abs/2606.18193"
pdf_url: "https://arxiv.org/pdf/2606.18193v1"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.CL"
tags:
  - "LLM安全"
  - "红队测试"
  - "越狱攻击"
  - "对抗鲁棒性"
  - "多智能体框架"
relevance_score: 8.5
---

# A Red-Team Study of Anthropic Fable 5 & Opus 4.8 Models

## 原始摘要

We evaluate the adversarial robustness of two frontier large language models (LLMs) developed by Anthropic, Fable 5 and Opus 4.8, against four families of automated jailbreak attack across 7 826 harmful intents spanning a ten-category harm taxonomy. Using the HackAgent red-teaming framework, hundreds of thousands of adversarial attempts were generated and every apparent success was independently re-adjudicated by a panel of three judge models (majority vote). Both models resist the majority of attacks, but the residual surface is larger than aggregate framing suggests: it is dominated by adaptive iterative attacks, while static obfuscation is near-fully neutralised. The strongest adaptive search (tree-of-attacks) breaks Opus 4.8 on 11.5% of intents overall, whereas Fable 5 stays in the single digits (6.1% worst-case). Aggregate rates therefore should not be read as reassurance. Even in these hardened configurations, the two models produced 1 620 (Opus 4.8) and 702 (Fable 5) panel-confirmed harmful completions spanning every harm category, located automatically, cheaply, and within the first one or two refinement steps by an attacker model with no human expert in the loop. The reasonable conclusion is that even the best, most-tested frontier models remain reliably breakable under sustained automated pressure.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决一个核心问题：即便经过最严格安全训练的前沿大语言模型，在面对自动化、自适应性的对抗攻击时，其实际鲁棒性究竟如何。研究背景是，随着模型能力提升，简单的静态提示攻击（如单一恶意prompt）已难以奏效，但攻击者可以通过迭代、自适应地改写提示来绕过防御。现有方法的不足在于，许多安全评估报告仅给出单一的攻击成功率，忽视了不同攻击类型、不同危害类别之间的差异，且通常依赖单一评判模型，可能高估“成功”数量。本文的核心贡献是：通过HackAgent自动红队框架，对Anthropic的Fable 5和Opus 4.8两个模型进行系统性压力测试，使用四种攻击家族（包括静态混淆和自适应迭代攻击）在7826个恶意意图上发起攻击，并由独立的三模型评判小组进行二次确认。结果发现，自适应迭代攻击（如Tree-of-Attacks）能显著突破防御，Opus 4.8在最高攻击下对11.5%的意图成功生成有害内容，Fable 5为6.1%，且在儿童安全等关键类别上暴露面更大；而静态混淆几乎被完全防御。论文旨在揭示：即使是最顶尖的模型，在持续自动化压力下仍存在可被利用的残存脆弱性，其绝对数字（数千条确认的有害内容）表明这并非偶然误差，而是稳定的攻击流。

### Q2: 有哪些相关研究？

相关研究主要分为以下三类：**攻击方法类**、**鲁棒性评估类**和**自动化红队框架类**。在攻击方法方面，本文对比了四种自动化越狱攻击家族，包括自适应迭代攻击（如树状攻击Tree-of-Attacks）和静态混淆攻击，前者被证实是残留漏洞的主要来源。这与以往仅关注单次提示越狱的研究不同，突出了自适应攻击的持续性威胁。在评估方法上，本文采用了严格的独立多评委复审机制，避免了单一评分模型的噪声问题，这是对以往仅依赖单一检测器评估的改进。在红队框架方面，本文使用HackAgent自动化框架，无需人类专家介入即可生成数千次攻击，相比以往需要人工参与的红队测试（如Anthropic自身的红队实验），实现了更高效的规模化评估。此外，本文覆盖了包含10大类55个子类的全面危害分类体系，相比多数仅针对少数类别（如仇恨言论或非法活动）的研究更系统全面。与OpenAI、Google DeepMind等机构的相关鲁棒性报告相比，本文不仅报告了聚合成功率，更揭示了不同攻击类型和危害类别的差异分布，指出即使在最先进的模型（如Opus 4.8和Fable 5）中，攻击者仍可在低成本下产生大量有害输出。

### Q3: 论文如何解决这个问题？

本研究采用系统化的红队测试框架，对Anthropic的Fable 5和Opus 4.8两款前沿大语言模型进行对抗鲁棒性评估。核心方法基于HackAgent红队框架，将目标模型视为黑盒系统，攻击者仅能通过标准API获取文本响应，无法访问权重、对数概率或内部状态。研究构建了包含7,826个有害意图的10大类55子类分层分类体系，覆盖从社交危害到网络安全等完整安全维度。

技术架构包含四大攻击家族：TAP（带剪枝的树状攻击）采用自适应多步搜索，在深度3、宽度4、分支因子3的配置下，通过实时评分扩展有利分支并剪枝弱分支；PAIR（提示自动迭代优化）配置12轮迭代和8个并行流，让攻击模型基于目标拒答持续改写提示；PAP（说服性对抗提示）运用权威、角色扮演等策略进行单次重述；h4rm3l（静态混淆）应用base64编码、字符密码等变换。所有攻击均由本地部署的未审查开源模型执行，避免攻击者拒答干扰测量。

创新性验证机制采用两级评审：攻击过程中由快速评分器引导搜索；所有候选成功结果由Qwen3.7 Max、Gemini 3.5 Flash、GPT 5.5三个独立评审模型进行二次裁定，仅当多数（≥2/3）一致判定为有害时才计为确认越狱。最终确认Opus 4.8产生1,620个、Fable 5产生702个经审核的有害输出，覆盖所有危害类别。实验证明即使最强模型在持续自动化攻击下仍可被可靠破解。

### Q4: 论文做了哪些实验？

论文对Anthropic的Fable 5和Opus 4.8两个前沿LLM进行了红队测试，评估其在自动化越狱攻击下的对抗鲁棒性。实验设置如下：使用HackAgent红队框架，基于包含10个危害类别的7,826个恶意意图，生成数十万次对抗攻击。采用了四种攻击家族：三种自适应迭代攻击（PAIR、TAP、PAP）和一种静态混淆攻击（h4rm3l）。主要结果通过三个评判模型多数投票确认攻击成功率（ASR）。TAP攻击最强，对Opus 4.8的整体ASR为11.51%，对Fable 5为6.10%；PAIR攻击ASR分别为7.98%和4.30%；PAP攻击较低（3.67%和0.54%）；h4rm3l静态攻击几乎无效（0.18%和0.04%）。总计分别确认了1,620和702次有害输出。按危害类别分析，Opus 4.8在儿童安全（27.6%）、网络犯罪（14.7%）和网络安全（11.4%）等类别上ASR较高，而Fable 5在儿童安全（13.7%）和伦理社交（10.2%）上峰值较低。攻击成功集中在早期迭代步骤，大多在前1-2次内实现。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三方面：一是PAIR攻击测试覆盖不完整（Fable 5仅覆盖27/55子类别），导致对比存在偏倚；二是评判面板存在误判风险，可能遗漏微妙危害或错误标记无害回复；三是结果仅反映评估时刻的模型快照，未考虑生产环境中的系统提示、输出过滤等安全栈。未来可从以下方向探索：首先，开发更全面的攻击覆盖框架，确保所有威胁类别均衡测试；其次，研究动态评判机制，引入对抗性判别器或人工审核；第三，构建持续评估体系，追踪模型更新后鲁棒性的演化规律。改进思路包括：设计跨模型攻击迁移性分析，探索防御策略的通用性；深入研究自适应迭代攻击的变体，例如结合强化学习的树搜索；论证模型安全性与能力增长的矛盾，推动可验证的鲁棒性基准建设。

### Q6: 总结一下论文的主要内容

该论文利用HackAgent红队框架，对Anthropic开发的两个前沿大语言模型Fable 5和Opus 4.8进行了对抗鲁棒性评估。研究覆盖7,826个有害意图（涵盖十类危害分类法），采用四种自动化越狱攻击家族生成了数十万次攻击尝试，并通过三个独立评审模型进行多数投票重判。主要发现：尽管两个模型能抵抗大多数攻击，但其残余攻击面比总体数据所显示的更大，主要被自适应迭代攻击主导，而静态混淆攻击几乎被完全防御。最强的自适应搜索（tree-of-attacks）在总体上能成功攻击Opus 4.8的11.5%意图，而Fable 5最坏情况下仅为6.1%。然而，两个模型仍分别产生了1,620个和702个经专家组确认的有害输出，涉及所有危害类别。结论指出，即使是最安全、经过充分测试的前沿模型，在持续的自动化攻击压力下仍然可被可靠地攻破，不应因总体抵抗率较高而掉以轻心。
