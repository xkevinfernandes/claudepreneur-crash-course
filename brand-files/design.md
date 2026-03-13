# Design System

> Visual rules for all carousel and social designs. Read by Canva-facing skills.

## Core Design

- Background: `#121212` (solid dark, never varies)
- Grid overlay: `#2A2A2A` thin 1px lines, 3-col × 4-row
- Font: Inter only (all weights)
- Alignment: Left-aligned everything. Never centered (except CTA slide).

## Typography

| Element | Weight | Size (content) | Size (cover) | Color |
|---------|--------|---------------|-------------|-------|
| H1 | 900 (Black) | 65px | 90px | #FFFFFF |
| H2 | 600 (Semi) | 32px | 40px | #FFFFFF |
| Body | 400 (Regular) | 30px | — | #FFFFFF |
| Label/Footer | 500 (Medium) | 14-16px | — | #9A9A9A |

> **Note:** Template defaults differ from these values (H1: 48.8px, Body: 22.5px, Labels: 22px). The Canva MCP `format_text` with `font_size` does NOT work reliably — it returns "success" but sizes don't persist. **Font sizes must be set manually in Canva after Claude commits.** Claude will tell you which sizes to apply.

- Line heights: H1 `1.05`, H2 `1.2`, Body `1.35`
- Padding: 80px all sides

## Colors

| Color | Hex | Usage |
|-------|---------|----------------------|
| White | #FFFFFF | ALL text |
| Dark BG | #121212 | Background |
| Grid | #2A2A2A | Grid overlay lines |
| Gray | #9A9A9A | Labels, footer, chrome |
| Lime | #C8FF00 | Barcode, QR code only |

No colored text. No highlights. Emphasis = size + weight only.

## Chrome (every slide)

These elements appear on every slide in the same position:

- **Barcode**: top-left (x:60, y:50), lime, 60×100px
- **QR code**: top-right (x:900, y:30), lime, 90×90px
- **Header**: AM 005 + dot + ADV, top-center, gray 14px
- **Tagline**: right side (x:600, y:130), gray italic 16px
- **Footer**: bottom (y:1290), gray uppercase 14px
- **Watermark**: @advancingman, left, gray 16px

## Layout

### Cover slide (page 1)
- Vertically center H1 + H2 group in usable area (same formula as content slides)
- H1 at x:80, width 920px, height ~296px (rendered)
- H2 at ~43px gap below H1 bottom edge, x:80, width 920px, height ~144px (rendered)

### Content slides (pages 2–9)
- Vertically center the text group within the usable area (between header chrome ~y:170 and footer chrome ~y:1220)
- Calculate total group height = sum of all active textbox rendered heights + 53px gaps between them
- `start_y = 170 + (1050 - total_group_height) / 2`
- Stack elements top-down with 53px gaps
- H1 at x:80, width 600px (rendered height varies: ~78px for 1-line, ~146px for 2-line)
- Body at x:80, width 813px (rendered height varies by text length)
- Text dimensions come from Canva's `start-editing-transaction` response → each element's `dimension.height`
- Text occupies left ~75% of slide, person cutout photos on right

### CTA slide (page 10)
- Vertically center H1 + Body group in usable area (same formula)
- H1 at x:212 (centered on slide), width 600px, height ~146px (rendered)
- Body at x:240 (centered on slide), width 600px, height ~102px (rendered)
- No separate CTA keyword element — merge CTA text into body
- Person photos: shifted right to make room for centered text

### General
- Person photos: men in casual clothing, transparent cutout, waist up

## What's NOT Allowed

- Centered text (except CTA)
- Colored text or highlights
- Background images/textures (only the grid)
- Gradients
- Rounded cards/containers
- Multiple font families
- Text over person photos
- Emojis
