# Edunos Claude Toolkit

Mes skills, agents et outils pour Claude Code, utilisables dans **n'importe quel projet**.

## Contenu

| Dossier | Quoi |
|---|---|
| `skills/video-in-code` | Faire des vidéos en code (trailers, pubs, Reels/TikTok, explainers) avec musique et voix off |
| `skills/motion-design` | Principes d'animation (LottieFiles) |
| `skills/gsap-*` | GSAP officiel (GreenSock) : timelines, easing, plugins |
| `skills/threejs-*` | Three.js : 3D, lumières, shaders, post-processing |
| `skills/design-dna` | Extraire un style depuis des références et le réappliquer |
| `skills/cast`, `paint`, `bunshin` (+ `_jutsu/`) | genjutsu : animation et direction artistique pour sites et applis |
| `skills/real-sfx` | Sound design avec de **vrais** sons enregistrés (whoosh, hits, UI…) calés à l'image + 78 sons UI CC0 |
| `skills/earshot`, `skills/real-sound` | earshot : Claude « écoute » l'audio (décrire, classer, critiquer une bande-son) ; real-sound : bande-son pro à partir d'enregistrements sous licence |
| `skills/openverse` | Chercher et télécharger sons et images libres (CC0, CC BY) via Openverse, avec CREDITS.csv |
| `agents/` | 283 agents spécialisés (agency-agents) : marketing, design, ventes, dev… |
| `templates/canvas-film` | Exemple complet de film en code (style aquarelle, musique synthétisée) |
| `templates/remotion` | Projet Remotion (vidéo en React) avec voix off |
| `install.sh` | Installe tout dans `~/.claude` + voix (Kokoro, Piper) + Agent Reach + earshot |

## Installation

**Sessions cloud (claude.ai/code)** : dans les réglages de l'environnement, *Setup script*, ajouter :

```bash
git clone --depth 1 https://github.com/JimmyDamelio/edunos-claude-toolkit /tmp/edunos-toolkit && sh /tmp/edunos-toolkit/install.sh
```

**Sur ton ordinateur** :

```bash
git clone https://github.com/JimmyDamelio/edunos-claude-toolkit && sh edunos-claude-toolkit/install.sh
```

`sh install.sh --light` installe seulement les skills et agents (sans téléchargements).

## Sources (licence MIT)

LottieFiles/motion-design-skill · Leonxlnx/earshot · real-sfx · WordPress/openverse (API) · greensock/gsap-skills · CloudAI-X/threejs-skills · zanwei/design-dna · AThevon/genjutsu · msitarzewski/agency-agents · Panniantong/Agent-Reach · thewh1teagle/kokoro-onnx · rhasspy/piper. Leurs licences sont conservées dans les dossiers concernés.
