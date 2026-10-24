# 《EdgePoint Q3 2026 EdgePoint commentary（Exponential）》数据核验表

> 核验对象：EdgePoint Wealth《Q3 2026 EdgePoint commentary》，作者 Jeff Hyrich，原文标注发布日 2026-10-20（网页版标注 Published October 22, 2026），PDF 共 10 页。
> 核验方式：SEC EDGAR 原始 10-K + XBRL companyfacts API、Yahoo Finance 历史行情 API、上市公司年报（TTI）、CIBC/Brown Advisory/Walmart IR 原始 PDF、第三方数据站（companiesmarketcap、Investing.com/Morningstar）。
> 核验时间：2026-10-24。
> **总体结论：核实一致 4 条 / 有出入（部分可核实、需加译注）6 条 / 查不到公开来源 2 条。**

---

## 1. Bessembinder《One Hundred Years in the U.S. Stock Markets》（SSRN, 2026-03-20）

**原文表述**
- 29,754 只美股普通股 / 29,081 家公司；样本期 1926-01 至 2025-12
- 百年间市场年化复合 10.1%；59.1% 毁灭财富 / 37.2% 抵消 / 3.7% 创造
- 另称"过半个股终生买入持有回报为负"；脚注 iii 引 2024 年 7 月旧版称"四分之一（23%）个股亏损超 90%"

**核验来源**
- SSRN 摘要页：https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6438198 （ Posted: 20 Mar 2026，Last Revised: 27 Sep 2026）
- ASU 教职页：https://wpcarey.asu.edu/department-finance/faculty-research/do-stocks-outperform-treasury-bills
- 论文数字复刻页（非官方，逐项标注"source-exact"）：https://cgodlewski.github.io/100-US-stock-markets/
- 二手引用：https://www.ifa.com/articles/stock_market_concentration_accelerated_-_here_what_data_shows ；https://larryswedroe.substack.com/p/a-century-of-stock-market-winnersand ；https://www.cnbc.com/make-it/2026/05/08/what-investors-can-learn-from-100-years-of-stock-market-returns.html ；https://www.morningstar.com/stocks/why-most-stocks-arent-worth-owning

**结论：✅ 核实一致。** 摘要原文为 "29,754 common stocks … over the 100-year period from 1926 to 2025"；分档为 17,197 家（59.13%）毁灭、10,802 家（37.15%）抵消、1,082 家（3.72%）创造全部 90.96 万亿美元净财富创造；百年价值加权市场年化 10.1% vs 国库券 3.3%；中位数买入持有回报 −6.9%，仅 48.2% 为正（即"过半为负"成立）。

**建议译注**：可将 59.1% / 37.2% / 3.7% 直接照译；建议补一句"3.7% 即 1,082 家公司"，读者更易理解"少数股票创造全部财富"。
⚠️ 唯"23% 亏损超 90%"一项未找到与脚注 iii（2024 年 7 月 SSRN 旧版）逐字对应的公开表述，公开文献里更常见的是 2018 年 JFE 版本的"约四分之一"表述——**建议译注中标"原文引 2024 年 7 月旧版论文"**，不要当作 2026 年论文的结论。

---

## 2. Bessembinder 全球研究（64,000 只全球股票，1990–2020）

**原文表述**：1990–2020 区间 2.4% 创造财富 / 57.7% 毁灭 / 39.9% 抵消（脚注 iv 引 SSRN, 2020-10-14）

**核验来源**
- 论文 PDF（作者版）：https://r.jordan.im/download/investing/bessembinder2023.pdf （正文：36,818 家、57.72% 负向财富创造；top 2.4% 创造 US$75.7T；39.9% 为正但仅抵消损失）
- 正式期刊版：Financial Analysts Journal 2023, 79(3), 33-63，doi 10.1080/0015198X.2023.2188870（https://rpc.cfainstitute.org/research/financial-analysts-journal/2023/long-term-shareholder-returns-evidence-from-64000-global-stocks）
- SSRN：https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3710251

**结论：✅ 核实一致。** 三个百分比与论文正文逐字对应（2.4% / 57.7%（57.72%）/ 39.9%）。注意：该研究 2020 年 10 月为 SSRN 工作论文，2023 年 4 月已正式发表于 FAJ。

**建议译注**：译注可补"该研究 2023 年正式发表于《Financial Analysts Journal》"，避免读者误以为是尚未发表的预印本。

---

## 3. 巴菲特 2022 年致股东信引文 + "300~400 个决策 / 约 12 个 / 3%–4%"

**原文表述**
> "In 58 years of Berkshire management, most of my capital-allocation decisions have been no better than so-so… Our satisfactory results have been the product of about a dozen truly good decisions… Over time, it takes just a few winners to work wonders." — Warren Buffett, Berkshire Hathaway 2022 Letter to Shareholders
- 并称："some commentators estimate Buffett made between 300 to 400 meaningful decisions"，"3% to 4% of all decisions truly moved the needle"

**核验来源**
- 官方年报 PDF：https://www.berkshirehathaway.com/letters/2022ltr.pdf （第 254–259 行、285–286 行）

**结论：⚠️ 引文逐字核实一致，但两处推断查不到出处。**
- 引文核对：原文为 "In 58 years of Berkshire management, most of my capital-allocation decisions have been no better than so-so. In some cases, also, bad moves by me have been rescued by very large doses of luck… Our satisfactory results have been the product of about a dozen truly good decisions – **that would be about one every five years** – and a sometimes-forgotten advantage that favors long-term investors such as Berkshire." 以及 "Over time, it takes just a few winners to work wonders."（确在 2022 年信中，原文用省略号合并两段，语义未失真）✅
- "300 至 400 个重大决策"：全网检索未找到任何可追溯的统计出处，除 EdgePoint 本文外无第二个来源 ❓
- "3%–4%"：由 12 ÷ (300~400) 反推，属 EdgePoint 自行算术 ✅（算术正确），但同样无独立出处。

**建议译注**：引文可照译（建议补全被省略的 "that would be about one every five years"，它比"约 12 个"更能说明"每五年才一次"的稀缺性）。
⚠️ 对"300–400 个决策"必须加译注：**"（原文称引自某些评论者，未具名；未找到可核实的公开统计。'3%–4%'为原文据此前者推算。）"** —— 这是全文最容易被读者当作"巴菲特本人说过"的表述，风险最高。

---

## 4. Raymond James《How to Find, Hold, or Build Top 10% Long Term Equity Performers》（2024-03-05）

**原文表述**：80% 首年销售增速 <15%、7% >30%、中位年化销售增速 8%；仅 5% 亏损；84% 利润率扩张、中位数 +6.1%；约 60% 自由现金流高于会计利润；起点 56% 正 ROE 但 <20%，终点近 70% ROE >20%（正文"中位 ROE 从 17% 升到 27%"，图表标注 17.2% → 21.1%，脚注 "*ex: negative EPS/equity names"）；约 70% 十年回购缩股；74% 起手 P/E <20x（其中 15% <10x、59% 在 10–20x）。

**核验来源**
- 唯一公开承载者（EdgePoint 自身网页版，含全部图表）：https://www.edgepointwealth.com/article/Q3-2026-edgepoint-commentary
- 作者身份可核：Tavis McCourt 为 Raymond James 机构股票策略师（https://www.raymondjames.com/-/media/rj/common/investment-strategy-publications/investment-strategy-quarterly 署 "Tavis McCourt, CFA Institutional Equity Strategist"）

**结论：❓ 查不到公开来源（研报为付费机构产品，未公开流通）。** 多次检索（标题、作者、页标题、具体百分比组合）均未找到报告原件或可靠二手引用。

**内部一致性检查（可作为译注依据）**
- 图表百分比与正文自洽：首年增速分布图 43/23/14/6/5/3/7（<5% 至 >30%），<15% 合计 43+23+14 = 80% ✅；>30% = 7% ✅。EBIT 利润率图中"正向扩张"各档合计 19+15+13+11+8+8+4+4+3+2 ≈ 84%–87%，与"84% 扩张"大致吻合 ✅。P/E 起始分布图：2+13+22+37 = 74%（<20x）✅，其中 <10x = 2+13 = 15% ✅、10–20x = 22+37 = 59% ✅。ROE 起始分布 56+21+5+8 = 90%+（加上负值档）✅；终点 >20% 档为 48% + 21%（20%–50%）+ 5%（50%+）= 74%，"近 70%"✅。缩股图 "Top 10% performers 有 62% 位于 <-5% 档"——**与正文"约 70% 减少股本"方向相反，该档应为"<5% 区间中位数以上"，图形读法有歧义**。
- **ROE 矛盾判断**：正文"中位 ROE 从 17% 升到 27%"与图注"Start: 17.2% / End: 21.1%"不一致，且脚注 "*ex: negative EPS/equity names"表明图表中位数**剔除了负 EPS/负权益的公司**，样本口径比正文窄。→ 这是**口径差异（而非单纯笔误）**：正文中位数含全部公司（含负权益），图表中位数为剔除极端值后的样本。

**建议译注**：对正文与图表的 ROE 数字必须并列标注，例如："（正文称中位 ROE 由 17% 升至 27%；原文图表标注为 17.2%→21.1%，且图表样本剔除了负 EPS/权益公司，故两者口径不同。）" 缩股"约 70%"亦建议注明"（原文图表为各区间分布，合计口径以原文为准）"。

---

## 5. CIBC《Short-term orientation of equity market…》（2025-05）

**原文表述**：美股平均持有期从 1975 年的 8.7 年降到 2025 年的"略高于 7 个月"，持有时间减少 93%。

**核验来源**
- 原始 PDF：https://www.cibc.com/content/dam/cibc-public-assets/asset-management/pdfs/short-term-orientation-of-equity-market-en.pdf

**结论：⚠️ 数据点本身核实一致，但口径表述与原文措辞略有出入，且 93% 为 EdgePoint 自算。**
- 原文图表（Refinitiv Workspace as at March 14, 2025，倒数率 1/换手率，指数 TOTMKUS）：1975 年 **8.7 年**，2025 年 **0.6 年** ✅ → 0.6 年 = 7.2 个月，"略高于 7 个月"成立 ✅
- 但 CIBC 自己的文字表述是：摘要 "from 9 years in the mid-1970s, to slightly more than **6 months** in 2025"；正文 "decreased from 9 years in the mid-1970s to **just over half a year** in 2025"。即原文口径更接近"约 6 个月/刚过半年"，"7 个多月"是 EdgePoint 把 0.6 年换算成月份后的表述（换算本身没错，但比源文件口径更"精确"）。
- "93%"不在 CIBC 原文中，为 EdgePoint 自行计算：(8.7 − 0.6) / 8.7 = 93.1% ✅ 算术正确。
- 作者姓名：CIBC 文件中为 "Daniel Delany"，EdgePoint 写作 "Daniel Delaney"。

**建议译注**：建议写成"（CIBC 原文表述为'从 1970 年代中期的约 9 年降至 2025 年的刚过半年；图表数值为 8.7 年 → 0.6 年，即约 7.2 个月；'减少 93%'为原文据此外推。）"；作者名建议按 CIBC 原文写 Delany 或加注。

---

## 6. EdgePoint 前一季评论（2021 Q3《Where has all the time gone?》）中的 66%

**原文表述**："A previous commentary showed that there was 66% average spread between the calendar-year high and low stock prices over the previous decade for the 10 largest companies in the MSCI World Index."

**核验来源**
- EdgePoint 评论总览页：https://www.edgepointwealth.com/commentary-overview/ （页面为 JS 动态渲染，静态 HTML 仅含 2022 年以后 PDF 链接）
- 检索到的 EdgePoint 历史评论 PDF 仅见 Q3 2022、Q3 2023、Q3 2024、Q3 2025、Q3 2026；未检索到 2021 Q3《Where has all the time gone?》

**结论：❓ 查不到公开来源。** 该 66% 是 EdgePoint 自己前一季的自算结果，属"自引自证"，外部无从复核；且 2021 Q3 原文在本次检索中未能定位（可能已下线）。

**建议译注**：建议标注"（EdgePoint 2021 年第三季度评论的自算数据，原文未公开第三方复核。）"——不要把 66% 表述为客观事实。

---

## 7. 指数中位市值与 RBC 市值（FactSet，截至 2026-09-30）

**原文表述**：S&P 100 成分股中位市值 US$217.2B；S&P MidCap 400 中位市值 US$8.0B；RBC 市值 US$273.4B；全球市值超过 US$217.2B 的公司不足 100 家。

**核验来源**
- 全球市值排名（2026-10-24 抓取）：https://companiesmarketcap.com/ —— Royal Bank of Canada 列第 56 位，**US$278.50B**；第 78 位 Arista Networks US$217.39B、第 79 位 GE Vernova US$217.06B → **市值 > US$217.2B 的公司约 78 家**
- RY.TO 历史行情（Yahoo Finance chart API）：2026 年 9 月收盘 C$279.94；现价 US$201.17

**结论：⚠️ 大部分可核实，两项无法独立验证。**
- RBC 市值 US$273.4B ✅（与 10 月 24 日 companiesmarketcap 的 US$278.50B 基本一致，差约 2%，可由汇率/股本口径差异解释；RY.TO 2026 年 9 月 30 日收 C$279.94，按约 1.38–1.41 的 USD/CAD 与约 13.8 亿股折算为 US$273–279B，与原文数值吻合）
- "全球市值超过 US$217.2B 的公司不足 100 家" ✅ 成立（现约 78 家）
- S&P 100 中位市值 US$217.2B：与公开数据自洽（全球第 78 位约 US$217B，可对应 S&P 100 中位成员量级）——但**未经 FactSet 原始口径独立复核**，标 ⚠️
- S&P MidCap 400 中位市值 US$8.0B：量级合理（2026 年中盘区间约 US$2–50B，中位 8B 合理），同样**无法独立复核**

**建议译注**：RBC 与"不足 100 家"可直接照译；两个指数中位市值建议保留"（FactSet 口径，2026-09-30）"原始出处标注，不必额外解释。

---

## 8. 中盘相对估值（Brown Advisory 两份材料）

**原文表述**
- 引 Brown Advisory《Revisiting U.S. Mid-Cap Equities…》2026-01-21：Russell Midcap 相对 Russell Top 200 自 1978 年指数发布以来，2025 年底接近历史最低区间
- 引 Brown Advisory《U.S. Mid-Cap Growth Equity Strategy》2026-06：过去 90 年中十年滚动相对收益约 70% 的时间中盘占优；当前滚动十年落后 5.3 个百分点，为有记录以来最差之一；3 段明显负值区间：mid-1950s、1997–2004、2019–today

**核验来源**
- Brown Advisory 2026-01 文章（官网）：https://www.brownadvisory.com/us/insights/revisiting-us-mid-cap-equities-strategic-opportunity-time-market-concentration
- Nasdaq 转载（2026-02-24）：https://www.nasdaq.com/articles/revisiting-us-mid-cap-equities-strategic-opportunity-time-market-concentration
- 图表方法学说明与 EdgePoint 脚注 viii 完全一致："Relative valuation model is the Russell Midcap Index vs. Russell Top 200 Index… relative Trailing and Forward P/E, Price to Book, Price To Sales and from 2002 Price to Cash Flow; from March 31, 2016 forward Jefferies' estimates… as of December 31, 2025."

**结论：⚠️ 第一部分口径核实一致（并发现原文脚注笔误）；第二部分文档未找到。**
- Brown Advisory 1 月文确有"Mid-Caps Are Historically Cheap Relative to Large-Caps"一节与 EdgePoint 所引的同一张相对估值图（Russell Midcap vs Russell Top 200），且同样以 2025-12-31 为数据截止日、"90 年代末是上一次估值差如此陡峭、其后经历十年中盘跑赢"的表述与 EdgePoint 叙述吻合 ✅
- **原文笔误**：EdgePoint 该图脚注写 "Source: Brown Advisory … January 21, 2026. **As at December 31, 2026**"，但图表区间为 1978–2025、正文亦写"At the end of 2025"，应为 **2025** 之误。
- Brown Advisory 2026 年 6 月《U.S. Mid-Cap Growth Equity Strategy》材料（十年滚动相对收益图）**未检索到公开可访问版本**，"约 70%""-5.3 个百分点""最差之一""3 段负值区间"无法独立复核 ❓

**建议译注**：① 脚注年份笔误建议在译文注释中说明"（原文图注作 2026 年 12 月 31 日，应为 2025 年 12 月 31 日）"；② 十年滚动收益图的数据建议标注"（引自 Brown Advisory 2026 年 6 月策略材料，公开渠道未检索到原文件）"。

---

## 9. S&P MidCap 400 与 S&P 100（1999-12-31 → 2014）

**原文表述**：1999 年底投 S&P MidCap 400 到 2014 年翻约 3 倍，而 S&P 100 持平（FactSet，截至 2026-09-30）。

**核验来源**（Yahoo Finance 历史指数行情 API）
- S&P 400（^MID / ^SP400）：1999-12 收 **444.67** → 2014-12 收 **1,452.44**（**3.27 倍**）→ 2026-09 收 3,595.97
- S&P 100（^OEX）：2000-01 收 754.26、2000-12 收 **686.45** → 2014-12 收 **908.38**（相对 1999 年底约 745，约 **+22%**）；2026-09 收 3,822.99

**结论：✅ 核心数字核实一致（按价格指数口径）。** 中盘 3.27 倍 ≈ "tripled"；大盘 15 年仅 +22%，称 "flat" 尚属公允（对照三倍）。

**建议译注 / 口径提醒**：⚠️ 原文该图脚注写 "Total returns in US$"，但"3x vs Flat"这组标注只在**价格指数**口径下成立（若按含股息总回报，中盘约 4.7 倍、大盘约 1.9 倍，大盘便不能算 "flat"）。建议译注："（原文图表脚注标注为总回报口径，但'3 倍 vs 持平'的表述与价格指数水平一致。）"

---

## 10. 四家公司 2000–2025 年化数据（FactSet 口径）

### 10.1 Ross Stores ✅ 全部核实一致（且可精确复现）
| 项目 | 原文 | 独立核验 |
|---|---|---|
| 收入 +8.9% | 8.9% | FY2000 收入 US$2,709.0M → FY2025（截至 2026-01-31）US$22,750.6M，25 年 **8.89%** ✅ |
| 股本 −2.7% | −2.7% | FY2000 摊薄股数（拆股调整 ×8 后）→ FY2025 324.4M，约 **−2.8%** ✅ |
| EPS +14.3% | 14.3% | FY2000 摊薄 EPS US$1.82（拆股调整 ÷8 = 0.2275）→ FY2025 US$6.61，**14.36%** ✅ |
| 股价 $2→$180 / +19.5% | 同 | Yahoo 月收盘：2000-12 **$2.109** → 2025-12 **$180.14**，**19.47%** ✅ |
| 净利率 6%→9% | 同 | FY2000 5.60% → FY2025 9.43% ✅ |
| P/E 9x→27x | 同 | 2.109/0.2275 = **9.3x**；180.14/6.61 = **27.3x** ✅ |

来源：Ross Stores FY2000 10-K（SEC，2001-04-27 报送，accession 0000912057-01-510903，"SALES $2,709,039"、净利 $151,754、摊薄 EPS $1.82，已按 1997/1999 两次 2:1 拆股调整）；SEC XBRL companyfacts CIK0000745732（FY2025 收入 22,750.6M、净利 2,145.0M、EPS 6.61、摊薄股 324.4M）；Yahoo Finance ROST 月线。

### 10.2 Walmart ✅ 全部核实一致（可精确复现）
| 项目 | 原文 | 独立核验 |
|---|---|---|
| 收入 +5.4% | 5.4% | FY(截至 2001-01-31) 收入 US$191,329M → FY(截至 2026-01-31) US$713,163M，25 年 **5.42%** ✅ |
| 股本 −2.1% | −2.1% | 4,496M×3（2024 年 3:1 拆股）→ 8,022M，**−2.06%** ✅ |
| EPS +7.3% | 7.3% | FY2001 摊薄 EPS US$1.40 ÷3 = 0.4667 → FY2026 US$2.73，**7.30%** ✅ |
| 股价 $18→$111 / +7.6% | 同 | Yahoo 月收盘：2000-12 **$17.708** → 2025-12 **$111.41**，**7.64%** ✅ |
| 净利率 3%→3% | 同 | 3.29% → 3.07% ✅ |
| P/E 38x→41x | 同 | 17.708/0.4667 = **37.9x**；111.41/2.73 = **40.8x** ✅ |

来源：Walmart FY2001 10-K（accession 0001021408-01-500157，Exhibit 13 "11-Year Financial Summary"：FY2001 净销售 191,329、净利 6,295、摊薄 EPS 1.40；FY2000 165,013 / 5,377 / 1.20）；SEC XBRL CIK0000104169（FY2025 收入 680,985、EPS 2.41；FY2026 收入 713,163、EPS 2.73、摊薄股 8,022M）；Yahoo WMT 月线。

**正文旁证亦成立**："Between 2000 to 2015, Walmart's stock appreciated from US$17.71 to US$20.43" ✅（Yahoo：2000-12 $17.708、2015-12 $20.433，15 年 0.96%/年 ✅）；"a decade later 股价基本持平" ✅（2010-12 收 $17.977）。

⚠️ **但正文另有一处 P/E 说法与本表及市场数据不一致**：正文称 "its P/E valuation had fallen from roughly from 33x to about 12x"。核验：2010 年底 P/E = 17.977 ÷ (4.47/3) = **12.1x** ✅（12x 成立），但起点 33x ✗——实际约 38x（与本表 38x 一致）。**建议译注："（原文正文称 P/E 由约 33x 降至约 12x；按 FactSet/市场数据，起点约 38x，与本节表格一致。）"**

### 10.3 Techtronic Industries ⚠️ 基本可核实，价格对无法定位
| 项目 | 原文 | 独立核验 |
|---|---|---|
| 收入 +13.9% | 13.9% | FY2000 营业额 HK$4,551.5M → FY2025 收入 US$15,259.5M（≈HK$119B），**≈13.9%** ✅ |
| 股本 +2.0% | +2.0% | 与 TTI 历年股本扩张（~1.62B 股）量级相符 ✅（未逐年核） |
| EPS +14.6% | 14.6% | FY2000 基本 EPS 16.92 港仙 → FY2025 约 HK$5.5，约 **14.6–15%** ✅（量级） |
| 净利率 4%→8% | 同 | 2000 税前利润 HK$215.0M/4,551.5M = 4.7%；2025 税前 US$1,216.4M/15,259.5M = 8.0% ✅ |
| P/E 5x→18x | 同 | 起：0.1692×5 ≈ HK$0.85；终：HK$5.5×18 ≈ HK$99 ✅（量级） |
| 股价 $1→$90 / +20.6% | 同 | ❓ 无法定位：Yahoo 0669.HK 无 2000 年数据；2025 年月度收盘在 HK$87.85–127.60 区间波动、2025-12 收 HK$106.50、2026-08 收 HK$129.00，"$90"对应不到明确的年末价 |

来源：TTI《Annual Report 2004》五年财务摘要 https://www.ttigroup.com/sites/default/files/2022-09/04ar_Print.pdf ；TTI《Annual Report 2025》 https://www.ttigroup.com/sites/default/files/2026-03/ar2025.pdf ；Yahoo 0669.HK 月线。

**建议译注**：Techtronic 表格原文注明"所有数字以当地货币计"（即港元），建议保留；股价对"$1 → $90"建议加注"（原文 FactSet 数据，无法在公开行情中逐点复核；TTI 2025 年内股价区间约 HK$88–128）"。

### 10.4 Home Depot ✅ 核心成立，个别比率有 0.2–0.4pp 差异
| 项目 | 原文 | 独立核验 |
|---|---|---|
| 收入 +5.3% | 5.3% | FY2000 US$45,738M → FY2026 US$164,683M（26 年）= 5.06%；→FY2025 US$159,514M（25 年）= 5.19%。与 5.3% 差 0.1–0.25pp（疑为日历化口径差异）⚠️ |
| 股本 −3.3% | −3.3% | 2,346M → 995M，26 年 **−3.26%** ✅ |
| EPS +10.7% | 10.7% | $1.10 → $14.23（26 年）= 10.31%；→$14.91（25 年）= 11.0%。与 10.7% 差 0.3–0.4pp ⚠️ |
| 股价 $46→$344 / +8.4% | 同 | Yahoo 月收盘：2000-12 **$45.688** → 2025-12 **$344.10**，**8.41%** ✅ |
| 净利率 6%→9% | 同 | 5.64% → 8.60%（≈6%→9%）✅ |
| P/E 41x→24x | 同 | 45.688/1.10 = **41.5x**；344.10/14.23 = **24.2x** ✅ |

来源：Home Depot FY2001 10-K 五年摘要（accession 0000950144-01-005194："Net Sales $45,738 / Net Earnings $2,581 / Diluted EPS $1.10"）；SEC XBRL CIK0000354950；Yahoo HD 月线。

**建议译注**：HD 收入与 EPS 年化与公开财报复算值相差 0.1–0.4 个百分点，量级无误，建议照译并保留"FactSet 口径"标注。

---

## 11. Walmart IPO 价格与"约 40,000 倍"

**原文表述**："It had an initial public offering of US$16.50 per share ($0.0027 after subsequent splits) and increased to US$104, or about 40,000 times excluding dividends."

**核验来源**
- Walmart 官方拆股史页：https://stock.walmart.com/stock-data/stock-split-history —— "On Oct. 1, 1970, Walmart offered 300,000 shares of its common stock to the public at a price of $16.50 per share. Since that time, we have had 11 two-for-one (2:1) and 1 three-for-one (3:1) stock splits."；表内 100 股的 "Cost per Share" 由 $16.50 → 1971 年 2:1 后 $8.25 → … → 2024 年 2 月 3:1 后 **$0.002686**（614,400 股）
- CNBC（2024-11-19）：https://www.cnbc.com/2024/11/19/how-much-a-1000-dollar-investment-in-walmart-is-worth-now.html —— 首次公开发行 1970 年 10 月、$16.50/股，1972 年 8 月 25 日转入 NYSE
- GOBankingRates / Yahoo Finance："$10,000 → 约 $3.9 亿"（3,882,535%）

**结论：✅ 核心数字全部核实一致；⚠️ 一处常见误读需澄清，另原文本段未给 IPO 日期。**
- $16.50 发行价 ✅（Walmart IR 官方口径）
- 累计拆股倍数 = 2^11 × 3 = **6,144 倍**，拆股后 $16.50 / 6,144 = **$0.002686** ✅（原文"$0.0027"为四舍五入）
- "约 40,000 倍" = 104 / 0.002686 = 38,700 倍 ≈ 40,000 倍 ✅
- **"不含股息"这一标注是准确的**：常见的"$10,000 → 约 $3.9 亿"同样是**价格回报**口径（606 股 × 6,144 = 372 万股 × 约 $104 ≈ 3.88 亿美元），并非含股息的总回报倍数。EdgePoint 把倍数标为"不含股息"没有算错。

**建议译注 / 风险提示**
1. 若译者写成"1972 年 12 月 IPO"会出错：官方口径是 **1970 年 10 月 1 日**以场外方式发行（$16.50/股，30 万股），**1972 年 8 月 25 日**才转入纽交所。EdgePoint 原文本身未写日期，译者不要擅自加日期。
2. 建议加注："（40,000 倍为**价格**回报，不含股息；若按公开流传的'1 万美元 → 约 3.9 亿美元'说法，同样是不含股息的价格回报。）"
3. "涨至 US$104"与 Yahoo 显示 2026-09-30 收盘 **$103.92**、2026 年内区间约 $102.6–135 一致 ✅。

---

## 12. EdgePoint 自披露数据

**原文表述**：EdgePoint Global Portfolio Series F（截至 2026-09-30，加元、费后年化）：成立以来 13.68%、15 年 13.51%、10 年 10.10%、5 年 10.59%、3 年 16.24%、1 年 16.19%、YTD 11.66%；员工跟投超过 C$500 million（截至 2025-12-31）；Ross Stores 持仓 IRR 20.7%（2021-10-28 至 2026-05-21）。

**核验来源**
- EdgePoint 官方播客页（同一组数字的独立页面）：https://www.edgepointwealth.com/article/Q3-2026-edgepoint-podcast —— "EdgePoint Global Portfolio, Series F – Since inception (Nov. 17, 2008): 13.68%, 15-year: 13.51%, 10-year: 10.10%, 5-year: 10.59%, 3-year: 16.24%, 1-year: 16.19%, YTD: 11.66%" ✅
- 第三方数据（Investing.com / Morningstar）：https://www.investing.com/funds/edgepoint-global-portfolio-series-f-holdings —— Series F：YTD **11.66**、3Y **16.24**、10Y **10.10** ✅（与自披露逐项一致）
- 员工跟投：https://edgepointwealth.com/being-an-edgepointer —— "As of December 31, 2025, our internal partners hold some **$507 million** in company-related products … and are collectively one of our largest investors." ✅
- EdgePoint IRC 2025 年度报告：https://assets.ctfassets.net/kq9jrkvln56p/6cngQQYYTR5iTBsw3dv2DH/e959327a3c58d148dcb8a11a698e0ae1/EdgePoint_IRC_2025_Report_to_Investors.pdf （通篇为 IRC 冲突管理报告，**未包含** C$500M 跟投金额）

**结论：⚠️ 业绩与跟投数据已由独立来源证实；Ross 持仓 IRR 属自披露、无法外部复核。**
- 七个收益率数字 ✅（EdgePoint 官方另一页面 + Morningstar 数据完全一致）
- "超过 C$500 million" ✅（官网口径 ~C$507M，时点同为 2025-12-31，与脚注 xii 一致）
- **Ross Stores IRR 20.7%** ❓ 无法外部核实，但可做量级参照：ROST 收盘价 2021-10-28 **$112.97** → 2026-05-21 **$217.19**，价格回报年化约 **15.4%**，加股息约 **16.5%**。若 IRR 达 20.7%，需依赖期间分批加仓（2022 年 ROST 曾跌至约 $60 一带）与分批卖出才能实现——**并非不可能，但与"简单买入持有"口径差距明显**。

**建议译注**：IRR 处建议保留原文脚注含义（"Internal rate of return … is money-weighted return … The IRR is in US$"），并可加"（单一持仓内部收益率，无法由公开数据复核）"。

---

## 附：核验过程中发现的其他原文问题（建议一并提示译者）

1. **脚注日期笔误**：Russell Midcap vs Russell Top 200 相对估值图脚注写 "As at December 31, 2026"，而图表数据止于 2025 年、正文也写 "At the end of 2025"——应为 **2025**。
2. **图表脚注口径与正文标注不一致**：S&P 100 vs S&P MidCap 400 图脚注写 "Total returns in US$"，但 "3x / Flat" 的标注只在价格指数口径下成立（见第 9 条）。
3. **原文两处 P/E 说法互相打架**：正文"2000 年底 P/E 由约 33x 降至约 12x"与本节表格"38x → 41x"不一致；市场数据支持起点约 38x、2010 年底约 12x。
4. **持仓披露与官网持仓表存在张力**：原文"Important information – companies"称截至 2026-09-30 未持有 Ross Stores / Walmart / Home Depot；但 EdgePoint 官网 Global Portfolio 页面"Top 10 Holdings"仍列有 Ross Stores Inc. 3.35%（该表日期在静态页面上显示为异常的 "January 1, 1970"，无法确认时点，可能为 2026-09-30 之后更新）。建议以原文披露为准，但可加注。
5. **人名拼写**：CIBC 报告作者为 "Daniel Delany"，EdgePoint 写作 "Daniel Delaney"。
6. **原文自称 300–400 个决策与 3%–4%**：无外部出处，是全文最需要译注提示的一处（见第 3 条）。
