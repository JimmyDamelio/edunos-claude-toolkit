import { chromium } from 'playwright';
const b = await chromium.launch();
const ctx = await b.newContext({ viewport: { width: 1280, height: 900 } });
const p = await ctx.newPage();
p.on('pageerror', e => console.log('[pageerror]', e.message));
await p.goto('https://edunosstudio.gumroad.com/l/prompt-to-reel', { waitUntil: 'domcontentloaded', timeout: 60000 });
await p.waitForTimeout(6000);
console.log('title:', await p.title(), '| url:', p.url());
let target = null;
for (const f of p.frames()) {
  const n = await f.locator('[data-gumroad-action="buy"]').count().catch(() => 0);
  const price = n ? await f.locator('[data-gumroad-field="price"]').first().textContent().catch(() => '') : '';
  console.log('frame', f.url().slice(0, 80), '| buy elements:', n, '| price text:', price);
  if (n && !target) target = f;
}
await p.screenshot({ path: 'live-top.png' });
if (!target) { console.log('NO BUY ELEMENT FOUND'); await b.close(); process.exit(1); }
const before = p.url();
await target.locator('.hero [data-gumroad-action="buy"]').first().click();
await p.waitForTimeout(7000);
console.log('after click url:', p.url(), '| changed:', p.url() !== before);
const pages = ctx.pages(); console.log('open pages:', pages.length, pages.map(x => x.url().slice(0, 90)));
const last = pages[pages.length - 1];
await last.screenshot({ path: 'live-checkout.png' });
const txt = (await last.locator('body').innerText().catch(() => '')).slice(0, 800).replace(/\s+/g, ' ');
console.log('checkout text:', txt);
await b.close();
