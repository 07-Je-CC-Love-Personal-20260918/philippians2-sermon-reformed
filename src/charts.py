# -*- coding: utf-8 -*-
"""全部图形手写 SVG，颜色一律走 CSS 变量，明暗主题自动适配。
   注意：SVG 的 <text> 内不可使用 HTML 的 <b>，加粗一律用 <tspan style="font-weight:700">。"""

HEAD = ('<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" '
        'aria-label="{alt}" style="min-width:{mw}px">')

def _s(w, h, alt, mw=640):
    return HEAD.format(w=w, h=h, alt=alt, mw=mw)

# ---------------------------------------------------------------- 1 全书结构
FIG_LETTER = _s(880, 330, "腓立比书全书结构与 1:27-2:18 的位置", 700) + """
<defs><marker id="ar1" markerWidth="9" markerHeight="7" refX="8" refY="3.5" orient="auto">
<path d="M0,0 L9,3.5 L0,7 z" fill="var(--gold)"/></marker></defs>
<text x="440" y="26" text-anchor="middle" font-size="15" font-weight="700" fill="var(--crimson)">腓立比书：一封「谢函—遗嘱—劝勉」三合一的狱中书信</text>
<rect x="24" y="48" width="150" height="62" rx="9" fill="none" stroke="var(--line)" stroke-width="1.5"/>
<text x="99" y="72" text-anchor="middle" font-size="13" font-weight="700" fill="var(--navy)">一 1:1-26</text>
<text x="99" y="92" text-anchor="middle" font-size="11.5" fill="var(--ink2)">问安·感恩·囚禁使</text>
<text x="99" y="106" text-anchor="middle" font-size="11.5" fill="var(--ink2)">福音兴旺</text>

<rect x="186" y="40" width="330" height="78" rx="9" fill="var(--sel)" stroke="var(--gold)" stroke-width="2.5"/>
<text x="351" y="64" text-anchor="middle" font-size="13.5" font-weight="700" fill="var(--crimson)">二 1:27-2:18　本讲经文所在的完整段落</text>
<text x="351" y="84" text-anchor="middle" font-size="11.5" fill="var(--ink2)">「行事为人与基督的福音相称」——</text>
<text x="351" y="100" text-anchor="middle" font-size="11.5" fill="var(--ink2)">合一的命令 → 基督的心 → 作成得救的工夫</text>

<rect x="528" y="48" width="150" height="62" rx="9" fill="none" stroke="var(--line)" stroke-width="1.5"/>
<text x="603" y="72" text-anchor="middle" font-size="13" font-weight="700" fill="var(--navy)">三 2:19-30</text>
<text x="603" y="92" text-anchor="middle" font-size="11.5" fill="var(--ink2)">提摩太·以巴弗提</text>
<text x="603" y="106" text-anchor="middle" font-size="11.5" fill="var(--ink2)">两个活标本</text>

<rect x="690" y="48" width="166" height="62" rx="9" fill="none" stroke="var(--line)" stroke-width="1.5"/>
<text x="773" y="72" text-anchor="middle" font-size="13" font-weight="700" fill="var(--navy)">四 3:1-4:23</text>
<text x="773" y="92" text-anchor="middle" font-size="11.5" fill="var(--ink2)">保罗的「虚己」·警戒</text>
<text x="773" y="106" text-anchor="middle" font-size="11.5" fill="var(--ink2)">友阿爹循都基·谢函</text>

<path d="M99 118 L99 150 L351 150" fill="none" stroke="var(--gold)" stroke-width="1.6" stroke-dasharray="4 4"/>
<path d="M603 118 L603 150 L351 150" fill="none" stroke="var(--gold)" stroke-width="1.6" stroke-dasharray="4 4"/>
<path d="M773 118 L773 166 L351 166 L351 152" fill="none" stroke="var(--gold)" stroke-width="1.6" stroke-dasharray="4 4" marker-end="url(#ar1)"/>

<rect x="140" y="182" width="600" height="46" rx="9" fill="none" stroke="var(--navy)" stroke-width="1.8"/>
<text x="440" y="203" text-anchor="middle" font-size="13" font-weight="700" fill="var(--navy)">全书的重心：2:6-11 基督颂（Carmen Christi）</text>
<text x="440" y="220" text-anchor="middle" font-size="11.5" fill="var(--ink2)">前后每一段都在围着它转——它不是插曲，是全书的心脏</text>

<text x="440" y="258" text-anchor="middle" font-size="12" fill="var(--muted)">写信人：被囚的保罗（罗马，约主后 60-62 年）　收信人：马其顿的罗马殖民城腓立比的教会</text>
<text x="440" y="278" text-anchor="middle" font-size="12" fill="var(--muted)">直接诱因：以巴弗提送来捐项、又病几乎死去；教会内有裂痕（4:2），外有逼迫（1:28-30），周边有犹太派（3:2）</text>
<line x1="140" y1="294" x2="740" y2="294" stroke="var(--line)" stroke-width="1"/>
<text x="440" y="314" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--crimson)">一句话概括：教会不合一的病，保罗没有开「相处技巧」的药，他开的是「基督论」。</text>
</svg>"""

# ---------------------------------------------------------------- 2 降卑升高
FIG_ARC = _s(880, 430, "腓立比书 2:6-11 降卑与升高的抛物线", 680) + """
<defs><marker id="ar2" markerWidth="9" markerHeight="7" refX="8" refY="3.5" orient="auto">
<path d="M0,0 L9,3.5 L0,7 z" fill="var(--crimson)"/></marker>
<marker id="ar3" markerWidth="9" markerHeight="7" refX="8" refY="3.5" orient="auto">
<path d="M0,0 L9,3.5 L0,7 z" fill="var(--gold)"/></marker></defs>
<text x="440" y="24" text-anchor="middle" font-size="15" font-weight="700" fill="var(--crimson)">V 字形：七级下降　→　三级上升</text>
<line x1="60" y1="60" x2="820" y2="60" stroke="var(--line)" stroke-dasharray="5 5"/>
<text x="64" y="52" font-size="11.5" fill="var(--muted)">神的形像／与神同等（永恒的荣耀）</text>
<line x1="60" y1="330" x2="820" y2="330" stroke="var(--line)" stroke-dasharray="5 5"/>
<text x="64" y="348" font-size="11.5" fill="var(--muted)">十字架的死——奴隶的刑罚，罗马公民不得受</text>

<path d="M120 62 Q 300 200 430 328" fill="none" stroke="var(--crimson)" stroke-width="2.4" marker-end="url(#ar2)"/>
<path d="M450 328 Q 600 180 800 62" fill="none" stroke="var(--gold)" stroke-width="2.4" marker-end="url(#ar3)"/>

<circle cx="120" cy="62" r="5" fill="var(--crimson)"/>
<text x="132" y="80" font-size="12" fill="var(--ink2)"><tspan style="font-weight:700">1</tspan> 本有神的形像</text>
<circle cx="168" cy="96" r="4.5" fill="var(--crimson)"/>
<text x="180" y="114" font-size="12" fill="var(--ink2)"><tspan style="font-weight:700">2</tspan> 不以自己与神同等为强夺的</text>
<circle cx="218" cy="134" r="4.5" fill="var(--crimson)"/>
<text x="230" y="152" font-size="12" fill="var(--ink2)"><tspan style="font-weight:700">3</tspan> 反倒虚己（把自己倒空）</text>
<circle cx="268" cy="174" r="4.5" fill="var(--crimson)"/>
<text x="280" y="192" font-size="12" fill="var(--ink2)"><tspan style="font-weight:700">4</tspan> 取了奴仆的形像</text>
<circle cx="316" cy="216" r="4.5" fill="var(--crimson)"/>
<text x="328" y="234" font-size="12" fill="var(--ink2)"><tspan style="font-weight:700">5</tspan> 成为人的样式</text>
<circle cx="362" cy="262" r="4.5" fill="var(--crimson)"/>
<text x="374" y="280" font-size="12" fill="var(--ink2)"><tspan style="font-weight:700">6</tspan> 自己卑微，存心顺服，以至于死</text>
<circle cx="430" cy="328" r="6" fill="var(--crimson)"/>
<text x="386" y="308" font-size="12" fill="var(--crimson)"><tspan style="font-weight:700">7</tspan> 且死在十字架上</text>

<circle cx="560" cy="238" r="5" fill="var(--gold)"/>
<text x="574" y="236" font-size="12" fill="var(--ink2)"><tspan style="font-weight:700">①</tspan> 神将他升为至高</text>
<circle cx="668" cy="152" r="5" fill="var(--gold)"/>
<text x="682" y="150" font-size="12" fill="var(--ink2)"><tspan style="font-weight:700">②</tspan> 赐他超乎万名之上的名</text>
<circle cx="800" cy="62" r="6" fill="var(--gold)"/>
<text x="818" y="88" text-anchor="end" font-size="12" fill="var(--ink2)"><tspan style="font-weight:700">③</tspan> 万膝跪拜·万口承认·归荣耀与父</text>

<text x="440" y="374" text-anchor="middle" font-size="13" font-weight="700" fill="var(--navy)">转折点是第 9 节的「所以」（[[διό]]）：降卑不是升高的原因，却是升高的道路</text>
<text x="440" y="396" text-anchor="middle" font-size="12" fill="var(--muted)">下降的每一步都是他「自己」动的手（主动语态）；上升的每一步都是「神」动的手（被动／神为主语）</text>
<text x="440" y="416" text-anchor="middle" font-size="12" fill="var(--muted)">2:12-13 正是把这条曲线搬进信徒身上：你自己作成（主动）——因为神在你里面运行（神是主语）</text>
</svg>"""

# ---------------------------------------------------------------- 3 亚当与基督
FIG_ADAM = _s(860, 300, "亚当的抓取与基督的舍弃", 660) + """
<text x="430" y="24" text-anchor="middle" font-size="15" font-weight="700" fill="var(--crimson)">两个人的两种「与神同等」</text>
<rect x="30" y="44" width="380" height="216" rx="11" fill="none" stroke="var(--crimson)" stroke-width="1.8"/>
<rect x="450" y="44" width="380" height="216" rx="11" fill="none" stroke="var(--navy)" stroke-width="1.8"/>
<text x="220" y="70" text-anchor="middle" font-size="13.5" font-weight="700" fill="var(--crimson)">亚当（创 3）</text>
<text x="640" y="70" text-anchor="middle" font-size="13.5" font-weight="700" fill="var(--navy)">末后的亚当（腓 2）</text>

<text x="48" y="98" font-size="12.5" fill="var(--ink2)">本是受造、按神形像被造的人</text>
<text x="468" y="98" font-size="12.5" fill="var(--ink2)">本有神的形像，本来就与神同等</text>
<text x="48" y="124" font-size="12.5" fill="var(--ink2)">「你们便如神」——把同等当成可抓取之物</text>
<text x="468" y="124" font-size="12.5" fill="var(--ink2)">不以与神同等为强夺的、可紧抓不放之事</text>
<text x="48" y="150" font-size="12.5" fill="var(--ink2)">伸手拿（抓取）</text>
<text x="468" y="150" font-size="12.5" fill="var(--ink2)">反倒虚己（倒空）</text>
<text x="48" y="176" font-size="12.5" fill="var(--ink2)">要作主人，结果作了罪的奴仆</text>
<text x="468" y="176" font-size="12.5" fill="var(--ink2)">甘作奴仆，结果被立为万有的主</text>
<text x="48" y="202" font-size="12.5" fill="var(--ink2)">自高 → 被降卑（创 3:19「你本是尘土」）</text>
<text x="468" y="202" font-size="12.5" fill="var(--ink2)">自卑 → 被升高（腓 2:9「升为至高」）</text>
<text x="48" y="228" font-size="12.5" fill="var(--ink2)">违背 → 众人成为罪人<tspan fill="var(--muted)">（罗 5:19上）</tspan></text>
<text x="468" y="228" font-size="12.5" fill="var(--ink2)">顺服 → 众人成为义人<tspan fill="var(--muted)">（罗 5:19下）</tspan></text>
<text x="48" y="252" font-size="12.5" fill="var(--crimson)"><tspan style="font-weight:700">行为之约的失败者</tspan></text>
<text x="468" y="252" font-size="12.5" fill="var(--navy)"><tspan style="font-weight:700">行为之约的成全者，恩典之约的中保</tspan></text>

<text x="430" y="286" text-anchor="middle" font-size="12.5" fill="var(--muted)">所以「基督的心」不是一种性格，而是一个位置：他站在亚当站不住的地方，替我们站住了。</text>
</svg>"""

# ---------------------------------------------------------------- 4 因果结构
FIG_GAR = _s(860, 340, "腓立比书 2:12-13 的因果结构", 660) + """
<defs><marker id="ar4" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
<path d="M0,0 L10,4 L0,8 z" fill="var(--navy)"/></marker></defs>
<text x="430" y="24" text-anchor="middle" font-size="15" font-weight="700" fill="var(--crimson)">「因为」不是例外，是根据</text>

<rect x="60" y="48" width="740" height="56" rx="10" fill="var(--sel)" stroke="var(--gold)" stroke-width="2"/>
<text x="430" y="72" text-anchor="middle" font-size="13.5" font-weight="700" fill="var(--crimson)">12 节　命令（人的动作·现在式命令语气·复数）</text>
<text x="430" y="92" text-anchor="middle" font-size="12.5" fill="var(--ink2)">「就当恐惧战兢，作成（[[κατεργάζεσθε]]）你们得救的工夫」</text>

<path d="M430 108 L430 148" stroke="var(--navy)" stroke-width="2.4" marker-end="url(#ar4)"/>
<rect x="352" y="116" width="156" height="26" rx="13" fill="var(--card)" stroke="var(--navy)" stroke-width="1.4"/>
<text x="430" y="134" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--navy)">因为（[[γάρ]]）</text>

<rect x="60" y="156" width="740" height="76" rx="10" fill="none" stroke="var(--navy)" stroke-width="2"/>
<text x="430" y="180" text-anchor="middle" font-size="13.5" font-weight="700" fill="var(--navy)">13 节　根据（神的动作·神是句子的主语）</text>
<text x="430" y="200" text-anchor="middle" font-size="12.5" fill="var(--ink2)">「你们立志（[[τὸ θέλειν]]）行事（[[τὸ ἐνεργεῖν]]），都是神在你们心里运行（[[ὁ ἐνεργῶν]]）」</text>
<text x="430" y="220" text-anchor="middle" font-size="12.5" fill="var(--ink2)">「为要成就他的美意（[[ὑπὲρ τῆς εὐδοκίας]]）」</text>

<rect x="60" y="250" width="352" height="54" rx="10" fill="none" stroke="var(--crimson)" stroke-width="1.5" stroke-dasharray="5 4"/>
<text x="236" y="271" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--crimson)">✗ 错读：神做一半，我做一半</text>
<text x="236" y="291" text-anchor="middle" font-size="11.8" fill="var(--ink2)">→ 半伯拉纠主义。经文说神做「立志与行事」的全部</text>

<rect x="448" y="250" width="352" height="54" rx="10" fill="none" stroke="var(--teal)" stroke-width="1.5"/>
<text x="624" y="271" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--teal)">✓ 正读：百分之百的神，百分之百的我</text>
<text x="624" y="291" text-anchor="middle" font-size="11.8" fill="var(--ink2)">→ 神的运行不是挤掉我的努力，而是生出我的努力</text>

<text x="430" y="328" text-anchor="middle" font-size="12.5" fill="var(--muted)">世上的逻辑是「既然神做，我就不必做」；圣经的逻辑是「正因为神做，我才做得成——所以要战兢」。</text>
</svg>"""

# ---------------------------------------------------------------- 5 海德堡骨架
FIG_HC = _s(860, 320, "海德堡要理问答三段骨架与主日24的位置", 660) + """
<text x="430" y="24" text-anchor="middle" font-size="15" font-weight="700" fill="var(--crimson)">主日 24 不在「感恩」篇，而在「救恩」篇的结尾——这个位置本身就是神学</text>
<rect x="30" y="46" width="230" height="120" rx="11" fill="none" stroke="var(--crimson)" stroke-width="1.8"/>
<text x="145" y="72" text-anchor="middle" font-size="13.5" font-weight="700" fill="var(--crimson)">一 · 罪　问 3-11</text>
<text x="145" y="96" text-anchor="middle" font-size="12" fill="var(--ink2)">我的困苦有多大</text>
<text x="145" y="118" text-anchor="middle" font-size="12" fill="var(--ink2)">律法照出无能与该死</text>
<text x="145" y="144" text-anchor="middle" font-size="11.5" fill="var(--muted)">主日 2-4</text>

<rect x="290" y="46" width="290" height="180" rx="11" fill="var(--sel)" stroke="var(--navy)" stroke-width="2.2"/>
<text x="435" y="72" text-anchor="middle" font-size="13.5" font-weight="700" fill="var(--navy)">二 · 救恩　问 12-85</text>
<text x="435" y="96" text-anchor="middle" font-size="12" fill="var(--ink2)">中保·信经·因信称义·圣礼</text>
<line x1="310" y1="110" x2="560" y2="110" stroke="var(--line)"/>
<text x="435" y="132" text-anchor="middle" font-size="12" fill="var(--ink2)">主日 23（问 59-61）单单因信称义</text>
<rect x="306" y="142" width="258" height="46" rx="8" fill="var(--card)" stroke="var(--crimson)" stroke-width="2"/>
<text x="435" y="160" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--crimson)">主日 24（问 62-64）</text>
<text x="435" y="178" text-anchor="middle" font-size="11.8" fill="var(--ink2)">替因信称义挡下三发子弹</text>
<text x="435" y="208" text-anchor="middle" font-size="11.5" fill="var(--muted)">主日 5-22 · 24-31</text>

<rect x="610" y="46" width="220" height="120" rx="11" fill="none" stroke="var(--teal)" stroke-width="1.8"/>
<text x="720" y="72" text-anchor="middle" font-size="13.5" font-weight="700" fill="var(--teal)">三 · 感恩　问 86-129</text>
<text x="720" y="96" text-anchor="middle" font-size="12" fill="var(--ink2)">为何仍要行善（问 86）</text>
<text x="720" y="118" text-anchor="middle" font-size="12" fill="var(--ink2)">十诫·主祷文</text>
<text x="720" y="144" text-anchor="middle" font-size="11.5" fill="var(--muted)">主日 32-52</text>

<path d="M260 106 L288 106" stroke="var(--gold)" stroke-width="2"/>
<path d="M580 106 L608 106" stroke="var(--gold)" stroke-width="2"/>

<text x="430" y="256" text-anchor="middle" font-size="12.5" fill="var(--ink2)">问 62「善行不能作义」· 问 63「赏赐不是赚的」· 问 64「这不会使人放荡」</text>
<text x="430" y="278" text-anchor="middle" font-size="12.5" fill="var(--ink2)">前两问把善行从「地基」的位置上搬下来，第三问立刻把它放回「果子」的位置上</text>
<text x="430" y="302" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--crimson)">腓 2:12-13 恰好同时说了这三件事：作成（果子）· 神运行（恩典）· 战兢（我本无有）</text>
</svg>"""

# ---------------------------------------------------------------- 6 救赎历史闭环
FIG_COV = _s(760, 560, "救赎历史的圣约闭环", 620) + """
<text x="380" y="24" text-anchor="middle" font-size="15" font-weight="700" fill="var(--crimson)">闭环一：救赎历史 · 圣约神学</text>
<circle cx="380" cy="300" r="212" fill="none" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="4 6"/>
<circle cx="380" cy="300" r="96" fill="none" stroke="var(--gold)" stroke-width="2"/>
<text x="380" y="288" text-anchor="middle" font-size="13" font-weight="700" fill="var(--gold)">起点与终点</text>
<text x="380" y="310" text-anchor="middle" font-size="12.5" fill="var(--ink2)">同一个「美意」</text>
<text x="380" y="330" text-anchor="middle" font-size="11.5" fill="var(--muted)">[[εὐδοκία]]　弗 1:5,9 ／ 腓 2:13</text>

<g font-size="11.8" fill="var(--ink2)">
<rect x="272" y="46" width="216" height="46" rx="9" fill="var(--card)" stroke="var(--navy)" stroke-width="1.5"/>
<text x="380" y="66" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--navy)">① 永恒 · 救赎之约</text>
<text x="380" y="84" text-anchor="middle">父定意、子受命、灵施行（亚 6:13；赛 53:10-12）</text>

<rect x="520" y="118" width="228" height="46" rx="9" fill="var(--card)" stroke="var(--navy)" stroke-width="1.5"/>
<text x="634" y="138" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--navy)">② 创造 · 行为之约</text>
<text x="634" y="156" text-anchor="middle">亚当被造、受命、被试（创 2:16-17）</text>

<rect x="560" y="222" width="196" height="46" rx="9" fill="var(--card)" stroke="var(--crimson)" stroke-width="1.5"/>
<text x="658" y="242" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--crimson)">③ 堕落 · 抓取</text>
<text x="658" y="260" text-anchor="middle">「你们便如神」（创 3:5）</text>

<rect x="552" y="326" width="204" height="46" rx="9" fill="var(--card)" stroke="var(--navy)" stroke-width="1.5"/>
<text x="654" y="346" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--navy)">④ 应许 · 恩典之约</text>
<text x="654" y="364" text-anchor="middle">女人的后裔 → 亚伯拉罕 → 大卫</text>

<rect x="440" y="430" width="240" height="46" rx="9" fill="var(--card)" stroke="var(--navy)" stroke-width="1.5"/>
<text x="560" y="450" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--navy)">⑤ 新约的应许</text>
<text x="560" y="468" text-anchor="middle">「我要将我的灵放在你们里面」结 36:27</text>

<rect x="178" y="492" width="252" height="46" rx="9" fill="var(--sel)" stroke="var(--gold)" stroke-width="2"/>
<text x="304" y="512" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--crimson)">⑥ 成全 · 末后亚当的顺服</text>
<text x="304" y="530" text-anchor="middle">腓 2:8「存心顺服，以至于死」</text>

<rect x="14" y="398" width="212" height="46" rx="9" fill="var(--card)" stroke="var(--teal)" stroke-width="1.5"/>
<text x="120" y="418" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--teal)">⑦ 施行 · 圣灵在你里面运行</text>
<text x="120" y="436" text-anchor="middle">腓 2:13＝结 36:27 的新约兑现</text>

<rect x="6" y="292" width="200" height="46" rx="9" fill="var(--card)" stroke="var(--teal)" stroke-width="1.5"/>
<text x="106" y="312" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--teal)">⑧ 今生 · 恐惧战兢作成</text>
<text x="106" y="330" text-anchor="middle">腓 2:12；1:6 那动了善工的必成全</text>

<rect x="18" y="186" width="196" height="46" rx="9" fill="var(--card)" stroke="var(--plum)" stroke-width="1.5"/>
<text x="116" y="206" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--plum)">⑨ 基督的日子</text>
<text x="116" y="224" text-anchor="middle">腓 2:16；3:20-21 身体改变形状</text>

<rect x="84" y="96" width="176" height="46" rx="9" fill="var(--card)" stroke="var(--plum)" stroke-width="1.5"/>
<text x="172" y="116" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--plum)">⑩ 万膝跪拜</text>
<text x="172" y="134" text-anchor="middle">腓 2:10-11；启 5:13 归荣耀与父</text>
</g>
<path d="M172 96 Q 300 30 380 46" fill="none" stroke="var(--gold)" stroke-width="1.6" stroke-dasharray="5 4"/>
<text x="380" y="552" text-anchor="middle" font-size="12" fill="var(--muted)">环的两端在「父的美意」处合拢：起头是他的美意，末了也归他的荣耀——中间这一段，就是你今天的顺服。</text>
</svg>"""

# ---------------------------------------------------------------- 7 经文闭环
FIG_CANON = _s(880, 300, "从创世记到启示录的经文闭环", 700) + """
<defs><marker id="ar5" markerWidth="9" markerHeight="7" refX="8" refY="3.5" orient="auto">
<path d="M0,0 L9,3.5 L0,7 z" fill="var(--teal)"/></marker></defs>
<text x="440" y="24" text-anchor="middle" font-size="15" font-weight="700" fill="var(--crimson)">闭环二：经文 · 圣经神学</text>
<line x1="50" y1="150" x2="830" y2="150" stroke="var(--teal)" stroke-width="2" marker-end="url(#ar5)"/>
<g font-size="11.6" fill="var(--ink2)">
<circle cx="90" cy="150" r="7" fill="var(--crimson)"/>
<text x="90" y="128" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--crimson)">创 3:5</text>
<text x="90" y="180" text-anchor="middle">抓取「如神」</text>
<circle cx="220" cy="150" r="7" fill="var(--navy)"/>
<text x="220" y="128" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--navy)">出 15-16</text>
<text x="220" y="180" text-anchor="middle">战兢敬畏／旷野发怨言</text>
<circle cx="350" cy="150" r="7" fill="var(--navy)"/>
<text x="350" y="128" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--navy)">申 32:5</text>
<text x="350" y="180" text-anchor="middle">弯曲悖谬的世代</text>
<circle cx="470" cy="150" r="7" fill="var(--navy)"/>
<text x="470" y="128" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--navy)">诗 2:11</text>
<text x="470" y="180" text-anchor="middle">存畏惧事奉·战兢而快乐</text>
<circle cx="590" cy="150" r="7" fill="var(--navy)"/>
<text x="590" y="128" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--navy)">赛 45:23 · 53</text>
<text x="590" y="180" text-anchor="middle">万膝跪拜·仆人的顺服</text>
<circle cx="700" cy="150" r="7" fill="var(--navy)"/>
<text x="700" y="128" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--navy)">结 36:27</text>
<text x="700" y="180" text-anchor="middle">我的灵使你们遵行</text>
<circle cx="800" cy="150" r="9" fill="var(--gold)"/>
<text x="800" y="128" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--gold)">启 5:13</text>
<text x="800" y="180" text-anchor="middle">万物都说：颂赞归羔羊</text>
</g>
<rect x="300" y="222" width="280" height="50" rx="11" fill="var(--sel)" stroke="var(--gold)" stroke-width="2"/>
<text x="440" y="243" text-anchor="middle" font-size="13" font-weight="700" fill="var(--crimson)">腓 2:1-18</text>
<text x="440" y="262" text-anchor="middle" font-size="11.8" fill="var(--ink2)">以上七处旧约，全部在这十八节里回响一遍</text>
<path d="M90 158 Q 250 230 300 244" fill="none" stroke="var(--line)" stroke-width="1.2"/>
<path d="M800 158 Q 660 230 580 244" fill="none" stroke="var(--line)" stroke-width="1.2"/>
<text x="440" y="292" text-anchor="middle" font-size="12" fill="var(--muted)">腓 2 不是一段孤立的伦理劝勉，它是整本圣经的缩影：抓取→倒空→顺服→高举→敬拜。</text>
</svg>"""

# ---------------------------------------------------------------- 8 罪-救赎-感恩
FIG_TRI = _s(720, 400, "罪—救赎—感恩三段闭环", 600) + """
<defs><marker id="ar6" markerWidth="9" markerHeight="7" refX="8" refY="3.5" orient="auto">
<path d="M0,0 L9,3.5 L0,7 z" fill="var(--gold)"/></marker></defs>
<text x="360" y="24" text-anchor="middle" font-size="15" font-weight="700" fill="var(--crimson)">闭环三：改革宗 · 罪—救赎—感恩</text>
<polygon points="360,60 630,330 90,330" fill="none" stroke="var(--line)" stroke-width="1.5"/>
<path d="M360 78 L600 318" stroke="var(--gold)" stroke-width="2" marker-end="url(#ar6)" fill="none"/>
<path d="M600 336 L128 336" stroke="var(--gold)" stroke-width="2" marker-end="url(#ar6)" fill="none"/>
<path d="M110 318 L348 80" stroke="var(--gold)" stroke-width="2" marker-end="url(#ar6)" fill="none"/>

<rect x="248" y="38" width="224" height="52" rx="10" fill="var(--card)" stroke="var(--crimson)" stroke-width="2"/>
<text x="360" y="58" text-anchor="middle" font-size="13" font-weight="700" fill="var(--crimson)">罪 · 我最好的善行仍有瑕疵</text>
<text x="360" y="78" text-anchor="middle" font-size="11.8" fill="var(--ink2)">赛 64:6；海德堡 62 → 所以要「战兢」</text>

<rect x="470" y="300" width="228" height="56" rx="10" fill="var(--card)" stroke="var(--navy)" stroke-width="2"/>
<text x="584" y="320" text-anchor="middle" font-size="13" font-weight="700" fill="var(--navy)">救恩 · 神在我里面运行</text>
<text x="584" y="340" text-anchor="middle" font-size="11.8" fill="var(--ink2)">腓 2:13；海德堡 60-61 → 所以能「作成」</text>

<rect x="22" y="300" width="228" height="56" rx="10" fill="var(--card)" stroke="var(--teal)" stroke-width="2"/>
<text x="136" y="320" text-anchor="middle" font-size="13" font-weight="700" fill="var(--teal)">感恩 · 善行是果子不是本钱</text>
<text x="136" y="340" text-anchor="middle" font-size="11.8" fill="var(--ink2)">腓 2:14-16；海德堡 64、86 → 必然「结果」</text>

<text x="360" y="216" text-anchor="middle" font-size="13" font-weight="700" fill="var(--gold)">腓 2:12-13</text>
<text x="360" y="238" text-anchor="middle" font-size="12" fill="var(--ink2)">一节经文同时含三段</text>
<text x="360" y="382" text-anchor="middle" font-size="12" fill="var(--muted)">顺序不可倒置：先知罪，才敢要恩典；先领恩典，才有真感恩；感恩之行又反过来叫人更看见自己的不配。</text>
</svg>"""

# ---------------------------------------------------------------- 9 根基与果子
FIG_FOUND = _s(820, 330, "善行的正确位置：果子而非地基", 640) + """
<text x="410" y="24" text-anchor="middle" font-size="15" font-weight="700" fill="var(--crimson)">同一件善行，放错位置就成了敌基督</text>
<rect x="34" y="46" width="356" height="248" rx="11" fill="none" stroke="var(--crimson)" stroke-width="1.8"/>
<text x="212" y="70" text-anchor="middle" font-size="13.5" font-weight="700" fill="var(--crimson)">✗ 放在地基上（罗马／律法主义）</text>
<rect x="74" y="90" width="276" height="34" rx="6" fill="none" stroke="var(--line)" stroke-width="1.4"/>
<text x="212" y="112" text-anchor="middle" font-size="12" fill="var(--ink2)">得救的确据（永远摇动）</text>
<rect x="74" y="132" width="276" height="34" rx="6" fill="none" stroke="var(--line)" stroke-width="1.4"/>
<text x="212" y="154" text-anchor="middle" font-size="12" fill="var(--ink2)">基督的功劳（只算一部分）</text>
<rect x="74" y="174" width="276" height="40" rx="6" fill="var(--card)" stroke="var(--crimson)" stroke-width="2"/>
<text x="212" y="199" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--crimson)">我的善行（承重墙）</text>
<path d="M74 226 L350 226" stroke="var(--crimson)" stroke-width="2" stroke-dasharray="6 4"/>
<text x="212" y="248" text-anchor="middle" font-size="11.8" fill="var(--ink2)">地基一裂，全楼皆垮：良心不安、</text>
<text x="212" y="266" text-anchor="middle" font-size="11.8" fill="var(--ink2)">数算功德、比较他人、临终无靠</text>
<text x="212" y="286" text-anchor="middle" font-size="11.8" fill="var(--muted)">加 5:4「你们就从恩典中坠落了」</text>

<rect x="430" y="46" width="356" height="248" rx="11" fill="none" stroke="var(--teal)" stroke-width="1.8"/>
<text x="608" y="70" text-anchor="middle" font-size="13.5" font-weight="700" fill="var(--teal)">✓ 放在果子上（改革宗）</text>
<rect x="470" y="90" width="276" height="40" rx="6" fill="var(--card)" stroke="var(--teal)" stroke-width="2"/>
<text x="608" y="115" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--teal)">我的善行（果子·凭据·感恩）</text>
<rect x="470" y="138" width="276" height="34" rx="6" fill="none" stroke="var(--line)" stroke-width="1.4"/>
<text x="608" y="160" text-anchor="middle" font-size="12" fill="var(--ink2)">圣灵重生、联于基督（约 15:5）</text>
<rect x="470" y="180" width="276" height="40" rx="6" fill="var(--card)" stroke="var(--navy)" stroke-width="2.4"/>
<text x="608" y="205" text-anchor="middle" font-size="12.5" font-weight="700" fill="var(--navy)">基督的义（唯一承重墙）</text>
<path d="M470 232 L746 232" stroke="var(--navy)" stroke-width="3"/>
<text x="608" y="254" text-anchor="middle" font-size="11.8" fill="var(--ink2)">地基不动，果子照长：良心得安、</text>
<text x="608" y="272" text-anchor="middle" font-size="11.8" fill="var(--ink2)">乐意服事、敢于认罪、临终有靠</text>
<text x="608" y="290" text-anchor="middle" font-size="11.8" fill="var(--muted)">海德堡 64；比利时信条 24 条</text>
<text x="410" y="320" text-anchor="middle" font-size="12.5" fill="var(--muted)">两边的「行善」在外表上可能一模一样；差别只在：它撑着谁，还是谁撑着它。</text>
</svg>"""

# ---------------------------------------------------------------- 10 恐惧战兢四象限
FIG_FEAR = _s(660, 480, "四种面对神的心态", 560) + """
<text x="330" y="24" text-anchor="middle" font-size="15" font-weight="700" fill="var(--crimson)">「恐惧战兢」在哪一格？</text>
<line x1="330" y1="52" x2="330" y2="420" stroke="var(--line)" stroke-width="1.5"/>
<line x1="40" y1="236" x2="620" y2="236" stroke="var(--line)" stroke-width="1.5"/>
<text x="330" y="44" text-anchor="middle" font-size="11.5" fill="var(--muted)">↑ 严肃 · 战兢</text>
<text x="330" y="440" text-anchor="middle" font-size="11.5" fill="var(--muted)">↓ 轻慢 · 松懈</text>
<text x="48" y="232" font-size="11.5" fill="var(--muted)">← 靠自己</text>
<text x="612" y="232" text-anchor="end" font-size="11.5" fill="var(--muted)">靠恩典 →</text>

<rect x="52" y="64" width="256" height="158" rx="11" fill="none" stroke="var(--crimson)" stroke-width="1.8"/>
<text x="180" y="90" text-anchor="middle" font-size="13" font-weight="700" fill="var(--crimson)">律法主义的惧怕</text>
<text x="180" y="114" text-anchor="middle" font-size="11.8" fill="var(--ink2)">「我做得不够，神要丢弃我」</text>
<text x="180" y="136" text-anchor="middle" font-size="11.8" fill="var(--ink2)">奴仆之惧（[[timor servilis]]）</text>
<text x="180" y="158" text-anchor="middle" font-size="11.8" fill="var(--ink2)">越努力越没有确据</text>
<text x="180" y="184" text-anchor="middle" font-size="11.5" fill="var(--muted)">对症：海德堡 62-63</text>
<text x="180" y="204" text-anchor="middle" font-size="11.5" fill="var(--muted)">——赏赐本来就不是赚的</text>

<rect x="352" y="64" width="256" height="158" rx="11" fill="var(--sel)" stroke="var(--gold)" stroke-width="2.4"/>
<text x="480" y="90" text-anchor="middle" font-size="13" font-weight="700" fill="var(--gold)">✓ 腓 2:12 的战兢</text>
<text x="480" y="114" text-anchor="middle" font-size="11.8" fill="var(--ink2)">「神竟然在我里面动工——」</text>
<text x="480" y="136" text-anchor="middle" font-size="11.8" fill="var(--ink2)">儿子之敬畏（[[timor filialis]]）</text>
<text x="480" y="158" text-anchor="middle" font-size="11.8" fill="var(--ink2)">越有确据越不敢儿戏</text>
<text x="480" y="184" text-anchor="middle" font-size="11.5" fill="var(--muted)">诗 2:11 战兢而快乐</text>
<text x="480" y="204" text-anchor="middle" font-size="11.5" fill="var(--muted)">诗 130:4 你有赦免之恩，要叫人敬畏你</text>

<rect x="52" y="252" width="256" height="158" rx="11" fill="none" stroke="var(--muted)" stroke-width="1.5"/>
<text x="180" y="278" text-anchor="middle" font-size="13" font-weight="700" fill="var(--muted)">道德自满</text>
<text x="180" y="302" text-anchor="middle" font-size="11.8" fill="var(--ink2)">「我还不错，比某某强」</text>
<text x="180" y="324" text-anchor="middle" font-size="11.8" fill="var(--ink2)">法利赛人的祷告（路 18:11）</text>
<text x="180" y="348" text-anchor="middle" font-size="11.8" fill="var(--ink2)">既无战兢，也无恩典</text>
<text x="180" y="374" text-anchor="middle" font-size="11.5" fill="var(--muted)">对症：海德堡 62 的「绝对完美」</text>

<rect x="352" y="252" width="256" height="158" rx="11" fill="none" stroke="var(--plum)" stroke-width="1.5"/>
<text x="480" y="278" text-anchor="middle" font-size="13" font-weight="700" fill="var(--plum)">廉价恩典 / 反律主义</text>
<text x="480" y="302" text-anchor="middle" font-size="11.8" fill="var(--ink2)">「反正都是恩典，随便活」</text>
<text x="480" y="324" text-anchor="middle" font-size="11.8" fill="var(--ink2)">把「不能赚」读成「不必行」</text>
<text x="480" y="348" text-anchor="middle" font-size="11.8" fill="var(--ink2)">正是海德堡 64 所设的问</text>
<text x="480" y="374" text-anchor="middle" font-size="11.5" fill="var(--muted)">对症：约 15:5 联于基督必结果子</text>

<text x="330" y="466" text-anchor="middle" font-size="12.2" fill="var(--muted)">只有右上角这一格，是「因为神在你心里运行，所以恐惧战兢」——恐惧的对象不是刑罚，是神自己的临在。</text>
</svg>"""
