// 由 content.json 生成 A4 Word 文档（house style：SimSun/SimHei，希腊文 Palatino 斜体深蓝）
const fs = require('fs');
const path = require('path');
const D = require('docx');
const {
  Document, Packer, Paragraph, TextRun, ImageRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, TableOfContents,
  PageNumber, Header, Footer, PageBreak, LevelFormat, TableLayoutType, LineRuleType
} = D;

const ROOT = path.join(__dirname);
const data = JSON.parse(fs.readFileSync(path.join(ROOT, 'content.json'), 'utf8'));
const figMeta = JSON.parse(fs.readFileSync(path.join(ROOT, 'img', 'meta.json'), 'utf8'));

const NAVY = '1E3A5F', CRIMSON = '8C2F39', GOLD = 'A5812A', GREY = '6B6155',
      INK = '241F1A', LINE = 'DDD2BC', SOFT = 'FBF6EA', HEADTXT = 'FFFFFF';

const CN = 'SimSun', CNB = 'SimHei', EN = 'Times New Roman', GK = 'Palatino Linotype';
const f = (ascii, ea) => ({ ascii, hAnsi: ascii, cs: ascii, eastAsia: ea || ascii });
const FBODY = f(EN, CN), FHEAD = f(EN, CNB), FGK = f(GK, CN);

const CONTENT_DXA = 9746;          // A4 11906 - 2*1080

/* ───────── 行内解析 ───────── */
const GREEK = /[\u0370-\u03FF\u1F00-\u1FFF]/;
const TOKEN = /\*\*(.+?)\*\*|\{\{(.+?)\}\}|\[\[(.+?)\]\]|\(\((.+?)\)\)/g;

// 把一段同质文本按「希腊字母 / 其它」切开，分别配字体
function segment(text, base) {
  const out = [];
  let buf = '', mode = null;
  const flush = () => {
    if (!buf) return;
    const o = Object.assign({}, base, { text: buf });
    if (mode === 'g') { o.font = FGK; o.italics = true; if (!base.color) o.color = NAVY; }
    out.push(new TextRun(o));
    buf = '';
  };
  for (const ch of text) {
    const m = GREEK.test(ch) ? 'g' : 'n';
    if (mode !== null && m !== mode) flush();
    mode = m; buf += ch;
  }
  flush();
  return out;
}

function runs(text, opts) {
  opts = opts || {};
  const base = { font: FBODY, size: opts.size || 21, color: opts.color || INK };
  if (opts.bold) base.bold = true;
  if (opts.italics) base.italics = true;
  const out = [];
  let last = 0, m;
  TOKEN.lastIndex = 0;
  while ((m = TOKEN.exec(text)) !== null) {
    if (m.index > last) out.push(...segment(text.slice(last, m.index), base));
    if (m[1] !== undefined) out.push(...segment(m[1], Object.assign({}, base, { bold: true })));
    else if (m[2] !== undefined) out.push(...segment(m[2], Object.assign({}, base, { bold: true, color: CRIMSON })));
    else if (m[3] !== undefined) out.push(...segment(m[3], Object.assign({}, base, { font: FGK, italics: true, color: NAVY })));
    else if (m[4] !== undefined) out.push(...segment(m[4], Object.assign({}, base, { size: Math.max(16, (opts.size || 21) - 3), color: GREY })));
    last = TOKEN.lastIndex;
  }
  if (last < text.length) out.push(...segment(text.slice(last), base));
  return out;
}

const P = (text, o) => {
  o = o || {};
  return new Paragraph({
    children: runs(text, o),
    spacing: { before: o.before === undefined ? 40 : o.before, after: o.after === undefined ? 110 : o.after, line: o.line || 320, lineRule: LineRuleType.AUTO },
    alignment: o.align || AlignmentType.JUSTIFIED,
    indent: o.indent,
    numbering: o.numbering,
    keepNext: o.keepNext,
  });
};

/* ───────── 标注框：单格表格 + 仅左边框 ───────── */
function callout(text, src, color, label) {
  const inner = [
    new Paragraph({
      children: [
        new TextRun({ text: label + '　', font: FHEAD, size: 17, color, bold: true }),
        ...runs(text, { size: 20 })
      ],
      spacing: { before: 60, after: src ? 40 : 60, line: 300, lineRule: LineRuleType.AUTO },
      alignment: AlignmentType.JUSTIFIED,
    })
  ];
  if (src) inner.push(new Paragraph({
    children: [new TextRun({ text: '— ' + src, font: FBODY, size: 17, color: GREY })],
    alignment: AlignmentType.RIGHT, spacing: { after: 60 },
  }));
  return new Table({
    columnWidths: [CONTENT_DXA],
    width: { size: CONTENT_DXA, type: WidthType.DXA },
    layout: TableLayoutType.FIXED,
    rows: [new TableRow({
      children: [new TableCell({
        width: { size: CONTENT_DXA, type: WidthType.DXA },
        shading: { type: ShadingType.CLEAR, fill: SOFT, color: 'auto' },
        margins: { top: 90, bottom: 90, left: 220, right: 180 },
        borders: {
          top: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' },
          bottom: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' },
          right: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' },
          left: { style: BorderStyle.SINGLE, size: 24, color },
        },
        children: inner,
      })],
    })],
  });
}

/* ───────── 数据表 ───────── */
function dataTable(cap, heads, rows) {
  const n = heads.length;
  const plain = s => String(s).replace(TOKEN, (m, a, b, c, d) => a || b || c || d || '');
  const w = heads.map((h, i) => {
    let len = plain(h).length;
    rows.forEach(r => { len = Math.max(len, Math.min(plain(r[i] || '').length, 46)); });
    return Math.max(len, 4);
  });
  const tot = w.reduce((a, b) => a + b, 0);
  let cols = w.map(x => Math.round(CONTENT_DXA * x / tot));
  cols[n - 1] += CONTENT_DXA - cols.reduce((a, b) => a + b, 0);

  const cell = (txt, i, opts) => new TableCell({
    width: { size: cols[i], type: WidthType.DXA },
    shading: opts.fill ? { type: ShadingType.CLEAR, fill: opts.fill, color: 'auto' } : undefined,
    margins: { top: 60, bottom: 60, left: 110, right: 110 },
    children: [new Paragraph({
      children: runs(String(txt), { size: opts.size || 18, color: opts.color, bold: opts.bold }),
      spacing: { before: 0, after: 0, line: 268, lineRule: LineRuleType.AUTO },
      alignment: AlignmentType.LEFT,
    })],
  });

  const out = [];
  if (cap) out.push(new Paragraph({
    children: [new TextRun({ text: '表 · ' + plain(cap), font: FHEAD, size: 17, color: GREY })],
    spacing: { before: 140, after: 60 }, keepNext: true,
  }));
  out.push(new Table({
    columnWidths: cols,
    width: { size: CONTENT_DXA, type: WidthType.DXA },
    layout: TableLayoutType.FIXED,
    borders: {
      top: { style: BorderStyle.SINGLE, size: 6, color: LINE },
      bottom: { style: BorderStyle.SINGLE, size: 6, color: LINE },
      left: { style: BorderStyle.SINGLE, size: 6, color: LINE },
      right: { style: BorderStyle.SINGLE, size: 6, color: LINE },
      insideHorizontal: { style: BorderStyle.SINGLE, size: 4, color: LINE },
      insideVertical: { style: BorderStyle.SINGLE, size: 4, color: LINE },
    },
    rows: [
      new TableRow({
        tableHeader: true,
        children: heads.map((h, i) => cell(h, i, { fill: NAVY, color: HEADTXT, bold: true, size: 18 })),
      }),
      ...rows.map((r, ri) => new TableRow({
        children: heads.map((_, i) => cell(r[i] === undefined ? '' : r[i], i,
          { fill: ri % 2 ? SOFT : undefined })),
      })),
    ],
  }));
  out.push(new Paragraph({ text: '', spacing: { after: 130 } }));
  return out;
}

/* ───────── 图 ───────── */
function figure(n, cap) {
  const meta = figMeta.find(m => m.n === n);
  const file = path.join(ROOT, 'img', 'fig' + n + '.png');
  const out = [];
  if (meta && fs.existsSync(file)) {
    const W = 630, H = Math.round(W * meta.h / meta.w);
    out.push(new Paragraph({
      children: [new ImageRun({ type: 'png', data: fs.readFileSync(file),
        transformation: { width: W, height: H } })],
      alignment: AlignmentType.CENTER, spacing: { before: 170, after: 60, line: 240, lineRule: LineRuleType.AUTO }, keepNext: true,
    }));
  }
  out.push(new Paragraph({
    children: runs(cap, { size: 17, color: GREY }),
    alignment: AlignmentType.CENTER, spacing: { after: 170 },
  }));
  return out;
}

/* ───────── 区块 → 段落 ───────── */
let olInstance = 0;
function blockToDocx(b) {
  switch (b.t) {
    case 'p':    return [P(b.x)];
    case 'lead': return [P(b.x, { size: 22, color: '4A4138', indent: { left: 220 }, after: 150 })];
    case 'h3':   return [new Paragraph({
        heading: HeadingLevel.HEADING_2,
        children: runs(b.x, { size: 26, color: NAVY, bold: true }),
        spacing: { before: 300, after: 110 }, keepNext: true,
      })];
    case 'h4':   return [new Paragraph({
        heading: HeadingLevel.HEADING_3,
        children: runs('◆ ' + b.x, { size: 22, color: INK, bold: true }),
        spacing: { before: 210, after: 80 }, keepNext: true,
      })];
    case 'ul':   return b.items.map(x => P(x, {
        numbering: { reference: 'bul', level: 0 }, after: 60, line: 300 }));
    case 'ol':   { olInstance += 1;
      return b.items.map(x => P(x, {
        numbering: { reference: 'num', level: 0, instance: olInstance }, after: 60, line: 300 })); }
    case 'table': return dataTable(b.cap, b.heads, b.rows);
    case 'scr':  return [callout(b.x, b.src, GOLD, '经'), new Paragraph({ text: '', spacing: { after: 130 } })];
    case 'cat':  return [callout(b.x, b.src, NAVY, '问'), new Paragraph({ text: '', spacing: { after: 130 } })];
    case 'app':  return [callout(b.x, b.src, CRIMSON, '用'), new Paragraph({ text: '', spacing: { after: 130 } })];
    case 'qa':   return [
        P('？ ' + b.q, { bold: true, color: NAVY, before: 150, after: 50 }),
        P('答：' + b.a, { color: '4A4138', indent: { left: 240 }, after: 140 }),
      ];
    case 'fig':  return figure(b.n, b.cap);
    case 'hr':   return [new Paragraph({
        text: '', spacing: { before: 120, after: 120 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: LINE } } })];
    default:     return [];
  }
}

/* ───────── 封面与目录 ───────── */
function cover() {
  const c = [];
  c.push(new Paragraph({ text: '', spacing: { before: 1400 } }));
  c.push(new Paragraph({
    children: [new TextRun({ text: 'CONTINENTAL REFORMED SERMON', font: FHEAD, size: 17, color: GOLD, characterSpacing: 90 })],
    alignment: AlignmentType.CENTER, spacing: { after: 240 },
  }));
  c.push(new Paragraph({
    children: [new TextRun({ text: data.title, font: FHEAD, size: 46, color: NAVY, bold: true })],
    alignment: AlignmentType.CENTER, spacing: { after: 160 },
  }));
  c.push(new Paragraph({
    children: [new TextRun({ text: '腓立比书 2:1-18　×　海德堡要理问答 主日 24（问 62-64）', font: FBODY, size: 24, color: '4A4138' })],
    alignment: AlignmentType.CENTER, spacing: { after: 420 },
  }));
  c.push(new Paragraph({
    children: [new TextRun({ text: '要点一　因神在你心里运行', font: FHEAD, size: 24, color: CRIMSON })],
    alignment: AlignmentType.CENTER, spacing: { after: 90 },
  }));
  c.push(new Paragraph({
    children: [new TextRun({ text: '要点二　为要成就他的美意', font: FHEAD, size: 24, color: CRIMSON })],
    alignment: AlignmentType.CENTER, spacing: { after: 520 },
  }));
  data.order.forEach(([k, v]) => {
    c.push(new Paragraph({
      children: [
        new TextRun({ text: k + '　', font: FHEAD, size: 18, color: GOLD }),
        new TextRun({ text: v, font: FBODY, size: 19, color: '4A4138' }),
      ],
      alignment: AlignmentType.CENTER, spacing: { after: 60 },
    }));
  });
  c.push(new Paragraph({ children: [new PageBreak()] }));
  c.push(new Paragraph({
    children: [new TextRun({ text: '目　录', font: FHEAD, size: 30, color: NAVY, bold: true })],
    alignment: AlignmentType.CENTER, spacing: { after: 200 },
  }));
  c.push(new TableOfContents('目录', { hyperlink: true, headingStyleRange: '1-2' }));
  c.push(new Paragraph({ children: [new PageBreak()] }));
  return c;
}

/* ───────── 组装 ───────── */
const body = [...cover()];
data.sections.forEach((s, i) => {
  if (i > 0) body.push(new Paragraph({ children: [new PageBreak()] }));
  body.push(new Paragraph({
    heading: HeadingLevel.HEADING_1,
    children: [
      new TextRun({ text: s.num + '　', font: FHEAD, size: 26, color: GOLD, bold: true }),
      ...runs(s.title, { size: 32, color: CRIMSON, bold: true }),
    ],
    spacing: { before: 120, after: 60 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: LINE } },
  }));
  body.push(new Paragraph({ text: '', spacing: { after: 130 } }));
  s.blocks.forEach(b => body.push(...blockToDocx(b)));
});

const doc = new Document({
  creator: 'Reformed Sermon Builder',
  title: data.title,
  description: data.subtitle,
  styles: {
    default: {
      document: { run: { font: FBODY, size: 21, color: INK }, paragraph: { spacing: { line: 320, lineRule: LineRuleType.AUTO } } },
      heading1: { run: { font: FHEAD, size: 32, bold: true, color: CRIMSON } },
      heading2: { run: { font: FHEAD, size: 26, bold: true, color: NAVY } },
      heading3: { run: { font: FHEAD, size: 22, bold: true, color: INK } },
    },
  },
  numbering: {
    config: [
      { reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '·',
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 460, hanging: 240 } },
                   run: { font: FBODY, color: GOLD } } }] },
      { reference: 'num', levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.',
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 460, hanging: 280 } },
                   run: { font: FBODY, color: GOLD, bold: true } } }] },
    ],
  },
  sections: [{
    properties: { page: { margin: { top: 1180, right: 1080, bottom: 1180, left: 1080 } } },
    headers: {
      default: new Header({
        children: [new Paragraph({
          children: [new TextRun({ text: data.title + '　·　腓立比书 2:1-18 × 海德堡主日 24',
            font: FBODY, size: 16, color: GREY })],
          alignment: AlignmentType.RIGHT,
          border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: LINE } },
        })],
      }),
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          children: [new TextRun({ children: ['— ', PageNumber.CURRENT, ' —'],
            font: FBODY, size: 18, color: GOLD })],
          alignment: AlignmentType.CENTER,
        })],
      }),
    },
    children: body,
  }],
});

Packer.toBuffer(doc).then(buf => {
  const out = path.join(ROOT, '当存敬畏战兢的心作成得救的工夫-腓立比书2章1-18节-海德堡主日24.docx');
  fs.writeFileSync(out, buf);
  console.log('written  %s  %.1f KB', path.basename(out), buf.length / 1024);
});
