# Claude Video Starter Kit

Skills, templates and an installer that turn **Claude Code** into a video studio: reels, trailers, explainers and animated ads made entirely in code, with real sound effects and free voice-overs.

Companion kit for the guide **Prompt to Reel**.

## Install (Claude Code on the web)

In your cloud environment settings (environment selector → settings icon), set **Network access** to **Full** and paste this into **Setup script**:

```bash
git clone --depth 1 https://github.com/JimmyDamelio/claude-video-starter-kit /tmp/kit && sh /tmp/kit/install.sh
```

In a session, ask Claude to run `sh /tmp/kit/install.sh --media` to add free voices (Kokoro, Piper) and earshot (lets Claude listen to audio), and `sh /tmp/kit/install.sh --doctor` to check everything.

**On your own computer** (Claude Code CLI): `git clone https://github.com/JimmyDamelio/claude-video-starter-kit && sh claude-video-starter-kit/install.sh`

## What's inside

| Folder | What |
|---|---|
| `skills/video-in-code` | The core workflow: storyboard, render frames in a headless browser, sound, ffmpeg, quality checks |
| `skills/motion-design` | Motion design principles (LottieFiles) |
| `skills/gsap-*` | Official GSAP skills (GreenSock) |
| `skills/threejs-*` | Three.js skills |
| `skills/design-dna` | Extract a visual style from references and reuse it |
| `skills/openverse` | Find openly licensed sounds and images, with credits |
| `skills/real-sfx`, `skills/real-sound`, `skills/earshot` | Sound design with real recordings, and listening tools |
| `templates/sunnah-list-reel` | Faceless-characters listicle reel (9:16, no voice, UI sound cues) |
| `templates/quran-reel` | Cinematic verse reel (9:16, voice-over, real ambience, verified Uthmani text) |
| `templates/remotion` | Remotion (React) video project |
| `GUIDE.md` | Routing guide, merged into `~/.claude/CLAUDE.md` |

## Credits and licences

See [THIRD_PARTY.md](THIRD_PARTY.md). Each third-party folder keeps its own licence. Not affiliated with Anthropic.
