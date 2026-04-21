# swarmcore
Patent Pending: GB2603013.0 (filed 10 Feb 2026) and related PCT applications.
Commercial use or derivative works may require licensing. Contact IBA@intentbound.com

**Lightweight multi-agent coordinator inspired by the Anthropic Claude Code leak**

While most forks focus on single agents or tools, Swarmcore brings the real power from the leak: a simple coordinator that orchestrates multiple agents working together (Researcher → Analyzer → Executor → Summarizer).

Combined with your other projects:
- Governed by IBA (`grk-html-2` + `iba-claw-starter`)
- Persistent memory via `dreamweave`
- Personality via `matey`

## Features
- Simple task decomposition and agent hand-off
- Built-in IBA governance hooks
- Easy to plug in Dreamweave memory and Matey companion
- Minimal and extensible

## Quick Start
```bash
git clone https://github.com/Grokipaedia/swarmcore.git
cd swarmcore
pip install -r requirements.txt
python example.py
