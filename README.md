# Claudepreneur Starter Course

**Learn Claude Code from zero.** 6 lessons, ~60 minutes, all free.

Build a complete carousel content pipeline — from CLAUDE.md to real Canva carousel images. Pure education: CLAUDE.md, brand files, skills, agents, MCP.

## What You'll Build

- **Lesson 1:** Your AI's Brain — build a CLAUDE.md so Claude knows your business
- **Lesson 2:** Your First Skill — hand-build a carousel copy writer
- **Lesson 3:** The Architecture Upgrade — brand.md, offer.md, icp.md + research
- **Lesson 4:** Build Skills From Examples — caption writer from real captions
- **Lesson 5:** Your AI Team — a carousel agent that orchestrates everything
- **Lesson 6:** Connect to Canva — MCP turns text into real carousel images

## Prerequisites

You need two things on your laptop before starting:

1. **A terminal** — macOS Terminal, iTerm, Windows Terminal, or the built-in terminal in VS Code / Cursor
2. **Claude Code** — Anthropic's CLI tool (installation steps below)

> **Prefer Cursor?** Claude Code works great inside Cursor's built-in terminal. If you already use Cursor, just open the terminal panel (`Ctrl+`` `) and follow the steps below — no separate terminal needed.

---

## Step 1: Install Claude Code

Claude Code runs in your terminal. Pick your operating system below and follow the instructions.

### macOS / Linux / WSL

Open your terminal and paste:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

> *On Mac: search "Terminal" in Spotlight. On Linux/WSL: open your default terminal.*

### Windows (PowerShell)

Open **PowerShell** and paste:

```powershell
irm https://claude.ai/install.ps1 | iex
```

### Verify it worked

After installing, run:

```bash
claude --version
```

You should see a version number. If you get "command not found", close your terminal, open a new one, and try again.

### First-time setup

The first time you run `claude`, it will ask you to log in to your Anthropic account. Just follow the prompts — it takes about 30 seconds.

---

## Step 2: Download the Course

```bash
git clone https://github.com/claudepreneur/crash-course.git
cd crash-course
```

> **Don't have git?**
> - **macOS:** Open Terminal and type `git`. macOS will prompt you to install it automatically.
> - **Windows:** Download from [git-scm.com](https://git-scm.com) and install.
> - **Alternative:** Click the green "Code" button on GitHub, then "Download ZIP". Unzip it and open a terminal inside that folder.

---

## Step 3: Install the Course Files

```bash
./install.sh
```

> **Windows users:** Run `bash install.sh` instead. If that doesn't work, install [Git Bash](https://git-scm.com) and run the command from there.

This copies the course skills into Claude Code. It takes a few seconds.

---

## Step 4: Start the Course

Open Claude Code in your terminal:

```bash
claude
```

Then type:

```
/cos-course:start
```

That's it — the course will guide you from here.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `claude: command not found` | Close and reopen your terminal. If still broken, run the install command from Step 1 again |
| `permission denied` on install.sh | Run `chmod +x install.sh` first, then `./install.sh` |
| `git: command not found` | See the "Don't have git?" note above |

---

## Gifts

Each lesson unlocks a gift:
- Cheat sheet (commands, shortcuts, concepts)
- 20 prompts that work 10x better with a CLAUDE.md
- Brand file templates
- Skill ideas library
- Agent workflow templates
- MCP tools guide + Business-in-a-Box prompt pack

Saved to `~/.claudepreneur/crash-course/gifts/`

---

By [Claudepreneur](https://claudepreneur.com) — Kevin Fernandes
