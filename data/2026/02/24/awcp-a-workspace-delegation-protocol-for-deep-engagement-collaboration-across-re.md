---
title: "AWCP: A Workspace Delegation Protocol for Deep-Engagement Collaboration across Remote Agents"
authors:
  - "Xiaohang Nie"
  - "Zihan Guo"
  - "Youliang Chen"
  - "Yuanjian Zhou"
  - "Weinan Zhang"
date: "2026-02-24"
arxiv_id: "2602.20493"
arxiv_url: "https://arxiv.org/abs/2602.20493"
pdf_url: "https://arxiv.org/pdf/2602.20493v1"
categories:
  - "cs.NI"
  - "cs.MA"
tags:
  - "Agent 架构"
  - "多智能体系统"
  - "Agent 协作"
  - "工具使用"
  - "Agentic Web"
  - "协议设计"
  - "工作空间管理"
  - "开源实现"
relevance_score: 9.5
---

# AWCP: A Workspace Delegation Protocol for Deep-Engagement Collaboration across Remote Agents

## 原始摘要

The rapid evolution of Large Language Model (LLM)-based autonomous agents is reshaping the digital landscape toward an emerging Agentic Web, where increasingly specialized agents must collaborate to accomplish complex tasks. However, existing collaboration paradigms are constrained to message passing, leaving execution environments as isolated silos. This creates a context gap: agents cannot directly manipulate files or invoke tools in a peer's environment, and must instead resort to costly, error-prone environment reconstruction. We introduce the Agent Workspace Collaboration Protocol (AWCP), which bridges this gap through temporary workspace delegation inspired by the Unix philosophy that everything is a file. AWCP decouples a lightweight control plane from pluggable transport mechanisms, allowing a Delegator to project its workspace to a remote Executor, who then operates on the shared files directly with unmodified local toolchains. We provide a fully open-source reference implementation with MCP tool integration and validate the protocol through live demonstrations of asymmetric collaboration, where agents with complementary capabilities cooperate through delegated workspaces. By establishing the missing workspace layer in the agentic protocol stack, AWCP paves the way for a universally interoperable agent ecosystem in which collaboration transcends message boundaries. The protocol and reference implementation are publicly available at https://github.com/SII-Holos/awcp.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型的自主智能体在协作过程中因执行环境隔离而导致的“上下文鸿沟”问题。随着智能体向专业化发展，它们需要在复杂的任务中进行协作，但现有的协作范式（如A2A、ANP等协议）主要局限于消息传递层面。这意味着智能体只能交换序列化的任务描述和结果，而无法直接访问或操作对等方的执行环境（如文件系统）。当远程智能体需要处理任务时，它不得不依赖发送方提供的、可能不完整或已过时的环境快照进行重建，这一过程不仅成本高昂、容易出错，还会导致上下文信息丢失、环境不匹配等问题，严重限制了深度协作的能力。

因此，本文的核心问题是：如何突破当前以消息为中心的协作限制，实现智能体间在系统层面的深度交互协作。具体而言，就是设计一种协议，能够安全、临时地将一个智能体的工作空间（workspace）委托给另一个远程智能体，使后者能像在本地一样，使用其原有的工具链直接操作原始文件和环境，从而在保持完整上下文的前提下进行高效、准确的协作。为此，论文提出了智能体工作空间协作协议（AWCP），通过借鉴“一切皆文件”的Unix哲学，将协作抽象为文件操作，并采用控制平面与传输机制解耦的架构，为构建一个普遍可互操作的智能体生态系统奠定了缺失的工作空间层基础。

### Q2: 有哪些相关研究？

本文的相关研究主要可分为三类：协议类、框架类与文件系统类。

在**协议类**研究中，早期如FIPA的Agent通信语言和合同网协议为基于规则的智能体定义了消息传递规范，但难以适配现代LLM的随机性。近期LLM驱动的协议如MCP（客户端-服务器工具调用）、A2A（点对点任务协调）和ANP（网络层身份协商）均专注于**消息层**的交互，通过结构化消息或附件传递数据。**AWCP与这些协议正交**，它引入了**工作空间层**，通过临时文件系统投影实现直接环境操作，而非仅传递序列化负载。

在**框架类**研究中，多智能体协作框架如AutoGen、CAMEL侧重于通过对话协调；MetaGPT、ChatDev采用标准化流程。新趋势包括去中心化协调（如Symphony）、拓扑自适应（如AdaptOrch）以及自演化系统（如InfiAgent）。特别相关的是**工作空间级协调**的研究，如EvoGit、AgentGit利用Git作为共享状态，Agyn使用沙盒合并，CodeCRDT采用CRDT实现并发。这些工作证明了工作空间协调的有效性，但缺乏统一的生命周期管理协议。**AWCP弥补了这一空白**，提供了标准化的、传输无关的工作空间委托原语，可供现有框架集成。

在**文件系统类**研究中，Unix“万物皆文件”哲学、Plan 9的9P协议、NFS和FUSE等奠定了远程资源文件化访问的基础。AWCP的传输层借鉴了这些成熟思想，将文件系统抽象适配为智能体间的通用接口。同时，近期研究如OpenHands、SWE-Agent关注单智能体执行环境供给，EnvX定义了环境初始化生命周期，Hassan等人提出了智能体执行环境的理论框架。**AWCP与这些工作的区别在于**，它专注于实现**跨智能体工作空间委托的具体协议**，使一个智能体能够将其工作空间投影给另一个智能体，而非仅关注单环境供给或理论构想。

### Q3: 论文如何解决这个问题？

论文通过提出一种名为“代理工作空间协作协议”（AWCP）的创新框架来解决远程代理间深度协作时执行环境隔离的问题。其核心方法是“工作空间投影”，即允许一个代理（委托方）将其本地工作空间（目录树）临时委托给远程代理（执行方），使执行方能够使用其本地的、未经修改的工具链直接操作共享文件，从而避免了复杂且易错的环境重建。

整体架构采用双层设计，严格分离控制平面与数据平面。主要组件包括运行在委托方和执行方上的专用AWCP服务。在委托方侧，服务包含**准入控制模块**（确保只有限定范围的工作空间被暴露）和**快照管理器**（在任务完成后协调结果）。在执行方侧，**执行器服务**接收委托请求并配置会话专用目录，并通过**可扩展适配器层**与不同的代理后端集成。两个服务通过两个协议层通信：**控制层**使用轻量级HTTP请求和服务器发送事件（SSE）来管理委托生命周期（包括会话协商、租约执行和状态同步）；**传输层**通过可插拔的适配器对（如SSHFS、Archive、Storage、Git）提供数据平面，负责工作空间的打包、传输和快照捕获。这种解耦设计使得控制逻辑独立于具体的文件传输机制。

关键技术体现在两个方面。一是**双状态机设计**，用于形式化委托生命周期并确保状态一致性。委托方运行一个包含九个状态（如created, invited, running, completed）的**DelegationStateMachine**，负责全生命周期管理；执行方运行一个仅包含四个状态（pending, active, completed, error）的**AssignmentStateMachine**，专注于任务执行。两者通过INVITE、ACCEPT、START、DONE等协议消息在关键点同步。二是**四阶段协议流程**：1) **协商阶段**：委托方发送INVITE提议任务，执行方回应ACCEPT或ERROR；2) **供应阶段**：委托方通过START消息启动数据传输，执行方配置工作空间访问；3) **执行阶段**：执行方使用本地工具操作文件，并通过SSE流式返回进度；4) **完成阶段**：委托方处理快照并确认，双方进行两阶段清理。

创新点在于：首次在代理协议栈中引入了“工作空间层”，通过临时的环境委托实现了超越消息传递的深度协作；其控制与传输分离的模块化架构，使得协议能灵活适配不同的网络拓扑和部署约束，而不改变核心协调逻辑；借鉴了“一切皆文件”的Unix哲学，使远程代理能获得“现场访问”能力，为构建普遍互操作的代理生态系统奠定了基础。

### Q4: 论文做了哪些实验？

论文通过两个现场协作演示实验来验证AWCP协议。实验设置方面，作者设计了两种体现不同不对称维度的协作场景，分别采用SSHFS和HTTP两种可插拔传输机制，并集成了MCP工具。

在数据集/基准测试上，第一个演示使用了一个包含100多张图像的杂乱目录，其中混合了损坏文件、空占位符和非图像文件；第二个演示则涉及一个包含多个Python脚本和依赖项的代码库。

对比方法上，论文主要与传统的基于消息传递的协作范式进行对比，后者需要代理在孤立环境中通过消息交换信息，无法直接操作对方工作空间。

主要结果方面，实验成功展示了跨能力、信任和领域知识不对称的深度协作。在第一个场景中，纯文本代理（Delegator）将杂乱图像目录委托给多模态代理（Executor），后者成功分类、过滤并重组了文件，所有文件操作通过FUSE挂载实时双向同步。关键数据指标包括：Executor直接操作了委托的文件，无需Delegator手动文件传输；文件操作（创建、删除、重命名）均实时同步。第二个场景中，安全代理通过HTTP传输委托代码库给开发代理，后者成功重构了代码，演示了跨信任边界的安全协作。两个实验均验证了AWCP能有效弥合上下文鸿沟，使代理能使用未修改的本地工具链直接操作共享文件。

### Q5: 有什么可以进一步探索的点？

该论文提出的AWCP协议虽在跨智能体深度协作上迈出重要一步，但仍存在若干局限和可探索方向。首先，协议的安全性机制尚显薄弱，临时工作区委托涉及敏感文件与工具链的远程暴露，需更精细的权限控制（如基于角色的访问、操作审计）和加密传输保障。其次，当前实现侧重于文件层面的共享，未来可扩展至更丰富的上下文共享，如数据库连接、GPU资源或特定软件许可证状态，以实现更全面的环境投影。此外，协议对动态协作场景的支持不足，例如多智能体同时写入冲突的协调、工作区状态的实时同步与版本管理，这些都是实际部署中必须解决的问题。从系统优化角度，可探索自适应传输机制，根据网络状况与任务类型在效率与一致性间权衡。最后，AWCP可结合学习机制，让智能体自动判断何时发起委托、选择最优执行器，从而提升协作系统的自主性与效率。

### Q6: 总结一下论文的主要内容

该论文针对当前基于大语言模型的自主智能体在协作时面临的环境隔离问题，提出了“智能体工作空间协作协议”（AWCP）。现有协作模式通常局限于消息传递，导致智能体无法直接操作对等方的文件或工具，只能进行低效且易错的环境重建。AWCP的核心贡献是引入了受Unix“万物皆文件”哲学启发的临时工作空间委托机制，将轻量级的控制平面与可插拔的传输机制解耦。这使得委托方（Delegator）能够将其工作空间投影给远程执行方（Executor），后者无需修改本地工具链即可直接操作共享文件。论文提供了开源的参考实现，并通过能力互补智能体间进行非对称协作的演示验证了协议的有效性。AWCP的主要意义在于为智能体协议栈补全了缺失的工作空间层，为实现超越消息边界、深度互操作的通用智能体生态系统奠定了基础。
