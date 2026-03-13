#!/usr/bin/env python3
"""Generate a nicely formatted PDF from cheat-sheet.md"""

from fpdf import FPDF

# Brand color
PURPLE = (108, 60, 233)
DARK = (26, 26, 26)
GRAY = (100, 100, 100)
LIGHT_BG = (248, 246, 255)
WHITE = (255, 255, 255)
TABLE_BORDER = (220, 220, 220)


def clean(text):
    """Replace unicode chars that core fonts can't handle."""
    return (text
        .replace("\u2014", "--")
        .replace("\u2013", "-")
        .replace("\u2018", "'").replace("\u2019", "'")
        .replace("\u201c", '"').replace("\u201d", '"')
        .replace("\u2026", "...")
        .replace("\u2192", "->")
    )


class CheatSheetPDF(FPDF):
    def header(self):
        pass

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*GRAY)
        self.cell(0, 10, f"{self.page_no()}", align="C")

    def section_title(self, title):
        self.set_font("Helvetica", "B", 15)
        self.set_text_color(*PURPLE)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        # Underline
        self.set_draw_color(*TABLE_BORDER)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(4)

    def table(self, headers, rows):
        col_count = len(headers)
        avail_w = self.w - self.l_margin - self.r_margin

        # Calculate column widths based on content
        if col_count == 2:
            col_widths = [avail_w * 0.30, avail_w * 0.70]
        elif col_count == 3:
            col_widths = [avail_w * 0.22, avail_w * 0.38, avail_w * 0.40]
        else:
            col_widths = [avail_w / col_count] * col_count

        # Header row
        self.set_font("Helvetica", "B", 9)
        self.set_fill_color(*PURPLE)
        self.set_text_color(*WHITE)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 7, f"  {clean(h)}", fill=True, border=0)
        self.ln()

        # Data rows
        self.set_font("Helvetica", "", 9.5)
        for row_idx, row in enumerate(rows):
            bg = LIGHT_BG if row_idx % 2 == 0 else WHITE
            self.set_fill_color(*bg)
            self.set_text_color(*DARK)

            # Calculate row height based on content
            max_lines = 1
            cell_texts = []
            for i, cell in enumerate(row):
                text = clean(cell.replace("**", ""))
                cell_texts.append(text)
                lines = self.multi_cell(col_widths[i], 5.5, text, dry_run=True, output="LINES")
                max_lines = max(max_lines, len(lines))

            row_h = max_lines * 5.5 + 1

            # Check if we need a new page
            if self.get_y() + row_h > self.h - 20:
                self.add_page()
                # Reprint header
                self.set_font("Helvetica", "B", 9)
                self.set_fill_color(*PURPLE)
                self.set_text_color(*WHITE)
                for i, h in enumerate(headers):
                    self.cell(col_widths[i], 7, f"  {clean(h)}", fill=True, border=0)
                self.ln()
                self.set_font("Helvetica", "", 9.5)
                self.set_fill_color(*bg)
                self.set_text_color(*DARK)

            x_start = self.get_x()
            y_start = self.get_y()

            # Draw background
            self.rect(x_start, y_start, avail_w, row_h, "F")

            # Draw bottom border
            self.set_draw_color(*TABLE_BORDER)
            self.line(x_start, y_start + row_h, x_start + avail_w, y_start + row_h)

            # Print cells
            for i, text in enumerate(cell_texts):
                x_pos = x_start + sum(col_widths[:i])
                self.set_xy(x_pos + 2, y_start + 0.5)

                # Bold the first column
                if i == 0:
                    self.set_font("Helvetica", "B", 9.5)
                else:
                    self.set_font("Helvetica", "", 9.5)
                self.set_text_color(*DARK)

                self.multi_cell(col_widths[i] - 4, 5.5, text, border=0)

            self.set_xy(x_start, y_start + row_h)

        self.ln(4)

    def code_block(self, text):
        self.set_font("Courier", "", 9)
        self.set_fill_color(30, 30, 46)
        self.set_text_color(205, 214, 244)

        text = clean(text)
        lines = text.strip().split("\n")
        line_h = 5
        block_h = len(lines) * line_h + 8

        if self.get_y() + block_h > self.h - 20:
            self.add_page()

        x = self.get_x()
        y = self.get_y()

        # Draw background with rounded effect
        self.rect(x, y, self.w - self.l_margin - self.r_margin, block_h, "F")

        self.set_xy(x + 6, y + 4)
        for line in lines:
            self.cell(0, line_h, line, new_x="LMARGIN", new_y="NEXT")
            self.set_x(x + 6)

        self.set_xy(self.l_margin, y + block_h + 3)
        self.set_text_color(*DARK)

    def body_text(self, text, bold=False):
        self.set_font("Helvetica", "B" if bold else "", 10)
        self.set_text_color(*DARK)
        self.cell(0, 6, clean(text), new_x="LMARGIN", new_y="NEXT")

    def bullet(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(*DARK)
        self.cell(6, 5.5, "-")
        t = clean(text.replace("`", ""))
        self.cell(0, 5.5, t, new_x="LMARGIN", new_y="NEXT")


def build_pdf():
    pdf = CheatSheetPDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    # Title
    pdf.set_font("Helvetica", "B", 28)
    pdf.set_text_color(*DARK)
    pdf.cell(0, 12, "Claude Code Cheat Sheet", new_x="LMARGIN", new_y="NEXT")

    # Subtitle
    pdf.set_font("Helvetica", "I", 11)
    pdf.set_text_color(*GRAY)
    pdf.set_draw_color(*PURPLE)
    x = pdf.get_x()
    y = pdf.get_y()
    pdf.line(x, y, x, y + 7)
    pdf.set_x(x + 5)
    pdf.cell(0, 7, "Your quick reference for Claude Code commands, shortcuts, and concepts.", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

    # Divider
    pdf.set_draw_color(*TABLE_BORDER)
    pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
    pdf.ln(5)

    # Core Concepts
    pdf.section_title("Core Concepts")
    pdf.table(
        ["Concept", "What It Is"],
        [
            ["CLAUDE.md", "A file Claude reads before every conversation. Your business context."],
            ["Brand Files", "Separate files for voice (brand.md), offer (offer.md), audience (icp.md). More detail = better output."],
            ["Skills", "Text files with instructions that Claude follows. Reusable commands (e.g., /carousel-copy)."],
            ["Agents", "Specialist team members Claude delegates to. Live in .claude/agents/. Have access to tools."],
            ["MCP", "Model Context Protocol — connects Claude to external tools (Canva, Notion, Calendar, etc)."],
        ],
    )

    # Modes
    pdf.section_title("Modes")
    pdf.table(
        ["Mode", "What It Does", "How to Use"],
        [
            ["Normal mode", "Claude reads + writes files, runs commands", "Default mode"],
            ["Plan mode", "Claude plans without changing anything — safe for exploring", 'Type "plan" or use the mode selector'],
            ["Edit mode", "Claude focuses on editing specific files", "Shift+Tab to toggle"],
        ],
    )

    # Essential Shortcuts
    pdf.section_title("Essential Shortcuts")
    pdf.table(
        ["Shortcut", "What It Does"],
        [
            ["Escape", "Cancel / go back / dismiss"],
            ["Ctrl+C", "Stop what Claude is doing"],
            ["/command", "Run a skill (slash command)"],
            ["Shift+Tab", "Toggle compact mode"],
            ["Up arrow", "Recall previous message"],
        ],
    )

    # Key File Locations
    pdf.section_title("Key File Locations")
    pdf.table(
        ["File", "Location", "Purpose"],
        [
            ["Project CLAUDE.md", "./CLAUDE.md", "Context for this project"],
            ["Global CLAUDE.md", "~/.claude/CLAUDE.md", "Context for ALL projects"],
            ["Skills", "~/.claude/skills/", "Your custom skills (global)"],
            ["Project skills", ".claude/skills/", "Skills for this project only"],
            ["Agents", ".claude/agents/", "Your agent files"],
            ["Brand files", "./brand-files/", "voice, offer, audience context"],
        ],
    )

    # The 5 Building Blocks
    pdf.section_title("The 5 Building Blocks")
    pdf.code_block(
        "  1. CLAUDE.md    = Brain      (who you are, what you do)\n"
        "  2. Brand Files  = Context    (voice, offer, audience — deep detail)\n"
        "  3. Skills       = Hands      (reusable commands, one task each)\n"
        "  4. Agents       = Team       (orchestrate multiple tasks)\n"
        "  5. MCP          = Phone Lines (connect to real tools)"
    )

    # Skill Anatomy
    pdf.section_title("Skill Anatomy (3 Parts)")
    pdf.code_block(
        '---\n'
        'description: "What this skill does — shows up in the / menu"\n'
        '---\n'
        '\n'
        '# Instructions\n'
        '\n'
        'Tell Claude what to do in plain English.\n'
        'Step by step. Be specific.\n'
        'Reference brand files for personalization.\n'
        '\n'
        '## Rules\n'
        '\n'
        '- Guardrails and standards\n'
        '- Tone and formatting constraints\n'
        '- What NOT to do'
    )

    # Agent Anatomy
    pdf.section_title("Agent Anatomy")
    pdf.code_block(
        '---\n'
        'name: agent-name\n'
        'description: "What this agent does"\n'
        'tools: Read, Write, Glob, Grep, Bash\n'
        '---\n'
        '\n'
        '# Instructions\n'
        '\n'
        'What this agent does and how.\n'
        'Reads brand files for context.\n'
        'Produces a complete deliverable.\n'
        '\n'
        '## Rules\n'
        '\n'
        '- Standards and constraints'
    )

    # The Carousel Pipeline
    pdf.section_title("The Carousel Pipeline You Built")
    pdf.code_block(
        "  Topic\n"
        "    → carousel-copy skill (10 slides)\n"
        "    → caption-writer skill (Instagram caption)\n"
        "    → carousel-writer agent (both at once)\n"
        "    → Canva MCP (real designed images)"
    )

    # Quick Prompts
    pdf.section_title("Quick Prompts That Work With Brand Files")

    pdf.ln(1)
    pdf.body_text("Content:", bold=True)
    pdf.bullet('"Give me 5 carousel topics for this week"')
    pdf.bullet('"Write an Instagram caption about [topic]"')
    pdf.bullet('"Draft a LinkedIn post about [lesson]"')
    pdf.ln(2)

    pdf.body_text("Client Work:", bold=True)
    pdf.bullet('"Write a welcome message for [client name]"')
    pdf.bullet('"Create a session prep sheet for tomorrow\'s call"')
    pdf.bullet('"Draft a follow-up for [prospect]"')
    pdf.ln(2)

    pdf.body_text("Strategy:", bold=True)
    pdf.bullet('"What content gaps exist in my niche?"')
    pdf.bullet('"Write 3 positioning statements for my business"')
    pdf.bullet('"Help me plan my content for next week"')

    pdf.ln(6)
    pdf.set_draw_color(*TABLE_BORDER)
    pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
    pdf.ln(3)

    # Footer text
    pdf.set_font("Helvetica", "I", 9)
    pdf.set_text_color(*GRAY)
    pdf.cell(0, 6, "From the Claudepreneur Starter Course -- claudepreneur.com", align="C")

    import os
    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "output")
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, "claude-code-cheat-sheet.pdf")
    pdf.output(out_path)
    print(f"PDF created: {out_path}")


if __name__ == "__main__":
    build_pdf()
