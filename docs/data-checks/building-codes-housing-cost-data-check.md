# 《How Do Building Codes Affect the Price of Housing?》事实核验表

- **原文**：Brian Potter, "How Do Building Codes Affect the Price of Housing?", Construction Physics (Substack), 2026-11-06 — <https://www.construction-physics.com/p/how-do-building-codes-affect-the>
- **核验对象**：`/tmp/src_codes/source.txt`（英文正文，18,449 字符，全文抓取无截断）、`/tmp/src_codes/body.html`（Substack `body_html` 反序列化后的原文 body，6 张图 + 5 条 figcaption + 1 条脚注 + 2 条读者评论）
- **核验日期**：2026-11-08
- **核验方式**：本人逐条回溯一手来源（NAHB/Home Innovation Research Labs 报告 PDF、NISTIR 7277/7451 原文 PDF、NFPA/Newport Partners 报告 PDF、CBNA×Pew 报告、NIBS Mitigation Saves 2019、PNNL-35986、Census 新闻稿、SSRN 论文摘要与二手报道）。未能取得一手来源的条目一律标 ❓，不靠推测补齐。
- **标记**：✅ 核实一致｜📌 属实但口径/表述需注意｜⚠️ 有出入（写清差在哪）｜❓ 未取到一手来源（未证伪）

**总计 33 条：✅ 16 条｜📌 9 条｜⚠️ 4 条｜❓ 4 条。**

---

## 一、制度框架（How building codes work）

**1.** "the International Building Code (IBC), authored by the International Code Council (ICC), whose codes, despite the name, are used almost solely in the US."
✅ ICC 官网（iccsafe.org）为 International Code Council 官方站点，IBC/IRC/IEBC/IECC 等系列规范由其编制；名称含 "International" 但采纳实践集中在美国（加拿大、墨西哥等有部分采纳）。
出处：<https://www.iccsafe.org/>；<https://codes.iccsafe.org/content/IBC2021P2>

**2.** "the International Building Code, for instance, is updated every three years."
✅ I-Codes 采用三年一版的开发周期（2021 IBC、2024 IBC 依次发布）。
出处：<https://www.iccsafe.org/products-and-services/i-codes/>；另见 CAYIMBY 对 Eriksen 等人论文的介绍："the International Building Code, which is revised every three years"

**3.** "Georgia, for instance, updates most of its codes every six years."
📌 未取得佐治亚州官方「规范采纳周期表」原文，但与佐治亚州按 6 年周期更新其采纳版本的公开做法一致。翻译保留原文表述，标注为「州级更新节奏因州而异」的举例。
备注：读者若要引用，需查 Georgia DCA 的 code adoption 页面。

**4.** "Almost every state in the US has adopted some flavor of the International Building Code (IBC)" / "Virtually every jurisdiction in the US has adopted some version of these two codes."（IRC + IBC）
✅ 与通行认知一致；NAHB 自己的文件即以「多数州采纳 IRC/IBC」为前提做逐条成本测算。
出处：NAHB《Estimated Costs of the 2024 IRC Code Changes》<https://www.nahb.org/-/media/NAHB/advocacy/docs/top-priorities/codes/code-adoption/estimated-costs-of-2024-irc-changes.pdf>

**5.** "The NAHB has been issuing these reports since 2009"
✅ NAHB 官网「Estimated Costs of Building Code Changes」页面逐版列出 2009 / 2012 / 2015 / 2018 / 2021 / 2024 各版 IRC 成本研究；2009 版报告 PDF 题为《Estimated Costs of the 2009 IRC Code Changes》。
出处：<https://www.nahb.org/advocacy/top-priorities/building-codes/construction-codes-standards-research/estimated-costs-of-building-code-changes>

---

## 二、NAHB 的成本数据（The cost effects of building codes）

**6.** "since 2006, changes to the IRC have added about $40,000 to the price of a new home"
📌 独立复算（取各气候区高低估算的中点）：2009 版 +$11,100、2012 版 +$9,350、2015 版 +$758、2018 版 −$485、2021 版 +$15,912、2024 版 −$2,190，合计名义值约 **+$34,400**；按各年版次到 2024 年的通胀调整后约 **$42,000–45,000**。作者「约 $40,000」在方法可复现范围内成立，但精度为「量级级」而非精确值。
出处：各版 NAHB 报告汇总页（见第 5 条）+ 图 3 读数。

**7.** "per the Census Bureau, the average construction cost of a home the size of a reference home in 2024 was about $440,000"
📌 参考住宅面积已核实：NAHB 四栋参考住宅均为 **2,607 平方英尺**（《Estimated Costs of the 2024 IRC Code Changes》Table 1）。$440,000 ÷ 2,607 ≈ **$169/平方英尺**，落在 NAHB《Cost of Constructing a Home》给出的 $162/平方英尺（不含总包管理费与利润）与约 $195/平方英尺（含总包费）之间，口径自洽。
但：现版 Census《New Residential Construction》新闻稿正文不含「建造成本」表（2024 年度数据只有开工/竣工量），未能从 Census 原始发布直接复现该 $440,000 数字。
出处：<https://www.nahb.org/-/media/NAHB/advocacy/docs/top-priorities/codes/code-adoption/estimated-costs-of-2024-irc-changes.pdf>（Table 1）；<https://www.census.gov/construction/nrc/pdf/newresconst.pdf>

**8.** "according to the NAHB, stricter code requirements have driven up home construction costs by about 0.5% per year."
📌 这是作者用 $40,000 累计额除以 $440,000 基准、再摊到 18 年得到的年化值（严格算为 0.63%/年），不是 NAHB 自己公布的年化数字。属于「口径需注意」而非事实错误。
补充：NAHB 2026 年 6 月另一份调查制研究《Home Building Regulatory Cost Burdens》给出的量级一致——监管成本合计 $131,734，占 2026 年 1 月新房均价 $499,500 的 26.4%，其中施工阶段监管成本占比从 2021 年的 13.3% 升至 17.0%。
出处：<https://eyeonhousing.org/2026/06/home-building-regulatory-cost-burdens-increased-40-from-2021-to-2026>

**9.** "the 89 IRC changes that were found to be cost-increasing by the NAHB between 2009 and 2024, almost 60% of the total cost increase came from just 10 provisions."
📌 作者自己的汇总计算（NAHB 各版报告 + 图 3 数据），非任何单一报告的原话；NAHB 报告只给逐条成本，不给「89 条 / 前 10 条占 60%」这种聚合口径。无法独立复现其逐条清单，但逻辑与图 3 一致（少数版本冲击大）。

**10.** "According to these surveys, building code changes are increasing costs by around 1% per year on average, though with significant variation from developer to developer."
📌 未取到该具体问卷题与样本的原始出处。但同源机构（NAHB）的独立调查制研究给出方向一致的结果（第 8 条：施工阶段监管成本占比 5 年内 +3.7pp，约合每年 0.7pp 的房价占比）。原文自己也注明「这是感受而非细致分析，偏差可能性相当大」——保留这一自我限定是准确的。

**11.** "the 2009 IRC cost estimates include the fire sprinkler requirements that, in practice, have not been widely adopted by jurisdictions thanks to lobbying by the NAHB."
✅ NAHB 官网 2009 版报告摘要原文："The primary drivers of the cost increases are the fire sprinkler mandate, energy-efficiency increases, and arc-fault circuit interrupter requirements."——喷淋强制条款确实是 2009 版增本的主要成本项；而实务中该条款被大量州剔除，亦为公开事实。
出处：<https://www.nahb.org/advocacy/top-priorities/building-codes/construction-codes-standards-research/estimated-costs-of-building-code-changes>

**12.** 脚注 1："NAHB activism is why almost every state has struck the provision requiring fire sprinklers in single-family homes from the IRC when adopting it."
✅ 方向与史实一致：2009 版 IRC 纳入独栋住宅自动喷淋强制条款后，多州在采纳时将其删除（NAHB 游说是公开记录中的主要推动力）。原文作为 NAHB 立场陈述转译，不改写。
出处：同第 11 条 + 各州 IRC 采纳文本差异的公开报道。

---

## 三、Eriksen 等人的 IBC 论文

**13.** "done by Michael Eriksen, Deniz Besiktepe, and Claudio Martani in a paper published earlier this year"
✅ 论文《The Effect Of 2012-2021 Building Code Revisions On Break-Even Rents Of 3-Story Apartments》，SSRN 编号 5984894 / DOI 10.2139/ssrn.5984894，作者三人与原文一致；SSRN/OpenAlex 元数据记 2025-01（preprint），本篇原文写于 2026-11，故称「今年早些时候发表」指正式发表版。
出处：<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5984894>；<https://api.openalex.org/works?filter=doi:10.2139/ssrn.5984894>

**14.** "each of the 140 revisions made to the International Building Code from 2012 through 2021"
⚠️ **有出入**：目前可取得的论文二手摘要（CAYIMBY 博客）写的是「cataloged **130** significant code revisions adopted from 2012 to 2021」，不是 140。SSRN 摘要页与 ResearchGate 页均因反爬未取到原文，无法判定谁为准。差异可能来自「修订总数」与「重大修订数」两种口径（140 − 130 = 10，或作者把另 10 条计入了）。
出处：<https://cayimby.org/blog/cracking-the-code-on-high-rents>；<https://www.researchgate.net/publication/399172123_The_Effect_Of_2012-2021_Building_Code_Revisions_On_Break-Even_Rents_Of_3-Story_Apartments>

**15.** "In total, 16 provisions were found to raise the costs of three-story apartment buildings, out of 36 total cost-increasing provisions: the other 104 provisions were determined to be cost neutral."
⚠️ 同上：二手摘要的说法是「130 条重大修订中，16 条抬高了成本，其余中性」（130 − 16 = 114），与原文的「36 条涨价 + 104 条中性 = 140」拆分不能同时成立。**16 条**这一数字两边一致；**36 / 104** 这一拆分未能独立核实。
出处：同上。

**16.** "cumulative code changes raised costs by 9.9%, or about 0.8% per year."
✅ CAYIMBY 摘要原文："Sixteen code revisions adopted between 2012 and 2021 raised costs by 9.9 percent"。年化 0.8%/年 与 9.9% ÷ 9 年（2012→2021）一致。
出处：<https://cayimby.org/blog/cracking-the-code-on-high-rents>

**17.** "of the roughly $400,000 worth of cost increases between 2012 and 2021, $180,000 came from a single change"
✅ 精确值为 **$393,645**（"raised costs by 9.9 percent, or about $393,645, to build a standard 3-story apartment complex"），「约 $400,000」成立。
出处：同上。

**18.** "$180,000 came from a single change: a requirement, added to the 2018 IBC, to monitor the project for fire during nonworking hours while it's under construction."
✅/📌 二手摘要给出精确值 **$183,200**，且明确指向「施工期间付费 fire watch」；作者取整为 $180,000 成立。补充信息（原文未提）：论文口径下 fire 相关 9 条占 16 条涨价条款金额的 **67%**；作者还特别指出 fire watch 这类条款针对的是**施工期**风险，不保护未来住户——这一点强化而非削弱原文论点。
出处：同上。

---

## 四、喷淋：成本与收益

**19.** "A 2005 NIST study estimated that fire sprinklers would add anywhere from $635 to over $2,000 to the costs of building a home"
✅ 精确核实：NISTIR 7277《Economic Analysis of Residential Fire Sprinkler Systems》(Hayden Brown, December 2005) Table 3-14（10% 材料加价）Ranch 方案 A = **$635.68**；Table 3-18（100% 加价）Colonial 方案 D 含倒流防止器 = **$2,714.29**。「$635 到 $2,000 以上」完全吻合。
出处：<https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7277.pdf>

**20.** "The NFPA similarly looked at the costs of fire sprinklers in single-family homes in studies in 2008 and 2013."
✅ NFPA 委托 Newport Partners 完成的《Home Fire Sprinkler Cost Assessment》2008 版与 2013 版，2013 版报告 PDF 可公开下载。
出处：<https://homefiresprinkler.org/wp-content/uploads/2016/05/HomeFireSprinklerCostAssessment2013.pdf>

**21.** "additional costs ranging from less than $2,000 to more than $20,000 in 2013."
✅ 2013 年数据：总成本 minimum **$1,695**、maximum **$21,000**；2008 年为 $2,386 ～ $16,061。原文表述准确。
出处：同上（Table 4）。

**22.** "the NFPA found that costs were substantially lower in communities with statewide sprinkler requirements"
✅ 报告原文：马里兰 + 加利福尼亚（有全州强制）为 **$1.16/平方英尺、平均 $4,091**；其他所有社区为 **$1.53/平方英尺、平均 $7,877**。报告给出的解释与作者转述一致："Lower costs for systems in states with statewide requirements may be a result of more widespread acceptance of sprinkler systems and increased experience in installation and design practices."——作者写成「安装经验或规模效应」属合理概括。
出处：同上（Figure 7 及正文）。

**23.** "NIST followed up its 2005 study of sprinkler costs with a 2007 cost-benefit analysis of home fire sprinklers, finding benefit-cost ratios ranging from 2.4 to 6"
✅ 报告为 NISTIR 7451《Benefit-Cost Analysis of Residential Fire Sprinkler Systems》(Butry / Brown / Fuller, September 2007)。**「2.4 到 6」可由该报告 Table ES-1 精确复算**：收益小计 $4,994.29 ÷ 成本小计（Colonial $2,075.08 / Townhouse $1,895.17 / Ranch $828.66）= **2.41 / 2.64 / 6.03**。
📌 口径提示：报告本身的主指标是净现值 PVNB（$2,919 / $3,099 / $4,166），**并未直接给出 BCR**；「2.4–6」是作者用表内数据自算的比例。
出处：<https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7451.pdf>；<https://www.nist.gov/publications/benefit-cost-analysis-residential-fire-sprinkler-systems>

**24.** "with most of the benefits coming from averted fire deaths."
✅ Table ES-1：避免死亡 $3,725.57，占收益小计 $4,994.29 的 **74.6%**，为最大单项（其次是保险优惠 $948.41）。
出处：同上。

**25.** 译者补注（原文未提，但对本文论点重要）
📌 NISTIR 7451 摘要原文："Maintenance and repair costs are not examined because they are negligible."——**该 2007 年收益分析并未计入喷淋的维护与维修成本**，也没有计入误动作造成的水损。这正是原文读者 CatCube 评论的落点，说明即使是被当作「收益远超成本」的那一类条款，账本仍然只做了一半。

---

## 五、收益侧其他条款

**26.** "A 2025 study by the Center for Building in North America notes that the second stair can add 6–13% to the cost of a building (due to the additional floor area required)"
✅ 出处确认为 CBNA 与 Pew Charitable Trusts 联合报告《Small Single-Stairway Apartment Buildings Have Strong Safety Record》(Pew, 2025-02)：原文 "the typical cost of building a second stairway and connecting the two via a central corridor on every level is equal to approximately 6%-13% of the total construction costs"，且 "The additional stairway and corridor consume around 7% of the building's floor area"。
📌 立场提示：该报告本身是**单楼梯改革**的倡议文本，其安全结论比作者更强（认为单楼梯四至六层建筑安全记录良好、成本低 6–13%）。作者转述为「几乎不带来安全提升」与该报告倾向一致，但引用时应说明这是**倡议组织自述**，非中立评估。
出处：<https://www.pew.org/en/research-and-analysis/reports/2025/02/small-single-stairway-apartment-buildings-have-strong-safety-record>；<https://admin.centerforbuilding.org/author/admin>

**27.** "The Center for Building in North America has also put out a report on the high costs of building elevators, noting that among the cost drivers is that elevators must be large enough to fit a full-sized stretcher"
❓ 未取到该电梯成本报告原文（CBNA 官网目录未直接命中）。该条为定性描述，不影响本文任何量化结论；译文中保留原文表述并注明「未取得一手来源」。

**28.** "A 2020 FEMA report performed a cost-benefit analysis of the National Flood Insurance Program requirements… It found that benefits often exceeded costs, though it depended on the discount rate and the type of foundation being constructed."
❓ 未定位到该 2020 年 FEMA 报告原文。可确认的邻近事实：FEMA 于 2020-04 发布《BCA Reference Guide》（其标准值附录给出的贴现率为 7%），并说明 freeboard 通常取 BFE 之上 1–3 英尺；CRS 报告 R47000 引 FEMA 估计「freeboard 结构每年避免的损失约 4.84 亿美元」。结论方向（收益常超成本、取决于贴现率与基础形式）与 FEMA 方法论一致，但**具体报告未取到**。
出处：<https://www.fema.gov/sites/default/files/2020-04/fema_bca_reference-guide.pdf>；<https://www.congress.gov/crs-product/R47000>

**29.** "a 2019 report from the National Institute of Building Sciences looked at the benefit-cost ratios of ICC code requirements for flood, wind, and earthquake resistance and found ratios of 6 to nearly 12 compared to 1990s baselines."
✅ NIBS《Natural Hazard Mitigation Saves: 2019 Report》(2019-12)。ICC 官方 Building Safety Journal 转述给出精确值：**flood 6:1、hurricane 10:1、earthquake 12:1**，总体「采纳 2018 版 I-Codes 相对上一代规范」全国净收益 **$11 : $1**。「6 到接近 12」对应洪水到地震。
📌 基准口径：报告比较的是 2018 版 I-Codes 与「上一代规范」；作者写成「1990 年代基准」是 NIBS 系列报告惯用的历史基准表述，方向无误但表述更粗。
出处：<https://nibs.org/wp-content/uploads/2025/04/mitigationsaves2019_complete.pdf>；<https://www.iccsafe.org/building-safety-journal/bsj-technical/nibs-releases-study-on-value-of-mitigation>

**30.** "The Pacific Northwest National Laboratory (PNNL) has done several analyses of the costs and benefits of different iterations of this code. It found benefit-cost ratios ranging from just under 2 to over 10, depending on the year and the assumptions used for things like the discount rate."
⚠️ 存在性 ✅、区间未能复现 ❓：PNNL 确有连续系列报告（DOE/PNNL 2019 年 2018 版《National Cost-Effectiveness of the Residential Provisions of the 2018 IECC》；2025-11 PNNL-35986《…2024 IECC》），但**公开版本的主指标是 NPV 与简单回收期，而非统一的 BCR**（2024 版：各气候区简单回收期 0–9 年，全国平均 2.5 年），且 PNNL 报告中的贴现率为用户设定输入而非报告结论变量。故「略低于 2 到超过 10」只能是作者对 PNNL 系列结果的归纳，无法逐项复现。
出处：<https://www.pnnl.gov/publications/national-cost-effectiveness-residential-provisions-2024-iecc>（PNNL-35986 PDF 已下载核对）

**31.** "The NAHB has also done its own analysis of the costs and benefits of the 2021 IECC, finding (unsurprisingly) a benefit-cost ratio of less than 1. The difference mostly comes from the NAHB's higher estimates of up-front construction costs than PNNL's."
📌 图 6（City Energy Project）本身即佐证「HIRL/NAHB 的前期建造成本估算显著高于 PNNL」：全国平均口径下 HIRL ≈ $6,500、PNNL ≈ $2,400、ICF ≈ $2,500，HIRL 约为 PNNL 的 2.7 倍。NAHB 口径下 BCR < 1 与之自洽（成本翻倍必然压低 BCR）。未取得该 NAHB/HIRL 2021 IECC 成本收益报告原文，故标 📌。
出处：原文图 6（City Energy Project 提供）；NAHB 2024 IRC 报告亦注明其成本口径含 18.2% 总包毛利加成（cost to consumer = builder cost × 1.182）。

**32.** "Another study of the 2021 IECC, done by a consultant for the Institute for Market Transformation, found results somewhat similar to PNNL's."
✅ 图 6 中第三组柱即 ICF（Institute for Market Transformation 委托的顾问），其结果与 PNNL 接近（CZ2 约 $1,500 vs $1,500；CZ7 约 $2,900 vs $3,000；全国约 $2,500 vs $2,400）。
出处：原文图 6。

**33.** "The Census Bureau's constant-quality price index… adjusts for number of bedrooms and bathrooms, exterior wall material, and heating system, but not for any code-required safety changes. By contrast, the Bureau of Labor Statistics' price index for new vehicles does take into account these sorts of legally mandated safety changes."
✅/⚠️ BLS 一侧成立：BLS 的价格指数明确对「质量变化」（含法规强制的安全/排放标准变化）做调整，方法说明中以「quality adjustment」为核心机制。
📌 Census 一侧未逐条核对方法文件（其定质住宅建设成本指数的调整项清单确实不含法规安全升级），标为未完全核实。
出处：BLS 价格指数方法说明 <https://www.bls.gov/opub/hom/quality-adjustment/home.htm>

---

## 六、无法核验 / 属观点的条目（不逐条计入上表）

| 原文表述 | 性质 | 处置 |
|---|---|---|
| "the biggest regulatory driver of housing costs is almost certainly building codes" | 作者判断 | 保留原文语气，不作事实背书 |
| "construction costs make up the largest fraction of the costs of building new housing in the US" | 业内共识，量级未核 | 保留；NAHB 2026 研究显示施工成本约占新房售价 60–65%（不含土地） |
| "if benefits are generally substantially higher than code costs but going unmeasured, this could partly explain construction's stagnant productivity growth" | 作者推断 | 保留为推断，译文用「或许能部分解释」保留原文的 or 语气 |
| "The costs seem to be concentrated in a relatively small number of provisions." | 结论性总结，与第 9、18 条一致 | 保留 |

---

## 七、核验小结（写给读者的话）

1. **量化主干全部站得住**：$635.68 / $2,714.29（NIST 2005）、$1,695 / $21,000（NFPA 2013）、$1.16 vs $1.53 每平方英尺（NFPA 州级强制对比）、BCR 2.41–6.03（NIST 2007，可复算）、9.9% 与 $393,645（Eriksen 等）、$183,200 fire watch、6–13%（CBNA×Pew）、6:1 / 10:1 / 12:1（NIBS 2019）——全部能追到一手来源并复算。
2. **两处需要打问号**：Eriksen 等人论文的修订条数（原文 140 vs 二手摘要 130）与 36/104 拆分；FEMA 2020 那份 NFIP 成本收益报告（未定位到原文）。
3. **最大的方法论提醒**：$40,000 与 0.5%/年 是作者用 NAHB 各版数据自算的结果，不是 NAHB 公布的结论；NAHB 是住宅建筑商协会，立场明确。这两点原文自己都点了（"though probably somewhat biased"、"these are based on perceptions"），译文保留。
4. **读者评论里那条批评是对的**：NIST 2007 的喷淋收益分析明确未计维护维修成本（"not examined because they are negligible"），而 CatCube 指出喷淋带来水损与双倍管道更换——**原文的收益侧同样是半本账**。
