# STARTUP PRESENTATION STYLE - QUICK START GUIDE

## What You Get

A complete 57-slide presentation deck with a professional 2025 startup pitch deck aesthetic:

- **Dual-theme design**: Alternates between light and dark backgrounds
- **Rounded card components**: Modern, clean, sophisticated
- **Numbered circular badges**: Visual hierarchy and navigation
- **Soft gradient overlays**: Creates depth without distraction
- **Professional typography**: SF Pro Display/Helvetica Neue
- **Perfect for**: Investor pitches, client presentations, training materials

## 30-Second Start

```bash
# Generate all slides
python3 generate_startup_slides.py

# Compile to PDF
python3 compile_startup_to_pdf.py
```

That's it! You'll have:
- **57 PNG slides**: `slide-01-startup.png` through `slide-57-startup.png`
- **1 PDF**: `M0-Mindset-Module-STARTUP-STYLE.pdf`

## Key Design Features

### 🎨 Color Palette
- **Light Blue Accent** (#A7D4F0): Badges, bullets, highlights
- **Dark Charcoal** (#3D3D3D): Primary text on light backgrounds
- **Light Gray** (#D8DDE2): Main light background
- **Dark Gray** (#4A4A4A): Dark theme background
- **Pure White** (#FFFFFF): Cards and text on dark

### 📐 Layout
- **1920x1080px**: Standard 16:9 presentation format
- **80px safe margins**: Professional spacing from edges
- **28px rounded corners**: Modern card aesthetic
- **Numbered badges**: 52px diameter circular accents

### ✍️ Typography
- **Hero text**: 120-140px bold (lesson titles)
- **Main titles**: 48-56px bold (slide headings)
- **Body text**: 18-20px regular (content)
- **Font stack**: SF Pro Display → Helvetica Neue → Helvetica

## Slide Types

### 🌑 Dark Title Slides
**When**: Start of each lesson (5 slides total)
**Look**: Dark background, large centered hero text, gradient overlay
**Examples**: Slides 1, 10, 19, 31, 46

### ☀️ Light Content Slides
**When**: Main content (most slides)
**Look**: Light background, numbered badge, white card with bullets
**Examples**: Slides 2-9, 11-18, 20-30, 32-45, 47-56

### 🎯 Framework Slides
**When**: Comparing concepts or showing multiple pillars
**Look**: Light background, 2-3 cards in a row, structured layout
**Examples**: Slides 14, 29, 34

### 📝 Quote/Emphasis Slides
**When**: Highlighting key insights or frameworks
**Look**: Light background, centered card with key points
**Examples**: Slides 8, 15, 25, 33, 37, 38, 41, 51

### 🏁 Final Slide
**When**: Closing slide (slide 57)
**Look**: Dark background, centered title + subtitle

## Content Structure

The 57 slides cover 5 progressive lessons:

1. **Slides 1-9**: Understanding High-Performance Mindset
2. **Slides 10-18**: Destroying Limiting Beliefs
3. **Slides 19-30**: Developing Mental Toughness
4. **Slides 31-45**: Success Habits of Top Performers
5. **Slides 46-57**: Creating Your Personal Success System

## Quick Customization

### Change Accent Color

Edit line 83 in `generate_startup_slides.py`:
```python
LIGHT_BLUE_ACCENT = (167, 212, 240)  # Change RGB values here
```

### Adjust Card Roundness

Edit line 123:
```python
CARD_BORDER_RADIUS = 28  # 24-32 recommended
```

### Modify Badge Size

Edit line 125:
```python
BADGE_SIZE = 52  # 48-56 recommended
```

### Change Font Sizes

Edit lines 111-116:
```python
FONT_HERO = lambda: load_font(130, bold=True)    # Lesson titles
FONT_H2 = lambda: load_font(52, bold=True)       # Slide titles
FONT_BODY_LARGE = lambda: load_font(19)          # Content
```

## File Output

### PNG Slides (57 files)
- **Naming**: `slide-01-startup.png` through `slide-57-startup.png`
- **Size**: ~30-50KB per file
- **Format**: PNG with transparency support
- **Resolution**: 1920x1080px (16:9)

### PDF Compilation
- **Filename**: `M0-Mindset-Module-STARTUP-STYLE.pdf`
- **Size**: ~2.5MB
- **Pages**: 57 slides in sequential order
- **Quality**: Optimized for screen and print

## System Requirements

- **Python**: 3.7 or higher
- **PIL/Pillow**: Image processing library
- **Fonts**: SF Pro Display or Helvetica Neue (macOS standard)
- **RAM**: Minimal (< 100MB during generation)
- **Disk space**: ~3MB for slides + 2.5MB for PDF

## Installation (if needed)

```bash
# Install Pillow if not already installed
pip3 install Pillow

# Or use requirements.txt if provided
pip3 install -r requirements.txt
```

## Generation Time

- **Per slide**: ~2-3 seconds
- **All 57 slides**: ~2-3 minutes
- **PDF compilation**: ~5-10 seconds

## Comparison with Other Styles

| Feature | Startup | Pitch Deck | Premium | Original |
|---------|---------|------------|---------|----------|
| Theme | Dual (light+dark) | Light only | Mixed | Light only |
| Cards | Rounded (28px) | Soft edges | Various | Rectangle |
| Badges | Circular numbered | None | Icons | None |
| Gradients | Radial soft | Organic soft | None | None |
| Feel | Modern startup | Airy presentation | Decorative | Executive minimal |

## When to Use This Style

### ✅ Perfect For:
- Startup pitch decks
- Investor presentations
- Modern tech company training
- Client-facing presentations
- Professional course materials
- Portfolio showcases

### ❌ Not Ideal For:
- Traditional corporate environments (use Original style)
- Decorative presentations (use Premium style)
- Ultra-minimal needs (use Pitch Deck style)

## Pro Tips

1. **Consistent branding**: Change accent color to match your brand
2. **Custom content**: Edit `slides_content` array for your own slides
3. **Print vs. Screen**: PDF optimized for both, PNGs best for digital
4. **Presentation mode**: Use PDF for seamless transitions
5. **Social media**: Export individual PNGs for social sharing

## Troubleshooting

### Issue: Fonts look different
**Solution**: macOS uses SF Pro Display automatically. On other systems, Helvetica Neue is used as fallback.

### Issue: Generation fails
**Solution**: Ensure Pillow is installed: `pip3 install Pillow`

### Issue: PDF compilation error
**Solution**: Check that all 57 PNG slides exist before compiling

### Issue: Text cutoff
**Solution**: Text is auto-wrapped. If issues persist, reduce bullet text length.

## Next Steps

1. **Generate slides**: Run `python3 generate_startup_slides.py`
2. **Review output**: Check slides 1, 10, 19 (dark titles) and 2, 11, 20 (content)
3. **Customize**: Adjust colors/fonts to match your brand
4. **Compile PDF**: Run `python3 compile_startup_to_pdf.py`
5. **Present**: Use PDF for presentations or PNGs for social media

## Documentation

- **Full docs**: See `STARTUP_STYLE_DOCUMENTATION.md` for complete guide
- **Design specs**: Detailed color, typography, and layout guidelines
- **Customization**: Advanced modification instructions
- **Technical**: Implementation details and API reference

## Support

For detailed documentation and advanced customization:
- Read `STARTUP_STYLE_DOCUMENTATION.md`
- Check `generate_startup_slides.py` inline comments
- Review slide type examples in code

---

**Ready to create stunning startup-style presentations!** 🚀

**Version**: 1.0
**Last Updated**: November 13, 2025
**Status**: Production Ready ✓
