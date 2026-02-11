# 🛠️ Promptcheck – Local Development & Release Manual

This document explains **exactly** how to:
- work on the code
- use virtual environments
- test locally
- install the CLI
- commit & push changes
- create releases safely

---

## 1️⃣ Project Structure (reference)

```
promptcheck/              ← repo root
│
├─ promptcheck/            ← Python package
│   ├─ cli.py
│   ├─ __init__.py
│   └─ .gitignore
│
├─ pyproject.toml
├─ README.md
├─ LICENSE
├─ .gitignore
└─ venv/                   ← local virtual environment (NOT committed)
```

---

## 2️⃣ First-time setup (only once per machine)

### Create virtual environment
```bat
python -m venv venv
```

### Activate virtual environment
```bat
venv\Scripts\activate
```

You should see:
```
(venv)
```

---

## 3️⃣ Install promptcheck in editable (dev) mode

Before reinstalling (recommended if you changed dependencies or entry points), uninstall any existing version:

```bat

```

Then install in editable mode. This makes `promptcheck` update automatically when you edit code.

```bat
python -m pip install -e .
```

Verify:
```bat
promptcheck --help
```

---

## 4️⃣ Everyday development workflow

### 4.1 Edit code
Edit:
```
promptcheck/cli.py
```

(No compilation step needed — Python is interpreted.)

---

### 4.2 Test locally
```bat
promptcheck test_prompt.txt
```

With options:
```bat
promptcheck test_prompt.txt --json
promptcheck test_prompt.txt --ai
```

---

### 4.3 Run tests
Just re-run the CLI after edits — editable install picks up changes automatically.

---

## 5️⃣ Git workflow (MOST IMPORTANT SECTION)

### Check status
```bat
git status
```

### Stage changes
```bat
git add .
```

### Commit
```bat
git commit -m "Describe what changed"
```

Example:
```bat
git commit -m "Improve AI cost estimation logic"
```

---

### Push to GitHub
```bat
git push origin main
```

⚠️ **Never force-push unless you rebased history** (rare).

---

## 6️⃣ Releasing a new version (safe process)

### 6.1 Update version
If/when you add a version number (recommended later), update it in `pyproject.toml`.

---

### 6.2 Commit release changes
```bat
git add .
git commit -m "Release v0.1.3"
```

---

### 6.3 Create a tag
```bat
git tag v0.1.3
```

### Push tag
```bat
git push origin v0.1.3
```

---

### 6.4 Create GitHub Release (IMPORTANT)

1. GitHub → **Releases**
2. **Draft new release**
3. Tag: `v0.1.3`
4. ✅ Check **Set as latest release**
5. Publish

📌 **Tags do NOT automatically become “Latest” — releases do.**

---

## 7️⃣ Virtual environment rules (very important)

### Activate venv before working
```bat
venv\Scripts\activate
```

### Deactivate when done
```bat
deactivate
```

### Never commit `venv/`
Already handled by `.gitignore`.

---

## 8️⃣ Installing promptcheck on another machine (dev)

```bat
git clone https://github.com/alexandeo-tech/promptcheck.git
cd promptcheck
python -m venv venv
venv\Scripts\activate
python -m pip install -e .
```

---

## 9️⃣ Installing promptcheck for users (current state)

For now (before PyPI):

```bat
git clone https://github.com/alexandeo-tech/promptcheck.git
cd promptcheck
python -m pip install -e .
```

Later, when published to PyPI:
```bat
pip install promptcheck
```

---

## 🔐 10️⃣ Security rules (DO NOT BREAK THESE)

- ❌ Never commit `.env`
- ❌ Never commit API keys
- ❌ Never hardcode secrets
- ✅ Use environment variables
- ✅ Keep AI optional & gated

---

## 11️⃣ Useful Git recovery commands (reference)

Abort a rebase:
```bat
git rebase --abort
```

Continue a rebase:
```bat
git rebase --continue
```

Check current branch:
```bat
git branch
```

Check repo root:
```bat
git rev-parse --show-toplevel
```

---

## 12️⃣ Recommended Git config (avoid Vim pain)

Use Notepad:
```bat
git config --global core.editor "notepad"
```

Or VS Code:
```bat
git config --global core.editor "code --wait"
```

---

## ✅ Final mental model (remember this)

- Python: **edit → run**
- Git: **edit → add → commit → push**
- Release: **commit → tag → push tag → GitHub release**
- Latest release = **GitHub Release UI**, not tag

---

This file is safe to keep at the root of the repository as a personal and team reference.

