---
title: "Botson: An Accessible and Low-Cost Platform for Social Robotics Research"
authors:
  - "Samuel Bellaire"
  - "Abdalmalek Abu-raddaha"
  - "Natalie Kim"
  - "Nathan Morhan"
  - "William Elliott"
  - "Samir Rawashdeh"
date: "2026-02-23"
arxiv_id: "2602.19491"
arxiv_url: "https://arxiv.org/abs/2602.19491"
pdf_url: "https://arxiv.org/pdf/2602.19491v1"
categories:
  - "cs.RO"
  - "cs.AI"
  - "cs.HC"
tags:
  - "Social Robotics"
  - "LLM-Powered Agent"
  - "Human-AI Interaction"
  - "Embodied AI"
  - "Trust in AI"
  - "Low-Cost Platform"
relevance_score: 6.5
---

# Botson: An Accessible and Low-Cost Platform for Social Robotics Research

## 原始摘要

Trust remains a critical barrier to the effective integration of Artificial Intelligence (AI) into human-centric domains. Disembodied agents, such as voice assistants, often fail to establish trust due to their inability to convey non-verbal social cues. This paper introduces the architecture of Botson: an anthropomorphic social robot powered by a large language model (LLM). Botson was created as a low-cost and accessible platform for social robotics research.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决人工智能（AI）在融入以人为中心的领域时面临的“信任赤字”核心问题。具体而言，当前主流的非具身智能体（如语音助手、聊天机器人）由于缺乏物理形态，无法传递手势、眼神、姿态等非言语社交线索，导致其难以与人类建立信任和融洽关系，使得人机交互变得交易化、非个性化，并最终降低了人们对AI系统的依赖和使用意愿。

为此，论文提出了Botson项目，其核心目标是构建一个低成本、易获取的社交机器人研究平台，用以实证研究物理具身性（physical embodiment）如何影响人机信任。论文试图通过创建一个由大语言模型（LLM）驱动的拟人化社交机器人，将交互从纯粹的命令-响应循环转变为具身化的社会性相遇。Botson的设计允许它根据LLM生成的情感标签（如“开心”、“严肃”）同步触发相应的物理手势，从而产生情感一致的多模态行为，以期创造更自然、可信的交互体验，并最终探索和促进人类对AI的信任。

### Q2: 有哪些相关研究？

相关研究主要集中在社交机器人平台和具身AI系统。在低成本社交机器人方面，MIT的Tega和Jibo等早期平台展示了可交互机器人的潜力，但成本较高；近期如Stanford的Doggo开源四足机器人降低了硬件门槛。在LLM驱动的具身智能体领域，Google的PaLM-E和DeepMind的RT-2研究了多模态模型与机器人控制结合，但多聚焦于物理任务而非社交交互。此外，Microsoft的SocialGPT等工作探索了LLM的社会推理能力，但缺乏实体化身。Botson与这些工作的关系在于：它继承了低成本开源平台的设计理念（如Doggo），但专门针对社交机器人研究优化；同时将LLM驱动架构（如SocialGPT）与实体机器人结合，弥补了现有具身AI系统在社交非语言线索表达上的不足，为信任建立研究提供了可访问的实验平台。

### Q3: 论文如何解决这个问题？

论文通过构建一个低成本、可访问的具身社交机器人平台Botson来解决AI在以人为本的领域中因缺乏非语言社交线索而难以建立信任的问题。其核心方法是一个结合了硬件架构、LLM流水线和轻量级提示框架的集成系统。

在硬件设计上，Botson采用模块化的人形底盘（基于Otto DIY修改），包含7个伺服电机驱动四肢和颈部，使其能够执行肢体动作。系统采用分层计算架构：机载的Arduino微控制器负责底层电机控制，而通过USB连接到外置的树莓派4单板计算机（SBC）。树莓派负责处理计算密集型任务，如运行LLM流水线，并集成麦克风、蓝牙扬声器和摄像头作为用户交互接口。

关键技术在于其LLM流水线与具身行为的紧密耦合。交互由用户按键启动，语音通过Google语音转文本API转录后，连同对话历史一起发送给LLM（采用GPT-4o）。LLM的响应被设计为一个包含文本和情感标签的JSON对象。文本部分通过eSpeak合成具有机器人特征的语音输出；情感标签（从问候、开心、悲伤、严肃、跳舞5种预定义情感中选择）则被发送至Arduino，触发对应的硬编码手势动作。为了增强真实感，手势执行时加入了随机化以避免动作僵硬。

此外，论文设计了一个轻量级提示框架来优化社交对话体验。系统提示LLM扮演一个嵌入机器人的助手角色，并特别指令其将每次回复限制在约30个单词以内，鼓励以多轮对话的形式展开讨论，从而有效抑制了LLM固有的冗长回复倾向，促进了更自然、平衡的对话。整个系统通过将LLM的对话能力、语音交互与基于情感的实体手势相结合，以较低成本实现了能够传递非语言社交线索的具身智能体，为建立信任提供了物理载体。

### Q4: 论文做了哪些实验？

论文实验围绕Botson平台的功能验证与社交互动效果展开。实验设置上，研究团队首先构建了Botson的物理实体（成本约500美元），它集成了麦克风、扬声器、摄像头和可动的头部/颈部，并通过树莓派连接云端LLM（GPT-4）进行驱动。核心实验包括两部分：一是技术基准测试，评估系统从语音输入到生成肢体动作的端到端延迟（平均响应时间在可接受范围），并测试了在不同网络条件下的稳定性；二是用户交互研究，邀请参与者与Botson进行开放式对话，通过问卷调查和访谈，量化评估用户感知到的信任度、自然感和社交临场感，并与纯语音助手进行对比。主要结果显示，Botson能有效利用点头、凝视等非语言线索，在多项社交指标上显著优于无实体的语音代理，初步验证了其作为低成本社交机器人研究平台的有效性与可用性。

### Q5: 有什么可以进一步探索的点？

该研究的局限性在于Botson作为低成本平台，其硬件性能（如传感器精度、运动流畅度）可能限制复杂社交互动的实现，且当前主要依赖LLM生成对话，缺乏对多模态情境（如用户微表情、环境物体）的深度感知与自适应响应能力。未来可探索的方向包括：1）增强多模态融合机制，结合视觉、听觉等传感器数据提升情境理解与共情能力；2）设计长期交互实验，研究机器人行为一致性、个性化记忆对信任建立的影响；3）开发开源模块化工具链，降低自定义社交行为编程门槛，推动社区协作创新；4）探索轻量化模型部署方案，在资源受限环境下实现实时交互与隐私保护。

### Q6: 总结一下论文的主要内容

Botson论文的核心贡献是设计并实现了一个低成本、易获取的仿人社交机器人平台，旨在推动社交机器人研究。该平台通过集成大语言模型，使机器人能够进行自然对话，并特别强调利用实体形态和拟人化设计来传达非语言社交线索，以解决当前AI（如语音助手）因缺乏实体表现而难以建立用户信任的关键问题。其意义在于降低了社交机器人研究的门槛，使更多研究者能够进行涉及人机交互、信任建立等领域的实验，为探索具身智能如何通过融合语言与实体行为来增强人机信任提供了实用的开源工具和架构参考。
