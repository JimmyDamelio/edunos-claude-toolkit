"""Draws the book's schematic screen illustrations into svg/ (simplified, brand-styled, not screenshots)."""
import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

INK, INK2, MUTED, LINE, SOFT, PAPER = "#17161F", "#4A4757", "#8B8796", "#E2DCD2", "#F3EEE6", "#FFFFFF"
CORAL, VIOLET, MINT, AMBER, NIGHT, GH = "#FF5A3C", "#6B4EFF", "#13A57F", "#F2A20C", "#141327", "#1F883D"
FONT = "font-family=\"Grotesk, Inter, sans-serif\""
MONO = "font-family=\"Mono, monospace\""


def svg(w, h, body, bg="#F6F2EC"):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img">'
            f'<rect width="{w}" height="{h}" rx="22" fill="{bg}"/>{body}</svg>')


def t(x, y, s, size=22, color=INK, weight=500, anchor="start", font=FONT, extra=""):
    s = s.replace("&", "&amp;").replace("<", "&lt;")
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}" {font} {extra}>{s}</text>'


def browser(x, y, w, h, url):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{PAPER}" stroke="{LINE}" stroke-width="2"/>'
            f'<path d="M{x} {y+16} a16 16 0 0 1 16 -16 h{w-32} a16 16 0 0 1 16 16 v40 h-{w} z" fill="#EFEAE2"/>'
            + "".join(f'<circle cx="{x+28+i*22}" cy="{y+28}" r="7" fill="{c}"/>' for i, c in enumerate(["#FF6159", "#FFBD2E", "#28C941"]))
            + f'<rect x="{x+110}" y="{y+13}" width="{w-140}" height="30" rx="15" fill="{PAPER}" stroke="{LINE}"/>'
            + t(x + 130, y + 34, url, 17, INK2, 500, font=MONO))


def badge(x, y, n, color=CORAL):
    return f'<circle cx="{x}" cy="{y}" r="19" fill="{color}"/>' + t(x, y + 7, str(n), 20, "#fff", 700, "middle")


def field(x, y, w, label, value="", h=46, focus=False):
    return (t(x, y - 10, label, 17, INK2, 700)
            + f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#fff" stroke="{VIOLET if focus else "#CFC8BC"}" stroke-width="{3 if focus else 2}"/>'
            + (t(x + 14, y + h / 2 + 7, value, 18, INK, 500, font=MONO) if value else ""))


def button(x, y, w, label, color=GH, h=48, tc="#fff"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{color}"/>' + t(x + w / 2, y + h / 2 + 7, label, 19, tc, 700, "middle")


def note(x, y, s):
    return t(x, y, s, 15, MUTED, 500, extra='font-style="italic"')


def save(name, content):
    open(os.path.join(OUT, name), "w").write(content)


# 1. pipeline -----------------------------------------------------------
steps = [("Storyboard", "scenes, timings, text", VIOLET), ("Animate", "code draws any frame", CORAL), ("Capture", "30 frames / second", AMBER), ("Sound", "voice, effects, ambience", MINT), ("Assemble", "ffmpeg → MP4", INK)]
body = ""
for i, (a, b, c) in enumerate(steps):
    x = 40 + i * 310
    body += f'<rect x="{x}" y="70" width="270" height="250" rx="22" fill="#fff" stroke="{LINE}" stroke-width="2"/>'
    body += f'<circle cx="{x+135}" cy="150" r="50" fill="{c}" opacity=".14"/><circle cx="{x+135}" cy="150" r="30" fill="{c}"/>'
    body += t(x + 135, 159, str(i + 1), 26, "#fff", 700, "middle")
    body += t(x + 135, 245, a, 28, INK, 700, "middle") + t(x + 135, 280, b, 18, INK2, 500, "middle")
    if i < 4:
        body += f'<path d="M{x+280} 195 l22 0 m-9 -9 l9 9 l-9 9" stroke="{MUTED}" stroke-width="3" fill="none" stroke-linecap="round"/>'
body += t(800, 380, "Claude checks its own work between every stage: stills, contact sheets and even the audio.", 18, MUTED, 500, "middle", extra='font-style="italic"')
save("pipeline.svg", svg(1600, 420, body))

# 2. GitHub sign-up ------------------------------------------------------
b = browser(40, 30, 1520, 700, "github.com/signup")
b += f'<rect x="40" y="86" width="1520" height="644" fill="#0D1117"/>'
b += t(800, 170, "Welcome to GitHub!", 38, "#fff", 700, "middle") + t(800, 210, "Let's begin the adventure", 20, "#8B949E", 500, "middle")
for i, (lab, val) in enumerate([("Email", "you@example.com"), ("Password", "••••••••••••"), ("Username", "yourbrand")]):
    y = 280 + i * 110
    b += t(560, y - 12, lab, 18, "#C9D1D9", 700) + f'<rect x="560" y="{y}" width="480" height="50" rx="8" fill="#0D1117" stroke="#30363D" stroke-width="2"/>' + t(578, y + 33, val, 19, "#C9D1D9", 500, font=MONO)
    b += badge(530, y + 25, i + 1 if i < 2 else 2)
b += button(560, 615, 480, "Create account / Continue", GH)
b += badge(530, 639, 3)
b += note(800, 715, "Then solve the puzzle and enter the code GitHub emails you.").replace('fill="#8B8796"', 'fill="#8B949E"').replace('text-anchor="start"', 'text-anchor="middle"')
save("github-signup.svg", svg(1600, 760, b))

# 3. New repository -------------------------------------------------------
b = browser(40, 30, 1520, 820, "github.com/new")
b += t(140, 150, "Create a new repository", 34, INK, 700) + f'<line x1="140" y1="180" x2="1460" y2="180" stroke="{LINE}" stroke-width="2"/>'
b += field(140, 235, 300, "Owner", "yourbrand") + t(455, 268, "/", 30, MUTED, 500)
b += field(480, 235, 520, "Repository name *", "my-video-studio", focus=True) + badge(1035, 258, 2)
b += t(140, 345, "Description (optional)", 17, INK2, 700) + f'<rect x="140" y="355" width="860" height="46" rx="8" fill="#fff" stroke="#CFC8BC" stroke-width="2"/>'
for i, (lab, sub, on) in enumerate([("Public", "Anyone on the internet can see this repository", False), ("Private", "You choose who can see and commit to this repository", True)]):
    y = 460 + i * 70
    b += f'<circle cx="160" cy="{y}" r="12" fill="#fff" stroke="{VIOLET if on else "#9C968C"}" stroke-width="3"/>' + (f'<circle cx="160" cy="{y}" r="6" fill="{VIOLET}"/>' if on else "")
    b += t(186, y - 2, lab, 21, INK, 700) + t(186, y + 24, sub, 16, MUTED, 500)
b += badge(1035, 530, 3)
b += f'<rect x="148" y="640" width="24" height="24" rx="5" fill="{VIOLET}"/><path d="M153 652 l6 6 l10 -12" stroke="#fff" stroke-width="3.5" fill="none" stroke-linecap="round"/>'
b += t(186, 660, "Add a README file", 21, INK, 700) + t(186, 686, "This is where you can write a long description for your project.", 16, MUTED, 500) + badge(1035, 655, 4)
b += button(140, 740, 260, "Create repository", GH) + badge(430, 764, 5)
save("github-newrepo.svg", svg(1600, 880, b))

# 4. Connect flow ---------------------------------------------------------
b = ""
cards = [
    (40, "claude.ai/code", "Sign in, then follow the prompt to connect GitHub", [("Connect GitHub", VIOLET)]),
    (560, "github.com · Authorize", "Approve access for Claude", [("Authorize", GH)]),
    (1080, "Claude GitHub App", "Only select repositories", [("Install", GH)]),
]
for i, (x, head, sub, btns) in enumerate(cards):
    b += f'<rect x="{x}" y="60" width="480" height="420" rx="22" fill="#fff" stroke="{LINE}" stroke-width="2"/>'
    b += f'<rect x="{x}" y="60" width="480" height="70" rx="22" fill="{NIGHT if i == 0 else "#24292F"}"/><rect x="{x}" y="100" width="480" height="30" fill="{NIGHT if i == 0 else "#24292F"}"/>'
    b += t(x + 30, 105, head, 21, "#fff", 700, font=MONO)
    b += t(x + 30, 185, sub, 19, INK2, 500)
    if i == 2:
        b += f'<rect x="{x+30}" y="215" width="420" height="120" rx="10" fill="{SOFT}"/>'
        b += f'<circle cx="{x+56}" cy="245" r="9" fill="#fff" stroke="#9C968C" stroke-width="2.5"/>' + t(x + 76, 252, "All repositories", 18, MUTED, 500)
        b += f'<circle cx="{x+56}" cy="285" r="9" fill="#fff" stroke="{VIOLET}" stroke-width="3"/><circle cx="{x+56}" cy="285" r="4.5" fill="{VIOLET}"/>' + t(x + 76, 292, "Only select repositories", 18, INK, 700)
        b += f'<rect x="{x+76}" y="305" width="250" height="24" rx="12" fill="#fff" stroke="{VIOLET}"/>' + t(x + 90, 323, "✓ my-video-studio", 15, VIOLET, 700, font=MONO)
    for label, col in btns:
        b += button(x + 30, 395, 420, label, col)
    b += badge(x + 460, 60, i + 1 if i == 0 else i + 1)
    if i < 2:
        b += f'<path d="M{x+490} 270 l50 0 m-12 -12 l12 12 l-12 12" stroke="{MUTED}" stroke-width="3.5" fill="none" stroke-linecap="round"/>'
b += t(800, 540, "Pro and Max: a \"Default\" environment is then created for you automatically.", 19, MUTED, 500, "middle", extra='font-style="italic"')
save("connect-flow.svg", svg(1600, 580, b))

# 5. Environment dialog ---------------------------------------------------
b = browser(40, 30, 1520, 900, "claude.ai/code")
b += t(800, 160, "What should Claude work on?", 30, INK, 700, "middle")
b += f'<rect x="300" y="190" width="1000" height="120" rx="18" fill="#fff" stroke="#CFC8BC" stroke-width="2"/>' + t(330, 235, "Describe a task…", 20, MUTED, 500)
for i, (lab, w, col) in enumerate([("☁ Default ▾", 170, VIOLET), ("my-video-studio ▾", 220, INK2), ("Accept edits ▾", 180, INK2)]):
    x = 320 + sum([190, 240, 200][:i])
    b += f'<rect x="{x}" y="325" width="{w}" height="40" rx="20" fill="{SOFT if i else "#ECE8FF"}" stroke="{col if i == 0 else LINE}" stroke-width="2"/>' + t(x + w / 2, 351, lab, 16, col, 700, "middle")
b += badge(310, 345, 1)
# dialog
b += f'<rect x="40" y="86" width="1520" height="844" fill="#17161F" opacity=".35"/>'
b += f'<rect x="380" y="300" width="840" height="590" rx="20" fill="#fff"/>'
b += t(420, 355, "Edit environment · Default", 26, INK, 700)
rows = [("Name", "Default", None), ("Network access", "Full", 2), ("Setup script", "git clone --depth 1 https://github.com/…/claude-video-starter-kit /tmp/kit && sh /tmp/kit/install.sh", 3), ("Environment variables", "—", None)]
for i, (lab, val, n) in enumerate(rows):
    y = 395 + i * 105
    b += f'<rect x="420" y="{y}" width="760" height="85" rx="12" fill="{SOFT}"/>'
    b += t(445, y + 34, lab, 19, INK, 700) + t(445, y + 64, val if len(val) < 70 else val[:66] + "…", 15 if i == 2 else 18, VIOLET if n else INK2, 600, font=MONO if i == 2 else FONT)
    b += t(1155, y + 50, "›", 30, MUTED, 500, "end")
    if n:
        b += badge(1210, y + 42, n)
b += button(960, 820, 220, "Save changes", VIOLET) + badge(1210, 844, 4)
save("env-dialog.svg", svg(1600, 960, b))

# 6. Download from GitHub -------------------------------------------------
b = browser(40, 30, 1520, 430, "github.com/yourbrand/my-video-studio/blob/main/videos/my-first-reel.mp4")
b += t(100, 140, "my-video-studio / videos / my-first-reel.mp4", 22, INK, 700, font=MONO)
b += f'<rect x="100" y="170" width="1400" height="64" rx="10" fill="{SOFT}" stroke="{LINE}"/>' + t(125, 210, "8.4 MB", 18, INK2, 600)
for i, lab in enumerate(["Raw", "⧉", "⤓"]):
    x = 1230 + i * 85
    b += f'<rect x="{x}" y="180" width="70" height="44" rx="8" fill="#fff" stroke="{CORAL if i == 2 else LINE}" stroke-width="{3 if i == 2 else 2}"/>' + t(x + 35, 209, lab, 20, CORAL if i == 2 else INK2, 700, "middle")
b += badge(1490, 160, 1) + t(1110, 290, "Download raw file", 20, CORAL, 700, "middle")
b += f'<rect x="100" y="260" width="300" height="160" rx="10" fill="#0D1117"/>' + t(250, 350, "▶", 46, "#fff", 700, "middle")
save("github-download.svg", svg(1600, 490, b))
print("svgs:", sorted(os.listdir(OUT)))
