"""Ad soundtrack: voice + music bed (music.mp3 if present, else a soft lo-fi bed made in code) + CC0 UI cues, ducked and loudness-normalised."""
import json, os, subprocess, numpy as np, soundfile as sf
SR, DUR = 48000, 32.5
N = int(SR * DUR); t = np.arange(N) / SR
U = "/root/.claude/skills/real-sfx/vendor/node_modules/uisfx/sounds/"
KIND = {"pop": ("rubber/select", -8), "whoosh": ("soft/swipe", -6), "tick": ("rubber/check", -12), "hit": ("cinematic/badge", -8),
        "swipe": ("soft/swipe", -9), "sparkle": ("dreamy/bonus", -10), "type": ("mechanical/typing", -16), "press": ("rubber/press", -8),
        "check": ("rubber/check", -8), "success": ("rubber/success", -7)}


def load(path, start=0, length=None):
    cmd = ["ffmpeg", "-v", "error", "-ss", str(start)] + (["-t", str(length)] if length else []) + ["-i", path, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, np.float32).reshape(-1, 2).copy()


def lowpass(x, cut):
    X = np.fft.rfft(x, axis=0); f = np.fft.rfftfreq(len(x), 1 / SR)
    X *= (1 / np.sqrt(1 + (f / cut) ** 4))[:, None]  # gentle 2nd-order-like roll-off
    return np.fft.irfft(X, len(x), axis=0).astype(np.float32)


def lofi_bed():
    bpm = 84; beat = 60 / bpm; rng = np.random.default_rng(3)
    hz = lambda m: 440 * 2 ** ((m - 69) / 12)
    chords = [[53, 57, 60, 64], [52, 55, 59, 62], [50, 53, 57, 60], [48, 52, 55, 59]]  # Fmaj7 Em7 Dm7 Cmaj7
    bed = np.zeros((N, 2), np.float32)
    bar = 4 * beat; nb = int(DUR / bar) + 1
    for b in range(nb):
        ch = chords[b % 4]; t0 = b * bar
        for k, m in enumerate(ch):  # soft electric-piano chord, slightly strummed
            st = t0 + k * .025; n = int(bar * 1.05 * SR); i = int(st * SR)
            if i >= N: continue
            tt = np.arange(min(n, N - i)) / SR; f = hz(m)
            tone = (np.sin(2 * np.pi * f * tt) + .35 * np.sin(2 * np.pi * 2 * f * tt) * np.exp(-tt * 3) + .12 * np.sin(2 * np.pi * 3 * f * tt) * np.exp(-tt * 5))
            env = np.minimum(1, tt / .01) * np.exp(-tt * .9)
            bed[i:i + len(tt)] += (tone * env * .08)[:, None] * np.array([1 - k * .1, .7 + k * .1])
        # bass
        i = int(t0 * SR); tt = np.arange(min(int(bar * SR), N - i)) / SR
        if len(tt): bed[i:i + len(tt)] += (np.sin(2 * np.pi * hz(ch[0] - 12) * tt) * np.exp(-tt * 1.2) * .12)[:, None]
    for k in range(int(DUR / beat) + 1):  # soft kick on 1 & 3, hat on offbeats
        st = k * beat; i = int(st * SR)
        if i >= N: break
        if k % 2 == 0:
            tt = np.arange(min(int(.35 * SR), N - i)) / SR
            bed[i:i + len(tt)] += (np.sin(2 * np.pi * (50 + 70 * np.exp(-tt * 30)) * tt) * np.exp(-tt * 9) * .28)[:, None]
        j = int((st + beat / 2) * SR); tt = np.arange(min(int(.06 * SR), max(0, N - j))) / SR
        if len(tt): bed[j:j + len(tt)] += (rng.standard_normal(len(tt)) * np.exp(-tt * 70) * .03)[:, None]
    bed += (rng.standard_normal((N, 2)) * .004 * (rng.random((N, 1)) > .9995) * 30).astype(np.float32)  # vinyl crackle
    return lowpass(bed, 5200)


voice, _ = sf.read("voice.wav", dtype="float32")
music = load("music.mp3", 0, DUR) if os.path.exists("music.mp3") else lofi_bed()
music = np.pad(music, ((0, max(0, N - len(music))), (0, 0)))[:N]
music *= (np.minimum(1, t / .6) * np.minimum(1, (DUR - t) / 1.5))[:, None]
sfx = np.zeros((N, 2), np.float32)
for n, c in enumerate(json.load(open("cues.json"))):
    f, g = KIND.get(c["kind"], ("rubber/select", -8))
    s = load(U + f + ".mp3"); i = int(c["t"] * SR); m = min(len(s), N - i)
    if m > 0:
        pan = .35 * np.sin(n * 2.1); sfx[i:i + m] += s[:m] * 10 ** (g / 20) * np.array([np.sqrt(1 - pan), np.sqrt(1 + pan)])
# duck the music under the voice
venv = np.abs(voice).max(1); k = int(.3 * SR)
gate = np.convolve((venv > 10 ** (-40 / 20)).astype(np.float32), np.ones(k) / k, "same")
music *= (1 - (1 - 10 ** (-9 / 20)) * np.clip(gate * 1.5, 0, 1))[:, None]
mix = voice * 1.0 + music * 10 ** (-6 / 20) + sfx
mix /= np.abs(mix).max() / 10 ** (-1.5 / 20)
sf.write("audio_raw.wav", mix, SR)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", "audio_raw.wav", "-af", "loudnorm=I=-14:TP=-1.5:LRA=9", "-ar", str(SR), "audio.wav"], check=True)
print("music:", "music.mp3" if os.path.exists("music.mp3") else "lo-fi bed made in code")
