# -*- coding: utf-8 -*-
"""轻量区块 DSL：一份内容，两种渲染（HTML / DOCX-JSON）。"""
import re, html as _h

# ---------- 构造器 ----------
def P(t):                 return {"t": "p", "x": t}
def H3(t, i=None):        return {"t": "h3", "x": t, "id": i}
def H4(t):                return {"t": "h4", "x": t}
def UL(*items):           return {"t": "ul", "items": list(items)}
def OL(*items):           return {"t": "ol", "items": list(items)}
def TB(cap, heads, rows): return {"t": "table", "cap": cap, "heads": heads, "rows": rows}
def SCR(t, src=""):       return {"t": "scr", "x": t, "src": src}
def CAT(t, src=""):       return {"t": "cat", "x": t, "src": src}
def APP(t, src=""):       return {"t": "app", "x": t, "src": src}
def QA(q, a):             return {"t": "qa", "q": q, "a": a}
def FIG(svg, cap, alt=""):return {"t": "fig", "svg": svg, "cap": cap, "alt": alt or cap}
def HR():                 return {"t": "hr"}
def LEAD(t):              return {"t": "lead", "x": t}

def SEC(sid, num, title, blocks, sub=""):
    return {"id": sid, "num": num, "title": title, "sub": sub, "blocks": blocks}

# ---------- 行内标记 ----------
def esc(s):
    return _h.escape(str(s), quote=False)

_B = re.compile(r"\*\*(.+?)\*\*")
_K = re.compile(r"\{\{(.+?)\}\}")      # 关键词高亮
_G = re.compile(r"\[\[(.+?)\]\]")      # 希腊文 / 拉丁文
_R = re.compile(r"\(\((.+?)\)\)")      # 经文出处小字

def inline(s):
    s = esc(s)
    s = _B.sub(r"<strong>\1</strong>", s)
    s = _K.sub(r'<em class="kw">\1</em>', s)
    s = _G.sub(r'<span class="gk">\1</span>', s)
    s = _R.sub(r'<span class="ref">\1</span>', s)
    return s

_FIGN = [0]
_SVGID = re.compile(r'\bid="([A-Za-z][\w-]*)"')

def prep_svg(svg):
    """去掉 SVG 里的 [[..]] 标记；并把内部 id 加后缀，避免同一张图重复插入时 id 冲突。"""
    _FIGN[0] += 1
    n = _FIGN[0]
    svg = _G.sub(r"\1", svg)
    names = set(_SVGID.findall(svg))
    for nm in names:
        svg = svg.replace('id="%s"' % nm, 'id="%s-f%d"' % (nm, n))
        svg = svg.replace('url(#%s)' % nm, 'url(#%s-f%d)' % (nm, n))
    return svg

# ---------- HTML 渲染 ----------
def render_blocks(blocks):
    out = []
    for b in blocks:
        t = b["t"]
        if t == "p":
            out.append("<p>%s</p>" % inline(b["x"]))
        elif t == "lead":
            out.append('<p class="lead">%s</p>' % inline(b["x"]))
        elif t == "h3":
            i = ' id="%s"' % b["id"] if b.get("id") else ""
            out.append("<h3%s>%s</h3>" % (i, inline(b["x"])))
        elif t == "h4":
            out.append("<h4>%s</h4>" % inline(b["x"]))
        elif t == "ul":
            out.append("<ul>%s</ul>" % "".join("<li>%s</li>" % inline(x) for x in b["items"]))
        elif t == "ol":
            out.append("<ol>%s</ol>" % "".join("<li>%s</li>" % inline(x) for x in b["items"]))
        elif t == "table":
            th = "".join("<th>%s</th>" % inline(x) for x in b["heads"])
            tr = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c) for c in r) for r in b["rows"])
            cap = '<caption>%s</caption>' % inline(b["cap"]) if b["cap"] else ""
            out.append('<div class="tablewrap"><table>%s<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
                       % (cap, th, tr))
        elif t in ("scr", "cat", "app"):
            cls = {"scr": "box scr", "cat": "box cat", "app": "box app"}[t]
            lbl = {"scr": "经", "cat": "问", "app": "用"}[t]
            src = '<span class="bsrc">%s</span>' % inline(b["src"]) if b.get("src") else ""
            out.append('<div class="%s"><span class="blab">%s</span>%s%s</div>'
                       % (cls, lbl, inline(b["x"]), src))
        elif t == "qa":
            out.append('<details class="qa"><summary>%s</summary><div class="qa-a">%s</div></details>'
                       % (inline(b["q"]), inline(b["a"])))
        elif t == "fig":
            b["n"] = _FIGN[0] + 1
            out.append('<figure class="fig">%s<figcaption>%s</figcaption></figure>'
                       % (prep_svg(b["svg"]), inline(b["cap"])))
        elif t == "hr":
            out.append('<hr class="rule">')
    return "\n".join(out)
