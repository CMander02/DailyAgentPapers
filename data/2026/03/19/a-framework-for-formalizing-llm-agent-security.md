---
title: "A Framework for Formalizing LLM Agent Security"
authors:
  - "Vincent Siu"
  - "Jingxuan He"
  - "Kyle Montgomery"
  - "Zhun Wang"
  - "Neil Gong"
  - "Chenguang Wang"
  - "Dawn Song"
date: "2026-03-19"
arxiv_id: "2603.19469"
arxiv_url: "https://arxiv.org/abs/2603.19469"
pdf_url: "https://arxiv.org/pdf/2603.19469v1"
categories:
  - "cs.CR"
  - "cs.AI"
tags:
  - "Agent Security"
  - "Formal Framework"
  - "Contextual Security"
  - "Security Properties"
  - "Attack Formalization"
  - "Defense Formalization"
relevance_score: 7.5
---

# A Framework for Formalizing LLM Agent Security

## 原始摘要

Security in LLM agents is inherently contextual. For example, the same action taken by an agent may represent legitimate behavior or a security violation depending on whose instruction led to the action, what objective is being pursued, and whether the action serves that objective. However, existing definitions of security attacks against LLM agents often fail to capture this contextual nature. As a result, defenses face a fundamental utility-security tradeoff: applying defenses uniformly across all contexts can lead to significant utility loss, while applying defenses in insufficient or inappropriate contexts can result in security vulnerabilities. In this work, we present a framework that systematizes existing attacks and defenses from the perspective of contextual security. To this end, we propose four security properties that capture contextual security for LLM agents: task alignment (pursuing authorized objectives), action alignment (individual actions serving those objectives), source authorization (executing commands from authenticated sources), and data isolation (ensuring information flows respect privilege boundaries). We further introduce a set of oracle functions that enable verification of whether these security properties are violated as an agent executes a user task. Using this framework, we reformalize existing attacks, such as indirect prompt injection, direct prompt injection, jailbreak, task drift, and memory poisoning, as violations of one or more security properties, thereby providing precise and contextual definitions of these attacks. Similarly, we reformalize defenses as mechanisms that strengthen oracle functions or perform security property checks. Finally, we discuss several important future research directions enabled by our framework.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决大型语言模型（LLM）智能体安全领域的一个核心问题：现有安全攻击的定义和防御方法普遍缺乏对**执行上下文**的考量，导致面临严重的“效用-安全”权衡困境。

研究背景是，随着LLM智能体越来越多地在现实环境中自主操作，其安全性变得至关重要。然而，智能体的安全本质上是**情境化的**。例如，一个“删除文件”的指令，如果是来自授权用户并服务于清理任务的目标，则是合法操作；但如果是来自恶意网页并旨在破坏数据，则构成安全攻击。现有研究（如Liu等人对提示注入攻击的定义）往往将攻击定义为某种固定的输入/输出模式（如数据输入中包含提示），而忽略了“谁发出的指令”、“追求什么目标”、“行动是否服务于该目标”以及“信息流权限”等关键上下文因素。

现有方法的不足正在于此。由于攻击定义是上下文无关的，当前的防御措施被迫在安全性和实用性之间做出艰难取舍：要么在所有上下文中统一应用防御（例如，一律阻止包含“删除”字样的指令），这会误阻合法操作，导致**效用严重损失**；要么防御应用不足或不当，则又会留下**安全漏洞**。

因此，本文要解决的核心问题是：如何建立一个系统化的**形式化框架**，以捕捉LLM智能体安全的上下文本质，从而为攻击和防御提供精确、情境化的定义与分析基础。为此，论文提出了一个以执行上下文为核心的形式化框架，定义了四个上下文安全属性（任务对齐、行动对齐、源授权、数据隔离），并引入了一组用于验证这些属性的“预言机函数”。通过该框架，论文将各种现有攻击（如间接/直接提示注入、越狱、任务漂移等）重新形式化为对上述一个或多个安全属性的违反，同时也将防御措施重新解释为强化预言机函数或执行安全属性检查的机制。最终，该框架旨在超越简单的模式匹配，实现对智能体行为的细粒度、上下文感知的安全判定，从而调和效用与安全之间的矛盾。

### Q2: 有哪些相关研究？

本文提出的形式化框架与多个领域的研究相关，主要可分为**安全攻击与防御方法**、**智能体形式化模型**以及**大语言模型安全评测**三类。

在**安全攻击与防御方法**方面，已有大量工作研究了针对LLM智能体的具体攻击，如间接提示注入、直接提示注入、越狱、任务漂移和记忆污染等，并提出了相应的防御机制。本文与这些工作的核心区别在于，现有研究通常孤立地定义攻击和设计防御，缺乏一个统一的、**情境化**的视角。本文的框架将这些攻击系统地重新形式化为对四个核心安全属性（任务对齐、行动对齐、源授权、数据隔离）中一个或多个的违反，并将防御机制重新解释为强化预言机函数或执行安全属性检查的机制，从而超越了具体攻击的枚举，提供了一个普适的分析工具。

在**智能体形式化模型**方面，已有研究对LLM智能体的架构和决策过程进行形式化建模。本文的工作在此基础上更进一步，不仅定义了智能体的执行模型（包含提示、轨迹、环境、记忆、行动和来源等组件），还**明确引入了来源权限图**这一概念，用以形式化地刻画不同信息源之间的访问控制关系。这使得安全分析能够深入到信息流和权限边界层面，为理解“情境”提供了数学基础。

在**大语言模型安全评测**方面，现有基准测试通常关注模型在特定对抗性输入下的行为。本文的框架为评测提供了更精细的维度，即可以基于四个安全属性是否被违反来评估智能体的安全性，从而能够更精确地诊断安全漏洞的根源，并评估防御措施在特定情境下的有效性，有助于缓解现有评测中普遍存在的**效用-安全权衡**困境。

### Q3: 论文如何解决这个问题？

论文通过提出一个形式化框架来解决LLM智能体安全性的上下文依赖问题。该框架的核心是定义了**执行上下文**的概念，将安全性的判断与具体的执行环境绑定。整体架构围绕四个**安全属性**和五个**预言机函数**构建。

**核心方法与架构设计：**
1.  **执行上下文**：形式化定义为 \(\mathcal{C}_t = (p, \mathbf{Tr}_{t-1}, \mathbf{M_t}, E_t, \mathbf{S}_{auth,t}, G)\)，它捕获了在时间步 \(t\) 做出授权决策所需的所有相关信息，包括用户提示 \(p\)、历史轨迹 \(\mathbf{Tr}_{t-1}\)、记忆 \(\mathbf{M_t}\)、环境状态 \(E_t\)、已认证源集合 \(\mathbf{S}_{auth,t}\) 和源权限图 \(G\)。安全被定义为行动与上下文之间的关系属性，而非行动本身的固有属性。

2.  **四个安全属性**：
    *   **任务对齐**：确保智能体追求的是用户授权的、安全的目标。它通过检查初始目标 \(o_0 = H_p(p)\) 是否在允许的目标空间 \(\mathbf{O}\) 内，以及整个执行轨迹 \(\mathbf{Tr}_{t-1}\) 是否服务于 \(o_0\)（通过 \(H_{Tr}\) 判断）来验证。这用于捕获越狱和任务漂移攻击。
    *   **行动对齐**：确保每个具体行动 \(a_t\) 都服务于授权目标 \(o_0\)，通过预言机函数 \(H_a\) 进行判断。这防止了合法能力被滥用于未授权目的，即使整体任务没有偏离。
    *   **源授权**：确保智能体只执行来自已认证源（\(\mathbf{S}_{auth,t}\)）的指令。这需要结合两个预言机函数：首先，\(\mathcal{I}\) 识别出导致行动 \(a_t\) 的输入指令；其次，\(\mathcal{L}\) 追溯这些输入的来源。如果任何来源未经验证，则构成违规。这用于形式化直接和间接提示注入攻击。
    *   **数据隔离**：确保信息流遵守权限边界，防止特权信息泄露。

3.  **五个预言机函数**：作为理想化的理论规范，定义了验证上述安全属性所需的信息。
    *   **目标评估函数**：\(H_p\)（从提示提取目标）、\(H_{Tr}\)（判断轨迹是否服务目标）、\(H_a\)（判断单个行动是否服务目标）。
    *   **指令归因函数** \(\mathcal{I}\)：识别导致特定行动的输入指令。
    *   **源归因函数** \(\mathcal{L}\)：映射输入到其来源，追踪信息在系统中的来源。

**创新点与关键技术：**
1.  **系统性形式化**：首次提出了一个统一的框架，将LLM智能体的多种攻击（如间接提示注入、越狱、任务漂移）系统地重新形式化为对上述一个或多个安全属性的违反，从而提供了精确且上下文相关的攻击定义。
2.  **上下文感知的安全模型**：明确指出安全决策必须基于完整的、动态演化的执行上下文 \(\mathcal{C}_t\)，并需要持续验证。这从根本上解释了为何现有防御措施面临效用与安全的根本权衡。
3.  **预言机抽象**：通过定义预言机函数，清晰地阐明了任何有效防御机制所需近似或实现的核心功能（如指令归因、目标一致性判断），从而揭示了当前防御方法的系统性差距（哪些预言机被近似得好、哪些被近似得差、哪些完全未被处理）。
4.  **防御措施的统一视角**：将现有防御措施重新解释为旨在增强这些预言机函数或执行安全属性检查的机制，为评估和改进防御提供了清晰的路线图。

### Q4: 论文做了哪些实验？

论文通过提出的框架对现有攻击和防御进行了系统化分析，但并未进行传统意义上的实证实验。其“实验”部分主要体现在理论验证和框架应用上。

**实验设置与数据集/基准测试**：研究未使用具体数据集或运行基准测试，而是基于理论框架，对多类已知攻击进行形式化重定义和分类。分析对象包括间接提示注入、直接提示注入、越狱、任务漂移和内存中毒等攻击，以及相应的防御机制。

**对比方法**：研究将现有攻击定义（如Liu等人将提示注入定义为“数据输入中插入提示导致执行注入任务”）与本文提出的基于上下文安全属性的定义进行对比。重点指出传统定义仅基于动作内容或来源，忽略了授权上下文，导致定义不精确且防御陷入效用-安全的根本权衡。

**主要结果与关键指标**：
1.  **理论验证**：成功将各类攻击重新形式化为对四个安全属性（任务对齐、动作对齐、源授权、数据隔离）中一个或多个的违反。例如，间接提示注入被重新定义为在特定上下文中违反“源授权”和/或“任务对齐”属性。
2.  **分类洞察**：通过基于安全属性的分类法揭示，表面不同的攻击可能共享更深层的结构违规（违反相同属性），而表面相似的行为可能违反不同属性，需要不同的防御措施。
3.  **框架效用**：展示了所提框架如何提供更精确、更具上下文感知的攻击定义，并能够将现有防御重新解释为强化预言机函数或执行安全属性检查的机制。

总之，论文的核心“实验”是通过提出的形式化框架，对现有攻击与防御进行系统性理论分析和重新归类，从而论证其框架在理解和定义智能体安全方面的有效性与优越性。

### Q5: 有什么可以进一步探索的点？

该论文提出的框架虽然系统化了LLM智能体的上下文安全属性，但其局限性在于依赖“预言机函数”进行安全验证，而这些函数在现实中难以完美实现。未来研究可首先探索如何通过增强的监控与审计机制来近似这些预言机，例如利用多模态感知或实时行为分析来更精准地判断任务对齐与行动意图。其次，框架尚未深入涉及动态环境下的自适应防御策略，未来可研究如何让智能体根据上下文风险自动调整安全措施的强度，以优化效用与安全的平衡。此外，论文未充分讨论多智能体协作场景中的跨域安全挑战，这是一个值得拓展的方向，例如设计去中心化的信任机制来确保跨智能体的数据隔离与指令授权。最后，结合形式化验证与机器学习方法，开发可证明安全的学习框架，也是提升智能体长期安全性的关键路径。

### Q6: 总结一下论文的主要内容

该论文针对LLM智能体安全性的语境依赖性，提出了一个形式化框架以系统化现有攻击与防御。核心问题是现有安全定义常忽视行为合法性高度依赖执行语境（如指令来源、任务目标），导致防御措施面临效用与安全的根本权衡。

论文方法包括：首先形式化定义了执行语境，并提炼出四个语境安全属性——任务对齐（追求授权目标）、行动对齐（单个行动服务目标）、来源授权（执行认证来源指令）和数据隔离（信息流遵守权限边界）。其次，引入一组预言机函数（如指令归因、来源追溯、目标评估函数），用于在运行时验证这些属性是否被违反。

主要结论是，该框架能将间接提示注入、直接提示注入、越狱等攻击重新定义为特定安全属性的违反，从而提供精确且语境化的攻击定义；同时将防御措施重新表述为强化预言机函数或执行属性检查的机制。这揭示了现有防御（如语境无关方法）的根本局限，并为实现兼具效用与安全的防御指明了方向，例如通过多属性协同检查来区分合法操作与攻击。
