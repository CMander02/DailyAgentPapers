---
title: "TrustedARI: Towards Trust-Native Agentic Routing Infrastructure for Agentic AI"
authors:
  - "Qi Li"
  - "Zhenhua Zou"
  - "Shuo Li"
  - "Mingwei Xu"
  - "Zhuotao Liu"
date: "2026-06-14"
arxiv_id: "2606.15822"
arxiv_url: "https://arxiv.org/abs/2606.15822"
pdf_url: "https://arxiv.org/pdf/2606.15822v1"
categories:
  - "cs.AI"
  - "cs.CR"
tags:
  - "安全路由"
  - "TLS握手"
  - "隐私保护"
  - "多方计算"
  - "可信基础设施"
relevance_score: 8.5
---

# TrustedARI: Towards Trust-Native Agentic Routing Infrastructure for Agentic AI

## 原始摘要

AI agents increasingly access external models, tools, and services through Agentic Routing Infrastructure (ARI) to manage the overhead of heterogeneous interfaces and fragmented subscriptions. Yet, the architecture of ARI introduces fundamental trust risks: it obtains plaintext access to agent queries and service responses, while leaving agents unable to verify that their queries are routed to intended service providers or that requests and responses remain untampered. To address this problem, we present TrustedARI, the first trust-native agentic routing infrastructure for agentic AI. Architecturally, TrustedARI is built upon three core innovations: (i) an ARI-adapted three-party TLS handshake that enables the agent and ARI to jointly authenticate the service provider through role-specific distribution of TLS key materials; (ii) a privacy-preserving query-construction protocol that allows the agent and ARI to collaboratively construct well-formed queries without exposing their respective private inputs; and (iii) a verifiable billing protocol that supports fair usage-based settlement while preserving the integrity and confidentiality of service responses.
  We implemented and extensively evaluated a prototype of TrustedARI to validate its performance. Experiments confirm that TrustedARI is highly efficient: our ARI-adapted handshake protocol reduces communication overhead by 39.34% compared to the existing three-party TLS handshake. Furthermore, the privacy-preserving query-construction protocol imposes negligible overhead-averaging 0.19 seconds in computation time and 0.58 MB in communication costs-while the verifiable billing protocol speeds up proof generation by 28.20x. Crucially, TrustedARI is readily deployable without any modification to the service providers.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

论文旨在解决AI Agent在通过Agentic Routing Infrastructure (ARI)访问外部模型、工具和服务时面临的信任风险。具体问题包括：(1) ARI能够以明文形式获取Agent的查询和服务提供商的响应，存在隐私泄露风险；(2) Agent无法验证其查询是否被路由到预期的服务提供商；(3) Agent无法验证请求和响应在传输过程中是否被篡改。论文提出TrustedARI，一个可信的Agentic路由基础设施，通过创新的三方TLS握手协议、隐私保护的查询构建协议和可验证计费协议来解决上述问题，确保Agent、ARI和服务提供商之间的通信安全、隐私和完整性。

### Q2: 有哪些相关研究？

相关研究主要分为三个方向：(1) 安全多方计算（MPC）和隐私保护协议，如Li等人提出的DistEFON（2023）和Celi等人提出的相关工作，这些工作为三方TLS握手提供了基础，但TrustedARI通过优化HKDF扩展和密钥派生协议减少了2PC的计算和通信开销。(2) 代理路由基础设施（ARI）的安全性，如OAuth和API网关相关的安全协议，但现有工作未考虑ARI作为中间人的信任风险。(3) Agent安全与隐私，如Agent记忆保护、工具使用安全性等，但TrustedARI是首个专门针对ARI基础设施的信任模型。论文在DistEFON的基础上提出了ARI适配的三方握手协议，通过预计算和优化HKDF扩展，将通信开销降低39.34%。

### Q3: 论文如何解决这个问题？

论文提出TrustedARI，包含三个核心创新：(1) ARI适配的三方TLS握手协议：通过角色特定的TLS密钥材料分发，使Agent和ARI能够联合认证服务提供商。该协议基于椭圆曲线Diffie-Hellman（ECDH）和秘密共享，Agent和ARI分别持有私钥份额，联合计算共享密钥。协议中引入了预计算（PreCompute）和优化HKDF扩展（HKDF.ExpandOptm）子协议，将2PC操作从多次减少为一次，显著降低通信开销。具体流程包括：Agent和ARI分别生成随机数并计算Z值，ARI组合后发送给工具服务器；工具服务器返回签名后的服务器密钥份额（SKS）；双方使用ECDH和秘密共享推导出握手机密（HS）和主机密（MS），进而生成应用流量密钥。(2) 隐私保护的查询构建协议：Agent和ARI在不暴露各自私有输入的情况下协作构建格式正确的查询请求，使用秘密共享和OT（不经意传输）技术实现。(3) 可验证计费协议：支持基于使用的公平结算，同时保持服务响应的完整性和机密性，通过零知识证明和承诺机制实现。整个系统无需修改服务提供商即可部署。

### Q4: 论文做了哪些实验？

论文实现了TrustedARI的原型系统并进行了全面的性能评估。实验设置包括：使用Go语言实现原型，部署在云环境中测试。主要实验结果：(1) 三方握手协议：与现有的DistEFON三方TLS握手相比，TrustedARI的ARI适配握手协议通信开销降低了39.34%。(2) 隐私保护查询构建协议：平均计算时间为0.19秒，通信成本为0.58 MB，对于实际Agent查询场景来说可忽略不计。(3) 可验证计费协议：证明生成速度提升了28.20倍，显著提高了计费验证的效率。(4) 整体性能：在不同网络延迟（10ms-100ms）和查询大小（1KB-100KB）下，TrustedARI的端到端延迟仅比标准TLS增加15%-25%，在实际部署中可接受。实验还验证了协议的正确性和安全性，通过模拟攻击场景确认了防篡改和防重放能力。

### Q5: 有什么可以进一步探索的点？

论文的局限性包括：(1) 目前仅支持静态的Agent-ARI-服务提供商三方模型，未来可扩展至支持动态加入和退出的多方场景。(2) 隐私保护查询构建协议假设查询是结构化的（如REST API调用），对于非结构化查询（如自由文本生成）的适配需要进一步研究。(3) 实验主要在模拟环境进行，未在真实大规模Agent系统（如WebArena或SWE-bench）中测试对Agent性能的影响。(4) 可验证计费协议假设服务提供商是诚实的但好奇的，未来可引入更强大的安全模型（如恶意安全）。(5) 与现有Agent框架（如LangChain、AutoGPT）的集成需进一步优化以降低部署门槛。

### Q6: 总结一下论文的主要内容

TrustedARI是首个针对Agentic AI的信任原生路由基础设施。论文针对Agent通过ARI访问外部服务时面临的隐私泄露和完整性风险，提出了三项核心技术创新：ARI适配的三方TLS握手协议（通信开销降低39.34%）、隐私保护的查询构建协议（平均0.19秒计算开销）以及可验证计费协议（证明生成速度提升28.20倍）。该系统无需修改现有服务提供商即可部署，通过在Agent和ARI之间引入秘密共享和优化的2PC协议，实现了查询和响应的机密性、完整性和路由验证。实验表明，TrustedARI在保证安全性的同时，性能开销接近实际部署可用范围。这是AI Agent安全基础设施领域的重要贡献，填补了Agent与外部服务通信信任模型的空白。
