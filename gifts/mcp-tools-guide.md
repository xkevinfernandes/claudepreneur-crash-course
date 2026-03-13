# MCP Tools — Connect Claude to Everything

> MCP (Model Context Protocol) lets Claude Code talk to external tools.
> These are the most useful ones for solopreneurs building with Claudepreneur.

---

## What Is MCP?

MCP is how Claude Code connects to external services. Instead of copy-pasting data between apps, Claude can directly read, write, and interact with your tools.

Think of it like giving Claude access to your team's toolbox — not just a chat window.

## How to Install MCP Servers

Add them to your Claude Code settings file (`~/.claude/settings.json`) or project settings (`.claude/settings.json`):

```json
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "@package/server-name"],
      "env": {
        "API_KEY": "your-key-here"
      }
    }
  }
}
```

---

## Recommended MCP Servers

### Notion
**What it does:** Read, create, update Notion pages and databases. Manage your content calendar, client CRM, project tracker — all from Claude Code.

**Use cases:**
- Save content ideas to your content calendar
- Create client records and update project status
- Query databases for reporting
- Build automated workflows

**Install:** Use the Notion MCP integration from Claude's built-in connectors (Settings → Integrations → Notion) or install manually.

### Canva
**What it does:** Create, edit, and export designs in Canva. Generate carousels, social posts, presentations.

**Use cases:**
- Generate carousel designs from text
- Create social media graphics
- Export designs as PNG/PDF
- Search your brand kit

**Install:** Available as a Claude integration (Settings → Integrations → Canva).

### Cal.com
**What it does:** Manage scheduling — create event types, check availability, manage bookings.

**Use cases:**
- Set up discovery call booking pages
- Check your upcoming schedule
- Manage availability
- Create new event types for workshops/calls

**Server:** `@calcom/mcp`

### Kit (ConvertKit)
**What it does:** Manage email subscribers, tags, sequences, and broadcasts.

**Use cases:**
- Check subscriber count and growth
- Create and manage email sequences
- Tag subscribers based on behavior
- Send broadcasts

**API:** Kit REST API via custom scripts or MCP wrapper.

### ManyChat
**What it does:** Manage Instagram DM automation — flows, subscribers, tags.

**Use cases:**
- Set up DM automation flows
- Tag and segment subscribers
- Track DM conversions
- Manage custom fields

**API:** ManyChat REST API.

### Stripe
**What it does:** Access payment and revenue data.

**Use cases:**
- Check revenue and MRR
- View recent charges and subscriptions
- Track customer lifetime value
- Monitor payment failures

**API:** Stripe REST API via custom scripts.

### Google Workspace
**What it does:** Access Google Sheets, Docs, Slides, Gmail.

**Use cases:**
- Export data to Google Sheets
- Create presentations in Google Slides
- Read and send emails
- Manage documents

**Server:** Various — `@anthropic/google-drive-mcp`, custom scripts.

### n8n
**What it does:** Build and manage automation workflows.

**Use cases:**
- Create automated posting workflows
- Set up webhook triggers
- Build data pipelines
- Monitor workflow executions

**Server:** `n8n-mcp`

### Apify
**What it does:** Web scraping and data extraction.

**Use cases:**
- Scrape competitor content
- Extract Instagram post data
- Build content corpuses
- Research audience conversations

**Server:** `@anthropic/apify-mcp` or custom scripts.

### Supabase
**What it does:** Database operations — read, write, query.

**Use cases:**
- Store content performance data
- Build analytics dashboards
- Track experiments
- Store competitor research

**API:** Supabase client library.

---

## Getting Started

**Start with 2-3 tools.** Don't try to connect everything at once.

**Recommended first setup:**
1. **Notion** — your business hub (content calendar, projects, CRM)
2. **Cal.com** — scheduling (discovery calls, coaching sessions)
3. **Kit** — email list (welcome sequence, nurture)

**Add later:**
4. Canva (design automation)
5. Stripe (revenue tracking)
6. n8n (workflow automation)

## Environment Variables

Most MCP servers need API keys. Store them in a `.env` file:

```bash
# .env — NEVER commit this file
NOTION_API_KEY=your-key
KIT_API_KEY=your-key
STRIPE_SECRET_KEY=your-key
MANYCHAT_API_KEY=your-key
ELEVENLABS_API_KEY=your-key
```

**Add `.env` to your `.gitignore` immediately:**
```
echo ".env" >> .gitignore
```

---

## What's .gitignore?

A `.gitignore` file tells Git which files to NOT track. You NEVER want to commit:
- `.env` files (API keys, secrets)
- `node_modules/` (installed packages — too large)
- `.DS_Store` (macOS junk files)
- Audio/video files (too large for Git)

Example `.gitignore`:
```
.env
node_modules/
.DS_Store
*.mp3
*.mp4
```

## What's .env?

A `.env` file stores environment variables — API keys, secrets, configuration that changes per machine. It's a simple key=value file that stays on YOUR computer and never gets shared.

---

*From the Claudepreneur Crash Course — claudepreneur.com*
