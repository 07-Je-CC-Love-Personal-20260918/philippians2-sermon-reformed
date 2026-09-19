# -*- coding: utf-8 -*-
import asyncio, sys
from playwright.async_api import async_playwright

URL = "http://127.0.0.1:8901/index.html"
WIDTHS = [320, 360, 390, 414, 480, 560, 768, 820, 1024, 1280, 1440, 1920]
ok = True


def chk(c, m):
    global ok
    print(("  ✓ " if c else "  ✗ ") + m)
    if not c:
        ok = False


async def main():
    global ok
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        errs = []
        print("── 横向溢出 / JS 错误 ──")
        for w in WIDTHS:
            pg = await b.new_page(viewport={"width": w, "height": 900})
            pg.on("pageerror", lambda e: errs.append(str(e)))
            pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
            await pg.goto(URL, wait_until="load")
            await pg.wait_for_timeout(250)
            over = await pg.evaluate(
                "()=>Math.max(0, document.documentElement.scrollWidth - window.innerWidth)")
            wide = await pg.evaluate("""()=>{
                const bad=[]; document.querySelectorAll('main *').forEach(el=>{
                  const r=el.getBoundingClientRect();
                  if(r.right>window.innerWidth+1.5 && el.offsetParent!==null &&
                     !el.closest('.tablewrap') && !el.closest('figure.fig'))
                    bad.push(el.tagName+'.'+(el.className||'').toString().slice(0,24));
                }); return bad.slice(0,4);}""")
            chk(over == 0 and not wide, "%4dpx 溢出 %s %s" % (w, over, wide or ""))
            await pg.close()
        chk(not errs, "无 JS 错误 %s" % (errs[:3] or ""))

        pg = await b.new_page(viewport={"width": 1440, "height": 900})
        await pg.goto(URL, wait_until="load")
        await pg.add_style_tag(content="html{scroll-behavior:auto!important}")

        print("── 目录滚动高亮 ──")
        ids = await pg.evaluate(
            "()=>[...document.querySelectorAll('nav#toc a')].map(a=>a.getAttribute('href').slice(1))")
        hit = 0
        test = ids[::5]
        for i in test:
            await pg.evaluate(
                "id=>document.getElementById(id).scrollIntoView({behavior:'instant',block:'start'})", i)
            await pg.wait_for_timeout(140)
            on = await pg.evaluate(
                "()=>{const a=document.querySelector('nav#toc a.on');return a?a.getAttribute('href').slice(1):null}")
            if on == i:
                hit += 1
            else:
                print("     miss %s -> %s" % (i, on))
        chk(hit == len(test), "高亮命中 %d/%d" % (hit, len(test)))

        print("── 交互 ──")
        await pg.evaluate("()=>window.scrollTo(0,0)")
        await pg.click('[data-act="theme"]')
        t1 = await pg.evaluate("()=>document.documentElement.getAttribute('data-theme')")
        await pg.click('[data-act="theme"]')
        t2 = await pg.evaluate("()=>document.documentElement.getAttribute('data-theme')")
        await pg.click('[data-act="theme"]')
        t3 = await pg.evaluate("()=>document.documentElement.getAttribute('data-theme')")
        chk([t1, t2, t3] == ["light", "dark", None], "主题三态循环 %s" % [t1, t2, t3])

        await pg.click('[data-act="expand"]')
        opened = await pg.evaluate(
            "()=>[...document.querySelectorAll('details.qa')].filter(d=>d.open).length")
        total = await pg.evaluate("()=>document.querySelectorAll('details.qa').length")
        chk(opened == total, "展开全部问答 %d/%d" % (opened, total))
        await pg.click('[data-act="expand"]')
        closed = await pg.evaluate(
            "()=>[...document.querySelectorAll('details.qa')].filter(d=>!d.open).length")
        chk(closed == total, "收起全部问答 %d/%d" % (closed, total))

        prog = await pg.evaluate("""async()=>{window.scrollTo(0,document.body.scrollHeight);
            await new Promise(r=>setTimeout(r,400));
            return parseFloat(document.getElementById('prog').style.width)}""")
        chk(prog > 90, "阅读进度条 %.0f%%" % prog)

        print("── SVG 文字出框 ──")
        outside = await pg.evaluate("""()=>{const bad=[];
            document.querySelectorAll('figure.fig svg').forEach((s,i)=>{
              const vb=s.viewBox.baseVal;
              s.querySelectorAll('text').forEach(t=>{
                const bb=t.getBBox();
                if(bb.x< -2 || bb.y< -2 || bb.x+bb.width>vb.width+2 || bb.y+bb.height>vb.height+2)
                  bad.push('fig'+(i+1)+':'+t.textContent.slice(0,14));});});
            return bad;}""")
        chk(not outside, "13 幅图文字零出框 %s" % (outside[:5] or ""))

        print("── 移动端抽屉 ──")
        mp = await b.new_page(viewport={"width": 390, "height": 844})
        await mp.goto(URL, wait_until="load")
        await mp.click("#menu")
        await mp.wait_for_timeout(300)
        chk(await mp.evaluate("()=>document.getElementById('toc').classList.contains('open')"), "抽屉打开")
        await mp.keyboard.press("Escape")
        await mp.wait_for_timeout(300)
        chk(not await mp.evaluate("()=>document.getElementById('toc').classList.contains('open')"),
            "Esc 关闭抽屉")
        await mp.close()

        print("── 打印 ──")
        await pg.emulate_media(media="print")
        await pg.wait_for_timeout(200)
        hid = await pg.evaluate("""()=>getComputedStyle(document.getElementById('toc')).display"""
                                )
        chk(hid == "none", "打印时隐藏侧栏目录 (%s)" % hid)
        await pg.emulate_media(media="screen")

        await b.close()
    print()
    print("浏览器测试：" + ("全部通过 ✓" if ok else "存在问题 ✗"))
    sys.exit(0 if ok else 1)

asyncio.run(main())
