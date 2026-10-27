import { chromium } from 'playwright';
const b = await chromium.launch({ args: ['--allow-file-access-from-files'] });
const p = await b.newPage({ viewport: { width: 1300, height: 1400 }, deviceScaleFactor: 2 });
await p.goto('file://' + process.cwd() + '/gumroad-art.html'); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
await p.locator('#cover').screenshot({ path: 'gumroad-cover.png' });
await p.locator('#thumb').screenshot({ path: 'gumroad-thumbnail.png' });
await b.close();
