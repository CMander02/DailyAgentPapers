---
title: "Data Journalist Agent: Transforming Data into Verifiable Multimodal Stories"
authors:
  - "Kevin Qinghong Lin"
  - "Batu EI"
  - "Yuhong Shi"
  - "Pan Lu"
  - "Philip Torr"
  - "James Zou"
date: "2026-06-09"
arxiv_id: "2606.11176"
arxiv_url: "https://arxiv.org/abs/2606.11176"
pdf_url: "https://arxiv.org/pdf/2606.11176v1"
github_url: "https://github.com/QinghongLin/data2story-skill"
categories:
  - "cs.CV"
  - "cs.CL"
  - "cs.CY"
  - "cs.HC"
tags:
  - "多智能体系统"
  - "数据驱动叙事"
  - "评测基准"
  - "可信性验证"
  - "多模态生成"
relevance_score: 7.5
---

# Data Journalist Agent: Transforming Data into Verifiable Multimodal Stories

## 原始摘要

Data tells stories that shape society; the data journalist's job is to turn raw information into stories non-experts can trust. A high-quality news feature takes a newsroom team weeks: hunting for context, running statistics, choosing an angle, and designing visuals. Recent agents handle individual steps well: data-science agents close the analysis loop, while design agents synthesize beautiful websites. But can an agent serve as a data journalist end to end? We introduce Data Journalist Agent (Data2Story), a multi-agent framework that orchestrates specialized roles into a single virtual newsroom. Data2Story contributes two innovations. (i) Claims are evidence-grounded: an Inspector links every number, angle, and asset back to data, code, or an external reference. (ii) Articles are multimodally generative: rather than defaulting to plain text and static charts, Data2Story reasons about what readers will want to see, then deploys multimodal tools, such as interactive maps for geography and audio for music. We evaluate Data2Story on 18 articles, each paired with the originally published expert piece, along four axes: (a) human-agent angle coverage; (b) rubric evaluation with 53 participants across five dimensions; (c) computer-use agents as judges, a cost-saving proxy for how readers navigate interactive articles; and (d) verifiability, where a coding verifier re-executes statements against the data and checks claims against references. Data2Story produces competitive, evidence-traceable multimedia stories, with particular strength in transparency and auditability. Human articles retain an edge in editorial angle, creative design, and presentation. We position Data2Story as a collaborator for journalists, enabling more evidence-based, transparent, and verifiable reporting. Code and demos are available at https://data2story.github.io.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决数据新闻制作过程中的一个核心挑战：能否构建一个端到端、可信且多模态的AI智能体，以完成从原始数据到可验证、可读性强的新闻故事的全流程自动生成。研究背景是，传统高质量数据新闻的制作耗时数周，需要新闻团队协作完成背景搜集、统计分析、角度选择、可视化设计等多个专业步骤。现有方法虽针对单一步骤有较好表现（如数据科学智能体可完成分析闭环，设计智能体可合成网页），但缺乏集成度和端到端能力。更关键的是，当前商业化AI新闻系统存在缺乏验证与可追溯性的核心不足，读者和编辑无法确认数据来源、图表准确性或事实性声明的真伪，AI智能体固有的幻觉问题使得这一挑战尤为严峻。为弥补这些不足，本文提出Data Journalist Agent（Data2Story）框架，其核心创新在于：①通过引入“Inspector”智能体将所有数字、角度和素材链接回数据、代码或外部参考文献，确保每个声明都有证据支撑，从而实现完全可审计；②文章以多模态生成方式呈现，即根据读者需求自动选择交互式地图、音频等丰富媒体形式，而非仅生成静态文本和图表。因此，本文试图解决的核心问题是：如何构建一个多智能体协作系统，使其能像专业新闻团队一样，端到端地生成具有证据可追溯性、多模态丰富性且读者乐于阅读和信任的数据新闻故事。

### Q2: 有哪些相关研究？

与本文相关的研究主要分为三类。首先是**搜索智能体**，如MindSearch、MMSearch和DR Tulu，这些系统能够自主浏览网页并生成基于检索增强的文本报告。它们擅长收集和综合外部证据，但输出形式局限于以来源为中心的文本，缺乏叙事角度构建和多模态生成能力。相比之下，本文的Data2Story不仅进行外部搜索，还围绕特定叙事角度组织内容，并生成包含图片、视频、音频和交互元素的多模态文章。

其次是**数据可视化智能体**，例如LIDA、MatplotAgent和CoDA。这些系统能将表格数据转换为可视化代码或信息图表，但它们通常假设数据集是固定的，不主动搜索外部证据，且输出多为静态视觉制品。Data2Story则在此基础上实现了对外部来源的主动搜索、交互式多模态输出以及完整的证据追溯链。

第三类是**数据科学智能体**，如Data Interpreter、DSGym和AI Scientist。它们结合代码执行来处理数据任务，但输出形式通常是结构化文本或PDF报告，缺乏为普通读者设计的多媒体叙事呈现。Data2Story的创新在于将数据分析直接包装成类似数据新闻的多媒体文章，而非静态文档。

最后，在**数据新闻智能体**方面，LLM writer虽能生成叙事角度，但缺乏多模态能力。人类记者虽产出多媒体文章，但多数缺乏代码级来源追溯。Data2Story通过融合七个专业角色的多智能体框架，在保证可验证性的同时，实现了全面多模态和证据追溯（代码引用和URL链接），从而与现有工作形成显著区别。

### Q3: 论文如何解决这个问题？

Data2Story通过构建一个多智能体虚拟新闻编辑室，将数据转化为可验证的多模态故事。其核心架构包含七个专业化角色：侦探（Detective）通过网页搜索获取外部上下文，增强原始数据集；分析师（Analyst）枚举数据支持的所有统计分析，并附带可追踪代码，确保每个发现都有代码行级来源；编辑（Editor）从分析结果中筛选关键发现，制定编辑计划并撰写段落大纲；设计师（Designer）针对每个发现选择合适的多媒体工具（如地图、音频、视频）生成视觉资产；程序员（Programmer）将上游成果组装成交互式HTML页面，并支持根据审计建议进行修订；审计员（Auditor）检查页面中的视觉或结构缺陷；督察员（Inspector）将页面中的每个片段（句子、图表、交互元素）链接回其支撑证据（包括代码、数据、上下文引用等），建立完整的证据链条。

关键技术包括：1）多重证据绑定机制，确保每个声明都能追溯至具体代码行或外部引用；2）多模态生成能力，能根据数据特征自动选择最佳可视化形式；3）迭代修订流程，通过审计-修订循环提升输出质量。创新点在于将数据新闻的整个生产流程端到端自动化，同时保证可审计性和透明度，使每个数字、角度和资产都有据可查。

### Q4: 论文做了哪些实验？

论文在18篇来自《经济学人》《布丁》和TidyTuesday的数据故事文章上评估了Data2Story，涵盖科学、体育、政治、健康等多领域及时序、表格等数据模态。实验设置了四个评估维度：(a) 人类-智能体角度覆盖，使用gpt-4o-mini和text-embedding-3-small提取并匹配事实声明，计算P(Agent|Human)和P(Human|Agent)覆盖率；(b) 通过Prolific平台招募53名评审员，在视觉设计、叙事与节奏、数据与方法透明性、声明-数据一致性、洞察价值五个维度上对人工与智能体文章进行1-7分盲评，并给出偏好选择；(c) 使用跨家族计算机使用智能体（OpenAI的gpt-5.5-xhigh）作为评审员，以节省成本，模拟读者交互操作评估文章；(d) 可验证性，用跨家族验证器（OpenAI的Codex-GPT-5.4）重新执行代码并核对声明，给出二元判断。主要结果是：Data2Story能生成竞争性的、证据可追溯的多媒体故事，在透明度与可审计性上表现突出，但人工文章在编辑角度、创意设计与呈现上仍具优势。

### Q5: 有什么可以进一步探索的点？

这篇论文提出的Data2Story框架虽在数据驱动新闻自动化方面取得进展，但仍存在若干局限与未来探索空间。首先，其证据溯源机制依赖外部代码和显式引用，难以处理隐含知识或采访素材中的主观论断，未来可引入语义推理或专家规则补全证据链。其次，多模态生成目前为工具调用式的组合（如地图、音频），缺乏对叙事节奏与视觉设计的深度美学优化，可借鉴Diffusion模型或神经渲染实现更自然的图文融合。再者，评估依赖53位参与者的主观评分，样本量有限且可能存在文化偏好偏差，未来可构建跨领域、多语言的基准数据集并引入自动化叙事连贯性指标。最后，端到端新闻生产仍面临编辑角度筛选的瓶颈，可探索结合大语言模型的意图识别与强化学习，使智能体在角度选择、证据权重分配上实现动态优化。此外，将代理与人类记者协作的工作流标准化，例如设计可解释的交互界面让记者实时干预故事策略，将是人机协同新闻的重要方向。

### Q6: 总结一下论文的主要内容

该论文提出了Data2Story，一个多智能体框架，旨在将原始数据端到端地转化为可验证的多模态新闻故事。核心问题在于，现有AI新闻系统缺乏可验证性和可追溯性，易产生幻觉。方法上，Data2Story构建了一个虚拟编辑部，包含侦探、分析师、编辑、设计师、程序员等七个专业角色，并创新性地引入了“检查员”角色，负责将文章中的事实、数字和视觉元素链接回其原始证据（如代码、数据源）。其主要贡献在于：一是实现基于证据的声明，确保可审计；二是生成多模态内容，根据主题自动选择交互式地图、音频等最佳表现媒介。在18个样本上的评估显示，Data2Story能产出有竞争力、证据可追溯的多媒体故事，在透明度和可审计性上表现突出。论文的意义在于，它定位为记者的协作工具而非替代品，能处理劳动密集型计算和图形设计，从而赋能更基于证据、透明和可核查的报道。
