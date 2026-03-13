#!/bin/bash
# Claudepreneur Starter Course — Installer
# Copies course to ~/.claude/skills/cos-course/

set -e

echo ""
echo "═══════════════════════════════════════════════════"
echo ""
echo "  CLAUDEPRENEUR STARTER COURSE — INSTALLER"
echo ""
echo "═══════════════════════════════════════════════════"
echo ""

# Get the directory where this script lives
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_SRC="$SCRIPT_DIR/.claude/skills"
SKILL_DEST="$HOME/.claude/skills"

# Check source files exist
if [ ! -d "$SKILL_SRC" ]; then
  echo "Error: Course files not found at $SKILL_SRC"
  echo "Make sure you're running this from the course directory."
  exit 1
fi

# Create destination directories
for dir in start lesson-1 lesson-2 lesson-3 lesson-4 lesson-5 lesson-6 canva-carousel learn-design; do
  mkdir -p "$SKILL_DEST/$dir"
done

# Copy skill files
SKILL_COUNT=0
for dir in start lesson-1 lesson-2 lesson-3 lesson-4 lesson-5 lesson-6 canva-carousel learn-design; do
  if [ -f "$SKILL_SRC/$dir/SKILL.md" ]; then
    cp "$SKILL_SRC/$dir/SKILL.md" "$SKILL_DEST/$dir/SKILL.md"
    SKILL_COUNT=$((SKILL_COUNT + 1))
  fi
done

echo "  Skills installed: $SKILL_COUNT files"
echo "  Location: $SKILL_DEST"
echo ""
echo "  Course:"
echo "    /cos-course:start        — Welcome + Claude Code Orientation"
echo "    /cos-course:lesson-1     — Your AI's Brain (CLAUDE.md)"
echo "    /cos-course:lesson-2     — Carousel Copy Writer (First Skill)"
echo "    /cos-course:lesson-3     — The Architecture Upgrade (Brand Files)"
echo "    /cos-course:lesson-4     — Build Skills From Examples (Caption Writer)"
echo "    /cos-course:lesson-5     — The Carousel Agent (Your AI Team)"
echo "    /cos-course:lesson-6     — Your Complete System + Finale"
echo ""
echo "  Tools (available from the start):"
echo "    /cos-course:canva-carousel — Design carousels in Canva"
echo "    /cos-course:learn-design   — Teach Claude your design preferences"
echo ""
echo "  You'll build during the course:"
echo "    .claude/skills/           — Your custom skills"
echo "    .claude/agents/           — Your custom agents"
echo ""

# Create user data directory
USER_DATA="$HOME/.claudepreneur/crash-course"
mkdir -p "$USER_DATA/gifts"
mkdir -p "$USER_DATA/reports"
mkdir -p "$USER_DATA/builds"

# Initialize progress if not exists
if [ ! -f "$USER_DATA/progress.json" ]; then
  echo '{"currentLesson": 0, "currentStep": 0, "completedLessons": [], "completedSteps": {}}' > "$USER_DATA/progress.json"
  echo "  Progress tracker initialized."
fi

echo ""
echo "  ┌─────────────────────────────────────────────────┐"
echo "  │                                                 │"
echo "  │  INSTALLED!                                     │"
echo "  │                                                 │"
echo "  │  6 lessons + 2 Canva tools ready.               │"
echo "  │                                                 │"
echo "  │  NEXT STEP — Connect Canva:                     │"
echo "  │  In Claude Code, go to Settings > Integrations  │"
echo "  │  and connect your Canva account.                │"
echo "  │                                                 │"
echo "  │  Then start the course:                         │"
echo "  │  Open Claude Code and type:                     │"
echo "  │  /cos-course:start                              │"
echo "  │                                                 │"
echo "  └─────────────────────────────────────────────────┘"
echo ""
