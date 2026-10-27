import { chromium } from 'playwright';
const b = await chromium.launch();
for (const [name, w, h, scheme] of [['desktop-light', 1280, 800, 'light'], ['desktop-dark', 1280, 800, 'dark'], ['mobile', 390, 844, 'light']]) {
  const p = await b.newPage({ viewport: { width: w, height: h }, colorScheme: scheme });
  p.on('pageerror', e => console.log('[error]', e.message));
  await p.goto('file://' + process.cwd() + '/landing.html'); await p.waitForTimeout(1500);
  await p.evaluate(() => { document.querySelectorAll('.reveal,.bar').forEach(el => { el.classList.add('in'); if (el.dataset.w) el.style.width = `calc(${el.dataset.w}% * .78)`; }); });
  await p.waitForTimeout(1300);
  await p.screenshot({ path: `shot-${name}.png`, fullPage: true });
  const ow = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth); console.log(name, 'horizontal overflow px:', ow);
}
await b.close();
