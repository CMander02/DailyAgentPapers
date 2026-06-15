---
title: "Communication Policy Evolution for Proactive LLM Agents"
authors:
  - "Xinbei Ma"
  - "Jiyang Qiu"
  - "Yao Yao"
  - "Zheng Wu"
  - "Yijie Lu"
  - "Xiangmou Qu"
  - "Jiaxin Yin"
  - "Xingyu Lou"
  - "Jun Wang"
  - "Weiwen Liu"
  - "Weinan Zhang"
  - "Zhuosheng Zhang"
  - "Hai Zhao"
date: "2026-06-12"
arxiv_id: "2606.14314"
arxiv_url: "https://arxiv.org/abs/2606.14314"
pdf_url: "https://arxiv.org/pdf/2606.14314v1"
categories:
  - "cs.AI"
tags:
  - "LLM Agent"
  - "Communication Policy"
  - "Self-Evolution"
  - "Multi-Modal Interaction"
  - "Proactive Agent"
  - "Persona Compliance"
relevance_score: 8.0
---

# Communication Policy Evolution for Proactive LLM Agents

## 原始摘要

LLM agents have rapidly evolved into autonomous systems, yet a persistent information gap remains between users and agents: communication is costly, while users' identical preferences further limit information exchange. To investigate how agents should communicate across modalities, this paper formalizes Communication Policy, establishes textual and UI-based policies, and then evaluates communication policies across diverse environments, personas, and model combinations. Building information asymmetry for proactive agents, we set up two complementary settings, User-Agent and Planner-Executor. Experimental results reveal complementary strengths between interaction channels: text-based interaction often facilitates task performance, while structured UI improves agents' response quality and persona compliance. Motivated by that, a hybrid method combines these advantages. We further propose Communication Policy Evolution (CPE), a self-evolution framework for refining communication policies through rollout and prompt-level evolving. Without model modification, CPE achieves the best task success across multiple settings using prompt refinement alone. Our findings identify communication behavior as a critical yet underexplored design dimension for LLM agents.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决LLM智能体在信息不对称条件下如何有效沟通的核心问题。研究背景方面，LLM智能体已发展为自主系统，但用户与智能体之间存在持久的信息鸿沟：用户掌握完整任务意图，但自然语言难以一次性传达所有约束、偏好和边缘情况，关键信息需通过交互逐步浮现。现有方法的不足主要体现在：当前研究主要关注智能体应该问什么（信息需求内容），而严重忽视了另一个同等重要的问题——智能体应该如何沟通（沟通渠道选择）。自由形式的自然语言交互虽然灵活，但导致高模糊性和用户负担；而结构化界面（如HTML表单）可降低歧义并提高响应质量，但现有工作主要聚焦于改进生成式UI本身而非将其部署到实际应用中。本文要解决的核心问题是：为主动型智能体形式化定义沟通策略（Communication Policy），系统评估文本与结构化UI两种沟通渠道在不同环境、用户画像和模型组合下的互补优势，并开发了无需修改模型权重、仅通过提示工程就能自动优化沟通策略的自我演化框架（CPE），以在任务完成率和用户体验间取得最佳平衡。

### Q2: 有哪些相关研究？

相关研究主要分为三类。第一类是LLM智能体的主动性研究，相关工作探索了智能体通过澄清对话、结构化提问、预期用户需求等方式主动获取缺失信息，但这些工作的核心是“问什么”，而本文首次将“如何问”即通信渠道本身作为设计变量，区分了文本与UI两种模态。第二类是用户中心智能体，已有研究通过角色条件用户模拟器、个性化技术实现智能体对不同用户偏好的适应，本文在此基础上引入通信渠道作为新的设计维度，探究结构化UI交互是否能提升智能体对用户角色的对齐能力。第三类是测试时优化方法，包括黑盒提示优化、文本梯度下降、自反思等，这些方法通常优化智能体的任务执行能力，而本文提出的Communication Policy Evolution（CPE）框架则聚焦于优化通信行为，即智能体何时通过自然语言、何时通过UI交互来恢复用户意图，与现有方法形成互补。

### Q3: 论文如何解决这个问题？

CPE（通信策略演化）通过一个无需模型修改、仅通过提示词优化的自演化框架，为LLM智能体制定如何以及在何时使用文本或UI交互的通信策略。

**整体框架**：CPE是一个迭代式提示词优化过程，旨在最大化任务完成的生产力分数。它包含评估、演化、变异和选择四个循环步骤，并设置了训练/验证集双门控机制以确保策略单调提升。

**核心流程与组件**：
1. **策略表示**：通信策略π_comm由三部分构成：系统提示（指定可用工具、调用格式和通道选择启发式规则）、示例（提供在何种情况下选择“提问”或“生成UI”的少样本演示）和附录（环境特定指导）。
2. **迭代四步法**：每轮循环中，(1) **评估**：在当前批次上运行当前策略π，收集每次交互的通道选择(ask_question/generate_ui)、用户响应及成本信息；(2) **演化**：利用同一个LLM分析评估结果（包含分数、轨迹、任务规格、当前策略和补丁历史），提出结构化的JSON补丁Δπ来修改策略文本；(3) **变异**：应用补丁生成候选策略π'；(4) **选择**：在训练批次上比较π'与π的性能，若候选策略显著优于当前策略（超过容忍度ε），则进入验证门控。
3. **双门控验证**：为确保泛化性，数据集被划分为训练集D_train和验证集D_val。候选策略必须在训练批次上表现更优（训练接受），同时在完整的验证集上超越迄今为止的最佳策略π*（验证接受），才能正式替换π*。这一设计保证了最佳策略在留出数据上的性能单调非递减。

**创新点**：CPE无需修改模型权重，仅通过迭代重写通信策略的提示词部分，即可在多个任务设置中取得最佳任务成功率。它将通信行为本身视为一个可优化的设计维度，并利用混合模式（混合使用文本和UI）的实际轨迹作为演化信号，有效避免了智能体在获得双通道后因不知如何选择而性能下降的“遗憾”问题。

### Q4: 论文做了哪些实验？

论文进行了系统性的实验评估，涵盖四个基准测试：SWE-bench（软件修复）、TravelGym（旅行规划）、τ²-bench（客户服务）和WebArena（网页导航）。实验设置包括两种互补场景：User-Agent（用户持有完整信息，遵循最小披露原则）和Planner-Executor（规划者完全合作）。对比了三种通信模式：文本（M_text）、结构化UI（M_ui）和混合模式（M_hybrid），以及提出的自演化框架CPE。评估使用四个模型作为Agent（DeepSeek-V3.2、GPT-5-mini、Qwen3-VL-32B和Seed-OSS-36B），两个模型作为用户侧（GPT-4o和Qwen3-VL-32B）。

主要结果包括：1）在User-Agent设置中，M_hybrid在14个Agent-用户对中8个取得最佳生产力（如SWE-bench GPT-5-mini：.043/.138/.667）；M_ui在10/14对中主导个性化（如τ²-bench DeepSeek-V3.2/GPT-4o：.275/.120/.850），8/14对中主导主动性；M_text在9/14对中生产力优于M_ui。2）Oracle实验显示，注入完整任务信息后生产力提升2.3-10.6倍（如DeepSeek-V3.2从.135升至.387），证实信息缺失是主要瓶颈。3）CPE在所有9个设置中达到最佳生产力（如WebArena GPT-5-mini：.275/.520/.835），同时改善主动性和个性化。4）在Planner-Executor设置中，M_hybrid在10对中7对领先（如TravelGym DeepSeek-V3.2/Qwen3-VL-32B：1.672），表明通信策略独立于用户人格具有价值。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在三个方面：首先，使用LLM模拟用户无法完全捕捉真实人类交互的变异性，真实用户可能有更复杂的认知偏差、适应性和不规范行为。其次，评估环境虽覆盖四类场景，但通信通道设计空间仍未被充分探索，例如缺乏对视觉通道、触觉反馈或情感化交互的研究。最后，成本注释依赖预设的敏感性模式，现实中的信息暴露行为更依赖动态上下文。未来可探索以下方向：(1) 引入真实人类用户进行对比实验，揭示模拟评估的偏差；(2) 设计更丰富的混合通信协议，例如让代理根据任务阶段动态切换文本与UI的占比，甚至通过元学习自适应选择通道；(3) 改进成本建模，基于强化学习在线学习用户敏感性的动态变化，而非固定模板。此外，CPE的提示级演化虽有效，但可考虑与轻量级模型微调结合，在保持零成本修改优势的同时提升演化效率。

### Q6: 总结一下论文的主要内容

这篇论文正式定义了大型语言模型（LLM）代理系统中的通信策略（Communication Policy），即代理在与用户或其他代理交互时，在文本与结构化UI等模态之间进行选择的提示词级策略。为弥补用户与代理间的信息不对称，论文提出了两种互补设置：用户-代理和规划者-执行者。实验发现，文本交互通常更利于任务推进，而结构化UI能提升代理的回复质量和角色遵从度，两者互补。据此，论文提出了通信策略进化（CPE）框架，通过滚动评估和提示词级进化，无需修改模型即可自动优化通信策略。实验结果表明，CPE在多个环境中取得了最佳任务成功率。该工作的核心贡献是揭示了通信行为是LLM代理设计中一个重要但被忽视的维度，并提供了自动化优化方法，鼓励社区将通信通道选择视为一等设计考量。
