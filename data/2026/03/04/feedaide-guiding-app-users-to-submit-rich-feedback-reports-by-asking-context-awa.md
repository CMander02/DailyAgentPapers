---
title: "FeedAIde: Guiding App Users to Submit Rich Feedback Reports by Asking Context-Aware Follow-Up Questions"
authors:
  - "Ali Ebrahimi Pourasad"
  - "Meyssam Saghiri"
  - "Walid Maalej"
date: "2026-03-04"
arxiv_id: "2603.04244"
arxiv_url: "https://arxiv.org/abs/2603.04244"
pdf_url: "https://arxiv.org/pdf/2603.04244v1"
categories:
  - "cs.SE"
  - "cs.AI"
  - "cs.HC"
tags:
  - "Reasoning & Planning"
  - "Human-Agent Interaction"
relevance_score: 5.5
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Human-Agent Interaction"
  domain: "Code & Software Engineering"
  research_type: "System/Tooling/Library"
attributes:
  base_model: "N/A"
  key_technique: "FeedAIde"
  primary_benchmark: "N/A"
---

# FeedAIde: Guiding App Users to Submit Rich Feedback Reports by Asking Context-Aware Follow-Up Questions

## 原始摘要

User feedback is essential for the success of mobile apps, yet what users report and what developers need often diverge. Research shows that users often submit vague feedback and omit essential contextual details. This leads to incomplete reports and time-consuming clarification discussions. To overcome this challenge, we propose FeedAIde, a context-aware, interactive feedback approach that supports users during the reporting process by leveraging the reasoning capabilities of Multimodal Large Language Models. FeedAIde captures contextual information, such as the screenshot where the issue emerges, and uses it for adaptive follow-up questions to collaboratively refine with the user a rich feedback report that contains information relevant to developers. We implemented an iOS framework of FeedAIde and evaluated it on a gym's app with its users. Compared to the app's simple feedback form, participants rated FeedAIde as easier and more helpful for reporting feedback. An assessment by two industry experts of the resulting 54 reports showed that FeedAIde improved the quality of both bug reports and feature requests, particularly in terms of completeness. The findings of our study demonstrate the potential of context-aware, GenAI-powered feedback reporting to enhance the experience for users and increase the information value for developers.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决移动应用用户反馈质量低下的问题。研究背景在于，用户反馈对应用成功至关重要，但当前应用商店的反馈机制存在显著缺陷：用户常提交模糊、缺乏关键上下文信息的报告，导致开发者难以理解问题本质，进而引发耗时的澄清讨论。现有方法（如简单文本反馈表单）无法主动引导用户提供结构化信息，且未充分利用设备上下文（如截图、交互日志）来动态优化反馈过程。

现有方法的不足主要体现在两方面：一是反馈内容与开发者需求脱节，约45%的开发者需反复追问细节，但用户回复率低、延迟高；二是已有研究虽尝试用生成式AI分析反馈，却未能结合上下文数据实时指导用户提交过程，限制了反馈的完整性和实用性。

本文核心问题是：如何利用多模态大语言模型的推理能力，设计一种上下文感知的交互式反馈系统，通过自适应追问引导用户协作生成富含开发者所需信息的高质量报告。为此，论文提出FeedAIde系统，自动捕获截图等上下文，动态生成跟进问题，以简化用户报告体验的同时提升反馈的信息价值。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为两类：**上下文感知的反馈收集方法**和**对话式反馈引导方法**。

在**上下文感知的反馈收集方法**方面，早期研究如 Seyff 等人提出的 AppEcho，允许用户在应用内直接提交包含截图和简短文本的反馈，强调了在应用内捕获上下文信息的重要性。本文的 FeedAIde 继承了这一核心理念，同样注重在应用内即时捕获屏幕截图等上下文信息。

在**对话式反馈引导方法**方面，Martens 和 Maalej 曾提出利用聊天机器人与用户交互以获取额外上下文信息的构想。Song 等人提出的 BURT 是一个更接近的、基于规则的聊天机器人，用于在 Android 上引导交互式错误报告，它通过自然语言确保报告包含关键质量要素（如观察到的行为、预期行为和复现步骤）。BURT 依赖于基于规则的解析和词性标注来理解自然语言。

**本文工作与这些研究的区别和关系在于**：FeedAIde 是一个**集成式、上下文感知的框架**，它将上述两条研究路线结合起来。它不仅像 AppEcho 一样在应用内捕获丰富的上下文，还像 BURT 一样通过对话引导用户。关键创新在于，FeedAIde 利用**多模态大语言模型** 来理解用户输入和上下文（如截图），并据此生成**自适应的后续问题**，以协作方式提炼出对开发者有价值的完整报告。这超越了 BURT 所依赖的、灵活性较差的基于规则的方法，实现了更智能、更动态的交互引导。

### Q3: 论文如何解决这个问题？

论文通过提出一个名为FeedAIde的上下文感知、交互式反馈框架来解决用户反馈信息不完整和模糊的问题。其核心方法是利用多模态大语言模型（MLLM）的推理能力，在用户报告过程中主动引导他们提供更丰富、更详细的反馈。

**整体框架与工作流程**：FeedAIde被实现为一个iOS框架，其工作流程分为六个步骤。首先，当用户通过摇动设备或点击按钮触发反馈流程时，系统自动收集上下文信息，包括当前屏幕截图、设备详情、应用版本以及近期用户交互日志。其次，MLLM基于这些上下文分析用户可能想报告的内容，生成最多三个具体的反馈预测（如“报告登录问题”或“添加深色模式选项”）供用户选择，用户也可自行输入。第三步，在用户选定或输入反馈主题后，MLLM会生成最多两个自适应的、上下文感知的后续问题，以挖掘缺失的关键细节。第四步，用户回答这些问题。第五步，系统将所有收集到的信息（用户初始反馈、问答记录、上下文数据）整合成一份丰富的反馈报告，其中包含面向用户的意图总结和面向开发者的技术性总结。最后，报告以JSON格式发送给开发者。

**主要模块与架构设计**：实现上主要包含几个关键组件。1) **上下文收集模块**：自动捕获截图、设备信息、应用日志等。2) **MLLM集成与代理层**：通过AIProxy Swift库连接外部MLLM API（如OpenAI），该设计实现了模块化和低耦合，便于切换模型，同时利用Apple的Device Check API确保安全，防止滥用。3) **提示工程模块**：这是技术的核心创新点。系统发送给MLLM的提示词经过精心设计，分为三个部分：第一部分是固定的“设定、指令和约束”，用于定义模型的角色（一个专注的反馈系统）和行为协议；第二部分是“应用描述”，由开发者提供，帮助MLLM理解应用功能；第三部分是动态的“上下文信息”，即收集到的具体数据。这种结构旨在平衡信息充分性与隐私安全，避免因上下文过载（“大海捞针”问题）而影响模型表现。4) **交互式UI模块**：基于SwiftUI构建，提供从预测选择到问答确认的完整引导流程。

**关键技术细节与创新点**：1) **上下文感知的自适应问答**：MLLM不仅基于静态截图，还结合了用户行为序列（如多次登录失败）来生成精准的反馈预测和后续问题（例如询问是否最近更改过密码），这是实现“丰富报告”的关键。2) **结构化输出与双总结**：通过约束MLLM的输出格式，确保生成包含`userIntentSummary`和`developerSummary`的结构化报告对象，前者反映用户视角，后者转化为开发者视角，极大提升了报告的可操作性和信息价值。3) **隐私与效率优化**：提示词设计强调只传输最相关的上下文，减少了令牌消耗、提升了响应速度，并降低了不必要的用户数据暴露风险。4) **端到端的集成方案**：作为一个即插即用的Swift Package，它简化了开发者的集成工作，同时通过预设的交互协议（如固定两次后续提问）保证了用户体验的一致性和效率。

### Q4: 论文做了哪些实验？

论文通过用户测试和专家评估进行了两项主要实验。实验设置方面，研究采用了一项受试者内用户测试，使用一款名为PPEmployee的健身房内部iOS应用，比较了传统文本反馈表单与FeedAIde系统。数据集包括7名真实用户（年龄19-51岁，职业为健身教练、经理等）在四个预设场景（两个Bug报告、两个功能请求）下生成的54份反馈报告（每个场景使用两种方法）。对比方法为应用原有的简单文本反馈表单。

主要结果如下：在用户感知（RQ1）方面，参与者对FeedAIde的易用性平均评分为3.71/4，显著高于传统系统的2.86/4；帮助性评分为3.43/4，远高于传统系统的1.14/4。所有参与者都更偏好FeedAIde。关键数据指标显示，易用性得分提升0.85，帮助性得分增加2.29。

在反馈质量（RQ2）方面，两位专家（iOS开发者和UX专家）的独立评估显示，FeedAIde生成的Bug报告在“观察到的行为”维度得分为1.50/2（传统系统为0.93/2），在“重现步骤”维度得分为2.00/2（传统系统为0.14/2）。功能请求评估中，FeedAIde在“描述”和“产品版本”等维度的完成度达到100%，而传统系统分别为0%和0%；在“指定问题”维度，FeedAIde为53.8%，传统系统为0%。评估者间一致性很高（Bug报告Cohen's Kappa=0.906，功能请求κ=0.9207）。专家指出FeedAIde提高了报告的完整性，但后续问题有时过于关注解决方案而非根本问题。

### Q5: 有什么可以进一步探索的点？

该论文的局限性主要体现在研究范围、评估方法和技术实现三个方面。首先，研究仅针对单一健身应用和有限用户样本，缺乏对不同应用类别（如社交、工具类）和多样化反馈类型（如内容建议、可用性问题）的验证，限制了结论的普适性。其次，评估指标虽借鉴现有研究，但可能忽略其他关键质量维度（如Bug报告中的堆栈跟踪、测试用例），且专家评估存在主观偏差风险。最后，技术依赖特定MLLM（GPT-4.1）和预定义场景，未探索不同模型（如Claude、Gemini）或提示策略的影响，也未考虑真实环境中用户自发反馈的复杂性。

未来研究方向可沿以下路径拓展：一是扩大实证范围，跨多个应用领域和用户群体进行纵向研究，探索文化、技术素养等因素对交互式反馈效果的影响；二是优化评估体系，开发更全面的质量指标，结合自动化分析（如情感识别、信息密度计算）与开发者实际需求数据；三是增强技术适应性，研究轻量化模型部署、动态上下文捕捉（如操作日志、设备状态）以及个性化提问策略，以降低对云端大模型的依赖并提升实时性。此外，可探索反馈闭环机制，将用户报告与开发流程（如问题跟踪系统）直接集成，进一步验证其在实际开发中的效能提升。

### Q6: 总结一下论文的主要内容

该论文提出了一种名为FeedAIde的上下文感知交互式反馈系统，旨在解决移动应用用户反馈中常见的信息模糊和上下文缺失问题。其核心贡献在于利用多模态大语言模型的推理能力，在用户提交反馈时实时捕获屏幕截图等上下文信息，并动态生成自适应追问，引导用户补充关键细节，从而协作生成对开发者更有价值的完整反馈报告。

方法上，FeedAIde通过iOS框架实现，在用户触发反馈时自动捕捉当前界面截图，结合大语言模型分析潜在问题点，并以交互式对话形式提出针对性的后续问题（如操作步骤、预期结果等），帮助用户逐步完善报告内容。研究在一款健身应用中进行用户实验，对比传统简单表单，参与者认为FeedAIde更易用且更有帮助。

主要结论显示，FeedAIde显著提升了反馈报告的质量，尤其是完整性方面。行业专家对生成的54份报告评估证实，该系统在缺陷报告和功能请求两类反馈中都提高了信息价值，证明了基于生成式AI的上下文感知反馈机制既能改善用户报告体验，又能为开发者提供更高效的信息支持。
