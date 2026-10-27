#!/bin/sh
# Claude Video Starter Kit installer (companion to the "Prompt to Reel" guide).
#   sh install.sh            skills + guide + templates, ffmpeg and a headless browser (fast: for the environment setup script)
#   sh install.sh --media    + free voices (Kokoro, Piper) and earshot (lets Claude listen); 2-4 minutes, needs Full network access
#   sh install.sh --doctor   show what's installed
SRC="$(cd "$(dirname "$0")" && pwd)"
CL="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
M="$HOME/tts-models"
export PATH="$HOME/.local/bin:$PATH"

ok() { printf '  [x] %s\n' "$1"; }
no() { printf '  [ ] %s\n' "$1"; }
doctor() {
  echo "Claude Video Starter Kit: status"
  [ -f "$CL/skills/video-in-code/SKILL.md" ] && ok "skills ($(ls "$CL/skills" | wc -l) in $CL/skills)" || no "skills (run: sh install.sh)"
  command -v ffmpeg >/dev/null && ok "ffmpeg" || no "ffmpeg"
  node -e "require('playwright').chromium.executablePath()" >/dev/null 2>&1 || NODE_PATH="$(npm root -g)" node -e "require('playwright')" >/dev/null 2>&1 && ok "headless browser (playwright)" || no "headless browser (playwright)"
  python3 -c "import numpy" 2>/dev/null && ok "python numpy" || no "python numpy"
  [ -s "$M/kokoro-v1.0.onnx" ] && ok "voices: Kokoro + Piper ($M)" || no "voices (run: sh install.sh --media)"
  command -v earshot >/dev/null && ok "earshot (listening)" || no "earshot (run: sh install.sh --media)"
}
[ "$1" = "--doctor" ] && { doctor; exit 0; }

# 1. skills, templates and the routing guide
mkdir -p "$CL/skills" "$CL/kit"
cp -R "$SRC/skills/." "$CL/skills/"
cp -R "$SRC/templates" "$CL/kit/"
touch "$CL/CLAUDE.md"
python3 - "$CL/CLAUDE.md" "$SRC/GUIDE.md" <<'PY'
import re, sys
p, g = sys.argv[1], open(sys.argv[2]).read().strip()
s = re.sub(r"<!-- video-kit:start -->.*?<!-- video-kit:end -->\n?", "", open(p).read(), flags=re.S).rstrip()
open(p, "w").write((s + "\n\n" if s else "") + g + "\n")
PY
echo "skills, templates and guide installed in $CL"

# 2. ffmpeg, numpy and a headless browser if missing
command -v ffmpeg >/dev/null || { (apt-get update -qq && apt-get install -y -qq ffmpeg) >/dev/null 2>&1 && echo "ffmpeg installed"; }
python3 -c "import numpy" 2>/dev/null || python3 -m pip install -q numpy soundfile 2>/dev/null || pip install -q --break-system-packages numpy soundfile
if ! node -e "require('playwright')" >/dev/null 2>&1 && ! NODE_PATH="$(npm root -g)" node -e "require('playwright')" >/dev/null 2>&1; then
  npm install -g --silent playwright >/dev/null 2>&1 && npx --yes playwright install --with-deps chromium >/dev/null 2>&1 && echo "headless browser installed"
fi
[ "$1" = "--media" ] || { echo "done. For voices and earshot: sh $SRC/install.sh --media"; exit 0; }

# 3. --media: voices and earshot
python3 -m pip install -q kokoro-onnx piper-tts soundfile numpy 2>/dev/null || pip install -q --break-system-packages kokoro-onnx piper-tts soundfile numpy
mkdir -p "$M"
get() { [ -s "$M/$2" ] || curl -fsSL -o "$M/$2" "$1"; }
get https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx kokoro-v1.0.onnx
get https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin voices-v1.0.bin
for v in fr/fr_FR/siwis/medium/fr_FR-siwis-medium en/en_US/lessac/medium/en_US-lessac-medium; do
  n=$(basename $v)
  get "https://huggingface.co/rhasspy/piper-voices/resolve/main/$v.onnx" "$n.onnx"
  get "https://huggingface.co/rhasspy/piper-voices/resolve/main/$v.onnx.json" "$n.onnx.json"
done
if [ ! -x "$HOME/.earshot-venv/bin/earshot" ]; then
  python3 -m venv "$HOME/.earshot-venv"
  "$HOME/.earshot-venv/bin/pip" install -q torch --index-url https://download.pytorch.org/whl/cpu
  "$HOME/.earshot-venv/bin/pip" install -q "earshot[mcp] @ git+https://github.com/Leonxlnx/earshot"
fi
mkdir -p "$HOME/.local/bin" "$HOME/.earshot"; ln -sf "$HOME/.earshot-venv/bin/earshot" "$HOME/.local/bin/earshot"
grep -q EARSHOT_HOME "$HOME/.bashrc" 2>/dev/null || echo 'export EARSHOT_HOME="$HOME/.earshot"; export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
doctor
