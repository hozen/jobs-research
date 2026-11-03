#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 essays/ms-capital-allocation.html（单页 88 页全文）拆成「按章节」的分页版。

背景：Mr. Buffett 2026-11-03 19:26 要求「中英对照翻译并上线 · 保留原图 · 分批上线，如按章节」。
全文版 2026-10-24 已上线（essays/ms-capital-allocation.html，48 张原图），
本次只做**分章**这一层：essays/ms-capital-allocation/{index,ch1..ch9}.html，原图共用 essays/img/。

产物：
    essays/ms-capital-allocation/index.html   章节目录（含 hero 一句话论点 + 全文版入口）
    essays/ms-capital-allocation/chN.html     第 N 章（中英对照原样搬运，图路径改 ../img/）

用法：
    python3 tools/split_ms_capital_allocation.py            # 只生成，不发布
    python3 tools/split_ms_capital_allocation.py --batch 1   # 生成第 1 批（1-3 章）
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent          # jobs-research/
ESSAYS = BASE / "essays"
SRC = ESSAYS / "ms-capital-allocation.html"
OUT_DIR = ESSAYS / "ms-capital-allocation"

BATCHES = {1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9]}
CHAPTER_TITLES = {
    1: "导言：资本配置是 CEO 的首要职责",
    2: "基础：钱从哪来、钱到哪去",
    3: "资本配置的其他选项",
    4: "评估管理层的资本配置能力",
    5: "结论",
    6: "评估资本配置能力的清单",
    7: "附录：股息与股份回购的等价性",
    8: "译者注与数据核验",
    9: "原文注释与数据来源",
}

EXTRA_CSS = """
.kicker { font-size: 13px; color: var(--meta); letter-spacing: .5px; margin: 0 0 6px; }
h1 .en { display: block; font-size: 15px; font-weight: 400; font-style: italic; color: var(--meta); margin-top: 6px; letter-spacing: 0; }
.chnav { margin: 48px 0 0; padding-top: 20px; border-top: 1px solid var(--rule); display: flex; gap: 16px; flex-wrap: wrap; justify-content: space-between; font-size: 14px; }
.chnav a { color: var(--meta); text-decoration: none; }
.chnav a:hover { color: var(--text); text-decoration: underline; }
.toc-list { list-style: none; padding: 0; margin: 24px 0 0; }
.toc-list li { margin: 0; padding: 16px 0; border-bottom: 1px solid var(--rule); }
.toc-list a { font-size: 17px; font-weight: 600; text-decoration: none; }
.toc-list a:hover { text-decoration: underline; }
.toc-list .en { display: block; font-size: 13px; font-style: italic; color: var(--meta); font-weight: 400; margin-top: 4px; }
.toc-list .sub { display: block; font-size: 14px; color: #555; margin-top: 6px; line-height: 1.6; }
.toc-list .badge { font-size: 12px; color: var(--meta); }
"""


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", type=int, choices=[1, 2, 3], help="只生成某一批（默认全量）")
    args = ap.parse_args()

    html = read(SRC)
    m_head = re.search(r"^(.*?)<body>", html, re.S)
    head = m_head.group(1)                      # <!DOCTYPE ... </head>
    css_end = head                                   # 样式已在 head 内
    body = html[m_head.end():]
    footer_start = body.find('<p class="footer">')
    assert footer_start > 0, "找不到 footer"
    footer = body[footer_start:]                     # footer + </body></html>

    # 切章节：每个 <h2 开始，到下一个 <h2 或 footer 结束
    idx = [m.start() for m in re.finditer(r"<h2[^>]*>", body)]
    idx.append(footer_start)
    chapters: dict[int, str] = {}
    for n in range(1, len(idx)):
        chapters[n] = body[idx[n - 1]:idx[n]].rstrip()

    assert len(chapters) == 9, f"章节数不是 9 而是 {len(chapters)}"

    # 校验：章节外不得丢内容
    pre = body[:idx[0]]
    lost = re.sub(r"<[^>]+>", "", pre).strip()
    assert len(lost) < 4000, f"h2 之前的内容过多（{len(lost)} 字），可能漏了正文"

    OUT_DIR.mkdir(exist_ok=True)
    wanted = ([n for b in range(1, args.batch + 1) for n in BATCHES[b]]
               if args.batch else list(range(1, 10)))

    def rel_fix(s: str) -> str:
        """章节页在 essays/ms-capital-allocation/ 下 —— 相对资源加一层 ../"""
        s = s.replace('src="img/', 'src="../img/')
        s = re.sub(r'href="(?!https?:|#|mailto:)([^"/]+\.html)"', r'href="../\1"', s)
        return s

    def h1_en(chunk: str) -> str:
        m = re.search(r"<h2[^>]*>(.*?)</h2>", chunk, re.S)
        inner = m.group(1)
        zh = re.sub(r'<span class="en">.*?</span>', "", inner, flags=re.S)
        zh = re.sub(r"<[^>]+>", "", zh).strip()
        en = re.search(r'<span class="en">(.*?)</span>', inner, re.S)
        return zh, (re.sub(r"<[^>]+>", "", en.group(1)).strip() if en else "")

    def page_head(title: str, desc: str = "") -> str:
        """按章重写 <title> / description（分享卡与搜索结果看这个）。"""
        h = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", head, count=1, flags=re.S)
        if desc:
            h = re.sub(r'<meta name="description" content="[^"]*"',
                       f'<meta name="description" content="{desc}"', h, count=1)
        return h

    for n in wanted:
        chunk = rel_fix(chapters[n])
        zh, en = h1_en(chapters[n])
        chunk = re.sub(r"<h2[^>]*>(.*?)</h2>",
                       lambda mm: f'<h1>{mm.group(1)}</h1>', chunk, count=1, flags=re.S)
        prev_link = (f'<a href="ch{n-1}.html">← 第 {n-1} 章 · {CHAPTER_TITLES[n-1]}</a>'
                     if n > 1 else '<a href="../ms-capital-allocation.html">← 全文版</a>')
        last_in_batch = bool(args.batch) and n == max(BATCHES[args.batch])
        if n >= 9:
            next_link = '<a href="index.html">读完，回目录 →</a>'
        elif last_in_batch:
            # 分批上线：本批最后一章的下一章还没上线 → 不给 href，避免死链
            next_link = f'<span style="color:var(--meta)">第 {n+1} 章 · {CHAPTER_TITLES[n+1]}（下一批上线）</span>'
        else:
            next_link = f'<a href="ch{n+1}.html">第 {n+1} 章 · {CHAPTER_TITLES[n+1]} →</a>'
        page = f"""{page_head(f'第 {n} 章 · {zh} · 资本配置（中英对照）— 乔布斯研究',
                                f'Morgan Stanley《资本配置》中英对照翻译第 {n} / 9 章：{zh}（{en}）。全文 48 张原图，按章节阅读。')}
<style>{EXTRA_CSS}</style>
</head>
<body>

<p class="back">← <a href="../index.html">站主随笔</a> · <a href="index.html">资本配置 · 分章阅读</a></p>

<p class="kicker">资本配置：五条原则，看管理层会不会把钱花对地方 · 中英对照 · 第 {n} / 9 章</p>

{chunk}

<div class="chnav">
  <span>{prev_link}</span>
  <span><a href="index.html">目录</a></span>
  <span>{next_link}</span>
</div>

{rel_fix(footer)}"""
        (OUT_DIR / f"ch{n}.html").write_text(page, encoding="utf-8")

    # ---------- 目录页 ----------
    subs = {
        1: "为什么资本配置是 CEO 的第一职责；事业部之间几乎不做资本再配置的证据（图 1）。",
        2: "内部资金与外部融资的来源结构、八种用途的长期占比：capex / 研发 / 并购 / SG&A / 营运资本 / 剥离 / 股息 / 回购。",
        3: "六种备选方案逐一验：并购、SG&A、研发、资本开支、营运资本、剥离，以及股息与回购的等价性。",
        4: "估值商、ROIIC、TSR 与激励：怎么用数据判断管理层到底会不会配置资本（含微软、亿滋等案例）。",
        5: "全文结论：资本配置的五条原则。",
        6: "一张可直接拿去用的评估清单（Checklist）。",
        7: "附录：为什么股息与股份回购在理论上是等价的（含税与信号两种摩擦）。",
        8: "译者注与数据核验：原文数字与公开来源逐项对照的结果。",
        9: "原文 190 条注释、参考文献与免责声明。",
    }
    rows = []
    for n in range(1, 10):
        zh, en = CHAPTER_TITLES[n], ""
        m = re.search(r'<span class="en">(.*?)</span>', chapters[n], re.S)
        if m:
            en = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        if args.batch:
            ready = n in BATCHES[args.batch] or n <= max(w for b in range(1, args.batch + 1) for w in BATCHES[b])
        else:
            ready = True
        title = (f'<a href="ch{n}.html">{n}. {zh}</a>' if ready
                 else f'<span>{n}. {zh} <span class="badge">（即将上线）</span></span>')
        rows.append(f'  <li>{title}<span class="en">{en}</span>'
                    f'<span class="sub">{subs[n]}</span></li>')

    hero = re.search(r'<div class="hero">.*?</div>\n', body, re.S)
    hero_html = hero.group(0) if hero else ""

    index = f"""{page_head('资本配置 · 分章阅读（中英对照全文 9 章）— 乔布斯研究',
                            'Morgan Stanley《Capital Allocation》中英对照全文，按章节阅读：9 章 · 48 张原图 · 1970–2024 五十五年数据。')}
<style>{EXTRA_CSS}</style>
</head>
<body>

<p class="back">← <a href="../index.html">站主随笔</a> · <a href="../ms-capital-allocation.html">单页全文版</a></p>

<p class="kicker">Morgan Stanley · Counterpoint Global Insights（Consilient Observer）· 2025-11-05</p>
<h1>资本配置：五条原则，看管理层会不会把钱花对地方<span class="en">Capital Allocation: Results, Analysis, and Assessment</span></h1>
<p class="byline">
  全文中英对照 · 按章节阅读 · 48 张原图 · 正文 57 页 + 注释 13 页<br>
  原文：<a href="https://www.morganstanley.com/im/publication/insights/articles/article_capitalallocation.pdf">article_capitalallocation.pdf</a>（88 页）·
  作者：Michael J. Mauboussin &amp; Dan Callahan · 译者：站主（Mr. Buffett 委托）
</p>

{hero_html}
<ul class="toc-list">
{chr(10).join(rows)}
</ul>

<p class="footer">
  单页全文版：<a href="../ms-capital-allocation.html">ms-capital-allocation.html</a>（一页读完，便于搜索与打印）<br>
  <a href="../index.html">← 返回站主随笔</a>
</p>

</body>
</html>
"""
    (OUT_DIR / "index.html").write_text(index, encoding="utf-8")

    # ---------- 自检 ----------
    def count(s: str, pat: str) -> int:
        return len(re.findall(pat, s))

    tot_img = count("".join(chapters.values()), '<img ')
    tot_en = count("".join(chapters.values()), 'class="en-source"')
    out_img = sum(count(read(OUT_DIR / f"ch{n}.html"), '<img ') for n in wanted)
    print(f"章节 {len(chapters)} · 原文图 {tot_img} · 英文对照块 {tot_en}")
    print(f"已生成 {len(wanted)} 章（{wanted}），其中图 {out_img} 张")
    for n in wanted:
        p = OUT_DIR / f"ch{n}.html"
        s = read(p)
        print(f"  ch{n}.html {len(s):>7}B  图{count(s,'<img '):>3} 对照{count(s,'class=\"en-source\"'):>3} "
              f"h3={count(s,'<h3'):>3} 表格={count(s,'<table'):>2}")
    print(f"目录页 {len(index)}B")
    return 0


if __name__ == "__main__":
    sys.exit(main())
