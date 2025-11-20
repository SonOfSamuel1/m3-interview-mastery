#!/usr/bin/env python3
"""
Generate updated M2-Reverse Attraction slides (3, 4, 5, 6, 7)
Matches Enhanced-WithGraphics design style from M0-Mindset Expanded
"""

from PIL import Image, ImageDraw, ImageFont

print("\n" + "="*80)
print("GENERATING M2 - REVERSE ATTRACTION UPDATED SLIDES")
print("Enhanced-WithGraphics Design Style")
print("="*80 + "\n")

# Configuration - Match Enhanced-WithGraphics exactly
WIDTH = 1920
HEIGHT = 1080
BG_LIGHT = (245, 245, 245)
BG_DARK = (26, 31, 46)
TEXT_DARK = (26, 31, 46)
TEXT_LIGHT = (255, 255, 255)
ACCENT_GOLD = (212, 175, 55)
MARGIN = 120

# Load fonts
try:
    FONT_TITLE = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 64)
    FONT_TITLE_LARGE = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 72)
    FONT_BODY = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 32)
    FONT_BODY_BOLD = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 32)
    FONT_BODY_SMALL = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 28)
    print("✓ Fonts loaded successfully\n")
except Exception as e:
    FONT_TITLE = FONT_TITLE_LARGE = FONT_BODY = FONT_BODY_BOLD = FONT_BODY_SMALL = ImageFont.load_default()
    print(f"⚠ Using default fonts (Arial not found: {e})\n")

# Helper functions
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

def gen_content_slide(title, bullets, num):
    """Generate light background content slide with gold bullets"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_LIGHT)
    draw = ImageDraw.Draw(img)

    # Title
    draw.text((MARGIN, MARGIN), title, fill=TEXT_DARK, font=FONT_TITLE)

    # Bullets
    y = MARGIN + 150
    bullet_indent = MARGIN + 50

    for bullet in bullets:
        # Draw gold bullet
        draw.ellipse([MARGIN, y + 12, MARGIN + 16, y + 28], fill=ACCENT_GOLD)

        # Wrap and draw bullet text
        lines = wrap_text(bullet, FONT_BODY, WIDTH - bullet_indent - MARGIN - 100)
        for i, line in enumerate(lines):
            draw.text((bullet_indent, y + i * 48), line, fill=TEXT_DARK, font=FONT_BODY)

        y += len(lines) * 48 + 30

    # Slide number (bottom right)
    draw.text((WIDTH - MARGIN - 50, HEIGHT - MARGIN - 30), str(num), fill=TEXT_DARK, font=FONT_BODY_SMALL)

    return img

def gen_two_section_slide(title, section1_title, section1_bullets, section2_title, section2_bullets, num):
    """Generate slide with two sections (Why/How format)"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_LIGHT)
    draw = ImageDraw.Draw(img)

    # Main title
    draw.text((MARGIN, MARGIN), title, fill=TEXT_DARK, font=FONT_TITLE)

    # Section 1 (Why)
    y = MARGIN + 150
    draw.text((MARGIN, y), section1_title, fill=TEXT_DARK, font=FONT_BODY_BOLD)
    y += 60

    bullet_indent = MARGIN + 50
    for bullet in section1_bullets:
        draw.ellipse([MARGIN, y + 12, MARGIN + 16, y + 28], fill=ACCENT_GOLD)
        lines = wrap_text(bullet, FONT_BODY, WIDTH - bullet_indent - MARGIN - 100)
        for i, line in enumerate(lines):
            draw.text((bullet_indent, y + i * 48), line, fill=TEXT_DARK, font=FONT_BODY)
        y += len(lines) * 48 + 25

    # Section 2 (How)
    y += 40
    draw.text((MARGIN, y), section2_title, fill=TEXT_DARK, font=FONT_BODY_BOLD)
    y += 60

    for bullet in section2_bullets:
        draw.ellipse([MARGIN, y + 12, MARGIN + 16, y + 28], fill=ACCENT_GOLD)
        lines = wrap_text(bullet, FONT_BODY, WIDTH - bullet_indent - MARGIN - 100)
        for i, line in enumerate(lines):
            draw.text((bullet_indent, y + i * 48), line, fill=TEXT_DARK, font=FONT_BODY)
        y += len(lines) * 48 + 25

    # Slide number
    draw.text((WIDTH - MARGIN - 50, HEIGHT - MARGIN - 30), str(num), fill=TEXT_DARK, font=FONT_BODY_SMALL)

    return img

# Slide content definitions
slides = {
    3: {
        "type": "content",
        "title": "Lesson Overview",
        "bullets": [
            "Resume Makeover",
            "Quick Cover Letter",
            "LinkedIn Profile Makeover",
            "LinkedIn Sales Navigator (Overview)",
            "Creating your List of Hiring Managers",
            "The Habit v.1 (Linkedin)",
            "The Habit v.2 (Email)"
        ]
    },
    4: {
        "type": "content",
        "title": "Foundation First: Why Profile Optimization Matters",
        "bullets": [
            "You can't attract what you haven't prepared to receive",
            "Hiring managers will review your profile before responding to outreach",
            "These three elements (Resume/LinkedIn/Cover Letter) form your professional foundation",
            "Complete these steps before executing the outreach habits",
            "Time Investment: 2-4 hours now saves months of ineffective outreach"
        ]
    },
    5: {
        "type": "two_section",
        "title": "Resume Makeover",
        "section1_title": "Why",
        "section1_bullets": [
            "Your resume content directly populates your LinkedIn profile's searchable fields",
            "Hiring managers search LinkedIn using specific keywords and job titles",
            "A keyword-optimized resume makes you discoverable in recruiter searches",
            "87% of recruiters use LinkedIn to find candidates - if you're not optimized, you're invisible"
        ],
        "section2_title": "How",
        "section2_bullets": [
            "Extract 15-20 keywords from your target job descriptions (titles, skills, tools)",
            "Place top keywords in your headline, summary, and most recent role",
            "Quantify achievements with specific metrics (%, $, #)",
            "Remove outdated skills and irrelevant experience (keep last 10-15 years)",
            "Add certifications and relevant training to skills section",
            "Request 3-5 LinkedIn recommendations from former managers/clients",
            "Ensure profile completion is 100% (LinkedIn's All-Star status)"
        ]
    },
    6: {
        "type": "two_section",
        "title": "Quick Cover Letter",
        "section1_title": "Why",
        "section1_bullets": [
            "Hiring managers may request a cover letter before scheduling interviews",
            "A strong cover letter reinforces your value proposition from LinkedIn conversations",
            "Differentiates you from candidates who only submit generic applications",
            "Demonstrates communication skills and professionalism hiring managers value"
        ],
        "section2_title": "How",
        "section2_bullets": [
            "Opening: Reference your LinkedIn conversation with the hiring manager by name",
            "Paragraph 1: State the specific role and why their company/team excites you",
            "Paragraph 2: Highlight 2-3 relevant achievements that match their needs",
            "Paragraph 3: Address how you'll solve their specific challenge (from conversation)",
            "Closing: Reinforce enthusiasm and propose next steps",
            "Keep it brief: 3-4 short paragraphs, 250-300 words maximum"
        ]
    },
    7: {
        "type": "two_section",
        "title": "LinkedIn Profile Makeover",
        "section1_title": "Why",
        "section1_bullets": [
            "Hiring managers validate your claims by reviewing your profile",
            "A polished profile reinforces everything you said in your outreach message",
            "Incomplete or outdated profiles create doubt about your professionalism",
            "Your profile should answer questions before hiring managers ask them"
        ],
        "section2_title": "How",
        "section2_bullets": [
            "Headline Formula: [Job Title] Helping [Target Industry] [Achieve Specific Result]",
            "About Section: Start with your unique value, not job history",
            "Experience Bullets: Lead with metrics (%, $, #) then explain how",
            "Skills Endorsements: Ask 5-10 connections to endorse your top skills",
            "Activity: Post or comment 2-3x/week to stay visible in feeds",
            "Creator Mode: Enable to increase visibility and add newsletter option",
            "Custom URL: linkedin.com/in/yourname (not random numbers)"
        ]
    }
}

# Generate slides
print("Generating slides...\n")

for num, content in slides.items():
    print(f"Generating Slide {num}: {content['title']}")

    if content["type"] == "content":
        img = gen_content_slide(content["title"], content["bullets"], num)
    elif content["type"] == "two_section":
        img = gen_two_section_slide(
            content["title"],
            content["section1_title"],
            content["section1_bullets"],
            content["section2_title"],
            content["section2_bullets"],
            num
        )

    # Save with leading zero for single digits
    filename = f"{num}.png"
    img.save(filename, 'PNG')
    print(f"  ✓ Saved: {filename}")

print("\n" + "="*80)
print("✓ GENERATION COMPLETE")
print("="*80)
print(f"\nGenerated 5 slides (3-7) in Enhanced-WithGraphics style")
print(f"Location: M2- Reverse Attraction/")
print(f"\nNext steps:")
print(f"1. Renumber existing slides 4-25 → 5-26")
print(f"2. Replace old slides 4, 5, 6 with new 5, 6, 7")
print(f"3. Insert new slide 4 (Foundation First)")
print(f"4. Update slide 3 (Lesson Overview)")
print("="*80 + "\n")
