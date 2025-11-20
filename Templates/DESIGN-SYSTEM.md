# Active Offer Design System

## Brand Foundation

This document defines the visual standards for all Active Offer templates, PDFs, and worksheets.

---

## Color Palette

### Primary Colors
| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Background | #F5F5F5 | 245, 245, 245 | Page backgrounds, form fields |
| Text Primary | #000000 | 0, 0, 0 | Headlines, body text |
| Text Secondary | #4A4A4A | 74, 74, 74 | Supporting text, captions |

### Accent Colors
| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Accent Blue | #2563EB | 37, 99, 235 | Links, CTAs, highlights |
| Success Green | #16A34A | 22, 163, 74 | Checkmarks, positive indicators |
| Warning Amber | #D97706 | 217, 119, 6 | Cautions, important notes |
| Error Red | #DC2626 | 220, 38, 38 | Red flags, critical warnings |

### Neutral Tones
| Name | Hex | Usage |
|------|-----|-------|
| Light Gray | #E5E5E5 | Borders, dividers |
| Medium Gray | #9CA3AF | Placeholder text |
| Dark Gray | #374151 | Secondary headings |

---

## Typography

### Font Family
**Primary:** Helvetica Neue (macOS) / Arial (Windows fallback)

### Type Scale

| Element | Size | Weight | Line Height | Usage |
|---------|------|--------|-------------|-------|
| H1 - Document Title | 32pt | Bold | 1.2 | Cover pages, main titles |
| H2 - Section Title | 24pt | Bold | 1.3 | Major sections |
| H3 - Subsection | 18pt | Semi-bold | 1.4 | Subsections |
| H4 - Component Title | 14pt | Semi-bold | 1.4 | Tables, callouts |
| Body | 11pt | Regular | 1.5 | Main content |
| Body Small | 10pt | Regular | 1.5 | Captions, footnotes |
| Label | 9pt | Medium | 1.3 | Form labels, tags |

### Text Colors by Context
- Headlines: #000000
- Body text: #000000
- Supporting text: #4A4A4A
- Links: #2563EB
- Placeholder/hint text: #9CA3AF

---

## Spacing System

### Base Unit: 8px

| Name | Size | Usage |
|------|------|-------|
| xs | 4px | Tight spacing within components |
| sm | 8px | Component internal padding |
| md | 16px | Between related elements |
| lg | 24px | Between sections |
| xl | 32px | Major section breaks |
| 2xl | 48px | Page margins |

### Page Margins
- **PDF Documents:** 48px (0.67") all sides
- **Worksheets:** 36px (0.5") all sides
- **Spreadsheets:** Standard Google Sheets margins

---

## Component Library

### 1. Section Header

```
┌─────────────────────────────────────────┐
│ SECTION TITLE                           │
│ ─────────────────────────               │
└─────────────────────────────────────────┘
```

- H2 in bold, all caps
- 2px underline in #E5E5E5
- 24px margin below

### 2. Callout Box

```
┌─────────────────────────────────────────┐
│ 💡 PRO TIP                              │
│                                         │
│ Callout content goes here with          │
│ important information highlighted.      │
└─────────────────────────────────────────┘
```

- Background: #F0F9FF (light blue tint)
- Border: 1px solid #2563EB
- Padding: 16px
- Icon + label in semi-bold

**Callout Types:**
- 💡 Pro Tip (blue)
- ⚠️ Warning (amber background #FFFBEB)
- 🚩 Red Flag (red background #FEF2F2)
- ✅ Quick Win (green background #F0FDF4)

### 3. Numbered List

```
1. First item with clear instruction

2. Second item continues the sequence

3. Third item completes the set
```

- Numbers in semi-bold
- 8px gap between number and text
- 12px margin between items

### 4. Checkbox List

```
☐ Item to be completed
☐ Another action item
☐ Final checklist item
```

- Interactive checkboxes in PDFs
- 8px gap between box and text
- 8px margin between items

### 5. Form Field

```
Label Text
┌─────────────────────────────────────────┐
│                                         │
│                                         │
└─────────────────────────────────────────┘
```

- Label: 9pt medium, #4A4A4A
- Field: 1px border #E5E5E5
- Background: #FFFFFF
- Padding: 8px
- Height: varies by content type

### 6. Rating Scale

```
How confident are you in X?

Not at all  ○ 1  ○ 2  ○ 3  ○ 4  ○ 5  Very confident
```

- Labels on ends in 9pt
- Radio buttons spaced evenly
- Numbers below each option

### 7. Table

```
┌──────────────┬──────────────┬──────────────┐
│ Header 1     │ Header 2     │ Header 3     │
├──────────────┼──────────────┼──────────────┤
│ Cell content │ Cell content │ Cell content │
├──────────────┼──────────────┼──────────────┤
│ Cell content │ Cell content │ Cell content │
└──────────────┴──────────────┴──────────────┘
```

- Header row: #F5F5F5 background, semi-bold
- Borders: 1px #E5E5E5
- Cell padding: 8px
- Alternating row colors optional

### 8. Progress Indicator

```
Phase 1    Phase 2    Phase 3    Phase 4
  ●──────────○──────────○──────────○
```

- Active: filled circle #2563EB
- Inactive: outline circle #E5E5E5
- Line: 2px #E5E5E5

---

## Page Templates

### Cover Page Layout

```
┌─────────────────────────────────────────┐
│                                         │
│                                         │
│         [DOCUMENT TITLE]                │
│         H1, centered                    │
│                                         │
│         Subtitle or description         │
│         Body, centered                  │
│                                         │
│                                         │
│                                         │
│         ACTIVE OFFER                    │
│         Logo/wordmark                   │
│                                         │
└─────────────────────────────────────────┘
```

### Content Page Layout

```
┌─────────────────────────────────────────┐
│ Section Title                      [3]  │
├─────────────────────────────────────────┤
│                                         │
│ Content area with appropriate           │
│ margins and spacing as defined          │
│ in the spacing system.                  │
│                                         │
│ Components placed according to          │
│ the component library specs.            │
│                                         │
│                                         │
│                                         │
│                                         │
├─────────────────────────────────────────┤
│ Active Offer              Document Name │
└─────────────────────────────────────────┘
```

- Page numbers: top right, 10pt
- Footer: brand name left, document name right, 9pt

### Worksheet Page Layout

```
┌─────────────────────────────────────────┐
│ Exercise Title                          │
├─────────────────────────────────────────┤
│                                         │
│ Instructions in body text               │
│                                         │
│ ┌─────────────────────────────────────┐ │
│ │ Form field or response area         │ │
│ │                                     │ │
│ │                                     │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ Additional guidance or examples         │
│                                         │
└─────────────────────────────────────────┘
```

---

## File Naming Convention

### PDFs
`[Category]-[Name]-v[Version].pdf`

Examples:
- `Guide-AE-Resume-Blueprint-v1.pdf`
- `Assessment-Fit-Finder-v1.pdf`
- `Worksheet-Stay-or-Go-Calculator-v1.pdf`

### Spreadsheets
`Active-Offer-[Name]-Template`

Examples:
- `Active-Offer-Job-Search-CRM-Template`
- `Active-Offer-Interview-Question-Bank`
- `Active-Offer-90-Day-Sprint-Planner`

---

## Google Sheets Standards

### Tab Colors
- Instructions: #2563EB (blue)
- Input/Tracker tabs: #F5F5F5 (light gray)
- Output/Dashboard: #16A34A (green)
- Reference: #9CA3AF (medium gray)

### Cell Formatting
- Headers: Bold, #F5F5F5 background, centered
- Input cells: White background, light border
- Calculated cells: #F0F9FF background (light blue)
- Locked cells: #F5F5F5 background

### Data Validation
- Use dropdowns for categorical fields
- Add helper text in cell notes
- Conditional formatting for status indicators:
  - Green: Complete/Good
  - Yellow: In Progress/Caution
  - Red: Not Started/Issue

---

## Accessibility Guidelines

### Color Contrast
- All text must meet WCAG 2.1 AA standards
- Minimum contrast ratio: 4.5:1 for body text
- Minimum contrast ratio: 3:1 for large text

### Form Fields
- Clear labels above or beside all fields
- Sufficient field size for text entry
- Tab order follows logical reading flow

### Document Structure
- Use proper heading hierarchy (H1 → H2 → H3)
- Include alt text for any images
- Provide text alternatives for charts/diagrams

---

## Export Settings

### PDF Export
- Format: PDF/A (for archival/accessibility)
- Quality: High
- Include: Bookmarks, hyperlinks
- Optimize for: Standard viewing

### Print Settings
- Size: US Letter (8.5" x 11")
- Orientation: Portrait (unless data-heavy tables)
- Margins: As specified in spacing system
- Color: Full color (grayscale fallback acceptable)

---

## Quick Reference

### Most Used Values
- Page margins: 48px
- Section spacing: 24px
- Component spacing: 16px
- Text color: #000000
- Background: #F5F5F5
- Accent: #2563EB
- Font: Helvetica Neue, 11pt body

### Component Checklist
When creating any deliverable, ensure:
- [ ] Correct fonts applied
- [ ] Color palette followed
- [ ] Spacing system used
- [ ] Headers properly styled
- [ ] Forms are fillable (if applicable)
- [ ] Page numbers included
- [ ] Footer with branding
- [ ] File named correctly

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024 | Initial design system |

---

*This design system should be referenced for all Active Offer course materials to ensure brand consistency and professional presentation.*
