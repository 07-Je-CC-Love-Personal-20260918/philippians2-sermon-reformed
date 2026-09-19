# -*- coding: utf-8 -*-
import re, io, sys, collections

p = "/home/claude/php2/site/index.html"
h = io.open(p, encoding="utf-8").read()
ok = True

def chk(cond, msg):
    global ok
    print(("  ✓ " if cond else "  ✗ ") + msg)
    if not cond:
        ok = False

print("── 锚点 ──")
ids = re.findall(r'\sid="([^"]+)"', h)
dup = [k for k, v in collections.Counter(ids).items() if v > 1]
anchors = sorted(set(re.findall(r'href="#([^"]+)"', h)))
missing = [a for a in anchors if a not in ids]
chk(not dup, "ID 无重复（共 %d 个）%s" % (len(ids), dup or ""))
chk(not missing, "目录锚点全部有效（%d/%d）%s" % (len(anchors) - len(missing), len(anchors), missing or ""))

print("── 标签平衡 ──")
for tag in ["div", "section", "nav", "main", "header", "footer", "table", "thead", "tbody",
            "tr", "td", "th", "ul", "ol", "li", "p", "details", "summary", "figure",
            "figcaption", "svg", "h2", "h3", "h4", "strong", "em", "span", "dl", "dt", "dd",
            "caption", "button", "a"]:
    o = len(re.findall(r"<%s[\s>]" % tag, h))
    c = len(re.findall(r"</%s>" % tag, h))
    chk(o == c, "<%s> %d / %d" % (tag, o, c))

print("── 结构计数 ──")
print("  section.part = %d" % len(re.findall(r'<section class="part"', h)))
print("  h3           = %d" % len(re.findall(r"<h3", h)))
print("  table        = %d" % len(re.findall(r"<table", h)))
print("  svg          = %d" % len(re.findall(r"<svg", h)))
print("  details.qa   = %d" % len(re.findall(r'<details class="qa"', h)))
print("  经文框/要理框/应用框 = %d / %d / %d" % (
    len(re.findall(r'class="box scr"', h)), len(re.findall(r'class="box cat"', h)),
    len(re.findall(r'class="box app"', h))))

print("── 外部依赖 ──")
ext = re.findall(r'(?:src|href)="(https?://[^"]+)"', h)
bad = [u for u in ext if "netlify.app" not in u]
chk(not bad, "无外部资源引用（仅姊妹站超链接 %d 条）%s" % (len(ext), bad or ""))
chk("fonts.googleapis" not in h, "未引用 Google Fonts")

print("── 内容完整性 ──")
chk("恐惧战兢，作成你们得救的工夫" in h, "主题经文在页内")
chk(h.count("κατεργάζ") >= 5, "κατεργάζομαι 出现 %d 次" % h.count("κατεργάζ"))
for q in ["62", "63", "64"]:
    chk(("海德堡 %s" % q) in h or ("问 %s" % q) in h, "海德堡问 %s 出现" % q)
for k in ["讨论题一", "讨论题二", "讨论题三", "讨论题四", "讨论题五"]:
    chk(k in h, k)
for k in ["闭环一", "闭环二", "闭环三"]:
    chk(k in h, k)

print("── 残留标记 ──")
for mk, name in [(r"\*\*", "**bold**"), (r"\{\{", "{{kw}}"), (r"\[\[", "[[gk]]"), (r"\(\(", "((ref))")]:
    n = len(re.findall(mk, h))
    chk(n == 0, "无未解析的 %s 标记（残留 %d）" % (name, n))

print("── SVG 规范 ──")
chk("<b>" not in h, "SVG/正文中无裸 <b> 标签")
svgtxt = re.findall(r"<text[^>]*>(.*?)</text>", h, re.S)
chk(all("<b" not in t for t in svgtxt), "SVG <text> 内无 <b>")

print()
print("总体：" + ("全部通过 ✓" if ok else "存在问题 ✗"))
sys.exit(0 if ok else 1)
