---
title: "A self-evolving agent for explainable diagnosis of DFT-experiment band-gap mismatch"
authors:
  - "Yue Li"
  - "Bijun Tang"
date: "2026-04-29"
arxiv_id: "2604.26703"
arxiv_url: "https://arxiv.org/abs/2604.26703"
pdf_url: "https://arxiv.org/pdf/2604.26703v1"
categories:
  - "cond-mat.mtrl-sci"
  - "cs.AI"
  - "physics.comp-ph"
tags:
  - "LLM Agent"
  - "Scientific Agent"
  - "Autonomous Diagnosis"
  - "Bayesian Hypothesis Selection"
  - "Materials Science"
  - "DFT"
relevance_score: 9.0
---

# A self-evolving agent for explainable diagnosis of DFT-experiment band-gap mismatch

## 原始摘要

Standard density functional theory (DFT) routinely misclassifies the electronic ground state of correlated and structurally complex compounds, predicting metallic behaviour for materials that experiments report as semiconductors. Each such mismatch encodes a specific non-ideality -- magnetic ordering, electron correlation, an alternative polymorph, or a defect -- that the calculation excluded, but extracting that signal at scale has remained a manual exercise. Here we introduce XDFT, a closed-loop agent that diagnoses the mismatch automatically: it draws candidate hypotheses from a curated catalogue, executes the corresponding first-principles tests, and updates a global Bayesian posterior over hypothesis usefulness from each verdict. On a verified benchmark of 124 materials, XDFT identifies a resolving mechanism for 70 of 90 mismatch cases (78\%), an order of magnitude above a uniform-random baseline (19\%) and a static LLM ordering (20\%). The internal posterior aligns with empirical performance over the benchmark timeline, and resolved cases collapse into a tri-partite element-class taxonomy that we distil into a four-line static rule. Each diagnosed material is returned with a corrected protocol and a mechanistic attribution; failed cases are flagged as evidence-backed targets for experimental re-examination.

## Q&A 论文解读

### Q1: 这篇论文试图解决什么问题？

这篇论文旨在解决材料科学中一个长期存在的难题：标准密度泛函理论（DFT，特别是GGA-PBE）在预测强关联氧化物、复杂结构半导体和稀土化合物时，常常错误地预测为金属，而实验却报告为半导体。这种理论-实验之间的带隙不匹配并非随机错误，而是蕴含着重要的物理信息（如磁序、电子关联、多晶型等），但传统高通量计算流程仅关注DFT预测本身，并未设计用于自动提取这些信号。论文提出的XDFT（eXplainable DFT）是一个闭环科学Agent，其核心目标是自动诊断每一个不匹配案例，找出具体是哪种被默认计算忽略的非理想因素导致了偏差，并以可解释的方式返回校正后的计算协议和机制归因。本质上，它试图将科学家的诊断思维（提出假设→第一性原理验证→更新信念）自动化、规模化，从而将计算材料学从单纯的‘高通量执行’提升到‘自主诊断’的层面。

### Q2: 有哪些相关研究？

相关工作主要分为三类：1）高通量DFT工作流引擎，如AiiDA和Atomate，它们自动化了计算任务的生成、执行与分析，但仍是“执行既定协议”，而非诊断偏差。2）材料属性预测网络与通用力场（如MACE、CHGNet、GNoME），它们基于DFT数据训练，隐含假定商品化DFT是实验的忠实代理，因此会传播相同的理想化偏置。3）自主实验室与AI科学家（如Coscientist），它们利用LLM驱动实验规划，但侧重于合成路线优化，而非诊断理论-实验偏差。XDFT的独特定位是作为“诊断层”工作于这些系统之上：它不直接预测属性，而是通过主动测试假设来解读偏差的意义。此外，固定流程的GGA+U（如Materials Project）仅对已知过渡金属化学预置U值，而XDFT动态选择并测试包括U在内的多种假设。论文引用了这些工作，并明确指出XDFT填补了从偏差中提取机制信号的空白，这是现有自动化流水线和机器学习代理均未覆盖的。

### Q3: 论文如何解决这个问题？

XDFT采用闭环Agent架构，核心包含四个模块：1) **Sherlock（假设选择器）**：维护一个包含41类假设（如点缺陷、磁序、Hubbard U、多晶型、应变、范德华修正、自旋-轨道耦合、泛函选择）的贝叶斯全局后验。每个假设建模为Beta分布，后验基于所有材料的历史结果更新。每轮选择时，结合Beta均值（权重0.6）、LLM顾问对特定材料的建议（权重0.2）和元素相容性过滤（权重0.2）计算评分，选择最高分假设。2) **Manipulator（操作器）**：根据选中假设，调用原子编辑工具生成具体计算输入，如创建缺陷超胞、交换阳离子、施加应变、设置Hubbard U参数或从Materials Project获取多晶型。3) **Simulation（执行器）**：运行VASP第一性原理计算（GGA-PBE基准，按假设开关自旋极化、Hubbard U、SOC等）。4) **Comparator（裁决器）**：比较计算与实验的电子特征（金属/半导体），返回匹配、部分匹配或失败三种判决。Sherlock据此更新对应假设的Beta后验（成功+1，失败+1，部分不计数但增加分母）。每材料最多迭代10轮。关键创新在于：贝叶斯后验是全局且自我进化的——所有材料的测试结果累积形成一个校准的先验，使后续材料的假设排序越来越准确；同时，每个判决都来自第一性原理计算（非代理模型），保证了归因的可信度。系统还实现了动态假设生成模式（本文未启用），用于处理库外机制。

### Q4: 论文做了哪些实验？

论文构建了一个包含124种候选材料的基准测试集，经过一致性审计（Bag-of-Bonds校验）后，有效运行98个（排除26个非算法性故障），其中90个为确实存在不匹配的案例。实验核心结果：XDFT成功解析了70/90个不匹配案例（解析率78%），远超随机基线（19%）和静态LLM假设排序（20%）。与一位凝聚态专家凭经验确定固定排序（69%）相比，XDFT不仅提升9个百分点，还将平均求解轮次从4.3降至2.7（降低37%）。论文还进行了多维度分析：1) **后验校准**：跟踪Sherlock内部后验与最终成功率的斯皮尔曼相关系数，从初始的-0.32（反相关）单调上升至第100材料时的+0.69，证明Agent确实在从经验中学习。2) **群体学习效应**：在d-block材料子集（n=50）上，后期材料的首轮命中率从早期33%上升至58%，三轮内命中率从71%升至89%，表明积累的先验提升了效率。3) **可解释分类**：解析案例按元素类别呈现清晰规律：主族→多晶型（83%）、d-block→磁+U（70%）、f-block→纯磁序（57%），该规律可浓缩为四行静态规则，独立复现71%解析率。实验在H100和RTX 3090上完成，共约1500 GPU小时。论文还分析了20个失败案例，主要集中于镧系化合物（中间价态、多信道关联、4f多重态效应）和结构奇异的非主族材料，为库扩展指明了方向。

### Q5: 有什么可以进一步探索的点？

论文明确指出三个主要限制和四个未来方向：**限制**：1) 仅覆盖金属/半导体特征不匹配，未处理“半导体但带隙定量误差”和“实验为金属、DFT预测半导体”的情形；2) 基准规模有限（98有效运行，90不匹配），统计功效对子分类尚显不足；3) 假设库静态，虽然已实现动态生成模式但未在此基准中启用。**未来方向**：1) 将相同框架扩展至诊断载流子类型、磁基态和有效质量等属性，只需更换裁决模块和补充计算任务；2) 启用生成式假设机制，让LLM根据失败模式创建新假设类，提升库覆盖率和泛化能力；3) 精细校准Hubbard U参数（当前仅采样三个预设水平，可改为贝叶斯优化扫描）；4) 应用于其他理论-实验不一致（如晶格常数、声子稳定性），继承相同的诊断范式。这些探索点均源自论文实验结果的分析，具有明确的技术可行性和物理必要性。

### Q6: 总结一下论文的主要内容

该论文提出了XDFT，一个用于自动诊断DFT-实验带隙不匹配的闭环科学Agent。核心创新在于将贝叶斯假设选择与第一性原理计算流水线耦合，实现自我进化的诊断能力：每处理一个材料，全局后验更新并改善后续假设排序。在精心构建的124材料基准上，XDFT解析了90个不匹配案例中的70个（78%），远优于随机和静态基线，并揭示了按元素类别分类的可解释物理规律。实验证明其内部信念与外部性能一致收敛，并展现了群体学习效率提升。论文的主要贡献是将科学Agent从高通量执行推进到自主诊断层，能够从理论-实验系统性偏差中提取可归因的物理洞察，为计算-实验闭环研究提供了新范式。
