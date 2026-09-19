# -*- coding: utf-8 -*-
import json, os, io, re, sys
from dsl import render_blocks, inline, esc
from css import CSS
from js import JS
import part1, part2, part3, part4, part5, part6, part7

SECTIONS = [part1.S0, part1.S1, part1.S2,
            part2.S3, part2.S4,
            part3.S5,
            part4.S6, part4.S7,
            part5.S8, part5.S9,
            part6.S10,
            part7.S11, part7.S12, part7.S13]

TITLE = "当存敬畏战兢的心作成得救的工夫"
SUBTITLE = ("腓立比书 2:1-18 · 海德堡要理问答主日 24（问 62-64）　"
            "欧陆改革宗式讲章全解")

ORDER = [
    ("上午诗歌", "圣诗第 4 首　·　韵诗 17 篇 1-3 节　·　圣诗 64 首　·　韵诗第 1 篇　·　圣洁诗第 9 首"),
    ("读经", "腓立比书 2:1-18"),
    ("要理问答", "海德堡要理问答 主日 24（问 62、63、64）"),
    ("讲题", "当存敬畏战兢的心作成得救的工夫"),
    ("要点一", "因神在你心里运行"),
    ("要点二", "为要成就他的美意"),
]

# ─────────────────────────────── 目录
def build_toc():
    out = ['<h5>目录 · Contents</h5>']
    for s in SECTIONS:
        out.append('<a class="l1" href="#%s">%s · %s</a>' % (s["id"], s["num"], esc(s["title"])))
        for b in s["blocks"]:
            if b["t"] == "h3" and b.get("id"):
                t = re.sub(r"\*\*|\{\{|\}\}|\[\[|\]\]", "", b["x"])
                if len(t) > 26:
                    t = t[:25] + "…"
                out.append('<a class="l2" href="#%s">%s</a>' % (b["id"], esc(t)))
    return "\n".join(out)

# ─────────────────────────────── 正文
def build_main():
    out = []
    for s in SECTIONS:
        out.append('<section class="part" id="%s">' % s["id"])
        out.append('<h2><span class="n">%s</span>%s</h2>' % (esc(s["num"]), inline(s["title"])))
        if s.get("sub"):
            out.append('<p class="psub">%s</p>' % inline(s["sub"]))
        out.append(render_blocks(s["blocks"]))
        out.append('</section>')
    return "\n".join(out)

HTML = """<!DOCTYPE html>
<html lang="zh-Hans">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="腓立比书 2:1-18 与海德堡要理问答主日 24 的欧陆改革宗式讲章全解：历史情境、逐节解经、原文字义、讲章正文、讨论题详解与三重闭环。">
<meta name="color-scheme" content="light dark">
<title>%(title)s · 腓立比书 2:1-18 × 海德堡主日 24</title>
<link rel="icon" href="data:image/svg+xml,%(favicon)s">
<style>%(css)s</style>
</head>
<body>
<div id="bar"><div class="in">
  <button class="btn" id="menu" data-act="menu">☰</button>
  <span class="ttl">%(title)s</span>
  <span class="sp"></span>
  <button class="btn hidesm" data-act="expand">▼ 展开全部问答</button>
  <button class="btn" id="theme" data-act="theme">◑ 跟随</button>
  <button class="btn hidesm" data-act="print">🖨 打印</button>
  <div id="prog"></div>
</div></div>
<div id="scrim"></div>

<div class="wrap">
<nav id="toc">%(toc)s</nav>
<main>
<header class="hero">
  <div class="eyebrow">Continental Reformed Sermon · 主日讲章全解</div>
  <h1>%(title)s</h1>
  <h2 class="sub">%(subtitle)s</h2>
  <div class="meta">
    <span>腓立比书 2:1-18</span><span>海德堡要理问答 主日 24</span>
    <span>问 62 · 63 · 64</span><span>三重闭环</span><span>讨论题详解</span>
  </div>
  <div class="order">
    <h6>崇拜与讲道纲要</h6>
    <dl>%(order)s</dl>
  </div>
</header>
%(main)s
</main>
</div>

<footer>
<p><strong>%(title)s</strong>　·　腓立比书 2:1-18　×　海德堡要理问答主日 24（问 62-64）</p>
<p>体例：欧陆改革宗讲道传统（救赎历史 · 经文 · 要理问答三线合一）。
经文用和合本；希腊文标注仅供查考。本页为纯静态单文件，无外部依赖，可离线保存与打印（A4）。</p>
<p>姊妹站 · 本信经系列：
<a href="https://nicene-creed-reformed.netlify.app">尼西亚信经全解</a> ·
<a href="https://athanasian-creed-reformed.netlify.app">亚他那修信经全解</a> ·
<a href="https://canons-of-dort-reformed.netlify.app">多特信经全解</a> ·
<a href="https://westminster-confession-reformed.netlify.app">威斯敏斯特信条全解</a></p>
<p><button class="btn noprint" data-act="top">↑ 回到顶部</button></p>
</footer>
<script>%(js)s</script>
</body>
</html>
"""

FAVICON = ("%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2064%2064'%3E"
           "%3Crect%20width='64'%20height='64'%20rx='12'%20fill='%231e3a5f'/%3E"
           "%3Ctext%20x='32'%20y='45'%20font-size='38'%20text-anchor='middle'%20"
           "fill='%23c9a33f'%20font-family='serif'%3E%E2%9C%9D%3C/text%3E%3C/svg%3E")


def main():
    order_html = "".join("<dt>%s</dt><dd>%s</dd>" % (esc(k), esc(v)) for k, v in ORDER)
    html = HTML % {
        "title": esc(TITLE), "subtitle": esc(SUBTITLE),
        "css": CSS, "js": JS, "toc": build_toc(), "main": build_main(),
        "order": order_html, "favicon": FAVICON,
    }
    out = os.path.join(os.path.dirname(__file__), "..", "site", "index.html")
    with io.open(out, "w", encoding="utf-8") as f:
        f.write(html)

    payload = {"title": TITLE, "subtitle": SUBTITLE, "order": ORDER,
               "sections": SECTIONS}
    jf = os.path.join(os.path.dirname(__file__), "..", "docx", "content.json")
    with io.open(jf, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)

    size = os.path.getsize(out)
    chars = len(re.findall(r"[\u4e00-\u9fff]", html))
    print("index.html  %.1f KB   中文字符 %d" % (size / 1024.0, chars))
    print("content.json %.1f KB  sections %d" % (os.path.getsize(jf) / 1024.0, len(SECTIONS)))


if __name__ == "__main__":
    main()
