"""landing.src.html -> landing.html: inline images as data URIs, comment bubbles, product cover URL."""
import base64, os, re, sys
H = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(H, "landing.src.html"), encoding="utf-8").read()
def img(name):
    return "data:image/jpeg;base64," + base64.b64encode(open(os.path.join(H, "img", name + ".jpg"), "rb").read()).decode()
src = re.sub(r"\{\{IMG:([\w.\-]+)\}\}", lambda m: img(m.group(1)), src)
cols = ["#E8492C", "#5B3FE8", "#B97800", "#0E8A69"]
def bubbles(items):
    return "".join(f'<span class="bubble"><i style="background:{cols[k % 4]}"></i>{t}</span>' for k, t in enumerate(items))
src = src.replace("{{BUBBLES}}", bubbles(["What app is this??", "tutorial please", "how do you make these", "which app?!", "teach me", "I NEED this"]))
src = src.replace("{{BUBBLES2}}", bubbles(["what software??", "how long did this take?", "is this After Effects?", "drop the tutorial", "this is so clean", "how??"]))
cover = sys.argv[1] if len(sys.argv) > 1 else ""
wide = sys.argv[2] if len(sys.argv) > 2 else ""
src = src.replace("{{COVERWIDE}}", wide) if wide else re.sub(r'\s*<img src="\{\{COVERWIDE\}\}"[^>]*>', "", src)
src = src.replace("{{COVER}}", cover) if cover else re.sub(r'\s*<img class="cover-chip"[^>]*>', "", src)
open(os.path.join(H, "landing.html"), "w", encoding="utf-8").write(src)
print("landing.html", len(src) // 1024, "KB", "(cover url set)" if cover else "(no cover url)")
