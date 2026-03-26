---
title: "APISENSOR: Robust Discovery of Web API from Runtime Traffic Logs"
authors:
  - "Yanjing Yang"
  - "Chenxing Zhong"
  - "Ke Han"
  - "Zeru Cheng"
  - "Jinwei Xu"
  - "Xin Zhou"
  - "He Zhang"
  - "Bohan Liu"
date: "2026-03-25"
arxiv_id: "2603.23852"
arxiv_url: "https://arxiv.org/abs/2603.23852"
pdf_url: "https://arxiv.org/pdf/2603.23852v1"
categories:
  - "cs.SE"
tags:
  - "Tool Use"
  - "Web Agent"
  - "API Discovery"
  - "Robustness"
  - "Agent Infrastructure"
  - "Unsupervised Learning"
  - "Software Engineering"
relevance_score: 7.5
---

# APISENSOR: Robust Discovery of Web API from Runtime Traffic Logs

## 原始摘要

Large Language Model (LLM)-based agents increasingly rely on APIs to operate complex web applications, but rapid evolution often leads to incomplete or inconsistent API documentation. Existing work falls into two categories: (1) static, white-box approaches based on source code or formal specifications, and (2) dynamic, black-box approaches that infer APIs from runtime traffic. Static approaches rely on internal artifacts, which are typically unavailable for closed-source systems, and often over-approximate API usage, resulting in high false-positive rates. Although dynamic black-box API discovery applies broadly, its robustness degrades in complex environments where shared collection points aggregate traffic from multiple applications. To improve robustness under mixed runtime traffic, we propose APISENSOR, a black-box API discovery framework that reconstructs application APIs unsupervised. APISENSOR performs structured analysis over complex traffic, combining traffic denoising and normalization with a graph-based two-stage clustering process to recover accurate APIs. We evaluated APISENSOR across six web applications using over 10,000 runtime requests with simulated mixed-traffic noise. Results demonstrate that APISENSOR significantly improves discovery accuracy, achieving an average Group Accuracy Precision of 95.92% and an F1-score of 94.91%, outperforming state-of-the-art methods. Across different applications and noise settings, APISENSOR achieves the lowest performance variance and at most an 8.11-point FGA drop, demonstrating the best robustness among 10 baselines. Ablation studies confirm that each component is essential. Furthermore, APISENSOR revealed API documentation inconsistencies in a real application, later confirmed by community developers.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决基于大语言模型（LLM）的智能体在操作复杂网络应用时，因API文档不完整或过时而面临的API发现难题。研究背景是，随着LLM智能体（如Openclaw）的兴起，它们需要通过调用API来操作网络应用，但API的实现因频繁的版本更新和功能迭代而快速演变，文档维护往往滞后，导致文档不完整、不一致甚至缺失。

现有方法主要分为两类：白盒方法和黑盒方法。白盒方法依赖于源代码或形式化规范，但其实际应用受限，因为大多数生产环境中的网络服务是闭源专有的，无法获取内部构件。此外，静态分析常采用过度近似来保守建模程序行为，可能导致发现代码中定义但运行时并未实际暴露的API（如仅用于内部服务调用的端点），产生高误报率。黑盒方法从运行时流量推断API，虽适用性更广，但在复杂环境中的鲁棒性不足。特别是在实际部署中，API流量通常在共享的网络网关处收集，这些网关汇聚了来自多个应用的流量，导致不同服务的请求相互交织，并混有背景流量（如静态资源请求）。这种异构混合流量使得现有黑盒方法难以正确将观察到的请求归因于实际暴露对应API的应用，性能显著下降。

因此，本文要解决的核心问题是：**如何在混合运行时流量（即多应用交织及含噪声的网关环境）中，实现鲁棒、准确的黑盒API发现**。具体而言，论文提出了APISENSOR框架，通过结合流量去噪、归一化以及基于图的两阶段聚类过程，从复杂的无标签流量中无监督地重建应用API，以提高在混合流量下的发现准确性和鲁棒性。

### Q2: 有哪些相关研究？

本文的相关研究主要分为两大类：白盒方法和黑盒方法。

**白盒方法**依赖于开发时工件，如源代码或API规范（如OpenAPI）。这类方法包括基于规范的静态分析、从源代码提取API信息的工具（如APIDocGen、RepoDocGen），以及将高层任务映射到API调用的研究（如TaskAPIRec）。它们能提供较全面的覆盖，但仅限于开源系统，且可能因规范过时或设计不一致而产生误报，无法反映实际的运行时使用情况。近期也有混合方法（如gDoc）结合静态分析与有限运行时信息。

**黑盒方法**从运行时流量或日志中推断API，无需内部工件。这包括开源工具（如Optic、Mitmproxy2Swagger）基于启发式方法从HTTP轨迹生成OpenAPI规范，以及更深入的研究：如APID2Spec通过爬取文档推断API、APICARV通过监控UI流量构建交互图、APIDrain3从流式流量中增量挖掘URL模板。此外，日志解析技术（如LogCluster、UniParser）通过抽象变量令牌来提取稳定模式，但主要依赖单个请求的词法模式，难以区分语义不同但URL结构相似的API操作。

**本文与这些工作的关系和区别**：APISENSOR属于黑盒方法，但针对现有动态方法的不足进行改进。现有黑盒工具（如Optic）在复杂环境（如混合流量、噪声干扰）下鲁棒性差，容易产生错误聚类或过度泛化。APISENSOR通过结合流量去噪、归一化以及基于图的两阶段聚类过程，在无监督下重建API，显著提升了在混合流量场景下的发现准确性和鲁棒性，解决了现有方法因依赖固定假设或浅层推理而导致的性能下降问题。

### Q3: 论文如何解决这个问题？

论文APISENSOR通过一个无监督的黑盒框架来解决从混合运行时流量中稳健发现Web API的问题。其核心方法是一个分层的、两阶段的处理流程，旨在从复杂、嘈杂的流量日志中逐步抽象和重构出准确的API资产。

整体框架由两大核心层构成：**流量去噪与规范化层**和**基于图的两阶段聚类层**。首先，针对流量多样性和噪声的挑战，框架对原始HTTP流量进行预处理。这包括两个关键步骤：1) **多信号噪声过滤**，通过级联的低成本检查（如静态文件扩展名、静态路径模式、Content-Type头信息）以及一个基于逻辑回归的轻量级健全性检查，过滤掉非API请求（如静态资源、网页）；2) **路径规范化**，通过剥离协议/主机、移除查询字符串、标准化路径格式，将请求路径转化为规范形式，为后续分析奠定基础。

预处理后，进入核心的**两阶段聚类过程**，以在无监督设置下实现高精度。第一阶段是**模板挖掘（结构视角）**。它使用Drain3算法将规范化后的路径插入一个固定深度的前缀树中，将仅因动态标识符（如用户ID）而不同的具体路径（如`/api/v1/items/123`）抽象为统一的接口级模板（如`/api/v1/items/*`）。这从结构上对请求进行了粗粒度分组，有效消除了动态路径片段带来的变异。

第二阶段是**语义细化（语义视角）**。针对同一结构模板下可能存在的不同行为，该阶段在每个模板组内进行细粒度划分。它为每个请求构建一个轻量级的语义特征向量，包括路径结构、查询参数和负载复杂性等特征。基于这些特征，在组内构建语义相似性图，仅在高相似度的请求对之间添加边。然后，采用图自编码聚类（DAEGC）等算法，通过最小化一致性损失和聚类正则化项，在嵌入空间中将具有一致行为的请求聚集在一起。如果样本不足或图不够稠密，则回退到K-means聚类以确保鲁棒性。

该方法的创新点在于：1) **级联去噪与规范化预处理**，显著提升了输入流量的质量；2) **结构先于语义的两阶段聚类架构**，先利用高效稳健的结构分析形成模板组，再在组内进行更具表达力的语义聚类，避免了过早合并和噪声干扰；3) **基于图的语义细化与自适应回退机制**，结合了图学习的表达能力和传统方法的稳定性。这种设计使得APISENSOR能够在混合流量环境中，以无监督的方式，高精度、高鲁棒性地发现API。

### Q4: 论文做了哪些实验？

论文实验设计围绕三个研究问题展开，旨在从不同角度评估APISENSOR（文中亦称APIGH）的有效性和鲁棒性。

**实验设置与数据集**：实验选取了六个开源Web应用作为评估对象，涵盖票务预订（Train-Ticket）、社交网络（Humhub）、笔记（Memos）、协同编辑（Overleaf）、云存储（Nextcloud）和LLM工作流平台（Dify），以覆盖不同功能域、架构（单体/微服务）和规模。通过本地部署并使用Burp Suite Pro代理捕获真实用户交互产生的HTTP(S)流量，共收集了超过10,000个运行时请求，并人工标注了真实API端点作为评估基准。为测试鲁棒性，实验构建了含噪声的数据集，引入了两种噪声：Lexify（模拟请求内部的词汇变异，如参数重排、编码变化）和Interfere（注入结构噪声，如静态资源、健康检查等无关HTTP请求）。

**对比方法**：实验与10种基线方法进行了对比，分为三类：1) 开源工具（如Optic、Mitmproxy2Swagger）；2) 基于日志的模板挖掘方法（如LogCluster、LogNgram、UniParser、LogPPT）；3) API流量驱动的端点发现方法（如WebAPISearch、APID2Spec、APICARV、APIDrain3）。

**主要结果与关键指标**：
1.  **有效性（RQ1）**：在六个应用上，APISENSOR在整体性能（FGA）上均优于所有基线，平均FGA达到94.91%。其平均组准确率精度（PGA）高达95.92%，在Overleaf和Train-Ticket上达到100%，在复杂的Dify上也达到98.89%，显示出高精度和跨项目的稳定性。
2.  **鲁棒性（RQ2）**：在混合流量噪声环境下，APISENSOR表现出最佳的鲁棒性，其性能方差最低。即使在噪声干扰下，其FGA下降最多仅为8.11个百分点，显著优于其他方法。
3.  **消融研究（RQ3）**：实验证实了APISENSOR的各个组件（流量去噪与归一化、基于图的两阶段聚类）对于整体有效性都是不可或缺的。

此外，APISENSOR还在一个真实应用中成功发现了API文档的不一致之处，并得到了社区开发者的确认。

### Q5: 有什么可以进一步探索的点？

该论文提出的APISENSOR框架在混合流量噪声环境下表现出色，但仍存在一些局限性，为未来研究提供了方向。首先，其评估主要基于模拟噪声，在真实世界更复杂、动态且包含加密或非标准协议流量的环境中，其鲁棒性有待进一步验证。其次，当前方法侧重于API端点的发现与分组，对API语义（如参数约束、行为描述）的推断能力有限，这限制了其在自动化API文档生成或智能体规划中的直接应用。

未来工作可沿几个方向深入：一是增强语义理解能力，结合自然语言处理技术分析请求/响应中的文本信息，或利用少量已知API作为种子进行半监督学习，以推断功能描述。二是探索实时或增量学习机制，以适应API的快速演变，而无需重新处理全部历史流量。三是将框架扩展至更广泛的协议（如gRPC、GraphQL）和架构（如微服务），并研究在存在对抗性干扰流量时的防御能力。此外，如何将发现的API结构与LLM智能体进行有效集成，以支持更可靠的自动化工具使用，也是一个极具价值的应用探索点。

### Q6: 总结一下论文的主要内容

本文针对LLM智能体依赖的Web API文档不完整或过时的问题，提出了一种名为APISENSOR的鲁棒性API发现框架。其核心贡献在于，在无法获取源代码的闭源系统及多应用流量混合的复杂运行时环境中，实现了高精度的无监督API重构。

现有方法分为依赖内部工件的静态白盒方法和从流量推断的动态黑盒方法，前者适用范围有限且误报率高，后者在混合流量场景下鲁棒性不足。APISENSOR属于动态黑盒方法，其创新方法包含对复杂流量进行结构化分析，具体结合了流量去噪与规范化，以及一个基于图的两阶段聚类过程，以从混合流量中准确恢复出各应用的API。

实验在六个Web应用上使用超万条含模拟噪声的运行时请求进行评估。结果表明，APISENSOR显著提升了发现精度，平均分组准确精度达95.92%，F1分数达94.91%，优于现有最佳方法，并且在各种噪声设置下性能方差最低，表现出最佳的鲁棒性。消融研究证实了各组件均不可或缺。此外，APISENSOR还在一个真实应用中成功发现了API文档的不一致之处，并得到了社区开发者的确认。
