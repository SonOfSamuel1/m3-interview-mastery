#!/usr/bin/env python3
"""
Generate ALL 24 M2-Reverse Attraction slides in Enhanced-WithGraphics style
Matches M0-Mindset Expanded premium design
"""

from PIL import Image, ImageDraw, ImageFont

print("\n" + "="*80)
print("GENERATING ALL 24 M2 - REVERSE ATTRACTION SLIDES")
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
    FONT_SUBTITLE = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 42)
    print("✓ Fonts loaded successfully\n")
except Exception as e:
    FONT_TITLE = FONT_TITLE_LARGE = FONT_BODY = FONT_BODY_BOLD = FONT_BODY_SMALL = FONT_SUBTITLE = ImageFont.load_default()
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

def gen_title_slide(title, num, subtitle=None):
    """Generate dark background title slide"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)

    # Title
    lines = wrap_text(title, FONT_TITLE_LARGE, WIDTH - (MARGIN * 2))
    start_y = (HEIGHT - len(lines) * 90) // 2

    # Add gold accent line above title
    draw.rectangle([(WIDTH - 200) // 2, start_y - 50, (WIDTH + 200) // 2, start_y - 46], fill=ACCENT_GOLD)

    # Draw title
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=FONT_TITLE_LARGE)
        x = (WIDTH - (bbox[2] - bbox[0])) // 2
        draw.text((x, start_y + i * 90), line, fill=TEXT_LIGHT, font=FONT_TITLE_LARGE)

    # Subtitle if provided
    if subtitle:
        sub_y = start_y + len(lines) * 90 + 40
        bbox = draw.textbbox((0, 0), subtitle, font=FONT_SUBTITLE)
        x = (WIDTH - (bbox[2] - bbox[0])) // 2
        draw.text((x, sub_y), subtitle, fill=TEXT_LIGHT, font=FONT_SUBTITLE)

    # Slide number
    draw.text((WIDTH - MARGIN - 50, HEIGHT - MARGIN - 30), str(num), fill=TEXT_LIGHT, font=FONT_BODY_SMALL)

    return img

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

    # Section 1
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

    # Section 2
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

def gen_video_placeholder_slide(title, subtitle, num):
    """Generate video placeholder slide"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_LIGHT)
    draw = ImageDraw.Draw(img)

    # Title
    bbox = draw.textbbox((0, 0), title, font=FONT_TITLE_LARGE)
    x = (WIDTH - (bbox[2] - bbox[0])) // 2
    y = (HEIGHT // 2) - 100
    draw.text((x, y), title, fill=TEXT_DARK, font=FONT_TITLE_LARGE)

    # Subtitle
    bbox = draw.textbbox((0, 0), subtitle, font=FONT_SUBTITLE)
    x = (WIDTH - (bbox[2] - bbox[0])) // 2
    draw.text((x, y + 100), subtitle, fill=TEXT_DARK, font=FONT_SUBTITLE)

    # Slide number
    draw.text((WIDTH - MARGIN - 50, HEIGHT - MARGIN - 30), str(num), fill=TEXT_DARK, font=FONT_BODY_SMALL)

    return img

# Complete slide content definitions
slides_content = {
    1: {
        "type": "title",
        "title": "Reverse Attraction"
    },
    2: {
        "type": "content",
        "title": "Overview",
        "bullets": [
            "In this module you will learn the exact steps you need to take to have hiring managers refer and/or interview for the high paying job opportunities you desire."
        ]
    },
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
    },
    8: {
        "type": "note",
        "note": "SLIDE 8: Contains embedded screenshot image - requires manual recreation or image integration"
    },
    9: {
        "type": "two_section",
        "title": "Sign-up For Linkedin Sales Navigator",
        "section1_title": "Purpose",
        "section1_bullets": [
            "Sales Navigator will supercharge your prospecting efforts for reaching out to hiring managers"
        ],
        "section2_title": "Cost",
        "section2_bullets": [
            "Sales Navigator provides a one month free trial to new subscribers (if you take the process seriously, you probably will only need one month of using this tool before you begin landing interviews)",
            "After 1-month trial, $80/mo for subscription"
        ]
    },
    10: {
        "type": "video_placeholder",
        "title": "Linkedin Sales Nav",
        "subtitle": "(Sign-up & Live Demo)"
    },
    11: {
        "type": "title",
        "title": "Create Your List of Hiring Managers"
    },
    12: {
        "type": "two_section",
        "title": "Creating Your List of Hiring Managers",
        "section1_title": "Purpose",
        "section1_bullets": [
            "Create a short list of managers with power who can hire you or refer you to a role to be hired for"
        ],
        "section2_title": "Action",
        "section2_bullets": [
            "Create Persona with following criteria:",
            "  Function: Sales, Business Development",
            "  Seniority Level: CXO, Vice President",
            "  Geography: North America",
            "  Name Persona: Active Offer- Hiring Manger List",
            "Workflow > People You Interacted with > Messaged > Excluded"
        ]
    },
    13: {
        "type": "two_section",
        "title": "Creating Your List of Hiring Managers",
        "section1_title": "Action (cont.)",
        "section1_bullets": [
            "Save search",
            "Re-name saved search for easy reference"
        ],
        "section2_title": "Optional",
        "section2_bullets": [
            "Turn on additional filters for more targeted messaging",
            "  Recent Update > Changed Jobs",
            "  (New leaders hire new AEs quickly when starting a new role)",
            "  Recent Update > Posted on Linkedin",
            "  (Shows they are active on Li and will respond to your message)",
            "  Recent Update > Mentioned in news",
            "  (Easy talking point in your outreach message, reference the article they were mentioned in)"
        ]
    },
    14: {
        "type": "video_placeholder",
        "title": "Insert Video",
        "subtitle": "(Me creating my list)"
    },
    15: {
        "type": "title",
        "title": "The Habit (v.1) Linkedin Method"
    },
    16: {
        "type": "two_section",
        "title": "The Habit",
        "section1_title": "Purpose",
        "section1_bullets": [
            "Getting interviewed for a high paying role is simply a numbers game at this point",
            "Establishing a simple habit of copy and pasting a standard outreach message for 30mins a will get you more interviews and connections than you know what to do with."
        ],
        "section2_title": "",
        "section2_bullets": []
    },
    17: {
        "type": "two_section",
        "title": "Understanding LI- Open Profile",
        "section1_title": "Purpose",
        "section1_bullets": [
            "Within LinkedIn there are people that you have to purchase InMail credits to message, but also those who you can message for free. Understanding the difference can help you leverage access to hundreds of hiring mangers."
        ],
        "section2_title": "",
        "section2_bullets": []
    },
    18: {
        "type": "note",
        "note": "SLIDE 18: Contains embedded screenshot with visual comparison - requires manual recreation"
    },
    19: {
        "type": "note",
        "note": "SLIDE 19: Contains embedded screenshot with visual comparison - requires manual recreation"
    },
    20: {
        "type": "video_placeholder",
        "title": "Insert Video",
        "subtitle": "(Me reviewing profiles for free open profile)"
    },
    21: {
        "type": "two_section",
        "title": "The Habit",
        "section1_title": "Refining Your Message",
        "section1_bullets": [
            "Open the Active Offer Scripts Playbook (page 6) to select one of the proven messages to use for the purposes of Hiring Manager Outreach",
            "Once you've selected your message, update with your name and any other relevant information that makes sense"
        ],
        "section2_title": "",
        "section2_bullets": []
    },
    22: {
        "type": "note",
        "note": "SLIDE 22: Contains embedded mobile screenshot of example message - requires manual recreation"
    },
    23: {
        "type": "content",
        "title": "The Habit",
        "bullets": [
            "Most Important Step:",
            "The most important step in this entire training is that you commit to doing the habit of sending out these outreach messages to your list",
            "30mins a day, no exceptions!",
            "Keep the habit going until you've secure the position you wanted."
        ]
    },
    24: {
        "type": "title",
        "title": "The Habit (v.2) Email Method"
    }
}

# Generate slides
print("Generating slides...\n")

for num in range(1, 25):
    content = slides_content.get(num)

    if not content:
        print(f"⚠ Slide {num}: No content defined")
        continue

    slide_type = content.get("type")

    if slide_type == "note":
        print(f"⚠ Slide {num}: {content['note']}")
        continue

    print(f"Generating Slide {num}...", end=" ")

    try:
        if slide_type == "title":
            img = gen_title_slide(content["title"], num, content.get("subtitle"))
        elif slide_type == "content":
            img = gen_content_slide(content["title"], content["bullets"], num)
        elif slide_type == "two_section":
            img = gen_two_section_slide(
                content["title"],
                content["section1_title"],
                content["section1_bullets"],
                content["section2_title"],
                content["section2_bullets"],
                num
            )
        elif slide_type == "video_placeholder":
            img = gen_video_placeholder_slide(content["title"], content["subtitle"], num)
        else:
            print(f"Unknown type: {slide_type}")
            continue

        # Save
        filename = f"{num}.png"
        img.save(filename, 'PNG')
        print(f"✓ Saved: {filename}")

    except Exception as e:
        print(f"✗ Error: {e}")

print("\n" + "="*80)
print("✓ GENERATION COMPLETE")
print("="*80)
print(f"\nGenerated text-based slides in Enhanced-WithGraphics style")
print(f"Location: M2- Reverse Attraction/")
print(f"\nSlides requiring manual work (contain embedded images):")
print(f"  - Slide 8: LinkedIn Sales Navigator screenshot")
print(f"  - Slide 18: Open Profile visual comparison (with checkmark/X)")
print(f"  - Slide 19: InMail vs Free messaging comparison")
print(f"  - Slide 22: Mobile screenshot of example message")
print(f"\nThese slides can be:")
print(f"  1. Recreated manually with design software")
print(f"  2. Left in original style (visual content is more important than design)")
print(f"  3. Replaced with text descriptions of the visuals")
print("="*80 + "\n")
