---
title: "Benchmarking MLLM-based Web Understanding: Reasoning, Robustness and Safety"
authors:
  - "Junliang Liu"
  - "Jingyu Xiao"
  - "Wenxin Tang"
  - "Zhixian Wang"
  - "Zipeng Xie"
date: "2025-09-26"
arxiv_id: "2509.21782"
arxiv_url: "https://arxiv.org/abs/2509.21782"
pdf_url: "https://arxiv.org/pdf/2509.21782v2"
categories:
  - "cs.AI"
tags:
  - "Reasoning & Planning"
  - "Perception & Multimodal"
relevance_score: 8.0
taxonomy:
  capability:
    - "Reasoning & Planning"
    - "Perception & Multimodal"
  domain: "General Purpose"
  research_type: "Benchmark/Evaluation"
attributes:
  base_model: "N/A"
  key_technique: "WebRRSBench"
  primary_benchmark: "WebRRSBench"
---

# Benchmarking MLLM-based Web Understanding: Reasoning, Robustness and Safety

## 原始摘要

Multimodal large language models (MLLMs) are increasingly deployed as the core reasoning engine for web-facing systems, powering GUI agents and front-end automation that must interpret page structure, select actionable widgets, and execute multi-step interactions reliably. However, existing benchmarks largely emphasize visual perception or UI code generation, showing insufficient evaluation on the reasoning, robustness and safety capability required for end-to-end web applications. To bridge the gap, we introduce a comprehensive web understanding benchmark, named WebRRSBench, that jointly evaluates Reasoning, Robustness, and Safety across eight tasks, such as position relationship reasoning, color robustness, and safety critical detection, etc. The benchmark is constructed from 729 websites and contains 3799 QA pairs that probe multi-step inference over page structure, text, widgets, and safety-critical interactions. To ensure reliable measurement, we adopt standardized prompts, a protocolized and deterministic evaluation pipeline, and multi-stage quality control combining automatic checks with targeted human verification. We evaluate 11 MLLMs on WebRRSBench. The results reveal significant gaps: models still struggle with compositional and cross-element reasoning over realistic layouts, show limited robustness when facing perturbations in user interfaces and content such as layout rearrangements or visual style shifts, and are rather conservative in recognizing and avoiding safety critical or irreversible actions. Our code and appendix are available at https: //github.com/annoy-worker/WebRSSBench.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前多模态大语言模型在面向网页的实际应用中所面临的核心能力评估不足的问题。研究背景是，随着MLLMs被越来越多地部署为网页自动化系统（如GUI智能体）的核心推理引擎，它们需要可靠地理解网页结构、选择可操作组件并执行多步交互。然而，现有的网页相关评测基准（如VisualWebBench、WebUIBench等）主要侧重于视觉感知或UI代码生成，存在明显不足。

现有方法的不足主要体现在三个方面：首先，**推理能力评估不足**，现有基准忽视了MLLMs对UI元素间空间位置关系和语义角色的理解能力，而这正是GUI智能体进行可靠交互的基础。其次，**缺乏鲁棒性和安全性评估**，现有基准的网页集合缺乏对抗性测试案例（如布局重组、视觉风格变化），未能系统评估模型在分布变化或面对潜在风险元素（如删除账户按钮）时的表现，而这对于实际部署至关重要。最后，**可扩展性有限**，大多数基准设计静态，难以通过编程方式扩展新的测试用例或评估维度，限制了其长期效用。

因此，本文要解决的核心问题是：**如何构建一个全面、系统的评测基准，以联合评估MLLMs在端到端网页应用场景下所必需的推理、鲁棒性和安全能力**。为此，作者提出了WebRRSBench基准，通过引入位置关系推理、表单填写等新任务、设计布局/颜色/文本扰动方法以及安全关键检测任务，来填补上述评估空白，并为网页理解与智能自动化的发展提供新的评估标准。

### Q2: 有哪些相关研究？

本文的相关研究主要分为网页理解基准和网页代码生成基准两大类。

在网页理解基准方面，已有研究关注用户界面（UI）属性（如字体、颜色）、整体页面理解以及OCR和文本功能。这些工作侧重于模型的感知和理解能力，但普遍忽略了跨元素的推理以及对抗性扰动对模型性能的影响。本文提出的WebRRSBench旨在填补这一空白，通过联合评估推理、鲁棒性和安全性，为网页理解领域的MLLM评估设立了新标准。

在网页代码生成基准方面，早期工作如WebSight和Web2Code通过网页代码生成基准（WCGB）开创了HTML代码合成和系统评估，但依赖于合成数据。后续研究如Design2Code引入了首个基于真实网页的基准，而WebCode2M则扩展了数据规模。此外，还出现了针对特定方面的专门基准，如交互式生成（Interaction2Code）、多页面资源感知网站（MRWeb）以及基于多任务框架的UI生成、编辑和修复（DesignBench）。这些基准共同为MLLM网页开发能力的不同维度提供了全面的评估框架。

本文与上述工作的主要区别在于：现有基准大多强调视觉感知或UI代码生成，对端到端Web应用所需的推理、鲁棒性和安全能力评估不足。WebRRSBench则构建了一个包含八个任务（如位置关系推理、颜色鲁棒性、安全关键检测等）的综合基准，专注于评估模型在真实网页布局下的组合推理、对抗扰动下的稳健性以及安全交互的识别能力。

### Q3: 论文如何解决这个问题？

论文通过构建一个名为WebRRSBench的综合基准测试来解决现有评估在端到端网络应用所需推理、鲁棒性和安全能力方面的不足。其核心方法是设计一个系统化的评估框架，该框架包含八个具体任务，覆盖了推理（如位置关系推理、UI分组、表单填写、提示文本预测）、鲁棒性（针对颜色、文本、布局的对抗性扰动）和安全性（安全关键检测）三个维度。

整体架构设计基于从729个真实世界网站收集的3799个问答对。关键技术包括：1）**数据集构建**：从现有数据集（如Mind2Web、WebMMU）筛选并补充设计社区网页，确保样本针对特定评估维度。2）**对抗性样本生成**：为评估鲁棒性，论文设计了自动化的扰动方法，包括颜色扰动（全局低对比度、部分/全部按钮色度偏移）、文本扰动（注入空格、符号或替换视觉相似字符）和布局扰动（最小化修改DOM结构）。这些扰动模拟了真实环境中的视觉退化、内容扭曲和前端更新。3）**评估流程**：采用标准化提示词和协议化的确定性评估管道，对原始和扰动后的网页截图进行配对测试，通过比较模型输出的语义一致性来衡量鲁棒性。对于推理和安全性任务，则依赖人工标注的真实值进行对比。

创新点主要体现在：首先，**多维度联合评估**：首次将推理、鲁棒性和安全能力整合到一个基准中，更全面地反映MLLM在网络理解中的实际表现。其次，**生态有效的对抗性测试**：通过受WCAG启发的颜色扰动和保留功能的布局修改，确保了扰动既具有感知显著性又不破坏语义，从而贴近真实场景。最后，**可扩展的任务设计**：例如在位置关系推理中，通过自动化脚本从HTML中随机采样元素对并计算空间关系，实现了低成本、高多样性的样本生成，使基准易于扩展。这些方法共同揭示了当前模型在组合推理、对抗扰动下的稳定性以及安全关键识别方面存在的显著差距。

### Q4: 论文做了哪些实验？

论文在自建的WebRRSBench基准上进行了全面的实验评估。实验设置方面，评估了11个多模态大语言模型（MLLM），包括闭源模型（GPT-5、Claude-4-Sonnet、Gemini 2.5-Pro）和开源模型（如Pixtral-Large、Qwen2.5-VL系列、Intern-S1等）。为确保公平，采用了统一的解码配置：温度设为0，top-p为1.0，最大生成长度为1024个token，并固定随机种子。评估流程结合了基于共识的人工标注真值（由四位博士生确定）和任务特定指标（如准确率、基于嵌入的相似度等），并引入了自我对比分析以揭示模型预测在扰动前后的潜在不稳定性。

数据集为论文构建的WebRRSBench，包含来自729个网站的3799个问答对，涵盖八个任务：位置关系推理（分简单、中等、困难三级）、UI分组、表单填充、提示文本完成、颜色鲁棒性、文本鲁棒性、布局鲁棒性以及安全关键按钮检测。其中鲁棒性任务在原始页面和施加扰动（如全局低对比度、部分/全部按钮色度变化、文本编辑、布局重排）的页面上进行配对评估。

主要结果通过表格呈现。关键发现包括：1）闭源模型在大多数任务上表现更优，尤其在安全关键检测上优势明显（如Gemini 2.5-Pro达91.1%）。2）开源模型表现差异大，大规模模型如Qwen2.5-VL-72B在颜色和文本鲁棒性上接近闭源模型，但所有模型在位置推理和表单填充等推理任务上普遍困难（例如，在困难级别的位置推理任务中，多数模型准确率低于30%）。3）微调实验（针对Qwen2.5-VL-7B，使用LoRA方法在位置关系推理、UI分组和颜色鲁棒性任务上进行）显著提升了性能：位置推理准确率从16.3%提升至41.3%，UI分组从67.6%提升至96.9%，颜色鲁棒性平均准确率从73.1%提升至80.1%。4）模型失败原因分析表明，颜色扰动会导致模型过度依赖视觉显著性且OCR性能下降；文本扰动暴露了字符级识别的脆弱性；布局扰动则使模型过度关注局部而忽略全局结构。

### Q5: 有什么可以进一步探索的点？

该论文提出的WebRRSBench在评估MLLM的网页理解能力方面迈出了重要一步，但仍存在一些局限性和可进一步探索的方向。首先，基准测试主要基于静态网页截图，未能充分模拟动态交互环境（如下拉菜单、弹窗、实时更新），未来可引入交互式评估框架，让模型在模拟浏览器环境中执行操作并观察结果。其次，当前任务虽涵盖推理、鲁棒性和安全性，但对多模态对齐的细粒度评估不足，例如模型对视觉元素（图标、颜色）与功能关联的理解能力；可探索引入对抗性样本，测试模型在界面元素被恶意篡改时的表现。此外，基准缺乏对长上下文和多步骤任务中错误累积的分析，未来可设计更复杂的跨页面工作流评估。从方法层面，当前评估依赖标准化提示词，但实际应用中用户指令多样且模糊，需研究提示工程对性能的影响。最后，论文发现模型对安全性行为过于保守，这可能导致实用性问题；可探索在安全边界内增强模型的风险权衡能力，例如通过强化学习优化决策阈值。这些方向将推动MLLM在真实网页环境中实现更可靠、灵活的应用。

### Q6: 总结一下论文的主要内容

该论文针对多模态大语言模型在网页理解任务中的能力评估不足问题，提出了一个名为WebRRSBench的综合基准测试。其核心贡献在于首次将推理能力、鲁棒性和安全性三个维度联合评估，覆盖了位置关系推理、颜色鲁棒性、安全关键检测等八项具体任务。该基准从729个真实网站构建了3799个问答对，要求模型对页面结构、文本、控件进行多步推理，并处理安全敏感的交互。

方法上，论文采用了标准化的提示词、流程化且确定性的评估流程，并结合自动检查与人工验证的多阶段质量控制，确保评估的可靠性。作者对11个主流MLLM进行了测试。

主要结论显示，现有模型存在显著不足：它们在面对真实布局时，仍难以进行组合式及跨元素的复杂推理；在界面布局重组、视觉风格变化等扰动下表现出有限的鲁棒性；并且在识别与规避安全关键或不可逆操作时往往过于保守。该研究为MLLM在网页端应用的发展指明了关键的改进方向。
