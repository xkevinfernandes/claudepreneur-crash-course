# Claudepreneur Starter Course — Setup Guide

## Step 1: Get a Claude Subscription

You need a Claude Pro ($20/mo) or Max subscription.

Go to [claude.ai/pricing](https://claude.ai/pricing/max) and subscribe.

This gives you access to both **Claude on the web** AND **Claude Code**. No API keys needed.

---

## Step 2: Open Your Terminal

- **Mac:** Press `Cmd + Space`, type "Terminal", hit Enter
- **Windows:** Press `Win + R`, type "powershell", hit Enter
- **Linux:** Press `Ctrl + Alt + T`

---

## Step 3: Install Claude Code

Run this in your terminal:

**Mac / Linux / WSL**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows (PowerShell)**
```powershell
irm https://claude.ai/install.ps1 | iex
```

To verify it worked, run:
```bash
claude --version
```

If you get "command not found", close your terminal, open a new one, and try again.

---

## Step 4: Sign In to Claude Code

Type `claude` in your terminal.

A browser window opens — sign in with your Claude account, authorize Claude Code, and you're connected.

No API keys, no tokens, no environment variables. Just sign in and go.

---

## Step 5: Download the Course

First, create a folder where you want to keep this course. Pick somewhere you'll remember — Desktop, Documents, wherever makes sense to you.

Then open your terminal and `cd` into that folder:

```bash
cd /path/to/your/folder
```

For example:
```bash
cd ~/Documents
```

Now clone the course into that folder:

```bash
git clone https://github.com/claudepreneur/crash-course.git
cd crash-course
```

> **Don't have git?**
> - **Mac:** Type `git` in Terminal — macOS will prompt you to install it automatically.
> - **Windows:** Download from [git-scm.com](https://git-scm.com) and install.
> - **Alternative:** Click the green "Code" button on GitHub, then "Download ZIP". Unzip it into your chosen folder and open a terminal inside it.

Then run the installer:

```bash
./install.sh
```

> **Windows users:** Run `bash install.sh` instead.

This copies the course files into Claude Code. Takes a few seconds.

---

## Step 6: Start the Course

Open Claude Code (type `claude` in your terminal) and then type:

```
/cos-course:start
```

That's it. You're in.

---

## Optional: Set Up Canva Integration (MCP)

If you want Claude to create carousels directly in Canva, you need to install the browser automation server:

```bash
cd MCPs
npm install
npx playwright install chromium
```

Then restart Claude Code. The first time you duplicate a template, Playwright will open a browser — log into Canva there. Your session is saved in `MCPs/.playwright-profile/` for future runs.

> **Note:** You also need the Canva MCP enabled in Claude Code. This is configured automatically via the course's `.mcp.json`.

---

## Optional: Install Cursor

You don't need a code editor for this course — everything runs in the terminal. But if you want an easy way to browse and edit your files, we recommend [Cursor](https://cursor.com). It's free and has a built-in terminal you can use for Claude Code too.
