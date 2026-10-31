# Carol Loomis《Mr. Buffett on the Stock Market》(FORTUNE, 1999-11-22) 数据核验表

- 核验日期：2026-10-31
- 原文版本：伯克希尔 1999 年报附录重印 PDF <https://www.berkshirehathaway.com/1999ar/FortuneMagazine.pdf>（扫描件，本次已 OCR 全文比对；转载版 <https://fortune.com/article/warren-buffett-on-stock-market>）
- 方法：OCR 原文取数 → 官方数据（FRED/BEA、美国财政部拍卖 API、ERP 统计附录、ICI、Wikipedia/媒体）逐项复算

---

## 1. 道指四个收盘点位

**原文**：`Dec. 31, 1964: 874.12 / Dec. 31, 1981: 875.00`；文中另称 1932 年最低日 7 月 8 日收于 `41.22`，1998 年末 `9,181`。

**结论：⚠️ 有出入（仅 1964 年差 1 分钱）**
- 1981-12-31 = **875.00** ✅；1998-12-31 = **9,181.43** ✅；1932-07-08 = **41.22** ✅
- 1964-12-31：美国政府《总统经济报告》统计附录为 **874.13**，原文写 874.12，差 0.01（应属四舍五入/当时数据源差异，不影响论证）

**出处**：
- ERP 2021 Table B-55（1949–2003 年末道指）<https://www.govinfo.gov/content/pkg/ERP-2021/pdf/ERP-2021-table55.pdf>
- SEC 存档道指日线（1998-12-31 = 9,181.43）<https://www.sec.gov/Archives/edgar/data/357298/000035729801500016/dowjones.html>
- Wikipedia: Closing milestones of the DJIA（1932-07-08 = 41.22）<https://en.wikipedia.org/wiki/Closing_milestones_of_the_Dow_Jones_Industrial_Average>

---

## 2. 美国名义 GDP：1964→1981 增 370%；1981→1998 "不到三倍"

**原文**：`almost quintupled, rising by 370%`；`GDP less than tripled`。

**结论：✅ 核实一致**
- FRED `GDPA`：1964 = 684.460；1981 = 3,207.041；1998 = 9,062.817（十亿美元）
- 1964→1981 = +**368.6%**（4.69 倍，"almost quintupled / 370%" 成立）
- 1981→1998 = **2.83 倍**（<3 倍，"less than tripled" 成立）

**出处**：FRED/BEA 名义 GDP（年度）<https://fred.stlouisfed.org/series/GDPA>

---

## 3. 长期国债收益率：1964 末 "just over 4%"；1981 末 "more than 15%"；1998 末 5%

**原文**：`just over 4% at year-end 1964 to more than 15% by late 1981`；`long-term government interest rates had made their way down to that 5%`。

**结论：✅ 核实一致**
- 1964-12 十年期常数到期收益率 = **4.18%**（"just over 4%"）
- 1981 年 30 年期峰值：FRED `WGS30YR` 1981-10-02 = **15.07%**（Macrotrends 记 10-26 高达 15.21%）；1981-10 月均 14.68%，符合 "more than 15% by late 1981"
- 1998-12 三十年期 = **5.06%**（十年期 4.65%），"5%" 成立

**出处**：FRED `GS10` / `GS30` / `WGS30YR` <https://fred.stlouisfed.org/data/WGS30YR>；<https://www.macrotrends.net/2521/30-year-treasury-bond-rate-yield-chart>

---

## 4. 1981-11-16 发行的 14% 三十年期国债；100 万美元滚息到 1998 年末约 818 万美元（年化 >13%）

**原文**：`$1 million into the 14% 30-year U.S. bond issued Nov. 16, 1981... At the end of 1998... you would have had $8,181,219... annual return of more than 13%`。

**结论：✅ 核实一致（票息与发行日可核；终值复算相符）**
- 美国财政部拍卖数据：1981-11-05 拍卖、**1981-11-16 发行**、30 年期、2011-11-15 到期、CUSIP 912810CY2、**中标收益率 14.24%**（票息定在 14%，发行价低于面值）
- 终值复算：$8,181,219 / $1,000,000，17.12 年 → **13.07%/年**（"more than 13%" 成立）
- 说明：该终值隐含票息在 1980 年代以约 10% 左右的市场利率再投资，属可复现量级

**出处**：Treasury Fiscal Data 拍卖查询 API（`security_type=Bond, auction_date=1981-11-05`）<https://fiscaldata.treasury.gov/datasets/treasury-securities-auctions-data>；FRED `WGS30YR`

---

## 5. 同期 100 万美元买道指、股息再投资，到 1998-12-31 约 1,972 万美元（年化 19%）

**原文**：`If you'd invested $1 million in the Dow on Nov. 16, 1981, and reinvested all dividends, you'd have had $19,720,112 on Dec. 31, 1998... annual return would have been 19%`。

**结论：✅ 核实一致**
- 终值复算：$19,720,112 / $1,000,000，17.12 年 → **19.02%/年**（与 "19%" 完全吻合）
- 分解合理性：道指 875（1981 年末）→ 9,181.43（1998 年末）价格年化约 14.8%，加股息约 4 个百分点 ≈ 19%
- 注：原文起点是 **1981-11-16**（不是 1981 年末），与第 4 条债券同日买入

**出处**：ERP 2021 Table B-55（道指年末值）；复算见上

---

## 6. 企业税后利润占 GDP 比重：1929 峰值；1951 后 4%–6.5%；1982 约 3.5%；1990 末约 6%

**原文**：`corporate profits as a percentage of GDP peaked in 1929`；`from 1951 on... 4% to 6.5% range`；`in 1982 profits tumbled to 3.5%`；`by the late 1990s... close to 6%`。

**结论：⚠️ 有出入（趋势对，具体点位与现行修订数据不符）**
- 1929 为峰值 ✅：税前利润 10.911 / GDP 104.556 = **10.4%**（税后约 9%），确为历史高点
- 1951–1981 区间 ⚠️：现行 BEA 修订数据 CP/GDP = **4.97%–8.93%**（1974–75、1980 衰退年冲高），并非整齐的 4%–6.5%；1999 年当时口径的数据更低，故原文表述与当时图表一致
- 1982 = 3.5% ⚠️：现行数据 **5.16%（CP）／5.29%（含 IVA/CCAdj）**，复现不出 3.5%（1982 确为战后低点，方向正确；差额来自 BEA 后续大幅上修）
- 1990 年代末 ≈6% ✅：1998 年 CP/GDP = **5.73%**，含 IVA/CCAdj = **6.64%**

**出处**：FRED `CP`、`CPATAX`、`GDPA`；EPI 对 1982 为战后低点的表述 <https://www.epi.org/publication/ib364-corporate-tax-rates-and-economic-growth>

---

## 7. 1999 年 7 月 Paine Webber/Gallup 调查：新手预期 22.6%，20 年以上老手 12.9%

**原文**：`least experienced investors... expect annual returns over the next ten years of 22.6%. Even those who have invested for more than 20 years are expecting 12.9%`。

**结论：✅ 核实一致**
- FORTUNE 原文转载版逐字一致；Gallup 1999-07-29 新闻稿（Paine Webber/Gallup 投资者乐观指数）同期发布，调查确为 1999 年 7 月

**出处**：<https://fortune.com/article/warren-buffett-on-stock-market>；<https://news.gallup.com/poll/3685/index-investor-optimism-moves-sharply-higher-july.aspx>

---

## 8. FORTUNE 500：1998 年利润 $334,335,000,000；1999-03-15 市值 $9,907,233,000,000

**原文**：同上两行数字。

**结论：✅ 核实一致**
- 两数字与原文完全一致，市值约 **9.9 万亿美元**（÷利润 ≈ 29.6 倍市盈率，文中"$10 trillion for $334 billion"表述相符）
- 说明：该市值是 1999-03-15 的时点值，非年末值；利润含 Ford 分拆的一次性收益（见第 11 条）

**出处**：FORTUNE 转载版 <https://fortune.com/article/warren-buffett-on-stock-market>；Rational Walk 复核（约 30 倍 PE）<https://rationalwalk.com/mr-buffett-on-the-stock-market>

---

## 9. 美国马匹数量：1900 年约 2,100 万；1998 年约 500 万

**原文**：`1900: 21 million / 1998: 5 million`（图表）。

**结论：✅ 核实一致（1900 年数字视口径 21–21.5 百万）**
- 1900 年马+骡约 **2,150 万**（1910–1920 年峰值 2,500–2,750 万）；此后降至 1960 年约 300 万，1990 年代回升至 **400–500 万**

**出处**：Yale Energy History（普查数据：1840 年 430 万，1910 年峰值 2,750 万）<https://energyhistory.yale.edu/horse-and-mule-population-statistics>；<https://en.wikipedia.org/wiki/Horses_in_the_United_States>

---

## 10. 汽车业与美国车企；航空业制造商/破产/累计利润

**原文**：`at least 2,000 car makes... we came down to three U.S. car companies`；`1919-39 period, there were about 300 companies`；`129 airlines that in the past 20 years filed for bankruptcy. Continental... twice. As of 1992... money that had been made since the dawn of aviation... was zero`。

**结论：分项**
- 约 2,000 个汽车品牌 ✅（维基：美国历史上约有 **3,000** 家汽车公司；Buffett 自述依据其 70 页名单，"at least 2,000" 属保守）
- 1990 年代只剩 3 家美国车企 ✅（GM/Ford/Chrysler "Big Three"；1998 年 Daimler-Chrysler 合并后变"Big Two"）
- 1919–1939 约 300 家飞机制造商 ❓：未找到独立权威统计；同期美国航空制造业高度分散、此后大幅整合为行业共识，但"300" 系 Buffett 自述
- 129 家航空公司 20 年内破产 ❓：该名单为 Buffett 自制清单，无独立公开名录可比；维基"美国航空公司破产列表"1979–1999 条目约 79 处年份记录（含重复/不全），只能支持"数十家破产"的量级
- Continental 破产两次 ✅（1983 年、1990 年 12 月）
- 截至 1992 年航空业累计利润为零 ❓：系 Buffett 引用的行业统计，未找到可独立复算的原始出处（其 1991 年报对行业毁灭性亏损的描述可作旁证）

**出处**：<https://en.wikipedia.org/wiki/Automotive_industry_in_the_United_States>；<https://en.wikipedia.org/wiki/List_of_airline_bankruptcies_in_the_United_States>；<https://dwuconsulting.com/dwu-ai/airline-bankruptcy-restructuring-history>；Yale SOM 收录的 Buffett 原文 <https://som.yale.edu/sites/default/files/2021-12/Module8-Readng.pdf>

---

## 11. 福特 1998 年因分拆 Associates 计入约 160 亿美元账面收益

**原文**：`a $16 billion bookkeeping gain that Ford reported from its spinoff of Associates`。

**结论：⚠️ 有出入（16.5 vs 16，属取整）**
- 1998-03 媒体报道：Ford 将因分拆 Associates First Capital 在 **1998 年一季度**确认 **165 亿美元**一次性非应税会计收益（同期向股东分配股票+现金 258 亿美元）
- Buffett 取整为 160 亿，量级正确

**出处**：Los Angeles Times, 1998-03-04 <https://www.latimes.com/archives/la-xpm-1998-mar-04-fi-25170-story.html>

---

## 12. 摩擦成本：总额约 1,300 亿美元；成交量 ≥3,500 亿股 × 每股每边 6 美分 ≈ 420 亿；股票基金 3.5 万亿 × 1% ≈ 350 亿

**原文**：`well over $100 billion a year—say, $130 billion`；`at least 350 billion shares of stock traded in the U.S. ... 6 cents ... adds up to $42 billion`；`assets of about $3.5 trillion ... at least 1%, or $35 billion`。

**结论：✅ 分项可核（总额 130 亿级为 Buffett 估算，无法外部证实）**
- 成交量 ✅：1999 年 NYSE **2,039 亿股** + Nasdaq **2,726 亿股** ≈ **4,760 亿股**，远超"至少 3,500 亿股"
- 算术 ✅：3,500 亿股 × 2（买卖两边）× $0.06 = **420 亿美元**
- 基金资产 ✅：ICI：1999 年末美国**国内股票型基金 3,008 只、资产 3.455 万亿美元**（"about $3.5 trillion" 精确命中）；× 1% = **345 亿美元**
- 总额 $130B ❓：Buffett 自估（文中亦自陈"highly defensible... possibly on the low side"），无独立统计可核

**出处**：NYSE 1999 年成交量公告（2,039 亿股）<https://mondovisione.com/media-and-resources/news/final-1999-trading-volume-ipos-star-at-the-nyse-2011124>；Nasdaq 1999 年成交量（2,726 亿股）<https://mondovisione.com/media-and-resources/news/nasdaqworlds-biggest-stock-market-by-dollar-value-2011124>；ICI《Mutual Fund Assets and Flows in 1999》<https://www.iciglobal.org/pubfile_pdf/per06-02.pdf>

---

## 汇总

| # | 项目 | 结论 |
|---|---|---|
| 1 | 道指四点位 | ⚠️ 1964 年为 874.13（原文 874.12），其余全对 |
| 2 | GDP 1964→1981 +370%；1981→1998 <3 倍 | ✅（+368.6%；2.83 倍） |
| 3 | 长债收益率 4% / >15% / 5% | ✅（4.18%；峰值 15.07–15.21%；5.06%） |
| 4 | 14% 三十年期国债、$8,181,219 (>13%) | ✅（1981-11-16 发行，中标 14.24%；复算 13.07%） |
| 5 | 道指 $19,720,112（19%） | ✅（复算 19.02%） |
| 6 | 利润/GDP 四个点位 | ⚠️ 1929 峰值✅、1990 末≈6%✅；区间与 1982 年 3.5% 与现行修订数据不符 |
| 7 | Paine Webber/Gallup 22.6% / 12.9% | ✅ |
| 8 | F500 利润 $334,335M、市值 $9,907,233M | ✅（≈29.6 倍 PE） |
| 9 | 马匹 2,100 万 / 500 万 | ✅（1900 约 2,150 万；1990s 400–500 万） |
| 10 | 汽车/航空业结构性事实 | 2,000 品牌✅、三巨头✅、Continental 两次✅；300 家飞机厂❓、129 家破产❓、1992 累计利润零❓ |
| 11 | Ford 160 亿美元分拆收益 | ⚠️ 实为 165 亿美元（1998Q1） |
| 12 | 摩擦成本三分项 | 成交量✅、$42B 算术✅、$3.5T×1%✅（ICI 3.455T）；$130B 总额❓（自估） |

**总评**：12 组核验点中，**7 组完全核实一致，3 组为可解释的小幅出入/口径差异，2 组含无法独立复核的 Buffett 自述数据**。核心论证链（GDP 增长 vs 道指零涨幅、利率 15%→5%、利润/GDP 均值回归、摩擦成本侵蚀回报）在官方数据上全部站得住；需要标注的软点是 1982 年"3.5%"利润占比与"129 家航空公司""300 家飞机制造商"三处自述数字。
