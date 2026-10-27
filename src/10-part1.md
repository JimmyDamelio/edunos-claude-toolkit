:::part 1 | Understand the magic | Five minutes of theory that will save you hours of trial and error.

## How Claude makes a *video*

<p class="lead">Claude doesn't "generate" a video the way image AIs do. It builds one, frame by frame, like a tiny animation studio.</p>

When you ask Claude Code for a video, it works like a team of specialists who never get tired:

:::figure pipeline.svg | The five stages Claude goes through for every video you request.

1. **The director** turns your request into a **storyboard**: scenes, timings, on-screen text, sound cues.
2. **The animator** writes a web page that can draw *any moment* of the film. Ask it for second 12.4 and it draws exactly that frame. This is what makes the result smooth and precise.
3. **The camera** is a hidden web browser that visits that page and takes a picture of every frame: 30 per second, so a 60-second reel is 1,800 pictures.
4. **The sound team** builds the audio: a voice-over from a text-to-speech model, real recorded sound effects, a synthesised score, or silence and ambience.
5. **The editor** (a free tool called ffmpeg) stitches the pictures and the sound into one MP4 file.

Along the way, Claude **looks at its own work**. It renders a few key frames, inspects them like a picture, notices that a title overlaps an image or that text is hard to read, fixes it and checks again. With the right tools it can even *listen* to the soundtrack and critique it.

### Why this beats editing apps

| | Editing app | Claude + code |
|---|---|---|
| Learning curve | Weeks | Minutes, you describe it |
| Changing a colour everywhere | Re-edit every clip | One sentence |
| Making 10 versions | 10× the work | "Now make it 9:16, 1:1 and 16:9" |
| Consistency across a series | Hard | Perfect: same code, new text |
| Cost per video | Your time | A slice of your Claude plan |

### What it's great at, and what it isn't

**Great:** motion graphics, kinetic typography, illustrated characters (faceless "pill people", mascots, icons), explainers, charts, maps, product mock-ups, 2D and stylised 3D, art styles, lyric videos, subtitles, sound design.

**Not great:** photorealistic people and real-world footage. If you need those, film them or use a dedicated video-generation tool, and you can still ask Claude to edit, caption and brand them.

:::tip
Think "animated", not "filmed". The most viral faceless accounts use exactly the styles Claude is best at.
:::

## What you *need*

<p class="lead">Three accounts, one browser, zero installs.</p>

### 1. A Claude plan that includes Claude Code in the cloud

You'll use **Claude Code on the web** at <a href="https://claude.ai/code">claude.ai/code</a>. Cloud sessions are available on the paid **Pro**, **Max** and **Team** plans (and some Enterprise seats). Check current prices and what each plan includes at <a href="https://claude.com/pricing">claude.com/pricing</a>.

- **Pro** is enough to start and learn.
- **Max** gives much more room if you plan to produce several videos a day: video work is long, detailed work.

Everything runs on Anthropic's computers in the cloud, so your laptop's speed doesn't matter. An old PC works perfectly; it only needs a browser.

### 2. A free GitHub account

GitHub is where your projects live. Think of it as a **Google Drive for projects**. Claude's cloud sessions are wiped when they end, so anything worth keeping (your videos, your templates, your settings) gets saved to GitHub. Part 2 shows you how to create an account in five minutes.

### 3. The starter kit (free, included)

This book comes with a ready-made **starter kit**: a collection of skills (instruction packs for Claude), video templates and an installer, all assembled from excellent open-source projects. You'll install it in one line.

### Optional

- An **Instagram, TikTok or YouTube** account to publish to.
- An **ElevenLabs** account if you ever want premium voices (the free voices in this book are already good).

:::note
**What's a "skill"?** A skill is a folder of instructions and tools that teaches Claude a specialised job, like "how to place sound effects on a video" or "the rules of good motion design". Claude loads the right skill automatically when your request needs it.
:::

### The words you'll see (mini glossary)

| Word | What it means for you |
|---|---|
| **Repository (repo)** | A project folder on GitHub. Your "studio" will be one repo. |
| **Session** | One conversation with Claude Code, running on its own cloud computer. |
| **Environment** | The saved settings for those cloud computers: internet access and a startup script. |
| **Setup script** | A few lines that run when a session starts, used here to install the starter kit. |
| **Render** | The moment Claude draws every frame and builds the MP4. |
| **Push** | Claude saving files to your GitHub repo. |
| **Context** | Claude's working memory for one conversation. It fills up over long sessions. |
