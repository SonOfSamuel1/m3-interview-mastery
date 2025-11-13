#!/usr/bin/env python3
"""
Active Offer Webinar v2.1 - Factual Slide Generator
Generates PNG slides at 1920x1080 resolution with 100% accurate content
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Design constants matching existing style
WIDTH = 1920
HEIGHT = 1080
BACKGROUND_COLOR = "#f5f7fa"
TEXT_COLOR = "#1e3a5f"
ACCENT_COLOR = "#4a90e2"
BULLET_COLOR = "#4a90e2"

# Typography
TITLE_SIZE = 80
SUBTITLE_SIZE = 60
BODY_SIZE = 48
SMALL_SIZE = 40
LINE_SPACING = 1.5
BULLET_INDENT = 100
TEXT_INDENT = 180

# Layout
LEFT_MARGIN = 120
TOP_MARGIN = 240

def get_font(size):
    """Get font with fallback options"""
    font_options = [
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf",
    ]

    for font_path in font_options:
        if os.path.exists(font_path):
            try:
                return ImageFont.truetype(font_path, size)
            except:
                pass

    return ImageFont.load_default()

def create_slide(title, bullets=None, centered_text=None, output_path="slide.png"):
    """Create a slide with title and optional bullets or centered text"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    title_font = get_font(TITLE_SIZE)
    body_font = get_font(BODY_SIZE)

    # Draw title
    draw.text((LEFT_MARGIN, TOP_MARGIN), title, fill=TEXT_COLOR, font=title_font)

    if centered_text:
        # For centered statement slides
        text_font = get_font(SUBTITLE_SIZE)

        # Simple text wrapping for centered content
        words = centered_text.split()
        lines = []
        current_line = []
        max_width = WIDTH - (LEFT_MARGIN * 2)

        for word in words:
            test_line = ' '.join(current_line + [word])
            bbox = draw.textbbox((0, 0), test_line, font=text_font)
            if bbox[2] - bbox[0] <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]

        if current_line:
            lines.append(' '.join(current_line))

        # Center the text block vertically
        total_height = len(lines) * (SUBTITLE_SIZE * LINE_SPACING)
        start_y = (HEIGHT - total_height) / 2

        for i, line in enumerate(lines):
            bbox = draw.textbbox((0, 0), line, font=text_font)
            text_width = bbox[2] - bbox[0]
            x = (WIDTH - text_width) / 2
            y = start_y + (i * SUBTITLE_SIZE * LINE_SPACING)
            draw.text((x, y), line, fill=TEXT_COLOR, font=text_font)

    elif bullets:
        # For bullet point slides
        y_offset = TOP_MARGIN + 160

        for bullet in bullets:
            # Draw bullet
            bullet_radius = 8
            draw.ellipse(
                [BULLET_INDENT - bullet_radius, y_offset + 20,
                 BULLET_INDENT + bullet_radius, y_offset + 20 + bullet_radius * 2],
                fill=BULLET_COLOR
            )

            # Draw text with word wrapping
            words = bullet.split()
            lines = []
            current_line = []
            max_width = WIDTH - TEXT_INDENT - LEFT_MARGIN

            for word in words:
                test_line = ' '.join(current_line + [word])
                bbox = draw.textbbox((0, 0), test_line, font=body_font)
                if bbox[2] - bbox[0] <= max_width:
                    current_line.append(word)
                else:
                    if current_line:
                        lines.append(' '.join(current_line))
                    current_line = [word]

            if current_line:
                lines.append(' '.join(current_line))

            # Draw the wrapped lines
            for i, line in enumerate(lines):
                draw.text((TEXT_INDENT, y_offset + (i * BODY_SIZE * 1.3)),
                         line, fill=TEXT_COLOR, font=body_font)

            y_offset += len(lines) * BODY_SIZE * 1.5 + 30

    img.save(output_path, 'PNG', quality=95)
    print(f"Created: {output_path}")

def create_large_text_slide(text, output_path="slide.png"):
    """Create a slide with large centered text"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    text_font = get_font(SUBTITLE_SIZE)

    # Word wrapping
    words = text.split()
    lines = []
    current_line = []
    max_width = WIDTH - (LEFT_MARGIN * 2)

    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=text_font)
        if bbox[2] - bbox[0] <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line))

    # Center vertically
    total_height = len(lines) * (SUBTITLE_SIZE * LINE_SPACING)
    start_y = (HEIGHT - total_height) / 2

    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=text_font)
        text_width = bbox[2] - bbox[0]
        x = (WIDTH - text_width) / 2
        y = start_y + (i * SUBTITLE_SIZE * LINE_SPACING)
        draw.text((x, y), line, fill=TEXT_COLOR, font=text_font)

    img.save(output_path, 'PNG', quality=95)
    print(f"Created: {output_path}")

# Output directory
output_dir = "/Users/terrancebrandon/Desktop/Active Offer/AO- Course Content/Active Offer- Course Material/.Webinar Script v.2.1"

# PHASE 1: Personal Story (Slides 6-29)

print("\n=== PHASE 1: Personal Story (Slides 6-29) ===\n")

# Slide 6: My Story - The Setup
create_slide(
    "I Was Just Like You",
    bullets=[
        "10 years at AT&T in various sales roles",
        "2021: Making $130K (final year)",
        "Long hours, feeling stuck, not enough money",
        "Unable to let wife stay home with daughter",
        "Overlooked for promotions despite being top performer"
    ],
    output_path=f"{output_dir}/6.png"
)

# Slide 7: The Breaking Point
create_slide(
    "The Breaking Point",
    bullets=[
        "2021: Overlooked for promotion despite being top performer",
        "After 10 years of loyalty and high performance, still passed over",
        "Questioning everything"
    ],
    output_path=f"{output_dir}/7.png"
)

# Slide 8: Aha Moment #1 - The Overheard Conversation
create_slide(
    "The Overheard Conversation",
    bullets=[
        "Random day in the office",
        "Overheard coworkers talking about former colleague",
        "He left AT&T, now making $400K+ at mid-market software company",
        "My reaction: How is he pulling this off? I barely cracked $150K in my best year"
    ],
    output_path=f"{output_dir}/8.png"
)

# Slide 9: Down the Rabbit Hole
create_slide(
    "Down the Rabbit Hole",
    bullets=[
        "Started researching top sales roles industry-wide",
        "Discovery: Average salespeople at top companies making hundreds of thousands more",
        "This wasn't about working harder",
        "It was about being in the RIGHT boat"
    ],
    output_path=f"{output_dir}/9.png"
)

# Slide 10: Aha Moment #1 Revealed
create_large_text_slide(
    "The role you're in matters more than how hard you work",
    output_path=f"{output_dir}/10.png"
)

# Slide 11: The Question
create_large_text_slide(
    "What if I could get into the RIGHT boat?",
    output_path=f"{output_dir}/11.png"
)

# Slide 12: The Numbers Game Problem
create_slide(
    "The Numbers Game",
    bullets=[
        "Trying to figure out how to beat 99% of applicants",
        "At Google: 2,000 applicants for each role",
        "Only 20 get interviewed",
        "Question: How do I stand out?"
    ],
    output_path=f"{output_dir}/12.png"
)

# Slide 13: The Mindshare Insight
create_large_text_slide(
    "Most candidates are never considered not because they CAN'T do the role... but because they have ZERO percent mindshare with the hiring manager",
    output_path=f"{output_dir}/13.png"
)

# Slide 14: The Strategy
create_slide(
    "The Strategy",
    bullets=[
        "If I can get in front of hiring managers and gain mindshare...",
        "...I can dramatically increase my chances",
        "Implemented first part of Active Offer strategy"
    ],
    output_path=f"{output_dir}/14.png"
)

# Slide 15: Aha Moment #2 Result
create_large_text_slide(
    "Within one week: Interviews with Salesforce, Google, and Amazon. ACCESS BEATS APPLICATIONS",
    output_path=f"{output_dir}/15.png"
)

# Slide 16: The First Salesforce Interview
create_slide(
    "The First Salesforce Interview",
    bullets=[
        "I bombed it completely",
        "I'm terrible at interviews",
        "The structure was unlike anything I'd experienced",
        "Devastating after all that work to get the interview"
    ],
    output_path=f"{output_dir}/16.png"
)

# Slide 17: The Second Chance
create_slide(
    "The Second Chance",
    bullets=[
        "Within a week: Another Salesforce interview for different position",
        "This time would be different"
    ],
    output_path=f"{output_dir}/17.png"
)

# Slide 18: The Preparation
create_slide(
    "The Preparation",
    bullets=[
        "Abundance of research on what hiring managers look for",
        "Pre-prepared interview assets",
        "Clear understanding of how these interviews differ",
        "Knew exactly what they were hiring for"
    ],
    output_path=f"{output_dir}/18.png"
)

# Slide 19: The Result
create_slide(
    "The Result",
    bullets=[
        "My plan worked like a charm",
        "Aced the interview"
    ],
    output_path=f"{output_dir}/19.png"
)

# Slide 20: Aha Moment #3 Revealed
create_large_text_slide(
    "PREPARATION BEATS NATURAL TALENT. With the right assets and strategy, anyone can ace these interviews",
    output_path=f"{output_dir}/20.png"
)

# Slide 21: Two Years Later
create_slide(
    "Two Years Later (2023)",
    bullets=[
        "Met with long-time VP of Sales at Salesforce",
        "He'd made millions during his time in tech sales",
        "Was about to share his framework..."
    ],
    output_path=f"{output_dir}/21.png"
)

# Slide 22: The Framework
create_slide(
    "The Framework",
    bullets=[
        "VP shared his framework for making $1M+ per year",
        "The secret: EQUITY",
        "Most people only focus on base + commission",
        "The real wealth is in stock/equity"
    ],
    output_path=f"{output_dir}/22.png"
)

# Slide 23: Taking Action (2024)
create_slide(
    "Taking Action (2024)",
    bullets=[
        "Applied his advice",
        "Targeted roles with significant equity components",
        "Negotiated for maximum equity, not just cash"
    ],
    output_path=f"{output_dir}/23.png"
)

# Slide 24: Aha Moment #4 Result
create_large_text_slide(
    "Landed role with high commissions AND over $1M in equity in 1.5 years. TOTAL COMPENSATION INCLUDES EQUITY - THAT'S WHERE THE REAL WEALTH IS",
    output_path=f"{output_dir}/24.png"
)

# Slide 25: The Full Transformation
create_slide(
    "The Full Transformation",
    bullets=[
        "2012: $65K",
        "2021: $130K (AT&T final year)",
        "2022: $514K (Salesforce first full year)",
        "2024-2025: $1.08M+ W2 + $1M equity",
        "300%+ income increase in first year"
    ],
    output_path=f"{output_dir}/25.png"
)

# Slide 26: Time to Hired
create_slide(
    "Time to Hired",
    bullets=[
        "Hired within 6 days after landing interviews",
        "From stuck at $130K to $514K first year"
    ],
    output_path=f"{output_dir}/26.png"
)

# Slide 27: The Peak
create_slide(
    "The Peak",
    bullets=[
        "Over $1M in W2 compensation as Account Executive",
        "Close to another million in equity",
        "Working from home, better hours, more family time"
    ],
    output_path=f"{output_dir}/27.png"
)

# Slide 28: August 2025 - Retirement
create_slide(
    "August 2025",
    bullets=[
        "Officially retired from corporate sales",
        "Living life on own terms",
        "More time with family",
        "Serving in the community"
    ],
    output_path=f"{output_dir}/28.png"
)

# Slide 29: My Mission Now
create_large_text_slide(
    "Giving back to Account Executives in the same position I was in. If I can do it, you can too. Let me show you how...",
    output_path=f"{output_dir}/29.png"
)

# PHASE 2: Student Stories (Slides 41-43, 43.5, 62-67)

print("\n=== PHASE 2: Student Stories ===\n")

# Slide 41: Meet Darrel
create_slide(
    "Meet Darrel",
    bullets=[
        "AT&T Account Manager",
        "Making $100K",
        "Felt stuck, felt underpaid, no real path out"
    ],
    output_path=f"{output_dir}/41.png"
)

# Slide 42: Darrel's Implementation
create_slide(
    "Darrel's Implementation",
    bullets=[
        "First test of Active Offer system outside of founder",
        "Used: Reverse Attraction, Interview Mastery, Negotiating the Offer",
        "Biggest breakthrough: Learned exactly what companies to look for and how to quickly lock down and ace interviews"
    ],
    output_path=f"{output_dir}/42.png"
)

# Slide 43: Darrel's First Result
create_slide(
    "Darrel's First Result",
    bullets=[
        "New role: Account Executive",
        "First offer: $90K raise (to $190K)",
        "I got a $90K raise on my first offer"
    ],
    output_path=f"{output_dir}/43.png"
)

# Slide 43.5: Darrel's Year 2 (NEW)
create_slide(
    "Darrel's Year 2",
    bullets=[
        "One year later: Used same method again",
        "Additional $80K raise on new offer",
        "Plus: $70K stock bonus",
        "Total progression: $100K to $190K to $340K+ in ~2 years"
    ],
    output_path=f"{output_dir}/43_5.png"
)

# Slide 62: Meet Simon
create_slide(
    "Meet Simon",
    bullets=[
        "Account Executive",
        "Making $90K",
        "Job wasn't paying enough to meet his needs"
    ],
    output_path=f"{output_dir}/62.png"
)

# Slide 63: Simon's Challenge
create_slide(
    "Simon's Challenge",
    bullets=[
        "Felt trapped at $90K",
        "Knew he was capable of more",
        "Didn't know how to break through"
    ],
    output_path=f"{output_dir}/63.png"
)

# Slide 64: Simon's Implementation
create_slide(
    "Simon's Implementation",
    bullets=[
        "Used: Reverse Attraction, Interview Mastery, Negotiation",
        "Biggest breakthrough: Targeted the right companies and gained access to hiring managers"
    ],
    output_path=f"{output_dir}/64.png"
)

# Slide 65: Simon's Offer
create_slide(
    "Simon's Offer",
    bullets=[
        "Final offer: $280K",
        "Increase: +$190K",
        "Over 3x his previous income!"
    ],
    output_path=f"{output_dir}/65.png"
)

# Slide 66: Simon's Result
create_slide(
    "Simon's Result",
    bullets=[
        "New role: Account Executive at premium tech company",
        "$90K to $280K",
        "Life-changing transformation"
    ],
    output_path=f"{output_dir}/66.png"
)

# Slide 67: The Pattern
create_large_text_slide(
    "Both Darrel and Simon used the same system. Both achieved life-changing raises ($90K-$190K). This system works. Period.",
    output_path=f"{output_dir}/67.png"
)

# PHASE 3: Program Details (Slides 100-114)

print("\n=== PHASE 3: Program Details (Slides 100-114) ===\n")

# Slide 100: Here's What You Get
create_slide(
    "Here's What You Get",
    bullets=[
        "The Active Offer System Video Training",
        "Scripts & Playbooks",
        "Interview Assets & Templates",
        "Group Coaching & Community",
        "Expert Support"
    ],
    output_path=f"{output_dir}/100.png"
)

# Slide 101: Component #1
create_slide(
    "Component #1: Video Training",
    bullets=[
        "The Active Offer System Video Training",
        "7+ comprehensive video modules",
        "The exact strategies that took me from $130K to $1M+",
        "Value: $3,000"
    ],
    output_path=f"{output_dir}/101.png"
)

# Slide 102: Component #2
create_slide(
    "Component #2: Scripts Workbook",
    bullets=[
        "Top Scripts That Land Interviews",
        "Proven scripts and templates for gaining access",
        "The exact language that opens doors",
        "Value: $500"
    ],
    output_path=f"{output_dir}/102.png"
)

# Slide 103: Component #3
create_slide(
    "Component #3: Sure Hire Plays",
    bullets=[
        "Real Plays to Get Recruited Fast",
        "Step-by-step playbooks for targeting top roles",
        "The strategies that got me interviews at Salesforce, Google, Amazon in one week",
        "Value: $1,000"
    ],
    output_path=f"{output_dir}/103.png"
)

# Slide 104: Component #4
create_slide(
    "Component #4: Interview Assets",
    bullets=[
        "Complete Interview Domination Toolkit",
        "Presentation Templates, 30-60-90 Day Plans",
        "Resume Template, Cover Letter Template",
        "Interview Questions Workbook",
        "Value: $1,500"
    ],
    output_path=f"{output_dir}/104.png"
)

# Slide 105: Component #5
create_slide(
    "Component #5: LinkedIn Profile",
    bullets=[
        "LinkedIn Optimization Checklist",
        "Complete profile audit and optimization guide",
        "Position yourself to attract recruiters",
        "Value: $300"
    ],
    output_path=f"{output_dir}/105.png"
)

# Slide 106: Component #6
create_slide(
    "Component #6: Accountability Log",
    bullets=[
        "90-Day Action Tracker",
        "Stay on track with daily 30-minute implementation",
        "Track progress toward your offer",
        "Value: $200"
    ],
    output_path=f"{output_dir}/106.png"
)

# Slide 107: Component #7
create_slide(
    "Component #7: Message Templates",
    bullets=[
        "Cold Email & LinkedIn Vault",
        "The exact outreach templates that work",
        "Never guess what to say again",
        "Value: $400"
    ],
    output_path=f"{output_dir}/107.png"
)

# Slide 108: Component #8
create_slide(
    "Component #8: Group Coaching",
    bullets=[
        "Twice-Weekly Group Coaching Calls",
        "Get your questions answered in real-time",
        "Learn from others in the cohort",
        "Stay accountable and motivated",
        "Value: $5,000"
    ],
    output_path=f"{output_dir}/108.png"
)

# Slide 109: Component #9
create_slide(
    "Component #9: Community Access",
    bullets=[
        "Private Slack Community",
        "Connect with other high-performing sales professionals",
        "Share wins, get support, build your network",
        "Value: $1,000"
    ],
    output_path=f"{output_dir}/109.png"
)

# Slide 110: Component #10
create_slide(
    "Component #10: Email Support",
    bullets=[
        "Direct Email Support",
        "Get unstuck when you need help",
        "Expert guidance throughout your 90 days",
        "Value: $2,000"
    ],
    output_path=f"{output_dir}/110.png"
)

# Slide 111: Component #11
create_slide(
    "Component #11: Negotiation Support",
    bullets=[
        "Offer Negotiation Strategy",
        "Don't leave $50K+ on the table",
        "Expert guidance when you have offers in hand",
        "Value: $2,000"
    ],
    output_path=f"{output_dir}/111.png"
)

# Slide 112: The Total Value
create_slide(
    "The Total Value",
    bullets=[
        "Video Training: $3,000",
        "Scripts & Plays: $1,900",
        "Group Coaching: $5,000",
        "Community & Support: $5,000",
        "Interview Assets: $2,000",
        "Total Value: $16,900"
    ],
    output_path=f"{output_dir}/112.png"
)

# Slide 113: Who This Is For
create_slide(
    "Who This Is For",
    bullets=[
        "Making $80K+ in B2B sales currently",
        "4+ years of sales experience",
        "Ready to invest 30 min/day for 90 days",
        "Want to achieve $50K-$150K+ raise",
        "Committed to implementation"
    ],
    output_path=f"{output_dir}/113.png"
)

# Slide 114: Who This ISN'T For
create_slide(
    "Who This ISN'T For",
    bullets=[
        "Less than 4 years sales experience",
        "Not in B2B sales",
        "Under $80K current income",
        "Looking for magic button (no work required)",
        "Not willing to invest 30 minutes per day"
    ],
    output_path=f"{output_dir}/114.png"
)

# PHASE 4: Close - Strategy Call CTA (Slides 118-120)

print("\n=== PHASE 4: Strategy Call CTA (Slides 118-120) ===\n")

# Slide 118: Book Your Free Strategy Call
create_slide(
    "Book Your Free Strategy Call",
    bullets=[
        "On this 45-minute call, we'll:",
        "Map out your ideal role (comp, company, lifestyle)",
        "Identify positioning gaps keeping you stuck",
        "Show you roadmap to $50K-$150K+ raise",
        "Determine if Active Offer System is right for you"
    ],
    output_path=f"{output_dir}/118.png"
)

# Slide 119: What To Do Right Now
create_slide(
    "What To Do Right Now",
    bullets=[
        "Click button below",
        "Pick time that works",
        "Show up ready to discuss goals",
        "Leave with complete clarity",
        "BOOK YOUR FREE STRATEGY CALL"
    ],
    output_path=f"{output_dir}/119.png"
)

# Slide 120: Final Slide
create_large_text_slide(
    "Your $130K to $1M+ transformation is possible. I did it. Darrel did it ($100K to $340K+). Simon did it ($90K to $280K). Now it's your turn. Book Your Free Strategy Call",
    output_path=f"{output_dir}/120.png"
)

print("\n=== COMPLETE ===")
print(f"\nAll slides generated in: {output_dir}")
print("\nSlides generated:")
print("- 6-29: Personal story (24 slides)")
print("- 41-43, 43.5: Darrel story (4 slides)")
print("- 62-67: Simon story (6 slides)")
print("- 100-114: Program components (15 slides)")
print("- 118-120: Strategy call CTA (3 slides)")
print("\nTotal: 52 slides with 100% factual content")
