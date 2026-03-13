---
description: "Edit a Canva carousel template end-to-end — inspect elements, replace text, format hierarchy, optional AI cover image, preview before commit."
---

# Canva Carousel Editor

Edit an existing Canva carousel template with new copy. Inspect first, then modify text, images, formatting, and positioning — all in one transaction.

---

## What You Can Do (Editing Operations)

These are the tools available to modify a Canva design within an editing transaction:

| Operation | Tool | Notes |
|---|---|---|
| **Analyse content** | `start-editing-transaction` | Returns ALL text elements and image fills — always do this first |
| **Replace entire text** | `replace_text` | Swap full text content of an element |
| **Find/replace within text** | `find_and_replace_text` | Change specific words or phrases |
| **Format text** | `format_text` | Color, size, weight, alignment, line height, style, decoration, links, lists |
| **Delete elements** | `delete_element` | Remove images or videos — NEVER delete text boxes (park them instead) |
| **Replace an image/video** | `update_fill` | Swap an existing image in-place (preserves z-order) |
| **Insert a new image/video** | `insert_fill` | Add a new image to a page (goes on top — can't control z-order) |
| **Move elements** | `position_element` | Reposition any element (top/left in px) |
| **Resize elements** | `resize_element` | Change dimensions (text: width only, height auto-calculated) |
| **Update design title** | `update_title` | Change the design's name |

### Importing Assets

- **`upload-asset-from-url`** — Upload any public image URL into Canva as an asset → returns an `asset_id`
- Then use `update_fill` or `insert_fill` to place it in the design
- User can provide an image URL and tell you where to put it (background, specific slide, specific position)

### What You CANNOT Do

- Group/ungroup elements
- Control z-order (send to back/front) — use `update_fill` instead of `insert_fill` to avoid layering issues
- Change font family (size, weight, style — yes; family — no)
- Add new text elements — can only edit/delete existing ones
- Set opacity on existing elements (only on `insert_fill`)
- Delete entire designs from the account — only move to a folder
- Delete assets from Canva's media library

### Known Limitations

**`format_text` with `font_size` DOES NOT WORK reliably.** The API returns "success" but font sizes do not persist after commit. Tested extensively:
- One element at a time, one slide at a time — returns success, doesn't stick
- With `replace_text` preceding `format_text` in the same transaction — returns success, doesn't stick
- Alone in an isolated transaction — returns success, doesn't stick
- Re-applying `format_text` in a new transaction can actually RESET existing formatting to template defaults

**The rule:** Do NOT use `format_text` with `font_size`. Font sizes must be set manually by the user in Canva. After committing, tell the user exactly which font sizes to apply per element role (from design.md).

**What `format_text` CAN do reliably:** `color`, `font_weight`, `text_align`, `line_height`, `font_style` — these appear to work. Only `font_size` is broken.

**What the API cannot READ:**
- `start-editing-transaction` returns text, positions, and dimensions only — it does NOT return font_size, font_weight, color, text_align, or line_height. Formatting cannot be verified through the API after applying it.

---

## Inputs I Need

1. **Canva template URL or design ID** — the carousel to edit
2. **Carousel copy** — pasted directly or output from `/carousel-copy`
3. **Cover image** (optional) — either:
   - A topic/vibe for AI generation (e.g., "dark moody workspace")
   - A public image URL to upload and use directly

If any input is missing, ask for it before starting.

---

## Phase 1 — Inspect Template (DO THIS FIRST)

Never edit blind. Always analyse every element before making changes.

1. If given a URL, use `resolve-shortlink` to get the design ID
2. `start-editing-transaction` on the design — this returns all text elements (`richtexts`) and image fills (`fills`) with their positions, dimensions, and element IDs
3. Print a summary table for the user:

```
| Page | Element ID | Type | Current Text / Asset | Position | Size | Role |
|------|------------|------|---------------------|----------|------|------|
| 1    | abc123     | TEXT | "Your hook here"    | 440,80   | 920w | H1   |
| 1    | def456     | TEXT | "Subtitle text"     | 700,80   | 920w | H2   |
| 1    | ghi789     | IMG  | asset: MAHD0xdbTow  | 0,0      | 1080x1350 | Background |
...
```

4. Identify the **pattern** — most carousel templates repeat the same element structure on every page. Note which elements are consistent (labels, CTAs, backgrounds) vs. which change per slide (headlines, body text).

Do NOT proceed to editing until this table is shown and the user confirms the mapping.

---

## Phase 2 — Plan the Edits

Based on the inspection, decide:

1. **Which text elements get new copy** — map carousel slides to the correct elements per page
2. **Split copy across text boxes** — don't cram everything into one element. Use the template's hierarchy:
   - H1 → punchy headline or key phrase
   - H2 → supporting line or subheading
   - Body → longer explanation or detail
   - If the slide copy is short, use H1 only and leave others empty
3. **Park unused elements** — NEVER delete text boxes. If a text box isn't needed for this slide:
   - Set its text to empty (`replace_text` with `""`)
   - Move it to the bottom-right corner (`position_element` to ~1000, 1300) so it's off-canvas but recoverable
   - This is critical because the same template is reused every time — we can't duplicate designs
4. **Reclaim parked elements** — check bottom-right corner for elements parked from a previous run. Bring them back into the layout if needed for this run.
5. **Format from design.md** — read `./brand-files/design.md` and apply formatting via `format_text`:
   - Apply font_weight, color, line_height, text_align (these work reliably)
   - **Do NOT apply font_size via API** — it doesn't persist. Tell user which sizes to set manually after commit.
   - Always left-align (`text_align: start`) except CTA slide which can center
   - All text white (`#FFFFFF`), labels/footers gray (`#9A9A9A`)
   - Never change font family (MCP can't do this anyway — set it in the Canva template)
6. **Position text as a group** — vertically center the text block within the usable area:
   - Usable area: y:250 to y:1250 (accounting for chrome elements and 80px padding)
   - Calculate total height of H1 + H2 + Body (based on font sizes and line heights)
   - Center that group vertically in the usable area
   - H2 starts ~40px below H1, Body starts ~40px below H2
   - Text width: left 55-60% of the slide (per design.md layout rules)
7. **Cover image plan** — if requested, decide whether to generate, upload from URL, or use an existing asset

Show the user the plan before executing.

---

## Phase 3 — Execute Edits

### 3a. Replace text
Use `replace_text` for each element, mapping carousel copy to the correct elements per slide.

### 3b. Park unused elements (NEVER delete)
For text boxes not needed on this slide:
1. `replace_text` with `""` (empty string)
2. `position_element` to bottom-right corner (~1000, 1300) — off-canvas but recoverable
The same template is reused every run — parked elements get reclaimed next time.

### 3c. Format text (from design.md)

Read `./brand-files/design.md` and apply non-font-size formatting with `format_text`.

**⚠️ DO NOT use `format_text` with `font_size` — it does not work.** The API returns "success" but sizes don't persist. Font sizes must be set manually by the user in Canva.

**What `format_text` CAN apply reliably (batch these freely):**

| Role | font_weight | color | line_height | text_align |
|------|-------------|-------|-------------|------------|
| H1 | bold | #FFFFFF | 1.05 | start |
| H2 | bold | #FFFFFF | 1.2 | start |
| Body | normal | #FFFFFF | 1.35 | start |
| Label/Footer | normal | #9A9A9A | 1.0 | start |

**CTA slide (10):** Same as content but `text_align: center` is allowed.

Note: Canva MCP only supports `bold` or `normal` for font_weight.

**After committing, tell the user to manually set these font sizes in Canva:**

| Role | Content slides | Cover slide |
|------|---------------|-------------|
| H1 | 65px | 90px |
| H2 | 32px | 40px |
| Body | 30px | — |
| Label/Footer | 14-16px | — |

### 3d. Position as a group
Vertically center the text group within the usable area (between header chrome ~y:170 and footer chrome ~y:1220).

**Centering formula (all slide types):**
1. Calculate the rendered height of each active text element (from Canva's response after text replacement)
2. `total_group_height = sum of all active textbox heights + (53 × number_of_gaps)`
3. `start_y = 170 + (1050 - total_group_height) / 2`
4. Place elements top-down from `start_y`, with 53px gaps between each

**Content slides (2–9):**
- H1 at x:80, width 600px
- Body at x:80, width 813px
- 53px gap between H1 bottom and Body top

**Cover slide (1):**
- H1 at x:80, width 920px (full width)
- H2 at x:80, width 920px (full width)
- 43px gap between H1 bottom and H2 top

**CTA slide (10):**
- H1 at x:212 (centered on slide), width 600px
- Body at x:240 (centered on slide), width 600px
- No separate CTA keyword element — merge CTA text into body
- 53px gap between elements

### 3e. Batch operations
Combine as many operations as possible into minimal `perform-editing-operations` calls. Don't make one API call per element — batch them across pages.

---

## Phase 4 — Cover Image (Optional)

Only run this if the user wants a cover image.

### Option A: AI-generated image

1. `generate-design` with format `instagram_post`
   - Always add "no text, no words, no typography" to the prompt
   - Show candidates → user picks
2. `create-design-from-candidate` → get design_id
3. `start-editing-transaction` on generated design → grab the `asset_id` from the fill → `cancel-editing-transaction`
4. `update_fill` on the carousel's existing cover image element with the new asset_id (replaces in-place, no z-order issues)
5. `format_text` all slide 1 text to white (`#FFFFFF`) or appropriate contrast color
6. **Clean up:** `search-designs` to find ALL generated candidates (they all get saved to the account) → move ALL to "AI Generated - Cleanup" folder → tell user to trash them manually

### Option B: Image from URL

1. `upload-asset-from-url` with the user's image URL → get `asset_id`
2. `update_fill` on the existing cover image element, or `insert_fill` to place it where the user wants
3. Adjust text color for readability if needed

---

## Phase 5 — Preview + Commit + Snapshot

1. Summarize all changes made (text replacements, parking, formatting, cover image swaps)
2. `commit-editing-transaction` immediately — don't ask for approval (changes aren't visible until committed anyway)
3. Tell the user to review in Canva — if anything needs adjusting, start a new transaction
4. After commit:
   - If `update_fill` was used for cover: no manual steps needed
   - If `insert_fill` was used: remind user to right-click → "Send to back" in Canva (MCP can't control z-order)
   - If AI images were generated: remind user to trash designs in "AI Generated - Cleanup" folder

### 5a. Save Snapshot (for `/learn-design`)

After committing, save a snapshot of every text element Claude placed. This is the "before" state that `/learn-design` will diff against Kevin's manual adjustments.

Write to `brand-files/snapshots/latest.json`:

```json
{
  "design_id": "<the design ID>",
  "timestamp": "<ISO 8601 UTC>",
  "elements": [
    {
      "page": 2,
      "element_id": "PB6lzd041Qw...",
      "role": "H1",
      "text": "The Real Problem",
      "top": 298,
      "left": 108,
      "width": 906,
      "height": 57
    }
  ]
}
```

**Rules for the snapshot:**
- Include ALL text elements that Claude placed (not parked elements)
- Record position (`top`, `left`), dimensions (`width`, `height`), text content, and role
- Do NOT record formatting (font_size, font_weight, color, text_align, line_height) — the API cannot verify these values, so recording them creates false confidence
- `role` should match the hierarchy assigned during Phase 2 (H1, H2, Body, Label, Footer, CTA)
- Parked elements (position ~1000, ~1300) should be excluded
- Tell the user: "Snapshot saved. After you adjust in Canva, run `/learn-design` to teach me your preferences. Tell me about any font size or formatting changes — I can't detect those through the API."

---

## Rules

- **ALWAYS inspect before editing** — never assume element IDs or structure
- **ALWAYS show the element map** before making changes
- **Summarize changes then commit immediately** — don't ask for approval (changes aren't visible in Canva until committed anyway)
- **NEVER delete text boxes** — park unused ones in the bottom-right corner (empty text, position ~1000,1300). The template is reused every time.
- **Reclaim parked elements** — on every run, check bottom-right for elements from previous runs and bring them back if needed
- **Split copy across text boxes** — use multiple elements per slide (H1 for headlines, H2/Body for supporting text). Don't cram everything into one box.
- **Always left-align text** — `text_align: start` on everything (except CTA slide)
- **Format from design.md** — apply color, weight, line_height, text_align via API. Font sizes must be set manually by user — tell them which sizes to apply after commit.
- **Vertically center text groups** — calculate combined height and center within usable area (y:250-1250), 40px gaps between elements
- **Batch API calls** — don't make one call per element
- **Keep the transaction open** across all phases — only commit at the end
- **Always save a snapshot** after committing — write to `brand-files/snapshots/latest.json` so `/learn-design` can diff Kevin's adjustments
