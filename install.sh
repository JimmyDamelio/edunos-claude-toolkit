#!/bin/sh
# Edunos Claude toolkit — installs skills, agents and media tools into ~/.claude.
# Usage: sh install.sh            (everything)
#        sh install.sh --light    (skills + agents only, no downloads)
set -e
SRC="$(cd "$(dirname "$0")" && pwd)"
CL="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
mkdir -p "$CL/skills" "$CL/agents" "$CL/toolkit"
cp -R "$SRC/skills/." "$CL/skills/"
cp -R "$SRC/agents/." "$CL/agents/"
cp -R "$SRC/templates" "$CL/toolkit/"
echo "skills + agents installed in $CL"
[ "$1" = "--light" ] && exit 0

# Voice-over: Kokoro + Piper (models in /root/tts-models or ~/tts-models)
M="${TTS_MODELS:-$HOME/tts-models}"; mkdir -p "$M"
python3 -m pip install -q kokoro-onnx piper-tts soundfile numpy uv 2>/dev/null || pip install -q kokoro-onnx piper-tts soundfile numpy uv
get() { [ -s "$M/$2" ] || curl -fsSL -o "$M/$2" "$1"; }
get https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx kokoro-v1.0.onnx
get https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin voices-v1.0.bin
for v in fr/fr_FR/siwis/medium/fr_FR-siwis-medium en/en_US/lessac/medium/en_US-lessac-medium; do
  n=$(basename $v)
  get "https://huggingface.co/rhasspy/piper-voices/resolve/main/$v.onnx" "$n.onnx"
  get "https://huggingface.co/rhasspy/piper-voices/resolve/main/$v.onnx.json" "$n.onnx.json"
done
[ "$M" = /root/tts-models ] || ln -sfn "$M" /root/tts-models 2>/dev/null || true

# Agent Reach: read X/Twitter, YouTube subtitles, Reddit, GitHub… (read-only)
export PATH="$HOME/.local/bin:$PATH"
command -v agent-reach >/dev/null || { uv tool install -q https://github.com/Panniantong/Agent-Reach/releases/latest/download/agent-reach.zip && agent-reach setup >/dev/null; }
# earshot: lets Claude "listen" to audio (describe, rank, critique a soundtrack). CPU torch + package; models download on first use.
if [ ! -x "$HOME/.earshot-venv/bin/earshot" ]; then
  python3 -m venv "$HOME/.earshot-venv"
  "$HOME/.earshot-venv/bin/pip" install -q torch --index-url https://download.pytorch.org/whl/cpu
  "$HOME/.earshot-venv/bin/pip" install -q "earshot[mcp] @ git+https://github.com/Leonxlnx/earshot"
fi
mkdir -p "$HOME/.local/bin" "$HOME/.earshot"; ln -sf "$HOME/.earshot-venv/bin/earshot" "$HOME/.local/bin/earshot"
grep -q EARSHOT_HOME "$HOME/.bashrc" 2>/dev/null || echo 'export EARSHOT_HOME="$HOME/.earshot"; export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"

echo "toolkit ready: voices in $M, agent-reach $(agent-reach version 2>/dev/null | grep -o '"version": "[^"]*"' | cut -d'"' -f4)"
