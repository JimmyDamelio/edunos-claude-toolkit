"""Voice-over lines with Kokoro (female). 'Allah' is re-phonemized as al-LAH."""
import json, re, soundfile as sf
from kokoro_onnx import Kokoro
from kokoro_onnx.tokenizer import Tokenizer

LINES = [
    "Have you ever felt like you've gone too far?",
    "Like your mistakes are too heavy to ever be forgiven?",
    "Like the door back to Allah has closed?",
    "Then listen to what Allah says to you.",
    "Say, O My servants who have transgressed against themselves, by sinning,",
    "do not despair of the mercy of Allah.",
    "Indeed, Allah forgives all sins.",
    "Indeed, it is He who is the Forgiving, the Merciful.",
    "Not some sins. All of them.",
    "And even while speaking of your mistakes, He calls you: My servants.",
    "So come back to Him. His door is still open.",
]
VOICE, SPEED = "af_heart", 0.86
k = Kokoro('/root/tts-models/kokoro-v1.0.onnx', '/root/tts-models/voices-v1.0.bin')
tok = Tokenizer()
meta = []
for i, line in enumerate(LINES):
    ph = tok.phonemize(line, 'en-us')
    ph = re.sub(r"ˈæl[əɑː]+", "ʌlˈɑː", ph)
    s, sr = k.create(ph, voice=VOICE, speed=SPEED, lang='en-us', is_phonemes=True)
    f = f"voice/l{i:02d}.wav"; sf.write(f, s, sr)
    meta.append({"i": i, "text": line, "file": f, "dur": round(len(s) / sr, 3), "ph": ph})
    print(i, round(len(s) / sr, 2), ph)
json.dump(meta, open("voice/lines.json", "w"), indent=1)
