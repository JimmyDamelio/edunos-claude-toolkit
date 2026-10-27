"""Ad voice-over: soft female voice (Kokoro). Writes voice/lNN.wav + voice/lines.json."""
import json, soundfile as sf
from kokoro_onnx import Kokoro
LINES = [
    "Everyone keeps asking what app made these videos.",
    "Here's the secret: there's no app.",
    "No editing. They're written.",
    "You describe the video to Claude, and it builds every frame, the sound, everything.",
    "Animated reels, cinematic quotes, launch trailers. Even if you've never edited anything.",
    "Prompt to Reel shows you exactly how, step by step, with fifty-six prompts ready to copy.",
    "Your first video is closer than you think. The link is in my bio.",
]
VOICE, SPEED = "af_heart", 0.93
k = Kokoro('/root/tts-models/kokoro-v1.0.onnx', '/root/tts-models/voices-v1.0.bin')
meta = []
for i, line in enumerate(LINES):
    s, sr = k.create(line, voice=VOICE, speed=SPEED, lang='en-us')
    f = f"voice/l{i:02d}.wav"; sf.write(f, s, sr)
    meta.append({"i": i, "text": line, "file": f, "dur": round(len(s) / sr, 3)})
    print(i, round(len(s) / sr, 2), line)
json.dump(meta, open("voice/lines.json", "w"), indent=1)
