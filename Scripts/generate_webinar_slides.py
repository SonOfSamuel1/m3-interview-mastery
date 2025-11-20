#!/usr/bin/env python3
"""
Generate professional slides for Active Offer Webinar v4.1 - Bold Promise
Brand Style: Minimalist, clean, black text on light gray background
Output: 1920x1080 PNG files at 16:9 aspect ratio
Total Slides: ~150 slides based on webinar script
"""

from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

# Brand Colors
BACKGROUND_COLOR = "#F5F5F5"
TEXT_COLOR = "#000000"
ACCENT_COLOR = "#333333"

# Slide dimensions (1920x1080 - 16:9 aspect ratio)
SLIDE_WIDTH = 1920
SLIDE_HEIGHT = 1080

# Typography settings
TITLE_FONT_SIZE = 120
SUBTITLE_FONT_SIZE = 80
BODY_FONT_SIZE = 52
SMALL_FONT_SIZE = 44
LARGE_NUMBER_FONT_SIZE = 180

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

def create_quote_slide(quote):
    """Create a slide with a centered quote"""
    img = Image.new('RGB', (SLIDE_WIDTH, SLIDE_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    try:
        quote_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", SUBTITLE_FONT_SIZE)
    except:
        quote_font = ImageFont.load_default()

    # Wrap quote text
    quote_lines = wrap_text(quote, quote_font, SLIDE_WIDTH - 300)

    # Calculate vertical centering
    line_height = int(SUBTITLE_FONT_SIZE * LINE_SPACING)
    total_height = len(quote_lines) * line_height
    y = (SLIDE_HEIGHT - total_height) // 2

    # Draw quote lines centered
    for line in quote_lines:
        bbox = quote_font.getbbox(line)
        text_width = bbox[2] - bbox[0]
        x = (SLIDE_WIDTH - text_width) // 2
        draw.text((x, y), line, fill=TEXT_COLOR, font=quote_font)
        y += line_height

    return img

def create_big_number_slide(number_text, context_text=""):
    """Create a slide with a large number and optional context"""
    img = Image.new('RGB', (SLIDE_WIDTH, SLIDE_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    try:
        number_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", LARGE_NUMBER_FONT_SIZE)
        context_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", BODY_FONT_SIZE)
    except:
        number_font = ImageFont.load_default()
        context_font = ImageFont.load_default()

    # Draw number centered
    bbox = number_font.getbbox(number_text)
    number_width = bbox[2] - bbox[0]
    number_height = bbox[3] - bbox[1]

    number_x = (SLIDE_WIDTH - number_width) // 2
    number_y = (SLIDE_HEIGHT - number_height) // 2 - 50

    draw.text((number_x, number_y), number_text, fill=TEXT_COLOR, font=number_font)

    # Draw context text below if provided
    if context_text:
        context_lines = wrap_text(context_text, context_font, SLIDE_WIDTH - 200)
        y = number_y + number_height + 60
        for line in context_lines:
            bbox = context_font.getbbox(line)
            text_width = bbox[2] - bbox[0]
            x = (SLIDE_WIDTH - text_width) // 2
            draw.text((x, y), line, fill=TEXT_COLOR, font=context_font)
            y += int(BODY_FONT_SIZE * LINE_SPACING)

    return img

def create_content_slide(title, bullets=None, body_text=None):
    """Create a content slide with title and bullet points or body text"""
    img = Image.new('RGB', (SLIDE_WIDTH, SLIDE_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    # Load fonts
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", SUBTITLE_FONT_SIZE)
        body_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", BODY_FONT_SIZE)
    except:
        title_font = ImageFont.load_default()
        body_font = ImageFont.load_default()

    # Draw title
    y = TOP_MARGIN
    title_lines = wrap_text(title, title_font, SLIDE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN)
    for line in title_lines:
        draw.text((LEFT_MARGIN, y), line, fill=TEXT_COLOR, font=title_font)
        y += int(SUBTITLE_FONT_SIZE * LINE_SPACING)

    y += 60  # Space after title

    if bullets:
        # Draw bullets
        max_text_width = SLIDE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN - BULLET_INDENT - 40
        line_height = int(BODY_FONT_SIZE * LINE_SPACING)

        for bullet in bullets:
            # Draw bullet point
            draw.text((LEFT_MARGIN, y), "•", fill=TEXT_COLOR, font=body_font)

            # Wrap and draw bullet text
            bullet_lines = wrap_text(bullet, body_font, max_text_width)
            for i, line in enumerate(bullet_lines):
                x_offset = LEFT_MARGIN + BULLET_INDENT
                draw.text((x_offset, y), line, fill=TEXT_COLOR, font=body_font)
                y += line_height

            y += 20  # Space between bullets

    elif body_text:
        # Draw body text (no bullets)
        max_text_width = SLIDE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN
        body_lines = wrap_text(body_text, body_font, max_text_width)
        line_height = int(BODY_FONT_SIZE * LINE_SPACING)

        for line in body_lines:
            draw.text((LEFT_MARGIN, y), line, fill=TEXT_COLOR, font=body_font)
            y += line_height

    return img

# Define all slide content based on webinar script
slides_content = [
    # SLIDE 1: Title Slide
    {
        "type": "title",
        "title": "How to Increase Your Annual Income by $75K-$125K in 90 Days or Less",
        "subtitle": "Without Applying Online"
    },

    # SLIDES 2-3: Hook
    {
        "type": "quote",
        "quote": "I want to show you how I went from being ghosted by companies..."
    },
    {
        "type": "quote",
        "quote": "To having the best companies and hiring managers recruit me for their top sales roles..."
    },

    # SLIDES 4A-4E: Bold Promise Progressive Reveal
    {
        "type": "quote",
        "quote": "In the next 60 minutes, I'm going to show you how to increase your annual income..."
    },
    {
        "type": "big_number",
        "number": "$75,000 to $125,000",
        "context": ""
    },
    {
        "type": "big_number",
        "number": "90 Days or Less",
        "context": ""
    },
    {
        "type": "content",
        "title": "Without",
        "bullets": [
            "Applying online",
            "Using recruiters",
            "Quitting your job"
        ]
    },
    {
        "type": "title",
        "title": "30 Minutes Per Day",
        "subtitle": "Using a Proven System"
    },

    # SLIDES 5-8: Credibility Setup
    {
        "type": "quote",
        "quote": "But first I need to address the elephant in the room..."
    },
    {
        "type": "quote",
        "quote": "Some of you might be wondering..."
    },
    {
        "type": "quote",
        "quote": "Who is this guy? And why should I listen to him?"
    },
    {
        "type": "quote",
        "quote": "Fair question..."
    },

    # SLIDES 9-12: Credibility Establishment
    {
        "type": "quote",
        "quote": "My name is Terrance Brandon, and I've been in sales for over 10 years..."
    },
    {
        "type": "content",
        "title": "I've worked at companies like",
        "bullets": [
            "Google",
            "Amazon",
            "Salesforce"
        ]
    },
    {
        "type": "quote",
        "quote": "But it wasn't always that way..."
    },
    {
        "type": "content",
        "title": "Just a few years ago",
        "body_text": "I was stuck at AT&T making $130,000 a year after 10 years of hard work..."
    },

    # SLIDES 13A-13F: Tier 1 Future Pacing
    {
        "type": "quote",
        "quote": "Before I tell you my story, I want you to imagine something with me for just a moment..."
    },
    {
        "type": "content",
        "title": "Imagine it's 90 days from today",
        "body_text": "You're sitting at your kitchen table. Your laptop is open. You have a coffee in your hand—the good kind you actually enjoy, not the break room stuff you choke down to get through the day."
    },
    {
        "type": "content",
        "title": "You're reviewing THREE job offers",
        "body_text": "Not one. Not 'I hope someone calls me back.' THREE companies are actively competing for YOU. Each offer is $80,000 to $150,000 higher than what you're making right now."
    },
    {
        "type": "content",
        "title": "And you get to CHOOSE",
        "bullets": [
            "Which company feels right?",
            "Which role excites you?",
            "Which comp package is best?",
            "Which work arrangement fits your life?",
            "YOU'RE in control. Not them. You."
        ]
    },
    {
        "type": "content",
        "title": "The Reversal",
        "body_text": "Hiring managers are calling YOUR references right now. They're trying to convince YOU to join their team. They're asking what it would take to get you to say yes. You're not chasing them anymore. They're recruiting you."
    },
    {
        "type": "content",
        "title": "How would that feel?",
        "body_text": "That weight you've been carrying—the stress of applying to jobs and hearing nothing back, the fear that you're stuck forever—it's gone. That's not fantasy. That's exactly what happened to me. And in the next 60 minutes, I'm going to show you exactly how to make it happen for you."
    },

    # SLIDES 14-20: Transition to Story
    {
        "type": "quote",
        "quote": "But I need to be honest with you..."
    },
    {
        "type": "quote",
        "quote": "Getting to where I am today required me to completely change the way I thought about career advancement..."
    },
    {
        "type": "quote",
        "quote": "I had to let go of everything I was taught about 'working hard' and 'paying my dues'..."
    },
    {
        "type": "quote",
        "quote": "And I had to embrace a completely different approach..."
    },
    {
        "type": "quote",
        "quote": "An approach that most people never discover..."
    },
    {
        "type": "quote",
        "quote": "But once you see it, you can't unsee it..."
    },
    {
        "type": "quote",
        "quote": "So let me show you what I discovered. Let me tell you my story..."
    },

    # SECRET #1: THE VEHICLE (Slides 21-50)
    {
        "type": "title",
        "title": "Secret #1",
        "subtitle": "Why Strategic Positioning Beats Traditional Job Search"
    },
    {
        "type": "content",
        "title": "The first thing you need to understand",
        "body_text": "Your income has nothing to do with how good you are at sales. Let me tell you the story of how I learned this the hard way..."
    },

    # Epiphany Bridge #1: The Income Discovery
    {
        "type": "content",
        "title": "It was 2021",
        "body_text": "I'd been at AT&T for 10 years. I'd worked my way up from $65,000 to $130,000. I was proud of that. It felt like progress."
    },
    {
        "type": "content",
        "title": "But here's what I didn't realize",
        "body_text": "After 10 years of loyalty, after being a top performer, after giving everything to that company... $130,000 was my ceiling. That was as far as I could go."
    },
    {
        "type": "content",
        "title": "And it wasn't enough",
        "bullets": [
            "I had debt I couldn't get out of",
            "My wife wanted to stay home with our daughter, but we couldn't afford it",
            "I was working long hours, stressed, and watching other people pass me by"
        ]
    },
    {
        "type": "content",
        "title": "The Overlooked Promotion",
        "body_text": "And then, in 2021, I got passed over for a promotion. Again. I was a top performer. Everyone knew it. But it didn't matter."
    },
    {
        "type": "content",
        "title": "The Inciting Incident",
        "body_text": "Then one random day in the office, I overheard two coworkers talking. They were talking about a guy who used to work with us. Someone who'd left AT&T a year earlier. And one of them said: 'Yeah, I heard he's making over $400,000 now at some software company.'"
    },
    {
        "type": "content",
        "title": "The Shock",
        "body_text": "I almost fell out of my chair. $400,000? This was a guy I'd worked with. We had similar skills. Similar work ethic. I'd even outperformed him when we worked together."
    },
    {
        "type": "content",
        "title": "The Question",
        "body_text": "So I asked myself: 'How is he pulling this off? I was pretty good at what I did, but I barely cracked $150,000 in my best year. How is he making $400,000?'"
    },
    {
        "type": "content",
        "title": "The Rabbit Hole",
        "body_text": "So I went down a rabbit hole. I spent the next two weeks researching top sales roles industry-wide. Google. Amazon. Salesforce. Snowflake. All the top tech companies. And what I discovered changed my life forever."
    },
    {
        "type": "content",
        "title": "The Discovery",
        "body_text": "I discovered that average salespeople at top companies were making hundreds of thousands of dollars more than top performers at companies like AT&T. Not because they were better at sales. Not because they worked harder. But because they worked at companies that PAY MORE for the same work."
    },
    {
        "type": "title",
        "title": "Your income isn't determined by how good you are at sales",
        "subtitle": "It's determined by WHO is hiring you and WHICH market you're in"
    },
    {
        "type": "content",
        "title": "Everything I'd been taught was wrong",
        "body_text": "They told me: 'Work hard, and you'll get ahead.' But that's not true. The role you're in matters MORE than how hard you work."
    },

    # Boat Analogy
    {
        "type": "content",
        "title": "The Boat Analogy",
        "body_text": "Imagine you're paddling a canoe as hard as you can. You're sweating. You're exhausted. You're giving it everything you've got. And you're going 10 miles per hour."
    },
    {
        "type": "content",
        "title": "Now imagine you take that same person",
        "body_text": "With that same effort, that same work ethic... And you put them in a speedboat. Suddenly they're going 60 miles per hour. Same person. Same effort. Different vehicle. 6x results."
    },
    {
        "type": "content",
        "title": "That's what I realized about sales careers",
        "body_text": "If you're at AT&T making $130,000, you're in a canoe. If someone's at Salesforce making $500,000, they're in a speedboat. It's not that they're better at sales than you. They're just in a better boat."
    },
    {
        "type": "content",
        "title": "Once I understood this principle",
        "body_text": "Once I accepted that it's about WHERE you sell, not HOW WELL you sell—everything changed. I stopped trying to be a better salesperson. I started trying to be a better-POSITIONED salesperson. And that's when the $80K-$150K raises became possible."
    },

    # Teaching: The Three Positioning Factors
    {
        "type": "content",
        "title": "What determines your positioning?",
        "bullets": [
            "WHO is hiring you - Which company, which market segment",
            "WHICH roles you target - The level, the comp structure, the opportunity",
            "HOW you position yourself - How you get in front of hiring managers"
        ]
    },
    {
        "type": "content",
        "title": "Here's the good news",
        "bullets": [
            "Positioning is NOT about luck",
            "It's NOT about connections",
            "It's NOT about having an Ivy League degree",
            "Positioning is a skill. And skills can be learned."
        ]
    },
    {
        "type": "content",
        "title": "Strategic positioning means",
        "bullets": [
            "Instead of sending out 100 applications and hoping someone notices you... You identify the 5-10 companies that pay $300K+ for your skillset",
            "Instead of competing with 2,000 other applicants... You get in front of hiring managers BEFORE they post the job publicly",
            "Instead of being an applicant... You become a candidate they're recruiting"
        ]
    },

    # Proof: The Google Example
    {
        "type": "content",
        "title": "The Google Example",
        "body_text": "When Google posts a sales role online, they receive over 2,000 applications. But do you know how many people they actually interview? Less than 20. That's a 1% interview rate if you apply online."
    },
    {
        "type": "content",
        "title": "But here's what most people don't know",
        "body_text": "Those 20 people who got interviewed? Most of them DIDN'T apply online. They were referred by employees. They were recruited by hiring managers. They were positioned as candidates, not applicants."
    },
    {
        "type": "content",
        "title": "Once I understood this",
        "body_text": "I made a decision: I was going to figure out how to get into one of those 'better boats.' Not by applying online like everyone else. But by positioning myself so companies like Google, Amazon, and Salesforce would WANT to recruit me."
    },
    {
        "type": "content",
        "title": "And it worked",
        "body_text": "Within a year, I went from AT&T making $130,000... To Salesforce making over $514,000 my first full year. Same skills. Same work ethic. Same effort. Different positioning. 4x income."
    },
    {
        "type": "content",
        "title": "But it wasn't just about the money",
        "bullets": [
            "At AT&T, I was working 60-hour weeks",
            "At Salesforce, I work 40-hour weeks",
            "I have dinner with my family every night",
            "My wife got to stay home with our daughter",
            "We got out of debt"
        ]
    },

    # Secret #1 Summary
    {
        "type": "title",
        "title": "Secret #1: Positioning > Performance",
        "subtitle": "Get into the right boat, and the same effort that got you $130K can get you $500K"
    },
    {
        "type": "content",
        "title": "Now, you might be thinking",
        "body_text": "'Okay Terrance, that's great for you. You figured it out. But can I do this? I don't have your background. I don't have connections at Google. What if I'm not qualified for those $300K+ roles?'"
    },
    {
        "type": "quote",
        "quote": "I get it. I had the same doubts. But let me tell you something that's going to blow your mind..."
    },
    {
        "type": "content",
        "title": "You already have everything you need",
        "body_text": "You don't need better skills. You don't need an MBA. You don't need connections. You just need to position what you already have correctly."
    },
    {
        "type": "quote",
        "quote": "Let me tell you the story of how I learned this lesson..."
    },

    # SECRET #2: INTERNAL BELIEFS (Slides 51-75)
    {
        "type": "title",
        "title": "Secret #2",
        "subtitle": "You Already Have Everything You Need - Positioning Is Learnable"
    },
    {
        "type": "content",
        "title": "So I'd figured out Secret #1",
        "body_text": "Positioning beats performance. I'd identified my target companies: Google, Amazon, Salesforce. I'd created a plan to get in front of hiring managers. And it worked. Within a week, I had interviews scheduled at all three companies."
    },
    {
        "type": "content",
        "title": "I was on top of the world",
        "body_text": "I thought: 'I figured it out. I beat the system. I'm getting interviews at the best companies in the world.' I felt unstoppable."
    },
    {
        "type": "content",
        "title": "And then came the Salesforce interview",
        "body_text": "It was my first interview with a top-tier tech company. I walked in feeling confident. And I completely bombed it."
    },
    {
        "type": "content",
        "title": "They asked me questions I wasn't prepared for",
        "body_text": "Questions I'd never heard in traditional sales interviews. Questions about deal structure, multi-threading, value frameworks. I froze. I stumbled. I gave weak answers."
    },
    {
        "type": "content",
        "title": "A week later, I got the email",
        "body_text": "'Thank you for your interest, but we've decided to move forward with other candidates.' Rejected. I'd beaten the odds to GET the interview. And then I blew it."
    },
    {
        "type": "content",
        "title": "And all my old doubts came rushing back",
        "bullets": [
            "'Maybe I'm not qualified for these roles after all.'",
            "'Maybe I'm out of my league.'",
            "'Maybe I should just stay at AT&T and be grateful for what I have.'"
        ]
    },
    {
        "type": "content",
        "title": "But here's what's crazy",
        "body_text": "Within three days of that rejection, I got another message. It was from a different hiring manager at Salesforce. For a different team. They wanted to interview me."
    },
    {
        "type": "content",
        "title": "And that's when it hit me",
        "body_text": "My positioning strategy was working. I wasn't failing to GET interviews. That part was easy once I had the positioning down. I was failing to WIN interviews. And that was a completely different skill."
    },
    {
        "type": "content",
        "title": "So I made another decision",
        "body_text": "I was NOT going to bomb this second interview. I was going to figure out exactly what these companies were looking for. I was going to prepare like I'd never prepared before. And I was going to position myself as the OBVIOUS choice."
    },
    {
        "type": "content",
        "title": "So I spent the next week preparing",
        "bullets": [
            "I researched what Salesforce was hiring for",
            "I studied the team's challenges",
            "I prepared specific examples that positioned my experience as the exact solution they needed",
            "I practiced answering their questions until I could do it in my sleep"
        ]
    },
    {
        "type": "content",
        "title": "And when I walked into that second interview?",
        "body_text": "It was completely different. They asked tough questions—but this time, I was ready. Every answer positioned me as someone who understood their problems and had solved them before. Every example was tailored to what THEY needed, not just what I'd done."
    },
    {
        "type": "content",
        "title": "At the end of the interview",
        "body_text": "The hiring manager said: 'I don't need to see anyone else. You're exactly what we're looking for.' They fast-tracked me to the final interview. And six days later, I was hired."
    },
    {
        "type": "title",
        "title": "The difference wasn't my skills",
        "subtitle": "The difference was my positioning. And positioning is LEARNABLE."
    },
    {
        "type": "content",
        "title": "So let me tell you something you need to hear",
        "body_text": "You're already qualified for $300K+ roles. You have the skills. You have the experience. You have the track record. You're not under-qualified. You're under-POSITIONED."
    },
    {
        "type": "content",
        "title": "Interview positioning means",
        "bullets": [
            "Instead of walking into an interview and hoping you say the right thing... You research what they're hiring for and prepare examples that position you as the solution",
            "Instead of talking about your generic experience... You translate your experience into THEIR language and THEIR problems",
            "Instead of being one of many candidates... You position yourself as THE obvious choice"
        ]
    },
    {
        "type": "content",
        "title": "Here's the secret",
        "body_text": "You don't need NEW skills to get $300K+ roles. You need to REPOSITION your existing skills. It's not about HAVING more. It's about POSITIONING what you have correctly."
    },
    {
        "type": "content",
        "title": "How do you position yourself for interviews?",
        "bullets": [
            "1. Research what THEY need - Understand their problems, their goals, their hiring criteria",
            "2. Map YOUR experience to THEIR needs - Find examples from your background that solve their problems",
            "3. Practice positioning your answers - Rehearse how you'll talk about your experience in their language"
        ]
    },

    # Simon's Story
    {
        "type": "quote",
        "quote": "Don't just take my word for it. Let me tell you about Simon."
    },
    {
        "type": "content",
        "title": "Simon's Before State",
        "body_text": "Simon was making $90,000 a year as an Account Executive in a telesales role. Good job. But the pay wasn't enough to meet his family's needs. He felt stuck. He'd been applying to higher-paying roles but kept getting rejected."
    },
    {
        "type": "content",
        "title": "Simon thought",
        "body_text": "'I'm in telesales. Nobody's going to hire me for a $280K enterprise role. I don't have the right experience.' Sound familiar? That's the 'I'm not qualified' belief. And it's what keeps people stuck in $90K roles when they could be making $300K."
    },
    {
        "type": "content",
        "title": "So I taught Simon the same framework I'd learned",
        "bullets": [
            "How to identify which skills translate from telesales to enterprise",
            "How to research what enterprise companies need",
            "How to position his experience as a solution to their problems",
            "How to prepare for interviews so he'd walk in positioned to win"
        ]
    },
    {
        "type": "content",
        "title": "Simon's Result",
        "body_text": "Within weeks of implementing the positioning strategies, Simon had interviews lined up. And he landed a job offer for $280,000. That's a $190,000 raise. Over 3x his previous income. Same person. Same core skills. Better positioning."
    },
    {
        "type": "content",
        "title": "Do you see the pattern?",
        "body_text": "I went from $130K to $514K with the same skills. Better positioning. Simon went from $90K to $280K with the same skills. Better positioning. This isn't luck. This isn't about being special. This is about mastering strategic positioning."
    },

    # Secret #2 Summary
    {
        "type": "title",
        "title": "Secret #2: You're Qualified. Just Mis-Positioned",
        "subtitle": "Positioning is a learnable skill"
    },
    {
        "type": "content",
        "title": "Now, I know what you're thinking",
        "body_text": "'Okay Terrance, I get it. Positioning beats performance. I'm already qualified. But I have a full-time job. I have a family. I don't have time to research companies and position myself for hours every day. And I can't afford to quit my job to search full-time. This sounds great, but is it realistic for MY situation?'"
    },

    # SECRET #3: EXTERNAL BELIEFS (Slides 76-100)
    {
        "type": "title",
        "title": "Secret #3",
        "subtitle": "The 30-Minutes-Per-Day System That Gets Results in Weeks, Not Years"
    },
    {
        "type": "content",
        "title": "Let me take you back to 2021",
        "body_text": "I'd just had my epiphany about positioning. I knew WHERE I wanted to be: companies like Google, Amazon, Salesforce. I knew WHAT I needed to do: position myself so they'd recruit me. But I had a problem..."
    },
    {
        "type": "content",
        "title": "The Obstacle",
        "body_text": "I was still working full-time at AT&T. 60-hour weeks. Quota to hit. Customers to manage. I had a wife and a young daughter. I didn't have 8 hours a day to job search. I couldn't quit my job and search full-time. I needed a way to do this while still employed. With limited time. Without burning out."
    },
    {
        "type": "content",
        "title": "And there was another problem",
        "body_text": "When I started researching how to get into top companies, everything I found said: 'You need connections at Google.' 'You need referrals to get past the ATS.' 'You need to network for months to build relationships.' I didn't have months. I didn't have connections. I needed a way to get results FAST."
    },
    {
        "type": "content",
        "title": "So I asked myself",
        "body_text": "What if I could create a systematic process that worked in 30 minutes per day? What if I could get in front of hiring managers at Google, Amazon, and Salesforce WITHOUT having connections there? What if I could do this while still employed, without anyone at AT&T knowing I was looking? Was that even possible?"
    },
    {
        "type": "content",
        "title": "That's when I had another epiphany",
        "body_text": "The reason 2,000 people apply to Google and only 20 get interviewed isn't just about qualifications. It's about mindshare. Most candidates are never considered not because they CAN'T do the role... But because they have ZERO mindshare with the person actually making the hiring decision."
    },
    {
        "type": "content",
        "title": "So I thought",
        "body_text": "What if I could gain mindshare with hiring managers at my target companies? What if I could position myself so that when they have an opening, they think of ME? What if I could do this systematically, predictably, in 30 minutes per day? That's when I created what I now call the Reverse Attraction Strategy."
    },
    {
        "type": "content",
        "title": "I created a simple plan",
        "body_text": "It took 30 minutes per day. I did it for just FIVE days. I targeted three companies: Google, Amazon, Salesforce. And I tracked what happened."
    },
    {
        "type": "content",
        "title": "By the end of those five days",
        "body_text": "I had interviews scheduled at Google, Amazon, AND Salesforce. Not just one interview. Three interviews. At the three best companies in tech sales. One week. 30 minutes per day. Zero connections. All three companies pursuing me."
    },
    {
        "type": "title",
        "title": "Access Beats Applications",
        "subtitle": "You can gain mindshare with the right hiring managers in 30 minutes per day"
    },
    {
        "type": "content",
        "title": "So what IS the Reverse Attraction Strategy?",
        "body_text": "It's simple: Instead of applying to jobs and hoping someone sees your resume... You gain mindshare with hiring managers BEFORE they post the job. Instead of competing with 2,000 applicants... You position yourself so hiring managers reach out to YOU when openings happen. Instead of chasing opportunities... You create a system where opportunities chase you."
    },
    {
        "type": "content",
        "title": "Here's why this strategy works",
        "body_text": "Hiring managers at top companies have a problem: They need great salespeople, but most of the applicants they see aren't qualified. They're drowning in unqualified applications while struggling to find great talent. When you position yourself strategically, you're solving THEIR problem. You become visible. You demonstrate value. You gain mindshare. And when they have an opening, they think of YOU first."
    },

    # The P.R.I.N.T System
    {
        "type": "content",
        "title": "The P.R.I.N.T System",
        "bullets": [
            "P - Profile Matching: Identify which companies/roles are your 'better boats'",
            "R - Reverse Attraction: Gain mindshare with hiring managers",
            "I - Interview Mastery: Position yourself to win interviews",
            "N - Negotiating the Offer: Use leverage to maximize comp",
            "T - Tell Your Story: Position your brand consistently"
        ]
    },
    {
        "type": "content",
        "title": "Why 30 minutes per day works",
        "body_text": "Because positioning isn't about VOLUME. It's about STRATEGY. You don't need to send 100 applications. You need to identify 5-10 target companies and position yourself strategically with each one. You don't need 8-hour days. You need 30 focused minutes doing the RIGHT activities. Quality over quantity. Strategy over effort."
    },
    {
        "type": "content",
        "title": "And here's the best part",
        "body_text": "You can do this while you're still employed. Nobody at your current company needs to know. You're not sending out hundreds of applications that can be traced back to you. You're strategically positioning yourself with a handful of target companies. 30 minutes per day. Before work. During lunch. After the kids go to bed. You stay employed with income and benefits while positioning yourself for your next $75K-$125K raise."
    },

    # Darrell's Story
    {
        "type": "quote",
        "quote": "Let me tell you about Darrell. Darrell was in the EXACT situation many of you are in right now."
    },
    {
        "type": "content",
        "title": "Darrell's Before State",
        "body_text": "Darrell was at AT&T making $100,000 as an Account Manager. He felt stuck. Underpaid. But he didn't see a path out. He had a full-time job. He had bills. He couldn't just quit and search full-time. Sound familiar?"
    },
    {
        "type": "content",
        "title": "So I taught Darrell the P.R.I.N.T system",
        "body_text": "He identified his target companies. He implemented the Reverse Attraction strategy—30 minutes per day. He prepared for interviews using the positioning framework. All while still working full-time at AT&T."
    },
    {
        "type": "content",
        "title": "Darrell's First Result",
        "body_text": "Within weeks, Darrell had interviews lined up. He landed an offer for $90,000 more than he was making. $100K to $190K. 30 minutes per day. Still employed. First major raise."
    },
    {
        "type": "content",
        "title": "But here's what's even better",
        "body_text": "A year later, Darrell used the SAME EXACT METHOD to get another raise. Another $80,000 increase plus a $70,000 stock bonus. Because once you master positioning, you can use it again and again. Darrell went from $100K to $340K in two years using this system."
    },
    {
        "type": "content",
        "title": "Look at the pattern",
        "bullets": [
            "I used this system: $130K → $514K. While employed.",
            "Simon used this system: $90K → $280K. While employed.",
            "Darrell used this system: $100K → $340K. While employed. Twice.",
            "Same system. Same time commitment. 30 minutes per day. Multiple people. Repeatable results."
        ]
    },
    {
        "type": "content",
        "title": "Why does this system work so fast?",
        "body_text": "Because you're not competing with 2,000 applicants. You're gaining mindshare with hiring managers before the job is even posted. You're positioning yourself as a solution to their problem. You're becoming a CANDIDATE they recruit, not an APPLICANT they filter. That's why you can get results in weeks instead of months or years."
    },

    # Secret #3 Summary
    {
        "type": "title",
        "title": "Secret #3: Access Beats Applications",
        "subtitle": "30 Min/Day × 90 Days = $75K-$125K Income Increase"
    },
    {
        "type": "content",
        "title": "So now you know the three secrets",
        "bullets": [
            "Secret #1: Positioning beats performance. Your income is determined by your market positioning.",
            "Secret #2: You're already qualified. You just need to position what you have correctly.",
            "Secret #3: You can do this in 30 minutes per day while still employed using the P.R.I.N.T system.",
            "Once you accept these three beliefs, increasing your income by $75K-$125K becomes inevitable."
        ]
    },
    {
        "type": "content",
        "title": "So the question now isn't WHETHER this works",
        "body_text": "The question is: How do you actually DO this? How do you implement the P.R.I.N.T system? How do you position yourself to increase your income by $75K-$125K in 90 days or less? That's what I want to show you next..."
    },

    # TIER 1 FUTURE PACING: Pre-Stack Vision (Slides 101-104)
    {
        "type": "content",
        "title": "One year from now",
        "body_text": "Before I show you how this works, let me paint you a picture of where you'll be one year from today if you commit to mastering strategic positioning. One year from now, you're not at the same company making the same money feeling the same frustration. You're at a company that values you. You're making $75,000-$125,000 more per year. But here's what nobody tells you about that raise—it's not just about the money. It's about having positioned yourself in a market where that income is NORMAL, not exceptional."
    },
    {
        "type": "content",
        "title": "It's Friday at 4:45 PM",
        "body_text": "Your coworkers are still online—they'll be grinding until 7 PM. But you're shutting down your laptop. Because at this company, they don't measure your value by how many hours you work. They measure your value by the results you drive. You actually GET to have dinner with your family. On a weekday. You're not stressed. You're not burned out. You're not wondering if there's something better out there. Because you KNOW you're in the right place."
    },
    {
        "type": "content",
        "title": "But here's the best part",
        "body_text": "You're not worried about job security anymore. Because you now have a skill that nobody can take away from you. You know how to position yourself strategically. You know how to get recruited. You know how to interview. You know how to negotiate. If you ever wanted to leave, you could have three offers in 60 days. That confidence—that knowing you're ALWAYS in control of your career—changes everything. That's what mastering positioning gives you. That's the real value."
    },
    {
        "type": "content",
        "title": "So the question is",
        "body_text": "Do you want to still be where you are now, one year from today? Or do you want to be THERE—in that life, with that income, with that confidence? If the answer is the second one, here's what we've created..."
    },

    # STACK & OFFER (Slides 105-150)
    {
        "type": "title",
        "title": "The Active Offer System",
        "subtitle": "Complete Positioning Mastery Program"
    },
    {
        "type": "quote",
        "quote": "We've taken everything I've learned—everything that took me from $130K to over $1M in compensation... Everything Simon used to 3x his income... Everything Darrell used to get $170K in raises... And we've packaged it into a complete system called The Active Offer System."
    },
    {
        "type": "quote",
        "quote": "Here's what's included when you join The Active Offer System..."
    },

    # Component breakdown
    {
        "type": "content",
        "title": "Component #1: Profile Matching",
        "body_text": "This is where we help you identify which companies are your 'better boats.' Not random companies. Not spray-and-pray. We use our network, industry insights, and market data to identify the 5-10 companies that will pay you $300K+ for your specific skillset. If you tried to research this yourself, it would take months and you'd likely target the wrong companies. We do this for you in week one. Value if purchased separately: $5,000"
    },
    {
        "type": "content",
        "title": "Component #2: The Reverse Attraction System",
        "body_text": "This is the exact 30-minutes-per-day system I used to get interviews at Google, Amazon, and Salesforce in one week. You'll get: The exact scripts that land interviews. The messaging templates that gain mindshare with hiring managers. The step-by-step process to implement while still employed. This is the system that creates the 'companies recruiting you' transformation. Value if purchased separately: $7,500"
    },
    {
        "type": "content",
        "title": "Component #3: Interview Mastery Training",
        "body_text": "Remember my story about bombing the first Salesforce interview and then crushing the second? This is how I did it. You'll get: The exact interview preparation framework. Company-specific interview assets (30-60-90 day plans, presentation templates). The questions top companies ask and how to position your answers. Real interview examples from Google, Amazon, Salesforce, and more. This is what transforms you from someone who GETS interviews to someone who WINS them. Value if purchased separately: $8,000"
    },
    {
        "type": "content",
        "title": "Component #4: Negotiation Mastery",
        "body_text": "This is how Darrell got a $90K raise on his first offer. This is how Simon negotiated from $90K to $280K. You'll learn: How to create leverage using multiple offers. The exact negotiation frameworks that get $75K-$125K raises. What to say, when to say it, and how to position your value. Real compensation negotiation support when you get your offers. Most people leave $50K-$100K on the table because they don't know how to negotiate from a position of strength. This component alone could be worth 10x your investment. Value if purchased separately: $10,000"
    },
    {
        "type": "content",
        "title": "Component #5: Live Group Coaching",
        "body_text": "You'll have access to me and our team twice per week for live coaching. Bring your questions. Get feedback on your positioning. Workshop your interview prep. Get real-time support. This isn't pre-recorded content you watch alone. This is live, ongoing support as you implement the system. Value for 90 days if purchased separately: $12,000"
    },
    {
        "type": "content",
        "title": "Component #6: Private Community Access",
        "body_text": "You'll join a community of ambitious sales professionals all mastering positioning together. Network with people who are going through the same transformation. Get referrals. Share wins. Learn from each other's experiences. Many of our members have connected and referred each other into roles at top companies. Value if purchased separately: $3,000"
    },
    {
        "type": "content",
        "title": "Component #7: Complete Resource Library",
        "body_text": "You'll get every template, script, and asset we've ever created: Resume templates optimized for ATS and tech sales. LinkedIn profile audit checklist and optimization templates. Cold email and LinkedIn message vault (200+ tested messages). Interview question database for top companies (Google, Amazon, Salesforce, etc.). 30-60-90 day plan templates. Presentation templates for interviews. Self-accountability tracking system. Everything you need to implement the P.R.I.N.T system. Value if purchased separately: $5,000"
    },

    # Total Value & Investment
    {
        "type": "content",
        "title": "Total Value",
        "bullets": [
            "Profile Matching: $5,000",
            "Reverse Attraction System: $7,500",
            "Interview Mastery Training: $8,000",
            "Negotiation Mastery: $10,000",
            "Live Group Coaching (90 days): $12,000",
            "Private Community Access: $3,000",
            "Complete Resource Library: $5,000",
            "TOTAL VALUE: $50,500"
        ]
    },
    {
        "type": "content",
        "title": "Your Investment",
        "body_text": "Now, if I wanted to, I could charge $50,000 for this program. And honestly? If it increases your income by just $100K, you'd make your money back in the first year. But I'm not going to charge you $50,000. I'm not even going to charge you $25,000. Your investment to join The Active Offer System is $5,000."
    },
    {
        "type": "content",
        "title": "Payment Plan Option",
        "body_text": "And if $5,000 all at once feels like too much, we have payment plans available. You can split it into monthly payments. That's less than $200 per week to master the skill that will control your income for the rest of your career."
    },

    # ROI Framing
    {
        "type": "content",
        "title": "Let's talk about ROI",
        "body_text": "If you're making $150K now, and this gets you a $100K raise (within the $75K-$125K range our students achieve), that's $250K total compensation. Over the next 5 years, that's $500,000 in additional income. Over your career? $2-3 million more. Your investment today is $5,000. That's a 20x return in year one. 100x return over five years. This isn't an expense. This is the highest-ROI investment you'll ever make."
    },
    {
        "type": "content",
        "title": "Cost of Inaction",
        "body_text": "Now let's look at the cost of doing NOTHING: If you stay at $150K for the next 5 years while your peers who master positioning move to $250K+ roles (a $100K increase within our typical $75K-$125K range)... You've lost $500,000. Not making a decision IS a decision. The question isn't 'Can I afford this?' The question is 'Can I afford NOT to do this?'"
    },

    # Guarantee
    {
        "type": "content",
        "title": "And here's the thing: You're not taking any risk",
        "body_text": "If you join The Active Offer System, implement the strategies, show up to the coaching calls, and don't see results... I'll personally work with you until you do. You're either increasing your income by $75K-$125K, or you're getting more support until you are. That's my commitment to you."
    },

    # Qualification
    {
        "type": "content",
        "title": "Who This Is For",
        "bullets": [
            "Experienced sales professionals currently making $80K+",
            "Want to increase income by $75K-$125K by positioning for $250K-$400K+ roles",
            "At least 4 years of sales experience in B2B sales",
            "Willing to invest 30 minutes per day for 90 days",
            "Ready to stop working harder and start positioning smarter"
        ]
    },
    {
        "type": "content",
        "title": "This is NOT for",
        "bullets": [
            "People just starting in sales",
            "People making under $80K who don't have the experience yet",
            "People who want a magic button that requires no work",
            "People who aren't willing to invest 30 minutes per day"
        ]
    },

    # Application Process
    {
        "type": "content",
        "title": "The Application Process",
        "body_text": "So here's how this works: This isn't a 'buy now' button. Because I only want to work with people who are the right fit, and I want to make sure YOU feel good about this decision too. So the next step is to book a free strategy call. On that call, we're going to: Map out your ideal role (compensation, company, lifestyle). Identify the positioning gaps keeping you stuck. Show you the roadmap to your $75K-$125K income increase. Determine if The Active Offer System is the right fit. If it's a great fit for both of us, we'll invite you to join. If not, you'll still walk away with a clear action plan."
    },
    {
        "type": "content",
        "title": "What Happens on the Call",
        "body_text": "The strategy call is simple: We'll spend 45 minutes mapping out your situation. You'll tell me where you are, where you want to be, and what's been holding you back. I'll show you exactly how someone in your situation can use strategic positioning to increase their income by $75K-$125K. You'll walk away with clarity on your next steps—whether you join The Active Offer System or not. No pressure. No manipulation. Just clarity on how positioning can transform your career."
    },

    # Urgency
    {
        "type": "content",
        "title": "Limited Availability",
        "body_text": "Now, I need to be transparent with you: I can only work with a limited number of people at a time. Between the live coaching calls twice per week and the personal support we provide, I can only take on 15 new members per month. That means there are only a limited number of strategy call slots available. If you're serious about increasing your income by $75K-$125K in the next 90 days, you need to book your call today. Spots fill up quickly, and if you wait, you might have to wait until next month."
    },
    {
        "type": "content",
        "title": "Cost of Delay",
        "body_text": "And here's the other thing to consider: Every month you wait is another month at your current income. If you could be earning $10K more per month (a $120K annual increase, which is within our typical $75K-$125K range)... That's $10,000 per month you're leaving on the table. Waiting 3 months to decide costs you $30,000. Waiting a year costs you $120,000. How much is procrastination costing you?"
    },

    # Final CTAs
    {
        "type": "content",
        "title": "45 Days After the Call",
        "body_text": "And 45 days after that call—if you decide to join us—you'll be sitting in your first interview with a company that's excited to meet you. Not because you applied online and got lucky. Because you positioned yourself strategically and they recruited you. That's when you'll know this was the right decision. That's when you'll see the Positioning Principle working in your life."
    },
    {
        "type": "content",
        "title": "Remember",
        "bullets": [
            "I did this. $130K to $514K.",
            "Simon did this. $90K to $280K.",
            "Darrell did this. $100K to $340K. Twice.",
            "This system works. The only question is: Will you be next?"
        ]
    },
    {
        "type": "content",
        "title": "The Choice",
        "body_text": "So you have a choice to make right now: Choice #1: Close this webinar. Go back to your current situation. Keep doing what you've been doing. And hope things change on their own. Choice #2: Book a free strategy call. Get clarity on how positioning can increase your income by $75K-$125K. And if it's the right fit, join The Active Offer System and master the skill that will control your income for the rest of your life. Which choice are you going to make?"
    },
    {
        "type": "title",
        "title": "BOOK YOUR FREE STRATEGY CALL",
        "subtitle": "Limited Slots Available"
    },
    {
        "type": "content",
        "title": "Click the button and book your call",
        "body_text": "You'll pick a time that works for you—probably sometime in the next 7 days. You'll hop on Zoom with me or someone from my team. We'll map out your exact situation and show you the roadmap to your $75K-$125K income increase. And if The Active Offer System is the right fit, we'll invite you to join. It starts with clicking the button below."
    },
    {
        "type": "title",
        "title": "BOOK YOUR FREE POSITIONING ASSESSMENT",
        "subtitle": "And Let's Increase Your Income by $75K-$125K in the Next 90 Days"
    },
    {
        "type": "title",
        "title": "Thank you for watching",
        "subtitle": "Book your free strategy call below"
    },
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
        elif slide_data["type"] == "quote":
            img = create_quote_slide(slide_data["quote"])
        elif slide_data["type"] == "big_number":
            img = create_big_number_slide(
                slide_data["number"],
                slide_data.get("context", "")
            )
        elif slide_data["type"] == "content":
            img = create_content_slide(
                slide_data["title"],
                slide_data.get("bullets"),
                slide_data.get("body_text")
            )

        # Save slide
        filename = f"{i}.png"
        filepath = os.path.join(output_dir, filename)
        img.save(filepath, "PNG", quality=95)
        print(f"  Saved: {filename}")

    print(f"\n✓ Successfully generated {len(slides_content)} slides")
    print(f"✓ Output directory: {output_dir}")

if __name__ == "__main__":
    output_directory = "/Users/terrancebrandon/Desktop/Active Offer/AO- Course Content/Active Offer- Course Material/Webinar-v4.1-Slides"
    generate_slides(output_directory)
