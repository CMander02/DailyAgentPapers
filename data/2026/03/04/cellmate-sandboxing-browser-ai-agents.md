---
title: "ceLLMate: Sandboxing Browser AI Agents"
authors:
  - "Luoxi Meng"
  - "Henry Feng"
  - "Ilia Shumailov"
  - "Earlence Fernandes"
date: "2025-12-14"
arxiv_id: "2512.12594"
arxiv_url: "https://arxiv.org/abs/2512.12594"
pdf_url: "https://arxiv.org/pdf/2512.12594v2"
categories:
  - "cs.CR"
  - "cs.LG"
tags:
  - "Agent Security"
  - "Browser Agent"
  - "Prompt Injection"
  - "Sandboxing"
  - "Agent Framework"
  - "Agent Evaluation"
relevance_score: 7.5
---

# ceLLMate: Sandboxing Browser AI Agents

## 原始摘要

Browser-using agents (BUAs) are an emerging class of AI agents that interact with web browsers in human-like ways, including clicking, scrolling, filling forms, and navigating across pages. While these agents help automate repetitive online tasks, they are vulnerable to prompt injection attacks that trick an agent into performing undesired actions, such as leaking private information or issuing unintended state-changing requests. We propose ceLLMate, a browser-level sandboxing framework that restricts the agent's ambient authority and reduces the blast radius of prompt injections. We address the semantic gap challenge that is fundamental to BUAs -- writing and enforcing security policies for low-level UI tools like clicks and keystrokes is brittle and error-prone. Our core insight is to perform sandboxing at the HTTP layer because all side-effecting UI operations will result in network communication to the website's backend. We implement ceLLMate as an agent-agnostic browser extension and demonstrate how it enables sandboxing policies that block prompt injection attacks in the WASP benchmark with 7.25--15% latency overhead.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决浏览器智能代理（BUAs）面临的安全问题，特别是针对提示注入攻击的防护挑战。研究背景是，随着AI代理（如Gemini-CUA、OpenAI Atlas等）的兴起，它们能够模拟人类操作浏览器，自动化完成点击、滚动、填写表单等在线任务，极大提升了效率。然而，这些代理容易受到提示注入攻击，攻击者可能诱导代理执行危险操作，如泄露私人信息或发起未经授权的状态变更请求，现有系统已出现多起实际案例。

现有方法的不足主要体现在两个方面：一是传统基于机器学习的防御手段（如训练模型抵抗或检测提示注入）存在局限性，容易陷入对抗性攻击的“军备竞赛”，自适应攻击者往往能突破这些防御；二是在BUAs环境中实施沙盒策略面临根本性挑战——语义鸿沟问题。由于代理通过低级UI操作（如点击坐标、按键）与浏览器交互，若直接在此层面定义和执行安全策略（例如限制点击特定坐标），会非常脆弱且容易出错，因为相同坐标在不同网站、状态或屏幕分辨率下语义完全不同，导致策略抽象级别与执行层面不匹配。

本文要解决的核心问题是：如何为BUAs设计一个有效的沙盒框架，既能限制代理的权限、减小提示注入攻击的影响范围，又能克服语义鸿沟，实现可靠的安全策略定义与执行。为此，论文提出了ceLLMate，其核心思路是将沙盒防护提升到HTTP层，因为所有产生副作用的UI操作最终都会转化为与网站后端的网络通信。HTTP消息本身具有明确语义，从而弥合了语义鸿沟。框架通过引入“代理站点地图”概念，由网站开发者定义关键HTTP资源，使策略能基于有意义的抽象层面（如拦截特定HTTP请求并检查参数）进行编写和强制执行。此外，论文还探讨了策略创建与选择的架构，并实现了一个与代理无关的浏览器扩展原型，在保证低延迟开销的同时，有效阻挡了基准测试中的攻击。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：**针对LLM/Agent的提示注入防御方法**、**系统级安全机制**以及**浏览器/Web自动化代理的研究**。

在**提示注入防御方法**方面，早期工作如CaMeL和Fides基于Willison的“双LLM”架构，通过分离可信与不可信上下文并强制执行来自可信上下文的控制和数据流来提供安全保证。Progent则通过对工具调用实施权限控制策略来限制Agent行为。然而，这些方法都隐含一个关键假设：安全策略可以通过单纯限制工具使用来强制执行。这要求工具接口与安全边界之间有清晰的映射关系，而本文研究的浏览器使用代理（BUAs）使用的恰恰是缺乏固有语义的低级工具（如点击、输入），其安全含义高度依赖于动态上下文，使得上述假设不成立，构成了本文要解决的“语义鸿沟”挑战。

在**系统级安全机制**方面，传统计算机安全中的访问控制和沙箱技术遵循最小权限原则，为本文提供了核心灵感。近期研究开始将这一原则应用于LLM集成系统。与本文工作最相关的是Foerster等人将CaMeL扩展到计算机使用代理的工作，它采用了执行计划内的“观察-验证-执行”范式。但该工作同样依赖于语义工具的假设，并且其作者承认系统仍易受“分支引导攻击”的影响（即通过操纵UI元素触发非预期但有效的操作），而本文的ceLLMate则明确消除了此类攻击向量。

在**浏览器/Web自动化代理**领域，已有大量关于使用Playwright、Puppeteer等框架构建代理的研究，但安全方面的工作相对较少。本文首次提出了一个在HTTP层进行沙箱化的系统级防御框架ceLLMate，其核心创新在于将策略执行与低级工具接口解耦。通过监控所有UI操作最终导致的网络通信，ceLLMate能够在网站后端层面实施安全策略，从而有效阻断提示注入攻击，并克服了基于工具限制的传统方法在BUA场景下的脆弱性。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为ceLLMate的浏览器级沙箱框架来解决浏览器AI代理（BUAs）面临的提示注入攻击问题。其核心方法是**在HTTP层进行沙箱化**，而非在易变且语义模糊的UI操作层（如点击、输入）实施策略。这基于一个关键洞察：所有具有副作用的UI操作最终都会转化为与网站后端通信的网络请求（HTTP），因此在此层进行拦截和策略执行更为根本和稳定。

整体框架包含三个主要阶段：
1.  **注册阶段**：网站开发者提供**代理站点地图**，将HTTP请求映射到高级别的语义化操作（如“在GitHub上评论”、“在亚马逊上下单”）；同时，可信来源（如开发者、企业管理员）提供**策略生成器**，定义如何创建策略。
2.  **策略实例化阶段**：根据用户任务，利用注册的策略生成器实例化具体策略，并将其绑定到代理控制的浏览器会话。
3.  **策略执行阶段**：在代理执行过程中，ceLLMate在HTTP层严格仲裁，拦截所有请求并根据已批准的策略进行放行或阻止。

主要模块/组件与创新点包括：
*   **HTTP层强制执行**：这是最核心的创新设计。它弥合了“高级策略意图”与“低级UI操作”之间的语义鸿沟。通过拦截HTTP请求，ceLLMate能够稳定、完整地仲裁所有与后端的通信，无论代理通过何种UI操作序列（如直接导航、通过搜索引擎点击）触发该请求，从而避免了在UI层枚举和阻断所有可能攻击路径的不可行性。
*   **代理站点地图**：这是一个关键抽象层。它由网站开发者为其域名创建和维护，类似于为BUAs编写的“API文档”，将具体的HTTP请求模式（如URL、方法）映射到语义明确的动作（如“ViewCart”）。这极大简化了后续的策略编写，使策略作者可以基于有意义的动作而非原始请求进行逻辑设计。
*   **灵活的策略创作与选择机制**：框架本身不限定单一策略形式，但论文特别设计了一种**自主策略机制**以适应不同用户。其创新点在于：1）提供由可信来源预定义的策略库（基于站点地图中的语义动作）；2）引入一个**策略选择器**，它仅依据可信上下文（用户原始提示、预定义策略及其自然语言描述）自动为给定任务选择一组最小够用的策略，并合并为**复合策略**。这确保了策略选择过程本身能抵抗来自网页上不可信数据的提示注入。

总之，ceLLMate通过将安全边界从脆弱的UI层下移至稳定的HTTP层，并引入代理站点地图作为语义桥梁，构建了一个与具体代理无关的沙箱框架，从而有效限制了代理的权限范围，降低了提示注入攻击的影响半径。

### Q4: 论文做了哪些实验？

论文实验主要包括以下方面：

**实验设置**：作者实现了ceLLMate作为一个与具体AI代理无关的浏览器扩展。其实验核心是评估该框架在真实场景中防御提示注入攻击的有效性，并测量其引入的性能开销。

**数据集/基准测试**：主要使用**WASP基准测试**来评估对提示注入攻击的防御能力。WASP是一个专门用于评估Web代理安全性的基准测试套件，包含多种攻击场景。此外，论文还以**Amazon**和**GitLab**作为案例研究，详细说明了站点地图（sitemap）的构建（例如为GitLab手动构建了包含51个API的站点地图）和政策编写过程。

**对比方法**：实验主要将ceLLMate的沙盒防护效果与**无防护的基线状态**（即当前易受攻击的BUA现状）进行对比，以证明其安全提升。论文未提及与其他具体防护框架的横向对比。

**主要结果与关键指标**：
1.  **安全有效性**：ceLLMate能够成功**阻断WASP基准测试中的所有提示注入攻击**，证明了其在HTTP层进行沙盒隔离的有效性。
2.  **性能开销**：引入ceLLMate框架带来的延迟开销在**7.25%到15%之间**。这个开销被认为是可以接受的，因为它显著提升了安全性。
3.  **实用性验证**：通过Amazon（购物车查看、限额购买）和GitLab（项目API管理）的详细政策案例，证明了该框架能够为复杂的、有状态的Web操作定义和实施具有语义的安全政策（如“仅允许查看购物车”或“单次购买金额不超过50美元”）。

### Q5: 有什么可以进一步探索的点？

该论文提出的HTTP层沙盒方案虽具创新性，但仍存在若干局限与可拓展方向。首先，其策略依赖对网络请求的语义理解，但当前方法可能难以处理复杂的前端交互（如WebSocket实时通信或动态加载内容），未来需增强对现代Web应用协议的覆盖能力。其次，框架仅防御提示注入攻击，但浏览器代理还可能面临UI混淆、会话劫持等威胁，可探索多维行为监控机制。此外，策略配置仍依赖人工定义，未来可结合LLM自动生成上下文感知的安全规则。从系统优化角度，延迟开销虽较低，但对高交互频率场景（如自动化交易）仍需进一步压缩性能损耗。最后，该框架未考虑多代理协作场景下的权限隔离问题，这为分布式浏览器智能体的安全架构设计提供了新的研究方向。

### Q6: 总结一下论文的主要内容

该论文提出了ceLLMate框架，旨在解决浏览器AI代理面临的安全风险。核心问题是浏览器代理在执行点击、输入等操作时易受提示注入攻击，导致隐私泄露或非预期操作。传统方法在UI层面实施安全策略存在语义鸿沟，难以精确控制。

ceLLMate的创新在于将沙箱机制提升至HTTP网络层，因为所有UI操作最终都会转化为后端网络请求。该方法通过浏览器扩展实现代理无关的防护，允许定义细粒度策略来限制代理权限并缩小攻击影响范围。

实验表明，ceLLMate能有效防御WASP基准测试中的提示注入攻击，仅产生7.25-15%的延迟开销。这项工作的意义在于为浏览器AI代理提供了实用的安全解决方案，平衡了功能性与安全性，为自动化网络任务的安全部署奠定了基础。
