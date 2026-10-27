:::part 2 | Set up your studio | A one-time, 30-minute setup. Keep this PDF open next to your browser and follow along.

## Step 1 · Create your *GitHub* account

<p class="lead">Skip this chapter if you already have one.</p>

:::figure github-signup.svg | Simplified illustration of GitHub's sign-up page.

1. Go to **<a href="https://github.com/signup">github.com/signup</a>**.
2. Enter your **email**, choose a **password** and pick a **username**.
3. Solve the quick puzzle that proves you're human, then type the **code GitHub emails you**.
4. If GitHub asks a few questions about how you'll use it, answer anything, or skip. Choose the **Free** plan: it's all you need.

:::tip
Your username appears in your project links (github.com/**yourname**/...). If you create content, pick something close to your brand name.
:::

:::note
Add **two-factor authentication** (Settings → Password and authentication) once you're set up. It takes two minutes and protects everything you build.
:::

## Step 2 · Create your *studio* repository

<p class="lead">One project folder where all your videos, templates and brand settings will live.</p>

:::figure github-newrepo.svg | Simplified illustration of the "Create a new repository" form.

1. Go to **<a href="https://github.com/new">github.com/new</a>**.
2. **Repository name:** `my-video-studio` (or any name you like).
3. Choose **Private**: only you will see it.
4. Tick **Add a README file**. Claude Code works with existing repositories, and the README makes sure yours isn't empty.
5. Click **Create repository**. Done.

:::tip
Later, you can make one repo per brand or per account, for example `faith-reels` and `shop-ads`, each with its own style settings. Start with one.
:::

## Step 3 · Connect *Claude Code* to GitHub

<p class="lead">This is where most beginners get stuck. Go slowly; you only do it once.</p>

1. Go to **<a href="https://claude.ai/code">claude.ai/code</a>** and sign in with your Claude account.
2. Claude Code asks you to **connect GitHub**. Follow the prompt: it opens GitHub's authorization page. Click **Authorize**, and GitHub sends you back to Claude Code.
3. Install the **Claude GitHub App** so Claude can work in your *private* studio repo. If onboarding offers it, accept. If not, open **<a href="https://github.com/apps/claude/installations/new">github.com/apps/claude/installations/new</a>**.
4. On the installation page, choose your account, then **Only select repositories**, pick `my-video-studio`, and click **Install**.
5. Back on claude.ai/code: on Pro and Max plans, Claude Code creates an environment called **Default** for you automatically. (On Team plans, a short form appears: keep the defaults and click **Create & finish**.)

:::figure connect-flow.svg | The connection flow: claude.ai/code ⇄ GitHub authorization ⇄ Claude GitHub App on your studio repo.

:::warn
**"My repository doesn't appear!"** This almost always means the Claude GitHub App isn't installed on it. Repeat steps 3–4 and make sure `my-video-studio` is selected. You can add more repositories to the app later from the same page.
:::

## Step 4 · Tune your *environment*

<p class="lead">Two settings make the difference between "it works" and "it works beautifully": internet access and the startup script.</p>

Your **environment** is the saved setup for every cloud computer Claude uses. The Default one has **Trusted** network access: it can reach package registries and GitHub, but not the websites where free voices, sound libraries and fonts live. We'll fix that and add the starter kit.

### Open the environment settings

1. On the **new session** screen at claude.ai/code, look at the row of controls **under the message box**. The first control is the **environment selector**.
2. Find **Default** under **Cloud**, hover over it and click the **settings icon** that appears on the right.

:::figure env-dialog.svg | Simplified illustration of the environment dialog: Network access, Setup script, Environment variables.

### Set Network access to Full

Select the **Network access** row and choose **Full**.

| Level | What sessions can reach | Good for video? |
|---|---|---|
| None | Nothing | ✗ |
| Trusted (default) | Package registries, GitHub, cloud SDKs | Partly: no voices, sound libraries or fonts |
| **Full** | **Any website** | **✓ Recommended** |
| Custom | Your own list of domains | ✓ For advanced users |

:::note
**Prefer Custom?** Allow at least: `huggingface.co`, `cdn.jsdelivr.net`, `fonts.googleapis.com`, `fonts.gstatic.com`, `api.openverse.org`, `cdn.freesound.org`, `api.quran.com` and `api.alquran.cloud` (for faith content), and keep the default list included.
:::

### Paste the setup script

Select the **Setup script** row and paste this single line:

```bash
git clone --depth 1 https://github.com/JimmyDamelio/claude-video-starter-kit /tmp/kit && sh /tmp/kit/install.sh
```

Then click **Save changes**.

From now on, **every new session** starts with the starter kit installed: the video skills, the motion-design and sound skills, the templates, plus ffmpeg and a headless browser if they're missing. It's quick by design, because setup scripts should finish in about five minutes.

:::tip
The heavier tools (free voices and the "ears" that let Claude listen to audio) are installed **on demand**. When a video needs them, just say *"install the media tools"* and Claude runs `sh /tmp/kit/install.sh --media`. It takes 2–4 minutes.
:::

:::note
**Changing settings during a session:** click the small arrow after the session title at the top and choose **Edit cloud environment**.
:::

## Step 5 · Your first session: *check everything*

<p class="lead">Two minutes to make sure the studio is ready, and to teach Claude your brand once and for all.</p>

1. On claude.ai/code, click the **repository selector** under the message box and choose `my-video-studio`.
2. Pick a **permission mode**. **Accept edits** (or **Auto**, if you see it) lets Claude work without stopping for approval at every step, which is what you want for long video jobs.
3. Paste this prompt:

:::prompt Studio check
Check that my video studio is ready. Run `sh /tmp/kit/install.sh --doctor` and tell me in a short list what's installed and what's missing (skills, ffmpeg, headless browser, voices, sound tools). If something essential is missing, fix it. Don't create any video yet.
:::

### Teach Claude your brand (do this once)

Claude reads a file called **CLAUDE.md** at the start of every session in a repo. Put your brand in it, and every video comes out on-brand without you repeating yourself.

:::prompt Create my studio brief
Interview me to create my studio brief. Ask me, one short question at a time: my account/brand name, my niche and audience, the language of my videos, 3–5 brand colours (or let me pick from palettes you propose), my fonts (or propose some), the tone (e.g. calm, punchy, funny), whether I use music or not, voice-over or not, my usual formats (9:16 / 1:1 / 16:9), and any rules (things I never want to see). Then write it all into CLAUDE.md at the root of this repo, as clear instructions for future video sessions, and push it to GitHub.
:::

:::tip
Run this again whenever your brand evolves, or open CLAUDE.md on github.com and edit it directly.
:::
