# 《Capital Allocation》（Morgan Stanley, Counterpoint Global）数据核验表

**核验对象**：Michael J. Mauboussin & Dan Callahan, CFA, *Capital Allocation: Results, Analysis, and Assessment*, Counterpoint Global Insights / Consilient Observer, 2025-11-05（88 页）

**核验日期**：2026-10-24
**核验人**：数据核验子代理
**本地原件**：`/tmp/ms_ca.pdf`（正文 1–57 页，脚注 58–70 页，披露 71–88 页）
**已确认的官方公开出处**：Morgan Stanley 官网公开 PDF 与本地副本 **MD5 完全一致**（`88ccdada33c4ccf9d7738ce4fe829f4d`，88 页）——即本报告核验的就是官方发布版，不存在二手转载误差。
公开链接：`https://www.morganstanley.com/im/publication/insights/articles/article_capitalallocation.pdf`（需带 referer 才能取到，Akamai 会 403 直连）

---

## 总体结论

**核实一致 5 条 / 有出入 5 条 / 查不到公开来源 0 条**（另有 3 处「部分子项查不到」，已分别标注在各条内）

分类口径：
- **✅ 核实一致** = 数字与权威来源逐字/逐值对得上
- **⚠️ 有出入** = 主体成立，但存在口径、卷期、归因、措辞等需要译注的偏差
- **❓ 查不到公开来源** = 无公开可核查来源（本次无整条落在此档）

**总体判断**：本报告的**可复算数学（附录）与可回归数据（国债、标普回报）质量很高**，全部对得上；但**引注层面存在 3 处硬伤**（Boudoukh 卷号、Gort/Klepper 五阶段归因、Value Imperative 副标题不一致），以及**两处依赖专有数据、无法外部核查**（Morningstar 评级分布、1970 年行业构成）。中文译稿的**注释负担主要集中在这 5 处**。

---

## 1. Morningstar 资本配置评级：覆盖家数与评级分布

### ① 原文表述（正文 p.6，脚注 13）

> "Morningstar, a financial services firm, provides a Capital Allocation Rating for roughly 1,850 public companies in the U.S. based on balance sheet strength, investment acumen, and appropriate distributions to shareholders. Of the companies rated as of September 2025, 16 percent score high enough in each area to be deemed exemplary, 78 percent are standard, and 5 percent rate low enough to be considered poor."

### ② 核验来源

| 来源 | URL | 核到的事实 |
|---|---|---|
| Hodge, Fleck, Utterback, Lane, Correonero, Baker, *The Morningstar Capital Allocation Rating*, Morningstar Equity Research, 2020-10-22（已下载全文 PDF） | `https://advhypo.morningstar.com/Enterprise/VTC/TheMorningstarCapitalAllocationRating_Oct2020.pdf` | 三支柱框架、评级命名、发布时点全部对得上 |
| Morningstar 官方访谈（Mark LaMonica × Matthew Hodge） | `https://www.morningstar.com/stocks/introducing-morningstar-capital-allocation-rating` | 确认三评级名称 Poor/Standard/Exemplary；确认"从 Stewardship 改名" |
| Morningstar 官方术语页 | `https://www.morningstar.com/investing-terms/capital-allocation-rating` | 确认评级为前瞻性、以股东视角、Standard 最常见；确认 2020-12-09 为方法论切换日 |
| Morningstar 企业版评级定义 PDF | `https://advisor.morningstar.com/Enterprise/VTC/UpdatedEquityResearchDefinitions.pdf` | 同上，独立第三方佐证 |

已核到（✅ 全部一致）：
- 三支柱：balance sheet health / investment efficacy / shareholder distributions — 原文与 Morningstar 原文逐字对应
- 三评级：Poor / Standard / Exemplary
- 时点：2020-10-22 方法论发布、**2020-12-09 正式生效**（原 Stewardship Rating 改名）
- 脚注 13 的作者名单与标题、日期 **逐字准确**

### ③ 结论：⚠️ 有出入

- **方法论、评级名称、发布时点：✅ 核实一致。**
- **"roughly 1,850 public companies" 与"截至 2025 年 9 月 16%/78%/5%"：❓ 查不到公开来源。** Morningstar 从不公开披露其 Capital Allocation Rating 的覆盖家数或评级分布；上述数字是 Counterpoint Global 自行统计 Morningstar 数据（很可能经 Morningstar Direct）得出的，**外部无法独立复核**。
- 附带观察：16 + 78 + 5 = 99%，缺 1 个百分点，疑为四舍五入；且 Morningstar 官方明确"Standard 最常见"，与 78% 的主导地位方向一致。

### ④ 建议译注

> 译注（覆盖范围与分布）："覆盖约 1,850 家美国上市公司"及"2025 年 9 月评级分布（16% 典范 / 78% 标准 / 5% 差）"系摩根士丹利基于 Morningstar 数据自行统计，Morningstar 未公开发布覆盖家数或评级分布，此处无法独立核验。
> 另注：Morningstar 该评级原名 Stewardship Rating，自 2020 年 12 月 9 日起改称 Capital Allocation Rating，方法论文 2020 年 10 月 22 日发布（见报告脚注 13）。

---

## 2. Walmart 案例：15 年年化 33%、三倍于标普 500

### ① 原文表述（正文 p.7，**本段无脚注**）

> "A classic example is Walmart, a global retailer, which grew faster than its ROIC in its first 15 years as a public company. The important point is that the company created a lot of value because its ROICs were well above its cost of capital. Even though Walmart required external capital to support its growth, the stock delivered an annual total shareholder return of 33 percent during that period, three times that of the S&P 500."

### ② 核验来源与复算

**（a）"最初 15 年"的真实区间 —— 这里有一个必须纠正的误读**

Walmart 的公开时间线：
- Walmart FY2026 10-K："We completed our initial public offering in **1970**"（`https://stock.walmart.com/sec-filings/all-sec-filings/content/0000104169-26-000055/wmt-20260131.htm`）
- 券商媒体口径：NYSE 挂牌日 **1972-10-01**，发行价 $16.50（Yahoo Finance / Business Insider 报道）
- Yahoo Finance 行情接口 `query2.finance.yahoo.com/v8/finance/chart/WMT` 首根月线：**1972-08**（firstTradeDate = 83597400 → 1972-08-01）

故"上市后最初 15 年"= **1970 或 1972 起算 → 1985 或 1987**。**不是 1992–2006**。

**（b）WMT 年化总回报 vs 标普 500 年化总回报**

数据源：WMT 复权收盘价（Yahoo Finance chart API，含分红再投资与拆股还原）；S&P 500 含息总回报（Aswath Damodaran, NYU Stern，`https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html` / `histretSP.xls`）

| 区间 | WMT 年化 | 标普 500 年化（含息） | 倍数 |
|---|---|---|---|
| 1972-08 → 1987-08（首根行情起算 + 15 年） | **34.97%** | 10.69%（1972–86） | **3.27×** |
| 1972-10 → 1987-10（NYSE 挂牌 + 15 年） | **31.50%** | 10.69% | 2.95× |
| 1972-12 → 1987-12（自然年末 + 15 年） | **30.40%** | 10.69% | 2.84× |
| 1973-01 → 1987-12 | **31.73%** | 10.13%（1973–86） | 3.13× |

标普 500 含息总回报 1973–1987 十五年 CAGR = **9.84%**（Damodaran 原始年表自算）。

→ **33% 与"三倍"落在合理区间内（30.4%–35.0%，2.8×–3.3×），✅ 核实一致。**

**（c）任务指定的 "1992–2006" 区间实测（供译稿纠错用）**

| 区间 | WMT 年化 | 标普 500 年化（含息） | 结果 |
|---|---|---|---|
| 1992-01 → 2006-12（15 年） | **9.34%** | **10.53%** | WMT **跑输**标普 500 |
| 1991-12 → 2006-12（15 年） | 8.69% | — | 跑输 |

→ 若中文译稿把该案例写成"1992–2006 年 Walmart 年化 33%、三倍于标普"，**结论方向完全相反，必须更正**。

**（d）Walmart ROIC 量级（任务指定核查项）**

任务提到"Walmart FY2001 10-K 的 ROIC 量级"——需说明：**该报告正文并未引用 Walmart FY2001 10-K，也未给出任何 Walmart 的 ROIC 数字**，Walmart 段落无脚注。我用 Walmart FY2003 10-K 内含的 11 年财务摘要（含 FY2001）独立测算作为佐证：

数据源：Walmart FY2003 10-K 附件 ex13，`https://stock.walmart.com/sec-filings/all-sec-filings/content/0000104169-03-000005/ex13final.htm`
FY2001（截至 2001-01-31）原始数：净销售 191,329；其他收入净额 1,787；销售成本 150,255；OSG&A 31,550；债务利息 1,104；资本租赁利息 279；利息收入 (188)；所得税 3,692；净利 6,295；总资产 78,130；股东权益 31,343；长期负债 12,501；资本租赁长期义务 3,154；公司自报 ROA 8.7%、ROE 22.0%

我的复算：
- 营业利润 = 191,329 + 1,787 − 150,255 − 31,550 = **11,311**
- 税前利润 = 11,311 − 1,104 − 279 + 188 = 10,116 → 有效税率 36.5%
- NOPAT ≈ 11,311 × (1 − 0.365) = **7,183**
- 投入资本 ≈ 权益 31,343 + 长期负债 12,501 + 资本租赁 3,154 − 现金约 1,900 = **45,098**
- **ROIC ≈ 15.9%**，对比当年 WACC（10 年期美债约 5.0% + 股权风险溢价）约 8–9%

→ "ROIC 远高于资本成本"这一**定性论断成立**，量级为高双位数。

### ③ 结论：✅ 核实一致（33% 与"三倍"）；⚠️ 但存在两处必须写进译注的口径问题

1. 数字本身：✅ 与独立数据源在合理区间内吻合。
2. **区间歧义**：报告只说"最初 15 年"，未给年份。Walmart 1970 年 OTC 上市 / 1972 年 NYSE 挂牌，两种起算都指向 33% 附近。译稿**必须明确写出起止年份**（建议"1972–1987"），否则读者无从核对。
3. **任务提示的 "1992–2006" 与原文不符，且该区间结论相反**（WMT 跑输标普）。若译稿已按 1992–2006 写，**必须改回**。
4. 本段在原报告中**无任何脚注支撑**，属"作者自述"型数据。

### ④ 建议译注

> 译注（Walmart 案例）："上市后最初 15 年"指 1972 年（Walmart 1970 年场外发行、1972 年 8–10 月登陆 NYSE）至 1987 年。按 Yahoo Finance 复权价测算，该期间 WMT 年化总回报约 30%–35%（区间随起止月份而异），同期标普 500 含息总回报年化约 10%–11%（Damodaran, NYU Stern），倍数约 2.8–3.3 倍，与原文"33%、三倍"相符。另：Walmart FY2001 口径 ROIC 约 16%（据 FY2003 10-K 11 年财务摘要自算），当年 WACC 约 8%–9%，支持原文"ROIC 远高于资本成本"的定性判断。原文此段未给出脚注来源。

---

## 3. S&P 500 行业构成：1970 vs 2024

### ① 原文表述（正文 p.9）

> "Exhibit 10 shows the shift in sector composition of the S&P 500... Information technology, healthcare, and communication services doubled as a share of the market over this period, from 26 percent in 1970 to 52 percent in 2024. At the same time, industrials, energy, and materials declined by more than half, from 30 to 13 percent of the index (see exhibit 11)."

### ② 核验来源与图像读取

| 来源 | URL | 结论 |
|---|---|---|
| 报告 Exhibit 10（图） | 本地 `ex10_sector-composition-of-the-s-p-500-1970-2024.jpg`（源：S&P DJI; Compustat; FactSet; **Counterpoint Global estimates**） | 1970：IT ≈12.5%、医疗保健 ≈7%、通信服务 ≈6% → **合计 ≈25.5%≈26%** ✓；2024：IT ≈32%、医疗保健 ≈10%、通信服务 ≈9% → **≈51%≈52%** ✓；1970 工业+能源+材料 ≈12.5+10+7.5 = **30%** ✓；2024 ≈8.5+3.5+1.5 = **13.5%≈13%** ✓ |
| 报告 Exhibit 11（图） | 本地 `ex11_shift-toward-intangible-heavy-sectors-in-the-s-p-500.jpg` | 两条曲线端点直读：虚线（工业+能源+材料）1970 ≈30% → 2024 ≈13%；实线（IT+医疗+通信）1970 ≈26% → 2024 ≈52%。**与正文逐字一致** |
| S&P DJI 官方 GICS 教育文档（截至 2025-12） | `https://www.spglobal.com/spdji/en/documents/education/education-an-overview-of-gics-and-sp-500-sector-industry-indices.pdf` | IT **32.6%**、医疗保健 **9.3%**、通信服务 **9.8%** → 合计 **51.7%**，与报告 2024 年的 **52%** 高度吻合（独立交叉验证 ✓） |
| Wikipedia GICS 权重（2026-08-12） | `https://en.wikipedia.org/wiki/S%26P_500` | IT 37.4% + 通信 9.67% + 医疗 9.09% = 56.2%（2024→2026 继续上行的合理轨迹）；工业 8.68% + 能源 3.27% + 材料 1.82% = **13.8%**（与 13% 接近） |

### ③ 结论：⚠️ 有出入

- **图表与正文内部完全自洽**（Exhibit 10 / 11 与正文的 26%、52%、30%、13% 逐项对得上，误差在读图精度内）——✅
- **2024 年的 52% 与 13% 得到 S&P DJI 官方 GICS 权重的独立交叉验证**（51.7%、13.8%）——✅
- **1970 年的 26% 与 30% 无法外部核查**：GICS 分类体系 1999 年才建立，S&P DJI 从未公开发布过 1970 年的行业权重。这两个数字是 Counterpoint Global 自行回溯估算的（图表 Source 行已注明 "Counterpoint Global estimates"）。

### ④ 建议译注

> 译注（1970 年行业构成）：2024 年的 52% / 13% 可用 S&P Dow Jones Indices 官方 GICS 权重交叉验证（2025 年 12 月口径分别为 51.7% 与 13.8%）；但 1970 年的 26% / 30% 系摩根士丹利依据历史成分股自行回溯估算——GICS 体系 1999 年才建立，S&P DJI 未发布过 1970 年行业权重，故此二数无法独立核验。另注：报告 Exhibit 10 注明"房地产板块自 2016 年起自金融板块分拆"，跨 1970–2024 的比较含此口径断点。

---

## 4. 美国 10 年期国债收益率：1970 年代 7.5%、过去 10 年 2.5%

### ① 原文表述（正文 p.9）

> "For example, the yield on the 10-year U.S. Treasury note had an annual average of 7.5 percent in the 1970s compared to an average of 2.5 percent over the past 10 years."

### ② 核验来源与复算

数据源：FRED `DGS10`（Board of Governors of the Federal Reserve System, H.15）日度序列，`https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10`（1962-08-01 起，样本 15,838 个交易日）；月频 `GS10` 交叉验证。

| 口径 | 1970 年代（1970–1979） | 最近 10 年 |
|---|---|---|
| 日频全样本均值（pooled） | **7.4983%** | 2015–2024：**2.4796%**（2,501 个交易日） |
| 各年年度均值再取平均 | **7.4997%** | 2015–2024：**2.4816%**（月频 GS10） |
| 各年年度均值明细 | 1970: 7.354 / 1971: 6.161 / 1972: 6.206 / 1973: 6.848 / 1974: 7.562 / 1975: 7.994 / 1976: 7.613 / 1977: 7.418 / 1978: 8.408 / 1979: 9.433 | 2016–2025：2.6946%；2015-11-05→2025-11-04：2.6662% |

### ③ 结论：✅ 核实一致

- **7.5%**：两种口径分别得 7.4983% 与 7.4997%，**与原文 7.5% 精确吻合**（原文未说明是日频还是月频，两者结果几乎相同，不构成问题）。
- **2.5%**：以 **2015–2024** 为"过去 10 年"窗口得 2.4796%（日频）/ 2.4816%（月频）→ **与原文 2.5% 吻合**。
- **⚠️ 但窗口依赖需注意**：若以报告发布日（2025-11）滚动 10 年计算，则为 2.67%（日频），四舍五入应为 2.7% 而非 2.5%。原文的 2.5% 对应的是与全文图表一致的 1970–2024 数据截止窗口。

### ④ 建议译注

> 译注（国债收益率）：FRED DGS10 日度序列，1970–1979 全期均值 7.4983%（各年年度均值再平均为 7.4997%），与原文 7.5% 一致。"过去 10 年"取 2015–2024 窗口为 2.48%（月频 GS10 为 2.48%），与原文 2.5% 一致；若按报告发布日 2025 年 11 月滚动计算，则为 2.67%。

---

## 5. Lovallo 等人的内部资本配置研究：5,760 个观测、38 个超阈值

### ① 原文表述（正文 p.5，脚注 5）

> "The researchers in fact found an optimal degree of reallocation. But they also discovered that only 38 of the 5,760 observations, or less than 1 percent, were above that threshold. In other words, the vast majority of companies could improve their financial performance by increasing their reallocation."

### ② 核验来源

| 来源 | URL | 核到的事实 |
|---|---|---|
| Lovallo, Brown, Teece, Bardolet, *Resource Re-Allocation Capabilities in Internal Capital Markets: The Value of Overcoming Inertia*, Strategic Management Journal, Vol. 41, No. 8, August 2020, 1365–1380 | RePEc: `https://ideas.repec.org/a/bla/stratm/v41y2020i8p1365-1380.html`；DOI `10.1002/smj.3157` | 期刊、卷、期、年月、页码**全部逐字准确** ✓ |
| 论文摘要（经 RePEc / BRG / Wiley 三方一致） | `https://www.thinkbrg.com/insights/publications/teece-resource-reallocation` | "a consistent **inverted U‑shape**... **nearly all the data lie on the upward sloping part of the curve**"——与原文"绝大多数公司加大再配置可改善业绩"一致 ✓ |
| 论文正文（悉尼大学机构库公开稿，经搜索引擎抓取到的原句） | `https://ses.library.usyd.edu.au/bitstream/handle/2123/28491/Lovallo et al - 2020 - Resource re-allocation capabilities...pdf` | **原句**："Only 27 (0.47%) and **38 (0.67%)** observations are to the right of the peak of the respective graphs point. That is, they are at a level where more reallocation is..." ✓ |

### ③ 结论：✅ 核实一致

- **"38" 完全对上**：论文原句明确给出 "38 (0.67%)"，MS 报告取用的正是这组数字（另一条曲线为 27 / 0.47%）。
- **"5,760" 反推验证**：38 ÷ 5,760 = **0.6597% ≈ 0.67%**，与论文自报的 0.67% 在舍入误差内完全吻合 → **分母 5,760 得到独立闭环验证**。
- **"less than 1 percent"** ✓（0.66% < 1%）。
- 期刊卷期页码、DOI、作者顺序全部准确。

**附带一处内部张力（值得译注）**：报告 Exhibit 1 的图内标注为 "Too Little Reallocation (98-99% of companies)" / "Too Much Reallocation (1-2% of companies)"，而正文说超阈值者"不到 1%"。两者口径不同（图内为 Counterpoint 对论文图的再标注，正文为论文"越过峰值"的观测占比），但读者容易困惑。

### ④ 建议译注

> 译注（Lovallo 等）：原文数字可回溯至论文正文——"Only 27 (0.47%) and 38 (0.67%) observations are to the right of the peak"；38 ÷ 5,760 = 0.66%，与论文自报 0.67% 吻合。期刊出处：Strategic Management Journal, 2020, 41(8): 1365–1380，DOI 10.1002/smj.3157。另注：报告 Exhibit 1 图内标注"过度再配置公司占 1%–2%"与正文"不到 1%"口径不同（图内为摩根士丹利对论文图的二次标注，正文为论文越过峰值观测占比），阅读时勿混。

---

## 6. "四条原则"的出处：McTaggart / Kontes / Mankins, *The Value Imperative*

### ① 原文表述（正文 p.53，脚注 181 / 183）

> "Five Principles of Capital Allocation. James McTaggart, Peter Kontes, and Michael Mankins, management consultants, described four principles of resource allocation in their book, The Value Imperative.¹⁸¹ We believe that these principles are useful for thinking about capital allocation. We add a fifth that emphasizes action."

脚注 181：*The Value Imperative: Managing for Superior Shareholder Returns* (New York: Free Press, 1994), 239-252。
脚注 183：*The Value Imperative*, 243。
脚注 104：*The Value Imperative: Managing Superior Shareholder Returns* (New York: Free Press, 1994), 241。

### ② 核验来源

| 来源 | URL | 核到的事实 |
|---|---|---|
| Open Library 书目记录 | `https://openlibrary.org/search.json?q=The+Value+Imperative+McTaggart` | 书名 *The value imperative*；**首版年 1994**；**出版社 Free Press**（另 Maxwell Macmillan Canada / Maxwell Macmillan International）；ISBN 0029206707 / 9780029206706；edition `OL1437579M` ✓ |
| WorldCat | `https://search.worldcat.org/oclc/1151671707` | 作者 James M. McTaggart、Peter W. Kontes、Michael C. Mankins ✓ |
| Internet Archive 扫描件元数据 | `https://archive.org/details/valueimperativem00mcta_0` | "Publication date: 1994" ✓（扫描件仅供馆内借阅，未开放下载） |
| AbeBooks / Amazon 版权与出版社信息 | `https://www.abebooks.com/9780029206706/Value-Imperative-Managing-Superior-Shareholder-0029206707/plp` | "Published by The Free Press, 1994"；ISBN 一致 ✓ |
| Amazon 作者页（Mankins 简介） | `https://www.amazon.com/Value-Imperative-Managing-Superior-Shareholder/dp/0029206707` | Mankins 简介中亦作 "The Value Imperative: Managing for Superior Shareholder Returns (Free Press, 1994)" ✓ |
| 出版社/内容简介（AbeBooks 书背） | 同上 | 该书核心命题："cash flows drive value"、单一治理目标、价值型管理框架，涵盖 strategic planning / **resource allocation** / performance management / 薪酬四大能力 |

### ③ 结论：⚠️ 有出入

**✅ 已核实一致的部分**
- 书真实存在，标题 *The Value Imperative*；作者三人 ✓
- **出版年 1994、出版社 The Free Press（纽约）、ISBN 0029206707** — 脚注 104 与 181 的书目信息与 Open Library / WorldCat / Internet Archive / AbeBooks **四源一致** ✓
- 章节覆盖 resource allocation ✓

**⚠️ 需要处理的三处**
1. **报告自身脚注不一致**：脚注 181 作 "Managing **for** Superior Shareholder Returns"（正确），脚注 104 作 "Managing Superior Shareholder Returns"（**漏 "for"**）。同一部书在同一份文件里副标题写法不一。译稿应统一采用 **Managing for Superior Shareholder Returns**。
2. **"确有四原则"这一具体措辞无法公开核验**：书为 1994 年在版/版权在版，全文不开放（Internet Archive 扫描件需登录借阅；Google Books API 配额耗尽）。公开可查的只有书背简介（四大管理能力、价值型管理框架），**没有公开来源能证明 pp.239–252 处确实以"four principles of resource allocation"的形式列出这四条**。
3. **存在 2008 年 HBR Press 再版**（*The Value Imperative: Managing for Superior Shareholder Returns*, Harvard Business Review Press, 2008），读者手上的版本可能与此不同；另有同作者姊妹作 *Value: The Four Cornerstones of Corporate Finance*（"four cornerstones"措辞出自此书，**不是** *The Value Imperative*）——中文译稿切勿把 "four principles" 与 "four cornerstones" 混用。

### ④ 建议译注

> 译注（《The Value Imperative》）：书名全称 *The Value Imperative: Managing for Superior Shareholder Returns*，James M. McTaggart、Peter W. Kontes、Michael C. Mankins 著，The Free Press（纽约）1994 年出版，ISBN 0029206707。原文脚注 104 副标题漏印 "for"，此处统一订正。需注意该书 2008 年由 Harvard Business Review Press 再版；同作者另有姊妹作 *Value: The Four Cornerstones of Corporate Finance*（"四大基石"一语出自该书），与本文所引"资源配置四原则"不是同一概念。此外，1994 年版全文不公开流通，原文脚注所标页码（239–252、243）无法由公众来源逐字复核。

---

## 7. 巴菲特引文：institutional imperative 与 "Any business craving of the leader"

### ① 原文表述（正文 p.2、p.5、p.53）

> p.2（脚注 4，标注 1987 年信）："Once they become CEOs, they face new responsibilities. They now must make capital allocation decisions, a critical job that they may have never tackled and that is not easily mastered."
> p.5："Finally, there is what Warren Buffett calls the 'institutional imperative.'¹¹ This says executives will 'mindlessly' imitate one another in their practices, including compensation and capital allocation..."
> p.53（脚注 186，标注 1989 年信）："As Buffett says, 'Any business craving of the leader, however foolish, will be quickly supported by detailed rate-of-return and strategic studies prepared by his troops.'"
> p.48（脚注 154，标注 1987 年信）："After ten years on the job, a CEO whose company annually retains earnings equal to 10% of net worth will have been responsible for the deployment of more than 60% of all the capital at work in the business."
> p.51（脚注 176，标注 1996 年信）："a good plan 'should be (1) tailored to the economics of the specific operating business; (2) simple in character so that the degree to which they are being realized can be easily measured; and (3) directly related to the daily activities of plan participants.'"

### ② 核验来源（逐字比对伯克希尔官方原文页）

| 原文引用 | 官方出处 | 核验结果 |
|---|---|---|
| "Any business craving of the leader, however foolish, will be quickly supported by detailed rate-of-return and strategic studies prepared by his troops" | `https://www.berkshirehathaway.com/letters/1989.html` | ✅ **逐字命中**。原文为四条清单第 (3) 条："(3) Any business craving of the leader, however foolish, will be quickly supported by detailed rate-of-return and strategic studies prepared by his troops;" |
| "institutional imperative" | 同上（1989） | ✅ 逐字命中："My most surprising discovery: the overwhelming importance in business of an unseen force that we might call 'the institutional imperative.'" 同页接："(4) The behavior of peer companies, whether they are expanding, acquiring, setting executive compensation or whatever, will be mindlessly imitated."——**报告"mindlessly imitate one another"的表述与 1989 年原文一致**（1990 年信则作 "the tendency of executives to mindlessly imitate the behavior of their peers, no matter how foolish it may be to do so"，见 `https://www.allbusiness.com/how-to-avoid-the-institutional-imperative-14597416-1.html`） |
| "Once they become CEOs, they face new responsibilities..." | `https://www.berkshirehathaway.com/letters/1987.html` | ✅ 逐字命中（"This point can be important because the heads of many companies are not skilled in capital allocation... Once they become CEOs, they face new responsibilities. They now must make capital allocation decisions, a critical job that they may have never tackled and that is not easily mastered."） |
| "After ten years on the job, a CEO whose company annually retains earnings equal to 10% of net worth..." | 同上（1987） | ✅ 逐字命中（"The lack of skill that many CEOs have at capital allocation is no small matter: After ten years on the job, a CEO whose company annually retains earnings equal to 10% of net worth will have been responsible for the deployment of more than 60% of all the capital at work in the business."） |
| "(1) tailored to the economics of the specific operating business; (2) simple in character... (3) directly related to the daily activities of plan participants" | `https://www.berkshirehathaway.com/letters/1996.html` | ✅ 逐字命中（GEICO 薪酬段："Goals should be (1) tailored to the economics of the specific operating business; (2) simple in character so that the degree to which they are being realized can be easily measured; and (3) directly related to the daily activities of plan participants."） |

**年份归属全部正确**：脚注 4 → 1987 ✓；脚注 11 → 1989 ✓；脚注 154 → 1987 ✓；脚注 176 → 1996 ✓；脚注 186 → 1989 ✓。

### ③ 结论：✅ 核实一致

五处巴菲特引文**全部逐字命中官方原文页**，且报告标注的致股东信年份全部正确。唯一的技术性瑕疵：PDF 排版把 "rate-of-return" 断行成 "rate-of- return"，属提取假象，原文无此问题。

### ④ 建议译注

> 译注（巴菲特引文）：均据伯克希尔官方致股东信原文页逐字核对——"Any business craving of the leader..." 出自 1989 年信"制度性冲动"四条表现之第 (3) 条；"institutional imperative"（"制度性冲动"）一词亦首见 1989 年信；"Once they become CEOs..." 与 "After ten years on the job..." 出自 1987 年信；GEICO 激励三原则出自 1996 年信。可引用链接：
> 1989 年信 https://www.berkshirehathaway.com/letters/1989.html
> 1987 年信 https://www.berkshirehathaway.com/letters/1987.html
> 1996 年信 https://www.berkshirehathaway.com/letters/1996.html
> 历年信索引 https://www.berkshirehathaway.com/letters/letters.html

---

## 8. 生命周期五阶段框架：Klepper & Gort + Dickinson

### ① 原文表述（正文 p.5，脚注 14）

> "Our analysis is based on work by Victoria Dickinson, a professor of accounting at the University of Mississippi. Dickinson starts with research by Steven Klepper and Michael Gort, professors of economics, who developed an empirically-grounded life cycle framework based on five stages: introduction, growth, maturity, shake-out, and decline. She then added rigor to the classification by linking the stages to results within the statement of cash flows."

脚注 14：（a）Mauboussin & Callahan, *Trading Stages in the Company Life Cycle*, Consilient Observer, 2023-09-26；（b）Victoria Dickinson, "Cash Flow Patterns as a Proxy for Firm Life Cycle," *Accounting Review*, Vol. 86, No. 6, November 2011, 1969-1994；（c）Michael Gort and Steven Klepper, "Time Paths in the Diffusion of Product Innovations," *The Economic Journal*, Vol. 92, No. 367, September 1982, 630-653.

### ② 核验来源

| 来源 | URL | 核到的事实 |
|---|---|---|
| RePEc（*Economic Journal*） | `https://ideas.repec.org/a/ecj/econjl/v92y1982i367p630-53.html` | Gort, Michael & Klepper, Steven（1982），vol. 92(367), 630-653, September ✓ 脚注 14(c) **逐字准确** |
| Google Scholar（Dickinson） | `https://scholar.google.com/citations?user=L94_P8YAAAAJ` | "Cash flow patterns as a proxy for firm life cycle, **The accounting review 86 (6), 1969-1994, 2011**" ✓ 脚注 14(b) **逐字准确** |
| Ole Miss 官方教师页 | `https://olemiss.edu/profiles/vdickins` | Victoria Dickinson，**Lucian Minor Chair of Accountancy, Associate Professor**，Patterson School of Accountancy, University of Mississippi；PhD Business, University of Wisconsin-Madison (2006) ✓ 报告"密西西比大学会计学教授"表述**准确** |
| 同作者姊妹篇 MS *Trading Stages in the Company Life Cycle*（2023-09-26，脚注 14(a)） | `https://www.morganstanley.com/im/publication/insights/articles/article_tradingstagesinthecompanylifecycle.pdf` | 原文："The economists Michael Gort and Steven Klepper developed a life cycle framework based on five stages. **Victoria Dickinson**... **named the stages** introduction, growth, maturity, shake-out, and decline." |
| 同作者 MS *The Neglected Value Driver* | `https://www.morganstanley.com/content/dam/im/assets/publication/thought-leadership/consilient-observer/article_theneglectedvaluedriver_ltr.pdf` | 原文："Grounded in substantial empirical work, Gort and Klepper identified five stages of the life cycle that have become known as: introduction, growth, maturity, shake-out, and decline." |
| 学术二手文献对 Gort & Klepper (1982) 五阶段的表述 | `https://www.econstor.eu/bitstream/10419/338577/1/11187_2026_Article_1139.pdf` | 表述为 "**emergence, growth, shakeout, decline, and stabilization**"——**与本报告的五个名称不同** |
| Klepper (1996), *American Economic Review* 86(3): 562-583 | `https://econpapers.repec.org/RePEc:aea:aecrev:v:86:y:1996:i:3:p:562-83`；全文 `http://www.iot.ntnu.no/innovation/norsi-pims-courses/laursenfoss/Klepper%20(1996).pdf` | 生命周期研究的标准文献；通行五阶段命名法（introduction / growth / maturity / shakeout / decline）由此篇推广 |
| 学界对 Dickinson 五阶段的引用 | `http://www.aeca1.org/xvencuentroaeca/cd/34b.pdf` | "Dickinson (2011) establishes five stages of life. The first stage is called introduction... growth... maturity... shake-out... decline." ✓ |

### ③ 结论：⚠️ 有出入

**✅ 核实一致的部分**
- 脚注 14 的三条文献（期刊、卷、期、年月、页码、作者顺序）**全部逐字准确** ✓
- Dickinson 的任职单位与职称 ✓
- 报告与 MS 自家 2023 年姊妹篇的表述框架一致（Gort/Klepper 提供五阶段框架，Dickinson 命名阶段并用现金流量表加以严格化）✓

**⚠️ 需要译注的归因问题**
- **"introduction, growth, maturity, shake-out, decline" 这五个具体名称，通行文献主要溯源到 Klepper (1996, AER) 与 Dickinson (2011)**；而 **Gort & Klepper (1982) 原文**的阶段命名在二手文献中通常记作 **"emergence, growth, shakeout, decline, stabilization"**（如 Econstor 2026 年那篇）。也就是说：**1982 年那篇是经验基础，但"这五个词"的命名归给 1982 年并不严谨**。
- 这也解释了报告为何在 2023 年姊妹篇里说"Victoria Dickinson **named the stages**"（ Dickinson 命名），而在本文里压缩成"Klepper and Gort ... based on five stages: introduction, growth, ..."——**同一作者群两篇表述侧重不同**。
- 附带：GICS 的 11 个板块与生命周期五阶段是两回事，译稿勿混。

### ④ 建议译注

> 译注（生命周期五阶段）：经验基础出自 Gort, M. & Klepper, S. (1982), "Time Paths in the Diffusion of Product Innovations," *The Economic Journal*, 92(367): 630–653；而"introduction / growth / maturity / shake-out / decline"这一通行命名法主要由 Klepper (1996, *AER* 86(3): 562–583) 与 Dickinson (2011, *The Accounting Review* 86(6): 1969–1994) 确立（Gort & Klepper 1982 原文的阶段表述在二手文献中常记作 emergence / growth / shakeout / decline / stabilization）。Dickinson 现任教于密西西比大学 Patterson School of Accountancy（ Lucian Minor Chair of Accountancy）。

---

## 9. 附录数学：股息 vs 回购等价性（**独立复算**）

### ① 原文表述（正文 p.56–57，附录）

> 现金流 6 年：$100.0 / $109.0 / $118.8 / $129.5 / $141.2 / $772.7；股权成本 7%；100 股。
> 现值合计 $1,000，每股 $10；终值 $1,500.7 = $1,000 × (1 + .07)⁶；因再投资于股权成本，**IRR = 7%**。
> 股息表："We end up with **$1,371.2 from the dividends and $129.5 from the reinvested proceeds** for a total of $1,500.7."
> 回购表："The sum of the aggregate value of the share buyback is **$1,371.2 (100 shares at an average cost of $13.71)** and the proceeds from reinvestment are **$129.5**. That gets us to $1,500.7."

### ② 复算代码与输出（Python 3，独立于原文，非复制原文数字）

```python
r = 0.07
cfs = [100.0, 109.0, 118.8, 129.5, 141.2, 772.7]

# (A) 现值
pv = [c/(1+r)**(i+1) for i, c in enumerate(cfs)]
print("PV:", [round(x,2) for x in pv], "sum =", round(sum(pv),4))
print("per share =", round(sum(pv)/100, 4))

# (B) 终值
print("1000*1.07^6 =", round(1000*1.07**6, 4))

# (C) 股息路径：R_t = R_{t-1}*1.07 + CF_{t-1}*0.07 ; Total_t = Total_{t-1} + CF_t + R_t
R = 0.0; tot = 0.0; cols = []
for i, c in enumerate(cfs):
    if i > 0: R = R*1.07 + cfs[i-1]*0.07
    tot = tot + c + R
    cols.append((i+1, c, R, tot))
for row in cols: print("  yr%d pay %.1f  reinv %.2f  total %.2f" % row)
print("sum dividends =", round(sum(cfs),1), " sum reinvest col =", round(sum(x[2] for x in cols),2),
      " total =", round(sum(cfs)+sum(x[2] for x in cols),2))

# (D) 真实终值：sum CF_t * 1.07^(6-t)
print("terminal wealth =", round(sum(c*(1+r)**(6-(i+1)) for i,c in enumerate(cfs)),4))

# (E) IRR
f = [-1000.0] + cfs
npv = lambda x: sum(v/(1+x)**i for i,v in enumerate(f))
lo, hi = 0.0, 1.0
for _ in range(300):
    mid = (lo+hi)/2
    if npv(mid) > 0: lo = mid
    else: hi = mid
print("IRR =", round((lo+hi)/2*100, 4), "%")

# (F) 回购路径
shares, vps = 100.0, 10.70
for i, c in enumerate(cfs):
    if i > 0: vps *= 1.07
    n = c/vps
    shares -= n
    print("  yr%d $%.1f  vps $%.3f  bought %.3f  after %.3f" % (i+1, c, vps, n, shares))
print("shares bought total =", round(9.346+9.520+9.698+9.879+10.067+51.488,3))
print("avg cost = 1371.2/100 =", round(1371.2/100, 4))
```

**输出：**

```
PV: [93.46, 95.20, 96.98, 98.79, 100.67, 514.88]  sum = 999.9902
per share = 9.9999
1000*1.07^6 = 1500.7304
  yr1 pay 100.0  reinv 0.00   total 100.00
  yr2 pay 109.0  reinv 7.00   total 216.00
  yr3 pay 118.8  reinv 15.12  total 349.92
  yr4 pay 129.5  reinv 24.49  total 503.91
  yr5 pay 141.2  reinv 35.27  total 680.39
  yr6 pay 772.7  reinv 47.63  total 1500.72
sum dividends = 1371.2   sum reinvest col = 129.51   total = 1500.71
terminal wealth = 1500.7156
IRR = 6.9998 %
  yr1 $100.0  vps $10.700  bought 9.346  after 90.654
  yr2 $109.0  vps $11.449  bought 9.520  after 81.134
  yr3 $118.8  vps $12.250  bought 9.698  after 71.436
  yr4 $129.5  vps $13.108  bought 9.879  after 61.557
  yr5 $141.2  vps $14.026  bought 10.067 after 51.489
  yr6 $772.7  vps $15.007  bought 51.488 after 0.001
shares bought total = 99.998
avg cost = 1371.2/100 = 13.712
```

### ③ 逐项结论

| 原文数字 | 复算 | 判定 |
|---|---|---|
| 现值合计 $1,000 | 999.9902 | ✅ |
| 每股 $10 | 9.9999 | ✅ |
| 终值 $1,500.7 = 1000×1.07⁶ | 1500.7304 | ✅ |
| 股息表 6 行（payment / reinvestment / total） | 逐格命中：0.00 / 7.00 / 15.12 / 24.49 / 35.27 / 47.63；100 / 216.00 / 349.92 / 503.91 / 680.39 / 1500.72 | ✅ **全部复现** |
| 回购表 6 行（金额 / 起始股数 / 每股价值 / 回购股数 / 剩余股数 / 再投资 / 合计） | 9.3 / 9.5 / 9.7 / 9.9 / 10.1 / 51.5；$10.70 / 11.45 / 12.25 / 13.11 / 14.03 / 15.01；100→90.7→81.1→71.4→61.6→51.5→0 | ✅ **全部复现** |
| 9% 增长（100→109→118.8→129.5→141.2） | 100×1.09^k 逐项吻合 | ✅ |
| IRR = 7% | 6.9998% | ✅ |
| **股息贡献 $1,371.2** | 100+109+118.8+129.5+141.2+772.7 = **1371.2** ✓ | ✅ |
| **再投资贡献 $129.5** | 1,500.7156 − 1,371.2 = **129.5156** ≈ 129.5 ✓；且恰好等于股息表 Reinvestment 列之和（0+7.00+15.12+24.49+35.27+47.63 = 129.51）✓ **双重闭环** | ✅ |
| 1,371.2 + 129.5 = 1,500.7 | 1,371.2 + 129.51 = 1,500.71 | ✅ |
| **100 股 @ 平均成本 $13.71** | 1371.2 / 100 = **13.712**，四舍五入为 13.71；**100 × 13.71 = 1,371.0 ≠ 1,371.2** | ⚠️ **舍入微差（$0.2）** |
| 第 6 年 $772.7 = $15.01 × 51.5 | 15.01 × 51.5 = 773.0（表内舍入值）；精确值 15.007 × 51.489 = **772.695** ✓ | ✅（表内为舍入） |

**关于"$1,371.2 = 100 × 13.712"**：任务提示要核对的两点——
- **$1,371.2 确由 100 股构成** ✓，平均成本精确值 **$13.712**，原文写 $13.71 是四舍五入；
- **"股息贡献 1,371.2、再投资贡献 129.5"完全正确** ✓，且 129.5 有两条独立验证路径（终值减名义股息 = 129.5156；股息表 Reinvestment 列求和 = 129.51），**这不是巧合而是恒等式**（可证：Σ_t R_t = Σ_s CF_s·(1.07^(6−s) − 1) = 终值 − 名义股息）。

**另有一处原文未言明、但值得译注的事实**：第 6 年的 $772.7 是**倒推出来的插值**，不是独立生成——(1000 − 前五年现值合计 485.1075) × 1.07⁶ = 772.7148，即"令六年现值恰为 $1,000"的配平数。

### ④ 建议译注

> 译注（附录数学）：本节全部数字已独立复算验证——现金流现值 999.99 ≈ $1,000、每股 $10、终值 1,000 × 1.07⁶ = 1,500.73、IRR = 6.9998% ≈ 7%，股息表与回购表六行数值逐格复现（末年回购 $15.007 × 51.489 股 = $772.70）。其中"股息 $1,371.2 + 再投资 $129.5 = $1,500.7"经两条独立路径互验（终值 1,500.7156 − 名义股息 1,371.2 = 129.5156；股息表再投资列求和亦为 129.51）。两处四舍五入微差：① 回购平均成本精确值为 $1,371.2 ÷ 100 = $13.712，原文列示的 $13.71 系舍入值（100 × 13.71 = 1,371.0）；② 第 6 年 $772.7 系为使六年现值恰等于 $1,000 而倒推的配平数（(1,000 − 前五年现值 485.11) × 1.07⁶ = 772.71），并非独立给定的现金流。

---

## 10. "Total payout yield" 1970–2024：回购从股息的 0.1 倍升至 1.3 倍

### ① 原文表述（正文 p.10，脚注 26）

> "From 1970 to 2024, buybacks went from 0.1 times to 1.3 times dividends. Total payout yield, dividends plus buybacks divided by equity market capitalization, does a better job of explaining shareholder returns than either dividend or buyback yield alone.²⁶"

脚注 26：Jacob Boudoukh, Roni Michaely, Matthew Richardson, and Michael R. Roberts, "On the Importance of Measuring Payout Yield: Implications for Empirical Asset Pricing," *Journal of Finance*, **Vol. 63, No. 2, April 2007, 877-915**。

### ② 核验来源

| 来源 | URL | 核到的事实 |
|---|---|---|
| RePEc（*Journal of Finance*） | `https://ideas.repec.org/a/bla/jfinan/v62y2007i2p877-915.html` | **卷号 62(2)，April 2007, 877-915**，DOI `10.1111/j.1540-6261.2007.01226.x` |
| EconPapers | `https://econpapers.repec.org/RePEc:bla:jfinan:v62:y:2007:i:2:p:877-915` | 同上：**vol. 62, issue 2, 877-915** |
| NBER 工作论文版原文 | `https://www.nber.org/system/files/working_papers/w10651/revisions/w10651.rev0.pdf` | 摘要："the evidence of stock return predictability is **much stronger using total payout yields**... for our sample period, 1926 to 2002, the regression of returns on dividend yields at an annual frequency and horizon generates an R2 of **4.1%** and an insignificant..." |
| 论文摘要（IDEAS / Scilit / ResearchGate 三方一致） | 同上 | "statistically and economically significant predictability is found at both short and long horizons when **total payout yield is used instead of dividend yield**... the high minus low payout yield portfolio is a priced factor." |
| 报告 Exhibit 36 / 40（图，源：Counterpoint Global; Compustat; FactSet; LSEG） | 本地 `ex36_*.jpg` / `ex40_*.jpg` | 2024：股息 ≈$800B、回购 ≈$1,100B → **1.375 ≈ 1.3 倍 ✓**；1970：回购近乎为零、股息数十亿量级 → 0.1 倍量级 ✓（内部自洽） |
| 报告脚注 130（另一处相关引用） | `https://rpc.cfainstitute.org/research/financial-analysts-journal/2017/the-long-run-drivers-of-stock-returns-total-payouts-and-the-real-economy`；`https://ideas.repec.org/a/taf/ufajxx/v73y2017i3p32-52.html` | Straehl & Ibbotson, FAJ **Vol. 73, No. 3, Third Quarter 2017, 32-52** ✓ 脚注 130 卷期页码**准确** |

### ③ 结论：⚠️ 有出入

**✅ 核实一致的部分**
- Boudoukh 等论文**真实存在**，期刊、期、年月、页码（877-915）**准确**，DOI 可查。
- 论文核心结论**支持**原文主张的**前半句**："total payout yield（股息＋回购）比单用股息收益率**显著更好地**解释/预测股东回报"，且"total payout yield 的截面信息超过 dividend yield""高减低 payout yield 组合是定价因子"，"对总支付口径的度量方法稳健"。
- "回购从股息的 0.1 倍升至 1.3 倍"与报告自有 Exhibit 36 / 40 图**内部自洽**（2024：1,100/800 ≈ 1.375；1970：回购近零）。

**⚠️ 两处需处理**
1. **脚注卷号错误**：原文作 "Vol. **63**, No. 2"，实际为 **Vol. 62, No. 2**（RePEc / EconPapers / Scilit 三源一致）。页码 877-915 与 April 2007 正确，仅卷号错。
2. **"or buyback yield alone" 这一比较超出被引文献范围**：Boudoukh 等比较的是 total / net payout yield **vs. dividend yield**，并未单独构造"buyback yield"作对照。原文中"比单看股息收益率**或回购收益率**都更好"的第二个比较，文献不直接支持（MS 自家脚注 130 引的 Straehl & Ibbotson 2017 支持的是"总支付是长周期股票回报的关键驱动"这一更强命题，但同样不是"总支付优于回购收益率"的对照检验）。

### ④ 建议译注

> 译注（总派息收益率）：Boudoukh, Michaely, Richardson & Roberts, "On the Importance of Measuring Payout Yield: Implications for Empirical Asset Pricing," *Journal of Finance*, 2007, 62(2): 877–915（DOI 10.1111/j.1540-6261.2007.01226.x）。**原文脚注 26 卷号误作 63，实为 62**。该文证明"总派息收益率（股息＋回购）较单用股息收益率具有显著更强的回报预测力"，但未单独以"仅回购收益率"作对照，故原文"比单看股息收益率**或回购收益率**都更好"的第二种比较属报告作者的延伸推论。
> 另注：文中"回购相当于股息的 0.1 倍→1.3 倍"取自报告自有 Exhibit 36 / Exhibit 40（源：Counterpoint Global、Compustat、FactSet、LSEG），2024 年约 1,100 / 800 ≈ 1.4 倍；底层数据为专有数据集，无法独立复核。

---

## 附：核验方法与可复现性说明

**数据源清单（均为公开、可引用）**
- FRED DGS10 / GS10（美联储 H.15）— 国债收益率
- Damodaran, *Historical Returns on Stocks, Bonds and Bills*（NYU Stern，2026-01 更新）— 标普 500 含息年回报
- Robert Shiller, *Irrational Exuberance* 数据表（耶鲁）— 标普 500 价格与股息，1970–2007 交叉校验
- Yahoo Finance chart API（WMT、^GSPC 月线复权）— 个股总回报
- SEC EDGAR / Walmart FY2003 10-K ex13 — Walmart FY2001 财务摘要
- Berkshire Hathaway 官方致股东信页（1977–2023）— 巴菲特引文逐字核对
- RePEc / IDEAS / EconPapers / WorldCat / Open Library / Internet Archive — 学术与书目元数据
- S&P DJI《An Overview of GICS and S&P 500 Sector & Industry Indices》— 2024/2025 行业权重交叉验证
- Morningstar《The Morningstar Capital Allocation Rating》（2020-10-22 PDF）+ Morningstar 官方术语页 — 评级方法论

**未能取得的源（诚实声明）**
1. Lovallo 等 2020 年论文**出版版全文 PDF**：Wiley 付费墙 403；悉尼大学机构库被 Cloudflare 拦截（多 UA / referer / 会话 / Wayback / fatcat 均失败）。已通过搜索引擎抓取到的论文原句 "Only 27 (0.47%) and 38 (0.67%)..." 完成关键数字核验，并用 38/5,760 = 0.66% 闭环验证分母。
2. *The Value Imperative*（1994）**全文**：付费/仅可借阅；公开来源只能确认书名、作者、年份、出版社、ISBN 与内容主题，**无法逐字复核 pp.239–252 的"四原则"措辞**。
3. Morningstar 评级覆盖家数与分布、1970 年 S&P 500 行业构成、Exhibit 36/40 底层数据 — **均为专有数据，无公开来源**。

**未做的事**
- 未改动 jobs-research 仓库任何其他文件，未执行 git commit。
- 未修改 `/tmp` 下原始材料。
