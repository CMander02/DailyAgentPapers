---
title: "PersonaArena: Dynamic Simulation for Evaluating and Enhancing Persona-Level Role-Playing in Large Language Models"
authors:
  - "Wenlong Shi"
  - "Jianxun Lian"
  - "Mingqi Wu"
  - "Haiming Qin"
  - "Mingyang Zhou"
  - "Xing Xie"
  - "Naipeng Chao"
  - "Hao Liao"
date: "2026-05-16"
arxiv_id: "2605.17044"
arxiv_url: "https://arxiv.org/abs/2605.17044"
pdf_url: "https://arxiv.org/pdf/2605.17044v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "角色扮演"
  - "动态模拟"
  - "多智能体评测"
  - "社交智能体"
relevance_score: 8.5
---

# PersonaArena: Dynamic Simulation for Evaluating and Enhancing Persona-Level Role-Playing in Large Language Models

## 原始摘要

Large language models (LLMs) increasingly serve as interactive social agents, yet their ability to maintain coherent and authentic persona-level role-playing remains limited, particularly in realistic social scenarios. Existing research predominantly focuses on character-level settings and relies on static evaluation formats, failing to capture the complexity of everyday social interactions. In this work, we present PersonaArena, a dynamic simulation framework for evaluating and improving persona-level role-playing in LLMs. PersonaArena leverages a large, filtered corpus of user-generated social content to construct a nuanced persona bank, and elicits multi-turn, context-rich interactions within simulated social environments. Our framework features a multi-agent debating judge for holistic and unbiased assessment. Through extensive experiments, we demonstrate that PersonaArena enables rigorous evaluation and enhancement of LLMs' role-playing capabilities, advancing the development of more authentic and socially adept AI agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决大型语言模型（LLM）在角色扮演能力评估与提升方面存在的三大核心问题。研究背景在于，LLM 正被越来越多地用作社交智能体，但其维持一致且真实的角色扮演能力，尤其是在日常社交场景中，仍存在显著局限。现有方法的不足主要体现在三个方面：第一，现有研究主要聚焦于基于知名角色的“角色级”扮演，这类角色通常存在于流行文化中，LLM 可能仅是记忆而非真正推理，且角色行为往往被夸大或理想化，偏离了普通人的日常行为模式。第二，用于训练和评估的对话数据存在局限性，早期数据集如 Persona-Chat 依赖于众包工人模拟他人性格，但非专业演员难以保证行为与角色真实一致。第三，评估方法不充分，现有评估多依赖 hit@k、困惑度（perplexity）或 BLEU 等表面指标，或仅关注单一维度（如忠实度），忽略了对角色一致性、适应性的全面评估；且评估形式多为静态的问答对，而非开放式的多轮对话，无法捕捉真实社交中角色自然浮现的复杂性。因此，本文要解决的核心问题是：如何构建一个能够动态模拟真实社交交互、提供真实细致角色库，并对 LLM 的角色扮演忠实度、一致性和适应性进行全面、公正评估的框架，以系统性地评估与增强 LLM 的日常社交角色扮演能力。

### Q2: 有哪些相关研究？

相关研究主要分为三类。首先是**角色级角色扮演**，如ChatHaruhi、Character-LLM和CharacterGLM，它们专注于拟真特定虚构或历史人物，但角色特质常被夸大，与现实人物有差距。评测基准如RoleLLM的RoleBench、CharacterEval、InCharacter和SocialBench，虽提升了评估粒度，但多采用静态格式，缺乏动态社交互动。与此不同，PersonaArena聚焦更广泛的“人格级”角色，旨在捕捉真实社会动态。

其次是**人格级角色扮演**，以Persona-Chat、Synthetic-Persona-Chat和Persona Hub为代表，强调基于职业、价值观等持久特质构建通用社交原型，而非固定身份。DMT-RoleBench等进一步引入动态意图驱动评估。这些工作关注人格忠实性，但评估环境仍偏静态或简单。PersonaArena则通过动态仿真环境，模拟多轮、上下文丰富的交互，弥补了这一不足。

最后是**应用与工具类**，如TinyTroupe和AgentSociety，它们利用人格驱动代理进行大规模社会模拟，但缺乏对交互式社会角色扮演能力的可靠评估。PersonaArena正是填补了这一空白，通过其多智能体辩论裁判实现全面、无偏的评估，从而系统提升LLM在现实社会互动中的角色扮演能力。

### Q3: 论文如何解决这个问题？

PersonaArena通过一个动态多智能体仿真框架来评估和增强大语言模型的角色扮演能力。整体架构包含三大核心组件：角色库、场景设置和评估引擎。

首先，角色库从博客作者数据集中提取1000个真实用户画像，经LLM处理生成包含人口统计、职业、性格、价值观、兴趣和经历的六维结构化角色描述。其次，场景设置模块由环境代理自动构建反映角色特征的社会场景，包括事件描述、时空语境、一个主角和2-3个NPC。

关键技术在于多智能体仿真机制：主角代理采用信念-欲望-意图(BDI)结构，具备目标导向推理和向量记忆检索能力，能动态更新自我信念和环境信念；NPC代理由固定高能力LLM驱动，保持行为稳定性。环境代理作为全局控制器，负责交互分析、自适应轮次控制、角色状态更新和环境同步，其中自适应轮次控制通过五维检查点（背景、性格、价值观、兴趣、经历）监控主角表现程度，实现早停机制。

评估阶段采用多智能体辩论法官系统：K个独立LLM法官对八个维度（包括新增的交互丰富度）打分，当出现重大分歧时启动辩论仲裁，由仲裁模型综合各法官的评分、理由和证据后给出最终裁决。

此外，PersonaArena还利用高质量仿真轨迹进行模型增强，通过监督微调(SFT)让模型模仿专家行为模式，或通过直接偏好优化(DPO)在高低质量轨迹对上进行偏好学习，从而提升角色扮演能力。

### Q4: 论文做了哪些实验？

论文进行了全面的实验评估。实验设置包括：从包含1,000个用户画像的画像库中随机采样10个画像，在模拟环境中进行多轮互动。评估模型涵盖闭源模型（GPT-5.1、GPT-4.1、GPT-4o系列、Grok-3）和开源模型（Qwen3系列、Mistral-Small-3.2-24B、Llama3系列、Phi-4、DeepSeek-R1/V3.2等）。采用多智能体辩论裁判框架（DeepSeek-R1、Qwen3-32B、Mistral-small3.2作为法官，GPT-4o-mini作为仲裁者），在8个维度进行评估。

主要结果：GPT-5.1取得最高整体性能，DeepSeek-V3.2在开源模型中表现最佳，Qwen3系列呈现清晰缩放规律。多裁判框架与人类评价的皮尔逊相关系数达0.683，优于单裁判设置。通过SFT和DPO微调Qwen3-8B，SFT提升21.96%，DPO进一步提升5.21%，在IR、BA、AD等维度显著改进，DPO-Qwen3-8B在6个维度超越GPT-4.1。NPC模型鲁棒性实验表明，替换NPC为GPT-4.1后性能曲线高度一致，验证了框架的稳定性。

### Q5: 有什么可以进一步探索的点？

首先，论文中采用的多法官辩论评估虽能部分缓解个体偏见，但本质上仍受限于LLM自身的模型偏差，无法完全替代人类判断的细致与准确性。未来可探索引入更多样化的评审模型，或采用混合人机评估机制以提升评价的鲁棒性。其次，研究当前聚焦于技术层面的角色一致性，未深入探讨模拟有害或反社会角色的伦理边界。如何安全地赋予模型模拟“邪恶”角色的能力，需要结合社会学与安全研究，构建合理的规范框架与防护机制。此外，驱动场景的NPC模型选择对评估结果有显著影响，不同架构和训练数据的NPC可能带来偏差，需系统研究NPC配置对模拟多样性与公平性的影响。最后，基于用户生成内容构建的角色库可能存在人口、文化或平台层面的偏见，限制了角色的代表性和泛化能力。未来可拓展数据源多样性，并开展系统性偏见审计，以提升框架的公平性与包容性，从而更真实地反映社会互动复杂性。

### Q6: 总结一下论文的主要内容

PersonaArena提出了一个动态模拟框架，用于评估和增强大语言模型在人格层面角色扮演的能力。现有研究多聚焦于“角色”层面（如小说人物），依赖静态问答评估，难以捕捉日常社交互动的复杂性。该框架的核心贡献在于：从大规模用户生成内容中构建了一个包含1000个精细人格档案库，并设计了由环境智能体和NPC组成的社交模拟环境，以引发多轮、上下文丰富的交互。为了进行公正全面的评估，论文引入了一个多智能体辩论评判机制，从人格一致性、连贯性和适应性等维度进行衡量。实验表明，PersonaArena能有效评估LLM的角色扮演质量，并且框架生成的数据可用于后期训练，进一步提升模型的人格一致性和真实感。这项工作为开发更真实、更具社交能力的AI智能体奠定了基础，并推动了动态、上下文驱动的评估与训练方法研究。
