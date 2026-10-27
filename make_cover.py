"""Cover art (svg/cover.svg): fills A4 or Letter (slice)."""
W, H = 1000, 1414
phones = [("assets/gallery/mercy-22.jpg", 120, 830, -8), ("assets/gallery/sleep-2.4.jpg", 380, 760, 0), ("assets/gallery/sleep-35.jpg", 640, 830, 8)]
ph = ""
for img, x, y, rot in phones:
    w, h = 250, 444
    ph += (f'<g transform="rotate({rot} {x+w/2} {y+h/2})"><rect x="{x-10}" y="{y-10}" width="{w+20}" height="{h+20}" rx="34" fill="#0B0A18" stroke="#3A3660" stroke-width="2"/>'
           f'<clipPath id="c{x}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="26"/></clipPath>'
           f'<image href="{img}" x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid slice" clip-path="url(#c{x})"/></g>')
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice">
<defs>
<radialGradient id="o1" cx="80%" cy="12%" r="55%"><stop offset="0" stop-color="#6B4EFF" stop-opacity=".75"/><stop offset="1" stop-color="#6B4EFF" stop-opacity="0"/></radialGradient>
<radialGradient id="o2" cx="10%" cy="78%" r="50%"><stop offset="0" stop-color="#FF5A3C" stop-opacity=".55"/><stop offset="1" stop-color="#FF5A3C" stop-opacity="0"/></radialGradient>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset=".55" stop-color="#141327" stop-opacity="0"/><stop offset="1" stop-color="#141327" stop-opacity=".95"/></linearGradient>
<pattern id="grid" width="50" height="50" patternUnits="userSpaceOnUse"><path d="M50 0H0V50" fill="none" stroke="#fff" stroke-opacity=".04"/></pattern>
</defs>
<rect width="{W}" height="{H}" fill="#141327"/><rect width="{W}" height="{H}" fill="url(#grid)"/>
<rect width="{W}" height="{H}" fill="url(#o1)"/><rect width="{W}" height="{H}" fill="url(#o2)"/>
<text x="80" y="150" font-family="Grotesk" font-weight="700" font-size="22" letter-spacing="7" fill="#F2A20C">THE COMPLETE BEGINNER'S GUIDE</text>
<text x="76" y="290" font-family="Grotesk" font-weight="700" font-size="138" fill="#fff" letter-spacing="-3">Prompt</text>
<text x="80" y="420" font-family="Serif" font-style="italic" font-size="150" fill="#B9A9FF">to Reel</text>
<text x="82" y="500" font-family="Grotesk" font-weight="500" font-size="31" fill="#E9E6F5">Make scroll-stopping animated videos</text>
<text x="82" y="542" font-family="Grotesk" font-weight="500" font-size="31" fill="#E9E6F5">with Claude, no editing skills needed.</text>
<g font-family="Grotesk" font-weight="700" font-size="20">
<rect x="80" y="600" width="270" height="52" rx="26" fill="#FF5A3C"/><text x="215" y="633" text-anchor="middle" fill="#fff">56 copy-paste prompts</text>
<rect x="365" y="600" width="230" height="52" rx="26" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="2"/><text x="480" y="633" text-anchor="middle" fill="#fff">Step-by-step setup</text>
<rect x="610" y="600" width="210" height="52" rx="26" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="2"/><text x="715" y="633" text-anchor="middle" fill="#fff">Free starter kit</text>
</g>
<g transform="translate(80 690)"><rect width="560" height="64" rx="16" fill="#fff" fill-opacity=".08" stroke="#fff" stroke-opacity=".15"/>
<text x="24" y="41" font-family="Mono" font-weight="600" font-size="19" fill="#E9E6F5">› Make a 30 s 9:16 reel about…</text>
<rect x="470" y="14" width="70" height="36" rx="10" fill="#6B4EFF"/><text x="505" y="39" text-anchor="middle" font-family="Grotesk" font-weight="700" font-size="18" fill="#fff">Go</text></g>
{ph}
<rect width="{W}" height="{H}" fill="url(#fade)"/>
<text x="500" y="1360" text-anchor="middle" font-family="Grotesk" font-weight="500" font-size="20" letter-spacing="4" fill="#CFCBE0">REELS · TRAILERS · EXPLAINERS · ANIMATED ADS</text>
</svg>'''
open("svg/cover.svg", "w").write(svg)
