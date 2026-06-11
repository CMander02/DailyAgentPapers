---
title: "MedCTA: A Benchmark for Clinical Tool Agents"
authors:
  - "Tajamul Ashraf"
  - "Hyewon Jeong"
  - "Fida Mohammad Thoker"
  - "Bernard Ghanem"
date: "2026-06-10"
arxiv_id: "2606.11702"
arxiv_url: "https://arxiv.org/abs/2606.11702"
pdf_url: "https://arxiv.org/pdf/2606.11702v1"
github_url: "https://github.com/IVUL-KAUST/MedCTA"
categories:
  - "cs.CV"
  - "cs.AI"
  - "cs.CL"
tags:
  - "Medical AI Agent"
  - "Benchmark"
  - "Tool Use"
  - "Multimodal Agent"
  - "Clinical Decision Making"
relevance_score: 9.0
---

# MedCTA: A Benchmark for Clinical Tool Agents

## 原始摘要

To make clinically grounded decisions, medical AI agents are expected to go beyond simple recognition and be capable of tool retrieval, evidence acquisition, and integration. Existing benchmarks largely evaluate isolated perception or single-turn question answering, and therefore provide limited visibility into failures of planning, tool recruitment, and rollout reliability. We introduce MedCTA, a benchmark for evaluating medical tool agents on clinician-validated, step-implicit tasks grounded in realistic multimodal clinical inputs, including radiology images, pathology slides, and reports. MedCTA comprises 107 real-world clinical tasks with clinician-verified executable trajectories over 5 deployed tools, and supports process-aware evaluation of tool selection, argument validity, execution stability, trajectory fidelity, and outcome quality. We benchmark 18 open- and closed-source multimodal models and find that even frontier systems remain brittle in multi-step clinical tool use: autonomous rollouts are dominated by protocol failures, premature stopping, and incorrect tool recruitment, while gold-standard tool routing yields large but still incomplete gains. These results show that strong backbone perception does not translate into reliable agentic behavior in clinical settings. MedCTA provides a rigorous testbed for auditing, diagnosing, and advancing trustworthy medical AI agents. The dataset and evaluation suite are available at https://ivul-kaust.github.io/MedCTA/

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决当前医疗AI代理在临床决策中缺乏规划与工具使用能力评估的问题。现有基准（如Medical VQA）大多局限于单轮感知或问答任务，无法揭示代理在复杂多步流程中的失败模式，例如工具检索错误、执行顺序混乱或可靠性不足。尽管多模态大模型在感知任务上表现优异，但在临床场景中，模型需要自主分解任务、调用工具并整合证据，而现有方法无法评估这种代理行为。为此，论文提出MedCTA基准，包含107个经临床医生验证的真实多模态任务（如放射影像、病理切片等），并配套5个可执行工具。核心创新在于：（1）构建了隐含工具需求的临床查询，要求模型自主规划而非遵循提示；（2）引入过程感知评估，覆盖工具选择、参数有效性、执行稳定性、轨迹忠实度及最终结果质量。实验表明，即使前沿模型在自主执行中仍存在协议失败、过早终止等脆弱性问题，证明强大的感知能力无法直接转化为可靠的临床代理行为。MedCTA为审计和发展可信医疗AI代理提供了严格测试平台。

### Q2: 有哪些相关研究？

- **工具增强与轨迹感知智能体**：相关系统如LangChain、Auto-GPT、WebGPT、HuggingGPT等，展示了语言模型通过工具与环境交互的能力。本文区别于这些开放域工作，聚焦于安全关键的临床场景，需要评估工具选择、参数有效性和中间证据一致性，而非仅关注最终任务成功率。

- **多模态医学基准与模型**：主流基准如VQA-RAD、SLAKE、Path-VQA等评估静态感知或单轮问答，模型如LLaVA-Med、RadFM等关注单一理解任务。本文则填补了评估模型在动态临床决策中“何时使用工具、使用何种工具、如何整合证据”这一核心空白。

- **医学智能体与交互式评估**：近期工作如MDAgents、AgentClinic、MedRAX、MedAgentGYM等，开始探索多智能体协作、模拟临床交互或轨迹级评估。本文是首个专门针对工具增强语言模型（LLM）设计的代理基准，提供经临床验证的可执行工具链和轨迹级审计（工具选择、参数有效性、执行稳定性、最终结果质量），弥补了现有工作缺乏临床生态和细粒度故障诊断的不足。

### Q3: 论文如何解决这个问题？

MedCTA通过构建一个结构化的基准框架来解决临床工具智能体评估问题。其核心是设计了一个包含五元组（临床上下文X、智能体查询Q、工具子集U、参考工具链π、最终结果A）的任务表示，将单步感知问题转化为需要多步工具调用的临床目标。

整体框架采用半自动化的人工参与流水线。首先，从现有医学VQA数据集中收集单步感知种子问题；然后利用多模态大模型（LMM）生成包含工具使用暗示的初始查询；接着由人类专家重写为“目标优先、工具无关”的临床请求，隐去所有工具名称和步骤指示；最终由临床医生验证医学正确性和可执行性。参考工具链的构建同样采用LMM生成初始轨迹、技术标注者去除冗余步骤并确保工具调用的稳定性和参数有效性、临床医生验证推理的医学合理性。

关键技术包括：隐式工具需求设计（查询不透露工具集和顺序）、过程感知评估（评估工具选择、参数有效性、执行稳定性、轨迹忠实度、结果质量五个维度）、以及多模态输入整合（CT、MRI、病理切片、报告等）。创新点在于实现了从感知级评测到智能体级评测的跨越，揭示了强骨干感知能力不保证临床可靠智能体行为的核心缺陷。

### Q4: 论文做了哪些实验？

论文对MedCTA基准进行了全面的实验评估，设置了三个互补的度量组：逐步（Step-by-Step）评估交互保真度（指令遵循、工具选择、参数有效性），临床推理（Clinical Reasoning）评估证据使用和摘要质量，以及结果（Outcome）评估最终答案准确性。实验基于107个临床验证的任务，对18个开源和闭源多模态大模型（包括GPT、Claude、Gemini、Qwen、LLaMA、DeepSeek、Mistral和Phi系列）进行了总计1926次自主rollout评估。主要结果显示，表现最好的模型GPT-5.4和Claude-opus-4-6在最终结果准确率G_acc上也仅分别达到31.54和31.32，远未饱和。通过金标准工具路由对比实验，发现模型表现显著提升（如Claude-opus-4-6从31.32升至66.40），揭示了自主规划的巨大瓶颈。全局rollout诊断显示，64.2%的回合遇到API/协议错误，99.2%存在过早停止问题。此外，与独立VLM性能对比表明，强骨干感知能力（如GPT-5.4达60.74）并不能转化为可靠的自主代理行为。

### Q5: 有什么可以进一步探索的点？

**局限性**：当前模型在多步临床工具使用中存在显著的"规划-执行"鸿沟。尽管骨干感知能力（如GPT-5.4单轮60.74）已较强，但自主智能体表现（31.54）远低于Gold标准路由（49.50），说明瓶颈在于无法可靠维护工具调用循环，具体表现为：64.2%的API协议错误、99.2%的过早终止、58.3%的流程崩溃。**未来方向**：1）开发更强的规划与元学习机制，让模型学会何时调用工具、何时停止；2）引入显式的执行监控与错误恢复模块，降低协议失败率；3）探索分层架构——由弱模型负责工具路由，强模型负责临床推理；4）设计对抗性压力测试，评估模型在工具失效下的鲁棒性；5）从评估角度，应扩展对"部分成功"的粒度分析，区分信息不足与错误推理导致的失败。最终，真正的临床信任需要同时具备感知准确性和执行可靠性。

### Q6: 总结一下论文的主要内容

MedCTA是一个用于评估医学工具代理的基准测试，针对临床验证的、步骤隐含的真实多模态临床任务（包括放射影像、病理切片和报告）。基准包含107个真实世界任务，配有临床医生验证的、跨越5个部署工具的可执行轨迹，并支持对工具选择、参数有效性、执行稳定性、轨迹保真度和结果质量的过程级评估。在对18个开源和闭源多模态模型进行的基准测试中，发现即使是顶尖系统在多步骤临床工具使用中也表现脆弱：自主执行主要受协议失败、过早停止和工具招募错误影响，最佳结果准确率仅31.54%，而采用金标准工具路由可提升高达35%。结果表明，强大的感知能力并不能转化为可靠的临床代理行为，错误主要源于控制器失败而非临床推理缺失。MedCTA为审计、诊断和推进可信赖的医学AI代理提供了严格的测试平台。
