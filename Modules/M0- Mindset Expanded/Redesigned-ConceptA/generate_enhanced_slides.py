"""
Enhanced Slide Generation with Vector Graphics
Concept A: Executive Minimalism with Professional Vector Icons
Generates all 57 slides with custom vector graphics for premium appearance
"""

from PIL import Image, ImageDraw, ImageFont
import textwrap
from vector_graphics_pil import create_icon, create_decorative_corner

# Image dimensions
WIDTH = 1920
HEIGHT = 1080

# Concept A: Executive Minimalism Colors
BG_LIGHT = (245, 245, 245)  # Light gray background
BG_DARK = (26, 31, 46)  # Deep navy
TEXT_DARK = (26, 31, 46)  # Deep navy text
TEXT_LIGHT = (255, 255, 255)  # White text
ACCENT_GOLD = (212, 175, 55)  # Gold accent

# Load fonts
try:
    FONT_TITLE = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 64)
    FONT_TITLE_LARGE = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 72)
    FONT_BODY = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 32)
    FONT_BODY_BOLD = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 32)
    FONT_BODY_SMALL = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 28)
    FONT_ICON_LABEL = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 24)
except:
    FONT_TITLE = FONT_TITLE_LARGE = FONT_BODY = FONT_BODY_BOLD = FONT_BODY_SMALL = FONT_ICON_LABEL = ImageFont.load_default()

MARGIN = 120
ICON_SIZE = 80  # Standard icon size


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


def add_decorative_corners(img, size=100):
    """Add subtle decorative corners to title slides"""
    corner = create_decorative_corner(size=size, color_rgb=ACCENT_GOLD, style='lines')

    # Top left corner
    img.paste(corner, (30, 30), corner)

    # Top right corner (flip horizontally)
    corner_right = corner.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    img.paste(corner_right, (WIDTH - size - 30, 30), corner_right)

    # Bottom left corner (flip vertically)
    corner_bottom_left = corner.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    img.paste(corner_bottom_left, (30, HEIGHT - size - 30), corner_bottom_left)

    # Bottom right corner (flip both)
    corner_bottom_right = corner.transpose(Image.Transpose.FLIP_LEFT_RIGHT).transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    img.paste(corner_bottom_right, (WIDTH - size - 30, HEIGHT - size - 30), corner_bottom_right)

    return img


def create_title_slide(title_text, slide_num, icon_name=None):
    """Create a title/section slide with dark background and optional icon"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)

    # Add decorative corners
    img = add_decorative_corners(img, size=100)

    # Wrap title text
    lines = wrap_text(title_text, FONT_TITLE_LARGE, WIDTH - (MARGIN * 2))

    # Calculate total height
    line_height = 90
    icon_space = 150 if icon_name else 0
    total_height = len(lines) * line_height
    start_y = (HEIGHT - total_height - icon_space) // 2

    # Draw icon above title if specified
    if icon_name:
        icon_img = create_icon(icon_name, size=120, color_rgb=ACCENT_GOLD)
        icon_x = (WIDTH - 120) // 2
        icon_y = start_y
        img.paste(icon_img, (icon_x, icon_y), icon_img)
        start_y += 150

    # Draw each line centered
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=FONT_TITLE_LARGE)
        text_width = bbox[2] - bbox[0]
        x = (WIDTH - text_width) // 2
        y = start_y + (i * line_height)
        draw.text((x, y), line, fill=TEXT_LIGHT, font=FONT_TITLE_LARGE)

    # Gold accent line above title (below icon if present)
    accent_width = 200
    accent_x = (WIDTH - accent_width) // 2
    accent_y = start_y - 50
    draw.rectangle([accent_x, accent_y, accent_x + accent_width, accent_y + 4], fill=ACCENT_GOLD)

    # Slide number in bottom right
    slide_text = f"{slide_num}"
    draw.text((WIDTH - MARGIN - 50, HEIGHT - MARGIN - 30), slide_text, fill=TEXT_LIGHT, font=FONT_BODY_SMALL)

    return img


def create_content_slide(title, bullets, slide_num, icon_name=None):
    """Create a standard content slide with bullets and optional header icon"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_LIGHT)
    draw = ImageDraw.Draw(img)

    # Draw header icon if specified
    title_y = MARGIN
    if icon_name:
        icon_img = create_icon(icon_name, size=60, color_rgb=ACCENT_GOLD)
        icon_x = MARGIN
        img.paste(icon_img, (icon_x, title_y), icon_img)
        title_x = MARGIN + 80
    else:
        title_x = MARGIN

    # Draw title
    draw.text((title_x, title_y), title, fill=TEXT_DARK, font=FONT_TITLE)

    # Draw bullets with custom gold bullet icons
    y_offset = MARGIN + 150
    bullet_spacing = 60

    for bullet in bullets:
        # Wrap bullet text if needed
        lines = wrap_text(bullet, FONT_BODY, WIDTH - MARGIN - 200)

        # Draw custom bullet point (small circle)
        bullet_r = 6
        bullet_center_y = y_offset + 16
        draw.ellipse([MARGIN, bullet_center_y - bullet_r,
                     MARGIN + bullet_r * 2, bullet_center_y + bullet_r * 2],
                    fill=ACCENT_GOLD)

        # Draw text
        for line in lines:
            draw.text((MARGIN + 30, y_offset), line, fill=TEXT_DARK, font=FONT_BODY)
            y_offset += 45

        y_offset += bullet_spacing - 45  # Adjust for multi-line

    # Slide number
    draw.text((WIDTH - MARGIN - 50, HEIGHT - MARGIN - 30), f"{slide_num}",
             fill=TEXT_DARK, font=FONT_BODY_SMALL)

    return img


def create_comparison_slide(title, old_beliefs, new_beliefs, slide_num):
    """Create split-screen comparison slide with transformation arrow"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_LIGHT)
    draw = ImageDraw.Draw(img)

    # Title with transformation icon
    icon_img = create_icon('transformation', size=60, color_rgb=ACCENT_GOLD)
    img.paste(icon_img, (MARGIN, MARGIN), icon_img)
    draw.text((MARGIN + 80, MARGIN), title, fill=TEXT_DARK, font=FONT_TITLE)

    # Vertical divider with decorative accent
    center_x = WIDTH // 2
    divider_top = MARGIN + 150
    divider_bottom = HEIGHT - MARGIN
    draw.line([center_x, divider_top, center_x, divider_bottom],
             fill=ACCENT_GOLD, width=3)

    # Draw small arrow on divider pointing right
    arrow_y = (divider_top + divider_bottom) // 2
    arrow_size = 40
    arrow_points = [
        (center_x - 20, arrow_y - 15),
        (center_x + 20, arrow_y),
        (center_x - 20, arrow_y + 15)
    ]
    draw.polygon(arrow_points, fill=ACCENT_GOLD)

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

    # Slide number
    draw.text((WIDTH - MARGIN - 50, HEIGHT - MARGIN - 30), f"{slide_num}",
             fill=TEXT_DARK, font=FONT_BODY_SMALL)

    return img


def create_framework_slide(title, pillars, pillar_content, slide_num):
    """Create three-pillar framework slide with pillar icons"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_LIGHT)
    draw = ImageDraw.Draw(img)

    # Title
    draw.text((MARGIN, MARGIN), title, fill=TEXT_DARK, font=FONT_TITLE)

    # Three pillars with icons
    start_y = MARGIN + 220
    box_width = 450
    box_height = 500
    spacing = 60

    total_width = (box_width * 3) + (spacing * 2)
    start_x = (WIDTH - total_width) // 2

    for i in range(3):
        box_x = start_x + (i * (box_width + spacing))

        # Draw pillar icon at top of box
        pillar_icon = create_icon('pillar', size=60, color_rgb=ACCENT_GOLD)
        pillar_icon_x = box_x + (box_width - 60) // 2
        img.paste(pillar_icon, (pillar_icon_x, start_y - 80), pillar_icon)

        # Draw box with gold border
        draw.rectangle([box_x, start_y, box_x + box_width, start_y + box_height],
                      outline=ACCENT_GOLD, width=3)

        # Pillar label
        label = pillars[i]
        bbox = draw.textbbox((0, 0), label, font=FONT_BODY_BOLD)
        label_width = bbox[2] - bbox[0]
        label_x = box_x + (box_width - label_width) // 2
        draw.text((label_x, start_y + 30), label, fill=ACCENT_GOLD, font=FONT_BODY_BOLD)

        # Content with custom bullets
        content_y = start_y + 100
        for item in pillar_content[i]:
            lines = wrap_text(item, FONT_BODY_SMALL, box_width - 60)
            for line_idx, line in enumerate(lines):
                if line_idx == 0:
                    # Draw bullet on first line
                    bullet_r = 4
                    bullet_y = content_y + 12
                    draw.ellipse([box_x + 30 - bullet_r, bullet_y - bullet_r,
                                 box_x + 30 + bullet_r, bullet_y + bullet_r],
                                fill=ACCENT_GOLD)
                    draw.text((box_x + 45, content_y), line, fill=TEXT_DARK, font=FONT_BODY_SMALL)
                else:
                    # Indent continuation lines
                    draw.text((box_x + 45, content_y), line, fill=TEXT_DARK, font=FONT_BODY_SMALL)
                content_y += 40
            content_y += 15

    # Slide number
    draw.text((WIDTH - MARGIN - 50, HEIGHT - MARGIN - 30), f"{slide_num}",
             fill=TEXT_DARK, font=FONT_BODY_SMALL)

    return img


def create_timeline_slide(title, days, activities, slide_num):
    """Create weekly timeline slide with calendar icon"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_LIGHT)
    draw = ImageDraw.Draw(img)

    # Title with calendar icon
    icon_img = create_icon('calendar', size=60, color_rgb=ACCENT_GOLD)
    img.paste(icon_img, (MARGIN, MARGIN), icon_img)
    draw.text((MARGIN + 80, MARGIN), title, fill=TEXT_DARK, font=FONT_TITLE)

    # Timeline with visual connectors
    start_y = MARGIN + 200
    day_height = 85

    for i, (day, activity) in enumerate(zip(days, activities)):
        y_pos = start_y + (i * day_height)

        # Timeline node (circle)
        node_x = MARGIN + 150
        node_r = 8
        draw.ellipse([node_x - node_r, y_pos + 10 - node_r,
                     node_x + node_r, y_pos + 10 + node_r],
                    fill=ACCENT_GOLD)

        # Day label with gold background
        day_bbox = draw.textbbox((0, 0), day, font=FONT_BODY_BOLD)
        day_width = day_bbox[2] - day_bbox[0]
        draw.rectangle([MARGIN, y_pos, MARGIN + day_width + 20, y_pos + 35],
                      fill=ACCENT_GOLD)
        draw.text((MARGIN + 10, y_pos), day, fill=TEXT_DARK, font=FONT_BODY_BOLD)

        # Activity
        activity_x = MARGIN + 300
        lines = wrap_text(activity, FONT_BODY, WIDTH - activity_x - MARGIN)
        for line in lines:
            draw.text((activity_x, y_pos), line, fill=TEXT_DARK, font=FONT_BODY)
            y_pos += 40

        # Connecting line to next node
        if i < len(days) - 1:
            line_start_y = start_y + (i * day_height) + 10 + node_r
            line_end_y = start_y + ((i + 1) * day_height) + 10 - node_r
            draw.line([node_x, line_start_y, node_x, line_end_y],
                     fill=ACCENT_GOLD, width=3)

    # Slide number
    draw.text((WIDTH - MARGIN - 50, HEIGHT - MARGIN - 30), f"{slide_num}",
             fill=TEXT_DARK, font=FONT_BODY_SMALL)

    return img


def create_icon_grid_slide(title, icon_items, slide_num, columns=4):
    """
    Create a slide with a grid of icons and labels
    icon_items: list of (icon_name, label) tuples
    """
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_LIGHT)
    draw = ImageDraw.Draw(img)

    # Title
    draw.text((MARGIN, MARGIN), title, fill=TEXT_DARK, font=FONT_TITLE)

    # Calculate grid layout
    content_start_y = MARGIN + 180
    content_width = WIDTH - (MARGIN * 2)
    content_height = HEIGHT - content_start_y - MARGIN - 50

    rows = (len(icon_items) + columns - 1) // columns
    cell_width = content_width // columns
    cell_height = content_height // rows

    # Draw each icon with label
    for idx, (icon_name, label) in enumerate(icon_items):
        row = idx // columns
        col = idx % columns

        # Calculate center position for this cell
        cell_center_x = MARGIN + (col * cell_width) + (cell_width // 2)
        cell_center_y = content_start_y + (row * cell_height) + (cell_height // 2)

        # Draw icon
        icon_img = create_icon(icon_name, size=ICON_SIZE, color_rgb=ACCENT_GOLD)
        icon_x = cell_center_x - (ICON_SIZE // 2)
        icon_y = cell_center_y - 60
        img.paste(icon_img, (icon_x, icon_y), icon_img)

        # Draw label
        bbox = draw.textbbox((0, 0), label, font=FONT_ICON_LABEL)
        label_width = bbox[2] - bbox[0]
        label_x = cell_center_x - (label_width // 2)
        label_y = icon_y + ICON_SIZE + 15
        draw.text((label_x, label_y), label, fill=TEXT_DARK, font=FONT_ICON_LABEL)

    # Slide number
    draw.text((WIDTH - MARGIN - 50, HEIGHT - MARGIN - 30), f"{slide_num}",
             fill=TEXT_DARK, font=FONT_BODY_SMALL)

    return img


# All slide content with icon assignments
slides_data = [
    # Slide 1 - Title
    ("title", "The Psychology of\nHigh-Ticket Job Searches", 1, "brain"),

    # Slide 2
    ("content", "Why Mindset Matters More Than Strategy", [
        "Your mindset determines your actions, and your actions determine your results",
        "Most job seekers focus on tactics but neglect the psychological foundation",
        "High-ticket roles require a different level of confidence and positioning",
        "Hiring managers can sense desperation, scarcity thinking, and lack of confidence",
        "Premium positioning starts in your mind before it shows up in your messaging"
    ], 2, "brain"),

    # Slide 3
    ("content", "The High-Ticket Job Search Mindset", [
        "You are interviewing the company as much as they are interviewing you",
        "You bring valuable skills and expertise that solve expensive business problems",
        "Scarcity vs. Abundance mindset comparison",
        "Your goal is to find the right high-value opportunity, not any job",
        "Confidence is not arrogance; it's knowing your worth"
    ], 3, "target"),

    # Slide 4
    ("content", "Common Psychological Barriers", [
        "Imposter syndrome",
        "Fear of rejection",
        "Salary anxiety",
        "Scarcity thinking",
        "Comparison trap"
    ], 4, "shield"),

    # Slide 5
    ("content", "The Cost of the Wrong Mindset", [
        "$50k-$200k+ per year in lost compensation",
        "$250k-$1M in lost lifetime earnings over 5 years",
        "1-2 years of career momentum wasted",
        "Tens of thousands left on the table in negotiations",
        "Your mindset compounds your success or stagnation"
    ], 5, "dollar_growth"),

    # Slide 6
    ("content", "Shifting to a High-Performer Mindset", [
        "View yourself as a business solving problems",
        "Approach interviews as collaborative discovery",
        "See compensation as a reflection of value created",
        "Embrace rejection as data and refinement",
        "Build evidence of your value"
    ], 6, "transformation"),

    # Slide 7
    ("content", "The Abundance Mentality in Job Search", [
        "Thousands of companies hiring for high-ticket sales roles",
        "Multiple opportunities create leverage",
        "You only need ONE great offer, but options give you power",
        "Abundance thinking makes you more attractive",
        "The right opportunity exists"
    ], 7, "growth_arrow"),

    # Slide 8
    ("content", "Reframing Rejection and Setbacks", [
        "Every 'no' brings you closer to the right 'yes'",
        "Rejection is feedback about fit, not worth",
        "Top performers get rejected often",
        "Use rejection to refine your approach",
        "The rejecting company might not be the right fit anyway"
    ], 8, "transformation"),

    # Slide 9
    ("content", "Building Psychological Resilience", [
        "Separate identity from job search outcomes",
        "Celebrate small wins",
        "Develop a support system",
        "Practice self-compassion",
        "Remember: building a career, not just finding a job"
    ], 9, "shield"),

    # Slide 10 - Title
    ("title", "Identifying Your\nLimiting Beliefs", 10, "unlock"),

    # Slide 11
    ("content", "What Are Limiting Beliefs?", [
        "Subconscious assumptions about yourself and what's possible",
        "Formed from past experiences, family messages, societal conditioning",
        "Feel like facts but are actually interpretations",
        "Create self-imposed ceilings on potential and income",
        "Most people are unaware of beliefs holding them back"
    ], 11, "brain"),

    # Slide 12
    ("content", "Common Limiting Beliefs in Job Search", [
        '"I\'m not qualified for roles at that level"',
        '"I don\'t have the right background or pedigree"',
        '"I\'m too old/young for that opportunity"',
        '"Companies won\'t pay me that much"',
        '"I\'m not good at interviews or selling myself"',
        '"I need more experience before I can make that move"'
    ], 12, "unlock"),

    # Slide 13
    ("content", "How Limiting Beliefs Sabotage Your Search", [
        "Don't apply to roles you're qualified for",
        "Undersell yourself in interviews and negotiations",
        "Accept lower compensation than you deserve",
        "Avoid uncomfortable growth-producing situations",
        "Create self-fulfilling prophecies"
    ], 13, None),

    # Slide 14
    ("content", "The Limiting Belief Identification Process", [
        "Step 1: Notice where you hesitate or avoid action",
        'Step 2: Ask "What would I have to believe to behave this way?"',
        "Step 3: Write down the belief and examine the evidence",
        "Step 4: Challenge with counter-evidence",
        "Step 5: Create new empowering belief with supporting evidence"
    ], 14, "checklist"),

    # Slide 15 - Comparison
    ("comparison", "Reframing Exercise", [
        '"I\'m not qualified"',
        '"I need more experience"',
        '"They won\'t pay me that much"',
        '"I\'m bad at interviews"',
        '"I don\'t have connections"'
    ], [
        '"I bring unique value they can\'t find elsewhere"',
        '"I have transferable skills that apply immediately"',
        '"I solve problems worth far more than my salary"',
        '"I\'m learning and improving with each conversation"',
        '"I\'m building relationships strategically"'
    ], 15),

    # Slide 16
    ("content", "Evidence Collection: Building Your Case", [
        "Document past wins",
        "Quantify your impact",
        "Collect testimonials and recommendations",
        "Identify skills others pay you for advice on",
        "Notice when people come to you for help"
    ], 16, "checklist"),

    # Slide 17
    ("content", "The Power of Borrowed Belief", [
        "Borrow belief from others who believe in you",
        "Study people with your background who landed the roles you want",
        "Find mentors who see potential you can't see yet",
        "Join communities of people pursuing similar goals",
        "Use their success as evidence of what's possible"
    ], 17, "network"),

    # Slide 18
    ("content", "Daily Practice: Belief Reinforcement", [
        "Morning: Review empowering beliefs and evidence",
        "During job search: Notice and reframe limiting beliefs",
        "After interactions: Collect evidence of your value",
        "Evening: Reflect on moments you showed up despite fear",
        "Weekly: Update evidence journal with wins and insights"
    ], 18, "checklist"),

    # Slide 19 - Title
    ("title", "Building Unshakeable\nConfidence", 19, "confidence"),

    # Slide 20
    ("content", "What Is True Confidence?", [
        "Not arrogance or bravado - quiet self-assurance",
        "Belief that you can handle whatever comes",
        "Comes from evidence and preparation, not positive thinking alone",
        "Being comfortable with uncertainty and embracing growth",
        "A skill you build through action, not something you wait to feel"
    ], 20, "confidence"),

    # Slide 21
    ("content", "The Confidence-Action Cycle", [
        "Most people think: Confidence → Action → Results",
        "Reality: Action → Results → Confidence",
        "Build confidence by taking action before you feel ready",
        "Each small action creates evidence that builds more confidence",
        "Waiting to feel confident keeps you stuck forever"
    ], 21, "transformation"),

    # Slide 22 - Framework
    ("framework", "The Three Pillars of Career Confidence",
     ["COMPETENCE", "PREPARATION", "EVIDENCE"],
     [
         ["Skills create value", "Expertise in areas", "Continuous learning", "Practice deliberately"],
         ["Research companies", "Prepare examples", "Practice pitch", "Anticipate objections"],
         ["Document wins", "Quantify results", "Save testimonials", "Review regularly"]
     ], 22),

    # Slide 23
    ("content", "Pillar 1: Building Competence", [
        "Master the fundamentals of your craft",
        "Develop expertise in specific areas",
        "Stay current with trends and best practices",
        "Invest in continuous learning",
        "Practice your skills deliberately and consistently"
    ], 23, "gear"),

    # Slide 24
    ("content", "Pillar 2: Rigorous Preparation", [
        "Research every company before engaging",
        "Prepare specific examples for common interview questions",
        "Practice your pitch, story, and value proposition",
        "Anticipate objections and prepare responses",
        "Mock interviews and role plays build readiness"
    ], 24, "checklist"),

    # Slide 25
    ("content", "Pillar 3: Collecting Evidence", [
        'Create a "wins document" tracking every success',
        "Quantify your achievements",
        "Save testimonials and positive feedback",
        "Document problems solved and value created",
        "Review this evidence regularly"
    ], 25, "trophy"),

    # Slide 26
    ("content", "Confidence-Building Exercises", [
        "Power posing: 2 minutes before interviews",
        "Visualization: See yourself succeeding",
        "Affirmations grounded in evidence",
        "Recall past wins",
        "Preparation rituals"
    ], 26, "lightbulb"),

    # Slide 27
    ("content", "Overcoming Confidence Killers", [
        "Comparison: Focus on your own progress",
        "Perfectionism: Done is better than perfect",
        "Negative self-talk: Catch it, challenge it, replace it",
        "Past failures: Reframe as learning experiences",
        "Fear of judgment: Most people are focused on themselves"
    ], 27, "shield"),

    # Slide 28
    ("content", "Confidence in High-Stakes Situations", [
        "Nervousness is normal - even top performers feel it",
        "Channel nervous energy into enthusiasm",
        "Focus on serving and helping, not proving yourself",
        "Remember: You're evaluating them too",
        "Your preparation will carry you through"
    ], 28, "mountain"),

    # Slide 29
    ("content", "The Compound Effect of Small Confidence Wins", [
        "Send one message today, even if imperfect",
        "Schedule one informational interview this week",
        "Apply to one role that feels slightly out of reach",
        "Ask one question that shows strategic thinking",
        "Each small action builds evidence and momentum",
        "Six months of small actions creates massive transformation"
    ], 29, "growth_arrow"),

    # Slide 30
    ("content", "Maintaining Confidence Through Challenges", [
        "Setbacks don't erase your capabilities",
        "Confidence fluctuates - that's normal",
        "Return to your evidence journal when doubt creeps in",
        "Seek support during difficult moments",
        "Your track record speaks louder than any single setback"
    ], 30, "shield"),

    # Slide 31 - Title
    ("title", "7 Success Habits to\nDevelop Now", 31, "rocket"),

    # Slide 32
    ("content", "Success Habit #1: Have A Specific Vision", [
        "Most people don't have a specific vision",
        "What do you want? When? Why?",
        "Clarity of vision helps you keep going when things get hard",
        "Vision is about what you're EXCLUDING",
        "My Challenge: Think about and decide your vision"
    ], 32, "compass"),

    # Slide 33
    ("content", "Creating Your Career Vision", [
        "Define your ideal role",
        "Set specific income goals",
        "Identify your timeline",
        "Clarify your why",
        "Write it down and review daily"
    ], 33, "target"),

    # Slide 34
    ("content", "Success Habit #2: Stop Negotiating With Yourself", [
        "How many times do you negotiate with yourself daily?",
        "When the alarm goes off...do you wake up?",
        "When you say you'll go to the gym...do you?",
        "When you write down goals...do you accomplish them?",
        "When you say you'll do more prospecting...do you?",
        "When you say 100% every day...do you do it?"
    ], 34, None),

    # Slide 35
    ("content", "Building Non-Negotiable Standards", [
        "Self-trust is built through keeping promises to yourself",
        "Every negotiation with yourself erodes self-confidence",
        "Successful people eliminate decision fatigue",
        "Your job search commitments: daily outreach, weekly applications",
        "Momentum from keeping promises compounds into success"
    ], 35, "confidence"),

    # Slide 36
    ("content", "Success Habit #3: Soft Skills Vs. Hard Skills", [
        "Hard skills: tactical stuff you'd do to get sales (can buy)",
        "Soft skills: you CAN'T buy...you have to develop",
        "Soft skills: relationship with money, emotional discipline, pressure handling",
        "Soft skills are always the limiting factor",
        "Confidence is one of the biggest soft skills"
    ], 36, "brain"),

    # Slide 37
    ("content", "Developing Critical Soft Skills for Job Search", [
        "Emotional regulation: staying calm during rejection",
        "Relationship building: genuine connections",
        "Communication: articulating your value clearly",
        "Resilience: bouncing back from setbacks",
        "Strategic thinking: positioning as problem-solver"
    ], 37, "network"),

    # Slide 38
    ("content", "Success Habit #4: Take Extreme Ownership", [
        "Most people place blame on everything and everyone else",
        "The moment you stop and realize everything starts and stops with you...",
        "...success will explode",
        "Take accountability for your success",
        "Realize nobody is beyond suffering and setbacks"
    ], 38, "confidence"),

    # Slide 39
    ("content", "Extreme Ownership in Your Job Search", [
        "Your results are a direct reflection of your actions",
        "Not getting interviews? Your approach needs improvement",
        "Not getting offers? Your skills need refinement",
        "Not getting the salary you want? Your negotiation needs work",
        "Taking ownership gives you power to change outcomes"
    ], 39, "gear"),

    # Slide 40
    ("content", "Success Habit #5: Don't Think of Success as Linear", [
        "Most people think of success as a start and a finish. It's not.",
        "When people think like that...they end up starting many things",
        "...and finishing nothing",
        "For example, switching businesses, methods, courses, etc.",
        "Instead, think of success as planting seeds...then watering and harvesting"
    ], 40, None),

    # Slide 41
    ("content", "The Non-Linear Path to Career Success", [
        "Job search progress is not a straight line",
        "Weeks of silence can be followed by multiple opportunities",
        "Trust the process even when results aren't visible",
        "Your consistent actions are accumulating",
        "Stay committed for at least 60-90 days before pivoting"
    ], 41, "growth_arrow"),

    # Slide 42
    ("content", "Success Habit #6: Questions Not Statements", [
        "Asking questions opens the mind to solutions",
        "Statements close the mind to possibility of solutions",
        'Train yourself to say "how can I?" instead of "I can\'t"',
        '"How can I scale this offer up?" vs. "I can\'t scale this offer up"'
    ], 42, "lightbulb"),

    # Slide 43
    ("content", "Empowering Questions for Job Search", [
        'Instead of "I can\'t get interviews" → "How can I improve my approach?"',
        'Instead of "I\'m not qualified" → "How can I position my experience?"',
        'Instead of "I won\'t get that salary" → "How can I negotiate effectively?"',
        'Instead of "I don\'t have connections" → "How can I build relationships?"',
        "Questions activate problem-solving; statements activate defensiveness"
    ], 43, "transformation"),

    # Slide 44
    ("content", "Success Habit #7: Be A Shark", [
        "What do sharks do?",
        "Does the shark ever wake up and decide not to do shark things that day? No!",
        "Same goes for you as a salesperson and entrepreneur",
        "Get up every day and do whatever it takes to be successful",
        "Hunt down your goals with the same ferocity that a shark would"
    ], 44, None),

    # Slide 45
    ("content", "Relentless Execution in Your Job Search", [
        "Show up every day with consistent effort",
        "Maintain your rhythm even during slow periods",
        "Follow up persistently but professionally",
        "Don't let rejection slow your momentum",
        "Success comes to those who refuse to quit"
    ], 45, "rocket"),

    # Slide 46 - Title
    ("title", "Creating Your Personal\nSuccess System", 46, "gear"),

    # Slide 47
    ("content", "Why Systems Beat Goals", [
        "Goals tell you where to go; systems get you there",
        "You don't rise to your goals - you fall to your systems",
        "Relying on motivation leads to inconsistent effort",
        "Systems create automatic progress regardless of how you feel",
        "Winners and losers have same goals; winners have better systems"
    ], 47, "gear"),

    # Slide 48
    ("content", "The Components of a Success System", [
        "DAILY HABITS: Non-negotiable actions every single day",
        "WEEKLY RHYTHMS: Recurring activities that move you forward",
        "TRACKING METRICS: Data showing progress and improvement areas",
        "FEEDBACK LOOPS: Regular review and adjustment",
        "ACCOUNTABILITY: People or systems keeping you honest"
    ], 48, "checklist"),

    # Slide 49
    ("content", "Your Daily Job Search System", [
        "Morning: Review vision and target company list (10 min)",
        "Mid-morning: 5 new LinkedIn connections or outreach messages (30 min)",
        "Afternoon: Research 2-3 target companies deeply (30 min)",
        "Evening: Update tracking spreadsheet and review progress (15 min)",
        "Total time investment: 85 minutes per day for career transformation"
    ], 49, "calendar"),

    # Slide 50 - Timeline
    ("timeline", "Your Weekly Job Search Rhythm",
     ["Monday", "Tuesday-Thursday", "Friday", "Saturday", "Sunday"],
     [
         "Set weekly goals and priority targets",
         "Execute daily system + 3-5 quality applications",
         "Review metrics, identify what worked, adjust",
         "Interview preparation and skill development",
         "Plan next week and recharge mentally"
     ], 50),

    # Slide 51
    ("content", "Essential Tracking Metrics", [
        "Outreach: Connection requests sent, messages sent, response rate",
        "Applications: Jobs applied to, interviews secured, conversion rate",
        "Interviews: Interviews completed, offer rate, feedback received",
        "Network: New connections made, informational interviews conducted",
        "Learning: Skills practiced, feedback implemented, improvements made",
        "What gets measured gets managed - and improved"
    ], 51, "metrics"),

    # Slide 52
    ("content", "Building Feedback Loops", [
        "Weekly self-review: What worked? What didn't? What will I test next?",
        "Track patterns: Which messages get responses? Which interviews go well?",
        "Seek external feedback: Mock interviews, message reviews, profile audits",
        "A/B test your approach",
        "Iterate rapidly based on data, not assumptions"
    ], 52, "transformation"),

    # Slide 53
    ("content", "Accountability Systems That Work", [
        "Find an accountability partner pursuing similar goals",
        "Schedule weekly check-ins to report progress",
        "Join a community of job seekers for mutual support",
        "Share your goals with mentors who will hold you to high standards",
        "Use the Active Offer Accountability Log",
        "Public commitment increases follow-through significantly"
    ], 53, "network"),

    # Slide 54
    ("content", "Designing Your Environment for Success", [
        "Remove distractions during dedicated job search time",
        "Create a workspace that signals focus and professionalism",
        "Use tools that make execution easier: templates, trackers, calendars",
        "Eliminate friction: Have everything prepared and ready",
        "Your environment should make good behaviors easy and bad behaviors hard"
    ], 54, "gear"),

    # Slide 55
    ("content", "The Power of Consistency Over Intensity", [
        "Working 1 hour daily for 90 days beats working 10 hours in one weekend",
        "Consistency builds momentum, skills, and relationships over time",
        "Intense bursts followed by inaction create poor results",
        "Your system should be sustainable long-term, not exhausting",
        "Small consistent actions compound into extraordinary outcomes"
    ], 55, "calendar"),

    # Slide 56
    ("content", "Your 90-Day Success System Implementation", [
        "Days 1-30: Build the habit, track everything, learn what works",
        "Days 31-60: Optimize based on data, increase volume, build momentum",
        "Days 61-90: Leverage your network and pipeline, multiple opportunities flowing",
        "This system, executed consistently, leads to interviews, offers, transformation",
        "Start today - your future self will thank you"
    ], 56, "rocket"),

    # Slide 57 - Title
    ("title", "You Now Have the Mindset\nFoundation for Success", 57, "trophy"),
]


def main():
    print("Generating all 57 slides with Concept A (Executive Minimalism + Vector Graphics)...")
    print("=" * 80)

    for slide_data in slides_data:
        slide_type = slide_data[0]
        slide_num = slide_data[-2] if slide_data[0] in ["comparison", "framework", "timeline"] else slide_data[-1]

        if slide_type == "title":
            _, title, num, icon = slide_data
            img = create_title_slide(title, num, icon)
        elif slide_type == "content":
            if len(slide_data) == 5:
                _, title, bullets, num, icon = slide_data
                img = create_content_slide(title, bullets, num, icon)
            else:
                _, title, bullets, num = slide_data
                img = create_content_slide(title, bullets, num, None)
        elif slide_type == "comparison":
            _, title, old, new, num = slide_data
            img = create_comparison_slide(title, old, new, num)
        elif slide_type == "framework":
            _, title, pillars, content, num = slide_data
            img = create_framework_slide(title, pillars, content, num)
        elif slide_type == "timeline":
            _, title, days, activities, num = slide_data
            img = create_timeline_slide(title, days, activities, num)

        filename = f"slide-{num:02d}.png"
        img.save(filename)
        title_preview = slide_data[1] if slide_type in ['title', 'content', 'comparison', 'framework', 'timeline'] else 'Special layout'
        if len(title_preview) > 50:
            title_preview = title_preview[:47] + "..."
        print(f"✓ Created: {filename} - {title_preview}")

    print("=" * 80)
    print(f"\n✅ Successfully generated all 57 slides with enhanced vector graphics!")
    print(f"📁 Location: M0- Mindset Expanded/Redesigned-ConceptA/")
    print(f"🎨 Design: Executive Minimalism with Custom Vector Icons")
    print(f"📊 Features:")
    print(f"   • 19 unique custom vector icons")
    print(f"   • Decorative corner elements on title slides")
    print(f"   • Enhanced visual hierarchy")
    print(f"   • Professional gold accents throughout")
    print(f"   • Context-specific icons for each major concept")


if __name__ == "__main__":
    main()
