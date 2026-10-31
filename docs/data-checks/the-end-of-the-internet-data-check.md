# 《The End of the Internet》事实核验表

- **原文**：Ben Thompson, "The End of the Internet", Stratechery, 2026-10-26 — <https://stratechery.com/2026/the-end-of-the-internet/>
- **核验对象**：`/tmp/endnet/part1_src.md`、`part2_src.md`、`part3_src.md`（共 18,264 字节，与已发布正文逐字一致，故可直接以上述 URL 作为引用源）
- **核验日期**：2026-10-31
- **标记**：✅ 核实无误｜📌 属实但口径/表述需注意｜⚠️ 部分成立、部分未坐实｜❓ 未取到一手来源（未证伪）｜❌ 错误

**总计 51 条：✅ 42 条｜仅 📌（属观点/口径需注意）5 条｜⚠️ 1 条｜❓ 3 条｜❌ 0 条。**
另有 8 条标 ✅ 的同时附 📌，提示口径差异（第 5、9、11、15、32、34、42、49 条）。

---

## 一、开篇：2003 年与 WordPress（part1 §1）

**1.** "It was the summer of 2003, just weeks before I was set to move to Taiwan"
✅ 本人自述，且与其"台湾六年、2009 年入读 Kellogg"的公开履历自洽。
出处：<https://stratechery.com/about/>；<https://en.wikipedia.org/wiki/Ben_Thompson_(writer)>

**2.** "this was my fourth swing at the blog thing (it was the seventh that ended up being Stratechery)"
❓ 仅作者自述，无外部可核记录（GeoCities / Blogspot / FrontPage 站点均未留档）。
备注：属个人史，翻译保留原话即可，不必加注。

**3.** "a just-released piece of software that promised a five-minute install; it was called WordPress"
✅ WordPress 0.7 于 2003-05-27 发布（2003-01-24 Mullenweg 发《The Blogging Software Dilemma》，4 月 fork b2），2003 年夏正是"刚发布"；"Famous 5-Minute Install" 是 WordPress Codex 官方沿用的说法。
出处：<https://learn.wordpress.org/lesson-plan/general-history-of-wordpress>；<https://journals.ala.org/index.php/ltr/article/view/4277/4898>

**4.** "it turned out I needed to learn how to create a MySQL database and configure PHP"
✅ WordPress 一直以 PHP + MySQL 为运行前提，2003 年需手工建库、改 `wp-config.php`，与描述一致。
出处：同上（WordPress 官方历史课件）

**5.** "news broke that every version of PHP had a critical bug that allowed for remote code execution on the host machine"
✅（📌 措辞注意）2026-10-21 披露 CVE-2026-109618 / CVE-2026-109619（CVSS 9.2），修复版 8.5.12 / 8.4.27 / 8.3.36 / 8.2.35，并回补 7.4 / 8.0 / 8.1，即"所有在用分支皆受影响"，10-17 已见在野利用。
📌 "every version"指**版本覆盖面**（连 PHP 5 都受影响），不是"每个版本各有一个洞"——原文下一节自己写明 "The PHP vulnerabilities were just two"。
出处：<https://www.datadoghq.com/blog/php2shell-cve-2026-109618/>；NVD CVE-2026-109618

**6.** "news broke … last week"
✅ 披露日 2026-10-21（周三），文章 2026-10-26（周一），"上周"成立。

**7.** "that WordPress is managed by Pressable, an Automattic company"
✅ Pressable（前身 ZippyKid，2010 年创立于圣安东尼奥）2016 年由 Automattic 取得多数股权，官网长期自称 "an Automattic company"。
出处：<https://pressable.com/>；<https://en.wikipedia.org/wiki/Automattic>

**8.** "twenty-some years ago I was doing everything by hand"
✅ 2003 → 2026 为 23 年，"twenty-some"准确。

---

## 二、博客前史（part1 §2）

**9.** "Dave Winer, often considered the father of blogs, started Scripting News in 1997, after early experiments with a personal site called DaveNet"
✅ / 📌 两处小口径：
- Scripting News 起点：Winer 自述页写 "1997"（并自嘲"或者 1994、1996，看你怎么算"），Wikipedia 记 1997 年 2 月。
- DaveNet 实际是 **1994 年 11 月起的邮件通讯（email newsletter）**，1995 年 1 月才有网页存档，称其为 "personal site" 略不精确。
出处：<http://scripting.com/about/>；<https://en.wikipedia.org/wiki/Dave_Winer>；<http://www.digitalriptide.org/2016/11/29/davenet/>

**10.** "Justin Hall started Links.net in 1994"
✅ 1994 年 1 月（Swarthmore 学生宿舍），"Justin's Links from the Underground"，被广泛称为最早的个人博客。
出处：<https://en.wikipedia.org/wiki/Justin_Hall>

**11.** "Jorn Barger coined the term 'weblog' for Robot Wisdom, also in 1997"
✅ 1997-12-17 起在 Robot Wisdom 使用 "weblog" 一词，为该词公认出处。
📌 Robot Wisdom 站点本身 1995 年 2 月已存在（当时是乔伊斯/人工智能论文站），"weblog"部分自 1997 年 12 月开始。
出处：<https://en.wikipedia.org/wiki/Jorn_Barger>；<https://en.wikipedia.org/wiki/Blog>

**12.** "the influential kottke.org started in 1998"
✅ 1998 年 3 月开站。
出处：<https://kottke.org/about>；<https://en.wikipedia.org/wiki/Jason_Kottke>

---

## 三、2000–2003 博客年表（part1 §2）

**13.** "Talking Points Memo … launched in 2000"
✅ 2000-11-12 首帖。
出处：<https://en.wikipedia.org/wiki/Talking_Points_Memo>

**14.** "Andrew Sullivan … launched in 2000"
✅ The Daily Dish 于 2000 年开写（早期平台为 Blogger，后转独立站）。
出处：<https://en.wikipedia.org/wiki/Andrew_Sullivan>

**15.** "Boing Boing launched in 2000"
✅ 2000 年转为 group blog（Mark Frauenfelder 等）。
📌 Boing Boing 前身是 1988 年的纸质 zine，网站 1995 年即有——"launched in 2000"指的是**博客形态**的起点，不是品牌起点。
出处：<https://en.wikipedia.org/wiki/Boing_Boing>

**16.** "Instapundit … launched in 2001"
✅ 2001 年（Glenn Reynolds）。
出处：<https://en.wikipedia.org/wiki/Instapundit>

**17.** "Little Green Footballs … launched in 2001"
❓ 通行记载为 2001 年（Charles Johnson 创立），本次未取到一手档案（站点旧档/权威条目均未直接命中），亦无任何反证。
备注：不影响段落结论；若需硬引用，建议补 Wayback 最早快照。

**18.** "Dooce launched in 2001"
✅ 2001 年 2 月首帖（Heather Armstrong，"Carnation Milk"）。
出处：<https://en.wikipedia.org/wiki/Heather_Armstrong>；Forbes 2009 专访 <https://www.forbes.com/2009/07/15/dooce-heather-armstrong-forbes-woman-power-women-blog.html>

**19.** "Matt Yglesias … launched in 2002"
✅ "Yglesias started blogging in early 2002, while still in college"。
出处：<https://en.wikipedia.org/wiki/Matthew_Yglesias>

**20.** "Daily Kos … launched in 2002"
✅ 2002-05-26 首帖（Markos Moulitsas）。
出处：<https://en.wikipedia.org/wiki/Daily_Kos>

**21.** "Eschaton … launched in 2002"
✅ Atrios 的 Eschaton 2002 年已在更新（2002-05 存档页可取）。
出处：<https://www.eschatonblog.com/2002_05_01_archive.html>

**22.** "The Volokh Conspiracy … launched in 2002"
✅ 2002 年 4 月（Eugene Volokh）。
出处：<https://en.wikipedia.org/wiki/The_Volokh_Conspiracy>

**23.** "Power Line … launched in 2002"
✅ 2002-05-27 首帖（Hindrocket / John Hinderaker 等）。
出处：<https://en.wikipedia.org/wiki/Power_Line>

**24.** "Gizmodo … launched in 2002"
✅ 2002-07-01（Gawker Media 旗下首个子站）。
出处：<https://en.wikipedia.org/wiki/Gizmodo>

**25.** "Gawker … launched in 2002"
✅ 2002 年末上线（Elizabeth Spiers 主编）。
出处：<https://en.wikipedia.org/wiki/Gawker>

**26.** "paidContent … launched in 2002"
✅ 2002 年（Rafat Ali）。
出处：<https://en.wikipedia.org/wiki/Rafat_Ali>

**27.** "Daring Fireball … launched in 2002"
✅ 官方存档最早条目为 2002 年 8 月。
出处：<https://daringfireball.net/archive>；<https://en.wikipedia.org/wiki/John_Gruber>

**28.** "Ezra Klein … launched in 2003"
❓ 通行记载为 2003 年（先在 American Prospect 开博，同年加入 Howard Dean 竞选团队），本次未取到其博客一手首帖时间。
备注：同 17，不影响段落结论。

**29.** "Marginal Revolution … launched in 2003"
✅ "Cowen … has co-authored *Marginal Revolution* with Alex Tabarrok since 2003"。
出处：<https://en.wikipedia.org/wiki/Tyler_Cowen>

**30.** "ReadWriteWeb … launched in 2003"
✅ 2003 年（Richard MacManus，后更名 ReadWrite）。
出处：<https://en.wikipedia.org/wiki/ReadWrite>

**31.** "AVC … launched in 2003"
✅ 2003-09-23 首帖 "MY First Post"（avc.typepad.com，Fred Wilson）。
出处：<https://avc.com/>；<https://en.wikipedia.org/wiki/Fred_Wilson_(financier)>

---

## 四、订阅制与 90-9-1（part1 §2–3、part2 §1）

**32.** "Sullivan was, for the last two years, supported by reader subscriptions to the tune of nearly one million dollars a year"
✅ 该句出自 Thompson 本人 2015 年《Blogging's Bright Future》，原文即 "nearly one million dollars a year"；数据源头为 GigaOm 2014-10-10 对 The Dish 的报道（约 $1M/年，订阅收入）。
📌 三点口径：①"nearly/almost"≈略低于 100 万美元；②口径是**订阅收入（gross）**，非净利；③时间窗是 2012 年转订阅制后的 2013–2014。
出处：<https://stratechery.com/2015/bloggings-bright-future/>；<https://gigaom.com/2014/10/10/andrew-sullivan/>

**33.** "by the end of the decade … the ads became more intrusive even as the payouts shrank"
📌 作者回忆性判断（AdSense 单位点击收入下滑、广告位内卷），方向上与业界共识一致，但无可引用的硬数据支撑。
备注：属观点句，翻译照录即可。

**34.** "Social media 1.0 … followed the 90-9-1 rule: one percent spoke, nine percent commented, and 90 percent lurked"
✅ 90-9-1 三分法出自 Jakob Nielsen（NN/g）2006-10-08《Participation Inequality: The 90-9-1 Rule》。
📌 Nielsen 原词是 "participate a lot / contribute from time to time / lurk"（1% / 9% / 90%），"spoke / commented / lurked" 是转述；更早的 "1% rule" 常被归给 McConnell & Huba（2003），Nielsen 是三分法出处。
出处：<https://www.nngroup.com/articles/participation-inequality/>

---

## 五、社交媒体（part2 §1）

**35.** "algorithms started to matter — Facebook had one relatively early, but it took Twitter much longer"
✅ 相对判断成立：Facebook News Feed 2006 年即算法排序；Twitter 直到 2016 年才默认切换算法时间线。
备注：原文是相对表述（"relatively early"），不涉具体年份，故风险低。

**36.** "culminating in TikTok, a social media site with basically zero social component"
📌 作者评价，不是可核事实（TikTok 仍有评论/合拍/私信，但产品核心是推荐流而非关系链）。

**37.** "social networking … isn't public, but is rather in group chats"
📌 作者判断。外部数据方向一致（Meta 2023 起反复强调私域消息量超公开动态），但无单一权威数字可引。

---

## 六、2026 年 10 月安全事件清单（part2 §2）—— 本文事实密度最高的一段

**38.** "The PHP vulnerabilities were just two of a host of security issues last week alone"
✅ 见第 5 条；"just two"与 CVE 数量完全对上。

**39.** "Compromised intermediate CA private keys (although this was an example of sheer incompetence, not AI hacking)"
✅ 事实：印度 CA **eMudhra（emSign）** 的 **8 张中间 CA 私钥**（6 张 TLS、2 张代码签名）可被还原——2025 年 4 月密钥生成仪式（KGC）中随机数只用了**单字节**（d = 4/56/66/115/155/156/230/237），任何人可用公开证书在毫秒级暴力取得；2026-10-17～10-23 集中披露，Chrome / Mozilla / Apple / Microsoft 撤信，Go 记为 CVE-2026-111943，Red Hat RHSB-2026-012。
✅ 作者的"sheer incompetence, not AI hacking"判断同样成立：这是**人为密钥生成错误**，与 AI 攻击无关。
出处：<https://unit42.paloaltonetworks.com/emudhra-certificate-compromise>；<https://blog.talosintelligence.com/compromised-intermediate-certificates>；<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-emudhra-info-ScS22A1r>；<https://access.redhat.com/security/vulnerabilities/RHSB-2026-012>；<https://www.microsoft.com/en-us/msrc/blog/2026/10/microsoft-response-to-compromised-emudhra-certificate-authority-keys>

**40.** "Major new vulnerabilities in Node.js, GitLab, Java, and Cisco products"
⚠️ 部分成立：
- **Java ✅**：eMudhra 事件中 Java 是重灾区（静态 `cacerts`、无 CT 强制、`com.sun.net.ssl.checkRevocation` 默认 false），各 JDK 需换信任库。
- **Cisco ✅**：Cisco 就 eMudhra 事件发了专门公告（cisco-sa-emudhra-info-ScS22A1r），并列出多款产品修复版本（Duo 系列 2026-10-21/22 发布）。
- **Node.js / GitLab ❓**：未取到当周（10/19–10/25）的一手安全公告，不能坐实"当周有重大新漏洞"。
备注：即使 Node.js、GitLab 两项不成立，"host of security issues last week"的整体论断已有 PHP、eMudhra、LiteLLM、Railway 四项硬证据支撑。

**41.** "Breaches in LiteLLM's supply chain"
✅ LiteLLM **1.107.0** 于 2026-10-21 被投毒（PyPI wheel + 官方容器镜像，窃取凭据并植入后门），约 2 小时窗口，Wiz 估约 4.9 万次下载，为 2026 年内第二次。
出处：<https://socket.dev/blog/malicious-litellm-versions>；<https://www.wiz.io/blog/lightllm-supply-chain-attack>

**42.** "…and Railway developer platform"
✅ Railway 于 2026-10-21 09:25 UTC 披露：攻击者经构建基础设施提权，窃取 CI 凭据并解密部分客户环境变量；官方称**最多 1.85% workspace** 可能受影响，已轮换全部 key / token / bucket 凭据并暂停部署，22 日起分批恢复。攻击窗口 10-20～10-22。
📌 严格说，LiteLLM 是"供应链投毒"，Railway 是"平台被入侵导致凭据泄露"，两者性质不同，原文并列可接受但不精确。
出处：<https://blog.railway.com/p/preliminary-report-october-security-incident>；TechCrunch 2026-10-22 报道

**43.** "AI … has limitless time and the ability to substitute iteration for cleverness"
📌 作者论断（对未来攻击范式的判断），无可核事实。

---

## 七、Venkatesh Rao《Cognitive Mercantilism》（part3 §1）

**44.** "Venkatesh Rao wrote an absolute must-read essay over the weekend called Cognitive Mercantilism"
✅ 该文确实存在，标题一致，发布于 **2026-10-25（周日）**，与"over the weekend"吻合。
出处：<https://contraptions.venkateshrao.com/p/cognitive-mercantilism>

**45.** "From a world where 80% of human brains are engaged in subsistence cognition to one in which 95% are engaged in satisfying previously unfulfillable cognitive demands."
✅ 与 Rao 原文**逐字一致**（80% / 95% 两个数字未走样）。

**46.** 对 Rao 论点的概述（"mercantilism 假设经济学是稀缺与控制；带来资本主义的是需求……'subsistence cognition'"）
✅ 忠实于原文：Rao 确以" subsistence cognition "设喻，并以农业革命→工业商业社会的类比推出"认知需求"的释放；"cognitive mercantilist / AI Malthusian / cognitive capitalist"三分法亦为原文所有（见 part3 引文）。
备注：概述属解释性转述，无失实；"subsistence cognition"带引号处为原文术语。

---

## 八、托克维尔引文（part3 §1–2）

**47.** "Alexis de Tocqueville, in Democracy in America, famously wrote:"
✅ 引文归属正确，出自《论美国的民主》**第二卷 第二部 第五章**"Of The Use Which The Americans Make Of Public Associations In Civil Life"。

**48.** 引文一："The political associations which exist in the United States are only a single feature in the midst of the immense assemblage of associations in that country. Americans of all ages, all conditions, and all dispositions, constantly form associations. …in the United States you will be sure to find an association."
✅ 与 Gutenberg 电子版（#816，Reeve 译本）**逐字一致**。
出处：<https://www.gutenberg.org/ebooks/816>（该书该章原文）

**49.** 引文二："I met with several kinds of associations in America, of which I confess I had no previous notion; …the latter seem to regard it as the only means they have of acting."
✅ 逐字一致，同属第五章。
📌 排版注意：这两段在托克维尔原文中是**同一自然段的前后两半**（"…you will be sure to find an association. I met with several kinds of associations in America…"），Stratechery 把它拆成两个 blockquote；译成中文时若合并为一段并加"（同段续）"更准确，不要误标为两处不同出处。

**50.** "the Internet is an American invention, and has long been defined by American mores"
📌 作者论断。史实层面需注意：分组交换/ARPANET 是美国（1969），但万维网是 CERN 的 Tim Berners-Lee（1989–91，英国/瑞士），原文说的是 "the Internet" 而非 "the Web"，故不算错，但中文若译成"互联网/万维网"混用会失真。

---

## 九、赞助段落（part3 §3）

**51.** "Stripe provides the foundation for Internet-native companies — including Stratechery… Substack creators are also Stripe customers"
✅ Substack 的支付与订阅计费确由 Stripe 提供，Substack 作者因此是 Stripe 客户；Stratechery 亦长期使用 Stripe。
📌 该段是 "Presented by Stripe" 赞助内容（广告），按惯例不做事实等级评判，仅作背景核对。

---

## 十、总体结论

- 全文事实密度集中在两类：①博客史年表（24 个站点/年份）；②2026 年 10 月安全事件清单（PHP、eMudhra、LiteLLM、Railway）。
- **2000–2003 年表 19 项中 17 项核到一手/权威来源**，仅 Little Green Footballs(2001)、Ezra Klein(2003) 两项属"通行说法、未取一手档案"，且不构成任何反证。
- **安全事件 4 项全部坐实**，是全文最硬的部分；唯一含糊的是"Node.js、GitLab 当周重大新漏洞"这一并列项，未取到当周公告。
- **未见明确错误（❌ = 0）**。需要译者留意的只有三处口径：PHP "every version"的所指、Pressable 收购年份（2016 非 2021）、托克维尔两段引文实为同段连续文本。
