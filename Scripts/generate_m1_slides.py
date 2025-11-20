#!/usr/bin/env python3
"""
Generate replacement slides for M1-Profile Matching Module
Slides: 9, 12, 13, 14 with updated content and naming convention
"""

from PIL import Image, ImageDraw, ImageFont
import textwrap

# Canvas settings (matching existing M1 slides)
WIDTH = 1920
HEIGHT = 1080
BACKGROUND_COLOR = (245, 245, 245)  # Light gray #F5F5F5
TEXT_COLOR = (0, 0, 0)  # Black

# Typography settings
TITLE_FONT_SIZE = 80
BODY_FONT_SIZE = 32
BULLET_FONT_SIZE = 32
LINE_SPACING = 50
BULLET_INDENT = 140

# Margins
TITLE_MARGIN_TOP = 120
TITLE_MARGIN_LEFT = 90
BODY_MARGIN_LEFT = 90
BODY_MARGIN_RIGHT = 90
BODY_MARGIN_TOP = 100

def get_font(size):
    """Get Helvetica font or fallback to default"""
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

def create_slide(title, bullets, subtitle=None):
    """Create a slide with title and bullet points"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    title_font = get_font(TITLE_FONT_SIZE)
    body_font = get_font(BODY_FONT_SIZE)

    # Draw title
    draw.text((TITLE_MARGIN_LEFT, TITLE_MARGIN_TOP), title, fill=TEXT_COLOR, font=title_font)

    # Calculate starting Y position for content
    y_position = TITLE_MARGIN_TOP + 150

    # Draw subtitle if provided
    if subtitle:
        draw.text((BODY_MARGIN_LEFT, y_position), subtitle, fill=TEXT_COLOR, font=body_font)
        y_position += 100

    # Draw bullets
    max_text_width = WIDTH - BODY_MARGIN_LEFT - BODY_MARGIN_RIGHT - BULLET_INDENT

    for bullet_text in bullets:
        # Draw bullet point
        draw.text((BODY_MARGIN_LEFT, y_position), "•", fill=TEXT_COLOR, font=body_font)

        # Wrap and draw bullet text
        wrapped_lines = wrap_text(bullet_text, body_font, max_text_width)

        for line in wrapped_lines:
            draw.text((BODY_MARGIN_LEFT + BULLET_INDENT, y_position), line, fill=TEXT_COLOR, font=body_font)
            y_position += LINE_SPACING

        # Add extra spacing between bullets
        y_position += 20

    return img

# Slide content
slides_content = {
    '9': {
        'title': 'Compensation Structure',
        'subtitle': 'Stocks',
        'bullets': [
            '.',
            '''Equity compensation (stock options or RSUs) represents partial ownership in the company, but only creates value if the company grows significantly and achieves a liquidity event (IPO or acquisition) or, for public companies, through stock price appreciation''',
            '''Enterprise Leaders (Salesforce, Google, Microsoft) offer RSUs that vest into liquid, tradable stock with immediate market value, providing predictable additional compensation ($50k-$200k+/year) on top of cash earnings that you can sell quarterly''',
            '''Growth Champions offer stock options or RSUs that may become valuable if the company goes public or gets acquired, typically within 3-5 year timeframe given their growth trajectory—realistic $100k-$1M potential but not guaranteed''',
            '''Venture-Backed Startups offer highest equity percentages (0.1%-0.5%) to offset risk, but these options are illiquid and speculative—70-80% of well-funded startups still fail, meaning most equity grants expire worthless despite impressive share counts''',
            '''Never rely on unvested or illiquid equity for living expenses or financial planning; only liquid RSUs from public companies should be considered as part of your reliable total compensation package'''
        ]
    },
    '12': {
        'title': 'Enterprise Leaders',
        'subtitle': 'Company Characteristics:',
        'bullets': [
            '''Established market dominators ($1B+ revenue) with household brand names like Salesforce, Google, Microsoft, and AWS—maximum job security, comprehensive benefits, and predictable career paths make these optimal for building enterprise skills and resume credibility''',
            '''Lowest risk profile with stable income, mature sales processes, and 70-85% of reps consistently hitting quota; best choice for career switchers, parents/providers, or anyone prioritizing income stability over equity speculation''',
            '''Highest cash compensation ($300k-$600k+ OTE) with liquid RSU grants vesting into tradable public stock worth $50k-$200k+ annually—immediate wealth accumulation without gambling on company success''',
            '''Strategic fit: Choose if you need predictable earnings, want enterprise methodology training, seek work-life balance, or plan to build savings before taking calculated risks at high-growth companies''',
            '''Trade-offs include slower promotions due to organizational layers, bureaucratic processes, and lower learning velocity, but provides foundation for future moves to leadership roles at smaller, faster-growing companies'''
        ]
    },
    '13': {
        'title': 'Growth Champions',
        'subtitle': 'Company Characteristics:',
        'bullets': [
            '''High-growth product leaders ($50M-$500M revenue) with strong market positioning, proven business models, and clear IPO trajectory within 3-5 years—balanced risk/reward profile optimal for mid-career professionals seeking acceleration''',
            '''Moderate risk with validated revenue streams and institutional funding, but still dependent on execution and market conditions; expect evolving processes, strategic shifts, and potential restructuring during downturns''',
            '''Competitive compensation ($200k-$400k OTE) with meaningful pre-IPO equity (0.01%-0.1%) that has realistic potential to yield $100k-$1M+ at successful exit—neither gambling nor guaranteed, but reasonable odds if you evaluate company fundamentals''',
            '''Strategic fit: Choose if you have 3+ years SaaS experience, can tolerate uncertainty for career growth, have 6-12 months financial cushion, and want to optimize for both current earnings and equity upside''',
            '''Expect fast-paced environment (50-60 hour weeks), frequent priority changes, and need for self-direction, but offers fastest path to leadership roles, skill diversification, and significant wealth creation in successful exit scenarios'''
        ]
    },
    '14': {
        'title': 'Venture-Backed Startups',
        'subtitle': 'Company Characteristics:',
        'bullets': [
            '''Well-funded early-stage startups (Series A-C, <$50M revenue) experiencing rapid growth but still proving scalability and business model viability—highest equity percentages but also highest risk of complete failure''',
            '''High risk profile with 70-80% failure rate despite venture funding; companies may run out of capital, pivot away from your market, or shut down unexpectedly even after raising significant funds—minimal job security regardless of your performance''',
            '''Compensation heavily weighted toward equity (0.1%-0.5% ownership) to offset lower cash ($140k-$220k OTE), requiring successful exit in 5-10 years to realize any value—90% probability equity becomes worthless, 10% chance of $500k-$10M+ payout''',
            '''Strategic fit: Only choose if you're risk-tolerant with 12-18 months financial runway, early in career without obligations, seeking maximum learning velocity, or making calculated bet as part of diversified strategy (not all-in on one startup)''',
            '''Reality check: Expect 60-70 hour weeks, ambiguous roles, constant change, limited resources, high stress, and strong possibility of job loss—most employees leave before equity vests, and even "hot" startups frequently fail to achieve exits'''
        ]
    }
}

def main():
    """Generate all slides"""
    output_dir = "/Users/terrancebrandon/Desktop/Active Offer/AO- Course Content/Active Offer- Course Material/M1- Profile Matching"

    print("Generating M1 Profile Matching slides...")

    for slide_num, content in slides_content.items():
        print(f"Creating slide {slide_num}...")

        # Skip the first bullet for slide 9 (it's just a placeholder dot)
        bullets = content['bullets'][1:] if slide_num == '9' else content['bullets']

        slide = create_slide(
            title=content['title'],
            bullets=bullets,
            subtitle=content.get('subtitle')
        )

        output_path = f"{output_dir}/{slide_num}.png"
        slide.save(output_path)
        print(f"✓ Saved {output_path}")

    print("\n✓ All slides generated successfully!")

if __name__ == "__main__":
    main()
