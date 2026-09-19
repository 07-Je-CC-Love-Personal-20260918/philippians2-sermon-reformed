# -*- coding: utf-8 -*-
CSS = r"""
:root{
  --bg:#f6f1e4; --bg2:#fbf8f0; --card:#fffdf7; --ink:#241f1a; --ink2:#4a4138;
  --muted:#7b6f61; --line:#ddd2bc; --line2:#eae0cc;
  --navy:#1e3a5f; --navy2:#2d5586; --crimson:#8c2f39; --gold:#a5812a; --gold2:#c9a33f;
  --teal:#1f5f5b; --plum:#5b3a6e; --sel:#f2e3b8;
  --shadow:0 1px 2px rgba(60,45,20,.06),0 8px 24px rgba(60,45,20,.06);
  --mono:ui-monospace,"SFMono-Regular",Menlo,Consolas,monospace;
  --serif:"Songti SC","Noto Serif CJK SC","Source Han Serif SC","Noto Serif SC",
          "SimSun","STSong","PingFang SC","Microsoft YaHei",serif;
  --sans:"PingFang SC","Hiragino Sans GB","Microsoft YaHei","Noto Sans CJK SC",system-ui,sans-serif;
  --west:"EB Garamond","Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif;
  --maxw:1320px;
}
html[data-theme="dark"]{
  --bg:#14120f; --bg2:#1a1713; --card:#1f1b16; --ink:#ece4d6; --ink2:#cfc4b2;
  --muted:#9b8f7d; --line:#3a3227; --line2:#2b251d;
  --navy:#7fb0e6; --navy2:#a8c9f0; --crimson:#e0868f; --gold:#d8b25a; --gold2:#eccb7d;
  --teal:#6fc4be; --plum:#bb96d2; --sel:#4a3d1c;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 30px rgba(0,0,0,.35);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:74px;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--serif);
  font-size:17px;line-height:1.95;letter-spacing:.012em;
  background-image:radial-gradient(circle at 12% 8%,rgba(165,129,42,.055),transparent 45%),
                   radial-gradient(circle at 88% 92%,rgba(30,58,95,.05),transparent 42%);
  background-attachment:fixed;}
::selection{background:var(--sel)}
a{color:var(--navy);text-underline-offset:3px;text-decoration-thickness:.06em}
a:hover{color:var(--crimson)}
.gk{font-family:var(--west);font-style:italic;color:var(--navy2);letter-spacing:.01em}
.kw{font-style:normal;font-weight:700;color:var(--crimson);
    background:linear-gradient(transparent 62%,rgba(165,129,42,.22) 62%)}
.ref{font-size:.82em;color:var(--muted);white-space:nowrap}
strong{color:var(--ink);font-weight:700}

/* 顶栏 */
#bar{position:sticky;top:0;z-index:60;background:color-mix(in srgb,var(--bg2) 92%,transparent);
  backdrop-filter:saturate(1.3) blur(10px);border-bottom:1px solid var(--line);}
#bar .in{max-width:var(--maxw);margin:0 auto;padding:9px 18px;display:flex;align-items:center;gap:12px}
#bar .ttl{font-weight:700;font-size:15.5px;letter-spacing:.04em;color:var(--navy);
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#bar .sp{flex:1}
.btn{font-family:var(--sans);font-size:12.5px;line-height:1;padding:8px 11px;border-radius:8px;
  border:1px solid var(--line);background:var(--card);color:var(--ink2);cursor:pointer;
  white-space:nowrap;transition:.15s}
.btn:hover{border-color:var(--gold);color:var(--gold)}
#prog{position:absolute;left:0;bottom:-1px;height:2px;width:0;
  background:linear-gradient(90deg,var(--gold),var(--crimson));transition:width .1s linear}
#menu{display:none}

/* 布局 */
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 18px 90px;
  display:grid;grid-template-columns:284px minmax(0,1fr);gap:40px;align-items:start}
nav#toc{position:sticky;top:64px;max-height:calc(100vh - 82px);overflow:auto;
  padding:16px 8px 30px 0;font-family:var(--sans);font-size:13.2px;line-height:1.55}
nav#toc h5{margin:0 0 10px;font-size:11px;letter-spacing:.22em;color:var(--muted);
  font-weight:600;text-transform:uppercase}
nav#toc a{display:block;padding:4.5px 10px;border-radius:7px;color:var(--ink2);
  text-decoration:none;border-left:2px solid transparent}
nav#toc a.l1{font-weight:600;margin-top:7px;color:var(--ink)}
nav#toc a.l2{padding-left:20px;font-size:12.4px;color:var(--muted)}
nav#toc a:hover{background:color-mix(in srgb,var(--gold) 12%,transparent);color:var(--ink)}
nav#toc a.on{background:color-mix(in srgb,var(--gold) 18%,transparent);
  border-left-color:var(--gold);color:var(--crimson);font-weight:700}
main{min-width:0}

/* 题头 */
header.hero{padding:54px 0 26px;border-bottom:2px solid var(--line);margin-bottom:8px}
header.hero .eyebrow{font-family:var(--sans);font-size:11.5px;letter-spacing:.34em;
  color:var(--gold);text-transform:uppercase;margin-bottom:16px}
header.hero h1{font-size:clamp(27px,5.2vw,42px);line-height:1.38;margin:0 0 10px;
  color:var(--navy);letter-spacing:.02em;font-weight:700}
header.hero h2.sub{font-size:clamp(15px,2.6vw,19px);font-weight:400;color:var(--ink2);
  margin:0 0 22px;line-height:1.7}
.meta{display:flex;flex-wrap:wrap;gap:8px;font-family:var(--sans);font-size:12.2px}
.meta span{padding:4px 11px;border:1px solid var(--line);border-radius:999px;
  background:var(--card);color:var(--muted)}
.order{margin:26px 0 4px;padding:18px 20px;border:1px solid var(--line);border-radius:12px;
  background:var(--card);box-shadow:var(--shadow)}
.order h6{margin:0 0 10px;font-family:var(--sans);font-size:11.5px;letter-spacing:.2em;
  color:var(--gold);font-weight:600}
.order dl{margin:0;display:grid;grid-template-columns:auto 1fr;gap:5px 16px;font-size:15.2px}
.order dt{color:var(--muted);white-space:nowrap;font-family:var(--sans);font-size:13px}
.order dd{margin:0;color:var(--ink2)}

/* 章节 */
section.part{padding:40px 0 6px}
section.part>h2{font-size:clamp(21px,3.6vw,27px);color:var(--crimson);margin:0 0 6px;
  padding-bottom:10px;border-bottom:1px solid var(--line);letter-spacing:.02em}
section.part>h2 .n{font-family:var(--west);font-size:.72em;color:var(--gold);margin-right:.5em;
  letter-spacing:.06em}
section.part>.psub{font-family:var(--sans);font-size:13px;color:var(--muted);margin:0 0 20px}
h3{font-size:clamp(17.5px,2.8vw,20.5px);color:var(--navy);margin:34px 0 12px;
  padding-left:13px;border-left:4px solid var(--gold);line-height:1.55}
h4{font-size:16.4px;color:var(--ink);margin:24px 0 8px;font-weight:700}
h4::before{content:"◆ ";color:var(--gold2);font-size:.8em}
p{margin:0 0 15px;text-align:justify}
p.lead{font-size:18px;color:var(--ink2);border-left:3px solid var(--line);padding-left:16px;
  font-style:normal}
ul,ol{margin:0 0 16px;padding-left:1.45em}
li{margin:0 0 7px;text-align:justify}
li::marker{color:var(--gold)}
hr.rule{border:0;height:1px;background:linear-gradient(90deg,transparent,var(--line),transparent);
  margin:32px 0}

/* 框 */
.box{position:relative;margin:20px 0;padding:16px 20px 16px 22px;border-radius:0 11px 11px 0;
  background:var(--card);box-shadow:var(--shadow);font-size:16.3px;line-height:1.85}
.box .blab{position:absolute;left:-1px;top:-1px;transform:translateX(-100%);
  writing-mode:vertical-rl;font-family:var(--sans);font-size:10.5px;letter-spacing:.2em;
  padding:6px 3px;border-radius:7px 0 0 7px;color:#fff}
.box .bsrc{display:block;margin-top:8px;font-family:var(--sans);font-size:12.4px;
  color:var(--muted);text-align:right}
.box.scr{border-left:4px solid var(--gold)}    .box.scr .blab{background:var(--gold)}
.box.cat{border-left:4px solid var(--navy)}    .box.cat .blab{background:var(--navy)}
.box.app{border-left:4px solid var(--crimson)} .box.app .blab{background:var(--crimson)}
@media(max-width:820px){.box .blab{display:none}}

/* 启发式问答 */
details.qa{margin:16px 0;border:1px solid var(--line);border-radius:11px;background:var(--card);
  overflow:hidden;box-shadow:var(--shadow)}
details.qa>summary{cursor:pointer;list-style:none;padding:13px 17px 13px 44px;position:relative;
  font-weight:700;color:var(--navy);font-size:16px;line-height:1.7}
details.qa>summary::-webkit-details-marker{display:none}
details.qa>summary::before{content:"?";position:absolute;left:15px;top:14px;width:19px;height:19px;
  border-radius:50%;background:var(--gold);color:#fff;font-family:var(--west);font-size:12.5px;
  font-weight:700;display:flex;align-items:center;justify-content:center}
details.qa[open]>summary{border-bottom:1px dashed var(--line);color:var(--crimson)}
details.qa .qa-a{padding:14px 17px 15px;font-size:16px;color:var(--ink2);
  background:color-mix(in srgb,var(--gold) 5%,transparent)}

/* 表格 */
.tablewrap{margin:22px 0;overflow-x:auto;border:1px solid var(--line);border-radius:11px;
  background:var(--card);box-shadow:var(--shadow);-webkit-overflow-scrolling:touch}
table{border-collapse:collapse;width:100%;min-width:520px;font-size:14.9px;line-height:1.7}
caption{caption-side:top;text-align:left;padding:12px 16px 8px;font-family:var(--sans);
  font-size:12.6px;color:var(--muted);letter-spacing:.04em}
thead th{background:var(--navy);color:#fff;font-weight:600;text-align:left;padding:10px 13px;
  font-size:14px;letter-spacing:.03em;position:sticky;top:0}
html[data-theme="dark"] thead th{background:#24384f;color:#f0e8d8}
tbody td{padding:9px 13px;border-top:1px solid var(--line2);vertical-align:top}
tbody tr:nth-child(even){background:color-mix(in srgb,var(--gold) 5%,transparent)}
tbody tr:hover{background:color-mix(in srgb,var(--gold) 11%,transparent)}
td strong{color:var(--crimson)}

/* 图 */
figure.fig{margin:26px 0;padding:18px 14px 10px;border:1px solid var(--line);border-radius:12px;
  background:var(--card);box-shadow:var(--shadow);overflow-x:auto}
figure.fig svg{display:block;width:100%;height:auto;max-width:100%;min-width:0}
figcaption{margin-top:10px;font-family:var(--sans);font-size:12.5px;color:var(--muted);
  text-align:center;line-height:1.6}
svg text{font-family:var(--sans)}

/* 底 */
footer{max-width:var(--maxw);margin:0 auto;padding:34px 18px 70px;border-top:1px solid var(--line);
  font-family:var(--sans);font-size:12.8px;color:var(--muted);line-height:1.9}
footer a{color:var(--navy)}

/* 移动端 */
#scrim{display:none;position:fixed;inset:0;background:rgba(20,15,8,.45);z-index:70}
@media(max-width:980px){
  body{font-size:16.4px}
  .wrap{grid-template-columns:1fr;gap:0;padding:0 15px 70px}
  #menu{display:inline-block}
  nav#toc{position:fixed;left:0;top:0;bottom:0;width:min(85vw,330px);z-index:80;
    background:var(--bg2);border-right:1px solid var(--line);padding:18px 12px 40px;
    transform:translateX(-102%);transition:transform .22s ease;max-height:none;
    box-shadow:0 0 40px rgba(0,0,0,.25)}
  nav#toc.open{transform:none}
  header.hero{padding:34px 0 22px}
  .order dl{grid-template-columns:1fr;gap:2px}
  .order dt{margin-top:8px}
}
@media(max-width:480px){
  body{font-size:16px;line-height:1.9}
  .box{padding:14px 15px}
  #bar .ttl{font-size:13.5px}
  .btn{padding:7px 9px;font-size:12px}
  .hidesm{display:none}
}

/* 打印 */
@media print{
  :root{--bg:#fff;--bg2:#fff;--card:#fff;--ink:#000;--ink2:#1a1a1a;--line:#bbb;--line2:#ddd;
        --shadow:none}
  body{font-size:10.6pt;line-height:1.7;background:none}
  #bar,nav#toc,#scrim,.noprint{display:none!important}
  .wrap{display:block;max-width:none;padding:0}
  section.part{page-break-before:always;padding-top:0}
  section.part:first-of-type{page-break-before:avoid}
  h3,h4,figure.fig,.tablewrap,.box{page-break-inside:avoid}
  details.qa{border:1px solid #bbb}
  details.qa .qa-a{display:block!important}
  a{color:#000;text-decoration:none}
  thead th{background:#26415f!important;-webkit-print-color-adjust:exact;print-color-adjust:exact}
  @page{size:A4;margin:16mm 14mm}
}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}
  html{scroll-behavior:auto}}
"""
