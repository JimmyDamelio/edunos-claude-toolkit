# Sunnah list reel template (9:16, no voice)

"N sunnahs …" listicle reel: hook (big number + curiosity line) → one scene per sunnah (title with amber keyword, italic line, faceless pastel characters, source tag) → recap checklist → CTA question. Palette "Midnight & Amber". Sound: CC0 crickets bed + CC0 uisfx 'rubber' cues placed on the film's own cue list.

- Verify every hadith before writing a scene: `https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/eng-bukhari/<n>.json` (sunnah.com numbering; sunnah.com itself blocks bots). Don't add details the narration doesn't contain (e.g. "3 times" for dusting the bed).
- `node render.mjs cues` → `python3 audio.py` → `node render.mjs frames 30 6` → ffmpeg mux. `film.html?t=12` to preview a moment.
- First film: 7 sunnahs before you sleep (Bukhari 247, 6320, 5017, 2311, 5009, 3705, 6324).
