:::part 4 | Sound that sells | Voice-overs, real sound effects and silence, and how Claude can actually listen to its own mix.

## Voice-over with *free voices*

<p class="lead">Natural-sounding narration in English, French and a dozen other languages, generated in seconds, at no extra cost.</p>

The starter kit uses two free, open-source voice engines that run on Claude's cloud computer:

| Engine | Strengths | Example voices |
|---|---|---|
| **Kokoro** | The most natural. Many English voices, plus French, Spanish, Italian, Portuguese, Hindi, Japanese, Chinese | `af_heart` (warm, female), `af_bella`, `bf_emma` (British, female), `am_michael` (male), `bm_george` (British, male), `ff_siwis` (French, female) |
| **Piper** | Very fast and light | French and English voices |

To use them, first say *"install the media tools"* (once per session, 2–4 minutes). Then just describe the voice you want in your prompt.

:::prompt Voice audition
Before making the video, generate the same 2-sentence line with 4 different voices (warm female, calm male, British female, energetic) and put the clips in audio/auditions/ so I can listen and choose. Line: "[YOUR LINE]".
:::

### Make the voice drive the edit

The best-paced videos are timed **to the voice**, not the other way around. Ask Claude to generate the narration first, measure each sentence, and then set the scene timings, with word-by-word subtitles synced to the speech.

:::prompt Voice-first video
Write a 35-second voice-over script for [TOPIC] in a warm, conversational tone (short sentences, one idea each). Generate it with a warm female voice at a slightly slow pace. Then build the 9:16 video around the voice: one scene per sentence, subtitles that highlight each word as it's spoken, and visuals that change on the voice's natural pauses. Duck any background sound under the voice.
:::

:::tip
**Pronunciation fixes.** If a name or foreign word sounds wrong ("Al-lah" read as "Ala", a brand name, a city), tell Claude: *"The voice mispronounces X. Fix it phonetically."* Text-to-speech engines accept phonetic spellings, and Claude knows how to apply them.
:::

:::warn
Some platforms ask you to **label realistic AI-generated audio**. On Instagram and Facebook, use the **AI info** label when you publish a video with an AI voice. It's honest, and it protects your account.
:::

## Real sound effects (and *no-music* videos)

<p class="lead">The difference between "made by AI" and "made by a studio" is often just the sound.</p>

### Where the sounds come from

- **Openverse:** a search engine for over 800 million openly licensed works, including tens of thousands of sound effects from Freesound. The starter kit's `openverse` skill searches it, prefers **CC0** (no attribution needed) and keeps a **CREDITS.csv** of everything it downloads.
- **Bundled UI sounds:** 78 small interface sounds (pops, ticks, whooshes, chimes) in 12 styles, all CC0. Perfect for animated listicles.
- **Synthesised sound:** Claude can also compose music and effects in code (soft pads, piano, chimes). It's great for calm trailers, but recorded sound usually feels more premium.

### Videos without music

Many creators prefer **no music**: faith content, calm educational content, or simply to stand out. A good no-music soundtrack combines:

1. **Ambience:** rain, night crickets, wind, a café, birds at dawn, at a low level.
2. **Foley and effects:** a door creaking open, pages turning, a soft impact on the key moment.
3. **UI cues:** a pop on every element that appears. This is what makes listicles feel "addictive".
4. **Voice, or nothing:** text on screen can carry the whole story.

:::prompt Real-sound design
Design the soundtrack with real recordings only, no music: find CC0 sounds on Openverse for [AMBIENCE, e.g. light rain at night] and [EFFECTS, e.g. a wooden door opening, a soft deep impact, birds at dawn]. Pick the best candidates by listening to them with earshot, place each effect on the exact frame of its visual event, keep the ambience low under the voice, and save the credits in CREDITS.csv.
:::

## Let Claude *listen*

<p class="lead">Claude can't hear, but the starter kit gives it ears.</p>

**earshot** is an open-source listening tool. It turns sound into evidence Claude can reason about:

- **describe** what a sound file sounds like ("a creaking door", "crickets at night");
- **rank** candidate sounds against a description, to pick the best whoosh out of ten;
- **find** the cleanest moment inside a long recording;
- **critique** a finished video's soundtrack against professional launch films: loudness, sync to picture, empty openings, endings that fall flat, harshness, stereo width, and whether it sounds synthetic.

:::prompt Sound review
Run an earshot critique on the final video and explain the results to me in plain English. Fix every issue that matters for this style (ignore "no music" if the video is intentionally music-free), then run the critique again and show me the before/after scores.
:::

:::note
earshot compares your film to music-led launch videos, so it always flags a missing music track. If no music is your choice, tell Claude to ignore that one point.
:::

### Loudness that fits social media

Reels and TikToks are watched on phones, often with the sound low. Ask for **around −14 LUFS integrated** (the standard for streaming platforms), peaks below **−1 dBTP**, and voices that stay clearly above the background. Claude can measure and fix this automatically. Just mention it once in your studio brief.
