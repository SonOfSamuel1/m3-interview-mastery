#!/usr/bin/env python3
"""
Generate professional slides for Active Offer M0- Course Intro Module
Brand Style: Minimalist, clean, black text on light gray background
Output: 1920x1080 PNG files at 16:9 aspect ratio
"""

from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

# Brand Colors
BACKGROUND_COLOR = "#F5F5F5"
TEXT_COLOR = "#000000"

# Slide dimensions (1920x1080 - 16:9 aspect ratio)
SLIDE_WIDTH = 1920
SLIDE_HEIGHT = 1080

# Typography settings
TITLE_FONT_SIZE = 120
SUBTITLE_FONT_SIZE = 80
BODY_FONT_SIZE = 52
SMALL_FONT_SIZE = 44

# Layout settings
LEFT_MARGIN = 100
RIGHT_MARGIN = 100
TOP_MARGIN = 80
BULLET_INDENT = 60
LINE_SPACING = 1.4

def wrap_text(text, font, max_width):
    """Wrap text to fit within max_width"""
    lines = []
    words = text.split()
    current_line = []

    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = font.getbbox(test_line)
        width = bbox[2] - bbox[0]

        if width <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line))

    return lines

def create_title_slide(title, subtitle=None):
    """Create a centered title slide"""
    img = Image.new('RGB', (SLIDE_WIDTH, SLIDE_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    # Load fonts (using system fonts)
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", TITLE_FONT_SIZE)
    except:
        title_font = ImageFont.load_default()

    # Draw title (centered)
    title_lines = wrap_text(title, title_font, SLIDE_WIDTH - 200)

    # Calculate total height for vertical centering
    line_height = int(TITLE_FONT_SIZE * LINE_SPACING)
    total_height = len(title_lines) * line_height

    if subtitle:
        try:
            subtitle_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", SUBTITLE_FONT_SIZE)
        except:
            subtitle_font = ImageFont.load_default()
        subtitle_lines = wrap_text(subtitle, subtitle_font, SLIDE_WIDTH - 200)
        total_height += len(subtitle_lines) * int(SUBTITLE_FONT_SIZE * LINE_SPACING) + 60

    # Start position for centered text
    y = (SLIDE_HEIGHT - total_height) // 2

    # Draw title lines
    for line in title_lines:
        bbox = title_font.getbbox(line)
        text_width = bbox[2] - bbox[0]
        x = (SLIDE_WIDTH - text_width) // 2
        draw.text((x, y), line, fill=TEXT_COLOR, font=title_font)
        y += line_height

    # Draw subtitle if provided
    if subtitle:
        y += 60
        for line in subtitle_lines:
            bbox = subtitle_font.getbbox(line)
            text_width = bbox[2] - bbox[0]
            x = (SLIDE_WIDTH - text_width) // 2
            draw.text((x, y), line, fill=TEXT_COLOR, font=subtitle_font)
            y += int(SUBTITLE_FONT_SIZE * LINE_SPACING)

    return img

def create_content_slide(title, bullets, small_bullets=False):
    """Create a content slide with title and bullet points"""
    img = Image.new('RGB', (SLIDE_WIDTH, SLIDE_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    # Load fonts
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", SUBTITLE_FONT_SIZE)
        bullet_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", SMALL_FONT_SIZE if small_bullets else BODY_FONT_SIZE)
    except:
        title_font = ImageFont.load_default()
        bullet_font = ImageFont.load_default()

    # Draw title
    y = TOP_MARGIN
    title_lines = wrap_text(title, title_font, SLIDE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN)
    for line in title_lines:
        draw.text((LEFT_MARGIN, y), line, fill=TEXT_COLOR, font=title_font)
        y += int(SUBTITLE_FONT_SIZE * LINE_SPACING)

    y += 60  # Space after title

    # Draw bullets
    max_text_width = SLIDE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN - BULLET_INDENT - 40
    font_size = SMALL_FONT_SIZE if small_bullets else BODY_FONT_SIZE
    line_height = int(font_size * LINE_SPACING)

    for bullet in bullets:
        # Draw bullet point
        draw.text((LEFT_MARGIN, y), "•", fill=TEXT_COLOR, font=bullet_font)

        # Wrap and draw bullet text
        bullet_lines = wrap_text(bullet, bullet_font, max_text_width)
        for i, line in enumerate(bullet_lines):
            x_offset = LEFT_MARGIN + BULLET_INDENT if i == 0 else LEFT_MARGIN + BULLET_INDENT
            draw.text((x_offset, y), line, fill=TEXT_COLOR, font=bullet_font)
            y += line_height

        y += 20  # Space between bullets

    return img

# Define all slide content for Course Intro
slides_content = [
    # Slide 1: Welcome
    {
        "type": "title",
        "title": "Welcome to Active Offer"
    },
    {
        "type": "content",
        "title": "Welcome to Active Offer",
        "bullets": [
            "Congratulations on investing in your $200k-$500k+ career transformation",
            "You've joined an exclusive community of elite sales professionals",
            "Your decision to be here separates you from 99% of sales professionals",
            "This program works - when you implement the systems, results follow"
        ]
    },
    # Slide 2: Transformation Journey
    {
        "type": "content",
        "title": "Your Transformation Journey",
        "bullets": [
            "From: Talented sales professional undervalued in the market",
            "To: Commanding $200k-$500k+ offers with confidence and clarity",
            "Timeline: 8-12 weeks of focused implementation",
            "Method: Proven systems used by top 1% earners in sales leadership",
            "Your role: Show up, implement, and execute the frameworks"
        ]
    },
    # Slide 3: Course Overview (Original Slide 1 - Updated)
    {
        "type": "content",
        "title": "Course Overview",
        "bullets": [
            "6 sequential modules: Mindset → Profile Matching → Reverse Attraction → Interview Mastery → Negotiation → Storytelling",
            "3-5 hours per week recommended (8-10 weeks total)",
            "Video lessons, templates, case studies, and implementation exercises",
            "Progress unlocks: Complete each module to access the next"
        ]
    },
    # Slide 4: How This Course Works
    {
        "type": "content",
        "title": "How This Course Works",
        "bullets": [
            "Focused video lessons: 5-10 minutes of actionable content per lesson",
            "Implementation first: Every module includes hands-on exercises",
            "Real-world application: Case studies from successful graduates",
            "Template library: Copy-paste resources to accelerate execution",
            "Sequential mastery: Each module builds on the previous",
            "No busywork: Every exercise directly impacts your job search outcomes"
        ],
        "small_bullets": True
    },
    # Slide 5: Your Weekly Commitment
    {
        "type": "content",
        "title": "Your Weekly Commitment",
        "bullets": [
            "Recommended pace: 1 module per week (6 weeks total)",
            "Weekly time investment: 3-5 hours (lessons + implementation)",
            "Best schedule: Three 60-90 minute focused sessions per week",
            "Flexibility: Self-paced with 12-month access",
            "Realistic timeline: Most working professionals complete in 8-10 weeks",
            "Block your calendar now: Consistency beats intensity"
        ],
        "small_bullets": True
    },
    # Slide 6: Measuring Your Success
    {
        "type": "content",
        "title": "Measuring Your Success",
        "bullets": [
            "Module completion: 6/6 modules finished with checkpoints passed",
            "Activity metrics: Interview requests, callbacks, offers received",
            "Quality indicators: Decision-maker connections, networking conversations",
            "Financial outcome: Signed offer at target compensation or higher",
            "Skill development: Confidence in positioning, interviewing, negotiating",
            "You'll define your personal success metrics in Module 0"
        ],
        "small_bullets": True
    },
    # Slide 7: How to Get Support (Original Slide 2 - Updated)
    {
        "type": "content",
        "title": "How to Get Support",
        "bullets": [
            "Questions about course content? → Email support@activeoffer.com",
            "Need strategic guidance? → Book 1-on-1 coaching session in portal",
            "Want peer accountability? → Join private community forum",
            "Technical issues? → Live chat in member dashboard",
            "Response time: Within 24 business hours for all channels"
        ]
    },
    # Slide 8: Your Professional Network
    {
        "type": "content",
        "title": "Your Professional Network",
        "bullets": [
            "Exclusive forum: Connect with peers targeting $200k-$500k+ roles",
            "Accountability partners: Find your implementation buddy in Week 1",
            "Alumni network: Access graduates now working at target companies",
            "Monthly masterminds: Share wins, challenges, and strategies",
            "LinkedIn group: Ongoing career support beyond course completion",
            "First action: Introduce yourself in the community forum today"
        ],
        "small_bullets": True
    },
    # Slide 9: Meet Your Instructor
    {
        "type": "content",
        "title": "Who's Guiding Your Journey",
        "bullets": [
            "[Your Name]",
            "[Current role/title or most impressive credential]",
            "[Key achievement - e.g., Negotiated 15+ offers over $300k]",
            "[Relevant experience - e.g., 12 years in enterprise sales leadership]",
            "[Why you created this - e.g., Built this after coaching 200+ sales professionals]",
            "This course contains the exact systems I used and refined over [X] years"
        ],
        "small_bullets": True
    },
    # Slide 10: Accessing the Course (Original Slide 3 - Updated)
    {
        "type": "content",
        "title": "Accessing the Course",
        "bullets": [
            "Go to: members.activeoffer.com and login with your credentials",
            "Start with Module 0: Mindset (unlocked immediately)",
            "Complete all lessons + submit checkpoint exercise to unlock next module",
            "Download course workbook from Resources for note-taking",
            "Join community forum and introduce yourself today"
        ]
    },
    # Slide 11: What You Need to Succeed
    {
        "type": "content",
        "title": "What You Need to Succeed",
        "bullets": [
            "Required: LinkedIn account (free works, Premium Career recommended)",
            "Required: Sales Navigator subscription (setup covered next slide)",
            "Required: Current resume/CV in editable format",
            "Required: Device with internet access (desktop/laptop recommended)",
            "Recommended: Note-taking system (Notion, Evernote, or course workbook)",
            "All templates and frameworks are provided within the course"
        ],
        "small_bullets": True
    },
    # Slide 12: Setting Up Sales Navigator (Original Slide 4 - Updated)
    {
        "type": "content",
        "title": "Setting Up Sales Navigator",
        "bullets": [
            "Investment: $79.99/month (cancel anytime after course completion)",
            "ROI: Required for Module 2 reverse attraction strategies",
            "Capabilities: Search 25M+ decision-makers, track company changes, InMail credits",
            "Course Integration: Specific Sales Navigator exercises in Modules 1, 2, and 3",
            "Setup time: 10 minutes today prevents delays in Week 2"
        ]
    },
    # Slide 13: Your First Week Game Plan
    {
        "type": "content",
        "title": "Your First Week Game Plan",
        "bullets": [
            "Today (30 min): Complete Course Intro + Set up Sales Navigator + Introduce yourself",
            "This Week (3-5 hrs): Complete Module 0: Mindset + Submit checkpoint",
            "Block recurring calendar time for weekly course work",
            "Connect with 2-3 accountability partners in community",
            "Download course workbook from Resources",
            "Small wins create momentum - check off your first item today"
        ],
        "small_bullets": True
    },
    # Slide 14: How to Get Maximum Value
    {
        "type": "content",
        "title": "How to Get Maximum Value",
        "bullets": [
            "Implementation over consumption: Do the exercises, don't just watch",
            "Sequential completion: Each module builds on previous - don't skip",
            "Use your support: Ask questions early, attend coaching, engage community",
            "Track your metrics: Document every interview, callback, and offer",
            "Consistency wins: 1 hour daily beats 7 hours once weekly",
            "The course content is valuable. Your implementation makes it transformational."
        ],
        "small_bullets": True
    },
    # Slide 15: You're Ready
    {
        "type": "content",
        "title": "Your $200k-$500k+ Journey Starts Now",
        "bullets": [
            "You have everything you need to succeed",
            "The systems in this course are proven and repeatable",
            "Your investment will return 10-100x when you execute",
            "Next Steps: Set up Sales Navigator + Introduce yourself in community + Start Module 0",
            "Welcome to Active Offer. Your transformation begins today."
        ]
    }
]

def generate_slides(output_dir):
    """Generate all slides and save as PNG files"""
    os.makedirs(output_dir, exist_ok=True)

    for i, slide_data in enumerate(slides_content, start=1):
        print(f"Generating slide {i}/{len(slides_content)}...")

        if slide_data["type"] == "title":
            img = create_title_slide(
                slide_data["title"],
                slide_data.get("subtitle")
            )
        else:  # content slide
            img = create_content_slide(
                slide_data["title"],
                slide_data["bullets"],
                slide_data.get("small_bullets", False)
            )

        # Save slide
        filename = f"{i}.png"
        filepath = os.path.join(output_dir, filename)
        img.save(filepath, "PNG", quality=95)
        print(f"  Saved: {filename}")

    print(f"\n✓ Successfully generated {len(slides_content)} slides")
    print(f"✓ Output directory: {output_dir}")

if __name__ == "__main__":
    output_directory = "/Users/terrancebrandon/Desktop/Active Offer/AO- Course Content/Active Offer- Course Material/M0- Course Intro"
    generate_slides(output_directory)
