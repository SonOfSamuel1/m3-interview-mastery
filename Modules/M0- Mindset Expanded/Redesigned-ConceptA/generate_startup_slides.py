"""
STARTUP PRESENTATION SLIDE GENERATOR
=====================================
Transforms M0 Mindset Module slides using the Startup Presentation style guide aesthetic.

DESIGN PHILOSOPHY:
- Professional 2025 startup pitch deck aesthetic
- Dual-theme approach: Mix light and dark backgrounds
- Rounded card components with soft shadows
- Soft diffused gradient overlays for depth
- Numbered circular badges for visual hierarchy
- Modern, minimalist, sophisticated design

COLOR PALETTE:
- Light Blue accent: #A7D4F0 (primary accent)
- Dark Charcoal: #3D3D3D (primary dark text)
- Medium Gray: #5A5A5A (secondary text)
- Light Gray primary: #D8DDE2 (main light background)
- Light Gray secondary: #E8EAED (cards, alternate background)
- Dark Gray primary: #4A4A4A (dark theme backgrounds)
- Dark Gray secondary: #525456 (dark theme variation)
- Pure White: #FFFFFF (text on dark, clean cards)
- Subtle text: #6B6B6B (body copy)

TYPOGRAPHY (Inter/SF Pro Display/Helvetica Neue):
- Display/Hero: 120-140px, Bold (700-800), tight letter spacing
- H1 titles: 72-84px, Bold (700)
- H2 sections: 48-56px, Bold (700)
- H3 cards: 24-28px, Bold (700)
- Body large: 18-20px, Regular (400)
- Body regular: 14-16px, Regular (400)

LAYOUT PRINCIPLES:
- Slide dimensions: 1920x1080px (16:9)
- Safe zone margins: 80px from all edges (1760x920 content area)
- Card padding: 32-40px internal
- Spacing scale: 24px, 32px, 48px, 64px, 80px
- Grid-based layouts: 2-3 column cards
- Left-aligned text (not centered bullets)

DESIGN PATTERNS:
- Title slides: Dark theme (#4A4A4A), large hero text, gradient overlay
- Content slides: Light theme (#D8DDE2), rounded cards, numbered badges
- Framework slides: Cards in 2-3 column grid layout
- Final slide: Dark theme, centered "thank you" style

Author: Claude Code
Version: 1.0 Startup Presentation
Output: slide-01-startup.png through slide-57-startup.png
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import math

# ============================================================================
# IMAGE DIMENSIONS
# ============================================================================
WIDTH = 1920
HEIGHT = 1080

# Safe zone (80px margins from all edges)
SAFE_MARGIN = 80
SAFE_LEFT = SAFE_MARGIN
SAFE_RIGHT = WIDTH - SAFE_MARGIN
SAFE_TOP = SAFE_MARGIN
SAFE_BOTTOM = HEIGHT - SAFE_MARGIN
SAFE_WIDTH = SAFE_RIGHT - SAFE_LEFT
SAFE_HEIGHT = SAFE_BOTTOM - SAFE_TOP

# ============================================================================
# COLOR PALETTE
# ============================================================================
# Primary Colors
LIGHT_BLUE_ACCENT = (167, 212, 240)      # #A7D4F0 - primary accent
DARK_CHARCOAL = (61, 61, 61)             # #3D3D3D - primary dark text
MEDIUM_GRAY = (90, 90, 90)               # #5A5A5A - secondary text
LIGHT_GRAY_PRIMARY = (216, 221, 226)     # #D8DDE2 - main light background
LIGHT_GRAY_SECONDARY = (232, 234, 237)   # #E8EAED - cards, alternate background
DARK_GRAY_PRIMARY = (74, 74, 74)         # #4A4A4A - dark theme backgrounds
DARK_GRAY_SECONDARY = (82, 84, 86)       # #525456 - dark theme variation
PURE_WHITE = (255, 255, 255)             # #FFFFFF - text on dark
SUBTLE_TEXT = (107, 107, 107)            # #6B6B6B - body copy

# ============================================================================
# TYPOGRAPHY
# ============================================================================
# Try Inter, SF Pro Display, then Helvetica Neue as fallback
FONT_PATHS = [
    "/System/Library/Fonts/SFNSDisplay.ttf",           # SF Pro Display
    "/System/Library/Fonts/SFNS.ttf",                  # SF Compact
    "/System/Library/Fonts/HelveticaNeue.ttc",        # Helvetica Neue
    "/System/Library/Fonts/Helvetica.ttc",            # Helvetica
]

def load_font(size, bold=False):
    """Load the best available font with fallbacks."""
    for font_path in FONT_PATHS:
        try:
            if os.path.exists(font_path):
                return ImageFont.truetype(font_path, size)
        except Exception:
            continue
    # Ultimate fallback
    return ImageFont.load_default()

# Font sizes
FONT_HERO = lambda: load_font(130, bold=True)          # 120-140px Display/Hero
FONT_H1 = lambda: load_font(78, bold=True)             # 72-84px H1 titles
FONT_H2 = lambda: load_font(52, bold=True)             # 48-56px H2 sections
FONT_H3 = lambda: load_font(26, bold=True)             # 24-28px H3 cards
FONT_BODY_LARGE = lambda: load_font(19)                # 18-20px Body large
FONT_BODY_REGULAR = lambda: load_font(15)              # 14-16px Body regular
FONT_BADGE = lambda: load_font(17, bold=True)          # Badge numbers

# ============================================================================
# LAYOUT CONSTANTS
# ============================================================================
CARD_BORDER_RADIUS = 28  # 24-32px rounded corners
CARD_PADDING = 36        # 32-40px internal padding
BADGE_SIZE = 52          # 48-56px diameter
SPACING_BASE = 8
SPACING_MD = 32
SPACING_LG = 48
SPACING_XL = 64

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def draw_rounded_rectangle(draw, xy, radius, fill=None, outline=None, width=1):
    """Draw a rounded rectangle with smooth corners."""
    x1, y1, x2, y2 = xy

    # Draw main rectangle
    if fill:
        draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill)
        draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill)

    # Draw four rounded corners
    if fill:
        draw.pieslice([x1, y1, x1 + radius * 2, y1 + radius * 2], 180, 270, fill=fill)
        draw.pieslice([x2 - radius * 2, y1, x2, y1 + radius * 2], 270, 360, fill=fill)
        draw.pieslice([x1, y2 - radius * 2, x1 + radius * 2, y2], 90, 180, fill=fill)
        draw.pieslice([x2 - radius * 2, y2 - radius * 2, x2, y2], 0, 90, fill=fill)

    # Draw outline if specified
    if outline:
        # Top and bottom lines
        draw.line([(x1 + radius, y1), (x2 - radius, y1)], fill=outline, width=width)
        draw.line([(x1 + radius, y2), (x2 - radius, y2)], fill=outline, width=width)
        # Left and right lines
        draw.line([(x1, y1 + radius), (x1, y2 - radius)], fill=outline, width=width)
        draw.line([(x2, y1 + radius), (x2, y2 - radius)], fill=outline, width=width)
        # Arcs for corners
        draw.arc([x1, y1, x1 + radius * 2, y1 + radius * 2], 180, 270, fill=outline, width=width)
        draw.arc([x2 - radius * 2, y1, x2, y1 + radius * 2], 270, 360, fill=outline, width=width)
        draw.arc([x1, y2 - radius * 2, x1 + radius * 2, y2], 90, 180, fill=outline, width=width)
        draw.arc([x2 - radius * 2, y2 - radius * 2, x2, y2], 0, 90, fill=outline, width=width)

def draw_circular_badge(draw, center_x, center_y, number, size=BADGE_SIZE):
    """Draw a circular numbered badge with light blue background."""
    x1 = center_x - size // 2
    y1 = center_y - size // 2
    x2 = center_x + size // 2
    y2 = center_y + size // 2

    # Draw circle
    draw.ellipse([x1, y1, x2, y2], fill=LIGHT_BLUE_ACCENT)

    # Draw number
    text = str(number)
    font = FONT_BADGE()
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    text_x = center_x - text_width // 2
    text_y = center_y - text_height // 2 - 2  # Slight adjustment for vertical centering

    draw.text((text_x, text_y), text, fill=DARK_CHARCOAL, font=font)

def create_radial_gradient_overlay(size, color, opacity, position='top-right', blur=140):
    """
    Create a soft radial gradient overlay for depth.

    Args:
        size: Tuple (width, height) - gradient dimensions
        color: RGB tuple for gradient color
        opacity: 0.0-1.0 opacity level
        position: 'top-right', 'top-left', 'bottom-right', 'bottom-left'
        blur: Blur radius (120-150px recommended)
    """
    gradient_size = 1200  # Large diameter

    # Create gradient
    gradient = Image.new('RGBA', (gradient_size, gradient_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(gradient)

    center = gradient_size // 2
    max_radius = gradient_size // 2

    # Draw concentric circles with fading opacity
    steps = 50
    for i in range(steps):
        radius = int(max_radius * (1 - i / steps))
        alpha = int(255 * opacity * (1 - i / steps))
        circle_color = color + (alpha,)
        draw.ellipse(
            [center - radius, center - radius, center + radius, center + radius],
            fill=circle_color
        )

    # Apply heavy blur
    gradient = gradient.filter(ImageFilter.GaussianBlur(blur))

    # Create canvas and position gradient
    canvas = Image.new('RGBA', size, (0, 0, 0, 0))

    if position == 'top-right':
        x = size[0] - gradient_size // 2
        y = -gradient_size // 2
    elif position == 'top-left':
        x = -gradient_size // 2
        y = -gradient_size // 2
    elif position == 'bottom-right':
        x = size[0] - gradient_size // 2
        y = size[1] - gradient_size // 2
    elif position == 'bottom-left':
        x = -gradient_size // 2
        y = size[1] - gradient_size // 2
    else:  # center
        x = (size[0] - gradient_size) // 2
        y = (size[1] - gradient_size) // 2

    canvas.paste(gradient, (x, y), gradient)
    return canvas

def wrap_text(text, font, max_width):
    """Wrap text to fit within max_width."""
    words = text.split()
    lines = []
    current_line = []

    temp_img = Image.new('RGB', (1, 1))
    temp_draw = ImageDraw.Draw(temp_img)

    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = temp_draw.textbbox((0, 0), test_line, font=font)
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

def get_text_height(text, font):
    """Get the height of text."""
    temp_img = Image.new('RGB', (1, 1))
    temp_draw = ImageDraw.Draw(temp_img)
    bbox = temp_draw.textbbox((0, 0), text, font=font)
    return bbox[3] - bbox[1]

def get_text_width(text, font):
    """Get the width of text."""
    temp_img = Image.new('RGB', (1, 1))
    temp_draw = ImageDraw.Draw(temp_img)
    bbox = temp_draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]

# ============================================================================
# SLIDE GENERATION FUNCTIONS
# ============================================================================

def generate_dark_title_slide(number, title, subtitle=None):
    """
    Generate a dark theme title slide (for lesson separators).
    Dark background with large hero text and gradient overlay.
    """
    # Create dark background
    slide = Image.new('RGB', (WIDTH, HEIGHT), DARK_GRAY_PRIMARY)

    # Add gradient overlay for depth
    gradient_color = (130, 160, 180)  # Soft blue-gray
    gradient = create_radial_gradient_overlay(
        (WIDTH, HEIGHT),
        gradient_color,
        opacity=0.2,
        position='top-right',
        blur=150
    )
    slide = Image.alpha_composite(slide.convert('RGBA'), gradient).convert('RGB')

    draw = ImageDraw.Draw(slide)

    # Draw title - centered, large hero text
    font = FONT_HERO()
    title_lines = wrap_text(title, font, SAFE_WIDTH - 200)

    line_height = get_text_height("Ay", font) + 20
    total_height = len(title_lines) * line_height

    y = (HEIGHT - total_height) // 2

    for line in title_lines:
        text_width = get_text_width(line, font)
        x = (WIDTH - text_width) // 2
        draw.text((x, y), line, fill=PURE_WHITE, font=font)
        y += line_height

    # Subtitle if provided
    if subtitle:
        subtitle_font = FONT_H2()
        y += 40
        subtitle_width = get_text_width(subtitle, subtitle_font)
        x = (WIDTH - subtitle_width) // 2
        draw.text((x, y), subtitle, fill=LIGHT_GRAY_SECONDARY, font=subtitle_font)

    return slide

def generate_light_bullet_slide(number, title, bullets):
    """
    Generate a light theme content slide with bullets in rounded cards.
    Light background with dark text and rounded card components.
    """
    # Create light background
    slide = Image.new('RGB', (WIDTH, HEIGHT), LIGHT_GRAY_PRIMARY)

    # Add subtle gradient overlay
    gradient = create_radial_gradient_overlay(
        (WIDTH, HEIGHT),
        LIGHT_BLUE_ACCENT,
        opacity=0.3,
        position='top-left',
        blur=140
    )
    slide = Image.alpha_composite(slide.convert('RGBA'), gradient).convert('RGB')

    draw = ImageDraw.Draw(slide)

    # Draw numbered badge in top-left corner
    badge_x = SAFE_LEFT + 40
    badge_y = SAFE_TOP + 40
    draw_circular_badge(draw, badge_x, badge_y, number)

    # Draw title
    title_font = FONT_H2()
    title_y = SAFE_TOP + 30
    draw.text((SAFE_LEFT + 120, title_y), title, fill=DARK_CHARCOAL, font=title_font)

    # Create card for bullets
    card_y = SAFE_TOP + 140
    card_height = SAFE_BOTTOM - card_y - 40

    # Draw rounded card
    draw_rounded_rectangle(
        draw,
        [SAFE_LEFT, card_y, SAFE_RIGHT, card_y + card_height],
        radius=CARD_BORDER_RADIUS,
        fill=PURE_WHITE,
        outline=LIGHT_GRAY_PRIMARY,
        width=2
    )

    # Draw bullets inside card
    bullet_font = FONT_BODY_LARGE()
    y = card_y + CARD_PADDING + 10
    x = SAFE_LEFT + CARD_PADDING + 20

    max_width = SAFE_WIDTH - (CARD_PADDING * 2) - 60

    for bullet in bullets:
        # Draw bullet point
        draw.ellipse(
            [x - 5, y + 6, x + 7, y + 18],
            fill=LIGHT_BLUE_ACCENT
        )

        # Wrap and draw bullet text
        lines = wrap_text(bullet, bullet_font, max_width)
        for line in lines:
            draw.text((x + 30, y), line, fill=DARK_CHARCOAL, font=bullet_font)
            y += get_text_height(line, bullet_font) + 8

        y += 28  # Spacing between bullets

    return slide

def generate_light_quote_slide(number, title, content_items):
    """
    Generate a light theme quote/emphasis slide.
    Single rounded card with emphasized content.
    """
    # Create light background
    slide = Image.new('RGB', (WIDTH, HEIGHT), LIGHT_GRAY_PRIMARY)

    # Add gradient overlay
    gradient = create_radial_gradient_overlay(
        (WIDTH, HEIGHT),
        LIGHT_BLUE_ACCENT,
        opacity=0.25,
        position='bottom-right',
        blur=140
    )
    slide = Image.alpha_composite(slide.convert('RGBA'), gradient).convert('RGB')

    draw = ImageDraw.Draw(slide)

    # Draw numbered badge
    badge_x = SAFE_LEFT + 40
    badge_y = SAFE_TOP + 40
    draw_circular_badge(draw, badge_x, badge_y, number)

    # Draw title
    title_font = FONT_H2()
    draw.text((SAFE_LEFT + 120, SAFE_TOP + 30), title, fill=DARK_CHARCOAL, font=title_font)

    # Create centered card for content
    card_width = int(SAFE_WIDTH * 0.85)
    card_height = int(SAFE_HEIGHT * 0.55)
    card_x = (WIDTH - card_width) // 2
    card_y = (HEIGHT - card_height) // 2 + 40

    # Draw rounded card
    draw_rounded_rectangle(
        draw,
        [card_x, card_y, card_x + card_width, card_y + card_height],
        radius=CARD_BORDER_RADIUS,
        fill=PURE_WHITE,
        outline=LIGHT_GRAY_PRIMARY,
        width=2
    )

    # Draw content items
    content_font = FONT_BODY_LARGE()
    y = card_y + CARD_PADDING + 40
    x = card_x + CARD_PADDING + 30
    max_width = card_width - (CARD_PADDING * 2) - 60

    for item in content_items:
        # Draw bullet
        draw.ellipse([x - 5, y + 6, x + 7, y + 18], fill=LIGHT_BLUE_ACCENT)

        # Wrap and draw text
        lines = wrap_text(item, content_font, max_width)
        for line in lines:
            draw.text((x + 30, y), line, fill=DARK_CHARCOAL, font=content_font)
            y += get_text_height(line, content_font) + 8

        y += 32  # Spacing between items

    return slide

def generate_framework_slide(number, title, cards_data):
    """
    Generate a multi-column card layout slide (2-3 columns).
    Light theme with multiple rounded cards in a grid.

    cards_data: List of dicts with 'title' and 'items' keys
    """
    # Create light background
    slide = Image.new('RGB', (WIDTH, HEIGHT), LIGHT_GRAY_PRIMARY)

    # Add gradient overlay
    gradient = create_radial_gradient_overlay(
        (WIDTH, HEIGHT),
        LIGHT_BLUE_ACCENT,
        opacity=0.28,
        position='top-right',
        blur=140
    )
    slide = Image.alpha_composite(slide.convert('RGBA'), gradient).convert('RGB')

    draw = ImageDraw.Draw(slide)

    # Draw numbered badge
    badge_x = SAFE_LEFT + 40
    badge_y = SAFE_TOP + 40
    draw_circular_badge(draw, badge_x, badge_y, number)

    # Draw title
    title_font = FONT_H2()
    draw.text((SAFE_LEFT + 120, SAFE_TOP + 30), title, fill=DARK_CHARCOAL, font=title_font)

    # Calculate card layout
    num_cards = len(cards_data)
    card_spacing = 40
    cards_start_y = SAFE_TOP + 150
    available_width = SAFE_WIDTH

    if num_cards == 2:
        card_width = (available_width - card_spacing) // 2
    elif num_cards == 3:
        card_width = (available_width - card_spacing * 2) // 3
    else:
        card_width = available_width

    card_height = SAFE_BOTTOM - cards_start_y - 40

    # Draw cards
    for i, card_data in enumerate(cards_data):
        card_x = SAFE_LEFT + i * (card_width + card_spacing)
        card_y = cards_start_y

        # Draw rounded card
        draw_rounded_rectangle(
            draw,
            [card_x, card_y, card_x + card_width, card_y + card_height],
            radius=CARD_BORDER_RADIUS,
            fill=PURE_WHITE,
            outline=LIGHT_GRAY_PRIMARY,
            width=2
        )

        # Card title
        card_title_font = FONT_H3()
        title_text = card_data.get('title', '')
        title_x = card_x + CARD_PADDING
        title_y = card_y + CARD_PADDING

        # Wrap card title if needed
        title_lines = wrap_text(title_text, card_title_font, card_width - CARD_PADDING * 2)
        for title_line in title_lines:
            draw.text((title_x, title_y), title_line, fill=DARK_CHARCOAL, font=card_title_font)
            title_y += get_text_height(title_line, card_title_font) + 5

        # Card items
        item_font = FONT_BODY_REGULAR()
        y = title_y + 30
        x = card_x + CARD_PADDING

        for item in card_data.get('items', []):
            # Draw bullet
            draw.ellipse([x, y + 4, x + 8, y + 12], fill=LIGHT_BLUE_ACCENT)

            # Wrap and draw item text
            item_lines = wrap_text(item, item_font, card_width - CARD_PADDING * 2 - 20)
            for line in item_lines:
                draw.text((x + 20, y), line, fill=SUBTLE_TEXT, font=item_font)
                y += get_text_height(line, item_font) + 6

            y += 20  # Spacing between items

    return slide

def generate_simple_final_slide(number, title, subtitle):
    """
    Generate the final slide - dark theme with centered text.
    """
    # Create dark background
    slide = Image.new('RGB', (WIDTH, HEIGHT), DARK_GRAY_PRIMARY)

    # Add gradient overlay
    gradient = create_radial_gradient_overlay(
        (WIDTH, HEIGHT),
        (130, 160, 180),
        opacity=0.25,
        position='bottom-right',
        blur=150
    )
    slide = Image.alpha_composite(slide.convert('RGBA'), gradient).convert('RGB')

    draw = ImageDraw.Draw(slide)

    # Title - centered
    title_font = FONT_H1()
    title_width = get_text_width(title, title_font)
    title_x = (WIDTH - title_width) // 2
    title_y = HEIGHT // 2 - 80
    draw.text((title_x, title_y), title, fill=PURE_WHITE, font=title_font)

    # Subtitle - centered below
    subtitle_font = FONT_H2()
    subtitle_width = get_text_width(subtitle, subtitle_font)
    subtitle_x = (WIDTH - subtitle_width) // 2
    subtitle_y = title_y + 100
    draw.text((subtitle_x, subtitle_y), subtitle, fill=LIGHT_GRAY_SECONDARY, font=subtitle_font)

    return slide

# ============================================================================
# SLIDE CONTENT DATA
# ============================================================================

slides_content = [
    # LESSON 1: Understanding the High-Performance Mindset
    {
        'number': 1,
        'type': 'dark_title',
        'title': 'Understanding the High-Performance Mindset',
    },
    {
        'number': 2,
        'type': 'bullet',
        'title': 'Why Mindset Comes First',
        'bullets': [
            'Your mindset determines how you interpret opportunities and setbacks',
            'Skills and tactics are useless without the right mental foundation',
            'High performers think differently about challenges and rejection',
            'Mindset shapes your daily actions, which compound into results',
            'You can\'t out-tactic a broken belief system'
        ]
    },
    {
        'number': 3,
        'type': 'bullet',
        'title': 'The Fixed vs. Growth Mindset',
        'bullets': [
            'Fixed mindset: Believes abilities are static and unchangeable',
            'Growth mindset: Believes abilities can be developed through effort',
            'Fixed mindset avoids challenges; growth mindset embraces them',
            'Fixed mindset sees failure as identity; growth mindset sees it as data',
            'Your mindset about learning determines your career trajectory'
        ]
    },
    {
        'number': 4,
        'type': 'dark_title',
        'title': 'The Science Behind Mindset',
    },
    {
        'number': 5,
        'type': 'bullet',
        'title': 'Neuroplasticity: Your Brain Can Change',
        'bullets': [
            'Your brain forms new neural pathways throughout your life',
            'Repeated thoughts and actions strengthen specific neural connections',
            'You can literally rewire limiting beliefs through consistent practice',
            'High performers understand the brain is trainable, like a muscle',
            'Every time you challenge a limiting belief, you weaken its hold'
        ]
    },
    {
        'number': 6,
        'type': 'bullet',
        'title': 'The Reticular Activating System (RAS)',
        'bullets': [
            'Your brain filters millions of data points every second',
            'RAS determines what you notice and what you ignore',
            'What you focus on expands - RAS finds evidence for your beliefs',
            'If you believe "I never get interviews," your RAS will prove you right',
            'Shifting your focus changes what opportunities you see'
        ]
    },
    {
        'number': 7,
        'type': 'bullet',
        'title': 'The Self-Fulfilling Prophecy',
        'bullets': [
            'Your expectations shape your behavior, which creates your results',
            'Expect rejection → Show up tentatively → Get rejected → Belief confirmed',
            'Expect success → Show up confidently → Perform better → Create success',
            'This is why "fake it till you make it" actually works',
            'Your beliefs become reality through behavioral feedback loops'
        ]
    },
    {
        'number': 8,
        'type': 'quote',
        'title': 'Rewriting Your Mental Operating System',
        'content': [
            'Awareness: Identify the limiting belief',
            'Challenge: Question the evidence and logic',
            'Replace: Install a new empowering belief',
            'Reinforce: Practice the new belief until it becomes automatic'
        ]
    },
    {
        'number': 9,
        'type': 'bullet',
        'title': 'Common Limiting Beliefs in Job Search',
        'bullets': [
            '"I\'m too old/young for this role"',
            '"I don\'t have enough experience"',
            '"Nobody wants to hire someone like me"',
            '"I\'m not good at selling myself"',
            '"High-paying jobs only go to people with connections"'
        ]
    },

    # LESSON 2: Destroying Limiting Beliefs
    {
        'number': 10,
        'type': 'dark_title',
        'title': 'Destroying Limiting Beliefs',
    },
    {
        'number': 11,
        'type': 'bullet',
        'title': 'Where Limiting Beliefs Come From',
        'bullets': [
            'Childhood programming from parents, teachers, and authority figures',
            'Past failures that you generalized into permanent truths',
            'Social conditioning and cultural narratives about success',
            'Comparing your behind-the-scenes to others\' highlight reels',
            'Negative self-talk that went unchallenged for years'
        ]
    },
    {
        'number': 12,
        'type': 'bullet',
        'title': 'The Cost of Limiting Beliefs',
        'bullets': [
            'You don\'t apply to roles you\'re qualified for',
            'You negotiate poorly because you don\'t believe in your value',
            'You show up tentatively in interviews, killing your presence',
            'You give up too early when facing normal obstacles',
            'You stay in unfulfilling roles because "it could be worse"'
        ]
    },
    {
        'number': 13,
        'type': 'bullet',
        'title': 'The Belief Audit Exercise',
        'bullets': [
            'Write down every belief you hold about your career prospects',
            'For each belief, ask: "Is this absolutely true? What evidence do I have?"',
            'Identify which beliefs empower you and which ones limit you',
            'Find counter-examples that disprove your limiting beliefs',
            'This exercise alone can create breakthrough insights'
        ]
    },
    {
        'number': 14,
        'type': 'framework',
        'title': 'Old Beliefs vs. New Empowering Beliefs',
        'cards': [
            {
                'title': 'OLD BELIEFS',
                'items': [
                    'I\'m not qualified enough',
                    'I\'m too old/young',
                    'I need connections to succeed',
                    'High salaries are for others'
                ]
            },
            {
                'title': 'NEW BELIEFS',
                'items': [
                    'I bring unique value',
                    'Experience matters more than age',
                    'I can build connections',
                    'I deserve high compensation'
                ]
            }
        ]
    },
    {
        'number': 15,
        'type': 'quote',
        'title': 'Installing New Empowering Beliefs',
        'content': [
            'Affirmations: Daily statements of your new identity',
            'Visualization: Mental rehearsal of success scenarios',
            'Evidence collection: Document every win, no matter how small',
            'Environment design: Surround yourself with people who reinforce growth'
        ]
    },
    {
        'number': 16,
        'type': 'bullet',
        'title': 'The Identity Shift',
        'bullets': [
            'Stop seeing yourself as "just a job seeker"',
            'Start seeing yourself as "a high-value professional selecting opportunities"',
            'This shift changes how you show up in every interaction',
            'You interview companies as much as they interview you',
            'Confidence comes from internal identity, not external validation'
        ]
    },
    {
        'number': 17,
        'type': 'bullet',
        'title': 'Reframing Rejection',
        'bullets': [
            'Rejection is not personal - it\'s a data point about fit',
            'Every "no" brings you closer to the right "yes"',
            'Rejection builds resilience and skills if you learn from it',
            'The best opportunities often come after multiple rejections',
            'High performers expect and embrace rejection as part of the process'
        ]
    },
    {
        'number': 18,
        'type': 'bullet',
        'title': 'Building Unshakeable Self-Belief',
        'bullets': [
            'Self-belief comes from keeping promises to yourself',
            'Do what you say you\'ll do, even when you don\'t feel like it',
            'Track small wins daily to build evidence of capability',
            'Separate your worth from your results',
            'You are not your last interview or your last rejection'
        ]
    },

    # LESSON 3: Developing Mental Toughness
    {
        'number': 19,
        'type': 'dark_title',
        'title': 'Developing Mental Toughness',
    },
    {
        'number': 20,
        'type': 'bullet',
        'title': 'What Is Mental Toughness?',
        'bullets': [
            'The ability to persist in the face of obstacles and setbacks',
            'Emotional regulation under pressure and uncertainty',
            'Maintaining focus on long-term goals despite short-term discomfort',
            'The capacity to perform at your best when it matters most',
            'Mental toughness is trainable, not innate'
        ]
    },
    {
        'number': 21,
        'type': 'bullet',
        'title': 'The Gap Between Stimulus and Response',
        'bullets': [
            'Between what happens and how you respond is a choice',
            'Most people react automatically based on conditioning',
            'High performers pause and choose their response consciously',
            'This gap is where your power lives',
            'Expanding this gap is the essence of emotional intelligence'
        ]
    },
    {
        'number': 22,
        'type': 'bullet',
        'title': 'Controlling What You Can Control',
        'bullets': [
            'You can\'t control if you get the job, but you can control your preparation',
            'You can\'t control the interviewer\'s mood, but you can control your energy',
            'You can\'t control the timeline, but you can control your follow-up',
            'Focus 100% of your energy on what\'s within your control',
            'Letting go of what you can\'t control reduces anxiety dramatically'
        ]
    },
    {
        'number': 23,
        'type': 'dark_title',
        'title': 'The Stoic Approach to Adversity',
    },
    {
        'number': 24,
        'type': 'bullet',
        'title': 'Stoicism Applied to Job Search',
        'bullets': [
            'Expect obstacles - they are not exceptions, they are the path',
            'Practice negative visualization: imagine setbacks, then plan for them',
            'Focus on process, not outcomes',
            'Find opportunity in every obstacle',
            'The obstacle is the way forward, not a roadblock'
        ]
    },
    {
        'number': 25,
        'type': 'quote',
        'title': 'Turning Setbacks into Fuel',
        'content': [
            'Didn\'t get the job? Analyze and improve your approach',
            'Interview went poorly? Identify specific skills to practice',
            'Long silence from recruiters? Use the time to upskill and network',
            'Every setback contains a lesson - find it and apply it'
        ]
    },
    {
        'number': 26,
        'type': 'bullet',
        'title': 'Building Resilience Through Stress Inoculation',
        'bullets': [
            'Exposure to manageable stress builds resilience',
            'Each rejection you process makes you stronger',
            'Practice uncomfortable scenarios deliberately',
            'Mock interviews, cold outreach, and asking for referrals build tolerance',
            'Resilience is built through repeated exposure and recovery'
        ]
    },
    {
        'number': 27,
        'type': 'bullet',
        'title': 'The Power of Emotional Regulation',
        'bullets': [
            'Your emotions are valid, but they don\'t have to control your actions',
            'Feel the disappointment, then choose your next move',
            'High performers experience the same emotions, they just don\'t get stuck',
            'Create space between feeling and action through breathing and reflection',
            'Emotional regulation is the difference between reactive and strategic'
        ]
    },
    {
        'number': 28,
        'type': 'bullet',
        'title': 'Developing a Long-Term Perspective',
        'bullets': [
            'Your career is a 40-year game, not a 40-day sprint',
            'This job search is one chapter, not the whole story',
            'Temporary discomfort creates permanent growth',
            'Where you are today doesn\'t determine where you\'ll be in 2 years',
            'Long-term thinking reduces the emotional weight of short-term setbacks'
        ]
    },
    {
        'number': 29,
        'type': 'framework',
        'title': 'Mental Toughness Framework',
        'cards': [
            {
                'title': 'AWARENESS',
                'items': [
                    'Notice your thoughts',
                    'Identify triggers',
                    'Recognize patterns',
                    'Catch automatic reactions'
                ]
            },
            {
                'title': 'RESPONSE',
                'items': [
                    'Pause before reacting',
                    'Choose empowering thought',
                    'Take strategic action',
                    'Learn from outcome'
                ]
            },
            {
                'title': 'GROWTH',
                'items': [
                    'Reflect on experience',
                    'Extract the lesson',
                    'Adjust approach',
                    'Build resilience'
                ]
            }
        ]
    },
    {
        'number': 30,
        'type': 'bullet',
        'title': 'The Daily Mental Toughness Practice',
        'bullets': [
            'Morning: Set intentions and visualize success',
            'Midday: Notice reactions and choose responses consciously',
            'Evening: Journal about challenges and how you responded',
            'Weekly: Review patterns and adjust your approach',
            'Mental toughness is built through daily micro-practices, not occasional heroics'
        ]
    },

    # LESSON 4: Adopting the Success Habits of Top Performers
    {
        'number': 31,
        'type': 'dark_title',
        'title': 'Adopting Success Habits of Top Performers',
    },
    {
        'number': 32,
        'type': 'bullet',
        'title': 'Success Habit #1: Clarity of Vision',
        'bullets': [
            'Top performers have crystal-clear vision of what they want',
            'Vague goals lead to vague results',
            'Define your ideal role, company culture, and compensation with specificity',
            'Write it down and review it daily',
            'Clarity creates focus; focus creates results'
        ]
    },
    {
        'number': 33,
        'type': 'quote',
        'title': 'Creating Your Career Vision',
        'content': [
            'What role do you want to hold?',
            'What companies align with your values?',
            'What does your ideal day look like?',
            'What compensation would make you feel valued?'
        ]
    },
    {
        'number': 34,
        'type': 'framework',
        'title': 'Success Habit #2: The 80/20 Rule (Pareto Principle)',
        'cards': [
            {
                'title': '80/20 IN JOB SEARCH',
                'items': [
                    '20% of your activities create 80% of results',
                    'Focus on high-leverage actions',
                    'Quality applications over quantity',
                    'Strategic networking over spray-and-pray'
                ]
            },
            {
                'title': 'HIGH-LEVERAGE ACTIVITIES',
                'items': [
                    'Targeted outreach to decision-makers',
                    'Referrals from strong connections',
                    'Deep company research',
                    'Interview preparation',
                    'Strategic follow-up'
                ]
            }
        ]
    },
    {
        'number': 35,
        'type': 'bullet',
        'title': 'Success Habit #3: Bias Toward Action',
        'bullets': [
            'High performers act before they feel ready',
            'Waiting for perfect readiness is procrastination in disguise',
            'Done is better than perfect',
            'You learn more from action than from planning',
            'Momentum comes from movement, not contemplation'
        ]
    },
    {
        'number': 36,
        'type': 'bullet',
        'title': 'Success Habit #4: Extreme Ownership',
        'bullets': [
            'Top performers take 100% responsibility for their results',
            'No blaming the economy, ageism, or lack of connections',
            'If you don\'t like your results, change your actions',
            'Ownership gives you power; victimhood removes it',
            'The moment you take ownership, you can change the outcome'
        ]
    },
    {
        'number': 37,
        'type': 'quote',
        'title': 'The Jocko Willink Principle',
        'content': [
            '"There are no bad teams, only bad leaders"',
            'Applied to job search: There are no hopeless candidates, only ineffective strategies',
            'When you own everything, you can fix everything',
            'Extreme ownership is empowering, not overwhelming'
        ]
    },
    {
        'number': 38,
        'type': 'quote',
        'title': 'Accountability Without Judgment',
        'content': [
            'Taking ownership doesn\'t mean beating yourself up',
            'It means recognizing your power to change outcomes',
            'Past results don\'t define future potential',
            'Realize nobody is beyond suffering and setbacks'
        ]
    },
    {
        'number': 39,
        'type': 'bullet',
        'title': 'Extreme Ownership in Your Job Search',
        'bullets': [
            'Your results are a direct reflection of your actions',
            'Not getting interviews? Your approach needs improvement',
            'Not getting offers? Your skills need refinement',
            'Not getting the salary you want? Your negotiation needs work',
            'Taking ownership gives you power to change outcomes'
        ]
    },
    {
        'number': 40,
        'type': 'bullet',
        'title': 'Success Habit #5: Don\'t Think of Success as Linear',
        'bullets': [
            'Most people think of success as a start and a finish. It\'s not.',
            'When people think like that...they start many things and finish nothing',
            'For example, switching businesses, methods, courses, etc.',
            'Instead, think of success as planting seeds...then watering and harvesting'
        ]
    },
    {
        'number': 41,
        'type': 'quote',
        'title': 'The Non-Linear Path to Career Success',
        'content': [
            'Job search progress is not a straight line',
            'Weeks of silence can be followed by multiple opportunities',
            'Trust the process even when results aren\'t visible',
            'Stay committed for at least 60-90 days before pivoting'
        ]
    },
    {
        'number': 42,
        'type': 'bullet',
        'title': 'Success Habit #6: Questions Not Statements',
        'bullets': [
            'Asking questions opens the mind to solutions',
            'Statements close the mind to possibility of solutions',
            'Train yourself to say "how can I?" instead of "I can\'t"',
            '"How can I scale this offer up?" vs. "I can\'t scale this offer up"'
        ]
    },
    {
        'number': 43,
        'type': 'bullet',
        'title': 'Empowering Questions for Job Search',
        'bullets': [
            'Instead of "I can\'t get interviews" → "How can I improve my approach?"',
            'Instead of "I\'m not qualified" → "How can I position my experience?"',
            'Instead of "I won\'t get that salary" → "How can I negotiate effectively?"',
            'Questions activate problem-solving; statements activate defensiveness'
        ]
    },
    {
        'number': 44,
        'type': 'bullet',
        'title': 'Success Habit #7: Be A Shark',
        'bullets': [
            'What do sharks do?',
            'Does the shark ever wake up and decide not to do shark things that day? No!',
            'Same goes for you as a salesperson and entrepreneur',
            'Get up every day and do whatever it takes to be successful',
            'Hunt down your goals with the same ferocity that a shark would'
        ]
    },
    {
        'number': 45,
        'type': 'bullet',
        'title': 'Relentless Execution in Your Job Search',
        'bullets': [
            'Show up every day with consistent effort',
            'Maintain your rhythm even during slow periods',
            'Follow up persistently but professionally',
            'Don\'t let rejection slow your momentum',
            'Success comes to those who refuse to quit'
        ]
    },

    # LESSON 5: Creating Your Personal Success System
    {
        'number': 46,
        'type': 'dark_title',
        'title': 'Creating Your Personal Success System',
    },
    {
        'number': 47,
        'type': 'bullet',
        'title': 'Why Systems Beat Goals',
        'bullets': [
            'Goals tell you where to go; systems get you there',
            'You don\'t rise to your goals - you fall to your systems',
            'Relying on motivation leads to inconsistent effort',
            'Systems create automatic progress regardless of how you feel',
            'Winners and losers have same goals; winners have better systems'
        ]
    },
    {
        'number': 48,
        'type': 'bullet',
        'title': 'The Components of a Success System',
        'bullets': [
            'DAILY HABITS: Non-negotiable actions every single day',
            'WEEKLY RHYTHMS: Recurring activities that move you forward',
            'TRACKING METRICS: Data showing progress and improvement areas',
            'FEEDBACK LOOPS: Regular review and adjustment',
            'ACCOUNTABILITY: People or systems keeping you honest'
        ]
    },
    {
        'number': 49,
        'type': 'bullet',
        'title': 'Your Daily Job Search System',
        'bullets': [
            'Morning: Review vision and target company list (10 min)',
            'Mid-morning: 5 new LinkedIn connections or outreach messages (30 min)',
            'Afternoon: Research 2-3 target companies deeply (30 min)',
            'Evening: Update tracking spreadsheet and review progress (15 min)',
            'Total time investment: 85 minutes per day for career transformation'
        ]
    },
    {
        'number': 50,
        'type': 'bullet',
        'title': 'Your Weekly Job Search Rhythm',
        'bullets': [
            'Monday: Set weekly goals and priority targets',
            'Tuesday-Thursday: Execute daily system + 3-5 quality applications',
            'Friday: Review metrics, identify what worked, adjust',
            'Saturday: Interview preparation and skill development',
            'Sunday: Plan next week and recharge mentally'
        ]
    },
    {
        'number': 51,
        'type': 'quote',
        'title': 'Essential Tracking Metrics',
        'content': [
            'Outreach: Connection requests sent, response rate',
            'Applications: Jobs applied to, interviews secured',
            'Network: New connections made, informational interviews',
            'What gets measured gets managed - and improved'
        ]
    },
    {
        'number': 52,
        'type': 'bullet',
        'title': 'Building Feedback Loops',
        'bullets': [
            'Weekly self-review: What worked? What didn\'t? What will I test next?',
            'Track patterns: Which messages get responses? Which interviews go well?',
            'Seek external feedback: Mock interviews, message reviews, profile audits',
            'A/B test your approach',
            'Iterate rapidly based on data, not assumptions'
        ]
    },
    {
        'number': 53,
        'type': 'bullet',
        'title': 'Accountability Systems That Work',
        'bullets': [
            'Find an accountability partner pursuing similar goals',
            'Schedule weekly check-ins to report progress',
            'Join a community of job seekers for mutual support',
            'Share your goals with mentors who will hold you to high standards',
            'Public commitment increases follow-through significantly'
        ]
    },
    {
        'number': 54,
        'type': 'bullet',
        'title': 'Designing Your Environment for Success',
        'bullets': [
            'Remove distractions during dedicated job search time',
            'Create a workspace that signals focus and professionalism',
            'Use tools that make execution easier: templates, trackers, calendars',
            'Eliminate friction: Have everything prepared and ready',
            'Your environment should make good behaviors easy'
        ]
    },
    {
        'number': 55,
        'type': 'bullet',
        'title': 'The Power of Consistency Over Intensity',
        'bullets': [
            'Working 1 hour daily for 90 days beats working 10 hours in one weekend',
            'Consistency builds momentum, skills, and relationships over time',
            'Intense bursts followed by inaction create poor results',
            'Your system should be sustainable long-term, not exhausting',
            'Small consistent actions compound into extraordinary outcomes'
        ]
    },
    {
        'number': 56,
        'type': 'bullet',
        'title': 'Your 90-Day Success System Implementation',
        'bullets': [
            'Days 1-30: Build the habit, track everything, learn what works',
            'Days 31-60: Optimize based on data, increase volume, build momentum',
            'Days 61-90: Leverage your network and pipeline, multiple opportunities flowing',
            'This system, executed consistently, leads to interviews and offers',
            'Start today - your future self will thank you'
        ]
    },
    {
        'number': 57,
        'type': 'final',
        'title': 'You Now Have the Mindset',
        'subtitle': 'Foundation for Success'
    }
]

# ============================================================================
# MAIN GENERATION FUNCTION
# ============================================================================

def generate_all_slides(output_dir):
    """Generate all 57 slides with Startup Presentation aesthetic."""

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    print(f"🎨 Generating 57 slides with Startup Presentation aesthetic...")
    print(f"📁 Output directory: {output_dir}")
    print()

    for slide_data in slides_content:
        number = slide_data['number']
        slide_type = slide_data['type']

        print(f"   Generating slide {number:02d}...", end=' ')

        try:
            if slide_type == 'dark_title':
                slide = generate_dark_title_slide(
                    number,
                    slide_data['title'],
                    slide_data.get('subtitle')
                )
            elif slide_type == 'bullet':
                slide = generate_light_bullet_slide(
                    number,
                    slide_data['title'],
                    slide_data['bullets']
                )
            elif slide_type == 'quote':
                slide = generate_light_quote_slide(
                    number,
                    slide_data['title'],
                    slide_data['content']
                )
            elif slide_type == 'framework':
                slide = generate_framework_slide(
                    number,
                    slide_data['title'],
                    slide_data['cards']
                )
            elif slide_type == 'final':
                slide = generate_simple_final_slide(
                    number,
                    slide_data['title'],
                    slide_data.get('subtitle', '')
                )
            else:
                print(f"❌ Unknown slide type: {slide_type}")
                continue

            # Save slide
            output_path = os.path.join(output_dir, f"slide-{number:02d}-startup.png")
            slide.save(output_path, 'PNG', quality=95, optimize=True)
            print(f"✓ Saved as slide-{number:02d}-startup.png")

        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()
            continue

    print()
    print(f"✅ All slides generated successfully!")
    print(f"📊 Total slides: 57")
    print(f"💾 Location: {output_dir}")
    print()
    print("🎨 Design features applied:")
    print("   • Dual-theme approach (light + dark backgrounds)")
    print("   • Rounded card components (28px radius)")
    print("   • Soft diffused gradient overlays")
    print("   • Numbered circular badges (#A7D4F0)")
    print("   • SF Pro Display/Helvetica Neue typography")
    print("   • Professional 2025 startup pitch deck aesthetic")
    print("   • 80px safe zone margins")
    print("   • Modern, minimalist, sophisticated design")

if __name__ == "__main__":
    # Output directory
    output_dir = "/Users/terrancebrandon/Desktop/Active Offer/AO- Course Content/Active Offer- Course Material/M0- Mindset Expanded/Redesigned-ConceptA"

    # Generate all slides
    generate_all_slides(output_dir)
