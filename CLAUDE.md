# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

@sessions/CLAUDE.sessions.md

## Repository Overview

This repository contains course materials for **Active Offer** - a high-ticket career development program for sales professionals targeting $200k-$500k+ roles. The repository includes course modules, webinar scripts, slide generation tools, and supporting resources.

## Key Architecture

### Content Types

**Course Modules (M0-M5)**
- Delivered as sequential PNG slide images (1920x1080, 16:9 aspect ratio)
- Original modules: M0 (Course Intro, Mindset), M1-M5 (tactical content)
- Expanded module: M0- Mindset Expanded (57 slides across 5 progressive lessons)
- All slides use minimalist design: light gray background (#F5F5F5), black text (#000000), Helvetica typography

**Webinar Scripts (Markdown)**
- Multiple versioned scripts tracking evolution of presentation
- Latest: v4.1 uses Russell Brunson's "Perfect Webinar" Three Secrets Framework
- Contains detailed slide-by-slide talking points and content
- Webinar slide decks stored as PNG exports in `.Webinar Script v.X` directories

**Supporting Resources**
- External Assets/: Student-facing templates and tools
- Internal Tools/: Internal-use tools (e.g., Comp Negotiator)
- Internal Documents/ and Internal SOPs/: Documentation folders

### Technology Stack

**Python Environment**
- Python 3.14+
- Virtual environment: `.venv/` (activate with `source .venv/bin/activate`)
- Primary tool: `generate_mindset_slides.py` for slide generation
- Dependencies: PIL (Pillow) for image generation

**Development Workflow**
- cc-sessions installed for task management and workflow automation
- DAIC mode system: Discussion → Implementation → Check pattern
- See [sessions/CLAUDE.sessions.md](sessions/CLAUDE.sessions.md) for collaboration philosophy

## Common Commands

### Python Slide Generation

**Generate Mindset Module Slides:**
```bash
# Activate virtual environment first
source .venv/bin/activate

# Generate all 57 slides
python3 generate_mindset_slides.py

# Output: M0- Mindset Expanded/*.png (1-57.png)
```

**Customize Slide Generation:**
The script uses configuration at the top of `generate_mindset_slides.py`:
- Modify `slides_content` array to change/add slide content
- Adjust typography constants (TITLE_FONT_SIZE, BODY_FONT_SIZE, etc.)
- Change brand colors (BACKGROUND_COLOR, TEXT_COLOR)
- Regenerate after modifications

### Sessions Workflow

**Check current mode:**
```bash
sessions mode
```

**Task Management:**
- User creates tasks with trigger phrase: `mek:`
- User starts tasks with: `start^`
- User completes tasks with: `finito`
- User compacts context with: `squish`
- User enters implementation mode with: `yert`
- User returns to discussion mode with: `SILENCE`

**Git Configuration:**
- Commit style: "detailed" (comprehensive commit messages)
- Auto-merge: enabled
- Auto-push: enabled
- Branch enforcement: enabled
- Default branch: main

## Repository Structure & Workflow

### Module Naming Convention

Modules follow sequential pattern: `M[number]- [Module Name]/`
- M0- Course Intro
- M0- Mindset (original)
- M0- Mindset Expanded (comprehensive version)
- M1- Profile Matching
- M2- Reverse Attraction
- M3- Interview Mastery
- M4- Negotiating the Offer
- M5- Tell Your Story

### Slide Numbering

Within each module directory:
- Sequential numbering: `1.png`, `2.png`, `3.png`, etc.
- No gaps in numbering
- Start at 1 for each module
- PNG format only (1920x1080 resolution)

### Webinar Script Versioning

Scripts follow pattern: `Webinar-Script-v[X.Y]-[Enhancement-Description].md`
- Hidden directories: `.Webinar Script v.X/` contain PNG slide exports
- Markdown files document script evolution and talking points
- Current version: v4.1 (Bold Promise Enhancement)

### Design Philosophy

**Content Creation Principles:**
- High-ticket positioning: Professional, authoritative, premium quality
- Minimalist aesthetics: Clean, focused, no decorative elements
- Evidence-based: All claims backed by research or case studies
- Transformation-focused: Systems and frameworks, not just information
- Progressive lesson structure: Scaffolded learning with clear progression

**Brand Consistency:**
- Maintain exact visual style across all slides
- Use system fonts (Helvetica on macOS)
- Generous white space and margins
- Bold titles, readable body text
- Bullet points for scannable content

## Key Files

**Documentation:**
- [CLAUDE.md](CLAUDE.md) - This file
- [sessions/CLAUDE.sessions.md](sessions/CLAUDE.sessions.md) - Collaboration philosophy and workflow
- [M0- Mindset Expanded/README.md](M0-%20Mindset%20Expanded/README.md) - Expanded module documentation
- [M0- Mindset Expanded/SLIDE_INDEX.md](M0-%20Mindset%20Expanded/SLIDE_INDEX.md) - Complete slide content reference
- [M0- Mindset Expanded/DESIGN_DOCUMENTATION.md](M0-%20Mindset%20Expanded/DESIGN_DOCUMENTATION.md) - Design rationale and guidelines
- [Course-Review-Feedback.md](Course-Review-Feedback.md) - Course architect's comprehensive review
- [Webinar-Evaluation-Report-v2.2.md](Webinar-Evaluation-Report-v2.2.md) - Latest webinar analysis

**Key Scripts:**
- [generate_mindset_slides.py](generate_mindset_slides.py) - Python script for generating M0 slides

**Configuration:**
- [sessions/sessions-config.json](sessions/sessions-config.json) - Workflow automation settings
- [.gitignore](.gitignore) - Excludes sessions runtime files and Python artifacts

## Working with This Repository

### When Creating New Content

1. **New Module Slides:**
   - Maintain 1920x1080 PNG format
   - Follow sequential numbering starting at 1
   - Use brand colors and typography consistently
   - Consider using `generate_mindset_slides.py` as template for automation

2. **Webinar Script Updates:**
   - Version appropriately: v[X.Y]-[Description].md
   - Document changes in version history section
   - Reference slide numbers for talking points
   - Keep evaluation reports to track improvements

3. **Supporting Resources:**
   - Student-facing materials → External Assets/
   - Internal tools → Internal Tools/
   - Documentation → Internal Documents/
   - Maintain README files for complex resources

### When Modifying Existing Content

1. **Slide Content Changes:**
   - Edit `generate_mindset_slides.py` `slides_content` array
   - Regenerate slides to maintain consistency
   - Update SLIDE_INDEX.md if structure changes
   - Test output before committing

2. **Webinar Iterations:**
   - Create new version file (don't overwrite)
   - Document rationale for changes
   - Update evaluation reports with performance data
   - Archive old slide directories if needed

3. **Module Expansions:**
   - Follow M0- Mindset Expanded as reference model
   - Create comprehensive documentation package
   - Include README, SLIDE_INDEX, and DESIGN_DOCUMENTATION
   - Document source script for reproducibility

## Development Philosophy

See [sessions/CLAUDE.sessions.md](sessions/CLAUDE.sessions.md) for detailed philosophy, but key principles:

- **Investigate patterns** - Understand existing conventions before creating new approaches
- **Confirm approach** - Explain reasoning and get consensus before major changes
- **Locality of behavior** - Keep related content together
- **Solve today's problems** - Avoid over-abstraction
- **Readability over cleverness** - Make content obvious and easy to follow
