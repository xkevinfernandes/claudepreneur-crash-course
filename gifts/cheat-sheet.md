# Claude Code Cheat Sheet

> Your quick reference for Claude Code commands, shortcuts, and concepts.

---

## Core Concepts

| Concept | What It Is |
|---------|-----------|
| **CLAUDE.md** | A file Claude reads before every conversation. Your business context. |
| **Brand Files** | Separate files for voice (brand.md), offer (offer.md), audience (icp.md). More detail = better output. |
| **Skills** | Text files with instructions that Claude follows. Reusable commands (e.g., `/carousel-copy`). |
| **Agents** | Specialist team members Claude delegates to. Live in `.claude/agents/`. Have access to tools. |
| **MCP** | Model Context Protocol — connects Claude to external tools (Canva, Notion, Calendar, etc). |

## Modes

| Mode | What It Does | How to Use |
|------|-------------|------------|
| **Normal mode** | Claude reads + writes files, runs commands | Default mode |
| **Plan mode** | Claude plans without changing anything — safe for exploring | Type `plan` or use the mode selector |
| **Edit mode** | Claude focuses on editing specific files | Shift+Tab to toggle |

## Essential Shortcuts

| Shortcut | What It Does |
|----------|-------------|
| `Escape` | Cancel / go back / dismiss |
| `Ctrl+C` | Stop what Claude is doing |
| `/command` | Run a skill (slash command) |
| `Shift+Tab` | Toggle compact mode |
| `Up arrow` | Recall previous message |

## Key File Locations

| File | Location | Purpose |
|------|----------|---------|
| Project CLAUDE.md | `./CLAUDE.md` | Context for this project |
| Global CLAUDE.md | `~/.claude/CLAUDE.md` | Context for ALL projects |
| Skills | `~/.claude/skills/` | Your custom skills (global) |
| Project skills | `.claude/skills/` | Skills for this project only |
| Agents | `.claude/agents/` | Your agent files |
| Brand files | `./brand-files/` | voice, offer, audience context |

## The 5 Building Blocks

```
  1. CLAUDE.md    = Brain      (who you are, what you do)
  2. Brand Files  = Context    (voice, offer, audience — deep detail)
  3. Skills       = Hands      (reusable commands, one task each)
  4. Agents       = Team       (orchestrate multiple tasks)
  5. MCP          = Phone Lines (connect to real tools)
```

## Skill Anatomy (3 Parts)

```markdown
---
description: "What this skill does — shows up in the / menu"
---

# Instructions

Tell Claude what to do in plain English.
Step by step. Be specific.
Reference brand files for personalization.

## Rules

- Guardrails and standards
- Tone and formatting constraints
- What NOT to do
```

## Agent Anatomy

```markdown
---
name: agent-name
description: "What this agent does"
tools: Read, Write, Glob, Grep, Bash
---

# Instructions

What this agent does and how.
Reads brand files for context.
Produces a complete deliverable.

## Rules

- Standards and constraints
```

## The Carousel Pipeline You Built

```
  Topic
    → carousel-copy skill (10 slides)
    → caption-writer skill (Instagram caption)
    → carousel-writer agent (both at once)
    → Canva MCP (real designed images)
```

## Quick Prompts That Work With Brand Files

**Content:**
- "Give me 5 carousel topics for this week"
- "Write an Instagram caption about [topic]"
- "Draft a LinkedIn post about [lesson]"

**Client Work:**
- "Write a welcome message for [client name]"
- "Create a session prep sheet for tomorrow's call"
- "Draft a follow-up for [prospect]"

**Strategy:**
- "What content gaps exist in my niche?"
- "Write 3 positioning statements for my business"
- "Help me plan my content for next week"

---

*From the Claudepreneur Starter Course — claudepreneur.com*
