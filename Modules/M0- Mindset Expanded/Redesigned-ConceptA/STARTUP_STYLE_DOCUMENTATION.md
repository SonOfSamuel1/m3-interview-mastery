# STARTUP PRESENTATION STYLE DOCUMENTATION

## Overview

The Startup Presentation style generator creates a professional, modern 2025 startup pitch deck aesthetic for the M0 Mindset Module slides. This style emphasizes sophistication, clean design, and the visual language of successful tech startups.

## Files

- **`generate_startup_slides.py`** - Main slide generator (creates all 57 slides)
- **`compile_startup_to_pdf.py`** - PDF compiler
- **Output slides:** `slide-01-startup.png` through `slide-57-startup.png`
- **Output PDF:** `M0-Mindset-Module-STARTUP-STYLE.pdf`

## Quick Start

```bash
# Generate all 57 slides
python3 generate_startup_slides.py

# Compile to PDF
python3 compile_startup_to_pdf.py
```

## Design Philosophy

### Core Aesthetic
- **Professional 2025 startup pitch deck look**
- **Dual-theme approach**: Alternates between light and dark backgrounds
- **Sophisticated and modern**: Clean, minimalist, with premium feel
- **Rounded components**: All cards use 24-32px border radius
- **Soft depth**: Gradient overlays create ambient lighting effects
- **Visual hierarchy**: Numbered circular badges guide the eye

### Design Inspiration
Think: Stripe, Linear, Notion, Vercel presentation decks - clean, modern, professional, with subtle sophistication.

## Color Palette

### Primary Colors
| Color | Hex | RGB | Usage |
|-------|-----|-----|-------|
| Light Blue Accent | `#A7D4F0` | `(167, 212, 240)` | Primary accent, badges, bullets |
| Dark Charcoal | `#3D3D3D` | `(61, 61, 61)` | Primary dark text |
| Medium Gray | `#5A5A5A` | `(90, 90, 90)` | Secondary text, headings on light |
| Light Gray Primary | `#D8DDE2` | `(216, 221, 226)` | Main light background |
| Light Gray Secondary | `#E8EAED` | `(232, 234, 237)` | Cards, alternate background |
| Dark Gray Primary | `#4A4A4A` | `(74, 74, 74)` | Dark theme backgrounds |
| Dark Gray Secondary | `#525456` | `(82, 84, 86)` | Dark theme variation |
| Pure White | `#FFFFFF` | `(255, 255, 255)` | Text on dark, clean cards |
| Subtle Text | `#6B6B6B` | `(107, 107, 107)` | Body copy |

### Color Usage Guidelines

**Light Theme Slides:**
- Background: `#D8DDE2` (Light Gray Primary)
- Cards: `#FFFFFF` (Pure White) with 2px border `#D8DDE2`
- Text: `#3D3D3D` (Dark Charcoal)
- Body text: `#6B6B6B` (Subtle Text)
- Bullets: `#A7D4F0` (Light Blue Accent)
- Badges: `#A7D4F0` background with `#3D3D3D` text

**Dark Theme Slides:**
- Background: `#4A4A4A` (Dark Gray Primary)
- Text: `#FFFFFF` (Pure White)
- Secondary text: `#E8EAED` (Light Gray Secondary)
- Gradients: Soft blue-gray `(130, 160, 180)` at 20% opacity

## Typography

### Font Stack
1. **SF Pro Display** (macOS system font)
2. **Helvetica Neue** (fallback)
3. **Helvetica** (final fallback)

### Font Sizes and Weights

| Element | Size | Weight | Usage |
|---------|------|--------|-------|
| Display/Hero | 120-140px | Bold (700-800) | Lesson title slides |
| H1 Titles | 72-84px | Bold (700) | Main titles |
| H2 Sections | 48-56px | Bold (700) | Slide titles |
| H3 Cards | 24-28px | Bold (700) | Card titles |
| Body Large | 18-20px | Regular (400) | Main content |
| Body Regular | 14-16px | Regular (400) | Secondary content |
| Badge Text | 16-18px | Bold (700) | Badge numbers |

### Typography Guidelines
- **Letter spacing**: Tight for display text (-2 to -3px), normal for body
- **Line height**: 1.4-1.6 for body text, tighter for headings
- **Alignment**: Left-aligned for content (not centered bullets)
- **Text color contrast**: Always ensure WCAG AA compliance

## Layout System

### Slide Dimensions
- **Resolution**: 1920x1080px (16:9 aspect ratio)
- **Safe zone**: 80px margins from all edges
- **Content area**: 1760x920px (available space within safe zone)

### Spacing Scale (8px base)
- **24px**: Tight spacing between related elements
- **32px**: Standard spacing between sections
- **48px**: Generous spacing for visual breathing room
- **64px**: Large spacing between major sections
- **80px**: Safe zone margin from edges

### Card Components
- **Border radius**: 28px (24-32px range)
- **Internal padding**: 36px (32-40px range)
- **Border**: 2px solid, color depends on theme
- **Shadow**: Subtle on light theme, more pronounced on dark

### Grid Layouts
- **2-column**: For comparison slides (old vs new beliefs)
- **3-column**: For framework slides (3 pillars/concepts)
- **Single column**: For content slides with bullets

## Gradient Overlays

### Purpose
Create depth and ambient lighting effects without overwhelming content.

### Specifications
- **Type**: Radial gradients
- **Diameter**: 1200px (large, soft circles)
- **Opacity**: 20-30% (0.2-0.3)
- **Blur**: 140-150px (heavy blur for softness)
- **Positions**:
  - `top-right`: Upper right corner
  - `top-left`: Upper left corner
  - `bottom-right`: Lower right corner
  - `bottom-left`: Lower left corner

### Light Theme Gradients
- **Color**: Light Blue Accent `(167, 212, 240)`
- **Opacity**: 25-30%
- **Position**: Varies by slide type

### Dark Theme Gradients
- **Color**: Soft blue-gray `(130, 160, 180)`
- **Opacity**: 20-25%
- **Position**: Typically top-right or bottom-right

## Slide Types

### 1. Dark Title Slide (Lesson Separators)
**Theme**: Dark background
**Purpose**: Introduce new lessons (Lessons 1-5)

**Design Elements:**
- Dark gray background (`#4A4A4A`)
- Large hero text (120-140px, bold)
- Centered alignment
- Soft gradient overlay (20% opacity)
- Pure white text (`#FFFFFF`)
- Optional subtitle in light gray

**When to use**: Start of each of the 5 major lessons

### 2. Light Bullet Slide (Content)
**Theme**: Light background
**Purpose**: Present bulleted lists of information

**Design Elements:**
- Light gray background (`#D8DDE2`)
- Numbered badge in top-left (52px diameter)
- Title in H2 size (48-56px bold)
- Single white card with rounded corners
- Bullets with light blue dots (`#A7D4F0`)
- Left-aligned bullet text
- Gradient overlay (25-30% opacity)

**When to use**: Most content slides with 3-5 bullet points

### 3. Light Quote/Emphasis Slide
**Theme**: Light background
**Purpose**: Emphasize key concepts or quotes

**Design Elements:**
- Light gray background (`#D8DDE2`)
- Numbered badge in top-left
- Title in H2 size
- Centered white card (85% width, 55% height)
- Bullets with light blue dots
- More generous internal spacing
- Gradient overlay (25-28% opacity)

**When to use**: Key frameworks, important concepts, summary points

### 4. Framework/Multi-Column Slide
**Theme**: Light background
**Purpose**: Present multiple concepts side-by-side

**Design Elements:**
- Light gray background (`#D8DDE2`)
- Numbered badge in top-left
- Title in H2 size
- 2-3 white cards in a row
- Each card has title + bulleted items
- Equal spacing between cards (40px)
- Gradient overlay (28% opacity)

**When to use**: Comparisons, multi-pillar frameworks, parallel concepts

### 5. Final Slide
**Theme**: Dark background
**Purpose**: Closing slide

**Design Elements:**
- Dark gray background (`#4A4A4A`)
- Centered title and subtitle
- H1 title (72-84px bold)
- H2 subtitle (48-56px)
- Gradient overlay (25% opacity)
- Pure white title, light gray subtitle

**When to use**: Slide 57 (final slide)

## Numbered Badges

### Design Specifications
- **Shape**: Perfect circle
- **Size**: 52px diameter (48-56px range)
- **Background**: Light Blue Accent `#A7D4F0`
- **Number color**: Dark Charcoal `#3D3D3D`
- **Number size**: 16-18px bold
- **Position**: Top-left corner of light theme slides
- **Purpose**: Visual hierarchy, slide numbering, accent element

### When to Use
- All light theme content slides (types 2, 3, 4)
- Not used on dark title slides or final slide
- Badge number matches slide number (1-57)

## Design Patterns by Lesson

### Lesson 1: Understanding High-Performance Mindset
- **Slide 1**: Dark title slide
- **Slides 2-9**: Mix of bullet and quote slides (light theme)

### Lesson 2: Destroying Limiting Beliefs
- **Slide 10**: Dark title slide
- **Slides 11-18**: Mix of bullet, framework, and quote slides (light theme)

### Lesson 3: Developing Mental Toughness
- **Slide 19**: Dark title slide
- **Slide 23**: Dark title slide (sub-section)
- **Slides 20-30**: Mix of bullet, quote, and framework slides (light theme)

### Lesson 4: Success Habits of Top Performers
- **Slide 31**: Dark title slide
- **Slides 32-45**: Mix of bullet, quote, and framework slides (light theme)

### Lesson 5: Creating Your Personal Success System
- **Slide 46**: Dark title slide
- **Slides 47-56**: Mix of bullet and quote slides (light theme)
- **Slide 57**: Final dark slide

## Customization Guide

### Changing Colors

Edit the color constants in `generate_startup_slides.py`:

```python
# COLOR PALETTE
LIGHT_BLUE_ACCENT = (167, 212, 240)      # Primary accent
DARK_CHARCOAL = (61, 61, 61)             # Primary text
MEDIUM_GRAY = (90, 90, 90)               # Secondary text
# ... etc
```

### Adjusting Typography

Modify font size functions:

```python
FONT_HERO = lambda: load_font(130, bold=True)      # Display/Hero
FONT_H1 = lambda: load_font(78, bold=True)         # H1 titles
FONT_H2 = lambda: load_font(52, bold=True)         # H2 sections
# ... etc
```

### Changing Card Appearance

Adjust layout constants:

```python
CARD_BORDER_RADIUS = 28  # 24-32px rounded corners
CARD_PADDING = 36        # 32-40px internal padding
BADGE_SIZE = 52          # 48-56px diameter
```

### Modifying Gradients

Edit gradient parameters in slide generation functions:

```python
gradient = create_radial_gradient_overlay(
    (WIDTH, HEIGHT),
    LIGHT_BLUE_ACCENT,    # Color
    opacity=0.3,          # 0.2-0.3 recommended
    position='top-left',  # Corner position
    blur=140              # 120-150px blur
)
```

### Adjusting Spacing

Modify spacing scale:

```python
SPACING_BASE = 8
SPACING_MD = 32
SPACING_LG = 48
SPACING_XL = 64
```

## Technical Implementation

### Dependencies
- **PIL (Pillow)**: Image generation and manipulation
- **Python 3.7+**: Required for f-strings and type hints

### Key Functions

#### Utility Functions
- `draw_rounded_rectangle()`: Creates rounded corner rectangles
- `draw_circular_badge()`: Creates numbered circular badges
- `create_radial_gradient_overlay()`: Generates soft gradient overlays
- `wrap_text()`: Wraps text to fit within specified width
- `get_text_height()` / `get_text_width()`: Measure text dimensions

#### Slide Generation Functions
- `generate_dark_title_slide()`: Lesson separator slides
- `generate_light_bullet_slide()`: Standard content slides
- `generate_light_quote_slide()`: Emphasis/quote slides
- `generate_framework_slide()`: Multi-column grid slides
- `generate_simple_final_slide()`: Closing slide

### Performance
- **Generation time**: ~2-3 seconds per slide
- **Total generation time**: ~2-3 minutes for all 57 slides
- **Output file size**: ~30-50KB per PNG slide
- **PDF file size**: ~2.5MB for complete 57-slide deck

## Comparison with Other Styles

### vs. Pitch Deck Style
- **Startup**: More rounded, card-based, numbered badges
- **Pitch Deck**: Softer gradients, more whitespace, lighter feel

### vs. Premium Style
- **Startup**: Cleaner, more minimalist, modern tech aesthetic
- **Premium**: More decorative elements, icons, varied layouts

### vs. Original Concept A
- **Startup**: Dual-theme, rounded cards, gradient overlays
- **Original**: Single light theme, simple rectangles, gold accents

## Best Practices

### Content Guidelines
1. **Bullet points**: 3-5 per slide maximum
2. **Text length**: Keep bullets under 15 words
3. **Card titles**: 2-5 words, bold and clear
4. **Hierarchy**: Use slide types to create visual rhythm

### Visual Balance
1. **Whitespace**: Aim for 40-50% empty space
2. **Alignment**: Consistent left-alignment for readability
3. **Contrast**: Ensure text is always readable against background
4. **Consistency**: Maintain spacing and sizing across slides

### Accessibility
1. **Color contrast**: Minimum 4.5:1 for body text
2. **Font size**: Minimum 14-16px for body text
3. **Text wrapping**: Avoid orphaned words
4. **Visual hierarchy**: Clear heading structure

## Troubleshooting

### Font Issues
**Problem**: Default fonts being used
**Solution**: Check font paths in `FONT_PATHS` array, ensure system fonts exist

### Gradient Not Visible
**Problem**: Gradient overlay not showing
**Solution**: Increase opacity (0.3-0.4) or adjust color for more contrast

### Text Overflow
**Problem**: Text exceeding card boundaries
**Solution**: Reduce bullet text length or adjust `max_width` in wrap functions

### Alignment Issues
**Problem**: Elements not properly aligned
**Solution**: Verify safe zone calculations and margin constants

## Future Enhancements

Potential improvements for future versions:

1. **Dynamic gradient colors**: Vary gradient by lesson
2. **Animated transitions**: Export with fade effects for presentations
3. **Interactive PDF**: Add hyperlinks and bookmarks
4. **Custom fonts**: Support for uploaded custom typefaces
5. **Template system**: Save/load custom slide templates
6. **Batch customization**: CLI options for quick style tweaks

## Credits

**Design System**: Based on modern startup presentation guidelines
**Generator**: Created by Claude Code
**Inspiration**: Stripe, Linear, Notion, Vercel presentation decks
**Typography**: SF Pro Display/Helvetica Neue
**Version**: 1.0 - November 2025

## Support

For questions or customization requests, refer to:
- Main README in repository root
- Original style guides
- PIL/Pillow documentation

---

**Last Updated**: November 13, 2025
**Status**: Production Ready ✓
**Slides Generated**: 57/57 ✓
**PDF Compiled**: ✓
