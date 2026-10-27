<!-- video-kit:start -->
# Claude Video Starter Kit — which tool for which job

- **Any video** (reel, trailer, ad, explainer, lyric video): use the `video-in-code` skill. Storyboard first, check stills before the full render, check a contact sheet at the end, save MP4s in `videos/` and push them.
- **Motion quality**: read `motion-design` (timing, easing, choreography); `gsap-*` for timelines; `threejs-*` for 3D.
- **Copy a look from references**: `design-dna`.
- **Sound, in this order**: find real recordings with `openverse` (CC0 first, keep CREDITS.csv) → place effects with `real-sfx` (or `real-sound` for a full licensed soundtrack) → check by ear with `earshot` before saying anything about how audio sounds.
- **Voices**: Kokoro / Piper (see `video-in-code`). Heavy tools come from `sh /tmp/kit/install.sh --media`.
- **Facts**: never invent facts, quotes, verses or hadiths; fetch them from a reliable source and show the reference.
- **Persistence**: cloud sessions are wiped; push finished work to GitHub.
- The project's own CLAUDE.md (brand, colours, fonts, rules) overrides this guide.
<!-- video-kit:end -->
