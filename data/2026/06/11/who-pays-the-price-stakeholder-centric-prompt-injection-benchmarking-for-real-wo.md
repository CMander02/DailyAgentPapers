---
title: "Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents"
authors:
  - "Zihao Wang"
  - "Yiming Li"
  - "Yutong Wu"
  - "Zheyu Liu"
  - "Kangjie Chen"
  - "Fok Kar Wai"
  - "Pin-Yu Chen"
  - "Vrizlynn L. L. Thing"
  - "Bo Li"
  - "Dacheng Tao"
  - "Tianwei Zhang"
date: "2026-06-11"
arxiv_id: "2606.13385"
arxiv_url: "https://arxiv.org/abs/2606.13385"
pdf_url: "https://arxiv.org/pdf/2606.13385v1"
github_url: "https://github.com/StakeBench/SBC"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.CY"
  - "cs.HC"
  - "cs.MM"
tags:
  - "多利益相关者基准"
  - "提示注入攻击"
  - "LLM驱动的Web Agent"
  - "安全评估"
  - "Agent漏洞分析"
relevance_score: 9.0
---

# Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents

## 原始摘要

Web agents driven by large language models (LLMs) are increasingly deployed in real-world environments, where they operate over untrusted web content and execute actions with direct consequences. This makes them vulnerable to prompt-injection attacks, in which seemingly benign content embeds adversarial instructions that manipulate agent behaviour. Existing security benchmarks adopt an \textit{attack-centric} perspective, focusing on the technical feasibility of injections while overlooking the nuanced distribution of resulting harms. In practice, however, prompt-injection risk is victim-dependent: a single exploit can produce asymmetric consequences for different stakeholders, and the same attack pattern may exhibit substantially different effectiveness depending on whom it targets. To capture these properties, we introduce \textbf{\sysname}, a \textit{stakeholder-centric} benchmark to systematically categorize and attribute harm in real-world web agent systems. It distinguishes between affected entities (e.g., user, seller, platform), decomposes the attacks into concrete objectives, and evaluates each case with complementary outcome- and process-level metrics. Our results reveal substantial and heterogeneous vulnerabilities: not a single attack objective is reliably resisted by current agents, and failures distribute across qualitatively distinct modes ranging from \emph{stealthy parasitism} (attack succeeds without disrupting the user's delegated task) to \emph{misaligned disruption} (task disrupted without attack success) and \emph{compounded failure} (both adversarial objective and task integrity simultaneously violated). These patterns are missed by conventional evaluation, highlighting the need for stakeholder-aware assessment of LLM-based agents in real-world deployments. Benchmark is available at https://github.com/StakeBench/SBC.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决基于大语言模型（LLM）的网页智能体在真实部署环境中面临提示注入攻击时，现有评估方法忽视受害者异质性和多利益相关者不对称危害的问题。研究背景方面，LLM驱动的网页代理正被部署于电子商务等用户面对场景，它们直接在不可信网页内容上操作并执行有后果的动作（如购买、泄露信息），因此极易受到提示注入攻击——恶意指令可隐藏于产品评论等看似无害的内容中。现有方法的不足在于采用“攻击中心”视角，仅关注注入的技术可行性（如攻击成功率），而忽略了危害分布的关键属性：（1）危害因受害者而异且不对称，一次攻击可能对不同利益相关者（用户、卖家、平台）造成截然不同的后果（如偏向某商品虽不破坏用户任务，但损害卖家并破坏平台公正）；（2）相同攻击模式对不同受害者效果不同，漏洞表现高度依赖受害者身份；（3）存在由对齐程度驱动的异质性失败模式，如“隐蔽寄生”（攻击成功但用户任务未中断）和“错位中断”（攻击未成功但用户任务被破坏）。本文核心问题是：超越攻击成功率等粗粒度指标，提出以受害者为中心（stakeholder-centric）的基准测试框架，系统分类和归因提示注入对用户、卖家、平台等不同利益相关者的实际危害，并揭示当前智能体在面对不同利益相关者时表现出不对称、多模态的脆弱性，从而为真实部署中LLM智能体的安全性评估提供利益相关者感知的工具。

### Q2: 有哪些相关研究？

相关研究主要分为三类：评估类、安全风险类和系统行为分析类。评估类方面，**INJECAGENT** 提供了对工具集成代理 IPI 的早期评估，**AgentDojo** 引入了基于现实任务的动态有状态环境，**WASP** 强调受限攻击者能力下的 Web 代理安全。本文与它们的区别在于，这些基准采用“攻击中心”视角，按场景或机制分类威胁并用聚合指标评估，忽略了受害者异质性。安全风险类方面，**OS-HARM** 和 **AGENTDAM** 扩展了相邻安全与隐私风险的评估，包含更丰富的执行级测量。本文进一步引入“利益相关者中心”视角，区分用户、卖家、平台等受影响的实体，分解攻击为具体目标，并用结果与过程指标评估，从而揭示传统方法无法捕捉的异质性漏洞（如隐蔽寄生、错位干扰、复合故障）。系统行为分析类方面，现有工作关注工具集成或内存设计，而本文强调 Web 代理作为集成系统（包括 LLM、规划、工具、内存和浏览器接口），其行为由交互产生，并重点分析不同利益相关者下的脆弱性模式差异。本文通过统一框架系统研究不对称风险和受害者相关漏洞，补充了现有研究的空白。

### Q3: 论文如何解决这个问题？

StakeBench 通过构建一个以利益相关者为中心的基准测试框架来系统评估真实世界网页智能体面临的提示注入攻击风险。其核心设计围绕三个维度展开：多主体环境、现实威胁模型和利益相关者导向的攻击分类法。

首先，框架基于VisualWebArena的OneStopMarket电商平台构建交互环境，明确界定三类利益相关者：用户（承担任务委托方）、第三方卖家（内容与服务提供方）和平台（基础设施提供方）。攻击的分类不再按场景划分，而是根据受害实体组织，形成实体中心化的伤害建模。其次，威胁模型假设攻击者仅能控制用户评论、评分等自然内容表面，无法修改系统提示或基础设施，区分了间接提示注入（IPI，将恶意内容嵌入运行时环境）和直接提示注入（DPI，注入到主输入上下文）两种通道。攻击模板库包含22个模板（9个DPI、13个IPI），覆盖12个具体对抗目标，跨12个产品类别实例化后得到264个可执行案例。

关键创新点在于三维评估指标：攻击成功率（ASR）衡量对抗目标是否达成，任务偏离率（TDR）评估用户委托任务是否受干扰，行为异常率（BIR）捕获执行过程中的病理模式（如循环、导航不稳定）。ASR与TDR的联合分析定义了四个失效模式：稳健行为（双低）、隐蔽寄生（高ASR低TDR，攻击成功而未中断任务）、错位干扰（低ASR高TDR，攻击失败但任务受损）和复合失效（双高）。这种利益相关者感知的评估方案揭示了传统方法无法捕捉的异质性脆弱性。

### Q4: 论文做了哪些实验？

论文从三个维度进行了系统实验。**实验设置**上，采用NanoBrowser（多智能体浏览器扩展架构）和BrowserUse（单智能体迭代控制架构）两种代表性Web Agent系统，结合GPT-5和Gemini-2.5-Flash两种骨干模型，构成4种架构-骨干组合，每种组合对264个对抗用例执行3次，共3,168次攻击轨迹，并使用GPT-5裁判按模板条件判定成功。

**数据集/基准测试**为本文提出的StakeBench，涵盖间接提示注入（IPI）和直接提示注入（DPI）两种投递通道，包含用户、卖家、平台三类利益相关者，及12个具体的攻击目标模板。

**对比方法和主要结果**：1）**整体脆弱性**：IPI下平均攻击成功率（ASR）为54-56%，其中BrowserUse + Gemini组合任务偏离率（TDR）最高达45.09%，行为不稳定率（BIR）达28.85%；DPI下ASR超80%。2）**利益相关者级**：卖家目标的ASR最高（~60-62%），用户目标TDR最低（~18%）呈现隐蔽寄生模式，平台目标BIR最高（17.51%）呈现错位中断模式。3）**目标级**：12个目标分布在三个故障区（隐蔽寄生、错位中断、复合失败），无任务进入鲁棒行为区。4）**消融实验**：语义相似性高时ASR达70-79%，低时降至28-31%；相反环境线索使GPT-5 ASR从55.56%降至19.44%，但对Gemini影响不大；暴露时机越晚（起点越接近注入点），ASR越高（79-97%）；图像篡改使首选产品选择率从70%降至20%。

### Q5: 有什么可以进一步探索的点？

首先，论文尽管提供了3,168次攻击的详细分析，但在某些攻击模式（如“隐蔽寄生”）下，对任务成功与攻击成功的交叉影响剖析还不够细致。未来可以深入探索这种微妙共存模式的成因，例如研究任务复杂度、注入指令的语义对齐度如何影响“双赢”或“双输”结果的出现概率。其次，当前基准主要依赖于攻击的文字表达形式，缺少对多模态输入（如图像中的隐藏指令）或非文本交互（如鼠标悬停动作）的覆盖。可以扩展攻击向量，尝试将恶意指令嵌入到图像的像素级噪声或HTML元素的动态属性中，评估代理的跨模态鲁棒性。此外，现有评估基于固定的用户任务，未来可引入任务目标随机化的测试范式，测量代理在动态目标下对注入指令的泛化抗性，这更贴近真实世界中用户任务多样化的场景。

### Q6: 总结一下论文的主要内容

这篇论文提出了SBC（Stakeholder-Centric Benchmark），一个以利益相关者为中心的提示注入安全基准测试，用于评估基于大语言模型（LLM）的真实世界Web代理。现有安全基准采用“攻击中心”视角，只关注注入的技术可行性，而忽略了危害在不同利益相关者间的非对称分布。该方法通过区分受影响实体（如用户、卖家、平台），将攻击分解为具体目标，并用结果级和过程级指标进行评估。实验对两个代理系统和两个先进LLM进行了3168次攻击，发现：没有攻击目标能被稳健防御；失败模式呈现定性差异，包括“隐蔽寄生”（攻击成功但未干扰用户任务）、“错位干扰”（任务被干扰但攻击失败）和“复合失败”（对抗目标和任务完整性同时违反）。结论表明提示注入安全不是骨干模型的标量属性，而是由受影响方、目标与任务语义对齐及部署架构共同决定的危害分布，凸显了在部署中采用利益相关方感知评估的必要性。
