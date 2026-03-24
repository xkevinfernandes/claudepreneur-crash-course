---
description: "Create or edit Canva carousels — duplicate a template, replace all text, commit. Use when the user says 'fill the carousel', 'put this in Canva', 'create a carousel', 'fill the template', or after any content writing skill produces carousel copy."
---

# Canva Carousel

Duplicate a template, replace all text with carousel content, commit.

---

## Inputs

1. **Content** — carousel copy (slide-by-slide text), pasted or from a previous skill run
2. **Template design ID** — the Canva design to duplicate. Ask the user for the URL if not known. Extract the 11-character ID after `/design/` in the URL.
3. **Output folder** — where to move the finished carousel. Ask the user for the folder name if not known. Use `search-folders` to resolve the ID.
4. **Design ID override** (optional) — if provided, skip duplication and edit this design directly

If content is missing, ask before starting.

---

## Phase 1 — Duplicate Template

**Never edit the base template directly.** Each carousel gets its own copy.

Skip duplication only if the user provides a design ID to edit.

1. Navigate to `https://www.canva.com/design/{template_id}/edit` via Playwright
2. Wait for the editor to load
3. Click **File → Make a copy**
4. Extract the new design ID from the URL (new tab opens)
5. Rename via `start-editing-transaction` + `update_title` + `commit-editing-transaction`
   - Format: `"YYYYMMDD — {carousel title}"`
6. Move to output folder via `move-item-to-folder`

Use the **new design_id** for Phase 2.

---

## Phase 2 — Replace Text

1. `start-editing-transaction` on the new copy — this returns ALL text elements and their IDs
2. Identify each element's role from its position and content:
   - **Handle:** top ≈ 1242, small width — SKIP (never edit)
   - **Page number:** top ≈ 323, empty or single number — SKIP (never edit)
   - **H1:** first substantial text element on the page
   - **H2:** second text element on the cover page (page 1)
   - **Body:** text element after H1 with wider width
   - **CTA elements (last page):** h1_qualifier (top text), cta (bold middle), h1_action (bottom text)
3. Map content to elements:

| Content | Page | Elements |
|---------|------|----------|
| Hook / headline | Page 1 (cover) | H1 + H2 |
| Body slides | Pages 2–9 | H1 + Body |
| Call to action | Last page | h1_qualifier + cta + h1_action |

4. `replace_text` for each editable element — batch all into minimal `perform-editing-operations` calls
5. **Park unused elements** off-canvas: set text to `""` and position to ~1000, 1300. NEVER delete text boxes.

Split copy across text boxes:
- **H1** → punchy headline or key phrase
- **H2** → supporting line (cover only)
- **Body** → longer explanation or detail

If fewer content slides than template pages, park the extras off-canvas.

Keep the transaction open for Phase 3.

---

## Phase 3 — Commit

1. Summarize all changes
2. `commit-editing-transaction` immediately — don't ask for approval (changes aren't visible until committed)
3. Tell user to review in Canva — thumbnails don't render in terminal

---

## Rules

- **NEVER edit the base template** — always duplicate first
- **Commit immediately** — don't ask for approval
- **NEVER delete text boxes** — park unused ones off-canvas (~1000, 1300)
- **Batch API calls** — minimize `perform-editing-operations` calls
- **`replace_text` preserves formatting** — the template's fonts, colors, and sizes carry over automatically
- **Skip handle and page_number elements** — these are fixed chrome, never edit them
