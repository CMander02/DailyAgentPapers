---
title: "Exploring Cross-Scenario Generality of Agentic Memory Systems: Diagnostics and a Strong Baseline"
authors:
  - "Zhikai Chen"
  - "Jialiang Gu"
  - "Junyu Yin"
  - "Xianxuan Long"
  - "Shenglai Zeng"
  - "Xiaoze Liu"
  - "Kai Guo"
  - "Keren Zhou"
  - "Jiliang Tang"
date: "2026-06-03"
arxiv_id: "2606.04315"
arxiv_url: "https://arxiv.org/abs/2606.04315"
pdf_url: "https://arxiv.org/pdf/2606.04315v1"
categories:
  - "cs.AI"
tags:
  - "Agent记忆系统"
  - "多场景泛化"
  - "工具接口"
  - "Agent评测"
  - "LLM Agent"
relevance_score: 8.5
---

# Exploring Cross-Scenario Generality of Agentic Memory Systems: Diagnostics and a Strong Baseline

## 原始摘要

LLM agents accumulate histories that outgrow their context windows, motivating a growing literature on memory systems. Yet most existing designs are tuned to a single scenario (multi-session chat or a single trajectory format), and there is little evidence that they generalize across the heterogeneous trajectories agents encounter in deployment. We revisit eight memory systems plus an agentic harness for search problems, on five scenarios: single-turn QA, multi-session chat, agentic-trajectory QA, memory stress tests, and long-horizon agentic tasks. The harness, which self-manages flat text-file storage via tool calls, achieves the best cross-task ranking, suggesting that memory performance hinges on giving the agent active control over storage and retrieval rather than on a passive store behind a fixed pipeline. We instantiate this insight in AutoMEM, an agentic memory harness with a self-managed tool interface that achieves the best cross-scenario generality among the systems we evaluate.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决现有智能体记忆系统在跨场景泛化能力上的严重不足。研究背景是，大语言模型已从单轮对话演变为能执行复杂任务的通用智能体，需要记忆系统来管理超出上下文窗口的历史信息。然而，现有记忆系统大多是“场景狭隘”的：它们通常针对单一场景（如多轮聊天或单一路径的任务轨迹）进行调优，其设计特性在不同场景下的表现差异巨大。论文指出，在部署环境中，智能体会遇到异构的轨迹（包括多轮聊天、代码交互、浏览器日志等），而现有系统缺乏证据表明其能很好地泛化到这些不同场景。核心问题是如何设计一个能有效跨越多种异构任务的通用记忆系统。作者通过实验发现，现有系统存在两种失败模式：一是表示层面的失败，即构建时的固定模式会丢弃步骤和动作级别的证据；二是检索层面的失败，即被动检索无法获取存储中的信息。为解决此问题，论文提出一个强基线方法——AutoMEM，这是一个通过工具调用实现自我管理的智能体记忆框架，它在跨场景泛化能力上显著优于现有系统，实现了最佳的整体性能。

### Q2: 有哪些相关研究？

本文的相关工作可分为方法类和评测类。方法类方面，现有记忆系统在存储粒度上分层设计：基线使用原始分块和相似性检索，而更丰富的设计包括原子笔记（适合演化稳定事实）、OS式分层内存（通过工具调用在有限工作区和长期区间分页）和基于图的存储（适合多跳组合）。在检索上，除默认形式外，还有RL训练工具策略和多阶段检索。但这些方法多针对单一场景（如多会话聊天），缺乏跨异构轨迹的泛化证据。效率类方法包括压缩、离线委派和成本分层路由，主要验证于对话问答，未在智能体工作负载上测试。评测类方面，现有基准分为三类：QA基准（如对话历史问答）、智能体QA基准（如AMA-Bench、SAGE，测试智能体轨迹因果依赖或深度研究检索）、真实任务基准（如MemoryArena，通过环境循环评测）。但现有基准多针对单一类别，未对跨任务、成本和延迟进行系统比较。本文与上述工作的区别在于：提出自管理扁平文件存储的工具接口（AutoMEM），通过赋予智能体主动控制存储和检索而非固定管道，实现跨场景通用性；并构建了包含五个场景（单轮QA、多会话聊天、智能体轨迹QA、记忆压力测试、长程任务）的系统评测，填补了跨场景泛化证据的空白。

### Q3: 论文如何解决这个问题？

该论文通过提出AutoMEM框架解决了智能体记忆系统在跨场景下的泛化性问题。核心方法是将记忆系统的主动控制权交给智能体本身，而非依赖固定管道。整体框架采用**规划-执行-判断**的智能体循环，主要包含三个模块：

1. **规划器（Planner）**：从四个动作（`rg`正则搜索、`read`按ID读取、`dump`批量发送、`index_query`索引查询）中选择一个操作，由单一LLM骨干网络执行。

2. **执行器（Executor）**：调用工具对记忆存储进行操作，无需LLM参与，将结果追加到运行轨迹中。

3. **判断器（Judge）**：检查轨迹是否足以回答问题。若充足则交由回答器生成最终答案；若不足则返回缺少内容的提示，重新调用规划器。

关键技术包括：
- **自管理工具接口**：智能体通过工具调用自主控制纯文本文件存储，而非被动存储。
- **双变种索引**：默认使用LightMem的Cypher图索引（含SAID_BY等关系），可选PlugMem的标签/语义/情景存储（含HAS_TAG等关系）。
- **效率优化**：包括KV缓存友好的对话布局（将指令块放在系统消息中，提升前缀缓存命中率至50%以上）和单次并行处理模式（`K_max=1`，并行执行读取操作，减少66-72%查询token）。

创新点在于：证明记忆性能的关键在于赋予智能体对存储和检索的主动控制权，而非被动存储结构。AutoMEM在LoCoMo基准上达到67.3%准确率，比长上下文基线提升5.8个百分点，平均排名3.10优于所有对比方法。

### Q4: 论文做了哪些实验？

论文在五个场景上评估了8种记忆系统和DCI-Lite基线：个人聊天助手（LoCoMo）、大语料检索（HotpotQA）、轨迹问答（AMABench-ALF/Web/T2SQL）、记忆压力测试（MemoryAgentBench的AR/TTL/LRU/CR子任务）以及真实代理任务（ALFWorld、MemoryArena购物/旅行）。对比方法包括无记忆（长上下文）、SimpleMem、LightMem、HippoRAG、PlugMem、AMA-Agent、DCI-Lite、DCI-Lite+Sum、Mem-T和MemRL。主要结果通过LLM评判分数（LoCoMo、HotpotQA等）和任务成功率（ALFWorld的SR、MA-Shop的PS、MA-Travel的c-sPS）衡量。DCI-Lite在所有基准测试中平均分数排名最佳（总体排名3.67），而长上下文在多个任务上仍具竞争力（如LoCoMo 61.5、ALFWorld 46.7）。索引方法依赖构建时间结构，在轨迹问答上表现较差（如AMABench中多种方法得分低于26%），且成本效率较低（如HippoRAG每问题需~130K令牌预计算成本），而DCI-Lite通过查询时灵活检索实现更优泛化性。

### Q5: 有什么可以进一步探索的点？

论文的局限性主要体现在两方面：一是AutoMEM未实现分层预算路由，其规划、判断和答案生成均使用同一强模型，而前两者难度较低，若引入廉价模型路由可将推理成本降低2-3倍；二是评判协议对会话型QA的绝对分数敏感，严格事实评判影响了不同方法间的排序稳定性。未来研究方向包括：1）实现自适应资源分配，通过任务难度感知路由优化成本效率；2）探索更鲁棒的跨场景评估协议，降低评判者偏差对方法排名的干扰；3）当前研究仅验证了工具化存储接口的有效性，可进一步研究记忆系统与推理过程的动态协同机制，例如让智能体在检索时自动调整记忆粒度；4）扩展至更复杂的多智能体协作场景，验证主动存储控制机制在分布式记忆管理中的泛化能力。

### Q6: 总结一下论文的主要内容

这篇论文系统性地评估了现有 LLM Agent 记忆系统在跨场景下的通用性。作者发现，大多数记忆系统仅针对单一场景（如多轮对话或单轨迹格式）进行优化，在混合异构轨迹的部署场景中表现不佳。论文首先对八种记忆系统及一个搜索问题工具框架进行了诊断，覆盖了单轮问答、多轮对话、Agent轨迹问答、记忆压力测试和长周期Agent任务五种场景。核心发现是：没有现有记忆系统在所有任务族上都胜出，而一个具备主动存储与检索控制能力的Agent工具框架反而取得了最佳的跨任务排名。基于此洞察，作者提出了AutoMEM，一种通过自管理工具接口实现Agent主动操控存储与检索的记忆框架。AutoMEM在跨场景通用性上达到了最优，并揭示了记忆性能的关键在于赋予Agent主动控制能力，而非依赖固定的被动管道。该工作为构建更通用的Agent记忆系统建立了新的基线和设计方向。
