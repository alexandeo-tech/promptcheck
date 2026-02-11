# promptcheck

**promptcheck** is a lightweight CLI tool that analyzes AI prompts for quality, risk, and cost *before* you run them in production.

It helps developers:
- Catch vague or risky prompts
- Reduce hallucination risk
- Control token usage and cost
- Improve prompt structure
- Automate prompt validation in CI/CD

No UI. No hype. Just useful signal.

---

## ✨ Features

### ✅ Deterministic (Free)
- Prompt quality scoring (0–10)
- Risk analysis (hallucination & cost)
- Concrete improvement suggestions
- Token & cost estimation (offline heuristic)
- JSON output for automation

### 🤖 AI-Powered Analysis (Optional, Bring Your Own Key)
- Optional AI deep analysis (`--ai`)
- Uses **your own OpenAI API key**
- AI usage is billed to **your OpenAI account**
- Includes a local free trial (20 AI runs)
- AI is **off by default** (no surprise costs)

---

## AI Usage Modes

promptcheck supports two AI usage modes:

### 1. Local AI — Bring Your Own API Key (Available Now)

- You provide your own OpenAI API key via environment variables
- AI calls are made directly from the CLI
- promptcheck does **not** proxy, store, or manage your key
- Usage is billed directly to your OpenAI account
- Includes a local, per-machine free trial (20 AI runs)

This mode is ideal for individual developers and local workflows.

---

### 2. Cloud AI — Managed Mode (Planned, Not Available Yet)

A managed cloud mode is planned for the future, where:

- No OpenAI API key is required
- AI usage is billed through a promptcheck subscription
- Monthly usage limits are enforced server-side
- Rate limiting and abuse protection are included

⚠️ **Cloud mode is not available yet.**  
No subscriptions, billing, or hosted AI services are currently offered.

---

## 🔐 Cost & Safety Notes

- promptcheck never ships with API keys
- All AI usage is explicit and opt-in
- AI features can be disabled instantly via a kill switch
- Local safety caps prevent runaway usage during testing
- No background or hidden AI calls are made
- No billing is enabled by default

---

## 📦 Installation (local / dev)

```bash
git clone https://github.com/YOUR_USERNAME/promptcheck.git
cd promptcheck
python -m venv venv
venv\Scripts\activate   # Windows
python -m pip install -e .
