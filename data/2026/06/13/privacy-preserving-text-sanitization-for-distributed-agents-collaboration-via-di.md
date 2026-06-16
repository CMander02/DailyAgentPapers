---
title: "Privacy-Preserving Text Sanitization for Distributed Agents Collaboration via Disentangled Representations"
authors:
  - "Xuan Liu"
  - "Hefeng Zhou"
  - "Sicheng Chen"
  - "Chao Yang"
  - "Xingcheng Xu"
  - "Jingjing Qu"
  - "Jiong Lou"
  - "Jie LI"
  - "Xia Hu"
date: "2026-06-13"
arxiv_id: "2606.15335"
arxiv_url: "https://arxiv.org/abs/2606.15335"
pdf_url: "https://arxiv.org/pdf/2606.15335v1"
categories:
  - "cs.CL"
  - "cs.AI"
tags:
  - "多智能体协作"
  - "隐私保护"
  - "文本消毒"
  - "分布式系统"
  - "解耦表示"
relevance_score: 7.5
---

# Privacy-Preserving Text Sanitization for Distributed Agents Collaboration via Disentangled Representations

## 原始摘要

When distributed agents exchange text across organizational boundaries, privacy leakage arises not only from explicit identifiers but also from distributional signatures such as formatting conventions, vocabulary choices, and syntactic patterns. We propose DiSan(Disentangled Sanitization), a privacy-preserving sanitization framework and a built-in component of Intern-Shannon for multi-agent collaboration. DiSan uses a two-stream encoder to factorize text into a source-invariant role subspace that preserves task semantics and a source-identifying style subspace that remains local. Federated proto-type alignment and adversarial regularization enable joint training without centralizing raw text. Experiments show that identifier-level masking is insufficient: masking 19.2% of tokens reduces TF-IDF stylometric attribution by only 18.6%. By contrast, DiSan reduces answer-level PII exposure by 20 times while maintaining 83% answer faithfulness on a distributed multi-agent RAG benchmark, and lowers Enron stylometric attribution by 73.2% under TF-IDF and 70.6% under a neural probe.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文试图解决分布式智能体跨组织协作中，文本交换导致的隐私泄露问题。研究背景是，在多智能体系统（如RAG、分布式问答）中，不同组织拥有私有文档库，在共享文本证据时，隐私风险不仅来自姓名、账号等显式标识符，更源于分布式的隐式签名，如格式惯例、词汇选择和句法模式。现有方法存在明显不足：基于规则的PII检测器只针对个别标识符，无法处理分布式的风格指纹；基于LLM的重写只是重新排列表面形式，无法保证输出在统计上与源无关；联邦学习虽能去中心化训练，但最终产出的是共享预测器，而非可直接共享的脱敏数据。核心挑战在于：如何找到一个最小充分的表示，既能保留任务语义，又在统计上与源无关。为此，本文提出DiSan（解耦脱敏）框架，通过角色-风格因子化，将文本解耦为保留任务语义的源不变子空间（角色）和捕获源相关变化的子空间（风格），并利用联邦原型对齐和对抗正则化，在不集中原始文本的情况下联合训练，最终仅发布角色子空间的文本，从而有效抑制隐式指纹泄露。

### Q2: 有哪些相关研究？

相关研究主要分为三类。首先是**隐私保护机器学习**，包括差分隐私（DP）和联邦学习等方法。本文与这类方法互补：现有工作关注训练过程隐私，而本文聚焦于数据本身（文本）的脱敏处理。其次是**文本脱敏与去标识化**，传统方法依赖规则或NER检测显式标识符并掩码，但无法防御写作风格等隐式泄漏。本文通过对比实验证明，仅掩码标识符无法有效降低风格归因。此外，基于LLM的改写和DP文本生成虽可用于隐私保护，但DP方法在低隐私预算（ε<10）下会损失30-50%的语义连贯性，不适合需要高语义保真度的RAG应用。第三是**解耦表示学习**，已有工作将文本分解为内容与风格、情感等因子，用于可控生成和隐私保护。本文创新性地将其应用于多智能体协作场景，通过双流编码器将文本解耦为任务相关的角色子空间和源标识风格子空间，并在不集中原始文本的情况下，通过联邦原型对齐和对抗正则化实现联合训练，在处理隐式风格指纹泄漏方面优于现有方法。

### Q3: 论文如何解决这个问题？

DiSan采用双流编码器架构将文本分解为角色子空间和风格子空间，实现隐私保护净化。整体框架包含三个核心模块：首先，双流投影模块使用预训练LongT5-TGlobal-Base编码器，通过两个独立线性变换W_r和W_s将隐藏状态H分别映射为256维的角色流Z_r和风格流Z_s，前者捕获源不变的任务语义（实体、关系、事件），后者编码代理特定的措辞和格式。其次，融合解码模块将两个流拼接后经投影层g恢复维度，再通过解码器自回归生成净化文本，其中风格流仅用于本地生成辅助且解码后即丢弃，仅净化文本跨组织边界传输。关键技术方面：解耦损失L_orth通过余弦相似度最小化角色与风格均值向量的相关性；联邦原型对齐利用各代理计算的角色原型EMA进行球面对齐，使局部角色分布趋向全局锚点而不共享原始数据；对抗正则化通过梯度反转层使原型判别器难以预测源代理身份，抑制源特定分布签名。创新点包括：将分布签名泄露（格式习惯、词汇选择、句法模式）纳入隐私保护范畴，实验表明仅遮掩标识符（19.2%词元）仅降低18.6%笔迹风格归因，而DiSan实现答案级PII暴露降低20倍、笔迹归因降低73.2%，同时保持83%答案忠实度。

### Q4: 论文做了哪些实验？

论文在合成金融语料库（synthetic_pii_finance_multilingual）上进行了实验，配置了7个非IID分布的分布式智能体（如CorporateBank、AssetManager等），采用RAG评估流水线（文档分块256 tokens，BGE-M3混合检索）。对比方法包括：Placeholder-only（使用GLiNER、Piiranha、DeBERTa三种PII检测器替换标识符）、LLM paraphrasing和Policy gating（Qwen2.5-7B决策共享策略）。主要结果：DiSan将答案级PII暴露从无保护的11.8%降至0.6%，保持83.17%的答案忠实度（无保护基线86.10%）。在Enron文风归因测试中，DiSan将TF-IDF归因降至0.221（降幅73.2%），BERT归因降至0.203（降幅70.6%），接近随机水平（0.143），而GLiNER掩码19.2% token仅降低18.6%。消融实验表明：移除正交损失（L_orth）使平均PII增加7.3倍（至0.9706），移除原型对齐（No-ProtoAlign）使余弦相似度下降6%、ChunkHit@3下降3.6个百分点、PII暴露增加2.7倍。分离验证显示角色嵌入在7路指纹探测中F1=0.05（随机），风格嵌入F1=0.84。

### Q5: 有什么可以进一步探索的点？

该文目前依赖合成金融数据与Enron邮件集验证，但合成数据可能无法完全模拟真实隐私泄露的复杂分布，未来可在真实医疗、法律等敏感领域扩展评估。核心局限在于缺乏差分隐私（DP）的形式化保证——文本生成场景下逐token噪声注入会破坏语义连贯性，可探索将解耦表示与DP结合，例如对角色子空间的连续表示加噪后解码，或使用离散高斯机制适配序列生成。对抗评估仅考虑单轮查询，而多轮协作中对手可通过查询关联逐步重建用户风格，需研究记忆型攻击下的退化防御。此外，当前风格子空间假设源间差异可完全分离，但真实场景中角色与风格存在交叠（如专业术语同时携带任务语义与机构特征），可通过引入互信息约束或对比学习增强解耦鲁棒性。

### Q6: 总结一下论文的主要内容

这篇论文提出了一个名为DiSan的隐私保护文本清洗框架，用于解决分布式智能体协作中因文本分布特征（如格式、词汇、句法）导致的隐私泄露问题。现有方法仅掩盖显式标识符，效果有限。DiSan通过双流编码器将文本分解为正交的角色子空间（保留任务语义）和风格子空间（包含来源标识特征），并采用联邦原型对齐与对抗正则化实现分布式联合训练，无需共享原始数据。实验表明，单纯掩盖19.2%的token仅降低18.6%的文风归因，而DiSan在分布式多智能体RAG基准上将答案级PII暴露降低20倍，同时保持83%的答案忠实度；在Enron数据集上，其TF-IDF和神经探针的文风归因率分别降低73.2%和70.6%。核心贡献在于证明表示层解耦比标识符掩盖更有效地抑制分布级隐私泄露，为跨组织文本安全共享提供了可行路径。
