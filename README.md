# 当存敬畏战兢的心作成得救的工夫

**腓立比书 2:1-18　×　海德堡要理问答 主日 24（问 62-64）　·　欧陆改革宗式讲章全解**

- 要点一　因神在你心里运行
- 要点二　为要成就他的美意

## 在线阅读

| 部署 | 链接 |
|---|---|
| Netlify | https://philippians2-sermon-reformed.netlify.app |
| GitHub Pages | https://07-je-cc-love-personal-20260918.github.io/philippians2-sermon-reformed/ |

## 内容结构（十三部 + 附录，81 个目录锚点）

| 部 | 标题 | 核心内容 |
|---|---|---|
| 序 | 怎样读这一讲 | 三条线索；两种致命误引 |
| 一 | 全景 | 神做工／人做工的四种排列；救赎历史七幕坐标；三项合一信条对照 |
| 二 | 情境 | 腓立比城档案；徒 16 三个人；罗马狱中；四重压力；1563 海德堡与特伦特对照 |
| 三 | 脉络 | 段落真正起点在 1:27；同心圆结构；三个关键连接词；基督颂的性质 |
| 四 | 逐节 | 2:1-18 全覆盖，九个语义单元 |
| 五 | **讲章** | 引言 · 第一要点 · 第二要点 · 教训/责备/安慰/劝勉四重应用 · 结语 |
| 六 | 字义 | κατεργάζομαι／ἐνεργέω／εὐδοκία／φόβος καὶ τρόμος 完整用法表 |
| 七 | 主日 24 | 问 62、63、64 逐问：骨架 · 经文 · 对手 · 与腓 2 的接点 |
| 八 | 跨经专题 | 主权与责任；称义与成圣；保罗与雅各；三重归算；确据；十个常见误读 |
| 九 | 拓展 | 2:19-30；3:4-14；4:2-3；虚己论与 extra Calvinisticum；三大信经；平行经文十处 |
| 十 | **讨论题详解** | 五题全解：题意辨析 · 分层答案 · 常见偏差 · 一句话总结 |
| 十一 | **三重闭环** | 救赎历史·圣约 ／ 经文·圣经神学 ／ 罪-救赎-感恩 |
| 十二 | 应用与操练 | 五种处境；一周操练表；记忆钩子与背诵卡 |
| 附 | 附录 | 经文全文 · 主日 24 全文 · 30 条术语表 · 信条索引 · 延伸阅读 · 结构一览 |

统计：14 个 section · 67 个二级标题 · 62 张表 · 13 幅手写 SVG · 17 组启发式问答 · 约 4 万中文字。

## 目录结构

```
src/          Python 内容与渲染模块（唯一真源）
  dsl.py        区块 DSL：一份内容 → HTML + DOCX-JSON
  css.py js.py  样式与脚本
  charts.py     13 幅手写 SVG（CSS 变量着色，双主题自适应）
  part1..part7  内容模块
  build.py      装配 → site/index.html + docx/content.json
  validate.py   静态校验（锚点、ID、标签平衡、残留标记）
  browser_test.py  Playwright：12 档溢出、目录高亮、交互、打印
  shots.py      把 13 幅 SVG 截成 PNG 供 DOCX 使用
site/         Netlify 部署目录（单文件 index.html + netlify.toml）
docs/         GitHub Pages 部署目录（index.html 副本）
docx/         render.js（docx@9）+ content.json + img/ + 成品 .docx
```

## 重新构建

```bash
cd src && python3 build.py          # 生成 site/index.html 与 docx/content.json
python3 validate.py                 # 静态校验
cd ../site && python3 -m http.server 8901 &
cd ../src && python3 browser_test.py && python3 shots.py
cd ../docx && node render.js        # 生成 Word 文档
cp ../site/index.html ../docs/index.html   # 同步 GitHub Pages
```

## 技术要点

- 单文件纯静态，**零外部资源**（仅四条姊妹站超链接）；系统中文字体栈，不引用 Google Fonts
- 明 / 暗 / 跟随系统三态主题，localStorage 记忆；所有 SVG 用 CSS 变量着色
- 目录滚动高亮用 **rAF + getBoundingClientRect**（勿用 IntersectionObserver）
- 注意：`scroll-padding-top` 与 `scroll-margin-top` 会**叠加**，两者同时设置会让目录高亮整体偏前一格
- SVG `<text>` 内不可用 HTML 的 `<b>`，加粗须用 `<tspan style="font-weight:700">`
- 同一张 SVG 多处复用时，内部 `marker` 的 `id` 必须加后缀，否则 HTML 出现重复 ID
- DOCX：docx@9；`spacing.line` 必须同时给 `lineRule: AUTO`，否则 LibreOffice 会把内嵌图片压成一条细线
- 校验：静态 81/81 锚点、标签全平衡；浏览器 12 档（320→1920）零横向溢出、零 JS 错误、目录高亮 17/17、13 幅图文字零出框

## 姊妹站

- 尼西亚信经全解 https://nicene-creed-reformed.netlify.app
- 亚他那修信经全解 https://athanasian-creed-reformed.netlify.app
- 多特信经全解 https://canons-of-dort-reformed.netlify.app
- 威斯敏斯特信条全解 https://westminster-confession-reformed.netlify.app
