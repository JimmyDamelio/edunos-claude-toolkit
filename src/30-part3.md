:::part 3 | Your first video | From one prompt to a finished MP4, then how to direct Claude like a creative director.

## The anatomy of a *great* video prompt

<p class="lead">Claude can do a lot with very little, but the more precisely you describe the film, the closer the first version lands.</p>

A weak prompt:

> make a video about productivity

A strong prompt answers the questions a director would ask. Use these eight blocks, or just the ones you care about:

| Block | What to say | Example |
|---|---|---|
| **Goal** | What the viewer should feel or do | "Make people save it and try tip #3 tonight" |
| **Format** | Ratio, length, platform | "9:16 Instagram Reel, 35–45 s" |
| **Hook** | The first 2 seconds | "Big '5' and 'habits that fix your mornings'" |
| **Beats** | The scenes, in order | "Hook → 5 habits, one scene each → recap → question" |
| **Style** | Look, colours, fonts, characters | "Flat pastel, faceless pill-shaped characters, cream on navy" |
| **Text** | On-screen words, subtitles | "Short titles with one highlighted keyword" |
| **Sound** | Music, voice, effects | "No voice. Soft UI pops on every appearance, light ambience" |
| **Checks** | What Claude must verify | "Check stills before the full render; keep text inside safe zones" |

### The master prompt (fill in the brackets)

:::prompt The master template
Make a [9:16 Instagram Reel / 1:1 post / 16:9 YouTube video] of [LENGTH] seconds about [TOPIC].
Goal: [WHAT THE VIEWER SHOULD FEEL OR DO].
Hook (first 2 seconds): [HOOK LINE + VISUAL].
Beats: [SCENE 1] → [SCENE 2] → [SCENE 3] → [ENDING / CALL TO ACTION].
Style: [STYLE], palette [COLOURS], fonts [FONTS OR "you choose"], [CHARACTERS / ILLUSTRATIONS].
On-screen text: [SUBTITLES / TITLES / KEY WORDS HIGHLIGHTED], large and readable on a phone, inside the safe zone (nothing important in the top 12% or bottom 20%).
Sound: [MUSIC STYLE or "no music"], [VOICE-OVER: voice + language, or "no voice"], [SOUND EFFECTS].
Facts: use only information I give you or that you verify from a reliable source; show sources on screen if relevant.
Process: storyboard first and show it to me, then render key stills and check them yourself, then render the full video at 30 fps, then check the final contact sheet. Save the MP4 in videos/ and push it to GitHub.
:::

:::tip
**"Storyboard first and show it to me"** is the most valuable sentence in any video prompt. You catch a wrong idea in 30 seconds instead of after a full render.
:::

## Your first video in *15 minutes*

<p class="lead">Let's make a real reel now. Pick any topic you know well.</p>

1. Open claude.ai/code, choose your `my-video-studio` repo and **Accept edits** mode.
2. Paste the prompt below, replacing the topic.
3. Read the storyboard Claude proposes. Reply *"go"* or ask for changes.
4. Wait while Claude renders. A 30–60 s reel usually takes a few minutes. You can close the tab: the session keeps working in the cloud.

:::prompt My first reel
Make a 25-second 9:16 Instagram Reel: "3 [TOPIC] tips nobody tells you".
Hook: a giant "3" that pops in, with the title. Then one scene per tip (6 s each): a short bold title with one highlighted keyword, an italic one-line explanation, and a simple animated illustration with flat, faceless pastel characters. End with "Which one will you try first?".
Style: dark navy background, warm amber highlight, cream text, modern grotesk font plus an elegant italic serif for accents.
Sound: no voice, no music: soft real UI sound effects (pops, ticks, whooshes) on every appearance, plus a quiet ambience.
Storyboard first, then check key stills yourself, then render at 30 fps, check the final contact sheet, save the MP4 in videos/ and push it to GitHub.
:::

### What you'll see Claude do

1. **Storyboard:** a table of scenes with timings and text.
2. **Stills check:** it renders a handful of frames, looks at them (yes, it can see images), and fixes overlaps, empty moments or unreadable text.
3. **Sound:** it finds or makes the audio and places each effect on its frame.
4. **Full render** and a final **contact sheet**: a grid of frames from the finished video, its last quality check.
5. **Push:** the MP4 lands in your repo.

### Download your video

:::figure github-download.svg | On github.com, open the MP4 and click Download raw file.

- **From GitHub (always works):** open your repo on github.com → `videos/` → click the MP4 → click the **Download raw file** button (the down-arrow icon at the top right of the file).
- **From the chat:** if Claude shows a file card with a download button, use it.
- **To your phone:** download on your computer, then send it to yourself (Google Drive, Telegram "Saved Messages", AirDrop…), or open github.com on your phone.

:::warn
Cloud sessions are wiped after a period of inactivity. Anything not pushed to GitHub can disappear. If you're not sure, ask: *"Is everything pushed?"*
:::

## Direct like a *pro*

<p class="lead">The first render is a draft. The magic is in the second and third.</p>

### Say what you see, and where

Claude fixes precise feedback instantly. Vague feedback ("make it better") gets random changes.

| Instead of… | Say… |
|---|---|
| "It's ugly" | "The title at 0:08 overlaps the illustration. Move the illustration down 100 px." |
| "Too slow" | "Each scene feels long. Cut scenes to 4 s and make the words pop in faster." |
| "Not readable" | "The subtitle on the light background has low contrast. Add a dark band behind it." |
| "More dynamic" | "Add a 1.1× scale pop with overshoot on each title word and a whoosh on each scene change." |
| "Different vibe" | "Keep the layout but switch to a cream background with coral and teal accents." |

### Useful vocabulary

- **Ease / easing:** how motion speeds up and slows down. *"Ease-out on entrances, ease-in on exits."*
- **Overshoot / bounce:** the playful "pop" past the final size. *"Back-ease with a slight overshoot."*
- **Stagger:** elements appearing one after another. *"Stagger the list items by 0.15 s."*
- **Safe zone:** where the app's interface doesn't cover your video. *"Keep text out of the bottom 20%."*
- **Contact sheet:** a grid of frames to review the whole film at a glance. *"Show me a contact sheet."*
- **Beat / cue:** a moment where something happens. *"Put a soft hit on every cue."*

### Iteration prompts that work

:::prompt Review pass
Before changing anything, render a contact sheet of the current video (one frame every 2 seconds) and critique it like a senior motion designer: readability on a phone, empty moments, overlaps, pacing, contrast, safe zones. List the 5 most important fixes, then apply them and show me a new contact sheet.
:::

:::prompt Make it more addictive
Make this reel more addictive without making it longer: a stronger first 2 seconds (big number or bold claim), something moving at all times, a sound on every appearance, a progress indicator so viewers know how many items are left, and a final recap screen people want to save.
:::

:::prompt Turn it into a template
Turn this video into a reusable template in templates/[NAME]/: keep the style, timings, sound design and code, but move all the text and data into one simple file I can edit for the next episode. Write a short README explaining how to make the next one, and push.
:::

### Keep sessions focused

- **One video per session.** Long sessions fill Claude's working memory (the *context*). Start a new session for the next video.
- Use **`/compact`** to summarise a long conversation, or **`/clear`** to start fresh in the same session.
- For complex films, you can raise the reasoning effort with **`/effort`**, for example `/effort high`. Higher effort means more detail and more usage.
- Videos with many scenes can take a while. Let Claude work, and come back later.

:::note
Your plan has usage limits that reset over time. Rendering itself happens on the cloud computer, but every message, image check and fix uses your plan. The *"storyboard first"* and *"check stills first"* habits save a lot of usage.
:::
