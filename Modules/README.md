# Modules

This directory contains all **Active Offer** course modules (M0-M5).

## Module Structure

Each module is delivered as a series of PNG slide images (1920x1080, 16:9 aspect ratio):

- **M0- Course Intro**: Introduction to the Active Offer program
- **M0- Mindset**: Original mindset module
- **M0- Mindset Expanded**: Comprehensive 57-slide mindset module with 5 progressive lessons
- **M1- Profile Matching**: Building your ideal candidate profile
- **M2- Reverse Attraction**: Making companies pursue you
- **M3- Interview Mastery**: Advanced interview techniques
- **M4- Negotiating the Offer**: Compensation negotiation strategies
- **M5- Tell Your Story**: Personal branding and storytelling

## Design Standards

All slides maintain consistent branding:
- **Resolution**: 1920x1080 pixels (16:9 aspect ratio)
- **Background**: Light gray (#F5F5F5)
- **Text**: Black (#000000)
- **Typography**: Helvetica (system font)
- **Style**: Minimalist, professional, high-ticket positioning

## Slide Numbering

Within each module directory:
- Sequential numbering: `1.png`, `2.png`, `3.png`, etc.
- No gaps in numbering
- All slides start at 1

## Generating Slides

Most modules have corresponding Python generation scripts in `Scripts/`:
- `Scripts/generate_mindset_slides.py` - Generate M0- Mindset Expanded slides
- `Scripts/generate_m1_slides.py` - Generate M1 slides
- `Scripts/generate_course_intro_slides.py` - Generate M0- Course Intro slides

See `Scripts/README.md` for usage instructions.

## Module Documentation

For detailed module documentation, see:
- `M0- Mindset Expanded/README.md` - Comprehensive expansion overview
- `M0- Mindset Expanded/SLIDE_INDEX.md` - Complete slide content reference
- `M0- Mindset Expanded/DESIGN_DOCUMENTATION.md` - Design rationale and guidelines
- `Documentation/Planning/` - Module enhancement summaries
