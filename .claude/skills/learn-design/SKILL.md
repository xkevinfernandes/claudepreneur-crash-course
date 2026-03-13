---
description: "Learn design preferences by diffing what Claude set vs what Kevin adjusted in Canva, then update design.md with the real rules."
---

# Learn Design

Compare what Claude applied to a carousel against what Kevin manually adjusted in Canva. Diff the before/after, show the changes, and update `brand-files/design.md` with approved corrections.

---

## Inputs

- **Design ID** (optional) — defaults to the `design_id` in the latest snapshot

If a design ID is provided as an argument, use it. Otherwise pull it from the snapshot.

---

## Phase 1 — Load Snapshot (the "before")

1. Read `brand-files/snapshots/latest.json`
2. If the file doesn't exist, stop and tell the user:
   > "No snapshot found. Run `/canva-carousel` first — it saves a snapshot of what Claude set so I can diff against your adjustments."
3. Parse the JSON. Store every element keyed by `element_id` for fast lookup.
4. If a design ID was passed as input, use that. Otherwise use `design_id` from the snapshot.

---

## Phase 2 — Inspect Current State (the "after")

1. `start-editing-transaction` on the design ID
2. Map every text element (`richtexts`) by its element ID. For each element capture:
   - `element_id`, `page` (page index), `text` content
   - `top`, `left` (position)
   - `width`, `height` (dimensions)
3. `cancel-editing-transaction` immediately — this is read-only, we don't want to edit anything

> **API limitation:** `start-editing-transaction` does NOT return formatting properties (font_size, font_weight, color, text_align, line_height). Only text content, positions, and dimensions are observable through the API.

---

## Phase 3 — Diff

For each element in the snapshot, find the matching `element_id` in the current state.

Compare these properties (only what the API can actually read):
- **Position:** `top`, `left`
- **Size:** `width`, `height`

> **Cannot diff formatting.** The API does not return font_size, font_weight, color, text_align, or line_height. If Kevin made formatting changes, ask him to report them verbally so they can be recorded in design.md.

Rules:
- Ignore elements that haven't changed at all
- Ignore elements that were parked (position ~1000, ~1300) in both states
- Ignore elements not found in current state (may have been deleted manually)
- Small rounding differences (±1px) should be ignored
- Group changes by **role** (H1, H2, Body, Label/Footer) and **type** (position, size)

---

## Phase 4 — Show Diff + Ask

Print a clear diff table:

```
| Element (Role) | Page | Property | Before (Claude) | After (You) | Delta |
|----------------|------|----------|-----------------|-------------|-------|
| H1             | 2    | top       | 450px          | 350px       | -100  |
| H2             | 3    | width     | 600px          | 750px       | +150  |
| Body           | 4    | left      | 80px           | 100px       | +20   |
```

> **Formatting changes** (font size, weight, color, alignment, line height) cannot be detected through the API. After showing the position/size diff, always ask: **"Did you also change any font sizes, weights, colors, or alignment? Tell me and I'll update design.md."**

If no differences found, tell the user:
> "No changes detected — either nothing was adjusted or the snapshot is stale."

If differences found, ask:
> "Which of these should I save as permanent design rules? Options: **all**, **none**, or list specific rows (e.g., 1, 3, 4)"

Wait for the user's answer before proceeding.

---

## Phase 5 — Update design.md

For each approved change:

1. Read `brand-files/design.md`
2. Map the change to the correct section:
   - `top`, `left` → **Layout section** (update position references)
   - `width`, `height` → **Layout section** (update dimension references)
   - For any formatting changes Kevin reports verbally (font_size, font_weight, color, text_align, line_height) → **Typography table** or **Core Design section** as appropriate
3. Edit the file with the new values
4. If multiple elements of the same role were changed the same way (e.g., H1 on pages 2-9 all moved up), treat it as a single rule change — don't add per-page rules
5. If a change only happened on one page and doesn't generalize, note it in the update but flag it to the user

After updating, print a summary:

```
Updated design.md:
- H1 content font_size: 65px → 72px
- H1 content top position: ~450px → ~350px
- Body line_height: 1.35 → 1.25
```

---

## Phase 6 — Cleanup

1. Delete `brand-files/snapshots/latest.json` (it's been consumed)
2. Tell the user the snapshot has been cleared and they're ready for the next `/canva-carousel` run

---

## Rules

- **Read-only Canva access** — always cancel the editing transaction, never commit
- **Never auto-approve changes** — always show the diff and wait for the user to pick
- **Generalize where possible** — if H1 moved on 7 out of 8 content slides, call it a general H1 rule, not 7 separate rules
- **Don't overwrite unrelated sections** — only edit the specific values that changed
- **Round consistently** — positions to nearest whole pixel, line heights to 2 decimal places
