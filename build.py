"""Builds the ebook: src/*.md -> book.html -> PDF (A4 and US Letter) via Chromium.

Markdown extras:
  :::prompt Title            dark copy-ready prompt card (text kept verbatim)
  :::tip / :::warn / :::note callouts (markdown inside)
  :::figure file.svg | caption
  :::part 1 | Title | subtitle   full-page part opener
Also writes dist/prompts.md: every prompt card, for buyers who want plain text.
"""
import glob, html, json, os, re, subprocess, sys
import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC, DIST = os.path.join(ROOT, "src"), os.path.join(ROOT, "dist")
os.makedirs(DIST, exist_ok=True)
prompts = []


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def block(kind, arg, body):
    if kind == "prompt":
        prompts.append((arg, body.strip()))
        n = len(prompts)
        return (f'<div class="prompt" id="prompt-{n}"><div class="prompt-head"><span class="prompt-label">PROMPT {n:02d}</span>'
                f'<span class="prompt-title">{html.escape(arg)}</span></div><div class="prompt-body">{html.escape(body.strip())}</div></div>')
    if kind in ("tip", "warn", "note"):
        label = {"tip": "Tip", "warn": "Watch out", "note": "Good to know"}[kind]
        inner = markdown.markdown(body, extensions=["tables", "sane_lists"])
        return f'<div class="callout {kind}"><div class="callout-label">{label}</div>{inner}</div>'
    if kind == "figure":
        f, _, cap = arg.partition("|")
        svg = open(os.path.join(ROOT, "svg", f.strip())).read()
        return f'<figure class="fig">{svg}<figcaption>{html.escape(cap.strip())}</figcaption></figure>'
    if kind == "part":
        num, title, sub = [x.strip() for x in (arg.split("|") + ["", ""])[:3]]
        return (f'<section class="part" id="part-{num}"><div class="part-num">Part {num}</div>'
                f'<h1 class="part-title">{html.escape(title)}</h1><p class="part-sub">{html.escape(sub)}</p></section>')
    if kind == "raw":
        return body
    raise ValueError(kind)


def render_md(text):
    out, parts = [], re.split(r"^:::(\w+)[ \t]*(.*)$", text, flags=re.M)
    # parts: [md, kind, arg, rest, kind, arg, rest...]; a block runs until a line ':::'
    md_buf = parts[0]
    i = 1
    while i < len(parts):
        kind, arg, rest = parts[i], parts[i + 1], parts[i + 2]
        if kind in ("figure", "part"):
            body, after = "", rest
        else:
            body, _, after = rest.partition("\n:::")
            after = after.split("\n", 1)[1] if "\n" in after else ""
        out.append(markdown.markdown(md_buf, extensions=["tables", "sane_lists", "attr_list", "fenced_code"]))
        out.append(block(kind, arg.strip(), body))
        md_buf = after
        i += 3
    out.append(markdown.markdown(md_buf, extensions=["tables", "sane_lists", "attr_list", "fenced_code"]))
    return "\n".join(out)


def main():
    chapters, toc = [], []
    for path in sorted(glob.glob(os.path.join(SRC, "*.md"))):
        h = render_md(open(path, encoding="utf-8").read())
        # chapter titles (h2) get ids + go into the table of contents
        def add_id(m):
            title = re.sub("<[^>]+>", "", m.group(1)); sid = slug(title)
            toc.append((sid, title)); return f'<h2 id="{sid}">{m.group(1)}</h2>'
        h = re.sub(r"<h2>(.*?)</h2>", add_id, h)
        for m in re.finditer(r'<section class="part" id="(part-\d+)"><div class="part-num">Part (\d+)</div><h1 class="part-title">(.*?)</h1>', h):
            toc.append((m.group(1), f"PART {m.group(2)} · {html.unescape(m.group(3))}"))
        chapters.append(h)
    # order toc as it appears in the text
    full = "\n".join(chapters)
    order = {sid: full.find(f'id="{sid}"') for sid, _ in toc}
    toc.sort(key=lambda x: order[x[0]])
    def find_text(t):
        return t.split(" · ", 1)[1] if t.startswith("PART ") else t
    toc_html = "".join(
        f'<li class="{"toc-part" if t.startswith("PART ") else "toc-ch"}"><a href="#{sid}" data-find="{html.escape(find_text(t))}"><span>{html.escape(t)}</span><span class="pn"></span></a></li>' for sid, t in toc)
    tpl = open(os.path.join(ROOT, "template.html"), encoding="utf-8").read()
    cover = open(os.path.join(ROOT, "svg", "cover.svg"), encoding="utf-8").read() if os.path.exists(os.path.join(ROOT, "svg", "cover.svg")) else ""
    book = tpl.replace("{{TOC}}", toc_html).replace("{{BODY}}", full).replace("{{COVER}}", cover)
    open(os.path.join(ROOT, "book.html"), "w", encoding="utf-8").write(book)
    with open(os.path.join(DIST, "prompt-library.md"), "w", encoding="utf-8") as f:
        f.write("# Prompt to Reel — Prompt Library\n\nEvery prompt from the book, ready to copy. Replace the [BRACKETS] with your own details.\n\n")
        for n, (t, b) in enumerate(prompts, 1):
            f.write(f"## {n:02d} · {t}\n\n```text\n{b}\n```\n\n")
    print(f"{len(toc)} toc entries, {len(prompts)} prompts")
    if "--pdf" in sys.argv:
        subprocess.run(["node", os.path.join(ROOT, "pdf.mjs")], check=True)


if __name__ == "__main__":
    main()
