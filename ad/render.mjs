// usage: node render.mjs cues | stills 1 3.2 ... | frames [fps] [workers]
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const dir = path.dirname(fileURLToPath(import.meta.url));
const url = 'file://' + path.join(dir, 'film.html');
const [mode, ...rest] = process.argv.slice(2);
const DURATION = 32.5;

const browser = await chromium.launch({ args: ['--allow-file-access-from-files'] });
async function openPage() {
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  page.on('pageerror', e => console.log('[error]', e.message));
  await page.goto(url);
  await page.evaluate(() => window.ready);
  return page;
}
async function grab(page, t, file) {
  const b64 = await page.evaluate(t => { renderAt(t); return document.getElementById('c').toDataURL('image/png').split(',')[1]; }, t);
  fs.writeFileSync(file, Buffer.from(b64, 'base64'));
}

if (mode === 'cues') {
  const page = await openPage();
  fs.writeFileSync(path.join(dir, 'cues.json'), JSON.stringify(await page.evaluate(() => window.CUES), null, 1));
} else if (mode === 'stills') {
  fs.mkdirSync(path.join(dir, 'stills'), { recursive: true });
  const page = await openPage();
  for (const t of rest.map(Number)) await grab(page, t, path.join(dir, 'stills', `t_${t.toFixed(2).padStart(5, '0')}.png`));
} else {
  const fps = +(rest[0] || 30), workers = +(rest[1] || 6), total = Math.round(DURATION * fps);
  const out = path.join(dir, 'frames'); fs.mkdirSync(out, { recursive: true });
  let next = 0;
  await Promise.all(Array.from({ length: workers }, async () => {
    const page = await openPage();
    while (next < total) { const i = next++; await grab(page, i / fps, path.join(out, `f_${String(i).padStart(5, '0')}.png`)); }
  }));
}
await browser.close();
