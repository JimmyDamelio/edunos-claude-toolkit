:::part 6 | Publish, grow, fix | Turn videos into reach, and get unstuck in minutes when something breaks.

## The posting *playbook*

<p class="lead">The algorithm rewards what people do with your video, not the tool you made it with.</p>

### What actually makes a reel travel

1. **Watch time and rewatches.** A strong first 2 seconds, and something moving all the time.
2. **Shares**, especially by DM. That's the strongest signal for reaching new people. "Send this to someone who…" works.
3. **Saves.** Useful, list-style content gets saved ("Save this for tonight").
4. **Comments.** Ask a question that takes zero effort to answer ("Comment the number you'll try").

### Before you publish

- [ ] **Cover image:** a clean frame with the big promise (ask Claude to export one: *"export the frame at 2.5 s as cover.jpg"*).
- [ ] **Caption:** hook line, value, sources if you cite any, one clear question, one call to save or share.
- [ ] **Hashtags:** Instagram now caps posts and Reels at **5 hashtags**. Pick 5 precise ones: 2 broad, 3 niche.
- [ ] **AI label** if you used an AI voice.
- [ ] **Pinned comment** with a question.

:::prompt Caption & hashtags
Act as my Instagram strategist. For the video we just made, write: 3 hook options for the first line of the caption, one full caption (value + question + save/share call to action, with sources if we cited any), the 5 best hashtags for reach in my niche, a pinned comment, a story idea to promote it, and the best time to post for my main audience in [COUNTRIES / TIME ZONES], converted to my time zone [YOUR CITY].
:::

### When to post

Your audience's evening is usually best. If your followers are spread across time zones, aim for the evening of your **largest** audience: the reel keeps being distributed for a day or two, so the next time zones pick it up later. After a few posts, check **Insights → Your audience** (top countries and most active times) and adjust.

:::tip
**Scheduling from a computer.** You can publish Reels from instagram.com, and schedule them from **Meta Business Suite** (business.facebook.com), with an Instagram professional account (free). Posting from a browser doesn't reduce reach.
:::

### Build a series, not a one-off

Accounts grow on **recognisable formats**. Once a video performs, turn it into a template (Part 3) and make an episode every week: same style, new content. Your profile grid starts to look like a brand.

## Troubleshooting

<p class="lead">Every problem below happened to real users. Here's the fix.</p>

| Problem | Fix |
|---|---|
| **My repository doesn't show up in Claude Code** | Install the Claude GitHub App on it: github.com/apps/claude/installations/new → Only select repositories → tick your repo. |
| **"Push refused" / "GitHub access denied"** | Same cause: the app isn't installed on that repo, or your GitHub connection expired. Reconnect GitHub in claude.ai's connector settings, then reinstall the app on the repo. |
| **Claude can't download voices, fonts or sounds (403, "tunnel failed")** | Your environment's network access is Trusted. Set it to **Full**, or add the domains from Part 2 to a Custom list. Start a new session if needed. |
| **"Setup script failed" / session won't start** | Open the environment settings and check the setup script line was pasted exactly. The script must finish in about 5 minutes; keep heavy installs for "install the media tools". |
| **Claude says ffmpeg or the browser is missing** | Say *"run sh /tmp/kit/install.sh --doctor and fix what's missing"*. |
| **I can't find my video** | Ask *"Where is the MP4, and is it pushed to GitHub?"* Then download it from github.com (Part 3). Files over 100 MB can't be pushed to GitHub: ask for a smaller file (CRF 20–23 or 1080p). |
| **The session forgot everything** | Cloud sessions are wiped after inactivity; the conversation is kept but files that weren't pushed are gone. Make pushing a habit: *"push after every finished video"*. |
| **"Context 80 % used" / Claude gets slower** | One video per session. Use `/compact` to summarise or `/clear` to start fresh. |
| **I hit my usage limit** | Limits reset over time. Save usage with "storyboard first", "check stills before full render" and shorter sessions. Bigger plans give more room. |
| **Text is cut off or covered by Instagram's buttons** | *"Keep all text inside the safe zone: nothing in the top 12% or bottom 20%, and nothing in the right 12% next to the buttons."* |
| **The voice mispronounces a word** | *"Fix the pronunciation of X phonetically."* |
| **Arabic, Hebrew or other scripts look broken** | Ask Claude to use a font made for that script and to check the rendering at high zoom. For Qur'anic text, use the quran.com API text that matches the KFGQPC font (see the verse prompt in Part 5). |
| **It looks generic / "AI-made"** | Give it a style reference: *"Use the design-dna skill on these 3 screenshots, then apply that style."* And use real sounds. |

:::tip
When in doubt, describe the problem to Claude in plain words. It can read its own error messages, check its setup and fix most issues itself.
:::

## The one-page *checklist*

<ul class="checklist">
<li><strong>Idea:</strong> one promise, one audience, one format (list, quote, story, explainer).</li>
<li><strong>Prompt:</strong> master template filled in, "storyboard first", safe zones, sound choice.</li>
<li><strong>Storyboard approved</strong>, hook checked: would you stop scrolling?</li>
<li><strong>Stills checked</strong>: readable on a phone, no overlaps, no empty moments.</li>
<li><strong>Sound:</strong> voice or not, real effects on the cues, around −14 LUFS, earshot critique.</li>
<li><strong>Facts and sources verified</strong>, shown on screen when it matters.</li>
<li><strong>Final contact sheet</strong> reviewed. MP4 <strong>pushed to GitHub</strong> and downloaded.</li>
<li><strong>Cover, caption, 5 hashtags, AI label if needed, pinned comment.</strong></li>
<li><strong>Posted</strong> at your audience's best time. Story shared within 30 minutes.</li>
<li><strong>Template saved</strong> for the next episode.</li>
</ul>

## Credits, licences and *thank yous*

The starter kit stands on the shoulders of generous open-source creators. Their licences are included in the kit; please keep them if you share it.

| Project | What it brings | Licence |
|---|---|---|
| <a href="https://github.com/LottieFiles/motion-design-skill">LottieFiles/motion-design-skill</a> | Motion design principles | MIT |
| <a href="https://github.com/greensock/gsap-skills">greensock/gsap-skills</a> | Official GSAP animation skills | MIT |
| <a href="https://github.com/CloudAI-X/threejs-skills">CloudAI-X/threejs-skills</a> | Three.js 3D skills | MIT |
| <a href="https://github.com/zanwei/design-dna">zanwei/design-dna</a> | Extract and reuse a visual style | MIT |
| <a href="https://github.com/Leonxlnx/earshot">Leonxlnx/earshot</a> | Listening tools for agents | MIT |
| real-sfx | Sound design with real recordings + uisfx sounds (CC0) | MIT |
| <a href="https://github.com/WordPress/openverse">Openverse</a> | Search for openly licensed media | Public API |
| <a href="https://github.com/thewh1teagle/kokoro-onnx">kokoro-onnx</a>, <a href="https://github.com/rhasspy/piper">Piper</a> | Free voices | Apache-2.0 / MIT |
| <a href="https://github.com/Panniantong/Agent-Reach">Agent Reach</a> | Reading X, YouTube, Reddit… | MIT |

For inspiration, these public collections are gold mines of styles and prompts: <a href="https://github.com/lemomo-ai/lemo-opuscar">lemo-opuscar</a> (59 film styles), <a href="https://github.com/Vincentwei1021/mg-styles-15">mg-styles-15</a>, <a href="https://github.com/JohnHeibel/ClaudeAnimationBase">ClaudeAnimationBase</a>, <a href="https://github.com/yihui-dev/awesome-opus5-5-videos">awesome-opus5-5-videos</a>, <a href="https://github.com/athemeroy/awesome-claude-5-5-videos">awesome-claude-5-5-videos</a> and <a href="https://github.com/joeseesun/opus-video-prompts">opus-video-prompts</a>.

<p class="legal"><strong>Disclaimer.</strong> This guide is independent and is not affiliated with, endorsed by or sponsored by Anthropic, GitHub, Meta or any project mentioned. "Claude" and "Claude Code" are trademarks of Anthropic; other names belong to their owners and are used only to describe compatibility. Features, plans, prices and interfaces change: check the official pages linked in this book. You're responsible for the content you publish, including the accuracy of facts and religious references, music and sound licences, and platform rules. Results vary with your plan, prompts and settings.</p>
