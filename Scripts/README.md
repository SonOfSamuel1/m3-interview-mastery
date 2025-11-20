# Scripts

Python automation scripts for generating course materials and resources.

## Environment Setup

All scripts require the Python virtual environment:

```bash
# Activate virtual environment
source .venv/bin/activate

# Install dependencies (if needed)
pip install -r requirements.txt
```

## Available Scripts

### Course Module Generation

**`generate_mindset_slides.py`**
- Generates all 57 slides for M0- Mindset Expanded module
- Output: `Modules/M0- Mindset Expanded/*.png`
- Usage: `python3 Scripts/generate_mindset_slides.py`

**`generate_course_intro_slides.py`**
- Generates slides for M0- Course Intro module
- Output: `Modules/M0- Course Intro/*.png`

**`generate_m1_slides.py`**
- Generates slides for M1- Profile Matching module
- Output: `Modules/M1- Profile Matching/*.png`

**`generate_m1_enhancements.py`**
- Generates enhanced content for M1 module
- Related to M1 enhancement project

**`generate_panel_slides.py`**
- Generates multi-panel layout slides
- Used for comparison or framework slides

**`generate_remaining_slides.py`**
- Batch generation for remaining module content

**`generate_slide_11_update.py`**
- Updates specific slide (likely M1 slide 11)

### Webinar Generation

**`generate_webinar_slides.py`**
- Generates webinar presentation slides
- Output: `Webinars/Current/` or version directories

### Resource Generation

**`generate_excel_templates.py`**
- Creates Excel-based student resources
- Generates tracking templates and worksheets

**`generate_self_assessment_pdf.py`**
- Creates PDF version of self-assessment worksheet
- Output: `External Assets/Self-Assessment-Worksheet.pdf`

### PDF Compilation

**`compile_m1_pdf.py`**
- Compiles M1 slides into single PDF document

**`compile_final_m1_pdf.py`**
- Final M1 PDF compilation with enhancements

## Customization

### Slide Content

Most scripts define slide content at the top of the file in a `slides_content` array:

```python
slides_content = [
    {
        "title": "Slide Title",
        "body": "Slide content here"
    },
    # ... more slides
]
```

Edit these arrays to modify slide content, then regenerate.

### Visual Style

Typography and color constants are typically defined near the top:

```python
BACKGROUND_COLOR = "#F5F5F5"  # Light gray
TEXT_COLOR = "#000000"        # Black
TITLE_FONT_SIZE = 72
BODY_FONT_SIZE = 36
```

Modify these to adjust brand styling (not recommended without updating CLAUDE.md).

### Output Paths

Scripts typically use relative paths from repository root. Ensure you run scripts from the correct directory or adjust paths as needed.

## Dependencies

Primary dependency: **Pillow (PIL)** for image generation

```bash
pip install Pillow
```

Some scripts may require additional libraries. Check individual script imports.

## Design Standards

All generated slides follow Active Offer brand guidelines:
- **Resolution**: 1920x1080 pixels (16:9)
- **Background**: #F5F5F5 (light gray)
- **Text**: #000000 (black)
- **Font**: Helvetica (system font)
- **Style**: Minimalist, professional, high-ticket positioning

See `Modules/M0- Mindset Expanded/DESIGN_DOCUMENTATION.md` for detailed design rationale.

## Best Practices

1. **Always activate .venv first** before running any script
2. **Backup existing slides** before regenerating (or commit to git)
3. **Test output** by viewing generated PNG files
4. **Update SLIDE_INDEX.md** if you modify slide content/structure
5. **Document custom scripts** with inline comments

## Creating New Scripts

When creating new slide generation scripts:

1. Copy an existing script as template (e.g., `generate_mindset_slides.py`)
2. Define slide content array
3. Use consistent brand styling constants
4. Output to appropriate `Modules/` subdirectory
5. Use sequential numbering (1.png, 2.png, etc.)
6. Add documentation to this README

## Troubleshooting

**"ModuleNotFoundError: No module named 'PIL'"**
- Activate virtual environment: `source .venv/bin/activate`
- Install Pillow: `pip install Pillow`

**"No such file or directory" errors**
- Ensure output directories exist
- Run from repository root or adjust paths

**Font issues on non-macOS systems**
- Scripts use system Helvetica font
- May need to adjust font names for Windows/Linux
