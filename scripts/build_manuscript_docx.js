// Build a bioRxiv-ready Word manuscript from the markdown draft.
// Deliberately a narrow converter for THIS document, not a general markdown engine.

const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType,
  ImageRun, PageOrientation, LevelFormat, convertInchesToTwip,
} = require("docx");

const SRC = "C:/ProjectAuxiliary/manuscript/preprint_draft.md";
const FIGDIR = "C:/ProjectAuxiliary/manuscript/figures";
const OUT = "C:/ProjectAuxiliary/manuscript/preprint_bioRxiv.docx";

const PAGE_W = 12240, PAGE_H = 15840;            // US Letter, DXA
const MARGIN = 1440;                              // 1 inch
const USABLE = PAGE_W - 2 * MARGIN;               // 9360 DXA
const USABLE_PX = 6.5 * 96;                       // 624 px at 96 dpi

// PNG dimensions straight from the IHDR chunk - avoids an image library.
function pngSize(file) {
  const b = fs.readFileSync(file);
  return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
}

// ---------- inline formatting ----------
// Handles **bold**, *italic*, `code`, [text](url), and nesting of bold+code.
function inline(text, base = {}) {
  const runs = [];
  const re = /(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`|\[[^\]]+\]\([^)]+\))/g;
  let last = 0, m;
  const push = (t, opts) => { if (t) runs.push(new TextRun({ text: t, ...base, ...opts })); };
  while ((m = re.exec(text)) !== null) {
    push(text.slice(last, m.index), {});
    const tok = m[0];
    if (tok.startsWith("**")) push(tok.slice(2, -2), { bold: true });
    else if (tok.startsWith("`")) push(tok.slice(1, -1), { font: "Consolas", size: 19 });
    else if (tok.startsWith("[")) {
      const mm = /\[([^\]]+)\]\(([^)]+)\)/.exec(tok);
      push(mm[1], { color: "0563C1" });
    } else push(tok.slice(1, -1), { italics: true });
    last = m.index + tok.length;
  }
  push(text.slice(last), {});
  return runs.length ? runs : [new TextRun({ text: "", ...base })];
}

// ---------- table ----------
function buildTable(lines) {
  const rows = lines
    .filter((l) => !/^\|[\s:|-]+\|$/.test(l.trim()))
    .map((l) => l.trim().replace(/^\||\|$/g, "").split("|").map((c) => c.trim()));
  const nCols = Math.max(...rows.map((r) => r.length));
  // Column widths must sum to the table width, and every cell needs its own width.
  const colW = Math.floor(USABLE / nCols);
  const widths = Array(nCols).fill(colW);
  widths[nCols - 1] = USABLE - colW * (nCols - 1);

  return new Table({
    columnWidths: widths,
    width: { size: USABLE, type: WidthType.DXA },
    rows: rows.map((cells, ri) =>
      new TableRow({
        tableHeader: ri === 0,
        children: Array.from({ length: nCols }, (_, ci) =>
          new TableCell({
            width: { size: widths[ci], type: WidthType.DXA },
            shading: ri === 0
              ? { type: ShadingType.CLEAR, fill: "EDEDF2", color: "auto" }
              : undefined,
            margins: { top: 60, bottom: 60, left: 100, right: 100 },
            children: [new Paragraph({
              spacing: { before: 20, after: 20 },
              children: inline(cells[ci] || "", { size: 18, bold: ri === 0 }),
            })],
          })
        ),
      })
    ),
  });
}

// ---------- main ----------
const md = fs.readFileSync(SRC, "utf8").split(/\r?\n/);
const children = [];
let i = 0;
let figuresPlaced = 0;

function addImage(relPath) {
  const file = path.resolve(path.dirname(SRC), relPath);
  if (!fs.existsSync(file)) {
    console.error("MISSING FIGURE:", file);
    process.exitCode = 1;
    return;
  }
  figuresPlaced++;
  const { w, h } = pngSize(file);
  const width = USABLE_PX;
  const height = Math.round((h / w) * width);
  children.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 120, after: 240 },
    children: [new ImageRun({
      type: "png",
      data: fs.readFileSync(file),
      transformation: { width, height },
    })],
  }));
}

while (i < md.length) {
  const line = md[i];
  const t = line.trim();

  if (t === "" ) { i++; continue; }

  // HTML comments are build markers (e.g. the Appendix A injection points) and must
  // never reach the page.
  if (/^<!--/.test(t)) {
    while (i < md.length && !/-->/.test(md[i])) i++;
    i++; continue;
  }

  // inline figure:  ![Figure N](figures/xxx.png)
  const im = /^!\[[^\]]*\]\(([^)]+)\)$/.exec(t);
  if (im) { addImage(im[1]); i++; continue; }

  if (t === "---") {                      // horizontal rule -> bottom-bordered paragraph
    children.push(new Paragraph({
      spacing: { before: 120, after: 120 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "C8C8D0" } },
      children: [new TextRun("")],
    }));
    i++; continue;
  }

  // headings
  let hm = /^(#{1,4})\s+(.*)$/.exec(t);
  if (hm) {
    const level = hm[1].length;
    const text = hm[2];
    if (level === 1) {
      children.push(new Paragraph({
        spacing: { after: 160 },
        children: inline(text, { bold: true, size: 32 }),
      }));
    } else {
      if (/^Figures\s*$/.test(text)) inFigures = true;
      children.push(new Paragraph({
        heading: level === 2 ? HeadingLevel.HEADING_1
               : level === 3 ? HeadingLevel.HEADING_2 : HeadingLevel.HEADING_3,
        spacing: { before: 280, after: 120 },
        children: inline(text),
      }));
    }
    i++; continue;
  }

  // table
  if (t.startsWith("|")) {
    const block = [];
    while (i < md.length && md[i].trim().startsWith("|")) block.push(md[i++]);
    children.push(buildTable(block));
    children.push(new Paragraph({ spacing: { after: 160 }, children: [new TextRun("")] }));
    continue;
  }

  // blockquote (callouts) - indent + left rule
  if (t.startsWith(">")) {
    const block = [];
    while (i < md.length && md[i].trim().startsWith(">")) {
      block.push(md[i].trim().replace(/^>\s?/, ""));
      i++;
    }
    const paras = block.join("\n").split(/\n\s*\n/);
    for (const p of paras) {
      if (!p.trim()) continue;
      if (p.trim().startsWith("|")) { children.push(buildTable(p.split("\n"))); continue; }
      children.push(new Paragraph({
        indent: { left: 360 },
        spacing: { before: 80, after: 80 },
        border: { left: { style: BorderStyle.SINGLE, size: 12, color: "9A9AA6", space: 8 } },
        children: inline(p.replace(/\s*\n\s*/g, " ").trim(), { size: 20 }),
      }));
    }
    continue;
  }

  // bullet / numbered list
  let lm = /^([-*]|\d+\.)\s+(.*)$/.exec(t);
  if (lm) {
    const numbered = /\d/.test(lm[1]);
    const parts = [lm[2]];
    i++;
    while (i < md.length && /^\s{2,}\S/.test(md[i]) && !/^\s*[-*]\s/.test(md[i])) {
      parts.push(md[i].trim()); i++;
    }
    children.push(new Paragraph({
      numbering: numbered ? { reference: "num", level: 0 } : undefined,
      bullet: numbered ? undefined : { level: 0 },
      spacing: { before: 40, after: 40 },
      children: inline(parts.join(" ")),
    }));
    continue;
  }

  // paragraph (join wrapped lines)
  const parts = [t];
  i++;
  while (i < md.length && md[i].trim() !== "" && !/^[|>#-]/.test(md[i].trim())
         && !/^(\d+\.|[-*])\s/.test(md[i].trim())) {
    parts.push(md[i].trim()); i++;
  }
  const text = parts.join(" ");
  // Figure captions are set smaller and kept with the image above them.
  const isCaption = /^\*\*Figure \d+ —/.test(text);
  children.push(new Paragraph({
    spacing: { before: isCaption ? 0 : 60, after: isCaption ? 240 : 120 },
    alignment: AlignmentType.LEFT,
    indent: isCaption ? { left: 240, right: 240 } : undefined,
    children: inline(text, isCaption ? { size: 18 } : {}),
  }));
}

const doc = new Document({
  creator: "Daniel Murphy",
  title: "Adjudicating the viral auxiliary metabolic gene record",
  numbering: {
    config: [{
      reference: "num",
      levels: [{
        level: 0, format: LevelFormat.DECIMAL, text: "%1.",
        alignment: AlignmentType.START,
        style: { paragraph: { indent: { left: 460, hanging: 260 } } },
      }],
    }],
  },
  styles: {
    default: {
      document: { run: { font: "Calibri", size: 21 }, paragraph: { spacing: { line: 276 } } },
    },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 27, bold: true, color: "1A1A22" } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 23, bold: true, color: "1A1A22" } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 21, bold: true, italics: true, color: "1A1A22" } },
    ],
  },
  sections: [{
    properties: {
      page: {
        size: { width: PAGE_W, height: PAGE_H, orientation: PageOrientation.PORTRAIT },
        margin: { top: MARGIN, bottom: MARGIN, left: MARGIN, right: MARGIN },
      },
    },
    children,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  try {
    fs.writeFileSync(OUT, buf);
  } catch (e) {
    if (e.code === "EBUSY") {
      console.error("\nCANNOT WRITE: " + OUT);
      console.error("The file is open in Word. Close it and re-run.\n");
      process.exit(2);
    }
    throw e;
  }
  console.log("wrote", OUT, (buf.length / 1024).toFixed(0) + " KB");
  console.log("blocks:", children.length, "| figures placed:", figuresPlaced);
  if (figuresPlaced !== 4) {
    console.error("EXPECTED 4 FIGURES, PLACED " + figuresPlaced);
    process.exitCode = 1;
  }
});
