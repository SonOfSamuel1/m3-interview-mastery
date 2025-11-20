#!/usr/bin/env python3
"""
Generate slides 8, 18, 19, 22 with image placeholders
These slides will have the Enhanced-WithGraphics design with designated areas for images
"""

from PIL import Image, ImageDraw, ImageFont

print("\n" + "="*80)
print("GENERATING IMAGE PLACEHOLDER SLIDES (8, 18, 19, 22)")
print("Enhanced-WithGraphics Design with Clear Image Insertion Areas")
print("="*80 + "\n")

# Configuration
WIDTH = 1920
HEIGHT = 1080
BG_LIGHT = (245, 245, 245)
BG_DARK = (26, 31, 46)
TEXT_DARK = (26, 31, 46)
TEXT_LIGHT = (255, 255, 255)
ACCENT_GOLD = (212, 175, 55)
PLACEHOLDER_BG = (220, 220, 220)  # Slightly darker gray for image areas
PLACEHOLDER_BORDER = (212, 175, 55)  # Gold border
MARGIN = 120

# Load fonts
try:
    FONT_TITLE = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 64)
    FONT_BODY = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 32)
    FONT_BODY_BOLD = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 32)
    FONT_BODY_SMALL = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 28)
    FONT_PLACEHOLDER = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 36)
    print("✓ Fonts loaded successfully\n")
except Exception as e:
    FONT_TITLE = FONT_BODY = FONT_BODY_BOLD = FONT_BODY_SMALL = FONT_PLACEHOLDER = ImageFont.load_default()
    print(f"⚠ Using default fonts: {e}\n")

def wrap_text(text, font, max_width):
    """Wrap text to fit within max_width"""
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = ImageDraw.Draw(Image.new('RGB', (1, 1))).textbbox((0, 0), test_line, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line))

    return lines

def draw_image_placeholder(draw, x, y, width, height, label):
    """Draw a clearly marked image placeholder area"""
    # Draw placeholder background
    draw.rectangle([x, y, x + width, y + height], fill=PLACEHOLDER_BG)

    # Draw gold border
    border_width = 4
    draw.rectangle([x, y, x + width, y + height], outline=PLACEHOLDER_BORDER, width=border_width)

    # Draw diagonal lines (crosshatch pattern)
    step = 40
    for i in range(0, width + height, step):
        # Top-left to bottom-right
        draw.line([(x + i, y), (x, y + i)], fill=ACCENT_GOLD, width=2)
        # Top-right to bottom-left
        draw.line([(x + width - i, y), (x + width, y + i)], fill=ACCENT_GOLD, width=2)

    # Draw label text
    label_lines = wrap_text(label, FONT_PLACEHOLDER, width - 40)
    label_height = len(label_lines) * 50
    label_y = y + (height - label_height) // 2

    for i, line in enumerate(label_lines):
        bbox = draw.textbbox((0, 0), line, font=FONT_PLACEHOLDER)
        text_width = bbox[2] - bbox[0]
        text_x = x + (width - text_width) // 2
        draw.text((text_x, label_y + i * 50), line, fill=ACCENT_GOLD, font=FONT_PLACEHOLDER)

# SLIDE 8: LinkedIn Sales Navigator Screenshot
def gen_slide_8():
    """LinkedIn Sales Navigator (Overview) with screenshot placeholder"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_LIGHT)
    draw = ImageDraw.Draw(img)

    # Title
    draw.text((MARGIN, MARGIN), "LinkedIn Sales Navigator (Overview)", fill=TEXT_DARK, font=FONT_TITLE)

    # Image placeholder for screenshot
    placeholder_width = WIDTH - (MARGIN * 2)
    placeholder_height = 600
    placeholder_y = MARGIN + 200

    draw_image_placeholder(
        draw,
        MARGIN,
        placeholder_y,
        placeholder_width,
        placeholder_height,
        "[INSERT SCREENSHOT: LinkedIn Sales Navigator Dashboard]"
    )

    # Instruction text below
    instruction_y = placeholder_y + placeholder_height + 30
    draw.text((MARGIN, instruction_y),
              "Recommended screenshot: Sales Navigator dashboard showing key features and navigation",
              fill=TEXT_DARK, font=FONT_BODY_SMALL)

    # Slide number
    draw.text((WIDTH - MARGIN - 50, HEIGHT - MARGIN - 30), "8", fill=TEXT_DARK, font=FONT_BODY_SMALL)

    return img

# SLIDE 18: Open Profile Visual Comparison
def gen_slide_18():
    """Understanding LI- Open Profile with gold icon visual"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_LIGHT)
    draw = ImageDraw.Draw(img)

    # Title
    draw.text((MARGIN, MARGIN), "Understanding LI- Open Profile", fill=TEXT_DARK, font=FONT_TITLE)

    # Subtitle
    draw.text((MARGIN, MARGIN + 100), "Gold LinkedIn Indicator", fill=TEXT_DARK, font=FONT_BODY_BOLD)

    # Left side: Text content
    left_bullets = [
        "As you're sorting through your list look for profiles with the gold icon next to their name.",
        "The icon indicates that you may be able to message them freely without have to use InMail"
    ]

    y = MARGIN + 180
    bullet_indent = MARGIN + 50

    for bullet in left_bullets:
        draw.ellipse([MARGIN, y + 12, MARGIN + 16, y + 28], fill=ACCENT_GOLD)
        lines = wrap_text(bullet, FONT_BODY, 700)
        for i, line in enumerate(lines):
            draw.text((bullet_indent, y + i * 48), line, fill=TEXT_DARK, font=FONT_BODY)
        y += len(lines) * 48 + 30

    # Right side: Image placeholder for comparison visual
    placeholder_x = MARGIN + 850
    placeholder_y = MARGIN + 180
    placeholder_width = 950
    placeholder_height = 400

    draw_image_placeholder(
        draw,
        placeholder_x,
        placeholder_y,
        placeholder_width,
        placeholder_height,
        "[INSERT IMAGE: LinkedIn profile showing gold 'Open Profile' icon with checkmark]"
    )

    # Instruction text
    instruction_y = placeholder_y + placeholder_height + 20
    draw.text((placeholder_x, instruction_y),
              "Recommended: Screenshot showing profile WITH gold icon indicator",
              fill=TEXT_DARK, font=FONT_BODY_SMALL)

    # Slide number
    draw.text((WIDTH - MARGIN - 50, HEIGHT - MARGIN - 30), "18", fill=TEXT_DARK, font=FONT_BODY_SMALL)

    return img

# SLIDE 19: InMail vs Free Messaging Comparison
def gen_slide_19():
    """Understanding LI- Open Profile with side-by-side comparison"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_LIGHT)
    draw = ImageDraw.Draw(img)

    # Title
    draw.text((MARGIN, MARGIN), "Understanding LI- Open Profile", fill=TEXT_DARK, font=FONT_TITLE)

    # Left side text
    left_bullets = [
        "Roughly 20% of all hiring managers' profiles will be \"Free to Open Profile\"",
        "Remember that all you need is a single persons to say \"yes\" to land a job making $100k more than what you're making today!"
    ]

    y = MARGIN + 180
    bullet_indent = MARGIN + 50

    for bullet in left_bullets:
        draw.ellipse([MARGIN, y + 12, MARGIN + 16, y + 28], fill=ACCENT_GOLD)
        lines = wrap_text(bullet, FONT_BODY, 650)
        for i, line in enumerate(lines):
            draw.text((bullet_indent, y + i * 48), line, fill=TEXT_DARK, font=FONT_BODY)
        y += len(lines) * 48 + 35

    # Right side: Two image placeholders (side by side with VS)
    placeholder_base_x = MARGIN + 800
    placeholder_y = MARGIN + 180
    placeholder_width = 450
    placeholder_height = 450

    # Left image placeholder (X - requires InMail)
    draw_image_placeholder(
        draw,
        placeholder_base_x,
        placeholder_y,
        placeholder_width,
        placeholder_height,
        "[INSERT IMAGE: Message showing 'Using 1 of 150 InMail' with X mark]"
    )

    # VS text
    vs_x = placeholder_base_x + placeholder_width + 30
    vs_y = placeholder_y + placeholder_height // 2 - 30
    draw.text((vs_x, vs_y), "vs", fill=ACCENT_GOLD, font=FONT_TITLE)

    # Right image placeholder (✓ - Free to Open Profile)
    placeholder2_x = vs_x + 100
    draw_image_placeholder(
        draw,
        placeholder2_x,
        placeholder_y,
        placeholder_width,
        placeholder_height,
        "[INSERT IMAGE: Message showing 'Free to Open Profile' with checkmark]"
    )

    # Instruction text
    instruction_y = placeholder_y + placeholder_height + 20
    draw.text((placeholder_base_x, instruction_y),
              "Recommended: Side-by-side LinkedIn message compose windows showing InMail cost vs Free",
              fill=TEXT_DARK, font=FONT_BODY_SMALL)

    # Slide number
    draw.text((WIDTH - MARGIN - 50, HEIGHT - MARGIN - 30), "19", fill=TEXT_DARK, font=FONT_BODY_SMALL)

    return img

# SLIDE 22: Example Message Mobile Screenshot
def gen_slide_22():
    """The Habit - Example Message with mobile screenshot placeholder"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_LIGHT)
    draw = ImageDraw.Draw(img)

    # Title
    draw.text((MARGIN, MARGIN), "The Habit", fill=TEXT_DARK, font=FONT_TITLE)

    # Subtitle
    draw.text((MARGIN, MARGIN + 100), "Example Message", fill=TEXT_DARK, font=FONT_BODY_BOLD)

    # Left side: Text content
    y = MARGIN + 180
    bullet_indent = MARGIN + 50

    bullet_text = "Here is an example of the exact message I used to land a job at Salesforce making $90k more than my previous role."

    draw.ellipse([MARGIN, y + 12, MARGIN + 16, y + 28], fill=ACCENT_GOLD)
    lines = wrap_text(bullet_text, FONT_BODY, 750)
    for i, line in enumerate(lines):
        draw.text((bullet_indent, y + i * 48), line, fill=TEXT_DARK, font=FONT_BODY)

    # Right side: Mobile phone screenshot placeholder
    placeholder_x = MARGIN + 900
    placeholder_y = MARGIN + 150
    placeholder_width = 500
    placeholder_height = 700

    draw_image_placeholder(
        draw,
        placeholder_x,
        placeholder_y,
        placeholder_width,
        placeholder_height,
        "[INSERT IMAGE: Mobile phone mockup showing LinkedIn message]"
    )

    # Instruction text
    instruction_y = placeholder_y + placeholder_height + 20
    draw.text((placeholder_x, instruction_y),
              "Recommended: Mobile phone screenshot of LinkedIn message conversation",
              fill=TEXT_DARK, font=FONT_BODY_SMALL)

    # Slide number
    draw.text((WIDTH - MARGIN - 50, HEIGHT - MARGIN - 30), "22", fill=TEXT_DARK, font=FONT_BODY_SMALL)

    return img

# Generate all four slides
slides_to_generate = {
    8: gen_slide_8,
    18: gen_slide_18,
    19: gen_slide_19,
    22: gen_slide_22
}

print("Generating image placeholder slides...\n")

for num, gen_func in slides_to_generate.items():
    print(f"Generating Slide {num}...", end=" ")
    try:
        img = gen_func()
        filename = f"{num}.png"
        img.save(filename, 'PNG')
        print(f"✓ Saved: {filename}")
    except Exception as e:
        print(f"✗ Error: {e}")

print("\n" + "="*80)
print("✓ IMAGE PLACEHOLDER SLIDES GENERATED")
print("="*80)
print(f"\nCreated 4 slides with clear image insertion areas:")
print(f"  - Slide 8: LinkedIn Sales Navigator dashboard placeholder")
print(f"  - Slide 18: Gold icon indicator comparison placeholder")
print(f"  - Slide 19: InMail vs Free messaging side-by-side placeholders")
print(f"  - Slide 22: Mobile phone message screenshot placeholder")
print(f"\nEach placeholder has:")
print(f"  ✓ Gold border for easy identification")
print(f"  ✓ Crosshatch pattern to show it's a placeholder")
print(f"  ✓ Clear label describing what image to insert")
print(f"  ✓ Instruction text below for guidance")
print(f"\nTo insert images:")
print(f"  1. Open slide PNG in image editor (Photoshop, Figma, Canva)")
print(f"  2. Delete or mask the placeholder area")
print(f"  3. Insert your screenshot/image")
print(f"  4. Align to match the placeholder dimensions")
print(f"  5. Export as PNG at 1920x1080")
print("="*80 + "\n")
