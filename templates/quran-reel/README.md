# Quran reel template (9:16)

Cinematic Islamic reel: night → door of light → verse in Uthmani script (KFGQPC font) → dawn → end card. Female voice-over (Kokoro `af_heart`, "Allah" re-phonemized as al-LAH), karaoke subtitles, real CC0 ambience (no music). First film: Az-Zumar 39:53.

Rules that made it right:
- **Never type Qur'an text by hand.** Fetch it: `https://api.quran.com/api/v4/verses/by_key/S:A?fields=qpc_uthmani_hafs` and render it with `fonts/UthmanicHafs.woff2` (the text and the font are made for each other: waqf marks sit on the word, the ayah number gets its ornament). `text_uthmani` + Amiri misplaces ۟ and ۚ.
- Translation: Sahih International from `https://api.alquran.cloud/v1/ayah/S:A/en.sahih`, quoted exactly (keep the brackets).
- No recitation by TTS; the voice reads the English meaning only.
- No music (ambience + voice); check with `earshot critique` (its "no music" flag is expected).

Build: `python3 voice.py` → (write verse.js from the APIs, see the original session) → `python3 timeline.py` (needs sfx/ from openverse) → `node render.mjs frames 30 6` → ffmpeg mux.
