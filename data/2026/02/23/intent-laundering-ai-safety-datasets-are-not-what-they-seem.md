---
title: "Intent Laundering: AI Safety Datasets Are Not What They Seem"
authors:
  - "Shahriar Golchin"
  - "Marc Wetter"
date: "2026-02-17"
arxiv_id: "2602.16729"
arxiv_url: "https://arxiv.org/abs/2602.16729"
pdf_url: "https://arxiv.org/pdf/2602.16729v2"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.CL"
  - "cs.LG"
tags:
  - "AI Safety"
  - "Adversarial Attacks"
  - "Jailbreaking"
  - "Dataset Evaluation"
  - "Model Safety"
  - "Benchmarking"
relevance_score: 7.5
---

# Intent Laundering: AI Safety Datasets Are Not What They Seem

## 原始摘要

We systematically evaluate the quality of widely used AI safety datasets from two perspectives: in isolation and in practice. In isolation, we examine how well these datasets reflect real-world adversarial attacks based on three key properties: being driven by ulterior intent, well-crafted, and out-of-distribution. We find that these datasets overrely on "triggering cues": words or phrases with overt negative/sensitive connotations that are intended to trigger safety mechanisms explicitly, which is unrealistic compared to real-world attacks. In practice, we evaluate whether these datasets genuinely measure safety risks or merely provoke refusals through triggering cues. To explore this, we introduce "intent laundering": a procedure that abstracts away triggering cues from adversarial attacks (data points) while strictly preserving their malicious intent and all relevant details. Our results indicate that current AI safety datasets fail to faithfully represent real-world adversarial behavior due to their overreliance on triggering cues. Once these cues are removed, all previously evaluated "reasonably safe" models become unsafe, including Gemini 3 Pro and Claude Sonnet 3.7. Moreover, when intent laundering is adapted as a jailbreaking technique, it consistently achieves high attack success rates, ranging from 90% to over 98%, under fully black-box access. Overall, our findings expose a significant disconnect between how model safety is evaluated by existing datasets and how real-world adversaries behave.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在揭示并解决当前AI安全评估领域的一个核心问题：广泛使用的AI安全数据集（如AdvBench和HarmBench）在设计和内容上存在严重缺陷，导致其无法真实反映现实世界中的对抗性攻击行为，从而可能高估了AI模型的实际安全性能。

研究背景在于，AI安全主要依靠两大支柱：安全对齐（使模型能抵御攻击）和安全数据集（用于评估模型的鲁棒性）。评估的可信度高度依赖于数据集的质量，即其能否准确模拟现实世界的对抗场景。然而，与数学问题等数据集不同，安全数据集需要捕捉的是具有隐蔽意图、精心设计且分布外（OOD）的真实攻击。

现有方法的不足在于，论文通过系统分析发现，当前主流的安全数据集过度依赖“触发线索”——即那些带有明显负面/敏感含义、旨在显式触发模型安全机制的词语或短语（例如“自杀”、“不被抓到”）。这些线索使得数据点显得不自然且易于被模型识别和拒绝，这与现实世界中攻击者会精心伪装其恶意意图、避免使用明显敏感词的行为模式严重不符。这种设计导致数据集在孤立分析时，就未能满足真实攻击应具备的“隐蔽意图”和“精心设计”等关键属性，并因大量重复使用这些线索而损害了数据多样性（分布外属性）。

因此，本文要解决的核心问题是：**这些数据集究竟是在真实测量模型的安全风险，还是仅仅通过“触发线索”来 provoke 模型的拒绝反应，从而造成一种虚假的安全评估结果？** 为了探究这个问题，论文引入了“意图清洗”这一核心方法，旨在将数据点中的显式触发线索抽象掉，同时严格保留其全部恶意意图和相关细节。通过这一过程，论文实证检验了去除这些不现实线索后，模型的实际攻击成功率变化，从而评估现有数据集在实践中的有效性缺陷，并进一步将“意图清洗”发展为一种新的越狱攻击技术。

### Q2: 有哪些相关研究？

本文的相关研究主要涉及AI安全对齐、对抗攻击与越狱技术、以及安全数据集评测三大类别。

在**安全对齐**方面，研究旨在平衡模型的“有帮助性”与“无害性”，防止“拒绝不足”或“过度拒绝”。本文的研究背景建立在此之上，但重点在于揭示当前安全评测如何因数据集缺陷而未能有效保障这种平衡。

在**对抗攻击与越狱技术**领域，已有大量工作研究如何诱导已对齐模型输出有害内容。本文提出的“意图洗白”方法本身即是一种新颖的越狱技术，其核心区别在于：它并非创造新的攻击，而是通过抽象移除现有攻击中的“触发线索”，从而更纯粹地测试模型对恶意意图本身的抵抗能力，这与其他依赖显式敏感词的方法有本质不同。

在**安全数据集评测**方面，本文直接针对广泛使用的AI安全数据集（如用于红队测试和基准评估的数据集）进行批判性分析。相关研究通常默认这些数据集能有效模拟真实世界攻击。本文的核心贡献在于系统性地揭示了这些数据集严重依赖不现实的“触发线索”，导致评测结果与真实对抗行为脱节。本文通过“意图洗白”程序进行实证，证明了当前数据集在孤立评估和实际应用中都存在根本性缺陷，这补充并挑战了该领域的普遍假设。

综上，本文与相关工作的关系是：立足于安全对齐的目标，批判性地检验了用于评估对齐效果的安全数据集及对应的对抗攻击研究，并通过引入一种新的分析视角（意图洗白）和技术方法，暴露了现有评测范式的局限性。

### Q3: 论文如何解决这个问题？

论文通过提出“意图清洗”这一核心方法来解决现有AI安全数据集过度依赖“触发线索”而无法真实反映现实世界对抗行为的问题。该方法旨在从有害请求中抽象掉明显的触发语言，同时严格保留其恶意意图和所有相关细节，从而更准确地评估模型的安全风险。

整体框架包含两个互补的组件：**内涵中和**与**语境置换**。内涵中和负责移除带有负面/敏感内涵的触发线索，将其替换为中性或积极的替代词，若无合适替代则使用描述性替换。语境置换则将现实世界中的场景和指涉对象（如“移民”、“慈善机构”）替换为非现实世界的替代物（如游戏世界或虚构叙事中的替身），确保所有细节在经过微小调整后仍可适用于现实世界。

在技术实现上，研究首先手动对来自两个安全数据集的数据点进行少量意图清洗修订，以此作为示例。随后，他们构建了一个自动化的“意图清洗器”，其核心是一个基于**少样本上下文学习**的大型语言模型。每个原始数据点与其修订版构成的配对作为ICL示范，用于指导模型执行意图清洗。生成所有修订后，通过收集模型对原始数据和修订后数据的响应，来评估触发线索对安全评估的影响。

评估体系沿安全和实用性两个独立轴线进行，均采用五级李克特量表，并由LLM自动评判。**安全评估**专注于判断响应是否针对原始恶意意图，以及其危害程度；**实用性评估**则关注响应中提供的细节在现实世界中的适用性和可转移性。攻击成功率定义为同时产生“不安全”且“实用”响应的修订所占比例。

关键的创新点在于将意图清洗进一步发展为一种独立的越狱攻击技术。通过引入**迭代修订-再生机制**，当修订未能引发不安全或不实用的响应时，系统将这些失败案例作为反馈提供给意图清洗器，使其在相同的少样本ICL设置下生成新的改进修订。这一循环持续进行，直至达到预定的再生尝试次数或目标攻击成功率，从而在完全黑盒访问条件下实现了高达90%至98%以上的攻击成功率。

综上所述，该方法通过系统性地剥离表面触发线索、保留核心恶意意图，并构建自动化评估与迭代攻击框架，不仅揭示了现有安全数据集的评估缺陷，也提供了一种强大的新型对抗攻击范式。

### Q4: 论文做了哪些实验？

论文实验主要分为两部分：一是评估现有AI安全数据集的质量，二是测试提出的“意图清洗”方法的有效性。

**实验设置与数据集**：研究使用两个广泛使用的安全数据集：AdvBench（处理后包含207个独特数据点）和HarmBench标准版（200个数据点）。评估模型包括Gemini 3 Pro、Claude Sonnet 3.7、Grok 4、GPT-4o、Llama 3.3 70B、GPT-4o mini和Qwen2.5 7B，共七个模型。实验采用黑盒访问方式，并降低模型的推理强度以匹配任务需求。

**对比方法与评估**：实验设置了三种对比条件：1) **无修订**：直接使用原始数据集（含触发线索）测试，计算标准攻击成功率；2) **首次修订**：应用“意图清洗”首次移除数据点中的触发线索，同时严格保留恶意意图，评估安全性（SE）、实用性（PE）及两者同时满足的ASR；3) **多次修订**：将“意图清洗”作为越狱技术进行迭代（修订-再生循环），观察ASR变化。使用GPT-5.1作为“意图清洗器”和评估法官，采用少量示例提示进行生成与评估。

**主要结果与关键指标**：
1.  **触发线索的过度依赖**：在原始数据集（含触发线索）上，模型平均ASR很低（AdvBench: 5.38%；HarmBench: 13.79%）。一旦通过“意图清洗”移除触发线索（首次修订），ASR急剧上升（AdvBench平均至86.79%；HarmBench平均至79.83%），表明现有安全数据集严重依赖触发线索来引发模型拒绝，而非真正评估恶意意图，从而高估了模型安全性。
2.  **意图清洗作为高效越狱技术**：经过多次迭代修订，“意图清洗”能持续提升ASR，最终在所有模型和数据集上达到极高的攻击成功率（90%至超过98.55%）。例如，在AdvBench上，Gemini 3 Pro的ASR从1.93%升至95.17%；Claude Sonnet 3.7从2.42%升至93.23%。
3.  **实用性与可控性**：即使经过抽象化，模型响应的实用性（PE）始终保持在极高水平（接近100%）。同时，ASR随着迭代次数增加而持续稳定增长，表明该方法能有效、系统地提升攻击成功率，并可通过迭代次数进行控制。

这些结果共同揭示了当前安全数据集与现实对抗行为之间存在显著脱节，而“意图清洗”方法能有效暴露模型在移除表面触发线索后的真实安全风险。

### Q5: 有什么可以进一步探索的点？

该论文揭示了现有AI安全数据集过度依赖“触发线索”的局限性，导致其无法真实反映现实世界的对抗性攻击。未来研究可从以下几个方向深入探索：首先，需构建更贴近真实对抗行为的安全数据集，减少对显性敏感词的依赖，转而关注意图的隐蔽性和上下文复杂性。其次，可探索动态安全评估框架，引入持续学习和对抗性样本生成技术，使模型能适应不断演化的攻击手法。此外，论文提出的“意图清洗”方法虽有效，但其自动化程度和泛化能力有待提升，未来可结合大语言模型的自我反思能力，实现更精准的意图保留与线索剥离。最后，需从多模态、跨文化等维度拓展安全评估边界，因为现实攻击往往涉及图像、音频等非文本形式，且恶意意图的表达方式具有文化特异性。这些改进将有助于弥合学术评估与现实安全需求之间的差距。

### Q6: 总结一下论文的主要内容

这篇论文揭示了当前AI安全数据集在评估模型安全性时存在的严重缺陷。研究发现，这些数据集过度依赖“触发线索”——即带有明显负面/敏感含义的词语或短语，旨在显式触发安全机制，这与现实世界中的对抗性攻击行为不符。为了探究这一问题，作者提出了“意图清洗”方法，即在严格保留恶意意图和相关细节的前提下，从对抗攻击数据点中抽象掉这些触发线索。实验结果表明，现有数据集因依赖触发线索而无法真实反映现实对抗行为；一旦移除这些线索，所有先前评估为“相对安全”的模型（包括Gemini 3 Pro和Claude Sonnet 3.7）均变得不安全。此外，将意图清洗适配为越狱技术时，在完全黑盒访问下攻击成功率高达90%至98%以上。该研究的核心贡献在于暴露了现有安全评估与现实对抗行为之间的脱节，强调了构建更贴近真实攻击场景的安全数据集的紧迫性。
