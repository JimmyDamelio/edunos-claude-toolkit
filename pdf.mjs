// book.html -> dist/Prompt-to-Reel-A4.pdf and -Letter.pdf. Two passes: the second fills the TOC page numbers.
import { chromium } from 'playwright';
import { execFileSync } from 'child_process';
import path from 'path';
import { fileURLToPath } from 'url';
const dir = path.dirname(fileURLToPath(import.meta.url));
const norm = s => s.replace(/[’']/g, "'").replace(/\s+/g, ' ').trim().toLowerCase();
const b = await chromium.launch({ args: ['--allow-file-access-from-files'] });
for (const [name, size, h] of [['A4', 'A4', '297mm'], ['Letter', 'letter', '279.4mm']]) {
  const p = await b.newPage();
  await p.goto('file://' + path.join(dir, 'book.html'), { waitUntil: 'networkidle' });
  await p.addStyleTag({ content: `@page{size:${size}} :root{--page-h:${h}}` });
  await p.evaluate(() => document.fonts.ready);
  const out = path.join(dir, 'dist', `Prompt-to-Reel-${name}.pdf`);
  const opts = { path: out, preferCSSPageSize: true, printBackground: true, tagged: true, outline: true };
  await p.pdf(opts);
  const pages = execFileSync('pdftotext', ['-layout', out, '-']).toString().split('\f').map(norm);
  const finds = await p.evaluate(() => [...document.querySelectorAll('.toc a')].map(a => a.dataset.find));
  let from = 2;
  const nums = finds.map(f => { const i = pages.findIndex((pg, k) => k >= from && pg.includes(f.toLowerCase().replace(/\s+/g, ' '))); if (i >= 0) from = i; return i >= 0 ? i + 1 : ''; });
  await p.evaluate(n => document.querySelectorAll('.toc .pn').forEach((s, i) => s.textContent = n[i]), nums);
  await p.pdf(opts);
  console.log('pdf', name, 'toc pages', nums.join(','));
  await p.close();
}
await b.close();
