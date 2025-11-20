#!/usr/bin/env python3
"""
Generate Panel Presentation slides for Active Offer M3- Interview Mastery Module
Slides 18-23: Complete the incomplete Panel Interview section
Brand Style: Minimalist, clean, black text on light gray background
Output: 1920x1080 PNG files at 16:9 aspect ratio
"""

from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

# Brand Colors (matching existing module slides)
BACKGROUND_COLOR = "#F5F5F5"
TEXT_COLOR = "#000000"

# Slide dimensions (1920x1080 - 16:9 aspect ratio)
SLIDE_WIDTH = 1920
SLIDE_HEIGHT = 1080

# Typography settings (matching existing Interview Mastery slides)
TITLE_FONT_SIZE = 80
SUBTITLE_FONT_SIZE = 52
BODY_FONT_SIZE = 48
SMALL_FONT_SIZE = 44

# Layout settings
LEFT_MARGIN = 100
RIGHT_MARGIN = 100
TOP_MARGIN = 80
LINE_SPACING = 1.5

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

def create_overview_slide(title, subtitle, overview_text, section_header, bullets):
    """Create an overview slide with paragraph and bullet sections (like Slide 9)"""
    img = Image.new('RGB', (SLIDE_WIDTH, SLIDE_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    # Load fonts
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", TITLE_FONT_SIZE)
        subtitle_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", SUBTITLE_FONT_SIZE)
        body_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", SMALL_FONT_SIZE)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        body_font = ImageFont.load_default()

    y = TOP_MARGIN

    # Draw title (bold)
    draw.text((LEFT_MARGIN, y), title, fill=TEXT_COLOR, font=title_font)
    y += int(TITLE_FONT_SIZE * 1.3)

    # Draw subtitle
    y += 20
    draw.text((LEFT_MARGIN, y), subtitle, fill=TEXT_COLOR, font=subtitle_font)
    y += int(SUBTITLE_FONT_SIZE * 1.5)

    # Draw overview paragraph
    y += 30
    max_text_width = SLIDE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN
    overview_lines = wrap_text(overview_text, body_font, max_text_width)

    for line in overview_lines:
        draw.text((LEFT_MARGIN, y), line, fill=TEXT_COLOR, font=body_font)
        y += int(SMALL_FONT_SIZE * 1.4)

    # Draw section header
    y += 40
    draw.text((LEFT_MARGIN, y), section_header, fill=TEXT_COLOR, font=subtitle_font)
    y += int(SUBTITLE_FONT_SIZE * 1.5)

    # Draw bullets
    y += 20
    for i, bullet in enumerate(bullets, 1):
        bullet_text = f"{i}. {bullet}"
        bullet_lines = wrap_text(bullet_text, body_font, max_text_width - 40)

        for j, line in enumerate(bullet_lines):
            x_offset = LEFT_MARGIN if j == 0 else LEFT_MARGIN + 40
            draw.text((x_offset, y), line, fill=TEXT_COLOR, font=body_font)
            y += int(SMALL_FONT_SIZE * 1.4)

        y += 15  # Space between bullets

    return img

def create_content_slide(title, subtitle, bullets, numbered=True):
    """Create a content slide with title, subtitle, and bullets"""
    img = Image.new('RGB', (SLIDE_WIDTH, SLIDE_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    # Load fonts
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", TITLE_FONT_SIZE)
        subtitle_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", SUBTITLE_FONT_SIZE)
        body_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", BODY_FONT_SIZE)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        body_font = ImageFont.load_default()

    y = TOP_MARGIN

    # Draw title
    draw.text((LEFT_MARGIN, y), title, fill=TEXT_COLOR, font=title_font)
    y += int(TITLE_FONT_SIZE * 1.3)

    # Draw subtitle
    y += 20
    draw.text((LEFT_MARGIN, y), subtitle, fill=TEXT_COLOR, font=subtitle_font)
    y += int(SUBTITLE_FONT_SIZE * 1.5)

    # Draw bullets
    y += 30
    max_text_width = SLIDE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN - 40

    for i, bullet in enumerate(bullets, 1):
        if numbered:
            bullet_text = f"{i}. {bullet}"
        else:
            bullet_text = bullet

        bullet_lines = wrap_text(bullet_text, body_font, max_text_width)

        for j, line in enumerate(bullet_lines):
            x_offset = LEFT_MARGIN if j == 0 else LEFT_MARGIN + 40
            draw.text((x_offset, y), line, fill=TEXT_COLOR, font=body_font)
            y += int(BODY_FONT_SIZE * 1.35)

        y += 15  # Space between bullets

    return img

def create_sections_slide(title, subtitle, sections):
    """Create a slide with multiple sections (for questions slide)"""
    img = Image.new('RGB', (SLIDE_WIDTH, SLIDE_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    # Load fonts
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", TITLE_FONT_SIZE)
        subtitle_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", SUBTITLE_FONT_SIZE)
        body_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", BODY_FONT_SIZE)
        section_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", SUBTITLE_FONT_SIZE)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        body_font = ImageFont.load_default()
        section_font = ImageFont.load_default()

    y = TOP_MARGIN

    # Draw title
    draw.text((LEFT_MARGIN, y), title, fill=TEXT_COLOR, font=title_font)
    y += int(TITLE_FONT_SIZE * 1.3)

    # Draw subtitle
    y += 20
    draw.text((LEFT_MARGIN, y), subtitle, fill=TEXT_COLOR, font=subtitle_font)
    y += int(SUBTITLE_FONT_SIZE * 1.5)

    # Draw sections
    y += 30
    max_text_width = SLIDE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN - 40

    question_num = 1
    for section_name, questions in sections:
        # Draw section header if provided
        if section_name:
            draw.text((LEFT_MARGIN, y), section_name, fill=TEXT_COLOR, font=section_font)
            y += int(SUBTITLE_FONT_SIZE * 1.3)

        # Draw questions
        for question in questions:
            bullet_text = f"{question_num}. {question}"
            bullet_lines = wrap_text(bullet_text, body_font, max_text_width)

            for j, line in enumerate(bullet_lines):
                x_offset = LEFT_MARGIN if j == 0 else LEFT_MARGIN + 40
                draw.text((x_offset, y), line, fill=TEXT_COLOR, font=body_font)
                y += int(BODY_FONT_SIZE * 1.35)

            y += 15  # Space between questions
            question_num += 1

        y += 20  # Extra space between sections

    return img

def create_reference_slide(title, subtitle, reference_text, frameworks):
    """Create a reference/answer examples slide (like Slide 12)"""
    img = Image.new('RGB', (SLIDE_WIDTH, SLIDE_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    # Load fonts
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", TITLE_FONT_SIZE)
        subtitle_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", SUBTITLE_FONT_SIZE)
        body_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", BODY_FONT_SIZE)
        small_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", SMALL_FONT_SIZE)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        body_font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    y = TOP_MARGIN

    # Draw title
    draw.text((LEFT_MARGIN, y), title, fill=TEXT_COLOR, font=title_font)
    y += int(TITLE_FONT_SIZE * 1.3)

    # Draw subtitle
    y += 20
    draw.text((LEFT_MARGIN, y), subtitle, fill=TEXT_COLOR, font=subtitle_font)
    y += int(SUBTITLE_FONT_SIZE * 1.5)

    # Draw reference section
    y += 40
    section_header = "Where to Find Example Answers"
    draw.text((LEFT_MARGIN, y), section_header, fill=TEXT_COLOR, font=subtitle_font)
    y += int(SUBTITLE_FONT_SIZE * 1.5)

    y += 20
    max_text_width = SLIDE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN
    ref_lines = wrap_text(reference_text, body_font, max_text_width)

    for line in ref_lines:
        draw.text((LEFT_MARGIN, y), line, fill=TEXT_COLOR, font=body_font)
        y += int(BODY_FONT_SIZE * 1.35)

    # Draw frameworks section
    y += 50
    framework_header = "Key Answer Frameworks to Use"
    draw.text((LEFT_MARGIN, y), framework_header, fill=TEXT_COLOR, font=subtitle_font)
    y += int(SUBTITLE_FONT_SIZE * 1.5)

    y += 20
    for framework_name, framework_desc in frameworks:
        # Framework name
        draw.text((LEFT_MARGIN, y), framework_name, fill=TEXT_COLOR, font=body_font)
        y += int(BODY_FONT_SIZE * 1.4)

        # Framework description
        desc_lines = wrap_text(framework_desc, small_font, max_text_width - 60)
        for line in desc_lines:
            draw.text((LEFT_MARGIN + 60, y), line, fill=TEXT_COLOR, font=small_font)
            y += int(SMALL_FONT_SIZE * 1.3)

        y += 25  # Space between frameworks

    return img

# Define all slide content for Panel Presentation section
panel_slides_content = [
    # Slide 18: Overview
    {
        "type": "overview",
        "title": "Final Panel Presentation",
        "subtitle": "Understanding Panel Interviews",
        "overview": "The panel interview represents the final evaluation stage where you'll present to multiple decision-makers simultaneously. This interview assesses your strategic thinking, executive presence, leadership potential, and ability to navigate complex stakeholder dynamics. Panel interviews for $200k+ roles often include a formal business presentation component (30-60-90 day plan or strategic proposal).",
        "section_header": "What Panel Interviews Evaluate",
        "bullets": [
            "Strategic thinking and business acumen",
            "Executive presence and confidence under pressure",
            "Ability to engage diverse stakeholders with competing priorities",
            "Communication clarity and persuasion skills",
            "Cultural fit at leadership/senior level"
        ]
    },
    # Slide 19: Before Actions
    {
        "type": "content",
        "title": "Final Panel Presentation",
        "subtitle": "Actions to Take Before",
        "bullets": [
            "LinkedIn research on every panel member (role, background, priorities, recent posts)",
            "Identify each stakeholder's likely concerns and evaluation criteria",
            "Research company's current challenges, initiatives, and strategic direction",
            "Create 30-60-90 day plan or strategic business case presentation (10-12 slides)",
            "Prepare customized talking points addressing each panel member's domain",
            "Rehearse presentation 5+ times (aim for 15-20 minute delivery)",
            "Practice with a timer—stay within time limits",
            "Prepare technical setup (if virtual: test screen share, lighting, audio)",
            "Plan arrival time (15 minutes early for in-person, 5 minutes early for virtual)",
            "Bring physical copies of presentation handouts (if in-person)",
            "Prepare strategic questions to ask each panel member"
        ]
    },
    # Slide 20: During Actions
    {
        "type": "content",
        "title": "Final Panel Presentation",
        "subtitle": "Actions to Take During",
        "bullets": [
            "Greet each panel member individually with confident handshake/acknowledgment",
            "Open presentation with compelling hook that frames the opportunity",
            "Establish credibility early—briefly reinforce your relevant expertise",
            "Project executive presence: confident posture, vocal clarity, steady pacing",
            "Distribute eye contact evenly across all panel members",
            "Read body language and engagement levels—adjust if needed",
            "Address questions to the person asking but include others in your response",
            "Acknowledge different perspectives when panel members have competing priorities",
            "Use data and specific examples to support recommendations",
            "Stay within time limits (respect their calendars)",
            "Handle interruptions gracefully—welcome questions as engagement",
            "Close with clear next steps and express genuine enthusiasm for the opportunity"
        ]
    },
    # Slide 21: After Actions
    {
        "type": "content",
        "title": "Final Panel Presentation",
        "subtitle": "Actions to Take After",
        "bullets": [
            "Send individual thank-you emails to each panel member (not group email)",
            "Reference specific conversation points from the presentation (show you listened)",
            "Address any questions you committed to researching during the interview",
            "Attach any supporting materials promised during discussion",
            "Reiterate your enthusiasm and specific interest in the role/company",
            "Connect with panel members on LinkedIn with personalized connection notes",
            "If panel suggested next steps, confirm timeline and your availability",
            "Send brief thank-you to recruiter/HR contact summarizing your interest",
            "Document key insights from interview (valuable for negotiation later)",
            "Note any concerns raised during Q&A—prepare stronger responses for final conversations",
            "Follow up on timeline if you haven't heard back within specified timeframe"
        ]
    },
    # Slide 22: Questions
    {
        "type": "questions",
        "title": "Final Panel Presentation",
        "subtitle": "Questions to Be Prepared For:",
        "sections": [
            ("Strategic Thinking & Vision", [
                "Walk us through your 30-60-90 day plan. What are your key priorities and why?",
                "What's your assessment of our biggest challenge right now, and how would you approach it?",
                "How would you measure success in this role during your first year?",
                "What strategic initiatives would you prioritize, and what would you intentionally not focus on initially?",
                "How do you balance short-term wins with long-term strategic goals?"
            ]),
            ("Leadership & Influence", [
                "How do you build credibility and influence when joining a new organization?",
                "Describe a time when you had to lead through significant change. What was your approach?",
                "How do you handle situations where senior stakeholders have competing priorities?",
                "Tell us about a time you had to influence upward (convince leadership to change direction)."
            ]),
            ("Team & Collaboration", [
                "How would you approach building relationships with this team and key stakeholders?",
                "What's your management philosophy, and how do you develop high-performing teams?"
            ]),
            ("Domain Expertise", [
                "Based on what you know about our business, what opportunities are we missing?",
                "How would you apply your experience from [previous company/industry] to our context?",
                "What makes you uniquely qualified for this role compared to other candidates?"
            ])
        ]
    },
    # Slide 23: Answer Examples
    {
        "type": "reference",
        "title": "Final Panel Presentation",
        "subtitle": "Answer Examples",
        "reference": "For detailed example answers to panel interview questions, including 30-60-90 day plan templates and presentation frameworks, refer to: Active Offer Scripts Workbook - Pages 18-25 (Strategic question response frameworks, 30-60-90 day plan structure and examples, Stakeholder engagement strategies, Executive presence techniques, Panel Q&A best practices)",
        "frameworks": [
            ("For Strategic Questions:", "State the challenge/opportunity clearly • Present your analytical process (how you'd assess) • Offer 2-3 specific recommendations with rationale • Quantify expected impact where possible • Acknowledge risks and mitigation strategies"),
            ("For Leadership Questions:", "Use STAR method (Situation, Task, Action, Result) • Emphasize collaboration and stakeholder engagement • Highlight both the outcome and what you learned • Connect past experience to future application in this role"),
            ("For Presentation Defense:", "Listen fully to the question/concern • Acknowledge valid points before responding • Use data to support your position • Show flexibility—\"Here's why I proposed X, but I'm open to Y if...\" • Demonstrate strategic thinking in real-time")
        ]
    }
]

def generate_slides(output_dir):
    """Generate Panel Presentation slides and save as PNG files"""

    # Starting slide number is 18
    start_number = 18

    for i, slide_data in enumerate(panel_slides_content, start=start_number):
        print(f"Generating slide {i}...")

        if slide_data["type"] == "overview":
            img = create_overview_slide(
                slide_data["title"],
                slide_data["subtitle"],
                slide_data["overview"],
                slide_data["section_header"],
                slide_data["bullets"]
            )
        elif slide_data["type"] == "content":
            img = create_content_slide(
                slide_data["title"],
                slide_data["subtitle"],
                slide_data["bullets"],
                numbered=True
            )
        elif slide_data["type"] == "questions":
            img = create_sections_slide(
                slide_data["title"],
                slide_data["subtitle"],
                slide_data["sections"]
            )
        elif slide_data["type"] == "reference":
            img = create_reference_slide(
                slide_data["title"],
                slide_data["subtitle"],
                slide_data["reference"],
                slide_data["frameworks"]
            )

        # Save slide
        filename = f"{i}.png"
        filepath = os.path.join(output_dir, filename)
        img.save(filepath, "PNG", quality=95)
        print(f"  Saved: {filename}")

    print(f"\n✓ Successfully generated {len(panel_slides_content)} slides (slides {start_number}-{start_number + len(panel_slides_content) - 1})")
    print(f"✓ Output directory: {output_dir}")
    print("\n⚠️  IMPORTANT: You must now rename the existing slides:")
    print("  • Rename 21.png → 24.png")
    print("  • Rename 22.png → 25.png")
    print("  • Rename 23.png → 26.png")
    print("\nFinal module will have 26 slides total.")

if __name__ == "__main__":
    output_directory = "/Users/terrancebrandon/Desktop/Active Offer/AO- Course Content/Active Offer- Course Material/M3- Interview Mastery"
    generate_slides(output_directory)
