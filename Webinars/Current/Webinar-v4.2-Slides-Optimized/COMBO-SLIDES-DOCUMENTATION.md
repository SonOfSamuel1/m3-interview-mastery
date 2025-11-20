# Combo Slide Documentation

## Overview

The webinar slide generation system has been enhanced to create **combo slides** - slides that integrate text content with image placeholders, rather than having standalone placeholder-only slides.

**Previous System:** 27 standalone slides with only "[INSERT IMAGE]" placeholders
**New System:** 27 combo slides with integrated text, context, and image placeholders

## Benefits

1. **Better Narrative Flow:** Text and imagery are integrated on the same slide, maintaining story momentum
2. **Clear Context:** Image placeholders have accompanying headlines, metrics, and takeaways
3. **Professional Design:** Four distinct layout patterns optimized for different content types
4. **Easy Maintenance:** All 27 slides defined in structured `COMBO_SLIDES` dictionary
5. **Consistent Styling:** Maintains v2.1 blue design system across all combo slides

## Four Layout Categories

### 1. Narrative Illustration (11 slides)
**Purpose:** Story-driven slides with emotional context
**Structure:** Context text → Image → Emotional hook

**Slides Using This Layout:**
- 12-img, 13B-img, 13D-img, 13F-img, 24-img, 26-img, 46-img, 56-img, 59-img, 75-img, 101-img, 126-img

**Example (Slide 26-img):**
```
Top: "Then I Overheard Two Coworkers Talking..."
[IMAGE PLACEHOLDER: Office scene with $400K speech bubble]
Bottom: "Same Skills as Me. Different Company. 3× the Income."
```

**Data Structure:**
```python
'26-img': {
    'type': 'narrative_illustration',
    'top_text': 'Then I Overheard Two Coworkers Talking...',
    'bottom_text': 'Same Skills as Me. Different Company. 3× the Income.',
    'image_desc': 'Office environment. Two silhouetted colleagues. Speech bubble: "$400,000". Shocked listener reaction.'
}
```

---

### 2. Framework Diagram (7 slides)
**Purpose:** Teaching slides with conceptual frameworks
**Structure:** Title → Framework/Diagram → Key Takeaway

**Slides Using This Layout:**
- 37-img, 66-img, 86-img, 110-img

**Example (Slide 37-img):**
```
Title: "The 3 Positioning Factors"
[FRAMEWORK DIAGRAM: Three architectural pillars]
Takeaway: "Master These → Control Your Income"
```

**Data Structure:**
```python
'37-img': {
    'type': 'framework_diagram',
    'title': 'The 3 Positioning Factors',
    'bottom_text': 'Master These → Control Your Income',
    'image_desc': 'Three architectural pillars. Left: "WHO - Which Companies Pay More". Center: "WHICH - Roles & Comp Structure". Right: "HOW - Strategic Positioning".'
}
```

---

### 3. Data Visualization (8 slides)
**Purpose:** Proof slides with metrics and results
**Structure:** Headline → Data Visual → Key Metric

**Slides Using This Layout:**
- 22-img, 23-img, 51-img, 73-img, 84-img, 93-img, 96-img, 139-img

**Example (Slide 84-img):**
```
Headline: "The 5-Day Experiment"
[DATA VISUALIZATION: 5-day calendar → 3 interviews]
Metric: "30 min/day × 5 days = 3 INTERVIEWS"
Bottom: "Same System Still Works Today"
```

**Data Structure:**
```python
'84-img': {
    'type': 'data_visualization',
    'headline': 'The 5-Day Experiment',
    'metric': '30 min/day × 5 days = 3 INTERVIEWS',
    'bottom_text': 'Same System Still Works Today',
    'image_desc': '5-day calendar with daily 30-min blocks. Leading to "Week 2: THREE INTERVIEWS SCHEDULED".'
}
```

---

### 4. Before/After Comparison (4 slides)
**Purpose:** Belief-shifting contrast slides
**Structure:** Split comparison → Transformation statement

**Slides Using This Layout:**
- 48-img, 64-img, 102-img

**Example (Slide 48-img):**
```
Top: "Here's What You Need to Hear..."

Left Column:                Right Column:
"YOU ALREADY HAVE:"        "YOU DON'T NEED:"
✓ Experience               ✗ MBA
✓ Skills                   ✗ Connections
✓ Track Record             ✗ More Skills

Bottom: "You're Not Under-Qualified. You're Under-POSITIONED."
```

**Data Structure:**
```python
'48-img': {
    'type': 'before_after',
    'top_text': 'Here\'s What You Need to Hear...',
    'left_title': 'YOU ALREADY HAVE:',
    'left_items': ['✓ Experience', '✓ Skills', '✓ Track Record'],
    'right_title': 'YOU DON\'T NEED:',
    'right_items': ['✗ MBA', '✗ Connections', '✗ More Skills'],
    'bottom_text': 'You\'re Not Under-Qualified. You\'re Under-POSITIONED.'
}
```

---

## Technical Implementation

### File Structure
```
generate_slides_v4_1.py
├── COMBO_SLIDES dictionary (lines 515-688)
│   └── 27 slide definitions with type, text content, image descriptions
├── create_combo_slide_html() (lines 513-527)
│   └── Routes to appropriate layout function
├── Layout Functions:
│   ├── create_narrative_illustration() (lines 529-597)
│   ├── create_framework_diagram() (lines 599-653)
│   ├── create_data_visualization() (lines 655-712)
│   └── create_before_after_comparison() (lines 714-807)
└── Generation Logic (lines 1031-1052)
    └── Loops through COMBO_SLIDES and generates PNGs
```

### Design Specifications

**Image Placeholder Boxes:**
- Border: 6px dashed #3182ce (accent blue)
- Background: #e2e8f0 (light gray)
- Padding: 80px 60px
- Border radius: 16px
- Min height: 400-500px depending on layout

**Typography:**
- Headlines: 72px, font-weight 600
- Titles: 56px, font-weight 600
- Metrics: 80px, font-weight 700, accent blue
- Body text: 38-42px, line-height 1.5-1.6
- Placeholder labels: 48px, font-weight 700, accent blue

**Spacing:**
- Top section: ~20% of slide
- Image area: 50-70% of slide
- Bottom section: ~15-20% of slide
- Consistent 30-40px margins between sections

---

## Adding New Combo Slides

To add a new combo slide to the system:

### Step 1: Choose Layout Type
Determine which of the 4 layout categories fits your content:
- **Narrative Illustration:** Story-driven with emotional context
- **Framework Diagram:** Teaching/conceptual framework
- **Data Visualization:** Metrics, results, timelines
- **Before/After:** Contrast and comparison

### Step 2: Define in COMBO_SLIDES
Add entry to the `COMBO_SLIDES` dictionary in `generate_slides_v4_1.py`:

```python
COMBO_SLIDES = {
    # ... existing slides ...

    'NEW-SLIDE-ID': {
        'type': 'narrative_illustration',  # or framework_diagram, data_visualization, before_after
        'top_text': 'Your headline text',
        'bottom_text': 'Your takeaway text',
        'image_desc': 'Description of what image should contain'
    }
}
```

### Step 3: Available Fields by Type

**Narrative Illustration:**
- `top_text` - Main headline
- `subtitle` - Secondary headline
- `bottom_text` - Emotional hook or takeaway
- `bullets` - List of items (displayed inline)
- `corners` - 4 items for 2×2 grid layout
- `image_desc` - Image description

**Framework Diagram:**
- `title` - Framework title
- `bottom_text` - Key takeaway
- `metric` - Optional large number/stat
- `image_desc` - Diagram description

**Data Visualization:**
- `headline` - Main headline
- `subtitle` - Secondary headline
- `metric` - Large prominent metric
- `bottom_text` - Context or reinforcement
- `image_desc` - Data viz description

**Before/After:**
- `title` - Large title (optional)
- `top_text` - Section header (optional)
- `subtitle` - Explanation text (optional)
- `left_title` - Left column header
- `left_items` - List for left column
- `left_text` - Paragraph for left (if no items)
- `right_title` - Right column header
- `right_items` - List for right column
- `right_text` - Paragraph for right (if no items)
- `bottom_text` - Transformation statement
- `image_desc` - Comparison visual description

### Step 4: Regenerate Slides
```bash
cd "Webinar-v4.1-Slides-Styled"
source ../.venv/bin/activate
python3 generate_slides_v4_1.py
```

---

## Design Guidelines

### Text Content Best Practices

1. **Headlines (top_text):**
   - Keep under 60 characters
   - Use action words or emotional language
   - End with ellipsis for narrative continuity

2. **Metrics:**
   - Make numbers prominent ($90K, 30 min/day, 3×)
   - Use formulas for clarity (30 min/day × 5 days = 3 INTERVIEWS)
   - Include units/context

3. **Bottom Text (takeaways):**
   - One clear idea per line
   - Use bullet separator (•) for multiple points
   - Bold key concepts

4. **Image Descriptions:**
   - Be specific about visual elements
   - Include key labels, numbers, colors
   - Describe spatial relationships (left/right, top/bottom)

### Visual Hierarchy

**Priority 1 (Most Prominent):**
- Large metrics and key numbers
- Main headlines
- Transformation statements

**Priority 2 (Supporting):**
- Subtitles and context text
- Image placeholder boxes
- Section headers

**Priority 3 (Tertiary):**
- Image descriptions within placeholders
- Corner text and bullets
- Attribution or notes

---

## Comparison: Before vs After

### Before (Standalone Placeholders)
```
Slide 26:
┌─────────────────────────────────────┐
│                                     │
│        [INSERT IMAGE]               │
│                                     │
│  Office environment. Two            │
│  silhouetted colleagues.            │
│  Speech bubble: "$400,000".         │
│  Shocked listener reaction.         │
│                                     │
└─────────────────────────────────────┘
```
**Issues:**
- No context without presenter's narration
- Interrupts story flow
- Image description feels like outline notes

### After (Combo Slide)
```
Slide 26-img:
┌─────────────────────────────────────┐
│  Then I Overheard Two Coworkers     │
│  Talking...                         │
│                                     │
│  ┌───────────────────────────────┐  │
│  │  [IMAGE PLACEHOLDER]          │  │
│  │  Office scene with colleagues │  │
│  │  Speech bubble: "$400,000"    │  │
│  └───────────────────────────────┘  │
│                                     │
│  Same Skills as Me. Different       │
│  Company. 3× the Income.            │
└─────────────────────────────────────┘
```
**Improvements:**
- Context maintains narrative flow
- Emotional impact of bottom text
- Self-explanatory even without audio
- Professional presentation quality

---

## Maintenance & Updates

### Updating Existing Combo Slides

1. **Locate slide in COMBO_SLIDES dictionary** (lines 515-688)
2. **Modify text fields** as needed
3. **Regenerate slides** with Python script
4. **Review output** in `Webinar-v4.1-Slides-Styled/` directory

### Changing Layout Type

If you need to change a slide from one layout type to another:

1. Update the `'type'` field
2. Add/remove fields to match new layout requirements
3. Regenerate slides
4. Verify visual output

Example: Converting narrative to data visualization
```python
# Before (narrative_illustration)
'93-img': {
    'type': 'narrative_illustration',
    'top_text': 'Darrell\'s Success',
    'image_desc': '...'
}

# After (data_visualization)
'93-img': {
    'type': 'data_visualization',
    'headline': 'Darrell\'s First Success',
    'metric': '+$90K Raise',
    'subtitle': '$100K → $190K',
    'bottom_text': '30 Min/Day • While Employed',
    'image_desc': '...'
}
```

---

## Next Phase: Actual Graphics

Currently, all 27 combo slides have **placeholder boxes** where images will eventually go. The next phase involves creating actual graphics:

### Priority Tier 1 - Frameworks (Weeks 8-9)
Create 7 framework diagrams using Python PIL/Pillow:
1. Slide 37-img - Three Positioning Pillars
2. Slide 66-img - Skills Translation Matrix
3. Slide 86-img - Reverse Attraction Process
4. Slide 110-img - Value Stack Calculator

### Priority Tier 2 - Data Viz (Week 10)
Generate 8 data visualizations:
1. Slide 22-img - 10-year timeline
2. Slide 23-img - Income ceiling graph
3. Slide 51-img - Success timeline
4. Slide 73-img - Pattern recognition
5. Slide 84-img - 5-day calendar
6. Slide 93-img - Transformation timeline
7. Slide 96-img - Three success stories
8. Slide 139-img - 45-day progression

### Priority Tier 3 - Illustrations (Weeks 11-12)
Source or create 12 narrative illustrations:
1. Slide 12-img - AT&T office scene
2. Slide 13B-img - Morning workspace
3. Slide 13D-img - Choice visualization
4. Slide 13F-img - Before/After transformation
5. Slide 24-img - Four pain points
6. Slide 26-img - $400K conversation
7. Slide 46-img - Doubt bubbles
8. Slide 56-img - Impostor syndrome
9. Slide 59-img - Determined preparation
10. Slide 75-img - Objection bubbles
11. Slide 101-img - One-year transformation
12. Slide 126-img - Scarcity urgency

---

## Generation Statistics

**Total Slides Generated:** 184
- 157 content slides (from markdown)
- 27 combo text+image slides

**Layout Distribution:**
- Narrative Illustration: 12 slides
- Framework Diagram: 4 slides
- Data Visualization: 8 slides
- Before/After Comparison: 3 slides

**Generation Time:** ~2 minutes for full deck

**File Naming Convention:**
- Content slides: `slide-1.png`, `slide-4A.png`, etc.
- Combo slides: `slide-12-img.png`, `slide-26-img.png`, etc.

---

## Troubleshooting

### Slide Not Generating
**Issue:** Slide ID in COMBO_SLIDES but PNG not created
**Solution:** Check for Python syntax errors in dictionary definition, ensure quotes are properly escaped

### Text Overlapping
**Issue:** Long text runs outside boundaries
**Solution:** Shorten text content or split into multiple lines using `\n`, consider line-height adjustments

### Wrong Layout Rendering
**Issue:** Slide using wrong template
**Solution:** Verify `'type'` field matches one of 4 valid options exactly

### Missing Fields Error
**Issue:** Layout function expecting field that doesn't exist
**Solution:** All fields are optional with `.get()`, but verify you're including required fields for that layout type

---

## Version History

**v1.0 (Current) - Combo Slide Implementation**
- Created 4 layout templates
- Mapped all 27 placeholders to combo structure
- Implemented text+image integration
- Generated initial combo slides with placeholders

**Future Versions:**
- v1.1 - Add actual framework diagrams (PIL-generated)
- v1.2 - Add data visualizations
- v1.3 - Add narrative illustrations
- v2.0 - Dynamic typography based on content length
- v2.1 - Auto-split logic for text-heavy slides

---

## Support & Contact

For questions about combo slide generation:
- Review this documentation first
- Check `generate_slides_v4_1.py` source code comments
- Test changes on individual slides before regenerating full deck
- Refer to `CLAUDE.md` for general repository guidance

Last Updated: 2025-01-17
