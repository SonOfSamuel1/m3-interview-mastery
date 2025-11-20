#!/usr/bin/env python3
"""
Generate COMPLETE M2-Reverse Attraction module with Email Method and Closing slides
Total: 42 slides (1-24 existing + 25-42 new)
"""

from PIL import Image, ImageDraw, ImageFont

print("\n" + "="*80)
print("GENERATING COMPLETE M2 - REVERSE ATTRACTION MODULE")
print("Enhanced-WithGraphics Design Style - 42 Slides")
print("="*80 + "\n")

# Configuration
WIDTH = 1920
HEIGHT = 1080
BG_LIGHT = (245, 245, 245)
BG_DARK = (26, 31, 46)
TEXT_DARK = (26, 31, 46)
TEXT_LIGHT = (255, 255, 255)
ACCENT_GOLD = (212, 175, 55)
PLACEHOLDER_BG = (220, 220, 220)
PLACEHOLDER_BORDER = (212, 175, 55)
MARGIN = 120

# Load fonts
try:
    FONT_TITLE = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 64)
    FONT_TITLE_LARGE = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 72)
    FONT_BODY = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 32)
    FONT_BODY_BOLD = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 32)
    FONT_BODY_SMALL = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 28)
    FONT_SUBTITLE = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 42)
    FONT_PLACEHOLDER = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 36)
    print("✓ Fonts loaded successfully\n")
except Exception as e:
    FONT_TITLE = FONT_TITLE_LARGE = FONT_BODY = FONT_BODY_BOLD = FONT_BODY_SMALL = FONT_SUBTITLE = FONT_PLACEHOLDER = ImageFont.load_default()
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

def gen_title_slide(title, num, subtitle=None):
    """Generate dark background title slide"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)

    lines = wrap_text(title, FONT_TITLE_LARGE, WIDTH - (MARGIN * 2))
    start_y = (HEIGHT - len(lines) * 90) // 2

    # Gold accent line
    draw.rectangle([(WIDTH - 200) // 2, start_y - 50, (WIDTH + 200) // 2, start_y - 46], fill=ACCENT_GOLD)

    # Title
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=FONT_TITLE_LARGE)
        x = (WIDTH - (bbox[2] - bbox[0])) // 2
        draw.text((x, start_y + i * 90), line, fill=TEXT_LIGHT, font=FONT_TITLE_LARGE)

    # Subtitle
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
        draw.ellipse([MARGIN, y + 12, MARGIN + 16, y + 28], fill=ACCENT_GOLD)
        lines = wrap_text(bullet, FONT_BODY, WIDTH - bullet_indent - MARGIN - 100)
        for i, line in enumerate(lines):
            draw.text((bullet_indent, y + i * 48), line, fill=TEXT_DARK, font=FONT_BODY)
        y += len(lines) * 48 + 30

    # Slide number
    draw.text((WIDTH - MARGIN - 50, HEIGHT - MARGIN - 30), str(num), fill=TEXT_DARK, font=FONT_BODY_SMALL)

    return img

def gen_two_section_slide(title, section1_title, section1_bullets, section2_title, section2_bullets, num):
    """Generate slide with two sections"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_LIGHT)
    draw = ImageDraw.Draw(img)

    # Title
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

# NEW SLIDES 25-42 CONTENT

new_slides_content = {
    25: {
        "type": "two_section",
        "title": "Why Email Outreach?",
        "section1_title": "The Problem with LinkedIn Only",
        "section1_bullets": [
            "LinkedIn message limits (100-150/month with Sales Nav)",
            "Inboxes get flooded (hiring managers receive 50+ LinkedIn messages/week)",
            "Messages often go to 'Message Requests' folder (70% never seen)",
            "Algorithm filters impact visibility"
        ],
        "section2_title": "The Email Advantage",
        "section2_bullets": [
            "Direct to inbox (bypasses LinkedIn filters)",
            "Unlimited sends (no platform restrictions)",
            "Better deliverability (90%+ reach possible)",
            "Professional channel for executive outreach",
            "Multi-touchpoint strategy increases response 2-3x"
        ]
    },
    26: {
        "type": "two_section",
        "title": "When to Use Email vs. LinkedIn",
        "section1_title": "Use LinkedIn When:",
        "section1_bullets": [
            "Connecting with peers at your level",
            "Building relationships before asking",
            "Target is active on LinkedIn daily",
            "Company culture is casual/social",
            "You want to leverage mutual connections"
        ],
        "section2_title": "Use Email When:",
        "section2_bullets": [
            "Reaching VP-level and above executives",
            "Target has limited LinkedIn presence",
            "You need formal communication trail",
            "Following up after no LinkedIn response",
            "Demonstrating serious professional intent",
            "Strategy: Use LinkedIn to build relationships. Use Email to close opportunities."
        ]
    },
    27: {
        "type": "content",
        "title": "Finding Hiring Manager Email Addresses",
        "bullets": [
            "Step 1: Research company email pattern (firstname.lastname@company.com)",
            "Visit company website 'About' or 'Team' pages to find 2-3 employee emails",
            "Step 2: Apply pattern to hiring manager's name from LinkedIn",
            "Step 3: Verify email with Hunter.io (free: 25/month) or NeverBounce",
            "Step 4: Backup option - Use general department emails (sales@, careers@)",
            "Pro Tip: Never guess emails. Always verify. One bounced email damages sender reputation."
        ]
    },
    28: {
        "type": "two_section",
        "title": "Email Outreach Tools & Setup",
        "section1_title": "Recommended Tools",
        "section1_bullets": [
            "Gmail or Outlook (Professional email required)",
            "Hunter.io - Email finding (Free: 25/month, Paid: $49/month for 500)",
            "Mailtrack - Open tracking (Free Chrome extension)",
            "Boomerang - Send scheduling (Free: 10/month)",
            "Investment: $0-50/month depending on volume"
        ],
        "section2_title": "Setup Checklist",
        "section2_bullets": [
            "Professional email signature with LinkedIn profile link",
            "Profile photo (professional headshot)",
            "Clear from name (FirstName LastName format)",
            "Email tracking enabled",
            "Templates saved in drafts folder",
            "CRM or spreadsheet ready for tracking"
        ]
    },
    29: {
        "type": "video_placeholder",
        "title": "Video: Email Tool Setup",
        "subtitle": "(Setting up your email outreach stack - 12 minutes)"
    },
    30: {
        "type": "content",
        "title": "The Perfect Cold Email Structure",
        "bullets": [
            "Part 1: PERSONALIZED HOOK (1-2 sentences) - Reference something specific about them/company",
            "Part 2: CREDIBILITY STATEMENT (1 sentence) - Your relevant background/results",
            "Part 3: VALUE PROPOSITION (2-3 sentences) - Why you're reaching out + what you bring",
            "Part 4: CLEAR CALL-TO-ACTION (1 sentence) - Specific, low-friction ask",
            "Critical Rules: Keep under 150 words total, No attachments on first email",
            "Mobile-friendly formatting (short paragraphs), Professional but conversational tone"
        ]
    },
    31: {
        "type": "content",
        "title": "Email Template #1 - Hiring Manager Direct",
        "bullets": [
            "Subject: Enterprise Sales Leader | [Your Name]",
            "Hi [First Name], I came across [Company]'s recent [specific news] and was impressed by [detail].",
            "I'm an Enterprise Account Executive with 7 years scaling revenue at [Companies], consistently hitting 150%+ of quota.",
            "I'm exploring my next role and believe my experience in [skill] aligns with [Company]'s expansion.",
            "Would you be open to a brief 15-minute call next week to discuss whether there might be a fit?",
            "Best regards, [Your Name] [Phone] [LinkedIn URL]"
        ]
    },
    32: {
        "type": "content",
        "title": "Email Template #2 - Recruiter Introduction",
        "bullets": [
            "Subject: Sales Leader | [Your Specialty] Expert",
            "Hi [First Name], I noticed you're recruiting for [specific role] at [Company]. I'm very interested.",
            "I'm currently a [Title] at [Company], where I: Grew territory from $3M to $12M ARR in 18 months",
            "My background in [industry] sales and proven track record with [customer type] aligns well with [Company].",
            "I'd love to schedule a conversation to discuss how I can contribute. Are you available this week?",
            "When to Use: Responding to posted job openings or reaching out to known recruiters"
        ]
    },
    33: {
        "type": "content",
        "title": "Email Template #3 - The Follow-Up",
        "bullets": [
            "When to Send: 5-7 days after initial email with no response",
            "Subject: Re: [Original Subject] (keeps thread together)",
            "Hi [First Name], I wanted to follow up on my email from last week about potential sales opportunities.",
            "I understand you're busy - I'm an Enterprise AE interested in [Company] because of [specific reason].",
            "If now isn't the right time, I completely understand. Should I reach back out in 30/60/90 days?",
            "Follow-Up Strategy: Email 1 (Day 0), Email 2 (Day 5-7), Email 3 (Day 14), Then nurture list"
        ]
    },
    34: {
        "type": "content",
        "title": "The Habit v.2 - Daily Email Routine",
        "bullets": [
            "Time Commitment: 20 minutes/day (100 minutes/week)",
            "Daily Workflow: 1) Send 5 new initial emails (10 min) - Personalize from templates",
            "2) Send 3-5 follow-ups (5 min) - Follow up on emails sent 5-7 days ago",
            "3) Respond to replies (5 min) - Schedule calls, update tracker",
            "Weekly Target: 25 new emails sent, 15-20 follow-ups, 40-45 total touchpoints",
            "Expected Results: 2-4 responses, 1-2 phone calls per week",
            "Monthly Target: 100-125 hiring managers contacted, 8-15 conversations, 3-5 interview opportunities"
        ]
    },
    35: {
        "type": "two_section",
        "title": "Email Tracking & Metrics",
        "section1_title": "Track These Metrics",
        "section1_bullets": [
            "Sent: Total emails sent this week/month",
            "Open Rate: % of emails opened (target: 40-60%)",
            "Response Rate: % who reply (target: 5-10%)",
            "Positive Response Rate: % interested (target: 2-4%)",
            "Meetings Booked: Actual calls scheduled"
        ],
        "section2_title": "Optimization Triggers",
        "section2_bullets": [
            "If open rate < 30%: Improve subject lines, verify emails, check spam score",
            "If response rate < 3%: Increase personalization, shorten email, test templates",
            "If positive responses but no meetings: Strengthen CTA, offer specific times",
            "Pro Tip: Review metrics weekly. A/B test one element at a time"
        ]
    },
    36: {
        "type": "content",
        "title": "Combining LinkedIn + Email (Multi-Touch Strategy)",
        "bullets": [
            "Touch 1 - Day 0: LinkedIn connection request (with personalized note)",
            "Touch 2 - Day 3: If accepted, send LinkedIn message thanking them + value prop",
            "Touch 3 - Day 5: Send email (use Template #1) - 'Following up on LinkedIn...'",
            "Touch 4 - Day 10: Second LinkedIn message or email follow-up",
            "Touch 5 - Day 17: Final email follow-up offering to reconnect later",
            "Why This Works: Multi-channel increases visibility 250%, shows persistence without annoying",
            "Expected Results: Single-channel 3-5%, Multi-channel 8-12%, Strategic multi-touch 12-18% response"
        ]
    },
    37: {
        "type": "content",
        "title": "Your First Week Action Plan",
        "bullets": [
            "Day 1 (60 min): Optimize resume, draft cover letter, update LinkedIn headline/about",
            "Day 2 (45 min): Sign up for Sales Navigator, complete LinkedIn profile optimization",
            "Day 3 (60 min): Build hiring manager list (50 people), organize in spreadsheet",
            "Day 4 (30 min): Install email tracking tools, set up Hunter.io, create email templates",
            "Day 5 (30 min): Send 5 LinkedIn connection requests, find/verify 10 email addresses",
            "Days 6-7 (30 min each): Send 5 LinkedIn messages, send 5 cold emails, track metrics",
            "Result: By end of Week 1, you'll have contacted 25 different hiring managers"
        ]
    },
    38: {
        "type": "content",
        "title": "The 30-Day Reverse Attraction Challenge",
        "bullets": [
            "Daily Habit (50 minutes/day): 30 min LinkedIn outreach + 20 min Email outreach",
            "Weekly Targets: 25 LinkedIn messages, 25 emails, 15-20 follow-ups (both channels)",
            "By Day 30 You Will Have: Contacted 200+ hiring managers across multiple channels",
            "Expected Results: 15-30 meaningful conversations, 3-8 phone/video calls, 1-3 actual interviews",
            "Make the Commitment: 'I commit to executing The Habit every day for 30 days.'",
            "Accountability: Share this commitment in the community and find an accountability partner"
        ]
    },
    39: {
        "type": "content",
        "title": "Module 2 Summary - Key Takeaways",
        "bullets": [
            "Foundation First: Profile optimization precedes outreach (Resume, Cover Letter, LinkedIn)",
            "Multi-Channel Approach: LinkedIn for relationships + Email for direct communication = 3x response",
            "The Habit v.1 (LinkedIn): Sales Navigator, hiring manager lists, daily outreach (30 min/day)",
            "The Habit v.2 (Email): Email discovery, 4-part formula, daily routine (20 min/day)",
            "Success Formula: Optimized Profile + Daily Habits + Multi-Channel Outreach + Consistency = Interviews"
        ]
    },
    40: {
        "type": "two_section",
        "title": "Troubleshooting & Support",
        "section1_title": "Common Issues",
        "section1_bullets": [
            "Not getting responses: Review templates, increase personalization, shorten messages",
            "LinkedIn account restricted: Slow down requests (max 20/day), personalize always",
            "Can't find email addresses: Focus on LinkedIn-only, use company careers email backup",
            "Low open rates: Improve subject lines, check spam score, verify email addresses"
        ],
        "section2_title": "Get Help",
        "section2_bullets": [
            "Community Support: Post questions in channel, share messages for peer review",
            "Weekly Office Hours: Join every Thursday, 2pm EST",
            "1-on-1 Coaching: Schedule 30-min strategy session (premium tier)",
            "Resource Library: Scripts Playbook, video tutorials, case studies"
        ]
    },
    41: {
        "type": "content",
        "title": "Next: Module 3 - Interview Mastery",
        "bullets": [
            "Coming Up Next: Now that you're generating interviews, it's time to convert them into offers",
            "What You'll Learn: Phone screen success, panel interviews, executive interview prep",
            "Also: Technical/case interviews, handling objections, following up to close the loop",
            "Your Assignment: Complete at least 2 weeks of The Habit (LinkedIn + Email) before M3",
            "Don't Skip Ahead: The best time to learn interview skills is right before you need them",
            "Ready to Begin M3? Master Reverse Attraction first, then advance."
        ]
    },
    42: {
        "type": "title",
        "title": "You've Completed Module 2!",
        "subtitle": "The next 30 days will determine your career trajectory"
    }
}

# Generate only NEW slides (25-42)
print("Generating NEW slides (25-42)...\n")

for num in range(25, 43):
    content = new_slides_content.get(num)

    if not content:
        print(f"⚠ Slide {num}: No content defined")
        continue

    slide_type = content.get("type")
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
print("✓ NEW SLIDES GENERATED")
print("="*80)
print(f"\nGenerated slides 25-42 (18 new slides)")
print(f"Total module now: 42 slides")
print(f"Location: M2- Reverse Attraction/")
print(f"\nModule Structure:")
print(f"  Slides 1-7: Profile Foundation")
print(f"  Slides 8-14: LinkedIn Sales Navigator & List Building")
print(f"  Slides 15-23: The Habit v.1 (LinkedIn Method)")
print(f"  Slide 24: The Habit v.2 Title")
print(f"  Slides 25-36: The Habit v.2 (Email Method) - NEW")
print(f"  Slides 37-42: Module Summary & Next Steps - NEW")
print("="*80 + "\n")
