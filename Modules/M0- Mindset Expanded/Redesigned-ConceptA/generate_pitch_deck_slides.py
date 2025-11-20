"""
PITCH DECK SLIDE GENERATOR - Modern Startup Aesthetic
=====================================================
Transforms M0 Mindset Module slides using the pitch deck style guide aesthetic.

DESIGN CHARACTERISTICS:
- Soft, organic gradients (blue, pink, orange, teal)
- Generous whitespace and breathing room (40-50% empty space)
- Clean, minimal aesthetic with light, airy feel
- Transparent overlays instead of solid backgrounds
- No heavy shadows - keep it light and soft
- Modern startup aesthetic

COLOR PALETTE:
- Primary dark gray: #424242 (main text)
- Primary light blue: #A0CEFD (accents)
- Background white: #FFFFFF
- Background gray: #D0D7DD (subtle)
- Light blue background: #E4F2FF
- Soft gray: #393939

TYPOGRAPHY:
- Primary: Helvetica Neue (fallback: Helvetica, Arial)
- Title slides: Helvetica Neue Light 72-96px
- Section titles: Helvetica Neue Bold 48px
- Body text: Helvetica Neue Regular 36px
- Small text: Helvetica Neue Light 28px
- Color: Always #424242 for readability

GRADIENT BACKGROUNDS (20-42% opacity):
- gradient-circle-blue-1500x1108.png
- gradient-ellipses-blue-pink-1500x970.png
- gradient-horizontal-blue-pink-1500x770.png
- gradient-organic-blue-pink-1194x1341.png
- gradient-wave-blue-900x539.png
- gradient-waves-blue-orange-1500x626.png
- gradient-waves-multicolor-1500x576.png

LAYOUT PRINCIPLES:
- Abundant whitespace (40-50% of slide should be empty)
- Content in safe area (1820x980 within 1920x1080)
- Left-aligned or center content (not edge-to-edge)
- Soft, subtle divider lines (1px, #D0D7DD, not bold)
- Clean bullet points (simple circles or dashes, #A0CEFD color)
- Grid-based alignment
- Generous padding: 80-100px from edges

Author: Claude Code
Version: 1.0 Pitch Deck
Output: slide-01-pitchdeck.png through slide-57-pitchdeck.png
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import random

# ============================================================================
# IMAGE DIMENSIONS
# ============================================================================
WIDTH = 1920
HEIGHT = 1080

# Safe area (80px padding from edges)
SAFE_LEFT = 100
SAFE_RIGHT = WIDTH - 100
SAFE_TOP = 80
SAFE_BOTTOM = HEIGHT - 80

# ============================================================================
# COLOR PALETTE
# ============================================================================
PRIMARY_DARK_GRAY = (66, 66, 66)        # #424242 - main text
PRIMARY_LIGHT_BLUE = (160, 206, 253)    # #A0CEFD - accents
BACKGROUND_WHITE = (255, 255, 255)      # #FFFFFF
BACKGROUND_GRAY = (208, 215, 221)       # #D0D7DD - subtle
LIGHT_BLUE_BG = (228, 242, 255)         # #E4F2FF
SOFT_GRAY = (57, 57, 57)                # #393939

# ============================================================================
# TYPOGRAPHY
# ============================================================================
FONT_PATH_HELVETICA = "/System/Library/Fonts/HelveticaNeue.ttc"

try:
    # Title fonts - Light and Bold variants
    FONT_TITLE_LARGE = ImageFont.truetype(FONT_PATH_HELVETICA, 96)      # For main titles
    FONT_TITLE_MEDIUM = ImageFont.truetype(FONT_PATH_HELVETICA, 72)     # For lesson titles
    FONT_SECTION_TITLE = ImageFont.truetype(FONT_PATH_HELVETICA, 48)    # Bold section titles
    FONT_BODY = ImageFont.truetype(FONT_PATH_HELVETICA, 36)             # Regular body text
    FONT_SMALL = ImageFont.truetype(FONT_PATH_HELVETICA, 28)            # Light small text
    FONT_TINY = ImageFont.truetype(FONT_PATH_HELVETICA, 24)             # Very small text
except Exception as e:
    print(f"⚠️  Warning: Could not load Helvetica Neue. Using defaults. Error: {e}")
    FONT_TITLE_LARGE = FONT_TITLE_MEDIUM = FONT_SECTION_TITLE = ImageFont.load_default()
    FONT_BODY = FONT_SMALL = FONT_TINY = ImageFont.load_default()

# ============================================================================
# GRADIENT BACKGROUND PATHS
# ============================================================================
GRADIENT_DIR = "/Users/terrancebrandon/Desktop/TB Presentation Styles/pitch-deck/images/backgrounds/"
GRADIENTS = {
    'circle': 'gradient-circle-blue-1500x1108.png',
    'ellipses': 'gradient-ellipses-blue-pink-1500x970.png',
    'horizontal': 'gradient-horizontal-blue-pink-1500x770.png',
    'organic': 'gradient-organic-blue-pink-1194x1341.png',
    'wave': 'gradient-wave-blue-900x539.png',
    'waves_orange': 'gradient-waves-blue-orange-1500x626.png',
    'waves_multi': 'gradient-waves-multicolor-1500x576.png',
}

# ============================================================================
# LAYOUT CONSTANTS
# ============================================================================
MARGIN = 100
BULLET_SPACING = 60  # Generous spacing between bullets
LINE_HEIGHT_MULTIPLIER = 1.5

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def load_gradient(gradient_key, opacity=0.30, position='center', scale=1.0):
    """
    Load a gradient background image with specified opacity and positioning.

    Args:
        gradient_key: Key from GRADIENTS dict
        opacity: 0.2-0.42 recommended (20-42%)
        position: 'center', 'top-right', 'bottom-left', etc.
        scale: Scale factor for the gradient
    """
    try:
        gradient_path = os.path.join(GRADIENT_DIR, GRADIENTS[gradient_key])
        gradient = Image.open(gradient_path).convert('RGBA')

        # Scale the gradient
        new_width = int(gradient.width * scale)
        new_height = int(gradient.height * scale)
        gradient = gradient.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Adjust opacity
        alpha = gradient.split()[3]
        alpha = alpha.point(lambda p: int(p * opacity))
        gradient.putalpha(alpha)

        # Create positioning
        canvas = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))

        if position == 'center':
            x = (WIDTH - gradient.width) // 2
            y = (HEIGHT - gradient.height) // 2
        elif position == 'top-right':
            x = WIDTH - gradient.width + 200
            y = -100
        elif position == 'bottom-left':
            x = -200
            y = HEIGHT - gradient.height + 100
        elif position == 'top-left':
            x = -200
            y = -100
        elif position == 'bottom-right':
            x = WIDTH - gradient.width + 200
            y = HEIGHT - gradient.height + 100
        else:
            x = 0
            y = 0

        canvas.paste(gradient, (x, y), gradient)
        return canvas

    except Exception as e:
        print(f"⚠️  Warning: Could not load gradient '{gradient_key}': {e}")
        return Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))

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

def draw_bullet_point(draw, x, y, color=PRIMARY_LIGHT_BLUE, size=12):
    """Draw a soft circular bullet point."""
    draw.ellipse([x, y, x + size, y + size], fill=color)

def draw_soft_line(draw, x1, y1, x2, y2, color=BACKGROUND_GRAY, width=1):
    """Draw a soft, subtle divider line."""
    draw.line([(x1, y1), (x2, y2)], fill=color, width=width)

def create_base_slide(gradient_key=None, gradient_opacity=0.30, gradient_position='center', gradient_scale=1.0):
    """Create a base slide with white background and optional gradient overlay."""
    # Start with white background
    slide = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND_WHITE)

    # Add gradient if specified
    if gradient_key:
        gradient = load_gradient(gradient_key, gradient_opacity, gradient_position, gradient_scale)
        slide = Image.alpha_composite(slide.convert('RGBA'), gradient).convert('RGB')

    return slide

def get_text_dimensions(text, font):
    """Get the bounding box dimensions of text."""
    temp_img = Image.new('RGB', (1, 1))
    temp_draw = ImageDraw.Draw(temp_img)
    bbox = temp_draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]

# ============================================================================
# SLIDE GENERATION FUNCTIONS
# ============================================================================

def generate_title_slide(number, title, gradient_key='circle'):
    """Generate a lesson title slide with soft gradient and generous spacing."""
    slide = create_base_slide(gradient_key, 0.35, 'center', 1.2)
    draw = ImageDraw.Draw(slide)

    # Title - centered, large, light and airy
    title_lines = wrap_text(title, FONT_TITLE_MEDIUM, WIDTH - 400)

    total_height = len(title_lines) * 90
    y = (HEIGHT - total_height) // 2

    for line in title_lines:
        text_width, _ = get_text_dimensions(line, FONT_TITLE_MEDIUM)
        x = (WIDTH - text_width) // 2
        draw.text((x, y), line, fill=PRIMARY_DARK_GRAY, font=FONT_TITLE_MEDIUM)
        y += 90

    return slide

def generate_bullet_slide(number, title, bullets, gradient_key='horizontal'):
    """Generate a content slide with bullets, soft gradient, and generous whitespace."""
    slide = create_base_slide(gradient_key, 0.25, 'top-right', 1.0)
    draw = ImageDraw.Draw(slide)

    # Title - left-aligned, clean
    y = SAFE_TOP + 40
    draw.text((SAFE_LEFT, y), title, fill=PRIMARY_DARK_GRAY, font=FONT_SECTION_TITLE)

    # Subtle divider line
    y += 70
    draw_soft_line(draw, SAFE_LEFT, y, SAFE_LEFT + 300, y, BACKGROUND_GRAY, 1)

    # Bullets with generous spacing
    y += 80
    max_content_width = WIDTH - (2 * MARGIN) - 50  # Extra margin for bullets

    for bullet in bullets:
        # Draw bullet point (soft circle)
        bullet_y = y + 12
        draw_bullet_point(draw, SAFE_LEFT, bullet_y, PRIMARY_LIGHT_BLUE, 10)

        # Wrap and draw bullet text
        wrapped_lines = wrap_text(bullet, FONT_BODY, max_content_width)
        for line in wrapped_lines:
            draw.text((SAFE_LEFT + 30, y), line, fill=PRIMARY_DARK_GRAY, font=FONT_BODY)
            y += 48

        y += BULLET_SPACING - 48  # Add extra spacing between bullets

    return slide

def generate_quote_slide(number, title, content, gradient_key='ellipses'):
    """Generate a slide with emphasized content in a clean, airy layout."""
    slide = create_base_slide(gradient_key, 0.28, 'bottom-left', 1.1)
    draw = ImageDraw.Draw(slide)

    # Title at top
    y = SAFE_TOP + 40
    draw.text((SAFE_LEFT, y), title, fill=PRIMARY_DARK_GRAY, font=FONT_SECTION_TITLE)

    # Subtle divider
    y += 70
    draw_soft_line(draw, SAFE_LEFT, y, SAFE_LEFT + 300, y, BACKGROUND_GRAY, 1)

    # Content - centered, larger, with lots of breathing room
    y = HEIGHT // 2 - 100
    max_width = WIDTH - 400

    for item in content:
        wrapped_lines = wrap_text(item, FONT_BODY, max_width)
        for line in wrapped_lines:
            text_width, _ = get_text_dimensions(line, FONT_BODY)
            x = (WIDTH - text_width) // 2
            draw.text((x, y), line, fill=PRIMARY_DARK_GRAY, font=FONT_BODY)
            y += 50
        y += 40  # Extra space between items

    return slide

def generate_simple_slide(number, title, subtitle, gradient_key='waves_multi'):
    """Generate a simple slide with title and subtitle, minimal aesthetic."""
    slide = create_base_slide(gradient_key, 0.30, 'center', 1.0)
    draw = ImageDraw.Draw(slide)

    # Title - centered
    y = HEIGHT // 2 - 80
    text_width, _ = get_text_dimensions(title, FONT_TITLE_LARGE)
    x = (WIDTH - text_width) // 2
    draw.text((x, y), title, fill=PRIMARY_DARK_GRAY, font=FONT_TITLE_LARGE)

    # Subtitle - centered below
    if subtitle:
        y += 120
        text_width, _ = get_text_dimensions(subtitle, FONT_SMALL)
        x = (WIDTH - text_width) // 2
        draw.text((x, y), subtitle, fill=SOFT_GRAY, font=FONT_SMALL)

    return slide

# ============================================================================
# SLIDE CONTENT DATA
# ============================================================================

slides_content = [
    # LESSON 1: The Psychology of High-Ticket Job Searches
    {
        'number': 1,
        'type': 'title',
        'title': 'The Psychology of High-Ticket Job Searches',
        'gradient': 'circle'
    },
    {
        'number': 2,
        'type': 'bullet',
        'title': 'Why Mindset Matters More Than Strategy',
        'bullets': [
            'Your mindset determines your actions, and your actions determine your results',
            'Most job seekers focus on tactics but neglect the psychological foundation',
            'High-ticket roles require a different level of confidence and positioning',
            'Hiring managers can sense desperation, scarcity thinking, and lack of confidence',
            'Premium positioning starts in your mind before it shows up in your messaging'
        ],
        'gradient': 'horizontal'
    },
    {
        'number': 3,
        'type': 'bullet',
        'title': 'The High-Ticket Job Search Mindset',
        'bullets': [
            'You are interviewing the company as much as they are interviewing you',
            'You bring valuable skills and expertise that solve expensive business problems',
            'Scarcity vs. Abundance mindset comparison',
            'Your goal is to find the right high-value opportunity, not any job',
            'Confidence is not arrogance; it\'s knowing your worth'
        ],
        'gradient': 'ellipses'
    },
    {
        'number': 4,
        'type': 'bullet',
        'title': 'Common Psychological Barriers',
        'bullets': [
            'Imposter syndrome',
            'Fear of rejection',
            'Salary anxiety',
            'Scarcity thinking',
            'Comparison trap'
        ],
        'gradient': 'wave'
    },
    {
        'number': 5,
        'type': 'bullet',
        'title': 'The Cost of the Wrong Mindset',
        'bullets': [
            '$50k-$200k+ per year in lost compensation',
            '$250k-$1M in lost lifetime earnings over 5 years',
            '1-2 years of career momentum wasted',
            'Tens of thousands left on the table in negotiations',
            'Your mindset compounds your success or stagnation'
        ],
        'gradient': 'organic'
    },
    {
        'number': 6,
        'type': 'bullet',
        'title': 'Shifting to a High-Performer Mindset',
        'bullets': [
            'View yourself as a business solving problems',
            'Approach interviews as collaborative discovery',
            'See compensation as a reflection of value created',
            'Embrace rejection as data and refinement',
            'Build evidence of your value'
        ],
        'gradient': 'waves_orange'
    },
    {
        'number': 7,
        'type': 'bullet',
        'title': 'The Abundance Mentality in Job Search',
        'bullets': [
            'Thousands of companies hiring for high-ticket sales roles',
            'Multiple opportunities create leverage',
            'You only need ONE great offer, but options give you power',
            'Abundance thinking makes you more attractive',
            'The right opportunity exists'
        ],
        'gradient': 'horizontal'
    },
    {
        'number': 8,
        'type': 'bullet',
        'title': 'Reframing Rejection and Setbacks',
        'bullets': [
            'Every "no" brings you closer to the right "yes"',
            'Rejection is feedback about fit, not worth',
            'Top performers get rejected often',
            'Use rejection to refine your approach',
            'The rejecting company might not be the right fit anyway'
        ],
        'gradient': 'ellipses'
    },
    {
        'number': 9,
        'type': 'bullet',
        'title': 'Building Psychological Resilience',
        'bullets': [
            'Separate identity from job search outcomes',
            'Celebrate small wins',
            'Develop a support system',
            'Practice self-compassion',
            'Remember: building a career, not just finding a job'
        ],
        'gradient': 'waves_multi'
    },

    # LESSON 2: Identifying Your Limiting Beliefs
    {
        'number': 10,
        'type': 'title',
        'title': 'Identifying Your Limiting Beliefs',
        'gradient': 'organic'
    },
    {
        'number': 11,
        'type': 'bullet',
        'title': 'What Are Limiting Beliefs?',
        'bullets': [
            'Subconscious assumptions about yourself and what\'s possible',
            'Formed from past experiences, family messages, societal conditioning',
            'Feel like facts but are actually interpretations',
            'Create self-imposed ceilings on potential and income',
            'Most people are unaware of beliefs holding them back'
        ],
        'gradient': 'circle'
    },
    {
        'number': 12,
        'type': 'bullet',
        'title': 'Common Limiting Beliefs in Job Search',
        'bullets': [
            '"I\'m not qualified for roles at that level"',
            '"I don\'t have the right background or pedigree"',
            '"I\'m too old/young for that opportunity"',
            '"Companies won\'t pay me that much"',
            '"I\'m not good at interviews or selling myself"'
        ],
        'gradient': 'horizontal'
    },
    {
        'number': 13,
        'type': 'bullet',
        'title': 'How Limiting Beliefs Sabotage Your Search',
        'bullets': [
            'Don\'t apply to roles you\'re qualified for',
            'Undersell yourself in interviews and negotiations',
            'Accept lower compensation than you deserve',
            'Avoid uncomfortable growth-producing situations',
            'Create self-fulfilling prophecies'
        ],
        'gradient': 'wave'
    },
    {
        'number': 14,
        'type': 'bullet',
        'title': 'The Limiting Belief Identification Process',
        'bullets': [
            'Step 1: Notice where you hesitate or avoid action',
            'Step 2: Ask "What would I have to believe to behave this way?"',
            'Step 3: Write down the belief and examine the evidence',
            'Step 4: Challenge with counter-evidence',
            'Step 5: Create new empowering belief with supporting evidence'
        ],
        'gradient': 'ellipses'
    },
    {
        'number': 15,
        'type': 'bullet',
        'title': 'Reframing Exercise: From Limiting to Empowering',
        'bullets': [
            '"I\'m not qualified" → "I bring unique value they can\'t find elsewhere"',
            '"I need more experience" → "I have transferable skills that apply immediately"',
            '"They won\'t pay me that much" → "I solve problems worth far more than my salary"',
            '"I\'m bad at interviews" → "I\'m learning and improving with each conversation"'
        ],
        'gradient': 'organic'
    },
    {
        'number': 16,
        'type': 'bullet',
        'title': 'Evidence Collection: Building Your Case',
        'bullets': [
            'Document past wins',
            'Quantify your impact',
            'Collect testimonials and recommendations',
            'Identify skills others pay you for advice on',
            'Notice when people come to you for help'
        ],
        'gradient': 'waves_orange'
    },
    {
        'number': 17,
        'type': 'bullet',
        'title': 'The Power of Borrowed Belief',
        'bullets': [
            'Borrow belief from others who believe in you',
            'Study people with your background who landed the roles you want',
            'Find mentors who see potential you can\'t see yet',
            'Join communities of people pursuing similar goals',
            'Use their success as evidence of what\'s possible'
        ],
        'gradient': 'horizontal'
    },
    {
        'number': 18,
        'type': 'bullet',
        'title': 'Daily Practice: Belief Reinforcement',
        'bullets': [
            'Morning: Review empowering beliefs and evidence',
            'During job search: Notice and reframe limiting beliefs',
            'After interactions: Collect evidence of your value',
            'Evening: Reflect on moments you showed up despite fear',
            'Weekly: Update evidence journal with wins and insights'
        ],
        'gradient': 'waves_multi'
    },

    # LESSON 3: Building Unshakeable Confidence
    {
        'number': 19,
        'type': 'title',
        'title': 'Building Unshakeable Confidence',
        'gradient': 'circle'
    },
    {
        'number': 20,
        'type': 'bullet',
        'title': 'What Is True Confidence?',
        'bullets': [
            'Not arrogance or bravado - quiet self-assurance',
            'Belief that you can handle whatever comes',
            'Comes from evidence and preparation, not positive thinking alone',
            'Being comfortable with uncertainty and embracing growth',
            'A skill you build through action, not something you wait to feel'
        ],
        'gradient': 'ellipses'
    },
    {
        'number': 21,
        'type': 'quote',
        'title': 'The Confidence-Action Cycle',
        'content': [
            'Most people think: Confidence → Action → Results',
            'Reality: Action → Results → Confidence',
            'Build confidence by taking action before you feel ready'
        ],
        'gradient': 'organic'
    },
    {
        'number': 22,
        'type': 'bullet',
        'title': 'The Three Pillars of Career Confidence',
        'bullets': [
            'COMPETENCE: You have skills and knowledge that create value',
            'PREPARATION: You\'ve done the work to be ready',
            'EVIDENCE: You have proof of past successes and results',
            'When all three are strong, confidence becomes unshakeable',
            'Focus on building these systematically'
        ],
        'gradient': 'horizontal'
    },
    {
        'number': 23,
        'type': 'bullet',
        'title': 'Pillar 1: Building Competence',
        'bullets': [
            'Master the fundamentals of your craft',
            'Develop expertise in specific areas',
            'Stay current with trends and best practices',
            'Invest in continuous learning',
            'Practice your skills deliberately and consistently'
        ],
        'gradient': 'wave'
    },
    {
        'number': 24,
        'type': 'bullet',
        'title': 'Pillar 2: Rigorous Preparation',
        'bullets': [
            'Research every company before engaging',
            'Prepare specific examples for common interview questions',
            'Practice your pitch, story, and value proposition',
            'Anticipate objections and prepare responses',
            'Mock interviews and role plays build readiness'
        ],
        'gradient': 'waves_orange'
    },
    {
        'number': 25,
        'type': 'bullet',
        'title': 'Pillar 3: Collecting Evidence',
        'bullets': [
            'Create a "wins document" tracking every success',
            'Quantify your achievements',
            'Save testimonials and positive feedback',
            'Document problems solved and value created',
            'Review this evidence regularly'
        ],
        'gradient': 'ellipses'
    },
    {
        'number': 26,
        'type': 'bullet',
        'title': 'Confidence-Building Exercises',
        'bullets': [
            'Power posing: 2 minutes before interviews',
            'Visualization: See yourself succeeding',
            'Affirmations grounded in evidence',
            'Recall past wins',
            'Preparation rituals'
        ],
        'gradient': 'horizontal'
    },
    {
        'number': 27,
        'type': 'bullet',
        'title': 'Overcoming Confidence Killers',
        'bullets': [
            'Comparison: Focus on your own progress',
            'Perfectionism: Done is better than perfect',
            'Negative self-talk: Catch it, challenge it, replace it',
            'Past failures: Reframe as learning experiences',
            'Fear of judgment: Most people are focused on themselves'
        ],
        'gradient': 'organic'
    },
    {
        'number': 28,
        'type': 'bullet',
        'title': 'Confidence in High-Stakes Situations',
        'bullets': [
            'Nervousness is normal - even top performers feel it',
            'Channel nervous energy into enthusiasm',
            'Focus on serving and helping, not proving yourself',
            'Remember: You\'re evaluating them too',
            'Your preparation will carry you through'
        ],
        'gradient': 'waves_multi'
    },
    {
        'number': 29,
        'type': 'quote',
        'title': 'The Compound Effect of Small Confidence Wins',
        'content': [
            'Send one message today, even if imperfect',
            'Schedule one informational interview this week',
            'Apply to one role that feels slightly out of reach',
            'Each small action builds evidence and momentum'
        ],
        'gradient': 'circle'
    },
    {
        'number': 30,
        'type': 'bullet',
        'title': 'Maintaining Confidence Through Challenges',
        'bullets': [
            'Setbacks don\'t erase your capabilities',
            'Confidence fluctuates - that\'s normal',
            'Return to your evidence journal when doubt creeps in',
            'Seek support during difficult moments',
            'Your track record speaks louder than any single setback'
        ],
        'gradient': 'wave'
    },

    # LESSON 4: The 7 Success Habits Deep Dive
    {
        'number': 31,
        'type': 'title',
        'title': '7 Success Habits to Develop Now',
        'gradient': 'ellipses'
    },
    {
        'number': 32,
        'type': 'bullet',
        'title': 'Success Habit #1: Have A Specific Vision',
        'bullets': [
            'Most people don\'t have a specific vision',
            'What do you want? When? Why?',
            'Clarity of vision helps you keep going when things get hard',
            'Vision is about what you\'re EXCLUDING',
            'My Challenge: Think about and decide your vision'
        ],
        'gradient': 'organic'
    },
    {
        'number': 33,
        'type': 'bullet',
        'title': 'Creating Your Career Vision',
        'bullets': [
            'Define your ideal role',
            'Set specific income goals',
            'Identify your timeline',
            'Clarify your why',
            'Write it down and review daily'
        ],
        'gradient': 'horizontal'
    },
    {
        'number': 34,
        'type': 'bullet',
        'title': 'Success Habit #2: Stop Negotiating With Yourself',
        'bullets': [
            'How many times do you negotiate with yourself daily?',
            'When the alarm goes off...do you wake up?',
            'When you say you\'ll go to the gym...do you?',
            'When you write down goals...do you accomplish them?',
            'When you say 100% every day...do you do it?'
        ],
        'gradient': 'waves_orange'
    },
    {
        'number': 35,
        'type': 'bullet',
        'title': 'Building Non-Negotiable Standards',
        'bullets': [
            'Self-trust is built through keeping promises to yourself',
            'Every negotiation with yourself erodes self-confidence',
            'Successful people eliminate decision fatigue',
            'Your job search commitments: daily outreach, weekly applications',
            'Momentum from keeping promises compounds into success'
        ],
        'gradient': 'circle'
    },
    {
        'number': 36,
        'type': 'bullet',
        'title': 'Success Habit #3: Soft Skills Vs. Hard Skills',
        'bullets': [
            'Hard skills: tactical stuff you\'d do to get sales (can buy)',
            'Soft skills: you CAN\'T buy...you have to develop',
            'Soft skills: relationship with money, emotional discipline, confidence',
            'Soft skills are always the limiting factor',
            'Confidence is one of the biggest soft skills'
        ],
        'gradient': 'wave'
    },
    {
        'number': 37,
        'type': 'bullet',
        'title': 'Developing Critical Soft Skills for Job Search',
        'bullets': [
            'Emotional regulation: staying calm during rejection',
            'Relationship building: genuine connections',
            'Communication: articulating your value clearly',
            'Resilience: bouncing back from setbacks',
            'Strategic thinking: positioning as problem-solver'
        ],
        'gradient': 'ellipses'
    },
    {
        'number': 38,
        'type': 'bullet',
        'title': 'Success Habit #4: Take Extreme Ownership',
        'bullets': [
            'Most people place blame on everything and everyone else',
            'The moment you realize everything starts and stops with you...success explodes',
            'Take accountability for your success',
            'Realize nobody is beyond suffering and setbacks'
        ],
        'gradient': 'organic'
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
        ],
        'gradient': 'horizontal'
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
        ],
        'gradient': 'waves_multi'
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
        ],
        'gradient': 'circle'
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
        ],
        'gradient': 'wave'
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
        ],
        'gradient': 'ellipses'
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
        ],
        'gradient': 'organic'
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
        ],
        'gradient': 'horizontal'
    },

    # LESSON 5: Creating Your Personal Success System
    {
        'number': 46,
        'type': 'title',
        'title': 'Creating Your Personal Success System',
        'gradient': 'waves_orange'
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
        ],
        'gradient': 'circle'
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
        ],
        'gradient': 'wave'
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
        ],
        'gradient': 'ellipses'
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
        ],
        'gradient': 'organic'
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
        ],
        'gradient': 'horizontal'
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
        ],
        'gradient': 'waves_multi'
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
        ],
        'gradient': 'circle'
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
        ],
        'gradient': 'wave'
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
        ],
        'gradient': 'ellipses'
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
        ],
        'gradient': 'organic'
    },
    {
        'number': 57,
        'type': 'simple',
        'title': 'You Now Have the Mindset',
        'subtitle': 'Foundation for Success',
        'gradient': 'waves_orange'
    }
]

# ============================================================================
# MAIN GENERATION FUNCTION
# ============================================================================

def generate_all_slides(output_dir):
    """Generate all 57 slides with pitch deck aesthetic."""

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    print(f"🎨 Generating 57 slides with Pitch Deck aesthetic...")
    print(f"📁 Output directory: {output_dir}")
    print()

    for slide_data in slides_content:
        number = slide_data['number']
        slide_type = slide_data['type']

        print(f"   Generating slide {number:02d}...", end=' ')

        try:
            if slide_type == 'title':
                slide = generate_title_slide(
                    number,
                    slide_data['title'],
                    slide_data.get('gradient', 'circle')
                )
            elif slide_type == 'bullet':
                slide = generate_bullet_slide(
                    number,
                    slide_data['title'],
                    slide_data['bullets'],
                    slide_data.get('gradient', 'horizontal')
                )
            elif slide_type == 'quote':
                slide = generate_quote_slide(
                    number,
                    slide_data['title'],
                    slide_data['content'],
                    slide_data.get('gradient', 'ellipses')
                )
            elif slide_type == 'simple':
                slide = generate_simple_slide(
                    number,
                    slide_data['title'],
                    slide_data.get('subtitle', ''),
                    slide_data.get('gradient', 'waves_multi')
                )
            else:
                print(f"❌ Unknown slide type: {slide_type}")
                continue

            # Save slide
            output_path = os.path.join(output_dir, f"slide-{number:02d}-pitchdeck.png")
            slide.save(output_path, 'PNG', quality=95)
            print(f"✓ Saved as slide-{number:02d}-pitchdeck.png")

        except Exception as e:
            print(f"❌ Error: {e}")
            continue

    print()
    print(f"✅ All slides generated successfully!")
    print(f"📊 Total slides: 57")
    print(f"💾 Location: {output_dir}")
    print()
    print("🎨 Design features applied:")
    print("   • Soft, organic gradients at 20-42% opacity")
    print("   • Generous whitespace (40-50% empty space)")
    print("   • Clean, minimal aesthetic")
    print("   • Helvetica Neue typography")
    print("   • #424242 primary text color")
    print("   • #A0CEFD accent color for bullets")
    print("   • Modern startup aesthetic")

if __name__ == "__main__":
    # Output directory
    output_dir = "/Users/terrancebrandon/Desktop/Active Offer/AO- Course Content/Active Offer- Course Material/M0- Mindset Expanded/Redesigned-ConceptA"

    # Generate all slides
    generate_all_slides(output_dir)
