"""Builds timeline.js (line + word timings for the film) and audio.wav (voice + real ambience, no music)."""
import json, subprocess, numpy as np, soundfile as sf

SR = 48000
DUR = 46.0
STARTS = [0.6, 3.6, 7.4, 10.4, 16.6, 21.3, 24.0, 26.8, 31.0, 33.6, 38.4]
lines = json.load(open("voice/lines.json"))


def load(path, start=0.0, length=None):
    cmd = ["ffmpeg", "-v", "error", "-ss", str(start)] + (["-t", str(length)] if length else []) + ["-i", path, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, np.float32).reshape(-1, 2).copy()


def db(x): return 10 ** (x / 20)


N = int(SR * DUR)
amb = np.zeros((N, 2), np.float32)
voc = np.zeros((N, 2), np.float32)


def place(buf, sig, t, gain_db=0.0, fade_in=0.0, fade_out=0.0):
    sig = sig * db(gain_db)
    n = len(sig)
    if fade_in: sig[: int(fade_in * SR)] *= np.linspace(0, 1, int(fade_in * SR))[:, None]
    if fade_out: sig[n - int(fade_out * SR):] *= np.linspace(1, 0, int(fade_out * SR))[:, None]
    i = int(t * SR); m = min(n, N - i)
    buf[i:i + m] += sig[:m]


# --- voice + word timings
TL = []
for L, t0 in zip(lines, STARTS):
    s, sr = sf.read(L["file"], dtype="float32")
    env = np.abs(s) > db(-38)
    a, b = np.argmax(env) / sr, (len(s) - np.argmax(env[::-1])) / sr
    words = L["text"].split()
    w = [len(x.strip(",.?:")) + 2 + (4 if x[-1] in ",.?:" else 0) for x in words]
    c = np.concatenate([[0], np.cumsum(w)]) / sum(w)
    TL.append({"text": L["text"], "start": round(t0 + a, 3), "end": round(t0 + b, 3),
               "words": [{"w": x, "t": round(t0 + a + (b - a) * c[i], 3)} for i, x in enumerate(words)]})
    v = np.repeat(s[:, None], 2, 1)
    v = np.interp(np.arange(0, len(s), sr / SR), np.arange(len(s)), s)  # resample 24k -> 48k
    place(voc, np.repeat(v[:, None], 2, 1).astype(np.float32), t0, 0)
open("timeline.js", "w").write("window.TL = " + json.dumps(TL) + ";\n")

# --- ambience (real CC0 recordings, see sfx/CREDITS.csv)
place(amb, load("sfx/Rainy_night_c1089776.mp3", 0.6, 29), 0.0, -4, 0.12, 5.0)                # rain, starts with distant thunder
place(amb, load("sfx/Soft_Wind_Ambience_wav_bc293722.mp3", 5, 36), 10.0, -14, 3.0, 3.0)  # soft wind under the verse
place(amb, load("sfx/squeaky_door_hinge_open_and_close_3ca9aeff.mp3", 0.9, 1.7), 12.75, -12, 0.05, 0.4)
place(amb, load("sfx/Low_impact_wav_a48224d6.mp3", 0, 5), 13.0, -7, 0.0, 1.5)              # door opens, light floods in
place(amb, load("sfx/dawn_chorus_wav_1a9c8792.mp3", 92.7, 23), 23.5, -9, 4.0, 2.5)        # dawn after "forgives all sins"
place(amb, load("sfx/Low_impact_wav_a48224d6.mp3", 0, 4), 31.95, -13, 0.0, 1.5)            # "ALL"
place(amb, load("sfx/Low_impact_wav_a48224d6.mp3", 0, 4.6), 41.4, -8, 0.0, 1.2)             # end card
place(amb, load("sfx/Soft_Wind_Ambience_wav_bc293722.mp3", 20, 6), 40.5, -6, 1.0, 1.0)      # keep the end card alive

# duck ambience under the voice (-7 dB, smooth)
venv = np.abs(voc).max(1)
k = int(0.25 * SR)
gate = np.convolve((venv > db(-40)).astype(np.float32), np.ones(k) / k, "same")
amb *= (1 - (1 - db(-7)) * np.clip(gate * 1.5, 0, 1))[:, None]

mix = amb + voc * db(-1)
t = np.arange(N) / SR
mix *= (np.minimum(1, t / 0.1) * np.minimum(1, (DUR - t) / 0.9))[:, None]
mix /= max(1e-9, np.abs(mix).max()) / db(-1.5)
sf.write("audio_raw.wav", mix, SR)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", "audio_raw.wav", "-af", "loudnorm=I=-14:TP=-1.5:LRA=9", "-ar", str(SR), "audio.wav"], check=True)
print("ok", len(TL), "lines; last line ends", TL[-1]["end"])
