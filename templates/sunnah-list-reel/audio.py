"""Soundtrack: CC0 crickets bed + CC0 UI cues (uisfx 'rubber' pack) placed on the film's own cue list (cues.json)."""
import json, subprocess, numpy as np, soundfile as sf
SR, DUR = 48000, 61.0
U = "/root/.claude/skills/real-sfx/vendor/node_modules/uisfx/sounds/"
KIND = {  # kind -> (file, gain dB)
    "pop": ("rubber/select", -6), "big": ("rubber/achievement", -4), "notify": ("rubber/notification", -6),
    "open": ("rubber/open", -6), "swipe": ("rubber/swipe", -9), "whoosh": ("rubber/swipe", -5),
    "drop": ("organic/drop", -5), "sparkle": ("dreamy/bonus", -9), "success": ("rubber/success", -5),
    "tick": ("rubber/check", -6), "check": ("rubber/check", -5), "lock": ("dreamy/lock", -5),
    "progress": ("rubber/progress-step", -8), "complete": ("rubber/complete", -5), "sleep": ("dreamy/sleep", -5),
    "type": ("rubber/typing", -12), "hl": ("rubber/select", -7),
}
def load(path, start=0, length=None):
    cmd = ["ffmpeg", "-v", "error", "-ss", str(start)] + (["-t", str(length)] if length else []) + ["-i", path, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, np.float32).reshape(-1, 2).copy()
N = int(SR * DUR); mix = np.zeros((N, 2), np.float32)
def place(sig, t, g, pan=0.0):
    i = int(t * SR); m = min(len(sig), N - i)
    if m > 0: mix[i:i + m] += sig[:m] * 10 ** (g / 20) * np.array([np.sqrt(.5 * (1 - pan)), np.sqrt(.5 * (1 + pan))]) * 1.414
bed = load("sfx/cricket_night_ambience_lebanon_pine_forest__wav_6a06e64a.mp3", 10, DUR)
bed[: int(.3 * SR)] *= np.linspace(0, 1, int(.3 * SR))[:, None]
place(bed, 0, -17)
cues = json.load(open("cues.json"))
for n, c in enumerate(cues):
    f, g = KIND[c["kind"]]
    place(load(U + f + ".mp3"), c["t"], g, pan=0.35 * np.sin(n * 2.1))   # spread the cues across the stereo field
t = np.arange(N) / SR
mix *= np.minimum(1, (DUR - t) / .6)[:, None]
mix /= np.abs(mix).max() / 10 ** (-1.5 / 20)
sf.write("audio_raw.wav", mix, SR)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", "audio_raw.wav", "-af", "loudnorm=I=-15:TP=-1.5:LRA=11", "-ar", str(SR), "audio.wav"], check=True)
print(len(cues), "cues,", round(len(cues) / DUR, 2), "per second")
