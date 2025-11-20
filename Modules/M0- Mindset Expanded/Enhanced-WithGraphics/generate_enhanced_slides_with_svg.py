#!/usr/bin/env python3
"""
Enhanced Slide Generator with Custom SVG Vector Graphics
Integrates premium custom SVG graphics into Executive Minimalism slides
"""

from PIL import Image, ImageDraw, ImageFont
import cairosvg
import io
import sys
import os

# Import SVG graphics library
from svg_graphics_library import SVG_LIBRARY

# Image dimensions
WIDTH = 1920
HEIGHT = 1080

# Concept A: Executive Minimalism Colors
BG_LIGHT = (245, 245, 245)
BG_DARK = (26, 31, 46)
TEXT_DARK = (26, 31, 46)
TEXT_LIGHT = (255, 255, 255)
ACCENT_GOLD = (212, 175, 55)

# Load fonts
try:
    FONT_TITLE = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 64)
    FONT_TITLE_LARGE = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 72)
    FONT_BODY = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 32)
    FONT_BODY_BOLD = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 32)
    FONT_BODY_SMALL = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 28)
except:
    FONT_TITLE = FONT_TITLE_LARGE = FONT_BODY = FONT_BODY_BOLD = FONT_BODY_SMALL = ImageFont.load_default()

MARGIN = 120


def svg_to_pil_image(svg_code):
    """Convert SVG code to PIL Image with transparency"""
    png_data = cairosvg.svg2png(bytestring=svg_code.encode('utf-8'))
    return Image.open(io.BytesIO(png_data))


def paste_svg_icon(img, icon_name, x, y, size=100):
    """Paste an SVG icon onto an image at specified coordinates"""
    if icon_name not in SVG_LIBRARY:
        print(f"Warning: Icon '{icon_name}' not found in library")
        return

    try:
        svg_code = SVG_LIBRARY[icon_name](size=size)
        svg_img = svg_to_pil_image(svg_code)

        # Paste with transparency
        if svg_img.mode == 'RGBA':
            img.paste(svg_img, (x, y), svg_img)
        else:
            img.paste(svg_img, (x, y))
    except Exception as e:
        print(f"Warning: Could not paste icon '{icon_name}': {e}")


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


def create_title_slide(title_text, slide_num, icon_name=None):
    """Create a title/section slide with dark background and optional icon"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)

    lines = wrap_text(title_text, FONT_TITLE_LARGE, WIDTH - (MARGIN * 2))
    line_height = 90
    total_height = len(lines) * line_height
    start_y = (HEIGHT - total_height) // 2

    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=FONT_TITLE_LARGE)
        text_width = bbox[2] - bbox[0]
        x = (WIDTH - text_width) // 2
        y = start_y + (i * line_height)
        draw.text((x, y), line, fill=TEXT_LIGHT, font=FONT_TITLE_LARGE)

    # Gold accent line
    accent_width = 200
    accent_x = (WIDTH - accent_width) // 2
    accent_y = start_y - 50
    draw.rectangle([accent_x, accent_y, accent_x + accent_width, accent_y + 4], fill=ACCENT_GOLD)

    # Optional icon
    if icon_name:
        paste_svg_icon(img, icon_name, WIDTH - MARGIN - 150, MARGIN, size=120)

    # Slide number
    draw.text((WIDTH - MARGIN - 50, HEIGHT - MARGIN - 30), f"{slide_num}", fill=TEXT_LIGHT, font=FONT_BODY_SMALL)

    return img


def create_content_slide(title, bullets, slide_num, icon_name=None, icon_position="top_right"):
    """Create standard content slide with bullets and optional icon"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_LIGHT)
    draw = ImageDraw.Draw(img)

    draw.text((MARGIN, MARGIN), title, fill=TEXT_DARK, font=FONT_TITLE)

    # Add icon
    if icon_name:
        if icon_position == "top_right":
            paste_svg_icon(img, icon_name, WIDTH - MARGIN - 150, MARGIN, size=120)
        elif icon_position == "center":
            paste_svg_icon(img, icon_name, (WIDTH - 200) // 2, MARGIN + 200, size=200)
        elif icon_position == "bottom_center":
            paste_svg_icon(img, icon_name, (WIDTH - 300) // 2, HEIGHT - MARGIN - 350, size=300)

    # Draw bullets
    y_offset = MARGIN + 150
    bullet_spacing = 60

    for bullet in bullets:
        lines = wrap_text(bullet, FONT_BODY, WIDTH - MARGIN - 200)
        draw.ellipse([MARGIN, y_offset + 10, MARGIN + 12, y_offset + 22], fill=ACCENT_GOLD)

        for line in lines:
            draw.text((MARGIN + 30, y_offset), line, fill=TEXT_DARK, font=FONT_BODY)
            y_offset += 45

        y_offset += bullet_spacing - 45

    draw.text((WIDTH - MARGIN - 50, HEIGHT - MARGIN - 30), f"{slide_num}", fill=TEXT_DARK, font=FONT_BODY_SMALL)

    return img


def create_comparison_slide(title, old_beliefs, new_beliefs, slide_num):
    """Create split-screen comparison slide"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_LIGHT)
    draw = ImageDraw.Draw(img)

    draw.text((MARGIN, MARGIN), title, fill=TEXT_DARK, font=FONT_TITLE)

    center_x = WIDTH // 2
    draw.line([center_x, MARGIN + 150, center_x, HEIGHT - MARGIN], fill=ACCENT_GOLD, width=3)

    # Left side (OLD)
    left_x = MARGIN
    left_y = MARGIN + 200
    draw.text((left_x, left_y), "OLD BELIEFS:", fill=ACCENT_GOLD, font=FONT_BODY_BOLD)

    y_offset = left_y + 60
    for belief in old_beliefs:
        lines = wrap_text(belief, FONT_BODY_SMALL, center_x - MARGIN - 60)
        for line in lines:
            draw.text((left_x, y_offset), line, fill=TEXT_DARK, font=FONT_BODY_SMALL)
            y_offset += 40
        y_offset += 30

    # Right side (NEW)
    right_x = center_x + 60
    right_y = MARGIN + 200
    draw.text((right_x, right_y), "NEW BELIEFS:", fill=ACCENT_GOLD, font=FONT_BODY_BOLD)

    y_offset = right_y + 60
    for belief in new_beliefs:
        lines = wrap_text(belief, FONT_BODY_SMALL, WIDTH - right_x - MARGIN)
        for line in lines:
            draw.text((right_x, y_offset), line, fill=TEXT_DARK, font=FONT_BODY_SMALL)
            y_offset += 40
        y_offset += 30

    # Arrow icon
    paste_svg_icon(img, 'arrow_up', center_x - 15, MARGIN + 400, size=30)

    draw.text((WIDTH - MARGIN - 50, HEIGHT - MARGIN - 30), f"{slide_num}", fill=TEXT_DARK, font=FONT_BODY_SMALL)

    return img


def create_framework_slide(title, pillars, pillar_content, slide_num):
    """Create three-pillar framework slide"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_LIGHT)
    draw = ImageDraw.Draw(img)

    draw.text((MARGIN, MARGIN), title, fill=TEXT_DARK, font=FONT_TITLE)

    start_y = MARGIN + 220
    box_width = 450
    box_height = 500
    spacing = 60

    total_width = (box_width * 3) + (spacing * 2)
    start_x = (WIDTH - total_width) // 2

    for i in range(3):
        box_x = start_x + (i * (box_width + spacing))

        draw.rectangle([box_x, start_y, box_x + box_width, start_y + box_height],
                      outline=ACCENT_GOLD, width=3)

        # Pillar icon
        icon_x = box_x + (box_width - 60) // 2
        paste_svg_icon(img, 'pillar', icon_x, start_y - 40, size=60)

        # Pillar label
        label = pillars[i]
        bbox = draw.textbbox((0, 0), label, font=FONT_BODY_BOLD)
        label_width = bbox[2] - bbox[0]
        label_x = box_x + (box_width - label_width) // 2
        draw.text((label_x, start_y + 30), label, fill=ACCENT_GOLD, font=FONT_BODY_BOLD)

        # Content
        content_y = start_y + 100
        for item in pillar_content[i]:
            lines = wrap_text(item, FONT_BODY_SMALL, box_width - 60)
            for line in lines:
                draw.text((box_x + 30, content_y), f"• {line}", fill=TEXT_DARK, font=FONT_BODY_SMALL)
                content_y += 40
            content_y += 15

    draw.text((WIDTH - MARGIN - 50, HEIGHT - MARGIN - 30), f"{slide_num}", fill=TEXT_DARK, font=FONT_BODY_SMALL)

    return img


def create_timeline_slide(title, days, activities, slide_num):
    """Create weekly timeline slide"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_LIGHT)
    draw = ImageDraw.Draw(img)

    draw.text((MARGIN, MARGIN), title, fill=TEXT_DARK, font=FONT_TITLE)

    # Calendar icon
    paste_svg_icon(img, 'calendar', WIDTH - MARGIN - 120, MARGIN, size=100)

    start_y = MARGIN + 200
    day_height = 85

    for i, (day, activity) in enumerate(zip(days, activities)):
        y_pos = start_y + (i * day_height)

        # Checkmark for each day
        paste_svg_icon(img, 'checkmark', MARGIN - 10, y_pos, size=30)

        draw.text((MARGIN + 30, y_pos), day, fill=ACCENT_GOLD, font=FONT_BODY_BOLD)

        activity_x = MARGIN + 300
        lines = wrap_text(activity, FONT_BODY, WIDTH - activity_x - MARGIN)
        for line in lines:
            draw.text((activity_x, y_pos), line, fill=TEXT_DARK, font=FONT_BODY)
            y_pos += 40

        if i < len(days) - 1:
            line_y = start_y + ((i + 1) * day_height) - 10
            draw.line([MARGIN + 15, line_y - 15, MARGIN + 15, line_y], fill=ACCENT_GOLD, width=2)

    draw.text((WIDTH - MARGIN - 50, HEIGHT - MARGIN - 30), f"{slide_num}", fill=TEXT_DARK, font=FONT_BODY_SMALL)

    return img


def create_cycle_diagram_slide(title, bullets, slide_num):
    """Create slide with confidence-action cycle graphic"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_LIGHT)
    draw = ImageDraw.Draw(img)

    draw.text((MARGIN, MARGIN), title, fill=TEXT_DARK, font=FONT_TITLE)

    y_offset = MARGIN + 150
    bullet_spacing = 60

    for bullet in bullets[:3]:
        lines = wrap_text(bullet, FONT_BODY, (WIDTH // 2) - MARGIN - 100)
        draw.ellipse([MARGIN, y_offset + 10, MARGIN + 12, y_offset + 22], fill=ACCENT_GOLD)

        for line in lines:
            draw.text((MARGIN + 30, y_offset), line, fill=TEXT_DARK, font=FONT_BODY)
            y_offset += 45
        y_offset += bullet_spacing - 45

    # Cycle arrows graphic
    cycle_x = WIDTH - MARGIN - 350
    cycle_y = MARGIN + 250
    paste_svg_icon(img, 'cycle_arrows', cycle_x, cycle_y, size=300)

    y_offset = cycle_y + 350
    for bullet in bullets[3:]:
        lines = wrap_text(bullet, FONT_BODY, WIDTH - MARGIN - 200)
        draw.ellipse([MARGIN, y_offset + 10, MARGIN + 12, y_offset + 22], fill=ACCENT_GOLD)

        for line in lines:
            draw.text((MARGIN + 30, y_offset), line, fill=TEXT_DARK, font=FONT_BODY)
            y_offset += 45
        y_offset += bullet_spacing - 45

    draw.text((WIDTH - MARGIN - 50, HEIGHT - MARGIN - 30), f"{slide_num}", fill=TEXT_DARK, font=FONT_BODY_SMALL)

    return img


print("Generating enhanced slides with custom SVG graphics...")
print("This script requires the virtual environment. Run with:")
print("source ../.venv/bin/activate && python3 generate_enhanced_slides_with_svg.py")
