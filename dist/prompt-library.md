# Prompt to Reel — Prompt Library

Every prompt from the book, ready to copy. Replace the [BRACKETS] with your own details.

## 01 · Studio check

```text
Check that my video studio is ready. Run `sh /tmp/kit/install.sh --doctor` and tell me in a short list what's installed and what's missing (skills, ffmpeg, headless browser, voices, sound tools). If something essential is missing, fix it. Don't create any video yet.
```

## 02 · Create my studio brief

```text
Interview me to create my studio brief. Ask me, one short question at a time: my account/brand name, my niche and audience, the language of my videos, 3–5 brand colours (or let me pick from palettes you propose), my fonts (or propose some), the tone (e.g. calm, punchy, funny), whether I use music or not, voice-over or not, my usual formats (9:16 / 1:1 / 16:9), and any rules (things I never want to see). Then write it all into CLAUDE.md at the root of this repo, as clear instructions for future video sessions, and push it to GitHub.
```

## 03 · The master template

```text
Make a [9:16 Instagram Reel / 1:1 post / 16:9 YouTube video] of [LENGTH] seconds about [TOPIC].
Goal: [WHAT THE VIEWER SHOULD FEEL OR DO].
Hook (first 2 seconds): [HOOK LINE + VISUAL].
Beats: [SCENE 1] → [SCENE 2] → [SCENE 3] → [ENDING / CALL TO ACTION].
Style: [STYLE], palette [COLOURS], fonts [FONTS OR "you choose"], [CHARACTERS / ILLUSTRATIONS].
On-screen text: [SUBTITLES / TITLES / KEY WORDS HIGHLIGHTED], large and readable on a phone, inside the safe zone (nothing important in the top 12% or bottom 20%).
Sound: [MUSIC STYLE or "no music"], [VOICE-OVER: voice + language, or "no voice"], [SOUND EFFECTS].
Facts: use only information I give you or that you verify from a reliable source; show sources on screen if relevant.
Process: storyboard first and show it to me, then render key stills and check them yourself, then render the full video at 30 fps, then check the final contact sheet. Save the MP4 in videos/ and push it to GitHub.
```

## 04 · My first reel

```text
Make a 25-second 9:16 Instagram Reel: "3 [TOPIC] tips nobody tells you".
Hook: a giant "3" that pops in, with the title. Then one scene per tip (6 s each): a short bold title with one highlighted keyword, an italic one-line explanation, and a simple animated illustration with flat, faceless pastel characters. End with "Which one will you try first?".
Style: dark navy background, warm amber highlight, cream text, modern grotesk font plus an elegant italic serif for accents.
Sound: no voice, no music: soft real UI sound effects (pops, ticks, whooshes) on every appearance, plus a quiet ambience.
Storyboard first, then check key stills yourself, then render at 30 fps, check the final contact sheet, save the MP4 in videos/ and push it to GitHub.
```

## 05 · Review pass

```text
Before changing anything, render a contact sheet of the current video (one frame every 2 seconds) and critique it like a senior motion designer: readability on a phone, empty moments, overlaps, pacing, contrast, safe zones. List the 5 most important fixes, then apply them and show me a new contact sheet.
```

## 06 · Make it more addictive

```text
Make this reel more addictive without making it longer: a stronger first 2 seconds (big number or bold claim), something moving at all times, a sound on every appearance, a progress indicator so viewers know how many items are left, and a final recap screen people want to save.
```

## 07 · Turn it into a template

```text
Turn this video into a reusable template in templates/[NAME]/: keep the style, timings, sound design and code, but move all the text and data into one simple file I can edit for the next episode. Write a short README explaining how to make the next one, and push.
```

## 08 · Voice audition

```text
Before making the video, generate the same 2-sentence line with 4 different voices (warm female, calm male, British female, energetic) and put the clips in audio/auditions/ so I can listen and choose. Line: "[YOUR LINE]".
```

## 09 · Voice-first video

```text
Write a 35-second voice-over script for [TOPIC] in a warm, conversational tone (short sentences, one idea each). Generate it with a warm female voice at a slightly slow pace. Then build the 9:16 video around the voice: one scene per sentence, subtitles that highlight each word as it's spoken, and visuals that change on the voice's natural pauses. Duck any background sound under the voice.
```

## 10 · Real-sound design

```text
Design the soundtrack with real recordings only, no music: find CC0 sounds on Openverse for [AMBIENCE, e.g. light rain at night] and [EFFECTS, e.g. a wooden door opening, a soft deep impact, birds at dawn]. Pick the best candidates by listening to them with earshot, place each effect on the exact frame of its visual event, keep the ambience low under the voice, and save the credits in CREDITS.csv.
```

## 11 · Sound review

```text
Run an earshot critique on the final video and explain the results to me in plain English. Fix every issue that matters for this style (ignore "no music" if the video is intentionally music-free), then run the critique again and show me the before/after scores.
```

## 12 · Faceless listicle with characters

```text
Make a 45–60 s 9:16 Instagram Reel: "[NUMBER] [THINGS] that [PROMISE]". Hook (0–2.5 s): a giant number popping in, the title, and a highlighted curiosity line: "#[N] [INTRIGUING DETAIL]". Then one 6 s scene per item: a short bold title with ONE highlighted keyword in a coloured box, an italic one-line explanation, and a small animated scene with faceless pastel characters (round head + capsule body) acting it out. Show progress dots so viewers know how many are left. End with a recap checklist of all items ticking one by one, then a question: "Which one are you starting today?". Style: [PALETTE], bold grotesk + italic serif accents. No voice. Sound: a soft pop on every appearance, a whoosh on scene changes, quiet ambience. Storyboard first, check stills, render at 30 fps, push the MP4.
```

## 13 · Cinematic quote reel

```text
Make a 30–40 s 9:16 cinematic reel around this quote: "[QUOTE]" by [AUTHOR]. Story: an emotional setup (2–3 short lines that describe a feeling the viewer knows), a visual turning point (a door opening, sunrise, rain stopping, light breaking through), then the quote revealed word by word in large elegant type, then one line of reflection, then an end card with the author's name. Visuals: atmospheric illustrated scene ([SCENE, e.g. a lone lantern in the desert at night]), slow camera drift, light particles. Sound: [voice-over with a calm warm voice / no voice], real ambience and one soft impact on the reveal. Storyboard first.
```

## 14 · 3 mistakes to avoid

```text
Make a 30 s 9:16 reel: "3 [TOPIC] mistakes that [CONSEQUENCE]". Each mistake gets a red ✗ stamp animation, a short title and a quick visual of the mistake; then the fix appears with a green ✓, a swipe transition and the better version. End: "Save this before your next [ACTIVITY]". Punchy pacing, bold condensed type, high contrast. UI sound effects on every stamp. Storyboard first, then render.
```

## 15 · Myth vs fact

```text
Make a 30 s 9:16 reel with 3 myth-vs-fact rounds about [TOPIC]. Each round: "MYTH" card slides in with the myth, a 1 s pause, the card flips (3D flip) to "FACT" with the truth and a one-line source. Use a split-colour layout (myth = muted grey, fact = vivid [COLOUR]). Countdown dots 1/3, 2/3, 3/3. Only use facts I give you or that you verify; show the source on screen. Sound: flip whoosh + soft ding on each fact.
```

## 16 · Countdown ranking

```text
Make a 40 s 9:16 "Top 5 [THINGS]" countdown from #5 to #1. Each entry: a huge number that slams in with a bass hit, the name, one reason, and a simple animated icon or illustration. Build suspense before #1 (darker background, a short drum roll from real recordings, then a bright reveal). End: "Agree? Comment your #1". Bold, energetic, [PALETTE].
```

## 17 · Stat shock

```text
Make a 20 s 9:16 reel built on one surprising number: [STAT + SOURCE]. 0–3 s: the number counts up from 0 with ticking sounds and lands with an impact. 3–12 s: what it means, shown with a simple animated visual (dots filling a grid, a bar growing, a clock). 12–17 s: what the viewer can do about it. 17–20 s: the source and "Follow for more". Clean data-journalism look, one accent colour.
```

## 18 · Before / after transformation

```text
Make a 25 s 9:16 before/after reel about [TRANSFORMATION, e.g. a messy morning routine → a calm one]. Left/right or top/bottom split; a wipe slider moves across to reveal the "after". Show 3 concrete changes as labelled callouts with arrows. End with "Try it for 7 days". Satisfying motion, soft clicks on each callout.
```

## 19 · Kinetic typography hook

```text
Make a 15 s 9:16 kinetic typography reel from this text: "[3–5 SHORT LINES]". Each word appears on the beat with varied scale, weight and position (some words huge, some tiny), with snappy easing and occasional colour inversions. Keep it readable: max 3 words on screen at once. [Soundtrack: punchy electronic loop at 120 BPM / no music, typing and impact sounds]. Make the last line stay on screen for 2 s.
```

## 20 · Day-in-the-life timeline

```text
Make a 40 s 9:16 animated "a day in the life of a [ROLE]" reel. A clock in the corner advances through the day; each time stamp gets a quick illustrated scene with a faceless character (wake up, work, lunch, …). Use a soft colour shift from morning to night. Add a funny or honest caption under each scene. Light ambience that changes with the time of day (birds, office hum, evening crickets).
```

## 21 · Interactive question / poll

```text
Make a 20 s 9:16 reel that asks viewers a question: "[QUESTION]?" with 2–4 animated answer options (A, B, C) as cards. A timer bar runs for 5 s, then one answer is revealed with an explanation, OR (if there's no right answer) end with "Comment your letter!". Game-show energy: bright colours, bouncy animations, buzzer and ding sounds from real recordings.
```

## 22 · Digital product trailer (ebook, course, template)

```text
Make a 30 s 16:9 launch trailer (plus a 9:16 version) for my product "[NAME]": [ONE-LINE DESCRIPTION], price [PRICE], link [URL]. Story: 1) the viewer's problem in one relatable scene, 2) "What if…" turning point, 3) the product revealed (a clean 3D-ish mock-up of the cover/screens with a soft shadow and a gentle float), 4) 3 benefits as animated callouts, 5) proof (numbers, testimonials or "what's inside"), 6) end card: name, price, link. Use only claims I give you. Style: [STYLE + PALETTE]. Sound: [soft piano / upbeat / no music + real effects]. Storyboard first.
```

## 23 · App / SaaS launch video

```text
Make a 40 s 16:9 product launch video for [APP NAME], an app that [WHAT IT DOES]. Show stylised UI mock-ups (not screenshots) of 3 key screens: [SCREEN 1], [SCREEN 2], [SCREEN 3], animated as if someone is using them (cursor, taps, cards sliding, numbers updating). Open with the pain point, end with the logo and "[CALL TO ACTION]". Clean modern look, [BRAND COLOURS], smooth easing, subtle depth and shadows. Modern electronic score at 110–120 BPM with whooshes and UI clicks synced to the motion.
```

## 24 · Feature explainer (one feature, 20 s)

```text
Make a 20 s 9:16 reel explaining one feature of [PRODUCT]: [FEATURE]. Structure: "Did you know you can [BENEFIT]?" → 3 steps shown on a simplified phone mock-up (tap, swipe, result) with numbered highlights → the result → "Try it today". Keep text short, add a progress bar across the bottom of the safe zone.
```

## 25 · Sale / promo announcement

```text
Make a 15 s 9:16 promo for [OFFER, e.g. -30% this weekend] at [SHOP]. Bold, high-energy: a big percentage slams in, products (from my descriptions or simple illustrations) fly in on a grid, a countdown timer ticks, end with the code [CODE] and the link. Retro-pop style with halftone dots and thick outlines. Cash-register and pop sounds.
```

## 26 · Animated testimonial card

```text
Make a 20 s 9:16 testimonial video from this review: "[REVIEW]" — [NAME, ROLE]. A clean card with 5 stars that fill one by one, the quote typed in with key words highlighted, the person's initials in a circle (no fake photos), and the product name at the end. Calm, trustworthy palette. Soft ticks on each star.
```

## 27 · Logo sting / channel intro

```text
Make a 5 s logo sting for [BRAND NAME] in 16:9 and 9:16. The logo is built from [SHAPES / LETTERS] that assemble with satisfying motion (overshoot, then settle), a light sweep across it, and the tagline "[TAGLINE]" fading in. One signature sound: [a soft whoosh + chime / a deep impact / a playful pop]. Export a version with transparent background too (WebM with alpha) if possible.
```

## 28 · Event promo with countdown

```text
Make a 25 s 9:16 promo for [EVENT] on [DATE] at [PLACE/ONLINE]. Show what people will get (3 animated highlights), the speakers or guests as stylised initial badges, a live-feeling countdown "[N] days left", and the sign-up link. Energetic but clear; ticking clock and crowd ambience at low level.
```

## 29 · Pricing explained in 30 s

```text
Make a 30 s 16:9 explainer of my pricing: [PLANS + PRICES + WHAT'S INCLUDED]. Animate the plan cards rising like a bar chart, highlight the recommended plan with a glow and a "Most popular" ribbon, and show a quick comparison of 3 key features with ticks and crosses. End with "[CALL TO ACTION]". Clean SaaS style.
```

## 30 · Watercolour & ink

```text
Make a 30 s [FORMAT] short film about [SUBJECT] in a hand-made watercolour and ink style: soft layered colour washes with darker edges on warm paper texture, ink lines that "boil" slightly (redrawn 8 times per second), gentle film grain and vignette, slow camera push. Transitions: watercolour blooms and brush wipes. Palette: [e.g. sage, blush, terracotta, cream]. Soft piano and real paper sounds.
```

## 31 · Paper cut-out

```text
Make a 25 s [FORMAT] video about [SUBJECT] in a layered paper cut-out style: flat coloured paper shapes with visible thickness and soft drop shadows, parallax between layers, slight paper texture, elements that pop up like a pop-up book. Palette: [COLOURS]. Sound: paper rustles, soft pops, light music box melody.
```

## 32 · 16-bit pixel art

```text
Make a 20 s 9:16 pixel-art video (16-bit console style, 320×568 virtual resolution scaled up with sharp pixels) about [SUBJECT]: a tiny character walking through [WORLD], collecting [ITEMS] that each reveal a tip. Retro UI frames, score counter, chiptune-style sound effects.
```

## 33 · Neon synthwave

```text
Make a 20 s [FORMAT] synthwave video for [SUBJECT]: purple-pink gradient sky, a glowing grid floor scrolling toward the horizon, a striped retro sun, chrome text with neon glow and scanlines. Pulsing 100 BPM retro synth beat; text hits on the downbeats.
```

## 34 · Low-poly 3D

```text
Make a 25 s 9:16 low-poly 3D scene (three.js) about [SUBJECT]: a small floating island with [ELEMENTS], soft pastel lighting, gentle orbit camera, objects that grow from the ground with bouncy easing. Titles in clean sans-serif over the scene. Light ambience + soft pops.
```

## 35 · Clay / soft 3D

```text
Make a 20 s 9:16 video in a soft "clay" 3D look (rounded shapes, matte pastel materials, soft shadows, tiny imperfections) showing [SUBJECT]. Objects squash and stretch when they land. Cute, tactile sound effects (boops, squishes).
```

## 36 · Whiteboard explainer

```text
Make a 45 s 16:9 whiteboard-style explainer of [CONCEPT]: black marker lines drawn progressively on a white board, handwritten-style titles, simple icons and arrows, a few colour highlights in [COLOUR]. Explain it in 4 steps. Add a calm voice-over in [LANGUAGE] and marker squeak sounds when drawing.
```

## 37 · Retro risograph poster

```text
Make a 15 s 9:16 animated poster for [EVENT / IDEA] in a risograph print style: 2–3 spot colours ([COLOURS]) with slight misregistration, grain texture, bold condensed type, shapes that slide and overlap. Loopable ending.
```

## 38 · Ukiyo-e woodblock

```text
Make a 30 s 16:9 short in a Japanese ukiyo-e woodblock style about [SUBJECT]: flat colour areas, bold outlines, stylised waves and clouds, washi paper texture, slow parallax. Gentle traditional-sounding plucked melody (synthesised) and wind.
```

## 39 · Blueprint / technical

```text
Make a 25 s 16:9 blueprint-style explainer of [PRODUCT / OBJECT]: white technical lines drawn on a blue grid, dimension arrows and callout labels that appear one by one, an exploded view that separates the parts, then reassembles. Mechanical click and drafting sounds.
```

## 40 · Minimal Swiss motion

```text
Make a 15 s 9:16 minimal Swiss-design motion piece for [MESSAGE]: strict grid, big Helvetica-style type, red/black/white only, shapes that snap into place with precise easing. Very clean, no textures. Tight percussive sound design.
```

## 41 · Isometric city

```text
Make a 30 s 9:16 isometric illustration video of [PLACE / BUSINESS / CITY]: buildings rise from the ground one by one, tiny cars and people move along roads, day turns to night with lights switching on. Labels pop up for [3 KEY POINTS]. City ambience that changes with the time of day.
```

## 42 · How it works (explainer)

```text
Make a 45 s 16:9 explainer: "How does [THING] work?" in 4 steps. Each step: a simple diagram that builds itself (shapes, arrows, labels), a one-sentence caption, and a highlight on the part being explained. Finish with a recap of all 4 steps on one screen. Calm voice-over in [LANGUAGE] synced to the steps, subtitles on. Only use facts I provide or that you verify.
```

## 43 · Data story with animated charts

```text
Make a 30 s 9:16 data story from this data: [PASTE NUMBERS / CSV]. Find the most surprising insight, open with it as a big number, then show 2–3 animated charts (bars growing, a line drawing itself, a donut filling) with clear labels and one highlighted bar. End with the takeaway and the data source. Colour-blind-safe palette, readable on a phone.
```

## 44 · Animated map journey

```text
Make a 30 s 16:9 animated map showing [JOURNEY / HISTORY / ROUTE]: a stylised map (no copyrighted map tiles), a path that draws itself from [A] to [B] to [C], labelled stops that pop up with a short fact each, and a moving dot with a soft trail. Old-paper or flat-modern style. Subtle wind and page sounds.
```

## 45 · History in 60 seconds

```text
Make a 60 s 9:16 animated timeline of [TOPIC] from [START YEAR] to [END YEAR]: a horizontal timeline that scrolls, with 6–8 key moments each shown as a small illustrated scene and a one-line caption. Line-art style with one accent colour. Accurate dates only; mark anything uncertain. Light ambient score.
```

## 46 · Zoom from big to tiny

```text
Make a 30 s 9:16 "powers of ten" style zoom from [START, e.g. a room] down to [END, e.g. atoms], with 6 levels, each with a label and one fact. Seamless zoom transitions, scale indicator on the side, wonder-filled ambient sound.
```

## 47 · Word of the day (language learning)

```text
Make a 15 s 9:16 language-learning reel: the word "[WORD]" in [LANGUAGE], its pronunciation, its meaning in [YOUR LANGUAGE], and 2 example sentences that animate in with the key word highlighted. Add a clear voice reading the word and the examples in [LANGUAGE] (native-sounding voice). Clean flashcard design.
```

## 48 · Recipe in 30 seconds

```text
Make a 30 s 9:16 animated recipe for [DISH]: flat illustrated ingredients drop into a bowl one by one with their quantities, then 4 quick steps with simple animations (stirring, baking timer, plating), then the final dish with "Save for later". Cosy warm palette, real kitchen sounds (chopping, sizzling, timer ding).
```

## 49 · Cinematic Qur'an verse reel

```text
Make a 45 s 9:16 cinematic reel about Qur'an [SURAH:AYAH]. First, fetch the exact Arabic text from https://api.quran.com/api/v4/verses/by_key/[SURAH:AYAH]?fields=qpc_uthmani_hafs and render it with the KFGQPC Uthmanic Hafs font (they're made for each other: waqf marks and the ayah number display correctly). Fetch the Sahih International translation from https://api.alquran.cloud/v1/ayah/[SURAH:AYAH]/en.sahih and quote it exactly. Never type Qur'anic text by hand. Story: an emotional setup (2–3 short lines), a visual turning point (light, dawn, a door opening), the verse revealed word by word in gold, the translation as elegant subtitles, one line of reflection, and an end card with the reference. No figures with faces. [No music: real ambience (rain, wind, birds) / soft nasheed-style vocals only]. [Optional: female or male voice reading the English meaning only, never a TTS recitation of the Arabic.] Storyboard first, check the Arabic rendering at high zoom before the full render.
```

## 50 · Hadith / sunnah listicle

```text
Make a 60 s 9:16 listicle: "[N] sunnahs [CONTEXT, e.g. before you sleep]" in the faceless-characters style (round head + capsule body, pastel colours, no faces). Before writing any scene, verify each hadith by fetching its text from https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/eng-bukhari/[NUMBER].json (or the matching collection), and only include details the narration actually contains. Each scene: a title with one highlighted keyword, an italic one-liner, an animated scene, and a source tag like "SAHIH AL-BUKHARI 247". Hook: the big number + a curiosity line about one item. End with a recap checklist and "Which one are you starting tonight?". No voice, soft UI pops, light night ambience. Show me the list of hadiths with their texts before animating.
```

## 51 · Du'a / dhikr card

```text
Make a 20 s 9:16 reel for the du'a "[TRANSLITERATION]" from [VERIFIED SOURCE]. Fetch the exact Arabic text from the source first. Show the Arabic in a beautiful Arabic font, the transliteration, the meaning, and when to say it. Elegant, calm design ([PALETTE]), gentle reveal animations, a soft chime. Include the source on screen.
```

## 52 · Ramadan / special-days countdown

```text
Make a 15 s 9:16 countdown reel: "[N] days until [RAMADAN / EID / EVENT]". A crescent moon that fills a little more each day, lanterns that light up, the number counting down, and one short reminder of something to prepare. Warm night palette, soft ambience. Make the number and the reminder easy for me to change for each day (template).
```

## 53 · Mindful breathing (any audience)

```text
Make a 60 s 9:16 guided breathing video using box breathing (4 s in, 4 s hold, 4 s out, 4 s hold) for 3 rounds: a soft shape that expands, holds and contracts with the timing, a gentle text guide ("Breathe in…"), a progress ring, calm gradient colours. Calm female voice guiding each phase, with soft ambience underneath.
```

## 54 · Lyric video with word-perfect sync

```text
Make a 9:16 lyric video for my song (audio file: [FILE], lyrics: [PASTE LYRICS]). Align every word to the vocals (use speech recognition / forced alignment), detect the beats and sections, then show the lyrics karaoke-style: the current word lights up exactly when it's sung, scene changes on the downbeats, and a different visual motif for each section. Style: [STYLE]. Check sync on 3 random lines before the full render.
```

## 55 · Podcast audiogram

```text
Make a 30 s 9:16 audiogram from this podcast clip ([FILE]): a live waveform that reacts to the voice, word-by-word captions with the key words highlighted, the episode title and guest name, and the show artwork from [IMAGE]. Clean branded design ([PALETTE]). End with "Full episode: [LINK]".
```

## 56 · Caption & hashtags

```text
Act as my Instagram strategist. For the video we just made, write: 3 hook options for the first line of the caption, one full caption (value + question + save/share call to action, with sources if we cited any), the 5 best hashtags for reach in my niche, a pinned comment, a story idea to promote it, and the best time to post for my main audience in [COUNTRIES / TIME ZONES], converted to my time zone [YOUR CITY].
```

