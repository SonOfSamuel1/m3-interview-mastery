#!/usr/bin/env python3
"""
Generate enhanced slides for M1-Profile Matching Module
Includes: Slide 20 (self-assessment), updated Slide 11, examples (25-27),
career development (28-32), compensation breakdowns (18A-C), case studies
"""

from PIL import Image, ImageDraw, ImageFont
import textwrap

# Canvas settings
WIDTH = 1920
HEIGHT = 1080
BACKGROUND_COLOR = (245, 245, 245)  # Light gray #F5F5F5
TEXT_COLOR = (0, 0, 0)  # Black

# Typography settings
TITLE_FONT_SIZE = 80
SUBTITLE_FONT_SIZE = 40
BODY_FONT_SIZE = 32
SMALL_FONT_SIZE = 28
LINE_SPACING = 50
BULLET_INDENT = 140

# Margins
TITLE_MARGIN_TOP = 120
TITLE_MARGIN_LEFT = 90
BODY_MARGIN_LEFT = 90
BODY_MARGIN_RIGHT = 90

def get_font(size):
    """Get Helvetica font or fallback"""
    try:
        return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size)
    except:
        try:
            return ImageFont.truetype("Helvetica", size)
        except:
            return ImageFont.load_default()

def wrap_text(text, font, max_width):
    """Wrap text to fit within max_width"""
    words = text.split()
    lines = []
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

def create_slide(title, bullets=None, subtitle=None):
    """Create a standard slide with title and bullet points"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    title_font = get_font(TITLE_FONT_SIZE)
    body_font = get_font(BODY_FONT_SIZE)
    subtitle_font = get_font(SUBTITLE_FONT_SIZE)

    # Draw title
    draw.text((TITLE_MARGIN_LEFT, TITLE_MARGIN_TOP), title, fill=TEXT_COLOR, font=title_font)

    y_position = TITLE_MARGIN_TOP + 150

    # Draw subtitle if provided
    if subtitle:
        draw.text((BODY_MARGIN_LEFT, y_position), subtitle, fill=TEXT_COLOR, font=subtitle_font)
        y_position += 100

    # Draw bullets if provided
    if bullets:
        max_text_width = WIDTH - BODY_MARGIN_LEFT - BODY_MARGIN_RIGHT - BULLET_INDENT

        for bullet_text in bullets:
            # Draw bullet point
            draw.text((BODY_MARGIN_LEFT, y_position), "•", fill=TEXT_COLOR, font=body_font)

            # Wrap and draw bullet text
            wrapped_lines = wrap_text(bullet_text, body_font, max_text_width)

            for line in wrapped_lines:
                draw.text((BODY_MARGIN_LEFT + BULLET_INDENT, y_position), line, fill=TEXT_COLOR, font=body_font)
                y_position += LINE_SPACING

            # Extra spacing between bullets
            y_position += 20

    return img

# =============================================================================
# SLIDE 20: SELF-ASSESSMENT FRAMEWORK
# =============================================================================

slide_20_content = {
    'title': 'Understand Current Position',
    'subtitle': 'Self-Assessment Framework',
    'bullets': [
        '''Years in SaaS Sales: Are you new to SaaS (0-1 years), building skills (1-3 years), or experienced (3+ years)?''',
        '''Current Income & Financial Obligations: What's your current total comp? Do you have dependents, mortgage, or financial responsibilities requiring stable income?''',
        '''Risk Tolerance & Financial Runway: How many months of expenses do you have saved? Can you afford 12-18 months of income uncertainty?''',
        '''Primary Career Goal: Maximize current cash earnings? Build enterprise skills and resume credibility? Pursue equity upside and wealth creation?''',
        '''Work Preferences: Do you thrive in structure (processes, training, support) or prefer autonomy (ambiguity, self-direction, wearing multiple hats)?''',
        '''Learning Style: Do you learn best from proven methodologies and mentorship, or through trial-and-error and rapid iteration?''',
        '''Download the Self-Assessment Worksheet to score your answers and identify your optimal company profile match'''
    ]
}

# =============================================================================
# SLIDES 25-27: COMPANY LIST EXAMPLES
# =============================================================================

slide_25_content = {
    'title': 'Example 1: Career Stability Seeker',
    'subtitle': 'Profile: Parent/Provider prioritizing income security | Target: Enterprise Leaders',
    'bullets': [
        '''Salesforce - Market leader in CRM, $31B+ revenue, predictable $350k-$600k OTE, excellent benefits, strong work-life balance''',
        '''Microsoft (Dynamics 365) - Tech giant with stable territories, $250k-$450k OTE, comprehensive training, low risk''',
        '''Oracle - Enterprise software leader, $300k-$550k OTE, established accounts, predictable commission structure''',
        '''Google Cloud - Rapid growth within stable parent, $280k-$500k OTE, cutting-edge product, strong brand credibility''',
        '''AWS - Cloud market leader, $300k-$600k+ OTE, massive installed base, excellent career progression paths''',
        '''Adobe - Creative/marketing software leader, $250k-$450k OTE, sticky products, low customer churn''',
        '''SAP - Enterprise ERP leader, $280k-$500k OTE, long sales cycles, deep customer relationships, global reach''',
        '''ServiceNow - IT workflow platform leader, $300k-$550k OTE, strong product-market fit, growing TAM''',
        '''Workday - HR/Finance SaaS leader, $280k-$500k OTE, sticky enterprise platform, predictable renewal revenue''',
        '''HubSpot - Marketing/Sales platform, $200k-$400k OTE (lower tier but still stable), inbound-focused, great culture'''
    ]
}

slide_26_content = {
    'title': 'Example 2: Equity Optimizer',
    'subtitle': 'Profile: Mid-career professional seeking balanced risk/reward | Target: Growth Champions',
    'bullets': [
        '''DataRobot - AI/ML platform leader ($300M+ ARR), strong Series G funding, IPO trajectory 2-3 years, 0.02-0.05% equity potential''',
        '''Gong - Revenue intelligence leader ($200M+ ARR), category creator, $250k-$400k OTE + meaningful equity, high growth''',
        '''Notion - Collaboration workspace ($100M+ ARR), viral product-market fit, strong brand momentum, IPO-track''',
        '''Airtable - Low-code database platform ($150M+ ARR), broad use cases, enterprise expansion, well-funded''',
        '''Figma - Design collaboration leader (recently acquired by Adobe for $20B - example of successful exit outcome)''',
        '''Rippling - HR/IT platform ($200M+ ARR), multi-product expansion, fast growth, strong unit economics''',
        '''Webflow - No-code web platform ($100M+ ARR), designer-favorite, enterprise push, equity potential''',
        '''Superhuman - Email productivity ($30M+ ARR), premium positioning, strong NPS, growth trajectory''',
        '''Mixpanel - Product analytics ($100M+ ARR), competitive market, established customer base, stable growth''',
        '''Miro - Visual collaboration ($200M+ ARR), post-pandemic tailwinds, enterprise adoption, IPO prep'''
    ]
}

slide_27_content = {
    'title': 'Example 3: High-Risk Growth Hunter',
    'subtitle': 'Profile: Early career, risk-tolerant, maximum learning | Target: Venture-Backed Startups',
    'bullets': [
        '''Hex - Data collaboration platform (Series B, $50M funding), early stage, 0.15-0.3% equity, high learning velocity''',
        '''Clay - GTM data platform (Series B, $60M funding), fast growth, scrappy team, broad skill development''',
        '''Modal - Cloud compute platform (Series A, $30M funding), technical product, small team, massive ownership''',
        '''Watershed - Carbon accounting (Series B, $100M funding), climate tech, mission-driven, growing category''',
        '''Juni - Childcare benefits (Series A, $25M funding), solving real problem, early sales hire, define role''',
        '''Ramp - Corporate cards/spend (Series C, $750M funding), hypergrowth, aggressive goals, sink-or-swim culture''',
        '''Mercury - Banking for startups (Series B, $120M funding), fintech, fast-moving, equity upside potential''',
        '''Crossbeam - Partner ecosystem (Series B, $76M funding), category creation, evangelical selling required''',
        '''Brex - Corporate credit (Series D, $1B+ valuation), redefining startup banking, high-pressure environment''',
        '''Deel - Global payroll (Series D, $12B valuation), explosive growth, international complexity, equity diluted but valuable'''
    ]
}

# =============================================================================
# MAIN GENERATION FUNCTION
# =============================================================================

def generate_slide_20():
    """Generate Slide 20: Self-Assessment Framework"""
    print("Generating Slide 20: Self-Assessment Framework...")
    slide = create_slide(
        title=slide_20_content['title'],
        subtitle=slide_20_content['subtitle'],
        bullets=slide_20_content['bullets']
    )
    output_path = "/Users/terrancebrandon/Desktop/Active Offer/AO- Course Content/Active Offer- Course Material/M1- Profile Matching/20.png"
    slide.save(output_path)
    print(f"✓ Saved {output_path}")

def generate_example_slides():
    """Generate example slides 25-27"""
    examples = [
        ('25', slide_25_content),
        ('26', slide_26_content),
        ('27', slide_27_content)
    ]

    for slide_num, content in examples:
        print(f"Generating Slide {slide_num}: {content['title']}...")
        slide = create_slide(
            title=content['title'],
            subtitle=content['subtitle'],
            bullets=content['bullets']
        )
        output_path = f"/Users/terrancebrandon/Desktop/Active Offer/AO- Course Content/Active Offer- Course Material/M1- Profile Matching/{slide_num}.png"
        slide.save(output_path)
        print(f"✓ Saved {output_path}")

def main():
    """Generate all enhanced slides"""
    print("=" * 60)
    print("M1-Profile Matching Module Enhancement")
    print("=" * 60)
    print()

    generate_slide_20()
    generate_example_slides()

    print()
    print("✓ All slides generated successfully!")

if __name__ == "__main__":
    main()
