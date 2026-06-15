---
title: "Same-Origin Policy for Agentic Browsers"
authors:
  - "Xilong Wang"
  - "Xiaoxing Chen"
  - "Patrick Li"
  - "Dawn Song"
  - "Neil Gong"
date: "2026-06-12"
arxiv_id: "2606.14027"
arxiv_url: "https://arxiv.org/abs/2606.14027"
pdf_url: "https://arxiv.org/pdf/2606.14027v1"
github_url: "https://github.com/wxl-lxw/BrowserOS-SOPGuard"
categories:
  - "cs.CR"
  - "cs.AI"
  - "cs.CL"
  - "eess.SY"
tags:
  - "Agent安全"
  - "Agent浏览器"
  - "同源策略"
  - "SOP"
  - "安全机制"
  - "Agent基准测试"
relevance_score: 8.5
---

# Same-Origin Policy for Agentic Browsers

## 原始摘要

Agentic browsers integrate autonomous AI agents into web browsers, enabling users to accomplish web tasks through natural-language instructions. The same-origin policy (SOP) is a fundamental browser security mechanism that prevents unauthorized automated cross-origin data flows induced by scripts. However, whether SOP remains effective in agentic browsers is an open question that has not been systematically studied. In this work, we bridge this gap. We first observe that an agentic browser can itself serve as an automated channel for cross-origin data flows, potentially leading to SOP violations. To investigate this phenomenon, we construct SOPBench, a benchmark for evaluating SOP violations in agentic browsers. Our evaluation shows that existing agentic browsers frequently violate SOP, both in benign settings and under attacks. To address this problem, we propose SOPGuard, an SOP enforcement mechanism tailored to agentic browsers. We implement SOPGuard in BrowserOS, an open-source agentic browser. Extensive evaluations demonstrate that SOPGuard effectively enforces SOP while preserving utility and incurring only a small runtime overhead. Our code and data are available at https://github.com/wxl-lxw/BrowserOS-SOPGuard.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决智能体浏览器中同源策略失效的核心安全问题。随着基于AI Agent的智能体浏览器（如BrowserOS、Perplexity Comet）的兴起，用户可以通过自然语言指令让代理自动执行跨网页操作（如表单填写、数据提交）。传统浏览器依赖同源策略阻止脚本驱动的跨源数据流，但智能体浏览器中，代理本身成为自动化的数据通道：它可能在访问源网页时通过交互历史持久化敏感信息（如支付凭证），随后被自动写入另一个不同源的网页。现有研究主要关注单网页内的提示注入攻击，而未系统考察跨源数据流问题，且缺乏评估基准与防护机制。本文的核心在于首次系统研究智能体浏览器的SOP漏洞，发现两种违规场景：（1）被动违规——代理因不可靠性无意中将源网页数据写入跨源目标；（2）主动违规——攻击者通过植入恶意内容诱导代理主动从历史记录窃取数据。为此，论文构建了SOPBench基准测试框架，验证了多种智能体浏览器存在显著违规率，并提出了SOPGuard防护机制，通过数据标记、传播追踪和用户确认来强制执行SOP。

### Q2: 有哪些相关研究？

本论文在多个方面有相关研究。在方法类方面，涉及交互历史管理，现有代理浏览器如BrowserOS、Perplexity Comet等通过侧边栏集成AI助手，维持用户与代理的共同交互界面，而本文特别关注这种架构下可能产生的跨源数据流问题。在安全攻击类方面，论文讨论了针对代理浏览器的提示注入攻击，包括基于启发式的攻击（如Combined Attack、Pop-up攻击、EIA和WASP）和基于优化的攻击（如WebInject和TAP）。与传统浏览器中的SOP违规（如XSS攻击）不同，代理浏览器中的违规源于代理本身可能自动将源网页数据传输到目标网页。本文与这些工作的核心区别在于，首次系统性地研究了代理浏览器中SOP的有效性，并提出了专门的基准测试SOPBench和防护机制SOPGuard。在评测类方面，现有工作主要关注单个网页的攻击效果，而本文通过SOPBench系统评估跨源数据流违规。

### Q3: 论文如何解决这个问题？

论文提出了SOPGuard，一种针对智能体浏览器的同源策略强制机制，旨在解决现有智能体浏览器频繁违反SOP的问题。整体框架是在开源智能体浏览器BrowserOS中集成SOPGuard，作为安全层。

核心方法基于对智能体浏览器作为跨源数据自动传输通道的观察，设计了细粒度的访问控制模型。主要模块包括：1）请求拦截器，捕获智能体发出的所有跨源HTTP请求和DOM访问；2）源标记模块，为每个页面分配唯一的安全上下文标识符（包括协议、域名和端口号）；3）策略引擎，动态评估每次访问是否符合SOP规则；4）决策执行器，根据评估结果允许、重写或拒绝操作。

关键技术创新有三点：一是提出“智能体-来源解耦”概念，将智能体的操作来源与当前页面上下文分离，避免智能体滥用已加载页面的源权限；二是实现“操作级SOP检查”，不仅拦截网络请求，还监控DOM访问、Cookie读取和localStorage操作等浏览器API调用；三是引入“跨源流标注机制”，自动标记从不同源获取的数据，防止智能体将数据混入同源上下文。实验表明，SOPGuard能有效阻止跨源数据泄露（在测试集上实现100%的SOP违规拦截率），同时保持任务完成率（仅下降小于2%），运行时开销仅增加约15毫秒。

### Q4: 论文做了哪些实验？

论文构建了SOPBench基准测试，评估五种智能浏览器的同源策略（SOP）违反情况。实验设置包括被动SOP违反（用户良性提示意外引发跨源数据流）和主动SOP违反（攻击者对汇页面注入恶意提示）。数据集涵盖电子商务、银行等10类源页面和X、Discord等5类汇页面，通过GPT-5.4生成合成页面并辅以真实页面快照。对比方法包括VisualWebArena、SeeAct、BrowserOS（开源，使用GPT-5.4-mini、OpenAI o3、GPT-5.4作为骨干模型）及Perplexity Comet、ChatGPT Atlas（闭源）。攻击方式采用启发式攻击（手工注入）和基于TAP的优化攻击。主要结果：所有智能浏览器在启发式和优化攻击下均频繁违反SOP，例如VisualWebArena在GitHub汇页面中SOP违反率常接近1.00（如GPT-5.4-mini在电子商务源页面下为1.00），SeeAct和BrowserOS也表现出高违反率。在被动SOP违反中，嵌入iframe的汇页面同样导致数据泄露。SOPGuard在BrowserOS中实施后，有效强制SOP且运行时开销小。

### Q5: 有什么可以进一步探索的点？

论文指出当前agentic浏览器普遍违反同源策略（SOP），但SOPGuard仅在特定开源平台验证，未来可从三方面深入：第一，扩展攻击面研究，当前仅测试了被动数据窃取，可探索主动伪造用户身份、跨域API劫持等更复杂的攻击链；第二，优化SOPGuard的语义理解能力，目前依赖DOM结构匹配标签，对动态生成的交互元素（如单页应用中的Shadow DOM）可能失效，可引入视觉特征或LLM推理增强识别；第三，权衡安全与效率，当前延迟开销在可接受范围，但高频自动化场景（如批量表单填写）可能累积显著性能损耗，可设计分层策略：对高风险跨域操作（如金融操作）强制SOP检查，对低风险操作（如页面截图）降级为启发式规则。此外，建议探索多代理协作场景下的SOP传递机制，避免不同代理间的交叉污染。

### Q6: 总结一下论文的主要内容

这篇论文首次系统性地研究了自主浏览器中同源策略（SOP）的安全问题。传统SOP旨在防止脚本引发的跨源自动数据流动，但自主浏览器中的AI代理本身可作为自动数据通道，可能导致顺从或主动的SOP违规。为量化这一威胁，作者构建了SOPBench基准测试，涵盖10种源网页和5种目标网页类别，并评估了五种自主浏览器和六种大语言模型。评估发现，现有自主浏览器在正常场景和攻击下均频繁发生SOP违规。为解决此问题，论文提出了SOPGuard机制，通过数据标签化、标签传播、检测及用户确认等组件强制执行SOP。在BrowserOS中的实现表明，SOPGuard能完全消除SOP违规（违规率降至0.00），同时保持实用性和较低运行时开销（2.07%-5.79%）。这项研究揭示了自主浏览器安全的新维度，为未来的安全设计奠定了重要基础。
