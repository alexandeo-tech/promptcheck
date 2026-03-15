# promptcheck

## ⭐ Support PromptCheck

If you find this project useful:

⭐ **Star the repository**
💬 **Share feedback or ideas in Discussions / Issues**

Even a quick star helps others discover the project and supports development.

👀 Watch the repository if you'd like to follow updates and new features.

This project is still evolving and many improvements are planned.

Early feedback and suggestions are very welcome.

🚀 Example
promptcheck analyze "Explain quantum computing simply"

Example output:

Prompt Quality Score: 7.8 / 10
Ambiguity Risk: Medium
Hallucination Risk: Low
Estimated Tokens: 45
Estimated Cost: $0.0001

Suggestions:
- Add target audience
- Specify output format


🛣 Roadmap

Planned improvements:
CI/CD integration for prompt validation
Prompt regression testing
GitHub Actions integration
Prompt security scanning
VS Code extension
Prompt dataset benchmarking


💬 Feedback & Ideas

Have ideas for prompt validation or prompt engineering tools?

Start a discussion here:
https://github.com/alexandeo-tech/promptcheck/discussions

Real developer feedback helps shape the project.


> Treat prompts like production artifacts — validate them before they ship.

**promptcheck** is a lightweight CLI tool that analyzes AI prompts for quality, risk, and cost **before** you run them in production.

It helps developers catch prompt issues early — similar to how we lint code or validate configuration files.

No UI. No hype. Just useful signal.

---

## 👥 Who is this for?

- Developers experimenting with LLM prompts
- Engineers learning prompt safety and structure
- Anyone who wants early signal on prompt risk and cost
- Future CI/CD use (early-stage project)

---

## ✨ Features

### ✅ Deterministic (Free)

- Prompt quality scoring (0–10)
- Hallucination & ambiguity risk analysis
- Token usage & cost estimation (offline heuristic)
- Concrete improvement suggestions
- JSON output for automation

### 🤖 AI-Powered Analysis (Optional – Bring Your Own Key)

- Optional AI analysis (`--ai`)
- Uses **your own OpenAI API key**
- AI usage is billed directly to **your OpenAI account**
- Local free trial (20 AI runs per machine)
- AI is **off by default**

---

## 🔍 Why promptcheck?

Prompt bugs are invisible until users hit them.

Unlike code, prompts are rarely validated — yet they directly affect system behavior, reliability, and cost.

As teams experiment with LLMs, prompts increasingly behave like **configuration and control logic**, but without the safeguards we apply to other production artifacts.

**promptcheck treats prompts as first-class artifacts**, not just strings — providing early signal before problems reach users.

---

## 📦 Installation (local / dev)

```bash
git clone https://github.com/alexandeo-tech/promptcheck.git
cd promptcheck
python -m venv venv
venv\Scripts\activate   # Windows
python -m pip install -e .
