"""Voice placement + word timings -> timeline.js and voice.wav (48 kHz stereo)."""
import json, numpy as np, soundfile as sf
SR, DUR = 48000, 32.5
STARTS = [0.3, 3.5, 5.9, 8.3, 13.8, 20.0, 26.3]
lines = json.load(open("voice/lines.json"))
N = int(SR * DUR); voc = np.zeros(N, np.float32); TL = []
for L, t0 in zip(lines, STARTS):
    s, sr = sf.read(L["file"], dtype="float32")
    env = np.abs(s) > 10 ** (-38 / 20); a, b = np.argmax(env) / sr, (len(s) - np.argmax(env[::-1])) / sr
    words = L["text"].split(); w = [len(x.strip(",.?:")) + 2 + (4 if x[-1] in ",.?:" else 0) for x in words]
    c = np.concatenate([[0], np.cumsum(w)]) / sum(w)
    TL.append({"text": L["text"], "start": round(t0 + a, 3), "end": round(t0 + b, 3), "words": [{"w": x, "t": round(t0 + a + (b - a) * c[i], 3)} for i, x in enumerate(words)]})
    v = np.interp(np.arange(0, len(s), sr / SR), np.arange(len(s)), s).astype(np.float32)
    i = int(t0 * SR); voc[i:i + len(v)] += v[:N - i]
open("timeline.js", "w").write("window.TL = " + json.dumps(TL) + ";\n")
sf.write("voice.wav", np.stack([voc, voc], 1), SR)
print("ok; last line ends", TL[-1]["end"])
