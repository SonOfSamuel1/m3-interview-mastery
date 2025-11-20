#!/usr/bin/env python3
"""
Generate remaining M1 enhancement slides:
- Career Development (28-32)
- Compensation Breakdowns (18A-C)
- Case Studies
"""

from PIL import Image, ImageDraw, ImageFont
import textwrap

# Canvas settings
WIDTH = 1920
HEIGHT = 1080
BACKGROUND_COLOR = (245, 245, 245)
TEXT_COLOR = (0, 0, 0)

# Typography
TITLE_FONT_SIZE = 80
SUBTITLE_FONT_SIZE = 40
BODY_FONT_SIZE = 32
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
    """Create a standard slide"""
    img = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    title_font = get_font(TITLE_FONT_SIZE)
    body_font = get_font(BODY_FONT_SIZE)
    subtitle_font = get_font(SUBTITLE_FONT_SIZE)

    # Title
    draw.text((TITLE_MARGIN_LEFT, TITLE_MARGIN_TOP), title, fill=TEXT_COLOR, font=title_font)

    y_position = TITLE_MARGIN_TOP + 150

    # Subtitle
    if subtitle:
        draw.text((BODY_MARGIN_LEFT, y_position), subtitle, fill=TEXT_COLOR, font=subtitle_font)
        y_position += 100

    # Bullets
    if bullets:
        max_text_width = WIDTH - BODY_MARGIN_LEFT - BODY_MARGIN_RIGHT - BULLET_INDENT

        for bullet_text in bullets:
            draw.text((BODY_MARGIN_LEFT, y_position), "•", fill=TEXT_COLOR, font=body_font)
            wrapped_lines = wrap_text(bullet_text, body_font, max_text_width)

            for line in wrapped_lines:
                draw.text((BODY_MARGIN_LEFT + BULLET_INDENT, y_position), line, fill=TEXT_COLOR, font=body_font)
                y_position += LINE_SPACING

            y_position += 20

    return img

# =============================================================================
# SLIDES 18A-C: COMPENSATION BREAKDOWNS
# =============================================================================

slide_18a_content = {
    'title': 'Compensation: Enterprise Leaders',
    'subtitle': 'Detailed Breakdown',
    'bullets': [
        '''Base Salary Range: $150k-$250k depending on role level (AE to Global Account Director) and company tier within Enterprise Leaders''',
        '''Variable/Commission: $150k-$350k at 100% quota attainment, structured as quarterly or annual bonuses with accelerators at 100%+''',
        '''Total OTE: $300k-$600k+ for enterprise roles, with top performers at companies like Salesforce, Google, AWS earning $800k-$1M+ total comp''',
        '''Liquid RSU Grants: $50k-$200k+ annual value that vests quarterly into tradable public stock you can sell immediately for cash''',
        '''Benefits Package: Comprehensive health insurance, 401k matching (typically 3-6%), unlimited PTO, professional development budgets, wellness programs''',
        '''Quota Attainment: 70-85% of reps consistently hit quota in healthy Enterprise Leader sales orgs, providing predictable income''',
        '''Real Total Comp: $350k-$800k all-in compensation including base, commissions, RSUs, and benefits for mid-to-senior level enterprise reps'''
    ]
}

slide_18b_content = {
    'title': 'Compensation: Growth Champions',
    'subtitle': 'Detailed Breakdown',
    'bullets': [
        '''Base Salary Range: $120k-$180k depending on company stage (Series B vs. Series D) and role complexity''',
        '''Variable/Commission: $80k-$220k at 100% quota attainment, with aggressive accelerators for over-performance common at high-growth companies''',
        '''Total OTE: $200k-$400k for mid-market and enterprise roles, competitive with Enterprise Leaders for cash compensation''',
        '''Pre-IPO Equity: 0.01%-0.1% ownership in stock options or RSUs that vest over 4 years, currently illiquid but potential $100k-$1M+ value at successful exit''',
        '''Benefits Package: Competitive health insurance, 401k (often no match), standard PTO, equity-heavy total comp philosophy''',
        '''Quota Attainment: 60-75% of reps hit quota in well-run Growth Champion companies, slightly more variable than Enterprise Leaders''',
        '''Risk-Adjusted Value: If company achieves successful IPO or acquisition in 3-5 years, total comp can match or exceed Enterprise Leaders when equity realizes'''
    ]
}

slide_18c_content = {
    'title': 'Compensation: Venture-Backed Startups',
    'subtitle': 'Detailed Breakdown',
    'bullets': [
        '''Base Salary Range: $100k-$140k at early-stage startups, with some well-funded Series B/C companies offering $120k-$160k''',
        '''Variable/Commission: $40k-$80k at 100% quota attainment, but quotas often change mid-year as company finds product-market fit''',
        '''Total OTE: $140k-$220k cash compensation, significantly lower than other profiles to offset with equity grants''',
        '''Equity Grants: 0.1%-0.5% ownership in stock options with 4-year vesting, but 70-80% probability this becomes worthless if company fails''',
        '''Benefits Package: Basic health insurance, limited or no 401k, minimal PTO, lean operating philosophy means fewer perks''',
        '''Quota Attainment: 40-60% of reps hit quota as company experiments with ICP, pricing, and sales process—highly variable performance''',
        '''Reality Check: You're betting $100k-$200k in foregone cash comp annually for 10% chance your equity is worth $500k-$10M+ in 7-10 years'''
    ]
}

# =============================================================================
# SLIDES 28-32: CAREER DEVELOPMENT PATHS
# =============================================================================

slide_28_content = {
    'title': 'Career Development Maps',
    'subtitle': 'Overview',
    'bullets': [
        '''Three distinct career pathways exist to reach different income milestones ($300k, $500k, $1M+), each requiring different company profile choices, timelines, and trade-offs''',
        '''Path to $300k: Most achievable at Enterprise Leaders within 3-5 years of focused enterprise sales experience and consistent quota attainment''',
        '''Path to $500k: Requires either senior Enterprise Leader role (Director/VP) or successful Growth Champion equity outcome through IPO or acquisition''',
        '''Path to $1M+: Achievable through Enterprise Leader leadership (VP/CRO), Growth Champion equity multiplier, or Venture-Backed Startup success (lowest probability, highest upside)''',
        '''Career stage matters: Your current position, skills, and financial situation determine which path is realistic and optimal for you right now''',
        '''The following slides break down specific timelines, milestones, probability analysis, and decision points for each income tier'''
    ]
}

slide_29_content = {
    'title': 'Path to $300k Total Comp',
    'subtitle': 'Realistic Timeline & Milestones',
    'bullets': [
        '''Timeline: 3-5 years from entry-level SaaS AE role to consistent $300k+ total compensation at Enterprise Leaders''',
        '''Year 1-2: Entry-level AE role at Enterprise Leader ($180k-$250k OTE), focus on learning enterprise sales methodology, CRM mastery, building pipeline discipline''',
        '''Year 3-4: Mid-market or Enterprise AE role ($250k-$350k OTE), demonstrate consistent quota attainment, expand deal sizes, develop champion-building skills''',
        '''Year 5+: Senior Enterprise AE or Account Director role ($300k-$450k OTE + $50k+ RSUs), handle strategic accounts, mentor junior reps, considered for management''',
        '''Probability of Success: 60-70% of reps who stay 3+ years at Enterprise Leaders and consistently hit 80%+ quota achieve $300k+ total comp''',
        '''Alternative Path: Join Growth Champion as experienced hire, achieve equity outcome through IPO that vests $100k-$300k annually on top of $200k+ cash OTE''',
        '''Best For: Professionals who prioritize predictable income growth, value enterprise skill development, and want 60-70% probability of achieving target within 5 years'''
    ]
}

slide_30_content = {
    'title': 'Path to $500k Total Comp',
    'subtitle': 'Multiple Routes & Trade-offs',
    'bullets': [
        '''Enterprise Leader Route: Progress to Director/Senior Director level managing $5M-$20M in ARR, 5-7 years experience required, $400k-$600k OTE + $100k+ RSUs''',
        '''Growth Champion Route: Senior AE/Account Director with equity grant that vests $150k-$300k+ annually after successful IPO, combined with $250k-$350k cash OTE''',
        '''Hybrid Strategy: Build skills at Enterprise Leader (3-4 years), then move to Growth Champion pre-IPO (2-3 years), time equity outcome for maximum value''',
        '''Probability Analysis: Enterprise Leader route 40-50% probability over 7-10 years | Growth Champion equity route 25-35% probability over 5-7 years (must pick winning company)''',
        '''Key Differentiator: Enterprise Leader path is more predictable but slower | Growth Champion path is higher risk but can accelerate timeline significantly''',
        '''Trade-off Decision: Choose Enterprise Leader route if you need income certainty and have time | Choose Growth Champion if you can tolerate 3-5 years of uncertainty for accelerated outcome''',
        '''Reality Check: $500k total comp puts you in top 5-10% of SaaS sales professionals—requires sustained high performance, strategic company selection, and some luck'''
    ]
}

slide_31_content = {
    'title': 'Path to $1M+ Total Comp',
    'subtitle': 'Extreme Performance or Equity Outcomes',
    'bullets': [
        '''Enterprise Leader Leadership: VP of Sales or CRO role at $500k-$800k base + $200k-$400k bonus + $200k-$400k RSUs, requires 10-15 years experience and executive skills''',
        '''Top 1% Individual Contributor: Global Account Director managing $50M+ portfolio at Salesforce/AWS/Google, $600k-$1M+ OTE + significant RSU grants, rare and competitive''',
        '''Growth Champion Equity Multiplier: Senior sales leader (Director+) with 0.05%-0.15% equity at company that IPOs at $5B+ valuation, creating $2.5M-$7.5M equity value vesting over 4 years''',
        '''Venture-Backed Startup Success: Early sales hire (employee #10-50) with 0.2%-0.5% equity at startup that achieves $5B+ exit, potential $10M-$25M outcome but <5% probability''',
        '''Founder/Consultant Route: Start your own SaaS company, consulting practice, or join as co-founder with meaningful equity (5-20%), highest upside but different risk profile entirely''',
        '''Probability Reality: <2% of SaaS sales professionals reach $1M+ sustained annual compensation | Requires exceptional performance, strategic career moves, executive skills, and significant luck/timing''',
        '''Best Path: Build elite enterprise sales skills at Enterprise Leader (5+ years), move to Director+ role at high-growth Growth Champion pre-IPO, time equity outcome successfully'''
    ]
}

slide_32_content = {
    'title': 'Career Path Decision Framework',
    'subtitle': 'Choosing Your Route',
    'bullets': [
        '''Current Position Analysis: Where are you now? (Years of experience, current comp, skill level, financial obligations) → This determines which paths are realistic''',
        '''Income Target Selection: $300k (achievable), $500k (challenging), $1M+ (exceptional) → Higher targets require more risk, longer timelines, or leadership trajectory''',
        '''Risk Tolerance Assessment: Can you afford 3-5 years of lower cash comp for equity upside? Do you have financial obligations requiring stable income? → Determines Enterprise Leader vs. Growth Champion focus''',
        '''Timeline Expectations: Need $300k in 3-5 years? Can wait 7-10 years for $500k+? → Patience and financial runway determine viable paths''',
        '''Strategic Company Moves: Plan 2-3 company transitions over 10-year career (Enterprise Leader → Growth Champion → Leadership role) rather than staying at one company entire career''',
        '''Continuous Skill Development: Top 10% of earners invest heavily in skills (MEDDIC, Command of Message, executive relationships, product knowledge, industry expertise)—never stop learning''',
        '''Action Step: Based on your self-assessment and target income goal, identify which company profile to target NOW and plan next career move in 3-4 years'''
    ]
}

# =============================================================================
# CASE STUDIES
# =============================================================================

case_study_1_slide_1 = {
    'title': 'Case Study 1: Sarah Chen',
    'subtitle': 'Career Switcher → Enterprise Leader Success',
    'bullets': [
        '''Background: Former teacher (age 32) transitioning to tech sales, no SaaS experience, needed stable income with two young children and mortgage''',
        '''Initial Situation: Received offers from both Venture-Backed Startup ($160k OTE + 0.3% equity) and Salesforce ($240k OTE + RSUs), startup offered "life-changing" equity potential''',
        '''Decision: Chose Salesforce despite lower equity because: Structured training program, predictable income, comprehensive benefits, work-life balance with family obligations''',
        '''Year 1-2 Results: Completed Salesforce training, ramped to 85% quota attainment, earned $220k total comp (base + commissions), gained enterprise sales methodology foundation''',
        '''Year 3-4 Progress: Promoted to Commercial Account Executive, $280k OTE, hit 110% quota, $320k total comp including RSUs, developed strategic account management skills''',
        '''Current Outcome (Year 5): Senior Enterprise AE, $350k OTE, $380k actual total comp, financially secure, work-life balance maintained, strong resume for future moves''',
        '''Counterfactual: The Venture-Backed Startup she declined ran out of funding after 2.5 years and shut down—her equity would have been worth $0 and she would have needed to find new job mid-pandemic'''
    ]
}

case_study_1_slide_2 = {
    'title': 'Case Study 1: Key Lessons',
    'subtitle': 'What We Learn from Sarah\'s Success',
    'bullets': [
        '''Profile Matching Worked: Sarah correctly identified as "Career Stability Seeker" needing predictable income—Enterprise Leader was optimal choice despite lower equity upside''',
        '''Short-term Sacrifice, Long-term Gain: By choosing lower equity for higher cash, she built financial security and skills that compound over decades of career''',
        '''Hidden Risk in Startups: Even "well-funded" Venture-Backed Startups fail 70-80% of time—Sarah avoided catastrophic career setback that would have derailed financial goals''',
        '''Training Value: Enterprise Leader training program accelerated her learning curve by 2-3 years compared to figuring it out at startup where "everyone is learning together"''',
        '''Life Stage Matters: At 32 with family obligations, she couldn't afford to gamble on equity—different decision would be appropriate for 25-year-old single professional''',
        '''Long-term Optionality: With 5 years of Salesforce on resume and proven enterprise sales skills, Sarah can NOW make calculated move to Growth Champion if she wants equity upside''',
        '''Profile Framework Value: Using self-assessment to match company profile to life situation prevented $200k+ in lost income and career disruption from choosing wrong path'''
    ]
}

case_study_2_slide_1 = {
    'title': 'Case Study 2: Marcus Rodriguez',
    'subtitle': 'Mid-Career Equity Optimizer → $850k Outcome',
    'bullets': [
        '''Background: 5 years at Oracle as Enterprise AE (age 31), single, $380k total comp, wanted equity upside without extreme startup risk''',
        '''Initial Situation: Choosing between staying at Oracle for VP track, joining AWS for $450k OTE, or joining Snowflake (pre-IPO Growth Champion) for $280k OTE + 0.03% equity''',
        '''Decision: Chose Snowflake in 2019 (Series D, $3.9B valuation) because: Proven product-market fit, clear IPO trajectory, reasonable cash comp reduction ($100k/year), meaningful equity grant''',
        '''Year 1-2 Experience: Lower cash comp ($280k vs. $380k Oracle), faster pace, more ambiguity, but direct impact on revenue and broader skill development than Oracle''',
        '''September 2020: Snowflake IPO at $70B market cap (18x valuation increase from his grant price), his 0.03% equity became worth $2.1M vesting over remaining 3 years''',
        '''Current Outcome (2023): Total comp from Snowflake: $280k salary/commissions + $700k equity vesting annually = $980k total comp, recently promoted to Director of Sales''',
        '''Lessons: By giving up $100k/year for 2 years ($200k total foregone income), he gained $2.1M in equity value—10.5x return on opportunity cost'''
    ]
}

case_study_2_slide_2 = {
    'title': 'Case Study 2: Key Lessons',
    'subtitle': 'What We Learn from Marcus\'s Success',
    'bullets': [
        '''Calculated Risk: Marcus didn\'t join early-stage startup (avoided 70-80% failure rate)—he chose late-stage Growth Champion with proven metrics and clear IPO path (much higher probability)''',
        '''Timing is Everything: Joined 18 months before IPO at $3.9B valuation, rode wave to $70B IPO, perfect timing created massive equity outcome''',
        '''Financial Runway Required: Could only afford $100k/year pay cut because he was single, had savings, and 5 years of high income from Oracle built cushion''',
        '''Profile Match: "Equity Optimizer" with moderate risk tolerance, 3+ years experience, financial cushion—perfect fit for Growth Champion route''',
        '''Not Pure Luck: Marcus researched Snowflake fundamentals (revenue growth, net retention, competitive moat) rather than just gambling on equity—thoughtful analysis increased probability''',
        '''Career Acceleration: Snowflake experience post-IPO carries more weight than Oracle—now has options for VP roles, consulting, or next Growth Champion opportunity''',
        '''Framework Application: Growth Champion company profile correctly balanced his desire for equity upside with need for reasonable income stability during vesting period'''
    ]
}

case_study_3_slide_1 = {
    'title': 'Case Study 3: Jessica Thompson',
    'subtitle': 'Venture-Backed Startup Reality Check',
    'bullets': [
        '''Background: 2 years SaaS experience at HubSpot (age 26), saw peers joining startups with "amazing equity", felt FOMO, wanted to "get rich" quickly''',
        '''Initial Situation: Offered roles at two Venture-Backed Startups: Company A (Series A, $15M funding, 0.4% equity, $160k OTE) and Company B (Series B, $50M funding, 0.15% equity, $180k OTE)''',
        '''Decision: Chose Company A for higher equity percentage (0.4% vs. 0.15%), reasoning that "4x the equity" meant "4x the outcome"—focused on share count not probability''',
        '''Year 1 Experience: Chaotic environment, quota changed 3x, product pivoted twice, burned through cash quickly, hired VP Sales who changed entire process''',
        '''Year 2 Crisis: Company raised bridge round at down valuation (from $75M to $50M), her equity diluted by 40%, new investors got liquidation preferences reducing her outcome even if successful exit''',
        '''Year 2.5 Outcome: Company ran out of runway, couldn\'t raise Series B, shut down operations—equity worth $0, Jessica unemployed with 2.5 year gap in resume at lower comp than HubSpot''',
        '''Financial Impact: Gave up $60k-$80k annually in foregone HubSpot comp ($150k-$200k total over 2.5 years), equity worth $0, lost career momentum and confidence'''
    ]
}

case_study_3_slide_2 = {
    'title': 'Case Study 3: Key Lessons',
    'subtitle': 'What We Learn from Jessica\'s Failure',
    'bullets': [
        '''Probability Matters More Than Percentage: 0.4% of $0 (70-80% probability) is worth less than 0.01% of $1B (40-50% probability at Growth Champion)—she optimized for wrong variable''',
        '''FOMO is Expensive: Emotional decision driven by peer comparison rather than systematic analysis of her profile, financial situation, and company fundamentals''',
        '''Stage Risk Underestimated: Series A startups have <20% probability of reaching Series B, much less IPO—she didn\'t understand how low probability her outcome was''',
        '''Career Setback Cost: 2.5 years at failed startup is gap on resume that\'s hard to explain to Enterprise Leaders, cost her $150k-$200k in foregone income plus career momentum''',
        '''Profile Mismatch: With only 2 years experience and no financial runway, she shouldn\'t have been in Venture-Backed Startup category at all—Growth Champion or Enterprise Leader would have been appropriate''',
        '''Due Diligence Failure: Didn\'t research Company A\'s burn rate, runway, competitive position, founder track record—treated equity like lottery ticket not investment''',
        '''Framework Value: If Jessica had used self-assessment honestly, she would have identified as "Early Career" with insufficient financial runway and chosen Enterprise Leader path to build skills and savings first'''
    ]
}

# =============================================================================
# GENERATION FUNCTIONS
# =============================================================================

def generate_compensation_slides():
    """Generate slides 18A-C"""
    slides = [
        ('18A', slide_18a_content),
        ('18B', slide_18b_content),
        ('18C', slide_18c_content)
    ]

    for slide_name, content in slides:
        print(f"Generating Slide {slide_name}: {content['title']}...")
        slide = create_slide(
            title=content['title'],
            subtitle=content['subtitle'],
            bullets=content['bullets']
        )
        # Note: these will be inserted after slide 18, so we'll save them with special names
        output_path = f"/Users/terrancebrandon/Desktop/Active Offer/AO- Course Content/Active Offer- Course Material/M1- Profile Matching/{slide_name}.png"
        slide.save(output_path)
        print(f"✓ Saved {output_path}")

def generate_career_development_slides():
    """Generate slides 28-32"""
    slides = [
        ('28', slide_28_content),
        ('29', slide_29_content),
        ('30', slide_30_content),
        ('31', slide_31_content),
        ('32', slide_32_content)
    ]

    for slide_num, content in slides:
        print(f"Generating Slide {slide_num}: {content['title']}...")
        slide = create_slide(
            title=content['title'],
            subtitle=content['subtitle'],
            bullets=content['bullets']
        )
        output_path = f"/Users/terrancebrandon/Desktop/Active Offer/AO- Course Content/Active Offer- Course Material/M1- Profile Matching/{slide_num}.png"
        slide.save(output_path)
        print(f"✓ Saved {output_path}")

def generate_case_study_slides():
    """Generate case study slides"""
    case_studies = [
        ('CS1-1', case_study_1_slide_1),
        ('CS1-2', case_study_1_slide_2),
        ('CS2-1', case_study_2_slide_1),
        ('CS2-2', case_study_2_slide_2),
        ('CS3-1', case_study_3_slide_1),
        ('CS3-2', case_study_3_slide_2)
    ]

    for slide_name, content in case_studies:
        print(f"Generating Case Study Slide {slide_name}...")
        slide = create_slide(
            title=content['title'],
            subtitle=content['subtitle'],
            bullets=content['bullets']
        )
        output_path = f"/Users/terrancebrandon/Desktop/Active Offer/AO- Course Content/Active Offer- Course Material/M1- Profile Matching/{slide_name}.png"
        slide.save(output_path)
        print(f"✓ Saved {output_path}")

def main():
    print("=" * 60)
    print("Generating Remaining M1 Enhancement Slides")
    print("=" * 60)
    print()

    generate_compensation_slides()
    print()
    generate_career_development_slides()
    print()
    generate_case_study_slides()

    print()
    print("✓ All remaining slides generated successfully!")

if __name__ == "__main__":
    main()
