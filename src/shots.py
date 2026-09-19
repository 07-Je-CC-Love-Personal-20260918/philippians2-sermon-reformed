# -*- coding: utf-8 -*-
import asyncio, os, json
from playwright.async_api import async_playwright
OUT = "/home/claude/php2/docx/img"
os.makedirs(OUT, exist_ok=True)
async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch()
        pg = await b.new_page(viewport={"width": 1500, "height": 1000}, device_scale_factor=2)
        await pg.goto("http://127.0.0.1:8901/index.html", wait_until="load")
        await pg.evaluate("()=>document.documentElement.setAttribute('data-theme','light')")
        await pg.add_style_tag(content="figure.fig{border:0;box-shadow:none;background:#fff;padding:6px}"
                                       "figure.fig figcaption{display:none}")
        figs = await pg.query_selector_all("figure.fig")
        meta = []
        for i, f in enumerate(figs, 1):
            path = os.path.join(OUT, "fig%d.png" % i)
            await f.screenshot(path=path)
            box = await f.bounding_box()
            meta.append({"n": i, "w": box["width"], "h": box["height"]})
            print("fig%d  %.0fx%.0f" % (i, box["width"], box["height"]))
        json.dump(meta, open(os.path.join(OUT, "meta.json"), "w"))
        await b.close()
asyncio.run(main())
