## Teach and *explain*

:::prompt How it works (explainer)
Make a 45 s 16:9 explainer: "How does [THING] work?" in 4 steps. Each step: a simple diagram that builds itself (shapes, arrows, labels), a one-sentence caption, and a highlight on the part being explained. Finish with a recap of all 4 steps on one screen. Calm voice-over in [LANGUAGE] synced to the steps, subtitles on. Only use facts I provide or that you verify.
:::

:::prompt Data story with animated charts
Make a 30 s 9:16 data story from this data: [PASTE NUMBERS / CSV]. Find the most surprising insight, open with it as a big number, then show 2–3 animated charts (bars growing, a line drawing itself, a donut filling) with clear labels and one highlighted bar. End with the takeaway and the data source. Colour-blind-safe palette, readable on a phone.
:::

:::prompt Animated map journey
Make a 30 s 16:9 animated map showing [JOURNEY / HISTORY / ROUTE]: a stylised map (no copyrighted map tiles), a path that draws itself from [A] to [B] to [C], labelled stops that pop up with a short fact each, and a moving dot with a soft trail. Old-paper or flat-modern style. Subtle wind and page sounds.
:::

:::prompt History in 60 seconds
Make a 60 s 9:16 animated timeline of [TOPIC] from [START YEAR] to [END YEAR]: a horizontal timeline that scrolls, with 6–8 key moments each shown as a small illustrated scene and a one-line caption. Line-art style with one accent colour. Accurate dates only; mark anything uncertain. Light ambient score.
:::

:::prompt Zoom from big to tiny
Make a 30 s 9:16 "powers of ten" style zoom from [START, e.g. a room] down to [END, e.g. atoms], with 6 levels, each with a label and one fact. Seamless zoom transitions, scale indicator on the side, wonder-filled ambient sound.
:::

:::prompt Word of the day (language learning)
Make a 15 s 9:16 language-learning reel: the word "[WORD]" in [LANGUAGE], its pronunciation, its meaning in [YOUR LANGUAGE], and 2 example sentences that animate in with the key word highlighted. Add a clear voice reading the word and the examples in [LANGUAGE] (native-sounding voice). Clean flashcard design.
:::

:::prompt Recipe in 30 seconds
Make a 30 s 9:16 animated recipe for [DISH]: flat illustrated ingredients drop into a bowl one by one with their quantities, then 4 quick steps with simple animations (stirring, baking timer, plating), then the final dish with "Save for later". Cosy warm palette, real kitchen sounds (chopping, sizzling, timer ding).
:::

## Faith and *reminders* (with verified sources)

<p class="lead">Faith content deserves the highest accuracy. These prompts make Claude fetch every reference from a reliable source instead of writing it from memory.</p>

:::warn
**Never let any AI write a verse, hadith or scripture from memory.** Always ask it to fetch the exact text from a reliable source and to show you the reference. Then double-check anything you're unsure about with a knowledgeable person.
:::

:::prompt Cinematic Qur'an verse reel
Make a 45 s 9:16 cinematic reel about Qur'an [SURAH:AYAH]. First, fetch the exact Arabic text from https://api.quran.com/api/v4/verses/by_key/[SURAH:AYAH]?fields=qpc_uthmani_hafs and render it with the KFGQPC Uthmanic Hafs font (they're made for each other: waqf marks and the ayah number display correctly). Fetch the Sahih International translation from https://api.alquran.cloud/v1/ayah/[SURAH:AYAH]/en.sahih and quote it exactly. Never type Qur'anic text by hand. Story: an emotional setup (2–3 short lines), a visual turning point (light, dawn, a door opening), the verse revealed word by word in gold, the translation as elegant subtitles, one line of reflection, and an end card with the reference. No figures with faces. [No music: real ambience (rain, wind, birds) / soft nasheed-style vocals only]. [Optional: female or male voice reading the English meaning only, never a TTS recitation of the Arabic.] Storyboard first, check the Arabic rendering at high zoom before the full render.
:::

:::prompt Hadith / sunnah listicle
Make a 60 s 9:16 listicle: "[N] sunnahs [CONTEXT, e.g. before you sleep]" in the faceless-characters style (round head + capsule body, pastel colours, no faces). Before writing any scene, verify each hadith by fetching its text from https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/eng-bukhari/[NUMBER].json (or the matching collection), and only include details the narration actually contains. Each scene: a title with one highlighted keyword, an italic one-liner, an animated scene, and a source tag like "SAHIH AL-BUKHARI 247". Hook: the big number + a curiosity line about one item. End with a recap checklist and "Which one are you starting tonight?". No voice, soft UI pops, light night ambience. Show me the list of hadiths with their texts before animating.
:::

:::prompt Du'a / dhikr card
Make a 20 s 9:16 reel for the du'a "[TRANSLITERATION]" from [VERIFIED SOURCE]. Fetch the exact Arabic text from the source first. Show the Arabic in a beautiful Arabic font, the transliteration, the meaning, and when to say it. Elegant, calm design ([PALETTE]), gentle reveal animations, a soft chime. Include the source on screen.
:::

:::prompt Ramadan / special-days countdown
Make a 15 s 9:16 countdown reel: "[N] days until [RAMADAN / EID / EVENT]". A crescent moon that fills a little more each day, lanterns that light up, the number counting down, and one short reminder of something to prepare. Warm night palette, soft ambience. Make the number and the reminder easy for me to change for each day (template).
:::

:::prompt Mindful breathing (any audience)
Make a 60 s 9:16 guided breathing video using box breathing (4 s in, 4 s hold, 4 s out, 4 s hold) for 3 rounds: a soft shape that expands, holds and contracts with the timing, a gentle text guide ("Breathe in…"), a progress ring, calm gradient colours. Calm female voice guiding each phase, with soft ambience underneath.
:::

## Music and *audio*

:::prompt Lyric video with word-perfect sync
Make a 9:16 lyric video for my song (audio file: [FILE], lyrics: [PASTE LYRICS]). Align every word to the vocals (use speech recognition / forced alignment), detect the beats and sections, then show the lyrics karaoke-style: the current word lights up exactly when it's sung, scene changes on the downbeats, and a different visual motif for each section. Style: [STYLE]. Check sync on 3 random lines before the full render.
:::

:::prompt Podcast audiogram
Make a 30 s 9:16 audiogram from this podcast clip ([FILE]): a live waveform that reacts to the voice, word-by-word captions with the key words highlighted, the episode title and guest name, and the show artwork from [IMAGE]. Clean branded design ([PALETTE]). End with "Full episode: [LINK]".
:::
