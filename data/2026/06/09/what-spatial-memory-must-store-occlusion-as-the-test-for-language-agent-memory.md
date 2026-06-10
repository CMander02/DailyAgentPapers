---
title: "What Spatial Memory Must Store: Occlusion as the Test for Language-Agent Memory"
authors:
  - "Doeon Kwon"
  - "Junho Bang"
date: "2026-06-09"
arxiv_id: "2606.10299"
arxiv_url: "https://arxiv.org/abs/2606.10299"
pdf_url: "https://arxiv.org/pdf/2606.10299v1"
categories:
  - "cs.AI"
  - "cs.CV"
  - "cs.MA"
tags:
  - "Agent记忆"
  - "空间记忆"
  - "记忆召回"
  - "几何推理"
  - "Agent评测"
  - "坐标锚定"
  - "消融实验"
relevance_score: 8.5
---

# What Spatial Memory Must Store: Occlusion as the Test for Language-Agent Memory

## 原始摘要

Language-agent "memory palace" systems anchor each memory to a world coordinate, on the intuition that geometry adds something text cannot. We make that intuition testable and report three results. First, the memory-palace default of folding spatial proximity into a linear blend beside recency and importance does not help and can hurt: in a pre-registered recall experiment the shipped blend fails its own frozen test (mean Delta-Hit@5 -0.0375, Wilcoxon p=0.306), sitting at a position-blind baseline, while a geometry-led weighting wins decisively (+0.3208, p<10^-15): geometry must lead recall when the query regime is spatial. Second, memory recall and visibility must be separated: recall is occlusion-blind by design (you correctly remember the next room behind a wall), while visibility is a perception predicate over stored geometry that the live system never computed. A one-line ray-versus-voxel digital differential analyzer (DDA), re-pointed from the gaze ray the agent already casts, supplies it: text and the live FoV cone both score 0.000 on 849 behind-wall targets while cone-plus-DDA reaches 0.982 (exact McNemar p<10^-6); coordinate recall separately resolves near-duplicate locations a cosine null cannot (1.000 vs 0.533, n=150). Third, the visibility predicate is confirmed live under a git-committed pre-registration (SPMEM-OCC-LIVE-v1: eight scripted worlds, automated oracle scoring, 96 behind-wall targets, false-visible 1.000->0.000, pooled exact McNemar p=2.5x10^-29), a run that surfaced and fixed a real relay anchor defect. We concede that occlusion-needs-geometry is near-tautological; the contribution is the measurement and isolation, separating what spatial memory must store from how it is read. These pilots power a frozen confirmatory study (SPMEM-ZERO-REAL-PREREG-v1); the full human-authored multi-world study with blind raters remains future work.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决语言智能体系统中空间记忆存储的核心问题：几何信息究竟为记忆检索带来了哪些纯文本无法提供的独特价值。研究背景是，近年来出现了一系列语言智能体系统，其中一种颇具特色的“记忆宫殿”系统将每条记忆锚定到世界坐标，期望几何位置能提供额外的检索线索。然而，现有方法存在明显不足：主流做法将空间邻近性简单地与时效性和重要性线性混合，但在召回实验中，这种混合策略的性能与无视位置的基线持平甚至更差，被实验证实无效。此外，许多系统混淆了“记忆召回”（根据位置检索信息，对遮挡不敏感，能正确回忆墙后房间）与“可见性判断”（感知谓词，判断目标是否在当前视角可见）这两个不同操作。本文要解决的核心问题是：精确定义并隔离测量空间记忆必须存储的、纯文本无法替代的核心几何信息。作者通过严谨实验证明，处理遮挡（计算视线是否被阻挡）是几何信息不可或缺的测试用例，而坐标召回与可见性判断是两套独立的机制，必须先分离理解。最终，论文贡献不在于提出新系统，而在于通过测量与隔离，明确了空间记忆“存什么”（存储几何信息）和“怎么读”（是位置召回还是可见性判断）的明确界限。

### Q2: 有哪些相关研究？

相关研究可分为五个类别。**代理记忆系统**方面，Generative Agents通过新颖度、重要性和相关性加权评分，是文本记忆基线；MemGPT采用操作系统式内存层级；A-MEM构建Zettelkasten笔记图；Mem0提取事实；Zep/Graphiti维护时序知识图谱。本文与之区别在于：空间锚点是免提取的结构先验，研究焦点是几何信息中真正起作用的部分。**空间与具身记忆**方面，3D-Mem用多视图快照表征场景；3DSPMR将视场覆盖作为几何先验，但其将几何折叠进综合排名项，而本文通过预注册实验分离了几何作为验证谓词与混合排名项的效果，并解耦了遮挡盲召回与独立可见性查询。**渲染即召回**方面，GSMem和RenderMem通过渲染恢复遮挡内容，但本文使用权威体素占用而非3DGS重建，并证明坐标存储而非渲染器是不可或缺的。**世界模型与缺失的记忆层**方面，Gen-erative Agents等无几何记忆系统无法回答可见性问题，而世界模型聚焦瞬时循环，本文补充了持久化层。**检索方法**方面，BM25、RAPTOR、GraphRAG等均无法处理遮挡查询。

### Q3: 论文如何解决这个问题？

该论文通过系统性实验分离“空间记忆必须存储什么”与“如何读取空间记忆”两个问题，核心贡献在于用测量和隔离方法证明了几何信息（尤其是遮挡关系）的必要性。整体框架包含三个对比记忆系统：M0（纯文本基线，无坐标）、M1b（坐标召回，仅用3D欧氏距离排序）、M3a/M3-occ（可见性感知分支）。关键组件包括：利用Zero工具中的数字微分分析器（DDA）射线与体素场交互，通过isSolidAt原语读取真实几何信息；采用“中继锚点”机制将记忆绑定到观察到的网格单元中心（subjectPosition），而非智能体位置；可见性判断复用已有DDA射线，只需将射线从“智能体看向注视点”重定向为“智能体看向候选目标”。创新点有三：一是几何主导的空间权重（M1b）显著优于默认的线性混合召回（Delta-Hit@5 +0.3208）；二是将召回（遮挡无关）与可见性判断（遮挡相关）明确分离，后者通过单行DDA射线实现（cone+DDA对墙后目标准确率0.982，而纯cone为0.000）；三是通过git预注册的在线实验（SPMEM-OCC-LIVE-v1）验证可见性谓词，修复了中继锚点缺陷。整个方法强调复用已有基础设施而无需新增几何数据结构。

### Q4: 论文做了哪些实验？

论文报告了一系列受控实验，分为三个主要部分。**实验1（近重复定位）** 在实时中继上使用150个试验，对比坐标召回（M1b）与纯文本余弦基线（M0）。M1b准确率达1.000，M0仅0.533，不对称对（70 vs 0）在精确McNemar检验中p<10^-6，证明几何坐标能解决文本无法区分的相同内容记忆。**实验2（遮蔽测试）** 在受控体素世界中，使用1144个锥内目标（849个被墙遮蔽，295个可见），比较文本（M0）、视场锥（M3a）与锥加DDA视线（M3-occ）。M0和M3a在遮蔽目标上准确率均为0.000（假可见率1.000），而M3-occ达到0.982（假可见率0.018），精确McNemar p<10^-6。**实验3（完整方法景观）** 在三个内容领域和四种几何必要查询类型上，以每单元格160个试验对比BM25、稠密检索、混合、RAPTOR、生成式智能体和HippoRAG，所有文本/RAG方法在几何必要查询上均处于机会水平（~0.46-0.47），而几何感知臂达到1.000。**实验4（行动消融）** 在24个情境警示场景中，世界绑定记忆的行动准确率为1.000，而扁平化为文本后降至0.625，配对McNemar p=0.0039。最后，**Tier-A电池**覆盖六种几何必要查询类型（每种400个试验），几何臂在所有类型上均优于文本空值（p<10^-6，经Holm校正），而文本充足控制组验证了反转效应。

### Q5: 有什么可以进一步探索的点？

论文的局限性和未来探索方向主要集中在以下几个方面。首先，当前研究仅验证了空间记忆在遮挡场景下的必要性，但未深入探讨几何信息与其他记忆权重（如时间近性、重要性）的最优融合方式。未来可设计动态权重机制，根据查询场景自动调整几何主导与语义引导的比例。其次，实验基于合成世界和脚本化任务，未来需在真实复杂环境中验证，如动态遮挡、多智能体协作场景。此外，可见性判别依赖简单的DDA射线追踪，未利用深度学习对部分遮挡进行概率建模，可探索神经辐射场（NeRF）等隐式几何表达来提升鲁棒性。另一个关键点是记忆存储与读取的分离设计——当前系统严格区分坐标存储与查询策略，但未评估跨模态（如文字描述与几何坐标）的互补性，可研究混合索引结构（如分层锚点+语义标签）以平衡精确性与灵活性。最后，预注册实验发现的中继锚点缺陷提示我们需要更系统的稀疏位置编码策略，例如结合拓扑图与度量嵌入来应对长程记忆漂移。

### Q6: 总结一下论文的主要内容

这篇论文探讨了语言智能体的空间记忆系统，核心目标是明确空间几何信息在记忆中不可替代的作用，即“空间记忆必须存储什么”。作者首先定义了问题：现有系统将坐标嵌入存储，但并未证明几何信息带来的增益超越了纯文本。主要方法包括：通过预注册的召回实验（Delta-Hit@5 -0.0375 vs +0.3208）证明，基于几何的加权检索远优于默认的线性混合；区分了“记忆召回”（对位置敏感的回忆，可穿透遮挡）与“可见性谓词”（基于几何的视线判断，文本无法计算）。核心贡献是隔离并度量了这两者，证明了遮挡问题必须依赖存储的几何信息，而非文本或视野锥（FoV）。主要结论是，用一行射线与体素交叉算法（DDA）即可从存储几何中计算可见性（准确率达0.982），并在真实系统预注册实验中确认了其必要性（精确McNemar检验p=2.5×10^-29）。该研究通过测量与隔离，为空间记忆系统提供了基础性设计原则。
